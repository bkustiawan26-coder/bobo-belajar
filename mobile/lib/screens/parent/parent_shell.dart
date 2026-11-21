import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/api.dart';
import '../../core/models.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';

class ParentShell extends StatefulWidget {
  const ParentShell({super.key});

  @override
  State<ParentShell> createState() => _ParentShellState();
}

class _ParentShellState extends State<ParentShell> {
  int _tab = 0;
  String? _childId;
  static const _titles = ['Dashboard', 'Anak', 'Perkembangan', 'Rekomendasi', 'Tanya BOBO'];

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    if (_childId == null || !app.children.any((c) => c.id == _childId)) {
      _childId = app.children.isEmpty ? null : app.children.first.id;
    }
    final child = app.children.where((c) => c.id == _childId).firstOrNull;
    Widget body;
    if (_tab == 1) {
      body = const _ChildrenTab();
    } else if (child == null) {
      body = EmptyState(icon: Icons.group_add_outlined, title: 'Belum ada profil anak', body: 'Tambahkan profil anak di menu Anak untuk mulai.', action: SizedBox(width: 220, child: PrimaryButton(label: 'Tambah anak', onPressed: () => setState(() => _tab = 1))));
    } else {
      final content = switch (_tab) {
        0 => _DashboardTab(key: ValueKey('d-${child.id}'), child: child, onSeeRecs: () => setState(() => _tab = 3), onSeeProgress: () => setState(() => _tab = 2)),
        2 => _ProgressTab(key: ValueKey('p-${child.id}'), child: child),
        3 => _RecsTab(key: ValueKey('r-${child.id}'), child: child),
        _ => _AskTab(key: ValueKey('a-${child.id}'), child: child),
      };
      body = Column(children: [
        SizedBox(
          height: 64,
          child: ListView(scrollDirection: Axis.horizontal, padding: const EdgeInsets.fromLTRB(20, 12, 20, 8), children: [
            for (final c in app.children)
              Padding(
                padding: const EdgeInsets.only(right: 8),
                child: ChoiceChip(
                  avatar: CircleAvatar(backgroundColor: BandTheme.forGrade(c.grade).accent, child: Text(c.initial, style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.w800))),
                  label: Text(c.nickname),
                  selected: c.id == _childId,
                  showCheckmark: false,
                  onSelected: (_) => setState(() => _childId = c.id),
                  selectedColor: Palette.parent,
                  backgroundColor: Palette.surface,
                  labelStyle: TextStyle(color: c.id == _childId ? Colors.white : Palette.ink, fontWeight: FontWeight.w700),
                  side: BorderSide(color: c.id == _childId ? Palette.parent : Palette.borderStrong),
                  shape: const StadiumBorder(),
                ),
              ),
          ]),
        ),
        Expanded(child: content),
      ]);
    }
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) {
          app.lock();
        }
      },
      child: Scaffold(
        appBar: AppBar(
          backgroundColor: Palette.parent,
          foregroundColor: Colors.white,
          automaticallyImplyLeading: false,
          title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(_titles[_tab], style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 18, color: Colors.white)),
            const Text('Mode Orang Tua', style: TextStyle(fontSize: 13, color: Colors.white)),
          ]),
          actions: [
            Padding(
              padding: const EdgeInsets.only(right: 12),
              child: OutlinedButton.icon(
                onPressed: app.lock,
                icon: const Icon(Icons.lock_outline_rounded, size: 18),
                label: const Text('Kunci'),
                style: OutlinedButton.styleFrom(foregroundColor: Colors.white, side: const BorderSide(color: Colors.white70), minimumSize: const Size(44, 44)),
              ),
            ),
          ],
        ),
        body: body,
        bottomNavigationBar: NavigationBar(
          selectedIndex: _tab,
          onDestinationSelected: (i) => setState(() => _tab = i),
          backgroundColor: Palette.surface,
          indicatorColor: Palette.parentSoft,
          labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
          destinations: const [
            NavigationDestination(icon: Icon(Icons.dashboard_outlined), selectedIcon: Icon(Icons.dashboard_rounded), label: 'Dashboard'),
            NavigationDestination(icon: Icon(Icons.groups_outlined), selectedIcon: Icon(Icons.groups_rounded), label: 'Anak'),
            NavigationDestination(icon: Icon(Icons.trending_up_rounded), label: 'Perkembangan'),
            NavigationDestination(icon: Icon(Icons.lightbulb_outline_rounded), selectedIcon: Icon(Icons.lightbulb_rounded), label: 'Rekomendasi'),
            NavigationDestination(icon: Icon(Icons.chat_bubble_outline_rounded), selectedIcon: Icon(Icons.chat_bubble_rounded), label: 'Tanya BOBO'),
          ],
        ),
      ),
    );
  }
}

