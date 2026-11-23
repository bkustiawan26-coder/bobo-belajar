import 'dart:convert';
import 'dart:io';

import 'package:bobo_belajar/core/theme.dart';
import 'package:bobo_belajar/widgets/figure_activity.dart';
import 'package:bobo_belajar/widgets/figures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

final fixtures = jsonDecode(File('test/fixtures/figures.json').readAsStringSync()) as Map<String, dynamic>;
List<Map<String, dynamic>> listOf(String key) => [for (final x in fixtures[key] as List) Map<String, dynamic>.from(x as Map)];

final spoken = <String>[];
void quiet(String text) => spoken.add(text);

Widget host(Widget child) => MaterialApp(home: Scaffold(body: SingleChildScrollView(padding: const EdgeInsets.all(16), child: child)));

Future<void> setWidth(WidgetTester tester, double width) async {
  tester.view.devicePixelRatio = 1;
  tester.view.physicalSize = Size(width, 2400);
  addTearDown(tester.view.reset);
}

void main() {
  final theme = BandTheme.forGrade(4);

  for (final width in [320.0, 800.0]) {
    testWidgets('semua jenis gambar tampil tanpa galat di lebar $width', (tester) async {
      await setWidth(tester, width);
      final shapes = ['square', 'rect', 'tri', 'right', 'circle', 'trap', 'para', 'rhombus', 'cube', 'box', 'cylinder', 'cone', 'sphere', 'prism', 'pyramid3', 'angle'];
      final specs = [
        ...listOf('figures'),
        for (final s in shapes) {'type': 'shape', 'shape': s, 'labels': ['a = 3 cm', 'b = 4 cm', 'c = 5 cm']},
        {'type': 'circuit', 'mode': 'seri', 'n': 3},
        {'type': 'pie', 'items': [{'n': 5, 'd': 4}]},
        {'type': 'frac', 'items': [{'n': 7, 'd': 4}]},
      ];
      for (final spec in specs) {
        await tester.pumpWidget(host(LessonFigure(spec: spec, theme: theme, say: quiet)));
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull, reason: spec['type'].toString());
        await tester.pumpWidget(host(LessonFigure(spec: spec, theme: theme, say: quiet, quiz: true)));
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull, reason: '${spec['type']} kuis');
      }
    });

    testWidgets('semua jenis aktivitas tampil tanpa galat di lebar $width', (tester) async {
      await setWidth(tester, width);
      for (final spec in listOf('activities')) {
        await tester.pumpWidget(host(FigureActivity(key: UniqueKey(), spec: spec, theme: theme, say: quiet)));
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull, reason: spec['mode'].toString());
        expect(find.text(spec['ask'].toString()), findsOneWidget);
      }
    });
  }

  testWidgets('mengurutkan kartu dengan benar memberi pujian', (tester) async {
    await setWidth(tester, 400);
    final spec = {
      'type': 'activity',
      'mode': 'order',
      'ask': 'Ketuk kartu sesuai urutan yang benar.',
      'items': [
        {'icon': '🥚', 'label': 'Telur'},
        {'icon': '🐛', 'label': 'Ulat'},
        {'icon': '🦋', 'label': 'Kupu-kupu'},
      ],
    };
    var done = 0;
    await tester.pumpWidget(host(FigureActivity(spec: spec, theme: theme, say: quiet, cheers: const ['Yeay, berhasil!'], onDone: () => done++)));
    await tester.tap(find.text('Ulat').last);
    await tester.pumpAndSettle();
    expect(done, 0);
    expect(find.textContaining('Kartu nomor 1'), findsOneWidget);
    for (final label in ['Telur', 'Ulat', 'Kupu-kupu']) {
      await tester.tap(find.text(label).last);
      await tester.pumpAndSettle();
    }
    expect(done, 1);
    expect(find.text('Yeay, berhasil!'), findsOneWidget);
    await tester.tap(find.text('Main lagi'));
    await tester.pumpAndSettle();
    expect(find.text('Yeay, berhasil!'), findsNothing);
  });

  testWidgets('memilih jawaban salah lalu benar', (tester) async {
    await setWidth(tester, 400);
    final spec = {'type': 'activity', 'mode': 'pick', 'ask': 'Berapa hasilnya?', 'options': ['5', '6', '4', '7'], 'answer': 0};
    var done = 0;
    await tester.pumpWidget(host(FigureActivity(spec: spec, theme: theme, say: quiet, retry: 'Coba lagi, ya!', onDone: () => done++)));
    await tester.tap(find.text('6'));
    await tester.pumpAndSettle();
    expect(find.text('Coba lagi, ya!'), findsOneWidget);
    await tester.tap(find.text('5'));
    await tester.pumpAndSettle();
    expect(done, 1);
  });

  testWidgets('mengelompokkan kartu ke kelompok yang cocok', (tester) async {
    await setWidth(tester, 400);
    final spec = {
      'type': 'activity',
      'mode': 'sort',
      'ask': 'Ketuk kartu, lalu ketuk kelompok yang cocok.',
      'groups': [
        {'label': 'Fakta'},
        {'label': 'Opini'},
      ],
      'cards': [
        {'label': 'Air mendidih pada 100 °C.', 'group': 0},
        {'label': 'Bakso paling enak.', 'group': 1},
        {'label': 'Jakarta ada di Pulau Jawa.', 'group': 0},
      ],
    };
    var done = 0;
    await tester.pumpWidget(host(FigureActivity(spec: spec, theme: theme, say: quiet, onDone: () => done++)));
    for (final (card, group) in [('Air mendidih pada 100 °C.', 'Fakta'), ('Bakso paling enak.', 'Opini'), ('Jakarta ada di Pulau Jawa.', 'Fakta')]) {
      await tester.tap(find.text(card));
      await tester.pumpAndSettle();
      await tester.tap(find.text(group));
      await tester.pumpAndSettle();
    }
    expect(done, 1);
  });

  test('urutan acak stabil dan tidak sama dengan urutan asli', () {
    final a = stableShuffle(5, 'soal');
    expect(a, stableShuffle(5, 'soal'));
    expect(a, isNot([0, 1, 2, 3, 4]));
    expect(a.toSet(), {0, 1, 2, 3, 4});
  });

  test('ringkasan gambar untuk pembaca layar', () {
    final s = figSummary({'type': 'flow', 'items': [{'icon': '🌊', 'label': 'Laut'}, {'label': 'Awan'}], 'caption': 'Siklus air'});
    expect(s, 'Laut. Awan. Siklus air');
  });
}
