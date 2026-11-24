# Suara & UX Berdasarkan Tahap Perkembangan Anak (1.3.0)

| | Kelas 1–2 | Kelas 3–4 | Kelas 5–6 | Kelas 7–9 |
|---|---|---|---|---|
| Tahap | operasional konkret awal, baru lancar membaca | operasional konkret, butuh rasa mampu | peralihan ke berpikir abstrak | remaja: otonomi, identitas, peka dianggap "anak kecil" |
| Suara (rate / pitch / jeda) | 0,40 / 1,25 / 600 ms | 0,43 / 1,18 / 480 ms | 0,46 / 1,08 / 360 ms | 0,49 / 1,00 / 280 ms |
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

- **Belajar lewat gambar dan bermain (1.7.0)**: setiap materi dibuka dengan gambar penjelas yang bisa diketuk (BOBO membacakan bagian yang diketuk), lalu langkah "Ayo coba"/"Ayo main" berisi aktivitas singkat yang diturunkan dari gambar (urutkan, kelompokkan, pasangkan, cari gambar, warnai pecahan, susun bilangan, ketuk garis bilangan, pilih jawaban). Salah diberi petunjuk lembut tanpa hukuman, benar diberi pujian usaha dan animasi bintang; aktivitas tidak menghalangi lanjut ke bagian berikutnya.
- **Suara lebih ramah (1.7.0)**: nada suara dinaikkan untuk SD agar terdengar ceria, tempo tetap pelan untuk kelas 1–2, sapaan pembuka lebih hangat, dan emoji tidak ikut dibacakan.
- **Sesi latihan pendek dan suara asli untuk ngaji (1.8.0)**: latihan dibagi 10 soal per sesi (5 untuk sesi pendek) dengan pilihan lanjut atau istirahat, supaya 20 soal per materi tidak terasa berat. Bacaan Al-Qur'an memakai rekaman qari sungguhan dengan sorotan ayat dan ketuk-untuk-mengulang (talaqqi), sedangkan doa memakai suara orang tua sendiri; ikatan dengan suara orang tua membuat hafalan doa lebih hangat, dan suara mesin tidak dipakai untuk bacaan Arab yang menuntut tajwid.

Kode: `mobile/lib/core/persona.dart` (bahasa & profil suara), `mobile/lib/core/speech.dart` (pembacaan per kalimat, sorotan, pilihan suara). Tes: `mobile/test/persona_test.dart`.
Batasan: kualitas suara bergantung mesin TTS di HP; pemetaan simbol bersifat aturan, bisa keliru pada notasi yang jarang. Belum diuji dengan anak/psikolog anak.
