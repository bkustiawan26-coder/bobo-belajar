import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';

import 'theme.dart';

class Speech {
  Speech._();

  static final Speech instance = Speech._();
  final FlutterTts _tts = FlutterTts();
  bool _ready = false;
  final ValueNotifier<String?> speaking = ValueNotifier<String?>(null);

  Future<void> _init() async {
    if (_ready) {
      return;
    }
    _ready = true;
    try {
      await _tts.setLanguage('id-ID');
      await _tts.setSpeechRate(0.45);
      await _tts.setPitch(1.0);
      _tts.setCompletionHandler(() => speaking.value = null);
      _tts.setCancelHandler(() => speaking.value = null);
      _tts.setErrorHandler((_) => speaking.value = null);
    } catch (_) {}
  }

  Future<void> speak(String text) async {
    await _init();
    final clean = text.replaceAll('×', ' kali ').replaceAll('÷', ' bagi ').replaceAll('−', ' kurang ').replaceAll('²', ' kuadrat').replaceAll('√', 'akar ').replaceAll('…', ' titik-titik ');
    if (speaking.value == text) {
      await stop();
      return;
    }
    await _tts.stop();
    speaking.value = text;
    try {
      await _tts.speak(clean);
    } catch (_) {
      speaking.value = null;
    }
  }

  Future<void> stop() async {
    speaking.value = null;
    try {
      await _tts.stop();
    } catch (_) {}
  }
}

class SpeakButton extends StatelessWidget {
  const SpeakButton({super.key, required this.text, this.color = Palette.inkSoft, this.label});

  final String text;
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
          return IconButton(onPressed: () => Speech.instance.speak(text), icon: icon, tooltip: on ? 'Berhenti membacakan' : 'Bacakan', constraints: const BoxConstraints(minWidth: 44, minHeight: 44));
        }
        return TextButton.icon(
          onPressed: () => Speech.instance.speak(text),
          icon: icon,
          label: Text(on ? 'Berhenti' : label!, style: TextStyle(color: color, fontWeight: FontWeight.w700)),
          style: TextButton.styleFrom(minimumSize: const Size(44, 44)),
        );
      },
    );
  }
}