class _Loader extends StatefulWidget {
  const _Loader({required this.load, required this.builder});

  final Future<Map<String, dynamic>> Function() load;
  final Widget Function(Map<String, dynamic> data, Future<void> Function() reload) builder;

  @override
  State<_Loader> createState() => _LoaderState();
}

class _LoaderState extends State<_Loader> {
  Map<String, dynamic>? _data;
  Object? _error;

  @override
  void initState() {
    super.initState();
    _reload();
  }

  Future<void> _reload() async {
    try {
      final d = await widget.load();
      if (mounted) {
        setState(() {
          _data = d;
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
    if (_error != null && _data == null) {
      return ErrorView(error: _error!, onRetry: _reload);
    }
    if (_data == null) {
      return const LoadingView();
    }
    return RefreshIndicator(onRefresh: _reload, child: widget.builder(_data!, _reload));
  }
}

class _DashboardTab extends StatelessWidget {
  const _DashboardTab({super.key, required this.child, required this.onSeeRecs, required this.onSeeProgress});

  final ChildInfo child;
  final VoidCallback onSeeRecs;
  final VoidCallback onSeeProgress;

  @override
  Widget build(BuildContext context) {
    final app = context.read<AppState>();
    return _Loader(
      load: () async => asMap(await app.parent('GET', '/parent/children/${child.id}/dashboard')),
      builder: (d, reload) {
        final k = asMap(d['kpis']);
        final last = k['last_assessment'] == null ? null : asMap(k['last_assessment']);
        final top = d['top_recommendation'] == null ? null : asMap(d['top_recommendation']);
        final mastery = asList(d['mastery']);
        final activity = asList(d['activity']);
        final tiles = [
          ('Materi selesai', '${k['lessons_completed']}', 'topik dibaca sampai tuntas'),
          ('Soal dikerjakan', '${k['answers_total']}', 'latihan dan asesmen'),
          ('Ketepatan', k['accuracy_pct'] == null ? '–' : '${k['accuracy_pct']}%', k['answers_total'] == 0 ? 'belum ada jawaban' : '${k['answers_correct']} dari ${k['answers_total']} jawaban benar'),
          ('Asesmen terakhir', last == null ? '–' : '${last['score']}', last == null ? 'belum ada asesmen' : '${last['date']} · ${last['final'] == true ? 'terverifikasi' : 'menunggu esai'}'),
        ];
        return ListView(padding: const EdgeInsets.fromLTRB(20, 8, 20, 24), children: [
          AppCard(
            child: Row(children: [
              Avatar(child.initial, color: BandTheme.forGrade(child.grade).accent, size: 52, radius: 16),
              const SizedBox(width: 14),
              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(child.nickname, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
                Text(gradeLabel(child.grade), style: const TextStyle(fontSize: 13, color: Palette.muted)),
                Text('Terakhir aktif: ${d['last_active'] ?? '–'}', style: const TextStyle(fontSize: 13, color: Palette.muted)),
              ])),
            ]),
          ),
          const SizedBox(height: 16),
          GridView.count(
            crossAxisCount: 2,
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            mainAxisSpacing: 12,
            crossAxisSpacing: 12,
            childAspectRatio: 1.35,
            children: [
              for (final (label, value, sub) in tiles)
                AppCard(
                  radius: 16,
                  padding: const EdgeInsets.all(14),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
                    Text(label, style: const TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w600)),
                    Text(value, style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w800, fontFeatures: [])),
                    Text(sub, maxLines: 2, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 12, color: Palette.muted, height: 1.35)),
                  ]),
                ),
            ],
          ),
          if (top != null) ...[
            const SizedBox(height: 16),
            AppCard(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                const Row(children: [Icon(Icons.lightbulb_outline_rounded, color: Palette.parent), SizedBox(width: 8), Text('Saran minggu ini', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800))]),
                const SizedBox(height: 10),
                Text(top['title'] as String, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700, height: 1.35)),
                const SizedBox(height: 8),
                Notice('Dasar: ${top['evidence']}', fg: Palette.inkSoft, bg: const Color(0xFFF1F5F9)),
                const SizedBox(height: 8),
                Text(top['activity'] as String, style: const TextStyle(fontSize: 14, height: 1.55)),
                const SizedBox(height: 12),
                SizedBox(width: 240, child: PrimaryButton(label: 'Lihat semua rekomendasi', height: 44, onPressed: onSeeRecs)),
              ]),
            ),
          ],
          if (mastery.isNotEmpty) ...[
            const SizedBox(height: 16),
            AppCard(
              padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
              child: Column(children: [
                Row(children: [
                  const Expanded(child: Text('Topik', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800))),
                  TextButton(onPressed: onSeeProgress, child: const Text('Detail')),
                ]),
                for (final m in mastery)
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    child: Row(children: [
                      Expanded(child: Text(m['topic'] as String, style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w600))),
                      MasteryChip(state: m['state'] as String, label: m['label'] as String),
                    ]),
                  ),
              ]),
            ),
          ],
          const SizedBox(height: 16),
          AppCard(
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Text('Aktivitas terbaru', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
              const SizedBox(height: 6),
              if (activity.isEmpty) const Padding(padding: EdgeInsets.symmetric(vertical: 10), child: Text('Belum ada aktivitas.', style: TextStyle(color: Palette.muted))),
              for (final a in activity)
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 9),
                  child: Row(children: [
                    Expanded(child: Text(a['text'] as String, style: const TextStyle(fontSize: 14, height: 1.4))),
                    const SizedBox(width: 8),
                    Text(a['when'] as String, style: const TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w600)),
                  ]),
                ),
            ]),
          ),
        ]);
      },
    );
  }
}

