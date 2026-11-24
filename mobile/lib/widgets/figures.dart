import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../core/speech.dart';
import '../core/theme.dart';
import 'hijaiyah.dart';
import 'recitation.dart';

typedef Say = void Function(String text, {String? gender});

void defaultSay(String text, {String? gender}) {
  if (text.trim().isNotEmpty) {
    Speech.instance.speak(text, gender: gender);
  }
}

const figSoft = [Color(0xFFFFEDD5), Color(0xFFDCFCE7), Color(0xFFDBEAFE), Color(0xFFFCE7F3), Color(0xFFFEF9C3), Color(0xFFE0E7FF), Color(0xFFCCFBF1), Color(0xFFFFE4E6)];
const figInk = [Color(0xFF9A3412), Color(0xFF166534), Color(0xFF1E40AF), Color(0xFF9D174D), Color(0xFF854D0E), Color(0xFF3730A3), Color(0xFF115E59), Color(0xFF9F1239)];
const figStrong = [Color(0xFFF97316), Color(0xFF22C55E), Color(0xFF3B82F6), Color(0xFFEC4899), Color(0xFFEAB308), Color(0xFF6366F1), Color(0xFF14B8A6), Color(0xFFF43F5E)];

List<Map<String, dynamic>> figList(Object? v) => [for (final x in (v as List? ?? const [])) Map<String, dynamic>.from(x as Map)];

String figText(Map<String, dynamic> it) {
  final label = (it['label'] ?? '').toString();
  final tag = (it['tag'] ?? '').toString();
  final say = (it['say'] ?? '').toString();
  return [if (tag.isNotEmpty) tag, if (label.isNotEmpty) label, if (say.isNotEmpty) say].join(', ');
}

String fmtNum(num v) {
  if (v == v.roundToDouble()) {
    return v.round().toString();
  }
  return (v * 100).round() / 100 == v ? v.toString().replaceAll('.', ',') : v.toStringAsFixed(2).replaceAll('.', ',');
}

String figSummary(Map<String, dynamic> spec) {
  final parts = <String>[];
  for (final key in ['center']) {
    if (spec[key] is Map) {
      parts.add(figText(Map<String, dynamic>.from(spec[key] as Map)));
    }
  }
  for (final it in figList(spec['items'])) {
    if (it.containsKey('label') || it.containsKey('say')) {
      parts.add(figText(it));
    }
  }
  for (final g in figList(spec['groups'])) {
    parts.add('${figText(Map<String, dynamic>.from(g['title'] as Map))}: ${figList(g['items']).map(figText).join(', ')}');
  }
  if (spec['caption'] != null) {
    parts.add(spec['caption'].toString());
  }
  return parts.join('. ');
}

class FigBox extends StatelessWidget {
  const FigBox({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) => Container(
        width: double.infinity,
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(color: const Color(0xFFF8FAFC), borderRadius: BorderRadius.circular(16), border: Border.all(color: const Color(0xFFE2E8F0))),
        child: child,
      );
}

class FigChip extends StatelessWidget {
  const FigChip({super.key, required this.item, required this.index, this.onTap, this.active = false, this.done = false, this.wrong = false, this.big = false, this.width});

  final Map<String, dynamic> item;
  final int index;
  final VoidCallback? onTap;
  final bool active;
  final bool done;
  final bool wrong;
  final bool big;
  final double? width;

  @override
  Widget build(BuildContext context) {
    final c = index % figSoft.length;
    final icon = (item['icon'] ?? '').toString();
    final label = (item['label'] ?? '').toString();
    final tag = (item['tag'] ?? '').toString();
    final bg = wrong ? Palette.badSoft : (done ? Palette.okSoft : figSoft[c]);
    final border = wrong ? Palette.bad : (done ? Palette.ok : (active ? figStrong[c] : Colors.transparent));
    return Semantics(
      button: onTap != null,
      label: figText(item),
      child: GestureDetector(
        onTap: onTap,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 220),
          width: width,
          constraints: const BoxConstraints(minHeight: 48),
          padding: EdgeInsets.symmetric(horizontal: 10, vertical: big ? 12 : 8),
          decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(14), border: Border.all(color: border, width: 2.5)),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            if (tag.isNotEmpty) Text(tag, textAlign: TextAlign.center, style: TextStyle(fontSize: 12, fontWeight: FontWeight.w800, color: figInk[c])),
            if (icon.isNotEmpty) Text(icon, style: TextStyle(fontSize: big ? 40 : 28, height: 1.15)),
            if (label.isNotEmpty) Text(label, textAlign: TextAlign.center, style: TextStyle(fontSize: 13.5, fontWeight: FontWeight.w700, color: done ? Palette.okInk : figInk[c], height: 1.25)),
            if (done) const Icon(Icons.check_circle_rounded, size: 16, color: Palette.ok),
          ]),
        ),
      ),
    );
  }
}

class LessonFigure extends StatefulWidget {
  const LessonFigure({super.key, required this.spec, required this.theme, this.say = defaultSay, this.quiz = false});

  final Map<String, dynamic> spec;
  final BandTheme theme;
  final Say say;
  final bool quiz;

  @override
  State<LessonFigure> createState() => _LessonFigureState();
}

class _LessonFigureState extends State<LessonFigure> {
  int _active = -1;

