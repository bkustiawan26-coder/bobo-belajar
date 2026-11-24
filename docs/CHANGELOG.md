# Changelog

## 1.10.0 — 2026-11-24
Semua kelas kini lengkap 10 topik per semester:
- Kelas 2, 3, 5, 6, 7, 8, dan 9: semua mapel kini 10 topik per semester (943 topik baru), lengkap dengan materi bergambar, aktivitas Ayo coba, 20 latihan per topik, dan SAS yang mencakup semua topik. Total 1.760 materi dan 35.200 soal latihan untuk Kelas 1–9.
- Bacaan Al-Qur'an baru dengan rekaman qari: Al-Qadr, An-Nahl 114, Az-Zalzalah, Al-Humazah, Al-Qari'ah, dan Al-Lahab.
- Bab tambahan disusun setelah bab yang sudah ada sehingga progres belajar anak tidak berubah (ID topik dan materi tetap).
- Lembar SAS cetak diperbarui untuk semua kelas.

## 1.9.0 — 2026-11-24
Logat sesuai bahasa, huruf hijaiyah, dan materi lebih banyak untuk Kelas 1 dan 4:
- Suara per bahasa: kalimat Bahasa Sunda dibacakan dengan suara Sunda (su-ID) dan kalimat Bahasa Inggris dengan suara Amerika (en-US). Kata atau kalimat dalam tanda petik di tengah penjelasan berbahasa Indonesia juga dibacakan dengan suara bahasanya. Jika HP belum punya suara Sunda, aplikasi memakai suara Indonesia.
- Modul huruf hijaiyah (PAI Kelas 1): papan huruf alif sampai ya, harakat fathah, kasrah, dammah, tanwin, bentuk huruf sambung, latihan menulis dengan jari, dan permainan "cari huruf". Huruf Arab tidak dibacakan suara mesin; suara pelafalan dari rekaman ustaz yang dibundel atau direkam orang tua/ustaz di aplikasi.
- Kelas 1 dan Kelas 4: semua mapel kini 10 topik per semester (202 topik baru), lengkap dengan materi bergambar, aktivitas Ayo coba, 20 latihan per topik, dan SAS yang mencakup semua topik. Total 817 materi.
- Bab tambahan disusun setelah bab yang sudah ada sehingga progres belajar anak tidak berubah (ID topik dan materi tetap).
- Generator soal Matematika baru untuk Kelas 1 dan 4 (bilangan sampai 100, jam, hari, bersusun, perkalian, pembagian, pecahan, satuan panjang dan berat, simetri, turus, uang).

## 1.8.0 — 2026-11-24
Latihan lebih banyak, mapel baru, dan bacaan Al-Qur'an dengan suara qari:
- Setiap materi kini punya tepat 20 soal latihan (12.300 soal untuk 615 materi). Latihan dibagi per sesi 10 soal (5 soal bila "Sesi pendek" aktif) dengan tombol "Lanjut" supaya anak tidak lelah.
- Mapel baru Kelas 1–9: Pendidikan Agama Islam (label PA) dan Bahasa Sunda (label Su), masing-masing 8 topik per kelas (4 per semester), lengkap dengan materi bergambar, aktivitas Ayo coba, 20 latihan per topik, dan SAS Ganjil/Genap. Total 88 mapel, 176 SAS (6.880 soal).
- Kartu bacaan Al-Qur'an: teks Arab (rasm Utsmani, huruf Amiri Quran) dengan rekaman qari Syaikh Mishary Rashid Alafasy per ayat, tersimpan di aplikasi (offline). Ayat yang sedang dibaca disorot; ketuk satu ayat untuk mendengarkan dan menirukan berulang. Basmalah diputar sebelum surah yang dimulai dari ayat 1.
- Kartu doa: bacaan latin dan arti, dengan rekaman suara Ayah/Bunda/ustaz yang direkam langsung di HP (izin mikrofon). Arab dan doa tidak pernah dibacakan suara mesin.
- Suara: tanda titik dua tidak lagi terbaca "dollar"; perbaikan pelafalan satuan, derajat, singkatan, dan simbol.
- Pengaturan orang tua baru: "Sembunyikan PAI dan Bahasa Sunda" untuk sekolah yang tidak memakai mapel ini.
- Lembar Soal Latihan SAS cetak (18 PDF) kini memuat PAI dan Bahasa Sunda.

