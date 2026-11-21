import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureStore {
  static const FlutterSecureStorage _s = FlutterSecureStorage(aOptions: AndroidOptions(encryptedSharedPreferences: true));

  Future<String?> read(String key) => _s.read(key: key);

  Future<void> write(String key, String? value) async {
    if (value == null) {
      await _s.delete(key: key);
    } else {
      await _s.write(key: key, value: value);
    }
  }

  Future<void> clear() => _s.deleteAll();

  Future<String?> studentToken(String childId) => read('student_$childId');

  Future<void> setStudentToken(String childId, String? token) => write('student_$childId', token);
}
