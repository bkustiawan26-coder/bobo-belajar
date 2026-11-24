import 'dart:convert';
import 'dart:math';

import 'package:uuid/uuid.dart';

import '../core/api.dart';
import '../core/grading.dart';
import 'content.dart';
import 'pin.dart';
import 'store.dart';
import 'tutor.dart';

typedef Json = Map<String, dynamic>;

const int minEvidence = 3;
const int masteryWindow = 5;
const double goodRatio = 0.8;
const List<int> reviewIntervals = [1, 3, 7];
const Set<String> settingKeys = {'short_sessions', 'larger_text', 'fewer_options', 'read_aloud', 'hide_mulok'};
const Set<String> mulokSubjects = {'Pendidikan Agama Islam', 'Bahasa Sunda'};
const int maxChildren = 6;
const int defaultTutorLimit = 20;
const int parentAssistantLimit = 30;
const int assessmentGraceSeconds = 30;
const String policyVersion = '2026-11-lokal';
const int backupFormat = 1;

const Map<String, String> stateLabels = {
  'not_started': 'Belum mulai',
  'insufficient': 'Bukti belum cukup',
  'developing': 'Berkembang',
  'demonstrated': 'Menunjukkan pemahaman',
};
const Map<String, int> kindOrder = {'practice': 0, 'foundation': 1, 'evidence': 2, 'next': 3, 'maintain': 4};
const Map<String, String> kindLabel = {'practice': 'Latih lagi', 'foundation': 'Perkuat pondasi', 'evidence': 'Kumpulkan bukti', 'next': 'Topik berikutnya', 'maintain': 'Pertahankan'};
const List<String> dataCollections = ['children', 'attempts', 'progress', 'reviews', 'sessions', 'activity', 'recs', 'tutor'];
const List<String> _bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'];

Json _j(Object? v) => v == null ? <String, dynamic>{} : Map<String, dynamic>.from(v as Map);

List<Json> _jl(Object? v) => v == null ? <Json>[] : (v as List).map(_j).toList();

int _i(Object? v) => (v as num).toInt();

int band(int grade) => grade <= 2 ? 1 : grade <= 4 ? 2 : grade <= 6 ? 3 : 4;

String level(int grade) => grade <= 6 ? 'SD' : 'SMP';

String phase(int grade) => const {1: 'Fase A', 2: 'Fase B', 3: 'Fase C', 4: 'Fase D'}[band(grade)]!;

class LocalEngine {
  LocalEngine(this.store, this.content, {DateTime Function()? clock, Random? random})
      : clock = clock ?? DateTime.now,
        rnd = random ?? Random(),
        index = KnowledgeIndex(content);

  final LocalStore store;
  final Content content;
  final DateTime Function() clock;
  final Random rnd;
  final KnowledgeIndex index;
  final Map<String, Map<String, Json>> _cache = {};
  final Uuid _uuid = const Uuid();
  int? _seq;

  DateTime get now => clock().toUtc();

  String _iso(DateTime d) => d.toUtc().toIso8601String();

  DateTime _parse(Object? s) => DateTime.parse(s as String).toUtc();

  DateTime _day(DateTime d) {
    final l = d.toLocal();
    return DateTime(l.year, l.month, l.day);
  }

  Future<Map<String, Json>> _col(String name) async => _cache[name] ??= await store.load(name);

  Future<void> _put(String col, String id, Json doc) async {
    (await _col(col))[id] = doc;
    await store.put(col, id, doc);
  }

  Future<void> _del(String col, String id) async {
    (await _col(col)).remove(id);
    await store.remove(col, id);
  }

  Future<int> _nextSeq() async {
    if (_seq == null) {
      var m = 0;
      for (final a in (await _col('attempts')).values) {
        m = max(m, _i(a['seq'] ?? 0));
      }
      _seq = m;
    }
    _seq = _seq! + 1;
    return _seq!;
  }

  String relativeLabel(DateTime when) {
    final d = _day(now).difference(_day(when)).inDays;
    if (d <= 0) {
      return 'Hari ini';
    }
    if (d == 1) {
      return 'Kemarin';
    }
    if (d < 7) {
      return '$d hari lalu';
    }
    final l = when.toLocal();
    return '${l.day} ${_bulan[l.month - 1]}';
  }

  Future<Json?> _meta() async => (await _col('meta'))['app'];

  Future<bool> hasPin() async => (await _meta())?['pin_hash'] != null;

  Future<String> setupPin(String pin) async {
    _checkPin(pin);
    final code = newRecoveryCode();
    final m = _j(await _meta());
    m['pin_hash'] = hashSecret(pin);
    m['recovery_hash'] = hashSecret(normalizeRecoveryCode(code));
    m['pin_failed'] = 0;
    m['pin_locked_until'] = null;
    m['consent_version'] ??= policyVersion;
    m['consent_at'] ??= _iso(now);
    m['created_at'] ??= _iso(now);
    await _put('meta', 'app', m);
    return code;
  }

  void _checkPin(String pin) {
    if (!RegExp(r'^\d{4,6}$').hasMatch(pin)) {
      throw ApiException(422, 'PIN harus 4–6 angka');
    }
  }

  Future<void> verifyPin(String pin) async {
    final m = _j(await _meta());
    final locked = m['pin_locked_until'];
    if (locked != null && _parse(locked).isAfter(now)) {
      final mins = _parse(locked).difference(now).inMinutes + 1;
      throw ApiException(423, 'PIN terkunci. Coba lagi dalam $mins menit.');
    }
    if (verifySecret(pin, m['pin_hash'] as String?)) {
      m['pin_failed'] = 0;
      m['pin_locked_until'] = null;
      await _put('meta', 'app', m);
      return;
    }
    final fails = _i(m['pin_failed'] ?? 0) + 1;
    m['pin_failed'] = fails;
    if (fails >= 5) {
      m['pin_failed'] = 0;
      m['pin_locked_until'] = _iso(now.add(const Duration(minutes: 15)));
      await _put('meta', 'app', m);
      throw ApiException(423, 'PIN salah 5 kali. Mode orang tua terkunci 15 menit.');
    }
    await _put('meta', 'app', m);
    throw ApiException(401, 'PIN salah. Sisa ${5 - fails} percobaan.');
  }

  Future<String> resetPinWithRecovery(String code, String newPin) async {
    _checkPin(newPin);
    final m = _j(await _meta());
    if (!verifySecret(normalizeRecoveryCode(code), m['recovery_hash'] as String?)) {
      throw ApiException(401, 'Kode pemulihan salah.');
    }
    return setupPin(newPin);
  }

  Future<void> wipeAll() async {
    await store.clear();
    _cache.clear();
    _seq = null;
  }

  Map<String, bool> cleanSettings(Object? raw) {
    final r = _j(raw);
    return {for (final k in settingKeys) k: r[k] == true};
  }

  Future<List<Json>> _children() async {
    final l = (await _col('children')).values.toList();
    l.sort((a, b) => (a['created_at'] as String).compareTo(b['created_at'] as String));
    return l;
  }

  Future<Json> _child(String id) async {
    final c = (await _col('children'))[id];
    if (c == null) {
      throw ApiException(404, 'Profil anak tidak ditemukan');
    }
    return c;
  }

  int _grade(Json c) => _i(c['grade']);

  Future<List<Json>> _attempts(String childId) async {
    final l = (await _col('attempts')).values.where((a) => a['child_id'] == childId).toList();
    l.sort((a, b) => _i(a['seq']).compareTo(_i(b['seq'])));
    return l;
  }

  Future<void> _log(String childId, String kind, String summary, {int? topicId, DateTime? when}) async {
    final id = _uuid.v4();
    await _put('activity', id, {'id': id, 'child_id': childId, 'kind': kind, 'summary': summary.length > 200 ? summary.substring(0, 200) : summary, 'topic_id': topicId, 'at': _iso(when ?? now)});
  }

  Future<int> _tutorUsedToday(String childId, String purpose) async {
    final today = _day(now);
    return (await _col('tutor')).values.where((t) => t['child_id'] == childId && t['purpose'] == purpose && _day(_parse(t['at'])) == today).length;
  }

