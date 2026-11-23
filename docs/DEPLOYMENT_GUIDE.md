# Panduan Deployment

Aplikasi Android 1.2.0 tidak butuh server. Server di bawah hanya untuk tim konten (CMS).

## Memperbarui materi di aplikasi
1. Tim konten menyusun dan meninjau materi di CMS sampai terbit.
2. CMS → Impor, AI & audit → **Unduh paket materi** (atau `docker compose exec api python -m app.cli export-bundle --out bobo-content.json`; tambah `--include-sample` hanya untuk demo).
3. Ganti `mobile/assets/content/bobo-content.json`, naikkan `version` di `mobile/pubspec.yaml`, push ke `main`, lalu tanda tangani dan rilis berkas dari GitHub Actions.

## Server (Docker Compose)
1. Siapkan server Linux dengan Docker. Minimal 2 vCPU, 2 GB RAM, 20 GB disk.
2. `cp .env.example .env`, isi `POSTGRES_PASSWORD`, `BOBO_JWT_SECRET` (acak 64 hex), `BOBO_CORS_ORIGINS` (alamat CMS), `CMS_API_BASE_URL` (alamat publik API).
3. `docker compose up -d --build` — API menjalankan migrasi otomatis saat start.
4. `docker compose exec api python -m app.cli seed --full` lalu buat akun staf: `docker compose exec api python -m app.cli create-staff --email ... --name ... --role admin` (juga buat akun `reviewer` terpisah).
5. Pasang reverse proxy TLS (Caddy/Nginx) untuk `api.domainmu` → `:8000` dan `cms.domainmu` → `:3000`. Jangan buka port database.
6. Backup harian otomatis ke `./backups` (simpan 14 hari); salin ke penyimpanan lain secara berkala.
7. Layanan `maintenance` menghapus percakapan AI berumur lebih dari 30 hari setiap hari (`python -m app.cli purge`).
8. Isi `BOBO_OPERATOR_NAME` dan `BOBO_PRIVACY_CONTACT_EMAIL` agar halaman `/privacy` menampilkan pengelola dan kontak yang benar.

## Aplikasi Android
- Otomatis: setiap push ke `main`, GitHub Actions menjalankan analisis + tes, lalu membangun APK (signing debug) dan App Bundle (tanpa tanda tangan rilis) ke GitHub Release `android-latest`. Branch `wip/**` hanya menjalankan analisis dan tes.
- Lokal:
  ```bash
  cd mobile
  flutter create --platforms=android --org id.bobo --project-name bobo_belajar .
  rm test/widget_test.dart
  python tool/prepare_android.py
  flutter pub get && flutter test
  flutter build appbundle --release
  ```
- Rilis (Play Store): taruh `upload-keystore.jks` di `mobile/android/app/` dan `mobile/android/key.properties` (isi: `storePassword`, `keyPassword`, `keyAlias=upload`, `storeFile=upload-keystore.jks`). `prepare_android.py` (tanpa `--allow-http`) otomatis memakai signing rilis jika `key.properties` ada. Lalu `flutter build appbundle --release`. Kedua file tidak boleh masuk git.
- CI membangun dua berkas: APK uji (signing debug, HTTP lokal diizinkan) dan App Bundle rilis tanpa tanda tangan rilis. App Bundle dan APK HTTPS ditandatangani di luar CI dengan upload key, karena kunci tidak disimpan di GitHub:
  ```bash
  zip -d app.aab 'META-INF/*.SF' 'META-INF/*.RSA' 'META-INF/MANIFEST.MF'
  jarsigner -keystore upload-keystore.jks -sigalg SHA256withRSA -digestalg SHA-256 -signedjar BOBO-Belajar.aab app.aab upload
  python mobile/tool/apk_sign_v2.py app-https.apk BOBO-Belajar-release.apk upload-keystore.jks <password>
  ```
  `apk_sign_v2.py` membuat tanda tangan APK Signature Scheme v2 (cukup untuk minSdk 24). Jika Android SDK tersedia, `apksigner sign` boleh dipakai sebagai gantinya.

## Lembar Soal Latihan SAS (PDF)
Setelah mengubah bank soal di `backend/app/seed/full/sas<kelas>.py` atau `sasx<kelas>.py`, buat ulang PDF cetak per kelas (Ganjil/Genap) dengan `cd backend && python tools/sas_pdf.py --out <folder>` (butuh `reportlab` dari `requirements-dev.txt` dan font DejaVu). Urutan pilihan A–D di PDF sama dengan di aplikasi karena memakai fungsi pengacak yang sama dengan seeding.
