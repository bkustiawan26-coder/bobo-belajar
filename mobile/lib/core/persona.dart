int stageOf(int grade) => grade <= 2 ? 0 : grade <= 4 ? 1 : grade <= 6 ? 2 : 3;

class VoiceProfile {
  const VoiceProfile(this.rate, this.pitch, this.pauseMs);

  final double rate;
  final double pitch;
  final int pauseMs;

  static const _all = [VoiceProfile(0.40, 1.10, 650), VoiceProfile(0.43, 1.05, 500), VoiceProfile(0.46, 1.00, 380), VoiceProfile(0.49, 0.97, 280)];

  static VoiceProfile forGrade(int grade) => _all[stageOf(grade)];
}

List<String> segmentsOf(String text) {
  final out = <String>[];
  final buf = StringBuffer();
  for (var i = 0; i < text.length; i++) {
    final ch = text[i];
    buf.write(ch);
    final next = i + 1 < text.length ? text[i + 1] : '';
    final end = ch == '\n' || ('.!?'.contains(ch) && (next == ' ' || next == '\n' || next.isEmpty));
    if (end) {
      while (i + 1 < text.length && text[i + 1] == ' ') {
        buf.write(' ');
        i++;
      }
      out.add(buf.toString());
      buf.clear();
    }
  }
  if (buf.isNotEmpty) {
    out.add(buf.toString());
  }
  final merged = <String>[];
  for (final s in out) {
    if (s.trim().isEmpty && merged.isNotEmpty) {
      merged[merged.length - 1] += s;
    } else {
      merged.add(s);
    }
  }
  return merged;
}

const _sup = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', 'ⁿ': 'n', '⁺': ' tambah ', '⁻': ' kurang ', 'ˣ': ' kali ', 'ᵐ': 'm'};
const _sub = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'};

String _superscripts(String s) => s.replaceAllMapped(RegExp('[${_sup.keys.join()}]+'), (m) {
      final run = m[0]!;
      if (run == '²') {
        return ' kuadrat ';
      }
      if (run == '³') {
        return ' pangkat tiga ';
      }
      return ' pangkat ${run.split('').map((c) => _sup[c]).join()} ';
    });

String toSpoken(String raw) {
  var s = raw.trim();
  if (s.isEmpty) {
    return s;
  }
  const units = [
    ('m/s²', ' meter per detik kuadrat'),
    ('km/jam', ' kilometer per jam'),
    ('cm²', ' sentimeter persegi'),
    ('m²', ' meter persegi'),
    ('cm³', ' sentimeter kubik'),
    ('m³', ' meter kubik'),
    ('kWh', ' kilowatt jam'),
    ('Wh', ' watt jam'),
    ('°C', ' derajat Celsius'),
    ('°', ' derajat'),
    ('Ω', ' ohm'),
  ];
  for (final (a, b) in units) {
    s = s.replaceAll(RegExp('(?<=[0-9 ])${RegExp.escape(a)}(?![A-Za-z])'), b);
  }
  s = s.replaceAllMapped(RegExp(r'Rp\s?([0-9][0-9.]*)'), (m) => '${m[1]} rupiah');
  for (final e in _sub.entries) {
    s = s.replaceAll(e.key, ' ${e.value}');
  }
  s = _superscripts(s);
  s = s.replaceAll('√', ' akar ').replaceAll('π', ' pi ').replaceAll('×', ' kali ').replaceAll('÷', ' bagi ');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*:\s*(?=\d+\s*=)'), (m) => '${m[1]} bagi ');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*:\s*(?=\d)'), (m) => '${m[1]} banding ');
  s = s.replaceAllMapped(RegExp(r'(\d)/(\d)'), (m) => '${m[1]} per ${m[2]}');
  s = s.replaceAllMapped(RegExp(r'(^|[\s(=,])[−-](?=[0-9a-z(])'), (m) => '${m[1]} negatif ');
  s = s.replaceAll(RegExp(r'\s[−-]\s'), ' kurang ').replaceAll('−', ' kurang ');
  s = s.replaceAll('≠', ' tidak sama dengan ').replaceAll('≤', ' kurang dari atau sama dengan ').replaceAll('≥', ' lebih dari atau sama dengan ');
  s = s.replaceAll(RegExp(r'\s<\s'), ' kurang dari ').replaceAll(RegExp(r'\s>\s'), ' lebih dari ');
  s = s.replaceAll('+', ' tambah ').replaceAll('=', ' sama dengan ').replaceAll('%', ' persen');
  s = s.replaceAll('→', ', jadi ').replaceAll('…', ' titik-titik ').replaceAll('...', ' titik-titik ');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*–\s*(\d)'), (m) => '${m[1]} sampai ${m[2]}');
  s = s.replaceAll(' – ', ', ').replaceAll(' — ', ', ').replaceAll('—', ', ').replaceAll('–', ' ke ');
  s = s.replaceAll(RegExp('[“”"•*_]'), ' ').replaceAll(RegExp(r'[()]'), ', ');
  s = s.replaceAll(RegExp(r'\s*,\s*(,\s*)+'), ', ').replaceAll(RegExp(r'\s+([,.!?])'), r'$1').replaceAll(RegExp(r'\s{2,}'), ' ').trim();
  s = s.replaceAll(RegExp(r'^,\s*'), '');
  return s;
}

