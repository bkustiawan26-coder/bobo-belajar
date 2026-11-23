import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/models.dart';
import '../../core/persona.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';
import 'child_shell.dart';
import 'growth_screen.dart';

class HomeTab extends StatefulWidget {
  const HomeTab({super.key});

  @override
  State<HomeTab> createState() => _HomeTabState();
}

class _HomeTabState extends State<HomeTab> {
  Map<String, dynamic>? _home;
  Map<String, dynamic>? _catalog;
  Object? _error;
  int _lastTab = -1;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final app = context.read<AppState>();
    try {
      final cat = await CatalogCache.load(app);
      Map<String, dynamic>? home;
      try {
        home = asMap(await app.student('GET', '/student/home'));
        await app.db.putJson('home_${app.child!.id}', home);
      } catch (_) {
        final cached = await app.db.getJson('home_${app.child!.id}');
        home = cached == null ? null : asMap(cached);
      }
      if (mounted) {
        setState(() {
          _catalog = cat;
          _home = home;
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
    final app = context.watch<AppState>();
    final nav = context.watch<ChildNav>();
    if (nav.tab == 0 && _lastTab != 0 && _catalog != null) {
      WidgetsBinding.instance.addPostFrameCallback((_) => _load());
    }
    _lastTab = nav.tab;
    final c = app.child!;
    final t = BandTheme.forGrade(c.grade);
    final young = c.grade <= 2;
    if (_error != null && _catalog == null) {
      return ErrorView(error: _error!, onRetry: _load);
    }
    if (_catalog == null) {
      return const LoadingView();
    }
    final subjects = asList(_catalog!['subjects']);
    final cont = _home == null ? null : (_home!['continue_lesson'] == null ? null : asMap(_home!['continue_lesson']));
    final targets = _home == null ? <Map<String, dynamic>>[] : asList(_home!['targets']);
    final dev = _home == null ? <Map<String, dynamic>>[] : asList(_home!['developing_topics']);
    final reviewDue = _home == null ? 0 : ((_home!['review_due'] as num?)?.toInt() ?? 0);
    final foundation = _home == null ? <Map<String, dynamic>>[] : asList(_home!['foundation']);
    return RefreshIndicator(
      onRefresh: _load,
      child: ListView(padding: const EdgeInsets.all(20), children: [
        if (young) ...[
          Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
            BoboLogo(size: 56, color: t.accent, smile: Colors.white),
            const SizedBox(width: 10),
            Expanded(
              child: AppCard(
                radius: 18,
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                child: Text(Persona.forGrade(c.grade).homeNudge(c.nickname, cont?['title']?.toString()), style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w600, height: 1.4)),
              ),
            ),
          ]),
          const SizedBox(height: 20),
        ],
        if (cont != null)
          _ContinueCard(data: cont, theme: t, onOpen: () => nav.lesson(cont['lesson_id'] as int))
        else
          AppCard(
            radius: t.radius,
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('Materi Kelas ${c.grade} sedang disiapkan', style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w800)),
              const SizedBox(height: 6),
              const Text('Tim konten BOBO sedang menyusun dan meninjau materi untuk kelasmu. Materi baru muncul setelah lolos review.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
            ]),
          ),
        if (reviewDue > 0) ...[
          const SizedBox(height: 16),
          _ActionCard(
            theme: t,
            icon: Icons.replay_rounded,
            title: 'Ulang sebentar',
            body: '$reviewDue soal yang dulu belum tepat siap diulang. Cuma sebentar, kok.',
            button: 'Mulai ulang',
            onTap: () => nav.practice(null, mode: 'review'),
          ),
        ],
        for (final f in foundation) ...[
          const SizedBox(height: 16),
          _ActionCard(
            theme: t,
            icon: Icons.foundation_rounded,
            title: 'Pondasi: ${f['topic']}',
            body: 'Supaya ${f['for_topic']} lebih mudah, perkuat dulu dasarnya${f['grade'] != c.grade ? ' dari Kelas ${f['grade']}' : ''}.',
            button: f['lesson_id'] != null ? 'Baca materinya' : 'Latihan dasar',
            onTap: () => f['lesson_id'] != null ? nav.lesson(f['lesson_id'] as int) : nav.practice(f['topic_id'] as int, mode: 'foundation'),
            secondary: (f['question_count'] as num) > 0 ? 'Latihan ${f['question_count']} soal' : null,
            onSecondary: () => nav.practice(f['topic_id'] as int, mode: 'foundation'),
          ),
        ],
        const SizedBox(height: 16),
        Material(
          color: Palette.surface,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radius), side: const BorderSide(color: Palette.border)),
          child: InkWell(
            borderRadius: BorderRadius.circular(t.radius),
            onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => GrowthScreen(theme: t, load: () async => asMap(await app.student('GET', '/student/growth'))))),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Row(children: [
                Container(width: 44, height: 44, decoration: BoxDecoration(color: t.soft, borderRadius: BorderRadius.circular(12)), child: Icon(Icons.trending_up_rounded, color: t.ink)),
                const SizedBox(width: 14),
                const Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text('Kemajuanku', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
                  Text('Lihat perkembanganmu dan lencana usaha', style: TextStyle(fontSize: 13, color: Palette.muted)),
                ])),
                const Icon(Icons.chevron_right_rounded, color: Palette.muted),
              ]),
            ),
          ),
        ),
        const SizedBox(height: 20),
        if (targets.isNotEmpty)
          AppCard(
            radius: t.radius,
            padding: const EdgeInsets.fromLTRB(20, 18, 20, 6),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Text('Target hari ini', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
              const SizedBox(height: 12),
              for (final g in targets)
                Padding(
                  padding: const EdgeInsets.only(bottom: 14),
                  child: Row(children: [
                    Container(
                      width: 26,
                      height: 26,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(shape: BoxShape.circle, color: g['done'] == true ? t.accent : Colors.white, border: Border.all(color: g['done'] == true ? t.accent : const Color(0xFF94A3B8), width: 2)),
                      child: g['done'] == true ? const Icon(Icons.check_rounded, size: 16, color: Colors.white) : null,
                    ),
                    const SizedBox(width: 12),
                    Expanded(child: Text(g['label'] as String, style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w600, color: g['done'] == true ? Palette.muted : Palette.ink))),
                    Text(g['progress'] as String, style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w700, color: Palette.muted)),
                  ]),
                ),
            ]),
          ),
        if (dev.isNotEmpty) ...[
          const SizedBox(height: 20),
          const SectionTitle('Perlu dilatih lagi'),
          Wrap(spacing: 8, runSpacing: 8, children: [
            for (final d in dev)
              ActionChip(
                avatar: Icon(Icons.edit_rounded, size: 16, color: t.ink),
                label: Text(d['topic'] as String),
                labelStyle: TextStyle(color: t.ink, fontWeight: FontWeight.w700),
                backgroundColor: t.soft,
                side: BorderSide(color: t.accent),
                shape: const StadiumBorder(),
                onPressed: () => nav.practice(d['topic_id'] as int),
              ),
          ]),
        ],
        const SizedBox(height: 20),
        const SectionTitle('Mata pelajaran'),
        GridView.count(
          crossAxisCount: 2,
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          mainAxisSpacing: 12,
          crossAxisSpacing: 12,
          childAspectRatio: 1.35,
          children: [
            for (final s in subjects)
              Material(
                color: Palette.surface,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radius), side: const BorderSide(color: Palette.border)),
                child: InkWell(
                  borderRadius: BorderRadius.circular(t.radius),
                  onTap: () => nav.subject(s['id'] as int),
                  child: Padding(
                    padding: const EdgeInsets.all(14),
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
                      Container(width: 40, height: 40, alignment: Alignment.center, decoration: BoxDecoration(color: t.soft, borderRadius: BorderRadius.circular(12)), child: Text(s['short_label'] as String, style: TextStyle(color: t.ink, fontWeight: FontWeight.w800))),
                      Text(s['name'] as String, maxLines: 2, overflow: TextOverflow.ellipsis, style: TextStyle(fontSize: t.body, fontWeight: FontWeight.w700, height: 1.2)),
                      Text(s['ready'] == true ? '${s['topic_count']} topik' : 'Sedang ditinjau', style: const TextStyle(fontSize: 13, color: Palette.muted)),
                    ]),
                  ),
                ),
              ),
          ],
        ),
      ]),
    );
  }
}

