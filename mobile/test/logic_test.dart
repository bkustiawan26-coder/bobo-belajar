import 'package:bobo_belajar/core/grading.dart';
import 'package:bobo_belajar/core/theme.dart';
import 'package:bobo_belajar/widgets/common.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('gradeLocally', () {
    test('pilihan ganda', () {
      final q = {'type': 'mc', 'answer': {'index': 2}};
      expect(gradeLocally(q, {'index': 2}), isTrue);
      expect(gradeLocally(q, {'index': 1}), isFalse);
      expect(gradeLocally(q, null), isFalse);
    });

    test('pilihan ganda kompleks tidak peduli urutan', () {
      final q = {'type': 'multi', 'answer': {'indices': [0, 1, 3]}};
      expect(gradeLocally(q, {'indices': [3, 0, 1]}), isTrue);
      expect(gradeLocally(q, {'indices': [0, 1]}), isFalse);
    });

    test('isian dinormalisasi', () {
      final q = {'type': 'fill', 'answer': {'accepted': ['0,5', '1/2']}};
      expect(gradeLocally(q, {'text': ' 0.5 '}), isTrue);
      expect(gradeLocally(q, {'text': '1 / 2'}), isTrue);
      expect(gradeLocally(q, {'text': '2'}), isFalse);
    });
  });

  test('tema berbeda per jenjang dan SMP tidak kekanakan', () {
    final sd1 = BandTheme.forGrade(1);
    final smp = BandTheme.forGrade(8);
    expect(sd1.accent, isNot(equals(smp.accent)));
    expect(sd1.body, greaterThan(smp.body));
    expect(sd1.radius, greaterThan(smp.radius));
    expect(gradeLabel(8), 'Kelas 8 · SMP · Fase D');
    expect(gradeLabel(2), 'Kelas 2 · SD · Fase A');
  });

  testWidgets('MasteryChip menampilkan kata, bukan hanya warna', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: MasteryChip(state: 'insufficient', label: 'Bukti belum cukup'))));
    expect(find.text('? Bukti belum cukup'), findsOneWidget);
  });

  testWidgets('EmptyState dan PrimaryButton dapat dirender', (tester) async {
    var tapped = false;
    await tester.pumpWidget(MaterialApp(
      home: Scaffold(
        body: EmptyState(icon: Icons.menu_book_outlined, title: 'Materi sedang ditinjau', body: 'Tunggu ya', action: PrimaryButton(label: 'Coba', onPressed: () => tapped = true)),
      ),
    ));
    await tester.tap(find.text('Coba'));
    expect(tapped, isTrue);
    expect(find.text('Materi sedang ditinjau'), findsOneWidget);
  });
}
