import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';
import 'package:record/record.dart';

import '../core/speech.dart';
import '../core/theme.dart';
import 'figures.dart';
import 'recitation.dart';

class HijaiyahAudio {
  HijaiyahAudio._();

  static final HijaiyahAudio instance = HijaiyahAudio._();
  final RecitationPlayer player = RecitationPlayer();
  Set<String>? _bundled;
  final ValueNotifier<int> changed = ValueNotifier(0);

  Future<Set<String>> bundled() async {
    final cached = _bundled;
    if (cached != null) {
      return cached;
    }
    try {
      final raw = jsonDecode(await rootBundle.loadString('assets/hijaiyah/index.json')) as Map<String, dynamic>;
      return _bundled = {for (final k in (raw['keys'] as List? ?? const [])) k.toString()};
    } catch (_) {
      return _bundled = <String>{};
    }
  }

  Future<File> recordingFile(String key) async {
    final dir = Directory('${(await getApplicationDocumentsDirectory()).path}/hijaiyah');
    if (!await dir.exists()) {
      await dir.create(recursive: true);
    }
    return File('${dir.path}/$key.m4a');
  }

  Future<bool> has(String key) async {
    if ((await bundled()).contains(key)) {
      return true;
    }
    try {
      final f = await recordingFile(key);
      return await f.exists() && await f.length() > 0;
    } catch (_) {
      return false;
    }
  }

  Future<bool> play(String key) async {
    Speech.instance.stop();
    try {
      if ((await bundled()).contains(key)) {
        await player.playAssets(['assets/hijaiyah/$key.mp3']);
        return true;
      }
      final f = await recordingFile(key);
      if (await f.exists() && await f.length() > 0) {
        await player.playFile(f.path);
        return true;
      }
    } catch (_) {}
    return false;
  }
}

String hijaiyahLabel(Map<String, dynamic> it) => (it['read'] ?? it['name'] ?? '').toString();

class HijaiyahGlyph extends StatelessWidget {
  const HijaiyahGlyph(this.text, {super.key, this.size = 40, this.color = const Color(0xFF0F172A)});

  final String text;
  final double size;
  final Color color;

  @override
  Widget build(BuildContext context) => Text(text, textDirection: TextDirection.rtl, textAlign: TextAlign.center, style: TextStyle(fontFamily: quranFont, fontSize: size, height: 1.6, color: color));
}

class HijaiyahBoard extends StatefulWidget {
  const HijaiyahBoard({super.key, required this.spec, required this.theme});

  final Map<String, dynamic> spec;
  final BandTheme theme;

  @override
  State<HijaiyahBoard> createState() => _HijaiyahBoardState();
}

class _HijaiyahBoardState extends State<HijaiyahBoard> {
  int _active = -1;
  bool _recordMode = false;
  String? _recordingKey;
  AudioRecorder? _recorder;
  String? _note;
  Set<String> _available = {};

  List<Map<String, dynamic>> get _items => figList(widget.spec['items']);

  @override
  void initState() {
    super.initState();
    _refresh();
  }

  @override
  void dispose() {
    _recorder?.dispose();
    super.dispose();
  }

  Future<void> _refresh() async {
    final out = <String>{};
    for (final it in _items) {
      final key = it['key'].toString();
      if (await HijaiyahAudio.instance.has(key)) {
        out.add(key);
      }
    }
    if (mounted) {
      setState(() => _available = out);
    }
  }

  Future<void> _tap(int i) async {
    final it = _items[i];
    final key = it['key'].toString();
    setState(() {
      _active = i;
      _note = null;
    });
    if (_recordMode) {
      await _toggleRecord(key);
      return;
    }
    final ok = await HijaiyahAudio.instance.play(key);
    if (!ok && mounted) {
      setState(() => _note = '${it['name']}${it['read'] != null ? ', dibaca "${it['read']}"' : ''}. Suaranya belum ada: minta Ayah, Bunda, atau ustaz merekamnya.');
    }
  }

