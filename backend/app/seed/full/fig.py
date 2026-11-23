import re
from fractions import Fraction

SEQ = {"flow", "cycle", "steps", "layers", "pyramid"}
SHAPES = {"square", "rect", "tri", "right", "circle", "trap", "para", "rhombus", "cube", "box", "cylinder", "cone", "sphere", "prism", "pyramid3", "angle"}
TYPES = SEQ | {"time", "mind", "compare", "venn", "bars", "line", "frac", "pie", "place", "array", "count", "shape", "table", "coord", "clock", "code", "icons", "circuit", "compass", "balance", "chat"}


class FigError(ValueError):
    pass


def _is_icon(tok: str) -> bool:
    return bool(tok) and not any(ch.isalnum() for ch in tok) and any(ord(ch) > 0x2000 for ch in tok)


def item(s: str) -> dict:
    s = s.strip()
    if not s:
        raise FigError("item kosong")
    head, _, rest = s.partition(" ")
    if _is_icon(head) and rest.strip():
        return {"icon": head, "label": rest.strip()}
    if _is_icon(head):
        return {"icon": head, "label": ""}
    return {"label": s}


def _split(s: str, sep: str) -> list[str]:
    return [p.strip() for p in s.split(sep) if p.strip()]


def _num(s: str) -> float:
    s = s.strip().replace(",", ".")
    if "/" in s:
        return float(Fraction(s))
    return float(s)


def _poly(expr: str) -> list[float]:
    e = expr.replace(" ", "").replace("−", "-").replace("^2", "²").replace(",", ".")
    if not e:
        raise FigError("persamaan kosong")
    a = b = c = 0.0
    for sign, coef, var in re.findall(r"([+-]?)(\d*\.?\d*(?:/\d+)?)(x²|x)?", e):
        if not coef and not var:
            continue
        k = float(Fraction(coef)) if coef else 1.0
        if sign == "-":
            k = -k
        if var == "x²":
            a += k
        elif var == "x":
            b += k
        else:
            c += k
    return [a, b, c]


_PT = re.compile(r"^([A-Z][a-z']?)\s*\(\s*(-?[\d.,]+)\s*[,;]\s*(-?[\d.,]+)\s*\)$")


def _point(s: str) -> dict:
    m = _PT.match(s.strip().replace("−", "-").replace(", ", ","))
    if not m:
        raise FigError(f"titik tidak dikenal: {s}")
    return {"name": m.group(1), "x": _num(m.group(2)), "y": _num(m.group(3))}


