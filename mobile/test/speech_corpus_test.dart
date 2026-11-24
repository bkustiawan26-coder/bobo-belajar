import 'dart:convert';
import 'dart:io';

import 'package:bobo_belajar/core/persona.dart';
import 'package:flutter_test/flutter_test.dart';

Iterable<String> _strings(Object? v) sync* {
  if (v is String) {
    yield v;
  } else if (v is List) {
    for (final x in v) {
      yield* _strings(x);
    }
  } else if (v is Map) {
    for (final e in v.entries) {
      if (e.key == 'icon' || e.key == 'type' || e.key == 'mode' || e.key == 'shape' || e.key == 'abc') {
        continue;
      }
      yield* _strings(e.value);
    }
  }
}

List<String> spokenCorpus() {
  final b = jsonDecode(File('assets/content/bobo-content.json').readAsStringSync()) as Map<String, dynamic>;
  final out = <String>{};
  for (final l in b['lessons'] as List) {
    out.add((l as Map)['title'].toString());
    for (final blk in l['blocks'] as List) {
      final m = blk as Map;
      for (final x in _strings([m['text'], m['points'], m['figure']])) {
        out.addAll(segmentsOf(x));
      }
    }
  }
  for (final q in b['questions'] as List) {
    final m = q as Map;
    for (final x in _strings([m['body'], m['options'], m['explanation'], m['mistake_hint'], m['scaffold'], (m['answer'] as Map)['model']])) {
      out.addAll(segmentsOf(x));
    }
  }
  return out.where((x) => x.trim().isNotEmpty).toList();
}

final forbidden = RegExp('[\\\$:;/|<>=+×÷√π²³°…≤≥≠→–—"*_#&^\\[\\]{}±⁰¹⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉\\u0600-\\u06FF]');

void main() {
  test('semua teks materi dan soal diucapkan tanpa simbol yang terbaca aneh', () {
    final bad = <String>[];
    final corpus = spokenCorpus();
    expect(corpus.length, greaterThan(20000));
    for (final raw in corpus) {
      for (final english in [false, true]) {
        final s = toSpoken(raw, english: english);
        if (forbidden.hasMatch(s) || s.contains(r'$')) {
          bad.add('$raw  =>  $s');
        }
      }
    }
    expect(bad.take(40).toList(), isEmpty, reason: '${bad.length} kalimat bermasalah');
  });
}
