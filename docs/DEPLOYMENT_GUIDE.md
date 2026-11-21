# Panduan Deployment

## Server (Docker Compose)
1. Siapkan server Linux dengan Docker. Minimal 2 vCPU, 2 GB RAM, 20 GB disk.
2. `cp .env.example .env`, isi `POSTGRES_PASSWORD`, `BOBO_JWT_SECRET` (acak 64 hex), `BOBO_CORS_ORIGINS` (alamat CMS), `CMS_API_BASE_URL` (alamat publik API).
3. `docker compose up -d --build` — API menjalankan migrasi otomatis saat start.
4. `docker compose exec api python -m app.cli seed --sample` lalu buat akun staf: `docker compose exec api python -m app.cli create-staff --email ... --name ... --role admin` (juga buat akun `reviewer` terpisah).
5. Pasang reverse proxy TLS (Caddy/Nginx) untuk `api.domainmu` → `:8000` dan `cms.domainmu` → `:3000`. Jangan buka port database.
6. Backup harian otomatis ke `./backups`; salin ke penyimpanan lain secara berkala.

## Aplikasi Android
- Otomatis: setiap push ke `main`, GitHub Actions membangun APK dan mengunggahnya ke GitHub Release `android-latest`. Isi variabel repo `API_BASE_URL` agar alamat server terisi di layar pertama.
- Lokal:
  ```bash
  cd mobile
  flutter create --platforms=android --org id.bobo --project-name bobo_belajar .
  rm test/widget_test.dart
  python tool/prepare_android.py            # tambah --allow-http hanya untuk server lokal tanpa HTTPS
  flutter pub get && flutter test
  flutter build apk --release --dart-define=API_BASE_URL=https://api.domainmu
  ```
- Untuk Play Store: buat upload keystore, konfigurasi `signingConfigs` release, build `appbundle`, jalankan tanpa `--allow-http`.

## Uji di jaringan lokal
Jalankan API di PC (`docker compose up`), lalu di aplikasi isi `http://IP-PC:8000` (APK dari CI sudah mengizinkan HTTP untuk pengujian).
