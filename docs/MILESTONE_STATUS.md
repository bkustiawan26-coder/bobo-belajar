# Status Milestone

Status per 2026-11-23 (versi 1.3.0, mode lokal, konten Kelas 1–9, suara & UX per jenjang). "Terverifikasi" berarti diuji otomatis di lingkungan pengembangan.

| Milestone | Status | Bukti |
|---|---|---|
| M0 Audit | Selesai | belum ada repo sebelumnya; dibangun dari nol |
| M1 Fondasi | Selesai, terverifikasi | CI GitHub Actions hijau: backend 32 tes lulus, CMS build lulus, Flutter analyze + test + APK + App Bundle lulus |
| M2 Orang tua & anak | Selesai, terverifikasi backend | registrasi + persetujuan, PIN + lockout, isolasi keluarga, token anak, lupa PIN di aplikasi |
| M3 Kurikulum & konten | Selesai, terverifikasi backend | kurikulum berversi, sumber dengan status verifikasi, review & publikasi, CMS; 1.2.0: draf konten Kelas 1–9 semua mapel (165 materi, 906 soal, 41 asesmen), belum ditinjau guru |
| M4 Latihan & asesmen | Selesai, terverifikasi backend | penilaian server, asesmen ber-timer server, submit idempoten, finalisasi otomatis, esai manual |
| M5 AI Tutor | Selesai, terverifikasi backend | provider-independent, safety, RAG full-text, kuota, log biaya, fallback, batas biaya global |
| M6 Dashboard orang tua | Selesai, terverifikasi backend | KPI, status penguasaan, rekomendasi berbasis bukti, Tanya BOBO |
| M7 Offline | Selesai, terverifikasi tes aplikasi | 1.1.0 lokal penuh: mesin belajar di HP, paket materi dibundel, tanpa izin internet; 14 tes mesin lokal + 7 tes logika lulus di CI |
| M9 Pendampingan anak tertinggal | Selesai, terverifikasi backend; aplikasi terkompilasi | ulang terjadwal, langkah kecil, jalur pondasi lintas kelas, mode bantuan, bacakan (TTS), alat peraga, Tutor jelaskan ulang, Kemajuanku, sinyal + rencana 7 hari, ringkasan guru; editor prasyarat & langkah kecil di CMS |
| M8 QA & rilis | Rilis 1.3.0 siap unggah | Folder `release\1.3.0` (di luar git): App Bundle dan APK bertanda tangan upload key (diverifikasi `bundletool validate`, `jarsigner -verify`, `apksigtool verify`), manifest tanpa izin internet, draf listing & Data safety (`PLAY_STORE.md`). Belum: uji perangkat nyata, tinjauan hukum, tinjauan guru atas draf konten, unggah ke Play Console |

Build terbaru dibangun otomatis setiap push ke `main` (Flutter stable) dan diunggah ke GitHub Release `android-latest`. `flutter analyze`: 0 error, 0 warning (hanya info deprecation `material.dart`).