class Persona {
  const Persona._(this.stage);

  final int stage;

  static Persona forGrade(int grade) => Persona._(stageOf(grade));

  bool get young => stage == 0;
  bool get teen => stage == 3;

  int get breakMinutes => const [10, 15, 20, 25][stage];

  static String _pick(List<String> xs, int seed) => xs[seed.abs() % xs.length];

  String _daypart(int hour) => hour < 11 ? 'pagi' : hour < 15 ? 'siang' : hour < 18 ? 'sore' : 'malam';

  String greeting(String name, int hour) {
    final d = _daypart(hour);
    return switch (stage) {
      0 => 'Selamat $d, $name!',
      1 => 'Selamat $d, $name!',
      2 => 'Hai, $name! Selamat $d.',
      _ => '${d[0].toUpperCase()}${d.substring(1)}, $name.',
    };
  }

  String homeNudge(String name, String? lessonTitle) {
    if (lessonTitle == null) {
      return switch (stage) {
        0 => 'Pilih pelajaran yang kamu suka, yuk, $name!',
        1 => 'Mau mulai dari pelajaran apa hari ini?',
        2 => 'Pilih topik yang ingin kamu pelajari hari ini.',
        _ => 'Pilih sendiri topik yang mau kamu kerjakan.',
      };
    }
    final t = lessonTitle.toLowerCase();
    return switch (stage) {
      0 => 'Yuk, lanjut belajar $t bareng BOBO!',
      1 => 'Lanjut belajar $t? Sedikit lagi selesai.',
      2 => 'Kamu terakhir belajar $t. Lanjut dari situ?',
      _ => 'Terakhir: $t. Lanjut, atau pilih topik lain.',
    };
  }

  String lessonIntro(String name, String title, int minutes) => switch (stage) {
        0 => 'Hai, $name! Hari ini kita belajar $title. Dengarkan pelan-pelan, ya.',
        1 => 'Halo, $name. Kita belajar $title. Cuma sekitar $minutes menit.',
        2 => 'Hai, $name. Topik kita: $title. Sekitar $minutes menit.',
        _ => 'Oke, $name. Topik kali ini: $title. Sekitar $minutes menit.',
      };

  String blockIntro(String kind) {
    const lines = {
      'Penjelasan': ['Yuk, kita simak.', 'Pertama, kita pahami dulu.', 'Kita mulai dari penjelasannya.', 'Penjelasan.'],
      'Contoh': ['Sekarang, lihat contohnya.', 'Ayo lihat contohnya.', 'Perhatikan contoh ini.', 'Contoh.'],
      'Poin penting': ['Ini yang perlu kamu ingat.', 'Ingat tiga hal ini, ya.', 'Poin pentingnya begini.', 'Poin penting.'],
      'Ringkasan': ['Jadi, intinya begini.', 'Jadi, kesimpulannya begini.', 'Ringkasnya begini.', 'Ringkasan.'],
    };
    final l = lines[kind];
    return l == null ? '$kind.' : l[stage];
  }

  String blockLabel(String kind) {
    if (stage > 0) {
      return kind;
    }
    return const {'Penjelasan': 'Yuk simak', 'Contoh': 'Lihat contoh', 'Poin penting': 'Ingat ini', 'Ringkasan': 'Intinya'}[kind] ?? kind;
  }

  String lessonDone() => switch (stage) {
        0 => 'Kamu sudah selesai belajar! Sekarang coba latihannya, yuk.',
        1 => 'Materi selesai. Ayo coba latihannya!',
        2 => 'Materi selesai. Coba latihan untuk mengecek pemahamanmu.',
        _ => 'Materi selesai. Lanjut latihan untuk mengecek pemahaman.',
      };