def parse(spec: str) -> dict:
    spec = spec.strip()
    caption = None
    if " ~ " in spec:
        spec, caption = spec.split(" ~ ", 1)
        caption = caption.strip()
    kind, _, body = spec.partition(" ")
    body = body.strip()
    if kind not in TYPES:
        raise FigError(f"jenis gambar tidak dikenal: {kind}")
    out: dict = {"type": kind}
    if kind in SEQ:
        out["items"] = [item(x) for x in _split(body, " > ")]
        if len(out["items"]) < 2:
            raise FigError("minimal 2 langkah")
    elif kind == "time":
        out["items"] = []
        for part in _split(body, " ; "):
            tag, _, rest = part.partition(" = ")
            if not rest:
                raise FigError(f"garis waktu butuh 'tahun = peristiwa': {part}")
            out["items"].append({**item(rest), "tag": tag.strip()})
    elif kind == "mind":
        center, _, rest = body.partition(" = ")
        out["center"] = item(center)
        out["items"] = [item(x) for x in _split(rest, " ; ")]
        if len(out["items"]) < 2:
            raise FigError("peta pikiran minimal 2 cabang")
    elif kind in ("compare", "venn"):
        out["groups"] = []
        for g in _split(body, " || "):
            title, _, rest = g.partition(" = ")
            out["groups"].append({"title": item(title), "items": [item(x) for x in _split(rest, " ; ")]})
        if len(out["groups"]) < 2 or any(not g["items"] for g in out["groups"]):
            raise FigError("perbandingan minimal 2 kelompok berisi")
        if kind == "venn" and len(out["groups"]) != 3:
            raise FigError("venn butuh 3 kelompok: A || B || keduanya")
    elif kind == "bars":
        out["items"] = []
        for part in _split(body, " ; "):
            label, _, val = part.rpartition(" ")
            out["items"].append({**item(label), "value": _num(val)})
        if len(out["items"]) < 2:
            raise FigError("diagram batang minimal 2 batang")
    elif kind == "line":
        parts = _split(body, " ; ")
        rng = parts[0].split(" step ")
        lo, _, hi = rng[0].partition("..")
        out.update({"from": _num(lo), "to": _num(hi), "step": _num(rng[1]) if len(rng) > 1 else 1.0, "marks": [], "jumps": []})
        for p in parts[1:]:
            k, _, v = p.partition(" ")
            if k == "mark":
                out["marks"] = [_num(x) for x in v.split("|")]
            elif k == "jump":
                out["jumps"] = [_num(x) for x in v.split(">")]
            else:
                raise FigError(f"garis bilangan: {p}")
        if out["to"] <= out["from"] or out["step"] <= 0 or (out["to"] - out["from"]) / out["step"] > 24:
            raise FigError("rentang garis bilangan tidak wajar")
        for v in out["marks"] + out["jumps"]:
            if not out["from"] <= v <= out["to"]:
                raise FigError(f"titik {v} di luar garis bilangan")
            k = (v - out["from"]) / out["step"]
            if abs(k - round(k)) > 1e-6:
                raise FigError(f"titik {v} tidak tepat pada garis bilangan")
    elif kind in ("frac", "pie"):
        out["items"] = []
        for p in _split(body, " ; "):
            n, _, d = p.partition("/")
            n, d = int(n), int(d)
            if d < 1 or d > 24 or n < 0 or n > d * 3:
                raise FigError(f"pecahan tidak wajar: {p}")
            out["items"].append({"n": n, "d": d})
    elif kind == "place":
        digits = body.replace(".", "")
        if not digits.isdigit() or len(digits) > 9:
            raise FigError("nilai tempat butuh bilangan bulat ≤ 9 angka")
        out["value"] = digits
    elif kind == "array":
        size, _, icon = body.partition(" ")
        r, _, c = size.partition("x")
        out.update({"rows": int(r), "cols": int(c), "icon": icon.strip() or "●"})
        if not (1 <= out["rows"] <= 10 and 1 <= out["cols"] <= 12):
            raise FigError("ukuran susunan tidak wajar")
    elif kind == "count":
        terms = []
        for tok in re.findall(r"\d+\s*\S+|[+\-−×:=]", body):
            if tok in "+-−×:=":
                terms.append({"op": tok.replace("-", "−")})
            else:
                n, icon = re.match(r"(\d+)\s*(\S+)", tok).groups()
                if int(n) > 20:
                    raise FigError("gambar hitung maksimal 20")
                terms.append({"n": int(n), "icon": icon})
        out["terms"] = terms
        if not terms:
            raise FigError("gambar hitung kosong")
    elif kind == "shape":
        name, _, rest = body.partition(" ")
        if name not in SHAPES:
            raise FigError(f"bangun tidak dikenal: {name}")
        out.update({"shape": name, "labels": _split(rest, " ; ")})
    elif kind == "table":
        rows = [[c.strip() for c in r.split(" | ")] for r in _split(body, " ;; ")]
        if len(rows) < 2 or len({len(r) for r in rows}) != 1:
            raise FigError("tabel butuh kepala dan baris dengan kolom sama")
        out.update({"head": rows[0], "rows": rows[1:]})
    elif kind == "coord":
        out.update({"points": [], "lines": [], "polys": [], "range": 6})
        for p in _split(body, " ; "):
            if p.startswith("range "):
                out["range"] = int(p[6:])
            elif p.startswith("poly "):
                out["polys"].append([_point(x) for x in re.findall(r"[A-Z][a-z']?\s*\([^)]*\)", p[5:])])
            elif p.startswith("y="):
                out["lines"].append({"label": p, "abc": _poly(p[2:])})
            else:
                out["points"].append(_point(p))
    elif kind == "clock":
        h, _, m = body.partition(":")
        out.update({"h": int(h), "m": int(m)})
        if not (0 <= out["h"] <= 24 and 0 <= out["m"] < 60):
            raise FigError("jam tidak wajar")
    elif kind == "code":
        src, _, output = body.partition(" => ")
        out.update({"lines": src.split(" ;; "), "output": output.replace(" ;; ", "\n")})
    elif kind == "icons":
        out["items"] = [item(x) for x in _split(body, " ; ")]
        if any("icon" not in x for x in out["items"]):
            raise FigError("setiap gambar butuh ikon")
    elif kind == "circuit":
        mode, _, n = body.partition(" ")
        if mode not in ("seri", "paralel"):
            raise FigError("rangkaian seri atau paralel")
        out.update({"mode": mode, "n": int(n or 2)})
    elif kind == "compass":
        out["mark"] = _split(body, " ; ")
    elif kind == "balance":
        parts = [p.strip() for p in body.split(" | ")]
        if len(parts) < 2:
            raise FigError("timbangan butuh 'kiri | kanan'")
        out.update({"left": parts[0], "right": parts[1]})
        if len(parts) > 2:
            m = re.match(r"^([a-z]) = (-?\d+)$", parts[2])
            if not m:
                raise FigError("jawaban timbangan harus 'x = angka'")
            out["solve"] = {"var": m.group(1), "value": int(m.group(2))}
    elif kind == "chat":
        out["items"] = []
        for p in _split(body, " ; "):
            who, _, said = p.partition(": ")
            if not said:
                raise FigError(f"percakapan butuh 'nama: ucapan': {p}")
            out["items"].append({**item(who), "say": said.strip()})
    if caption:
        out["caption"] = caption
    return out


