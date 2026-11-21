import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../core/theme.dart';
import 'common.dart';

int gcd(int a, int b) => b == 0 ? a.abs() : gcd(b, a % b);

String simplest(int num, int den) {
  if (num == 0) {
    return '0';
  }
  final g = gcd(num, den);
  return den ~/ g == 1 ? '${num ~/ g}' : '${num ~/ g}/${den ~/ g}';
}

List<String> equivalents(int num, int den, {int maxDen = 12}) {
  if (num == 0) {
    return [];
  }
  final g = gcd(num, den);
  final n = num ~/ g;
  final d = den ~/ g;
  final out = <String>[];
  for (var k = 1; d * k <= maxDen; k++) {
    final s = '${n * k}/${d * k}';
    if (s != '$num/$den') {
      out.add(s);
    }
  }
  return out;
}

class PlaygroundScreen extends StatelessWidget {
  const PlaygroundScreen({super.key, required this.kind, required this.theme});

  final String kind;
  final BandTheme theme;

  @override
  Widget build(BuildContext context) {
    final title = switch (kind) {
      'frac' => 'Alat peraga pecahan',
      'tens' => 'Alat peraga puluhan & satuan',
      _ => 'Alat peraga segitiga siku-siku',
    };
    return Scaffold(
      appBar: AppBar(title: Text(title, style: const TextStyle(fontWeight: FontWeight.w800))),
      body: SafeArea(
        child: ListView(padding: const EdgeInsets.all(20), children: [
          switch (kind) {
            'frac' => FractionPlayground(theme: theme),
            'tens' => TensPlayground(theme: theme),
            _ => PythagorasPlayground(theme: theme),
          },
        ]),
      ),
    );
  }
}

class _Stepper extends StatelessWidget {
  const _Stepper({required this.label, required this.value, required this.onMinus, required this.onPlus});

  final String label;
  final String value;
  final VoidCallback? onMinus;
  final VoidCallback? onPlus;

  @override
  Widget build(BuildContext context) {
    return Row(children: [
      Expanded(child: Text(label, style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 15))),
      IconButton.outlined(onPressed: onMinus, icon: const Icon(Icons.remove_rounded), tooltip: 'Kurangi $label'),
      SizedBox(width: 56, child: Text(value, textAlign: TextAlign.center, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w800))),
      IconButton.outlined(onPressed: onPlus, icon: const Icon(Icons.add_rounded), tooltip: 'Tambah $label'),
    ]);
  }
}

class FractionPlayground extends StatefulWidget {
  const FractionPlayground({super.key, required this.theme});

  final BandTheme theme;

  @override
  State<FractionPlayground> createState() => _FractionPlaygroundState();
}

class _FractionPlaygroundState extends State<FractionPlayground> {
  int _den = 4;
  final Set<int> _on = {0};

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    final num = _on.length;
    final eq = equivalents(num, _den);
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      const Text('Ketuk kotak untuk mewarnai bagian. Ubah jumlah potongan dengan tombol + dan −.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
      const SizedBox(height: 16),
      _Stepper(
        label: 'Jumlah potongan',
        value: '$_den',
        onMinus: _den > 2 ? () => setState(() { _den--; _on.removeWhere((i) => i >= _den); }) : null,
        onPlus: _den < 12 ? () => setState(() => _den++) : null,
      ),
      const SizedBox(height: 16),
      Row(children: List.generate(_den, (i) {
        final on = _on.contains(i);
        return Expanded(
          child: Semantics(
            button: true,
            selected: on,
            label: 'Potongan ${i + 1}${on ? ', diwarnai' : ''}',
            child: GestureDetector(
              onTap: () => setState(() => on ? _on.remove(i) : _on.add(i)),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 150),
                height: 64,
                margin: EdgeInsets.only(right: i == _den - 1 ? 0 : 4),
                decoration: BoxDecoration(color: on ? t.accent : const Color(0xFFE2E8F0), borderRadius: BorderRadius.circular(8)),
              ),
            ),
          ),
        );
      })),
      const SizedBox(height: 20),
      AppCard(
        radius: t.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text('$num/$_den', style: TextStyle(fontSize: 40, fontWeight: FontWeight.w800, color: t.ink)),
          Text('$num bagian berwarna dari $_den bagian sama besar.', style: const TextStyle(fontSize: 15, height: 1.5)),
          if (num > 0 && simplest(num, _den) != '$num/$_den') Text('Bentuk paling sederhana: ${simplest(num, _den)}', style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700)),
          if (eq.isNotEmpty) ...[
            const SizedBox(height: 8),
            Text('Senilai dengan: ${eq.join(', ')}', style: const TextStyle(fontSize: 15, color: Palette.inkSoft)),
          ],
        ]),
      ),
    ]);
  }
}

class TensPlayground extends StatefulWidget {
  const TensPlayground({super.key, required this.theme});

  final BandTheme theme;

