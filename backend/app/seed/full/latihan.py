import hashlib
import random

from app.seed.full.dsl import Q, fill, mc, tf
from app.seed.full.sas import _variants

TARGET = 20


def parse_bank(text: str) -> dict[tuple[str, str], list[Q]]:
    bank: dict[tuple[str, str], list[Q]] = {}
    key = None
    for no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            code, _, title = line[3:].partition("|")
            key = (code.strip(), title.strip())
            bank.setdefault(key, [])
            continue
        if key is None:
            raise ValueError(f"baris {no}: soal sebelum judul topik")
        parts = [p.strip() for p in line.split("|")]
        head = parts[0]
        if head in ("B", "S"):
            if len(parts) != 3:
                raise ValueError(f"baris {no}: benar/salah harus 3 kolom: {line}")
            q = tf(parts[1], head == "B", parts[2])
        elif head == "=":
            if len(parts) != 4:
                raise ValueError(f"baris {no}: isian harus 4 kolom: {line}")
            q = fill(parts[1], _variants(parts[2].split(";")), parts[3])
        else:
            if len(parts) < 5 or len(parts) > 6:
                raise ValueError(f"baris {no}: pilihan ganda harus 5 atau 6 kolom: {line}")
            q = mc(parts[0], parts[1:-1], 0, parts[-1])
        bank[key].append(q)
    return bank


def _label(it: dict) -> str:
    return (it.get("label") or "").strip()


def _seed(text: str) -> random.Random:
    return random.Random(int(hashlib.sha256(text.encode()).hexdigest(), 16))


def _choices(right: str, pool: list[str], rnd: random.Random, k: int = 3) -> list[str] | None:
    others = [p for p in dict.fromkeys(pool) if p and p != right]
    if len(others) < 2:
        return None
    rnd.shuffle(others)
    return [right] + others[:k]


def from_figure(fig: dict, topic: str) -> list[Q]:
    k = fig.get("type")
    rnd = _seed(topic)
    out: list[Q] = []

    def add_mc(body, right, pool, expl):
        opts = _choices(right, pool, rnd)
        if opts:
            out.append(mc(body, opts, 0, expl))

    if k in ("flow", "steps", "cycle", "layers", "pyramid"):
        labels = [_label(x) for x in fig["items"] if _label(x)]
        if len(labels) >= 3 and len(set(labels)) == len(labels):
            chain = " → ".join(labels)
            for a, b in zip(labels, labels[1:]):
                add_mc(f"Pada {topic.lower()}, setelah \"{a}\" adalah …", b, [x for x in labels if x != a], f"Urutannya: {chain}.")
            if k == "steps":
                add_mc(f"Langkah pertama pada {topic.lower()} adalah …", labels[0], labels, f"Urutannya: {chain}.")
                add_mc(f"Langkah terakhir pada {topic.lower()} adalah …", labels[-1], labels, f"Urutannya: {chain}.")
            elif k in ("layers", "pyramid"):
                add_mc(f"Bagian paling atas pada {topic.lower()} adalah …", labels[0], labels, f"Dari atas ke bawah: {chain}.")
            elif k == "flow":
                add_mc(f"Bagian awal pada {topic.lower()} adalah …", labels[0], labels, f"Urutannya: {chain}.")
    elif k == "time":
        items = [x for x in fig["items"] if _label(x)]
        tags = [x["tag"] for x in items]
        labels = [_label(x) for x in items]
        if len(items) >= 3 and len(set(tags)) == len(tags) and len(set(labels)) == len(labels):
            for x in items:
                add_mc(f"\"{_label(x)}\" terjadi pada …", x["tag"], tags, f"{_label(x)}: {x['tag']}.")
            add_mc(f"Peristiwa yang paling awal pada {topic.lower()} adalah …", labels[0], labels, f"Urutan waktunya: {' → '.join(labels)}.")
    elif k == "table":
        head, rows = fig["head"], fig["rows"]
        left, right = [r[0] for r in rows], [r[1] for r in rows]
        if len(rows) >= 3 and len(set(left)) == len(left) and len(set(right)) == len(right):
            for a, b in zip(left, right):
                add_mc(f"{head[1]} untuk \"{a}\" adalah …", b, right, f"{a}: {b}.")
            for a, b in zip(left, right):
                add_mc(f"{head[0]} yang sesuai dengan \"{b}\" adalah …", a, left, f"{a}: {b}.")
    elif k in ("compare", "venn"):
        groups = fig["groups"]
        titles = [_label(g["title"]) for g in groups]
        items = [(_label(x), gi) for gi, g in enumerate(groups) for x in g["items"] if _label(x)]
        if len({t for t in titles}) == len(titles):
            for lab, gi in items:
                if len(titles) >= 3:
                    add_mc(f"\"{lab}\" termasuk kelompok …", titles[gi], titles, f"\"{lab}\" termasuk {titles[gi]}.")
                else:
                    other = titles[1 - gi]
                    truth = rnd.random() < 0.5
                    out.append(tf(f"\"{lab}\" termasuk {titles[gi] if truth else other}.", truth, f"\"{lab}\" termasuk {titles[gi]}."))
    elif k == "icons":
        items = [x for x in fig["items"] if _label(x)]
        labels = [_label(x) for x in items]
        icons = [x["icon"] for x in items]
        if len(items) >= 3 and len(set(labels)) == len(labels) and len(set(icons)) == len(icons):
            for x in items:
                add_mc(f"Gambar {x['icon']} artinya …", _label(x), labels, f"{x['icon']} = {_label(x)}.")
            for x in items:
                add_mc(f"Gambar untuk \"{_label(x)}\" adalah …", x["icon"], icons, f"{_label(x)} = {x['icon']}.")
    elif k == "chat":
        lines = [x["say"] for x in fig["items"]]
        if len(lines) >= 3 and len(set(lines)) == len(lines):
            for a, b in zip(lines, lines[1:]):
                add_mc(f"Setelah \"{a}\", ucapan berikutnya adalah …", b, [x for x in lines if x != a], "Urutan percakapan: " + " / ".join(lines) + ".")
    elif k == "bars":
        items = fig["items"]
        vals = [x["value"] for x in items]
        labels = [_label(x) for x in items]
        if len(items) >= 3 and len(set(labels)) == len(labels):
            if vals.count(max(vals)) == 1:
                add_mc(f"Pada data {topic.lower()}, nilai terbesar dimiliki …", labels[vals.index(max(vals))], labels, f"Nilai terbesar adalah {max(vals):g}.")
            if vals.count(min(vals)) == 1:
                add_mc(f"Pada data {topic.lower()}, nilai terkecil dimiliki …", labels[vals.index(min(vals))], labels, f"Nilai terkecil adalah {min(vals):g}.")
    seen, uniq = set(), []
    for q in out:
        if q.body not in seen:
            seen.add(q.body)
            uniq.append(q)
    return uniq


def complete(existing: list[Q], manual: list[Q], auto: list[Q], generated: list[Q], cap_auto: int = 8) -> list[Q]:
    out, bodies = [], set()
    for q in existing + manual + auto[:cap_auto] + generated + auto[cap_auto:]:
        if q.body in bodies:
            continue
        bodies.add(q.body)
        out.append(q)
        if len(out) == TARGET:
            break
    return out