  @override
  void didUpdateWidget(covariant LessonFigure oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.spec != widget.spec) {
      _active = -1;
      _run++;
      _playing = false;
    }
  }

  int _run = 0;
  bool _playing = false;

  void _tap(int i, String text, {String? gender}) {
    _run++;
    setState(() {
      _active = i;
      _playing = false;
    });
    widget.say(text, gender: gender);
  }

  Future<void> _playChat(List<Map<String, dynamic>> items) async {
    if (_playing) {
      _run++;
      setState(() => _playing = false);
      await Speech.instance.stop();
      return;
    }
    final my = ++_run;
    setState(() => _playing = true);
    for (final (i, it) in items.indexed) {
      if (my != _run || !mounted) {
        return;
      }
      final text = (it['say'] ?? '').toString();
      if (text.trim().isEmpty) {
        continue;
      }
      setState(() => _active = i);
      widget.say(text, gender: it['voice']?.toString());
      if (!await Speech.instance.finished(text)) {
        break;
      }
    }
    if (my == _run && mounted) {
      setState(() => _playing = false);
    }
  }

  Widget _chip(Map<String, dynamic> it, int i, {double? width, bool big = false}) =>
      FigChip(item: it, index: i, active: _active == i, width: width, big: big, onTap: () => _tap(i, figText(it)));

  Widget _arrow({bool down = false}) => Padding(
        padding: const EdgeInsets.symmetric(horizontal: 2, vertical: 2),
        child: Icon(down ? Icons.arrow_downward_rounded : Icons.arrow_forward_rounded, color: widget.theme.accent, size: 22),
      );

  @override
  Widget build(BuildContext context) {
    final s = widget.spec;
    final type = s['type']?.toString() ?? '';
    if (type == 'quran') {
      return QuranCard(surah: (s['surah'] as num).toInt(), from: (s['from'] as num).toInt(), to: (s['to'] as num).toInt(), theme: widget.theme);
    }
    if (type == 'hijaiyah') {
      return HijaiyahBoard(key: ValueKey('hijaiyah-${s['mode']}-${(s['items'] as List?)?.length}'), spec: s, theme: widget.theme);
    }
    if (type == 'doa') {
      return DoaCard(id: s['id'].toString(), title: s['title'].toString(), latin: s['latin'].toString(), meaning: s['meaning'].toString(), theme: widget.theme);
    }
    final body = _body(type, s);
    final caption = s['caption']?.toString();
    final hint = widget.quiz ? null : _hint(type);
    return Semantics(
      label: figSummary(s),
      child: FigBox(
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          body,
          if (caption != null && caption.isNotEmpty) ...[
            const SizedBox(height: 10),
            Text(caption, textAlign: TextAlign.center, style: const TextStyle(fontSize: 13.5, color: Palette.inkSoft, fontWeight: FontWeight.w700, height: 1.35)),
          ],
          if (hint != null) ...[
            const SizedBox(height: 6),
            Row(mainAxisAlignment: MainAxisAlignment.center, children: [
              Icon(Icons.touch_app_rounded, size: 15, color: widget.theme.ink),
              const SizedBox(width: 4),
              Flexible(child: Text(hint, style: TextStyle(fontSize: 12, color: widget.theme.ink, fontWeight: FontWeight.w600))),
            ]),
          ],
        ]),
      ),
    );
  }

  String? _hint(String type) {
    const tappable = {'flow', 'cycle', 'steps', 'layers', 'pyramid', 'time', 'mind', 'compare', 'icons', 'chat', 'bars', 'table', 'venn'};
    return tappable.contains(type) ? 'Ketuk gambar untuk mendengarkan' : null;
  }

  Widget _body(String type, Map<String, dynamic> s) {
    final items = figList(s['items']);
    switch (type) {
      case 'flow':
        return Wrap(alignment: WrapAlignment.center, crossAxisAlignment: WrapCrossAlignment.center, runSpacing: 8, children: [
          for (final (i, it) in items.indexed) ...[_chip(it, i, width: 108), if (i < items.length - 1) _arrow()],
        ]);
      case 'cycle':
        return items.length > 6 ? _body('flow', s) : _ring(items, arrows: true);
      case 'mind':
        return _ring(items, center: Map<String, dynamic>.from(s['center'] as Map));
      case 'steps':
        return Column(children: [
          for (final (i, it) in items.indexed) ...[
            GestureDetector(
              onTap: () => _tap(i, figText(it)),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(color: figSoft[i % 8], borderRadius: BorderRadius.circular(14), border: Border.all(color: _active == i ? figStrong[i % 8] : Colors.transparent, width: 2.5)),
                child: Row(children: [
                  CircleAvatar(radius: 15, backgroundColor: figStrong[i % 8], child: Text('${i + 1}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800))),
                  const SizedBox(width: 10),
                  if ((it['icon'] ?? '').toString().isNotEmpty) Padding(padding: const EdgeInsets.only(right: 8), child: Text(it['icon'].toString(), style: const TextStyle(fontSize: 26))),
                  Expanded(child: Text((it['label'] ?? '').toString(), style: TextStyle(fontSize: 14.5, fontWeight: FontWeight.w700, color: figInk[i % 8]))),
                ]),
              ),
            ),
            if (i < items.length - 1) _arrow(down: true),
          ],
        ]);
      case 'layers':
      case 'pyramid':
        final n = items.length;
        return Column(children: [
          for (final (i, it) in items.indexed)
            Padding(
              padding: const EdgeInsets.only(bottom: 4),
              child: FractionallySizedBox(
                widthFactor: type == 'pyramid' ? (0.42 + 0.58 * (n == 1 ? 1 : i / (n - 1))) : 1,
                child: _chip(it, i),
              ),
            ),
        ]);
      case 'time':
        return Column(children: [
          for (final (i, it) in items.indexed)
            IntrinsicHeight(
              child: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                SizedBox(
                  width: 70,
                  child: Column(children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 4),
                      decoration: BoxDecoration(color: widget.theme.accent, borderRadius: BorderRadius.circular(8)),
                      child: Text((it['tag'] ?? '').toString(), textAlign: TextAlign.center, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 12.5)),
                    ),
                    if (i < items.length - 1) Expanded(child: Container(width: 3, color: widget.theme.soft)),
                  ]),
                ),
                const SizedBox(width: 8),
                Expanded(child: Padding(padding: const EdgeInsets.only(bottom: 10), child: _chip({...it, 'tag': ''}, i))),
              ]),
            ),
        ]);
      case 'compare':
        final groups = figList(s['groups']);
        if (groups.length >= 3) {
          return LayoutBuilder(builder: (context, box) => box.maxWidth < 520 ? _compareRows(groups) : _compareColumns(groups));
        }
        return _compareColumns(groups);
      case 'venn':
        final groups = figList(s['groups']);
        return GestureDetector(
          onTap: () => widget.say(figSummary(s)),
          child: SizedBox(height: 230, child: CustomPaint(painter: VennPainter(groups), size: Size.infinite)),
        );
      case 'bars':
        return SizedBox(height: 210, child: _bars(items));
      case 'line':
        return SizedBox(height: 96, child: CustomPaint(painter: NumberLinePainter(from: (s['from'] as num).toDouble(), to: (s['to'] as num).toDouble(), step: (s['step'] as num).toDouble(), marks: _nums(s['marks']), jumps: _nums(s['jumps']), color: widget.theme.accent), size: Size.infinite));
      case 'frac':
        return Column(children: [for (final f in items) _fracBar((f['n'] as num).toInt(), (f['d'] as num).toInt())]);
      case 'pie':
        return Wrap(alignment: WrapAlignment.center, spacing: 18, runSpacing: 12, children: [
          for (final f in items)
            Column(mainAxisSize: MainAxisSize.min, children: [
              SizedBox(width: 120, height: 120, child: CustomPaint(painter: PiePainter(n: (f['n'] as num).toInt(), d: (f['d'] as num).toInt(), color: widget.theme.accent))),
              const SizedBox(height: 6),
              Text('${f['n']}/${f['d']}', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w800)),
            ]),
        ]);
      case 'place':
        return _place(s['value'].toString());
      case 'array':
        final rows = (s['rows'] as num).toInt();
        final cols = (s['cols'] as num).toInt();
        final icon = (s['icon'] ?? '●').toString();
        return Column(children: [
          for (var r = 0; r < rows; r++)
            Row(mainAxisAlignment: MainAxisAlignment.center, children: [
              for (var c = 0; c < cols; c++) Flexible(child: FittedBox(child: Padding(padding: const EdgeInsets.all(2), child: Text(icon, style: const TextStyle(fontSize: 26))))),
            ]),
          const SizedBox(height: 6),
          Text('$rows baris, masing-masing $cols', style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w700, color: Palette.inkSoft)),
        ]);
      case 'count':
        return Wrap(alignment: WrapAlignment.center, crossAxisAlignment: WrapCrossAlignment.center, spacing: 6, runSpacing: 8, children: [
          for (final t in figList(s['terms']))
            if (t['op'] != null)
              Text(t['op'].toString(), style: TextStyle(fontSize: 30, fontWeight: FontWeight.w900, color: widget.theme.accent))
            else if ((t['n'] as num).toInt() == 0)
              Container(width: 56, height: 56, alignment: Alignment.center, decoration: BoxDecoration(color: Palette.warnSoft, borderRadius: BorderRadius.circular(14)), child: const Text('?', style: TextStyle(fontSize: 30, fontWeight: FontWeight.w900, color: Palette.warnInk)))
            else
              Container(
                constraints: const BoxConstraints(maxWidth: 150),
                padding: const EdgeInsets.all(6),
                decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(14), border: Border.all(color: const Color(0xFFE2E8F0))),
                child: Column(mainAxisSize: MainAxisSize.min, children: [
                  Wrap(alignment: WrapAlignment.center, children: [for (var k = 0; k < (t['n'] as num).toInt(); k++) Text(t['icon'].toString(), style: const TextStyle(fontSize: 22))]),
                  if (!widget.quiz) Text('${t['n']}', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
                ]),
              ),
        ]);
      case 'shape':
        final labels = [for (final l in (s['labels'] as List? ?? const [])) l.toString()];
        return Column(children: [
          SizedBox(height: 190, child: CustomPaint(painter: ShapePainter(shape: s['shape'].toString(), labels: labels, color: widget.theme.accent, soft: widget.theme.soft), size: Size.infinite)),
          if (labels.isNotEmpty)
            Wrap(alignment: WrapAlignment.center, spacing: 6, runSpacing: 6, children: [
              for (final (i, l) in labels.indexed) _chip({'label': l}, i),
            ]),
        ]);
      case 'table':
        final head = [for (final h in s['head'] as List) h.toString()];
        final rows = [for (final r in s['rows'] as List) [for (final c in r as List) c.toString()]];
        return Table(
          border: TableBorder.all(color: const Color(0xFFCBD5E1), borderRadius: BorderRadius.circular(10)),
          defaultVerticalAlignment: TableCellVerticalAlignment.middle,
          children: [
            TableRow(decoration: BoxDecoration(color: widget.theme.accent), children: [for (final h in head) Padding(padding: const EdgeInsets.all(8), child: Text(h, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 13.5)))]),
            for (final (ri, r) in rows.indexed)
              TableRow(decoration: BoxDecoration(color: ri.isEven ? Colors.white : widget.theme.soft.withValues(alpha: 0.5)), children: [
                for (final c in r)
                  GestureDetector(onTap: () => widget.say(r.join(', ')), child: Padding(padding: const EdgeInsets.all(8), child: Text(c, style: const TextStyle(fontSize: 13.5, color: Palette.ink, height: 1.3)))),
              ]),
          ],
        );
      case 'coord':
        return AspectRatio(aspectRatio: 1, child: CustomPaint(painter: CoordPainter(spec: s, color: widget.theme.accent, quiz: widget.quiz)));
      case 'clock':
        final h = (s['h'] as num).toInt();
        final m = (s['m'] as num).toInt();
        return Column(children: [
          SizedBox(width: 180, height: 180, child: CustomPaint(painter: ClockPainter(h: h, m: m, color: widget.theme.accent))),
          if (!widget.quiz) Padding(padding: const EdgeInsets.only(top: 6), child: Text('Pukul ${h.toString().padLeft(2, '0')}.${m.toString().padLeft(2, '0')}', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800))),
        ]);
      case 'code':
        final lines = [for (final l in s['lines'] as List) l.toString()];
        final output = (s['output'] ?? '').toString();
        return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: const Color(0xFF0F172A), borderRadius: BorderRadius.circular(12)),
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                for (final (i, l) in lines.indexed)
                  Text.rich(TextSpan(children: [
                    TextSpan(text: '${(i + 1).toString().padLeft(2)}  ', style: const TextStyle(color: Color(0xFF64748B))),
                    TextSpan(text: l, style: const TextStyle(color: Color(0xFFE2E8F0))),
                  ]), style: const TextStyle(fontFamily: 'monospace', fontSize: 13.5, height: 1.5)),
              ]),
            ),
          ),
          if (output.isNotEmpty && !widget.quiz) ...[
            const SizedBox(height: 8),
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(color: Palette.okBg, borderRadius: BorderRadius.circular(12), border: Border.all(color: Palette.okSoft)),
              child: Text('Hasil:\n$output', style: const TextStyle(fontFamily: 'monospace', fontSize: 13.5, color: Palette.okInk, height: 1.4)),
            ),
          ],
        ]);
      case 'icons':
        return Wrap(alignment: WrapAlignment.center, spacing: 8, runSpacing: 8, children: [for (final (i, it) in items.indexed) _chip(it, i, width: 96, big: true)]);
      case 'circuit':
        return SizedBox(height: 170, child: CustomPaint(painter: CircuitPainter(parallel: s['mode'] == 'paralel', n: (s['n'] as num).toInt(), color: widget.theme.accent), size: Size.infinite));
      case 'compass':
        return SizedBox(height: 220, child: CustomPaint(painter: CompassPainter(marks: [for (final m in s['mark'] as List? ?? const []) m.toString()], color: widget.theme.accent), size: Size.infinite));
      case 'balance':
        return SizedBox(height: 170, child: CustomPaint(painter: BalancePainter(left: s['left'].toString(), right: s['right'].toString(), color: widget.theme.accent), size: Size.infinite));
      case 'chat':
        final who = <String>[];
        for (final it in items) {
          if (!who.contains(it['label'])) {
            who.add(it['label'].toString());
          }
        }
        return Column(children: [
          if (!widget.quiz)
            Align(
              alignment: Alignment.centerLeft,
              child: TextButton.icon(
                onPressed: () => _playChat(items),
                icon: Icon(_playing ? Icons.stop_circle_outlined : Icons.play_circle_fill_rounded, color: widget.theme.ink),
                label: Text(_playing ? 'Berhenti' : 'Putar percakapan', style: TextStyle(color: widget.theme.ink, fontWeight: FontWeight.w800)),
              ),
            ),
          for (final (i, it) in items.indexed) _bubble(it, i, who.indexOf(it['label'].toString()).isOdd),
        ]);
      default:
        return const SizedBox.shrink();
    }
  }

  Widget _compareColumns(List<Map<String, dynamic>> groups) {
    return Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
      for (final (gi, g) in groups.indexed) ...[
        if (gi > 0) const SizedBox(width: 8),
        Expanded(
          child: Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(color: figSoft[gi % 8].withValues(alpha: 0.6), borderRadius: BorderRadius.circular(14)),
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              _chip(Map<String, dynamic>.from(g['title'] as Map), gi, big: true),
              const SizedBox(height: 6),
              for (final it in figList(g['items']))
                GestureDetector(
                  onTap: () => widget.say(figText(it)),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: 4),
                    child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text((it['icon'] ?? '•').toString(), style: TextStyle(fontSize: (it['icon'] ?? '').toString().isEmpty ? 16 : 18, color: figInk[gi % 8], fontWeight: FontWeight.w900)),
                      const SizedBox(width: 6),
                      Expanded(child: Text((it['label'] ?? '').toString(), style: const TextStyle(fontSize: 13.5, color: Palette.ink, height: 1.3))),
                    ]),
                  ),
                ),
            ]),
          ),
        ),
      ],
    ]);
  }

  Widget _compareRows(List<Map<String, dynamic>> groups) {
    return Column(children: [
      for (final (gi, g) in groups.indexed)
        Container(
          margin: const EdgeInsets.only(bottom: 8),
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(color: figSoft[gi % 8].withValues(alpha: 0.6), borderRadius: BorderRadius.circular(14)),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            SizedBox(width: 108, child: _chip(Map<String, dynamic>.from(g['title'] as Map), gi)),
            const SizedBox(width: 10),
            Expanded(
              child: Wrap(spacing: 6, runSpacing: 6, children: [
                for (final it in figList(g['items']))
                  GestureDetector(
                    onTap: () => widget.say(figText(it)),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 6),
                      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(10)),
                      child: Text('${(it['icon'] ?? '').toString().isEmpty ? '' : '${it['icon']} '}${it['label'] ?? ''}', style: TextStyle(fontSize: 13.5, color: figInk[gi % 8], fontWeight: FontWeight.w600)),
                    ),
                  ),
              ]),
            ),
          ]),
        ),
    ]);
  }

  Widget _bubble(Map<String, dynamic> it, int i, bool right) {
    final c = right ? 2 : 0;
    final avatar = Column(children: [
      Text((it['icon'] ?? '🙂').toString(), style: const TextStyle(fontSize: 26)),
      Text((it['label'] ?? '').toString(), style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w700, color: Palette.muted)),
    ]);
    final bubble = Flexible(
      child: GestureDetector(
        onTap: () => _tap(i, (it['say'] ?? '').toString(), gender: it['voice']?.toString()),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 9),
          decoration: BoxDecoration(
            color: figSoft[c],
            border: Border.all(color: _active == i ? figStrong[c] : Colors.transparent, width: 2),
            borderRadius: BorderRadius.only(topLeft: const Radius.circular(14), topRight: const Radius.circular(14), bottomLeft: Radius.circular(right ? 14 : 2), bottomRight: Radius.circular(right ? 2 : 14)),
          ),
          child: Text((it['say'] ?? '').toString(), style: TextStyle(fontSize: 14.5, color: figInk[c], fontWeight: FontWeight.w600, height: 1.35)),
        ),
      ),
    );
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(mainAxisAlignment: right ? MainAxisAlignment.end : MainAxisAlignment.start, crossAxisAlignment: CrossAxisAlignment.end, children: right ? [const SizedBox(width: 30), bubble, const SizedBox(width: 6), avatar] : [avatar, const SizedBox(width: 6), bubble, const SizedBox(width: 30)]),
    );
  }

  List<double> _nums(Object? v) => [for (final x in (v as List? ?? const [])) (x as num).toDouble()];

  Widget _ring(List<Map<String, dynamic>> items, {bool arrows = false, Map<String, dynamic>? center}) {
    return LayoutBuilder(builder: (context, box) {
      final w = box.maxWidth.isFinite ? box.maxWidth : 340.0;
      final n = items.length;
      final chipW = math.min(116.0, w * (n > 4 ? 0.3 : 0.36));
      final h = w * (n > 4 ? 1.0 : 0.85) + 60;
      final cx = w / 2;
      final cy = h / 2;
      final rx = w / 2 - chipW / 2 - 2;
      final ry = h / 2 - 58;
      final pos = [for (var i = 0; i < n; i++) Offset(cx + rx * math.sin(2 * math.pi * i / n), cy - ry * math.cos(2 * math.pi * i / n))];
      return SizedBox(
        height: h,
        child: Stack(clipBehavior: Clip.none, children: [
          Positioned.fill(child: CustomPaint(painter: RingPainter(points: pos, center: center == null ? null : Offset(cx, cy), arrows: arrows, color: widget.theme.accent))),
          if (center != null)
            Positioned(left: cx - chipW / 2 - 6, top: cy - 40, width: chipW + 12, child: Center(child: FigChip(item: center, index: 5, big: true, active: _active == 99, onTap: () => _tap(99, figText(center))))),
          for (final (i, it) in items.indexed)
            Positioned(left: pos[i].dx - chipW / 2, top: pos[i].dy - 40, width: chipW, child: Center(child: _chip(it, i))),
        ]),
      );
    });
  }

  Widget _bars(List<Map<String, dynamic>> items) {
    final maxV = items.map((e) => (e['value'] as num).toDouble()).fold<double>(0, math.max);
    return Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
      for (final (i, it) in items.indexed)
        Expanded(
          child: GestureDetector(
            onTap: () => _tap(i, '${it['label']}, ${fmtNum(it['value'] as num)}'),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 3),
              child: Column(mainAxisAlignment: MainAxisAlignment.end, children: [
                Text(fmtNum(it['value'] as num), style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w800)),
                const SizedBox(height: 2),
                AnimatedContainer(
                  duration: const Duration(milliseconds: 400),
                  height: maxV <= 0 ? 4 : math.max(4, 120 * (it['value'] as num).toDouble() / maxV),
                  decoration: BoxDecoration(color: _active == i ? figInk[i % 8] : figStrong[i % 8], borderRadius: const BorderRadius.vertical(top: Radius.circular(8))),
                ),
                Container(height: 2, color: Palette.borderStrong),
                const SizedBox(height: 4),
                if ((it['icon'] ?? '').toString().isNotEmpty) Text(it['icon'].toString(), style: const TextStyle(fontSize: 18)),
                Text((it['label'] ?? '').toString(), textAlign: TextAlign.center, maxLines: 2, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 11.5, fontWeight: FontWeight.w700, color: Palette.inkSoft)),
              ]),
            ),
          ),
        ),
    ]);
  }

  Widget _fracBar(int n, int d) {
    final wholes = math.max(1, (n / d).ceil());
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Row(children: [
        SizedBox(width: 52, child: Text('$n/$d', style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 18))),
        Expanded(
          child: Column(children: [
            for (var w = 0; w < wholes; w++)
              Padding(
                padding: EdgeInsets.only(bottom: w < wholes - 1 ? 4 : 0),
                child: Row(children: [
                  for (var i = 0; i < d; i++)
                    Expanded(
                      child: Container(
                        height: 30,
                        margin: EdgeInsets.only(right: i == d - 1 ? 0 : 2),
                        decoration: BoxDecoration(color: w * d + i < n ? widget.theme.accent : const Color(0xFFE2E8F0), borderRadius: BorderRadius.circular(5)),
                      ),
                    ),
                ]),
              ),
          ]),
        ),
      ]),
    );
  }

  Widget _place(String value) {
    const names = ['Satuan', 'Puluhan', 'Ratusan', 'Ribuan', 'Puluh ribuan', 'Ratus ribuan', 'Jutaan', 'Puluh jutaan', 'Ratus jutaan'];
    final digits = value.split('');
    final k = digits.length;
    final parts = <String>[];
    for (var i = 0; i < k; i++) {
      final d = int.parse(digits[i]);
      if (d > 0) {
        final v = d * math.pow(10, k - 1 - i).toInt();
        parts.add(groupDigits(v.toString()));
      }
    }
    return Column(children: [
      Row(children: [
        for (var i = 0; i < k; i++)
          Expanded(
            child: GestureDetector(
              onTap: () => _tap(i, '${digits[i]} ${names[k - 1 - i]}'),
              child: Container(
                margin: const EdgeInsets.symmetric(horizontal: 2),
                padding: const EdgeInsets.symmetric(vertical: 8),
                decoration: BoxDecoration(color: figSoft[(k - 1 - i) % 8], borderRadius: BorderRadius.circular(10), border: Border.all(color: _active == i ? figStrong[(k - 1 - i) % 8] : Colors.transparent, width: 2)),
                child: Column(children: [
                  FittedBox(child: Text(names[k - 1 - i], style: TextStyle(fontSize: 11, fontWeight: FontWeight.w700, color: figInk[(k - 1 - i) % 8]))),
                  const SizedBox(height: 4),
                  Text(digits[i], style: TextStyle(fontSize: 28, fontWeight: FontWeight.w900, color: figInk[(k - 1 - i) % 8])),
                ]),
              ),
            ),
          ),
      ]),
      const SizedBox(height: 8),
      Text('${groupDigits(value)} = ${parts.isEmpty ? '0' : parts.join(' + ')}', textAlign: TextAlign.center, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700)),
    ]);
  }
}

