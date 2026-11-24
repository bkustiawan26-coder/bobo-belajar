import 'package:flutter/material.dart';

import '../core/theme.dart';
import '../widgets/common.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});

  static const sections = [
    ('Ringkasnya', 'BOBO Belajar adalah aplikasi lokal. Semua data belajar disimpan di HP ini saja. Aplikasi tidak meminta izin internet dan tidak mengirim data ke server BOBO atau pihak lain.'),
    ('Data yang disimpan di HP', 'PIN orang tua (tersimpan dalam bentuk hash, bukan angka aslinya), kode pemulihan (juga dalam bentuk hash), nama panggilan dan kelas anak, pengaturan bantuan belajar, jawaban latihan dan asesmen, kemajuan membaca materi, jadwal soal ulang, catatan aktivitas, dan jumlah pertanyaan ke Tutor per hari. Isi pertanyaan ke Tutor tidak disimpan.'),
    ('Data yang tidak dikumpulkan', 'Nama lengkap, tanggal lahir, sekolah, foto, lokasi, kontak, nomor HP, email, dan ID perangkat. Tidak ada iklan, pelacak, atau analitik pihak ketiga.'),
    ('Tutor dan Tanya BOBO', 'Jawaban disusun di HP dari materi yang ada di aplikasi, bukan dari layanan AI di internet. Permintaan yang tidak aman (misalnya meminta data pribadi) ditolak, dan jumlah penolakannya ditampilkan ke orang tua.'),
    ('Suara', 'Fitur bacakan memakai mesin suara (TTS) bawaan Android di HP ini.'),
    ('Berbagi dan cadangan', 'Data hanya keluar dari HP jika orang tua sendiri memilih membagikan ringkasan untuk guru atau menyimpan berkas cadangan. Simpan berkas cadangan di tempat aman karena berisi data belajar anak.'),
    ('Menghapus data', 'Orang tua dapat menghapus satu profil anak atau semua data dari menu Anak. Menghapus aplikasi juga menghapus semua data di HP ini.'),
    ('Status konten', 'Materi dan soal Kelas 1–9 (Semester 1 dan 2, mengikuti urutan capaian pembelajaran Kurikulum Merdeka 2025 yang berlaku untuk tahun ajaran 2026/2027) di versi ini adalah draf yang disusun dengan bantuan AI dan diperiksa otomatis, tetapi belum ditinjau guru atau tim kurikulum. Ini bukan materi resmi sekolah dan bukan pengganti buku pelajaran. Hasil latihan dan sinyal pendampingan bukan diagnosis.'),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Kebijakan privasi', style: TextStyle(fontWeight: FontWeight.w800))),
      body: ContentWidth(maxWidth: 720, child: ListView(padding: const EdgeInsets.all(20), children: [
        const Text('Berlaku untuk BOBO Belajar versi lokal (1.7.0), November 2026.', style: TextStyle(fontSize: 13, color: Palette.muted)),
        const SizedBox(height: 12),
        for (final (title, body) in sections) ...[
          Text(title, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
          const SizedBox(height: 6),
          Text(body, style: const TextStyle(fontSize: 14, height: 1.55)),
          const SizedBox(height: 16),
        ],
      ])),
    );
  }
}
