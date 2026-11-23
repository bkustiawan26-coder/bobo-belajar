import 'package:bobo_belajar/core/persona.dart';
import 'package:bobo_belajar/local/content.dart';
import 'package:bobo_belajar/local/engine.dart';
import 'package:bobo_belajar/local/store.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('teks ke ucapan', () {
    test('simbol matematika dibaca sebagai kata', () {
      expect(toSpoken('c² = a² + b²'), 'c kuadrat sama dengan a kuadrat tambah b kuadrat');
      expect(toSpoken('6 × 8 = 48'), '6 kali 8 sama dengan 48');
      expect(toSpoken('🍎 Apel ☀️ pagi'), 'Apel pagi');
      expect(toSpoken('a = 30 : 6 = 5'), 'a sama dengan 30 bagi 6 sama dengan 5');
      expect(toSpoken('MM : Mm : mm = 1 : 2 : 1'), contains('1 banding 2 banding 1'));
      expect(toSpoken('y = −3x + 7'), contains('negatif 3x tambah 7'));
      expect(toSpoken('5 − 3 = 2'), '5 kurang 3 sama dengan 2');
      expect(toSpoken('√144 = 12'), 'akar 144 sama dengan 12');
      expect(toSpoken('2⁵ = 32'), '2 pangkat 5 sama dengan 32');
      expect(toSpoken('3/4 bagian'), '3 per 4 bagian');
      expect(toSpoken('Biaya Rp1.500'), 'Biaya 1.500 rupiah');
      expect(toSpoken('a = 10 m/s²'), 'a sama dengan 10 meter per detik kuadrat');
      expect(toSpoken('Luasnya 6 cm²'), 'Luasnya 6 sentimeter persegi');
      expect(toSpoken('Kelas 1–9'), 'Kelas 1 sampai 9');
      expect(toSpoken('2 + 3 = …'), '2 tambah 3 sama dengan titik-titik');
      expect(toSpoken('Kata “bahwa” dipakai.'), 'Kata bahwa dipakai.');
    });

    test('kata berimbuhan tidak berubah', () {
      expect(toSpoken('paru-paru dan anak-anak'), 'paru-paru dan anak-anak');
      expect(toSpoken('Pilihan A: Benar.'), 'Pilihan A: Benar.');
    });

    test('pemenggalan kalimat utuh dan tidak memotong angka', () {
      const text = 'Hasilnya 0,7 dan 1.000. Lalu kita cek!\nc = 10';
      final segs = segmentsOf(text);
      expect(segs.join(), text);
      expect(segs.length, 3);
      expect(segs.first.trim(), 'Hasilnya 0,7 dan 1.000.');
    });
  });

  group('persona per jenjang', () {
    test('suara makin cepat dan netral untuk anak yang lebih besar', () {
      for (var g = 1; g < 9; g++) {
        expect(VoiceProfile.forGrade(g + 1).rate, greaterThanOrEqualTo(VoiceProfile.forGrade(g).rate));
        expect(VoiceProfile.forGrade(g + 1).pitch, lessThanOrEqualTo(VoiceProfile.forGrade(g).pitch));
        expect(VoiceProfile.forGrade(g + 1).pauseMs, lessThanOrEqualTo(VoiceProfile.forGrade(g).pauseMs));
      }
      expect(Persona.forGrade(1).breakMinutes, lessThan(Persona.forGrade(9).breakMinutes));
    });

    List<String> allLines(Persona p) => [
          for (var i = 0; i < 6; i++) ...[p.correct(i), p.wrong(i)],
          p.streak(),
          p.struggle(),
          p.summary(5, 5),
          p.summary(3, 5),
          p.summary(1, 5),
          p.lessonDone(),
          p.lessonIntro('Raka', 'Pecahan', 8),
          p.greeting('Raka', 8),
          p.homeNudge('Raka', 'Pecahan'),
          p.breakBody(20),
          for (final k in ['Penjelasan', 'Contoh', 'Ayo coba', 'Poin penting', 'Ringkasan']) p.blockIntro(k),
          ...p.cheers(),
          p.tryAgain(),
        ];

    test('memuji usaha dan strategi, bukan kecerdasan, dan tidak merendahkan', () {
      final banned = RegExp(r'\b(pintar|jenius|cerdas|bodoh|payah|malas|lambat)\b', caseSensitive: false);
      for (var g = 1; g <= 9; g++) {
        for (final line in allLines(Persona.forGrade(g))) {
          expect(banned.hasMatch(line), isFalse, reason: 'Kelas $g: $line');
          expect(line.trim(), isNotEmpty);
        }
      }
    });

    test('nada SMP tidak kekanak-kanakan, nada Kelas 1–2 hangat', () {
      final childish = RegExp(r'(yeay|yuk|hebat!|bareng|\bya\b)', caseSensitive: false);
      for (final line in allLines(Persona.forGrade(8))) {
        expect(childish.hasMatch(line), isFalse, reason: line);
      }
      expect(Persona.forGrade(1).lessonIntro('Nadia', 'Penjumlahan', 8), contains('Nadia'));
      expect(Persona.forGrade(1).blockLabel('Poin penting'), 'Ingat ini');
      expect(Persona.forGrade(8).blockLabel('Poin penting'), 'Poin penting');
    });

    test('umpan balik salah tidak menyalahkan anak', () {
      for (var g = 1; g <= 9; g++) {
        for (var i = 0; i < 6; i++) {
          final w = Persona.forGrade(g).wrong(i).toLowerCase();
          expect(w.contains('salah kamu') || w.startsWith('salah!'), isFalse);
          expect(w, anyOf(contains('belum'), contains('hampir'), contains('ups')));
        }
      }
    });
  });

  test('profil Kelas 1–2 otomatis dibacakan, kelas lain tidak', () async {
    final content = Content({'format': 1, 'includes_sample': true, 'subjects': [], 'chapters': [], 'topics': [], 'prerequisites': [], 'lessons': [], 'questions': [], 'assessment_templates': [], 'assessments': []});
    final e = LocalEngine(MemoryStore(), content);
    final small = Map<String, dynamic>.from(await e.parent('POST', '/parent/children', body: {'nickname': 'Nadia', 'grade': 1}) as Map);
    final big = Map<String, dynamic>.from(await e.parent('POST', '/parent/children', body: {'nickname': 'Raka', 'grade': 7}) as Map);
    expect((small['settings'] as Map)['read_aloud'], isTrue);
    expect((big['settings'] as Map)['read_aloud'], isFalse);
  });
}
