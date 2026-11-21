# Keamanan & Privasi

## Kontrol yang diterapkan
- Kata sandi & PIN: bcrypt (cost 12). PIN wajib untuk membuka mode orang tua; 5x salah → terkunci 15 menit.
- Token JWT HS256 dengan rahasia dari environment (aplikasi menolak start tanpa `BOBO_JWT_SECRET`). Tidak ada rahasia di repo.
- RBAC: orang tua, anak, admin, editor, reviewer. Token anak tidak bisa memanggil endpoint orang tua/admin.
- Isolasi keluarga: setiap akses data anak dicek lewat `guardian_child_links`; anak milik keluarga lain → 404.
- Validasi input (Pydantic), batas panjang teks, batas laju per IP untuk login/refresh/registrasi.
- Header keamanan (`nosniff`, `no-referrer`, CMS `X-Frame-Options: DENY`); dokumentasi API dimatikan di production.
- Audit log untuk login, perubahan profil, PIN, persetujuan, review, publikasi, ekspor, hapus akun.
- Aplikasi Android: token di Encrypted SharedPreferences (flutter_secure_storage); token orang tua hanya di memori saat mode orang tua terbuka.
- Enkripsi in-transit: wajib HTTPS di production (pasang reverse proxy TLS di depan API & CMS). Enkripsi at-rest: gunakan disk/volume terenkripsi di server.

## Privasi anak
- Data minimum: nama panggilan + kelas. Nama panggilan yang berisi angka ditolak.
- Tanpa iklan, tanpa iklan perilaku, tanpa pelacak pihak ketiga.
- Persetujuan orang tua dicatat dengan versi kebijakan (`guardian_consents`).
- Kebijakan privasi publik di `/privacy` (Bahasa Indonesia), ditautkan dari menu Anak di aplikasi. Isi nama pengelola & email kontak lewat environment.
- Fitur suara memakai mesin TTS bawaan Android di perangkat; teks tidak dikirim ke server BOBO.
- Ekspor data (`/parent/export`) dan hapus permanen profil/akun (`/parent/children/{id}`, `/parent/delete-account`) tersedia di aplikasi.

## Kepatuhan
Dirancang dengan memperhatikan UU Pelindungan Data Pribadi Indonesia, perlindungan anak, dan kebijakan Google Play Families. **Belum ada verifikasi hukum.** Sebelum rilis: tinjau kebijakan privasi oleh ahli hukum, isi formulir Data safety dan Target audience Google Play, dan evaluasi persyaratan Families Policy.
