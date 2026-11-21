class ChildInfo {
  ChildInfo({required this.id, required this.nickname, required this.grade, this.tutorToday = 0, this.tutorLimit = 10, this.safetyRefusals = 0});

  factory ChildInfo.fromJson(Map<String, dynamic> j) => ChildInfo(
        id: j['id'] as String,
        nickname: j['nickname'] as String,
        grade: (j['grade'] as num).toInt(),
        tutorToday: (j['tutor_today'] as num?)?.toInt() ?? 0,
        tutorLimit: (j['tutor_limit'] as num?)?.toInt() ?? 10,
        safetyRefusals: (j['safety_refusals'] as num?)?.toInt() ?? 0,
      );

  final String id;
  final String nickname;
  final int grade;
  final int tutorToday;
  final int tutorLimit;
  final int safetyRefusals;

  String get initial => nickname.isEmpty ? '?' : nickname.substring(0, 1).toUpperCase();

  Map<String, dynamic> toJson() => {'id': id, 'nickname': nickname, 'grade': grade, 'tutor_today': tutorToday, 'tutor_limit': tutorLimit, 'safety_refusals': safetyRefusals};
}

Map<String, dynamic> asMap(Object? v) => v == null ? <String, dynamic>{} : Map<String, dynamic>.from(v as Map);

List<Map<String, dynamic>> asList(Object? v) => v == null ? <Map<String, dynamic>>[] : (v as List).map((e) => Map<String, dynamic>.from(e as Map)).toList();