class _ProgressTab extends StatelessWidget {
  const _ProgressTab({super.key, required this.child});

  final ChildInfo child;

  @override
  Widget build(BuildContext context) {
    final app = context.read<AppState>();
    return _Loader(
      load: () async => asMap(await app.parent('GET', '/parent/children/${child.id}/dashboard')),
      builder: (d, reload) {
        final mastery = asList(d['mastery']);
        final exams = asList(d['assessments']);
        return ListView(padding: const EdgeInsets.fromLTRB(20, 8, 20, 24), children: [
          const AppCard(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('Arti status', style: TextStyle(fontSize: 14, fontWeight: FontWeight.w800)),
              SizedBox(height: 10),
              Wrap(spacing: 8, runSpacing: 8, children: [
                MasteryChip(state: 'not_started', label: 'Belum mulai'),
                MasteryChip(state: 'insufficient', label: 'Bukti belum cukup'),
                MasteryChip(state: 'developing', label: 'Berkembang'),
                MasteryChip(state: 'demonstrated', label: 'Menunjukkan pemahaman'),
              ]),
              SizedBox(height: 10),
              Text('BOBO baru menilai setelah minimal 3 jawaban per topik, dan memakai 5 jawaban terakhir. Satu jawaban benar belum dianggap paham.', style: TextStyle(fontSize: 13, color: Palette.muted, height: 1.5)),
            ]),
          ),
          const SizedBox(height: 16),
          if (mastery.isEmpty)
            AppCard(child: Text('Belum ada data. Materi Kelas ${child.grade} masih disiapkan, jadi ${child.nickname} belum bisa berlatih.', style: const TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)))
          else
            AppCard(
              padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                const Text('Topik', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
                for (final m in mastery)
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Row(children: [
                        Expanded(child: Text(m['topic'] as String, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700))),
                        MasteryChip(state: m['state'] as String, label: m['label'] as String),
                      ]),
                      const SizedBox(height: 8),
                      Row(children: [
                        ExcludeSemantics(
                          child: Row(children: [
                            for (final ok in ((m['recent'] as List?) ?? const []))
                              Container(
                                width: 20,
                                height: 20,
                                margin: const EdgeInsets.only(right: 4),
                                alignment: Alignment.center,
                                decoration: BoxDecoration(color: ok == true ? Palette.ok : Palette.badSoft, borderRadius: BorderRadius.circular(5)),
                                child: Text(ok == true ? '✓' : '✕', style: TextStyle(fontSize: 11, fontWeight: FontWeight.w800, color: ok == true ? Colors.white : Palette.badInk)),
                              ),
                          ]),
                        ),
                        const SizedBox(width: 6),
                        Expanded(child: Text(m['evidence'] as String, style: const TextStyle(fontSize: 13, color: Palette.muted))),
                      ]),
                    ]),
                  ),
              ]),
            ),
          const SizedBox(height: 16),
          AppCard(
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Text('Riwayat asesmen', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
              if (exams.isEmpty) const Padding(padding: EdgeInsets.symmetric(vertical: 10), child: Text('Belum ada asesmen.', style: TextStyle(color: Palette.muted))),
              for (final e in exams)
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 10),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [
                      Expanded(child: Text(e['title'] as String, style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w700, height: 1.4))),
                      Text('${e['score']}', style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w800)),
                    ]),
                    const SizedBox(height: 4),
                    Row(children: [
                      Text(e['date'] as String, style: const TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w600)),
                      const SizedBox(width: 8),
                      e['final'] == true ? const Tag('✓ Terverifikasi', fg: Palette.okInk, bg: Palette.okSoft, size: 11) : const Tag('Menunggu penilaian esai', fg: Palette.warnInk, bg: Palette.warnSoft, size: 11),
                    ]),
                    const SizedBox(height: 4),
                    Text(((e['weak_topics'] as List?) ?? const []).isEmpty ? 'Semua topik terjawab benar' : 'Perlu dilatih: ${(e['weak_topics'] as List).join(', ')}', style: const TextStyle(fontSize: 13, color: Palette.inkSoft)),
                  ]),
                ),
            ]),
          ),
        ]);
      },
    );
  }
}

