import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/api.dart';
import '../../core/models.dart';
import '../../core/persona.dart';
import '../../core/speech.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';
import '../../widgets/playground.dart';
import '../../widgets/visuals.dart';
import 'child_shell.dart';

class BelajarTab extends StatefulWidget {
  const BelajarTab({super.key});

  @override
  State<BelajarTab> createState() => _BelajarTabState();
}

class _BelajarTabState extends State<BelajarTab> {
  Map<String, dynamic>? _catalog;
  Object? _error;
  int? _subjectId;
  int? _semester;
  int? _lessonId;
  int _seenVersion = 0;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load({bool refresh = false}) async {
    final app = context.read<AppState>();
    try {
      final cat = await CatalogCache.load(app, refresh: refresh);
      if (mounted) {
        setState(() {
          _catalog = cat;
          _error = null;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() => _error = e);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final nav = context.watch<ChildNav>();
    final app = context.watch<AppState>();
    if (nav.lessonVersion != _seenVersion) {
      _seenVersion = nav.lessonVersion;
      _lessonId = nav.openLessonId;
      _subjectId = nav.openSubjectId ?? _subjectId;
      if (_lessonId != null) {
        _subjectId = _subjectOfLesson(_lessonId!) ?? _subjectId;
      }
    }
    final t = BandTheme.forGrade(app.child!.grade);
    if (_error != null && _catalog == null) {
      return ErrorView(error: _error!, onRetry: () => _load(refresh: true));
    }
    if (_catalog == null) {
      return const LoadingView();
    }
    if (_lessonId != null) {
      return LessonReader(
        key: ValueKey('lesson-$_lessonId'),
        lessonId: _lessonId!,
        theme: t,
        onClose: () {
          setState(() => _lessonId = null);
          _load();
        },
      );
    }
    final subjects = asList(_catalog!['subjects']);
    if (_subjectId == null) {
      return RefreshIndicator(
        onRefresh: () => _load(refresh: true),
        child: ListView(padding: const EdgeInsets.all(20), children: [
          Text('${_catalog!['curriculum'] ?? 'Kurikulum'} · ${phaseFor(app.child!.grade)} · Kelas ${app.child!.grade}', style: const TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w600)),
          const SizedBox(height: 12),
          for (final s in subjects) ...[
            _row(t, s, () => setState(() => _subjectId = s['id'] as int)),
            const SizedBox(height: 12),
          ],
        ]),
      );
    }
    final s = subjects.firstWhere((x) => x['id'] == _subjectId, orElse: () => subjects.isEmpty ? <String, dynamic>{} : subjects.first);
    final allChapters = asList(s['chapters']);
    final semesters = {for (final ch in allChapters) ((ch['semester'] as num?) ?? 1).toInt()}.toList()..sort();
    final sem = semesters.contains(_semester) ? _semester! : (semesters.contains(_catalog!['semester']) ? (_catalog!['semester'] as num).toInt() : (semesters.isEmpty ? 1 : semesters.first));
    final chapters = allChapters.where((ch) => ((ch['semester'] as num?) ?? 1).toInt() == sem).toList();
    return ListView(padding: const EdgeInsets.fromLTRB(20, 8, 20, 24), children: [
      Align(
        alignment: Alignment.centerLeft,
        child: TextButton.icon(onPressed: () => setState(() => _subjectId = null), icon: const Icon(Icons.chevron_left_rounded), label: const Text('Mata pelajaran'), style: TextButton.styleFrom(foregroundColor: Palette.ink)),
      ),
      Text((s['name'] ?? '') as String, style: TextStyle(fontSize: t.title, fontWeight: FontWeight.w800)),
      const SizedBox(height: 12),
      if (semesters.length > 1) ...[
        SegmentedButton<int>(
          segments: [for (final x in semesters) ButtonSegment<int>(value: x, label: Text('Semester $x'), icon: x == _catalog!['semester'] ? const Icon(Icons.today_rounded, size: 18) : null)],
          selected: {sem},
          showSelectedIcon: false,
          onSelectionChanged: (v) => setState(() => _semester = v.first),
          style: SegmentedButton.styleFrom(selectedBackgroundColor: t.soft, selectedForegroundColor: t.ink, minimumSize: const Size(0, 44)),
        ),
        const SizedBox(height: 16),
      ],
      if (s['ready'] != true)
        AppCard(
          radius: t.radius,
          child: EmptyState(icon: Icons.menu_book_outlined, iconColor: t.accent, title: 'Materi belum tersedia', body: 'Materi ${s['name']} Kelas ${app.child!.grade} belum ada di versi ini. Materi baru akan datang lewat pembaruan aplikasi.'),
        ),
      for (final ch in chapters) ...[
        Text('Bab ${ch['number']} · ${ch['title']}', style: const TextStyle(fontSize: 14, color: Palette.muted, fontWeight: FontWeight.w700)),
        const SizedBox(height: 10),
        for (final (i, tp) in asList(ch['topics']).indexed) ...[
          _topicCard(t, tp, i + 1),
          const SizedBox(height: 12),
        ],
      ],
    ]);
  }

  int? _subjectOfLesson(int lessonId) {
    if (_catalog == null) {
      return null;
    }
    for (final s in asList(_catalog!['subjects'])) {
      for (final ch in asList(s['chapters'])) {
        for (final tp in asList(ch['topics'])) {
          final l = tp['lesson'];
          if (l != null && (l as Map)['id'] == lessonId) {
            return s['id'] as int;
          }
        }
      }
    }
    return null;
  }

  Widget _row(BandTheme t, Map<String, dynamic> s, VoidCallback onTap) {
    return Material(
      color: Palette.surface,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radius), side: const BorderSide(color: Palette.border)),
      child: InkWell(
        borderRadius: BorderRadius.circular(t.radius),
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Row(children: [
            Container(width: 44, height: 44, alignment: Alignment.center, decoration: BoxDecoration(color: t.soft, borderRadius: BorderRadius.circular(12)), child: Text(s['short_label'] as String, style: TextStyle(color: t.ink, fontWeight: FontWeight.w800))),
            const SizedBox(width: 14),
            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(s['name'] as String, style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w700)),
              Text(s['ready'] == true ? '${s['topic_count']} topik' : 'Belum tersedia', style: const TextStyle(fontSize: 13, color: Palette.muted)),
            ])),
            const Icon(Icons.chevron_right_rounded, color: Palette.muted),
          ]),
        ),
      ),
    );
  }

  Widget _topicCard(BandTheme t, Map<String, dynamic> tp, int n) {
    final nav = context.read<ChildNav>();
    final lesson = tp['lesson'] == null ? null : asMap(tp['lesson']);
    final nq = (tp['question_count'] as num).toInt();
    return AppCard(
      radius: t.radius,
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Container(width: 32, height: 32, alignment: Alignment.center, decoration: BoxDecoration(color: t.soft, borderRadius: BorderRadius.circular(10)), child: Text('$n', style: TextStyle(color: t.ink, fontWeight: FontWeight.w800))),
          const SizedBox(width: 12),
          Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(tp['title'] as String, style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w700)),
            const SizedBox(height: 4),
            Text(lesson != null ? '${lesson['minutes']} menit · ${lesson['block_count']} bagian' : 'Materi belum tersedia', style: const TextStyle(fontSize: 13, color: Palette.muted)),
          ])),
          if (lesson != null && lesson['completed'] == true) const Tag('✓ Selesai', fg: Palette.okInk, bg: Palette.okSoft),
        ]),
        const SizedBox(height: 12),
        Wrap(spacing: 8, runSpacing: 8, children: [
          if (lesson != null)
            FilledButton(
              onPressed: () => setState(() => _lessonId = lesson['id'] as int),
              style: FilledButton.styleFrom(backgroundColor: t.accent, minimumSize: const Size(0, 44), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
              child: const Text('Buka materi', style: TextStyle(fontWeight: FontWeight.w700)),
            ),
          if (nq > 0)
            OutlinedButton(
              onPressed: () => nav.practice(tp['id'] as int),
              style: OutlinedButton.styleFrom(minimumSize: const Size(0, 44), foregroundColor: Palette.ink, side: const BorderSide(color: Palette.borderStrong), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
              child: Text('Latihan · $nq soal'),
            ),
        ]),
      ]),
    );
  }
}

