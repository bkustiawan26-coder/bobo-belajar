import re
from dataclasses import dataclass

import httpx

from app.core.config import get_settings


@dataclass
class GenRequest:
    purpose: str
    system: str
    user: str
    passages: list
    grade: int
    max_tokens: int
    extras: dict


@dataclass
class GenResult:
    text: str
    input_tokens: int
    output_tokens: int
    provider: str
    model: str


def approx_tokens(s: str) -> int:
    return max(1, len(s) // 4)


HINT_WORDS = re.compile(r"(petunjuk|bantu|langkah|gimana|bagaimana cara|caranya|hint|cek jawaban|benar nggak|benar tidak)")


def _sentences(text: str) -> list[str]:
    text = re.sub(r"^[A-Za-z ]+: ", "", text.strip())
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


class GroundedProvider:
    name = "grounded"

    def __init__(self, model: str = "grounded-v1") -> None:
        self.model = model

    def generate(self, req: GenRequest) -> GenResult:
        if req.purpose == "parent":
            out = req.extras.get("grounded_answer") or ""
        else:
            out = self._tutor(req)
        return GenResult(out, approx_tokens(req.system + req.user), approx_tokens(out), self.name, self.model)

    def _tutor(self, req: GenRequest) -> str:
        style = req.extras.get("style")
        if style and req.passages:
            return self._styled(req, style)
        if not req.passages:
            scope = req.extras.get("scope") or "materi yang tersedia"
            return f"Aku hanya menjawab dari materi BOBO yang sudah ditinjau, yaitu {scope}. Coba tanyakan dengan kata kunci dari materi itu, atau minta bantuan orang tua dan gurumu."
        top = req.passages[0]
        sentences = _sentences(top.content)
        young = req.grade <= 2
        n = 2 if young else 4
        if HINT_WORDS.search(req.user.lower()):
            key = next((s for s in sentences if any(k in s.lower() for k in ("dulu", "kalikan", "jumlahkan", "kurangi", "kuadrat", "pisahkan", "tulis"))), sentences[0])
            return f"Petunjuk dulu, ya: {key}\n\nCoba kerjakan langkah itu sendiri. Kalau sudah, ketik jawabanmu dan aku bantu cek caranya."
        body = " ".join(sentences[:n])
        topic = top.topic or top.title
        tail = f"\n\nMau coba latihan soal tentang {topic}? Buka menu Latihan." if topic else ""
        return body + tail


    def _styled(self, req: GenRequest, style: str) -> str:
        top = req.passages[0]
        sentences = _sentences(top.content)
        topic = (top.topic or top.title or "").lower()
        if style == "steps":
            steps = sentences[:4]
            return "Langkah demi langkah:\n" + "\n".join(f"{i + 1}. {x}" for i, x in enumerate(steps)) + "\n\nCoba ikuti langkahnya satu per satu, lalu kerjakan satu soal di Latihan."
        if style == "story":
            if "pecahan" in topic:
                frame = "kamu dan temanmu berbagi satu martabak yang dipotong sama besar"
            elif "pythagoras" in topic or "segitiga" in topic:
                frame = "sebuah tangga bersandar ke dinding, membentuk segitiga siku-siku dengan lantai"
            elif "jumlah" in topic or "kurang" in topic or "cerita" in topic:
                frame = "kamu mengumpulkan kelereng dari dua kantong lalu menghitung semuanya"
            else:
                frame = "kamu sedang menjelaskan hal ini kepada adikmu"
            return f"Bayangkan {frame}. " + " ".join(sentences[:2]) + "\n\nSekarang coba ceritakan ulang dengan kata-katamu sendiri."
        return "Lihat gambarnya, lalu coba sendiri di Alat peraga. " + " ".join(sentences[:2])


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str) -> None:
        self.model = model

    def generate(self, req: GenRequest) -> GenResult:
        s = get_settings()
        if not s.anthropic_api_key:
            raise RuntimeError("anthropic api key missing")
        ctx = "\n\n".join(f"[{i + 1}] {p.title}\n{p.content}" for i, p in enumerate(req.passages)) or "(tidak ada materi yang cocok)"
        r = httpx.post(
            f"{s.anthropic_base_url}/v1/messages",
            headers={"x-api-key": s.anthropic_api_key, "anthropic-version": "2023-06-01", "content-type": "application/json"},
            json={"model": self.model, "max_tokens": req.max_tokens, "system": req.system, "messages": [{"role": "user", "content": f"MATERI RUJUKAN:\n{ctx}\n\nPERTANYAAN:\n{req.user}"}]},
            timeout=s.ai_timeout_seconds,
        )
        r.raise_for_status()
        data = r.json()
        text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
        u = data.get("usage", {})
        return GenResult(text, int(u.get("input_tokens", 0)), int(u.get("output_tokens", 0)), self.name, self.model)


class OpenAICompatProvider:
    name = "openai_compat"

    def __init__(self, model: str) -> None:
        self.model = model

    def generate(self, req: GenRequest) -> GenResult:
        s = get_settings()
        if not s.openai_compat_base_url:
            raise RuntimeError("openai compatible base url missing")
        ctx = "\n\n".join(f"[{i + 1}] {p.title}\n{p.content}" for i, p in enumerate(req.passages)) or "(tidak ada materi yang cocok)"
        headers = {"content-type": "application/json"}
        if s.openai_compat_api_key:
            headers["authorization"] = f"Bearer {s.openai_compat_api_key}"
        r = httpx.post(
            f"{s.openai_compat_base_url.rstrip('/')}/chat/completions",
            headers=headers,
            json={"model": self.model, "max_tokens": req.max_tokens, "messages": [{"role": "system", "content": req.system}, {"role": "user", "content": f"MATERI RUJUKAN:\n{ctx}\n\nPERTANYAAN:\n{req.user}"}]},
            timeout=s.ai_timeout_seconds,
        )
        r.raise_for_status()
        data = r.json()
        text = data["choices"][0]["message"]["content"] or ""
        u = data.get("usage", {})
        return GenResult(text, int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0)), self.name, self.model)


def build_provider(kind: str, model: str):
    if kind == "anthropic":
        return AnthropicProvider(model)
    if kind == "openai_compat":
        return OpenAICompatProvider(model)
    return GroundedProvider(model if kind == "grounded" else "grounded-v1")
