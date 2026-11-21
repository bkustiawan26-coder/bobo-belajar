import re
from dataclasses import dataclass

from sqlalchemy import delete, func, literal, select, text
from sqlalchemy.orm import Session

from app.models import KnowledgeChunk, KnowledgeDocument, Lesson, Question, Topic


@dataclass
class Passage:
    title: str
    content: str
    source_type: str
    topic_id: int | None
    topic: str | None
    rank: float


def _chunks(text_value: str, size: int = 700) -> list[str]:
    paras = [p.strip() for p in text_value.split("\n\n") if p.strip()]
    out, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 2 > size and cur:
            out.append(cur)
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        out.append(cur)
    return out or [text_value[:size]]


def _upsert(db: Session, source_type: str, source_id: int, title: str, grade: int, topic_id: int | None, priority: int, version: int, body: str) -> None:
    doc = db.scalar(select(KnowledgeDocument).where(KnowledgeDocument.source_type == source_type, KnowledgeDocument.source_id == source_id))
    if doc is None:
        doc = KnowledgeDocument(source_type=source_type, source_id=source_id, title=title, grade_number=grade, topic_id=topic_id, priority=priority, version=version)
        db.add(doc)
        db.flush()
    else:
        doc.title, doc.grade_number, doc.topic_id, doc.priority, doc.version = title, grade, topic_id, priority, version
        db.execute(delete(KnowledgeChunk).where(KnowledgeChunk.document_id == doc.id))
    for i, c in enumerate(_chunks(body)):
        db.add(KnowledgeChunk(document_id=doc.id, position=i, content=c))


def index_lesson(db: Session, lesson: Lesson, grade: int) -> None:
    parts = [lesson.title]
    for b in lesson.blocks:
        if b.text:
            parts.append(f"{b.kind}: {b.text}")
        if b.points:
            parts.append(f"{b.kind}: " + " ".join(str(p) for p in b.points))
    _upsert(db, "lesson", lesson.id, lesson.title, grade, lesson.topic_id, 3, lesson.version, "\n\n".join(parts))


def index_question(db: Session, q: Question, grade: int, topic_title: str) -> None:
    if q.usage == "assessment" or q.explanation is None:
        return
    body = f"Contoh soal {topic_title}: {q.body}\n\nPembahasan: {q.explanation.explanation}"
    _upsert(db, "question", q.id, f"Bank soal · {topic_title}", grade, q.topic_id, 2, q.version, body)


def unindex(db: Session, source_type: str, source_id: int) -> None:
    db.execute(delete(KnowledgeDocument).where(KnowledgeDocument.source_type == source_type, KnowledgeDocument.source_id == source_id))


def _select(rank):
    return (
        select(KnowledgeDocument.title, KnowledgeChunk.content, KnowledgeDocument.source_type, KnowledgeDocument.topic_id, Topic.title, rank.label("rank"))
        .join(KnowledgeDocument, KnowledgeDocument.id == KnowledgeChunk.document_id)
        .outerjoin(Topic, Topic.id == KnowledgeDocument.topic_id)
    )


def search(db: Session, query: str, grade: int, topic_id: int | None = None, limit: int = 4) -> list[Passage]:
    rows = []
    words = [re.sub(r"[^0-9a-z]", "", w) for w in query.lower().split()]
    words = [w for w in words if len(w) >= 3]
    if words:
        tsq = func.to_tsquery(text("'indonesian'::regconfig"), " | ".join(words))
        rank = func.ts_rank_cd(KnowledgeChunk.tsv, tsq)
        rows = db.execute(
            _select(rank).where(KnowledgeDocument.grade_number == grade, KnowledgeChunk.tsv.op("@@")(tsq))
            .order_by(rank.desc(), KnowledgeDocument.priority.desc()).limit(limit)
        ).all()
    if topic_id is not None:
        rows = [r for r in rows if r[3] == topic_id] + [r for r in rows if r[3] != topic_id]
        if not rows:
            rows = db.execute(
                _select(literal(0.0)).where(KnowledgeDocument.grade_number == grade, KnowledgeDocument.topic_id == topic_id)
                .order_by(KnowledgeDocument.priority.desc(), KnowledgeChunk.position).limit(limit)
            ).all()
    return [Passage(title=r[0], content=r[1], source_type=r[2], topic_id=r[3], topic=r[4], rank=float(r[5] or 0)) for r in rows]
