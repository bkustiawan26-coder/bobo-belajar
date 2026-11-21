class ApiException implements Exception {
  ApiException(this.status, this.message);

  final int status;
  final String message;

  bool get isOffline => status == 0;

  @override
  String toString() => message;
}
