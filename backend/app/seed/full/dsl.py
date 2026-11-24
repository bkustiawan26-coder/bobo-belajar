from dataclasses import dataclass, field


@dataclass
class Q:
    type: str
    body: str
    options: list[str]
    answer: dict
    explanation: str
    hint: str | None = None
    scaffold: dict | None = None
    topic: int = 0
    difficulty: str | None = None


@dataclass
class L:
    minutes: int
    explain: str
    example: str
    points: list[str]
    summary: str
    visual: str | None = None


@dataclass
class T:
    title: str
    act: str
    mistake: str | None
    lesson: L
    qs: list[Q]


@dataclass
class C:
    title: str
    topics: list[T]
    semester: int = 1
    ext: bool = False
    first: bool = False


@dataclass
class S:
    code: str
    chapters: list[C]
    exam: list[Q] = field(default_factory=list)
    exam_title: str | None = None


def _sc(sc):
    if sc is None:
        return None
    example, steps = sc
    return {"example": example, "steps": list(steps)}


def mc(body, options, index, explanation, hint=None, sc=None, t=0, d=None):
    return Q("mc", body, list(options), {"index": index}, explanation, hint, _sc(sc), t, d)


def tf(body, true, explanation, hint=None, sc=None, t=0, d=None):
    return Q("tf", body, ["Benar", "Salah"], {"index": 0 if true else 1}, explanation, hint, _sc(sc), t, d)


def fill(body, accepted, explanation, hint=None, sc=None, t=0, d=None):
    acc = [accepted] if isinstance(accepted, str) else list(accepted)
    return Q("fill", body, [], {"accepted": acc}, explanation, hint, _sc(sc), t, d)


def multi(body, options, indices, explanation, hint=None, sc=None, t=0, d=None):
    return Q("multi", body, list(options), {"indices": sorted(indices)}, explanation, hint, _sc(sc), t, d)


def essay(body, model, keys, explanation, t=0, d=None):
    return Q("essay", body, [], {"model": model, "keys": list(keys)}, explanation, None, None, t, d)
