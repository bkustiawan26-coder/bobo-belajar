import 'content.dart';

class SafetyVerdict {
  const SafetyVerdict(this.category, this.action, this.reply);

  final String? category;
  final String action;
  final String? reply;
}

final List<(String, RegExp)> _patterns = [
  ('self_harm', RegExp(r'\b(bunuh diri|ingin mati|pengen mati|mau mati aja|menyakiti diri|melukai diri|nyakitin diri)\b')),
  ('personal_info_request', RegExp(r'(alamat(mu| kamu| rumah)|rumahmu|nomor (hp|telepon|wa)|no\.? ?hp|whatsapp|password|kata sandi|\bpin\b|kirim foto|foto kamu|ketemuan|bertemu langsung|kopdar)')),
  ('adult', RegExp(r'\b(seks|sex|porno|bokep|telanjang|bugil|ngewe|mesum)\b')),
  ('violence', RegExp(r'\b(cara membunuh|bikin bom|membuat bom|senjata api|merakit senjata|menusuk orang)\b')),
  ('drugs', RegExp(r'\b(narkoba|sabu|ganja|cara mabuk|beli obat terlarang)\b')),
  ('homework_dump', RegExp(r'((jawaban|kunci)\s.*(pr|tugas|ujian))|kerjain pr|kerjakan pr(ku)?|contekan|nyontek|langsung jawabannya')),
];

final RegExp _piiShare = RegExp(r'(\b0?8\d{8,11}\b|\+62\s?\d{8,12}|\b\d{16}\b|alamat(ku| saya| rumahku)?\s+(di|jl|jalan)|@\w+\.(com|id|co))');
final RegExp _diagnosis = RegExp(r'(disleksia|diskalkulia|adhd|autis|autisme|gangguan (belajar|konsentrasi|mental)|diagnos|bodoh|malas|lambat belajar|\biq\b|keterbelakangan)');
final RegExp _url = RegExp(r'https?://\S+');

const Map<String, String> _childReplies = {
  'self_harm': 'Terima kasih sudah cerita. Perasaanmu penting. Tolong segera bicara dengan orang dewasa yang kamu percaya, seperti ayah, ibu, guru, atau keluargamu, sekarang juga. Kalau kamu merasa tidak aman, minta orang dewasa di dekatmu untuk menghubungi layanan darurat 112.',
  'personal_info_request': 'Itu informasi pribadi. Jangan bagikan alamat, nomor HP, kata sandi, atau foto ke siapa pun di aplikasi, termasuk ke BOBO. Kalau ada yang memintanya, ceritakan ke orang tuamu.\n\nYuk, kembali ke pelajaran!',
  'pii_share': 'Sepertinya kamu menulis informasi pribadi. Jangan tulis nomor HP, alamat, atau data pribadi lain di sini, ya. BOBO tidak membutuhkannya.\n\nAda yang mau kamu tanyakan tentang pelajaran?',
  'adult': 'BOBO hanya membahas pelajaran sekolah. Pertanyaan seperti itu sebaiknya kamu tanyakan ke orang tua atau guru yang kamu percaya.\n\nYuk, kembali ke materi!',
  'violence': 'BOBO tidak bisa membantu hal yang bisa membahayakan orang lain. Kalau ada yang membuatmu takut atau tidak aman, ceritakan ke orang dewasa yang kamu percaya.',
  'drugs': 'BOBO tidak membahas hal itu. Kalau kamu punya pertanyaan atau kekhawatiran, bicarakan dengan orang tua atau guru yang kamu percaya.',
  'homework_dump': 'Aku tidak memberi jawaban PR atau ujian secara langsung, tapi aku bisa memandu langkah demi langkah. Ketik soalnya, lalu kita kerjakan bersama.',
};

SafetyVerdict checkChildInput(String text) {
  final t = text.toLowerCase();
  for (final (cat, pat) in _patterns) {
    if (pat.hasMatch(t)) {
      return SafetyVerdict(cat, cat == 'homework_dump' ? 'guide' : 'refuse', _childReplies[cat]);
    }
  }
  if (_piiShare.hasMatch(t)) {
    return SafetyVerdict('pii_share', 'refuse', _childReplies['pii_share']);
  }
  return const SafetyVerdict(null, 'allow', null);
}

