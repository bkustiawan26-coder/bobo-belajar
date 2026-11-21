import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/api.dart';
import '../../core/grading.dart';
import '../../core/models.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';
import 'child_shell.dart';

class LatihanTab extends StatefulWidget {
  const LatihanTab({super.key});

  @override
  State<LatihanTab> createState() => _LatihanTabState();
}

class _Result {
  _Result(this.question, this.correct, this.answer, this.answerKey, this.explanation, this.mistake, this.relatedLessonId);

  final Map<String, dynamic> question;
  final bool correct;
  final String answer;
  final Map<String, dynamic> answerKey;
  final String explanation;
  final String? mistake;
  final int? relatedLessonId;
}

class _LatihanTabState extends State<LatihanTab> {
  List<Map<String, dynamic>> _topics = [];
  int? _topicId;
  List<Map<String, dynamic>> _questions = [];
  int _idx = 0;
  List<int> _selected = [];
  final _text = TextEditingController();
  _Result? _current;
  final List<_Result> _results = [];
  bool _done = false;
  bool _loading = true;
  bool _checking = false;
  bool _offlineMode = false;
  Object? _error;
  int _seenVersion = -1;

  @override
  void dispose() {
    _text.dispose();
    super.dispose();
  }

  Future<void> _init(int? topicId) async {
    final app = context.read<AppState>();
    setState(() {
      _loading = true;
      _error = null;
      _topicId = topicId;
    });
    try {
      final cat = await CatalogCache.load(app);
      final topics = <Map<String, dynamic>>[];
      for (final s in asList(cat['subjects'])) {
        for (final ch in asList(s['chapters'])) {
          for (final tp in asList(ch['topics'])) {
            if ((tp['question_count'] as num) > 0) {
              topics.add(tp);
            }
          }
        }
      }
      List<Map<String, dynamic>> qs;
      var offline = false;
      try {
        final r = asMap(await app.student('GET', '/student/practice', query: topicId == null ? null : {'topic_id': '$topicId'}));
        qs = asList(r['questions']);
      } on ApiException catch (e) {
        final pack = await CatalogCache.pack(app);
        if (!e.isOffline || pack == null) {
          rethrow;
        }
        qs = asList(pack['questions']).where((q) => topicId == null || q['topic_id'] == topicId).toList();
        offline = true;
      }
      if (!mounted) {
        return;
      }
      setState(() {
        _topics = topics;
        _questions = qs;
        _offlineMode = offline;
        _reset();
        _loading = false;
      });
    } catch (e) {
      if (mounted) {
        setState(() {
          _error = e;
          _loading = false;
        });
      }
    }
  }

  void _reset() {
    _idx = 0;
    _selected = [];
    _text.clear();
    _current = null;
    _results.clear();
    _done = false;
  }

  Map<String, dynamic>? get _q => _idx < _questions.length ? _questions[_idx] : null;

  bool get _answered => _q == null ? false : (_q!['type'] == 'fill' || _q!['type'] == 'short' ? _text.text.trim().isNotEmpty : _selected.isNotEmpty);

  Map<String, dynamic> _response() {
    final q = _q!;
    switch (q['type']) {
      case 'multi':
        return {'indices': _selected};
      case 'fill':
      case 'short':
        return {'text': _text.text.trim()};
      default:
        return {'index': _selected.first};
    }
  }

  Future<void> _check() async {
    final app = context.read<AppState>();
    final q = _q!;
    final resp = _response();
    final attempt = {'client_uuid': uuidGen.v4(), 'question_id': q['id'], 'response': resp, 'answered_at': DateTime.now().toUtc().toIso8601String()};
    setState(() => _checking = true);
    _Result? res;
    if (!_offlineMode) {
      try {
        final r = asMap(await app.student('POST', '/student/practice/attempts', body: attempt));
        res = _Result(q, r['correct'] == true, (r['correct_answer'] ?? '') as String, asMap(r['answer_key']), (r['explanation'] ?? '') as String, r['mistake_hint'] as String?, r['related_lesson_id'] as int?);
      } on ApiException catch (e) {
        if (!e.isOffline) {
          if (mounted) {
            setState(() => _checking = false);
            showToast(context, e.message);
          }
          return;
        }
      }
    }
    if (res == null) {
      final pack = await CatalogCache.pack(app);
      final full = pack == null ? null : asList(pack['questions']).where((x) => x['id'] == q['id']).firstOrNull;
      if (full == null) {
        if (mounted) {
          setState(() => _checking = false);
          showToast(context, 'Tidak ada koneksi. Unduh latihan dulu agar bisa dikerjakan offline.');
        }
        return;
      }
      final ok = gradeLocally(full, resp);
      await app.queueAttempt(attempt);
      res = _Result(q, ok, (full['answer_text'] ?? '') as String, asMap(full['answer']), (full['explanation'] ?? '') as String, ok ? null : full['mistake_hint'] as String?, null);
      _offlineMode = true;
    }
    if (!mounted) {
      return;
    }
    setState(() {
      _current = res;
      _results.add(res!);
      _checking = false;
    });
  }