String groupDigits(String digits) {
  final out = StringBuffer();
  for (var i = 0; i < digits.length; i++) {
    if (i > 0 && (digits.length - i) % 3 == 0) {
      out.write('.');
    }
    out.write(digits[i]);
  }
  return out.toString();
}

void paintLabel(Canvas canvas, String text, Offset at, {double size = 13, Color color = Palette.ink, FontWeight weight = FontWeight.w700, double maxWidth = 140, bool center = true, Color? bg}) {
  final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(fontFamily: 'PlusJakartaSans', fontSize: size, color: color, fontWeight: weight)), textDirection: TextDirection.ltr, textAlign: TextAlign.center, maxLines: 3, ellipsis: '…')..layout(maxWidth: maxWidth);
  final o = center ? at - Offset(tp.width / 2, tp.height / 2) : at;
  if (bg != null) {
    canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(o.dx - 4, o.dy - 2, tp.width + 8, tp.height + 4), const Radius.circular(6)), Paint()..color = bg);
  }
  tp.paint(canvas, o);
}

void paintArrowHead(Canvas canvas, Offset tip, double angle, Paint p, {double size = 9}) {
  final path = Path()
    ..moveTo(tip.dx, tip.dy)
    ..lineTo(tip.dx - size * math.cos(angle - 0.45), tip.dy - size * math.sin(angle - 0.45))
    ..lineTo(tip.dx - size * math.cos(angle + 0.45), tip.dy - size * math.sin(angle + 0.45))
    ..close();
  canvas.drawPath(path, Paint()..color = p.color);
}