SafetyVerdict checkParentInput(String text, String childName) {
  final t = text.toLowerCase();
  if (_diagnosis.hasMatch(t)) {
    return SafetyVerdict('diagnosis', 'redirect',
        'BOBO tidak memberi diagnosis atau label tentang $childName. Data di aplikasi hanya berisi hasil latihan dan asesmen, yang tidak cukup untuk menyimpulkan kondisi belajar, psikologis, atau medis.\n\nJika Anda khawatir, bicarakan dengan guru kelas, psikolog, atau dokter anak. Untuk pelajaran sehari-hari, saya bisa membantu menyusun latihan yang sesuai.');
  }
  if (_patterns.first.$2.hasMatch(t)) {
    return const SafetyVerdict('self_harm', 'redirect', 'Jika Anda atau anak Anda dalam bahaya atau berpikir untuk menyakiti diri, segera hubungi layanan darurat 112 atau tenaga kesehatan terdekat. BOBO hanya membantu urusan belajar dan tidak dapat menggantikan bantuan profesional.');
  }
  return const SafetyVerdict(null, 'allow', null);
}

String cleanOutput(String text, int maxChars) {
  var out = text.replaceAll(_url, '').trim();
  if (_piiShare.hasMatch(out.toLowerCase())) {
    out = out.replaceAll(_piiShare, '[disembunyikan]');
  }
  for (final (_, pat) in _patterns.take(5)) {
    if (pat.hasMatch(out.toLowerCase())) {
      return 'Maaf, BOBO tidak bisa menjawab itu. Yuk, kembali ke materi pelajaran.';
    }
  }
  if (out.length > maxChars) {
    final cut = out.substring(0, maxChars);
    final dot = [cut.lastIndexOf('. '), cut.lastIndexOf('\n')].reduce((a, b) => a > b ? a : b);
    out = (dot > maxChars ~/ 2 ? cut.substring(0, dot + 1) : cut).trim();
  }
  return out;
}

class Passage {
  Passage(this.title, this.content, this.sourceType, this.topicId, this.topic, this.priority);

  final String title;
  final String content;
  final String sourceType;
  final int? topicId;
  final String? topic;
  final int priority;
  double rank = 0;
}

List<String> _chunks(String text, {int size = 700}) {
  final paras = text.split('\n\n').map((p) => p.trim()).where((p) => p.isNotEmpty);
  final out = <String>[];
  var cur = '';
  for (final p in paras) {
    if (cur.isNotEmpty && cur.length + p.length + 2 > size) {
      out.add(cur);
      cur = p;
    } else {
      cur = cur.isEmpty ? p : '$cur\n\n$p';
    }
  }
  if (cur.isNotEmpty) {
    out.add(cur);
  }
  return out.isEmpty ? [text.length > size ? text.substring(0, size) : text] : out;
}

class KnowledgeIndex {
  KnowledgeIndex(Content content) {
    for (final l in content.lessons) {
      final tid = (l['topic_id'] as num).toInt();
      final grade = content.gradeOfTopic(tid);
      if (grade == null) {
        continue;
      }
      final parts = <String>[l['title'] as String];
      for (final b in (l['blocks'] as List? ?? const [])) {
        final m = Map<String, dynamic>.from(b as Map);
        if (m['text'] != null && (m['text'] as String).isNotEmpty) {
          parts.add('${m['kind']}: ${m['text']}');
        }
        final pts = m['points'] as List?;
        if (pts != null && pts.isNotEmpty) {
          parts.add('${m['kind']}: ${pts.join(' ')}');
        }
      }
      for (final c in _chunks(parts.join('\n\n'))) {
        _byGrade.putIfAbsent(grade, () => []).add(Passage(l['title'] as String, c, 'lesson', tid, content.topicTitle(tid), 3));
      }
    }
    for (final q in content.questions) {
      if (q['usage'] == 'assessment' || ((q['explanation'] as String?) ?? '').isEmpty) {
        continue;
      }
      final tid = (q['topic_id'] as num).toInt();
      final grade = content.gradeOfTopic(tid);
      if (grade == null) {
        continue;
      }
      final title = content.topicTitle(tid);
      _byGrade.putIfAbsent(grade, () => []).add(Passage('Bank soal · $title', 'Contoh soal $title: ${q['body']}\n\nPembahasan: ${q['explanation']}', 'question', tid, title, 2));
    }
  }

  final Map<int, List<Passage>> _byGrade = {};

  List<Passage> search(String query, int grade, {int? topicId, int limit = 4}) {
    final words = query.toLowerCase().split(RegExp(r'\s+')).map((w) => w.replaceAll(RegExp(r'[^0-9a-z]'), '')).where((w) => w.length >= 3).toSet();
    final pool = _byGrade[grade] ?? const <Passage>[];
    final scored = <Passage>[];
    if (words.isNotEmpty) {
      for (final p in pool) {
        final hay = p.content.toLowerCase();
        var hits = 0;
        for (final w in words) {
          if (hay.contains(w)) {
            hits++;
          }
        }
        if (hits > 0) {
          p.rank = hits.toDouble();
          scored.add(p);
        }
      }
      scored.sort((a, b) {
        final c = b.rank.compareTo(a.rank);
        return c != 0 ? c : b.priority.compareTo(a.priority);
      });
    }
    var rows = scored.take(limit).toList();
    if (topicId != null) {
      rows = [...rows.where((r) => r.topicId == topicId), ...rows.where((r) => r.topicId != topicId)];
      if (rows.isEmpty) {
        final same = pool.where((p) => p.topicId == topicId).toList()..sort((a, b) => b.priority.compareTo(a.priority));
        rows = same.take(limit).toList();
      }
    }
    return rows;
  }
}

