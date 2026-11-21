# Spesifikasi API

Basis: `/v1`. JSON. Autentikasi: `Authorization: Bearer <token>`. OpenAPI lengkap tersedia di `/docs` dan `/openapi.json` saat `BOBO_ENV` bukan production.

## Auth
| Metode | Path | Keterangan |
|---|---|---|
| POST | /auth/register | orang tua; wajib `accept_privacy_policy` dan `accept_child_data_processing` |
| POST | /auth/login | orang tua atau staf |
| POST | /auth/refresh | `refresh_token` + `pin` (wajib jika PIN sudah diset) |
| POST | /auth/child-session | token orang tua → token anak |

## Anak (token anak)
| Metode | Path | Keterangan |
|---|---|---|
| GET | /student/me, /student/home, /student/catalog, /student/progress | profil, target harian, katalog per kelas, status penguasaan |
| GET | /student/lessons/{id} | hanya materi terbit kelas yang sama |
| POST | /student/lessons/{id}/progress | langkah & selesai |
| GET | /student/practice?topic_id= | soal tanpa kunci |
| POST | /student/practice/attempts | dinilai server; idempoten via `client_uuid` |
| GET | /student/offline-pack | materi + latihan dengan kunci untuk offline (bukan asesmen) |
| POST | /student/sync | batch jawaban/progres offline; dinilai ulang server; idempoten |
| GET | /student/assessments | daftar + hasil terakhir; sesi kedaluwarsa difinalisasi otomatis |
| POST | /student/assessments/{id}/start | buat/lanjutkan sesi; `deadline_at` dari server |
| PUT | /student/assessment-sessions/{sid}/answers | simpan otomatis; 409 setelah batas waktu + 30 detik |
| POST | /student/assessment-sessions/{sid}/submit | `idempotency_key`; kirim ulang mengembalikan hasil yang sama |
| GET | /student/assessment-sessions/{sid}/result | hasil + pembahasan |
| POST | /student/tutor/messages | tutor AI; 429 jika kuota habis |
| GET | /student/tutor/quota | kuota harian |

## Orang tua (token orang tua)
`GET /parent/me` · `PUT /parent/pin` · `GET/POST /parent/children` · `PATCH/DELETE /parent/children/{id}` · `GET /parent/children/{id}/dashboard` · `GET /parent/children/{id}/recommendations` · `POST /parent/children/{id}/recommendations/{rid}/done` · `POST /parent/assistant/messages` · `GET/POST /parent/consents` · `GET /parent/export` · `POST /parent/delete-account`

Semua endpoint anak-spesifik mengembalikan 404 untuk anak yang tidak terhubung ke akun.

## Admin (peran admin / editor / reviewer)
Kurikulum: `/admin/curriculum/versions`, `/admin/curriculum/versions/{id}/activate`, `/admin/curriculum/versions/{id}/sources`, `/admin/curriculum/sources/{id}`, `/admin/grades`, `/admin/subjects`, `/admin/subjects/{id}/tree`, `/admin/chapters`, `/admin/topics`, `/admin/topics/{id}`, `/admin/objectives`
Konten: `/admin/lessons[/{id}[/submit|/review|/publish|/unpublish]]`, `/admin/questions[...]` (sama)
Asesmen: `/admin/assessment-templates`, `/admin/assessments[/{id}[/publish|/unpublish]]`, `/admin/essay-reviews`, `/admin/assessment-answers/{id}/score`
Lainnya: `/admin/export`, `/admin/import`, `/admin/ai/usage`, `/admin/ai/prompts`, `/admin/stats`, `/admin/audit`

## Kode status
401 sesi tidak valid · 403 peran salah · 404 tidak ditemukan/tidak berhak · 409 konflik status · 422 validasi · 423 PIN terkunci · 429 batas laju/kuota
