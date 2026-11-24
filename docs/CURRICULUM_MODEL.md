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

## Semester dan mapel (1.4.0, tahun ajaran 2026/2027)
- Setiap bab punya `semester` (1 atau 2). SAS Ganjil/Genap dibuat per mapel per semester, mengikuti format soal SAS Kurikulum Merdeka yang umum dipakai sekolah: SD (Kelas 1–6) 20 PG + 10 isian + 5 uraian, SMP (Kelas 7–9) 35 PG + 5 isian + 5 uraian. Bank soal ada di `backend/app/seed/full/sas<kelas>.py` dan `sasx<kelas>.py`; baris uraian berformat `?topik|soal|contoh jawaban|poin1;poin2`. Aplikasi memilih semester otomatis dari bulan (Juli–Desember = 1, Januari–Juni = 2); anak bisa berpindah semester di tab Belajar.
- Setiap materi berisi 5 bagian: Penjelasan (dengan gambar), Contoh, Ayo coba (aktivitas), Poin penting, Ringkasan. Gambar ditulis per topik di `backend/app/seed/full/fig<kelas>.py` dengan baris `Judul topik :: jenis isi ~ keterangan`, misalnya `flow 🌊 Air laut > ☀️ Menguap > ☁️ Awan`, `compare A = x ; y || B = z`, `table Kepala | Kepala ;; isi | isi`, `line 0..20 step 2 ; jump 4>8`, `frac 3/8`, `place 4682`, `coord A(2,3) ; y=2x+1`, `balance 2x + 3 | 11 | x = 4`. Aktivitas Ayo coba dibuat otomatis dari gambar (`fig.activity`). Validasi menolak gambar yang tidak dikenal, titik di luar garis bilangan, atau materi tanpa gambar.
- Mapel per jenjang: Kelas 1–2 MAT, BIN, PPK, Seni dan Budaya, PJOK; Kelas 3–4 + IPAS, Bahasa Inggris; Kelas 5–6 + Bahasa Inggris, Koding dan KA; Kelas 7–9 MAT, BIN, IPA, IPS, Bahasa Inggris, PPK, Seni dan Budaya, PJOK, Informatika, Koding dan KA.
- Acuan draf konten (wajib dicatat sebagai sumber di CMS saat ditinjau): Keputusan Kepala BSKAP No. 046/H/KR/2025 tentang Capaian Pembelajaran, Keputusan Kepala BKPDM No. 020/2026 (perubahan CP Pendidikan Agama), Permendikdasmen No. 13/2025, dan buku teks Kurikulum Merdeka di buku.kemendikdasmen.go.id.
- Pendidikan Agama Islam (PAI) dan Bahasa Sunda (muatan lokal Jawa Barat) tersedia sejak 1.8.0 untuk Kelas 1–9, 8 topik per kelas, mengikuti urutan buku PAI dan Budi Pekerti Kurikulum Merdeka serta KD Bahasa Sunda Jawa Barat. Bacaan Al-Qur'an memakai figur `quran S:A-B` (hanya ayat yang rekamannya dibundel, daftar di `fig.QURAN`), doa memakai figur `doa Judul | latin | arti`; keduanya ada di blok Contoh dan tidak pernah dibacakan TTS. Agama lain belum tersedia.
- Setiap topik wajib tepat 20 soal latihan (manual ditambah soal turunan gambar dan generator Matematika), divalidasi `validate_all`.
