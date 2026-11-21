# Known Issues & Batasan

1. Aplikasi sudah terkompilasi dan lulus tes otomatis di CI, tetapi belum diuji di perangkat Android nyata (layar kecil, TalkBack, suara TTS, cadangan antar-HP).
2. Konten hanya contoh: Matematika kelas 2, 5, 8 (1 bab) dan masih menunggu tinjauan tim kurikulum. Ditandai "materi contoh" di aplikasi. Kelas dan mapel lain kosong.
3. Materi baru hanya bisa masuk lewat rilis aplikasi baru (paket materi dibundel saat build).
4. Tutor lokal memakai pencarian kata kunci dan menyusun jawaban dari kalimat materi; belum ada model AI di perangkat, jadi jawabannya sederhana dan hanya sebatas materi yang ada.
5. Data hanya ada di satu HP. Jika aplikasi dihapus atau HP hilang tanpa cadangan, data hilang. Belum ada sinkron antar-perangkat.
6. Basis data lokal belum dienkripsi (mengandalkan sandbox Android). Berkas cadangan berupa JSON biasa.
7. Waktu asesmen memakai jam HP; anak yang mengubah jam HP bisa memengaruhi batas waktu.
8. Esai tidak tersedia di mode lokal (tidak ada peninjau); paket materi tidak menyertakan soal esai.
9. Alat peraga baru 3 jenis (pecahan, nilai tempat, Pythagoras).
10. Google Play mewajibkan URL kebijakan privasi publik; teks di dalam aplikasi perlu dipasang juga di halaman web (lihat `PLAY_STORE.md`).
11. Kunci signing tidak disimpan di GitHub (proxy sesi ini tidak bisa mengatur GitHub Secrets). CI menghasilkan App Bundle tanpa tanda tangan rilis; penandatanganan dilakukan manual.
12. Tag dan GitHub Release `v1.0.0`/`v1.1.0` belum dibuat karena sesi pengembangan tidak diizinkan membuat tag/release.
13. Kepatuhan UU PDP dan Google Play Families belum diverifikasi ahli hukum.
14. Flutter 3.50 menandai `package:flutter/material.dart` deprecated (pindah ke `material_ui`); masih berfungsi.
