import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:just_audio/just_audio.dart';
import 'package:path_provider/path_provider.dart';
import 'package:record/record.dart';

import '../core/speech.dart';
import '../core/theme.dart';

const quranFont = 'AmiriQuran';
const basmalahText = 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ';

String ayahAsset(int surah, int ayah) => 'assets/quran/audio/${surah.toString().padLeft(3, '0')}${ayah.toString().padLeft(3, '0')}.mp3';

String arabicNumber(int n) {
  const digits = '٠١٢٣٤٥٦٧٨٩';
  return n.toString().split('').map((d) => digits[int.parse(d)]).join();
}

class QuranData {
  QuranData._(this.raw);

  final Map<String, dynamic> raw;
  static QuranData? _cache;

  static Future<QuranData> load() async {
    return _cache ??= QuranData._(jsonDecode(await rootBundle.loadString('assets/quran/quran.json')) as Map<String, dynamic>);
  }

  String get reciter => (raw['reciter'] ?? '').toString();

  Map<String, dynamic>? surah(int n) {
    final s = (raw['surahs'] as Map?)?['$n'];
    return s == null ? null : Map<String, dynamic>.from(s as Map);
  }

  String? ayah(int surah, int ayah) => (this.surah(surah)?['ayahs'] as Map?)?['$ayah']?.toString();
}

class RecitationPlayer {
  RecitationPlayer();

  AudioPlayer? _player;
  final List<StreamSubscription<dynamic>> _subs = [];
  final ValueNotifier<int> index = ValueNotifier(-1);
  final ValueNotifier<bool> playing = ValueNotifier(false);

  AudioPlayer _ensure() {
    final existing = _player;
    if (existing != null) {
      return existing;
    }
    final p = AudioPlayer();
    _subs.add(p.currentIndexStream.listen((i) {
      if (playing.value) {
        index.value = i ?? -1;
      }
    }));
    _subs.add(p.playerStateStream.listen((s) {
      if (s.processingState == ProcessingState.completed) {
        playing.value = false;
        index.value = -1;
        p.stop();
      }
    }));
    _player = p;
    return p;
  }

  Future<void> playAssets(List<String> assets) async {
    Speech.instance.stop();
    final p = _ensure();
    await p.stop();
    await p.setAudioSources([for (final a in assets) AudioSource.asset(a)], initialIndex: 0);
    playing.value = true;
    index.value = 0;
    unawaited(p.play());
  }

  Future<void> playFile(String path) async {
    Speech.instance.stop();
    final p = _ensure();
    await p.stop();
    await p.setFilePath(path);
    playing.value = true;
    index.value = 0;
    unawaited(p.play());
  }

  Future<void> stop() async {
    playing.value = false;
    index.value = -1;
    await _player?.stop();
  }

  Future<void> dispose() async {
    for (final s in _subs) {
      await s.cancel();
    }
    await _player?.dispose();
    index.dispose();
    playing.dispose();
  }
}

class QuranCard extends StatefulWidget {
  const QuranCard({super.key, required this.surah, required this.from, required this.to, required this.theme});

  final int surah;
  final int from;
  final int to;
  final BandTheme theme;

  @override
  State<QuranCard> createState() => _QuranCardState();
}

class _QuranCardState extends State<QuranCard> {
  final _player = RecitationPlayer();
  QuranData? _data;
  List<int> _queue = [];

  bool get _basmalah => widget.from == 1 && widget.surah != 1 && widget.surah != 9;

  List<int> get _lines => [if (_basmalah) 0, for (var a = widget.from; a <= widget.to; a++) a];

  String _asset(int line) => line == 0 ? ayahAsset(1, 1) : ayahAsset(widget.surah, line);

  @override
  void initState() {
    super.initState();
    QuranData.load().then((d) {
      if (mounted) {
        setState(() => _data = d);
      }
    });
  }

  @override
  void dispose() {
    _player.dispose();
    super.dispose();
  }

  Future<void> _playAll() async {
    _queue = _lines;
    await _player.playAssets([for (final l in _queue) _asset(l)]);
  }

