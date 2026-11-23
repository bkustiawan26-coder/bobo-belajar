import 'dart:convert';
import 'dart:io';

import 'package:bobo_belajar/core/grading.dart';
import 'package:bobo_belajar/local/content.dart';
import 'package:bobo_belajar/local/engine.dart';
import 'package:bobo_belajar/local/store.dart';
import 'package:flutter_test/flutter_test.dart';

Content bundled() => Content(Map<String, dynamic>.from(jsonDecode(File('assets/content/bobo-content.json').readAsStringSync()) as Map));

Map<String, dynamic> correctResponse(Map<String, dynamic> q) {
  final a = Map<String, dynamic>.from(q['answer'] as Map);
  switch (q['type']) {
    case 'mc':
    case 'tf':
      return {'index': a['index']};
    case 'multi':
      return {'indices': a['indices']};
    default:
      return {'text': (a['accepted'] as List).first};
  }
}

void main() {
  final content = bundled();

  test('bundle berisi materi, latihan, dan asesmen untuk kelas 1 sampai 9', () {
    expect(content.includesSample, isTrue);
    const expected = {1: 5, 2: 5, 3: 6, 4: 6, 5: 8, 6: 8, 7: 10, 8: 10, 9: 10};
    for (var g = 1; g <= 9; g++) {
      final subjects = content.subjectsOfGrade(g);
      expect(subjects.length, expected[g], reason: 'kelas $g');
      for (final s in subjects) {
        final sid = (s['id'] as num).toInt();
        final topics = [for (final ch in content.chaptersOfSubject(sid)) ...content.topicsOfChapter((ch['id'] as num).toInt())];
        expect(topics.length, greaterThanOrEqualTo(4), reason: 'kelas $g ${s['name']}');
        for (final t in topics) {
          final tid = (t['id'] as num).toInt();
          expect(content.lessonForTopic(tid), isNotNull, reason: 'materi ${t['title']}');
          expect(content.practiceCount(tid), greaterThanOrEqualTo(4), reason: 'latihan ${t['title']}');
        }
        final chapters = content.chaptersOfSubject(sid);
        expect({for (final ch in chapters) (ch['semester'] as num).toInt()}, {1, 2}, reason: 'semester kelas $g ${s['name']}');
        final exams = content.assessments.where((a) => (a['grade'] as num).toInt() == g && a['short_title'] == s['name']).toList();
        expect(exams.length, 2, reason: 'asesmen kelas $g ${s['name']}');
        expect({for (final a in exams) (a['semester'] as num).toInt()}, {1, 2});
        for (final a in exams) {
          expect((a['questions'] as List).length, greaterThanOrEqualTo(5));
        }
      }
    }
  });

  test('setiap kunci jawaban konsisten dengan pilihannya', () {
    for (final q in content.questions) {
      final opts = (q['options'] as List?) ?? const [];
      final a = Map<String, dynamic>.from(q['answer'] as Map);
      if (q['type'] == 'mc' || q['type'] == 'tf') {
        expect((a['index'] as num).toInt(), inInclusiveRange(0, opts.length - 1), reason: '${q['id']}');
      }
      expect(gradeLocally(q, correctResponse(q)), isTrue, reason: 'soal ${q['id']}');
      expect((q['explanation'] as String?)?.isNotEmpty, isTrue, reason: 'pembahasan ${q['id']}');
    }
  });

  test('anak kelas 1 dan kelas 9 melihat semua mapel siap dan bisa berlatih', () async {
    for (final g in [1, 9]) {
      final e = LocalEngine(MemoryStore(), content);
      final c = Map<String, dynamic>.from(await e.parent('POST', '/parent/children', body: {'nickname': 'Raka', 'grade': g}) as Map);
      final id = c['id'] as String;
      final cat = await e.student(id, 'GET', '/student/catalog') as Map;
      final subjects = (cat['subjects'] as List).cast<Map>();
      expect(subjects.every((s) => s['ready'] == true), isTrue);
      final firstTopic = ((subjects.first['chapters'] as List).first as Map)['topics'] as List;
      final lessonId = ((firstTopic.first as Map)['lesson'] as Map)['id'];
      final lesson = await e.student(id, 'GET', '/student/lessons/$lessonId') as Map;
      expect((lesson['blocks'] as List).length, 4);
      final practice = (await e.student(id, 'GET', '/student/practice') as Map)['questions'] as List;
      expect(practice.length, greaterThanOrEqualTo(subjects.length * 16));
      final exams = (await e.student(id, 'GET', '/student/assessments') as Map)['assessments'] as List;
      expect(exams.length, subjects.length * 2);
      expect((exams.first as Map)['semester'], 1);
    }
  });
}
