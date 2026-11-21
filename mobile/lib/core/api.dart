import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

class ApiException implements Exception {
  ApiException(this.status, this.message);

  final int status;
  final String message;

  bool get isOffline => status == 0;

  @override
  String toString() => message;
}

class ApiClient {
  ApiClient(this.baseUrl);

  String baseUrl;
  final http.Client _http = http.Client();

  Uri _uri(String path, Map<String, String>? query) {
    final base = baseUrl.endsWith('/') ? baseUrl.substring(0, baseUrl.length - 1) : baseUrl;
    final u = Uri.parse('$base/v1$path');
    return query == null ? u : u.replace(queryParameters: query);
  }

  Future<dynamic> request(String method, String path, {String? token, Object? body, Map<String, String>? query}) async {
    final req = http.Request(method, _uri(path, query));
    req.headers['Accept'] = 'application/json';
    req.headers['Content-Type'] = 'application/json';
    if (token != null) {
      req.headers['Authorization'] = 'Bearer $token';
    }
    if (body != null) {
      req.body = jsonEncode(body);
    }
    http.Response res;
    try {
      final streamed = await _http.send(req).timeout(const Duration(seconds: 20));
      res = await http.Response.fromStream(streamed);
    } on SocketException {
      throw ApiException(0, 'Tidak ada koneksi ke server');
    } on TimeoutException {
      throw ApiException(0, 'Server tidak merespons');
    } on HandshakeException {
      throw ApiException(0, 'Koneksi aman ke server gagal');
    } on http.ClientException {
      throw ApiException(0, 'Tidak ada koneksi ke server');
    }
    dynamic data;
    if (res.bodyBytes.isNotEmpty) {
      try {
        data = jsonDecode(utf8.decode(res.bodyBytes));
      } catch (_) {
        data = null;
      }
    }
    if (res.statusCode >= 400) {
      var msg = 'Terjadi kesalahan (${res.statusCode})';
      if (data is Map && data['detail'] != null) {
        final d = data['detail'];
        if (d is String) {
          msg = d;
        } else if (d is List && d.isNotEmpty && d.first is Map) {
          msg = (d.first as Map)['msg']?.toString() ?? msg;
        }
      }
      throw ApiException(res.statusCode, msg);
    }
    return data;
  }

  Future<dynamic> get(String path, {String? token, Map<String, String>? query}) => request('GET', path, token: token, query: query);

  Future<dynamic> post(String path, {String? token, Object? body}) => request('POST', path, token: token, body: body ?? <String, dynamic>{});

  Future<dynamic> put(String path, {String? token, Object? body}) => request('PUT', path, token: token, body: body);

  Future<dynamic> delete(String path, {String? token}) => request('DELETE', path, token: token);

  Future<bool> health() async {
    try {
      final base = baseUrl.endsWith('/') ? baseUrl.substring(0, baseUrl.length - 1) : baseUrl;
      final r = await _http.get(Uri.parse('$base/health')).timeout(const Duration(seconds: 8));
      return r.statusCode == 200;
    } catch (_) {
      return false;
    }
  }
}
