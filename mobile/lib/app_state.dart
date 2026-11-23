import 'package:flutter/foundation.dart';
import 'package:uuid/uuid.dart';

import 'core/api.dart';
import 'core/local_db.dart';
import 'core/models.dart';
import 'core/speech.dart';
import 'local/content.dart';
import 'local/engine.dart';
import 'local/store.dart';

enum AppMode { loading, setup, profiles, child, parent }

const uuidGen = Uuid();

class AppState extends ChangeNotifier {
  AppState({LocalDb? db, LocalStore? store, Future<Content> Function()? contentLoader})
      : db = db ?? LocalDb(),
        _store = store,
        _contentLoader = contentLoader ?? Content.load;

  final LocalDb db;
  final LocalStore? _store;
  final Future<Content> Function() _contentLoader;
  late LocalEngine engine;
  AppMode mode = AppMode.loading;
  bool hasPin = false;
  bool parentUnlocked = false;
  List<ChildInfo> children = [];
  ChildInfo? child;
  Map<String, bool> childSettings = {};
  String? setupRecoveryCode;
  bool sampleContent = false;
  Object? loadError;
  final bool offline = false;
  final int pending = 0;

  Future<void> init() async {
    try {
      final content = await _contentLoader();
      sampleContent = content.includesSample;
      engine = LocalEngine(_store ?? SqliteStore(db), content);
      hasPin = await engine.hasPin();
      await _loadVoice();
      await _reloadChildren();
      mode = hasPin ? AppMode.profiles : AppMode.setup;
    } catch (e) {
      loadError = e;
    }
    notifyListeners();
  }

  Future<void> _loadVoice() async {
    try {
      final v = await db.getJson('tts_voice');
      if (v is Map) {
        await Speech.instance.setVoice({for (final e in v.entries) '${e.key}': '${e.value}'});
      }
    } catch (_) {}
  }

  Future<void> saveVoice(Map<String, String>? voice) async {
    await Speech.instance.setVoice(voice);
    try {
      await db.putJson('tts_voice', voice);
    } catch (_) {}
    notifyListeners();
  }

  Future<void> _reloadChildren() async {
    final r = asMap(await engine.parent('GET', '/parent/children'));
    children = asList(r['children']).map(ChildInfo.fromJson).toList();
  }

  Future<String> createPin(String pin) async {
    final code = await engine.setupPin(pin);
    hasPin = true;
    setupRecoveryCode = code;
    notifyListeners();
    return code;
  }

  void finishSetup() {
    setupRecoveryCode = null;
    parentUnlocked = true;
    child = null;
    mode = AppMode.parent;
    notifyListeners();
  }

  Future<void> unlockParent(String pin) async {
    await engine.verifyPin(pin);
    await _reloadChildren();
    parentUnlocked = true;
    child = null;
    mode = AppMode.parent;
    notifyListeners();
  }

  Future<String> resetPin(String recoveryCode, String newPin) async {
    final code = await engine.resetPinWithRecovery(recoveryCode, newPin);
    hasPin = true;
    return code;
  }

  void lock() {
    parentUnlocked = false;
    child = null;
    mode = hasPin ? AppMode.profiles : AppMode.setup;
    notifyListeners();
  }

  Future<void> loadChildren() async {
    await _reloadChildren();
    notifyListeners();
  }

  Future<String?> enterChild(ChildInfo c) async {
    final fresh = children.where((x) => x.id == c.id).firstOrNull ?? c;
    child = fresh;
    childSettings = Map.of(fresh.settings);
    parentUnlocked = false;
    mode = AppMode.child;
    notifyListeners();
    return null;
  }

  bool setting(String key) => childSettings[key] == true;

  Future<void> wipeAll() async {
    await engine.wipeAll();
    hasPin = false;
    parentUnlocked = false;
    children = [];
    child = null;
    mode = AppMode.setup;
    notifyListeners();
  }

  Future<dynamic> student(String method, String path, {Object? body, Map<String, String>? query}) async {
    final c = child;
    if (c == null) {
      throw ApiException(401, 'Pilih profil anak dulu.');
    }
    return engine.student(c.id, method, path, body: body, query: query);
  }

  Future<dynamic> parent(String method, String path, {Object? body}) async {
    if (!parentUnlocked) {
      lock();
      throw ApiException(401, 'Mode orang tua terkunci. Masukkan PIN lagi.');
    }
    final r = await engine.parent(method, path, body: body);
    if (path == '/parent/delete-account') {
      hasPin = false;
      parentUnlocked = false;
      children = [];
      child = null;
      mode = AppMode.setup;
      notifyListeners();
    }
    return r;
  }
}