## 1.7.0 — 2026-11-23
Materi kini bergambar dan interaktif, dengan suara yang lebih ramah anak:
- Setiap materi (471) punya gambar penjelas di bagian Penjelasan: diagram alur dan siklus, peta pikiran, perbandingan dua/tiga kelompok, diagram Venn, diagram batang, garis bilangan, pecahan (batang dan lingkaran), nilai tempat, susunan benda, gambar hitung, bangun datar dan ruang berlabel, bidang koordinat dan grafik fungsi, jam analog, kode program, kartu kosakata bergambar, rangkaian listrik, mata angin, timbangan persamaan, dan percakapan. Semua digambar oleh aplikasi, tetap offline.
- Gambar bisa diketuk: BOBO membacakan bagian yang diketuk.
- Langkah baru "Ayo coba" ("Ayo main" untuk kelas 1–2) di setiap materi: aktivitas singkat yang dibuat dari gambarnya, yaitu mengurutkan kartu, mengelompokkan, memasangkan, mencari gambar yang disebut, mewarnai pecahan, menyusun bilangan dengan tombol + dan −, mengetuk letak angka di garis bilangan, memilih jawaban, atau menebak hasil program. Ada petunjuk lembut saat keliru, pujian dan animasi saat berhasil, serta tombol "Main lagi".
- Suara: nada lebih ceria untuk SD (pitch 1,25 kelas 1–2; 1,18 kelas 3–4; 1,08 kelas 5–6), sapaan pembuka lebih hangat, kalimat pengantar tiap bagian lebih ramah, emoji tidak ikut dibacakan.
- Data: kolom `figure` (JSON) di blok materi (migrasi 0003), bank gambar per kelas di `backend/app/seed/full/fig<kelas>.py` dengan validasi format.

## 1.6.0 — 2026-11-23
Format SAS disesuaikan dengan contoh soal SAS Kurikulum Merdeka 2026/2027 yang banyak dipakai sekolah (acuan: websiteedukasi.com):
- SD (Kelas 1–6): 35 soal per SAS = 20 pilihan ganda + 10 isian + 5 uraian.
- SMP (Kelas 7–9): 45 soal per SAS = 35 pilihan ganda + 5 isian + 5 uraian.
- Total 140 SAS berisi 5.500 soal (2.700 soal baru, termasuk 700 uraian dengan contoh jawaban dan poin penting). Soal latihan tetap 2.637.
- Aplikasi: soal uraian dijawab di kotak teks panjang. Nilai dihitung dari PG dan isian; uraian tidak dinilai otomatis dan ditampilkan bersama contoh jawaban di Pembahasan untuk dicocokkan bersama orang tua atau guru.
- Durasi SAS dihitung ulang (2 menit per soal + 3 menit per uraian).
- Lembar Soal Latihan SAS cetak (18 PDF) kini punya Bagian C. Uraian dengan baris jawaban, kisi-kisi dengan kolom nomor uraian, dan kunci berisi contoh jawaban.
- Validasi dan tes mengikuti komposisi baru per jenjang.

