# BOBO BELAJAR

Teman belajar Android untuk siswa SD kelas 1–SMP kelas 9, dengan mode orang tua di aplikasi yang sama. Versi 1.0.0 (Android 7.0+).

| Bagian | Teknologi | Folder |
|---|---|---|
| Aplikasi Android (mode anak + orang tua) | Flutter, SQLite (offline), secure storage | `mobile/` |
| API & AI service | Python 3.13, FastAPI, PostgreSQL 16, Alembic | `backend/` |
| CMS konten (admin/editor/peninjau) | Next.js 16, TypeScript | `cms/` |
| Infrastruktur | Docker Compose, GitHub Actions | `docker-compose.yml`, `.github/` |

## Menjalankan cepat (server)

```bash
cp .env.example .env
# isi POSTGRES_PASSWORD dan BOBO_JWT_SECRET (python -c "import secrets;print(secrets.token_hex(32))")
docker compose up -d --build
docker compose exec api python -m app.cli seed --sample            # struktur kurikulum + konten contoh (status review)
docker compose exec api python -m app.cli create-staff --email admin@contoh.id --name Admin --role admin
```

- API: `http://SERVER:8000` (dokumentasi interaktif `/docs` hanya di non-production)
- CMS: `http://SERVER:3000`

Konten contoh masuk sebagai **menunggu review**; terbitkan lewat CMS setelah ditinjau. Untuk demo lokal saja: `seed --sample --publish-sample` (ditolak di `BOBO_ENV=production`).

## Aplikasi Android

Rilis 1.0.0 ada di GitHub Release `v1.0.0` (App Bundle bertanda tangan untuk Play Store, APK rilis, APK uji). Build terbaru dari setiap push ada di `android-latest`. Build lokal dan signing: `docs/DEPLOYMENT_GUIDE.md`; persiapan Play Store: `docs/PLAY_STORE.md`.
Saat pertama dibuka, aplikasi meminta alamat server, lalu orang tua mendaftar, membuat PIN, dan menambah profil anak.

## Dokumentasi

`docs/`: SYSTEM_ARCHITECTURE, DATABASE_ERD, API_SPECIFICATION, CURRICULUM_MODEL, AI_ARCHITECTURE, SECURITY_AND_PRIVACY, CHILD_SAFETY, DEPLOYMENT_GUIDE, TESTING_STRATEGY, COST_ESTIMATION, MILESTONE_STATUS, CHANGELOG, KNOWN_ISSUES, PLAY_STORE.
