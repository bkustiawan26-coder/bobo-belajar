# Keamanan & Privasi

## Aplikasi Android 1.1.0 (lokal)
- Tanpa izin `INTERNET`: aplikasi tidak bisa mengirim data ke mana pun. Data keluar hanya jika orang tua sendiri membagikan ringkasan guru atau berkas cadangan.
- PIN dan kode pemulihan disimpan sebagai PBKDF2-SHA256 (20.000 iterasi, salt acak 16 byte), dibandingkan dengan waktu konstan. 5x salah → terkunci 15 menit.
- Data di SQLite privat aplikasi (sandbox Android). Berkas cadangan berisi data belajar tanpa PIN; orang tua diingatkan menyimpannya di tempat aman.
- Isi pertanyaan ke Tutor/Tanya BOBO tidak disimpan; hanya waktu, jenis tindakan, dan kategori penolakan.
- Hapus profil menghapus seluruh data anak itu; "Hapus semua data" menghapus PIN, profil, dan riwayat. Kebijakan privasi tersedia di dalam aplikasi.
- Batasan: perangkat yang sudah di-root atau cadangan yang bocor dapat membuka data belajar; enkripsi basis data lokal belum diterapkan.

## Backend server (untuk CMS)
- Kata sandi & PIN: bcrypt (cost 12). PIN wajib untuk membuka mode orang tua; 5x salah → terkunci 15 menit.
- Token JWT HS256 dengan rahasia dari environment (aplikasi menolak start tanpa `BOBO_JWT_SECRET`). Tidak ada rahasia di repo.
- RBAC: orang tua, anak, admin, editor, reviewer. Token anak tidak bisa memanggil endpoint orang tua/admin.
- Isolasi keluarga: setiap akses data anak dicek lewat `guardian_child_links`; anak milik keluarga lain → 404.
- Validasi input (Pydantic), batas panjang teks, batas laju per IP untuk login/refresh/registrasi.
- Header keamanan (`nosniff`, `no-referrer`, CMS `X-Frame-Options: DENY`); dokumentasi API dimatikan di production.
- Audit log untuk login, perubahan profil, PIN, persetujuan, review, publikasi, ekspor, hapus akun.
- Enkripsi in-transit: wajib HTTPS di production (pasang reverse proxy TLS di depan API & CMS). Enkripsi at-rest: gunakan disk/volume terenkripsi di server.

## Privasi anak
- Data minimum: nama panggilan + kelas. Nama panggilan yang berisi angka ditolak.
- Tanpa iklan, tanpa iklan perilaku, tanpa pelacak pihak ketiga.
- Persetujuan orang tua dicatat dengan versi kebijakan (`guardian_consents`).
- Kebijakan privasi publik di `/privacy` milik server (untuk mode server). Aplikasi lokal memakai kebijakan di dalam aplikasi; Google Play tetap meminta URL kebijakan privasi yang bisa diakses publik.
- Fitur suara memakai mesin TTS bawaan Android di perangkat; teks tidak dikirim ke server BOBO.
- Ekspor data (`/parent/export`) dan hapus permanen profil/akun (`/parent/children/{id}`, `/parent/delete-account`) tersedia di aplikasi.

## Kepatuhan
Dirancang dengan memperhatikan UU Pelindungan Data Pribadi Indonesia, perlindungan anak, dan kebijakan Google Play Families. **Belum ada verifikasi hukum.** Sebelum rilis: tinjau kebijakan privasi oleh ahli hukum, isi formulir Data safety dan Target audience Google Play, dan evaluasi persyaratan Families Policy.
