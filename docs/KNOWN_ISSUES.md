# Known Issues & Batasan

1. Aplikasi sudah terkompilasi dan lulus tes di CI, tetapi belum diuji di perangkat Android nyata (layar kecil, TalkBack, suara TTS, offline end-to-end) dan belum terhubung ke server production.
2. Konten hanya contoh: Matematika kelas 2, 5, 8 (1 bab) beserta langkah kecil dan prasyaratnya. Wajib ditinjau tim kurikulum; kelas dan mapel lain kosong.
3. Sumber kurikulum resmi belum diisi (placeholder berstatus belum diverifikasi).
4. Alat peraga baru 3 jenis (pecahan, nilai tempat, Pythagoras); topik lain belum punya alat peraga.
5. Bacakan memakai TTS bawaan perangkat; jika suara Bahasa Indonesia belum terpasang, Android memakai suara default atau tidak bersuara.
6. "Ulang sebentar" dan "Soal serupa" butuh internet; saat offline anak tetap bisa latihan biasa dari paket offline.
7. Pembayaran/langganan premium belum dibangun (tabel dan entitlement ada; paket diatur manual di database).
8. Retrieval memakai full-text search, belum semantic search (pgvector bisa ditambah).
9. Filter keselamatan berbasis aturan; perlu ditinjau dan diuji berkala.
10. Kunci signing tidak disimpan di GitHub (proxy sesi ini tidak bisa mengatur GitHub Secrets). CI menghasilkan App Bundle tanpa tanda tangan rilis; penandatanganan dilakukan manual dengan `jarsigner`. Untuk otomatisasi, tambahkan secret keystore sendiri lalu tambahkan langkah signing di workflow.
11. Rate limiter berada di memori proses (cukup untuk satu instance API).
12. Media (gambar/audio/video) di materi: tabel tersedia, unggahan belum dibuat di CMS.
13. Kepatuhan UU PDP dan Google Play Families belum diverifikasi ahli hukum. Halaman `/privacy` adalah draf.
14. Ekspor data di aplikasi disalin ke clipboard (belum disimpan sebagai file).
15. Flutter 3.50 menandai `package:flutter/material.dart` deprecated (pindah ke `material_ui`); masih berfungsi.
16. Tag `v1.0.0` dan GitHub Release `v1.0.0` belum dibuat karena sesi pengembangan tidak diizinkan membuat tag/release. Buat manual: `git tag v1.0.0 && git push origin v1.0.0`, lalu unggah berkas dari folder `release\1.0.0`.