class RingPainter extends CustomPainter {
  RingPainter({required this.points, required this.center, required this.arrows, required this.color});

  final List<Offset> points;
  final Offset? center;
  final bool arrows;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..color = color.withValues(alpha: 0.55)
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;
    if (center != null) {
      for (final q in points) {
        canvas.drawLine(center!, q, p);
      }
      return;
    }
    if (!arrows || points.length < 2) {
      return;
    }
    final c = Offset(size.width / 2, size.height / 2);
    final rx = (points.map((e) => (e.dx - c.dx).abs()).reduce(math.max)) * 0.78;
    final ry = (points.map((e) => (e.dy - c.dy).abs()).reduce(math.max)) * 0.78;
    final n = points.length;
    for (var i = 0; i < n; i++) {
      final a0 = 2 * math.pi * i / n + 0.38;
      final a1 = 2 * math.pi * (i + 1) / n - 0.38;
      final path = Path();
      for (var k = 0; k <= 12; k++) {
        final a = a0 + (a1 - a0) * k / 12;
        final pt = Offset(c.dx + rx * math.sin(a), c.dy - ry * math.cos(a));
        if (k == 0) {
          path.moveTo(pt.dx, pt.dy);
        } else {
          path.lineTo(pt.dx, pt.dy);
        }
      }
      canvas.drawPath(path, p);
      final tip = Offset(c.dx + rx * math.sin(a1), c.dy - ry * math.cos(a1));
      final before = Offset(c.dx + rx * math.sin(a1 - 0.05), c.dy - ry * math.cos(a1 - 0.05));
      paintArrowHead(canvas, tip, math.atan2(tip.dy - before.dy, tip.dx - before.dx), p..color = color, size: 11);
    }
  }

  @override
  bool shouldRepaint(covariant RingPainter old) => old.points != points || old.color != color;
}

