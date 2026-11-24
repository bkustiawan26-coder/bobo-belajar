import 'package:bobo_belajar/local/tutor.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('tutor menjawab pertanyaan huruf hijaiyah', () {
    final a = hijaiyahAnswer('huruf tsa')!;
    expect(a, contains('ث'));
    expect(a, contains('tiga titik di atas'));
    expect(a, contains('tsa, tsi, tsu'));
    expect(hijaiyahAnswer('huruf ya')!, contains('ي'));
    expect(hijaiyahAnswer('apa itu huruf hijaiyah ya?'), isNull);
    expect(hijaiyahAnswer('apa itu bilangan 1 sampai 10?'), isNull);
    expect(hijaiyahAnswer('huruf hijaiyah apa saja?')!, contains('29'));
  });

  test('jawaban tutor memilih kalimat yang relevan tanpa judul', () {
    final s = sentencesOf("Mengenal huruf hijaiyah\n\nPenjelasan: Al-Qur'an ditulis dengan huruf hijaiyah. Huruf tsa punya tiga titik di atas.", title: 'Mengenal huruf hijaiyah');
    expect(s.first, startsWith("Al-Qur'an"));
    expect(relevantSentences(s, 'titik tsa', 1), ['Huruf tsa punya tiga titik di atas.']);
  });
}
