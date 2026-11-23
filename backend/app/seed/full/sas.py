import re

from app.seed.full.dsl import Q, essay, fill, mc

RANK = {"mc": 0, "fill": 1, "essay": 2}


def target(grade: int) -> tuple[int, int, int]:
    return (20, 10, 5) if grade <= 6 else (35, 5, 5)

_NUM = re.compile(r"^-?\d{1,3}(\.\d{3})+(,\d+)?$")


_FRAC = re.compile(r"^(-?)(\d+)/(\d+)$")


def _forms(a: str) -> list[str]:
    forms = [a, a.replace("\u2212", "-")]
    if _NUM.match(forms[1]):
        forms.append(forms[1].replace(".", ""))
    m = _FRAC.match(forms[1])
    if m and int(m.group(3)) and (10 ** 3 * int(m.group(2))) % int(m.group(3)) == 0:
        value = int(m.group(2)) / int(m.group(3))
        forms.append(m.group(1) + f"{value:.3f}".rstrip("0").rstrip(".").replace(".", ","))
    if "-" in forms[1] and not forms[1].lstrip("-").replace("/", "").isdigit():
        forms.append(forms[1].replace("-", ""))
    if ", " in a:
        forms.append(a.replace(",", ""))
    return forms


def _variants(answers: list[str]) -> list[str]:
    out = []
    for a in answers:
        for f in _forms(a.strip()):
            if f and f not in out:
                out.append(f)
    return out


def parse(text: str) -> dict[tuple[str, int], list[tuple[int, Q]]]:
    bank: dict[tuple[str, int], list[tuple[int, Q]]] = {}
    key = None
    for no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("##"):
            code, sem = line[2:].split()
            key = (code, int(sem))
            bank.setdefault(key, [])
            continue
        if key is None:
            raise ValueError(f"baris {no}: soal sebelum judul mapel")
        isian = line.startswith("=")
        uraian = line.startswith("?")
        parts = [p.strip() for p in line.lstrip("=?").split("|")]
        local = int(parts[0])
        if uraian:
            if len(parts) != 4:
                raise ValueError(f"baris {no}: uraian harus 4 kolom")
            keys = [k.strip() for k in parts[3].split(";") if k.strip()]
            q = essay(parts[1], parts[2], keys, "Poin penting: " + "; ".join(keys) + ".")
        elif isian:
            if len(parts) != 4:
                raise ValueError(f"baris {no}: isian harus 4 kolom")
            q = fill(parts[1], _variants(parts[2].split(";")), parts[3])
        else:
            if len(parts) != 7:
                raise ValueError(f"baris {no}: pilihan ganda harus 7 kolom")
            q = mc(parts[1], parts[2:6], 0, parts[6])
        bank[key].append((local, q))
    return bank
