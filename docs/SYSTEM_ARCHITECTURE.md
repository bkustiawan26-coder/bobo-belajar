# Arsitektur Sistem

Modular monolith. Tidak ada microservice.

```
Android (Flutter) ──HTTPS──► FastAPI /v1 ──► PostgreSQL 16
   │  SQLite: cache katalog, paket offline, antrean sinkron      │
   │  Secure storage: refresh token, token per anak              ├─ full-text search (indonesian) untuk RAG
CMS (Next.js) ──HTTPS──► FastAPI /v1/admin                       └─ backup harian (pg_dump, simpan 14 hari)
FastAPI AI service ──► Safety → Retrieval → Provider (grounded | anthropic | openai_compat) → Validasi output
```

## Modul backend (`backend/app`)
| Modul | Isi |
|---|---|
| `api/auth.py` | daftar, masuk, refresh (wajib PIN bila sudah diset), sesi anak |
| `api/student.py` | katalog, materi, latihan, sinkron offline, asesmen, tutor |
| `api/parent.py` | profil anak, dashboard, rekomendasi, Tanya BOBO, persetujuan, ekspor, hapus akun |
| `api/admin.py` | kurikulum, materi, bank soal, review/publikasi, asesmen, impor/ekspor, pemakaian AI, prompt, audit |
| `services/learning.py` | status penguasaan, rekomendasi berbasis bukti, log aktivitas |
| `services/grading.py` | penilaian objektif server-side |
| `services/ai/` | safety, retrieval, provider, layanan tutor & asisten orang tua |

## Model sesi
- Orang tua: access token 30 menit + refresh 60 hari. Refresh **wajib PIN** setelah PIN diset (5x salah → kunci 15 menit).
- Anak: token khusus anak 30 hari, dibuat orang tua; tidak bisa memanggil endpoint orang tua/admin; tidak berlaku lagi jika profil dihapus.
- Admin/editor/peninjau: login CMS, peran dicek per endpoint.

## Struktur aplikasi Android (`mobile/lib`)
`app_state.dart` (mode, sesi, sinkron) · `core/` (API, SQLite, secure storage, tema per jenjang, penilaian lokal) · `screens/child/` (Home, Belajar, Latihan, Ujian, Tutor) · `screens/parent/` (Dashboard, Anak, Perkembangan, Rekomendasi, Tanya BOBO) · `widgets/`.

Tema dibedakan untuk SD 1–2, 3–4, 5–6, dan SMP (warna, ukuran huruf, radius).
