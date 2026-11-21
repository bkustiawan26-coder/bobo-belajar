import 'dart:convert';
import 'dart:math';

import 'package:crypto/crypto.dart';

const int pinIterations = 20000;

List<int> pbkdf2Sha256(List<int> password, List<int> salt, int iterations, int length) {
  final hmac = Hmac(sha256, password);
  final out = <int>[];
  var block = 1;
  while (out.length < length) {
    var u = hmac.convert([...salt, (block >> 24) & 0xff, (block >> 16) & 0xff, (block >> 8) & 0xff, block & 0xff]).bytes;
    final t = List<int>.from(u);
    for (var i = 1; i < iterations; i++) {
      u = hmac.convert(u).bytes;
      for (var j = 0; j < t.length; j++) {
        t[j] ^= u[j];
      }
    }
    out.addAll(t);
    block++;
  }
  return out.sublist(0, length);
}

String hashSecret(String secret, {Random? random, int iterations = pinIterations}) {
  final r = random ?? Random.secure();
  final salt = List<int>.generate(16, (_) => r.nextInt(256));
  final dk = pbkdf2Sha256(utf8.encode(secret), salt, iterations, 32);
  return 'pbkdf2-sha256\$$iterations\$${base64Encode(salt)}\$${base64Encode(dk)}';
}

bool verifySecret(String secret, String? stored) {
  if (stored == null) {
    return false;
  }
  final parts = stored.split('\$');
  if (parts.length != 4 || parts[0] != 'pbkdf2-sha256') {
    return false;
  }
  final iterations = int.tryParse(parts[1]) ?? 0;
  final salt = base64Decode(parts[2]);
  final want = base64Decode(parts[3]);
  final got = pbkdf2Sha256(utf8.encode(secret), salt, iterations, want.length);
  var diff = got.length ^ want.length;
  for (var i = 0; i < want.length && i < got.length; i++) {
    diff |= got[i] ^ want[i];
  }
  return diff == 0;
}

String newRecoveryCode({Random? random}) {
  const alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  final r = random ?? Random.secure();
  final chars = List.generate(10, (_) => alphabet[r.nextInt(alphabet.length)]).join();
  return '${chars.substring(0, 5)}-${chars.substring(5)}';
}

String normalizeRecoveryCode(String code) => code.toUpperCase().replaceAll(RegExp(r'[^A-Z0-9]'), '');
