import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../app_state.dart';
import '../core/api.dart';
import '../core/theme.dart';
import '../widgets/common.dart';
import 'setup_screens.dart';

class ProfilesScreen extends StatelessWidget {
  const ProfilesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final app = context.watch<AppState>();
    return Scaffold(
      body: SafeArea(
        child: ListView(padding: const EdgeInsets.fromLTRB(24, 32, 24, 28), children: [
          const Row(children: [
            BoboLogo(),
            SizedBox(width: 12),
            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('BOBO BELAJAR', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 19)),
              Text('Belajar Lebih Mandiri, Mendampingi Lebih Percaya Diri', style: TextStyle(fontSize: 12, color: Palette.muted, fontWeight: FontWeight.w500)),
            ])),
          ]),
          const SizedBox(height: 28),
          const Text('Siapa yang mau belajar hari ini?', style: TextStyle(fontSize: 28, fontWeight: FontWeight.w800, height: 1.2)),
          const SizedBox(height: 8),
          const Text('Pilih profilmu untuk mulai.', style: TextStyle(fontSize: 15, color: Palette.muted)),
          const SizedBox(height: 24),
          if (app.children.isEmpty)
            const AppCard(child: Text('Belum ada profil anak. Buka Mode Orang Tua lalu tambahkan profil di menu Anak.', style: TextStyle(fontSize: 14, color: Palette.muted, height: 1.5))),
          for (final c in app.children) ...[
            Material(
              color: Palette.surface,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20), side: const BorderSide(color: Palette.border)),
              child: InkWell(
                borderRadius: BorderRadius.circular(20),
                onTap: () async {
                  final err = await app.enterChild(c);
                  if (err != null && context.mounted) {
                    showToast(context, err);
                  }
                },
                child: Padding(
                  padding: const EdgeInsets.all(14),
                  child: Row(children: [
                    Avatar(c.initial, color: BandTheme.forGrade(c.grade).accent, size: 52, radius: 16),
                    const SizedBox(width: 16),
                    Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(c.nickname, style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 17)),
                      Text(gradeLabel(c.grade), style: const TextStyle(fontSize: 14, color: Palette.muted)),
                    ])),
                    const Icon(Icons.chevron_right_rounded, color: Palette.muted),
                  ]),
                ),
              ),
            ),
            const SizedBox(height: 12),
          ],
          const SizedBox(height: 20),
          PrimaryButton(
            label: 'Mode Orang Tua',
            icon: Icons.lock_outline_rounded,
            onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => const PinScreen())),
          ),
          const SizedBox(height: 12),
          const Text('Laporan dan pengaturan akun hanya terbuka dengan PIN orang tua.', textAlign: TextAlign.center, style: TextStyle(fontSize: 13, color: Palette.muted)),
        ]),
      ),
    );
  }
}

class PinScreen extends StatefulWidget {
  const PinScreen({super.key});

  @override
  State<PinScreen> createState() => _PinScreenState();
}

class _PinScreenState extends State<PinScreen> {
  String _pin = '';
  String? _error;
  bool _busy = false;

  Future<void> _press(String k) async {
    if (_busy) {
      return;
    }
    if (k == 'del') {
      setState(() {
        _pin = _pin.isEmpty ? '' : _pin.substring(0, _pin.length - 1);
        _error = null;
      });
      return;
    }
    if (_pin.length >= 6) {
      return;
    }
    setState(() {
      _pin += k;
      _error = null;
    });
  }

