# Database ERD

52 tabel, migrasi `backend/alembic/versions/0001_initial_schema.py`. Semua relasi memakai foreign key.

```mermaid
erDiagram
  users ||--o{ user_roles : has
  users ||--o| parent_profiles : is
  parent_profiles ||--o{ guardian_child_links : links
  student_profiles ||--o{ guardian_child_links : linked
  parent_profiles ||--o{ guardian_consents : gives
  curriculum_versions ||--o{ curriculum_sources : cites
  curriculum_versions ||--o{ subjects : has
  grades ||--o{ subjects : for
  education_levels ||--o{ grades : has
  subjects ||--o{ chapters : has
  chapters ||--o{ topics : has
  topics ||--o{ learning_objectives : has
  topics ||--o{ lessons : has
  lessons ||--o{ lesson_blocks : has
  topics ||--o{ questions : has
  questions ||--o{ question_options : has
  questions ||--o| question_explanations : has
  questions ||--o{ question_sources : cites
  questions ||--o{ question_reviews : reviewed
  questions ||--o{ question_versions : versions
  assessment_templates ||--o{ assessments : types
  assessments ||--o{ assessment_questions : has
  assessments ||--o{ assessment_sessions : taken
  assessment_sessions ||--o{ assessment_answers : has
  assessment_sessions ||--o| assessment_results : yields
  student_profiles ||--o{ exercise_attempts : makes
  student_profiles ||--o{ lesson_progress : tracks
  student_profiles ||--o{ mastery_records : has
  student_profiles ||--o{ learning_recommendations : gets
  student_profiles ||--o{ learning_sessions : logs
  student_profiles ||--o{ ai_conversations : has
  ai_conversations ||--o{ ai_messages : has
  knowledge_documents ||--o{ knowledge_chunks : has
  parent_profiles ||--o{ subscriptions : has
```

Tabel lain: `media_assets`, `content_versions`, `content_reviews`, `ai_providers`, `ai_models`, `ai_prompt_versions`, `ai_usage_logs`, `ai_safety_events`, `subscription_entitlements`, `payments`, `notifications`, `audit_logs`, `sync_jobs`, `privacy_requests`.

## Indeks penting
- `exercise_attempts.client_uuid` unik (sinkron idempoten), indeks `(student_id)`, `(topic_id)`, `(answered_at)`.
- `assessment_sessions.submit_key` unik; `assessment_answers (session_id, question_id)` unik.
- `knowledge_chunks.tsv` GIN (kolom terhitung `to_tsvector('indonesian', content)`).
- `lessons.status`, `questions.status` untuk antrean review.

## Data anak yang disimpan
Nama panggilan, kelas, aktivitas belajar. Tidak ada nama lengkap, tanggal lahir, sekolah, foto, atau kontak anak.

## Retensi
| Data | Retensi |
|---|---|
| Aktivitas & nilai | selama akun aktif; dihapus permanen saat profil/akun dihapus |
| Percakapan AI | target 30 hari (job pembersihan belum dibuat, lihat KNOWN_ISSUES) |
| Log pemakaian AI | tanpa isi pesan; disimpan untuk kontrol biaya |
| Backup | 14 hari (layanan `backup` di Compose) |

## Backup & pemulihan
`docker compose` menjalankan `pg_dump -Fc` harian ke `./backups`. Pemulihan: `pg_restore -h HOST -U bobo -d bobo --clean backups/bobo-YYYYMMDD-HHMM.dump`. Uji pemulihan minimal sebulan sekali.
