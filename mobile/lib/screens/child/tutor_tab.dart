import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/api.dart';
import '../../core/models.dart';
import '../../core/speech.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';
import '../../widgets/playground.dart';
import '../../widgets/visuals.dart';
import 'child_shell.dart';

class _Msg {
  _Msg(this.me, this.text, {this.source, this.flagged = false, this.question, this.visual, this.canRestyle = false, this.style});

  final bool me;
  final String text;
  final String? source;
  final bool flagged;
  final String? question;
  final String? visual;
  final bool canRestyle;
  final String? style;
}

class TutorTab extends StatefulWidget {
  const TutorTab({super.key});

  @override
  State<TutorTab> createState() => _TutorTabState();
}

class _TutorTabState extends State<TutorTab> {
  final List<_Msg> _msgs = [];
  final _input = TextEditingController();
  final _scroll = ScrollController();
  String? _conversationId;
  int? _left;
  int _limit = 10;
  bool _typing = false;
  List<String> _starters = [];
  bool _hasContent = true;

  @override
  void initState() {
    super.initState();
    _loadMeta();
  }

  @override
  void dispose() {
    _input.dispose();
    _scroll.dispose();
    super.dispose();
  }

  Future<void> _loadMeta() async {
    final app = context.read<AppState>();
    try {
      final cat = await CatalogCache.load(app);
      final topics = <String>[];
      for (final s in asList(cat['subjects'])) {
        for (final ch in asList(s['chapters'])) {
          for (final tp in asList(ch['topics'])) {
            topics.add(tp['title'] as String);
          }
        }
      }
      final q = asMap(await app.student('GET', '/student/tutor/quota'));
      if (!mounted) {
        return;
      }
      setState(() {
        _hasContent = topics.isNotEmpty;
        _left = (q['left'] as num).toInt();
        _limit = (q['limit'] as num).toInt();
        _starters = topics.isEmpty
            ? []
            : [
                'Apa itu ${topics.first.toLowerCase()}?',
                if (topics.length > 1) 'Beri aku petunjuk tentang ${topics[1].toLowerCase()}',
                'Buatkan 1 contoh soal ${topics.first.toLowerCase()}',
                if (topics.length > 2) 'Jelaskan ${topics[2].toLowerCase()}',
              ];
      });
    } catch (_) {}
  }