  Future<void> _toggleRecord(String key) async {
    final rec = _recorder ??= AudioRecorder();
    try {
      if (_recordingKey == key) {
        await rec.stop();
        setState(() {
          _recordingKey = null;
          _note = 'Tersimpan. Ketuk huruf lain untuk merekam berikutnya.';
        });
        await _refresh();
        return;
      }
      if (_recordingKey != null) {
        await rec.stop();
      }
      if (!await rec.hasPermission()) {
        setState(() => _note = 'Izin mikrofon belum diberikan.');
        return;
      }
      final f = await HijaiyahAudio.instance.recordingFile(key);
      await rec.start(const RecordConfig(encoder: AudioEncoder.aacLc, sampleRate: 44100, bitRate: 96000, numChannels: 1), path: f.path);
      setState(() {
        _recordingKey = key;
        _note = 'Merekam… bacakan dengan makhraj yang benar, lalu ketuk huruf yang sama untuk selesai.';
      });
    } catch (_) {
      setState(() {
        _recordingKey = null;
        _note = 'Mikrofon tidak bisa dipakai saat ini.';
      });
    }
  }

  Future<void> _confirmRecordMode() async {
    if (_recordMode) {
      if (_recordingKey != null) {
        await _recorder?.stop();
      }
      setState(() {
        _recordMode = false;
        _recordingKey = null;
        _note = null;
      });
      await _refresh();
      return;
    }
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Rekam suara huruf'),
        content: const Text('Bagian ini untuk Ayah, Bunda, atau ustaz. Ketuk satu huruf untuk mulai merekam, bacakan dengan makhraj yang benar, lalu ketuk huruf yang sama untuk selesai.'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Batal')),
          FilledButton(onPressed: () => Navigator.pop(context, true), child: const Text('Mulai')),
        ],
      ),
    );
    if (ok == true) {
      setState(() => _recordMode = true);
    }
  }

  void _trace(Map<String, dynamic> it) {
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      showDragHandle: true,
      builder: (_) => Padding(padding: const EdgeInsets.fromLTRB(16, 0, 16, 24), child: TracePad(glyph: it['glyph'].toString(), title: 'Tulis huruf ${it['name']}', theme: widget.theme)),
    );
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    final items = _items;
    final sambung = widget.spec['mode'] == 'sambung';
    final active = _active >= 0 && _active < items.length ? items[_active] : null;
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(color: const Color(0xFFF0FDF4), borderRadius: BorderRadius.circular(18), border: Border.all(color: const Color(0xFFBBF7D0), width: 1.5)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Wrap(
          alignment: WrapAlignment.center,
          textDirection: TextDirection.rtl,
          spacing: 8,
          runSpacing: 8,
          children: [
            for (final (i, it) in items.indexed)
              GestureDetector(
                onTap: () => _tap(i),
                child: AnimatedContainer(
                  duration: const Duration(milliseconds: 180),
                  width: sambung ? 150 : 82,
                  padding: const EdgeInsets.symmetric(vertical: 6, horizontal: 4),
                  decoration: BoxDecoration(
                    color: _recordingKey == it['key'] ? const Color(0xFFFEE2E2) : (_active == i ? const Color(0xFFDCFCE7) : Colors.white),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: _recordingKey == it['key'] ? const Color(0xFFDC2626) : (_active == i ? const Color(0xFF16A34A) : const Color(0xFFE2E8F0)), width: _active == i ? 2 : 1),
                  ),
                  child: Column(mainAxisSize: MainAxisSize.min, children: [
                    if (sambung)
                      FittedBox(
                        fit: BoxFit.scaleDown,
                        child: Row(mainAxisSize: MainAxisSize.min, textDirection: TextDirection.rtl, children: [
                          for (final f in (it['forms'] as List? ?? const [])) Padding(padding: const EdgeInsets.symmetric(horizontal: 4), child: HijaiyahGlyph(f.toString(), size: 24)),
                        ]),
                      )
                    else
                      HijaiyahGlyph(it['glyph'].toString(), size: 38),
                    Text(hijaiyahLabel(it), style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w800, color: Color(0xFF166534))),
                    Icon(_recordingKey == it['key'] ? Icons.fiber_manual_record_rounded : (_available.contains(it['key']) ? Icons.volume_up_rounded : Icons.volume_off_rounded), size: 15, color: _recordingKey == it['key'] ? const Color(0xFFDC2626) : const Color(0xFF16A34A)),
                  ]),
                ),
              ),
          ],
        ),
        if (sambung) ...[
          const SizedBox(height: 6),
          const Text('Urutan bentuk dari kanan: berdiri sendiri, di awal, di tengah, di akhir.', textAlign: TextAlign.center, style: TextStyle(fontSize: 12, color: Color(0xFF166534), fontWeight: FontWeight.w600)),
        ],
        if (_note != null) ...[
          const SizedBox(height: 8),
          Text(_note!, textAlign: TextAlign.center, style: const TextStyle(fontSize: 13, color: Color(0xFF14532D), fontWeight: FontWeight.w600)),
        ],
        const SizedBox(height: 8),
        Wrap(alignment: WrapAlignment.center, spacing: 8, runSpacing: 6, children: [
          if (active != null && !_recordMode)
            FilledButton.icon(
              style: FilledButton.styleFrom(backgroundColor: const Color(0xFF16A34A), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
              onPressed: () => _trace(active),
              icon: const Icon(Icons.draw_rounded),
              label: Text('Latihan menulis ${active['name']}'),
            ),
          OutlinedButton.icon(
            style: OutlinedButton.styleFrom(foregroundColor: const Color(0xFF166534), side: const BorderSide(color: Color(0xFF86EFAC)), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
            onPressed: _confirmRecordMode,
            icon: Icon(_recordMode ? Icons.check_rounded : Icons.mic_rounded),
            label: Text(_recordMode ? 'Selesai merekam' : 'Rekam suara (orang tua/ustaz)'),
          ),
        ]),
      ]),
    );
  }
}