  Future<Json> childInfo(Json c) async {
    final id = c['id'] as String;
    final refusals = (await _col('tutor')).values.where((t) => t['child_id'] == id && t['purpose'] == 'tutor' && t['action'] == 'refuse').length;
    final g = _grade(c);
    return {
      'id': id, 'nickname': c['nickname'], 'grade': g, 'level': level(g), 'phase': phase(g), 'band': band(g),
      'tutor_today': await _tutorUsedToday(id, 'tutor'), 'tutor_limit': _i(c['tutor_limit'] ?? defaultTutorLimit), 'safety_refusals': refusals,
      'consent_active': true, 'settings': cleanSettings(c['settings']),
    };
  }

  List<Json> masteryFrom(int grade, List<Json> attempts, {List<Json>? topics}) {
    final ts = topics ?? content.topicsWithContent(grade);
    final byTopic = <int, List<bool>>{};
    for (final a in attempts) {
      byTopic.putIfAbsent(_i(a['topic_id']), () => []).add(a['correct'] == true);
    }
    return [
      for (final t in ts)
        () {
          final tid = _i(t['id']);
          final seq = byTopic[tid] ?? const <bool>[];
          final recent = seq.length > masteryWindow ? seq.sublist(seq.length - masteryWindow) : seq;
          final rc = recent.where((x) => x).length;
          String st;
          if (seq.isEmpty) {
            st = 'not_started';
          } else if (seq.length < minEvidence) {
            st = 'insufficient';
          } else if (rc / recent.length >= goodRatio) {
            st = 'demonstrated';
          } else {
            st = 'developing';
          }
          final evidence = seq.isEmpty ? 'Belum ada jawaban' : '$rc dari ${recent.length} jawaban terakhir benar${st == 'insufficient' ? ' · butuh minimal $minEvidence' : ''}';
          return <String, dynamic>{
            'topic_id': tid, 'topic': t['title'], 'state': st, 'label': stateLabels[st], 'evidence_count': seq.length, 'recent_correct': rc,
            'recent_total': recent.length, 'recent': recent, 'evidence': evidence, 'home_activity': t['home_activity'], 'common_mistake': t['common_mistake'],
          };
        }(),
    ];
  }

  Future<List<Json>> mastery(Json c) async => masteryFrom(_grade(c), await _attempts(c['id'] as String));

  Set<int> allowedTopicIds(int grade) {
    final base = content.gradeTopics(grade).map((t) => _i(t['id'])).toSet();
    final allowed = {...base};
    var frontier = base.toList();
    for (var d = 0; d < 3; d++) {
      final next = <int>[];
      for (final t in frontier) {
        for (final p in content.prereqs[t] ?? const <int>[]) {
          if (allowed.add(p)) {
            next.add(p);
          }
        }
      }
      frontier = next;
    }
    return allowed;
  }

  bool _struggling(Json m) => m['state'] == 'developing' && _i(m['evidence_count']) >= 6 && _i(m['recent_total']) > 0 && _i(m['recent_correct']) / _i(m['recent_total']) < 0.5;

  Json? _topicInfo(int tid) {
    final t = content.topicById[tid];
    final s = content.subjectOfTopic(tid);
    if (t == null || s == null) {
      return null;
    }
    return {'topic_id': tid, 'topic': t['title'], 'grade': _i(s['grade']), 'subject': s['name']};
  }

  Future<List<Json>> foundationSuggestions(Json c, {List<Json>? masteryRows, List<Json>? attempts}) async {
    final atts = attempts ?? await _attempts(c['id'] as String);
    final m = masteryRows ?? masteryFrom(_grade(c), atts);
    final out = <Json>[];
    final seen = <int>{};
    for (final x in m.where(_struggling)) {
      for (final p in content.prereqs[_i(x['topic_id'])] ?? const <int>[]) {
        final info = _topicInfo(p);
        if (seen.contains(p) || info == null) {
          continue;
        }
        final seq = atts.where((a) => _i(a['topic_id']) == p).map((a) => a['correct'] == true).toList();
        final recent = seq.length > 5 ? seq.sublist(seq.length - 5) : seq;
        if (seq.length >= 3 && recent.where((v) => v).length / recent.length >= 0.8) {
          continue;
        }
        seen.add(p);
        out.add({
          ...info, 'for_topic': x['topic'], 'for_topic_id': x['topic_id'], 'lesson_id': content.lessonForTopic(p)?['id'], 'question_count': content.practiceCount(p),
          'reason': '${x['recent_correct']} dari ${x['recent_total']} jawaban terakhir di ${x['topic']} benar. ${info['topic']} adalah dasarnya.',
        });
      }
    }
    return out;
  }

  Future<List<Json>> recommendations(Json c) async {
    final childId = c['id'] as String;
    final atts = await _attempts(childId);
    final m = masteryFrom(_grade(c), atts);
    final young = band(_grade(c)) <= 2;
    final dur = young ? '10 menit' : '10–15 menit';
    final nick = c['nickname'];
    final wanted = <String, Json>{};
    for (final x in m) {
      final act = (x['home_activity'] as String?) ?? 'Buka materi topik ini bersama anak dan minta ia menjelaskan kembali dengan kata-katanya sendiri.';
      final tid = x['topic_id'];
      if (x['state'] == 'developing') {
        wanted['dev:$tid'] = {'kind': 'practice', 'topic_id': tid, 'title': 'Latih lagi ${x['topic']} di rumah', 'evidence': '${x['recent_correct']} dari ${x['recent_total']} jawaban terakhir benar di ${x['topic']}.', 'activity': act, 'duration_label': dur};
      } else if (x['state'] == 'insufficient') {
        final need = minEvidence - _i(x['evidence_count']);
        wanted['ins:$tid'] = {'kind': 'evidence', 'topic_id': tid, 'title': 'Ajak $nick mengerjakan $need soal ${x['topic']} lagi', 'evidence': 'Baru ${x['evidence_count']} jawaban, belum cukup untuk menilai.', 'activity': 'Buka menu Latihan bersama, pilih topik ini, lalu minta anak menjelaskan caranya dengan kata-katanya sendiri.', 'duration_label': '5–10 menit'};
      } else if (x['state'] == 'demonstrated') {
        wanted['good:$tid'] = {'kind': 'maintain', 'topic_id': tid, 'title': 'Apresiasi usaha $nick di ${x['topic']}', 'evidence': '${x['recent_correct']} dari ${x['recent_total']} jawaban terakhir benar.', 'activity': 'Puji prosesnya ("kamu teliti menghitungnya"), bukan kecerdasannya. Sesekali ajak mengulang satu soal agar tetap ingat.', 'duration_label': '2 menit'};
      }
    }
    for (final f in await foundationSuggestions(c, masteryRows: m, attempts: atts)) {
      final note = f['grade'] != _grade(c) ? ' dari Kelas ${f['grade']}' : '';
      wanted['found:${f['topic_id']}'] = {'kind': 'foundation', 'topic_id': f['topic_id'], 'title': 'Perkuat pondasi: ${f['topic']}$note', 'evidence': f['reason'], 'activity': 'Sebelum lanjut ${f['for_topic']}, ajak anak membuka jalur Pondasi di menu Home: baca materi ${f['topic']} lalu kerjakan 3 soal. Dasar yang kuat membuat topik berikutnya lebih mudah.', 'duration_label': dur};
    }
    final next = m.where((x) => x['state'] == 'not_started').firstOrNull;
    if (next != null) {
      wanted['next:${next['topic_id']}'] = {'kind': 'next', 'topic_id': next['topic_id'], 'title': 'Mulai topik ${next['topic']}', 'evidence': 'Belum ada aktivitas di topik ini.', 'activity': (next['home_activity'] as String?) ?? 'Mulai dari materi topik ini di menu Belajar.', 'duration_label': dur};
    }
    final stored = await _col('recs');
    final out = <Json>[];
    var order = 0;
    for (final e in wanted.entries) {
      final x = m.where((y) => y['topic_id'] == e.value['topic_id']).firstOrNull;
      final sig = x == null ? '' : '${x['recent_correct']}/${x['recent_total']}/${x['evidence_count']}/${x['state']}';
      final s = stored['$childId|${e.key}'];
      final done = s != null && s['done_at'] != null && s['sig'] == sig;
      out.add({...e.value, 'id': e.key, 'sig': sig, 'done': done, 'order': order++});
    }
    out.sort((a, b) {
      final c = (kindOrder[a['kind']] ?? 9).compareTo(kindOrder[b['kind']] ?? 9);
      return c != 0 ? c : _i(a['order']).compareTo(_i(b['order']));
    });
    return out;
  }

