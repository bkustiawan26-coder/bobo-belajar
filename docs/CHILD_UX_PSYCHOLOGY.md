# Suara & UX Berdasarkan Tahap Perkembangan Anak (1.3.0)

| | Kelas 1–2 | Kelas 3–4 | Kelas 5–6 | Kelas 7–9 |
|---|---|---|---|---|
| Tahap | operasional konkret awal, baru lancar membaca | operasional konkret, butuh rasa mampu | peralihan ke berpikir abstrak | remaja: otonomi, identitas, peka dianggap "anak kecil" |
| Suara (rate / pitch / jeda) | 0,40 / 1,10 / 650 ms | 0,43 / 1,05 / 500 ms | 0,46 / 1,00 / 380 ms | 0,49 / 0,97 / 280 ms |
| Gaya bahasa | hangat, kalimat pendek, "yuk", menyebut nama | menyemangati, memuji cara | ramah, menyebut strategi | lugas, setara, tanpa kata kekanakan |
| Bacakan otomatis | aktif saat profil dibuat | pilihan orang tua | pilihan orang tua | pilihan orang tua |
| Pengingat jeda | 10 menit | 15 menit | 20 menit | 25 menit |

Prinsip yang dipakai:
- **Growth mindset**: pujian untuk usaha, ketelitian, dan strategi; tidak pernah memuji/menilai kecerdasan ("pintar", "bodoh" dilarang, dicek tes otomatis).
- **Kesalahan = informasi**: warna kuning hangat dan ikon lampu, bukan merah/✕; kalimat "belum tepat/hampir"; tombol "Ulangi yang belum tepat".
- **Beban kognitif**: suara dibacakan per kalimat dengan jeda; kalimat yang sedang dibaca disorot (membantu anak yang baru belajar membaca); simbol matematika diucapkan sebagai kata (×, ², √, :, −, satuan).
- **Rasa mampu & bantuan tepat waktu**: pengakuan 3 benar beruntun; setelah 2 kali belum tepat, BOBO menawarkan langkah kecil, materi, atau istirahat.
- **Otonomi (SMP)**: kalimat menawarkan pilihan ("lanjut, atau pilih topik lain"), tanpa perbandingan dengan anak lain.
- **Rutinitas**: sapaan sesuai waktu (pagi/siang/sore/malam), pembuka materi menyebut topik dan lamanya.

Kode: `mobile/lib/core/persona.dart` (bahasa & profil suara), `mobile/lib/core/speech.dart` (pembacaan per kalimat, sorotan, pilihan suara). Tes: `mobile/test/persona_test.dart`.
Batasan: kualitas suara bergantung mesin TTS di HP; pemetaan simbol bersifat aturan, bisa keliru pada notasi yang jarang. Belum diuji dengan anak/psikolog anak.
