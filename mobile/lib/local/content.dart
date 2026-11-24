import 'dart:convert';
import 'dart:isolate';

import 'package:flutter/services.dart' show rootBundle;

Map<String, dynamic> _map(Object? v) => v == null ? <String, dynamic>{} : (v is Map<String, dynamic> ? v : Map<String, dynamic>.from(v as Map));

List<Map<String, dynamic>> _list(Object? v) => v == null ? <Map<String, dynamic>>[] : [for (final e in v as List) _map(e)];

int _bySortThenId(Map<String, dynamic> a, Map<String, dynamic> b) {
  final c = _int(a['sort_order'] ?? 0).compareTo(_int(b['sort_order'] ?? 0));
  return c != 0 ? c : _int(a['id']).compareTo(_int(b['id']));
}

int _int(Object? v) => (v as num).toInt();

int schoolSemester(DateTime d) => d.month >= 7 ? 1 : 2;

class Content {
  Content(Map<String, dynamic> raw)
      : curriculum = raw['curriculum'] as String?,
        includesSample = raw['includes_sample'] == true,
        subjects = _list(raw['subjects']),
        chapters = _list(raw['chapters']),
        topics = _list(raw['topics']),
        lessons = _list(raw['lessons']),
        assessments = _list(raw['assessments']),
        templates = ((raw['assessment_templates'] as List?) ?? const []).map((e) => e.toString()).toList() {
    for (final s in subjects) {
      subjectById[_int(s['id'])] = s;
    }
    for (final c in chapters) {
      chapterById[_int(c['id'])] = c;
    }
    for (final t in topics) {
      topicById[_int(t['id'])] = t;
    }
    for (final l in lessons) {
      lessonById[_int(l['id'])] = l;
    }
    for (final a in assessments) {
      assessmentById[_int(a['id'])] = a;
    }
    for (final p in (raw['prerequisites'] as List?) ?? const []) {
      final pair = p as List;
      prereqs.putIfAbsent(_int(pair[0]), () => <int>[]).add(_int(pair[1]));
    }
    for (final s in subjects) {
      _subjectsByGrade.putIfAbsent(_int(s['grade']), () => []).add(s);
    }
    for (final c in chapters) {
      _chaptersBySubject.putIfAbsent(_int(c['subject_id']), () => []).add(c);
    }
    for (final t in topics) {
      _topicsByChapter.putIfAbsent(_int(t['chapter_id']), () => []).add(t);
    }
    for (final l in lessons) {
      final tid = _int(l['topic_id']);
      _lessonsByTopic.putIfAbsent(tid, () => []).add(l);
      _withContent.add(tid);
    }
    final grouped = <int, List<Object?>>{};
    for (final e in (raw['questions'] as List?) ?? const []) {
      final q = e as Map;
      final tid = _int(q['topic_id']);
      grouped.putIfAbsent(tid, () => []).add(q);
      questionTopic[_int(q['id'])] = tid;
      _withContent.add(tid);
      if (isPractice(q)) {
        _practiceCount[tid] = (_practiceCount[tid] ?? 0) + 1;
      }
    }
    for (final g in grouped.entries) {
      _packedQuestions[g.key] = jsonEncode(g.value);
    }
    for (final v in _subjectsByGrade.values) {
      v.sort(_bySortThenId);
    }
    for (final v in _chaptersBySubject.values) {
      v.sort((a, b) => _int(a['number']).compareTo(_int(b['number'])));
    }
    for (final v in _topicsByChapter.values) {
      v.sort(_bySortThenId);
    }
    for (final v in _lessonsByTopic.values) {
      v.sort((a, b) => _int(a['id']).compareTo(_int(b['id'])));
    }
  }

  static const assetPath = 'assets/content/bobo-content.json';