  void _next() {
    setState(() {
      if (_idx + 1 >= _questions.length) {
        _done = true;
      } else {
        _idx++;
        _selected = [];
        _text.clear();
        _current = null;
      }
    });
  }

  void _retryWrong() {
    final wrong = _results.where((r) => !r.correct).map((r) => r.question).toList();
    setState(() {
      _questions = wrong;
      _reset();
    });
  }

  @override
  Widget build(BuildContext context) {
    final nav = context.watch<ChildNav>();
    final app = context.watch<AppState>();
    if (nav.practiceVersion != _seenVersion) {
      _seenVersion = nav.practiceVersion;
      final tid = nav.practiceTopicId;
      WidgetsBinding.instance.addPostFrameCallback((_) => _init(tid));
    }
    final t = BandTheme.forGrade(app.child!.grade);
    if (_loading) {
      return const LoadingView();
    }
    if (_error != null) {
      return ErrorView(error: _error!, onRetry: () => _init(_topicId));
    }
    if (_topics.isEmpty) {
      return EmptyState(icon: Icons.edit_outlined, iconColor: t.accent, title: 'Soal latihan belum tersedia', body: 'Bank soal Kelas ${app.child!.grade} sedang ditinjau. Soal hanya tampil setelah kunci jawaban dan pembahasannya diperiksa.');
    }
    return Column(children: [
      SizedBox(
        height: 60,
        child: ListView(scrollDirection: Axis.horizontal, padding: const EdgeInsets.fromLTRB(20, 12, 20, 8), children: [
          _chip(t, 'Semua topik', _topicId == null, () => _init(null)),
          for (final tp in _topics) _chip(t, tp['title'] as String, _topicId == tp['id'], () => _init(tp['id'] as int)),
        ]),
      ),
      if (_offlineMode) const Padding(padding: EdgeInsets.fromLTRB(20, 0, 20, 8), child: Notice('Mode offline: jawaban dinilai di perangkat dan dikirim saat online.')),
      Expanded(child: _done ? _summary(t, app) : _runner(t)),
    ]);
  }

  Widget _chip(BandTheme t, String label, bool on, VoidCallback onTap) {
    return Padding(
      padding: const EdgeInsets.only(right: 8),
      child: ChoiceChip(
        label: Text(label),
        selected: on,
        onSelected: (_) => onTap(),
        showCheckmark: false,
        selectedColor: t.accent,
        backgroundColor: Palette.surface,
        labelStyle: TextStyle(color: on ? Colors.white : Palette.inkSoft, fontWeight: FontWeight.w700, fontSize: 13),
        side: BorderSide(color: on ? t.accent : Palette.borderStrong),
        shape: const StadiumBorder(),
      ),
    );
  }