## 1.5.0 — 2026-11-23
Sumatif Akhir Semester (SAS) mengikuti format soal latihan SAS Kurikulum Merdeka:
- Setiap mapel di setiap kelas punya SAS Ganjil dan SAS Genap berisi tepat 20 soal: 15 pilihan ganda (A–D) + 5 isian, mencakup semua topik semester itu. Total 140 SAS, 2.800 soal baru.
- Soal asesmen lama (770 soal) dipindah menjadi soal latihan tambahan, sehingga latihan bertambah menjadi 2.637 soal.
- Bahasa Inggris ditambahkan untuk Kelas 3–4 (8 topik per kelas: salam, angka, warna, benda di kelas, keluarga, bagian tubuh, hari, hewan; ungkapan sopan, angka 21–100, bulan, ruangan, buah dan sayur, pakaian, perasaan, olahraga).
- Nama asesmen di aplikasi: "SAS Ganjil (Semester 1)" dan "SAS Genap (Semester 2)".
- Lembar Soal Latihan SAS cetak per kelas (18 PDF: Ganjil/Genap Kelas 1–9) dengan kisi-kisi, lembar soal per mapel, dan kunci jawaban; urutan pilihan sama dengan di aplikasi. Generator: `backend/tools/sas_pdf.py`.
- Validasi baru: setiap SAS wajib 15 PG berpilihan 4 + 5 isian, tanpa soal kembar, dan tidak sama dengan soal latihan.

## 1.4.0 — 2026-11-23
Materi dan latihan Semester 1 dan Semester 2 untuk semua mapel umum Kelas 1–9, mengikuti kurikulum tahun ajaran 2026/2027:
- Acuan: Capaian Pembelajaran Keputusan Kepala BSKAP No. 046/H/KR/2025 (masih berlaku 2026/2027), Keputusan Kepala BKPDM No. 020/2026 (hanya mengubah CP Pendidikan Agama), Permendikdasmen No. 13/2025 (struktur kurikulum, mapel pilihan Koding dan Kecerdasan Artifisial), dan urutan bab buku teks Kurikulum Merdeka Kemendikdasmen.
- Mapel baru: Seni dan Budaya dan PJOK (Kelas 1–9), Pendidikan Pancasila (SMP), Informatika (Kelas 7–9), Koding dan Kecerdasan Artifisial (Kelas 5–9). Total 68 mapel.
- Setiap mapel kini punya bab Semester 1 dan Semester 2. Mapel inti 8–9 topik per tahun; Seni, PJOK, Informatika, KKA 4–8 topik.
- 455 materi, 1.820 soal latihan dengan pembahasan (525 dengan langkah kecil), 136 Asesmen Akhir Semester (770 soal, satu per semester per mapel), 282 relasi prasyarat.
- Aplikasi: pilihan Semester 1/Semester 2 di tab Belajar (otomatis sesuai bulan: Juli–Desember Semester 1, Januari–Juni Semester 2), topik semester berjalan didahulukan di beranda, daftar asesmen diurutkan per semester.
- Pendidikan Agama dan Budi Pekerti belum disertakan: materinya berbeda per agama dan perlu ditinjau guru agama, dan aplikasi tidak menanyakan agama anak.
- Tes diperbarui: validasi minimal 5 soal asesmen per semester, struktur semester di paket materi.

## 1.3.0 — 2026-11-23
Suara dan UX menyesuaikan tahap perkembangan anak (lihat `CHILD_UX_PSYCHOLOGY.md`):
- Suara BOBO per jenjang: kecepatan, nada, dan jeda berbeda untuk Kelas 1–2, 3–4, 5–6, 7–9; dibacakan per kalimat dengan sorotan kalimat yang sedang dibaca.
- Simbol matematika dan satuan diucapkan sebagai kata (kuadrat, akar, bagi/banding, negatif, meter persegi, rupiah, dll.).
- Pembuka materi menyebut nama anak, topik, dan lamanya; label bagian materi ramah anak untuk Kelas 1–2.
- Umpan balik growth mindset per jenjang, warna kuning hangat untuk jawaban belum tepat, dibacakan otomatis; pengakuan 3 benar beruntun; tawaran bantuan setelah 2 kali belum tepat.
- Sapaan sesuai waktu, ringkasan hasil latihan/ujian yang menekankan usaha, pengingat jeda 10/15/20/25 menit.
- Orang tua bisa memilih suara Bahasa Indonesia yang terpasang di HP dan mendengarkan contohnya.
- Profil Kelas 1–2 baru otomatis mengaktifkan "Bacakan otomatis".
- Perbaikan teks: hasil ujian "Tersimpan di HP ini" (sebelumnya menyebut server).

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
