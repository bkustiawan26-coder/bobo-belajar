# Arsitektur Sistem

Sejak 1.1.0 aplikasi Android berjalan **lokal**: tidak ada akun, tidak ada server, tidak ada izin internet. Server (FastAPI + PostgreSQL + CMS) hanya dipakai tim konten untuk menyusun dan meninjau materi, lalu mengekspor paket materi yang dibundel ke aplikasi.

```
Tim konten: CMS (Next.js) ──► FastAPI /v1/admin ──► PostgreSQL 16
                                     │
                    GET /admin/content-bundle  atau  python -m app.cli export-bundle
                                     ▼
                     mobile/assets/content/bobo-content.json  (dibundel saat build)

Aplikasi Android (Flutter, offline penuh)
  UI ──► AppState.student()/parent() ──► LocalEngine (mobile/lib/local)
                                          ├─ Content: paket materi (read-only)
                                          ├─ SQLite tabel docs: profil, jawaban, progres, jadwal ulang, sesi asesmen, aktivitas
                                          ├─ PIN & kode pemulihan: PBKDF2-SHA256
                                          └─ Tutor lokal: safety → pencarian kata kunci → jawaban grounded
```

`LocalEngine` menjawab path yang sama dengan API server (`/student/...`, `/parent/...`) dengan bentuk JSON yang sama, sehingga logika penilaian, penguasaan, rekomendasi, jadwal ulang, pondasi, sinyal, dan asesmen identik dengan versi server.

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

## Model sesi (server, untuk CMS dan integrasi masa depan)
- Orang tua: access token 30 menit + refresh 60 hari. Refresh **wajib PIN** setelah PIN diset (5x salah → kunci 15 menit).
- Anak: token khusus anak 30 hari, dibuat orang tua; tidak bisa memanggil endpoint orang tua/admin; tidak berlaku lagi jika profil dihapus.
- Admin/editor/peninjau: login CMS, peran dicek per endpoint.

## Sesi di aplikasi
Mode Orang Tua dibuka dengan PIN (5x salah → terkunci 15 menit). Lupa PIN → kode pemulihan 10 karakter yang ditampilkan sekali saat setup. Mode anak tidak butuh PIN dan tidak bisa memanggil fungsi orang tua.

## Struktur aplikasi Android (`mobile/lib`)
`app_state.dart` (mode: setup, profil, anak, orang tua) · `local/` (engine, content, store, pin, tutor) · `core/` (SQLite, tema per jenjang, penilaian, suara) · `screens/child/` (Home, Belajar, Latihan, Ujian, Tutor) · `screens/parent/` (Dashboard, Anak, Perkembangan, Rekomendasi, Tanya BOBO) · `widgets/`.

Tema dibedakan untuk SD 1–2, 3–4, 5–6, dan SMP (warna, ukuran huruf, radius).
