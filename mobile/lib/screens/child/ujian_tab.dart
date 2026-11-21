import 'dart:async';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/api.dart';
import '../../core/models.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';
import 'child_shell.dart';

enum _Phase { list, intro, run, result }

class UjianTab extends StatefulWidget {
  const UjianTab({super.key});

  @override
  State<UjianTab> createState() => _UjianTabState();
}

class _UjianTabState extends State<UjianTab> {
  _Phase _phase = _Phase.list;
  Map<String, dynamic>? _list;
  Map<String, dynamic>? _selected;
  Map<String, dynamic>? _session;
  Map<String, dynamic>? _result;
  final Map<String, Map<String, dynamic>> _answers = {};
  final Set<String> _unsaved = {};
  int _cur = 0;
  DateTime? _deadline;
  Timer? _timer;
  bool _busy = false;
  bool _submitPending = false;
  String? _submitKey;
  Object? _error;
  int _lastTab = -1;

  String get _pendingKey => 'pending_submit_${context.read<AppState>().child!.id}';

  @override
  void initState() {
    super.initState();
    _loadList();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  Future<void> _loadList() async {
    final app = context.read<AppState>();
    setState(() => _error = null);
    final pending = await app.db.getJson(_pendingKey);
    if (pending != null) {
      await _sendSubmit(asMap(pending), silent: true);
    }
    try {
      final r = asMap(await app.student('GET', '/student/assessments'));
      if (mounted) {
        setState(() => _list = r);
      }
    } catch (e) {
      if (mounted) {
        setState(() => _error = e);
      }
    }
  }

  Future<void> _start() async {
    final app = context.read<AppState>();
    final nav = context.read<ChildNav>();
    setState(() => _busy = true);
    try {
      final s = asMap(await app.student('POST', '/student/assessments/${_selected!['id']}/start'));
      final serverNow = DateTime.parse(s['server_now'] as String);
      final offset = serverNow.difference(DateTime.now().toUtc());
      _deadline = DateTime.parse(s['deadline_at'] as String).subtract(offset);
      _answers
        ..clear()
        ..addAll(asMap(s['answers']).map((k, v) => MapEntry(k, asMap(v))));
      _unsaved.clear();
      _submitKey = 'sub-${uuidGen.v4()}';
      _submitPending = false;
      _cur = 0;
      _timer?.cancel();
      _timer = Timer.periodic(const Duration(seconds: 1), (_) => _tick());
      nav.setExamRunning(true);
      setState(() {
        _session = s;
        _phase = _Phase.run;
      });
    } on ApiException catch (e) {
      if (mounted) {
        showToast(context, e.isOffline ? 'Asesmen formal butuh koneksi internet.' : e.message);
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  int get _remaining => _deadline == null ? 0 : _deadline!.difference(DateTime.now()).inSeconds;

  void _tick() {
    if (!mounted || _phase != _Phase.run) {
      return;
    }
    if (_remaining <= 0 && !_busy && !_submitPending) {
      _submit(auto: true);
    }
    setState(() {});
  }

  Future<void> _answer(int qid, Map<String, dynamic> resp) async {
    final app = context.read<AppState>();
    final key = '$qid';
    setState(() {
      _answers[key] = resp;
      _unsaved.add(key);
    });
    try {
      await app.student('PUT', '/student/assessment-sessions/${_session!['session_id']}/answers', body: {'question_id': qid, 'response': resp});
      if (mounted) {
        setState(() => _unsaved.remove(key));
      }
    } on ApiException catch (e) {
      if (!e.isOffline && mounted) {
        showToast(context, e.message);
      }
    }
  }

  Future<void> _submit({bool auto = false}) async {
    final app = context.read<AppState>();
    final payload = {
      'session_id': _session!['session_id'],
      'idempotency_key': _submitKey,
      'answers': _answers.entries.map((e) => {'question_id': int.parse(e.key), 'response': e.value}).toList(),
    };
    await app.db.putJson(_pendingKey, payload);
    await _sendSubmit(payload, silent: false, auto: auto);
  }

  Future<void> _sendSubmit(Map<String, dynamic> payload, {required bool silent, bool auto = false}) async {
    final app = context.read<AppState>();
    final nav = context.read<ChildNav>();
    if (mounted) {
      setState(() => _busy = true);
    }
    try {
      final r = asMap(await app.student('POST', '/student/assessment-sessions/${payload['session_id']}/submit', body: {'idempotency_key': payload['idempotency_key'], 'answers': payload['answers']}));
      await app.db.putJson(_pendingKey, null);
      _timer?.cancel();
      nav.setExamRunning(false);
      if (mounted) {
        setState(() {
          _result = r;
          _phase = _Phase.result;
          _submitPending = false;
        });
      }
    } on ApiException catch (e) {
      if (e.status == 404) {
        await app.db.putJson(_pendingKey, null);
      } else if (mounted && !silent) {
        setState(() => _submitPending = true);
        showToast(context, e.isOffline ? 'Belum terkirim. Jawaban tersimpan di perangkat dan akan dikirim saat online.' : e.message);
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  Future<void> _confirmSubmit() async {
    final qs = asList(_session!['questions']);
    final answered = qs.where((q) => _answers.containsKey('${q['id']}')).length;
    final un = qs.length - answered;
    final t = BandTheme.forGrade(context.read<AppState>().child!.grade);
    final ok = await showModalBottomSheet<bool>(
      context: context,
      backgroundColor: Palette.surface,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(24))),
      builder: (ctx) => Padding(
        padding: const EdgeInsets.fromLTRB(20, 24, 20, 28),
        child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Kumpulkan jawaban?', style: TextStyle(fontSize: 20, fontWeight: FontWeight.w800)),
          const SizedBox(height: 10),
          Text('$answered dari ${qs.length} soal terjawab. ${un > 0 ? '$un soal belum dijawab dan akan dihitung salah.' : 'Semua soal sudah terjawab.'}', style: const TextStyle(fontSize: 15, height: 1.55, color: Palette.inkSoft)),
          const SizedBox(height: 16),
          PrimaryButton(label: 'Ya, kumpulkan', color: t.accent, radius: t.radiusSmall, onPressed: () => Navigator.pop(ctx, true)),
          const SizedBox(height: 10),
          SecondaryButton(label: 'Periksa lagi', radius: t.radiusSmall, onPressed: () => Navigator.pop(ctx, false)),
        ]),
      ),
    );
    if (ok == true) {
      await _submit();
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    final nav = context.watch<ChildNav>();
    if (nav.tab == 3 && _lastTab != 3 && _phase == _Phase.list && _list != null) {
      WidgetsBinding.instance.addPostFrameCallback((_) => _loadList());
    }
    _lastTab = nav.tab;
    final t = BandTheme.forGrade(app.child!.grade);
    switch (_phase) {
      case _Phase.list:
        return _buildList(t, app);
      case _Phase.intro:
        return _buildIntro(t);
      case _Phase.run:
        return _buildRun(t, app);
      case _Phase.result:
        return _buildResult(t);
    }
  }

  Widget _buildList(BandTheme t, AppState app) {
    if (_error != null && _list == null) {
      return ErrorView(error: _error!, onRetry: _loadList);
    }
    if (_list == null) {
      return const LoadingView();
    }
    final items = asList(_list!['assessments']);
    final upcoming = ((_list!['upcoming'] as List?) ?? const []).map((e) => e.toString()).toList();
    return RefreshIndicator(
      onRefresh: _loadList,
      child: ListView(padding: const EdgeInsets.all(20), children: [
        if (app.offline) ...[const Notice('Kamu sedang offline. Asesmen formal butuh koneksi agar waktu dan nilainya diverifikasi server.'), const SizedBox(height: 14)],
        if (items.isEmpty)
          EmptyState(icon: Icons.assignment_outlined, iconColor: t.accent, title: 'Belum ada asesmen untuk Kelas ${app.child!.grade}', body: 'Asesmen akan muncul setelah soal dan kunci jawabannya selesai ditinjau.'),
        for (final a in items) ...[
          AppCard(
            radius: t.radius,
            padding: const EdgeInsets.all(20),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Tag(a['type'] as String, fg: t.ink, bg: t.soft),
              const SizedBox(height: 10),
              Text(a['title'] as String, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800, height: 1.3)),
              const SizedBox(height: 8),
              Row(children: [
                const Icon(Icons.schedule_rounded, size: 16, color: Palette.muted),
                const SizedBox(width: 6),
                Text('${a['duration_minutes']} menit · ${a['question_count']} soal', style: const TextStyle(fontSize: 14, color: Palette.muted, fontWeight: FontWeight.w600)),
              ]),
              if (a['last_result'] != null) ...[
                const SizedBox(height: 10),
                Notice('Terakhir: nilai ${a['last_result']['score']} · ${a['last_result']['date']}${a['last_result']['final'] == true ? ' · terverifikasi server' : ' · menunggu penilaian esai'}', fg: Palette.inkSoft, bg: const Color(0xFFF1F5F9)),
              ],
              const SizedBox(height: 14),
              PrimaryButton(
                label: a['active_session_id'] != null ? 'Lanjutkan asesmen' : (a['last_result'] != null ? 'Kerjakan lagi' : 'Mulai asesmen'),
                color: t.accent,
                radius: t.radiusSmall,
                onPressed: () => setState(() {
                  _selected = a;
                  _phase = _Phase.intro;
                }),
              ),
            ]),
          ),
          const SizedBox(height: 14),
        ],
        if (upcoming.isNotEmpty) ...[
          const SectionTitle('Asesmen lainnya'),
          for (final u in upcoming) ...[
            AppCard(
              radius: t.radius,
              child: Row(children: [
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(u, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700)),
                  const Text('Soal sedang ditinjau tim konten', style: TextStyle(fontSize: 13, color: Palette.muted)),
                ])),
                const Tag('Segera'),
              ]),
            ),
            const SizedBox(height: 10),
          ],
        ],
      ]),
    );
  }

  Widget _buildIntro(BandTheme t) {
    final a = _selected!;
    final steps = [
      'Ada ${a['question_count']} soal. Kerjakan sendiri, tanpa bantuan.',
      'Waktu ${a['duration_minutes']} menit, mulai berjalan setelah kamu menekan Mulai. Waktu dihitung oleh server.',
      'Jawaban tersimpan otomatis. Kalau koneksi putus, jawabanmu tidak hilang.',
      'Tutor BOBO tidak aktif selama asesmen.',
      'Saat waktu habis, jawaban dikumpulkan otomatis.',
    ];
    return ListView(padding: const EdgeInsets.all(20), children: [
      Text(a['title'] as String, style: TextStyle(fontSize: t.title, fontWeight: FontWeight.w800, height: 1.25)),
      const SizedBox(height: 16),
      AppCard(
        radius: t.radius,
        padding: const EdgeInsets.all(20),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Petunjuk', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
          const SizedBox(height: 12),
          for (final (i, s) in steps.indexed)
            Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                SizedBox(width: 22, child: Text('${i + 1}.', style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w700))),
                Expanded(child: Text(s, style: TextStyle(fontSize: t.body, height: 1.5))),
              ]),
            ),
        ]),
      ),
      const SizedBox(height: 16),
      PrimaryButton(label: 'Saya siap, mulai', color: t.accent, radius: t.radiusSmall, height: 54, busy: _busy, onPressed: _start),
      const SizedBox(height: 12),
      SecondaryButton(label: 'Nanti dulu', radius: t.radiusSmall, onPressed: () => setState(() => _phase = _Phase.list)),
    ]);
  }

  Widget _buildRun(BandTheme t, AppState app) {
    final qs = asList(_session!['questions']);
    final q = qs[_cur];
    final rem = _remaining.clamp(0, 999999);
    final mm = (rem ~/ 60).toString().padLeft(2, '0');
    final ss = (rem % 60).toString().padLeft(2, '0');
    final warn = rem < 60;
    final key = '${q['id']}';
    final resp = _answers[key];
    final type = q['type'] as String;
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    final saveText = _unsaved.isNotEmpty ? 'Tersimpan di perangkat' : '✓ Tersimpan otomatis';
    return ListView(padding: const EdgeInsets.fromLTRB(20, 16, 20, 24), children: [
      if (_submitPending) ...[
        const Notice('Belum terkirim ke server. Nilai belum resmi. Jawaban tersimpan di perangkat; tekan Kirim ulang saat online.'),
        const SizedBox(height: 10),
        PrimaryButton(label: 'Kirim ulang', color: t.accent, radius: t.radiusSmall, busy: _busy, onPressed: () => _submit(auto: rem <= 0)),
        const SizedBox(height: 14),
      ],
      Row(children: [
        Semantics(
          label: 'Sisa waktu $mm menit $ss detik',
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(color: warn ? const Color(0xFFFEE2E2) : t.soft, borderRadius: BorderRadius.circular(10)),
            child: Row(children: [
              Icon(Icons.schedule_rounded, size: 16, color: warn ? Palette.badInk : t.ink),
              const SizedBox(width: 6),
              Text('$mm:$ss', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: warn ? Palette.badInk : t.ink, fontFeatures: const [FontFeature.tabularFigures()])),
            ]),
          ),
        ),
        const SizedBox(width: 10),
        Expanded(child: Text('Soal ${_cur + 1} dari ${qs.length}', style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w700, color: Palette.inkSoft))),
        Text(saveText, style: TextStyle(fontSize: 12, fontWeight: FontWeight.w700, color: _unsaved.isNotEmpty ? Palette.warnInk : Palette.okInk)),
      ]),
      const SizedBox(height: 14),
      Wrap(spacing: 8, runSpacing: 8, children: [
        for (final (i, x) in qs.indexed)
          SizedBox(
            width: 52,
            height: 44,
            child: OutlinedButton(
              onPressed: () => setState(() => _cur = i),
              style: OutlinedButton.styleFrom(
                padding: EdgeInsets.zero,
                backgroundColor: _answers.containsKey('${x['id']}') ? t.soft : Palette.surface,
                foregroundColor: _answers.containsKey('${x['id']}') ? t.ink : Palette.inkSoft,
                side: BorderSide(color: i == _cur ? t.accent : (_answers.containsKey('${x['id']}') ? t.soft : Palette.borderStrong), width: 2),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              ),
              child: Text('${i + 1}', semanticsLabel: 'Soal ${i + 1}${_answers.containsKey('${x['id']}') ? ', terjawab' : ', belum dijawab'}', style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 15)),
            ),
          ),
      ]),
      const SizedBox(height: 14),
      AppCard(
        radius: t.radius,
        padding: const EdgeInsets.all(20),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(q['body'] as String, style: TextStyle(fontSize: t.question, fontWeight: FontWeight.w700, height: 1.45)),
          const SizedBox(height: 16),
          if (type == 'fill' || type == 'short')
            _ExamTextAnswer(key: ValueKey('t-$key'), initial: (resp?['text'] ?? '') as String, onSaved: (v) => _answer(q['id'] as int, {'text': v}))
          else
            for (final o in asList(q['options']))
              Builder(builder: (context) {
                final idx = (o['index'] as num).toInt();
                final on = type == 'multi' ? ((resp?['indices'] as List?) ?? const []).contains(idx) : resp?['index'] == idx;
                return Padding(
                  padding: const EdgeInsets.only(bottom: 10),
                  child: Semantics(
                    selected: on,
                    button: true,
                    child: Material(
                      color: on ? t.soft : Palette.surface,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall), side: BorderSide(color: on ? t.accent : Palette.border, width: 2)),
                      child: InkWell(
                        borderRadius: BorderRadius.circular(t.radiusSmall),
                        onTap: _submitPending
                            ? null
                            : () {
                                if (type == 'multi') {
                                  final cur = ((resp?['indices'] as List?) ?? const []).map((e) => e as int).toList();
                                  if (on) {
                                    cur.remove(idx);
                                  } else {
                                    cur.add(idx);
                                  }
                                  _answer(q['id'] as int, {'indices': cur});
                                } else {
                                  _answer(q['id'] as int, {'index': idx});
                                }
                              },
                        child: ConstrainedBox(
                          constraints: const BoxConstraints(minHeight: 56),
                          child: Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                            child: Row(children: [
                              Container(width: 30, height: 30, alignment: Alignment.center, decoration: BoxDecoration(color: on ? t.accent : const Color(0xFFF1F5F9), shape: BoxShape.circle), child: Text(letters[asList(q['options']).indexOf(o) % letters.length], style: TextStyle(color: on ? Colors.white : Palette.inkSoft, fontWeight: FontWeight.w800))),
                              const SizedBox(width: 12),
                              Expanded(child: Text(o['label'] as String, style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w600))),
                            ]),
                          ),
                        ),
                      ),
                    ),
                  ),
                );
              }),
        ]),
      ),
      const SizedBox(height: 16),
      Row(children: [
        Expanded(child: SecondaryButton(label: 'Sebelumnya', radius: t.radiusSmall, onPressed: _cur == 0 ? null : () => setState(() => _cur--))),
        const SizedBox(width: 12),
        Expanded(
          child: PrimaryButton(
            label: _cur + 1 >= qs.length ? 'Kumpulkan' : 'Berikutnya',
            color: t.accent,
            radius: t.radiusSmall,
            busy: _busy,
            onPressed: _submitPending ? null : (_cur + 1 >= qs.length ? _confirmSubmit : () => setState(() => _cur++)),
          ),
        ),
      ]),
    ]);
  }

  Widget _buildResult(BandTheme t) {
    final r = _result!;
    final nav = context.read<ChildNav>();
    final weak = asList(r['weak_topics']);
    return ListView(padding: const EdgeInsets.all(20), children: [
      Container(
        padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 20),
        decoration: BoxDecoration(color: t.accent, borderRadius: BorderRadius.circular(t.radius)),
        child: Column(children: [
          const Text('NILAI KAMU', style: TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w700, letterSpacing: 0.5)),
          Text('${r['score']}', style: const TextStyle(color: Colors.white, fontSize: 56, fontWeight: FontWeight.w800, height: 1.1)),
          Text('${r['correct']} dari ${r['total']} soal benar', style: const TextStyle(color: Colors.white, fontSize: 15, fontWeight: FontWeight.w600)),
          if (r['auto_submitted'] == true) const Text('Waktu habis · dikumpulkan otomatis', style: TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w600)),
        ]),
      ),
      const SizedBox(height: 12),
      Notice(
        r['final'] == true ? '✓ Terkirim dan terverifikasi server' : 'Terkirim. Ada soal esai yang masih menunggu penilaian guru/peninjau, jadi nilai belum final.',
        fg: r['final'] == true ? Palette.okInk : Palette.warnInk,
        bg: r['final'] == true ? Palette.okSoft : Palette.warnSoft,
      ),
      const SizedBox(height: 16),
      AppCard(
        radius: t.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Topik yang perlu dilatih', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
          const SizedBox(height: 10),
          if (weak.isEmpty)
            const Text('✓ Semua topik di asesmen ini terjawab benar.', style: TextStyle(fontSize: 14, color: Palette.okInk, fontWeight: FontWeight.w700))
          else
            Wrap(spacing: 8, runSpacing: 8, children: [
              for (final w in weak)
                ActionChip(
                  label: Text('Latih: ${w['title']}'),
                  labelStyle: TextStyle(color: t.ink, fontWeight: FontWeight.w700),
                  backgroundColor: t.soft,
                  side: BorderSide(color: t.accent),
                  shape: const StadiumBorder(),
                  onPressed: () => nav.practice(w['id'] as int),
                ),
            ]),
        ]),
      ),
      const SizedBox(height: 16),
      const SectionTitle('Pembahasan'),
      for (final rv in asList(r['review'])) ...[
        AppCard(
          radius: t.radius,
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Container(width: 26, height: 26, alignment: Alignment.center, decoration: BoxDecoration(color: rv['correct'] == true ? Palette.ok : (rv['needs_review'] == true ? Palette.warnInk : Palette.bad), shape: BoxShape.circle), child: Text(rv['correct'] == true ? '✓' : (rv['needs_review'] == true ? '?' : '✕'), style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 13))),
              const SizedBox(width: 10),
              Expanded(child: Text('${rv['n']}. ${rv['question']}', style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700, height: 1.4))),
            ]),
            Padding(
              padding: const EdgeInsets.only(left: 36, top: 8),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text.rich(TextSpan(children: [const TextSpan(text: 'Jawabanmu: ', style: TextStyle(color: Palette.muted)), TextSpan(text: '${rv['your_answer']}', style: const TextStyle(fontWeight: FontWeight.w800))]), style: const TextStyle(fontSize: 14)),
                if (rv['correct'] != true) Text.rich(TextSpan(children: [const TextSpan(text: 'Jawaban benar: ', style: TextStyle(color: Palette.muted)), TextSpan(text: '${rv['correct_answer']}', style: const TextStyle(fontWeight: FontWeight.w800))]), style: const TextStyle(fontSize: 14)),
                const SizedBox(height: 6),
                Text('${rv['explanation']}', style: const TextStyle(fontSize: 14, color: Palette.inkSoft, height: 1.55)),
              ]),
            ),
          ]),
        ),
        const SizedBox(height: 12),
      ],
      SecondaryButton(
        label: 'Kembali ke daftar asesmen',
        radius: t.radiusSmall,
        onPressed: () {
          setState(() {
            _phase = _Phase.list;
            _result = null;
            _session = null;
          });
          _loadList();
        },
      ),
    ]);
  }
}

class _ExamTextAnswer extends StatefulWidget {
  const _ExamTextAnswer({super.key, required this.initial, required this.onSaved});

  final String initial;
  final ValueChanged<String> onSaved;

  @override
  State<_ExamTextAnswer> createState() => _ExamTextAnswerState();
}

class _ExamTextAnswerState extends State<_ExamTextAnswer> {
  late final TextEditingController _c = TextEditingController(text: widget.initial);
  Timer? _debounce;

  @override
  void dispose() {
    _debounce?.cancel();
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _c,
      decoration: const InputDecoration(labelText: 'Jawabanmu'),
      onChanged: (v) {
        _debounce?.cancel();
        _debounce = Timer(const Duration(milliseconds: 700), () => widget.onSaved(v.trim()));
      },
    );
  }
}