  Future<void> _playLine(int line) async {
    _queue = [line];
    await _player.playAssets([_asset(line)]);
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    final data = _data;
    final surah = data?.surah(widget.surah);
    final name = surah?['name']?.toString() ?? 'Surah ${widget.surah}';
    final range = widget.from == widget.to ? 'ayat ${widget.from}' : 'ayat ${widget.from} sampai ${widget.to}';
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(color: const Color(0xFFF0FDF4), borderRadius: BorderRadius.circular(18), border: Border.all(color: const Color(0xFFBBF7D0), width: 1.5)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Row(children: [
          const Text('📖', style: TextStyle(fontSize: 26)),
          const SizedBox(width: 8),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('$name, $range', style: const TextStyle(fontSize: 15.5, fontWeight: FontWeight.w800, color: Color(0xFF14532D))),
              if (data != null && data.reciter.isNotEmpty) Text('Bacaan qari ${data.reciter}', style: const TextStyle(fontSize: 12.5, color: Color(0xFF166534), fontWeight: FontWeight.w600)),
            ]),
          ),
        ]),
        const SizedBox(height: 10),
        ValueListenableBuilder<bool>(
          valueListenable: _player.playing,
          builder: (context, playing, _) => FilledButton.icon(
            style: FilledButton.styleFrom(backgroundColor: const Color(0xFF16A34A), padding: const EdgeInsets.symmetric(vertical: 12), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
            onPressed: playing ? _player.stop : _playAll,
            icon: Icon(playing ? Icons.stop_rounded : Icons.play_arrow_rounded),
            label: Text(playing ? 'Berhenti' : 'Dengarkan bacaan qari', style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 15)),
          ),
        ),
        const SizedBox(height: 10),
        if (data == null)
          const Padding(padding: EdgeInsets.all(12), child: Center(child: CircularProgressIndicator()))
        else
          ValueListenableBuilder<int>(
            valueListenable: _player.index,
            builder: (context, idx, _) {
              final activeLine = idx < 0 || idx >= _queue.length ? -1 : _queue[idx];
              return Column(children: [
                for (final line in _lines) _ayah(line, line == 0 ? basmalahText : (data.ayah(widget.surah, line) ?? ''), activeLine == line),
              ]);
            },
          ),
        const SizedBox(height: 4),
        const Text('Ketuk satu ayat untuk mendengarkan dan menirukan berulang kali.', textAlign: TextAlign.center, style: TextStyle(fontSize: 12, color: Color(0xFF166534), fontWeight: FontWeight.w600)),
      ]),
    );
  }

  Widget _ayah(int line, String text, bool active) {
    return GestureDetector(
      onTap: () => _playLine(line),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 220),
        margin: const EdgeInsets.only(bottom: 6),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        decoration: BoxDecoration(
          color: active ? const Color(0xFFDCFCE7) : Colors.white,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: active ? const Color(0xFF16A34A) : const Color(0xFFE2E8F0), width: active ? 2 : 1),
        ),
        child: Row(children: [
          Icon(active ? Icons.volume_up_rounded : Icons.play_circle_outline_rounded, color: const Color(0xFF16A34A), size: 22),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              line == 0 ? text : '$text ﴿${arabicNumber(line)}﴾',
              textAlign: TextAlign.right,
              textDirection: TextDirection.rtl,
              style: const TextStyle(fontFamily: quranFont, fontSize: 25, height: 2.0, color: Color(0xFF0F172A)),
            ),
          ),
        ]),
      ),
    );
  }
}

class DoaRecordings {
  static Future<File> fileFor(String id) async {
    final dir = Directory('${(await getApplicationDocumentsDirectory()).path}/doa');
    if (!await dir.exists()) {
      await dir.create(recursive: true);
    }
    return File('${dir.path}/$id.m4a');
  }
}

class DoaCard extends StatefulWidget {
  const DoaCard({super.key, required this.id, required this.title, required this.latin, required this.meaning, required this.theme});

  final String id;
  final String title;
  final String latin;
  final String meaning;
  final BandTheme theme;

  @override
  State<DoaCard> createState() => _DoaCardState();
}

class _DoaCardState extends State<DoaCard> {
  final _player = RecitationPlayer();
  AudioRecorder? _recorder;
  bool _recording = false;
  bool _has = false;
  String? _message;

  @override
  void initState() {
    super.initState();
    _check();
  }

  Future<void> _check() async {
    try {
      final f = await DoaRecordings.fileFor(widget.id);
      final has = await f.exists() && await f.length() > 0;
      if (mounted) {
        setState(() => _has = has);
      }
    } catch (_) {}
  }

  @override
  void dispose() {
    _player.dispose();
    _recorder?.dispose();
    super.dispose();
  }

