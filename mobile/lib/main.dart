import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import 'app_state.dart';
import 'core/theme.dart';
import 'screens/child/child_shell.dart';
import 'screens/parent/parent_shell.dart';
import 'screens/profiles_screen.dart';
import 'screens/setup_screens.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
  runApp(ChangeNotifierProvider(create: (_) => AppState()..init(), child: const BoboApp()));
}

class BoboApp extends StatelessWidget {
  const BoboApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'BOBO Belajar',
      debugShowCheckedModeBanner: false,
      theme: buildTheme(),
      home: const _Root(),
    );
  }
}

class _Root extends StatelessWidget {
  const _Root();

  @override
  Widget build(BuildContext context) {
    final mode = context.select<AppState, AppMode>((s) => s.mode);
    final error = context.select<AppState, Object?>((s) => s.loadError);
    final Widget screen = switch (mode) {
      AppMode.loading => Scaffold(body: Center(child: error == null ? const CircularProgressIndicator() : Padding(padding: const EdgeInsets.all(24), child: Text('Materi aplikasi gagal dimuat: $error', textAlign: TextAlign.center)))),
      AppMode.setup => const SetupScreen(),
      AppMode.profiles => const ProfilesScreen(),
      AppMode.child => const ChildShell(),
      AppMode.parent => const ParentShell(),
    };
    return AnimatedSwitcher(duration: const Duration(milliseconds: 200), child: KeyedSubtree(key: ValueKey(mode), child: screen));
  }
}
