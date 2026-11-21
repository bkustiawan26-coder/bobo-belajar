import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../app_state.dart';
import '../core/theme.dart';
import '../widgets/common.dart';

class ServerScreen extends StatefulWidget {
  const ServerScreen({super.key});

  @override
  State<ServerScreen> createState() => _ServerScreenState();
}

class _ServerScreenState extends State<ServerScreen> {
  final _ctl = TextEditingController(text: const String.fromEnvironment('API_BASE_URL'));
  String? _error;
  bool _busy = false;

  @override
  void initState() {
    super.initState();
    final current = context.read<AppState>().serverUrl;
    if (current.isNotEmpty) {
      _ctl.text = current;
    }
  }

  @override
  void dispose() {
    _ctl.dispose();
    super.dispose();
  }

  Future<void> _save() async {
    setState(() {
      _busy = true;
      _error = null;
    });
    final err = await context.read<AppState>().setServer(_ctl.text);
    if (!mounted) {
      return;
    }
    setState(() {
      _busy = false;
      _error = err;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: ListView(padding: const EdgeInsets.all(24), children: [
          const Row(children: [BoboLogo(), SizedBox(width: 12), Text('BOBO BELAJAR', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 19))]),
          const SizedBox(height: 32),
          const Text('Sambungkan ke server', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800)),
          const SizedBox(height: 8),
          const Text('Masukkan alamat server BOBO BELAJAR yang dipakai keluargamu.', style: TextStyle(fontSize: 15, color: Palette.muted)),
          const SizedBox(height: 24),
          TextField(
            controller: _ctl,
            keyboardType: TextInputType.url,
            autocorrect: false,
            decoration: InputDecoration(labelText: 'Alamat server', hintText: 'https://api.contoh.id', errorText: _error),
            onSubmitted: (_) => _save(),
          ),
          const SizedBox(height: 16),
          PrimaryButton(label: 'Sambungkan', busy: _busy, onPressed: _save),
        ]),
      ),
    );
  }
}

class AuthScreen extends StatefulWidget {
  const AuthScreen({super.key});

  @override
  State<AuthScreen> createState() => _AuthScreenState();
}

class _AuthScreenState extends State<AuthScreen> {
  bool _register = false;
  final _name = TextEditingController();
  final _email = TextEditingController();
  final _pw = TextEditingController();
  bool _privacy = false;
  bool _childData = false;
  bool _busy = false;
  String? _error;

  @override
  void dispose() {
    _name.dispose();
    _email.dispose();
    _pw.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    final app = context.read<AppState>();
    if (_register && (!_privacy || !_childData)) {
      setState(() => _error = 'Centang kedua persetujuan untuk membuat akun.');
      return;
    }
    if (_register && _pw.text.length < 8) {
      setState(() => _error = 'Kata sandi minimal 8 karakter.');
      return;
    }
    setState(() {
      _busy = true;
      _error = null;
    });
    try {
      if (_register) {
        await app.register(_name.text, _email.text, _pw.text);
      } else {
        await app.login(_email.text, _pw.text);
      }
    } catch (e) {
      if (mounted) {
        setState(() => _error = e.toString());
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: ListView(padding: const EdgeInsets.all(24), children: [
          const Row(children: [BoboLogo(), SizedBox(width: 12), Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('BOBO BELAJAR', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 19)),
            Text('Belajar Lebih Mandiri, Mendampingi Lebih Percaya Diri', style: TextStyle(fontSize: 12, color: Palette.muted)),
          ]))]),
          const SizedBox(height: 28),
          Text(_register ? 'Buat akun orang tua' : 'Masuk sebagai orang tua', style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w800)),
          const SizedBox(height: 8),
          const Text('Akun dikelola orang tua. Anak belajar lewat profil yang Anda buat, tanpa email atau kata sandi.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
          const SizedBox(height: 20),
          if (_register) ...[
            TextField(controller: _name, textCapitalization: TextCapitalization.words, decoration: const InputDecoration(labelText: 'Nama Anda')),
            const SizedBox(height: 12),
          ],
          TextField(controller: _email, keyboardType: TextInputType.emailAddress, autocorrect: false, decoration: const InputDecoration(labelText: 'Email')),
          const SizedBox(height: 12),
          TextField(controller: _pw, obscureText: true, decoration: const InputDecoration(labelText: 'Kata sandi'), onSubmitted: (_) => _submit()),
          if (_register) ...[
            const SizedBox(height: 12),
            CheckboxListTile(
              value: _privacy,
              onChanged: (v) => setState(() => _privacy = v ?? false),
              contentPadding: EdgeInsets.zero,
              controlAffinity: ListTileControlAffinity.leading,
              title: const Text('Saya menyetujui Kebijakan Privasi BOBO BELAJAR.', style: TextStyle(fontSize: 14)),
            ),
            CheckboxListTile(
              value: _childData,
              onChanged: (v) => setState(() => _childData = v ?? false),
              contentPadding: EdgeInsets.zero,
              controlAffinity: ListTileControlAffinity.leading,
              title: const Text('Sebagai orang tua/wali, saya mengizinkan BOBO memproses nama panggilan, kelas, dan aktivitas belajar anak saya untuk keperluan belajar.', style: TextStyle(fontSize: 14)),
            ),
            const Text('Percakapan anak tidak dipakai untuk melatih model AI. Tidak ada iklan.', style: TextStyle(fontSize: 12, color: Palette.muted)),
          ],
          if (_error != null) ...[const SizedBox(height: 12), Text(_error!, style: const TextStyle(color: Palette.bad, fontWeight: FontWeight.w700))],
          const SizedBox(height: 20),
          PrimaryButton(label: _register ? 'Buat akun' : 'Masuk', busy: _busy, onPressed: _submit),
          const SizedBox(height: 12),
          TextButton(
            onPressed: () => setState(() {
              _register = !_register;
              _error = null;
            }),
            child: Text(_register ? 'Sudah punya akun? Masuk' : 'Belum punya akun? Daftar'),
          ),
          TextButton(onPressed: () => context.read<AppState>().changeServer(), child: const Text('Ganti alamat server')),
        ]),
      ),
    );
  }
}

