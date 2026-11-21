import 'package:flutter/material.dart';

import '../core/theme.dart';

class LessonVisual extends StatelessWidget {
  const LessonVisual({super.key, required this.kind, required this.theme});

  final String kind;
  final BandTheme theme;

  @override
  Widget build(BuildContext context) {
    switch (kind) {
      case 'frac':
        return _box(Semantics(label: 'Batang 1/2, 2/4, dan 4/8 dengan bagian berwarna yang sama panjang', child: _fractions()));
      case 'tens':
        return _box(Semantics(label: '23 adalah 2 puluhan dan 3 satuan. 15 adalah 1 puluhan dan 5 satuan.', child: _tens()));
      case 'tri':
        return _box(Semantics(
          label: 'Segitiga siku-siku dengan sisi tegak a dan b serta sisi miring c',
          child: Column(children: [
            SizedBox(height: 150, width: double.infinity, child: CustomPaint(painter: _TrianglePainter())),
            const Text('c = sisi miring, di depan sudut siku-siku', style: TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w600)),
          ]),
        ));
      default:
        return const SizedBox.shrink();
    }
  }

  Widget _box(Widget child) => Container(
        width: double.infinity,
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(color: const Color(0xFFF8FAFC), borderRadius: BorderRadius.circular(14)),
        child: child,
      );

  Widget _bar(String label, int parts, int filled) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Row(children: [
        SizedBox(width: 40, child: Text(label, style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 16))),
        Expanded(
          child: Row(
            children: List.generate(parts, (i) => Expanded(
                  child: Container(
                    height: 28,
                    margin: EdgeInsets.only(right: i == parts - 1 ? 0 : 3),
                    decoration: BoxDecoration(color: i < filled ? theme.accent : const Color(0xFFE2E8F0), borderRadius: BorderRadius.circular(6)),
                  ),
                )),
          ),
        ),
      ]),
    );
  }

  Widget _fractions() => Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        _bar('1/2', 2, 1),
        _bar('2/4', 4, 2),
        _bar('4/8', 8, 4),
        const Text('Bagian berwarna sama panjang, jadi nilainya sama.', style: TextStyle(fontSize: 13, color: Palette.muted, fontWeight: FontWeight.w600)),
      ]);

  Widget _tensRow(String label, int tens, int ones) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
        SizedBox(width: 52, child: Text(label, style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 20))),
        ...List.generate(tens, (_) => Container(width: 14, height: 56, margin: const EdgeInsets.only(right: 6), decoration: BoxDecoration(color: theme.accent, borderRadius: BorderRadius.circular(4)))),
        const SizedBox(width: 8),
        ...List.generate(ones, (_) => Container(width: 14, height: 14, margin: const EdgeInsets.only(right: 6), decoration: BoxDecoration(color: const Color(0xFFFDBA74), borderRadius: BorderRadius.circular(4)))),
      ]),
    );
  }

  Widget _tens() => Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        _tensRow('23', 2, 3),
        _tensRow('+15', 1, 5),
        const Text('Batang = puluhan · Kotak kecil = satuan', style: TextStyle(fontSize: 14, color: Palette.muted, fontWeight: FontWeight.w600)),
      ]);
}

class _TrianglePainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final sx = size.width / 300;
    final sy = size.height / 150;
    final path = Path()
      ..moveTo(70 * sx, 130 * sy)
      ..lineTo(250 * sx, 130 * sy)
      ..lineTo(70 * sx, 24 * sy)
      ..close();
    canvas.drawPath(path, Paint()..color = const Color(0xFFE0E7FF));
    canvas.drawPath(path, Paint()
      ..color = const Color(0xFF4338CA)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..strokeJoin = StrokeJoin.round);
    final corner = Path()
      ..moveTo(70 * sx, 114 * sy)
      ..lineTo(86 * sx, 114 * sy)
      ..lineTo(86 * sx, 130 * sy);
    canvas.drawPath(corner, Paint()
      ..color = const Color(0xFF4338CA)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2);
    void label(String t, double x, double y) {
      final tp = TextPainter(text: TextSpan(text: t, style: const TextStyle(fontFamily: 'PlusJakartaSans', fontSize: 20, fontWeight: FontWeight.w700, color: Color(0xFF312E81))), textDirection: TextDirection.ltr)..layout();
      tp.paint(canvas, Offset(x * sx, y * sy - tp.height));
    }

    label('a', 48, 84);
    label('b', 154, 150);
    label('c', 166, 70);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