final RegExp _hintWords = RegExp(r'(petunjuk|bantu|langkah|gimana|bagaimana cara|caranya|hint|cek jawaban|benar nggak|benar tidak)');

List<String> sentencesOf(String text) {
  final t = text.trim().replaceFirst(RegExp(r'^[A-Za-z ]+: '), '');
  return t.split(RegExp(r'(?<=[.!?])\s+|\n+')).map((p) => p.trim()).where((p) => p.isNotEmpty).toList();
}

String groundedTutor(String question, List<Passage> passages, int grade, String scope, String? style) {
  if (passages.isEmpty) {
    return 'Aku hanya menjawab dari materi BOBO yang sudah tersedia di aplikasi, yaitu $scope. Coba tanyakan dengan kata kunci dari materi itu, atau minta bantuan orang tua dan gurumu.';
  }
  final top = passages.first;
  final sentences = sentencesOf(top.content);
  if (sentences.isEmpty) {
    return 'Coba buka materinya di menu Belajar, ya.';
  }
  if (style != null) {
    final topic = (top.topic ?? top.title).toLowerCase();
    if (style == 'steps') {
      final steps = sentences.take(4).toList();
      return 'Langkah demi langkah:\n${[for (var i = 0; i < steps.length; i++) '${i + 1}. ${steps[i]}'].join('\n')}\n\nCoba ikuti langkahnya satu per satu, lalu kerjakan satu soal di Latihan.';
    }
    if (style == 'story') {
      String frame;
      if (topic.contains('pecahan')) {
        frame = 'kamu dan temanmu berbagi satu martabak yang dipotong sama besar';
      } else if (topic.contains('pythagoras') || topic.contains('segitiga')) {
        frame = 'sebuah tangga bersandar ke dinding, membentuk segitiga siku-siku dengan lantai';
      } else if (topic.contains('jumlah') || topic.contains('kurang') || topic.contains('cerita')) {
        frame = 'kamu mengumpulkan kelereng dari dua kantong lalu menghitung semuanya';
      } else {
        frame = 'kamu sedang menjelaskan hal ini kepada adikmu';
      }
      return 'Bayangkan $frame. ${sentences.take(2).join(' ')}\n\nSekarang coba ceritakan ulang dengan kata-katamu sendiri.';
    }
    return 'Lihat gambarnya, lalu coba sendiri di Alat peraga. ${sentences.take(2).join(' ')}';
  }
  if (_hintWords.hasMatch(question.toLowerCase())) {
    const keys = ['dulu', 'kalikan', 'jumlahkan', 'kurangi', 'kuadrat', 'pisahkan', 'tulis'];
    final key = sentences.firstWhere((s) => keys.any((k) => s.toLowerCase().contains(k)), orElse: () => sentences.first);
    return 'Petunjuk dulu, ya: $key\n\nCoba kerjakan langkah itu sendiri. Kalau sudah, ketik jawabanmu dan aku bantu cek caranya.';
  }
  final n = grade <= 2 ? 2 : 4;
  final body = sentences.take(n).join(' ');
  final topic = top.topic ?? top.title;
  return topic.isEmpty ? body : '$body\n\nMau coba latihan soal tentang $topic? Buka menu Latihan.';
}

