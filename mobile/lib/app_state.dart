import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:uuid/uuid.dart';

import 'core/api.dart';
import 'core/local_db.dart';
import 'core/models.dart';
import 'core/secure_store.dart';

enum AppMode { loading, server, auth, setPin, profiles, child, parent }

const uuidGen = Uuid();

class AppState extends ChangeNotifier {
  AppState({SecureStore? store, LocalDb? db})
      : store = store ?? SecureStore(),
        db = db ?? LocalDb();

  final SecureStore store;
  final LocalDb db;
  ApiClient api = ApiClient('');
  AppMode mode = AppMode.loading;
  String serverUrl = '';
  String? refreshToken;
  String? parentAccess;
  String parentName = '';
  bool hasPin = false;
  List<ChildInfo> children = [];
  ChildInfo? child;
  String? studentToken;
  bool offline = false;
  int pending = 0;
  Timer? _syncTimer;
  bool _syncing = false;

  Future<void> init() async {
    serverUrl = await store.read('server_url') ?? '';
    refreshToken = await store.read('refresh_token');
    parentName = await store.read('parent_name') ?? '';
    hasPin = (await store.read('has_pin')) == '1';
    api = ApiClient(serverUrl);
    final cached = await db.getJson('children');
    if (cached is List) {
      children = cached.map((e) => ChildInfo.fromJson(Map<String, dynamic>.from(e as Map))).toList();
    }
    if (serverUrl.isEmpty) {
      mode = AppMode.server;
    } else if (refreshToken == null) {
      mode = AppMode.auth;
    } else if (!hasPin) {
      mode = AppMode.auth;
    } else {
      mode = AppMode.profiles;
    }
    notifyListeners();
  }

  Future<String?> setServer(String url) async {
    var u = url.trim();
    if (u.isEmpty) {
      return 'Alamat server wajib diisi';
    }
    if (!u.startsWith('http://') && !u.startsWith('https://')) {
      u = 'https://$u';
    }
    final probe = ApiClient(u);
    if (!await probe.health()) {
      return 'Server tidak bisa dihubungi. Periksa alamat dan koneksi.';
    }
    serverUrl = u;
    api = probe;
    await store.write('server_url', u);
    mode = AppMode.auth;
    notifyListeners();
    return null;
  }

  void changeServer() {
    mode = AppMode.server;
    notifyListeners();
  }

  Future<void> _saveTokens(Map<String, dynamic> t) async {
    refreshToken = t['refresh_token'] as String;
    parentAccess = t['access_token'] as String;
    parentName = (t['display_name'] as String?) ?? '';
    hasPin = t['has_pin'] == true;
    await store.write('refresh_token', refreshToken);
    await store.write('parent_name', parentName);
    await store.write('has_pin', hasPin ? '1' : '0');
  }

  Future<void> _afterParentAuth() async {
    await loadChildren();
    await _ensureStudentTokens();
    if (hasPin) {
      parentAccess = null;
      mode = AppMode.profiles;
    } else {
      mode = AppMode.setPin;
    }
    notifyListeners();
  }

  Future<void> login(String email, String password) async {
    final t = asMap(await api.post('/auth/login', body: {'email': email.trim(), 'password': password}));
    if (!(t['roles'] as List).contains('parent')) {
      throw ApiException(403, 'Akun ini bukan akun orang tua. Gunakan CMS untuk akun admin.');
    }
    await _saveTokens(t);
    await _afterParentAuth();
  }

  Future<void> register(String name, String email, String password) async {
    final t = asMap(await api.post('/auth/register', body: {
      'email': email.trim(),
      'password': password,
      'display_name': name.trim(),
      'accept_privacy_policy': true,
      'accept_child_data_processing': true,
    }));
    await _saveTokens(t);
    await _afterParentAuth();
  }

  Future<void> setPin(String pin, String password) async {
    await api.put('/parent/pin', token: parentAccess, body: {'pin': pin, 'password': password});
    hasPin = true;
    await store.write('has_pin', '1');
    parentAccess = null;
    mode = AppMode.profiles;
    notifyListeners();
  }

  Future<void> unlockParent(String pin) async {
    final t = asMap(await api.post('/auth/refresh', body: {'refresh_token': refreshToken, 'pin': pin}));
    await _saveTokens(t);
    await loadChildren();
    await _ensureStudentTokens();
    child = null;
    studentToken = null;
    mode = AppMode.parent;
    _stopSyncTimer();
    notifyListeners();
  }

