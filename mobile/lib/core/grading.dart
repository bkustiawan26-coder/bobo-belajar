String normalizeAnswer(Object? v) => (v ?? '').toString().trim().toLowerCase().replaceAll(',', '.').replaceAll(RegExp(r'\s+'), '');

bool gradeLocally(Map<String, dynamic> question, Map<String, dynamic>? response) {
  if (response == null) {
    return false;
  }
  final type = question['type'] as String;
  final answer = Map<String, dynamic>.from((question['answer'] as Map?) ?? const {});
  switch (type) {
    case 'mc':
    case 'tf':
      return response['index'] != null && response['index'] == answer['index'];
    case 'multi':
      final got = ((response['indices'] as List?) ?? const []).map((e) => e as int).toSet().toList()..sort();
      final want = ((answer['indices'] as List?) ?? const []).map((e) => e as int).toSet().toList()..sort();
      return got.join(',') == want.join(',');
    case 'fill':
    case 'short':
      final accepted = ((answer['accepted'] as List?) ?? const []).map(normalizeAnswer).toSet();
      return accepted.contains(normalizeAnswer(response['text']));
    default:
      return false;
  }
}
