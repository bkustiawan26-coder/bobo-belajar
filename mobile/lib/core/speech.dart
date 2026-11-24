import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';

import 'persona.dart';
import 'theme.dart';

class Speech {
  Speech._();

  static final Speech instance = Speech._();
  final FlutterTts _tts = FlutterTts();
  bool _ready = false;
  int _gen = 0;
  VoiceProfile _profile = VoiceProfile.forGrade(5);
  Map<String, String>? _voice;
  String _lang = 'id';
  final Map<String, bool> _available = {};
  final ValueNotifier<String?> speaking = ValueNotifier<String?>(null);
  final ValueNotifier<int> sentence = ValueNotifier<int>(-1);

  Future<void> _init() async {
    if (_ready) {
      return;
    }
    _ready = true;
    try {
      await _tts.setLanguage('id-ID');
      await _tts.awaitSpeakCompletion(true);
      await _apply();
    } catch (_) {}
  }

  Future<void> _apply() async {
    try {
      await _tts.setSpeechRate(_profile.rate);
      await _tts.setPitch(_profile.pitch);
      if (_voice != null) {
        await _tts.setVoice(_voice!);
      }
    } catch (_) {}
  }

  Future<void> configure(int grade) async {
    _profile = VoiceProfile.forGrade(grade);
    if (_ready) {
      await _apply();
    }
  }

  Future<void> setVoice(Map<String, String>? voice) async {
    _voice = voice;
    if (_ready) {
      if (voice == null) {
        try {
          await _tts.setLanguage('id-ID');
        } catch (_) {}
      }
      _lang = 'id';
      await _apply();
    }
  }

  Map<String, String>? get voice => _voice;

  Future<List<Map<String, String>>> indonesianVoices() async {
    await _init();
    try {
      final raw = await _tts.getVoices;
      final out = <Map<String, String>>[];
      for (final v in (raw as List? ?? const [])) {
        final m = Map<String, dynamic>.from(v as Map);
        final locale = (m['locale'] ?? '').toString().toLowerCase().replaceAll('_', '-');
        if (!locale.startsWith('id') && !locale.startsWith('in')) {
          continue;
        }
        final network = (m['network_required'] ?? '').toString() == '1' || (m['name'] ?? '').toString().contains('network');
        if (network) {
          continue;
        }
        out.add({'name': m['name'].toString(), 'locale': m['locale'].toString()});
      }
      out.sort((a, b) => a['name']!.compareTo(b['name']!));
      return out;
    } catch (_) {
      return const [];
    }
  }

  static const _locales = {'id': 'id-ID', 'en': 'en-US', 'su': 'su-ID'};

  Future<bool> _use(String lang) async {
    if (lang == _lang) {
      return true;
    }
    try {
      if (lang == 'id') {
        await _tts.setLanguage('id-ID');
        if (_voice != null) {
          await _tts.setVoice(_voice!);
        }
      } else {
        final ok = _available[lang] ??= (await _tts.isLanguageAvailable(_locales[lang]!)) == true;
        if (!ok) {
          return false;
        }
        await _tts.setLanguage(_locales[lang]!);
      }
      await _tts.setSpeechRate(_profile.rate);
      await _tts.setPitch(_profile.pitch);
      _lang = lang;
      return true;
    } catch (_) {
      _available[lang] = false;
      return false;
    }
  }

  static String languageOf(String text, {bool englishBias = false, bool sundaneseBias = false}) {
    if (looksEnglish(text, bias: englishBias)) {
      return 'en';
    }
    if (looksSundanese(text, bias: sundaneseBias)) {
      return 'su';
    }
    return 'id';
  }

  static List<(String, String)> plan(String raw, {bool englishBias = false, bool sundaneseBias = false}) {
    final whole = languageOf(raw, englishBias: englishBias, sundaneseBias: sundaneseBias);
    if (whole != 'id') {
      return [(raw, whole)];
    }
    final runs = quotedRuns(raw);
    final out = <(String, String)>[];
    for (final (text, quoted) in runs) {
      out.add((text, quoted ? languageOf(text, englishBias: englishBias, sundaneseBias: sundaneseBias) : 'id'));
    }
    return out.any((r) => r.$2 != 'id') ? out : [(raw, 'id')];
  }

