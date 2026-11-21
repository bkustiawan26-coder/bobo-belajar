import uuid
from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base, TimestampMixin

QUESTION_TYPES = ("mc", "multi", "tf", "matching", "fill", "short", "essay")


class Question(Base, TimestampMixin):
    __tablename__ = "questions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"), index=True, nullable=False)
    learning_objective_id: Mapped[int | None] = mapped_column(ForeignKey("learning_objectives.id", ondelete="SET NULL"))
    type: Mapped[str] = mapped_column(String(12), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    image_asset_id: Mapped[int | None] = mapped_column(ForeignKey("media_assets.id", ondelete="SET NULL"))
    difficulty: Mapped[str] = mapped_column(String(12), default="mudah", nullable=False)
    answer: Mapped[dict | None] = mapped_column(JSON)
    rubric: Mapped[str | None] = mapped_column(Text)
    usage: Mapped[str] = mapped_column(String(12), default="both", nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="draft", index=True, nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_sample: Mapped[bool] = mapped_column(default=False, nullable=False)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    author_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    options: Mapped[list["QuestionOption"]] = relationship(cascade="all, delete-orphan", order_by="QuestionOption.position", lazy="selectin")
    explanation: Mapped["QuestionExplanation | None"] = relationship(cascade="all, delete-orphan", uselist=False, lazy="selectin")
    sources: Mapped[list["QuestionSource"]] = relationship(cascade="all, delete-orphan", lazy="selectin")


class QuestionVersion(Base, TimestampMixin):
    __tablename__ = "question_versions"
    __table_args__ = (UniqueConstraint("question_id", "version"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), index=True, nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False)
    snapshot: Mapped[dict] = mapped_column(JSON, nullable=False)


class QuestionOption(Base):
    __tablename__ = "question_options"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), index=True, nullable=False)
    position: Mapped[int] = mapped_column(Integer, nullable=False)
    label: Mapped[str] = mapped_column(String(500), nullable=False)
    side: Mapped[str] = mapped_column(String(5), default="a", nullable=False)


class QuestionExplanation(Base, TimestampMixin):
    __tablename__ = "question_explanations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), unique=True, nullable=False)
    explanation: Mapped[str] = mapped_column(Text, nullable=False)
    mistake_hint: Mapped[str | None] = mapped_column(Text)


class QuestionSource(Base, TimestampMixin):
    __tablename__ = "question_sources"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), index=True, nullable=False)
    source: Mapped[str] = mapped_column(String(300), nullable=False)
    reference: Mapped[str | None] = mapped_column(String(500))


class QuestionReview(Base, TimestampMixin):
    __tablename__ = "question_reviews"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), index=True, nullable=False)
    reviewer_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    decision: Mapped[str] = mapped_column(String(20), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)
