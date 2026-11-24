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
    case 'essay':
      return {'text': a['model']};
    default:
      return {'text': (a['accepted'] as List).first};
  }
}

void main() {
  final content = bundled();

  test('bundle berisi materi, latihan, dan asesmen untuk kelas 1 sampai 9', () {
    expect(content.includesSample, isTrue);
    const expected = {1: 7, 2: 7, 3: 9, 4: 9, 5: 10, 6: 10, 7: 12, 8: 12, 9: 12};
    final typeOf = {for (final q in content.questions) (q['id'] as num).toInt(): q['type']};
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
          expect(content.practiceCount(tid), 20, reason: 'latihan ${t['title']}');
        }
        final chapters = content.chaptersOfSubject(sid);
        expect({for (final ch in chapters) (ch['semester'] as num).toInt()}, {1, 2}, reason: 'semester kelas $g ${s['name']}');
        final exams = content.assessments.where((a) => (a['grade'] as num).toInt() == g && a['short_title'] == s['name']).toList();
        expect(exams.length, 2, reason: 'asesmen kelas $g ${s['name']}');
        expect({for (final a in exams) (a['semester'] as num).toInt()}, {1, 2});
        final want = g <= 6 ? [20, 10, 5] : [35, 5, 5];
        for (final a in exams) {
          final types = [for (final x in a['questions'] as List) typeOf[((x as Map)['id'] as num).toInt()]];
          expect(types.length, want[0] + want[1] + want[2], reason: '${a['title']}');
          expect(types.where((t) => t == 'mc').length, want[0], reason: '${a['title']}');
          expect(types.where((t) => t == 'fill').length, want[1], reason: '${a['title']}');
          expect(types.where((t) => t == 'essay').length, want[2], reason: '${a['title']}');
        }
      }
    }
  });

  test('setiap materi punya gambar dan aktivitas Ayo coba', () {
    expect(content.lessons.length, 1760);
    for (final l in content.lessons) {
      final blocks = [for (final b in l['blocks'] as List) Map<String, dynamic>.from(b as Map)];
      expect(blocks.map((b) => b['kind']).toList(), ['Penjelasan', 'Contoh', 'Ayo coba', 'Poin penting', 'Ringkasan'], reason: l['title'].toString());
      expect((blocks[0]['figure'] as Map)['type'], isNotNull, reason: l['title'].toString());
      final act = blocks[2]['figure'] as Map;
      expect(act['type'], 'activity');
      expect(const ['order', 'sort', 'match', 'find', 'color', 'build', 'point', 'pick', 'reveal', 'explore', 'letter'], contains(act['mode']));
      expect((blocks[2]['text'] as String).isNotEmpty, isTrue);
    }
  });

  test('setiap kunci jawaban konsisten dengan pilihannya', () {
    for (final q in content.questions) {
      final opts = (q['options'] as List?) ?? const [];
      final a = Map<String, dynamic>.from(q['answer'] as Map);
      if (q['type'] == 'mc' || q['type'] == 'tf') {
        expect((a['index'] as num).toInt(), inInclusiveRange(0, opts.length - 1), reason: '${q['id']}');
      }
      if (q['type'] == 'essay') {
        expect((a['model'] as String).isNotEmpty, isTrue, reason: 'contoh jawaban ${q['id']}');
        expect((a['keys'] as List).isNotEmpty, isTrue, reason: 'poin penting ${q['id']}');
      } else {
        expect(gradeLocally(q, correctResponse(q)), isTrue, reason: 'soal ${q['id']}');
      }
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
      expect((lesson['blocks'] as List).length, 5);
      final practice = (await e.student(id, 'GET', '/student/practice') as Map)['questions'] as List;
      expect(practice.length, greaterThanOrEqualTo(subjects.length * 16));
      final exams = (await e.student(id, 'GET', '/student/assessments') as Map)['assessments'] as List;
      expect(exams.length, subjects.length * 2);
      expect((exams.first as Map)['semester'], 1);
    }
  });

  test('SAS dengan uraian: nilai dari PG dan isian, uraian dicocokkan dengan contoh jawaban', () async {
    final e = LocalEngine(MemoryStore(), content);
    final c = Map<String, dynamic>.from(await e.parent('POST', '/parent/children', body: {'nickname': 'Sari', 'grade': 4}) as Map);
    final id = c['id'] as String;
    final exams = ((await e.student(id, 'GET', '/student/assessments') as Map)['assessments'] as List).cast<Map>();
    final sess = await e.student(id, 'POST', '/student/assessments/${exams.first['id']}/start') as Map;
    final answers = [
      for (final q in (sess['questions'] as List).cast<Map>())
        {'question_id': q['id'], 'response': correctResponse(Map<String, dynamic>.from(content.questionById[(q['id'] as num).toInt()]!))},
    ];
    final res = await e.student(id, 'POST', '/student/assessment-sessions/${sess['session_id']}/submit', body: {'idempotency_key': 'uraian-0001', 'answers': answers}) as Map;
    expect(res['score'], 100);
    expect(res['total'], 30);
    expect(res['essays'], 5);
    final review = (res['review'] as List).cast<Map>();
    expect(review.length, 35);
    expect(review.where((r) => r['essay'] == true && r['needs_review'] == true).length, 5);
  });
}