class SetPinScreen extends StatefulWidget {
  const SetPinScreen({super.key});

  @override
  State<SetPinScreen> createState() => _SetPinScreenState();
}

class _SetPinScreenState extends State<SetPinScreen> {
  final _pin = TextEditingController();
  final _pin2 = TextEditingController();
  final _pw = TextEditingController();
  String? _error;
  bool _busy = false;

  @override
  void dispose() {
    _pin.dispose();
    _pin2.dispose();
    _pw.dispose();
    super.dispose();
  }

  Future<void> _save() async {
    if (!RegExp(r'^\d{4,6}$').hasMatch(_pin.text)) {
      setState(() => _error = 'PIN harus 4–6 angka.');
      return;
    }
    if (_pin.text != _pin2.text) {
      setState(() => _error = 'Kedua PIN tidak sama.');
      return;
    }
    setState(() {
      _busy = true;
      _error = null;
    });
    try {
      await context.read<AppState>().setPin(_pin.text, _pw.text);
    } catch (e) {
      if (mounted) {
        setState(() => _error = e.toString());
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: ListView(padding: const EdgeInsets.all(24), children: [
          const Icon(Icons.lock_outline_rounded, size: 48, color: Palette.parent),
          const SizedBox(height: 16),
          const Text('Buat PIN orang tua', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800)),
          const SizedBox(height: 8),
          const Text('PIN dipakai untuk membuka Mode Orang Tua di perangkat ini, supaya anak tidak bisa membuka laporan dan pengaturan.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
          const SizedBox(height: 20),
          TextField(controller: _pin, keyboardType: TextInputType.number, obscureText: true, maxLength: 6, decoration: const InputDecoration(labelText: 'PIN (4–6 angka)', counterText: '')),
          const SizedBox(height: 12),
          TextField(controller: _pin2, keyboardType: TextInputType.number, obscureText: true, maxLength: 6, decoration: const InputDecoration(labelText: 'Ulangi PIN', counterText: '')),
          const SizedBox(height: 12),
          TextField(controller: _pw, obscureText: true, decoration: const InputDecoration(labelText: 'Kata sandi akun (untuk konfirmasi)')),
          if (_error != null) ...[const SizedBox(height: 12), Text(_error!, style: const TextStyle(color: Palette.bad, fontWeight: FontWeight.w700))],
          const SizedBox(height: 20),
          PrimaryButton(label: 'Simpan PIN', busy: _busy, onPressed: _save),
        ]),
      ),
    );
  }
}