class TracePad extends StatefulWidget {
  const TracePad({super.key, required this.glyph, required this.title, required this.theme});

  final String glyph;
  final String title;
  final BandTheme theme;

  @override
  State<TracePad> createState() => _TracePadState();
}

class _TracePadState extends State<TracePad> {
  final List<List<Offset>> _strokes = [];

  @override
  Widget build(BuildContext context) {
    return Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Text(widget.title, textAlign: TextAlign.center, style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w800)),
      const SizedBox(height: 4),
      const Text('Ikuti bentuk huruf dengan jarimu. Huruf Arab ditulis dari kanan.', textAlign: TextAlign.center, style: TextStyle(fontSize: 13, color: Color(0xFF475569))),
      const SizedBox(height: 10),
      AspectRatio(
        aspectRatio: 1.1,
        child: Container(
          decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(18), border: Border.all(color: const Color(0xFFE2E8F0), width: 1.5)),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(18),
            child: Stack(fit: StackFit.expand, children: [
              Center(child: FittedBox(child: Padding(padding: const EdgeInsets.all(8), child: HijaiyahGlyph(widget.glyph, size: 220, color: const Color(0xFFD1FAE5))))),
              GestureDetector(
                onPanStart: (d) => setState(() => _strokes.add([d.localPosition])),
                onPanUpdate: (d) => setState(() => _strokes.last.add(d.localPosition)),
                child: CustomPaint(painter: _InkPainter(_strokes, widget.theme.accent), size: Size.infinite),
              ),
            ]),
          ),
        ),
      ),
      const SizedBox(height: 10),
      Row(children: [
        Expanded(child: OutlinedButton.icon(onPressed: _strokes.isEmpty ? null : () => setState(() => _strokes.removeLast()), icon: const Icon(Icons.undo_rounded), label: const Text('Urungkan'))),
        const SizedBox(width: 8),
        Expanded(child: FilledButton.icon(onPressed: () => setState(_strokes.clear), icon: const Icon(Icons.refresh_rounded), label: const Text('Ulangi'))),
      ]),
    ]);
  }
}

class _InkPainter extends CustomPainter {
  _InkPainter(this.strokes, this.color);

  final List<List<Offset>> strokes;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..color = color
      ..strokeWidth = 14
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round
      ..style = PaintingStyle.stroke;
    for (final s in strokes) {
      if (s.length == 1) {
        canvas.drawCircle(s.first, 7, p..style = PaintingStyle.fill);
        p.style = PaintingStyle.stroke;
        continue;
      }
      final path = Path()..moveTo(s.first.dx, s.first.dy);
      for (final o in s.skip(1)) {
        path.lineTo(o.dx, o.dy);
      }
      canvas.drawPath(path, p);
    }
  }

  @override
  bool shouldRepaint(covariant _InkPainter old) => true;
}
