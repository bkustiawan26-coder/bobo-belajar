# BOBO BELAJAR

Teman belajar Android untuk siswa SD kelas 1–SMP kelas 9, dengan mode orang tua di aplikasi yang sama. Versi 1.4.0 (Android 7.0+): berjalan **lokal penuh** di HP, tanpa server, tanpa akun, tanpa internet. Berisi draf materi, latihan, dan asesmen Semester 1 dan 2 untuk Kelas 1–9: Matematika, Bahasa Indonesia, IPAS/IPA/IPS, Pendidikan Pancasila, Bahasa Inggris, Seni dan Budaya, PJOK, Informatika, serta Koding dan Kecerdasan Artifisial (belum ditinjau guru; Pendidikan Agama belum tersedia).

| Bagian | Teknologi | Folder |
|---|---|---|
| Aplikasi Android (mode anak + orang tua), mesin belajar lokal | Flutter, SQLite | `mobile/` |
| API untuk tim konten + ekspor paket materi | Python 3.13, FastAPI, PostgreSQL 16, Alembic | `backend/` |
| CMS konten (admin/editor/peninjau) | Next.js 16, TypeScript | `cms/` |
| Infrastruktur | Docker Compose, GitHub Actions | `docker-compose.yml`, `.github/` |

## Menjalankan cepat (server konten, opsional)

```bash
cp .env.example .env
# isi POSTGRES_PASSWORD dan BOBO_JWT_SECRET (python -c "import secrets;print(secrets.token_hex(32))")
docker compose up -d --build
docker compose exec api python -m app.cli seed --full              # struktur kurikulum + draf konten Kelas 1–9 (status review)
docker compose exec api python -m app.cli create-staff --email admin@contoh.id --name Admin --role admin
```

- API: `http://SERVER:8000` (dokumentasi interaktif `/docs` hanya di non-production)
- CMS: `http://SERVER:3000`

Konten contoh masuk sebagai **menunggu review**; terbitkan lewat CMS setelah ditinjau. Untuk demo lokal saja: `seed --full --publish-sample` (ditolak di `BOBO_ENV=production`).

## Aplikasi Android

Saat pertama dibuka: orang tua menyetujui kebijakan privasi, membuat PIN, menyimpan kode pemulihan, lalu menambah profil anak. Materi dibundel di `mobile/assets/content/bobo-content.json` (diekspor dari CMS). Build otomatis ada di GitHub Release `android-latest`; berkas rilis bertanda tangan disimpan di luar git, di folder `release\<versi>` pada salinan proyek pengelola. Build, signing, dan pembaruan materi: `docs/DEPLOYMENT_GUIDE.md`; persiapan Play Store: `docs/PLAY_STORE.md`.

## Dokumentasi

`docs/`: SYSTEM_ARCHITECTURE, DATABASE_ERD, API_SPECIFICATION, CURRICULUM_MODEL, AI_ARCHITECTURE, SECURITY_AND_PRIVACY, CHILD_SAFETY, DEPLOYMENT_GUIDE, TESTING_STRATEGY, COST_ESTIMATION, MILESTONE_STATUS, CHANGELOG, KNOWN_ISSUES, PLAY_STORE.
