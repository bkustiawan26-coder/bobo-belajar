abstract class LocalStore {
  Future<Map<String, Map<String, dynamic>>> load(String collection);

  Future<void> put(String collection, String id, Map<String, dynamic> doc);

  Future<void> remove(String collection, String id);

  Future<void> clear({Set<String> keep = const {}});
}

class MemoryStore implements LocalStore {
  final Map<String, Map<String, Map<String, dynamic>>> data = {};

  @override
  Future<Map<String, Map<String, dynamic>>> load(String collection) async {
    final c = data[collection] ?? {};
    return c.map((k, v) => MapEntry(k, Map<String, dynamic>.from(v)));
  }

  @override
  Future<void> put(String collection, String id, Map<String, dynamic> doc) async {
    data.putIfAbsent(collection, () => {})[id] = Map<String, dynamic>.from(doc);
  }

  @override
  Future<void> remove(String collection, String id) async {
    data[collection]?.remove(id);
  }

  @override
  Future<void> clear({Set<String> keep = const {}}) async {
    data.removeWhere((k, _) => !keep.contains(k));
  }
}