class _ContinueCard extends StatelessWidget {
  const _ContinueCard({required this.data, required this.theme, required this.onOpen});

  final Map<String, dynamic> data;
  final BandTheme theme;
  final VoidCallback onOpen;

  @override
  Widget build(BuildContext context) {
    final blocks = (data['block_count'] as num).toInt();
    final step = (data['step'] as num).toInt();
    final done = data['completed'] == true;
    final pct = done ? 1.0 : (blocks == 0 ? 0.0 : step / blocks);
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(color: theme.accent, borderRadius: BorderRadius.circular(theme.radius)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(done ? 'MATERI SELESAI' : (step > 0 ? 'LANJUTKAN BELAJAR' : 'MULAI BELAJAR'), style: const TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w700, letterSpacing: 0.5)),
        const SizedBox(height: 8),
        Text(data['title'] as String, style: TextStyle(color: Colors.white, fontSize: theme.title, fontWeight: FontWeight.w800, height: 1.2)),
        const SizedBox(height: 6),
        Text('${data['subject'] ?? ''} · ${done ? 'Semua bagian selesai' : 'Bagian ${step + 1} dari $blocks'}', style: const TextStyle(color: Colors.white, fontSize: 14)),
        const SizedBox(height: 12),
        ClipRRect(borderRadius: BorderRadius.circular(999), child: LinearProgressIndicator(value: pct, minHeight: 8, color: Colors.white, backgroundColor: Colors.white.withValues(alpha: 0.32))),
        const SizedBox(height: 14),
        FilledButton(
          onPressed: onOpen,
          style: FilledButton.styleFrom(backgroundColor: Colors.white, foregroundColor: theme.ink, minimumSize: const Size(0, 48), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(theme.radiusSmall))),
          child: Text(done ? 'Buka lagi' : (step > 0 ? 'Lanjut belajar' : 'Mulai'), style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 15)),
        ),
      ]),
    );
  }
}