def _labels(items: list[dict]) -> list[dict]:
    return [{k: v for k, v in x.items() if k in ("icon", "label", "tag", "say")} for x in items]


def activity(fig: dict) -> dict:
    k = fig["type"]
    if k in SEQ or k == "time" or k == "chat":
        items = fig["items"]
        if len(items) >= 3 and len({(x.get("label"), x.get("say")) for x in items}) == len(items):
            ask = "Ketuk kartu sesuai urutan yang benar." if k != "chat" else "Susun percakapan sesuai urutan yang benar."
            if k == "time":
                ask = "Ketuk peristiwa dari yang paling dulu terjadi."
            return {"type": "activity", "mode": "order", "ask": ask, "items": _labels(items), "fixed_first": k == "cycle"}
    if k in ("compare", "venn"):
        cards = []
        for gi, g in enumerate(fig["groups"]):
            for x in g["items"]:
                cards.append({**x, "group": gi})
        if len(cards) >= 3 and len({c["label"] for c in cards}) == len(cards):
            titles = [g["title"] for g in fig["groups"]]
            return {"type": "activity", "mode": "sort", "ask": "Ketuk kartu, lalu ketuk kelompok yang cocok.", "groups": titles, "cards": cards}
    if k == "table" and len(fig["rows"]) >= 2 and len(fig["head"]) >= 2:
        left = [r[0] for r in fig["rows"]]
        right = [r[1] for r in fig["rows"]]
        if len(set(left)) == len(left) and len(set(right)) == len(right):
            return {"type": "activity", "mode": "match", "ask": f"Pasangkan {fig['head'][0]} dengan {fig['head'][1]} yang cocok.", "pairs": [[a, b] for a, b in zip(left, right)]}
    if k == "icons" and len(fig["items"]) >= 3 and all(x["label"] for x in fig["items"]):
        return {"type": "activity", "mode": "find", "ask": "Dengarkan, lalu ketuk gambar yang disebut.", "items": _labels(fig["items"])}
    if k in ("frac", "pie"):
        f = fig["items"][0]
        if 0 < f["n"] <= f["d"]:
            return {"type": "activity", "mode": "color", "ask": f"Warnai {f['n']}/{f['d']} bagian dengan mengetuk kotaknya.", "n": f["n"], "d": f["d"]}
    if k == "place":
        return {"type": "activity", "mode": "build", "ask": f"Susun bilangan {int(fig['value']):,}".replace(",", ".") + " dengan tombol + dan −.", "value": fig["value"]}
    if k == "line":
        target = fig["jumps"][-1] if fig["jumps"] else (fig["marks"][0] if fig["marks"] else None)
        if target is not None:
            return {"type": "activity", "mode": "point", "ask": f"Ketuk letak {_fmt(target)} pada garis bilangan.", "from": fig["from"], "to": fig["to"], "step": fig["step"], "target": target}
    if k == "array":
        n = fig["rows"] * fig["cols"]
        return _pick(f"Ada berapa {fig['icon']} semuanya?", str(n), [str(n + fig["cols"]), str(fig["rows"] + fig["cols"]), str(max(1, n - fig["rows"]))], fig)
    if k == "count":
        nums = [t["n"] for t in fig["terms"] if "n" in t]
        if len(fig["terms"]) == 1:
            n = nums[0]
            return _pick(f"Ada berapa {fig['terms'][0]['icon']}?", str(n), [str(n + 1), str(max(1, n - 1)), str(n + 2)], {k2: v for k2, v in fig.items() if k2 != "caption"})
        if any(t.get("op") == "=" for t in fig["terms"]) and len(nums) >= 2:
            ans = nums[-1]
            terms = fig["terms"][:-1]
            return _pick("Berapa hasilnya?", str(ans), [str(ans + 1), str(max(0, ans - 1)), str(ans + 2)], {**fig, "terms": terms + [{"n": 0, "icon": "❓"}]})
    if k == "bars":
        vals = [x["value"] for x in fig["items"]]
        top = max(vals)
        if vals.count(top) == 1:
            best = fig["items"][vals.index(top)]["label"]
            return _pick("Mana yang nilainya paling besar?", best, [x["label"] for x in fig["items"] if x["label"] != best][:3], None)
    if k == "clock":
        h, m = fig["h"], fig["m"]
        right = f"{h:02d}.{m:02d}"
        wrong = {f"{m // 5 if m else 12:02d}.{(h % 12) * 5:02d}", f"{(h % 12) + 1:02d}.{m:02d}", f"{h:02d}.{(m + 30) % 60:02d}"} - {right}
        return _pick("Pukul berapa yang ditunjukkan jam ini?", right, sorted(wrong)[:3], fig)
    if k == "coord" and fig["points"]:
        p = fig["points"][0]
        x, y = _fmt(p["x"]), _fmt(p["y"])
        right = f"({x}, {y})"
        wrong = {f"({y}, {x})", f"({_fmt(-p['x'])}, {y})", f"({x}, {_fmt(-p['y'])})", f"({_fmt(-p['x'])}, {_fmt(-p['y'])})"} - {right}
        if len(wrong) >= 2:
            return _pick(f"Koordinat titik {p['name']} adalah …", right, sorted(wrong)[:3], fig)
    if k == "circuit":
        if fig["mode"] == "seri":
            return _pick("Pada rangkaian seri, jika satu lampu padam, lampu lainnya …", "ikut padam", ["tetap menyala", "makin terang", "berkedip"], fig)
        return _pick("Pada rangkaian paralel, jika satu lampu padam, lampu lainnya …", "tetap menyala", ["ikut padam", "makin redup semua", "meledak"], fig)
    if k == "balance" and fig.get("solve"):
        v, n = fig["solve"]["var"], fig["solve"]["value"]
        return _pick(f"Agar timbangan seimbang, berapa nilai {v}?", f"{v} = {n}", [f"{v} = {n + 1}", f"{v} = {n - 1}", f"{v} = {n * 2}"], {k2: fig[k2] for k2 in ("type", "left", "right")})
    if k == "compass":
        return _pick("Matahari terbit dari arah …", "Timur", ["Barat", "Utara", "Selatan"], fig)
    if k == "code" and fig["output"]:
        return {"type": "activity", "mode": "reveal", "ask": "Tebak dulu hasil programnya di kepalamu, lalu ketuk untuk melihat jawabannya.", "show": fig, "answer": fig["output"]}
    hot = _hotspots(fig)
    if len(hot) >= 2:
        return {"type": "activity", "mode": "explore", "ask": "Ketuk setiap bagian untuk mendengarkan BOBO menjelaskan.", "items": hot}
    return {"type": "activity", "mode": "explore", "ask": "Perhatikan gambarnya, lalu ketuk untuk mendengarkan penjelasannya.", "items": [{"label": fig.get("caption") or "Perhatikan gambarnya baik-baik."}], "show": fig}


