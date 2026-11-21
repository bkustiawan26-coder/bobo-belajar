import re

from app.models import Question


def normalize(value) -> str:
    s = str(value or "").strip().lower().replace(",", ".")
    return re.sub(r"\s+", "", s)


def grade(q: Question, response: dict | None) -> bool | None:
    if q.type == "essay":
        return None
    if not response:
        return False
    a = q.answer or {}
    if q.type in ("mc", "tf"):
        return response.get("index") is not None and response.get("index") == a.get("index")
    if q.type == "multi":
        got = response.get("indices") or []
        return sorted(set(int(x) for x in got)) == sorted(set(a.get("indices") or []))
    if q.type in ("fill", "short"):
        return normalize(response.get("text")) in {normalize(x) for x in a.get("accepted") or []}
    if q.type == "matching":
        got = {str(k): str(v) for k, v in (response.get("pairs") or {}).items()}
        want = {str(k): str(v) for k, v in (a.get("pairs") or {}).items()}
        return bool(want) and got == want
    return False


def answer_text(q: Question) -> str:
    a = q.answer or {}
    labels = {o.position: o.label for o in q.options}
    if q.type in ("mc", "tf"):
        return labels.get(a.get("index"), "")
    if q.type == "multi":
        return ", ".join(labels.get(i, "") for i in a.get("indices") or [])
    if q.type in ("fill", "short"):
        acc = a.get("accepted") or []
        return acc[0] if acc else ""
    if q.type == "matching":
        return "; ".join(f"{labels.get(int(k), k)} → {labels.get(int(v), v)}" for k, v in (a.get("pairs") or {}).items())
    return q.rubric or ""


def response_text(q: Question, response: dict | None) -> str:
    if not response:
        return "Tidak dijawab"
    labels = {o.position: o.label for o in q.options}
    if q.type in ("mc", "tf"):
        return labels.get(response.get("index"), "Tidak dijawab")
    if q.type == "multi":
        return ", ".join(labels.get(int(i), "") for i in response.get("indices") or []) or "Tidak dijawab"
    if q.type in ("fill", "short", "essay"):
        return str(response.get("text") or "Tidak dijawab")
    if q.type == "matching":
        return "; ".join(f"{labels.get(int(k), k)} → {labels.get(int(v), v)}" for k, v in (response.get("pairs") or {}).items())
    return ""


def validate_answer_shape(qtype: str, answer: dict | None, option_count: int) -> str | None:
    if qtype == "essay":
        return None
    if not isinstance(answer, dict):
        return "Kunci jawaban wajib diisi"
    if qtype in ("mc", "tf"):
        i = answer.get("index")
        if not isinstance(i, int) or not 0 <= i < option_count:
            return "Kunci jawaban harus menunjuk salah satu pilihan"
    elif qtype == "multi":
        idx = answer.get("indices")
        if not isinstance(idx, list) or not idx or any(not isinstance(i, int) or not 0 <= i < option_count for i in idx):
            return "Kunci jawaban pilihan ganda kompleks tidak valid"
    elif qtype in ("fill", "short"):
        acc = answer.get("accepted")
        if not isinstance(acc, list) or not acc or not all(str(x).strip() for x in acc):
            return "Isi minimal satu jawaban yang diterima"
    elif qtype == "matching":
        if not isinstance(answer.get("pairs"), dict) or not answer["pairs"]:
            return "Pasangan jawaban wajib diisi"
    return None
