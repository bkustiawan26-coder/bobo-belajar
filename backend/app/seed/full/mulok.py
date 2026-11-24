from dataclasses import dataclass, field

from app.seed.full.dsl import C, L, S, T


@dataclass
class Parsed:
    subjects: list[S] = field(default_factory=list)
    figs: list[tuple[str, str, str]] = field(default_factory=list)
    reads: list[tuple[str, str, str]] = field(default_factory=list)


KEYS = {"min", "act", "mis", "exp", "ex", "pt", "sum", "fig", "read"}


def parse(text: str) -> Parsed:
    out = Parsed()
    subj: S | None = None
    chap: C | None = None
    cur: dict | None = None

    def close():
        nonlocal cur
        if cur is None:
            return
        missing = [k for k in ("exp", "ex", "pt", "sum", "act", "fig") if k not in cur]
        if missing:
            raise ValueError(f"{subj.code} {cur['title']}: kolom {missing} belum diisi")
        lesson = L(int(cur.get("min", 8)), cur["exp"], cur["ex"].replace(" // ", "\n"), [p.strip() for p in cur["pt"].split(" ; ") if p.strip()], cur["sum"])
        chap.topics.append(T(cur["title"], cur["act"], cur.get("mis"), lesson, []))
        out.figs.append((subj.code, cur["title"], cur["fig"]))
        if "read" in cur:
            out.reads.append((subj.code, cur["title"], cur["read"]))
        cur = None

    for no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            close()
            subj = S(line[3:].strip(), [])
            out.subjects.append(subj)
            chap = None
        elif line.startswith("# "):
            close()
            sem, _, title = line[2:].partition("|")
            first = sem.strip().endswith("^")
            chap = C(title.strip(), [], int(sem.strip().rstrip("^")), first=first)
            subj.chapters.append(chap)
        elif line.startswith("@ "):
            close()
            if chap is None:
                raise ValueError(f"baris {no}: topik sebelum bab")
            cur = {"title": line[2:].strip()}
        else:
            key, sep, val = line.partition(":")
            if not sep or key not in KEYS or cur is None:
                raise ValueError(f"baris {no}: tidak dikenal: {line[:60]}")
            cur[key] = val.strip()
    close()
    return out
