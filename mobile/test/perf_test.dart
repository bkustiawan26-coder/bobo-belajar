import 'dart:convert';
import 'dart:io';

import 'package:bobo_belajar/local/content.dart';
import 'package:bobo_belajar/local/engine.dart';
import 'package:bobo_belajar/local/store.dart';
import 'package:flutter_test/flutter_test.dart';

Map<String, dynamic> m(Object? v) => Map<String, dynamic>.from(v as Map);

void main() {
  test('endpoint siswa dan orang tua tetap cepat dengan bundel penuh', () async {
    final sw = Stopwatch()..start();
    final content = Content(m(jsonDecode(File('assets/content/bobo-content.json').readAsStringSync())));
    final loadMs = sw.elapsedMilliseconds;
    final e = LocalEngine(MemoryStore(), content);
    final child = m(await e.parent('POST', '/parent/children', body: {'nickname': 'Uji', 'grade': 4}));
    final id = child['id'] as String;
    final worst = <String, int>{};
    Future<Object?> time(String name, Future<Object?> Function() f) async {
      final t = Stopwatch()..start();
      Object? r;
      try {
        r = await f();
      } catch (_) {}
      final ms = t.elapsedMilliseconds;
      if (ms > (worst[name] ?? -1)) {
        worst[name] = ms;
      }
      return r;
    }

    for (var round = 0; round < 3; round++) {
      final cat = m(await time('catalog', () => e.student(id, 'GET', '/student/catalog')));
      await time('home', () => e.student(id, 'GET', '/student/home'));
      final lessons = <int>[];
      for (final s in cat['subjects'] as List) {
        for (final ch in (s as Map)['chapters'] as List) {
          for (final tp in (ch as Map)['topics'] as List) {
            final l = (tp as Map)['lesson'];
            if (l != null) {
              lessons.add(((l as Map)['id'] as num).toInt());
            }
          }
        }
      }
      for (final lid in lessons.skip(round * 5).take(5)) {
        await time('lesson', () => e.student(id, 'GET', '/student/lessons/$lid'));
        await time('lesson_progress', () => e.student(id, 'POST', '/student/lessons/$lid/progress', body: {'step': 1, 'completed': true}));
      }
      final p = m(await time('practice_all', () => e.student(id, 'GET', '/student/practice', query: {'limit': '50'})));
      final qs = (p['questions'] as List).take(15).toList();
      for (final q in qs) {
        final qm = m(q);
        final opts = (qm['options'] as List?) ?? const [];
        final resp = opts.isEmpty ? {'text': 'x'} : {'index': ((opts.first as Map)['index'] as num).toInt()};
        await time('attempt', () => e.student(id, 'POST', '/student/practice/attempts', body: {'question_id': qm['id'], 'response': resp, 'mode': 'practice'}));
      }
      await time('review', () => e.student(id, 'GET', '/student/review'));
      await time('growth', () => e.student(id, 'GET', '/student/growth'));
      await time('assessments', () => e.student(id, 'GET', '/student/assessments'));
      await time('tutor', () => e.student(id, 'POST', '/student/tutor/messages', body: {'text': 'apa itu pecahan senilai'}));
      await time('dashboard', () => e.parent('GET', '/parent/children/$id/dashboard'));
      await time('parent_growth', () => e.parent('GET', '/parent/children/$id/growth'));
      await time('recommendations', () => e.parent('GET', '/parent/children/$id/recommendations'));
    }
    final report = (worst.entries.toList()..sort((a, b) => b.value.compareTo(a.value))).map((x) => '${x.key}=${x.value}ms').join(' ');
    stdout.writeln('PERF load=${loadMs}ms $report');
    for (final x in worst.entries) {
      expect(x.value, lessThan(400), reason: '${x.key} ${x.value}ms');
    }
  }, timeout: const Timeout(Duration(minutes: 5)));
}
