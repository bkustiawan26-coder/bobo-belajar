import 'package:flutter/material.dart';

import '../core/api.dart';
import '../core/theme.dart';

class AppCard extends StatelessWidget {
  const AppCard({super.key, required this.child, this.padding = const EdgeInsets.all(16), this.radius = 18, this.color = Palette.surface, this.borderColor = Palette.border});

  final Widget child;
  final EdgeInsetsGeometry padding;
  final double radius;
  final Color color;
  final Color borderColor;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: padding,
      decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(radius), border: Border.all(color: borderColor)),
      child: child,
    );
  }
}

class PrimaryButton extends StatelessWidget {
  const PrimaryButton({super.key, required this.label, required this.onPressed, this.color = Palette.parent, this.radius = 14, this.icon, this.busy = false, this.height = 52});

  final String label;
  final VoidCallback? onPressed;
  final Color color;
  final double radius;
  final IconData? icon;
  final bool busy;
  final double height;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: height,
      width: double.infinity,
      child: FilledButton(
        onPressed: busy ? null : onPressed,
        style: FilledButton.styleFrom(
          backgroundColor: color,
          foregroundColor: Colors.white,
          disabledBackgroundColor: const Color(0xFFE2E8F0),
          disabledForegroundColor: Palette.muted,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(radius)),
          textStyle: const TextStyle(fontFamily: 'PlusJakartaSans', fontWeight: FontWeight.w800, fontSize: 15),
        ),
        child: busy
            ? const SizedBox(width: 22, height: 22, child: CircularProgressIndicator(strokeWidth: 2.5, color: Palette.muted))
            : Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                if (icon != null) ...[Icon(icon, size: 20), const SizedBox(width: 8)],
                Flexible(child: Text(label, textAlign: TextAlign.center)),
              ]),
      ),
    );
  }
}

class SecondaryButton extends StatelessWidget {
  const SecondaryButton({super.key, required this.label, required this.onPressed, this.radius = 14, this.height = 50, this.foreground = Palette.ink, this.icon});

  final String label;
  final VoidCallback? onPressed;
  final double radius;
  final double height;
  final Color foreground;
  final IconData? icon;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: height,
      width: double.infinity,
      child: OutlinedButton(
        onPressed: onPressed,
        style: OutlinedButton.styleFrom(
          foregroundColor: foreground,
          backgroundColor: Palette.surface,
          side: const BorderSide(color: Palette.borderStrong),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(radius)),
          textStyle: const TextStyle(fontFamily: 'PlusJakartaSans', fontWeight: FontWeight.w700, fontSize: 15),
        ),
        child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          if (icon != null) ...[Icon(icon, size: 18), const SizedBox(width: 8)],
          Flexible(child: Text(label, textAlign: TextAlign.center)),
        ]),
      ),
    );
  }
}

class Tag extends StatelessWidget {
  const Tag(this.text, {super.key, this.fg = Palette.inkSoft, this.bg = Palette.neutralSoft, this.size = 12});

  final String text;
  final Color fg;
  final Color bg;
  final double size;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(6)),
      child: Text(text, style: TextStyle(color: fg, fontSize: size, fontWeight: FontWeight.w700)),
    );
  }
}

class Avatar extends StatelessWidget {
  const Avatar(this.initial, {super.key, required this.color, this.size = 44, this.radius = 14});

  final String initial;
  final Color color;
  final double size;
  final double radius;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      alignment: Alignment.center,
      decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(radius)),
      child: Text(initial, style: TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: size * 0.42)),
    );
  }
}

class SectionTitle extends StatelessWidget {
  const SectionTitle(this.text, {super.key});

  final String text;

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.only(bottom: 10),
        child: Text(text, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
      );
}

class EmptyState extends StatelessWidget {
  const EmptyState({super.key, required this.icon, required this.title, required this.body, this.action, this.iconColor = Palette.muted});

  final IconData icon;
  final String title;
  final String body;
  final Widget? action;
  final Color iconColor;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 40),
      child: Column(mainAxisSize: MainAxisSize.min, children: [
        Icon(icon, size: 56, color: iconColor),
        const SizedBox(height: 12),
        Text(title, textAlign: TextAlign.center, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
        const SizedBox(height: 8),
        Text(body, textAlign: TextAlign.center, style: const TextStyle(fontSize: 14, color: Palette.muted, height: 1.5)),
        if (action != null) ...[const SizedBox(height: 16), action!],
      ]),
    );
  }
}

class Notice extends StatelessWidget {
  const Notice(this.text, {super.key, this.fg = Palette.warnInk, this.bg = Palette.warnSoft});

  final String text;
  final Color fg;
  final Color bg;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(12)),
      child: Text(text, style: TextStyle(color: fg, fontSize: 13, fontWeight: FontWeight.w600, height: 1.45)),
    );
  }
}

class OfflineBanner extends StatelessWidget {
  const OfflineBanner({super.key, required this.pending});

  final int pending;

  @override
  Widget build(BuildContext context) {
    return Semantics(
      liveRegion: true,
      child: Container(
        width: double.infinity,
        color: const Color(0xFF1E293B),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        child: Row(children: [
          const Icon(Icons.wifi_off_rounded, color: Colors.white, size: 16),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              pending > 0 ? 'Offline · $pending jawaban menunggu sinkron' : 'Offline · materi yang sudah diunduh tetap bisa dibuka',
              style: const TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w600),
            ),
          ),
        ]),
      ),
    );
  }
}