  void _toBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scroll.hasClients) {
        _scroll.animateTo(_scroll.position.maxScrollExtent, duration: const Duration(milliseconds: 250), curve: Curves.easeOut);
      }
    });
  }

  Future<void> _send(String text, {String? style}) async {
    final app = context.read<AppState>();
    final v = text.trim();
    if (v.isEmpty || _typing || app.offline || (_left != null && _left! <= 0)) {
      return;
    }
    const styleLabel = {'story': 'Jelaskan lewat cerita', 'visual': 'Jelaskan dengan gambar', 'steps': 'Jelaskan langkah demi langkah'};
    setState(() {
      _msgs.add(_Msg(true, style == null ? v : '${styleLabel[style]}: $v'));
      _typing = true;
      _input.clear();
    });
    _toBottom();
    try {
      final r = asMap(await app.student('POST', '/student/tutor/messages', body: {'text': v, if (_conversationId != null) 'conversation_id': _conversationId, if (style != null) 'style': style}));
      final sources = ((r['sources'] as List?) ?? const []).map((e) => e.toString()).toList();
      if (!mounted) {
        return;
      }
      setState(() {
        _conversationId = r['conversation_id'] as String?;
        _left = (r['quota_left'] as num).toInt();
        _limit = (r['quota_limit'] as num).toInt();
        _msgs.add(_Msg(false, r['reply'] as String, source: r['refused'] == true ? 'Pengaman anak · permintaan ditolak' : (sources.isEmpty ? null : 'Sumber · ${sources.join(' · ')}'), flagged: r['refused'] == true, question: v, visual: r['visual'] as String?, canRestyle: r['can_restyle'] == true && r['refused'] != true, style: style));
      });
      if (app.setting('read_aloud')) {
        Speech.instance.speak(r['reply'] as String);
      }
    } on ApiException catch (e) {
      if (!mounted) {
        return;
      }
      setState(() {
        if (e.status == 429) {
          _left = 0;
        }
        _msgs.add(_Msg(false, e.message, flagged: true));
      });
    } finally {
      if (mounted) {
        setState(() => _typing = false);
        _toBottom();
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    final nav = context.watch<ChildNav>();
    final t = BandTheme.forGrade(app.child!.grade);
    if (nav.tab == 4 && nav.tutorPrompt != null) {
      final p = nav.takeTutorPrompt();
      WidgetsBinding.instance.addPostFrameCallback((_) => _send(p ?? ''));
    }
    if (!_hasContent) {
      return EmptyState(icon: Icons.chat_bubble_outline_rounded, iconColor: t.accent, title: 'Tutor belum aktif untuk Kelas ${app.child!.grade}', body: 'Tutor BOBO menjawab dari materi yang sudah ditinjau. Ia akan aktif setelah materi kelasmu tersedia.');
    }
    final out = _left != null && _left! <= 0;
    final disabled = app.offline || out || _typing;
    final note = app.offline ? 'Tutor butuh internet. Materi yang sudah diunduh tetap bisa dibaca.' : (out ? 'Batas pertanyaan Tutor hari ini sudah tercapai. Kamu tetap bisa membaca materi dan berlatih. Besok bisa bertanya lagi.' : null);
    return Column(children: [
      Expanded(
        child: ListView(controller: _scroll, padding: const EdgeInsets.fromLTRB(16, 16, 16, 20), children: [
          AppCard(
            radius: 16,
            padding: const EdgeInsets.all(12),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Tag('AI', fg: t.ink, bg: t.soft, size: 11),
              const SizedBox(width: 10),
              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                const Text('Tutor menjawab dari materi di aplikasi ini dan memberi petunjuk, bukan jawaban PR langsung. Tidak perlu internet.', style: TextStyle(fontSize: 13, height: 1.5, color: Palette.inkSoft)),
                const SizedBox(height: 4),
                Text('Sisa ${_left ?? '-'} dari $_limit pertanyaan hari ini', style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w700, color: Palette.muted)),
              ])),
            ]),
          ),
          const SizedBox(height: 12),
          for (final m in _msgs) ...[
            Align(
              alignment: m.me ? Alignment.centerRight : Alignment.centerLeft,
              child: ConstrainedBox(
                constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.82),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                  decoration: BoxDecoration(
                    color: m.me ? t.accent : (m.flagged ? const Color(0xFFFFFBEB) : Palette.surface),
                    border: Border.all(color: m.me ? t.accent : (m.flagged ? const Color(0xFFFCD34D) : Palette.border)),
                    borderRadius: BorderRadius.only(topLeft: const Radius.circular(18), topRight: const Radius.circular(18), bottomLeft: Radius.circular(m.me ? 18 : 4), bottomRight: Radius.circular(m.me ? 4 : 18)),
                  ),
                  child: Text(m.text, style: TextStyle(fontSize: t.body, height: 1.5, color: m.me ? Colors.white : Palette.ink)),
                ),
              ),
            ),
            if (m.source != null) Padding(padding: const EdgeInsets.only(top: 4, left: 4), child: Text(m.source!, style: const TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w600))),
            if (!m.me && m.visual != null) ...[
              const SizedBox(height: 8),
              LessonVisual(kind: m.visual!, theme: t),
              Align(
                alignment: Alignment.centerLeft,
                child: TextButton.icon(
                  onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => PlaygroundScreen(kind: m.visual!, theme: t))),
                  icon: const Icon(Icons.touch_app_rounded, size: 18),
                  label: const Text('Coba di alat peraga'),
                  style: TextButton.styleFrom(foregroundColor: t.ink, minimumSize: const Size(0, 44)),
                ),
              ),
            ],
            if (!m.me && !m.flagged)
              Row(children: [
                SpeakButton(text: m.text, color: t.ink),
                if (m.canRestyle && identical(m, _msgs.last))
                  Expanded(
                    child: SingleChildScrollView(
                      scrollDirection: Axis.horizontal,
                      child: Row(children: [
                        const Text('Belum paham? ', style: TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w700)),
                        for (final e in const [['story', 'Cerita'], ['visual', 'Gambar'], ['steps', 'Langkah']])
                          if (e[0] != m.style)
                            Padding(
                              padding: const EdgeInsets.only(right: 6),
                              child: ActionChip(
                                label: Text(e[1]),
                                onPressed: disabled ? null : () => _send(m.question!, style: e[0]),
                                backgroundColor: t.soft,
                                side: BorderSide.none,
                                labelStyle: TextStyle(fontWeight: FontWeight.w700, color: t.ink, fontSize: 13),
                              ),
                            ),
                      ]),
                    ),
                  ),
              ]),
            const SizedBox(height: 10),
          ],
          if (_typing) const Align(alignment: Alignment.centerLeft, child: Text('BOBO sedang menulis…', style: TextStyle(fontSize: 14, color: Palette.muted, fontWeight: FontWeight.w600))),
          if (_starters.isNotEmpty) ...[
            const SizedBox(height: 8),
            const Text('Coba tanyakan:', style: TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w700)),
            const SizedBox(height: 8),
            Wrap(spacing: 8, runSpacing: 8, children: [
              for (final s in _starters)
                ActionChip(label: Text(s), onPressed: disabled ? null : () => _send(s), backgroundColor: Palette.surface, side: const BorderSide(color: Palette.borderStrong), labelStyle: const TextStyle(fontWeight: FontWeight.w600, color: Palette.ink)),
            ]),
          ],
        ]),
      ),
      Container(
        color: Palette.surface,
        padding: const EdgeInsets.fromLTRB(12, 10, 12, 10),
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          if (note != null) ...[Notice(note), const SizedBox(height: 6)],
          Row(children: [
            Expanded(
              child: TextField(
                controller: _input,
                enabled: !disabled,
                maxLength: 500,
                textInputAction: TextInputAction.send,
                onSubmitted: _send,
                decoration: const InputDecoration(hintText: 'Tanya tentang materi…', counterText: '', semanticCounterText: ''),
              ),
            ),
            const SizedBox(width: 8),
            SizedBox(
              width: 48,
              height: 48,
              child: IconButton.filled(
                onPressed: disabled ? null : () => _send(_input.text),
                icon: const Icon(Icons.send_rounded),
                tooltip: 'Kirim pertanyaan',
                style: IconButton.styleFrom(backgroundColor: t.accent, foregroundColor: Colors.white, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14))),
              ),
            ),
          ]),
        ]),
      ),
    ]);
  }
}
