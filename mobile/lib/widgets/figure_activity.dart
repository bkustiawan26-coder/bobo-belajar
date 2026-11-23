import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../core/theme.dart';
import 'figures.dart';

class FigureActivity extends StatefulWidget {
  const FigureActivity({super.key, required this.spec, required this.theme, this.say = defaultSay, this.cheers = const ['Hebat! Kamu berhasil.'], this.retry = 'Belum pas. Coba lagi, ya!', this.onDone});

  final Map<String, dynamic> spec;
  final BandTheme theme;
  final Say say;
  final List<String> cheers;
  final String retry;
  final VoidCallback? onDone;

  @override
  State<FigureActivity> createState() => _FigureActivityState();
}

List<int> stableShuffle(int n, String seedText) {
  final order = List<int>.generate(n, (i) => i);
  if (n < 2) {
    return order;
  }
  var seed = 7;
  for (final c in seedText.codeUnits) {
    seed = (seed * 31 + c) & 0x7fffffff;
  }
  order.shuffle(math.Random(seed));
  var same = true;
  for (var i = 0; i < n; i++) {
    if (order[i] != i) {
      same = false;
    }
  }
  if (same) {
    order.add(order.removeAt(0));
  }
  return order;
}

class _FigureActivityState extends State<FigureActivity> with SingleTickerProviderStateMixin {
  bool _done = false;
  int _tries = 0;
  int _wrongAt = -1;
  String _note = '';
  final List<int> _picked = [];
  final Map<int, int> _placed = {};
  int _selected = -1;
  final Set<int> _visited = {};
  final Set<int> _colored = {};
  List<int> _digits = [];
  double? _point;
  bool? _pointOk;
  int _pickWrong = -1;
  bool _revealed = false;
  int _findAt = 0;
  final Map<int, int> _matched = {};
  late final AnimationController _pop = AnimationController(vsync: this, duration: const Duration(milliseconds: 650));

  Map<String, dynamic> get s => widget.spec;
  String get mode => (s['mode'] ?? '').toString();
  String get seed => (s['ask'] ?? '').toString();

  @override
  void initState() {
    super.initState();
    _prepare();
  }

  void _prepare() {
    if (mode == 'order' && s['fixed_first'] == true) {
      _picked.add(0);
    }
    if (mode == 'build') {
      _digits = List<int>.filled(s['value'].toString().length, 0);
    }
  }