class MasteryChip extends StatelessWidget {
  const MasteryChip({super.key, required this.state, required this.label});

  final String state;
  final String label;

  @override
  Widget build(BuildContext context) {
    final (fg, bg, mark) = switch (state) {
      'demonstrated' => (Palette.okInk, Palette.okSoft, '✓'),
      'developing' => (Palette.devInk, Palette.devSoft, '+'),
      'insufficient' => (Palette.warnInk, Palette.warnSoft, '?'),
      _ => (Palette.inkSoft, Palette.neutralSoft, '–'),
    };
    return Tag('$mark $label', fg: fg, bg: bg);
  }
}

class LoadingView extends StatelessWidget {
  const LoadingView({super.key});

  @override
  Widget build(BuildContext context) => const Center(child: Padding(padding: EdgeInsets.all(32), child: CircularProgressIndicator()));
}

class ErrorView extends StatelessWidget {
  const ErrorView({super.key, required this.error, required this.onRetry});

  final Object error;
  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    final offline = error is ApiException && (error as ApiException).isOffline;
    return EmptyState(
      icon: offline ? Icons.wifi_off_rounded : Icons.error_outline_rounded,
      title: offline ? 'Tidak ada koneksi' : 'Gagal memuat',
      body: error.toString(),
      action: SizedBox(width: 200, child: SecondaryButton(label: 'Coba lagi', onPressed: onRetry)),
    );
  }
}

void showToast(BuildContext context, String message) {
  ScaffoldMessenger.of(context)
    ..hideCurrentSnackBar()
    ..showSnackBar(SnackBar(content: Text(message), behavior: SnackBarBehavior.floating, backgroundColor: Palette.ink));
}

class BoboLogo extends StatelessWidget {
  const BoboLogo({super.key, this.size = 48, this.color = const Color(0xFF1E3A8A), this.smile = const Color(0xFFFDBA74)});

  final double size;
  final Color color;
  final Color smile;

  @override
  Widget build(BuildContext context) => ExcludeSemantics(child: CustomPaint(size: Size.square(size), painter: _LogoPainter(color, smile)));
}

class _LogoPainter extends CustomPainter {
  _LogoPainter(this.color, this.smile);

  final Color color;
  final Color smile;

  @override
  void paint(Canvas canvas, Size size) {
    final s = size.width / 48;
    canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(2 * s, 2 * s, 44 * s, 44 * s), Radius.circular(14 * s)), Paint()..color = color);
    final white = Paint()..color = Colors.white;
    final dark = Paint()..color = Palette.ink;
    canvas.drawCircle(Offset(17 * s, 21 * s), 4.5 * s, white);
    canvas.drawCircle(Offset(31 * s, 21 * s), 4.5 * s, white);
    canvas.drawCircle(Offset(18 * s, 22 * s), 2 * s, dark);
    canvas.drawCircle(Offset(32 * s, 22 * s), 2 * s, dark);
    final path = Path()
      ..moveTo(17 * s, 31 * s)
      ..quadraticBezierTo(24 * s, 37 * s, 31 * s, 31 * s);
    canvas.drawPath(path, Paint()
      ..color = smile
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3 * s
      ..strokeCap = StrokeCap.round);
  }

  @override
  bool shouldRepaint(covariant _LogoPainter old) => old.color != color || old.smile != smile;
}

const double kRailBreakpoint = 720;
const double kContentMaxWidth = 920;
const double kFormMaxWidth = 560;

bool useRail(BuildContext context) => MediaQuery.sizeOf(context).width >= kRailBreakpoint;

bool isTabletSize(Size logical) => logical.shortestSide >= 600;

int gridColumns(double width, {double cell = 210, int min = 2, int max = 4}) {
  final n = (width / cell).floor();
  return n < min ? min : (n > max ? max : n);
}

double bubbleMaxWidth(BuildContext context, double fraction) {
  final w = MediaQuery.sizeOf(context).width * fraction;
  return w > 620 ? 620 : w;
}

class ContentWidth extends StatelessWidget {
  const ContentWidth({super.key, required this.child, this.maxWidth = kContentMaxWidth});

  final Widget child;
  final double maxWidth;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(builder: (context, box) {
      final w = box.maxWidth.isFinite && box.maxWidth < maxWidth ? box.maxWidth : maxWidth;
      return Align(
        alignment: Alignment.topCenter,
        child: SizedBox(width: w, height: box.maxHeight.isFinite ? box.maxHeight : null, child: child),
      );
    });
  }
}

class AdaptiveGrid extends StatelessWidget {
  const AdaptiveGrid({super.key, required this.children, this.cell = 210, this.min = 2, this.max = 4, this.aspect = 1.35, this.spacing = 12});

  final List<Widget> children;
  final double cell;
  final int min;
  final int max;
  final double aspect;
  final double spacing;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(builder: (context, box) {
      final width = box.maxWidth.isFinite ? box.maxWidth : MediaQuery.sizeOf(context).width;
      return GridView.count(
        crossAxisCount: gridColumns(width, cell: cell, min: min, max: max),
        shrinkWrap: true,
        physics: const NeverScrollableScrollPhysics(),
        mainAxisSpacing: spacing,
        crossAxisSpacing: spacing,
        childAspectRatio: aspect,
        children: children,
      );
    });
  }
}