  Future<void> speak(String text, {String? intro, bool englishBias = false, bool sundaneseBias = false}) async {
    await _init();
    if (speaking.value == text) {
      await stop();
      return;
    }
    final my = ++_gen;
    try {
      await _tts.stop();
    } catch (_) {}
    speaking.value = text;
    final lead = intro == null ? const <String>[] : segmentsOf(intro.trim());
    final body = segmentsOf(text.trim());
    final total = lead.length + body.length;
    for (var i = 0; i < total; i++) {
      if (my != _gen) {
        return;
      }
      final isLead = i < lead.length;
      final raw = isLead ? lead[i] : body[i - lead.length];
      sentence.value = isLead ? -1 : i - lead.length;
      final parts = isLead ? [(raw, 'id')] : plan(raw, englishBias: englishBias, sundaneseBias: sundaneseBias);
      var failed = false;
      for (final (part, lang) in parts) {
        if (my != _gen) {
          return;
        }
        final used = await _use(lang) ? lang : 'id';
        if (used == 'id') {
          await _use('id');
        }
        final spoken = toSpoken(part, english: used == 'en');
        if (spoken.isEmpty) {
          continue;
        }
        try {
          await _tts.speak(spoken).timeout(Duration(seconds: 8 + spoken.length ~/ 6));
        } catch (_) {
          failed = true;
          break;
        }
      }
      if (failed) {
        break;
      }
      if (my != _gen) {
        return;
      }
      await Future<void>.delayed(Duration(milliseconds: _profile.pauseMs));
    }
    if (my == _gen) {
      speaking.value = null;
      sentence.value = -1;
      await _use('id');
    }
  }

  Future<void> stop() async {
    _gen++;
    speaking.value = null;
    sentence.value = -1;
    try {
      await _tts.stop();
    } catch (_) {}
  }
}

class SpeakButton extends StatelessWidget {
  const SpeakButton({super.key, required this.text, this.intro, this.color = Palette.inkSoft, this.label, this.englishBias = false, this.sundaneseBias = false});

  final String text;
  final bool englishBias;
  final bool sundaneseBias;
  final String? intro;
  final Color color;
  final String? label;

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<String?>(
      valueListenable: Speech.instance.speaking,
      builder: (context, current, _) {
        final on = current == text;
        final icon = Icon(on ? Icons.stop_circle_outlined : Icons.volume_up_rounded, color: color, size: 20);
        if (label == null) {
          return IconButton(onPressed: () => Speech.instance.speak(text, intro: intro, englishBias: englishBias, sundaneseBias: sundaneseBias), icon: icon, tooltip: on ? 'Berhenti membacakan' : 'Bacakan', constraints: const BoxConstraints(minWidth: 44, minHeight: 44));
        }
        return TextButton.icon(
          onPressed: () => Speech.instance.speak(text, intro: intro, englishBias: englishBias, sundaneseBias: sundaneseBias),
          icon: icon,
          label: Text(on ? 'Berhenti' : label!, style: TextStyle(color: color, fontWeight: FontWeight.w700)),
          style: TextButton.styleFrom(minimumSize: const Size(44, 44)),
        );
      },
    );
  }
}

class ReadAlongText extends StatelessWidget {
  const ReadAlongText({super.key, required this.speechKey, required this.text, required this.offset, required this.style, required this.highlight});

  final String speechKey;
  final String text;
  final int offset;
  final TextStyle style;
  final Color highlight;

  @override
  Widget build(BuildContext context) {
    final segs = segmentsOf(text.trim());
    return ValueListenableBuilder<String?>(
      valueListenable: Speech.instance.speaking,
      builder: (context, current, _) => ValueListenableBuilder<int>(
        valueListenable: Speech.instance.sentence,
        builder: (context, idx, _) {
          final active = current == speechKey ? idx - offset : -1;
          return Text.rich(
            TextSpan(children: [
              for (var i = 0; i < segs.length; i++) TextSpan(text: segs[i], style: i == active ? TextStyle(backgroundColor: highlight, fontWeight: FontWeight.w700) : null),
            ]),
            style: style,
          );
        },
      ),
    );
  }
}
