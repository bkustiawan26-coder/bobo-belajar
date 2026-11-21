import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../app_state.dart';
import '../../core/models.dart';
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

  void practice(int? topicId) {
    practiceTopicId = topicId;
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

class _ChildScaffold extends StatelessWidget {
  const _ChildScaffold();

  static const _titles = ['', 'Belajar', 'Latihan', 'Ujian', 'Tutor BOBO'];

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    final nav = context.watch<ChildNav>();
    final ChildInfo c = app.child!;
    final t = BandTheme.forGrade(c.grade);
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop && nav.tab != 0 && !nav.examRunning) {
          nav.go(0);
        }
      },
      child: Scaffold(
        body: SafeArea(
          child: Column(children: [
            if (app.offline) OfflineBanner(pending: app.pending),
            Container(
              color: Palette.surface,
              padding: const EdgeInsets.fromLTRB(20, 10, 16, 10),
              child: Row(children: [
                Avatar(c.initial, color: t.accent, size: 40, radius: 12),
                const SizedBox(width: 12),
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(nav.tab == 0 ? 'Hai, ${c.nickname}!' : _titles[nav.tab], maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 17)),
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
    );
  }
}

class CatalogCache {
  static Future<Map<String, dynamic>> load(AppState app, {bool refresh = false}) async {
    final key = 'catalog_${app.child!.id}';
    if (!refresh) {
      final cached = await app.db.getJson(key);
      if (cached != null && app.offline) {
        return asMap(cached);
      }
    }
    try {
      final data = asMap(await app.student('GET', '/student/catalog'));
      await app.db.putJson(key, data);
      return data;
    } catch (e) {
      final cached = await app.db.getJson(key);
      if (cached != null) {
        return asMap(cached);
      }
      rethrow;
    }
  }

  static Future<Map<String, dynamic>?> pack(AppState app) async {
    final p = await app.db.getJson('pack_${app.child!.id}');
    return p == null ? null : asMap(p);
  }

  static Future<void> download(AppState app) async {
    final p = asMap(await app.student('GET', '/student/offline-pack'));
    await app.db.putJson('pack_${app.child!.id}', p);
  }

  static Future<void> removePack(AppState app) => app.db.putJson('pack_${app.child!.id}', null);
}
