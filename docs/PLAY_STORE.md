# Persiapan Google Play

## Berkas
| Berkas | Untuk |
|---|---|
| `BOBO-Belajar-1.0.0.aab` (ditandatangani upload key) | unggah ke Play Console |
| `BOBO-Belajar-1.0.0-release.apk` | pasang langsung, HTTPS saja |
| `BOBO-Belajar-1.0.0-uji.apk` | uji dengan server lokal (HTTP diizinkan, signing debug) |
| `play-store-icon-512.png` | ikon listing |

Aktifkan **Play App Signing** saat unggah pertama. Upload key (`upload-keystore.jks` + `key.properties`) disimpan di `F:\BOBOCUAN2026\BOBO Belajar\release-signing\`. Jika hilang, upload key bisa direset lewat Play Console, tetapi simpan cadangannya di dua tempat.

## Listing (draf)
- **Nama**: BOBO Belajar
- **Deskripsi singkat** (≤80): Teman belajar SD–SMP: materi, latihan, dan Tutor AI yang aman untuk anak.
- **Deskripsi lengkap**: BOBO Belajar membantu anak Kelas 1–9 belajar sesuai kelasnya. Anak membaca materi bertahap, berlatih dengan pembahasan, dan bertanya ke Tutor yang menjawab dari materi yang sudah ditinjau. Anak yang butuh waktu lebih lama mendapat bantuan: langkah kecil saat salah, soal yang diulang beberapa hari kemudian, jalur pondasi dari kelas sebelumnya, suara pembaca, huruf besar, dan alat peraga interaktif. Orang tua melihat perkembangan berbasis bukti, saran kegiatan di rumah, dan ringkasan yang bisa dibagikan ke guru. Tanpa iklan, tanpa chat antar pengguna, tanpa papan peringkat.
- **Kategori**: Pendidikan. **Kebijakan privasi**: `https://<domain-api>/privacy`.

## Target audience & Families
- Kelompok usia: 6–8, 9–12, 13–15. Aplikasi dirancang untuk anak dan orang tua → wajib mengikuti **Families Policy**.
- Akun dibuat orang tua; anak masuk lewat profil yang dibuat orang tua (tanpa email anak).
- Tidak ada iklan, SDK iklan, analitik pihak ketiga, atau pembelian dalam aplikasi di versi ini.
- Tutor AI: jawaban dibatasi materi, filter keselamatan, kuota harian (lihat `CHILD_SAFETY.md`). Cantumkan fitur AI di deskripsi sesuai kebijakan konten AI Google Play.

## Data safety (isian yang sesuai kode saat ini)
| Data | Dikumpulkan | Tujuan | Dibagikan |
|---|---|---|---|
| Nama & email orang tua | Ya | akun | Tidak |
| Nama panggilan & kelas anak | Ya | fungsi aplikasi | Tidak |
| Aktivitas belajar (jawaban, progres) | Ya | fungsi aplikasi, personalisasi | Tidak |
| Pesan ke Tutor / Tanya BOBO | Ya, dihapus 30 hari | fungsi aplikasi | Ke penyedia AI hanya jika `BOBO_AI_PROVIDER` eksternal diaktifkan |
| Lokasi, kontak, foto, perangkat ID | Tidak | – | – |

Enkripsi in-transit: Ya (HTTPS wajib di APK rilis). Pengguna bisa meminta penghapusan: Ya (hapus profil/akun di aplikasi).

## Sebelum menekan "Kirim untuk ditinjau"
1. Server production berjalan dengan HTTPS, `BOBO_OPERATOR_NAME` dan `BOBO_PRIVACY_CONTACT_EMAIL` terisi.
2. Konten kelas yang diiklankan sudah ditinjau tim kurikulum (konten contoh tidak boleh dipublikasikan sebagai materi resmi).
3. Kebijakan privasi ditinjau ahli hukum (UU PDP).
4. Uji di minimal 2 perangkat nyata (layar kecil, TalkBack, offline) memakai jalur uji internal Play Console.
5. Screenshot 2–8 per jenis perangkat dari aplikasi sungguhan.
