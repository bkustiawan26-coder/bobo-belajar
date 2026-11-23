# Known Issues & Batasan

1. Aplikasi sudah terkompilasi dan lulus tes otomatis di CI, tetapi belum diuji di perangkat Android nyata (layar kecil, TalkBack, suara TTS, cadangan antar-HP).
2. Materi dan soal Kelas 1–9 semua mapel adalah **draf buatan AI** yang baru diperiksa otomatis (kunci jawaban, pilihan, prasyarat), belum ditinjau guru/tim kurikulum. Urutan mengikuti CP BSKAP 046/2025 dan buku teks Kurikulum Merdeka, tetapi satu topik di aplikasi merangkum beberapa subbab buku; ini bukan pengganti buku pelajaran. Seni dan Budaya, PJOK, Informatika, dan KKA baru 4–8 topik per tahun, sehingga soal SAS-nya berasal dari 2–4 topik saja. Beberapa topik lama (misalnya persamaan kuadrat dan bilangan berpangkat di Kelas 9) di buku Kurikulum Merdeka ada di kelas lain, jadi anggap sebagai pengayaan. Pembagian semester per sekolah bisa berbeda. Ditandai "draf materi" di aplikasi. Tidak ada kunci jawaban resmi sekolah.
16. Pendidikan Agama dan Budi Pekerti belum tersedia (perlu konten per agama yang ditinjau guru agama). Bahasa Inggris Kelas 1–2 dan muatan lokal/bahasa daerah juga belum tersedia. Soal SAS (5.500, termasuk 700 uraian) adalah draf AI. Soal uraian tidak dinilai otomatis di aplikasi: nilai hanya dari PG dan isian, jawaban uraian dicocokkan sendiri dengan contoh jawaban bersama orang tua atau guru. Soal SAS yang diperiksa otomatis untuk format dan kunci, belum ditinjau guru; mohon laporkan soal yang keliru.
3. Materi baru hanya bisa masuk lewat rilis aplikasi baru (paket materi dibundel saat build).
4. Tutor lokal memakai pencarian kata kunci dan menyusun jawaban dari kalimat materi; belum ada model AI di perangkat, jadi jawabannya sederhana dan hanya sebatas materi yang ada.
5. Data hanya ada di satu HP. Jika aplikasi dihapus atau HP hilang tanpa cadangan, data hilang. Belum ada sinkron antar-perangkat.
6. Basis data lokal belum dienkripsi (mengandalkan sandbox Android). Berkas cadangan berupa JSON biasa.
7. Waktu asesmen memakai jam HP; anak yang mengubah jam HP bisa memengaruhi batas waktu.
8. Esai tidak tersedia di mode lokal (tidak ada peninjau); paket materi tidak menyertakan soal esai.
9. Alat peraga baru 3 jenis (pecahan, nilai tempat, Pythagoras).
10. Google Play mewajibkan URL kebijakan privasi publik; teks di dalam aplikasi perlu dipasang juga di halaman web (lihat `PLAY_STORE.md`).
11. Kunci signing tidak disimpan di GitHub (proxy sesi ini tidak bisa mengatur GitHub Secrets). CI menghasilkan App Bundle tanpa tanda tangan rilis; penandatanganan dilakukan manual.
12. Tag dan GitHub Release `v1.0.0`–`v1.6.0` belum dibuat karena sesi pengembangan tidak diizinkan membuat tag/release.
13. Kepatuhan UU PDP dan Google Play Families belum diverifikasi ahli hukum.
14. Flutter 3.50 menandai `package:flutter/material.dart` deprecated (pindah ke `material_ui`); masih berfungsi.
15. Suara bergantung mesin TTS di HP (kualitas berbeda antar merek); jika suara Bahasa Indonesia offline belum terpasang, orang tua perlu memasangnya di pengaturan Android. Gaya bahasa per jenjang disusun dari prinsip psikologi perkembangan, belum divalidasi psikolog anak atau uji dengan anak.
