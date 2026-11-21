# Status Milestone

Status per 2026-11-21. "Terverifikasi" berarti diuji otomatis di lingkungan pengembangan.

| Milestone | Status | Bukti |
|---|---|---|
| M0 Audit | Selesai | belum ada repo sebelumnya; dibangun dari nol |
| M1 Fondasi | Selesai, terverifikasi | CI GitHub Actions hijau: backend 25 tes lulus, CMS build lulus, Flutter analyze + test + APK lulus |
| M2 Orang tua & anak | Selesai, terverifikasi backend | registrasi + persetujuan, PIN + lockout, isolasi keluarga, token anak, lupa PIN di aplikasi |
| M3 Kurikulum & konten | Selesai, terverifikasi backend | kurikulum berversi, sumber dengan status verifikasi, review & publikasi, CMS |
| M4 Latihan & asesmen | Selesai, terverifikasi backend | penilaian server, asesmen ber-timer server, submit idempoten, finalisasi otomatis, esai manual |
| M5 AI Tutor | Selesai, terverifikasi backend | provider-independent, safety, RAG full-text, kuota, log biaya, fallback, batas biaya global |
| M6 Dashboard orang tua | Selesai, terverifikasi backend | KPI, status penguasaan, rekomendasi berbasis bukti, Tanya BOBO |
| M7 Offline | Kode selesai, terkompilasi | paket offline, antrean SQLite, sinkron idempoten (server teruji; alur aplikasi belum diuji di perangkat) |
| M8 QA & rilis | Sebagian | APK uji otomatis di GitHub Release `android-latest`; belum: uji perangkat nyata, tinjauan privasi/hukum, signing rilis, Google Play |

APK uji dibangun otomatis setiap push ke `main` (Flutter stable 3.50.1) dan diunggah ke GitHub Release `android-latest`. `flutter analyze`: 0 error, 0 warning (hanya info deprecation `material.dart`).