  Json _recOut(Json r) => {'id': r['id'], 'kind': r['kind'], 'kind_label': kindLabel[r['kind']] ?? r['kind'], 'title': r['title'], 'evidence': r['evidence'], 'activity': r['activity'], 'duration': r['duration_label'], 'done': r['done']};

  Future<void> _scheduleReview(String childId, Json q, bool correct, String mode) async {
    final id = '$childId|${q['id']}';
    final item = (await _col('reviews'))[id];
    if (mode == 'review') {
      if (item == null) {
        return;
      }
      if (correct) {
        final step = _i(item['step']) + 1;
        if (step >= reviewIntervals.length) {
          await _del('reviews', id);
        } else {
          await _put('reviews', id, {...item, 'step': step, 'last_correct': true, 'due_at': _iso(now.add(Duration(days: reviewIntervals[step])))});
        }
      } else {
        await _put('reviews', id, {...item, 'step': 0, 'last_correct': false, 'due_at': _iso(now.add(Duration(days: reviewIntervals[0])))});
      }
      return;
    }
    if (correct) {
      return;
    }
    await _put('reviews', id, {'child_id': childId, 'question_id': q['id'], 'topic_id': q['topic_id'], 'step': 0, 'last_correct': false, 'due_at': _iso(now.add(Duration(days: reviewIntervals[0])))});
  }

  Future<List<Json>> _dueReviews(String childId) async {
    final l = (await _col('reviews')).values.where((r) => r['child_id'] == childId && !_parse(r['due_at']).isAfter(now)).toList();
    l.sort((a, b) => (a['due_at'] as String).compareTo(b['due_at'] as String));
    return l;
  }

  List<int>? _keepOptions(Json q, Json c) {
    final opts = _jl(q['options']);
    if (!cleanSettings(c['settings'])['fewer_options']! || q['type'] != 'mc' || opts.length < 4) {
      return null;
    }
    final correct = _j(q['answer'])['index'];
    final wrong = opts.map((o) => _i(o['index'])).where((i) => i != correct).toList();
    if (wrong.isEmpty) {
      return null;
    }
    var h = 0x811c9dc5;
    for (final b in utf8.encode('${c['id']}:${q['id']}')) {
      h = ((h ^ b) * 0x01000193) & 0xffffffff;
    }
    final drop = wrong[h % wrong.length];
    return opts.map((o) => _i(o['index'])).where((i) => i != drop).toList();
  }

  Json questionPayload(Json q, {List<int>? order, bool withKey = false, Json? child}) {
    final ord = order ?? (child == null ? null : _keepOptions(q, child));
    final opts = {for (final o in _jl(q['options'])) _i(o['index']): o};
    final seq = ord ?? (opts.keys.toList()..sort());
    final tid = _i(q['topic_id']);
    final d = <String, dynamic>{
      'id': q['id'], 'type': q['type'], 'body': q['body'], 'difficulty': q['difficulty'], 'topic_id': tid, 'topic': content.topicTitle(tid),
      'options': [for (final i in seq) if (opts.containsKey(i)) {'index': i, 'label': opts[i]!['label'], 'side': opts[i]!['side']}],
    };
    if (withKey) {
      d['answer'] = q['answer'];
      d['answer_text'] = answerText(q);
      d['explanation'] = q['explanation'] ?? '';
      d['mistake_hint'] = q['mistake_hint'];
      d['scaffold'] = q['scaffold'];
    }
    return d;
  }

  String answerText(Json q) {
    final a = _j(q['answer']);
    final labels = {for (final o in _jl(q['options'])) _i(o['index']): o['label'] as String};
    switch (q['type']) {
      case 'mc':
      case 'tf':
        return labels[a['index']] ?? '';
      case 'multi':
        return ((a['indices'] as List?) ?? const []).map((i) => labels[i] ?? '').join(', ');
      case 'fill':
      case 'short':
        final acc = (a['accepted'] as List?) ?? const [];
        return acc.isEmpty ? '' : acc.first.toString();
      case 'matching':
        return _j(a['pairs']).entries.map((e) => '${labels[int.tryParse(e.key)] ?? e.key} → ${labels[int.tryParse(e.value.toString())] ?? e.value}').join('; ');
      case 'essay':
        return (a['model'] ?? '').toString();
      default:
        return '';
    }
  }

  String responseText(Json q, Json? response) {
    if (response == null || response.isEmpty) {
      return 'Tidak dijawab';
    }
    final labels = {for (final o in _jl(q['options'])) _i(o['index']): o['label'] as String};
    switch (q['type']) {
      case 'mc':
      case 'tf':
        return labels[response['index']] ?? 'Tidak dijawab';
      case 'multi':
        final s = ((response['indices'] as List?) ?? const []).map((i) => labels[(i as num).toInt()] ?? '').join(', ');
        return s.isEmpty ? 'Tidak dijawab' : s;
      case 'fill':
      case 'short':
      case 'essay':
        final t = response['text']?.toString() ?? '';
        return t.isEmpty ? 'Tidak dijawab' : t;
      case 'matching':
        return _j(response['pairs']).entries.map((e) => '${labels[int.tryParse(e.key)] ?? e.key} → ${labels[int.tryParse(e.value.toString())] ?? e.value}').join('; ');
      default:
        return '';
    }
  }

  Json? _lessonForChild(Json c, int lessonId) {
    final l = content.lessonById[lessonId];
    if (l == null || !allowedTopicIds(_grade(c)).contains(_i(l['topic_id']))) {
      return null;
    }
    return l;
  }

  Future<Json?> _progress(String childId, int lessonId) async => (await _col('progress'))['$childId|$lessonId'];

  Json _lessonPayload(Json l, Json? p) => {
        'id': l['id'], 'topic_id': l['topic_id'], 'title': l['title'], 'minutes': l['minutes'], 'version': l['version'], 'reviewed': l['sample'] != true, 'sample': l['sample'] == true,
        'blocks': [
          for (var i = 0; i < _jl(l['blocks']).length; i++) {..._jl(l['blocks'])[i], 'position': i},
        ],
        'step': p?['step'] ?? 0, 'completed': p?['completed_at'] != null, 'downloaded': true,
      };

  Future<Json> growth(Json c) async {
    final atts = await _attempts(c['id'] as String);
    final byTopic = <int, List<bool>>{};
    final days = <DateTime>{};
    final weekly = <int, int>{};
    var reviewsOk = 0;
    var retrySuccess = 0;
    final lastWrong = <int, bool>{};
    for (final a in atts) {
      final tid = _i(a['topic_id']);
      final ok = a['correct'] == true;
      final at = _parse(a['at']);
      byTopic.putIfAbsent(tid, () => []).add(ok);
      days.add(_day(at));
      final wk = now.difference(at).inDays ~/ 7;
      if (wk < 4) {
        weekly[wk] = (weekly[wk] ?? 0) + 1;
      }
      if (a['source'] == 'review' && ok) {
        reviewsOk++;
      }
      if (ok && lastWrong[tid] == true) {
        retrySuccess++;
      }
      lastWrong[tid] = !ok;
    }
    final topics = <Json>[];
    byTopic.forEach((tid, seq) {
      final info = _topicInfo(tid);
      if (seq.length < 6 || info == null) {
        return;
      }
      final first = seq.sublist(0, 5);
      final last = seq.sublist(seq.length - 5);
      topics.add({'topic': info['topic'], 'before_pct': (first.where((v) => v).length * 100 / first.length).round(), 'now_pct': (last.where((v) => v).length * 100 / last.length).round(), 'answers': seq.length});
    });
    var streak = 0;
    var d = _day(now);
    while (days.contains(d)) {
      streak++;
      d = DateTime(d.year, d.month, d.day - 1);
    }
    final total = atts.length;
    return {
      'weekly_answers': [for (final i in const [3, 2, 1, 0]) weekly[i] ?? 0],
      'streak_days': streak,
      'topics': topics,
      'badges': [
        {'key': 'first', 'title': 'Langkah pertama', 'desc': 'Menjawab soal pertama', 'earned': total >= 1},
        {'key': 'tries', 'title': 'Rajin mencoba', 'desc': 'Menjawab 20 soal', 'earned': total >= 20},
        {'key': 'persist', 'title': 'Pantang menyerah', 'desc': 'Benar setelah sebelumnya salah di topik yang sama, 3 kali', 'earned': retrySuccess >= 3},
        {'key': 'review', 'title': 'Ingat terus', 'desc': 'Berhasil di 3 soal Ulang sebentar', 'earned': reviewsOk >= 3},
        {'key': 'streak', 'title': 'Rutin 3 hari', 'desc': 'Belajar 3 hari berturut-turut', 'earned': streak >= 3},
      ],
      'total_answers': total,
    };
  }

