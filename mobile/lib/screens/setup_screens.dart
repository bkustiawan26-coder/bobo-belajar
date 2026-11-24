import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../app_state.dart';
import '../core/api.dart';
import '../core/theme.dart';
import '../widgets/common.dart';
import 'privacy_screen.dart';

class SetupScreen extends StatefulWidget {
  const SetupScreen({super.key});

  @override
  State<SetupScreen> createState() => _SetupScreenState();
}

class _SetupScreenState extends State<SetupScreen> {
  int _step = 0;
  bool _agreePrivacy = false;
  bool _agreeChild = false;
  final _pin = TextEditingController();
  final _pin2 = TextEditingController();
  String? _error;
  bool _busy = false;

  @override
  void dispose() {
    _pin.dispose();
    _pin2.dispose();
    super.dispose();
  }

  Future<void> _savePin() async {
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
      await context.read<AppState>().createPin(_pin.text);
      if (mounted) {
        setState(() => _step = 2);
      }
    } on ApiException catch (e) {
      if (mounted) {
        setState(() => _error = e.message);
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    if (app.setupRecoveryCode != null && _step < 2) {
      _step = 2;
    }
    final Widget body = switch (_step) {
      0 => _welcome(),
      1 => _pinForm(),
      _ => RecoveryCodeView(code: app.setupRecoveryCode ?? '', buttonLabel: 'Saya sudah menyimpannya, lanjut', onDone: app.finishSetup),
    };
    return Scaffold(body: SafeArea(child: ContentWidth(maxWidth: kFormMaxWidth, child: body)));
  }

  Widget _welcome() {
    return ListView(padding: const EdgeInsets.all(24), children: [
      const Row(children: [BoboLogo(), SizedBox(width: 12), Text('BOBO BELAJAR', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 19))]),
      const SizedBox(height: 28),
      const Text('Selamat datang!', style: TextStyle(fontSize: 28, fontWeight: FontWeight.w800)),
      const SizedBox(height: 8),
      const Text('Teman belajar untuk anak Kelas 1–9. Semua materi, latihan, dan data belajar tersimpan di HP ini saja, tanpa akun dan tanpa internet.', style: TextStyle(fontSize: 15, color: Palette.muted, height: 1.5)),
      const SizedBox(height: 20),
      const AppCard(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          _Point(icon: Icons.phone_android_rounded, text: 'Data anak tidak dikirim ke server mana pun.'),
          _Point(icon: Icons.lock_outline_rounded, text: 'Mode Orang Tua dikunci dengan PIN.'),
          _Point(icon: Icons.backup_outlined, text: 'Buat cadangan berkala dari menu Anak, karena data hilang jika aplikasi dihapus.'),
        ]),
      ),
      const SizedBox(height: 16),
      CheckboxListTile(
        value: _agreePrivacy,
        onChanged: (v) => setState(() => _agreePrivacy = v == true),
        controlAffinity: ListTileControlAffinity.leading,
        contentPadding: EdgeInsets.zero,
        title: const Text('Saya sudah membaca kebijakan privasi', style: TextStyle(fontSize: 14)),
        subtitle: Align(
          alignment: Alignment.centerLeft,
          child: TextButton(
            onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => const PrivacyScreen())),
            style: TextButton.styleFrom(padding: EdgeInsets.zero, minimumSize: const Size(0, 36)),
            child: const Text('Baca kebijakan privasi'),
          ),
        ),
      ),
      CheckboxListTile(
        value: _agreeChild,
        onChanged: (v) => setState(() => _agreeChild = v == true),
        controlAffinity: ListTileControlAffinity.leading,
        contentPadding: EdgeInsets.zero,
        title: const Text('Saya orang tua/wali dan menyetujui aktivitas belajar anak disimpan di HP ini', style: TextStyle(fontSize: 14)),
      ),
      const SizedBox(height: 12),
      PrimaryButton(label: 'Mulai', onPressed: _agreePrivacy && _agreeChild ? () => setState(() => _step = 1) : null),
    ]);
  }

  Widget _pinForm() {
    return ListView(padding: const EdgeInsets.all(24), children: [
      Align(alignment: Alignment.centerLeft, child: IconButton(onPressed: () => setState(() => _step = 0), icon: const Icon(Icons.arrow_back_rounded), tooltip: 'Kembali')),
      const Icon(Icons.lock_outline_rounded, size: 48, color: Palette.parent),
      const SizedBox(height: 16),
      const Text('Buat PIN orang tua', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800)),
      const SizedBox(height: 8),
      const Text('PIN membuka Mode Orang Tua, supaya anak tidak bisa membuka laporan dan pengaturan.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
      const SizedBox(height: 20),
      TextField(controller: _pin, keyboardType: TextInputType.number, obscureText: true, maxLength: 6, inputFormatters: [FilteringTextInputFormatter.digitsOnly], decoration: const InputDecoration(labelText: 'PIN (4–6 angka)', counterText: '')),
      const SizedBox(height: 12),
      TextField(controller: _pin2, keyboardType: TextInputType.number, obscureText: true, maxLength: 6, inputFormatters: [FilteringTextInputFormatter.digitsOnly], decoration: const InputDecoration(labelText: 'Ulangi PIN', counterText: ''), onSubmitted: (_) => _savePin()),
      if (_error != null) ...[const SizedBox(height: 12), Text(_error!, style: const TextStyle(color: Palette.bad, fontWeight: FontWeight.w700))],
      const SizedBox(height: 20),
      PrimaryButton(label: 'Simpan PIN', busy: _busy, onPressed: _savePin),
    ]);
  }
}

class _Point extends StatelessWidget {
  const _Point({required this.icon, required this.text});

  final IconData icon;
  final String text;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Icon(icon, size: 20, color: Palette.parent),
        const SizedBox(width: 10),
        Expanded(child: Text(text, style: const TextStyle(fontSize: 14, height: 1.45))),
      ]),
    );
  }
}

class RecoveryCodeView extends StatelessWidget {
  const RecoveryCodeView({super.key, required this.code, required this.onDone, required this.buttonLabel});

  final String code;
  final VoidCallback onDone;
  final String buttonLabel;

  @override
  Widget build(BuildContext context) {
    return ListView(padding: const EdgeInsets.all(24), children: [
      const Icon(Icons.key_rounded, size: 48, color: Palette.parent),
      const SizedBox(height: 16),
      const Text('Simpan kode pemulihan', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800)),
      const SizedBox(height: 8),
      const Text('Jika lupa PIN, kode ini satu-satunya cara membuat PIN baru tanpa menghapus data. Tulis di kertas atau simpan di tempat aman, jangan berikan ke anak.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
      const SizedBox(height: 20),
      AppCard(
        color: Palette.parentSoft,
        borderColor: Palette.parentSoft,
        child: Column(children: [
          SelectableText(code, textAlign: TextAlign.center, style: const TextStyle(fontSize: 30, fontWeight: FontWeight.w800, letterSpacing: 3, color: Palette.parent)),
          const SizedBox(height: 8),
          TextButton.icon(
            onPressed: () async {
              await Clipboard.setData(ClipboardData(text: code));
              if (context.mounted) {
                showToast(context, 'Kode disalin.');
              }
            },
            icon: const Icon(Icons.copy_rounded, size: 18),
            label: const Text('Salin kode'),
          ),
        ]),
      ),
      const SizedBox(height: 20),
      PrimaryButton(label: buttonLabel, onPressed: onDone),
    ]);
  }
}
