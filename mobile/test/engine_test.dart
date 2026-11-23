import 'dart:convert';
import 'dart:io';

import 'package:bobo_belajar/core/api.dart';
import 'package:bobo_belajar/local/content.dart';
import 'package:bobo_belajar/local/engine.dart';
import 'package:bobo_belajar/local/pin.dart';
import 'package:bobo_belajar/local/store.dart';
import 'package:flutter_test/flutter_test.dart';

Content loadContent() => Content(Map<String, dynamic>.from(jsonDecode(File('test/fixtures/sample-content.json').readAsStringSync()) as Map));

class Clock {
  DateTime t = DateTime.utc(2026, 11, 2, 3);

  DateTime call() => t;

  void days(int n) => t = t.add(Duration(days: n));
}

Future<(LocalEngine, Clock, String)> setup({int grade = 5, MemoryStore? store}) async {
  final clock = Clock();
  final e = LocalEngine(store ?? MemoryStore(), loadContent(), clock: clock.call);
  final c = Map<String, dynamic>.from(await e.parent('POST', '/parent/children', body: {'nickname': 'Nadia', 'grade': grade}) as Map);
  return (e, clock, c['id'] as String);
}

Future<Map<String, dynamic>> answer(LocalEngine e, String child, int qid, Map<String, dynamic> response, {String mode = 'practice'}) async =>
    Map<String, dynamic>.from(await e.student(child, 'POST', '/student/practice/attempts', body: {'question_id': qid, 'response': response, 'mode': mode}) as Map);

