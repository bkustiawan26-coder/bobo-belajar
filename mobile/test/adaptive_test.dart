import 'package:bobo_belajar/widgets/common.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('grid columns follow available width', () {
    expect(gridColumns(360), 2);
    expect(gridColumns(700), 3);
    expect(gridColumns(920), 4);
    expect(gridColumns(2000), 4);
  });

  test('tablet detection uses the shortest side', () {
    expect(isTabletSize(const Size(411, 891)), isFalse);
    expect(isTabletSize(const Size(800, 1280)), isTrue);
    expect(isTabletSize(const Size(1280, 800)), isTrue);
  });

  testWidgets('content is centered and capped on wide screens', (tester) async {
    tester.view.physicalSize = const Size(1280, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: ContentWidth(child: SizedBox.expand(key: Key('c'))))));
    final box = tester.getRect(find.byKey(const Key('c')));
    expect(box.width, kContentMaxWidth);
    expect(box.left, (1280 - kContentMaxWidth) / 2);
  });

  testWidgets('content keeps full width on phones', (tester) async {
    tester.view.physicalSize = const Size(400, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: ContentWidth(child: SizedBox.expand(key: Key('c'))))));
    expect(tester.getRect(find.byKey(const Key('c'))).width, 400);
  });
}