class VennPainter extends CustomPainter {
  VennPainter(this.groups);

  final List<Map<String, dynamic>> groups;

  @override
  void paint(Canvas canvas, Size size) {
    final r = math.min(size.height * 0.46, size.width * 0.3);
    final cy = size.height / 2 + 8;
    final a = Offset(size.width / 2 - r * 0.62, cy);
    final b = Offset(size.width / 2 + r * 0.62, cy);
    canvas.drawCircle(a, r, Paint()..color = figStrong[0].withValues(alpha: 0.22));
    canvas.drawCircle(b, r, Paint()..color = figStrong[2].withValues(alpha: 0.22));
    final stroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2;
    canvas.drawCircle(a, r, stroke..color = figStrong[0]);
    canvas.drawCircle(b, r, stroke..color = figStrong[2]);
    String title(int i) => figText(Map<String, dynamic>.from(groups[i]['title'] as Map));
    String list(int i) => figList(groups[i]['items']).map((e) => '${e['icon'] ?? ''}${(e['icon'] ?? '').toString().isEmpty ? '' : ' '}${e['label']}').join('\n');
    paintLabel(canvas, title(0), Offset(a.dx - r * 0.35, 10), color: figInk[0], size: 13.5, weight: FontWeight.w800, maxWidth: r * 1.2);
    paintLabel(canvas, title(1), Offset(b.dx + r * 0.35, 10), color: figInk[2], size: 13.5, weight: FontWeight.w800, maxWidth: r * 1.2);
    paintLabel(canvas, list(0), Offset(a.dx - r * 0.42, cy), maxWidth: r * 0.85, size: 12.5);
    paintLabel(canvas, list(1), Offset(b.dx + r * 0.42, cy), maxWidth: r * 0.85, size: 12.5);
    paintLabel(canvas, list(2), Offset(size.width / 2, cy), maxWidth: r * 0.62, size: 12.5, color: figInk[5]);
    paintLabel(canvas, title(2), Offset(size.width / 2, cy + r * 0.78), maxWidth: r * 0.9, size: 11.5, color: figInk[5]);
  }

  @override
  bool shouldRepaint(covariant VennPainter old) => old.groups != groups;
}

class NumberLinePainter extends CustomPainter {
  NumberLinePainter({required this.from, required this.to, required this.step, this.marks = const [], this.jumps = const [], required this.color, this.selected, this.correct});

  final double from;
  final double to;
  final double step;
  final List<double> marks;
  final List<double> jumps;
  final Color color;
  final double? selected;
  final bool? correct;

  static const pad = 18.0;

  double xOf(double v, Size size) => pad + (v - from) / (to - from) * (size.width - 2 * pad);

  static double? valueAt(double dx, Size size, double from, double to, double step) {
    final t = ((dx - pad) / (size.width - 2 * pad)).clamp(0.0, 1.0);
    final v = from + t * (to - from);
    final snapped = from + ((v - from) / step).round() * step;
    return double.parse(snapped.toStringAsFixed(4));
  }

  @override
  void paint(Canvas canvas, Size size) {
    final y = size.height * 0.68;
    final p = Paint()
      ..color = Palette.inkSoft
      ..strokeWidth = 2.5;
    canvas.drawLine(Offset(pad - 8, y), Offset(size.width - pad + 8, y), p);
    paintArrowHead(canvas, Offset(size.width - 2, y), 0, p);
    paintArrowHead(canvas, Offset(2, y), math.pi, p);
    final count = ((to - from) / step).round();
    final every = count > 12 ? 2 : 1;
    for (var i = 0; i <= count; i++) {
      final v = from + i * step;
      final x = xOf(v, size);
      canvas.drawLine(Offset(x, y - 7), Offset(x, y + 7), p);
      if (i % every == 0 || i == count) {
        paintLabel(canvas, fmtNum(v), Offset(x, y + 18), size: 12.5);
      }
    }
    if (jumps.length >= 2) {
      final arc = Paint()
        ..color = color
        ..strokeWidth = 2.5
        ..style = PaintingStyle.stroke;
      for (var i = 0; i + 1 < jumps.length; i++) {
        final x0 = xOf(jumps[i], size);
        final x1 = xOf(jumps[i + 1], size);
        final rect = Rect.fromLTRB(math.min(x0, x1), y - 40, math.max(x0, x1), y + 10);
        canvas.drawArc(rect, math.pi, math.pi * 0.98, false, arc);
        paintArrowHead(canvas, Offset(x1, y - 14), x1 > x0 ? math.pi / 2.4 : math.pi - math.pi / 2.4, arc, size: 8);
        final d = jumps[i + 1] - jumps[i];
        paintLabel(canvas, '${d >= 0 ? '+' : '−'}${fmtNum(d.abs())}', Offset((x0 + x1) / 2, y - 44), size: 11.5, color: color);
      }
    }
    for (final m in [...marks, ...jumps.take(1)]) {
      canvas.drawCircle(Offset(xOf(m, size), y), 7, Paint()..color = color);
    }
    if (selected != null) {
      final c = correct == null ? color : (correct! ? Palette.ok : Palette.bad);
      final x = xOf(selected!, size);
      canvas.drawCircle(Offset(x, y), 10, Paint()..color = c);
      paintLabel(canvas, fmtNum(selected!), Offset(x, y - 26), size: 15, color: Colors.white, bg: c, weight: FontWeight.w800);
    }
  }

  @override
  bool shouldRepaint(covariant NumberLinePainter old) => old.selected != selected || old.correct != correct || old.from != from || old.to != to;
}

class PiePainter extends CustomPainter {
  PiePainter({required this.n, required this.d, required this.color, this.filled});

  final int n;
  final int d;
  final Color color;
  final Set<int>? filled;

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);
    final r = math.min(size.width, size.height) / 2 - 2;
    final rect = Rect.fromCircle(center: c, radius: r);
    final sweep = 2 * math.pi / d;
    for (var i = 0; i < d; i++) {
      final on = filled == null ? i < n : filled!.contains(i);
      canvas.drawArc(rect, -math.pi / 2 + i * sweep, sweep, true, Paint()..color = on ? color : const Color(0xFFE2E8F0));
      canvas.drawArc(rect, -math.pi / 2 + i * sweep, sweep, true, Paint()
        ..color = Colors.white
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5);
    }
  }

  @override
  bool shouldRepaint(covariant PiePainter old) => old.n != n || old.d != d || old.filled != filled;
}

class ShapePainter extends CustomPainter {
  ShapePainter({required this.shape, required this.labels, required this.color, required this.soft});

  final String shape;
  final List<String> labels;
  final Color color;
  final Color soft;

  String _l(int i) => i < labels.length ? labels[i] : '';