class _RecsTab extends StatelessWidget {
  const _RecsTab({super.key, required this.child});

  final ChildInfo child;

  @override
  Widget build(BuildContext context) {
    final app = context.read<AppState>();
    return _Loader(
      load: () async => asMap(await app.parent('GET', '/parent/children/${child.id}/recommendations')),
      builder: (d, reload) {
        final recs = asList(d['recommendations']);
        return ListView(padding: const EdgeInsets.fromLTRB(20, 8, 20, 24), children: [
          Text('Disusun dari jawaban latihan dan asesmen ${child.nickname}. BOBO tidak menilai kecerdasan anak, hanya menunjukkan apa yang bisa dilatih.', style: const TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
          const SizedBox(height: 14),
          if (recs.isEmpty) const AppCard(child: Text('Belum ada data belajar untuk menyusun rekomendasi.', style: TextStyle(color: Palette.muted))),
          for (final r in recs) ...[
            AppCard(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Row(children: [
                  _kindTag(r['kind'] as String, r['kind_label'] as String),
                  const Spacer(),
                  const Icon(Icons.schedule_rounded, size: 14, color: Palette.muted),
                  const SizedBox(width: 4),
                  Text(r['duration'] as String, style: const TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w700)),
                ]),
                const SizedBox(height: 10),
                Text(r['title'] as String, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700, height: 1.35)),
                const SizedBox(height: 8),
                Notice('Dasar: ${r['evidence']}', fg: Palette.inkSoft, bg: const Color(0xFFF1F5F9)),
                const SizedBox(height: 8),
                Text(r['activity'] as String, style: const TextStyle(fontSize: 14, height: 1.55)),
                const SizedBox(height: 10),
                OutlinedButton(
                  onPressed: () async {
                    try {
                      await app.parent('POST', '/parent/children/${child.id}/recommendations/${r['id']}/done', body: {'done': r['done'] != true});
                      await reload();
                    } on ApiException catch (e) {
                      if (context.mounted) {
                        showToast(context, e.message);
                      }
                    }
                  },
                  style: OutlinedButton.styleFrom(
                    minimumSize: const Size(0, 44),
                    backgroundColor: r['done'] == true ? Palette.okSoft : Palette.surface,
                    foregroundColor: r['done'] == true ? Palette.okInk : Palette.ink,
                    side: BorderSide(color: r['done'] == true ? const Color(0xFF86EFAC) : Palette.borderStrong),
                  ),
                  child: Text(r['done'] == true ? '✓ Sudah dilakukan' : 'Tandai sudah dilakukan', style: const TextStyle(fontWeight: FontWeight.w700)),
                ),
              ]),
            ),
            const SizedBox(height: 14),
          ],
        ]);
      },
    );
  }

  Widget _kindTag(String kind, String label) {
    final (fg, bg) = switch (kind) {
      'practice' => (Palette.devInk, Palette.devSoft),
      'evidence' => (Palette.warnInk, Palette.warnSoft),
      'maintain' => (Palette.okInk, Palette.okSoft),
      _ => (Palette.inkSoft, Palette.neutralSoft),
    };
    return Tag(label, fg: fg, bg: bg);
  }
}