  List<Json> weeklyPlan(Json c, Json m) {
    final pre = (content.prereqs[_i(m['topic_id'])] ?? const <int>[]).map(_topicInfo).whereType<Json>().firstOrNull;
    final preName = pre?['topic'];
    final act = (m['home_activity'] as String?) ?? 'Ajak anak menjelaskan ${m['topic']} dengan kata-katanya sendiri.';
    final short = band(_grade(c)) <= 2 ? '10 menit' : '15 menit';
    return [
      {'day': 'Hari 1', 'task': 'Baca ulang materi ${m['topic']} bersama, berhenti di setiap contoh. ($short)'},
      {'day': 'Hari 2', 'task': act},
      {'day': 'Hari 3', 'task': 'Latihan 3 soal ${m['topic']}. Saat salah, buka Langkah kecil bersama.'},
      {'day': 'Hari 4', 'task': 'Istirahat dari topik ini. Kerjakan Ulang sebentar saja jika ada.'},
      {'day': 'Hari 5', 'task': preName != null ? 'Perkuat dasar: latihan topik $preName.' : 'Pakai Alat peraga atau minta Tutor menjelaskan ${m['topic']} dengan cara lain.'},
      {'day': 'Hari 6', 'task': 'Latihan 3 soal ${m['topic']} lagi, biarkan anak mengerjakan sendiri dulu.'},
      {'day': 'Hari 7', 'task': 'Lihat Kemajuanku bersama dan puji usahanya, bukan nilainya.'},
    ];
  }

  Future<List<Json>> signals(Json c) async {
    final atts = await _attempts(c['id'] as String);
    final out = <Json>[];
    for (final x in masteryFrom(_grade(c), atts)) {
      if (x['state'] != 'developing' || _i(x['evidence_count']) < 8) {
        continue;
      }
      final rows = atts.where((a) => _i(a['topic_id']) == x['topic_id']).toList();
      final seq = rows.map((a) => a['correct'] == true).toList();
      final days = rows.sublist(max(0, rows.length - 10)).map((a) => _day(_parse(a['at']))).toSet();
      final last = seq.sublist(seq.length - 5);
      final prev = seq.sublist(max(0, seq.length - 10), seq.length - 5);
      final lastOk = last.where((v) => v).length;
      final prevOk = prev.where((v) => v).length;
      if (days.length < 3 || prev.isEmpty || lastOk / last.length > prevOk / prev.length) {
        continue;
      }
      out.add({
        'topic_id': x['topic_id'], 'topic': x['topic'], 'days': days.length,
        'message': 'Dalam ${days.length} hari belajar terakhir, hasil ${c['nickname']} di ${x['topic']} belum naik ($prevOk dari ${prev.length} lalu $lastOk dari ${last.length} benar).',
        'plan': weeklyPlan(c, x),
      });
    }
    return out;
  }

  Future<List<Json>> _results(String childId) async {
    final l = (await _col('sessions')).values.where((s) => s['child_id'] == childId && s['result'] != null).toList();
    l.sort((a, b) => (b['submitted_at'] as String).compareTo(a['submitted_at'] as String));
    return l;
  }

  Future<String> teacherSummary(Json c) async {
    final atts = await _attempts(c['id'] as String);
    final since = now.subtract(const Duration(days: 30));
    final recent = atts.where((a) => _parse(a['at']).isAfter(since)).toList();
    final ok = recent.where((a) => a['correct'] == true).length;
    final l = now.toLocal();
    final date = '${l.day.toString().padLeft(2, '0')}-${l.month.toString().padLeft(2, '0')}-${l.year}';
    final lines = <String>[
      'Ringkasan belajar ${c['nickname']} (Kelas ${_grade(c)}) dari aplikasi BOBO BELAJAR',
      'Periode: 30 hari terakhir, dibuat $date',
      '',
      recent.isNotEmpty ? 'Soal dikerjakan: ${recent.length} ($ok benar)' : 'Soal dikerjakan: belum ada dalam 30 hari terakhir',
      '',
      'Status per topik (berdasarkan 5 jawaban terakhir, minimal 3 jawaban):',
      for (final x in masteryFrom(_grade(c), atts)) '- ${x['topic']}: ${x['label']} (${x['evidence']})',
    ];
    final exams = (await _results(c['id'] as String)).take(3).toList();
    if (exams.isNotEmpty) {
      lines.addAll(['', 'Asesmen terakhir:']);
      for (final s in exams) {
        final r = _j(s['result']);
        lines.add('- ${content.assessmentById[_i(s['assessment_id'])]?['title'] ?? 'Asesmen'}: nilai ${(r['score'] as num).round()}');
      }
    }
    final sig = await signals(c);
    if (sig.isNotEmpty) {
      lines.addAll(['', 'Perlu perhatian:', for (final s in sig) '- ${s['message']}']);
    }
    lines.addAll(['', 'Catatan: ringkasan ini dibuat otomatis dari aktivitas di aplikasi, bukan penilaian resmi sekolah dan bukan diagnosis.']);
    return lines.join('\n');
  }

  static final RegExp _idLike = RegExp(r'^([0-9]+|[0-9a-f]{8}-[0-9a-f-]{27,}|[a-z]+:[0-9]+)$');

  String _pattern(String segment) => _idLike.hasMatch(segment) ? '*' : segment;

  List<String> _seg(String path) => path.split('?').first.split('/').where((s) => s.isNotEmpty).toList();

  Future<dynamic> student(String childId, String method, String path, {Object? body, Map<String, String>? query}) async {
    final c = await _child(childId);
    final s = _seg(path);
    final b = _j(body);
    final q = query ?? const <String, String>{};
    if (s.length < 2 || s[0] != 'student') {
      throw ApiException(404, 'Tidak ditemukan');
    }
    final key = '$method ${s.sublist(1).map(_pattern).join('/')}';
    switch (key) {
      case 'GET me':
        final g = _grade(c);
        return {'id': childId, 'nickname': c['nickname'], 'grade': g, 'level': level(g), 'phase': phase(g), 'band': band(g), 'settings': cleanSettings(c['settings'])};
      case 'GET catalog':
        return _catalog(c);
      case 'GET lessons/*':
        final l = _lessonForChild(c, int.parse(s[2]));
        if (l == null) {
          throw ApiException(404, 'Materi tidak ditemukan');
        }
        return _lessonPayload(l, await _progress(childId, _i(l['id'])));
      case 'POST lessons/*/progress':
        final l = _lessonForChild(c, int.parse(s[2]));
        if (l == null) {
          throw ApiException(404, 'Materi tidak ditemukan');
        }
        return _applyProgress(c, l, _i(b['step'] ?? 0), b['completed'] == true);
      case 'GET practice':
        final tid = int.tryParse(q['topic_id'] ?? '');
        final allowed = tid != null ? allowedTopicIds(_grade(c)) : content.gradeTopics(_grade(c)).map((t) => _i(t['id'])).toSet().difference(hiddenTopicIds(c));
        final rows = content.practiceQuestions(tid == null ? allowed : (allowed.contains(tid) ? {tid} : <int>{}));
        return {'questions': [for (final x in rows) questionPayload(x, child: c)]};
      case 'GET practice/similar':
        return _similar(c, int.tryParse(q['question_id'] ?? '') ?? -1);
      case 'GET review':
        final due = await _dueReviews(childId);
        final qs = due.take(5).map((r) => content.questionById[_i(r['question_id'])]).whereType<Json>().toList();
        return {'due': due.length, 'questions': [for (final x in qs) questionPayload(x, child: c)]};
      case 'GET foundation':
        return {'topics': await foundationSuggestions(c)};
      case 'GET growth':
        return growth(c);
      case 'POST practice/attempts':
        return _attempt(c, b);
      case 'GET home':
        return _home(c);
      case 'GET progress':
        return {
          'mastery': [for (final x in await mastery(c)) (Map<String, dynamic>.from(x)..remove('home_activity')..remove('common_mistake'))],
        };
      case 'GET tutor/quota':
        return _tutorQuota(c);
      case 'POST tutor/messages':
        return _tutor(c, b);
      case 'GET assessments':
        return _assessments(c);
      case 'POST assessments/*/start':
        return _startAssessment(c, int.parse(s[2]));
      case 'PUT assessment-sessions/*/answers':
        return _saveAnswer(c, s[2], b);
      case 'POST assessment-sessions/*/submit':
        return _submit(c, s[2], b);
      case 'GET assessment-sessions/*/result':
        final sess = await _ownSession(c, s[2]);
        if (sess['status'] != 'submitted') {
          throw ApiException(409, 'Asesmen belum dikumpulkan');
        }
        return _resultPayload(sess);
    }
    throw ApiException(404, 'Tidak ditemukan');
  }