  Future<void> _start() async {
    Speech.instance.stop();
    await _player.stop();
    final rec = _recorder ??= AudioRecorder();
    try {
      if (!await rec.hasPermission()) {
        setState(() => _message = 'Izin mikrofon belum diberikan. Buka pengaturan HP untuk mengizinkan.');
        return;
      }
      final f = await DoaRecordings.fileFor(widget.id);
      await rec.start(const RecordConfig(encoder: AudioEncoder.aacLc, sampleRate: 44100, bitRate: 96000, numChannels: 1), path: f.path);
      setState(() {
        _recording = true;
        _message = null;
      });
    } catch (_) {
      setState(() => _message = 'Mikrofon tidak bisa dipakai saat ini.');
    }
  }

  Future<void> _finish() async {
    final rec = _recorder;
    if (rec == null) {
      return;
    }
    await rec.stop();
    setState(() {
      _recording = false;
      _message = 'Rekaman tersimpan. Anak bisa mendengarkannya kapan saja.';
    });
    await _check();
  }

  Future<void> _play() async {
    final f = await DoaRecordings.fileFor(widget.id);
    await _player.playFile(f.path);
  }

  Future<void> _confirmRecord() async {
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Rekam bacaan doa'),
        content: Text('Bagian ini untuk Ayah, Bunda, atau ustaz. Bacakan "${widget.title}" dengan pelan dan jelas supaya anak bisa menirukan.${_has ? '\n\nRekaman lama akan diganti.' : ''}'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Batal')),
          FilledButton(onPressed: () => Navigator.pop(context, true), child: const Text('Mulai rekam')),
        ],
      ),
    );
    if (ok == true) {
      await _start();
    }
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.theme;
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(color: const Color(0xFFFFFBEB), borderRadius: BorderRadius.circular(18), border: Border.all(color: const Color(0xFFFDE68A), width: 1.5)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Row(children: [
          const Text('🤲', style: TextStyle(fontSize: 26)),
          const SizedBox(width: 8),
          Expanded(child: Text(widget.title, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: Color(0xFF78350F)))),
        ]),
        const SizedBox(height: 10),
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(14)),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(widget.latin, style: const TextStyle(fontSize: 16, fontStyle: FontStyle.italic, fontWeight: FontWeight.w700, height: 1.6, color: Color(0xFF0F172A))),
            const SizedBox(height: 8),
            Text('Artinya: ${widget.meaning}', style: const TextStyle(fontSize: 14, height: 1.5, color: Color(0xFF475569))),
          ]),
        ),
        const SizedBox(height: 10),
        if (_has && !_recording)
          ValueListenableBuilder<bool>(
            valueListenable: _player.playing,
            builder: (context, playing, _) => FilledButton.icon(
              style: FilledButton.styleFrom(backgroundColor: const Color(0xFFD97706), padding: const EdgeInsets.symmetric(vertical: 12), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
              onPressed: playing ? _player.stop : _play,
              icon: Icon(playing ? Icons.stop_rounded : Icons.play_arrow_rounded),
              label: Text(playing ? 'Berhenti' : 'Dengarkan bacaan Ayah/Bunda', style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 15)),
            ),
          ),
        if (!_has && !_recording)
          const Padding(
            padding: EdgeInsets.only(bottom: 6),
            child: Text('Belum ada rekaman. Minta Ayah, Bunda, atau ustaz membacakan doa ini, lalu rekam di sini.', textAlign: TextAlign.center, style: TextStyle(fontSize: 13, color: Color(0xFF92400E), fontWeight: FontWeight.w600)),
          ),
        const SizedBox(height: 6),
        _recording
            ? FilledButton.icon(
                style: FilledButton.styleFrom(backgroundColor: const Color(0xFFDC2626), padding: const EdgeInsets.symmetric(vertical: 12), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
                onPressed: _finish,
                icon: const Icon(Icons.stop_circle_rounded),
                label: const Text('Selesai merekam', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 15)),
              )
            : OutlinedButton.icon(
                style: OutlinedButton.styleFrom(foregroundColor: const Color(0xFF92400E), side: const BorderSide(color: Color(0xFFF59E0B)), padding: const EdgeInsets.symmetric(vertical: 10), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusSmall))),
                onPressed: _confirmRecord,
                icon: const Icon(Icons.mic_rounded),
                label: Text(_has ? 'Rekam ulang (untuk orang tua)' : 'Rekam bacaan (untuk orang tua)', style: const TextStyle(fontWeight: FontWeight.w700)),
              ),
        if (_message != null) ...[
          const SizedBox(height: 8),
          Text(_message!, textAlign: TextAlign.center, style: const TextStyle(fontSize: 12.5, color: Color(0xFF78350F))),
        ],
      ]),
    );
  }
}
