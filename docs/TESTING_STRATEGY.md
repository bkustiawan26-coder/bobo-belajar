# Strategi Pengujian

| Lapisan | Alat | Cakupan |
|---|---|---|
| Backend | pytest + PostgreSQL asli (`backend/tests`) | registrasi & persetujuan, PIN & lockout, isolasi keluarga, token anak vs orang tua, latihan dinilai server, idempotensi jawaban & sinkron, aturan penguasaan & rekomendasi, alur asesmen (skor, submit idempoten, batas waktu, finalisasi otomatis), tutor (sumber, mode petunjuk, penolakan data pribadi, kuota, di luar materi), provider eksternal (biaya, sanitasi, fallback, batas biaya), alur review/publish, impor selalu draft, jadwal ulang 1/3/7 hari, langkah kecil hanya saat salah, prasyarat lintas kelas & tolak lingkaran, pilihan lebih sedikit (kunci tetap benar), sinyal pendampingan, ringkasan guru, pertumbuhan, pembersihan 30 hari |
| Aplikasi | flutter test (`mobile/test`) | penilaian lokal offline, tema per jenjang, komponen aksesibel, logika alat peraga pecahan |
| Statis | flutter analyze, `next build` (TypeScript strict) | error kompilasi & tipe |
| CI | GitHub Actions | ketiga job di setiap push |

Menjalankan backend lokal: `cd backend && pip install -r requirements-dev.txt && BOBO_DATABASE_URL=postgresql+psycopg://bobo:bobo@localhost/bobo_test pytest`.

## Belum otomatis (manual sebelum rilis)
Uji UI di perangkat Android nyata (layar kecil, Android 7–15), uji offline end-to-end, uji aksesibilitas TalkBack, uji penetrasi, uji beban.