  bool hidesSubject(Json c, Json sub) => cleanSettings(c['settings'])['hide_mulok'] == true && mulokSubjects.contains(sub['name']);

  Set<int> hiddenTopicIds(Json c) {
    final out = <int>{};
    for (final sub in content.subjectsOfGrade(_grade(c))) {
      if (!hidesSubject(c, sub)) {
        continue;
      }
      for (final ch in content.chaptersOfSubject(_i(sub['id']))) {
        for (final t in content.topicsOfChapter(_i(ch['id']))) {
          out.add(_i(t['id']));
        }
      }
    }
    return out;
  }

  Future<Json> _catalog(Json c) async {
    final g = _grade(c);
    final progress = await _col('progress');
    final subjects = <Json>[];
    for (final sub in content.subjectsOfGrade(g)) {
      if (hidesSubject(c, sub)) {
        continue;
      }
      final chOut = <Json>[];
      var ready = false;
      var nTopics = 0;
      for (final ch in content.chaptersOfSubject(_i(sub['id']))) {
        final tOut = <Json>[];
        for (final t in content.topicsOfChapter(_i(ch['id']))) {
          final tid = _i(t['id']);
          final lesson = content.lessonForTopic(tid);
          final nq = content.practiceCount(tid);
          if (lesson != null || nq > 0) {
            ready = true;
          }
          final p = lesson == null ? null : progress['${c['id']}|${lesson['id']}'];
          tOut.add({
            'id': tid, 'title': t['title'], 'question_count': nq,
            'lesson': lesson == null
                ? null
                : {'id': lesson['id'], 'title': lesson['title'], 'minutes': lesson['minutes'], 'block_count': _jl(lesson['blocks']).length, 'step': p?['step'] ?? 0, 'completed': p?['completed_at'] != null, 'downloaded': true, 'sample': lesson['sample'] == true},
          });
        }
        nTopics += tOut.length;
        chOut.add({'id': ch['id'], 'number': ch['number'], 'title': ch['title'], 'semester': ch['semester'] ?? 1, 'topics': tOut});
      }
      subjects.add({'id': sub['id'], 'name': sub['name'], 'short_label': sub['short_label'], 'ready': ready, 'topic_count': nTopics, 'chapters': ready ? chOut : <Json>[]});
    }
    return {'grade': g, 'phase': phase(g), 'curriculum': content.curriculum, 'sample_content': content.includesSample, 'semester': schoolSemester(now), 'subjects': subjects};
  }

  Future<Json> _applyProgress(Json c, Json l, int step, bool completed) async {
    final childId = c['id'] as String;
    final lid = _i(l['id']);
    final id = '$childId|$lid';
    final p = _j(await _progress(childId, lid));
    final blocks = _jl(l['blocks']).length;
    p['child_id'] = childId;
    p['lesson_id'] = lid;
    p['step'] = min(step, max(0, blocks - 1));
    final first = completed && p['completed_at'] == null;
    if (first) {
      p['completed_at'] = _iso(now);
    }
    await _put('progress', id, p);
    if (first) {
      await _log(childId, 'lesson', 'Menyelesaikan materi ${l['title']}', topicId: _i(l['topic_id']));
    }
    return {'lesson_id': lid, 'step': p['step'], 'completed': p['completed_at'] != null, 'downloaded': true};
  }

  Future<Json> _similar(Json c, int questionId) async {
    final base = content.questionById[questionId];
    if (base == null || !allowedTopicIds(_grade(c)).contains(_i(base['topic_id']))) {
      throw ApiException(404, 'Soal tidak ditemukan');
    }
    const rank = {'mudah': 0, 'sedang': 1, 'menantang': 2};
    final solved = (await _attempts(c['id'] as String)).where((a) => a['correct'] == true).map((a) => a['question_id']).toSet();
    final br = rank[base['difficulty']] ?? 1;
    final cands = content.practiceQuestions({_i(base['topic_id'])}).where((x) => x['id'] != base['id']).toList();
    int key(Json x) {
      final r = rank[x['difficulty']] ?? 1;
      return (r > br ? 1000 : 0) + (solved.contains(x['id']) ? 100 : 0) + r * 10;
    }
    cands.sort((a, b) {
      final k = key(a).compareTo(key(b));
      return k != 0 ? k : _i(a['id']).compareTo(_i(b['id']));
    });
    if (cands.isEmpty) {
      throw ApiException(404, 'Belum ada soal serupa');
    }
    return questionPayload(cands.first, child: c);
  }

  Future<Json> _attempt(Json c, Json b) async {
    final childId = c['id'] as String;
    final cu = (b['client_uuid'] as String?) ?? _uuid.v4();
    final existing = (await _col('attempts'))[cu];
    final qid = _i(b['question_id']);
    final q = content.questionById[qid];
    if (q == null || !content.isPractice(q) || !allowedTopicIds(_grade(c)).contains(_i(q['topic_id']))) {
      throw ApiException(422, 'soal tidak tersedia');
    }
    if (existing != null) {
      return _attemptResult(q, existing['correct'] == true, cu);
    }
    final mode = (b['mode'] as String?) ?? 'practice';
    final response = b['response'] == null ? null : _j(b['response']);
    final ok = gradeLocally(q, response);
    const source = {'practice': 'latihan', 'review': 'review', 'foundation': 'pondasi'};
    await _put('attempts', cu, {'id': cu, 'seq': await _nextSeq(), 'child_id': childId, 'question_id': qid, 'topic_id': q['topic_id'], 'response': response, 'correct': ok, 'source': source[mode] ?? 'latihan', 'at': _iso(now)});
    await _scheduleReview(childId, q, ok, mode);
    return _attemptResult(q, ok, cu);
  }

  Json _attemptResult(Json q, bool ok, String cu) {
    final tid = _i(q['topic_id']);
    return {
      'client_uuid': cu, 'question_id': q['id'], 'correct': ok, 'correct_answer': answerText(q), 'answer_key': q['answer'], 'explanation': q['explanation'] ?? '',
      'mistake_hint': ok ? null : q['mistake_hint'], 'topic_id': tid, 'topic': content.topicTitle(tid), 'related_lesson_id': content.lessonForTopic(tid)?['id'], 'scaffold': ok ? null : q['scaffold'],
    };
  }

  Future<Json> _tutorQuota(Json c) async {
    final limit = _i(c['tutor_limit'] ?? defaultTutorLimit);
    final used = await _tutorUsedToday(c['id'] as String, 'tutor');
    return {'limit': limit, 'used': used, 'left': max(0, limit - used)};
  }

