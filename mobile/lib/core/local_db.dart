import 'dart:convert';

import 'package:path/path.dart' as p;
import 'package:sqflite/sqflite.dart';

class QueuedItem {
  QueuedItem(this.id, this.kind, this.payload);

  final int id;
  final String kind;
  final Map<String, dynamic> payload;
}

class LocalDb {
  Database? _db;

  Future<Database> get db async {
    if (_db != null) {
      return _db!;
    }
    final dir = await getDatabasesPath();
    _db = await openDatabase(
      p.join(dir, 'bobo_belajar.db'),
      version: 1,
      onCreate: (d, v) async {
        await d.execute('CREATE TABLE kv (k TEXT PRIMARY KEY, v TEXT NOT NULL)');
        await d.execute('CREATE TABLE queue (id INTEGER PRIMARY KEY AUTOINCREMENT, child_id TEXT NOT NULL, kind TEXT NOT NULL, payload TEXT NOT NULL, created_at TEXT NOT NULL)');
        await d.execute('CREATE INDEX ix_queue_child ON queue(child_id)');
      },
    );
    return _db!;
  }

  Future<dynamic> getJson(String key) async {
    final rows = await (await db).query('kv', where: 'k = ?', whereArgs: [key]);
    if (rows.isEmpty) {
      return null;
    }
    return jsonDecode(rows.first['v'] as String);
  }

  Future<void> putJson(String key, Object? value) async {
    final d = await db;
    if (value == null) {
      await d.delete('kv', where: 'k = ?', whereArgs: [key]);
      return;
    }
    await d.insert('kv', {'k': key, 'v': jsonEncode(value)}, conflictAlgorithm: ConflictAlgorithm.replace);
  }

  Future<void> enqueue(String childId, String kind, Map<String, dynamic> payload) async {
    await (await db).insert('queue', {'child_id': childId, 'kind': kind, 'payload': jsonEncode(payload), 'created_at': DateTime.now().toUtc().toIso8601String()});
  }

  Future<List<QueuedItem>> queued(String childId) async {
    final rows = await (await db).query('queue', where: 'child_id = ?', whereArgs: [childId], orderBy: 'id', limit: 400);
    return rows.map((r) => QueuedItem(r['id'] as int, r['kind'] as String, Map<String, dynamic>.from(jsonDecode(r['payload'] as String) as Map))).toList();
  }

  Future<int> countQueued(String childId) async {
    final r = await (await db).rawQuery('SELECT COUNT(*) AS n FROM queue WHERE child_id = ?', [childId]);
    return (r.first['n'] as int?) ?? 0;
  }

  Future<void> deleteQueued(List<int> ids) async {
    if (ids.isEmpty) {
      return;
    }
    final marks = List.filled(ids.length, '?').join(',');
    await (await db).delete('queue', where: 'id IN ($marks)', whereArgs: ids);
  }

  Future<void> wipe() async {
    final d = await db;
    await d.delete('kv');
    await d.delete('queue');
  }
}
