"""initial schema

Revision ID: 0001
Revises: 
Create Date: 2026-11-21 09:10:06.939815
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ai_prompt_versions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purpose', sa.String(length=30), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('template', sa.Text(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('purpose', 'version')
    )
    op.create_table('ai_providers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=False),
    sa.Column('kind', sa.String(length=30), nullable=False),
    sa.Column('base_url', sa.String(length=300), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('assessment_templates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=False),
    sa.Column('label', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('audit_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actor_user_id', sa.Uuid(), nullable=True),
    sa.Column('actor_role', sa.String(length=20), nullable=True),
    sa.Column('action', sa.String(length=60), nullable=False),
    sa.Column('entity_type', sa.String(length=30), nullable=True),
    sa.Column('entity_id', sa.String(length=60), nullable=True),
    sa.Column('meta', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audit_logs_action'), 'audit_logs', ['action'], unique=False)
    op.create_index(op.f('ix_audit_logs_actor_user_id'), 'audit_logs', ['actor_user_id'], unique=False)
    op.create_table('content_versions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entity_type', sa.String(length=20), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('snapshot', sa.JSON(), nullable=False),
    sa.Column('published_by', sa.Uuid(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_versions_entity_id'), 'content_versions', ['entity_id'], unique=False)
    op.create_index(op.f('ix_content_versions_entity_type'), 'content_versions', ['entity_type'], unique=False)
    op.create_table('curriculum_versions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('version', sa.String(length=40), nullable=False),
    sa.Column('academic_year', sa.String(length=20), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('education_levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('media_assets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(length=20), nullable=False),
    sa.Column('storage_key', sa.String(length=300), nullable=False),
    sa.Column('mime_type', sa.String(length=80), nullable=False),
    sa.Column('bytes', sa.Integer(), nullable=False),
    sa.Column('sha256', sa.String(length=64), nullable=False),
    sa.Column('alt_text', sa.String(length=300), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_profiles',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=False),
    sa.Column('grade_number', sa.SmallInteger(), nullable=False),
    sa.Column('tutor_daily_limit_override', sa.Integer(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscription_entitlements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan', sa.String(length=20), nullable=False),
    sa.Column('key', sa.String(length=40), nullable=False),
    sa.Column('value', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plan', 'key')
    )
    op.create_table('users',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('email', sa.String(length=254), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('display_name', sa.String(length=60), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('ai_models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price_input_per_mtok', sa.Float(), nullable=False),
    sa.Column('price_output_per_mtok', sa.Float(), nullable=False),
    sa.Column('is_default', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['provider_id'], ['ai_providers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_id', 'name')
    )
    op.create_table('ai_safety_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=True),
    sa.Column('purpose', sa.String(length=20), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=False),
    sa.Column('stage', sa.String(length=10), nullable=False),
    sa.Column('action', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_safety_events_student_id'), 'ai_safety_events', ['student_id'], unique=False)
    op.create_table('content_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entity_type', sa.String(length=20), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('reviewer_id', sa.Uuid(), nullable=True),
    sa.Column('decision', sa.String(length=20), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['reviewer_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_reviews_entity_id'), 'content_reviews', ['entity_id'], unique=False)
    op.create_index(op.f('ix_content_reviews_entity_type'), 'content_reviews', ['entity_type'], unique=False)
    op.create_table('curriculum_sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curriculum_version_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('issuing_authority', sa.String(length=200), nullable=True),
    sa.Column('reference', sa.String(length=500), nullable=True),
    sa.Column('published_on', sa.Date(), nullable=True),
    sa.Column('retrieved_on', sa.Date(), nullable=True),
    sa.Column('verification_status', sa.String(length=20), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['curriculum_version_id'], ['curriculum_versions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_curriculum_sources_curriculum_version_id'), 'curriculum_sources', ['curriculum_version_id'], unique=False)
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('education_level_id', sa.Integer(), nullable=False),
    sa.Column('number', sa.SmallInteger(), nullable=False),
    sa.Column('phase', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['education_level_id'], ['education_levels.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('read_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notifications_user_id'), 'notifications', ['user_id'], unique=False)
    op.create_table('parent_profiles',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('pin_hash', sa.String(length=100), nullable=True),
    sa.Column('pin_failed_attempts', sa.Integer(), nullable=False),
    sa.Column('pin_locked_until', sa.DateTime(timezone=True), nullable=True),
    sa.Column('plan', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('sync_jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('batch_uuid', sa.Uuid(), nullable=False),
    sa.Column('received', sa.Integer(), nullable=False),
    sa.Column('accepted', sa.Integer(), nullable=False),
    sa.Column('duplicates', sa.Integer(), nullable=False),
    sa.Column('rejected', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('batch_uuid')
    )
    op.create_index(op.f('ix_sync_jobs_student_id'), 'sync_jobs', ['student_id'], unique=False)
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'role')
    )
    op.create_index(op.f('ix_user_roles_user_id'), 'user_roles', ['user_id'], unique=False)
    op.create_table('ai_conversations',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('purpose', sa.String(length=20), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('parent_id', sa.Uuid(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_conversations_parent_id'), 'ai_conversations', ['parent_id'], unique=False)
    op.create_index(op.f('ix_ai_conversations_student_id'), 'ai_conversations', ['student_id'], unique=False)
    op.create_table('ai_usage_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purpose', sa.String(length=20), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=True),
    sa.Column('parent_id', sa.Uuid(), nullable=True),
    sa.Column('provider', sa.String(length=30), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('prompt_version', sa.Integer(), nullable=True),
    sa.Column('input_tokens', sa.Integer(), nullable=False),
    sa.Column('output_tokens', sa.Integer(), nullable=False),
    sa.Column('cost_usd', sa.Float(), nullable=False),
    sa.Column('latency_ms', sa.Integer(), nullable=False),
    sa.Column('outcome', sa.String(length=20), nullable=False),
    sa.Column('cached', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_usage_logs_parent_id'), 'ai_usage_logs', ['parent_id'], unique=False)
    op.create_index(op.f('ix_ai_usage_logs_purpose'), 'ai_usage_logs', ['purpose'], unique=False)
    op.create_index(op.f('ix_ai_usage_logs_student_id'), 'ai_usage_logs', ['student_id'], unique=False)
    op.create_table('guardian_child_links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Uuid(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('relationship_type', sa.String(length=20), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('parent_id', 'student_id')
    )
    op.create_index(op.f('ix_guardian_child_links_parent_id'), 'guardian_child_links', ['parent_id'], unique=False)
    op.create_index(op.f('ix_guardian_child_links_student_id'), 'guardian_child_links', ['student_id'], unique=False)
    op.create_table('guardian_consents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Uuid(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=True),
    sa.Column('consent_type', sa.String(length=40), nullable=False),
    sa.Column('policy_version', sa.String(length=20), nullable=False),
    sa.Column('granted', sa.Boolean(), nullable=False),
    sa.Column('granted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('revoked_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardian_consents_parent_id'), 'guardian_consents', ['parent_id'], unique=False)
    op.create_index(op.f('ix_guardian_consents_student_id'), 'guardian_consents', ['student_id'], unique=False)
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Uuid(), nullable=False),
    sa.Column('provider', sa.String(length=30), nullable=False),
    sa.Column('provider_ref', sa.String(length=120), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_ref')
    )
    op.create_index(op.f('ix_payments_parent_id'), 'payments', ['parent_id'], unique=False)
    op.create_table('privacy_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Uuid(), nullable=True),
    sa.Column('student_id', sa.Uuid(), nullable=True),
    sa.Column('kind', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_privacy_requests_parent_id'), 'privacy_requests', ['parent_id'], unique=False)
    op.create_index(op.f('ix_privacy_requests_student_id'), 'privacy_requests', ['student_id'], unique=False)
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curriculum_version_id', sa.Integer(), nullable=False),
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('short_label', sa.String(length=4), nullable=False),
    sa.Column('sort_order', sa.Integer(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['curriculum_version_id'], ['curriculum_versions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['grade_id'], ['grades.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('curriculum_version_id', 'grade_id', 'code')
    )
    op.create_index(op.f('ix_subjects_curriculum_version_id'), 'subjects', ['curriculum_version_id'], unique=False)
    op.create_index(op.f('ix_subjects_grade_id'), 'subjects', ['grade_id'], unique=False)
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Uuid(), nullable=False),
    sa.Column('plan', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('current_period_end', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscriptions_parent_id'), 'subscriptions', ['parent_id'], unique=False)
    op.create_table('ai_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.Uuid(), nullable=False),
    sa.Column('role', sa.String(length=12), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('sources', sa.JSON(), nullable=True),
    sa.Column('flagged', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['ai_conversations.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_messages_conversation_id'), 'ai_messages', ['conversation_id'], unique=False)
    op.create_table('assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('short_title', sa.String(length=80), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('grade_number', sa.SmallInteger(), nullable=False),
    sa.Column('semester', sa.SmallInteger(), nullable=True),
    sa.Column('duration_minutes', sa.Integer(), nullable=False),
    sa.Column('shuffle_questions', sa.Boolean(), nullable=False),
    sa.Column('shuffle_options', sa.Boolean(), nullable=False),
    sa.Column('passing_score', sa.Float(), nullable=True),
    sa.Column('show_result', sa.String(length=20), nullable=False),
    sa.Column('difficulty_distribution', sa.JSON(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('is_sample', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['template_id'], ['assessment_templates.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assessments_grade_number'), 'assessments', ['grade_number'], unique=False)
    op.create_index(op.f('ix_assessments_status'), 'assessments', ['status'], unique=False)
    op.create_index(op.f('ix_assessments_subject_id'), 'assessments', ['subject_id'], unique=False)
    op.create_table('chapters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=160), nullable=False),
    sa.Column('semester', sa.SmallInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chapters_subject_id'), 'chapters', ['subject_id'], unique=False)
    op.create_table('assessment_sessions',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('assessment_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('deadline_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('submitted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('question_order', sa.JSON(), nullable=False),
    sa.Column('option_orders', sa.JSON(), nullable=False),
    sa.Column('submit_key', sa.String(length=80), nullable=True),
    sa.Column('auto_submitted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['assessment_id'], ['assessments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submit_key')
    )
    op.create_index(op.f('ix_assessment_sessions_assessment_id'), 'assessment_sessions', ['assessment_id'], unique=False)
    op.create_index(op.f('ix_assessment_sessions_status'), 'assessment_sessions', ['status'], unique=False)
    op.create_index(op.f('ix_assessment_sessions_student_id'), 'assessment_sessions', ['student_id'], unique=False)
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chapter_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=160), nullable=False),
    sa.Column('sort_order', sa.Integer(), nullable=False),
    sa.Column('home_activity', sa.Text(), nullable=True),
    sa.Column('common_mistake', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_topics_chapter_id'), 'topics', ['chapter_id'], unique=False)
    op.create_table('assessment_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Uuid(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('assessment_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Float(), nullable=False),
    sa.Column('correct_count', sa.Integer(), nullable=False),
    sa.Column('total_count', sa.Integer(), nullable=False),
    sa.Column('pending_review_count', sa.Integer(), nullable=False),
    sa.Column('weak_topic_ids', sa.JSON(), nullable=False),
    sa.Column('passed', sa.Boolean(), nullable=True),
    sa.Column('is_final', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['assessment_id'], ['assessments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['session_id'], ['assessment_sessions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    op.create_index(op.f('ix_assessment_results_assessment_id'), 'assessment_results', ['assessment_id'], unique=False)
    op.create_index(op.f('ix_assessment_results_student_id'), 'assessment_results', ['student_id'], unique=False)
    op.create_table('knowledge_documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_type', sa.String(length=20), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('grade_number', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source_type', 'source_id')
    )
    op.create_index(op.f('ix_knowledge_documents_grade_number'), 'knowledge_documents', ['grade_number'], unique=False)
    op.create_index(op.f('ix_knowledge_documents_topic_id'), 'knowledge_documents', ['topic_id'], unique=False)
    op.create_table('learning_objectives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=40), nullable=True),
    sa.Column('outcome', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['curriculum_sources.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_learning_objectives_topic_id'), 'learning_objectives', ['topic_id'], unique=False)
    op.create_table('learning_recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('key', sa.String(length=80), nullable=False),
    sa.Column('kind', sa.String(length=20), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('evidence', sa.Text(), nullable=False),
    sa.Column('activity', sa.Text(), nullable=False),
    sa.Column('duration_label', sa.String(length=30), nullable=False),
    sa.Column('evidence_data', sa.JSON(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('done_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id', 'key')
    )
    op.create_index(op.f('ix_learning_recommendations_student_id'), 'learning_recommendations', ['student_id'], unique=False)
    op.create_table('learning_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('kind', sa.String(length=20), nullable=False),
    sa.Column('summary', sa.String(length=200), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('occurred_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_learning_sessions_occurred_at'), 'learning_sessions', ['occurred_at'], unique=False)
    op.create_index(op.f('ix_learning_sessions_student_id'), 'learning_sessions', ['student_id'], unique=False)
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=160), nullable=False),
    sa.Column('minutes', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('is_sample', sa.Boolean(), nullable=False),
    sa.Column('published_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('author_id', sa.Uuid(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lessons_status'), 'lessons', ['status'], unique=False)
    op.create_index(op.f('ix_lessons_topic_id'), 'lessons', ['topic_id'], unique=False)
    op.create_table('mastery_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.Column('evidence_count', sa.Integer(), nullable=False),
    sa.Column('recent_correct', sa.Integer(), nullable=False),
    sa.Column('recent_total', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id', 'topic_id')
    )
    op.create_index(op.f('ix_mastery_records_student_id'), 'mastery_records', ['student_id'], unique=False)
    op.create_table('knowledge_chunks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('tsv', postgresql.TSVECTOR(), sa.Computed("to_tsvector('indonesian'::regconfig, content)", persisted=True), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['document_id'], ['knowledge_documents.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_knowledge_chunks_document_id'), 'knowledge_chunks', ['document_id'], unique=False)
    op.create_index('ix_knowledge_chunks_tsv', 'knowledge_chunks', ['tsv'], unique=False, postgresql_using='gin')
    op.create_table('lesson_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(length=30), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('points', sa.JSON(), nullable=True),
    sa.Column('visual', sa.String(length=30), nullable=True),
    sa.Column('media_asset_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['media_asset_id'], ['media_assets.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lesson_blocks_lesson_id'), 'lesson_blocks', ['lesson_id'], unique=False)
    op.create_table('lesson_progress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('step', sa.Integer(), nullable=False),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('downloaded', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('student_id', 'lesson_id')
    )
    op.create_index(op.f('ix_lesson_progress_student_id'), 'lesson_progress', ['student_id'], unique=False)
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('learning_objective_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=12), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('image_asset_id', sa.Integer(), nullable=True),
    sa.Column('difficulty', sa.String(length=12), nullable=False),
    sa.Column('answer', sa.JSON(), nullable=True),
    sa.Column('rubric', sa.Text(), nullable=True),
    sa.Column('usage', sa.String(length=12), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('is_sample', sa.Boolean(), nullable=False),
    sa.Column('published_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('author_id', sa.Uuid(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['image_asset_id'], ['media_assets.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['learning_objective_id'], ['learning_objectives.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_status'), 'questions', ['status'], unique=False)
    op.create_index(op.f('ix_questions_topic_id'), 'questions', ['topic_id'], unique=False)
    op.create_table('assessment_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Uuid(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('response', sa.JSON(), nullable=True),
    sa.Column('is_correct', sa.Boolean(), nullable=True),
    sa.Column('points_awarded', sa.Float(), nullable=True),
    sa.Column('needs_review', sa.Boolean(), nullable=False),
    sa.Column('ai_suggested_points', sa.Float(), nullable=True),
    sa.Column('ai_suggestion_reason', sa.Text(), nullable=True),
    sa.Column('reviewed_by', sa.Uuid(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['reviewed_by'], ['users.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['session_id'], ['assessment_sessions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_id', 'question_id')
    )
    op.create_index(op.f('ix_assessment_answers_session_id'), 'assessment_answers', ['session_id'], unique=False)
    op.create_table('assessment_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assessment_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('points', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['assessment_id'], ['assessments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('assessment_id', 'question_id')
    )
    op.create_index(op.f('ix_assessment_questions_assessment_id'), 'assessment_questions', ['assessment_id'], unique=False)
    op.create_table('exercise_attempts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_uuid', sa.Uuid(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('response', sa.JSON(), nullable=True),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.Column('source', sa.String(length=20), nullable=False),
    sa.Column('answered_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('synced_offline', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student_profiles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('client_uuid')
    )
    op.create_index(op.f('ix_exercise_attempts_answered_at'), 'exercise_attempts', ['answered_at'], unique=False)
    op.create_index(op.f('ix_exercise_attempts_question_id'), 'exercise_attempts', ['question_id'], unique=False)
    op.create_index(op.f('ix_exercise_attempts_student_id'), 'exercise_attempts', ['student_id'], unique=False)
    op.create_index(op.f('ix_exercise_attempts_topic_id'), 'exercise_attempts', ['topic_id'], unique=False)
    op.create_table('question_explanations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('explanation', sa.Text(), nullable=False),
    sa.Column('mistake_hint', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question_id')
    )
    op.create_table('question_options',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=500), nullable=False),
    sa.Column('side', sa.String(length=5), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_options_question_id'), 'question_options', ['question_id'], unique=False)
    op.create_table('question_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('reviewer_id', sa.Uuid(), nullable=True),
    sa.Column('decision', sa.String(length=20), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['reviewer_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_reviews_question_id'), 'question_reviews', ['question_id'], unique=False)
    op.create_table('question_sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=300), nullable=False),
    sa.Column('reference', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_sources_question_id'), 'question_sources', ['question_id'], unique=False)
    op.create_table('question_versions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('snapshot', sa.JSON(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question_id', 'version')
    )
    op.create_index(op.f('ix_question_versions_question_id'), 'question_versions', ['question_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_question_versions_question_id'), table_name='question_versions')
    op.drop_table('question_versions')
    op.drop_index(op.f('ix_question_sources_question_id'), table_name='question_sources')
    op.drop_table('question_sources')
    op.drop_index(op.f('ix_question_reviews_question_id'), table_name='question_reviews')
    op.drop_table('question_reviews')
    op.drop_index(op.f('ix_question_options_question_id'), table_name='question_options')
    op.drop_table('question_options')
    op.drop_table('question_explanations')
    op.drop_index(op.f('ix_exercise_attempts_topic_id'), table_name='exercise_attempts')
    op.drop_index(op.f('ix_exercise_attempts_student_id'), table_name='exercise_attempts')
    op.drop_index(op.f('ix_exercise_attempts_question_id'), table_name='exercise_attempts')
    op.drop_index(op.f('ix_exercise_attempts_answered_at'), table_name='exercise_attempts')
    op.drop_table('exercise_attempts')
    op.drop_index(op.f('ix_assessment_questions_assessment_id'), table_name='assessment_questions')
    op.drop_table('assessment_questions')
    op.drop_index(op.f('ix_assessment_answers_session_id'), table_name='assessment_answers')
    op.drop_table('assessment_answers')
    op.drop_index(op.f('ix_questions_topic_id'), table_name='questions')
    op.drop_index(op.f('ix_questions_status'), table_name='questions')
    op.drop_table('questions')
    op.drop_index(op.f('ix_lesson_progress_student_id'), table_name='lesson_progress')
    op.drop_table('lesson_progress')
    op.drop_index(op.f('ix_lesson_blocks_lesson_id'), table_name='lesson_blocks')
    op.drop_table('lesson_blocks')
    op.drop_index('ix_knowledge_chunks_tsv', table_name='knowledge_chunks', postgresql_using='gin')
    op.drop_index(op.f('ix_knowledge_chunks_document_id'), table_name='knowledge_chunks')
    op.drop_table('knowledge_chunks')
    op.drop_index(op.f('ix_mastery_records_student_id'), table_name='mastery_records')
    op.drop_table('mastery_records')
    op.drop_index(op.f('ix_lessons_topic_id'), table_name='lessons')
    op.drop_index(op.f('ix_lessons_status'), table_name='lessons')
    op.drop_table('lessons')
    op.drop_index(op.f('ix_learning_sessions_student_id'), table_name='learning_sessions')
    op.drop_index(op.f('ix_learning_sessions_occurred_at'), table_name='learning_sessions')
    op.drop_table('learning_sessions')
    op.drop_index(op.f('ix_learning_recommendations_student_id'), table_name='learning_recommendations')
    op.drop_table('learning_recommendations')
    op.drop_index(op.f('ix_learning_objectives_topic_id'), table_name='learning_objectives')
    op.drop_table('learning_objectives')
    op.drop_index(op.f('ix_knowledge_documents_topic_id'), table_name='knowledge_documents')
    op.drop_index(op.f('ix_knowledge_documents_grade_number'), table_name='knowledge_documents')
    op.drop_table('knowledge_documents')
    op.drop_index(op.f('ix_assessment_results_student_id'), table_name='assessment_results')
    op.drop_index(op.f('ix_assessment_results_assessment_id'), table_name='assessment_results')
    op.drop_table('assessment_results')
    op.drop_index(op.f('ix_topics_chapter_id'), table_name='topics')
    op.drop_table('topics')
    op.drop_index(op.f('ix_assessment_sessions_student_id'), table_name='assessment_sessions')
    op.drop_index(op.f('ix_assessment_sessions_status'), table_name='assessment_sessions')
    op.drop_index(op.f('ix_assessment_sessions_assessment_id'), table_name='assessment_sessions')
    op.drop_table('assessment_sessions')
    op.drop_index(op.f('ix_chapters_subject_id'), table_name='chapters')
    op.drop_table('chapters')
    op.drop_index(op.f('ix_assessments_subject_id'), table_name='assessments')
    op.drop_index(op.f('ix_assessments_status'), table_name='assessments')
    op.drop_index(op.f('ix_assessments_grade_number'), table_name='assessments')
    op.drop_table('assessments')
    op.drop_index(op.f('ix_ai_messages_conversation_id'), table_name='ai_messages')
    op.drop_table('ai_messages')
    op.drop_index(op.f('ix_subscriptions_parent_id'), table_name='subscriptions')
    op.drop_table('subscriptions')
    op.drop_index(op.f('ix_subjects_grade_id'), table_name='subjects')
    op.drop_index(op.f('ix_subjects_curriculum_version_id'), table_name='subjects')
    op.drop_table('subjects')
    op.drop_index(op.f('ix_privacy_requests_student_id'), table_name='privacy_requests')
    op.drop_index(op.f('ix_privacy_requests_parent_id'), table_name='privacy_requests')
    op.drop_table('privacy_requests')
    op.drop_index(op.f('ix_payments_parent_id'), table_name='payments')
    op.drop_table('payments')
    op.drop_index(op.f('ix_guardian_consents_student_id'), table_name='guardian_consents')
    op.drop_index(op.f('ix_guardian_consents_parent_id'), table_name='guardian_consents')
    op.drop_table('guardian_consents')
    op.drop_index(op.f('ix_guardian_child_links_student_id'), table_name='guardian_child_links')
    op.drop_index(op.f('ix_guardian_child_links_parent_id'), table_name='guardian_child_links')
    op.drop_table('guardian_child_links')
    op.drop_index(op.f('ix_ai_usage_logs_student_id'), table_name='ai_usage_logs')
    op.drop_index(op.f('ix_ai_usage_logs_purpose'), table_name='ai_usage_logs')
    op.drop_index(op.f('ix_ai_usage_logs_parent_id'), table_name='ai_usage_logs')
    op.drop_table('ai_usage_logs')
    op.drop_index(op.f('ix_ai_conversations_student_id'), table_name='ai_conversations')
    op.drop_index(op.f('ix_ai_conversations_parent_id'), table_name='ai_conversations')
    op.drop_table('ai_conversations')
    op.drop_index(op.f('ix_user_roles_user_id'), table_name='user_roles')
    op.drop_table('user_roles')
    op.drop_index(op.f('ix_sync_jobs_student_id'), table_name='sync_jobs')
    op.drop_table('sync_jobs')
    op.drop_table('parent_profiles')
    op.drop_index(op.f('ix_notifications_user_id'), table_name='notifications')
    op.drop_table('notifications')
    op.drop_table('grades')
    op.drop_index(op.f('ix_curriculum_sources_curriculum_version_id'), table_name='curriculum_sources')
    op.drop_table('curriculum_sources')
    op.drop_index(op.f('ix_content_reviews_entity_type'), table_name='content_reviews')
    op.drop_index(op.f('ix_content_reviews_entity_id'), table_name='content_reviews')
    op.drop_table('content_reviews')
    op.drop_index(op.f('ix_ai_safety_events_student_id'), table_name='ai_safety_events')
    op.drop_table('ai_safety_events')
    op.drop_table('ai_models')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('subscription_entitlements')
    op.drop_table('student_profiles')
    op.drop_table('media_assets')
    op.drop_table('education_levels')
    op.drop_table('curriculum_versions')
    op.drop_index(op.f('ix_content_versions_entity_type'), table_name='content_versions')
    op.drop_index(op.f('ix_content_versions_entity_id'), table_name='content_versions')
    op.drop_table('content_versions')
    op.drop_index(op.f('ix_audit_logs_actor_user_id'), table_name='audit_logs')
    op.drop_index(op.f('ix_audit_logs_action'), table_name='audit_logs')
    op.drop_table('audit_logs')
    op.drop_table('assessment_templates')
    op.drop_table('ai_providers')
    op.drop_table('ai_prompt_versions')
