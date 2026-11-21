# Known Issues & Batasan

1. Aplikasi Flutter sudah terkompilasi dan lulus tes di CI, tetapi belum diuji di perangkat Android nyata (layar kecil, TalkBack, offline end-to-end) dan belum diuji terhubung ke server sungguhan.
2. Flutter 3.50 menandai `package:flutter/material.dart` deprecated (pindah ke `material_ui`); masih berfungsi, migrasi impor bisa dilakukan nanti.
3. Konten hanya contoh: Matematika kelas 2, 5, 8 (1 bab). Wajib ditinjau tim kurikulum; kelas dan mapel lain kosong.
4. Sumber kurikulum resmi belum diisi (placeholder berstatus belum diverifikasi).
5. Pembayaran/langganan premium belum dibangun (tabel dan entitlement sudah ada; paket diatur manual di database).
6. Job pembersihan percakapan AI 30 hari belum dibuat.
7. Retrieval memakai full-text search, belum semantic search (pgvector bisa ditambah).
8. Filter keselamatan berbasis aturan; perlu ditinjau dan diuji berkala.
9. APK dari CI memakai signing debug dan mengizinkan HTTP untuk pengujian lokal. Untuk Play Store: keystore rilis, tanpa `--allow-http`, App Bundle.
10. Rate limiter berada di memori proses (cukup untuk satu instance API).
11. Media (gambar/audio/video) di materi: tabel tersedia, unggahan belum dibuat di CMS.
12. Kepatuhan UU PDP dan Google Play Families belum diverifikasi ahli hukum.
13. Ekspor data di aplikasi disalin ke clipboard (belum disimpan sebagai file).
14. Kuota penyimpanan artifact GitHub Actions di akun sempat penuh; karena itu APK dipublikasikan sebagai aset GitHub Release, bukan artifact.