  @override
  void paint(Canvas canvas, Size size) {
    final fill = Paint()..color = soft;
    final line = Paint()
      ..color = color
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke
      ..strokeJoin = StrokeJoin.round;
    final dash = Paint()
      ..color = color.withValues(alpha: 0.6)
      ..strokeWidth = 2
      ..style = PaintingStyle.stroke;
    final w = size.width;
    final h = size.height;
    final cx = w / 2;
    final cy = h / 2;
    void poly(List<Offset> pts) {
      final path = Path()..addPolygon(pts, true);
      canvas.drawPath(path, fill);
      canvas.drawPath(path, line);
    }

    void lab(String t, Offset at) {
      if (t.isNotEmpty) {
        final half = math.min(70.0, 4.0 + t.length * 3.9);
        final safe = Offset(at.dx.clamp(half, math.max(half, w - half)), at.dy.clamp(10.0, math.max(10.0, h - 10)));
        paintLabel(canvas, t, safe, size: 13, bg: Colors.white, color: Palette.ink);
      }
    }

    switch (shape) {
      case 'square':
        final s = math.min(w * 0.5, h * 0.72);
        poly([Offset(cx - s / 2, cy - s / 2), Offset(cx + s / 2, cy - s / 2), Offset(cx + s / 2, cy + s / 2), Offset(cx - s / 2, cy + s / 2)]);
        lab(_l(0), Offset(cx, cy + s / 2 + 12));
        lab(_l(0), Offset(cx + s / 2 + 30, cy));
      case 'rect':
        final rw = math.min(w * 0.58, 240.0);
        final rh = h * 0.5;
        poly([Offset(cx - rw / 2, cy - rh / 2), Offset(cx + rw / 2, cy - rh / 2), Offset(cx + rw / 2, cy + rh / 2), Offset(cx - rw / 2, cy + rh / 2)]);
        lab(_l(0), Offset(cx, cy + rh / 2 + 14));
        lab(_l(1), Offset(cx + rw / 2 + 4, cy) + const Offset(26, 0));
      case 'tri':
        final bw = math.min(w * 0.7, 250.0);
        final top = Offset(cx - bw * 0.1, cy - h * 0.34);
        final bl = Offset(cx - bw / 2, cy + h * 0.3);
        final br = Offset(cx + bw / 2, cy + h * 0.3);
        poly([top, br, bl]);
        canvas.drawLine(top, Offset(top.dx, bl.dy), dash);
        canvas.drawRect(Rect.fromLTWH(top.dx, bl.dy - 10, 10, 10), dash);
        lab(_l(0), Offset(cx, bl.dy + 14));
        lab(_l(1), Offset(top.dx + 28, cy + 6));
      case 'right':
        final a = math.min(w * 0.55, 220.0);
        final b = h * 0.62;
        final o = Offset(cx - a / 2, cy + b / 2);
        poly([o, Offset(o.dx, o.dy - b), Offset(o.dx + a, o.dy)]);
        canvas.drawRect(Rect.fromLTWH(o.dx, o.dy - 14, 14, 14), line..strokeWidth = 2);
        lab(_l(0), Offset(o.dx - 30, o.dy - b / 2));
        lab(_l(1), Offset(o.dx + a / 2, o.dy + 14));
        lab(_l(2), Offset(o.dx + a / 2 + 26, o.dy - b / 2 - 8));
      case 'circle':
        final r = math.min(w, h) * 0.38;
        canvas.drawCircle(Offset(cx, cy), r, fill);
        canvas.drawCircle(Offset(cx, cy), r, line);
        canvas.drawLine(Offset(cx, cy), Offset(cx + r, cy), dash..strokeWidth = 2.5);
        canvas.drawCircle(Offset(cx, cy), 4, Paint()..color = color);
        lab(_l(0), Offset(cx + r / 2, cy - 14));
        if (_l(1).isNotEmpty) {
          canvas.drawLine(Offset(cx - r, cy + 1), Offset(cx, cy + 1), dash);
          lab(_l(1), Offset(cx - r / 2, cy + 16));
        }
      case 'trap':
        final bw = math.min(w * 0.72, 260.0);
        final tw = bw * 0.5;
        final th = h * 0.55;
        final pts = [Offset(cx - tw / 2, cy - th / 2), Offset(cx + tw / 2, cy - th / 2), Offset(cx + bw / 2, cy + th / 2), Offset(cx - bw / 2, cy + th / 2)];
        poly(pts);
        canvas.drawLine(pts[0], Offset(pts[0].dx, pts[3].dy), dash);
        lab(_l(0), Offset(cx, pts[0].dy - 14));
        lab(_l(1), Offset(cx, pts[3].dy + 14));
        lab(_l(2), Offset(pts[0].dx + 26, cy));
      case 'para':
        final bw = math.min(w * 0.55, 210.0);
        final sk = bw * 0.3;
        final th = h * 0.55;
        final pts = [Offset(cx - bw / 2 + sk / 2, cy - th / 2), Offset(cx + bw / 2 + sk / 2, cy - th / 2), Offset(cx + bw / 2 - sk / 2, cy + th / 2), Offset(cx - bw / 2 - sk / 2, cy + th / 2)];
        poly(pts);
        canvas.drawLine(pts[0], Offset(pts[0].dx, pts[3].dy), dash);
        lab(_l(0), Offset(cx - sk / 2, pts[3].dy + 14));
        lab(_l(1), Offset(pts[0].dx + 24, cy));
      case 'rhombus':
        final dx = math.min(w * 0.32, 130.0);
        final dy = h * 0.4;
        poly([Offset(cx, cy - dy), Offset(cx + dx, cy), Offset(cx, cy + dy), Offset(cx - dx, cy)]);
        canvas.drawLine(Offset(cx - dx, cy), Offset(cx + dx, cy), dash);
        canvas.drawLine(Offset(cx, cy - dy), Offset(cx, cy + dy), dash);
        lab(_l(0), Offset(cx + dx / 2, cy + 12));
        lab(_l(1), Offset(cx + 26, cy - dy / 2));
      case 'cube':
      case 'box':
      case 'prism':
        final bw = shape == 'cube' ? h * 0.5 : math.min(w * 0.5, 200.0);
        final bh = shape == 'cube' ? h * 0.5 : h * 0.42;
        final d = bh * 0.45;
        final f = Offset(cx - bw / 2 - d / 4, cy - bh / 2 + d / 3);
        if (shape == 'prism') {
          final a = Offset(f.dx, f.dy + bh);
          final b = Offset(f.dx + bw, f.dy + bh);
          final t = Offset(f.dx + bw / 2, f.dy);
          final back = Offset(d, -d * 0.6);
          poly([a, b, t]);
          poly([b, b + back, t + back, t]);
          canvas.drawLine(a + back, b + back, dash);
          canvas.drawLine(a + back, t + back, dash);
          canvas.drawLine(a, a + back, dash);
        } else {
          final back = Offset(d, -d * 0.6);
          final front = [f, Offset(f.dx + bw, f.dy), Offset(f.dx + bw, f.dy + bh), Offset(f.dx, f.dy + bh)];
          poly([front[0], front[0] + back, front[1] + back, front[1]]);
          poly([front[1], front[1] + back, front[2] + back, front[2]]);
          poly(front);
          canvas.drawLine(front[3], front[3] + back, dash);
          canvas.drawLine(front[3] + back, front[2] + back, dash);
          canvas.drawLine(front[3] + back, front[0] + back, dash);
          lab(_l(0), Offset(f.dx + bw / 2, f.dy + bh + 14));
          lab(_l(shape == 'cube' ? 0 : 1), Offset(front[2].dx + d / 2 + 26, front[2].dy - d * 0.3));
          lab(_l(shape == 'cube' ? 0 : 2), Offset(f.dx - 28, f.dy + bh / 2));
        }
      case 'cylinder':
        final rw = math.min(w * 0.22, 90.0);
        final rh = rw * 0.32;
        final th = h * 0.62;
        final top = cy - th / 2;
        final bot = cy + th / 2;
        canvas.drawRect(Rect.fromLTRB(cx - rw, top, cx + rw, bot), fill);
        canvas.drawOval(Rect.fromCenter(center: Offset(cx, bot), width: rw * 2, height: rh * 2), fill);
        canvas.drawArc(Rect.fromCenter(center: Offset(cx, bot), width: rw * 2, height: rh * 2), 0, math.pi, false, line);
        canvas.drawArc(Rect.fromCenter(center: Offset(cx, bot), width: rw * 2, height: rh * 2), math.pi, math.pi, false, dash);
        canvas.drawLine(Offset(cx - rw, top), Offset(cx - rw, bot), line);
        canvas.drawLine(Offset(cx + rw, top), Offset(cx + rw, bot), line);
        canvas.drawOval(Rect.fromCenter(center: Offset(cx, top), width: rw * 2, height: rh * 2), Paint()..color = Colors.white);
        canvas.drawOval(Rect.fromCenter(center: Offset(cx, top), width: rw * 2, height: rh * 2), line);
        canvas.drawLine(Offset(cx, top), Offset(cx + rw, top), dash);
        lab(_l(0), Offset(cx + rw / 2, top - 16));
        lab(_l(1), Offset(cx + rw + 30, cy));
      case 'cone':
        final rw = math.min(w * 0.24, 95.0);
        final rh = rw * 0.3;
        final apex = Offset(cx, cy - h * 0.36);
        final base = cy + h * 0.3;
        final path = Path()
          ..moveTo(apex.dx, apex.dy)
          ..lineTo(cx + rw, base)
          ..arcTo(Rect.fromCenter(center: Offset(cx, base), width: rw * 2, height: rh * 2), 0, math.pi, false)
          ..close();
        canvas.drawPath(path, fill);
        canvas.drawPath(path, line);
        canvas.drawArc(Rect.fromCenter(center: Offset(cx, base), width: rw * 2, height: rh * 2), math.pi, math.pi, false, dash);
        canvas.drawLine(apex, Offset(cx, base), dash);
        canvas.drawLine(Offset(cx, base), Offset(cx + rw, base), dash);
        lab(_l(0), Offset(cx + rw / 2, base + 16));
        lab(_l(1), Offset(cx - 26, cy));
        lab(_l(2), Offset(cx + rw / 2 + 30, cy - 10));
      case 'sphere':
        final r = math.min(w, h) * 0.4;
        canvas.drawCircle(Offset(cx, cy), r, fill);
        canvas.drawCircle(Offset(cx, cy), r, line);
        canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy), width: r * 2, height: r * 0.5), dash);
        canvas.drawLine(Offset(cx, cy), Offset(cx + r, cy), dash..strokeWidth = 2.5);
        lab(_l(0), Offset(cx + r / 2, cy - 16));
      case 'pyramid3':
        final bw = math.min(w * 0.5, 200.0);
        final apex = Offset(cx, cy - h * 0.38);
        final a = Offset(cx - bw / 2, cy + h * 0.28);
        final b = Offset(cx + bw / 2 - 20, cy + h * 0.36);
        final c = Offset(cx + bw / 2 + 24, cy + h * 0.2);
        final dd = Offset(cx - bw / 2 + 44, cy + h * 0.13);
        poly([a, b, apex]);
        poly([b, c, apex]);
        canvas.drawLine(a, dd, dash);
        canvas.drawLine(dd, c, dash);
        canvas.drawLine(dd, apex, dash);
        lab(_l(0), Offset((a.dx + b.dx) / 2, b.dy + 12));
        lab(_l(1), Offset(cx - 34, cy));
      case 'angle':
        final o = Offset(cx - w * 0.2, cy + h * 0.3);
        final deg = double.tryParse(_l(0).replaceAll(RegExp(r'[^0-9.]'), '')) ?? 60;
        final rad = deg * math.pi / 180;
        final len = math.min(w * 0.5, 190.0);
        canvas.drawLine(o, o + Offset(len, 0), line);
        canvas.drawLine(o, o + Offset(len * math.cos(rad), -len * math.sin(rad)), line);
        canvas.drawArc(Rect.fromCircle(center: o, radius: 34), -rad, rad, true, Paint()..color = soft);
        canvas.drawArc(Rect.fromCircle(center: o, radius: 34), -rad, rad, false, line..strokeWidth = 2);
        lab(_l(0), o + Offset(60 * math.cos(rad / 2), -60 * math.sin(rad / 2)));
    }
  }

  @override
  bool shouldRepaint(covariant ShapePainter old) => old.shape != shape || old.labels != labels;
}

