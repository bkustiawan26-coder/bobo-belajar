from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, Integer, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, TimestampMixin


class EducationLevel(Base, TimestampMixin):
    __tablename__ = "education_levels"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(60), nullable=False)


class Grade(Base, TimestampMixin):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    education_level_id: Mapped[int] = mapped_column(ForeignKey("education_levels.id"), nullable=False)
    number: Mapped[int] = mapped_column(SmallInteger, unique=True, nullable=False)
    phase: Mapped[str | None] = mapped_column(String(10))


class CurriculumVersion(Base, TimestampMixin):
    __tablename__ = "curriculum_versions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    version: Mapped[str] = mapped_column(String(40), nullable=False)
    academic_year: Mapped[str | None] = mapped_column(String(20))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="draft", nullable=False)


class CurriculumSource(Base, TimestampMixin):
    __tablename__ = "curriculum_sources"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    curriculum_version_id: Mapped[int] = mapped_column(ForeignKey("curriculum_versions.id", ondelete="CASCADE"), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    issuing_authority: Mapped[str | None] = mapped_column(String(200))
    reference: Mapped[str | None] = mapped_column(String(500))
    published_on: Mapped[date | None] = mapped_column(Date)
    retrieved_on: Mapped[date | None] = mapped_column(Date)
    verification_status: Mapped[str] = mapped_column(String(20), default="unverified", nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)


class Subject(Base, TimestampMixin):
    __tablename__ = "subjects"
    __table_args__ = (UniqueConstraint("curriculum_version_id", "grade_id", "code"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    curriculum_version_id: Mapped[int] = mapped_column(ForeignKey("curriculum_versions.id", ondelete="CASCADE"), index=True, nullable=False)
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"), index=True, nullable=False)
    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    short_label: Mapped[str] = mapped_column(String(4), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class Chapter(Base, TimestampMixin):
    __tablename__ = "chapters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id", ondelete="CASCADE"), index=True, nullable=False)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(160), nullable=False)
    semester: Mapped[int | None] = mapped_column(SmallInteger)


class Topic(Base, TimestampMixin):
    __tablename__ = "topics"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("chapters.id", ondelete="CASCADE"), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(160), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    home_activity: Mapped[str | None] = mapped_column(Text)
    common_mistake: Mapped[str | None] = mapped_column(Text)


class LearningObjective(Base, TimestampMixin):
    __tablename__ = "learning_objectives"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"), index=True, nullable=False)
    code: Mapped[str | None] = mapped_column(String(40))
    outcome: Mapped[str | None] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    source_id: Mapped[int | None] = mapped_column(ForeignKey("curriculum_sources.id", ondelete="SET NULL"))
    status: Mapped[str] = mapped_column(String(20), default="unverified", nullable=False)
