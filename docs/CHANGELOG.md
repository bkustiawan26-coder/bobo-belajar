# Changelog

## 1.0.0 — 2026-11-21
Fitur untuk anak yang tertinggal atau lambat memahami:
- **Ulang sebentar**: soal yang salah dijadwalkan muncul lagi 1, 3, lalu 7 hari kemudian sampai benar.
- **Langkah kecil**: saat salah, anak melihat contoh mirip lalu membuka langkah satu per satu; tombol "Coba lagi" dan "Soal serupa".
- **Jalur pondasi**: jika anak kesulitan di satu topik, BOBO menyarankan topik prasyarat, termasuk dari kelas di bawahnya. Editor CMS bisa mengatur prasyarat.
- **Mode bantuan** (diatur orang tua per anak): sesi pendek 3 soal, huruf lebih besar, pilihan lebih sedikit, bacakan otomatis.
- **Bacakan**: tombol suara di soal, pembahasan, materi, dan jawaban Tutor (TTS bawaan Android, Bahasa Indonesia).
- **Alat peraga interaktif**: pecahan, nilai tempat puluhan–satuan, dan Pythagoras; bisa dibuka dari materi dan Tutor.
- **Tutor menjelaskan ulang** dengan cara lain: cerita, gambar, atau langkah.
- **Kemajuanku**: perkembangan dibandingkan dengan diri sendiri dan lencana usaha.
- **Orang tua**: sinyal "perlu pendampingan" berbasis bukti + rencana 7 hari, ringkasan untuk guru yang bisa dibagikan, grafik pertumbuhan.

Rilis & operasional:
- Halaman kebijakan privasi `/privacy`; pembersihan percakapan AI otomatis 30 hari.
- Ikon aplikasi, signing rilis dengan upload key, App Bundle untuk Play Store, minSdk 24 (Android 7.0+).
- Migrasi database 0002.

## 0.1.0 — 2026-11-21
- Mockup UI/UX interaktif (canvas desain).
- Backend FastAPI: auth orang tua + PIN, profil anak, kurikulum berversi, materi & bank soal dengan review, latihan, asesmen dengan waktu server dan submit idempoten, penguasaan & rekomendasi berbasis bukti, Tutor & Tanya BOBO (provider-independent, safety, RAG full-text), kuota & log biaya, sinkron offline, ekspor & hapus data, audit.
- Aplikasi Flutter Android: mode anak (Home, Belajar, Latihan, Ujian, Tutor) dan mode orang tua (Dashboard, Anak, Perkembangan, Rekomendasi, Tanya BOBO), tema per jenjang, offline + sinkron.
- CMS Next.js: kurikulum & sumber, materi, bank soal, antrean review, asesmen, impor/ekspor, pemakaian AI, prompt, audit.
- Docker Compose dengan backup harian, GitHub Actions (tes backend, build CMS, analisis + tes + APK Flutter).
