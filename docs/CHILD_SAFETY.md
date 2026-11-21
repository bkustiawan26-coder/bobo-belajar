# Keselamatan Anak

## Tutor anak
| Kategori | Tindakan |
|---|---|
| Meminta data pribadi (alamat, nomor HP, kata sandi, foto, ajakan bertemu) | ditolak, anak diingatkan memberi tahu orang tua |
| Anak menulis nomor HP/alamat/email | ditolak, data tidak diteruskan ke provider |
| Konten dewasa, kekerasan, narkoba | ditolak dengan arahan ke orang dewasa tepercaya |
| Tanda menyakiti diri | jawaban suportif, minta segera bicara dengan orang dewasa tepercaya, sebut 112 |
| Minta jawaban PR/ujian langsung | dipandu langkah demi langkah |
| Di luar materi | dijawab jujur bahwa materi belum tersedia |

Setiap penolakan dicatat di `ai_safety_events` (kategori saja, tanpa isi) dan jumlahnya tampil di menu Anak untuk orang tua. Output provider disaring: URL dibuang, data pribadi disamarkan, konten terlarang diganti.

## Fitur yang sengaja tidak ada
Chat antar pengguna, profil publik, papan peringkat, iklan, unggah foto anak.

## Asisten orang tua
Tidak mendiagnosis atau melabeli anak; pertanyaan diagnosis dialihkan ke profesional. Rekomendasi selalu menyebut dasar datanya, dan "paham" baru dinilai setelah minimal 3 jawaban (5 terakhir, ≥80% benar).

## Batasan
Filter berbasis aturan (regex Bahasa Indonesia). Perlu ditinjau berkala dan diuji dengan kasus baru sebelum rilis.
