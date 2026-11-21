import 'package:flutter/material.dart';

class Palette {
  static const ground = Color(0xFFF4F6FA);
  static const surface = Color(0xFFFFFFFF);
  static const border = Color(0xFFE3E8F0);
  static const borderStrong = Color(0xFFCBD5E1);
  static const ink = Color(0xFF0F172A);
  static const inkSoft = Color(0xFF334155);
  static const muted = Color(0xFF475569);
  static const parent = Color(0xFF1E3A5F);
  static const parentSoft = Color(0xFFDCE6F2);
  static const ok = Color(0xFF15803D);
  static const okInk = Color(0xFF166534);
  static const okSoft = Color(0xFFDCFCE7);
  static const okBg = Color(0xFFF0FDF4);
  static const bad = Color(0xFFB91C1C);
  static const badInk = Color(0xFF991B1B);
  static const badSoft = Color(0xFFFECACA);
  static const badBg = Color(0xFFFEF2F2);
  static const warnInk = Color(0xFF92400E);
  static const warnSoft = Color(0xFFFEF3C7);
  static const devInk = Color(0xFF1E40AF);
  static const devSoft = Color(0xFFDBEAFE);
  static const neutralSoft = Color(0xFFEEF1F5);
}

class BandTheme {
  const BandTheme({required this.accent, required this.soft, required this.ink, required this.radius, required this.radiusSmall, required this.title, required this.body, required this.question});

  final Color accent;
  final Color soft;
  final Color ink;
  final double radius;
  final double radiusSmall;
  final double title;
  final double body;
  final double question;

  static BandTheme forGrade(int grade) {
    if (grade <= 2) {
      return const BandTheme(accent: Color(0xFFC2410C), soft: Color(0xFFFFEDD5), ink: Color(0xFF7C2D12), radius: 22, radiusSmall: 16, title: 24, body: 17, question: 20);
    }
    if (grade <= 4) {
      return const BandTheme(accent: Color(0xFF0F766E), soft: Color(0xFFCCFBF1), ink: Color(0xFF134E4A), radius: 20, radiusSmall: 14, title: 22, body: 16, question: 19);
    }
    if (grade <= 6) {
      return const BandTheme(accent: Color(0xFF1D4ED8), soft: Color(0xFFDBEAFE), ink: Color(0xFF1E3A8A), radius: 18, radiusSmall: 12, title: 22, body: 15, question: 18);
    }
    return const BandTheme(accent: Color(0xFF4338CA), soft: Color(0xFFE0E7FF), ink: Color(0xFF312E81), radius: 14, radiusSmall: 10, title: 20, body: 15, question: 17);
  }

  static const parent = BandTheme(accent: Palette.parent, soft: Palette.parentSoft, ink: Palette.parent, radius: 18, radiusSmall: 12, title: 20, body: 15, question: 17);
}

String phaseFor(int grade) => grade <= 2 ? 'Fase A' : grade <= 4 ? 'Fase B' : grade <= 6 ? 'Fase C' : 'Fase D';

String gradeLabel(int grade) => 'Kelas $grade · ${grade <= 6 ? 'SD' : 'SMP'} · ${phaseFor(grade)}';

ThemeData buildTheme() {
  final base = ThemeData(
    useMaterial3: true,
    fontFamily: 'PlusJakartaSans',
    colorScheme: ColorScheme.fromSeed(seedColor: Palette.parent, surface: Palette.surface),
    scaffoldBackgroundColor: Palette.ground,
  );
  return base.copyWith(
    textTheme: base.textTheme.apply(bodyColor: Palette.ink, displayColor: Palette.ink),
    appBarTheme: const AppBarTheme(backgroundColor: Palette.surface, foregroundColor: Palette.ink, elevation: 0, scrolledUnderElevation: 0),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: const Color(0xFFF8FAFC),
      contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
      border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: const BorderSide(color: Palette.borderStrong)),
      enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: const BorderSide(color: Palette.borderStrong)),
    ),
  );
}
