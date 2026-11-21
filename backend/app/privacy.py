from html import escape

from app.core.config import get_settings


def privacy_html() -> str:
    s = get_settings()
    operator = escape(s.operator_name or "[NAMA PENGELOLA]")
    email = escape(s.privacy_contact_email or "[EMAIL KONTAK PRIVASI]")
    version = escape(s.privacy_policy_version)
    return f"""<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kebijakan Privasi BOBO BELAJAR</title>
<style>body{{font-family:system-ui,sans-serif;max-width:760px;margin:0 auto;padding:24px;line-height:1.6;color:#0f172a}}h1{{font-size:24px}}h2{{font-size:18px;margin-top:28px}}</style></head>
<body>
<h1>Kebijakan Privasi BOBO BELAJAR</h1>
<p>Versi {version}. Pengelola layanan: {operator}. Kontak privasi: {email}.</p>
<h2>Untuk siapa aplikasi ini</h2>
<p>BOBO BELAJAR adalah aplikasi belajar untuk siswa SD dan SMP. Akun dibuat dan dikelola oleh orang tua atau wali. Anak memakai profil yang dibuat orang tua dan tidak membuat akun sendiri.</p>
<h2>Data yang kami kumpulkan</h2>
<ul>
<li>Orang tua: nama, email, kata sandi (disimpan dalam bentuk hash), PIN (hash), catatan persetujuan.</li>
<li>Anak: nama panggilan, kelas, aktivitas belajar (materi yang dibaca, jawaban latihan dan asesmen, nilai), pertanyaan ke Tutor BOBO, dan pengaturan belajar yang dipilih orang tua.</li>
</ul>
<p>Kami tidak meminta nama lengkap, tanggal lahir, sekolah, foto, lokasi, atau kontak anak.</p>
<h2>Untuk apa data dipakai</h2>
<p>Menampilkan materi sesuai kelas, menilai latihan dan asesmen, menyusun status perkembangan dan rekomendasi untuk orang tua, menjalankan Tutor BOBO, menjaga keamanan, dan mengendalikan biaya layanan.</p>
<h2>Yang tidak kami lakukan</h2>
<ul>
<li>Tidak menampilkan iklan dan tidak memakai iklan perilaku.</li>
<li>Tidak menjual data.</li>
<li>Tidak memakai percakapan anak untuk melatih model AI tanpa persetujuan orang tua.</li>
<li>Tidak memberi diagnosis psikologis atau medis.</li>
</ul>
<h2>Pihak ketiga</h2>
<p>Jika pengelola mengaktifkan penyedia AI eksternal, pertanyaan Tutor (tanpa nama anak) dan potongan materi dikirim ke penyedia tersebut untuk membuat jawaban. Permintaan yang berisi data pribadi ditolak sebelum dikirim. Fitur baca suara memakai mesin suara bawaan perangkat.</p>
<h2>Penyimpanan dan keamanan</h2>
<p>Data dikirim melalui koneksi terenkripsi dan disimpan di server pengelola. Percakapan Tutor dihapus otomatis setelah 30 hari. Cadangan database disimpan maksimal 14 hari.</p>
<h2>Hak orang tua</h2>
<p>Melalui Mode Orang Tua, Anda dapat melihat aktivitas anak, menyalin data akun, menghapus profil anak, dan menghapus akun secara permanen. Permintaan lain dapat dikirim ke {email}.</p>
<h2>Perubahan</h2>
<p>Perubahan kebijakan akan diberitahukan di aplikasi sebelum berlaku.</p>
</body></html>"""