void main() {
  test('pbkdf2 dan kode pemulihan', () {
    final h = hashSecret('2468', iterations: 1000);
    expect(verifySecret('2468', h), isTrue);
    expect(verifySecret('1357', h), isFalse);
    expect(newRecoveryCode(), matches(RegExp(r'^[A-Z2-9]{5}-[A-Z2-9]{5}$')));
    expect(normalizeRecoveryCode('abcde-23456'), 'ABCDE23456');
  });

  test('PIN, kunci 5 kali salah, dan reset dengan kode pemulihan', () async {
    final clock = Clock();
    final e = LocalEngine(MemoryStore(), loadContent(), clock: clock.call);
    expect(await e.hasPin(), isFalse);
    final code = await e.setupPin('2468');
    expect(await e.hasPin(), isTrue);
    await e.verifyPin('2468');
    for (var i = 0; i < 4; i++) {
      await expectLater(e.verifyPin('0000'), throwsA(isA<ApiException>().having((x) => x.status, 'status', 401)));
    }
    await expectLater(e.verifyPin('0000'), throwsA(isA<ApiException>().having((x) => x.status, 'status', 423)));
    await expectLater(e.verifyPin('2468'), throwsA(isA<ApiException>().having((x) => x.status, 'status', 423)));
    clock.t = clock.t.add(const Duration(minutes: 16));
    await e.verifyPin('2468');
    await expectLater(e.resetPinWithRecovery('XXXXX-XXXXX', '1111'), throwsA(isA<ApiException>()));
    final code2 = await e.resetPinWithRecovery(code.toLowerCase(), '1111');
    expect(code2, isNot(code));
    await e.verifyPin('1111');
    await expectLater(e.resetPinWithRecovery(code, '2222'), throwsA(isA<ApiException>()));
  });

  test('profil anak divalidasi dan dibatasi', () async {
    final (e, _, _) = await setup();
    await expectLater(e.parent('POST', '/parent/children', body: {'nickname': 'R2', 'grade': 3}), throwsA(isA<ApiException>()));
    await expectLater(e.parent('POST', '/parent/children', body: {'nickname': 'Raka', 'grade': 10}), throwsA(isA<ApiException>()));
    for (var i = 0; i < 5; i++) {
      await e.parent('POST', '/parent/children', body: {'nickname': 'Anak ${String.fromCharCode(65 + i)}', 'grade': 2});
    }
    await expectLater(e.parent('POST', '/parent/children', body: {'nickname': 'Lebih', 'grade': 2}), throwsA(isA<ApiException>().having((x) => x.status, 'status', 409)));
    final kids = (await e.parent('GET', '/parent/children') as Map)['children'] as List;
    expect(kids.length, 6);
  });

  test('katalog, materi, latihan tanpa kunci, dan progres', () async {
    final (e, _, child) = await setup();
    final cat = await e.student(child, 'GET', '/student/catalog') as Map;
    final mat = (cat['subjects'] as List).cast<Map>().firstWhere((s) => s['ready'] == true);
    expect((mat['chapters'] as List).isNotEmpty, isTrue);
    final practice = (await e.student(child, 'GET', '/student/practice') as Map)['questions'] as List;
    expect(practice, isNotEmpty);
    expect(practice.cast<Map>().every((q) => !q.containsKey('answer')), isTrue);
    expect(practice.cast<Map>().map((q) => q['id']), isNot(contains(15)));
    final lesson = await e.student(child, 'GET', '/student/lessons/2') as Map;
    expect(lesson['blocks'], isNotEmpty);
    await expectLater(e.student(child, 'GET', '/student/lessons/3'), throwsA(isA<ApiException>().having((x) => x.status, 'status', 404)));
    final p = await e.student(child, 'POST', '/student/lessons/2/progress', body: {'step': 99, 'completed': true}) as Map;
    expect(p['completed'], isTrue);
    expect(p['step'], (lesson['blocks'] as List).length - 1);
  });

  test('jawaban salah dijadwalkan ulang 1, 3, 7 hari', () async {
    final (e, clock, child) = await setup();
    final r = await answer(e, child, 12, {'index': 2});
    expect(r['correct'], isFalse);
    expect(r['scaffold'], isNotNull);
    expect(((await e.student(child, 'GET', '/student/review')) as Map)['questions'], isEmpty);
    clock.days(1);
    final due = (await e.student(child, 'GET', '/student/review')) as Map;
    expect((due['questions'] as List).single['id'], 12);
    await answer(e, child, 12, {'index': 0}, mode: 'review');
    clock.days(1);
    expect(((await e.student(child, 'GET', '/student/review')) as Map)['questions'], isEmpty);
    clock.days(2);
    await answer(e, child, 12, {'index': 0}, mode: 'review');
    clock.days(7);
    await answer(e, child, 12, {'index': 0}, mode: 'review');
    clock.days(30);
    expect(((await e.student(child, 'GET', '/student/review')) as Map)['due'], 0);
    final ok = await answer(e, child, 12, {'index': 0});
    expect(ok['correct'], isTrue);
    expect(ok['scaffold'], isNull);
  });

  test('penguasaan butuh minimal 3 jawaban dan rekomendasi bisa ditandai', () async {
    final (e, _, child) = await setup();
    await answer(e, child, 10, {'index': 0});
    var dash = await e.parent('GET', '/parent/children/$child/dashboard') as Map;
    var m = (dash['mastery'] as List).cast<Map>().firstWhere((x) => x['topic_id'] == 4);
    expect(m['state'], 'insufficient');
    await answer(e, child, 11, {'indices': [0, 1, 3]});
    await answer(e, child, 14, {'text': ' 4 '});
    dash = await e.parent('GET', '/parent/children/$child/dashboard') as Map;
    m = (dash['mastery'] as List).cast<Map>().firstWhere((x) => x['topic_id'] == 4);
    expect(m['state'], 'demonstrated');
    final recs = ((await e.parent('GET', '/parent/children/$child/recommendations')) as Map)['recommendations'] as List;
    final good = recs.cast<Map>().firstWhere((r) => r['id'] == 'good:4');
    final done = await e.parent('POST', '/parent/children/$child/recommendations/${good['id']}/done', body: {'done': true}) as Map;
    expect(done['done'], isTrue);
    final again = ((await e.parent('GET', '/parent/children/$child/recommendations')) as Map)['recommendations'] as List;
    expect(again.cast<Map>().firstWhere((r) => r['id'] == 'good:4')['done'], isTrue);
    await answer(e, child, 10, {'index': 1});
    final after = ((await e.parent('GET', '/parent/children/$child/recommendations')) as Map)['recommendations'] as List;
    expect(after.cast<Map>().where((r) => r['id'] == 'good:4' && r['done'] == true), isEmpty);
  });

  test('jalur pondasi lintas kelas dan sinyal pendampingan', () async {
    final (e, clock, child) = await setup();
    for (var i = 0; i < 6; i++) {
      await answer(e, child, 12, {'index': 1});
      if (i.isOdd) {
        clock.days(1);
      }
    }
    final home = await e.student(child, 'GET', '/student/home') as Map;
    final f = (home['foundation'] as List).cast<Map>();
    expect(f.map((x) => x['topic_id']), containsAll([4, 1]));
    expect(f.firstWhere((x) => x['topic_id'] == 1)['grade'], 2);
    final prereqPractice = (await e.student(child, 'GET', '/student/practice', query: {'topic_id': '1'}) as Map)['questions'] as List;
    expect(prereqPractice, isNotEmpty);
    final lowerLesson = await e.student(child, 'GET', '/student/lessons/1') as Map;
    expect(lowerLesson['id'], 1);
    for (var i = 0; i < 4; i++) {
      await answer(e, child, 12, {'index': 1});
    }
    final dash = await e.parent('GET', '/parent/children/$child/dashboard') as Map;
    final signals = (dash['signals'] as List).cast<Map>();
    expect(signals.single['topic_id'], 5);
    expect((signals.single['plan'] as List).length, 7);
    final summary = (await e.parent('GET', '/parent/children/$child/summary') as Map)['text'] as String;
    expect(summary, contains('bukan diagnosis'));
    expect(summary, contains('Perlu perhatian'));
  });

  test('pilihan lebih sedikit tetap menyisakan jawaban benar', () async {
    final (e, _, child) = await setup();
    await e.parent('PATCH', '/parent/children/$child', body: {'settings': {'fewer_options': true, 'unknown': true}});
    final me = await e.student(child, 'GET', '/student/me') as Map;
    expect((me['settings'] as Map).keys.toSet(), settingKeys);
    final qs = ((await e.student(child, 'GET', '/student/practice') as Map)['questions'] as List).cast<Map>();
    final q12 = qs.firstWhere((q) => q['id'] == 12);
    expect((q12['options'] as List).length, 3);
    expect((q12['options'] as List).cast<Map>().map((o) => o['index']), contains(0));
  });

  test('asesmen: waktu, simpan, kumpulkan sekali, hasil', () async {
    final (e, clock, child) = await setup();
    final list = await e.student(child, 'GET', '/student/assessments') as Map;
    final a = (list['assessments'] as List).cast<Map>().single;
    final sess = await e.student(child, 'POST', '/student/assessments/${a['id']}/start') as Map;
    final sid = sess['session_id'] as String;
    final again = await e.student(child, 'POST', '/student/assessments/${a['id']}/start') as Map;
    expect(again['session_id'], sid);
    final qs = (sess['questions'] as List).cast<Map>();
    expect(qs.every((q) => !q.containsKey('answer')), isTrue);
    await e.student(child, 'PUT', '/student/assessment-sessions/$sid/answers', body: {'question_id': 15, 'response': {'index': 0}});
    await expectLater(e.student(child, 'PUT', '/student/assessment-sessions/$sid/answers', body: {'question_id': 12, 'response': {'index': 0}}), throwsA(isA<ApiException>().having((x) => x.status, 'status', 422)));
    final res = await e.student(child, 'POST', '/student/assessment-sessions/$sid/submit', body: {'idempotency_key': 'abcdefgh12', 'answers': [{'question_id': 17, 'response': {'index': 0}}]}) as Map;
    expect(res['correct'], 2);
    expect(res['total'], 5);
    expect(res['score'], 40);
    final dup = await e.student(child, 'POST', '/student/assessment-sessions/$sid/submit', body: {'idempotency_key': 'abcdefgh12', 'answers': []}) as Map;
    expect(dup['score'], 40);
    final result = await e.student(child, 'GET', '/student/assessment-sessions/$sid/result') as Map;
    expect((result['review'] as List).length, 5);
    final s2 = await e.student(child, 'POST', '/student/assessments/${a['id']}/start') as Map;
    clock.t = clock.t.add(const Duration(hours: 2));
    await expectLater(e.student(child, 'PUT', '/student/assessment-sessions/${s2['session_id']}/answers', body: {'question_id': 15, 'response': {'index': 0}}), throwsA(isA<ApiException>().having((x) => x.status, 'status', 409)));
    final listAfter = await e.student(child, 'GET', '/student/assessments') as Map;
    expect((listAfter['assessments'] as List).cast<Map>().single['active_session_id'], isNull);
    final dash = await e.parent('GET', '/parent/children/$child/dashboard') as Map;
    expect((dash['assessments'] as List).length, 2);
  });

  test('tutor lokal: sumber, gaya lain, penolakan data pribadi, batas harian', () async {
    final (e, _, child) = await setup();
    final r = await e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'Apa itu pecahan senilai?'}) as Map;
    expect(r['sources'], isNotEmpty);
    expect(r['can_restyle'], isTrue);
    final v = await e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'Apa itu pecahan senilai?', 'style': 'visual'}) as Map;
    expect(v['visual'], 'frac');
    final st = await e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'Apa itu pecahan senilai?', 'style': 'steps'}) as Map;
    expect(st['reply'] as String, startsWith('Langkah demi langkah'));
    final no = await e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'boleh minta nomor hp kamu?'}) as Map;
    expect(no['refused'], isTrue);
    final pii = await e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'nomorku 081234567890 ya'}) as Map;
    expect(pii['category'], 'pii_share');
    final out = await e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'Siapa presiden pertama Amerika?'}) as Map;
    expect(out['reply'] as String, contains('hanya menjawab dari materi'));
    final kids = ((await e.parent('GET', '/parent/children')) as Map)['children'] as List;
    expect((kids.single as Map)['safety_refusals'], 2);
    await e.parent('PATCH', '/parent/children/$child', body: {'tutor_daily_limit': 6});
    await expectLater(e.student(child, 'POST', '/student/tutor/messages', body: {'text': 'pecahan'}), throwsA(isA<ApiException>().having((x) => x.status, 'status', 429)));
  });

  test('tanya BOBO menolak diagnosis', () async {
    final (e, _, child) = await setup();
    final r = await e.parent('POST', '/parent/assistant/messages', body: {'child_id': child, 'text': 'Apakah anak saya disleksia?'}) as Map;
    expect(r['reply'] as String, contains('tidak memberi diagnosis'));
    final ok = await e.parent('POST', '/parent/assistant/messages', body: {'child_id': child, 'text': 'Bagaimana membangun rutinitas belajar yang sehat?'}) as Map;
    expect(ok['reply'] as String, contains('kelas 5–6'));
  });

  test('cadangan dipulihkan ke perangkat lain dan hapus data', () async {
    final (e, _, child) = await setup();
    await answer(e, child, 12, {'index': 0});
    final backup = Map<String, dynamic>.from(await e.parent('GET', '/parent/export') as Map);
    final roundTrip = Map<String, dynamic>.from(jsonDecode(jsonEncode(backup)) as Map);
    final other = LocalEngine(MemoryStore(), loadContent());
    await expectLater(other.parent('POST', '/parent/import', body: {'backup': {'app': 'lain'}}), throwsA(isA<ApiException>()));
    final r = await other.parent('POST', '/parent/import', body: {'backup': roundTrip}) as Map;
    expect(r['children'], 1);
    final g = await other.parent('GET', '/parent/children/$child/growth') as Map;
    expect(g['total_answers'], 1);
    await other.student(child, 'POST', '/student/practice/attempts', body: {'question_id': 12, 'response': {'index': 0}});
    expect((await other.parent('GET', '/parent/children/$child/growth') as Map)['total_answers'], 2);
    await e.setupPin('2468');
    await expectLater(e.parent('POST', '/parent/delete-account', body: {'confirm': 'hapus'}), throwsA(isA<ApiException>()));
    await e.parent('POST', '/parent/delete-account', body: {'confirm': 'HAPUS'});
    expect(await e.hasPin(), isFalse);
    expect(((await e.parent('GET', '/parent/children')) as Map)['children'], isEmpty);
  });

  test('hapus satu profil menghapus seluruh datanya', () async {
    final store = MemoryStore();
    final (e, _, child) = await setup(store: store);
    await answer(e, child, 12, {'index': 1});
    await e.parent('DELETE', '/parent/children/$child');
    for (final col in dataCollections) {
      expect((store.data[col] ?? {}).values.where((d) => d['child_id'] == child || d['id'] == child), isEmpty, reason: col);
    }
  });
}
