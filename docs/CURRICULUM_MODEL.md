# Model Kurikulum

Hierarki: Jenjang → Kelas → Versi kurikulum → Mata pelajaran → Bab → Topik → (Tujuan pembelajaran, Materi, Soal).

- Semua bisa dikonfigurasi lewat CMS; tidak ada kurikulum yang di-hardcode di aplikasi.
- Hanya satu versi kurikulum aktif. Versi baru bisa disiapkan lalu diaktifkan tanpa mengubah kode.
- Mata pelajaran per kelas berbeda dan bisa ditambah/dinonaktifkan.
- Fase (A–D) diturunkan dari kelas: 1–2 A, 3–4 B, 5–6 C, 7–9 D.

## Sumber resmi
Setiap sumber menyimpan judul, instansi penerbit, nomor dokumen/URL, tanggal terbit, tanggal diambil, versi kurikulum, dan status verifikasi (`unverified`, `verified`, `rejected`). Status `verified` ditolak jika referensi kosong. Tujuan pembelajaran yang ditautkan ke sumber belum terverifikasi berstatus `unverified`.

**Status saat ini:** seed hanya membuat satu sumber placeholder berstatus *belum diverifikasi*. Tidak ada referensi resmi yang dikarang. Tim kurikulum wajib mengisi dokumen resmi sebelum rilis.

## Konten contoh
Seed `--sample` membuat 1 bab Matematika untuk kelas 2, 5, dan 8 (materi, latihan, asesmen) dengan penanda `is_sample` dan sumber "Konten contoh BOBO (wajib ditinjau ulang)". Di produksi konten ini masuk sebagai *menunggu review*. CMS menampilkan peringatan selama konten contoh terbit.

## Alur publikasi
Draft → Kirim review → Disetujui/ditolak peninjau (tidak boleh penulisnya sendiri, kecuali admin) → Terbit (versi naik, snapshot disimpan, diindeks untuk Tutor). Mengubah konten terbit mengembalikannya ke draft dan menariknya dari aplikasi.
