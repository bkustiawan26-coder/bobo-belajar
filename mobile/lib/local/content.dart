import 'dart:convert';

import 'package:flutter/services.dart' show rootBundle;

Map<String, dynamic> _map(Object? v) => v == null ? <String, dynamic>{} : Map<String, dynamic>.from(v as Map);

List<Map<String, dynamic>> _list(Object? v) => v == null ? <Map<String, dynamic>>[] : (v as List).map(_map).toList();

int _int(Object? v) => (v as num).toInt();

class Content {
  Content(Map<String, dynamic> raw)
      : curriculum = raw['curriculum'] as String?,
        includesSample = raw['includes_sample'] == true,
        subjects = _list(raw['subjects']),
        chapters = _list(raw['chapters']),
        topics = _list(raw['topics']),
        lessons = _list(raw['lessons']),
        questions = _list(raw['questions']),
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
    for (final q in questions) {
      questionById[_int(q['id'])] = q;
    }
    for (final a in assessments) {
      assessmentById[_int(a['id'])] = a;
    }
    for (final p in (raw['prerequisites'] as List?) ?? const []) {
      final pair = p as List;
      prereqs.putIfAbsent(_int(pair[0]), () => <int>[]).add(_int(pair[1]));
    }
  }

  static const assetPath = 'assets/content/bobo-content.json';

  static Future<Content> load() async => Content(_map(jsonDecode(await rootBundle.loadString(assetPath))));

  final String? curriculum;
  final bool includesSample;
  final List<Map<String, dynamic>> subjects;
  final List<Map<String, dynamic>> chapters;
  final List<Map<String, dynamic>> topics;
  final List<Map<String, dynamic>> lessons;
  final List<Map<String, dynamic>> questions;
  final List<Map<String, dynamic>> assessments;
  final List<String> templates;
  final Map<int, Map<String, dynamic>> subjectById = {};
  final Map<int, Map<String, dynamic>> chapterById = {};
  final Map<int, Map<String, dynamic>> topicById = {};
  final Map<int, Map<String, dynamic>> lessonById = {};
  final Map<int, Map<String, dynamic>> questionById = {};
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

  List<Map<String, dynamic>> subjectsOfGrade(int grade) {
    final out = subjects.where((s) => _int(s['grade']) == grade).toList();
    out.sort((a, b) {
      final c = _int(a['sort_order']).compareTo(_int(b['sort_order']));
      return c != 0 ? c : _int(a['id']).compareTo(_int(b['id']));
    });
    return out;
  }

  List<Map<String, dynamic>> chaptersOfSubject(int subjectId) {
    final out = chapters.where((c) => _int(c['subject_id']) == subjectId).toList();
    out.sort((a, b) => _int(a['number']).compareTo(_int(b['number'])));
    return out;
  }

  List<Map<String, dynamic>> topicsOfChapter(int chapterId) {
    final out = topics.where((t) => _int(t['chapter_id']) == chapterId).toList();
    out.sort((a, b) {
      final c = _int(a['sort_order']).compareTo(_int(b['sort_order']));
      return c != 0 ? c : _int(a['id']).compareTo(_int(b['id']));
    });
    return out;
  }

  List<Map<String, dynamic>> gradeTopics(int grade) {
    final out = <Map<String, dynamic>>[];
    for (final s in subjectsOfGrade(grade)) {
      for (final c in chaptersOfSubject(_int(s['id']))) {
        out.addAll(topicsOfChapter(_int(c['id'])));
      }
    }
    return out;
  }

  List<Map<String, dynamic>> topicsWithContent(int grade) {
    final all = gradeTopics(grade);
    final withContent = <int>{};
    for (final l in lessons) {
      withContent.add(_int(l['topic_id']));
    }
    for (final q in questions) {
      withContent.add(_int(q['topic_id']));
    }
    final chaptersWithContent = all.where((t) => withContent.contains(_int(t['id']))).map((t) => _int(t['chapter_id'])).toSet();
    return all.where((t) => chaptersWithContent.contains(_int(t['chapter_id']))).toList();
  }

  Map<String, dynamic>? lessonForTopic(int topicId) {
    Map<String, dynamic>? best;
    for (final l in lessons) {
      if (_int(l['topic_id']) == topicId && (best == null || _int(l['id']) < _int(best['id']))) {
        best = l;
      }
    }
    return best;
  }

  bool isPractice(Map<String, dynamic> q) => (q['usage'] == 'practice' || q['usage'] == 'both') && q['type'] != 'essay';

  List<Map<String, dynamic>> practiceQuestions(Set<int> topicIds) {
    final out = questions.where((q) => isPractice(q) && topicIds.contains(_int(q['topic_id']))).toList();
    out.sort((a, b) {
      final ta = topicById[_int(a['topic_id'])];
      final tb = topicById[_int(b['topic_id'])];
      final c = _int(ta?['sort_order'] ?? 0).compareTo(_int(tb?['sort_order'] ?? 0));
      return c != 0 ? c : _int(a['id']).compareTo(_int(b['id']));
    });
    return out;
  }

  int practiceCount(int topicId) => questions.where((q) => isPractice(q) && _int(q['topic_id']) == topicId).length;

  String? visualForTopic(int? topicId, String? topicTitle) {
    if (topicId != null) {
      for (final l in lessons.where((l) => _int(l['topic_id']) == topicId)) {
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
