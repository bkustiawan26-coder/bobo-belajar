@Tags(['shots'])
library;

import 'dart:convert';
import 'dart:io';
import 'dart:ui' as ui;

import 'package:bobo_belajar/core/persona.dart';
import 'package:bobo_belajar/core/theme.dart';
import 'package:bobo_belajar/widgets/common.dart';
import 'package:bobo_belajar/widgets/figure_activity.dart';
import 'package:bobo_belajar/widgets/figures.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

import '../speech_corpus_test.dart' show spokenCorpus;

Future<void> loadFont(String family, List<String> paths) async {
  final loader = FontLoader(family);
  var any = false;
  for (final p in paths) {
    final f = File(p);
    if (f.existsSync()) {
      loader.addFont(Future.value(ByteData.view(f.readAsBytesSync().buffer)));
      any = true;
    }
  }
  if (any) {
    await loader.load();
  }
}

void main() {
  final fixtures = jsonDecode(File('test/fixtures/figures.json').readAsStringSync()) as Map<String, dynamic>;
  final theme = BandTheme.forGrade(4);
  final out = Directory('shots')..createSync(recursive: true);

  test('contoh ucapan BOBO', () {
    final corpus = spokenCorpus();
    final buf = StringBuffer();
    for (final raw in corpus) {
      final spoken = toSpoken(raw);
      if (spoken != raw.trim()) {
        buf.writeln('$raw\n    => $spoken');
      }
    }
    File('${out.path}/spoken.txt').writeAsStringSync(buf.toString());
  });

  testWidgets('tangkapan layar gambar dan aktivitas', (tester) async {
    await tester.runAsync(() async {
      await loadFont('PlusJakartaSans', ['assets/fonts/PlusJakartaSans-Regular.ttf', 'assets/fonts/PlusJakartaSans-Bold.ttf', 'assets/fonts/PlusJakartaSans-ExtraBold.ttf']);
      await loadFont('Emoji', ['/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf']);
      await loadFont('AmiriQuran', ['assets/fonts/AmiriQuran.ttf']);
      final root = Platform.environment['FLUTTER_ROOT'] ?? '';
      await loadFont('MaterialIcons', ['$root/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf']);
    });
    tester.view.devicePixelRatio = 2;
    tester.view.physicalSize = const Size(780, 2400);
    addTearDown(tester.view.reset);
    final items = <(String, Widget)>[
      for (final (i, f) in (fixtures['figures'] as List).indexed) ('fig_${i.toString().padLeft(2, '0')}_${(f as Map)['type']}', LessonFigure(spec: Map<String, dynamic>.from(f), theme: theme, say: (_, {gender}) {})),
      for (final (i, a) in (fixtures['activities'] as List).indexed) ('act_${i.toString().padLeft(2, '0')}_${(a as Map)['mode']}', FigureActivity(key: UniqueKey(), spec: Map<String, dynamic>.from(a), theme: theme, say: (_, {gender}) {})),
    ];
    final tablet = <(String, Widget)>[
      for (final (i, f) in (fixtures['figures'] as List).indexed)
        if (const {'cycle', 'mind', 'hijaiyah', 'compare', 'chat', 'venn', 'coord'}.contains((f as Map)['type']))
          ('tab_${i.toString().padLeft(2, '0')}_${f['type']}', ContentWidth(child: LessonFigure(spec: Map<String, dynamic>.from(f), theme: theme, say: (_, {gender}) {}))),
    ];
    for (final (name, w) in [...items, ...tablet]) {
      if (name.startsWith('tab_')) {
        tester.view.physicalSize = const Size(2560, 3200);
      }
      final key = GlobalKey();
      await tester.pumpWidget(MaterialApp(
        theme: ThemeData(fontFamily: 'PlusJakartaSans', textTheme: const TextTheme().apply(fontFamilyFallback: const ['Emoji'])),
        home: Scaffold(
          backgroundColor: Colors.white,
          body: SingleChildScrollView(
            child: RepaintBoundary(key: key, child: Container(color: Colors.white, padding: const EdgeInsets.all(16), child: DefaultTextStyle.merge(style: const TextStyle(fontFamilyFallback: ['Emoji']), child: w))),
          ),
        ),
      ));
      await tester.pumpAndSettle();
      await tester.runAsync(() async {
        final boundary = key.currentContext!.findRenderObject()! as RenderRepaintBoundary;
        final image = await boundary.toImage(pixelRatio: 2);
        final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
        File('${out.path}/$name.png').writeAsBytesSync(bytes!.buffer.asUint8List());
      });
    }
  });
}
