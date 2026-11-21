"""learning support features

Revision ID: 0002
Revises: 0001
Create Date: 2026-11-21 10:46:13.857507
"""
from alembic import op
import sqlalchemy as sa


revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('topic_prerequisites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('prerequisite_topic_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['prerequisite_topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('topic_id', 'prerequisite_topic_id')
    )
    op.create_index(op.f('ix_topic_prerequisites_prerequisite_topic_id'), 'topic_prerequisites', ['prerequisite_topic_id'], unique=False)
    op.create_index(op.f('ix_topic_prerequisites_topic_id'), 'topic_prerequisites', ['topic_id'], unique=False)
    op.create_table('review_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('step', sa.Integer(), nullable=False),
    sa.Column('due_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_correct', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id', 'question_id')
    )
    op.create_index(op.f('ix_review_items_due_at'), 'review_items', ['due_at'], unique=False)
    op.create_index(op.f('ix_review_items_student_id'), 'review_items', ['student_id'], unique=False)
    op.add_column('questions', sa.Column('scaffold', sa.JSON(), nullable=True))
    op.add_column('student_profiles', sa.Column('settings', sa.JSON(), server_default='{}', nullable=False))


def downgrade() -> None:
    op.drop_column('student_profiles', 'settings')
    op.drop_column('questions', 'scaffold')
    op.drop_index(op.f('ix_review_items_student_id'), table_name='review_items')
    op.drop_index(op.f('ix_review_items_due_at'), table_name='review_items')
    op.drop_table('review_items')
    op.drop_index(op.f('ix_topic_prerequisites_topic_id'), table_name='topic_prerequisites')
    op.drop_index(op.f('ix_topic_prerequisites_prerequisite_topic_id'), table_name='topic_prerequisites')
    op.drop_table('topic_prerequisites')
