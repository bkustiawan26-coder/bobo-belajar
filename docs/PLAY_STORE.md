# Persiapan Google Play

## Berkas
| Berkas | Untuk |
|---|---|
| `BOBO-Belajar-1.7.0.aab` (ditandatangani upload key) | unggah ke Play Console |
| `BOBO-Belajar-1.7.0.apk` (ditandatangani upload key) | pasang langsung di HP |
| `play-store-icon-512.png` | ikon listing |

Aktifkan **Play App Signing** saat unggah pertama. Upload key (`upload-keystore.jks` + `key.properties`) disimpan di `F:\BOBOCUAN2026\BOBO Belajar\release-signing\`. Jika hilang, upload key bisa direset lewat Play Console, tetapi simpan cadangannya di dua tempat.

## Listing (draf)
- **Nama**: BOBO Belajar
- **Deskripsi singkat** (≤80): Teman belajar SD–SMP: materi, latihan, dan Tutor AI yang aman untuk anak.
- **Deskripsi lengkap**: BOBO Belajar membantu anak Kelas 1–9 belajar sesuai kelasnya. Anak membaca materi bertahap, berlatih dengan pembahasan, dan bertanya ke Tutor yang menjawab dari materi yang sudah ditinjau. Anak yang butuh waktu lebih lama mendapat bantuan: langkah kecil saat salah, soal yang diulang beberapa hari kemudian, jalur pondasi dari kelas sebelumnya, suara pembaca, huruf besar, dan alat peraga interaktif. Orang tua melihat perkembangan berbasis bukti, saran kegiatan di rumah, dan ringkasan yang bisa dibagikan ke guru. Semua berjalan di HP tanpa internet dan tanpa akun: data anak tidak dikirim ke mana pun. Tanpa iklan, tanpa chat antar pengguna, tanpa papan peringkat.
- **Kategori**: Pendidikan. **Kebijakan privasi**: pasang teks dari layar Kebijakan privasi di aplikasi (`mobile/lib/screens/privacy_screen.dart`) di halaman web publik, misalnya GitHub Pages atau situs pengelola, lalu isi URL-nya.

## Target audience & Families
- Kelompok usia: 6–8, 9–12, 13–15. Aplikasi dirancang untuk anak dan orang tua → wajib mengikuti **Families Policy**.
- Tanpa akun: orang tua membuat PIN dan profil anak di HP; tidak ada email atau data kontak.
- Tidak ada iklan, SDK iklan, analitik pihak ketiga, atau pembelian dalam aplikasi di versi ini.
- Tutor: jawaban disusun di HP dari materi aplikasi (bukan AI generatif di internet), dengan filter keselamatan dan batas harian (lihat `CHILD_SAFETY.md`).

## Data safety (isian yang sesuai kode 1.7.0)
- **Mengumpulkan data pengguna: Tidak.** Aplikasi tidak punya izin internet; semua data disimpan di HP dan tidak dikirim ke developer atau pihak ketiga.
- **Membagikan data: Tidak.** Ringkasan guru dan berkas cadangan hanya dibagikan atas tindakan orang tua sendiri lewat menu bagikan Android.
- Penghapusan data: tersedia di aplikasi (hapus profil / hapus semua data) dan otomatis saat aplikasi dihapus.

## Sebelum menekan "Kirim untuk ditinjau"
1. Kebijakan privasi terpasang di URL publik, dengan nama pengelola dan email kontak.
2. Konten 1.7.0 masih draf buatan AI yang belum ditinjau guru. Jangan iklankan sebagai materi resmi/sesuai kurikulum sebelum ditinjau; deskripsi listing harus menyebut "draf materi".
3. Kebijakan privasi ditinjau ahli hukum (UU PDP).
4. Uji di minimal 2 perangkat nyata (layar kecil, TalkBack, offline) memakai jalur uji internal Play Console.
5. Screenshot 2–8 per jenis perangkat dari aplikasi sungguhan.