class _AskTab extends StatefulWidget {
  const _AskTab({super.key, required this.child});

  final ChildInfo child;

  @override
  State<_AskTab> createState() => _AskTabState();
}

class _AskTabState extends State<_AskTab> {
  final List<(bool, String, String?)> _msgs = [];
  final _input = TextEditingController();
  final _scroll = ScrollController();
  String? _conv;
  bool _typing = false;

  @override
  void dispose() {
    _input.dispose();
    _scroll.dispose();
    super.dispose();
  }

  Future<void> _send(String text) async {
    final v = text.trim();
    if (v.isEmpty || _typing) {
      return;
    }
    final app = context.read<AppState>();
    setState(() {
      _msgs.add((true, v, null));
      _typing = true;
      _input.clear();
    });
    try {
      final r = asMap(await app.parent('POST', '/parent/assistant/messages', body: {'child_id': widget.child.id, 'text': v, if (_conv != null) 'conversation_id': _conv}));
      if (mounted) {
        setState(() {
          _conv = r['conversation_id'] as String?;
          _msgs.add((false, r['reply'] as String, r['basis'] as String?));
        });
      }
    } on ApiException catch (e) {
      if (mounted) {
        setState(() => _msgs.add((false, e.message, null)));
      }
    } finally {
      if (mounted) {
        setState(() => _typing = false);
        WidgetsBinding.instance.addPostFrameCallback((_) {
          if (_scroll.hasClients) {
            _scroll.animateTo(_scroll.position.maxScrollExtent, duration: const Duration(milliseconds: 250), curve: Curves.easeOut);
          }
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final starters = ['Kenapa ${widget.child.nickname} kesulitan di topik ini?', 'Bagaimana cara menjelaskan materinya di rumah?', 'Apa yang sebaiknya dipelajari selanjutnya?', 'Bagaimana menyiapkan asesmen?', 'Bagaimana membangun rutinitas belajar yang sehat?'];
    return Column(children: [
      Expanded(
        child: ListView(controller: _scroll, padding: const EdgeInsets.fromLTRB(16, 8, 16, 16), children: [
          AppCard(
            radius: 16,
            padding: const EdgeInsets.all(12),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Tag('AI', fg: Palette.parent, bg: Palette.parentSoft, size: 11),
              const SizedBox(width: 10),
              Expanded(child: Text('Jawaban memakai data belajar ${widget.child.nickname} yang tercatat. Ini panduan belajar, bukan diagnosis psikologis atau medis.', style: const TextStyle(fontSize: 13, height: 1.5, color: Palette.inkSoft))),
            ]),
          ),
          const SizedBox(height: 12),
          for (final (me, text, basis) in _msgs) ...[
            Align(
              alignment: me ? Alignment.centerRight : Alignment.centerLeft,
              child: ConstrainedBox(
                constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.86),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                  decoration: BoxDecoration(
                    color: me ? Palette.parent : Palette.surface,
                    border: Border.all(color: me ? Palette.parent : Palette.border),
                    borderRadius: BorderRadius.only(topLeft: const Radius.circular(18), topRight: const Radius.circular(18), bottomLeft: Radius.circular(me ? 18 : 4), bottomRight: Radius.circular(me ? 4 : 18)),
                  ),
                  child: Text(text, style: TextStyle(fontSize: 15, height: 1.55, color: me ? Colors.white : Palette.ink)),
                ),
              ),
            ),
            if (basis != null) Padding(padding: const EdgeInsets.only(top: 4, left: 4), child: Text(basis, style: const TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w600))),
            const SizedBox(height: 10),
          ],
          if (_typing) const Text('BOBO sedang menyusun jawaban…', style: TextStyle(fontSize: 14, color: Palette.muted, fontWeight: FontWeight.w600)),
          const SizedBox(height: 8),
          const Text('Pertanyaan yang sering diajukan:', style: TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w700)),
          const SizedBox(height: 8),
          for (final s in starters)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: OutlinedButton(
                onPressed: _typing ? null : () => _send(s),
                style: OutlinedButton.styleFrom(alignment: Alignment.centerLeft, minimumSize: const Size(0, 44), foregroundColor: Palette.ink, backgroundColor: Palette.surface, side: const BorderSide(color: Palette.borderStrong), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12))),
                child: Text(s, style: const TextStyle(fontWeight: FontWeight.w600)),
              ),
            ),
        ]),
      ),
      Container(
        color: Palette.surface,
        padding: const EdgeInsets.fromLTRB(12, 10, 12, 10),
        child: Row(children: [
          Expanded(child: TextField(controller: _input, maxLength: 600, textInputAction: TextInputAction.send, onSubmitted: _send, decoration: const InputDecoration(hintText: 'Tanya tentang belajar anak…', counterText: ''))),
          const SizedBox(width: 8),
          SizedBox(
            width: 48,
            height: 48,
            child: IconButton.filled(
              onPressed: _typing ? null : () => _send(_input.text),
              icon: const Icon(Icons.send_rounded),
              tooltip: 'Kirim pertanyaan',
              style: IconButton.styleFrom(backgroundColor: Palette.parent, foregroundColor: Colors.white, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14))),
            ),
          ),
        ]),
      ),
    ]);
  }
}