class LessonReader extends StatefulWidget {
  const LessonReader({super.key, required this.lessonId, required this.theme, required this.onClose});

  final int lessonId;
  final BandTheme theme;
  final VoidCallback onClose;

  @override
  State<LessonReader> createState() => _LessonReaderState();
}

class _LessonReaderState extends State<LessonReader> {
  Map<String, dynamic>? _lesson;
  Object? _error;
  int _step = 0;
  int _spoken = -1;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final app = context.read<AppState>();
    try {
      final l = asMap(await app.student('GET', '/student/lessons/${widget.lessonId}'));
      if (mounted) {
        setState(() {
          _lesson = l;
          _step = ((l['completed'] == true) ? 0 : (l['step'] as num).toInt());
        });
      }
    } on ApiException catch (e) {
      if (mounted) {
        setState(() => _error = e);
      }
    }
  }

  Future<void> _saveProgress(int step, bool completed) async {
    final app = context.read<AppState>();
    try {
      await app.student('POST', '/student/lessons/${widget.lessonId}/progress', body: {'step': step, 'completed': completed});
    } on ApiException catch (e) {
      if (mounted) {
        showToast(context, e.message);
      }
    }
  }

  Future<void> _next() async {
    Speech.instance.stop();
    final blocks = asList(_lesson!['blocks']);
    final nav = context.read<ChildNav>();
    if (_step + 1 < blocks.length) {
      setState(() => _step++);
      await _saveProgress(_step, false);
      return;
    }
    await _saveProgress(_step, true);
    if (!mounted) {
      return;
    }
    showToast(context, Persona.forGrade(context.read<AppState>().child!.grade).lessonDone());
    widget.onClose();
    nav.practice(_lesson!['topic_id'] as int);
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    if (_error != null) {
      return ErrorView(error: _error!, onRetry: () {
        setState(() => _error = null);
        _load();
      });
    }
    if (_lesson == null) {
      return const LoadingView();
    }
    final blocks = asList(_lesson!['blocks']);
    final b = blocks[_step.clamp(0, blocks.length - 1)];
    final points = (b['points'] as List?)?.map((e) => e.toString().trim()).where((e) => e.isNotEmpty).toList();
    final last = _step + 1 >= blocks.length;
    final app = context.read<AppState>();
    final child = app.child!;
    final persona = Persona.forGrade(child.grade);
    final kind = b['kind'] as String;
    final bodyText = (b['text'] as String?)?.trim();
    final speakText = [if (bodyText != null && bodyText.isNotEmpty) bodyText, ...?points].join('\n');
    final intro = '${_step == 0 ? '${persona.lessonIntro(child.nickname, _lesson!['title'] as String, (_lesson!['minutes'] as num).toInt())} ' : ''}${persona.blockIntro(kind)}';
    final pointOffsets = <int>[];
    var offset = bodyText == null || bodyText.isEmpty ? 0 : segmentsOf(bodyText).length;
    for (final p in points ?? const <String>[]) {
      pointOffsets.add(offset);
      offset += segmentsOf(p).length;
    }
    final lineHeight = persona.young ? 1.8 : 1.65;
    if (_spoken != _step && app.setting('read_aloud')) {
      _spoken = _step;
      WidgetsBinding.instance.addPostFrameCallback((_) => Speech.instance.speak(speakText, intro: intro));
    }
    return ListView(padding: const EdgeInsets.fromLTRB(20, 16, 20, 24), children: [
      Row(children: List.generate(blocks.length, (i) => Expanded(
            child: Container(height: 6, margin: EdgeInsets.only(right: i == blocks.length - 1 ? 0 : 6), decoration: BoxDecoration(color: i <= _step ? t.accent : const Color(0xFFE2E8F0), borderRadius: BorderRadius.circular(999))),
          ))),
      const SizedBox(height: 14),
      Row(children: [
        Tag('Bagian ${_step + 1} dari ${blocks.length} · ${persona.blockLabel(kind)}', fg: t.ink, bg: t.soft, size: 13),
        const Spacer(),
        if (_lesson!['reviewed'] == true) const Tag('✓ Sudah ditinjau', fg: Palette.okInk, bg: Palette.okSoft),
      ]),
      const SizedBox(height: 14),
      Text(_lesson!['title'] as String, style: TextStyle(fontSize: t.title, fontWeight: FontWeight.w800, height: 1.2)),
      Text('${_lesson!['minutes']} menit${_lesson!['sample'] == true ? ' · draf materi, belum ditinjau guru' : ''}', style: const TextStyle(fontSize: 13, color: Palette.muted)),
      const SizedBox(height: 16),
      AppCard(
        radius: t.radius,
        padding: const EdgeInsets.all(20),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Row(children: [
            const Spacer(),
            SpeakButton(text: speakText, intro: intro, color: t.ink, label: persona.young ? 'Dengarkan BOBO' : 'Dengarkan'),
          ]),
          if (b['visual'] != null) ...[
            LessonVisual(kind: b['visual'] as String, theme: t),
            Align(
              alignment: Alignment.centerLeft,
              child: TextButton.icon(
                onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => PlaygroundScreen(kind: b['visual'] as String, theme: t))),
                icon: const Icon(Icons.touch_app_rounded, size: 18),
                label: const Text('Coba sendiri di alat peraga'),
                style: TextButton.styleFrom(foregroundColor: t.ink, minimumSize: const Size(0, 44)),
              ),
            ),
            const SizedBox(height: 8),
          ],
          if (bodyText != null && bodyText.isNotEmpty) ReadAlongText(speechKey: speakText, text: bodyText, offset: 0, style: TextStyle(fontSize: t.body, height: lineHeight, color: Palette.ink), highlight: t.soft),
          if (points != null)
            for (final (pi, p) in points.indexed)
              Padding(
                padding: const EdgeInsets.only(bottom: 12),
                child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Container(width: 24, height: 24, alignment: Alignment.center, decoration: BoxDecoration(color: t.soft, shape: BoxShape.circle), child: Icon(Icons.check_rounded, size: 15, color: t.ink)),
                  const SizedBox(width: 12),
                  Expanded(child: ReadAlongText(speechKey: speakText, text: p, offset: pointOffsets[pi], style: TextStyle(fontSize: t.body, height: 1.5, color: Palette.ink), highlight: t.soft)),
                ]),
              ),
        ]),
      ),
      const SizedBox(height: 16),
      OutlinedButton.icon(
        onPressed: () => context.read<ChildNav>().askTutor('Jelaskan lagi tentang ${_lesson!['title']}'),
        icon: const Icon(Icons.chat_bubble_outline_rounded, size: 18),
        label: const Text('Masih bingung? Tanya Tutor BOBO'),
        style: OutlinedButton.styleFrom(minimumSize: const Size(0, 48), foregroundColor: t.ink, side: BorderSide(color: t.accent), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
      ),
      const SizedBox(height: 12),
      Row(children: [
        Expanded(child: SecondaryButton(label: _step == 0 ? 'Daftar topik' : 'Sebelumnya', radius: t.radiusSmall, onPressed: () {
          if (_step == 0) {
            widget.onClose();
          } else {
            setState(() => _step--);
          }
        })),
        const SizedBox(width: 12),
        Expanded(child: PrimaryButton(label: last ? 'Selesai & latihan' : 'Berikutnya', color: t.accent, radius: t.radiusSmall, onPressed: _next)),
      ]),
    ]);
  }
}