  Future<void> _submit() async {
    if (_pin.length < 4) {
      setState(() => _error = 'PIN minimal 4 angka.');
      return;
    }
    setState(() => _busy = true);
    final app = context.read<AppState>();
    final nav = Navigator.of(context);
    try {
      await app.unlockParent(_pin);
      nav.pop();
    } on ApiException catch (e) {
      setState(() {
        _error = e.message;
        _pin = '';
      });
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  Future<void> _forgot() async {
    final code = TextEditingController();
    final pin = TextEditingController();
    final pin2 = TextEditingController();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Buat PIN baru'),
        content: SingleChildScrollView(
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            const Text('Masukkan kode pemulihan yang disimpan saat pertama kali membuat PIN.'),
            const SizedBox(height: 12),
            TextField(controller: code, textCapitalization: TextCapitalization.characters, autocorrect: false, decoration: const InputDecoration(labelText: 'Kode pemulihan', hintText: 'XXXXX-XXXXX')),
            const SizedBox(height: 10),
            TextField(controller: pin, keyboardType: TextInputType.number, obscureText: true, maxLength: 6, decoration: const InputDecoration(labelText: 'PIN baru (4–6 angka)', counterText: '')),
            const SizedBox(height: 10),
            TextField(controller: pin2, keyboardType: TextInputType.number, obscureText: true, maxLength: 6, decoration: const InputDecoration(labelText: 'Ulangi PIN baru', counterText: '')),
          ]),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Batal')),
          FilledButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('Simpan')),
        ],
      ),
    );
    final c = code.text;
    final p = pin.text;
    final p2 = pin2.text;
    code.dispose();
    pin.dispose();
    pin2.dispose();
    if (ok != true || !mounted) {
      return;
    }
    if (p != p2) {
      setState(() => _error = 'Kedua PIN baru tidak sama.');
      return;
    }
    setState(() => _busy = true);
    final app = context.read<AppState>();
    try {
      final newCode = await app.resetPin(c, p);
      if (!mounted) {
        return;
      }
      await Navigator.of(context).push(MaterialPageRoute(builder: (ctx) => Scaffold(body: SafeArea(child: RecoveryCodeView(code: newCode, buttonLabel: 'Sudah disimpan', onDone: () => Navigator.of(ctx).pop())))));
      if (mounted) {
        setState(() {
          _error = null;
          _pin = '';
        });
        showToast(context, 'PIN baru tersimpan. Kode pemulihan lama tidak berlaku lagi.');
      }
    } on ApiException catch (err) {
      if (mounted) {
        setState(() => _error = err.message);
      }
    } finally {
      if (mounted) {
        setState(() => _busy = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    const keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'del', '0', 'ok'];
    return Scaffold(
      appBar: AppBar(backgroundColor: Palette.ground),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(24, 0, 24, 24),
          child: Column(children: [
            Expanded(
              child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
                Container(width: 64, height: 64, decoration: BoxDecoration(color: Palette.parentSoft, borderRadius: BorderRadius.circular(20)), child: const Icon(Icons.lock_outline_rounded, size: 30, color: Palette.parent)),
                const SizedBox(height: 14),
                const Text('Mode Orang Tua', style: TextStyle(fontSize: 24, fontWeight: FontWeight.w800)),
                const SizedBox(height: 6),
                const Text('Masukkan PIN untuk melanjutkan.', style: TextStyle(fontSize: 15, color: Palette.muted)),
                const SizedBox(height: 18),
                Semantics(
                  label: '${_pin.length} angka dimasukkan',
                  child: Row(mainAxisSize: MainAxisSize.min, children: List.generate(6, (i) => Container(
                        width: 14,
                        height: 14,
                        margin: const EdgeInsets.symmetric(horizontal: 7),
                        decoration: BoxDecoration(shape: BoxShape.circle, border: Border.all(color: i < 4 || i < _pin.length ? Palette.parent : Palette.borderStrong, width: 2), color: i < _pin.length ? Palette.parent : Colors.transparent),
                      ))),
                ),
                const SizedBox(height: 12),
                SizedBox(height: 22, child: _error == null ? null : Text(_error!, style: const TextStyle(color: Palette.bad, fontWeight: FontWeight.w700))),
              ]),
            ),
            TextButton(onPressed: _busy ? null : _forgot, child: const Text('Lupa PIN? Pakai kode pemulihan')),
            const SizedBox(height: 8),
            GridView.count(
              crossAxisCount: 3,
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              mainAxisSpacing: 12,
              crossAxisSpacing: 12,
              childAspectRatio: 1.8,
              children: [
                for (final k in keys)
                  k == 'ok'
                      ? FilledButton(
                          onPressed: _busy ? null : _submit,
                          style: FilledButton.styleFrom(backgroundColor: Palette.parent, shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18))),
                          child: _busy ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2.5, color: Colors.white)) : const Text('Buka', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 16)),
                        )
                      : OutlinedButton(
                          onPressed: () => _press(k),
                          style: OutlinedButton.styleFrom(
                            backgroundColor: k == 'del' ? Colors.transparent : Palette.surface,
                            foregroundColor: Palette.ink,
                            side: BorderSide(color: k == 'del' ? Colors.transparent : Palette.border),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
                          ),
                          child: k == 'del'
                              ? const Icon(Icons.backspace_outlined, semanticLabel: 'Hapus angka')
                              : Text(k, style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w700)),
                        ),
              ],
            ),
          ]),
        ),
      ),
    );
  }
}