  static Future<Content> load() async {
    final data = await rootBundle.load(assetPath);
    final bytes = data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes);
    return Isolate.run(() => Content(_map(jsonDecode(utf8.decode(bytes)))));
  }

  final Map<int, List<Map<String, dynamic>>> _subjectsByGrade = {};
  final Map<int, List<Map<String, dynamic>>> _chaptersBySubject = {};
  final Map<int, List<Map<String, dynamic>>> _topicsByChapter = {};
  final Map<int, List<Map<String, dynamic>>> _lessonsByTopic = {};
  final Map<int, String> _packedQuestions = {};
  final Map<int, int> questionTopic = {};
  final Map<int, List<Map<String, dynamic>>> _questionCache = {};
  static const _questionCacheSize = 48;
  final Map<int, int> _practiceCount = {};
  final Set<int> _withContent = {};
  final Map<int, List<Map<String, dynamic>>> _gradeTopics = {};
  final Map<int, List<Map<String, dynamic>>> _topicsWithContent = {};

  List<Map<String, dynamic>> lessonsOfTopic(int topicId) => List.of(_lessonsByTopic[topicId] ?? const []);

  List<Map<String, dynamic>> _questionsOf(int topicId) {
    final hit = _questionCache.remove(topicId);
    if (hit != null) {
      _questionCache[topicId] = hit;
      return hit;
    }
    final packed = _packedQuestions[topicId];
    if (packed == null) {
      return const [];
    }
    final out = _list(jsonDecode(packed));
    _questionCache[topicId] = out;
    if (_questionCache.length > _questionCacheSize) {
      _questionCache.remove(_questionCache.keys.first);
    }
    return out;
  }

  List<Map<String, dynamic>> questionsOfTopic(int topicId) => List.of(_questionsOf(topicId));

  Map<String, dynamic>? question(int id) {
    final tid = questionTopic[id];
    if (tid == null) {
      return null;
    }
    for (final q in _questionsOf(tid)) {
      if (_int(q['id']) == id) {
        return q;
      }
    }
    return null;
  }

  List<Map<String, dynamic>> get questions => [for (final tid in _packedQuestions.keys) ..._questionsOf(tid)];

  late final QuestionLookup questionById = QuestionLookup(this);

  final String? curriculum;
  final bool includesSample;
  final List<Map<String, dynamic>> subjects;
  final List<Map<String, dynamic>> chapters;
  final List<Map<String, dynamic>> topics;
  final List<Map<String, dynamic>> lessons;
  final List<Map<String, dynamic>> assessments;
  final List<String> templates;
  final Map<int, Map<String, dynamic>> subjectById = {};
  final Map<int, Map<String, dynamic>> chapterById = {};
  final Map<int, Map<String, dynamic>> topicById = {};
  final Map<int, Map<String, dynamic>> lessonById = {};
  final Map<int, Map<String, dynamic>> assessmentById = {};
  final Map<int, List<int>> prereqs = {};

  Map<String, dynamic>? subjectOfTopic(int topicId) {
    final t = topicById[topicId];
    if (t == null) {
      return null;
    }
    final c = chapterById[_int(t['chapter_id'])];
    return c == null ? null : subjectById[_int(c['subject_id'])];
  }

  int? gradeOfTopic(int topicId) {
    final s = subjectOfTopic(topicId);
    return s == null ? null : _int(s['grade']);
  }

  String topicTitle(int topicId) => (topicById[topicId]?['title'] as String?) ?? '';

  List<Map<String, dynamic>> subjectsOfGrade(int grade) => List.of(_subjectsByGrade[grade] ?? const []);

  List<Map<String, dynamic>> chaptersOfSubject(int subjectId) => List.of(_chaptersBySubject[subjectId] ?? const []);

  int semesterOfTopic(int topicId) {
    final t = topicById[topicId];
    final c = t == null ? null : chapterById[_int(t['chapter_id'])];
    return c == null ? 1 : ((c['semester'] as num?) ?? 1).toInt();
  }

  List<Map<String, dynamic>> topicsOfChapter(int chapterId) => List.of(_topicsByChapter[chapterId] ?? const []);

  List<Map<String, dynamic>> gradeTopics(int grade) => List.of(_gradeTopics[grade] ??= [
        for (final s in _subjectsByGrade[grade] ?? const <Map<String, dynamic>>[])
          for (final c in _chaptersBySubject[_int(s['id'])] ?? const <Map<String, dynamic>>[]) ...?_topicsByChapter[_int(c['id'])],
      ]);

  List<Map<String, dynamic>> topicsWithContent(int grade) => List.of(_topicsWithContent[grade] ??= () {
        final all = gradeTopics(grade);
        final chaptersWithContent = all.where((t) => _withContent.contains(_int(t['id']))).map((t) => _int(t['chapter_id'])).toSet();
        return all.where((t) => chaptersWithContent.contains(_int(t['chapter_id']))).toList();
      }());

  Map<String, dynamic>? lessonForTopic(int topicId) => _lessonsByTopic[topicId]?.firstOrNull;

  bool isPractice(Map q) => (q['usage'] == 'practice' || q['usage'] == 'both') && q['type'] != 'essay';

  List<Map<String, dynamic>> practiceQuestions(Set<int> topicIds) {
    final out = [
      for (final tid in topicIds)
        for (final q in _questionsOf(tid))
          if (isPractice(q)) q,
    ];
    out.sort((a, b) {
      final ta = topicById[_int(a['topic_id'])];
      final tb = topicById[_int(b['topic_id'])];
      final c = _int(ta?['sort_order'] ?? 0).compareTo(_int(tb?['sort_order'] ?? 0));
      return c != 0 ? c : _int(a['id']).compareTo(_int(b['id']));
    });
    return out;
  }

  int practiceCount(int topicId) => _practiceCount[topicId] ?? 0;

  String? visualForTopic(int? topicId, String? topicTitle) {
    if (topicId != null) {
      for (final l in _lessonsByTopic[topicId] ?? const <Map<String, dynamic>>[]) {
        for (final b in _list(l['blocks'])) {
          final v = b['visual'];
          if (v is String && v.isNotEmpty) {
            return v;
          }
        }
      }
    }
    final t = (topicTitle ?? '').toLowerCase();
    if (t.contains('pecahan')) {
      return 'frac';
    }
    if (t.contains('pythagoras') || t.contains('segitiga') || t.contains('jarak')) {
      return 'tri';
    }
    if (t.contains('jumlah') || t.contains('kurang') || t.contains('cerita')) {
      return 'tens';
    }
    return null;
  }
}

class QuestionLookup {
  QuestionLookup(this._content);

  final Content _content;

  Map<String, dynamic>? operator [](int id) => _content.question(id);
}