  Widget _runner(BandTheme t) {
    final q = _q;
    if (q == null) {
      return EmptyState(icon: Icons.edit_outlined, title: 'Belum ada soal di topik ini', body: 'Pilih topik lain di atas.', iconColor: t.accent);
    }
    final type = q['type'] as String;
    final checked = _current != null;
    final opts = asList(q['options']);
    final instr = switch (type) {
      'multi' => 'Pilih semua jawaban yang benar.',
      'fill' || 'short' => 'Ketik jawabanmu lalu tekan Periksa.',
      'tf' => 'Pernyataan ini benar atau salah?',
      _ => 'Pilih satu jawaban.',
    };
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    return ListView(padding: const EdgeInsets.fromLTRB(20, 4, 20, 24), children: [
      Row(children: [
        Text('Soal ${_idx + 1} dari ${_questions.length}', style: const TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w700)),
        const Spacer(),
        Text(_cap(q['difficulty'] as String? ?? ''), style: const TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w700)),
      ]),
      const SizedBox(height: 8),
      ClipRRect(borderRadius: BorderRadius.circular(999), child: LinearProgressIndicator(value: (_idx + (checked ? 1 : 0)) / _questions.length, minHeight: 8, color: t.accent, backgroundColor: const Color(0xFFE2E8F0))),
      const SizedBox(height: 16),
      AppCard(
        radius: t.radius,
        padding: const EdgeInsets.all(20),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          if (q['topic'] != null) Tag(q['topic'] as String, fg: t.ink, bg: t.soft),
          const SizedBox(height: 14),
          Text(q['body'] as String, style: TextStyle(fontSize: t.question, fontWeight: FontWeight.w700, height: 1.45)),
          const SizedBox(height: 10),
          Text(instr, style: const TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w600)),
          const SizedBox(height: 14),
          if (type == 'fill' || type == 'short')
            TextField(
              controller: _text,
              enabled: !checked,
              keyboardType: TextInputType.text,
              onChanged: (_) => setState(() {}),
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w700),
              decoration: InputDecoration(
                labelText: 'Jawabanmu',
                enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(t.radiusSmall), borderSide: BorderSide(color: checked ? (_current!.correct ? Palette.ok : Palette.bad) : Palette.borderStrong, width: 2)),
                disabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(t.radiusSmall), borderSide: BorderSide(color: checked ? (_current!.correct ? Palette.ok : Palette.bad) : Palette.borderStrong, width: 2)),
              ),
            )
          else
            for (final o in opts) _option(t, o, letters, type == 'multi', checked),
        ]),
      ),
      if (checked) ...[const SizedBox(height: 16), _feedback(t)],
      const SizedBox(height: 16),
      PrimaryButton(
        label: checked ? (_idx + 1 >= _questions.length ? 'Lihat hasil' : 'Soal berikutnya') : 'Periksa jawaban',
        color: t.accent,
        radius: t.radiusSmall,
        height: 54,
        busy: _checking,
        onPressed: checked ? _next : (_answered ? _check : null),
      ),
    ]);
  }

  String _cap(String s) => s.isEmpty ? s : s[0].toUpperCase() + s.substring(1);

  Widget _option(BandTheme t, Map<String, dynamic> o, List<String> letters, bool multi, bool checked) {
    final i = (o['index'] as num).toInt();
    final picked = _selected.contains(i);
    var bg = Palette.surface;
    var border = Palette.border;
    var mark = letters[i % letters.length];
    var mBg = const Color(0xFFF1F5F9);
    var mFg = Palette.inkSoft;
    if (!checked && picked) {
      bg = t.soft;
      border = t.accent;
      mBg = t.accent;
      mFg = Colors.white;
    }
    if (checked) {
      final key = _current!.answerKey;
      final isAns = multi ? ((key['indices'] as List?) ?? const []).contains(i) : key['index'] == i;
      if (isAns) {
        bg = Palette.okBg;
        border = Palette.ok;
        mark = '✓';
        mBg = Palette.ok;
        mFg = Colors.white;
      } else if (picked) {
        bg = Palette.badBg;
        border = Palette.bad;
        mark = '✕';
        mBg = Palette.bad;
        mFg = Colors.white;
      }
    }
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Semantics(
        selected: picked,
        button: true,
        child: Material(
          color: bg,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall), side: BorderSide(color: border, width: 2)),
          child: InkWell(
            borderRadius: BorderRadius.circular(t.radiusSmall),
            onTap: checked
                ? null
                : () => setState(() {
                      if (multi && picked) {
                        _selected.remove(i);
                      } else if (multi) {
                        _selected.add(i);
                      } else {
                        _selected = [i];
                      }
                    }),
            child: ConstrainedBox(
              constraints: const BoxConstraints(minHeight: 56),
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                child: Row(children: [
                  Container(width: 30, height: 30, alignment: Alignment.center, decoration: BoxDecoration(color: mBg, borderRadius: BorderRadius.circular(multi ? 8 : 15)), child: Text(mark, style: TextStyle(color: mFg, fontWeight: FontWeight.w800))),
                  const SizedBox(width: 12),
                  Expanded(child: Text(o['label'] as String, style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w600))),
                ]),
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _feedback(BandTheme t) {
    final r = _current!;
    final young = context.read<AppState>().child!.grade <= 2;
    final nav = context.read<ChildNav>();
    return Semantics(
      liveRegion: true,
      child: AppCard(
        radius: t.radius,
        color: r.correct ? Palette.okBg : Palette.badBg,
        borderColor: r.correct ? const Color(0xFFBBF7D0) : Palette.badSoft,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(r.correct ? (young ? '✓ Benar! Hebat!' : '✓ Benar! Kerja bagus.') : '✕ Belum tepat, tidak apa-apa', style: TextStyle(fontSize: 17, fontWeight: FontWeight.w800, color: r.correct ? Palette.okInk : Palette.badInk)),
          if (!r.correct) ...[
            const SizedBox(height: 8),
            Text.rich(TextSpan(children: [const TextSpan(text: 'Jawaban benar: ', style: TextStyle(fontWeight: FontWeight.w800)), TextSpan(text: r.answer)]), style: const TextStyle(fontSize: 15, height: 1.5)),
            if (r.mistake != null) ...[
              const SizedBox(height: 6),
              Text.rich(TextSpan(children: [const TextSpan(text: 'Letak kesalahannya: ', style: TextStyle(fontWeight: FontWeight.w800)), TextSpan(text: r.mistake)]), style: const TextStyle(fontSize: 14, color: Color(0xFF7F1D1D), height: 1.5)),
            ],
          ],
          const SizedBox(height: 8),
          Text.rich(TextSpan(children: [const TextSpan(text: 'Pembahasan: ', style: TextStyle(fontWeight: FontWeight.w800)), TextSpan(text: r.explanation)]), style: const TextStyle(fontSize: 15, height: 1.55)),
          const SizedBox(height: 4),
          TextButton(
            onPressed: () => r.relatedLessonId != null ? nav.lesson(r.relatedLessonId!) : nav.askTutor('Jelaskan tentang ${r.question['topic'] ?? 'soal ini'}'),
            style: TextButton.styleFrom(padding: EdgeInsets.zero, foregroundColor: t.ink),
            child: Text(r.relatedLessonId != null ? 'Baca lagi materinya' : 'Tanya Tutor tentang ini', style: const TextStyle(decoration: TextDecoration.underline, fontWeight: FontWeight.w700)),
          ),
        ]),
      ),
    );
  }

  Widget _summary(BandTheme t, AppState app) {
    final right = _results.where((r) => r.correct).length;
    final total = _results.length;
    final wrong = total - right;
    final msg = right == total ? 'Sempurna! Semua jawaban benar.' : (right * 2 >= total ? 'Bagus! Ulangi soal yang salah supaya makin paham.' : 'Salah itu bagian dari belajar. Baca lagi materinya, lalu coba lagi.');
    return ListView(padding: const EdgeInsets.fromLTRB(20, 4, 20, 24), children: [
      AppCard(
        radius: t.radius,
        padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 20),
        child: Column(children: [
          Text.rich(TextSpan(children: [TextSpan(text: '$right', style: TextStyle(fontSize: 44, fontWeight: FontWeight.w800, color: t.ink)), TextSpan(text: '/$total', style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w800, color: Palette.muted))])),
          const Text('jawaban benar', style: TextStyle(fontSize: 14, fontWeight: FontWeight.w700, color: Palette.muted)),
          const SizedBox(height: 8),
          Text(msg, textAlign: TextAlign.center, style: const TextStyle(fontSize: 15, height: 1.5)),
        ]),
      ),
      const SizedBox(height: 16),
      AppCard(
        radius: t.radius,
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
        child: Column(children: [
          for (final r in _results)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 10),
              child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Container(width: 24, height: 24, alignment: Alignment.center, decoration: BoxDecoration(color: r.correct ? Palette.ok : Palette.bad, shape: BoxShape.circle), child: Text(r.correct ? '✓' : '✕', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 13))),
                const SizedBox(width: 12),
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(r.question['body'] as String, style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w600, height: 1.4)),
                  Text('${r.question['topic'] ?? ''} · ${r.correct ? 'Benar' : 'Belum tepat'}', style: const TextStyle(fontSize: 12, color: Palette.muted)),
                ])),
              ]),
            ),
        ]),
      ),
      if (app.pending > 0) ...[const SizedBox(height: 12), Notice('${app.pending} jawaban tersimpan di perangkat dan akan tersinkron saat online.')],
      const SizedBox(height: 16),
      if (wrong > 0) ...[PrimaryButton(label: 'Ulangi soal yang salah ($wrong)', color: t.accent, radius: t.radiusSmall, onPressed: _retryWrong), const SizedBox(height: 12)],
      SecondaryButton(label: 'Latihan dari awal', radius: t.radiusSmall, onPressed: () => _init(_topicId)),
    ]);
  }
}
