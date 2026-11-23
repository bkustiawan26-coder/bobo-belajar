"""lesson block figure

Revision ID: 0003
Revises: 0002
Create Date: 2026-11-23 14:00:00
"""
from alembic import op
import sqlalchemy as sa


revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('lesson_blocks', sa.Column('figure', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('lesson_blocks', 'figure')