  @override
  void didUpdateWidget(covariant FigureActivity oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.spec != widget.spec) {
      _digits = [];
      _reset();
      _picked.clear();
      _prepare();
    }
  }

  @override
  void dispose() {
    _pop.dispose();
    super.dispose();
  }

  void _success() {
    if (_done) {
      return;
    }
    setState(() {
      _done = true;
      _note = '';
    });
    _pop.forward(from: 0);
    final cheer = widget.cheers[(seed.length + _tries) % widget.cheers.length];
    widget.say(cheer);
    widget.onDone?.call();
  }

  void _miss(String? hint) {
    _tries++;
    setState(() => _note = hint ?? widget.retry);
    widget.say(hint ?? widget.retry);
  }

  void _reset() {
    setState(() {
      _done = false;
      _tries = 0;
      _wrongAt = -1;
      _note = '';
      _picked
        ..clear()
        ..addAll(mode == 'order' && s['fixed_first'] == true ? [0] : const []);
      _placed.clear();
      _selected = -1;
      _visited.clear();
      _colored.clear();
      _digits = mode == 'build' ? List<int>.filled(s['value'].toString().length, 0) : <int>[];
      _point = null;
      _pointOk = null;
      _pickWrong = -1;
      _revealed = false;
      _findAt = 0;
      _matched.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(color: t.soft, borderRadius: BorderRadius.circular(14)),
        child: Row(children: [
          const Text('🎯', style: TextStyle(fontSize: 26)),
          const SizedBox(width: 10),
          Expanded(child: Text(seed, style: TextStyle(fontSize: 15.5, fontWeight: FontWeight.w800, color: t.ink, height: 1.3))),
          IconButton(
            tooltip: 'Dengarkan perintah',
            onPressed: () => widget.say(seed),
            icon: Icon(Icons.volume_up_rounded, color: t.ink),
          ),
        ]),
      ),
      const SizedBox(height: 12),
      _body(),
      if (_note.isNotEmpty && !_done) ...[
        const SizedBox(height: 10),
        Container(
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(color: Palette.warnBg, borderRadius: BorderRadius.circular(12), border: Border.all(color: Palette.warnSoft)),
          child: Row(children: [
            const Text('🤔', style: TextStyle(fontSize: 20)),
            const SizedBox(width: 8),
            Expanded(child: Text(_note, style: const TextStyle(color: Palette.warnInk, fontWeight: FontWeight.w700, fontSize: 14))),
          ]),
        ),
      ],
      if (_done) ...[
        const SizedBox(height: 12),
        ScaleTransition(
          scale: CurvedAnimation(parent: _pop, curve: Curves.elasticOut),
          child: Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(gradient: const LinearGradient(colors: [Color(0xFFDCFCE7), Color(0xFFFEF9C3)]), borderRadius: BorderRadius.circular(16), border: Border.all(color: Palette.ok, width: 2)),
            child: Row(children: [
              const Text('🌟', style: TextStyle(fontSize: 34)),
              const SizedBox(width: 10),
              Expanded(child: Text(widget.cheers[(seed.length + _tries) % widget.cheers.length], style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: Palette.okInk))),
              const Text('🎉', style: TextStyle(fontSize: 28)),
            ]),
          ),
        ),
        Align(
          alignment: Alignment.centerRight,
          child: TextButton.icon(onPressed: _reset, icon: const Icon(Icons.replay_rounded, size: 18), label: const Text('Main lagi'), style: TextButton.styleFrom(foregroundColor: t.ink, minimumSize: const Size(0, 44))),
        ),
      ],
    ]);
  }

  Widget _body() {
    switch (mode) {
      case 'order':
        return _order();
      case 'sort':
        return _sort();
      case 'match':
        return _match();
      case 'find':
        return _find();
      case 'color':
        return _color();
      case 'build':
        return _build();
      case 'point':
        return _pointLine();
      case 'pick':
        return _pick();
      case 'reveal':
        return _reveal();
      default:
        return _explore();
    }
  }

  Widget _show() {
    final show = s['show'];
    if (show is! Map) {
      return const SizedBox.shrink();
    }
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: LessonFigure(spec: Map<String, dynamic>.from(show), theme: widget.theme, say: widget.say, quiz: true),
    );
  }

  Widget _slot(int n, Widget? child) => Container(
        constraints: const BoxConstraints(minHeight: 52, minWidth: 52),
        padding: const EdgeInsets.all(4),
        decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(14), border: Border.all(color: widget.theme.accent.withValues(alpha: 0.45), width: 2)),
        child: child ?? Center(child: Text('$n', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: widget.theme.accent.withValues(alpha: 0.6)))),
      );

  Widget _order() {
    final items = figList(s['items']);
    final order = stableShuffle(items.length, seed);
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Wrap(spacing: 6, runSpacing: 6, alignment: WrapAlignment.center, children: [
        for (var i = 0; i < items.length; i++)
          SizedBox(
            width: items[0].containsKey('say') ? double.infinity : 104,
            child: _slot(i + 1, i < _picked.length ? _orderCard(items[_picked[i]], _picked[i], true) : null),
          ),
      ]),
      const SizedBox(height: 14),
      if (!_done) Text('Kartu:', style: TextStyle(fontWeight: FontWeight.w800, color: widget.theme.ink)),
      const SizedBox(height: 6),
      Wrap(spacing: 8, runSpacing: 8, alignment: WrapAlignment.center, children: [
        for (final i in order)
          if (!_picked.contains(i))
            GestureDetector(
              onTap: _done
                  ? null
                  : () {
                      final want = _picked.length;
                      widget.say(figText(items[i]));
                      if (i == want) {
                        setState(() {
                          _picked.add(i);
                          _wrongAt = -1;
                          _note = '';
                        });
                        if (_picked.length == items.length) {
                          _success();
                        }
                      } else {
                        setState(() => _wrongAt = i);
                        _miss('Hmm, belum yang itu. Kartu nomor ${want + 1} yang mana, ya?');
                      }
                    },
              child: SizedBox(width: items[0].containsKey('say') ? double.infinity : 104, child: _orderCard(items[i], i, false, wrong: _wrongAt == i)),
            ),
      ]),
    ]);
  }

  Widget _orderCard(Map<String, dynamic> it, int i, bool done, {bool wrong = false}) {
    if (it.containsKey('say')) {
      return FigChip(item: {'icon': it['icon'], 'label': '${it['label']}: ${it['say']}'}, index: i, done: done, wrong: wrong);
    }
    return FigChip(item: it, index: i, done: done, wrong: wrong);
  }

  Widget _sort() {
    final groups = figList(s['groups']);
    final cards = figList(s['cards']);
    final order = stableShuffle(cards.length, seed);
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Wrap(spacing: 8, runSpacing: 8, alignment: WrapAlignment.center, children: [
        for (final i in order)
          if (!_placed.containsKey(i))
            GestureDetector(
              onTap: () {
                setState(() => _selected = i);
                widget.say(figText(cards[i]));
              },
              child: AnimatedScale(
                scale: _selected == i ? 1.08 : 1,
                duration: const Duration(milliseconds: 160),
                child: FigChip(item: cards[i], index: 4, active: _selected == i, wrong: _wrongAt == i),
              ),
            ),
      ]),
      const SizedBox(height: 12),
      Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
        for (final (gi, g) in groups.indexed) ...[
          if (gi > 0) const SizedBox(width: 8),
          Expanded(
            child: GestureDetector(
              onTap: () {
                if (_selected < 0 || _done) {
                  widget.say(_selected < 0 ? 'Pilih kartunya dulu, lalu ketuk kelompoknya.' : figText(g));
                  return;
                }
                final c = _selected;
                if ((cards[c]['group'] as num).toInt() == gi) {
                  setState(() {
                    _placed[c] = gi;
                    _selected = -1;
                    _wrongAt = -1;
                    _note = '';
                  });
                  if (_placed.length == cards.length) {
                    _success();
                  } else {
                    widget.say('Betul!');
                  }
                } else {
                  setState(() => _wrongAt = c);
                  _miss('Hmm, "${cards[c]['label']}" bukan di kelompok itu. Coba kelompok lain!');
                }
              },
              child: Container(
                constraints: const BoxConstraints(minHeight: 120),
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(color: figSoft[gi % 8].withValues(alpha: 0.7), borderRadius: BorderRadius.circular(16), border: Border.all(color: _selected >= 0 ? figStrong[gi % 8] : Colors.transparent, width: 2.5)),
                child: Column(children: [
                  FigChip(item: g, index: gi),
                  const SizedBox(height: 6),
                  for (final e in _placed.entries)
                    if (e.value == gi)
                      Padding(padding: const EdgeInsets.only(bottom: 4), child: FigChip(item: cards[e.key], index: gi, done: true)),
                ]),
              ),
            ),
          ),
        ],
      ]),
    ]);
  }

  Widget _match() {
    final pairs = [for (final p in s['pairs'] as List) [for (final x in p as List) x.toString()]];
    final right = stableShuffle(pairs.length, seed);
    Widget cell(String text, bool done, bool active, bool wrong, VoidCallback? onTap) => GestureDetector(
          onTap: onTap,
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 180),
            margin: const EdgeInsets.only(bottom: 8),
            constraints: const BoxConstraints(minHeight: 48),
            padding: const EdgeInsets.all(10),
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: done ? Palette.okSoft : (wrong ? Palette.badSoft : Colors.white),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: done ? Palette.ok : (active ? widget.theme.accent : const Color(0xFFCBD5E1)), width: active ? 2.5 : 1.5),
            ),
            child: Text(text, textAlign: TextAlign.center, style: TextStyle(fontSize: 14, fontWeight: FontWeight.w700, color: done ? Palette.okInk : Palette.ink)),
          ),
        );
    return Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Expanded(
        child: Column(children: [
          for (var i = 0; i < pairs.length; i++)
            cell(pairs[i][0], _matched.containsKey(i), _selected == i, false, _matched.containsKey(i) || _done
                ? null
                : () {
                    setState(() => _selected = i);
                    widget.say(pairs[i][0]);
                  }),
        ]),
      ),
      Padding(padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 12), child: Icon(Icons.swap_horiz_rounded, color: widget.theme.accent)),
      Expanded(
        child: Column(children: [
          for (final j in right)
            cell(pairs[j][1], _matched.containsValue(j), false, _wrongAt == j, _matched.containsValue(j) || _done
                ? null
                : () {
                    if (_selected < 0) {
                      widget.say('Ketuk dulu kotak di kiri, ya.');
                      return;
                    }
                    if (_selected == j) {
                      setState(() {
                        _matched[_selected] = j;
                        _selected = -1;
                        _wrongAt = -1;
                        _note = '';
                      });
                      if (_matched.length == pairs.length) {
                        _success();
                      } else {
                        widget.say('Cocok!');
                      }
                    } else {
                      setState(() => _wrongAt = j);
                      _miss('Belum cocok. Coba pasangan lain!');
                    }
                  }),
        ]),
      ),
    ]);
  }

  Widget _find() {
    final items = figList(s['items']);
    final order = stableShuffle(items.length, seed);
    final targetOrder = stableShuffle(items.length, '$seed#');
    final target = _findAt < items.length ? targetOrder[_findAt] : -1;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      if (!_done && target >= 0)
        Center(
          child: FilledButton.tonalIcon(
            onPressed: () => widget.say(items[target]['label'].toString()),
            icon: const Icon(Icons.hearing_rounded),
            label: Text('Cari: ${items[target]['label']}', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
            style: FilledButton.styleFrom(minimumSize: const Size(0, 52), backgroundColor: widget.theme.soft, foregroundColor: widget.theme.ink),
          ),
        ),
      const SizedBox(height: 10),
      Wrap(spacing: 8, runSpacing: 8, alignment: WrapAlignment.center, children: [
        for (final i in order)
          GestureDetector(
            onTap: _done || target < 0
                ? null
                : () {
                    if (i == target) {
                      setState(() {
                        _visited.add(i);
                        _findAt++;
                        _wrongAt = -1;
                        _note = '';
                      });
                      if (_findAt >= items.length) {
                        _success();
                      } else {
                        widget.say('Betul! Sekarang cari ${items[targetOrder[_findAt]]['label']}.');
                      }
                    } else {
                      setState(() => _wrongAt = i);
                      _miss('Itu ${items[i]['label']}. Cari ${items[target]['label']}, ya!');
                    }
                  },
            child: SizedBox(width: 96, child: FigChip(item: {'icon': items[i]['icon']}, index: i, big: true, done: _visited.contains(i), wrong: _wrongAt == i)),
          ),
      ]),
    ]);
  }

  Widget _color() {
    final n = (s['n'] as num).toInt();
    final d = (s['d'] as num).toInt();
    final t = widget.theme;
    return Column(children: [
      Row(children: [
        for (var i = 0; i < d; i++)
          Expanded(
            child: GestureDetector(
              onTap: _done
                  ? null
                  : () => setState(() {
                        if (!_colored.remove(i)) {
                          _colored.add(i);
                        }
                        _note = '';
                      }),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 180),
                height: 54,
                margin: EdgeInsets.only(right: i == d - 1 ? 0 : 3),
                decoration: BoxDecoration(color: _colored.contains(i) ? t.accent : const Color(0xFFE2E8F0), borderRadius: BorderRadius.circular(8), border: Border.all(color: Colors.white, width: 1)),
              ),
            ),
          ),
      ]),
      const SizedBox(height: 10),
      SizedBox(width: 130, height: 130, child: CustomPaint(painter: PiePainter(n: n, d: d, color: t.accent, filled: _colored))),
      const SizedBox(height: 8),
      Text('${_colored.length}/$d', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w900, color: t.ink)),
      const SizedBox(height: 8),
      if (!_done)
        FilledButton(
          onPressed: () {
            if (_colored.length == n) {
              _success();
            } else {
              _miss(_colored.length < n ? 'Masih kurang. Kamu baru mewarnai ${_colored.length} bagian, perlu $n.' : 'Kebanyakan. Kamu mewarnai ${_colored.length} bagian, cukup $n.');
            }
          },
          style: FilledButton.styleFrom(backgroundColor: t.accent, minimumSize: const Size(160, 48)),
          child: const Text('Periksa', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 16)),
        ),
    ]);
  }

  Widget _build() {
    const names = ['Satuan', 'Puluhan', 'Ratusan', 'Ribuan', 'Puluh ribuan', 'Ratus ribuan', 'Jutaan', 'Puluh jutaan', 'Ratus jutaan'];
    final target = s['value'].toString();
    final k = target.length;
    final t = widget.theme;
    final now = _digits.join();
    return Column(children: [
      Row(children: [
        for (var i = 0; i < k; i++)
          Expanded(
            child: Container(
              margin: const EdgeInsets.symmetric(horizontal: 2),
              padding: const EdgeInsets.symmetric(vertical: 6),
              decoration: BoxDecoration(color: figSoft[(k - 1 - i) % 8], borderRadius: BorderRadius.circular(12)),
              child: Column(children: [
                FittedBox(child: Text(names[k - 1 - i], style: TextStyle(fontSize: 11, fontWeight: FontWeight.w700, color: figInk[(k - 1 - i) % 8]))),
                IconButton(
                  visualDensity: VisualDensity.compact,
                  onPressed: _done ? null : () => setState(() => _digits[i] = (_digits[i] + 1) % 10),
                  icon: Icon(Icons.add_circle_rounded, color: figStrong[(k - 1 - i) % 8], size: 30),
                ),
                Text('${_digits[i]}', style: TextStyle(fontSize: 30, fontWeight: FontWeight.w900, color: figInk[(k - 1 - i) % 8])),
                IconButton(
                  visualDensity: VisualDensity.compact,
                  onPressed: _done ? null : () => setState(() => _digits[i] = (_digits[i] + 9) % 10),
                  icon: Icon(Icons.remove_circle_rounded, color: figStrong[(k - 1 - i) % 8], size: 30),
                ),
              ]),
            ),
          ),
      ]),
      const SizedBox(height: 10),
      Text(groupDigits(now), style: TextStyle(fontSize: 26, fontWeight: FontWeight.w900, color: t.ink)),
      const SizedBox(height: 8),
      if (!_done)
        FilledButton(
          onPressed: () {
            if (now == target) {
              _success();
            } else {
              final i = List<int>.generate(k, (x) => x).firstWhere((x) => now[x] != target[x]);
              _miss('Hampir! Periksa lagi angka di tempat ${names[k - 1 - i].toLowerCase()}.');
            }
          },
          style: FilledButton.styleFrom(backgroundColor: t.accent, minimumSize: const Size(160, 48)),
          child: const Text('Periksa', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 16)),
        ),
    ]);
  }

  Widget _pointLine() {
    final from = (s['from'] as num).toDouble();
    final to = (s['to'] as num).toDouble();
    final step = (s['step'] as num).toDouble();
    final target = (s['target'] as num).toDouble();
    return LayoutBuilder(builder: (context, box) {
      final size = Size(box.maxWidth, 110);
      return GestureDetector(
        onTapUp: _done
            ? null
            : (e) {
                final v = NumberLinePainter.valueAt(e.localPosition.dx, size, from, to, step);
                if (v == null) {
                  return;
                }
                final ok = (v - target).abs() < 1e-6;
                setState(() {
                  _point = v;
                  _pointOk = ok;
                });
                if (ok) {
                  _success();
                } else {
                  _miss('Itu angka ${fmtNum(v)}. ${v < target ? 'Geser ke kanan' : 'Geser ke kiri'}, ya!');
                }
              },
        child: SizedBox(width: size.width, height: size.height, child: CustomPaint(painter: NumberLinePainter(from: from, to: to, step: step, color: widget.theme.accent, selected: _point, correct: _pointOk))),
      );
    });
  }

  Widget _pick() {
    final options = [for (final o in s['options'] as List) o.toString()];
    final answer = (s['answer'] as num).toInt();
    final order = stableShuffle(options.length, seed);
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      _show(),
      Wrap(spacing: 8, runSpacing: 8, alignment: WrapAlignment.center, children: [
        for (final i in order)
          SizedBox(
            width: 150,
            child: OutlinedButton(
              onPressed: _done
                  ? null
                  : () {
                      if (i == answer) {
                        _success();
                      } else {
                        setState(() => _pickWrong = i);
                        _miss(null);
                      }
                    },
              style: OutlinedButton.styleFrom(
                minimumSize: const Size(0, 52),
                backgroundColor: _done && i == answer ? Palette.okSoft : (_pickWrong == i ? Palette.badSoft : Colors.white),
                side: BorderSide(color: _done && i == answer ? Palette.ok : (_pickWrong == i ? Palette.bad : widget.theme.accent), width: 2),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                foregroundColor: Palette.ink,
                disabledForegroundColor: Palette.ink,
              ),
              child: Text(options[i], textAlign: TextAlign.center, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
            ),
          ),
      ]),
    ]);
  }

  Widget _reveal() {
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      _show(),
      if (!_revealed)
        Center(
          child: FilledButton.icon(
            onPressed: () {
              setState(() => _revealed = true);
              _success();
            },
            icon: const Icon(Icons.visibility_rounded),
            label: const Text('Lihat jawaban', style: TextStyle(fontWeight: FontWeight.w800)),
            style: FilledButton.styleFrom(backgroundColor: widget.theme.accent, minimumSize: const Size(180, 48)),
          ),
        )
      else
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Palette.okBg, borderRadius: BorderRadius.circular(12), border: Border.all(color: Palette.okSoft)),
          child: Text('Jawaban:\n${s['answer']}', style: const TextStyle(fontFamily: 'monospace', fontSize: 14.5, fontWeight: FontWeight.w700, color: Palette.okInk, height: 1.4)),
        ),
    ]);
  }

  Widget _explore() {
    final items = figList(s['items']);
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      _show(),
      Wrap(spacing: 8, runSpacing: 8, alignment: WrapAlignment.center, children: [
        for (final (i, it) in items.indexed)
          ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 300),
            child: FigChip(
              item: it,
              index: i,
              done: _visited.contains(i),
              onTap: () {
                widget.say(figText(it));
                setState(() => _visited.add(i));
                if (_visited.length == items.length) {
                  _success();
                }
              },
            ),
          ),
      ]),
      if (!_done) ...[
        const SizedBox(height: 8),
        Text('${_visited.length} dari ${items.length} sudah kamu dengarkan', textAlign: TextAlign.center, style: const TextStyle(fontSize: 12.5, color: Palette.muted, fontWeight: FontWeight.w600)),
      ],
    ]);
  }
}