  Future<Json> _home(Json c) async {
    final childId = c['id'] as String;
    final atts = await _attempts(childId);
    final m = masteryFrom(_grade(c), atts);
    final quota = await _tutorQuota(c);
    final progress = await _col('progress');
    final lessons = <Json>[];
    final sem = schoolSemester(now);
    final all = content.gradeTopics(_grade(c));
    final topics = [...all.where((t) => content.semesterOfTopic(_i(t['id'])) == sem), ...all.where((t) => content.semesterOfTopic(_i(t['id'])) != sem)];
    for (final t in topics) {
      lessons.addAll(content.lessons.where((l) => _i(l['topic_id']) == _i(t['id'])));
    }
    Json? pick = lessons.where((l) {
          final p = progress['$childId|${l['id']}'];
          return p != null && p['completed_at'] == null;
        }).firstOrNull ??
        lessons.where((l) => progress['$childId|${l['id']}'] == null).firstOrNull ??
        lessons.firstOrNull;
    Json? cont;
    if (pick != null) {
      final p = progress['$childId|${pick['id']}'];
      cont = {'lesson_id': pick['id'], 'title': pick['title'], 'subject': content.subjectOfTopic(_i(pick['topic_id']))?['name'], 'step': p?['step'] ?? 0, 'block_count': _jl(pick['blocks']).length, 'completed': p?['completed_at'] != null};
    }
    final today = _day(now);
    final goal = band(_grade(c)) <= 2 ? 3 : 5;
    final nAtt = atts.where((a) => _day(_parse(a['at'])) == today).length;
    final nLes = progress.values.where((p) => p['child_id'] == childId && p['completed_at'] != null && _day(_parse(p['completed_at'])) == today).length;
    final used = _i(quota['used']);
    return {
      'targets': [
        {'key': 'lesson', 'label': 'Selesaikan 1 materi', 'done': nLes >= 1, 'progress': '${min(nLes, 1)}/1'},
        {'key': 'practice', 'label': 'Kerjakan $goal soal', 'done': nAtt >= goal, 'progress': '${min(nAtt, goal)}/$goal'},
        {'key': 'tutor', 'label': 'Tanya Tutor 1 kali', 'done': used >= 1, 'progress': '${min(used, 1)}/1'},
      ],
      'continue_lesson': cont,
      'developing_topics': [for (final x in m.where((x) => x['state'] == 'developing')) {'topic_id': x['topic_id'], 'topic': x['topic']}],
      'tutor_quota': quota,
      'review_due': (await _dueReviews(childId)).length,
      'foundation': await foundationSuggestions(c, masteryRows: m, attempts: atts),
      'settings': cleanSettings(c['settings']),
    };
  }

  Future<void> _logTutor(String childId, String purpose, String action, String? category) async {
    final id = _uuid.v4();
    await _put('tutor', id, {'id': id, 'child_id': childId, 'purpose': purpose, 'action': action, 'category': category, 'at': _iso(now)});
  }

  Future<Json> _tutor(Json c, Json b) async {
    final childId = c['id'] as String;
    final text = ((b['text'] as String?) ?? '').trim();
    if (text.isEmpty || text.length > 500) {
      throw ApiException(422, 'Pertanyaan harus 1–500 karakter');
    }
    final style = b['style'] as String?;
    final topicId = b['topic_id'] == null ? null : _i(b['topic_id']);
    final limit = _i(c['tutor_limit'] ?? defaultTutorLimit);
    final used = await _tutorUsedToday(childId, 'tutor');
    if (used >= limit) {
      throw ApiException(429, 'Batas pertanyaan Tutor hari ini sudah tercapai');
    }
    final g = _grade(c);
    final verdict = checkChildInput(text);
    var sources = <String>[];
    String? visual;
    String reply;
    if (verdict.action != 'allow') {
      reply = verdict.reply!;
      await _logTutor(childId, 'tutor', verdict.action, verdict.category);
      await _log(childId, 'tutor', verdict.action == 'guide' ? 'Tutor memandu langkah, bukan memberi jawaban langsung' : 'Tutor menolak permintaan yang tidak aman');
    } else {
      final scope = content.topicsWithContent(g).take(3).map((t) => t['title']).join(', ');
      final passages = index.search(text, g, topicId: topicId);
      final hij = style == null ? hijaiyahAnswer(text) : null;
      reply = cleanOutput(hij ?? groundedTutor(text, passages, g, scope.isEmpty ? 'materi kelasmu' : scope, style), band(g) <= 2 ? 900 : 1400);
      sources = <String>{for (final p in passages.take(2)) '${p.sourceType == 'lesson' ? 'Materi' : 'Bank soal'}: ${p.topic ?? p.title}'}.toList();
      final topicName = passages.isNotEmpty ? passages.first.topic : null;
      if (passages.isNotEmpty) {
        visual = content.visualForTopic(passages.first.topicId, topicName);
      }
      await _logTutor(childId, 'tutor', 'ok', null);
      await _log(childId, 'tutor', 'Bertanya ke Tutor (${topicName ?? 'umum'})', topicId: passages.isNotEmpty ? passages.first.topicId : null);
    }
    return {
      'conversation_id': (b['conversation_id'] as String?) ?? _uuid.v4(), 'reply': reply, 'sources': sources, 'refused': verdict.action == 'refuse', 'category': verdict.category,
      'quota_limit': limit, 'quota_left': max(0, limit - used - 1), 'visual': style == 'visual' ? visual : null, 'visual_available': visual != null, 'can_restyle': sources.isNotEmpty,
    };
  }

  Future<void> _finalizeExpired(Json c) async {
    for (final s in (await _col('sessions')).values.toList()) {
      if (s['child_id'] == c['id'] && s['status'] == 'active' && _parse(s['deadline_at']).add(const Duration(seconds: assessmentGraceSeconds)).isBefore(now)) {
        await _finalize(c, s, auto: true);
      }
    }
  }

  Future<Json> _assessments(Json c) async {
    await _finalizeExpired(c);
    final sessions = (await _col('sessions')).values.where((s) => s['child_id'] == c['id']).toList();
    final mine0 = content.assessments.where((a) => _i(a['grade']) == _grade(c)).toList();
    final list = [for (final sem in [1, 2]) ...mine0.where((a) => ((a['semester'] as num?) ?? 1).toInt() == sem)];
    final out = <Json>[];
    for (final a in list) {
      final mine = sessions.where((s) => s['assessment_id'] == a['id']).toList();
      final done = mine.where((s) => s['result'] != null).toList()..sort((x, y) => (y['submitted_at'] as String).compareTo(x['submitted_at'] as String));
      final active = mine.where((s) => s['status'] == 'active').firstOrNull;
      final last = done.firstOrNull;
      out.add({
        'id': a['id'], 'type': a['template'], 'semester': a['semester'] ?? 1, 'title': a['title'], 'duration_minutes': a['duration_minutes'], 'question_count': _jl(a['questions']).length, 'sample': a['sample'] == true,
        'active_session_id': active?['id'],
        'last_result': last == null ? null : {'score': (_j(last['result'])['score'] as num).round(), 'date': relativeLabel(_parse(last['submitted_at'])), 'final': true},
      });
    }
    final available = list.map((a) => a['template']).toSet();
    return {'assessments': out, 'upcoming': out.isEmpty ? content.templates.where((t) => !available.contains(t)).toList() : const <String>[]};
  }

  Json _sessionPayload(Json sess) {
    final a = content.assessmentById[_i(sess['assessment_id'])]!;
    final orders = _j(sess['option_orders']);
    return {
      'session_id': sess['id'], 'assessment_id': a['id'], 'title': a['title'], 'status': sess['status'], 'started_at': sess['started_at'], 'deadline_at': sess['deadline_at'], 'server_now': _iso(now),
      'questions': [
        for (final qid in (sess['order'] as List).map((e) => (e as num).toInt()))
          if (content.questionById[qid] != null) questionPayload(content.questionById[qid]!, order: ((orders['$qid'] as List?) ?? const []).map((e) => (e as num).toInt()).toList()),
      ],
      'answers': _j(sess['answers']),
    };
  }

