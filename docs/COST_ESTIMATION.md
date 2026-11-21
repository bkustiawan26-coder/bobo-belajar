# Estimasi Biaya (asumsi, belum diverifikasi harga terkini)

| Komponen | Asumsi | Catatan |
|---|---|---|
| Server API + DB + CMS | 1 VPS 2 vCPU / 4 GB | cukup untuk tahap awal ribuan pengguna aktif harian; cek harga penyedia saat membeli |
| Penyimpanan & backup | 20–50 GB | konten teks kecil; media akan menambah |
| Bandwidth | rendah | materi teks, paket offline hanya teks |
| AI mode `grounded` | $0 | default |
| AI provider eksternal | `biaya = token_masuk × harga_masuk + token_keluar × harga_keluar` | isi `BOBO_AI_PRICE_*`; dibatasi kuota per anak + batas harian global |

Contoh rumus: 1.000 siswa aktif × 5 pertanyaan/hari × (1.500 token masuk + 300 token keluar). Kalikan dengan tarif per juta token dari penyedia yang dipilih. Pantau angka nyata di CMS › Impor, AI & audit (biaya per siswa aktif).

Metrik yang dipantau: biaya AI per siswa aktif, penyimpanan, bandwidth, biaya infrastruktur, konversi, retensi, keterlibatan belajar. Pembayaran belum dibangun (lihat KNOWN_ISSUES).
