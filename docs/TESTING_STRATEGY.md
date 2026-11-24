# Strategi Pengujian

| Lapisan | Alat | Cakupan |
|---|---|---|
| Backend | pytest + PostgreSQL asli (`backend/tests`) | registrasi & persetujuan, PIN & lockout, isolasi keluarga, token anak vs orang tua, latihan dinilai server, idempotensi jawaban & sinkron, aturan penguasaan & rekomendasi, alur asesmen (skor, submit idempoten, batas waktu, finalisasi otomatis), tutor (sumber, mode petunjuk, penolakan data pribadi, kuota, di luar materi), provider eksternal (biaya, sanitasi, fallback, batas biaya), alur review/publish, impor selalu draft, jadwal ulang 1/3/7 hari, langkah kecil hanya saat salah, prasyarat lintas kelas & tolak lingkaran, pilihan lebih sedikit (kunci tetap benar), sinyal pendampingan, ringkasan guru, pertumbuhan, pembersihan 30 hari |
| Aplikasi | flutter test (`mobile/test`) | mesin lokal dengan paket materi asli: PIN & kunci 5x, kode pemulihan, validasi & batas profil, katalog & hak akses materi, latihan tanpa kunci, jadwal ulang 1/3/7 hari, penguasaan & rekomendasi (status selesai direset saat bukti berubah), pondasi lintas kelas, sinyal & ringkasan guru, pilihan lebih sedikit, asesmen (simpan, kumpulkan sekali, batas waktu, finalisasi otomatis), tutor lokal (sumber, gaya, penolakan data pribadi, batas harian), Tanya BOBO menolak diagnosis, cadangan & pulihkan, hapus profil/semua data; kartu bacaan Al-Qur'an, kartu doa, papan hijaiyah dan aktivitas cari huruf (tanpa TTS); pemilihan suara Sunda/Inggris per kalimat dan kutipan; penilaian, tema, komponen, alat peraga |
| Paket materi | pytest `test_bundle.py` | hanya konten terbit (atau contoh jika diminta), tanpa esai, relasi valid, hanya editor/admin |
| Gambar & aktivitas | pytest `test_figures.py`, flutter `figures_test.dart` | setiap materi punya gambar dan aktivitas, format gambar ditolak bila salah, semua jenis gambar (26) dan aktivitas (10) tampil tanpa galat di layar 320 dan 800 px, interaksi urutkan/pilih/kelompokkan sampai pujian |
| Konten Kelas 1–9 | pytest `test_full_content.py`, flutter `content_bundle_test.dart` | validasi kunci/pilihan/prasyarat, acak pilihan tetap benar, seeding 1.760 materi & 176 SAS, tiap topik tepat 20 soal latihan, bacaan Al-Qur'an hanya untuk ayat yang audionya tersedia, tiap mapel punya bab Semester 1 & 2 dan SAS per semester tepat SD 20 PG (4 pilihan) + 10 isian + 5 uraian atau SMP 35 PG + 5 isian + 5 uraian, uraian punya contoh jawaban dan poin penting, uraian tidak ikut skor, tanpa soal kembar atau sama dengan latihan, tiap kelas punya materi-latihan-asesmen, tiap kunci lulus penilaian |
| Suara & persona | flutter `persona_test.dart` | simbol diucapkan benar, pemenggalan kalimat, profil suara per jenjang, larangan pujian kecerdasan, nada SMP tidak kekanakan, Kelas 1–2 dibacakan otomatis |
| Statis | flutter analyze, `next build` (TypeScript strict) | error kompilasi & tipe |
| CI | GitHub Actions | ketiga job di setiap push |

Menjalankan backend lokal: `cd backend && pip install -r requirements-dev.txt && BOBO_DATABASE_URL=postgresql+psycopg://bobo:bobo@localhost/bobo_test pytest`.

## Belum otomatis (manual sebelum rilis)
Uji UI di perangkat Android nyata (layar kecil, Android 7–15), uji aksesibilitas TalkBack, uji cadangan/pulihkan antar-HP, uji performa dengan riwayat jawaban besar.