class CoordPainter extends CustomPainter {
  CoordPainter({required this.spec, required this.color, this.quiz = false});

  final Map<String, dynamic> spec;
  final Color color;
  final bool quiz;

  @override
  void paint(Canvas canvas, Size size) {
    final r = ((spec['range'] ?? 6) as num).toDouble();
    final pad = 14.0;
    final s = (math.min(size.width, size.height) - 2 * pad) / (2 * r);
    final o = Offset(size.width / 2, size.height / 2);
    Offset at(double x, double y) => o + Offset(x * s, -y * s);
    final grid = Paint()
      ..color = const Color(0xFFE2E8F0)
      ..strokeWidth = 1;
    for (var i = -r; i <= r; i++) {
      canvas.drawLine(at(i, -r), at(i, r), grid);
      canvas.drawLine(at(-r, i), at(r, i), grid);
    }
    final axis = Paint()
      ..color = Palette.inkSoft
      ..strokeWidth = 2;
    canvas.drawLine(at(-r, 0), at(r, 0), axis);
    canvas.drawLine(at(0, -r), at(0, r), axis);
    paintArrowHead(canvas, at(r, 0), 0, axis);
    paintArrowHead(canvas, at(0, r), -math.pi / 2, axis);
    paintLabel(canvas, 'x', at(r, 0) + const Offset(-6, -12), size: 12);
    paintLabel(canvas, 'y', at(0, r) + const Offset(10, 6), size: 12);
    final every = r > 8 ? 2 : 1;
    for (var i = -r.toInt(); i <= r.toInt(); i++) {
      if (i == 0 || i % every != 0) {
        continue;
      }
      paintLabel(canvas, '$i', at(i.toDouble(), 0) + const Offset(0, 10), size: 10, color: Palette.muted, weight: FontWeight.w500);
      paintLabel(canvas, '$i', at(0, i.toDouble()) + const Offset(-10, 0), size: 10, color: Palette.muted, weight: FontWeight.w500);
    }
    for (final (pi, poly) in (spec['polys'] as List? ?? const []).indexed) {
      final pts = [for (final p in poly as List) at(((p as Map)['x'] as num).toDouble(), (p['y'] as num).toDouble())];
      final path = Path()..addPolygon(pts, true);
      canvas.drawPath(path, Paint()..color = figStrong[(pi * 2 + 2) % 8].withValues(alpha: 0.18));
      canvas.drawPath(path, Paint()
        ..color = figStrong[(pi * 2 + 2) % 8]
        ..strokeWidth = 2.5
        ..style = PaintingStyle.stroke);
      for (final p in poly) {
        final m = p as Map;
        paintLabel(canvas, m['name'].toString(), at((m['x'] as num).toDouble(), (m['y'] as num).toDouble()) + const Offset(10, -10), size: 12, color: figInk[(pi * 2 + 2) % 8]);
      }
    }
    for (final (li, l) in (spec['lines'] as List? ?? const []).indexed) {
      final abc = [for (final v in (l as Map)['abc'] as List) (v as num).toDouble()];
      final path = Path();
      var started = false;
      Offset? labelAt;
      for (var k = 0; k <= 200; k++) {
        final x = -r + 2 * r * k / 200;
        final y = abc[0] * x * x + abc[1] * x + abc[2];
        if (y.abs() > r) {
          started = false;
          continue;
        }
        final pt = at(x, y);
        if (!started) {
          path.moveTo(pt.dx, pt.dy);
          started = true;
        } else {
          path.lineTo(pt.dx, pt.dy);
        }
        labelAt = pt;
      }
      final c = li == 0 ? color : figStrong[(li * 3) % 8];
      canvas.drawPath(path, Paint()
        ..color = c
        ..strokeWidth = 3
        ..style = PaintingStyle.stroke);
      if (labelAt != null) {
        paintLabel(canvas, l['label'].toString(), labelAt + const Offset(-30, -14), size: 12, color: c, bg: Colors.white);
      }
    }
    for (final p in spec['points'] as List? ?? const []) {
      final m = p as Map;
      final x = (m['x'] as num).toDouble();
      final y = (m['y'] as num).toDouble();
      canvas.drawCircle(at(x, y), 6, Paint()..color = Palette.bad);
      paintLabel(canvas, quiz ? m['name'].toString() : '${m['name']}(${fmtNum(x)}, ${fmtNum(y)})', at(x, y) + const Offset(0, -16), size: 12, color: Palette.badInk, bg: Colors.white);
    }
  }

  @override
  bool shouldRepaint(covariant CoordPainter old) => old.spec != spec;
}