def _hotspots(fig: dict) -> list[dict]:
    k = fig["type"]
    if k == "mind":
        return _labels([fig["center"]] + fig["items"])
    if "items" in fig and isinstance(fig["items"], list) and fig["items"] and "label" in fig["items"][0]:
        return _labels(fig["items"])
    if k == "shape":
        return [{"label": x} for x in fig["labels"]]
    if k in ("compare", "venn"):
        return _labels([g["title"] for g in fig["groups"]])
    return []


def _pick(ask: str, right: str, wrong: list[str], show: dict | None) -> dict:
    opts = [right] + [w for w in dict.fromkeys(wrong) if w != right][:3]
    out = {"type": "activity", "mode": "pick", "ask": ask, "options": opts, "answer": 0}
    if show:
        out["show"] = show
    return out


def _fmt(v: float) -> str:
    if float(v).is_integer():
        return str(int(v))
    return str(round(v, 2)).replace(".", ",")


def parse_bank(text: str) -> dict[tuple[str, str], dict]:
    out: dict[tuple[str, str], dict] = {}
    code = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            code = line[3:].strip()
            continue
        title, sep, spec = line.partition(" :: ")
        if not sep or code is None:
            raise FigError(f"baris gambar tidak dikenal: {line}")
        key = (code, title.strip())
        if key in out:
            raise FigError(f"gambar ganda: {key}")
        try:
            out[key] = parse(spec)
        except (FigError, ValueError, ZeroDivisionError) as e:
            raise FigError(f"{code} {title}: {e}") from e
    return out