class _ActionCard extends StatelessWidget {
  const _ActionCard({required this.theme, required this.icon, required this.title, required this.body, required this.button, required this.onTap, this.secondary, this.onSecondary});

  final BandTheme theme;
  final IconData icon;
  final String title;
  final String body;
  final String button;
  final VoidCallback onTap;
  final String? secondary;
  final VoidCallback? onSecondary;

  @override
  Widget build(BuildContext context) {
    return AppCard(
      radius: theme.radius,
      color: theme.soft,
      borderColor: theme.soft,
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(children: [
          Icon(icon, color: theme.ink),
          const SizedBox(width: 8),
          Expanded(child: Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: theme.ink))),
        ]),
        const SizedBox(height: 6),
        Text(body, style: TextStyle(fontSize: theme.body - 1, height: 1.45, color: Palette.ink)),
        const SizedBox(height: 12),
        Wrap(spacing: 8, runSpacing: 8, children: [
          FilledButton(
            onPressed: onTap,
            style: FilledButton.styleFrom(backgroundColor: theme.accent, minimumSize: const Size(0, 44), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(theme.radiusSmall))),
            child: Text(button, style: const TextStyle(fontWeight: FontWeight.w700)),
          ),
          if (secondary != null)
            OutlinedButton(
              onPressed: onSecondary,
              style: OutlinedButton.styleFrom(backgroundColor: Palette.surface, foregroundColor: theme.ink, minimumSize: const Size(0, 44), side: BorderSide(color: theme.accent), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(theme.radiusSmall))),
              child: Text(secondary!, style: const TextStyle(fontWeight: FontWeight.w700)),
            ),
        ]),
      ]),
    );
  }
}
