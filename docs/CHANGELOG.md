# Changelog

## 1.2.0 — 2026-11-23
Materi dan soal lengkap untuk semua kelas dan mapel di aplikasi:
- Kelas 1–9, 41 mapel (SD 1–4: MAT, BIN, PPK, SBD/IPAS; SD 5–6: + BIG; SMP: MAT, BIN, IPA, IPS, BIG), masing-masing 2 bab × 2 topik.
- 165 materi (penjelasan, contoh, poin penting, ringkasan), 660 soal latihan dengan pembahasan (229 dengan langkah kecil), 41 asesmen lingkup materi (246 soal), 112 relasi prasyarat termasuk lintas kelas untuk jalur pondasi.
- Semua konten adalah draf buatan AI, diperiksa otomatis (kunci jawaban, pilihan, prasyarat), ditandai "draf materi, belum ditinjau guru" di aplikasi. Belum ditinjau guru/tim kurikulum.
- Urutan pilihan jawaban diacak tetap saat seeding agar kunci tidak menumpuk di satu huruf.
- Backend: `python -m app.cli seed --full` (konten masuk sebagai menunggu tinjauan; `--publish-sample` hanya untuk demo).
- Tes baru: validasi konten dan seeding penuh (backend), cakupan paket materi Kelas 1–9 dan konsistensi kunci (aplikasi).

## 1.1.0 — 2026-11-21
Aplikasi berjalan **lokal penuh**, tanpa alamat server, tanpa akun, tanpa internet:
- Mesin belajar di HP (`mobile/lib/local`): penilaian, penguasaan, rekomendasi, ulang terjadwal, jalur pondasi, sinyal pendampingan, ringkasan guru, asesmen ber-waktu, Tutor dan Tanya BOBO lokal dengan filter keselamatan yang sama.
- Materi dibundel ke aplikasi dari paket materi yang diekspor CMS (`/admin/content-bundle`, `app.cli export-bundle`). Konten contoh ditandai di aplikasi.
- Setup baru: persetujuan orang tua → PIN → kode pemulihan. Lupa PIN memakai kode pemulihan.
- Cadangan & pulihkan lewat berkas JSON; hapus profil atau semua data.
- Izin internet dihapus; kebijakan privasi di dalam aplikasi.
- Dihapus: layar alamat server, login/daftar email, sinkron, unduh offline.

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