  void lock() {
    parentAccess = null;
    child = null;
    studentToken = null;
    mode = AppMode.profiles;
    _stopSyncTimer();
    notifyListeners();
  }

  Future<void> loadChildren() async {
    final r = asMap(await api.get('/parent/children', token: parentAccess));
    children = asList(r['children']).map(ChildInfo.fromJson).toList();
    await db.putJson('children', children.map((c) => c.toJson()).toList());
    notifyListeners();
  }

  Future<void> _ensureStudentTokens() async {
    for (final c in children) {
      final existing = await store.studentToken(c.id);
      if (existing == null) {
        await fetchStudentToken(c.id);
      }
    }
  }

  Future<void> fetchStudentToken(String childId) async {
    final r = asMap(await api.post('/auth/child-session', token: parentAccess, body: {'child_id': childId}));
    await store.setStudentToken(childId, r['student_token'] as String);
  }

  Future<String?> enterChild(ChildInfo c) async {
    final token = await store.studentToken(c.id);
    if (token == null) {
      return 'Profil ini belum siap di perangkat. Buka Mode Orang Tua sekali untuk menyiapkannya.';
    }
    child = c;
    studentToken = token;
    mode = AppMode.child;
    pending = await db.countQueued(c.id);
    notifyListeners();
    unawaited(syncNow());
    _startSyncTimer();
    return null;
  }

  Future<void> logout() async {
    _stopSyncTimer();
    await store.clear();
    await store.write('server_url', serverUrl);
    await db.wipe();
    refreshToken = null;
    parentAccess = null;
    children = [];
    child = null;
    studentToken = null;
    hasPin = false;
    mode = AppMode.auth;
    notifyListeners();
  }

  void _markOnline(bool online) {
    if (offline == online) {
      offline = !online;
      notifyListeners();
    }
  }

  Future<dynamic> student(String method, String path, {Object? body, Map<String, String>? query}) async {
    try {
      final r = await api.request(method, path, token: studentToken, body: body, query: query);
      _markOnline(true);
      return r;
    } on ApiException catch (e) {
      if (e.isOffline) {
        _markOnline(false);
      } else if (e.status == 401 && child != null) {
        await store.setStudentToken(child!.id, null);
      }
      rethrow;
    }
  }

  Future<dynamic> parent(String method, String path, {Object? body}) async {
    if (parentAccess == null) {
      lock();
      throw ApiException(401, 'Sesi orang tua berakhir. Masukkan PIN lagi.');
    }
    try {
      return await api.request(method, path, token: parentAccess, body: body);
    } on ApiException catch (e) {
      if (e.status == 401) {
        lock();
      }
      rethrow;
    }
  }

  Future<void> queueAttempt(Map<String, dynamic> attempt) async {
    final c = child;
    if (c == null) {
      return;
    }
    await db.enqueue(c.id, 'attempt', attempt);
    pending = await db.countQueued(c.id);
    notifyListeners();
  }

  Future<void> queueProgress(Map<String, dynamic> progress) async {
    final c = child;
    if (c == null) {
      return;
    }
    await db.enqueue(c.id, 'progress', progress);
    pending = await db.countQueued(c.id);
    notifyListeners();
  }

  Future<void> syncNow() async {
    final c = child;
    if (c == null || _syncing) {
      return;
    }
    _syncing = true;
    try {
      final items = await db.queued(c.id);
      if (items.isEmpty) {
        pending = 0;
        return;
      }
      final body = {
        'batch_uuid': uuidGen.v4(),
        'attempts': items.where((i) => i.kind == 'attempt').map((i) => i.payload).toList(),
        'lesson_progress': items.where((i) => i.kind == 'progress').map((i) => i.payload).toList(),
      };
      await student('POST', '/student/sync', body: body);
      await db.deleteQueued(items.map((i) => i.id).toList());
      pending = await db.countQueued(c.id);
    } on ApiException {
      pending = await db.countQueued(c.id);
    } finally {
      _syncing = false;
      notifyListeners();
    }
  }

  void _startSyncTimer() {
    _syncTimer?.cancel();
    _syncTimer = Timer.periodic(const Duration(seconds: 30), (_) async {
      if (offline) {
        if (await api.health()) {
          _markOnline(true);
          await syncNow();
        }
      } else if (pending > 0) {
        await syncNow();
      }
    });
  }

  void _stopSyncTimer() {
    _syncTimer?.cancel();
    _syncTimer = null;
  }

  @override
  void dispose() {
    _stopSyncTimer();
    super.dispose();
  }
}