class _ChildrenTab extends StatefulWidget {
  const _ChildrenTab();

  @override
  State<_ChildrenTab> createState() => _ChildrenTabState();
}

class _ChildrenTabState extends State<_ChildrenTab> {
  final _name = TextEditingController();
  int _grade = 3;
  String? _error;
  bool _busy = false;

  @override
  void dispose() {
    _name.dispose();
    super.dispose();
  }

  Future<void> _add() async {
    final app = context.read<AppState>();
    final name = _name.text.trim();
    if (name.length < 2) {
      setState(() => _error = 'Isi nama panggilan minimal 2 huruf.');
      return;
    }
    setState(() {
      _busy = true;
      _error = null;
    });
    try {
      final r = asMap(await app.parent('POST', '/parent/children', body: {'nickname': name, 'grade': _grade}));
      await app.fetchStudentToken(r['id'] as String);
      await app.loadChildren();
      _name.clear();
      if (mounted) {
        showToast(context, 'Profil $name ditambahkan');
      }
    } on ApiException catch (e) {
      if (mounted) {
        setState(() => _error = e.message);
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  Future<void> _delete(ChildInfo c) async {
    final app = context.read<AppState>();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text('Hapus profil ${c.nickname}?'),
        content: const Text('Semua riwayat belajar, nilai, dan percakapan Tutor profil ini akan dihapus permanen dan tidak bisa dikembalikan.'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Batal')),
          FilledButton(onPressed: () => Navigator.pop(ctx, true), style: FilledButton.styleFrom(backgroundColor: Palette.bad), child: const Text('Hapus permanen')),
        ],
      ),
    );
    if (ok != true) {
      return;
    }
    try {
      await app.parent('DELETE', '/parent/children/${c.id}');
      await app.store.setStudentToken(c.id, null);
      await app.loadChildren();
    } on ApiException catch (e) {
      if (mounted) {
        showToast(context, e.message);
      }
    }
  }

  Future<void> _export() async {
    final app = context.read<AppState>();
    try {
      final data = await app.parent('GET', '/parent/export');
      await Clipboard.setData(ClipboardData(text: const JsonEncoder.withIndent('  ').convert(data)));
      if (mounted) {
        showToast(context, 'Data akun disalin ke clipboard (format JSON).');
      }
    } on ApiException catch (e) {
      if (mounted) {
        showToast(context, e.message);
      }
    }
  }

  Future<void> _deleteAccount() async {
    final app = context.read<AppState>();
    final pw = TextEditingController();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Hapus akun?'),
        content: Column(mainAxisSize: MainAxisSize.min, children: [
          const Text('Akun orang tua dan semua profil anak beserta riwayat belajarnya akan dihapus permanen.'),
          const SizedBox(height: 12),
          TextField(controller: pw, obscureText: true, decoration: const InputDecoration(labelText: 'Kata sandi')),
        ]),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Batal')),
          FilledButton(onPressed: () => Navigator.pop(ctx, true), style: FilledButton.styleFrom(backgroundColor: Palette.bad), child: const Text('Hapus permanen')),
        ],
      ),
    );
    final password = pw.text;
    pw.dispose();
    if (ok != true) {
      return;
    }
    try {
      await app.parent('POST', '/parent/delete-account', body: {'password': password, 'confirm': 'HAPUS'});
      await app.logout();
    } on ApiException catch (e) {
      if (mounted) {
        showToast(context, e.message);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    return ListView(padding: const EdgeInsets.all(20), children: [
      Text('${app.children.length} profil anak terhubung ke akun ${app.parentName}.', style: const TextStyle(fontSize: 14, color: Palette.muted)),
      const SizedBox(height: 14),
      for (final c in app.children) ...[
        AppCard(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [
              Avatar(c.initial, color: BandTheme.forGrade(c.grade).accent),
              const SizedBox(width: 12),
              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(c.nickname, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
                Text(gradeLabel(c.grade), style: const TextStyle(fontSize: 13, color: Palette.muted)),
              ])),
              const Tag('✓ Persetujuan aktif', fg: Palette.okInk, bg: Palette.okSoft, size: 11),
            ]),
            const SizedBox(height: 10),
            Text('Tutor hari ini: ${c.tutorToday} dari ${c.tutorLimit} pertanyaan', style: const TextStyle(fontSize: 13, color: Palette.inkSoft)),
            Text(c.safetyRefusals > 0 ? '${c.safetyRefusals} permintaan tidak aman ditolak Tutor' : 'Tidak ada permintaan tidak aman ke Tutor', style: const TextStyle(fontSize: 13, color: Palette.inkSoft)),
            const SizedBox(height: 8),
            Align(alignment: Alignment.centerLeft, child: TextButton.icon(onPressed: () => _delete(c), icon: const Icon(Icons.delete_outline_rounded, size: 18), label: const Text('Hapus profil'), style: TextButton.styleFrom(foregroundColor: Palette.bad))),
          ]),
        ),
        const SizedBox(height: 12),
      ],
      AppCard(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Tambah profil anak', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
          const SizedBox(height: 12),
          TextField(controller: _name, maxLength: 20, textCapitalization: TextCapitalization.words, decoration: const InputDecoration(labelText: 'Nama panggilan', counterText: '')),
          const SizedBox(height: 12),
          const Text('Kelas', style: TextStyle(fontSize: 13, fontWeight: FontWeight.w700, color: Palette.inkSoft)),
          const SizedBox(height: 8),
          Wrap(spacing: 8, runSpacing: 8, children: [
            for (var g = 1; g <= 9; g++)
              SizedBox(
                width: 56,
                height: 52,
                child: OutlinedButton(
                  onPressed: () => setState(() => _grade = g),
                  style: OutlinedButton.styleFrom(
                    padding: EdgeInsets.zero,
                    backgroundColor: _grade == g ? Palette.parent : Palette.surface,
                    foregroundColor: _grade == g ? Colors.white : Palette.ink,
                    side: BorderSide(color: _grade == g ? Palette.parent : Palette.borderStrong),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: Column(mainAxisSize: MainAxisSize.min, children: [
                    Text('$g', style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w800)),
                    Text(g <= 6 ? 'SD' : 'SMP', style: const TextStyle(fontSize: 10, fontWeight: FontWeight.w700)),
                  ]),
                ),
              ),
          ]),
          const SizedBox(height: 10),
          const Text('BOBO hanya meminta nama panggilan dan kelas. Tidak perlu nama lengkap, tanggal lahir, sekolah, atau foto anak.', style: TextStyle(fontSize: 12, color: Palette.muted, height: 1.5)),
          if (_error != null) ...[const SizedBox(height: 8), Text(_error!, style: const TextStyle(color: Palette.bad, fontWeight: FontWeight.w700))],
          const SizedBox(height: 12),
          PrimaryButton(label: 'Tambah anak', icon: Icons.add_rounded, busy: _busy, onPressed: _add),
        ]),
      ),
      const SizedBox(height: 20),
      const SectionTitle('Akun & privasi'),
      SecondaryButton(label: 'Salin data akun (ekspor)', icon: Icons.download_rounded, onPressed: _export),
      const SizedBox(height: 10),
      SecondaryButton(label: 'Keluar dari perangkat ini', icon: Icons.logout_rounded, onPressed: () => app.logout()),
      const SizedBox(height: 10),
      SecondaryButton(label: 'Hapus akun', icon: Icons.delete_forever_outlined, foreground: Palette.bad, onPressed: _deleteAccount),
    ]);
  }
}