  String correct(int seed) => _pick(const [
        ['Yeay, benar! Kamu teliti sekali.', 'Betul! Kamu mau berusaha, keren.', 'Benar! Kamu membaca soalnya dengan baik.', 'Tepat! Ayo lanjut pelan-pelan.'],
        ['Benar! Caramu tepat.', 'Betul! Kamu teliti membaca soalnya.', 'Mantap, benar! Usahamu kelihatan.', 'Benar! Langkahmu sudah pas.'],
        ['Benar. Strategimu berhasil.', 'Tepat! Langkahmu sudah runtut.', 'Benar. Ketelitianmu membuahkan hasil.', 'Betul. Caramu masuk akal.'],
        ['Benar.', 'Tepat. Langkahmu konsisten.', 'Benar, cara berpikirmu sudah tepat.', 'Benar. Lanjut.'],
      ][stage], seed);

  String wrong(int seed) => _pick(const [
        ['Hampir! Tidak apa-apa, kita lihat bareng, ya.', 'Belum tepat. Salah itu biasa, kita coba lagi.', 'Ups, belum pas. Ayo lihat caranya pelan-pelan.'],
        ['Belum tepat. Lihat pembahasannya, lalu coba lagi.', 'Hampir benar. Dari kesalahan, otak kita belajar.', 'Belum pas, tidak apa-apa. Kita cari bagian yang terlewat.'],
        ['Belum tepat. Cek lagi langkahmu satu per satu.', 'Belum tepat. Ini kesempatan untuk tahu bagian yang perlu diperkuat.', 'Hampir. Bandingkan jawabanmu dengan pembahasan.'],
        ['Belum tepat. Cek pembahasan untuk melihat bedanya.', 'Belum tepat. Wajar, bagian ini sering terlewat.', 'Belum. Bandingkan langkahmu dengan pembahasan.'],
      ][stage], seed);

  String streak() => const [
        'Tiga kali benar berturut-turut! Kamu fokus sekali.',
        'Tiga benar berturut-turut. Fokusmu bagus!',
        'Tiga benar berturut-turut. Konsisten!',
        'Tiga benar beruntun. Konsisten.',
      ][stage];

  String struggle() => const [
        'Soal ini memang menantang. Mau lihat langkah kecil dulu, atau istirahat sebentar?',
        'Soal ini cukup sulit. Coba buka langkah kecil, atau baca lagi materinya.',
        'Bagian ini menantang. Langkah kecil atau materi bisa membantu sebelum mencoba lagi.',
        'Dua kali belum tepat. Coba lihat langkah kecil atau materi, lalu ulangi.',
      ][stage];

  String correctAnswerSpoken(String answer) => stage == 0 ? 'Jawaban yang benar adalah $answer.' : 'Jawaban benar: $answer.';

  String summary(int right, int total) {
    if (total > 0 && right == total) {
      return const ['Semua benar! Kamu berusaha dengan sungguh-sungguh.', 'Semua benar! Usahamu terbayar.', 'Semua benar. Pemahamanmu sudah kuat di topik ini.', 'Semua benar.'][stage];
    }
    if (right * 2 >= total) {
      return const [
        'Bagus! Yang belum tepat bisa kita ulang bareng.',
        'Bagus! Ulangi yang belum tepat supaya makin paham.',
        'Sebagian besar benar. Ulangi yang belum tepat untuk menguatkan.',
        'Sebagian besar benar. Ulangi yang belum tepat untuk menguatkan.',
      ][stage];
    }
    return const [
      'Kamu sudah mencoba semuanya, itu hebat. Yuk baca lagi materinya, lalu coba lagi.',
      'Kamu sudah berusaha. Baca lagi materinya, lalu coba lagi, pasti makin bisa.',
      'Belum banyak yang tepat, dan itu wajar di awal. Baca ulang materinya, lalu coba lagi.',
      'Belum banyak yang tepat, normal di awal. Baca ulang materinya, lalu coba lagi.',
    ][stage];
  }

  String breakTitle() => const ['Waktunya istirahat!', 'Istirahat sebentar, yuk', 'Saatnya jeda sejenak', 'Jeda sebentar?'][stage];

  String breakBody(int minutes) => switch (stage) {
        0 => 'Kamu sudah belajar $minutes menit. Hebat! Ayo minum air, lalu regangkan badan.',
        1 => 'Kamu sudah belajar $minutes menit. Minum air atau jalan sebentar supaya segar lagi.',
        2 => 'Sudah $minutes menit belajar. Istirahat 5 menit membantu otak menyimpan yang baru dipelajari.',
        _ => 'Sudah $minutes menit fokus. Jeda 5 menit membantu otak menyimpan yang baru dipelajari.',
      };

  String voicePreview(String name) => switch (stage) {
        0 => 'Hai, $name! Aku BOBO. Yuk, kita belajar bareng!',
        1 => 'Halo, $name. Aku BOBO, teman belajarmu.',
        2 => 'Hai, $name. Aku BOBO. Siap belajar hari ini?',
        _ => 'Halo, $name. Ini suara BOBO.',
      };
}