  Future<Json> _startAssessment(Json c, int aid) async {
    final a = content.assessmentById[aid];
    if (a == null || _i(a['grade']) != _grade(c)) {
      throw ApiException(404, 'Asesmen tidak ditemukan');
    }
    await _finalizeExpired(c);
    final existing = (await _col('sessions')).values.where((s) => s['child_id'] == c['id'] && s['assessment_id'] == aid && s['status'] == 'active').firstOrNull;
    if (existing != null) {
      return _sessionPayload(existing);
    }
    final order = _jl(a['questions']).map((x) => _i(x['id'])).where((id) => content.questionById[id] != null).toList();
    if (order.isEmpty) {
      throw ApiException(409, 'Asesmen belum memiliki soal');
    }
    if (a['shuffle_questions'] == true) {
      order.shuffle(rnd);
    }
    final optOrders = <String, dynamic>{};
    for (final qid in order) {
      final q = content.questionById[qid]!;
      final pos = _jl(q['options']).map((o) => _i(o['index'])).toList();
      if (a['shuffle_options'] == true && (q['type'] == 'mc' || q['type'] == 'multi')) {
        pos.shuffle(rnd);
      }
      optOrders['$qid'] = pos;
    }
    final id = _uuid.v4();
    final sess = <String, dynamic>{
      'id': id, 'child_id': c['id'], 'assessment_id': aid, 'started_at': _iso(now), 'deadline_at': _iso(now.add(Duration(minutes: _i(a['duration_minutes'])))),
      'status': 'active', 'order': order, 'option_orders': optOrders, 'answers': <String, dynamic>{},
    };
    await _put('sessions', id, sess);
    return _sessionPayload(sess);
  }

  Future<Json> _ownSession(Json c, String sid) async {
    final s = (await _col('sessions'))[sid];
    if (s == null || s['child_id'] != c['id']) {
      throw ApiException(404, 'Sesi asesmen tidak ditemukan');
    }
    return s;
  }

  bool _late(Json sess) => now.isAfter(_parse(sess['deadline_at']).add(const Duration(seconds: assessmentGraceSeconds)));

  Future<Json> _saveAnswer(Json c, String sid, Json b) async {
    final sess = await _ownSession(c, sid);
    if (sess['status'] != 'active') {
      throw ApiException(409, 'Asesmen sudah dikumpulkan');
    }
    if (_late(sess)) {
      throw ApiException(409, 'Waktu asesmen sudah habis');
    }
    final qid = _i(b['question_id']);
    if (!(sess['order'] as List).map((e) => (e as num).toInt()).contains(qid)) {
      throw ApiException(422, 'Soal bukan bagian dari asesmen ini');
    }
    final answers = _j(sess['answers']);
    answers['$qid'] = b['response'];
    await _put('sessions', sid, {...sess, 'answers': answers});
    return {'saved': true, 'question_id': qid, 'server_now': _iso(now)};
  }

  Future<Json> _submit(Json c, String sid, Json b) async {
    var sess = await _ownSession(c, sid);
    if (sess['status'] == 'submitted') {
      return _resultPayload(sess);
    }
    final late = _late(sess);
    if (!late) {
      final answers = _j(sess['answers']);
      final order = (sess['order'] as List).map((e) => (e as num).toInt()).toSet();
      for (final x in _jl(b['answers'])) {
        final qid = _i(x['question_id']);
        if (order.contains(qid)) {
          answers['$qid'] = x['response'];
        }
      }
      sess = {...sess, 'answers': answers};
    }
    final done = await _finalize(c, sess, auto: late, key: b['idempotency_key'] as String?);
    return _resultPayload(done);
  }

  Future<Json> _finalize(Json c, Json sess, {required bool auto, String? key}) async {
    final childId = c['id'] as String;
    final a = content.assessmentById[_i(sess['assessment_id'])]!;
    final points = {for (final x in _jl(a['questions'])) _i(x['id']): ((x['points'] ?? 1) as num).toDouble()};
    final answers = _j(sess['answers']);
    final order = (sess['order'] as List).map((e) => (e as num).toInt()).toList();
    final graded = <String, dynamic>{};
    var total = 0.0;
    var got = 0.0;
    var correct = 0;
    var objective = 0;
    var essays = 0;
    final weak = <int>[];
    for (final qid in order) {
      final q = content.questionById[qid];
      if (q == null) {
        continue;
      }
      if (q['type'] == 'essay') {
        essays++;
        graded['$qid'] = null;
        continue;
      }
      objective++;
      final pts = points[qid] ?? 1.0;
      total += pts;
      final resp = answers['$qid'] == null ? null : _j(answers['$qid']);
      final ok = gradeLocally(q, resp);
      graded['$qid'] = ok;
      if (ok) {
        got += pts;
        correct++;
      } else if (!weak.contains(_i(q['topic_id']))) {
        weak.add(_i(q['topic_id']));
      }
      final aid = '${sess['id']}:$qid';
      await _put('attempts', aid, {'id': aid, 'seq': await _nextSeq(), 'child_id': childId, 'question_id': qid, 'topic_id': q['topic_id'], 'response': resp, 'correct': ok, 'source': 'asesmen', 'at': _iso(now)});
    }
    final score = total == 0 ? 0.0 : (got / total * 1000).round() / 10;
    final passing = a['passing_score'] == null ? null : score >= (a['passing_score'] as num).toDouble();
    final out = <String, dynamic>{
      ...sess, 'status': 'submitted', 'submitted_at': _iso(now), 'auto_submitted': auto, 'submit_key': key,
      'result': {'score': score, 'correct': correct, 'total': objective, 'essays': essays, 'weak_topic_ids': weak, 'graded': graded, 'passed': passing},
    };
    await _put('sessions', sess['id'] as String, out);
    await _log(childId, 'assessment', 'Asesmen ${a['short_title']}: nilai ${score.round()}');
    return out;
  }

  Json _resultPayload(Json sess) {
    final r = _j(sess['result']);
    final graded = _j(r['graded']);
    final answers = _j(sess['answers']);
    final order = (sess['order'] as List).map((e) => (e as num).toInt()).toList();
    return {
      'session_id': sess['id'], 'score': (r['score'] as num).round(), 'correct': r['correct'], 'total': r['total'], 'pending_review': 0, 'essays': r['essays'] ?? 0, 'final': true, 'auto_submitted': sess['auto_submitted'] == true,
      'weak_topics': [for (final t in (r['weak_topic_ids'] as List)) {'id': t, 'title': content.topicTitle((t as num).toInt())}],
      'submitted_at': sess['submitted_at'], 'verified_by_server': false,
      'review': [
        for (var i = 0; i < order.length; i++)
          if (content.questionById[order[i]] != null)
            () {
              final q = content.questionById[order[i]]!;
              return <String, dynamic>{
                'n': i + 1, 'question_id': order[i], 'question': q['body'], 'your_answer': responseText(q, answers['${order[i]}'] == null ? null : _j(answers['${order[i]}'])),
                'correct_answer': answerText(q), 'correct': graded['${order[i]}'] == true, 'needs_review': q['type'] == 'essay', 'essay': q['type'] == 'essay', 'explanation': q['explanation'] ?? '', 'topic': content.topicTitle(_i(q['topic_id'])),
              };
            }(),
      ],
    };
  }

  Future<dynamic> parent(String method, String path, {Object? body}) async {
    final s = _seg(path);
    final b = _j(body);
    if (s.isEmpty || s[0] != 'parent') {
      throw ApiException(404, 'Tidak ditemukan');
    }
    final key = '$method ${s.sublist(1).map(_pattern).join('/')}';
    switch (key) {
      case 'GET children':
        return {'children': [for (final c in await _children()) await childInfo(c)]};
      case 'POST children':
        return _addChild(b);
      case 'PATCH children/*':
        return _patchChild(s[2], b);
      case 'DELETE children/*':
        await _child(s[2]);
        await _eraseChild(s[2]);
        return {'deleted': true};
      case 'GET children/*/dashboard':
        return _dashboard(await _child(s[2]));
      case 'GET children/*/summary':
        return {'text': await teacherSummary(await _child(s[2]))};
      case 'GET children/*/growth':
        return growth(await _child(s[2]));
      case 'GET children/*/recommendations':
        return {'recommendations': [for (final r in await recommendations(await _child(s[2]))) _recOut(r)]};
      case 'POST children/*/recommendations/*/done':
        return _recDone(await _child(s[2]), s[4], b['done'] != false);
      case 'POST assistant/messages':
        return _assistant(await _child(b['child_id'] as String), ((b['text'] as String?) ?? '').trim(), b['conversation_id'] as String?);
      case 'GET export':
        return exportBackup();
      case 'POST import':
        return importBackup(_j(b['backup']));
      case 'POST delete-account':
        if (b['confirm'] != 'HAPUS') {
          throw ApiException(422, 'Ketik HAPUS untuk konfirmasi');
        }
        await wipeAll();
        return {'deleted': true};
    }
    throw ApiException(404, 'Tidak ditemukan');
  }