  @override
  State<TensPlayground> createState() => _TensPlaygroundState();
}

class _TensPlaygroundState extends State<TensPlayground> {
  int _tens = 2;
  int _ones = 3;

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      const Text('Tambah atau kurangi batang puluhan dan kotak satuan, lalu lihat bilangannya.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
      const SizedBox(height: 16),
      _Stepper(label: 'Puluhan (batang)', value: '$_tens', onMinus: _tens > 0 ? () => setState(() => _tens--) : null, onPlus: _tens < 9 ? () => setState(() => _tens++) : null),
      const SizedBox(height: 8),
      _Stepper(
        label: 'Satuan (kotak)',
        value: '$_ones',
        onMinus: _ones > 0 ? () => setState(() => _ones--) : null,
        onPlus: () => setState(() {
          if (_ones == 9 && _tens < 9) {
            _ones = 0;
            _tens++;
          } else if (_ones < 9) {
            _ones++;
          }
        }),
      ),
      const SizedBox(height: 16),
      Semantics(
        label: '$_tens puluhan dan $_ones satuan',
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(color: const Color(0xFFF8FAFC), borderRadius: BorderRadius.circular(14)),
          child: Wrap(crossAxisAlignment: WrapCrossAlignment.end, spacing: 6, runSpacing: 6, children: [
            ...List.generate(_tens, (_) => Container(width: 16, height: 64, decoration: BoxDecoration(color: t.accent, borderRadius: BorderRadius.circular(4)))),
            const SizedBox(width: 10),
            ...List.generate(_ones, (_) => Container(width: 16, height: 16, decoration: BoxDecoration(color: const Color(0xFFFDBA74), borderRadius: BorderRadius.circular(4)))),
          ]),
        ),
      ),
      const SizedBox(height: 16),
      AppCard(
        radius: t.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text('${_tens * 10 + _ones}', style: TextStyle(fontSize: 40, fontWeight: FontWeight.w800, color: t.ink)),
          Text('$_tens puluhan = ${_tens * 10}, ditambah $_ones satuan.', style: const TextStyle(fontSize: 15, height: 1.5)),
          const Text('Kalau satuan sudah 10, tukar dengan 1 batang puluhan.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
        ]),
      ),
    ]);
  }
}

class PythagorasPlayground extends StatefulWidget {
  const PythagorasPlayground({super.key, required this.theme});

  final BandTheme theme;

  @override
  State<PythagorasPlayground> createState() => _PythagorasPlaygroundState();
}

class _PythagorasPlaygroundState extends State<PythagorasPlayground> {
  double _a = 3;
  double _b = 4;

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    final a = _a.round();
    final b = _b.round();
    final c2 = a * a + b * b;
    final c = math.sqrt(c2.toDouble());
    final whole = c == c.roundToDouble();
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      const Text('Geser panjang sisi tegak a dan b, lalu perhatikan sisi miring c.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
      const SizedBox(height: 12),
      Text('a = $a', style: const TextStyle(fontWeight: FontWeight.w700)),
      Slider(value: _a, min: 1, max: 15, divisions: 14, label: '$a', onChanged: (v) => setState(() => _a = v), activeColor: t.accent),
      Text('b = $b', style: const TextStyle(fontWeight: FontWeight.w700)),
      Slider(value: _b, min: 1, max: 15, divisions: 14, label: '$b', onChanged: (v) => setState(() => _b = v), activeColor: t.accent),
      SizedBox(
        height: 180,
        width: double.infinity,
        child: Semantics(label: 'Segitiga siku-siku dengan a $a dan b $b', child: CustomPaint(painter: _TriPainter(a.toDouble(), b.toDouble(), t.accent))),
      ),
      const SizedBox(height: 12),
      AppCard(
        radius: t.radius,
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text('c² = $a² + $b² = ${a * a} + ${b * b} = $c2', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700)),
          Text('c = √$c2 ${whole ? '= ${c.round()}' : '≈ ${c.toStringAsFixed(2)}'}', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800, color: t.ink)),
          if (whole) const Text('Ketiga sisinya bilangan bulat: ini tripel Pythagoras!', style: TextStyle(color: Palette.okInk, fontWeight: FontWeight.w700)),
        ]),
      ),
    ]);
  }
}

class _TriPainter extends CustomPainter {
  _TriPainter(this.a, this.b, this.color);

  final double a;
  final double b;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final scale = math.min((size.width - 40) / b, (size.height - 30) / a);
    final ox = 20.0;
    final oy = size.height - 10;
    final path = Path()
      ..moveTo(ox, oy)
      ..lineTo(ox + b * scale, oy)
      ..lineTo(ox, oy - a * scale)
      ..close();
    canvas.drawPath(path, Paint()..color = color.withValues(alpha: 0.15));
    canvas.drawPath(path, Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3);
  }

  @override
  bool shouldRepaint(covariant _TriPainter old) => old.a != a || old.b != b || old.color != color;
}
