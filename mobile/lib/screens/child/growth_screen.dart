import 'package:flutter/material.dart';

import '../../core/models.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';

class GrowthView extends StatelessWidget {
  const GrowthView({super.key, required this.data, required this.theme, required this.forParent});

  final Map<String, dynamic> data;
  final BandTheme theme;
  final bool forParent;

  @override
  Widget build(BuildContext context) {
    final weekly = ((data['weekly_answers'] as List?) ?? const []).map((e) => (e as num).toInt()).toList();
    final maxW = weekly.isEmpty ? 1 : weekly.reduce((a, b) => a > b ? a : b).clamp(1, 1 << 30);
    final topics = asList(data['topics']);
    final badges = asList(data['badges']);
    final streak = (data['streak_days'] as num?)?.toInt() ?? 0;
    const labels = ['3 mgg lalu', '2 mgg lalu', 'Mgg lalu', 'Minggu ini'];
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      AppCard(
        radius: theme.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(forParent ? 'Jumlah soal per minggu' : 'Soal yang kamu kerjakan', style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
          const SizedBox(height: 12),
          SizedBox(
            height: 130,
            child: Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
              for (var i = 0; i < weekly.length; i++)
                Expanded(
                  child: Semantics(
                    label: '${labels[i]}: ${weekly[i]} soal',
                    child: Column(mainAxisAlignment: MainAxisAlignment.end, children: [
                      Text('${weekly[i]}', style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 13)),
                      const SizedBox(height: 4),
                      Container(height: 80 * weekly[i] / maxW + 4, margin: const EdgeInsets.symmetric(horizontal: 10), decoration: BoxDecoration(color: i == weekly.length - 1 ? theme.accent : theme.soft, borderRadius: BorderRadius.circular(6))),
                      const SizedBox(height: 6),
                      Text(labels[i], style: const TextStyle(fontSize: 11, color: Palette.muted, fontWeight: FontWeight.w600)),
                    ]),
                  ),
                ),
            ]),
          ),
          const SizedBox(height: 10),
          Text(streak > 0 ? 'Belajar $streak hari berturut-turut.' : 'Belajar hari ini untuk memulai rangkaian hari belajar.', style: const TextStyle(fontSize: 14, color: Palette.inkSoft)),
        ]),
      ),
      const SizedBox(height: 16),
      AppCard(
        radius: theme.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(forParent ? 'Dulu vs sekarang' : 'Dulu vs sekarang (kamu dibandingkan dengan dirimu sendiri)', style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
          const SizedBox(height: 10),
          if (topics.isEmpty) const Text('Kerjakan minimal 6 soal di satu topik untuk melihat perbandingannya.', style: TextStyle(fontSize: 14, color: Palette.muted)),
          for (final tp in topics)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 8),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(tp['topic'] as String, style: const TextStyle(fontWeight: FontWeight.w700)),
                const SizedBox(height: 6),
                _bar('5 jawaban pertama', (tp['before_pct'] as num).toInt(), theme.soft, theme.ink),
                const SizedBox(height: 4),
                _bar('5 jawaban terakhir', (tp['now_pct'] as num).toInt(), theme.accent, Colors.white),
              ]),
            ),
        ]),
      ),
      const SizedBox(height: 16),
      AppCard(
        radius: theme.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Lencana usaha', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
          const SizedBox(height: 10),
          for (final b in badges)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 6),
              child: Row(children: [
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(color: b['earned'] == true ? theme.accent : const Color(0xFFF1F5F9), shape: BoxShape.circle),
                  child: Icon(b['earned'] == true ? Icons.emoji_events_rounded : Icons.lock_outline_rounded, color: b['earned'] == true ? Colors.white : Palette.muted, size: 20),
                ),
                const SizedBox(width: 12),
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(b['title'] as String, style: TextStyle(fontWeight: FontWeight.w700, color: b['earned'] == true ? Palette.ink : Palette.muted)),
                  Text(b['desc'] as String, style: const TextStyle(fontSize: 13, color: Palette.muted)),
                ])),
                if (b['earned'] == true) const Tag('Didapat', fg: Palette.okInk, bg: Palette.okSoft, size: 11),
              ]),
            ),
        ]),
      ),
    ]);
  }

  Widget _bar(String label, int pct, Color bg, Color fg) {
    return Row(children: [
      SizedBox(width: 130, child: Text(label, style: const TextStyle(fontSize: 12, color: Palette.muted))),
      Expanded(
        child: Stack(children: [
          Container(height: 22, decoration: BoxDecoration(color: const Color(0xFFF1F5F9), borderRadius: BorderRadius.circular(6))),
          FractionallySizedBox(
            widthFactor: (pct / 100).clamp(0.08, 1.0),
            child: Container(height: 22, alignment: Alignment.centerRight, padding: const EdgeInsets.only(right: 6), decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(6)), child: Text('$pct%', style: TextStyle(fontSize: 11, fontWeight: FontWeight.w800, color: fg))),
          ),
        ]),
      ),
    ]);
  }
}

class GrowthScreen extends StatelessWidget {
  const GrowthScreen({super.key, required this.load, required this.theme});

  final Future<Map<String, dynamic>> Function() load;
  final BandTheme theme;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Kemajuanku', style: TextStyle(fontWeight: FontWeight.w800))),
      body: FutureBuilder<Map<String, dynamic>>(
        future: load(),
        builder: (context, snap) {
          if (snap.hasError) {
            return EmptyState(icon: Icons.wifi_off_rounded, title: 'Belum bisa dimuat', body: snap.error.toString());
          }
          if (!snap.hasData) {
            return const LoadingView();
          }
          return ListView(padding: const EdgeInsets.all(20), children: [GrowthView(data: snap.data!, theme: theme, forParent: false)]);
        },
      ),
    );
  }
}