  String _cleanNickname(Object? raw) {
    final v = (raw?.toString() ?? '').trim().split(RegExp(r'\s+')).where((x) => x.isNotEmpty).join(' ');
    if (v.length < 2 || v.length > 20) {
      throw ApiException(422, 'Nama panggilan 2–20 huruf');
    }
    if (RegExp(r'\d').hasMatch(v)) {
      throw ApiException(422, 'Nama panggilan tidak boleh berisi angka');
    }
    return v;
  }

  int _cleanGrade(Object? raw) {
    final g = raw is num ? raw.toInt() : int.tryParse(raw?.toString() ?? '') ?? 0;
    if (g < 1 || g > 9) {
      throw ApiException(422, 'Kelas harus 1–9');
    }
    return g;
  }

  Future<Json> _addChild(Json b) async {
    if ((await _children()).length >= maxChildren) {
      throw ApiException(409, 'Maksimal $maxChildren profil anak');
    }
    final id = _uuid.v4();
    final grade = _cleanGrade(b['grade']);
    final c = <String, dynamic>{'id': id, 'nickname': _cleanNickname(b['nickname']), 'grade': grade, 'settings': cleanSettings(b['settings'] ?? (grade <= 2 ? {'read_aloud': true} : null)), 'tutor_limit': defaultTutorLimit, 'created_at': _iso(now)};
    await _put('children', id, c);
    await _log(id, 'profile', 'Profil dibuat oleh orang tua');
    return childInfo(c);
  }

  Future<Json> _patchChild(String id, Json b) async {
    final c = {...await _child(id)};
    if (b['nickname'] != null) {
      c['nickname'] = _cleanNickname(b['nickname']);
    }
    if (b['grade'] != null) {
      c['grade'] = _cleanGrade(b['grade']);
    }
    if (b['tutor_daily_limit'] != null) {
      c['tutor_limit'] = _i(b['tutor_daily_limit']).clamp(0, 100);
    }
    if (b['settings'] != null) {
      c['settings'] = cleanSettings(b['settings']);
    }
    await _put('children', id, c);
    return childInfo(c);
  }

  Future<void> _eraseChild(String id) async {
    for (final col in dataCollections) {
      final docs = await _col(col);
      for (final e in docs.entries.toList()) {
        if (e.value['child_id'] == id || (col == 'children' && e.key == id)) {
          await _del(col, e.key);
        }
      }
    }
  }

  Future<Json> _recDone(Json c, String recId, bool done) async {
    final recs = await recommendations(c);
    final r = recs.where((x) => x['id'] == recId).firstOrNull;
    if (r == null) {
      throw ApiException(404, 'Rekomendasi tidak ditemukan');
    }
    await _put('recs', '${c['id']}|$recId', {'child_id': c['id'], 'key': recId, 'done_at': done ? _iso(now) : null, 'sig': r['sig']});
    return _recOut({...r, 'done': done});
  }

  Future<Json> _dashboard(Json c) async {
    final childId = c['id'] as String;
    final atts = await _attempts(childId);
    final m = masteryFrom(_grade(c), atts);
    final ok = atts.where((a) => a['correct'] == true).length;
    final lessonsDone = (await _col('progress')).values.where((p) => p['child_id'] == childId && p['completed_at'] != null).length;
    final exams = (await _results(childId)).take(10).toList();
    final titles = {for (final x in m) x['topic_id']: x['topic']};
    final log = (await _col('activity')).values.where((a) => a['child_id'] == childId).toList()..sort((a, b) => (b['at'] as String).compareTo(a['at'] as String));
    final recs = await recommendations(c);
    final top = recs.where((r) => r['kind'] != 'maintain').firstOrNull;
    final last = exams.firstOrNull;
    Json examOut(Json s) {
      final r = _j(s['result']);
      return {
        'title': content.assessmentById[_i(s['assessment_id'])]?['title'] ?? 'Asesmen', 'score': (r['score'] as num).round(), 'date': relativeLabel(_parse(s['submitted_at'])), 'final': true, 'pending_review': 0,
        'weak_topics': [for (final t in (r['weak_topic_ids'] as List)) if (titles[t] != null) titles[t]],
      };
    }

    return {
      'child': await childInfo(c),
      'last_active': log.isEmpty ? null : relativeLabel(_parse(log.first['at'])),
      'kpis': {
        'lessons_completed': lessonsDone, 'answers_total': atts.length, 'answers_correct': ok, 'accuracy_pct': atts.isEmpty ? null : (ok * 100 / atts.length).round(),
        'last_assessment': last == null ? null : {'score': (_j(last['result'])['score'] as num).round(), 'date': relativeLabel(_parse(last['submitted_at'])), 'final': true},
      },
      'mastery': [for (final x in m) (Map<String, dynamic>.from(x)..remove('home_activity')..remove('common_mistake'))],
      'top_recommendation': top == null ? null : _recOut(top),
      'assessments': [for (final s in exams) examOut(s)],
      'activity': [for (final a in log.take(8)) {'text': a['summary'], 'when': relativeLabel(_parse(a['at']))}],
      'signals': await signals(c),
      'review_due': (await _dueReviews(childId)).length,
    };
  }

  Future<Json> _assistant(Json c, String text, String? conv) async {
    if (text.isEmpty || text.length > 600) {
      throw ApiException(422, 'Pertanyaan harus 1–600 karakter');
    }
    final childId = c['id'] as String;
    final used = await _tutorUsedToday(childId, 'parent');
    if (used >= parentAssistantLimit) {
      throw ApiException(429, 'Batas Tanya BOBO hari ini sudah tercapai');
    }
    final verdict = checkParentInput(text, c['nickname'] as String);
    String reply;
    String basis;
    if (verdict.action != 'allow') {
      reply = verdict.reply!;
      basis = 'Panduan keamanan · bukan diagnosis';
      await _logTutor(childId, 'parent', verdict.action, verdict.category);
    } else {
      final atts = await _attempts(childId);
      final m = masteryFrom(_grade(c), atts);
      final exams = await _results(childId);
      final last = exams.firstOrNull;
      final weak = last == null ? <String>[] : [for (final t in (_j(last['result'])['weak_topic_ids'] as List)) content.topicTitle((t as num).toInt())].where((x) => x.isNotEmpty).toList();
      basis = 'Berdasarkan ${atts.length} jawaban${exams.isNotEmpty ? ' dan ${exams.length} asesmen' : ''} ${c['nickname']}';
      reply = cleanOutput(groundedParentAnswer(text, c['nickname'] as String, _grade(c), m, last == null ? null : (_j(last['result'])['score'] as num).round(), weak), 1800);
      await _logTutor(childId, 'parent', 'ok', null);
    }
    return {'conversation_id': conv ?? _uuid.v4(), 'reply': reply, 'basis': basis, 'quota_limit': parentAssistantLimit, 'quota_left': max(0, parentAssistantLimit - used - 1)};
  }

  Future<Json> exportBackup() async {
    final cols = <String, dynamic>{};
    for (final col in dataCollections) {
      cols[col] = await _col(col);
    }
    return {'app': 'bobo-belajar', 'backup_format': backupFormat, 'created_at': _iso(now), 'collections': cols};
  }

  Future<Json> importBackup(Json backup) async {
    if (backup['app'] != 'bobo-belajar' || backup['backup_format'] != backupFormat) {
      throw ApiException(422, 'Berkas ini bukan cadangan BOBO Belajar yang valid');
    }
    final cols = _j(backup['collections']);
    final children = _j(cols['children']);
    if (children.isEmpty) {
      throw ApiException(422, 'Cadangan tidak berisi profil anak');
    }
    for (final col in dataCollections) {
      for (final id in (await _col(col)).keys.toList()) {
        await _del(col, id);
      }
      for (final e in _j(cols[col]).entries) {
        await _put(col, e.key, _j(e.value));
      }
    }
    _seq = null;
    return {'restored': true, 'children': children.length};
  }
}