class ClockPainter extends CustomPainter {
  ClockPainter({required this.h, required this.m, required this.color});

  final int h;
  final int m;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);
    final r = math.min(size.width, size.height) / 2 - 4;
    canvas.drawCircle(c, r, Paint()..color = Colors.white);
    canvas.drawCircle(c, r, Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 5);
    for (var i = 0; i < 60; i++) {
      final a = i * math.pi / 30;
      final inner = i % 5 == 0 ? r - 12 : r - 6;
      canvas.drawLine(c + Offset(math.sin(a) * inner, -math.cos(a) * inner), c + Offset(math.sin(a) * (r - 3), -math.cos(a) * (r - 3)), Paint()
        ..color = Palette.inkSoft
        ..strokeWidth = i % 5 == 0 ? 2.5 : 1);
    }
    for (var i = 1; i <= 12; i++) {
      final a = i * math.pi / 6;
      paintLabel(canvas, '$i', c + Offset(math.sin(a) * (r - 26), -math.cos(a) * (r - 26)), size: 15, weight: FontWeight.w800);
    }
    final ha = ((h % 12) + m / 60) * math.pi / 6;
    final ma = m * math.pi / 30;
    canvas.drawLine(c, c + Offset(math.sin(ha) * r * 0.5, -math.cos(ha) * r * 0.5), Paint()
      ..color = Palette.ink
      ..strokeWidth = 7
      ..strokeCap = StrokeCap.round);
    canvas.drawLine(c, c + Offset(math.sin(ma) * r * 0.75, -math.cos(ma) * r * 0.75), Paint()
      ..color = color
      ..strokeWidth = 4.5
      ..strokeCap = StrokeCap.round);
    canvas.drawCircle(c, 6, Paint()..color = Palette.ink);
  }

  @override
  bool shouldRepaint(covariant ClockPainter old) => old.h != h || old.m != m;
}

class CircuitPainter extends CustomPainter {
  CircuitPainter({required this.parallel, required this.n, required this.color});

  final bool parallel;
  final int n;
  final Color color;

  void _lamp(Canvas canvas, Offset c) {
    canvas.drawCircle(c, 15, Paint()..color = const Color(0xFFFEF08A));
    canvas.drawCircle(c, 15, Paint()
      ..color = Palette.warn
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.5);
    final x = Paint()
      ..color = Palette.warn
      ..strokeWidth = 2;
    canvas.drawLine(c + const Offset(-10, -10), c + const Offset(10, 10), x);
    canvas.drawLine(c + const Offset(10, -10), c + const Offset(-10, 10), x);
  }

  @override
  void paint(Canvas canvas, Size size) {
    final wire = Paint()
      ..color = Palette.inkSoft
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke;
    final l = size.width * 0.12;
    final r = size.width * 0.88;
    const t = 26.0;
    final b = size.height - 30;
    final mid = size.width / 2;
    canvas.drawLine(Offset(l, t), Offset(l, b), wire);
    canvas.drawLine(Offset(l, b), Offset(mid - 14, b), wire);
    canvas.drawLine(Offset(mid + 14, b), Offset(r, b), wire);
    canvas.drawLine(Offset(r, b), Offset(r, t), wire);
    canvas.drawLine(Offset(mid - 8, b - 18), Offset(mid - 8, b + 18), Paint()
      ..color = Palette.ink
      ..strokeWidth = 4);
    canvas.drawLine(Offset(mid + 8, b - 10), Offset(mid + 8, b + 10), Paint()
      ..color = Palette.ink
      ..strokeWidth = 8);
    paintLabel(canvas, 'baterai', Offset(mid, b + 26), size: 11.5, color: Palette.muted);
    paintLabel(canvas, '+', Offset(mid - 18, b - 22), size: 13, color: Palette.bad);
    if (!parallel) {
      canvas.drawLine(Offset(l, t), Offset(r, t), wire);
      for (var i = 0; i < n; i++) {
        _lamp(canvas, Offset(l + (r - l) * (i + 1) / (n + 1), t));
      }
      paintLabel(canvas, 'Rangkaian seri: arus melewati satu jalur', Offset(mid, (t + b) / 2), size: 12.5, color: color, maxWidth: size.width * 0.7);
    } else {
      final gap = (b - t - 30) / math.max(1, n);
      for (var i = 0; i < n; i++) {
        final y = t + i * gap;
        canvas.drawLine(Offset(l, y), Offset(r, y), wire);
        _lamp(canvas, Offset(mid, y));
      }
      paintLabel(canvas, 'Rangkaian paralel: arus bercabang', Offset(mid, b - 18), size: 12, color: color, maxWidth: size.width * 0.5, bg: Colors.white);
    }
  }

  @override
  bool shouldRepaint(covariant CircuitPainter old) => old.parallel != parallel || old.n != n;
}

class CompassPainter extends CustomPainter {
  CompassPainter({required this.marks, required this.color});

  final List<String> marks;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);
    final r = math.min(size.width, size.height) / 2 - 22;
    canvas.drawCircle(c, r, Paint()..color = const Color(0xFFF1F5F9));
    const names = ['Utara', 'Timur Laut', 'Timur', 'Tenggara', 'Selatan', 'Barat Daya', 'Barat', 'Barat Laut'];
    for (var i = 0; i < 8; i++) {
      final a = i * math.pi / 4;
      final len = i.isEven ? r : r * 0.62;
      final dir = Offset(math.sin(a), -math.cos(a));
      final side = Offset(-dir.dy, dir.dx) * (i.isEven ? 10 : 6);
      final path = Path()
        ..moveTo(c.dx + dir.dx * len, c.dy + dir.dy * len)
        ..lineTo(c.dx + side.dx, c.dy + side.dy)
        ..lineTo(c.dx - side.dx, c.dy - side.dy)
        ..close();
      final on = marks.contains(names[i]);
      canvas.drawPath(path, Paint()..color = i == 0 ? Palette.bad : (on ? color : (i.isEven ? Palette.inkSoft : Palette.borderStrong)));
      paintLabel(canvas, names[i], c + dir * (len + (i.isEven ? 12 : 14)), size: i.isEven ? 13 : 11, color: on || i == 0 ? (i == 0 ? Palette.bad : color) : Palette.ink, weight: on ? FontWeight.w900 : FontWeight.w700, bg: Colors.white.withValues(alpha: 0.85));
    }
  }

  @override
  bool shouldRepaint(covariant CompassPainter old) => old.marks != marks;
}

class BalancePainter extends CustomPainter {
  BalancePainter({required this.left, required this.right, required this.color});

  final String left;
  final String right;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2;
    final beam = 46.0;
    final p = Paint()
      ..color = Palette.inkSoft
      ..strokeWidth = 4
      ..strokeCap = StrokeCap.round;
    final half = size.width * 0.34;
    canvas.drawLine(Offset(cx - half, beam), Offset(cx + half, beam), p);
    canvas.drawLine(Offset(cx, beam), Offset(cx, size.height - 14), p);
    canvas.drawPath(Path()
      ..moveTo(cx - 30, size.height - 6)
      ..lineTo(cx + 30, size.height - 6)
      ..lineTo(cx, size.height - 26)
      ..close(), Paint()..color = Palette.inkSoft);
    for (final (i, t) in [left, right].indexed) {
      final x = i == 0 ? cx - half : cx + half;
      canvas.drawLine(Offset(x, beam), Offset(x - 34, beam + 56), p..strokeWidth = 2);
      canvas.drawLine(Offset(x, beam), Offset(x + 34, beam + 56), p);
      canvas.drawArc(Rect.fromCenter(center: Offset(x, beam + 56), width: 92, height: 30), 0, math.pi, true, Paint()..color = i == 0 ? figStrong[0] : figStrong[2]);
      paintLabel(canvas, t, Offset(x, beam + 28), size: 16, weight: FontWeight.w900, bg: Colors.white, maxWidth: size.width * 0.32);
    }
    paintLabel(canvas, 'Seimbang: kiri = kanan', Offset(cx, 14), size: 12.5, color: color);
  }

  @override
  bool shouldRepaint(covariant BalancePainter old) => old.left != left || old.right != right;
}
