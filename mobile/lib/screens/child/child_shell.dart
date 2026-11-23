import 'dart:async';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/models.dart';
import '../../core/persona.dart';
import '../../core/speech.dart';
import '../../core/theme.dart';
import '../../widgets/common.dart';
import 'belajar_tab.dart';
import 'home_tab.dart';
import 'latihan_tab.dart';
import 'tutor_tab.dart';
import 'ujian_tab.dart';

class ChildNav extends ChangeNotifier {
  int tab = 0;
  int? practiceTopicId;
  String practiceMode = 'practice';
  int practiceVersion = 0;
  int? openLessonId;
  int? openSubjectId;
  int lessonVersion = 0;
  String? tutorPrompt;
  bool examRunning = false;

  void go(int t) {
    tab = t;
    notifyListeners();
  }

  void practice(int? topicId, {String mode = 'practice'}) {
    practiceTopicId = topicId;
    practiceMode = mode;
    practiceVersion++;
    tab = 2;
    notifyListeners();
  }

  void lesson(int lessonId) {
    openLessonId = lessonId;
    lessonVersion++;
    tab = 1;
    notifyListeners();
  }

  void subject(int subjectId) {
    openSubjectId = subjectId;
    openLessonId = null;
    lessonVersion++;
    tab = 1;
    notifyListeners();
  }

  void askTutor(String prompt) {
    tutorPrompt = prompt;
    tab = 4;
    notifyListeners();
  }

  String? takeTutorPrompt() {
    final p = tutorPrompt;
    tutorPrompt = null;
    return p;
  }

  void setExamRunning(bool v) {
    if (examRunning != v) {
      examRunning = v;
      notifyListeners();
    }
  }
}

class ChildShell extends StatelessWidget {
  const ChildShell({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(create: (_) => ChildNav(), child: const _ChildScaffold());
  }
}

class _ChildScaffold extends StatefulWidget {
  const _ChildScaffold();

  @override
  State<_ChildScaffold> createState() => _ChildScaffoldState();
}

class _ChildScaffoldState extends State<_ChildScaffold> {
  static const _titles = ['', 'Belajar', 'Latihan', 'Ujian', 'Tutor BOBO'];
  Timer? _timer;
  DateTime _since = DateTime.now();
  bool _asking = false;

  @override
  void initState() {
    super.initState();
    final grade = context.read<AppState>().child!.grade;
    Speech.instance.configure(grade);
    _timer = Timer.periodic(const Duration(seconds: 30), (_) => _maybeBreak());
  }

  @override
  void dispose() {
    _timer?.cancel();
    Speech.instance.stop();
    super.dispose();
  }

  Future<void> _maybeBreak() async {
    if (!mounted || _asking) {
      return;
    }
    final app = context.read<AppState>();
    final nav = context.read<ChildNav>();
    final c = app.child;
    if (c == null || nav.examRunning) {
      return;
    }
    final persona = Persona.forGrade(c.grade);
    final minutes = DateTime.now().difference(_since).inMinutes;
    if (minutes < persona.breakMinutes) {
      return;
    }
    _asking = true;
    final body = persona.breakBody(minutes);
    if (app.setting('read_aloud')) {
      Speech.instance.speak('${persona.breakTitle()}\n$body');
    } else {
      Speech.instance.stop();
    }
    final t = BandTheme.forGrade(c.grade);
    final rest = await showDialog<bool>(
      context: context,
      barrierDismissible: false,
      builder: (ctx) => AlertDialog(
        icon: Icon(Icons.self_improvement_rounded, color: t.accent, size: 36),
        title: Text(persona.breakTitle(), textAlign: TextAlign.center),
        content: Text(body, textAlign: TextAlign.center, style: const TextStyle(fontSize: 15, height: 1.5)),
        actionsAlignment: MainAxisAlignment.center,
        actions: [
          TextButton(onPressed: () => Navigator.of(ctx).pop(false), child: const Text('Lanjut belajar')),
          FilledButton(onPressed: () => Navigator.of(ctx).pop(true), style: FilledButton.styleFrom(backgroundColor: t.accent), child: const Text('Istirahat dulu')),
        ],
      ),
    );
    Speech.instance.stop();
    _since = DateTime.now();
    _asking = false;
    if (rest == true && mounted) {
      nav.go(0);
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    final nav = context.watch<ChildNav>();
    final ChildInfo c = app.child!;
    final t = BandTheme.forGrade(c.grade);
    final scale = app.setting('larger_text') ? 1.18 : 1.0;
    return MediaQuery(
      data: MediaQuery.of(context).copyWith(textScaler: TextScaler.linear(MediaQuery.textScalerOf(context).scale(1) * scale)),
      child: PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop && nav.tab != 0 && !nav.examRunning) {
          nav.go(0);
        }
      },
      child: Scaffold(
        body: SafeArea(
          child: Column(children: [
            Container(
              color: Palette.surface,
              padding: const EdgeInsets.fromLTRB(20, 10, 16, 10),
              child: Row(children: [
                Avatar(c.initial, color: t.accent, size: 40, radius: 12),
                const SizedBox(width: 12),
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(nav.tab == 0 ? Persona.forGrade(c.grade).greeting(c.nickname, DateTime.now().hour) : _titles[nav.tab], maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 17)),
                  Text(gradeLabel(c.grade), style: const TextStyle(fontSize: 13, color: Palette.muted)),
                ])),
                if (!nav.examRunning)
                  OutlinedButton(
                    onPressed: () => app.lock(),
                    style: OutlinedButton.styleFrom(minimumSize: const Size(44, 44), foregroundColor: Palette.ink, side: const BorderSide(color: Palette.borderStrong), shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12))),
                    child: const Text('Ganti profil', style: TextStyle(fontWeight: FontWeight.w600)),
                  ),
              ]),
            ),
            const Divider(height: 1, color: Palette.border),
            Expanded(
              child: IndexedStack(index: nav.tab, children: const [HomeTab(), BelajarTab(), LatihanTab(), UjianTab(), TutorTab()]),
            ),
          ]),
        ),
        bottomNavigationBar: nav.examRunning
            ? null
            : NavigationBar(
                selectedIndex: nav.tab,
                onDestinationSelected: nav.go,
                backgroundColor: Palette.surface,
                indicatorColor: t.soft,
                labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
                destinations: const [
                  NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home_rounded), label: 'Home'),
                  NavigationDestination(icon: Icon(Icons.menu_book_outlined), selectedIcon: Icon(Icons.menu_book_rounded), label: 'Belajar'),
                  NavigationDestination(icon: Icon(Icons.edit_outlined), selectedIcon: Icon(Icons.edit_rounded), label: 'Latihan'),
                  NavigationDestination(icon: Icon(Icons.assignment_outlined), selectedIcon: Icon(Icons.assignment_rounded), label: 'Ujian'),
                  NavigationDestination(icon: Icon(Icons.chat_bubble_outline_rounded), selectedIcon: Icon(Icons.chat_bubble_rounded), label: 'Tutor'),
                ],
              ),
      ),
      ),
    );
  }
}

class CatalogCache {
  static Future<Map<String, dynamic>> load(AppState app, {bool refresh = false}) async => asMap(await app.student('GET', '/student/catalog'));
}
