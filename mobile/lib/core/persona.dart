int stageOf(int grade) => grade <= 2 ? 0 : grade <= 4 ? 1 : grade <= 6 ? 2 : 3;

class VoiceProfile {
  const VoiceProfile(this.rate, this.pitch, this.pauseMs);

  final double rate;
  final double pitch;
  final int pauseMs;

  static const _all = [VoiceProfile(0.40, 1.25, 600), VoiceProfile(0.43, 1.18, 480), VoiceProfile(0.46, 1.08, 360), VoiceProfile(0.49, 1.00, 280)];

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

const _arabic = '[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+';
const _emoji = r'[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{FE0F}\u{200D}\u{20E3}\u{1F1E6}-\u{1F1FF}]';

const _roman = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9'};

const _idWords = {
  'yang', 'dan', 'di', 'ke', 'dari', 'ini', 'itu', 'adalah', 'untuk', 'dengan', 'kita', 'kamu', 'aku', 'saya', 'tidak', 'ada', 'akan', 'juga',
  'atau', 'karena', 'jadi', 'artinya', 'arti', 'contoh', 'kata', 'kalimat', 'bahasa', 'soal', 'jawab', 'jawaban', 'berapa', 'apa', 'siapa', 'mana',
  'bagaimana', 'mengapa', 'kapan', 'sudah', 'belum', 'lalu', 'kemudian', 'setelah', 'sebelum', 'hari', 'pagi', 'siang', 'malam', 'ibu', 'ayah',
  'kakak', 'adik', 'teman', 'sekolah', 'rumah', 'ayo', 'yuk', 'mari', 'coba', 'ketuk', 'pilih', 'benar', 'salah', 'bagus', 'hebat', 'sekarang',
  'kalau', 'jika', 'bisa', 'harus', 'boleh', 'mau', 'ingin', 'sedang', 'pada', 'dalam', 'sebagai', 'seperti', 'lebih', 'sangat', 'semua', 'setiap',
  'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'berarti', 'menjadi', 'dibaca', 'ditulis', 'maaf',
  'terima', 'kasih', 'selamat', 'nama', 'namaku', 'kucing', 'anjing', 'buku', 'dipakai', 'gunanya', 'bentuk', 'pakai', 'waktu', 'tempat', 'orang',
  'baik', 'besar', 'kecil', 'panjang', 'pendek', 'cara', 'menyapa', 'perhatikan', 'urutan', 'kelompok', 'gambar', 'bagian', 'ya', 'kok', 'lho',
  'nah', 'betul', 'cocok', 'hore', 'yeay', 'keren', 'mantap', 'tepat', 'lagi', 'cari', 'pas', 'hmm', 'ups', 'tos', 'wah', 'tentu', 'dong',
};

bool _idShaped(String w) => (w.length >= 6 && RegExp(r'^(meng|meny|mem|men|ber|ter|per)[a-z]+$').hasMatch(w)) || (w.length >= 5 && RegExp(r'[a-z]+(nya|kan|lah|kah)$').hasMatch(w));

const _enWords = {
  'the', 'a', 'an', 'is', 'are', 'am', 'was', 'were', 'be', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your', 'his', 'her', 'our', 'their',
  'this', 'that', 'these', 'those', 'what', 'where', 'when', 'who', 'why', 'how', 'do', 'does', 'did', 'can', 'will', 'would', 'should', 'must',
  'have', 'has', 'had', 'to', 'of', 'in', 'on', 'at', 'for', 'with', 'and', 'or', 'but', 'not', "don't", "can't", "i'm", "it's", 'yes', 'no',
  'please', 'thank', 'thanks', 'hello', 'hi', 'good', 'morning', 'afternoon', 'evening', 'night', 'name', 'there', 'here', 'very', 'like', 'go',
  'going', 'went', 'some', 'many', 'much', 'every', 'always', 'usually', 'sometimes', 'never', 'today', 'tomorrow', 'yesterday', 'from', 'by',
};

bool looksEnglish(String text, {bool bias = false}) {
  final words = RegExp(r"[a-zA-Z']+").allMatches(text.toLowerCase()).map((m) => m[0]!).toList();
  if (words.isEmpty) {
    return false;
  }
  var en = 0;
  for (final w in words) {
    if (_idWords.contains(w) || _idShaped(w)) {
      return false;
    }
    if (_enWords.contains(w)) {
      en++;
    }
  }
  if (bias) {
    return true;
  }
  return en >= 2 && en * 10 >= words.length * 3;
}

String _time(Match m, bool english) {
  final h = int.parse(m[2]!);
  final mm = int.parse(m[3]!);
  final lead = m[1] ?? '';
  final before = m.input.substring(m.start < 8 ? 0 : m.start - 8, m.start + lead.length);
  final said = RegExp(r'(pukul|jam)\s*$', caseSensitive: false).hasMatch(before);
  if (english) {
    return '$lead$h ${mm == 0 ? "o'clock" : mm < 10 ? 'oh $mm' : '$mm'}';
  }
  final head = said ? '' : 'pukul ';
  return '$lead$head$h${mm == 0 ? '' : ' lewat $mm menit'}';
}

String toSpoken(String raw, {bool english = false}) {
  var s = raw.replaceAll(RegExp(_emoji, unicode: true), ' ').replaceAll(RegExp(_arabic), ' ').replaceAll(' ', ' ').trim();
  if (s.isEmpty) {
    return s;
  }
  s = s.replaceAll('==', ' ⩵ ').replaceAll('!=', ' ≠ ').replaceAll('>=', ' ≥ ').replaceAll('<=', ' ≤ ');
  const units = [
    ('m/s²', ' meter per detik kuadrat'),
    ('km/jam', ' kilometer per jam'),
    ('m/s', ' meter per detik'),
    ('km²', ' kilometer persegi'),
    ('cm²', ' sentimeter persegi'),
    ('m²', ' meter persegi'),
    ('dm³', ' desimeter kubik'),
    ('cm³', ' sentimeter kubik'),
    ('m³', ' meter kubik'),
    ('kWh', ' kilowatt jam'),
    ('Wh', ' watt jam'),
    ('°C', ' derajat Celsius'),
    ('°F', ' derajat Fahrenheit'),
    ('°', ' derajat'),
    ('Ω', ' ohm'),
    ('kHz', ' kilohertz'),
    ('Hz', ' hertz'),
    ('dB', ' desibel'),
    ('mm', ' milimeter'),
    ('cm', ' sentimeter'),
    ('dm', ' desimeter'),
    ('km', ' kilometer'),
    ('kg', ' kilogram'),
    ('mg', ' miligram'),
    ('ml', ' mililiter'),
    ('mL', ' mililiter'),
    ('ha', ' hektare'),
  ];
  for (final (a, b) in units) {
    s = s.replaceAll(RegExp('(?<=[0-9])\\s?${RegExp.escape(a)}(?![A-Za-z0-9²³])'), b);
  }
  s = s.replaceAllMapped(RegExp(r'(?<=[0-9]) (m|g|L|W|V|N|J|A)(?![A-Za-z0-9²³(])'), (m) => ' ${const {'m': 'meter', 'g': 'gram', 'L': 'liter', 'W': 'watt', 'V': 'volt', 'N': 'newton', 'J': 'joule', 'A': 'ampere'}[m[1]]}');
  s = s.replaceAllMapped(RegExp(r'Rp\s?([0-9][0-9.]*)'), (m) => '${m[1]} rupiah').replaceAll(RegExp(r'\bRp\b'), 'rupiah');
  s = s.replaceAllMapped(RegExp(r'(^|[^\d.,])([01]?\d|2[0-3])\.([0-5]\d)(?![\d,]|\.\d)'), (m) => _time(m, english));
  s = s.replaceAllMapped(RegExp(r'(^|[^\d.,])([01]?\d|2[0-3]):([0-5]\d)(?![\d:])(?!\s*=)'), (m) => _time(m, english));
  for (final e in _sub.entries) {
    s = s.replaceAll(e.key, ' ${e.value}');
  }
  s = _superscripts(s);
  s = s.replaceAllMapped(RegExp(r'\b(Hukum Newton|Kelas|Bab|Sila|Amandemen|Fase)\s+(IX|VIII|VII|VI|IV|V|III|II|I)\b'), (m) => '${m[1]} ${_roman[m[2]]}');
  s = s.replaceAllMapped(RegExp(r'\bke-(\d+)'), (m) => 'ke ${m[1]}');
  final abbr = {
    RegExp(r'\bdll\.?'): 'dan lain-lain',
    RegExp(r'\bdsb\.?'): 'dan sebagainya',
    RegExp(r'\bdst\.?'): 'dan seterusnya',
    RegExp(r'\bdkk\.?'): 'dan kawan-kawan',
    RegExp(r'\btsb\.?'): 'tersebut',
    RegExp(r'\bs\.d\.'): 'sampai dengan',
    RegExp(r'\byg\b'): 'yang',
    RegExp(r'\bdgn\b'): 'dengan',
    RegExp(r'\bNo\.\s?(?=\d)'): 'nomor ',
    RegExp(r'\bhlm\.\s?'): 'halaman ',
    RegExp(r'\bMoh\.'): 'Mohammad',
    RegExp(r'\bJl\.'): 'Jalan',
    RegExp(r'\bSWT\b'): 'subhanahu wa taala',
    RegExp(r'\bSAW\b'): 'sallallahu alaihi wasallam',
  };
  for (final e in abbr.entries) {
    s = s.replaceAll(e.key, e.value);
  }
  s = s.replaceAll('√', ' akar ').replaceAll('π', ' pi ').replaceAll('×', ' kali ').replaceAll('÷', ' bagi ').replaceAll('·', ' kali ').replaceAll('⩵', ' sama dengan ');
  s = s.replaceAll('±', ' kurang lebih ').replaceAll('≈', ' kira-kira ').replaceAll('∠', ' sudut ').replaceAll('△', ' segitiga ').replaceAll('&', ' dan ').replaceAll('^', ' pangkat ');
  s = s.replaceAllMapped(RegExp(r'\b([A-Za-z])\(\s*([^()]{1,12}?)\s*\)'), (m) => '${m[1]} ${m[2]} ');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*:\s*(?=\d+\s*=)'), (m) => '${m[1]} bagi ');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*:\s*(?=\d)'), (m) => '${m[1]} banding ');
  s = s.replaceAllMapped(RegExp(r'(?<![\d/,.])([1-3])/([24])(?![\d/])'), (m) => const {'1/2': 'setengah', '1/4': 'seperempat', '3/4': 'tiga perempat', '2/4': 'dua perempat', '1/3': 'sepertiga', '2/3': 'dua pertiga'}['${m[1]}/${m[2]}'] ?? '${m[1]} per ${m[2]}');
  s = s.replaceAllMapped(RegExp(r'(?<![\d/,.])1/3(?![\d/])'), (m) => 'sepertiga').replaceAllMapped(RegExp(r'(?<![\d/,.])2/3(?![\d/])'), (m) => 'dua pertiga');
  s = s.replaceAllMapped(RegExp(r'(\d{4})/(\d{4})'), (m) => '${m[1]} sampai ${m[2]}');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*/\s*(\d)'), (m) => '${m[1]} per ${m[2]}');
  s = s.replaceAllMapped(RegExp(r'([A-Za-z])/([A-Za-z])'), (m) => '${m[1]} atau ${m[2]}');
  s = s.replaceAllMapped(RegExp(r'(^|[\s(=,\[])[−-](?=[0-9a-z(])'), (m) => '${m[1]} negatif ');
  s = s.replaceAll(RegExp(r'\s[−-]\s'), ' kurang ').replaceAll('−', ' kurang ');
  s = s.replaceAll('≠', ' tidak sama dengan ').replaceAll('≤', ' kurang dari atau sama dengan ').replaceAll('≥', ' lebih dari atau sama dengan ');
  s = s.replaceAll('<', ' kurang dari ').replaceAll('>', ' lebih dari ');
  s = s.replaceAll('+', ' tambah ').replaceAll('=', ' sama dengan ').replaceAll('%', ' persen');
  s = s.replaceAll('→', ', jadi ').replaceAll('⇒', ', jadi ').replaceAll('…', ' titik-titik ').replaceAll('...', ' titik-titik ');
  s = s.replaceAllMapped(RegExp(r'(\d)\s*–\s*(\d)'), (m) => '${m[1]} sampai ${m[2]}');
  s = s.replaceAll(' – ', ', ').replaceAll(' — ', ', ').replaceAll('—', ', ').replaceAll('–', ' sampai ');
  s = s.replaceAll(RegExp('[“”"•*_#@\\\$~`]'), ' ').replaceAll(RegExp(r'[()\[\]{}|;:/\\]'), ', ');
  s = s.replaceAll(RegExp(r'\s*,\s*(,\s*)+'), ', ').replaceAllMapped(RegExp(r'\s+([,.!?])'), (m) => m[1]!).replaceAllMapped(RegExp(r',([.!?])'), (m) => m[1]!).replaceAll(RegExp(r'\s{2,}'), ' ').trim();
  s = s.replaceAll(RegExp(r'^[,.\s]+'), '').replaceAll(RegExp(r'[,\s]+$'), '');
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
        0 => 'Hai, $name! Aku BOBO. Hari ini kita belajar $title bareng-bareng. Siap? Yuk!',
        1 => 'Halo, $name! Kita belajar $title, yuk. Cuma sekitar $minutes menit, kok.',
        2 => 'Hai, $name. Topik kita: $title. Sekitar $minutes menit.',
        _ => 'Oke, $name. Topik kali ini: $title. Sekitar $minutes menit.',
      };

  String blockIntro(String kind) {
    const lines = {
      'Penjelasan': ['Yuk, lihat gambarnya dulu, ya!', 'Ayo kita pahami pelan-pelan sambil lihat gambarnya.', 'Kita mulai dari penjelasan dan gambarnya.', 'Penjelasan.'],
      'Contoh': ['Sekarang, kita lihat contohnya, yuk!', 'Ayo lihat contohnya!', 'Perhatikan contoh ini.', 'Contoh.'],
      'Ayo coba': ['Sekarang giliranmu main! Ayo coba, ya.', 'Saatnya mencoba sendiri! Kamu pasti bisa.', 'Ayo coba sendiri.', 'Coba sendiri.'],
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
    return const {'Penjelasan': 'Yuk simak', 'Contoh': 'Lihat contoh', 'Ayo coba': 'Ayo main', 'Poin penting': 'Ingat ini', 'Ringkasan': 'Intinya'}[kind] ?? kind;
  }

  List<String> cheers() => const [
        ['Yeay, kamu berhasil! Hebat!', 'Hore, betul semua! Tos dulu!', 'Keren! Kamu teliti sekali.', 'Wah, berhasil! Usahamu hebat.'],
        ['Mantap, kamu berhasil!', 'Hore, semuanya tepat!', 'Keren, kamu teliti!', 'Berhasil! Usahamu kelihatan.'],
        ['Berhasil! Langkahmu tepat.', 'Tepat semua. Mantap!', 'Bagus, kamu menyelesaikannya.', 'Selesai dengan tepat!'],
        ['Selesai, semua tepat.', 'Tepat.', 'Bagus, selesai.', 'Semua benar.'],
      ][stage];

  String tryAgain() => const ['Ups, belum pas. Tidak apa-apa, coba lagi, ya!', 'Belum pas. Ayo coba lagi!', 'Belum tepat. Coba lagi.', 'Belum tepat.'][stage];

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