String groundedParentAnswer(String text, String name, int grade, List<Map<String, dynamic>> mastery, int? lastScore, List<String> weak) {
  final t = text.toLowerCase();
  final b = grade <= 2 ? 1 : grade <= 4 ? 2 : grade <= 6 ? 3 : 4;
  bool has(List<String> ks) => ks.any(t.contains);
  if (has(['rutin', 'jadwal', 'kebiasaan', 'berapa lama', 'waktu belajar', 'sehat'])) {
    const tips = {
      1: 'Untuk anak kelas 1–2, sesi singkat 10–15 menit biasanya lebih efektif daripada satu sesi panjang. Pilih jam yang sama setiap hari, temani di awal, dan tutup dengan pujian atas usahanya.',
      2: 'Untuk anak kelas 3–4, coba 15–25 menit per sesi dengan jeda singkat. Biarkan anak memilih urutan mata pelajaran agar merasa punya kendali.',
      3: 'Untuk anak kelas 5–6, 20–30 menit per sesi dengan jeda 5 menit biasanya cukup. Ajak anak mencentang target hariannya sendiri di aplikasi.',
      4: 'Untuk siswa SMP, 30–45 menit per sesi dengan jeda 5–10 menit. Libatkan anak menyusun jadwalnya sendiri dan jauhkan ponsel dari notifikasi lain saat belajar.',
    };
    return '${tips[b]}\n\nIni panduan umum. Sesuaikan dengan kondisi dan kegiatan anak.';
  }
  if (mastery.isEmpty) {
    return 'Belum ada materi atau data belajar untuk Kelas $grade, jadi saya belum bisa menganalisis perkembangan $name.';
  }
  final dev = mastery.where((x) => x['state'] == 'developing').toList();
  final ins = mastery.where((x) => x['state'] == 'insufficient').toList();
  final none = mastery.where((x) => x['state'] == 'not_started').toList();
  if (has(['kesulitan', 'kenapa', 'mengapa', 'susah', 'sulit'])) {
    if (dev.isEmpty) {
      if (ins.isNotEmpty) {
        return 'Saat ini belum terlihat topik yang sulit. Untuk ${ins.first['topic']}, $name baru menjawab ${ins.first['evidence_count']} soal, jadi belum cukup untuk menyimpulkan apa pun. Ajak $name mengerjakan beberapa soal lagi agar gambarannya lebih jelas.';
      }
      return 'Dari data yang ada, belum terlihat topik yang sulit untuk $name.';
    }
    final x = dev.first;
    final mistake = x['common_mistake'] != null ? ' Kesalahan yang umum di topik ini adalah ${x['common_mistake']}.' : '';
    final act = (x['home_activity'] as String?) ?? 'Buka materinya bersama dan minta anak menjelaskan kembali.';
    return 'Di ${x['topic']}, $name menjawab benar ${x['recent_correct']} dari ${x['recent_total']} soal terakhir, jadi topik ini masih berkembang.$mistake Ini wajar saat anak baru mempelajarinya dan tidak menggambarkan kemampuan $name secara umum.\n\nYang bisa dicoba di rumah: $act';
  }
  if (has(['jelaskan', 'menjelaskan', 'cara', 'ajarkan', 'mengajar'])) {
    final x = (dev.isNotEmpty ? dev : ins.isNotEmpty ? ins : mastery).first;
    final act = (x['home_activity'] as String?) ?? 'Buka materi topik ini bersama anak.';
    return 'Cara menjelaskan ${x['topic']} di rumah:\n\n$act\n\nMinta $name menjelaskan kembali dengan kata-katanya sendiri. Jika ia bisa "mengajari" Anda, itu tanda pemahamannya mulai kuat.';
  }
  if (has(['selanjutnya', 'berikutnya', 'belajar apa'])) {
    final lines = <String>[];
    if (dev.isNotEmpty) {
      lines.add('Perkuat ${dev.map((x) => x['topic']).join(', ')}, karena hasilnya masih naik-turun.');
    }
    if (ins.isNotEmpty) {
      lines.add('Tambah 3–5 soal di ${ins.map((x) => x['topic']).join(', ')} agar BOBO bisa menilai.');
    }
    if (none.isNotEmpty) {
      lines.add('Setelah itu, mulai topik ${none.first['topic']}.');
    }
    if (lines.isEmpty) {
      lines.add('Semua topik yang tersedia sudah baik. Lanjutkan ke bab berikutnya setelah materinya tersedia.');
    }
    return 'Saran urutan untuk $name:\n${[for (var i = 0; i < lines.length; i++) '${i + 1}. ${lines[i]}'].join('\n')}';
  }
  if (has(['ujian', 'asesmen', 'persiapan', 'tes', 'try out', 'menyiapkan'])) {
    final w = weak.isNotEmpty ? weak : dev.map((x) => x['topic'] as String).toList();
    final head = w.isEmpty ? 'Belum ada topik lemah yang tercatat.' : 'Fokuskan persiapan ke ${w.join(' dan ')}${lastScore != null && weak.isNotEmpty ? ', topik yang belum tepat di asesmen terakhir (nilai $lastScore)' : ''}.';
    return '$head Ajak $name mengerjakan 5 soal latihan per topik selama 2–3 hari, lalu coba asesmen di menu Ujian. Hindari belajar maraton semalam sebelum ujian.';
  }
  return 'Saya bisa membantu soal perkembangan belajar $name, cara menjelaskan materi di rumah, persiapan asesmen, dan rutinitas belajar. Coba pilih salah satu pertanyaan yang tersedia.';
}
