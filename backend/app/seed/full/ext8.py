TOPICS = ""
BANK = ""
SAS = ""

TOPICS += """
## MAT
# 1|Aljabar, Fungsi, dan Lingkaran
@ Koordinat Kartesius
min: 15
act: Gambar denah kamarmu di kertas berpetak, lalu tentukan koordinat letak meja, lemari, dan pintu.
mis: menukar urutan x dan y saat menulis koordinat
exp: Bidang Kartesius dibentuk oleh sumbu X mendatar dan sumbu Y tegak yang berpotongan di titik asal O(0, 0). Letak titik ditulis (x, y), dengan x jarak mendatar dan y jarak tegak. Bidang Kartesius terbagi menjadi empat kuadran. Kuadran I berisi titik dengan x positif dan y positif.
ex: Titik A(3, 2) berada di kuadran I. // Titik B(-4, 1) berada di kuadran II.
pt: Sumbu X dan sumbu Y ; Titik ditulis (x, y) ; Empat kuadran
sum: Koordinat menunjukkan letak titik secara tepat.
fig: table Titik | Letak ;; (3, 2) | kuadran I ;; (-4, 1) | kuadran II ;; (-2, -5) | kuadran III ;; (6, -3) | kuadran IV ;; (0, 0) | titik asal ;; (0, 4) | pada sumbu Y ~ Letak titik pada bidang Kartesius.
@ Faktorisasi bentuk aljabar
min: 15
act: Faktorkan x² + 5x + 6 dengan mencari dua bilangan yang hasil kalinya 6 dan jumlahnya 5.
mis: mencari dua bilangan yang jumlahnya c dan hasil kalinya b
exp: Faktorisasi adalah mengubah bentuk aljabar menjadi perkalian faktor-faktornya. Bentuk ax + ay difaktorkan menjadi a(x + y). Bentuk x² + bx + c difaktorkan dengan mencari dua bilangan p dan q yang hasil kalinya c dan jumlahnya b, sehingga menjadi (x + p)(x + q). Selisih dua kuadrat x² - y² = (x + y)(x - y).
ex: x² + 5x + 6 = (x + 2)(x + 3). // x² - 9 = (x + 3)(x - 3).
pt: ax + ay = a(x + y) ; x² + bx + c: cari p × q = c dan p + q = b ; Selisih dua kuadrat
sum: Faktorisasi memudahkan penyederhanaan bentuk aljabar.
fig: table Bentuk aljabar | Faktorisasi ;; 2x + 6 | 2(x + 3) ;; x² + 5x + 6 | (x + 2)(x + 3) ;; x² - 9 | (x + 3)(x - 3) ;; x² + 7x + 10 | (x + 2)(x + 5) ;; x² - 4x | x(x - 4) ;; x² - 1 | (x + 1)(x - 1) ~ Contoh faktorisasi.
@ Korespondensi satu-satu
min: 15
act: Pasangkan anggota keluarga dengan nomor kursinya di meja makan, lalu periksa apakah termasuk korespondensi satu-satu.
mis: mengira setiap fungsi adalah korespondensi satu-satu
exp: Korespondensi satu-satu adalah fungsi yang memasangkan setiap anggota himpunan A tepat dengan satu anggota himpunan B, dan sebaliknya setiap anggota B tepat berpasangan dengan satu anggota A. Syaratnya banyak anggota A sama dengan banyak anggota B. Jika n(A) = n(B) = n, banyak korespondensi satu-satu yang mungkin adalah n! atau n faktorial.
ex: Negara dan ibu kotanya adalah korespondensi satu-satu. // Jika n = 3, banyak korespondensi satu-satu = 3 × 2 × 1 = 6.
pt: Setiap anggota A tepat satu pasangan di B ; n(A) = n(B) ; Banyaknya n!
sum: Korespondensi satu-satu adalah pemasangan yang adil dua arah.
fig: table Banyak anggota | Banyak korespondensi satu-satu ;; 1 | 1 ;; 2 | 2 ;; 3 | 6 ;; 4 | 24 ;; 5 | 120 ;; 6 | 720 ~ Banyak korespondensi satu-satu.
@ Grafik fungsi linear
min: 15
act: Buat tabel nilai f(x) = 2x + 1 untuk x = 0 sampai 4, lalu gambar grafiknya di kertas berpetak.
mis: menghubungkan titik-titik fungsi linear dengan garis lengkung
exp: Fungsi linear berbentuk f(x) = mx + c. Grafiknya berupa garis lurus. Cara menggambarnya adalah membuat tabel nilai x dan f(x), menempatkan pasangan titik pada bidang Kartesius, lalu menghubungkannya dengan garis lurus. Nilai c menunjukkan titik potong dengan sumbu Y.
ex: f(x) = 2x + 1 memotong sumbu Y di (0, 1). // f(3) = 2(3) + 1 = 7.
pt: Bentuk f(x) = mx + c ; Grafik garis lurus ; c titik potong sumbu Y
sum: Grafik fungsi linear selalu berupa garis lurus.
fig: table x | f(x) = 2x + 1 ;; 0 | 1 ;; 1 | 3 ;; 2 | 5 ;; 3 | 7 ;; 4 | 9 ;; 5 | 11 ~ Tabel nilai fungsi linear.
@ Unsur-unsur lingkaran
min: 15
act: Gambar lingkaran dengan jangka, lalu beri nama titik pusat, jari-jari, diameter, tali busur, dan juring.
mis: menganggap tali busur selalu melalui titik pusat
exp: Lingkaran adalah kumpulan titik yang berjarak sama dari titik pusat. Unsur lingkaran meliputi titik pusat, jari-jari, diameter, tali busur, busur, apotema, juring, dan tembereng. Diameter adalah tali busur terpanjang yang melalui titik pusat, panjangnya dua kali jari-jari.
ex: Jari-jari 7 cm maka diameter 14 cm. // Juring berbentuk seperti potongan pizza.
pt: Titik berjarak sama dari pusat ; Diameter = 2 × jari-jari ; Juring dan tembereng
sum: Mengenal unsur lingkaran adalah dasar menghitung lingkaran.
fig: table Unsur | Pengertian ;; jari-jari | jarak pusat ke lingkaran ;; diameter | tali busur melalui pusat ;; tali busur | ruas garis menghubungkan dua titik lingkaran ;; busur | bagian lengkung lingkaran ;; juring | daerah antara dua jari-jari dan busur ;; tembereng | daerah antara tali busur dan busur ~ Unsur-unsur lingkaran.
@ Keliling dan luas lingkaran
min: 15
act: Ukur keliling tutup toples dengan benang, lalu bandingkan dengan hasil rumus 2πr.
mis: memakai rumus luas untuk menghitung keliling
exp: Keliling lingkaran adalah panjang garis lengkung lingkaran, dihitung dengan K = 2πr atau K = πd. Luas lingkaran dihitung dengan L = πr². Nilai π sekitar 3,14 atau 22/7. Gunakan 22/7 jika jari-jari kelipatan 7.
ex: r = 7 cm, K = 2 × 22/7 × 7 = 44 cm. // r = 10 cm, L = 3,14 × 100 = 314 cm².
pt: K = 2πr = πd ; L = πr² ; π ≈ 3,14 atau 22/7
sum: Keliling dan luas lingkaran bergantung pada jari-jari.
fig: table Jari-jari | Luas lingkaran ;; 7 cm | 154 cm² ;; 14 cm | 616 cm² ;; 10 cm | 314 cm² ;; 20 cm | 1.256 cm² ;; 21 cm | 1.386 cm² ;; 35 cm | 3.850 cm² ~ Luas lingkaran untuk beberapa jari-jari.
# 2|Barisan, Garis, dan Bangun Ruang
@ Barisan aritmetika
min: 15
act: Catat tabunganmu yang bertambah tetap setiap minggu, lalu tentukan suku ke-10.
mis: mengira beda barisan selalu bilangan positif
exp: Barisan aritmetika adalah barisan bilangan yang selisih dua suku berurutannya tetap. Selisih itu disebut beda (b). Rumus suku ke-n adalah Un = a + (n - 1)b, dengan a suku pertama. Beda dapat positif atau negatif.
ex: 3, 7, 11, 15 memiliki b = 4. // Barisan 20, 17, 14 memiliki b = -3.
pt: Selisih suku berurutan tetap ; Beda dilambangkan b ; Un = a + (n - 1)b
sum: Rumus suku ke-n memudahkan mencari suku jauh.
fig: table Barisan | Beda ;; 3, 7, 11, 15 | 4 ;; 2, 4, 6, 8 | 2 ;; 20, 17, 14, 11 | -3 ;; 5, 10, 15, 20 | 5 ;; 1, 8, 15, 22 | 7 ;; 50, 40, 30, 20 | -10 ~ Barisan aritmetika dan bedanya.
@ Garis sejajar dan tegak lurus
min: 15
act: Cari dua garis sejajar dan dua garis tegak lurus di ruang kelas, lalu gambarkan.
mis: mengira dua garis tegak lurus memiliki gradien sama
exp: Dua garis sejajar memiliki gradien yang sama, m1 = m2. Dua garis tegak lurus memiliki hasil kali gradien -1, yaitu m1 × m2 = -1. Jadi, jika gradien suatu garis 2, gradien garis yang tegak lurus dengannya adalah -1/2.
ex: y = 3x + 1 sejajar y = 3x - 5. // Garis bergradien 2 tegak lurus garis bergradien -1/2.
pt: Sejajar: m1 = m2 ; Tegak lurus: m1 × m2 = -1 ; Gradien tegak lurus adalah lawan kebalikan
sum: Gradien menentukan hubungan dua garis.
fig: table Gradien garis | Gradien garis tegak lurus ;; 2 | -1/2 ;; 3 | -1/3 ;; -4 | 1/4 ;; 1/2 | -2 ;; -1 | 1 ;; 5 | -1/5 ~ Gradien garis tegak lurus.
@ Kubus dan balok
min: 15
act: Ukur sebuah kardus, lalu hitung luas permukaan dan volumenya.
mis: menjumlahkan panjang, lebar, dan tinggi untuk mencari volume
exp: Kubus memiliki 6 sisi persegi yang sama, 12 rusuk, dan 8 titik sudut. Balok memiliki 6 sisi persegi panjang. Volume kubus V = s³ dan luas permukaannya 6s². Volume balok V = p × l × t dan luas permukaannya 2(pl + pt + lt).
ex: Kubus s = 4 cm, V = 64 cm³. // Balok 5 × 3 × 2 cm, V = 30 cm³.
pt: Kubus V = s³ ; Balok V = p × l × t ; Luas permukaan jumlah luas semua sisi
sum: Volume menunjukkan isi bangun ruang.
fig: table Ukuran kubus | Volume ;; s = 2 cm | 8 cm³ ;; s = 3 cm | 27 cm³ ;; s = 4 cm | 64 cm³ ;; s = 5 cm | 125 cm³ ;; s = 6 cm | 216 cm³ ;; s = 10 cm | 1.000 cm³ ~ Volume kubus.
@ Prisma dan limas
min: 15
act: Buat jaring-jaring prisma segitiga dari karton, lalu rakit menjadi bangun ruang.
mis: lupa mengalikan sepertiga pada volume limas
exp: Prisma adalah bangun ruang dengan alas dan tutup kongruen serta sisi tegak berbentuk persegi panjang. Limas memiliki satu alas dan sisi tegak berbentuk segitiga yang bertemu di puncak. Volume prisma = luas alas × tinggi. Volume limas = 1/3 × luas alas × tinggi.
ex: Prisma alas 12 cm², tinggi 10 cm, V = 120 cm³. // Limas alas 36 cm², tinggi 5 cm, V = 60 cm³.
pt: Prisma: alas dan tutup kongruen ; Limas: sisi tegak segitiga ; Volume limas sepertiga prisma
sum: Volume limas sepertiga volume prisma beralas dan bertinggi sama.
fig: table Bangun ruang | Banyak titik sudut ;; prisma segitiga | 6 ;; prisma segiempat | 8 ;; prisma segilima | 10 ;; limas segitiga | 4 ;; limas segiempat | 5 ;; limas segienam | 7 ~ Banyak titik sudut prisma dan limas.
@ Tabel distribusi frekuensi
min: 15
act: Data nomor sepatu teman sekelas, lalu susun dalam tabel frekuensi dengan turus.
mis: lupa menghitung data yang muncul berulang
exp: Tabel distribusi frekuensi menyajikan data beserta banyak kemunculannya. Langkahnya mengurutkan data, membuat turus atau tally, lalu menghitung frekuensi. Jumlah semua frekuensi sama dengan banyak data. Data yang frekuensinya paling besar disebut modus.
ex: Nilai 8 muncul 5 kali maka frekuensinya 5. // Jumlah frekuensi 30 berarti ada 30 data.
pt: Data dan banyak kemunculannya ; Memakai turus ; Jumlah frekuensi = banyak data
sum: Tabel frekuensi membuat data mudah dibaca.
fig: table Nomor sepatu | Frekuensi ;; 36 | 3 ;; 37 | 5 ;; 38 | 8 ;; 39 | 6 ;; 40 | 4 ;; 41 | 2 ~ Tabel frekuensi nomor sepatu.
@ Sudut pusat dan sudut keliling
min: 15
act: Gambar lingkaran, buat sudut pusat dan sudut keliling yang menghadap busur sama, lalu ukur dengan busur derajat.
mis: mengira sudut keliling sama besar dengan sudut pusat
exp: Sudut pusat adalah sudut yang titik sudutnya di pusat lingkaran. Sudut keliling adalah sudut yang titik sudutnya pada lingkaran. Jika menghadap busur yang sama, besar sudut pusat dua kali sudut keliling. Sudut keliling yang menghadap diameter besarnya 90 derajat.
ex: Sudut pusat 80° maka sudut keliling 40°. // Sudut keliling menghadap diameter = 90°.
pt: Sudut pusat di titik pusat ; Sudut keliling pada lingkaran ; Sudut pusat = 2 × sudut keliling
sum: Hubungan sudut pusat dan keliling memudahkan perhitungan.
fig: table Sudut pusat | Sudut keliling ;; 60° | 30° ;; 80° | 40° ;; 100° | 50° ;; 120° | 60° ;; 180° | 90° ;; 140° | 70° ~ Sudut pusat dan sudut keliling.
"""

BANK += """
## MAT|Koordinat Kartesius
Titik (-4, 1) terletak di kuadran …|II|I|III|IV|x negatif, y positif.
Titik (6, -3) terletak di kuadran …|IV|I|II|III|x positif, y negatif.
=|Titik potong sumbu X dan sumbu Y disebut titik …|asal|Titik asal O(0, 0).
=|Titik (2, 5) berjarak … satuan dari sumbu X.|5|Nilai y.
B|Titik (0, 4) terletak pada sumbu Y.|x = 0.
S|Pada koordinat (x, y), nilai y ditulis lebih dulu.|x dulu.
Titik (-2, -5) terletak di kuadran …|III|I|II|IV|Keduanya negatif.
Titik A(3, 2) digeser 2 satuan ke kanan menjadi …|(5, 2)|(3, 4)|(1, 2)|(5, 4)|x + 2.
## MAT|Faktorisasi bentuk aljabar
Faktorisasi dari x² + 5x + 6 adalah …|(x + 2)(x + 3)|(x + 1)(x + 6)|(x - 2)(x - 3)|(x + 5)(x + 1)|2 × 3 = 6, 2 + 3 = 5.
Faktorisasi dari x² - 9 adalah …|(x + 3)(x - 3)|(x - 3)²|(x + 9)(x - 1)|(x + 3)²|Selisih dua kuadrat.
=|Faktorisasi dari 2x + 6 adalah 2(x + …)|3|2(x + 3).
=|Faktorisasi x² - 4x adalah x(x - …)|4|x(x - 4).
B|x² - 1 = (x + 1)(x - 1).|Selisih kuadrat.
S|x² + 7x + 10 = (x + 3)(x + 4).|(x + 2)(x + 5).
Faktorisasi dari x² + 7x + 12 adalah …|(x + 3)(x + 4)|(x + 2)(x + 6)|(x + 1)(x + 12)|(x - 3)(x - 4)|3 × 4 = 12.
Faktorisasi dari 3x² + 6x adalah …|3x(x + 2)|3(x² + 6x)|x(3x + 2)|6x(x + 1)|FPB 3x.
## MAT|Korespondensi satu-satu
Syarat korespondensi satu-satu adalah banyak anggota A … banyak anggota B.|sama dengan|lebih dari|kurang dari|dua kali|n(A) = n(B).
Banyak korespondensi satu-satu dari dua himpunan masing-masing 3 anggota adalah …|6|3|9|27|3! = 6.
=|Banyak korespondensi satu-satu jika n = 4 adalah …|24|4! = 24.
=|Banyak korespondensi satu-satu jika n = 5 adalah …|120|5! = 120.
B|Negara dan ibu kotanya merupakan korespondensi satu-satu.|Satu pasangan.
S|Setiap fungsi pasti korespondensi satu-satu.|Belum tentu.
Contoh korespondensi satu-satu adalah …|siswa dan nomor absen|siswa dan golongan darah|kota dan provinsi|hewan dan warnanya|Unik dua arah.
n! dengan n = 2 bernilai …|2|1|4|0|2 × 1.
## MAT|Grafik fungsi linear
Grafik fungsi linear berbentuk …|garis lurus|garis lengkung|lingkaran|parabola|Lurus.
Jika f(x) = 2x + 1, maka f(3) = …|7|6|5|9|2(3) + 1.
=|Fungsi f(x) = 2x + 1 memotong sumbu Y di titik (0, …)|1|c = 1.
=|Jika f(x) = 3x - 2, maka f(4) = …|10|12 - 2.
B|Bentuk umum fungsi linear adalah f(x) = mx + c.|Bentuk.
S|Titik-titik fungsi linear dihubungkan dengan garis lengkung.|Lurus.
Jika f(x) = 2x + 1 dan f(a) = 9, maka a = …|4|5|3|8|2a = 8.
Fungsi f(x) = 5 - x untuk x = 2 bernilai …|3|7|-3|10|5 - 2.
## MAT|Unsur-unsur lingkaran
Tali busur terpanjang yang melalui titik pusat disebut …|diameter|jari-jari|apotema|busur|Diameter.
Jika jari-jari 7 cm, maka diameternya …|14 cm|7 cm|3,5 cm|21 cm|2 × 7.
=|Daerah antara dua jari-jari dan busur disebut …|juring|Juring.
=|Daerah antara tali busur dan busur disebut …|tembereng|Tembereng.
B|Busur adalah bagian lengkung lingkaran.|Busur.
S|Setiap tali busur pasti melalui titik pusat.|Hanya diameter.
Jarak terpendek titik pusat ke tali busur disebut …|apotema|juring|diameter|tembereng|Apotema.
Jika diameter 20 cm, jari-jarinya …|10 cm|20 cm|40 cm|5 cm|20 : 2.
## MAT|Keliling dan luas lingkaran
Rumus luas lingkaran adalah …|πr²|2πr|πd|2πr²|L = πr².
Keliling lingkaran berjari-jari 7 cm dengan π = 22/7 adalah …|44 cm|22 cm|154 cm|88 cm|2 × 22/7 × 7.
=|Luas lingkaran berjari-jari 7 cm dengan π = 22/7 adalah … cm².|154|22/7 × 49.
=|Luas lingkaran berjari-jari 10 cm dengan π = 3,14 adalah … cm².|314|3,14 × 100.
B|Keliling lingkaran dapat dihitung dengan πd.|K = πd.
S|Rumus keliling lingkaran adalah πr².|2πr.
Keliling lingkaran berdiameter 10 cm dengan π = 3,14 adalah …|31,4 cm|314 cm|62,8 cm|15,7 cm|3,14 × 10.
Luas lingkaran berjari-jari 14 cm dengan π = 22/7 adalah …|616 cm²|88 cm²|154 cm²|308 cm²|22/7 × 196.
## MAT|Barisan aritmetika
Beda barisan 3, 7, 11, 15 adalah …|4|3|7|11|7 - 3.
Suku ke-10 barisan 3, 7, 11, … adalah …|39|40|43|37|3 + 9 × 4.
=|Beda barisan 20, 17, 14, 11 adalah …|-3|Turun 3.
=|Suku berikutnya dari 5, 10, 15, 20 adalah …|25|b = 5.
B|Rumus suku ke-n barisan aritmetika adalah a + (n - 1)b.|Un.
S|Beda barisan aritmetika selalu positif.|Bisa negatif.
Suku ke-6 barisan 2, 4, 6, … adalah …|12|10|14|16|2 + 5 × 2.
Barisan 50, 40, 30, 20 memiliki beda …|-10|10|20|-20|Turun 10.
## MAT|Garis sejajar dan tegak lurus
Dua garis sejajar memiliki gradien yang …|sama|berlawanan|berkebalikan|nol|m1 = m2.
Gradien garis yang tegak lurus dengan garis bergradien 2 adalah …|-1/2|2|1/2|-2|m1 × m2 = -1.
=|Hasil kali gradien dua garis tegak lurus adalah …|-1|-1.
=|Gradien garis yang sejajar y = 3x + 1 adalah …|3|Sama.
B|Garis y = 3x + 1 sejajar dengan y = 3x - 5.|Gradien sama.
S|Dua garis tegak lurus memiliki gradien yang sama.|Hasil kali -1.
Gradien garis tegak lurus terhadap garis bergradien -4 adalah …|1/4|-1/4|4|-4|-1 : -4.
Gradien garis tegak lurus terhadap garis bergradien 1/2 adalah …|-2|2|1/2|-1/2|Lawan kebalikan.
## MAT|Kubus dan balok
Volume kubus bersisi 4 cm adalah …|64 cm³|16 cm³|48 cm³|96 cm³|4³.
Volume balok 5 cm × 3 cm × 2 cm adalah …|30 cm³|10 cm³|62 cm³|25 cm³|5 × 3 × 2.
=|Banyak rusuk kubus adalah …|12|12.
=|Luas permukaan kubus bersisi 3 cm adalah … cm².|54|6 × 9.
B|Kubus memiliki 8 titik sudut.|8.
S|Volume balok dihitung dengan p + l + t.|Dikali.
Luas permukaan balok 4 × 3 × 2 cm adalah …|52 cm²|24 cm²|26 cm²|48 cm²|2(12 + 8 + 6).
Volume kubus bersisi 10 cm adalah …|1.000 cm³|100 cm³|600 cm³|30 cm³|10³.
## MAT|Prisma dan limas
Volume limas = 1/3 × luas alas × …|tinggi|keliling|panjang rusuk|jari-jari|Tinggi.
Sisi tegak limas berbentuk …|segitiga|persegi panjang|lingkaran|trapesium|Segitiga.
=|Banyak sisi prisma segitiga adalah …|5|5.
=|Banyak sisi limas segitiga adalah …|4|4.
B|Volume prisma = luas alas × tinggi.|Prisma.
S|Sisi tegak prisma berbentuk segitiga.|Persegi panjang.
Volume limas dengan luas alas 36 cm² dan tinggi 5 cm adalah …|60 cm³|180 cm³|41 cm³|90 cm³|1/3 × 180.
Volume prisma dengan luas alas 12 cm² dan tinggi 10 cm adalah …|120 cm³|40 cm³|22 cm³|1.200 cm³|12 × 10.
## MAT|Tabel distribusi frekuensi
Tanda garis untuk mencatat data disebut …|turus|modus|median|rentang|Turus.
Jumlah semua frekuensi sama dengan …|banyak data|data terbesar|rata-rata|modus|Banyak data.
=|Data dengan frekuensi terbesar disebut …|modus|Modus.
=|Jika nilai 8 muncul 5 kali, frekuensinya …|5|5.
B|Data perlu diurutkan sebelum dibuat tabel frekuensi.|Urutkan.
S|Data yang muncul berulang cukup dihitung sekali.|Semua dihitung.
Pada tabel nomor sepatu 36 (3), 37 (5), 38 (8), modusnya …|38|36|37|8|Frekuensi 8.
Frekuensi 3, 5, 8, 6, 4, 2 berarti banyak data …|28|8|6|30|Jumlah frekuensi.
## MAT|Sudut pusat dan sudut keliling
Besar sudut pusat sama dengan … sudut keliling yang menghadap busur sama.|dua kali|setengah|sama dengan|tiga kali|2 ×.
Sudut keliling yang menghadap diameter besarnya …|90°|180°|45°|60°|Siku-siku.
=|Jika sudut pusat 80°, sudut kelilingnya … derajat.|40|80 : 2.
=|Jika sudut keliling 35°, sudut pusatnya … derajat.|70|2 × 35.
B|Titik sudut pusat berada di pusat lingkaran.|Pusat.
S|Sudut keliling sama besar dengan sudut pusat yang menghadap busur sama.|Setengah.
Jika sudut pusat 120°, sudut kelilingnya …|60°|240°|120°|30°|Setengah.
Dua sudut keliling yang menghadap busur sama besarnya …|sama|berbeda|dua kali|setengah|Sama.
"""

SAS += """
## MAT 1
0|Titik (0, -3) terletak pada ....|sumbu Y negatif|sumbu X positif|kuadran I|kuadran III|x = 0.
1|Faktorisasi dari x² + 6x + 8 adalah ....|(x + 2)(x + 4)|(x + 1)(x + 8)|(x + 3)²|(x - 2)(x - 4)|2 × 4 = 8.
2|Banyak korespondensi satu-satu dari dua himpunan masing-masing 6 anggota adalah ....|720|36|120|12|6!.
3|Grafik f(x) = x + 4 memotong sumbu Y di titik ....|(0, 4)|(4, 0)|(1, 4)|(0, 1)|c = 4.
4|Garis dari pusat ke lingkaran disebut ....|jari-jari|diameter|tali busur|apotema|Jari-jari.
5|Luas lingkaran berjari-jari 21 cm dengan π = 22/7 adalah ....|1.386 cm²|132 cm²|462 cm²|693 cm²|22/7 × 441.
## MAT 2
0|Suku ke-8 barisan 1, 8, 15, 22, ... adalah ....|50|57|43|49|1 + 7 × 7.
1|Gradien garis tegak lurus terhadap garis bergradien 5 adalah ....|-1/5|5|1/5|-5|Lawan kebalikan.
2|Volume kubus bersisi 6 cm adalah ....|216 cm³|36 cm³|72 cm³|108 cm³|6³.
3|Banyak sisi prisma segilima adalah ....|7|5|6|10|5 + 2.
4|Frekuensi nomor sepatu 39 pada tabel 36 (3), 37 (5), 38 (8), 39 (6) adalah ....|6|39|8|3|Frekuensi.
5|Jika sudut keliling 70°, sudut pusat yang menghadap busur sama adalah ....|140°|35°|70°|110°|2 × 70.
"""

TOPICS += """
## BIN
# 1|Kebahasaan dan Teks Informasi
@ Kata baku dan tidak baku
min: 15
act: Cari lima kata tidak baku di spanduk atau media sosial, lalu tulis bentuk bakunya sesuai KBBI.
mis: menganggap kata yang sering diucapkan pasti baku
exp: Kata baku adalah kata yang sesuai kaidah bahasa Indonesia dan tercantum dalam Kamus Besar Bahasa Indonesia atau KBBI. Kata tidak baku biasanya muncul dalam percakapan sehari-hari. Kata baku dipakai dalam surat resmi, karya ilmiah, dan pidato resmi.
ex: Kata apotek adalah bentuk baku, apotik tidak baku. // Kata nasihat baku, nasehat tidak baku.
pt: Sesuai kaidah dan KBBI ; Tidak baku dalam percakapan ; Baku untuk situasi resmi
sum: Kata baku membuat tulisan resmi lebih tepat.
fig: table Kata baku | Kata tidak baku ;; apotek | apotik ;; nasihat | nasehat ;; risiko | resiko ;; kualitas | kwalitas ;; jadwal | jadual ;; praktik | praktek ~ Kata baku dan tidak baku.
@ Kalimat efektif
min: 15
act: Perbaiki tiga kalimat panjang dari pengumuman sekolah menjadi kalimat efektif.
mis: memakai kata bermakna sama secara berulang dalam satu kalimat
exp: Kalimat efektif adalah kalimat yang mampu menyampaikan gagasan dengan jelas dan tepat. Ciri kalimat efektif meliputi kesepadanan struktur, kehematan kata, kecermatan, kelogisan, kesejajaran bentuk, dan kepaduan. Kalimat efektif tidak memakai kata berlebihan seperti para siswa-siswa.
ex: Para siswa berkumpul (bukan para siswa-siswa). // Kami naik ke atas panggung diperbaiki menjadi kami naik ke panggung.
pt: Menyampaikan gagasan dengan jelas ; Hemat dan logis ; Hindari kata berulang
sum: Kalimat efektif mudah dipahami pembaca.
fig: table Kalimat tidak efektif | Perbaikan ;; para siswa-siswa | para siswa ;; naik ke atas | naik ;; mundur ke belakang | mundur ;; sangat indah sekali | sangat indah ;; agar supaya | agar ;; demi untuk | demi ~ Perbaikan kalimat efektif.
@ Konjungsi kausalitas
min: 15
act: Tulis lima kalimat sebab akibat tentang kejadian di rumah memakai konjungsi yang berbeda.
mis: menukar letak sebab dan akibat dalam kalimat
exp: Konjungsi kausalitas adalah kata hubung yang menyatakan hubungan sebab akibat. Konjungsi penanda sebab antara lain karena, sebab, dan oleh karena itu. Konjungsi penanda akibat antara lain sehingga, akibatnya, maka, dan oleh sebab itu. Konjungsi ini banyak dipakai dalam teks eksplanasi.
ex: Jalan licin karena hujan deras. // Hujan deras sehingga jalan licin.
pt: Menyatakan sebab akibat ; Penanda sebab: karena, sebab ; Penanda akibat: sehingga, akibatnya
sum: Konjungsi kausalitas membuat hubungan peristiwa jelas.
fig: table Konjungsi | Penanda ;; karena | sebab ;; sebab | sebab dalam kalimat ;; sehingga | akibat ;; akibatnya | akibat di awal kalimat ;; maka | akibat atau simpulan ;; oleh karena itu | akibat antar kalimat ~ Konjungsi kausalitas.
@ Surat pribadi dan surat dinas
min: 15
act: Tulis surat pribadi kepada saudara di kota lain, lalu bandingkan dengan contoh surat dinas dari sekolah.
mis: memakai bahasa santai dalam surat dinas
exp: Surat pribadi ditulis untuk keluarga atau teman dengan bahasa santai dan akrab. Surat dinas ditulis oleh lembaga untuk keperluan resmi dengan bahasa baku. Surat dinas memiliki kop surat, nomor, lampiran, perihal, dan cap lembaga, sedangkan surat pribadi tidak memerlukannya.
ex: Surat untuk sepupu menanyakan kabar (pribadi). // Surat undangan rapat orang tua dari sekolah (dinas).
pt: Pribadi: bahasa santai ; Dinas: bahasa baku ; Dinas ada kop, nomor, perihal
sum: Jenis surat menentukan bahasa dan bagiannya.
fig: table Bagian surat | Keterangan ;; kop surat | identitas lembaga ;; nomor surat | kode surat dinas ;; perihal | pokok isi surat ;; salam pembuka | sapaan awal ;; isi surat | maksud penulis ;; tanda tangan | pengesahan penulis ~ Bagian surat dinas.
@ Teks biografi
min: 15
act: Wawancarai kakek, nenek, atau tokoh di sekitarmu, lalu tulis biografi singkatnya.
mis: menulis biografi dengan sudut pandang orang pertama
exp: Teks biografi adalah teks yang menceritakan riwayat hidup seorang tokoh yang ditulis oleh orang lain. Struktur biografi terdiri atas orientasi, peristiwa dan masalah, serta reorientasi. Biografi memakai sudut pandang orang ketiga dan kata keterangan waktu. Autobiografi adalah riwayat hidup yang ditulis tokoh itu sendiri.
ex: Ki Hajar Dewantara lahir di Yogyakarta pada 2 Mei 1889. // Biografi menceritakan perjuangan dan prestasi tokoh.
pt: Riwayat hidup ditulis orang lain ; Orientasi, peristiwa, reorientasi ; Sudut pandang orang ketiga
sum: Biografi menginspirasi lewat kisah hidup tokoh.
fig: table Struktur biografi | Isi ;; orientasi | identitas dan latar tokoh ;; peristiwa dan masalah | perjalanan hidup tokoh ;; reorientasi | penilaian penulis ;; sudut pandang | orang ketiga ;; autobiografi | ditulis tokoh sendiri ;; keterangan waktu | urutan peristiwa ~ Unsur teks biografi.
@ Iklan layanan masyarakat
min: 15
act: Rancang iklan layanan masyarakat tentang hemat air dengan slogan singkat.
mis: menganggap iklan layanan masyarakat bertujuan menjual produk
exp: Iklan layanan masyarakat atau ILM adalah iklan yang berisi ajakan atau imbauan untuk kepentingan umum, bukan untuk mencari keuntungan. Contohnya ajakan menjaga kebersihan, hemat energi, dan imunisasi. ILM memakai kalimat persuasif, slogan menarik, dan gambar pendukung.
ex: Ayo buang sampah pada tempatnya. // Matikan lampu jika tidak dipakai.
pt: Ajakan untuk kepentingan umum ; Tidak mencari keuntungan ; Kalimat persuasif dan slogan
sum: ILM mengajak masyarakat berbuat baik.
fig: table Jenis iklan | Tujuan ;; iklan layanan masyarakat | mengajak untuk kepentingan umum ;; iklan niaga | menjual produk ;; iklan pengumuman | memberi informasi ;; iklan lowongan | mencari pekerja ;; iklan permintaan | mencari barang ;; iklan duka cita | menyampaikan kabar duka ~ Jenis iklan dan tujuannya.
# 2|Sastra dan Teks Argumentasi
@ Majas dalam puisi
min: 15
act: Temukan majas dalam lirik puisi di buku pelajaran, lalu tentukan jenisnya.
mis: mengira semua perbandingan termasuk majas personifikasi
exp: Majas adalah gaya bahasa untuk memperindah tulisan. Majas personifikasi membuat benda seolah hidup seperti manusia. Metafora membandingkan langsung tanpa kata pembanding. Simile membandingkan dengan kata seperti atau bagai. Hiperbola melebih-lebihkan. Litotes merendahkan diri.
ex: Angin berbisik di telingaku (personifikasi). // Wajahnya seperti bulan purnama (simile).
pt: Personifikasi: benda seperti hidup ; Metafora tanpa kata pembanding ; Simile memakai seperti
sum: Majas membuat puisi lebih indah dan bermakna.
fig: table Majas | Contoh ;; personifikasi | angin berbisik ;; metafora | dia bintang kelas ;; simile | wajahnya seperti bulan ;; hiperbola | tangisnya membanjiri bumi ;; litotes | mampirlah ke gubuk kami ;; ironi | rapi sekali kamarmu penuh sampah ~ Jenis majas.
@ Gurindam
min: 15
act: Buat dua bait gurindam berisi nasihat tentang belajar.
mis: menulis gurindam empat baris seperti pantun
exp: Gurindam adalah puisi lama yang terdiri atas dua baris setiap bait dengan rima a-a. Baris pertama berisi syarat atau sebab, baris kedua berisi akibat atau jawaban. Gurindam berisi nasihat. Gurindam terkenal adalah Gurindam Dua Belas karya Raja Ali Haji dari Riau.
ex: Apabila banyak berkata-kata, di situlah jalan masuk dusta. // Baris pertama sebab, baris kedua akibat.
pt: Dua baris setiap bait ; Rima a-a ; Gurindam Dua Belas karya Raja Ali Haji
sum: Gurindam memberi nasihat singkat dan padat.
fig: table Puisi lama | Ciri ;; gurindam | dua baris rima a-a ;; pantun | empat baris rima a-b-a-b ;; syair | empat baris rima a-a-a-a ;; karmina | pantun kilat dua baris ;; talibun | lebih dari empat baris ;; seloka | pantun berkait ~ Jenis puisi lama.
@ Kata serapan
min: 15
act: Kumpulkan sepuluh kata serapan dari buku IPA, lalu tebak bahasa asalnya.
mis: menulis kata serapan sesuai ejaan bahasa asing
exp: Kata serapan adalah kata dari bahasa lain yang dipakai dalam bahasa Indonesia. Penyerapan dapat dilakukan dengan penyesuaian ejaan dan lafal, misalnya system menjadi sistem, atau tanpa perubahan, misalnya radio. Bahasa sumber kata serapan antara lain bahasa Sanskerta, Arab, Belanda, Portugis, dan Inggris.
ex: Kata kantor diserap dari bahasa Belanda kantoor. // Kata kitab diserap dari bahasa Arab.
pt: Kata dari bahasa lain ; Disesuaikan ejaan atau tanpa perubahan ; Sumber Sanskerta, Arab, Belanda, Inggris
sum: Kata serapan memperkaya kosakata bahasa Indonesia.
fig: table Kata serapan | Bahasa asal ;; kitab | Arab ;; kantor | Belanda ;; meja | Portugis ;; komputer | Inggris ;; bahasa | Sanskerta ;; teh | Cina ~ Kata serapan dan asalnya.
@ Paragraf argumentasi
min: 15
act: Tulis satu paragraf argumentasi tentang pentingnya sarapan dengan dua bukti.
mis: menulis pendapat tanpa bukti atau alasan
exp: Paragraf argumentasi adalah paragraf yang berisi pendapat penulis disertai alasan dan bukti untuk meyakinkan pembaca. Unsurnya terdiri atas pernyataan atau tesis, alasan, bukti berupa data atau fakta, dan kesimpulan. Bukti dapat berupa data statistik, hasil penelitian, atau pendapat ahli.
ex: Sarapan penting karena memberi energi untuk belajar. // Menurut penelitian, siswa yang sarapan lebih mudah berkonsentrasi.
pt: Pendapat dengan alasan ; Bukti berupa data atau fakta ; Ada kesimpulan
sum: Argumen kuat didukung bukti yang tepat.
fig: table Unsur argumentasi | Fungsi ;; tesis | pendapat utama penulis ;; alasan | dasar pendapat ;; bukti | data atau fakta pendukung ;; pendapat ahli | penguat dari pakar ;; kesimpulan | penegasan akhir ;; kata penghubung | merangkai alasan ~ Unsur paragraf argumentasi.
@ Teks prosedur
min: 15
act: Tulis langkah membuat minuman kesukaanmu, lalu minta adik atau teman mempraktikkannya.
mis: menulis langkah tidak berurutan sehingga sulit diikuti
exp: Teks prosedur berisi langkah-langkah melakukan sesuatu secara berurutan. Strukturnya terdiri atas tujuan, bahan dan alat, langkah-langkah, dan penutup. Ciri kebahasaannya memakai kalimat perintah, kata kerja tindakan, konjungsi urutan seperti pertama, kemudian, dan terakhir, serta keterangan jumlah dan waktu.
ex: Pertama, didihkan air. // Kemudian, masukkan teh ke dalam gelas.
pt: Langkah berurutan ; Tujuan, bahan, langkah ; Kalimat perintah dan konjungsi urutan
sum: Teks prosedur membantu orang melakukan sesuatu dengan benar.
fig: table Struktur | Contoh isi ;; tujuan | cara membuat teh manis ;; bahan | teh, gula, air panas ;; alat | gelas dan sendok ;; langkah pertama | didihkan air ;; langkah terakhir | aduk sampai rata ;; penutup | teh siap diminum ~ Struktur teks prosedur.
@ Notulen rapat
min: 15
act: Catat jalannya rapat keluarga atau rapat kelas dalam bentuk notulen.
mis: menulis semua percakapan rapat kata per kata
exp: Notulen adalah catatan singkat tentang jalannya rapat dan hasil keputusan. Notulen ditulis oleh notulis. Isi notulen meliputi hari dan tanggal, tempat, peserta, pimpinan rapat, acara, pembahasan singkat, dan keputusan. Notulen ditandatangani pimpinan rapat dan notulis.
ex: Keputusan: kerja bakti dilaksanakan Sabtu pukul 07.00. // Notulis mencatat pokok pembicaraan saja.
pt: Catatan singkat jalannya rapat ; Ditulis notulis ; Memuat keputusan
sum: Notulen menjadi bukti hasil rapat.
fig: table Bagian notulen | Isi ;; waktu | hari, tanggal, jam ;; tempat | lokasi rapat ;; peserta | daftar hadir ;; pimpinan | ketua rapat ;; pembahasan | pokok pembicaraan ;; keputusan | hasil kesepakatan ~ Bagian notulen rapat.
"""

BANK += """
## BIN|Kata baku dan tidak baku
Bentuk baku dari kata apotik adalah …|apotek|apotik|apoteik|apotiek|Apotek.
Bentuk baku dari kata resiko adalah …|risiko|resiko|resico|risico|Risiko.
=|Bentuk baku kata nasehat adalah …|nasihat|Nasihat.
=|Bentuk baku kata praktek adalah …|praktik|Praktik.
B|Kata baku tercantum dalam KBBI.|KBBI.
S|Kata yang sering diucapkan pasti kata baku.|Belum tentu.
Bentuk baku dari kata kwalitas adalah …|kualitas|kwalitas|kwalitet|qualitas|Kualitas.
Kata baku dipakai terutama dalam situasi …|resmi|bercanda|santai di rumah|bermain|Resmi.
## BIN|Kalimat efektif
Bentuk efektif dari para siswa-siswa adalah …|para siswa|siswa-siswa para|para-para siswa|siswa para|Hemat.
Bentuk efektif dari naik ke atas adalah …|naik|naik atas|ke atas naik|naik-naik|Naik sudah ke atas.
=|Bentuk efektif dari mundur ke belakang adalah …|mundur|Mundur.
=|Bentuk efektif dari agar supaya adalah …|agar;supaya|Pilih satu.
B|Kalimat efektif menyampaikan gagasan dengan jelas.|Jelas.
S|Sangat indah sekali termasuk kalimat efektif.|Berlebihan.
Ciri kalimat efektif yang menghindari kata berlebihan adalah …|kehematan|kepaduan|kelogisan|kesejajaran|Hemat.
Kalimat yang masuk akal memenuhi ciri …|kelogisan|kehematan|kesepadanan|kecermatan|Logis.
## BIN|Konjungsi kausalitas
Konjungsi penanda sebab adalah …|karena|sehingga|akibatnya|maka|Sebab.
Konjungsi penanda akibat adalah …|sehingga|karena|sebab|walaupun|Akibat.
=|Lengkapi: Hujan deras … jalan licin.|sehingga|Akibat.
=|Lengkapi: Jalan licin … hujan deras.|karena;sebab|Sebab.
B|Konjungsi kausalitas banyak dipakai dalam teks eksplanasi.|Eksplanasi.
S|Kata walaupun termasuk konjungsi kausalitas.|Konsesif.
Konjungsi akibat yang menghubungkan antarkalimat adalah …|oleh karena itu|karena|sebab|dan|Antarkalimat.
Kalimat yang memakai konjungsi kausalitas adalah …|Ia sakit karena kehujanan.|Ia makan lalu tidur.|Ia pandai dan rajin.|Ia datang atau pergi.|Sebab akibat.
## BIN|Surat pribadi dan surat dinas
Surat yang ditulis untuk teman atau keluarga disebut surat …|pribadi|dinas|niaga|kuasa|Pribadi.
Bahasa dalam surat dinas adalah bahasa …|baku|santai|gaul|daerah|Baku.
=|Identitas lembaga di bagian atas surat dinas disebut … surat.|kop|Kop.
=|Pokok isi surat dinas ditulis pada bagian …|perihal|Perihal.
B|Surat dinas memiliki nomor surat.|Nomor.
S|Surat pribadi wajib memakai kop surat.|Tidak perlu.
Surat undangan rapat orang tua dari sekolah termasuk surat …|dinas|pribadi|niaga|lamaran|Dinas.
Bagian surat untuk pengesahan adalah …|tanda tangan|perihal|lampiran|kop|Tanda tangan.
## BIN|Teks biografi
Teks biografi ditulis oleh …|orang lain|tokoh itu sendiri|tokoh fiksi|penerbit saja|Orang lain.
Riwayat hidup yang ditulis tokoh sendiri disebut …|autobiografi|biografi|novel|cerpen|Autobiografi.
=|Bagian awal biografi yang memperkenalkan tokoh disebut …|orientasi|Orientasi.
=|Bagian akhir biografi berisi penilaian penulis disebut …|reorientasi|Reorientasi.
B|Biografi memakai sudut pandang orang ketiga.|Orang ketiga.
S|Biografi selalu memakai kata ganti aku.|Orang ketiga.
Ki Hajar Dewantara lahir pada tanggal …|2 Mei 1889|17 Agustus 1945|20 Mei 1908|28 Oktober 1928|2 Mei.
Ciri kebahasaan biografi adalah banyak memakai keterangan …|waktu|perintah|ajakan|harga|Waktu.
## BIN|Iklan layanan masyarakat
Iklan layanan masyarakat bertujuan …|mengajak untuk kepentingan umum|menjual produk|mencari pekerja|menyampaikan duka|ILM.
Iklan yang bertujuan menjual produk disebut iklan …|niaga|layanan masyarakat|duka cita|pengumuman|Niaga.
=|Kalimat ajakan singkat dalam iklan disebut …|slogan|Slogan.
=|Iklan untuk mencari pekerja disebut iklan …|lowongan|Lowongan.
B|ILM tidak bertujuan mencari keuntungan.|Nirlaba.
S|ILM bertujuan menjual produk sebanyak-banyaknya.|Kepentingan umum.
Contoh ILM adalah …|Ayo buang sampah pada tempatnya.|Diskon 50 persen hari ini!|Dicari karyawan toko.|Dijual rumah murah.|Ajakan.
Kalimat dalam ILM bersifat …|persuasif|naratif|deskriptif saja|prosedural|Persuasif.
## BIN|Majas dalam puisi
Majas yang membuat benda seolah hidup disebut …|personifikasi|hiperbola|litotes|metafora|Personifikasi.
Wajahnya seperti bulan termasuk majas …|simile|metafora|personifikasi|ironi|Simile.
=|Majas yang melebih-lebihkan disebut …|hiperbola|Hiperbola.
=|Majas yang merendahkan diri disebut …|litotes|Litotes.
B|Metafora membandingkan tanpa kata seperti.|Metafora.
S|Angin berbisik termasuk majas hiperbola.|Personifikasi.
Dia bintang kelas termasuk majas …|metafora|simile|litotes|hiperbola|Metafora.
Majas sindiran dengan menyatakan kebalikan disebut …|ironi|simile|litotes|personifikasi|Ironi.
## BIN|Gurindam
Gurindam terdiri atas … baris setiap bait.|dua|empat|tiga|enam|Dua.
Rima gurindam adalah …|a-a|a-b-a-b|a-a-a-a|a-b-b-a|a-a.
=|Pengarang Gurindam Dua Belas adalah Raja Ali …|Haji|Raja Ali Haji.
=|Baris pertama gurindam berisi syarat atau …|sebab|Sebab.
B|Gurindam berisi nasihat.|Nasihat.
S|Gurindam terdiri atas empat baris seperti pantun.|Dua baris.
Gurindam Dua Belas berasal dari daerah …|Riau|Aceh|Bali|Papua|Riau.
Puisi lama empat baris dengan rima a-a-a-a adalah …|syair|gurindam|karmina|pantun|Syair.
## BIN|Kata serapan
Kata kantor diserap dari bahasa …|Belanda|Arab|Inggris|Sanskerta|Belanda.
Kata kitab diserap dari bahasa …|Arab|Belanda|Portugis|Inggris|Arab.
=|Kata meja diserap dari bahasa …|Portugis|Portugis.
=|Kata system diserap menjadi …|sistem|Sistem.
B|Kata radio diserap tanpa perubahan.|Utuh.
S|Kata serapan harus ditulis sesuai ejaan bahasa asing.|Disesuaikan.
Kata komputer diserap dari bahasa …|Inggris|Arab|Sanskerta|Portugis|Inggris.
Kata bahasa diserap dari bahasa …|Sanskerta|Belanda|Inggris|Arab|Sanskerta.
## BIN|Paragraf argumentasi
Paragraf argumentasi berisi pendapat yang disertai …|alasan dan bukti|cerita khayalan|langkah kerja|percakapan|Bukti.
Pendapat utama penulis dalam argumentasi disebut …|tesis|bukti|kesimpulan|alasan|Tesis.
=|Data atau fakta pendukung pendapat disebut …|bukti|Bukti.
=|Penegasan akhir paragraf argumentasi disebut …|kesimpulan|Kesimpulan.
B|Pendapat ahli dapat memperkuat argumentasi.|Ahli.
S|Paragraf argumentasi tidak memerlukan bukti.|Perlu bukti.
Tujuan paragraf argumentasi adalah …|meyakinkan pembaca|menghibur pembaca|menjelaskan langkah|menceritakan khayalan|Meyakinkan.
Contoh bukti yang kuat adalah …|data hasil penelitian|kata orang|mimpi penulis|tebakan|Data.
## BIN|Teks prosedur
Teks prosedur berisi langkah-langkah yang …|berurutan|acak|tidak penting|tersembunyi|Urut.
Kalimat yang banyak dipakai dalam teks prosedur adalah kalimat …|perintah|tanya|seru|berita panjang|Perintah.
=|Konjungsi urutan untuk langkah terakhir adalah …|terakhir;akhirnya|Terakhir.
=|Bagian awal teks prosedur berisi …|tujuan|Tujuan.
B|Teks prosedur memakai kata kerja tindakan.|Tindakan.
S|Langkah dalam teks prosedur boleh ditulis acak.|Urut.
Konjungsi urutan dalam teks prosedur adalah …|kemudian|karena|walaupun|tetapi|Urutan.
Gelas dan sendok dalam resep termasuk …|alat|bahan|langkah|tujuan|Alat.
## BIN|Notulen rapat
Orang yang menulis notulen disebut …|notulis|moderator|peserta|pembicara|Notulis.
Notulen berisi catatan … jalannya rapat.|singkat|seluruh kata|khayalan|lagu|Singkat.
=|Hasil kesepakatan rapat ditulis pada bagian …|keputusan|Keputusan.
=|Ketua rapat disebut juga … rapat.|pimpinan|Pimpinan.
B|Notulen ditandatangani pimpinan rapat dan notulis.|Tanda tangan.
S|Notulis harus menulis seluruh percakapan kata per kata.|Pokok saja.
Daftar orang yang hadir dalam notulen disebut …|peserta|keputusan|tempat|acara|Peserta.
Fungsi notulen adalah sebagai …|bukti hasil rapat|hiasan|undangan|iklan|Bukti.
"""

SAS += """
## BIN 1
0|Bentuk baku dari kata jadual adalah ....|jadwal|jadual|jadwel|jaddual|Jadwal.
1|Bentuk efektif dari demi untuk kemajuan adalah ....|demi kemajuan|untuk demi kemajuan|demi-demi kemajuan|kemajuan demi untuk|Hemat.
2|Konjungsi maka dapat menyatakan ....|akibat atau simpulan|syarat|perlawanan|waktu|Maka.
3|Bagian surat yang berisi sapaan awal disebut ....|salam pembuka|perihal|kop|tanda tangan|Salam.
4|Bagian biografi yang menceritakan perjalanan hidup tokoh adalah ....|peristiwa dan masalah|orientasi|reorientasi|penutup|Peristiwa.
5|Iklan yang menyampaikan kabar kematian disebut iklan ....|duka cita|niaga|lowongan|layanan masyarakat|Duka cita.
## BIN 2
0|Mampirlah ke gubuk kami termasuk majas ....|litotes|hiperbola|simile|personifikasi|Litotes.
1|Pantun kilat yang terdiri atas dua baris disebut ....|karmina|gurindam|syair|talibun|Karmina.
2|Kata teh diserap dari bahasa ....|Cina|Arab|Belanda|Portugis|Cina.
3|Kata penghubung dalam paragraf argumentasi berfungsi ....|merangkai alasan|menghias tulisan|menghapus bukti|memperpanjang judul|Penghubung.
4|Teh, gula, dan air panas dalam teks prosedur termasuk ....|bahan|alat|tujuan|penutup|Bahan.
5|Lokasi rapat dalam notulen ditulis pada bagian ....|tempat|peserta|keputusan|pembahasan|Tempat.
"""

TOPICS += """
## IPA
# 1|Tubuh Manusia, Tumbuhan, dan Zat
@ Sistem gerak manusia
min: 15
act: Raba tulang dan otot lenganmu saat menekuk dan meluruskan siku, lalu catat yang terjadi.
mis: mengira tulang dapat bergerak sendiri tanpa otot
exp: Sistem gerak manusia terdiri atas tulang sebagai alat gerak pasif dan otot sebagai alat gerak aktif. Tulang membentuk rangka, melindungi organ, dan tempat melekatnya otot. Sendi adalah hubungan antartulang, misalnya sendi engsel pada siku dan sendi peluru pada bahu. Otot bisep dan trisep bekerja berlawanan atau antagonis.
ex: Saat siku ditekuk, bisep berkontraksi. // Tengkorak melindungi otak.
pt: Tulang alat gerak pasif ; Otot alat gerak aktif ; Sendi menghubungkan tulang
sum: Tulang dan otot bekerja sama sehingga tubuh dapat bergerak.
fig: table Jenis sendi | Contoh letak ;; sendi engsel | siku dan lutut ;; sendi peluru | bahu dan pangkal paha ;; sendi putar | leher ;; sendi pelana | ibu jari ;; sendi geser | pergelangan tangan ;; sendi mati | tengkorak ~ Jenis sendi.
@ Sistem pencernaan
min: 15
act: Kunyah nasi tanpa lauk selama satu menit, lalu rasakan perubahan rasanya.
mis: mengira penyerapan sari makanan terjadi di lambung
exp: Sistem pencernaan mengubah makanan menjadi zat yang dapat diserap tubuh. Saluran pencernaan terdiri atas mulut, kerongkongan, lambung, usus halus, usus besar, dan anus. Di mulut, enzim amilase mengubah zat tepung menjadi gula. Penyerapan sari makanan terjadi di usus halus, sedangkan penyerapan air terjadi di usus besar.
ex: Nasi terasa manis setelah lama dikunyah. // Lambung menghasilkan asam klorida.
pt: Mulut, lambung, usus halus, usus besar ; Amilase mengubah tepung menjadi gula ; Penyerapan sari makanan di usus halus
sum: Setiap organ pencernaan memiliki tugas khusus.
fig: table Organ | Fungsi ;; mulut | mengunyah makanan ;; kerongkongan | menyalurkan makanan ke lambung ;; lambung | mencerna protein dengan asam ;; usus halus | menyerap sari makanan ;; usus besar | menyerap air ;; anus | mengeluarkan feses ~ Organ pencernaan.
@ Jaringan tumbuhan
min: 15
act: Amati batang seledri yang direndam air berpewarna selama sehari, lalu potong dan lihat jalurnya.
mis: menukar fungsi xilem dan floem
exp: Tumbuhan memiliki beberapa jaringan. Jaringan epidermis melindungi bagian luar. Jaringan pengangkut terdiri atas xilem yang mengangkut air dan mineral dari akar ke daun, serta floem yang mengangkut hasil fotosintesis ke seluruh tubuh. Jaringan meristem membuat tumbuhan bertambah tinggi dan besar.
ex: Pewarna naik melalui xilem batang seledri. // Ujung akar tumbuh karena meristem.
pt: Epidermis pelindung ; Xilem angkut air ; Floem angkut hasil fotosintesis
sum: Jaringan tumbuhan bekerja sama menjaga kehidupan tumbuhan.
fig: table Jaringan | Fungsi ;; epidermis | pelindung terluar ;; xilem | mengangkut air dan mineral ;; floem | mengangkut hasil fotosintesis ;; meristem | membuat tumbuhan tumbuh ;; parenkim | menyimpan cadangan makanan ;; sklerenkim | penguat tubuh tumbuhan ~ Jaringan tumbuhan.
@ Fotosintesis
min: 15
act: Tutup sebagian daun dengan kertas timah selama dua hari, lalu bandingkan warnanya dengan daun lain.
mis: mengira tumbuhan mengambil makanan dari tanah
exp: Fotosintesis adalah proses tumbuhan membuat makanan sendiri. Bahannya karbon dioksida dan air, dengan bantuan cahaya matahari dan klorofil. Hasilnya glukosa dan oksigen. Fotosintesis terjadi di kloroplas, terutama pada daun. Oksigen hasil fotosintesis sangat penting bagi makhluk hidup lain.
ex: Daun yang tertutup menjadi pucat karena tidak berfotosintesis. // Tanaman air mengeluarkan gelembung oksigen di bawah cahaya.
pt: CO2 + air + cahaya ; Hasil glukosa dan oksigen ; Terjadi di kloroplas
sum: Fotosintesis menghasilkan makanan dan oksigen.
fig: table Komponen fotosintesis | Peran ;; karbon dioksida | bahan dari udara ;; air | bahan dari akar ;; cahaya matahari | sumber energi ;; klorofil | penangkap cahaya ;; glukosa | makanan hasil ;; oksigen | hasil yang dilepas ~ Komponen fotosintesis.
@ Kalor dan perpindahannya
min: 15
act: Masukkan sendok logam dan sendok plastik ke gelas air panas, lalu bandingkan mana yang lebih cepat panas.
mis: mengira kalor sama dengan suhu
exp: Kalor adalah energi panas yang berpindah dari benda bersuhu tinggi ke benda bersuhu rendah. Kalor berpindah secara konduksi melalui zat padat tanpa perpindahan zat, konveksi melalui aliran zat cair atau gas, dan radiasi tanpa zat perantara. Konduktor menghantarkan panas dengan baik, sedangkan isolator sulit menghantarkan panas.
ex: Sendok logam cepat panas (konduksi). // Panas matahari sampai ke bumi (radiasi).
pt: Kalor berpindah dari panas ke dingin ; Konduksi, konveksi, radiasi ; Konduktor dan isolator
sum: Kalor berpindah dengan tiga cara.
fig: table Peristiwa | Cara perpindahan ;; sendok panas di gelas teh | konduksi ;; air mendidih bergolak | konveksi ;; hangat api unggun | radiasi ;; angin darat dan laut | konveksi udara ;; setrika menghaluskan baju | konduksi logam ;; panas matahari ke bumi | radiasi tanpa perantara ~ Contoh perpindahan kalor.
@ Unsur, senyawa, dan campuran
min: 15
act: Kelompokkan benda di dapur menjadi unsur, senyawa, atau campuran.
mis: mengira air laut adalah senyawa murni
exp: Unsur adalah zat tunggal yang tidak dapat diuraikan lagi, misalnya oksigen (O) dan besi (Fe). Senyawa adalah gabungan dua unsur atau lebih secara kimia dengan perbandingan tetap, misalnya air (H2O) dan garam dapur (NaCl). Campuran adalah gabungan zat tanpa reaksi kimia, misalnya udara dan air gula.
ex: Air tersusun dari hidrogen dan oksigen. // Air laut adalah campuran air dan garam.
pt: Unsur zat tunggal ; Senyawa gabungan kimia ; Campuran tanpa reaksi kimia
sum: Materi dibedakan menjadi unsur, senyawa, dan campuran.
fig: table Zat | Golongan ;; oksigen | unsur gas ;; besi | unsur logam ;; air | senyawa ;; garam dapur | senyawa ion ;; udara | campuran homogen ;; air kopi berampas | campuran heterogen ~ Unsur, senyawa, dan campuran.
# 2|Bunyi, Cahaya, dan Lingkungan
@ Bunyi dan pendengaran
min: 15
act: Buat telepon kaleng dengan benang, lalu uji apakah suara terdengar saat benang kendur dan tegang.
mis: mengira bunyi dapat merambat di ruang hampa
exp: Bunyi adalah getaran yang merambat melalui medium berupa zat padat, cair, atau gas. Bunyi tidak dapat merambat di ruang hampa. Bunyi yang dapat didengar manusia berfrekuensi 20 sampai 20.000 Hz atau audiosonik. Di bawahnya infrasonik dan di atasnya ultrasonik. Telinga terdiri atas telinga luar, tengah, dan dalam.
ex: Kelelawar memakai ultrasonik. // Suara terdengar lewat benang tegang.
pt: Getaran merambat lewat medium ; Tidak merambat di ruang hampa ; Audiosonik 20 sampai 20.000 Hz
sum: Bunyi membutuhkan medium untuk merambat.
fig: table Bagian telinga | Fungsi ;; daun telinga | mengumpulkan bunyi ;; gendang telinga | bergetar menerima bunyi ;; tulang pendengaran | memperkuat getaran ;; koklea | mengubah getaran menjadi sinyal ;; saluran eustachius | menyeimbangkan tekanan udara ;; saraf pendengaran | mengirim sinyal ke otak ~ Bagian telinga.
@ Pemantulan cahaya pada cermin
min: 15
act: Amati bayanganmu pada cermin datar, sendok bagian cekung, dan sendok bagian cembung.
mis: mengira bayangan cermin datar terbalik atas bawah
exp: Cahaya merambat lurus dan dapat dipantulkan. Cermin datar menghasilkan bayangan maya, tegak, sama besar, dan tertukar kiri kanan. Cermin cekung mengumpulkan cahaya dan dapat menghasilkan bayangan nyata atau maya. Cermin cembung menyebarkan cahaya dan selalu menghasilkan bayangan maya, tegak, dan diperkecil.
ex: Spion kendaraan memakai cermin cembung. // Lampu senter memakai cermin cekung.
pt: Datar: maya, tegak, sama besar ; Cekung mengumpulkan cahaya ; Cembung: maya, tegak, diperkecil
sum: Jenis cermin menentukan sifat bayangan.
fig: table Cermin | Contoh penggunaan ;; cermin datar | bercermin di kamar ;; cermin cekung | reflektor lampu senter ;; cermin cembung | spion kendaraan ;; cermin cembung besar | tikungan jalan ;; cermin cekung kecil | alat periksa dokter gigi ;; periskop | dua cermin datar ~ Penggunaan cermin.
@ Mata dan kelainan penglihatan
min: 15
act: Tanyakan kepada anggota keluarga yang berkacamata jenis lensa dan kelainan matanya.
mis: mengira rabun jauh ditolong lensa cembung
exp: Mata adalah alat penglihatan. Bagiannya antara lain kornea, pupil, iris, lensa, retina, dan saraf optik. Bayangan benda jatuh tepat di retina pada mata normal. Rabun jauh atau miopi ditolong lensa cekung. Rabun dekat atau hipermetropi ditolong lensa cembung. Presbiopi terjadi pada lansia.
ex: Penderita miopi sulit membaca tulisan di papan tulis. // Kakek memakai kacamata baca karena presbiopi.
pt: Bayangan jatuh di retina ; Miopi lensa cekung ; Hipermetropi lensa cembung
sum: Kacamata membantu bayangan jatuh tepat di retina.
fig: table Bagian mata | Fungsi ;; kornea | pelindung depan mata ;; iris | memberi warna mata ;; pupil | mengatur cahaya masuk ;; lensa | memfokuskan bayangan ;; retina | tempat bayangan jatuh ;; saraf optik | mengirim sinyal ke otak ~ Bagian mata.
@ Sifat fisika dan kimia zat
min: 15
act: Amati perubahan es mencair dan kertas terbakar, lalu tentukan mana perubahan fisika dan kimia.
mis: mengira es mencair adalah perubahan kimia
exp: Sifat fisika adalah sifat yang dapat diamati tanpa mengubah jenis zat, misalnya warna, wujud, titik didih, dan kelarutan. Sifat kimia berkaitan dengan kemampuan zat berubah menjadi zat baru, misalnya mudah terbakar dan mudah berkarat. Perubahan fisika tidak menghasilkan zat baru, sedangkan perubahan kimia menghasilkan zat baru.
ex: Es mencair adalah perubahan fisika. // Besi berkarat adalah perubahan kimia.
pt: Sifat fisika tanpa mengubah zat ; Sifat kimia membentuk zat baru ; Perubahan fisika dan kimia
sum: Perubahan kimia menghasilkan zat baru.
fig: table Peristiwa | Jenis perubahan ;; es mencair | fisika wujud ;; kertas terbakar | kimia ;; gula larut | fisika pelarutan ;; besi berkarat | kimia oksidasi ;; nasi basi | kimia pembusukan ;; kayu dipotong | fisika bentuk ~ Perubahan fisika dan kimia.
@ Jaring-jaring makanan
min: 15
act: Amati makhluk hidup di kebun atau sawah, lalu susun rantai makanannya.
mis: menempatkan panah dari pemangsa ke mangsa
exp: Rantai makanan adalah peristiwa makan dan dimakan dengan urutan tertentu. Produsen adalah tumbuhan yang membuat makanan sendiri. Konsumen tingkat I memakan produsen, konsumen tingkat II memakan konsumen tingkat I, dan seterusnya. Dekomposer menguraikan makhluk hidup yang mati. Gabungan banyak rantai makanan membentuk jaring-jaring makanan.
ex: Padi → tikus → ular → elang. // Jamur dan bakteri sebagai pengurai.
pt: Produsen membuat makanan sendiri ; Konsumen tingkat I, II, III ; Dekomposer pengurai
sum: Jaring-jaring makanan menunjukkan keseimbangan ekosistem.
fig: table Makhluk hidup | Peran ;; padi | produsen ;; tikus | konsumen tingkat I ;; ular | konsumen tingkat II ;; elang | konsumen puncak ;; jamur | dekomposer ;; belalang | konsumen pemakan daun ~ Peran dalam rantai makanan.
@ Tata surya
min: 15
act: Buat model tata surya dari bola plastik berbagai ukuran sesuai urutan planet.
mis: mengira Bulan adalah planet
exp: Tata surya terdiri atas Matahari sebagai pusat dan benda langit yang mengelilinginya, yaitu planet, satelit, asteroid, dan komet. Ada delapan planet: Merkurius, Venus, Bumi, Mars, Yupiter, Saturnus, Uranus, dan Neptunus. Bulan adalah satelit alami Bumi. Bumi berotasi sehingga terjadi siang dan malam, serta berevolusi mengelilingi Matahari selama sekitar 365 hari.
ex: Yupiter adalah planet terbesar. // Merkurius adalah planet terdekat dengan Matahari.
pt: Matahari pusat tata surya ; Delapan planet ; Rotasi siang malam, revolusi setahun
sum: Tata surya adalah keluarga Matahari.
fig: table Planet | Keistimewaan ;; Merkurius | terdekat dengan Matahari ;; Venus | planet terpanas ;; Bumi | ada kehidupan ;; Mars | planet merah ;; Yupiter | planet terbesar ;; Saturnus | cincin paling indah ~ Keistimewaan planet.

## IPS
# 1|Kehidupan Sosial dan Ruang Indonesia
@ Interaksi sosial
min: 15
act: Catat interaksi yang kamu lakukan seharian, lalu kelompokkan menjadi kerja sama, persaingan, atau akomodasi.
mis: mengira interaksi sosial hanya terjadi jika bertatap muka
exp: Interaksi sosial adalah hubungan timbal balik antara individu atau kelompok. Syaratnya ada kontak sosial dan komunikasi. Bentuk interaksi asosiatif mendekatkan, misalnya kerja sama, akomodasi, dan asimilasi. Bentuk disosiatif menjauhkan, misalnya persaingan, kontravensi, dan konflik. Interaksi dapat terjadi langsung atau lewat media.
ex: Gotong royong membersihkan selokan (kerja sama). // Lomba antarkelas (persaingan).
pt: Hubungan timbal balik ; Syarat kontak dan komunikasi ; Asosiatif dan disosiatif
sum: Interaksi sosial membentuk kehidupan bermasyarakat.
fig: table Bentuk interaksi | Sifat ;; kerja sama | asosiatif ;; akomodasi | asosiatif meredakan pertentangan ;; asimilasi | asosiatif peleburan budaya ;; persaingan | disosiatif ;; kontravensi | disosiatif tersembunyi ;; konflik | disosiatif terbuka ~ Bentuk interaksi sosial.
@ Kelompok sosial
min: 15
act: Tulis kelompok sosial yang kamu ikuti, lalu bedakan mana kelompok primer dan sekunder.
mis: menganggap kerumunan di pasar sebagai kelompok sosial
exp: Kelompok sosial adalah kumpulan orang yang memiliki kesadaran bersama, tujuan, dan saling berinteraksi. Kelompok primer bersifat akrab dan pribadi, misalnya keluarga. Kelompok sekunder bersifat formal, misalnya organisasi. Paguyuban didasari ikatan batin, sedangkan patembayan didasari kepentingan.
ex: Keluarga termasuk kelompok primer. // Koperasi sekolah termasuk patembayan.
pt: Kesadaran dan tujuan bersama ; Primer dan sekunder ; Paguyuban dan patembayan
sum: Setiap orang menjadi anggota berbagai kelompok sosial.
fig: table Kelompok | Jenis ;; keluarga | primer ;; organisasi siswa | sekunder ;; rukun tetangga | paguyuban tempat ;; perusahaan | patembayan ;; teman bermain | primer sebaya ;; partai politik | sekunder formal ~ Contoh kelompok sosial.
@ Letak dan luas Indonesia
min: 15
act: Cari letak astronomis kotamu di peta atau aplikasi peta digital.
mis: menukar letak astronomis dan letak geografis
exp: Letak astronomis Indonesia adalah 6° LU sampai 11° LS dan 95° BT sampai 141° BT, sehingga beriklim tropis. Letak geografis Indonesia di antara Benua Asia dan Australia serta Samudra Hindia dan Pasifik, sehingga ramai jalur perdagangan dan dipengaruhi angin muson. Indonesia memiliki tiga zona waktu: WIB, WITA, dan WIT.
ex: Indonesia dilalui garis khatulistiwa. // Jakarta menggunakan WIB.
pt: Astronomis 6° LU–11° LS ; Geografis antara dua benua dan dua samudra ; Tiga zona waktu
sum: Letak Indonesia memengaruhi iklim dan perdagangannya.
fig: table Letak | Pengaruh ;; astronomis | iklim tropis ;; geografis | jalur perdagangan dunia ;; antara dua benua | angin muson ;; dilalui khatulistiwa | hujan sepanjang tahun ;; pertemuan lempeng | banyak gunung api ;; rentang bujur | tiga zona waktu ~ Letak Indonesia dan pengaruhnya.
@ Sumber daya alam Indonesia
min: 15
act: Buat peta sederhana persebaran tambang dan hasil perkebunan di Indonesia.
mis: mengira semua sumber daya alam dapat diperbarui
exp: Sumber daya alam adalah kekayaan alam yang dapat dimanfaatkan manusia. Sumber daya alam yang dapat diperbarui antara lain hutan, air, dan hasil laut. Sumber daya alam yang tidak dapat diperbarui antara lain minyak bumi, batu bara, dan emas. Pemanfaatannya harus bijaksana agar lestari.
ex: Batu bara banyak di Kalimantan dan Sumatra. // Tembaga dan emas ditambang di Papua.
pt: Dapat diperbarui: hutan, air ; Tidak dapat diperbarui: minyak, batu bara ; Dimanfaatkan secara lestari
sum: Kekayaan alam harus dijaga untuk generasi mendatang.
fig: table Sumber daya | Daerah penghasil ;; minyak bumi | Riau ;; batu bara | Kalimantan Timur ;; emas dan tembaga | Papua ;; timah | Bangka Belitung ;; nikel | Sulawesi Tenggara ;; gas alam | Natuna ~ Persebaran sumber daya alam.
@ Persebaran flora dan fauna
min: 15
act: Kelompokkan gambar hewan khas Indonesia ke dalam wilayah barat, peralihan, dan timur.
mis: menempatkan komodo pada fauna tipe Asiatis
exp: Persebaran fauna Indonesia dibagi oleh garis Wallace dan garis Weber. Fauna Asiatis di bagian barat, misalnya harimau dan gajah. Fauna peralihan di Sulawesi dan Nusa Tenggara, misalnya anoa dan komodo. Fauna Australis di bagian timur, misalnya kanguru pohon dan cenderawasih.
ex: Gajah Sumatra termasuk fauna Asiatis. // Cenderawasih termasuk fauna Australis.
pt: Garis Wallace dan Weber ; Asiatis, peralihan, Australis ; Fauna endemik Indonesia
sum: Indonesia kaya keanekaragaman hayati.
fig: table Fauna | Tipe ;; harimau Sumatra | Asiatis ;; badak bercula satu | Asiatis Jawa ;; anoa | peralihan ;; komodo | peralihan Nusa Tenggara ;; cenderawasih | Australis ;; kanguru pohon | Australis Papua ~ Tipe fauna Indonesia.
@ Pembagian kerja dan spesialisasi
min: 15
act: Amati pembagian tugas di rumah atau warung dekat rumah, lalu tulis manfaatnya.
mis: mengira spesialisasi membuat pekerjaan lebih lambat
exp: Pembagian kerja adalah pemisahan pekerjaan sesuai keahlian. Spesialisasi adalah pemusatan pada satu jenis pekerjaan tertentu. Manfaatnya pekerjaan lebih cepat, hasil lebih bermutu, dan keterampilan meningkat. Spesialisasi daerah terjadi karena perbedaan sumber daya, misalnya daerah penghasil kopi atau kerajinan.
ex: Di pabrik roti ada bagian adonan, pemanggangan, dan pengemasan. // Jepara terkenal dengan ukiran kayu.
pt: Pemisahan pekerjaan sesuai keahlian ; Lebih cepat dan bermutu ; Spesialisasi daerah
sum: Spesialisasi meningkatkan produktivitas.
fig: table Daerah | Spesialisasi ;; Jepara | ukiran kayu ;; Pekalongan | batik ;; Cianjur | beras ;; Toraja | kopi ;; Kasongan | gerabah ;; Garut | dodol ~ Spesialisasi daerah.
# 2|Sejarah dan Ekonomi
@ Pendudukan Jepang di Indonesia
min: 15
act: Tanyakan kepada kakek atau nenek cerita yang mereka dengar tentang masa pendudukan Jepang.
mis: mengira Jepang datang untuk memerdekakan Indonesia
exp: Jepang menduduki Indonesia pada 1942 sampai 1945 setelah Belanda menyerah melalui Perjanjian Kalijati. Jepang membentuk organisasi seperti PETA, Heiho, dan Putera untuk kepentingan perang. Rakyat menderita akibat romusha atau kerja paksa. Pendudukan berakhir setelah Jepang menyerah kepada Sekutu pada Agustus 1945.
ex: PETA melatih pemuda Indonesia secara militer. // Romusha dipaksa bekerja membangun jalan dan benteng.
pt: Pendudukan 1942–1945 ; PETA, Heiho, Putera ; Romusha kerja paksa
sum: Masa Jepang singkat tetapi berat bagi rakyat.
fig: table Organisasi | Keterangan ;; PETA | tentara Pembela Tanah Air ;; Heiho | pembantu prajurit Jepang ;; Putera | Pusat Tenaga Rakyat ;; Seinendan | barisan pemuda ;; Keibodan | pembantu polisi ;; Fujinkai | perkumpulan perempuan ~ Organisasi bentukan Jepang.
@ Perlawanan rakyat terhadap kolonial
min: 15
act: Cari pahlawan dari daerahmu yang melawan penjajah, lalu buat kartu tokohnya.
mis: mengira perlawanan sebelum 1908 gagal karena rakyat tidak berani
exp: Sebelum abad ke-20, rakyat melawan penjajah di berbagai daerah. Perlawanan ini bersifat kedaerahan, mengandalkan pemimpin, dan memakai senjata tradisional sehingga mudah dipatahkan, terutama dengan politik adu domba. Contohnya Perang Diponegoro, Perang Padri, Perang Aceh, dan perlawanan Pattimura.
ex: Perang Diponegoro berlangsung 1825–1830. // Tuanku Imam Bonjol memimpin Perang Padri.
pt: Bersifat kedaerahan ; Bergantung pada pemimpin ; Dipatahkan dengan adu domba
sum: Perlawanan rakyat menunjukkan semangat menolak penjajahan.
fig: table Perlawanan | Tokoh ;; Perang Diponegoro | Pangeran Diponegoro ;; Perang Padri | Tuanku Imam Bonjol ;; Perang Aceh | Cut Nyak Dien ;; perlawanan Maluku | Pattimura ;; Perang Banjar | Pangeran Antasari ;; perlawanan Bali | I Gusti Ketut Jelantik ~ Perlawanan rakyat dan tokohnya.
@ Produksi, distribusi, dan konsumsi
min: 15
act: Telusuri perjalanan sebungkus roti dari pabrik sampai ke tanganmu.
mis: mengira kegiatan distribusi hanya dilakukan oleh pabrik
exp: Produksi adalah kegiatan menghasilkan atau menambah nilai guna barang dan jasa. Distribusi adalah kegiatan menyalurkan barang dari produsen ke konsumen. Konsumsi adalah kegiatan memakai atau menghabiskan nilai guna barang dan jasa. Faktor produksi meliputi alam, tenaga kerja, modal, dan kewirausahaan.
ex: Petani menanam padi (produksi). // Agen menyalurkan beras ke toko (distribusi).
pt: Produksi menghasilkan ; Distribusi menyalurkan ; Konsumsi memakai
sum: Ketiga kegiatan ekonomi saling berkaitan.
fig: table Pelaku | Kegiatan ;; petani menanam padi | produksi ;; pabrik membuat roti | produksi barang ;; agen beras | distribusi ;; sopir truk barang | distribusi pengangkutan ;; keluarga makan nasi | konsumsi ;; siswa memakai buku | konsumsi barang ~ Kegiatan ekonomi.
@ Pajak dan APBN
min: 15
act: Cari contoh fasilitas umum di sekitarmu yang dibangun dari uang pajak.
mis: mengira pajak memberi imbalan langsung kepada pembayarnya
exp: Pajak adalah iuran wajib rakyat kepada negara berdasarkan undang-undang tanpa imbalan langsung. Pajak menjadi sumber utama penerimaan negara dalam APBN atau Anggaran Pendapatan dan Belanja Negara. Uang pajak dipakai untuk membangun jalan, sekolah, rumah sakit, dan membayar gaji pegawai negeri.
ex: PPN dibayar saat membeli barang. // Pajak kendaraan bermotor dibayar setiap tahun.
pt: Iuran wajib berdasarkan undang-undang ; Tanpa imbalan langsung ; Sumber utama APBN
sum: Membayar pajak berarti ikut membangun negara.
fig: table Jenis pajak | Dikenakan pada ;; PPh | penghasilan ;; PPN | pembelian barang dan jasa ;; PBB | tanah dan bangunan ;; PKB | kendaraan bermotor ;; bea cukai | barang impor ;; pajak hotel | jasa penginapan ~ Jenis pajak.
@ Perdagangan antardaerah
min: 15
act: Catat asal daerah lima bahan makanan di dapurmu dari kemasannya atau tanya penjual.
mis: mengira perdagangan antardaerah hanya merugikan daerah pembeli
exp: Perdagangan antardaerah adalah kegiatan jual beli barang antara satu daerah dan daerah lain di dalam negeri. Penyebabnya perbedaan sumber daya alam, iklim, dan keahlian. Manfaatnya memenuhi kebutuhan, memperluas lapangan kerja, dan mempererat persatuan. Kelancarannya didukung jalan, pelabuhan, dan alat transportasi.
ex: Apel dari Malang dijual di Jakarta. // Ikan dari Maluku dikirim ke Jawa.
pt: Jual beli antardaerah dalam negeri ; Karena perbedaan sumber daya ; Memenuhi kebutuhan dan mempererat persatuan
sum: Perdagangan antardaerah saling menguntungkan.
fig: table Komoditas | Daerah asal ;; apel | Malang ;; salak pondoh | Sleman ;; ikan tuna | Maluku ;; kopi gayo | Aceh ;; jeruk | Kalimantan Barat ;; garam | Madura ~ Komoditas antardaerah.
@ Ketenagakerjaan
min: 15
act: Wawancarai dua orang dewasa tentang pekerjaan mereka dan keterampilan yang dibutuhkan.
mis: menganggap semua penduduk usia kerja termasuk angkatan kerja
exp: Tenaga kerja adalah penduduk usia kerja, yaitu 15 sampai 64 tahun. Angkatan kerja adalah tenaga kerja yang bekerja atau sedang mencari kerja. Bukan angkatan kerja meliputi pelajar, ibu rumah tangga, dan pensiunan. Pengangguran terjadi jika lowongan kerja lebih sedikit dari pencari kerja atau keterampilan tidak sesuai.
ex: Siswa SMA termasuk bukan angkatan kerja. // Lulusan yang sedang mencari kerja termasuk angkatan kerja.
pt: Usia kerja 15–64 tahun ; Angkatan kerja bekerja atau mencari kerja ; Pengangguran karena lowongan kurang
sum: Keterampilan membantu bersaing di dunia kerja.
fig: table Jenis pengangguran | Penyebab ;; friksional | sedang pindah pekerjaan ;; struktural | keterampilan tidak sesuai ;; musiman | pergantian musim ;; siklis | ekonomi lesu ;; terselubung | bekerja tidak sesuai kemampuan ;; teknologi | digantikan mesin ~ Jenis pengangguran.
"""

BANK += """
## IPA|Sistem gerak manusia
Alat gerak aktif pada manusia adalah …|otot|tulang|sendi|kulit|Otot.
Sendi pada siku termasuk sendi …|engsel|peluru|putar|pelana|Engsel.
=|Alat gerak pasif pada manusia adalah …|tulang|Tulang.
=|Sendi pada bahu termasuk sendi …|peluru|Peluru.
B|Otot bisep dan trisep bekerja antagonis.|Berlawanan.
S|Tulang dapat bergerak sendiri tanpa otot.|Perlu otot.
Tulang yang melindungi otak adalah …|tengkorak|rusuk|tulang belakang|tulang paha|Tengkorak.
Sendi pada leher termasuk sendi …|putar|engsel|geser|mati|Putar.
## IPA|Sistem pencernaan
Penyerapan sari makanan terjadi di …|usus halus|lambung|usus besar|kerongkongan|Usus halus.
Enzim di mulut yang mengubah tepung menjadi gula adalah …|amilase|pepsin|lipase|tripsin|Amilase.
=|Organ yang menyerap air dari sisa makanan adalah usus …|besar|Usus besar.
=|Saluran dari mulut ke lambung disebut …|kerongkongan|Kerongkongan.
B|Lambung menghasilkan asam klorida.|HCl.
S|Penyerapan sari makanan terjadi di lambung.|Usus halus.
Nasi terasa manis setelah lama dikunyah karena kerja enzim …|amilase|pepsin|renin|lipase|Amilase.
Urutan saluran pencernaan yang benar adalah …|mulut, kerongkongan, lambung, usus halus|mulut, lambung, kerongkongan, usus besar|lambung, mulut, usus halus, anus|mulut, usus halus, lambung, anus|Urutan.
## IPA|Jaringan tumbuhan
Jaringan yang mengangkut air dari akar ke daun adalah …|xilem|floem|epidermis|meristem|Xilem.
Jaringan yang mengangkut hasil fotosintesis adalah …|floem|xilem|parenkim|sklerenkim|Floem.
=|Jaringan pelindung terluar tumbuhan adalah …|epidermis|Epidermis.
=|Jaringan yang membuat tumbuhan bertambah tinggi adalah …|meristem|Meristem.
B|Parenkim dapat menyimpan cadangan makanan.|Parenkim.
S|Xilem mengangkut hasil fotosintesis dari daun.|Floem.
Pewarna yang naik pada batang seledri melalui jaringan …|xilem|floem|epidermis|kambium|Xilem.
Jaringan penguat tubuh tumbuhan adalah …|sklerenkim|parenkim|epidermis|meristem|Sklerenkim.
## IPA|Fotosintesis
Fotosintesis menghasilkan glukosa dan …|oksigen|karbon dioksida|nitrogen|air raksa|O2.
Zat hijau daun penangkap cahaya adalah …|klorofil|hemoglobin|melanin|amilase|Klorofil.
=|Fotosintesis terjadi di organel …|kloroplas|Kloroplas.
=|Gas dari udara yang diperlukan fotosintesis adalah karbon …|dioksida|CO2.
B|Cahaya matahari adalah sumber energi fotosintesis.|Cahaya.
S|Tumbuhan mengambil makanan jadi dari tanah.|Membuat sendiri.
Bahan fotosintesis yang diserap akar adalah …|air|oksigen|glukosa|klorofil|Air.
Daun yang ditutup kertas timah menjadi pucat karena …|tidak mendapat cahaya|kelebihan air|terlalu dingin|kena hama|Tanpa cahaya.
## IPA|Kalor dan perpindahannya
Perpindahan kalor melalui zat padat tanpa perpindahan zat disebut …|konduksi|konveksi|radiasi|evaporasi|Konduksi.
Panas matahari sampai ke bumi secara …|radiasi|konduksi|konveksi|kondensasi|Radiasi.
=|Perpindahan kalor dengan aliran zat cair atau gas disebut …|konveksi|Konveksi.
=|Bahan yang sulit menghantarkan panas disebut …|isolator|Isolator.
B|Kalor berpindah dari benda bersuhu tinggi ke rendah.|Arah.
S|Kalor sama dengan suhu.|Berbeda.
Bahan yang termasuk konduktor adalah …|besi|plastik|kayu|kain|Logam.
Air mendidih bergolak menunjukkan perpindahan kalor secara …|konveksi|konduksi|radiasi|isolasi|Konveksi.
## IPA|Unsur, senyawa, dan campuran
Air (H2O) termasuk …|senyawa|unsur|campuran|larutan|Senyawa.
Lambang unsur besi adalah …|Fe|Be|Bi|Ir|Fe.
=|Udara termasuk … homogen.|campuran|Campuran.
=|Rumus kimia garam dapur adalah …|NaCl|NaCl.
B|Unsur tidak dapat diuraikan lagi.|Tunggal.
S|Air laut adalah senyawa murni.|Campuran.
Contoh unsur adalah …|oksigen|air|garam dapur|gula|Oksigen.
Air kopi berampas termasuk campuran …|heterogen|homogen|senyawa|unsur|Heterogen.
## IPA|Bunyi dan pendengaran
Bunyi tidak dapat merambat di …|ruang hampa|air|udara|kayu|Hampa.
Bunyi berfrekuensi 20–20.000 Hz disebut …|audiosonik|infrasonik|ultrasonik|supersonik|Audiosonik.
=|Bunyi di atas 20.000 Hz disebut …|ultrasonik|Ultrasonik.
=|Bagian telinga yang bergetar menerima bunyi adalah gendang …|telinga|Gendang telinga.
B|Kelelawar memakai ultrasonik.|Ekolokasi.
S|Bunyi dapat merambat di ruang hampa.|Butuh medium.
Bagian telinga yang mengubah getaran menjadi sinyal saraf adalah …|koklea|daun telinga|gendang telinga|eustachius|Koklea.
Bunyi di bawah 20 Hz disebut …|infrasonik|ultrasonik|audiosonik|resonansi|Infrasonik.
## IPA|Pemantulan cahaya pada cermin
Spion kendaraan memakai cermin …|cembung|cekung|datar|ganda|Cembung.
Bayangan pada cermin datar bersifat …|maya, tegak, sama besar|nyata, terbalik|maya, diperkecil|nyata, diperbesar|Datar.
=|Reflektor lampu senter memakai cermin …|cekung|Cekung.
=|Cermin cembung selalu menghasilkan bayangan maya, tegak, dan …|diperkecil|Diperkecil.
B|Cahaya merambat lurus.|Lurus.
S|Bayangan cermin datar terbalik atas bawah.|Kiri kanan.
Cermin yang dipasang di tikungan jalan adalah cermin …|cembung|cekung|datar|kaca biasa|Cembung.
Periskop menggunakan dua cermin …|datar|cekung|cembung|lengkung|Datar.
## IPA|Mata dan kelainan penglihatan
Rabun jauh ditolong dengan lensa …|cekung|cembung|datar|silinder|Cekung.
Rabun dekat ditolong dengan lensa …|cembung|cekung|datar|ganda|Cembung.
=|Bagian mata tempat bayangan jatuh adalah …|retina|Retina.
=|Bagian mata yang mengatur cahaya masuk adalah …|pupil|Pupil.
B|Presbiopi umumnya terjadi pada lansia.|Lansia.
S|Rabun jauh ditolong lensa cembung.|Cekung.
Nama lain rabun jauh adalah …|miopi|hipermetropi|presbiopi|astigmatisme|Miopi.
Bagian mata yang memberi warna adalah …|iris|retina|lensa|kornea|Iris.
## IPA|Sifat fisika dan kimia zat
Es mencair termasuk perubahan …|fisika|kimia|biologi|nuklir|Fisika.
Besi berkarat termasuk perubahan …|kimia|fisika|wujud|bentuk|Kimia.
=|Perubahan yang menghasilkan zat baru adalah perubahan …|kimia|Kimia.
=|Kertas terbakar termasuk perubahan …|kimia|Kimia.
B|Gula larut dalam air termasuk perubahan fisika.|Fisika.
S|Kayu dipotong menghasilkan zat baru.|Fisika.
Contoh sifat kimia adalah …|mudah terbakar|warna|wujud|titik didih|Kimia.
Nasi basi termasuk perubahan …|kimia|fisika|wujud|bentuk|Kimia.
## IPA|Jaring-jaring makanan
Tumbuhan dalam rantai makanan berperan sebagai …|produsen|konsumen I|konsumen II|dekomposer|Produsen.
Jamur dan bakteri berperan sebagai …|dekomposer|produsen|konsumen puncak|konsumen I|Pengurai.
=|Pada rantai padi → tikus → ular, tikus adalah konsumen tingkat …|I;1;satu|I.
=|Gabungan beberapa rantai makanan disebut … makanan.|jaring-jaring|Jaring-jaring.
B|Elang dapat menjadi konsumen puncak.|Puncak.
S|Panah rantai makanan menunjuk dari pemangsa ke mangsa.|Mangsa ke pemangsa.
Pada rantai padi → tikus → ular → elang, ular adalah konsumen tingkat …|II|I|III|puncak|Kedua.
Belalang yang memakan daun berperan sebagai konsumen tingkat …|I|II|III|puncak|Pertama.
## IPA|Tata surya
Planet terbesar dalam tata surya adalah …|Yupiter|Saturnus|Bumi|Neptunus|Yupiter.
Planet terdekat dengan Matahari adalah …|Merkurius|Venus|Mars|Bumi|Merkurius.
=|Pusat tata surya adalah …|Matahari|Matahari.
=|Planet yang dijuluki planet merah adalah …|Mars|Mars.
B|Bulan adalah satelit alami Bumi.|Satelit.
S|Bulan termasuk planet.|Satelit.
Siang dan malam terjadi karena Bumi …|berotasi|berevolusi|berhenti|mengecil|Rotasi.
Planet terpanas dalam tata surya adalah …|Venus|Merkurius|Mars|Yupiter|Venus.
## IPS|Interaksi sosial
Syarat interaksi sosial adalah kontak sosial dan …|komunikasi|persaingan|konflik|kekayaan|Komunikasi.
Gotong royong termasuk interaksi …|kerja sama|persaingan|konflik|kontravensi|Kerja sama.
=|Peleburan dua budaya menjadi budaya baru disebut …|asimilasi|Asimilasi.
=|Interaksi yang meredakan pertentangan disebut …|akomodasi|Akomodasi.
B|Lomba antarkelas termasuk persaingan.|Persaingan.
S|Interaksi sosial hanya terjadi saat bertatap muka.|Lewat media juga.
Bentuk interaksi disosiatif yang tersembunyi adalah …|kontravensi|kerja sama|akomodasi|asimilasi|Kontravensi.
Interaksi yang mendekatkan disebut interaksi …|asosiatif|disosiatif|konflik|individual|Asosiatif.
## IPS|Kelompok sosial
Keluarga termasuk kelompok …|primer|sekunder|patembayan|formal|Primer.
Kelompok yang didasari kepentingan disebut …|patembayan|paguyuban|keluarga|kerabat|Patembayan.
=|Kelompok yang didasari ikatan batin disebut …|paguyuban|Paguyuban.
=|Organisasi resmi termasuk kelompok …|sekunder|Sekunder.
B|Perusahaan termasuk patembayan.|Kepentingan.
S|Kerumunan di pasar adalah kelompok sosial tetap.|Kerumunan.
Contoh paguyuban adalah …|rukun tetangga|perusahaan|partai politik|bank|Paguyuban.
Ciri kelompok sosial adalah memiliki …|tujuan bersama|anggota tidak saling kenal|tanpa interaksi|tanpa kesadaran|Tujuan.
## IPS|Letak dan luas Indonesia
Letak astronomis Indonesia menyebabkan iklim …|tropis|subtropis|kutub|gurun|Tropis.
Indonesia terletak di antara Benua Asia dan Benua …|Australia|Afrika|Eropa|Amerika|Australia.
=|Jumlah zona waktu di Indonesia adalah …|3;tiga|Tiga.
=|Zona waktu yang dipakai Jakarta adalah …|WIB|WIB.
B|Indonesia dilalui garis khatulistiwa.|Khatulistiwa.
S|Letak astronomis adalah letak di antara dua benua.|Geografis.
Letak geografis Indonesia membuatnya ramai dilalui …|jalur perdagangan dunia|salju|gurun pasir|angin kutub|Perdagangan.
Indonesia terletak di antara Samudra Hindia dan Samudra …|Pasifik|Atlantik|Arktik|Selatan|Pasifik.
## IPS|Sumber daya alam Indonesia
Contoh sumber daya alam yang dapat diperbarui adalah …|hutan|minyak bumi|batu bara|emas|Hutan.
Daerah penghasil timah di Indonesia adalah …|Bangka Belitung|Papua|Riau|Natuna|Timah.
=|Emas dan tembaga banyak ditambang di …|Papua|Papua.
=|Minyak bumi banyak dihasilkan di …|Riau|Riau.
B|Sumber daya alam harus dimanfaatkan secara lestari.|Lestari.
S|Semua sumber daya alam dapat diperbarui.|Ada yang tidak.
Nikel banyak ditambang di …|Sulawesi Tenggara|Bali|Jawa Barat|Aceh|Nikel.
Gas alam banyak dihasilkan di …|Natuna|Yogyakarta|Bali|Lombok|Natuna.
## IPS|Persebaran flora dan fauna
Harimau Sumatra termasuk fauna tipe …|Asiatis|Australis|peralihan|Eropa|Asiatis.
Komodo termasuk fauna tipe …|peralihan|Asiatis|Australis|Afrika|Peralihan.
=|Cenderawasih termasuk fauna tipe …|Australis|Australis.
=|Garis yang membatasi fauna Asiatis dan peralihan disebut garis …|Wallace|Wallace.
B|Anoa termasuk fauna peralihan.|Sulawesi.
S|Komodo termasuk fauna Asiatis.|Peralihan.
Garis yang membatasi fauna peralihan dan Australis disebut garis …|Weber|Wallace|khatulistiwa|meridian|Weber.
Badak bercula satu hidup di …|Jawa|Papua|Sulawesi|Maluku|Ujung Kulon.
## IPS|Pembagian kerja dan spesialisasi
Pemusatan pada satu jenis pekerjaan disebut …|spesialisasi|distribusi|konsumsi|produksi|Spesialisasi.
Daerah yang terkenal dengan ukiran kayu adalah …|Jepara|Pekalongan|Garut|Cianjur|Jepara.
=|Pekalongan terkenal dengan …|batik|Batik.
=|Kasongan terkenal dengan kerajinan …|gerabah|Gerabah.
B|Spesialisasi membuat hasil kerja lebih bermutu.|Bermutu.
S|Spesialisasi membuat pekerjaan lebih lambat.|Lebih cepat.
Garut terkenal dengan makanan khas …|dodol|bakpia|gudeg|pempek|Dodol.
Toraja terkenal sebagai penghasil …|kopi|batik|gerabah|ukiran|Kopi.
## IPS|Pendudukan Jepang di Indonesia
Jepang menduduki Indonesia mulai tahun …|1942|1945|1908|1928|1942.
Kerja paksa pada masa Jepang disebut …|romusha|rodi|cultuurstelsel|tanam paksa|Romusha.
=|Tentara Pembela Tanah Air disingkat …|PETA|PETA.
=|Belanda menyerah kepada Jepang melalui Perjanjian …|Kalijati|Kalijati.
B|Heiho adalah pembantu prajurit Jepang.|Heiho.
S|Jepang datang untuk memerdekakan Indonesia.|Kepentingan perang.
Organisasi perempuan bentukan Jepang adalah …|Fujinkai|Keibodan|Seinendan|Heiho|Fujinkai.
Pendudukan Jepang berakhir setelah Jepang menyerah kepada …|Sekutu|Belanda|Indonesia|Portugis|Sekutu.
## IPS|Perlawanan rakyat terhadap kolonial
Tokoh Perang Padri adalah …|Tuanku Imam Bonjol|Pangeran Diponegoro|Pattimura|Cut Nyak Dien|Imam Bonjol.
Perang Diponegoro berlangsung tahun …|1825–1830|1945–1949|1908–1912|1873–1904|1825–1830.
=|Tokoh perlawanan dari Maluku adalah …|Pattimura|Pattimura.
=|Tokoh perempuan dalam Perang Aceh adalah Cut Nyak …|Dien|Cut Nyak Dien.
B|Perlawanan sebelum abad ke-20 bersifat kedaerahan.|Kedaerahan.
S|Perlawanan rakyat gagal karena rakyat tidak berani.|Adu domba.
Taktik Belanda memecah belah rakyat disebut politik …|adu domba|etis|pintu terbuka|balas budi|Devide et impera.
Tokoh Perang Banjar adalah …|Pangeran Antasari|Pattimura|Imam Bonjol|Diponegoro|Antasari.
## IPS|Produksi, distribusi, dan konsumsi
Kegiatan menyalurkan barang dari produsen ke konsumen disebut …|distribusi|produksi|konsumsi|investasi|Distribusi.
Petani menanam padi termasuk kegiatan …|produksi|distribusi|konsumsi|promosi|Produksi.
=|Kegiatan memakai nilai guna barang disebut …|konsumsi|Konsumsi.
=|Faktor produksi berupa uang dan peralatan disebut …|modal|Modal.
B|Agen beras melakukan distribusi.|Distribusi.
S|Distribusi hanya dilakukan oleh pabrik.|Banyak pelaku.
Faktor produksi yang berupa tanah dan air adalah …|alam|modal|tenaga kerja|kewirausahaan|Alam.
Keluarga makan nasi termasuk kegiatan …|konsumsi|produksi|distribusi|ekspor|Konsumsi.
## IPS|Pajak dan APBN
Pajak adalah iuran wajib kepada negara tanpa …|imbalan langsung|undang-undang|aturan|pencatatan|Tanpa imbalan.
Pajak yang dibayar saat membeli barang adalah …|PPN|PBB|PKB|PPh|PPN.
=|Pajak atas tanah dan bangunan disingkat …|PBB|PBB.
=|Pajak atas penghasilan disingkat …|PPh|PPh.
B|Pajak adalah sumber utama penerimaan APBN.|APBN.
S|Pembayar pajak mendapat imbalan langsung dari negara.|Tidak langsung.
Kepanjangan APBN adalah Anggaran Pendapatan dan … Negara.|Belanja|Bunga|Bantuan|Bisnis|Belanja.
Pajak kendaraan bermotor disingkat …|PKB|PBB|PPN|PPh|PKB.
## IPS|Perdagangan antardaerah
Penyebab perdagangan antardaerah adalah perbedaan …|sumber daya alam|bahasa|agama|warna kulit|SDA.
Apel banyak dihasilkan di …|Malang|Madura|Aceh|Maluku|Malang.
=|Garam banyak dihasilkan di …|Madura|Madura.
=|Kopi gayo berasal dari …|Aceh|Aceh.
B|Perdagangan antardaerah mempererat persatuan.|Persatuan.
S|Perdagangan antardaerah hanya merugikan daerah pembeli.|Saling untung.
Salak pondoh berasal dari …|Sleman|Malang|Garut|Medan|Sleman.
Sarana pendukung perdagangan antardaerah adalah …|pelabuhan|stadion|museum|taman bermain|Pelabuhan.
## IPS|Ketenagakerjaan
Usia kerja di Indonesia adalah …|15–64 tahun|10–50 tahun|18–70 tahun|5–60 tahun|15–64.
Pelajar termasuk …|bukan angkatan kerja|angkatan kerja|pengangguran|pekerja tetap|Bukan angkatan kerja.
=|Pengangguran karena keterampilan tidak sesuai disebut pengangguran …|struktural|Struktural.
=|Pengangguran karena pergantian musim disebut pengangguran …|musiman|Musiman.
B|Orang yang sedang mencari kerja termasuk angkatan kerja.|Angkatan kerja.
S|Semua penduduk usia kerja termasuk angkatan kerja.|Tidak semua.
Pengangguran karena digantikan mesin disebut pengangguran …|teknologi|friksional|musiman|siklis|Teknologi.
Pengangguran karena sedang pindah pekerjaan disebut pengangguran …|friksional|struktural|musiman|siklis|Friksional.
"""

SAS += """
## IPA 1
0|Sendi pada ibu jari termasuk sendi ....|pelana|engsel|peluru|putar|Pelana.
1|Organ yang mengeluarkan sisa pencernaan adalah ....|anus|lambung|usus halus|kerongkongan|Anus.
2|Jaringan yang menyimpan cadangan makanan adalah ....|parenkim|xilem|epidermis|meristem|Parenkim.
3|Gas yang dilepas tumbuhan saat fotosintesis adalah ....|oksigen|karbon dioksida|nitrogen|hidrogen|O2.
4|Hangat api unggun yang terasa dari jauh merupakan perpindahan kalor secara ....|radiasi|konduksi|konveksi|isolasi|Radiasi.
5|Garam dapur termasuk ....|senyawa|unsur|campuran heterogen|logam|Senyawa.
## IPA 2
0|Saluran eustachius berfungsi ....|menyeimbangkan tekanan udara|mengumpulkan bunyi|mengirim sinyal ke otak|memperkuat getaran|Eustachius.
1|Alat periksa dokter gigi memakai cermin ....|cekung|cembung|datar|ganda|Cekung.
2|Bagian depan mata yang bening dan melindungi disebut ....|kornea|iris|retina|pupil|Kornea.
3|Contoh sifat fisika zat adalah ....|titik didih|mudah berkarat|mudah terbakar|mudah membusuk|Fisika.
4|Pada rantai padi → tikus → ular → elang, konsumen puncaknya adalah ....|elang|ular|tikus|padi|Elang.
5|Planet yang memiliki cincin paling indah adalah ....|Saturnus|Yupiter|Mars|Venus|Saturnus.
## IPS 1
0|Konflik terbuka antara dua kelompok termasuk interaksi ....|disosiatif|asosiatif|akomodasi|asimilasi|Disosiatif.
1|Teman bermain sebaya termasuk kelompok ....|primer|sekunder|patembayan|formal|Primer.
2|Letak Indonesia di pertemuan lempeng menyebabkan banyak ....|gunung api|salju|gurun|padang rumput|Gunung api.
3|Batu bara banyak dihasilkan di ....|Kalimantan Timur|Bali|Papua|Bangka Belitung|Batu bara.
4|Kanguru pohon termasuk fauna tipe ....|Australis|Asiatis|peralihan|Eropa|Australis.
5|Cianjur terkenal sebagai penghasil ....|beras|batik|ukiran|gerabah|Beras.
## IPS 2
0|Pusat Tenaga Rakyat bentukan Jepang disingkat ....|Putera|PETA|Heiho|Keibodan|Putera.
1|Tokoh perlawanan rakyat Bali adalah ....|I Gusti Ketut Jelantik|Pattimura|Antasari|Diponegoro|Jelantik.
2|Sopir truk yang mengangkut barang melakukan kegiatan ....|distribusi|produksi|konsumsi|investasi|Distribusi.
3|Bea cukai dikenakan pada ....|barang impor|tanah|penghasilan|kendaraan|Impor.
4|Ikan tuna banyak dikirim dari ....|Maluku|Malang|Madura|Sleman|Maluku.
5|Pengangguran karena ekonomi lesu disebut pengangguran ....|siklis|musiman|friksional|struktural|Siklis.
"""

TOPICS += """
## BIG
# 1|Past Events and Expressions
@ Simple past tense
min: 15
act: Write five sentences about what you did last Sunday using the simple past tense.
mis: memakai bentuk kata kerja pertama untuk kejadian kemarin
exp: Simple past tense dipakai untuk menceritakan kejadian yang sudah selesai di masa lampau. Polanya subjek + kata kerja bentuk kedua. Kalimat negatif memakai did not + kata kerja pertama, dan kalimat tanya memakai Did + subjek + kata kerja pertama. Keterangan waktunya antara lain yesterday, last week, dan two days ago.
ex: I visited my grandmother yesterday. // Did you watch the match last night?
pt: Kejadian selesai di masa lampau ; Subjek + verb 2 ; Negatif dan tanya memakai did
sum: Simple past tense menceritakan masa lalu.
fig: table Kalimat | Pola ;; I played football yesterday. | positif ;; I did not play football. | negatif ;; Did you play football? | tanya ;; She was happy. | positif dengan was ;; They were at school. | positif dengan were ;; Were they late? | tanya dengan were ~ Pola simple past tense.
@ Irregular verbs
min: 15
act: Make flashcards of ten irregular verbs and test your family members.
mis: menambahkan -ed pada semua kata kerja
exp: Kata kerja beraturan atau regular verbs membentuk bentuk lampau dengan menambah -ed, misalnya play menjadi played. Kata kerja tidak beraturan atau irregular verbs berubah bentuk tanpa pola tetap, misalnya go menjadi went dan eat menjadi ate. Irregular verbs perlu dihafalkan.
ex: I went to the market. // She ate fried rice.
pt: Regular verbs + -ed ; Irregular verbs berubah bentuk ; Perlu dihafalkan
sum: Hafalkan irregular verbs agar kalimat lampau benar.
fig: table Verb 1 | Verb 2 ;; go | went ;; eat | ate ;; buy | bought ;; see | saw ;; write | wrote ;; swim | swam ~ Irregular verbs.
@ Congratulating and complimenting
min: 15
act: Write a short congratulation message for a friend who won a competition.
mis: menjawab ucapan selamat tanpa berterima kasih
exp: Congratulating adalah memberi ucapan selamat atas keberhasilan atau peristiwa bahagia, misalnya Congratulations on your success. Complimenting adalah memuji, misalnya What a beautiful drawing! Respons yang sopan adalah Thank you atau Thanks a lot.
ex: Congratulations on winning the race! // Your speech was great!
pt: Congratulating ucapan selamat ; Complimenting memuji ; Jawab dengan thank you
sum: Ucapan selamat dan pujian mempererat persahabatan.
fig: table Expression | Function ;; Congratulations! | memberi selamat ;; Happy birthday! | selamat ulang tahun ;; Well done! | memuji hasil kerja ;; You look nice today. | memuji penampilan ;; What a great idea! | memuji gagasan ;; Thank you very much. | merespons pujian ~ Ungkapan selamat dan pujian.
@ Be going to
min: 15
act: Write your plans for next holiday using be going to.
mis: lupa menambahkan am, is, atau are sebelum going to
exp: Be going to dipakai untuk menyatakan rencana atau niat yang sudah dipikirkan sebelumnya. Polanya subjek + am, is, atau are + going to + kata kerja pertama. Keterangan waktunya antara lain tomorrow, next week, dan this evening.
ex: I am going to visit Bali next month. // She is going to study tonight.
pt: Rencana atau niat ; Subjek + to be + going to + verb 1 ; Keterangan waktu mendatang
sum: Be going to menyatakan rencana.
fig: table Subject | To be ;; I | am going to ;; you | are going to ;; she | is going to ;; he | is going to read ;; we | are going to travel ;; they | are going to play ~ Pasangan subjek dan to be.
@ Greeting cards
min: 15
act: Make a greeting card for a family member's birthday in English.
mis: menulis kartu ucapan tanpa nama penerima dan pengirim
exp: Greeting card atau kartu ucapan berisi ucapan untuk acara tertentu, misalnya ulang tahun, hari raya, kelulusan, atau cepat sembuh. Bagiannya meliputi penerima, isi ucapan, harapan atau doa, dan pengirim. Bahasanya singkat, hangat, dan sopan.
ex: Dear Rina, happy birthday! Wish you all the best. // Get well soon, Grandpa.
pt: Ucapan untuk acara tertentu ; Penerima, ucapan, harapan, pengirim ; Singkat dan hangat
sum: Kartu ucapan menunjukkan perhatian kepada orang lain.
fig: table Occasion | Greeting ;; birthday | Happy birthday! ;; graduation | Happy graduation! ;; sickness | Get well soon! ;; Eid al-Fitr | Happy Eid! ;; new year | Happy New Year! ;; wedding | Happy wedding! ~ Ucapan pada kartu.
@ Expressing sympathy
min: 15
act: Practice a short dialogue showing sympathy to a friend who lost something.
mis: menertawakan teman yang sedang sedih
exp: Expressing sympathy adalah ungkapan simpati atau ikut prihatin atas kesulitan orang lain. Contohnya I'm sorry to hear that, That's too bad, dan I hope you feel better soon. Respons yang dapat diberikan adalah Thank you for your concern.
ex: I'm sorry to hear that you are sick. // That's too bad. I hope you find your bag.
pt: Ikut prihatin ; I'm sorry to hear that ; Respons thank you for your concern
sum: Ungkapan simpati menunjukkan kepedulian.
fig: table Situation | Expression of sympathy ;; a friend is sick | I hope you get well soon. ;; a friend lost a wallet | That's too bad. ;; a friend failed a test | Don't give up. ;; a pet died | I'm sorry to hear that. ;; a friend is sad | I'm here for you. ;; a flood hit a village | Our prayers are with them. ~ Ungkapan simpati.
# 2|People, Things, and Plans
@ Describing people
min: 15
act: Describe a family member's appearance and personality in five sentences.
mis: memakai has untuk menyatakan sifat seperti she has kind
exp: Mendeskripsikan orang meliputi penampilan fisik dan sifat. Penampilan memakai kata tall, short, slim, curly hair, dan round face. Sifat memakai kata kind, friendly, smart, dan diligent. Kalimat sifat memakai to be, misalnya She is kind, sedangkan ciri fisik dapat memakai has, misalnya She has long hair.
ex: My brother is tall and friendly. // My mother has curly hair.
pt: Penampilan dan sifat ; Is untuk sifat ; Has untuk ciri fisik
sum: Deskripsi yang baik membuat pembaca membayangkan orangnya.
fig: table Adjective | Meaning ;; tall | tinggi ;; slim | langsing ;; curly | keriting ;; friendly | ramah ;; diligent | rajin ;; generous | dermawan ~ Kata sifat untuk orang.
@ Adverbs of frequency
min: 15
act: Write your daily routines using always, usually, sometimes, and never.
mis: meletakkan adverb of frequency di akhir kalimat sembarangan
exp: Adverbs of frequency menunjukkan seberapa sering sesuatu dilakukan. Urutannya dari paling sering: always, usually, often, sometimes, seldom atau rarely, dan never. Kata ini biasanya diletakkan sebelum kata kerja utama atau sesudah to be.
ex: I always brush my teeth before bed. // She is never late.
pt: Menunjukkan seberapa sering ; Always sampai never ; Sebelum verb, sesudah to be
sum: Adverbs of frequency menjelaskan kebiasaan.
fig: table Adverb | Frequency ;; always | 100 persen ;; usually | 80 persen ;; often | 60 persen ;; sometimes | 40 persen ;; rarely | 10 persen ;; never | 0 persen ~ Tingkat adverbs of frequency.
@ Countable and uncountable nouns
min: 15
act: Sort items in your kitchen into countable and uncountable nouns.
mis: menulis two waters atau many sugar
exp: Countable nouns adalah benda yang dapat dihitung dan memiliki bentuk jamak, misalnya apple menjadi apples. Uncountable nouns tidak dapat dihitung langsung, misalnya water, sugar, dan rice. Many dipakai untuk countable nouns, much untuk uncountable nouns, dan a lot of untuk keduanya.
ex: How many eggs do we need? // How much sugar is in the jar?
pt: Countable punya bentuk jamak ; Uncountable tidak dihitung langsung ; Many dan much
sum: Jenis kata benda menentukan pemakaian many atau much.
fig: table Noun | Type ;; apple | countable ;; egg | countable jamak eggs ;; water | uncountable ;; sugar | uncountable butiran ;; book | countable jamak books ;; rice | uncountable makanan pokok ~ Countable dan uncountable nouns.
@ Offering help
min: 15
act: Role-play offering help to a neighbor carrying heavy bags.
mis: menolak bantuan dengan kasar
exp: Offering help adalah menawarkan bantuan kepada orang lain. Ungkapannya antara lain Can I help you?, May I help you?, dan Let me help you. Untuk menerima bantuan, katakan Yes, please atau Thank you. Untuk menolak dengan sopan, katakan No, thanks. I can do it myself.
ex: Let me carry your bag. // No, thanks. I can manage.
pt: Menawarkan bantuan ; Can I help you? ; Menerima atau menolak dengan sopan
sum: Menawarkan bantuan menunjukkan kepedulian.
fig: table Expression | Use ;; Can I help you? | menawarkan bantuan ;; Let me help you. | menawarkan langsung ;; Yes, please. | menerima tawaran ;; That's very kind of you. | menerima dengan terima kasih ;; No, thanks. | menolak dengan sopan ;; I can do it myself. | menolak karena mampu ~ Ungkapan menawarkan bantuan.
@ Making appointments
min: 15
act: Practice making an appointment with a friend to study together.
mis: membuat janji tanpa menyebutkan waktu dan tempat
exp: Making an appointment adalah membuat janji bertemu. Ungkapannya antara lain Can we meet tomorrow?, How about at four o'clock?, dan Let's meet at the library. Respons menerima seperti Sure, see you then, dan menolak seperti Sorry, I can't. How about Monday?
ex: Can we meet at the library at 3 p.m.? // Sorry, I'm busy. How about tomorrow?
pt: Membuat janji bertemu ; Sebutkan waktu dan tempat ; Menerima atau mengusulkan waktu lain
sum: Janji yang jelas memudahkan pertemuan.
fig: table Expression | Function ;; Can we meet tomorrow? | mengajak bertemu ;; How about at four? | mengusulkan waktu ;; Let's meet at the library. | mengusulkan tempat ;; Sure, see you then. | menerima janji ;; Sorry, I can't. | menolak janji ;; Can we make it Monday? | mengubah jadwal ~ Ungkapan membuat janji.
@ Simple future with will
min: 15
act: Write five predictions about your life ten years from now using will.
mis: menulis will diikuti kata kerja berakhiran -s atau -ed
exp: Simple future dengan will dipakai untuk prediksi, keputusan spontan, dan janji. Polanya subjek + will + kata kerja pertama. Bentuk negatifnya will not atau won't. Kalimat tanya memakai Will + subjek + kata kerja pertama.
ex: It will rain this afternoon. // I will help you with your homework.
pt: Prediksi, keputusan spontan, janji ; Subjek + will + verb 1 ; Negatif won't
sum: Will dipakai untuk masa depan yang tidak direncanakan.
fig: table Sentence | Use of will ;; It will rain later. | prediksi ;; I will open the door. | keputusan spontan ;; I will always help you. | janji ;; Will you come? | pertanyaan ;; She won't be late. | negatif ;; We will win the game. | keyakinan ~ Fungsi will.

## PPK
# 1|Ideologi dan Demokrasi
@ Pancasila dan ideologi dunia
min: 15
act: Buat tabel perbandingan Pancasila dengan liberalisme dan sosialisme.
mis: mengira Pancasila meniru ideologi negara lain
exp: Ideologi adalah kumpulan gagasan dasar yang menjadi pedoman hidup bernegara. Ideologi besar dunia antara lain liberalisme yang mengutamakan kebebasan individu dan sosialisme yang mengutamakan kepentingan bersama. Pancasila berbeda karena menyeimbangkan kepentingan individu dan masyarakat serta berlandaskan ketuhanan.
ex: Pancasila mengakui hak milik pribadi yang berfungsi sosial. // Pancasila menempatkan musyawarah dalam pengambilan keputusan.
pt: Ideologi pedoman bernegara ; Liberalisme dan sosialisme ; Pancasila menyeimbangkan individu dan masyarakat
sum: Pancasila adalah ideologi khas bangsa Indonesia.
fig: table Ideologi | Ciri utama ;; liberalisme | kebebasan individu ;; sosialisme | kepentingan bersama ;; komunisme | menolak hak milik pribadi ;; fasisme | kekuasaan mutlak negara ;; kapitalisme | pasar bebas ;; Pancasila | keseimbangan individu dan masyarakat ~ Ideologi dunia.
@ Demokrasi Pancasila
min: 15
act: Amati cara pemilihan ketua kelas, lalu tentukan prinsip demokrasi yang diterapkan.
mis: menganggap demokrasi berarti bebas tanpa batas
exp: Demokrasi adalah pemerintahan dari rakyat, oleh rakyat, dan untuk rakyat. Demokrasi Pancasila adalah demokrasi yang dijiwai nilai-nilai Pancasila, mengutamakan musyawarah mufakat, menghormati hak asasi, dan bertanggung jawab kepada Tuhan. Kebebasan dalam demokrasi dibatasi oleh hukum dan hak orang lain.
ex: Musyawarah untuk menentukan kegiatan kelas. // Menghargai pendapat yang berbeda.
pt: Dari, oleh, untuk rakyat ; Mengutamakan musyawarah mufakat ; Kebebasan dibatasi hukum
sum: Demokrasi Pancasila menyeimbangkan kebebasan dan tanggung jawab.
fig: table Prinsip demokrasi | Contoh ;; kedaulatan rakyat | pemilu ;; musyawarah | rapat kelas ;; persamaan di depan hukum | semua warga diadili sama ;; kebebasan berpendapat | menyampaikan usul ;; pembatasan kekuasaan | masa jabatan presiden ;; penghormatan HAM | menghargai perbedaan ~ Prinsip demokrasi.
@ Makna Pembukaan UUD 1945
min: 15
act: Baca Pembukaan UUD 1945, lalu tandai bagian yang memuat tujuan negara.
mis: mengira Pembukaan UUD 1945 boleh diubah seperti pasal-pasalnya
exp: Pembukaan UUD 1945 terdiri atas empat alinea. Alinea pertama menyatakan kemerdekaan adalah hak segala bangsa. Alinea kedua memuat perjuangan pergerakan kemerdekaan. Alinea ketiga memuat pernyataan kemerdekaan atas berkat rahmat Allah. Alinea keempat memuat tujuan negara dan dasar negara Pancasila. Pembukaan tidak boleh diubah.
ex: Mencerdaskan kehidupan bangsa termasuk tujuan negara. // Penjajahan harus dihapuskan karena tidak sesuai perikemanusiaan.
pt: Empat alinea ; Alinea keempat memuat tujuan dan dasar negara ; Pembukaan tidak boleh diubah
sum: Pembukaan UUD 1945 memuat cita-cita bangsa.
fig: table Alinea | Isi pokok ;; pertama | kemerdekaan hak segala bangsa ;; kedua | perjuangan pergerakan kemerdekaan ;; ketiga | pernyataan kemerdekaan ;; keempat | tujuan dan dasar negara ;; tujuan pertama | melindungi segenap bangsa ;; tujuan ketiga | mencerdaskan kehidupan bangsa ~ Isi Pembukaan UUD 1945.
@ Kemerdekaan berpendapat
min: 15
act: Tulis satu usul untuk sekolah, lalu sampaikan dengan sopan kepada wali kelas.
mis: menyampaikan pendapat dengan menghina orang lain
exp: Kemerdekaan berpendapat dijamin Pasal 28E ayat 3 UUD 1945. Pendapat dapat disampaikan secara lisan maupun tulisan, misalnya melalui musyawarah, surat, media massa, atau unjuk rasa damai. Pendapat harus disampaikan dengan sopan, bertanggung jawab, berdasarkan fakta, dan tidak melanggar hak orang lain.
ex: Menyampaikan usul di rapat OSIS. // Menulis surat pembaca di koran.
pt: Dijamin Pasal 28E ayat 3 ; Lisan atau tulisan ; Sopan dan bertanggung jawab
sum: Kebebasan berpendapat disertai tanggung jawab.
fig: table Saluran pendapat | Bentuk ;; rapat kelas | lisan langsung ;; surat pembaca | tulisan di media ;; kotak saran | tulisan tertutup ;; diskusi | lisan bersama ;; unjuk rasa damai | aksi bersama ;; petisi | tanda tangan dukungan ~ Saluran menyampaikan pendapat.
@ Sistem pemerintahan Indonesia
min: 15
act: Cari tahu nama presiden, wakil presiden, dan tiga menteri saat ini.
mis: mengira menteri bertanggung jawab kepada DPR
exp: Indonesia menganut sistem pemerintahan presidensial. Presiden adalah kepala negara sekaligus kepala pemerintahan. Presiden dipilih langsung oleh rakyat untuk masa jabatan lima tahun dan dapat dipilih kembali satu kali. Menteri diangkat dan diberhentikan oleh presiden serta bertanggung jawab kepada presiden.
ex: Presiden membentuk kabinet. // Presiden dan wakil presiden dipilih dalam pemilu.
pt: Sistem presidensial ; Presiden kepala negara dan pemerintahan ; Menteri bertanggung jawab kepada presiden
sum: Presiden memimpin pemerintahan dalam sistem presidensial.
fig: table Ciri presidensial | Penjelasan ;; kepala negara | presiden ;; kepala pemerintahan | juga presiden ;; pemilihan presiden | langsung oleh rakyat ;; masa jabatan | lima tahun ;; menteri | pembantu presiden ;; batas jabatan | dua periode ~ Ciri sistem presidensial.
@ Musyawarah dalam demokrasi
min: 15
act: Pimpin musyawarah keluarga untuk menentukan menu makan akhir pekan.
mis: memaksakan pendapat saat musyawarah
exp: Musyawarah adalah pembahasan bersama untuk mencapai keputusan. Musyawarah mencerminkan sila keempat Pancasila. Dalam musyawarah, setiap peserta berhak berpendapat, wajib mendengarkan, dan menghormati keputusan. Jika mufakat tidak tercapai, keputusan diambil dengan pemungutan suara.
ex: Musyawarah menentukan tujuan karyawisata. // Semua peserta melaksanakan hasil mufakat.
pt: Pembahasan bersama ; Mencerminkan sila keempat ; Mufakat atau voting
sum: Musyawarah menghasilkan keputusan yang adil.
fig: table Peran | Sikap dalam musyawarah ;; pemimpin | memberi kesempatan semua bicara ;; peserta | menyampaikan pendapat dengan sopan ;; pendengar | menyimak tanpa memotong ;; notulis | mencatat hasil ;; peserta yang kalah suara | menerima keputusan ;; semua anggota | melaksanakan hasil ~ Sikap dalam musyawarah.
# 2|Wawasan Kebangsaan
@ Wawasan Nusantara
min: 15
act: Lihat peta Indonesia, lalu jelaskan mengapa laut dianggap pemersatu, bukan pemisah.
mis: menganggap laut memisahkan pulau-pulau Indonesia
exp: Wawasan Nusantara adalah cara pandang bangsa Indonesia tentang diri dan lingkungannya yang mengutamakan persatuan wilayah dan bangsa. Laut dipandang sebagai pemersatu pulau-pulau. Wawasan Nusantara diperjuangkan melalui Deklarasi Djuanda 1957 dan diakui dunia lewat UNCLOS 1982.
ex: Deklarasi Djuanda menyatukan wilayah laut Indonesia. // Indonesia disebut negara kepulauan.
pt: Cara pandang persatuan ; Laut sebagai pemersatu ; Deklarasi Djuanda dan UNCLOS
sum: Wawasan Nusantara menyatukan wilayah Indonesia.
fig: table Peristiwa | Tahun ;; Deklarasi Djuanda | 1957 ;; Sumpah Pemuda | 1928 ;; Proklamasi | 1945 ;; UNCLOS | 1982 ;; Undang-undang Wawasan Nusantara | 1960 ;; Hari Nusantara pertama | 2001 ~ Peristiwa penting kesatuan wilayah.
@ Ketahanan nasional
min: 15
act: Sebutkan satu contoh ketahanan di bidang ekonomi yang ada di lingkungan rumahmu.
mis: mengira ketahanan nasional hanya urusan militer
exp: Ketahanan nasional adalah kondisi dinamis bangsa yang ulet dan tangguh dalam menghadapi ancaman. Ketahanan nasional mencakup bidang ideologi, politik, ekonomi, sosial budaya, dan pertahanan keamanan. Setiap warga negara dapat berperan, misalnya dengan menjaga persatuan dan mencintai produk dalam negeri.
ex: Petani menjaga ketahanan pangan. // Pelajar menolak paham yang bertentangan dengan Pancasila.
pt: Kondisi ulet dan tangguh ; Ideologi, politik, ekonomi, sosbud, hankam ; Semua warga berperan
sum: Ketahanan nasional dijaga oleh seluruh rakyat.
fig: table Bidang | Contoh ketahanan ;; ideologi | memegang teguh Pancasila ;; politik | pemilu yang tertib ;; ekonomi | membeli produk lokal ;; sosial budaya | melestarikan budaya ;; pertahanan | menjaga perbatasan ;; pangan | swasembada beras ~ Bidang ketahanan nasional.
@ Sikap terhadap budaya asing
min: 15
act: Diskusikan dengan keluarga budaya asing yang positif dan negatif bagi remaja.
mis: menerima semua budaya asing tanpa menyaring
exp: Globalisasi membawa budaya asing masuk ke Indonesia. Budaya asing yang positif, seperti disiplin dan menghargai waktu, dapat ditiru. Budaya asing yang negatif, seperti gaya hidup konsumtif dan individualis, harus dihindari. Sikap yang tepat adalah selektif, kritis, dan tetap melestarikan budaya sendiri.
ex: Meniru budaya antre dengan tertib. // Menolak gaya hidup boros.
pt: Budaya asing masuk lewat globalisasi ; Tiru yang positif ; Selektif dan kritis
sum: Kita boleh terbuka, tetapi tetap berjati diri Indonesia.
fig: table Budaya asing | Sikap ;; disiplin waktu | ditiru ;; budaya antre | ditiru dengan tertib ;; gaya hidup konsumtif | dihindari ;; individualisme | dihindari karena egois ;; etos kerja keras | ditiru untuk maju ;; pergaulan bebas | ditolak ~ Sikap terhadap budaya asing.
@ Bangga produk dalam negeri
min: 15
act: Periksa lima barang di rumahmu dan catat mana yang buatan Indonesia.
mis: menganggap produk impor selalu lebih baik
exp: Mencintai produk dalam negeri adalah wujud cinta tanah air. Membeli produk lokal membantu usaha kecil, membuka lapangan kerja, dan memperkuat ekonomi nasional. Pemerintah mendorong gerakan Bangga Buatan Indonesia. Produk dalam negeri antara lain batik, makanan khas, dan aplikasi digital karya anak bangsa.
ex: Memakai batik pada hari tertentu. // Membeli camilan dari UMKM sekitar.
pt: Wujud cinta tanah air ; Membantu usaha kecil dan lapangan kerja ; Gerakan Bangga Buatan Indonesia
sum: Membeli produk lokal ikut membangun negeri.
fig: table Tindakan | Manfaat ;; membeli batik lokal | perajin sejahtera ;; makan di warung UMKM | usaha kecil tumbuh ;; memakai aplikasi lokal | teknologi anak bangsa maju ;; berwisata di dalam negeri | pariwisata berkembang ;; membeli buah lokal | petani untung ;; mempromosikan produk daerah | dikenal luas ~ Manfaat bangga produk dalam negeri.
@ Hak-hak anak
min: 15
act: Buat poster tentang hak anak yang perlu dijaga di sekolah.
mis: mengira hak anak hanya hak bermain
exp: Anak adalah setiap orang yang berusia di bawah 18 tahun. Hak anak dilindungi Undang-Undang Perlindungan Anak dan Konvensi Hak Anak PBB. Hak anak antara lain hak hidup, hak mendapat nama dan identitas, hak pendidikan, hak kesehatan, hak bermain, dan hak dilindungi dari kekerasan. Anak juga memiliki kewajiban, seperti menghormati orang tua dan guru.
ex: Setiap anak berhak bersekolah. // Anak berhak mendapat akta kelahiran.
pt: Usia di bawah 18 tahun ; UU Perlindungan Anak dan Konvensi Hak Anak ; Hak pendidikan, kesehatan, perlindungan
sum: Hak anak wajib dihormati semua pihak.
fig: table Hak anak | Contoh pemenuhan ;; hak identitas | akta kelahiran ;; hak pendidikan | bersekolah ;; hak kesehatan | imunisasi ;; hak bermain | waktu istirahat ;; hak perlindungan | bebas dari kekerasan ;; hak berpendapat | didengar suaranya ~ Hak anak.
@ Organisasi kepemudaan
min: 15
act: Cari informasi organisasi pemuda di lingkunganmu, seperti Karang Taruna atau Pramuka.
mis: menganggap organisasi pemuda hanya tempat berkumpul tanpa manfaat
exp: Organisasi kepemudaan adalah wadah bagi pemuda untuk mengembangkan diri dan berkontribusi bagi masyarakat. Contohnya Pramuka, OSIS, Palang Merah Remaja, dan Karang Taruna. Organisasi melatih kepemimpinan, kerja sama, tanggung jawab, dan kepedulian sosial.
ex: OSIS mengadakan kegiatan bakti sosial. // Pramuka melatih kemandirian.
pt: Wadah pengembangan diri ; Pramuka, OSIS, PMR, Karang Taruna ; Melatih kepemimpinan dan kepedulian
sum: Organisasi membentuk pemuda yang tangguh dan peduli.
fig: table Organisasi | Kegiatan utama ;; Pramuka | kepanduan dan kemandirian ;; OSIS | kegiatan siswa di sekolah ;; Palang Merah Remaja | pertolongan pertama ;; Karang Taruna | sosial di kampung ;; Paskibra | pengibaran bendera ;; Rohis | kerohanian ~ Organisasi kepemudaan.
"""

BANK += """
## BIG|Simple past tense
Simple past tense is used for actions …|in the past|now|in the future|every day|Lampau.
The past form of visit is …|visited|visits|visiting|visit|-ed.
=|Complete: I … (play) football yesterday.|played|Played.
=|Complete: … you watch the match last night?|Did|Did.
B|"She was happy" is in the simple past tense.|Was.
S|"I did not played" is correct.|Did not play.
The correct negative sentence is …|I did not go to school.|I not went to school.|I did not went to school.|I no go to school.|Did + V1.
Which time signal is for the past?|yesterday|tomorrow|next week|now|Yesterday.
## BIG|Irregular verbs
The past form of go is …|went|goed|gone|goes|Went.
The past form of eat is …|ate|eated|eaten|eats|Ate.
=|The past form of buy is …|bought|Bought.
=|The past form of write is …|wrote|Wrote.
B|Play is a regular verb.|Played.
S|The past form of see is seed.|Saw.
The past form of swim is …|swam|swimmed|swum|swims|Swam.
Which verb is irregular?|bring|walk|clean|cook|Brought.
## BIG|Congratulating and complimenting
"Congratulations on your success" is used to …|congratulate|apologize|invite|complain|Selamat.
A good response to a compliment is …|Thank you.|Never mind.|Sorry.|Go away.|Thanks.
=|Complete: … done! Your project is great.|Well|Well done.
=|"What a beautiful drawing!" is an expression of …|compliment;complimenting|Pujian.
B|"Happy birthday!" is a greeting for a birthday.|Birthday.
S|"I'm sorry" is a common response to a compliment.|Thank you.
"You look nice today" compliments someone's …|appearance|idea|homework|cooking|Penampilan.
Which expression congratulates a winner?|Congratulations on winning!|Get well soon!|Sorry to hear that.|See you later.|Menang.
## BIG|Be going to
Be going to is used to express …|plans|past events|habits|commands|Rencana.
Complete: She … going to study tonight.|is|am|are|be|She is.
=|Complete: I … going to visit Bali.|am|I am.
=|Complete: They … going to play futsal.|are|They are.
B|"We are going to travel" shows a plan.|Rencana.
S|"He going to read" is a correct sentence.|He is going to.
After going to, we use the verb in …|the first form|the second form|-ing form|-ed form|V1.
Which sentence is correct?|I am going to cook.|I going to cook.|I am going to cooked.|I is going to cook.|Pola.
## BIG|Greeting cards
"Get well soon" is written for someone who is …|sick|getting married|graduating|having a birthday|Sakit.
A greeting card usually includes the receiver and the …|sender|price|address only|recipe|Pengirim.
=|The greeting for a birthday is "Happy …!"|birthday|Birthday.
=|The greeting for graduation is "Happy …!"|graduation|Graduation.
B|"Happy Eid!" is a greeting for Eid al-Fitr.|Eid.
S|A greeting card should be very long and formal.|Singkat.
"Happy New Year!" is used on …|January 1|August 17|the last day of school|a sick day|Tahun baru.
The language of a greeting card is usually …|short and warm|long and rude|scientific|full of numbers|Hangat.
## BIG|Expressing sympathy
"I'm sorry to hear that" expresses …|sympathy|congratulation|invitation|agreement|Simpati.
A good response to sympathy is …|Thank you for your concern.|Congratulations!|Well done!|Happy birthday!|Terima kasih.
=|Complete: That's too … I hope you find your bag.|bad|Too bad.
=|To a sick friend we say: I hope you get … soon.|well|Get well.
B|"I'm here for you" shows care.|Peduli.
S|Laughing at a sad friend shows sympathy.|Tidak.
"Don't give up" is suitable for a friend who …|failed a test|won a prize|has a birthday|is getting married|Gagal.
Which expression shows sympathy?|That's too bad.|Well done!|Congratulations!|Good job!|Simpati.
## BIG|Describing people
The opposite of tall is …|short|slim|big|curly|Pendek.
"Friendly" means …|ramah|rajin|pemalu|pemarah|Ramah.
=|Complete: My mother … curly hair.|has|Has.
=|Complete: My brother … kind.|is|Is.
B|"Diligent" means rajin.|Rajin.
S|"She has kind" is a correct sentence.|She is kind.
"Generous" means …|dermawan|kikir|pemalas|sombong|Dermawan.
Which word describes personality?|smart|curly|tall|slim|Sifat.
## BIG|Adverbs of frequency
The adverb that means 100 percent is …|always|never|sometimes|often|Always.
The adverb that means 0 percent is …|never|always|usually|often|Never.
=|Complete: She is … late. (0 percent)|never|Never.
=|"Sometimes" is about … percent.|40|40.
B|Adverbs of frequency usually come before the main verb.|Posisi.
S|"Rarely" means very often.|Jarang.
The correct sentence is …|I always brush my teeth.|I brush always my teeth.|Always I brush teeth my.|I brush my teeth always am.|Posisi.
"Usually" is about … percent.|80|10|0|100|80.
## BIG|Countable and uncountable nouns
Which noun is uncountable?|water|apple|egg|book|Water.
We use "many" with …|countable nouns|uncountable nouns|verbs|adjectives|Countable.
=|Complete: How … sugar is in the jar?|much|Much.
=|Complete: How … eggs do we need?|many|Many.
B|"Apple" is a countable noun.|Countable.
S|"Two waters" is the correct form.|Two glasses of water.
Which phrase is correct?|a lot of rice|many rice|two rices|a rices|A lot of.
Which noun is countable?|book|rice|sugar|milk|Book.
## BIG|Offering help
"Can I help you?" is an expression of …|offering help|asking permission|complaining|apologizing|Menawarkan.
To accept help politely, we say …|Yes, please.|Go away.|No way.|Leave me.|Menerima.
=|Complete: Let me … you carry the bag.|help|Help.
=|To refuse help politely: No, …|thanks;thank you|No, thanks.
B|"That's very kind of you" accepts help politely.|Terima.
S|Refusing help rudely is polite.|Sopan.
"I can do it myself" is used to …|refuse help|offer help|ask for help|say goodbye|Menolak.
Which expression offers help?|May I help you?|Can you help me?|Help!|Where is it?|Menawarkan.
## BIG|Making appointments
"Can we meet tomorrow?" is used to …|make an appointment|apologize|congratulate|describe|Janji.
To accept an appointment, we say …|Sure, see you then.|Sorry, I can't.|No idea.|Never mind.|Menerima.
=|Complete: How … at four o'clock?|about|How about.
=|Complete: Let's … at the library.|meet|Meet.
B|An appointment should include time and place.|Jelas.
S|"Sorry, I can't" accepts an appointment.|Menolak.
"Can we make it Monday?" is used to …|change the schedule|accept|end a call|greet|Ubah jadwal.
Which sentence suggests a place?|Let's meet at the park.|How about at three?|Sure, see you.|Sorry, I'm busy.|Tempat.
## BIG|Simple future with will
"It will rain later" expresses a …|prediction|habit|past event|command|Prediksi.
The short form of will not is …|won't|willn't|wont|wan't|Won't.
=|Complete: I … help you with your homework.|will|Will.
=|Complete: … you come to my party?|Will|Will.
B|After will we use the first form of the verb.|V1.
S|"She will goes" is correct.|Will go.
"I will open the door" shows a …|spontaneous decision|past habit|daily routine|completed action|Spontan.
Which sentence is correct?|We will win the game.|We will won the game.|We wills win.|We will winning.|Pola.
## PPK|Pancasila dan ideologi dunia
Ideologi yang mengutamakan kebebasan individu adalah …|liberalisme|sosialisme|komunisme|fasisme|Liberalisme.
Ideologi yang mengutamakan kepentingan bersama adalah …|sosialisme|liberalisme|kapitalisme|individualisme|Sosialisme.
=|Kumpulan gagasan dasar pedoman bernegara disebut …|ideologi|Ideologi.
=|Ideologi yang menolak hak milik pribadi adalah …|komunisme|Komunisme.
B|Pancasila menyeimbangkan kepentingan individu dan masyarakat.|Seimbang.
S|Pancasila meniru ideologi liberal secara utuh.|Khas.
Ideologi yang menekankan kekuasaan mutlak negara adalah …|fasisme|liberalisme|Pancasila|sosialisme|Fasisme.
Ideologi yang bertumpu pada pasar bebas adalah …|kapitalisme|komunisme|fasisme|sosialisme|Kapitalisme.
## PPK|Demokrasi Pancasila
Demokrasi adalah pemerintahan dari, oleh, dan untuk …|rakyat|presiden|partai|tentara|Rakyat.
Demokrasi Pancasila mengutamakan …|musyawarah mufakat|kekerasan|kehendak satu orang|suara terbanyak tanpa diskusi|Musyawarah.
=|Kebebasan dalam demokrasi dibatasi oleh …|hukum|Hukum.
=|Prinsip demokrasi yang diwujudkan melalui pemilu adalah kedaulatan …|rakyat|Rakyat.
B|Pembatasan masa jabatan presiden termasuk prinsip demokrasi.|Pembatasan.
S|Demokrasi berarti bebas tanpa batas.|Dibatasi.
Semua warga diadili dengan cara sama mencerminkan prinsip …|persamaan di depan hukum|kebebasan pers|pembatasan kekuasaan|musyawarah|Persamaan.
Demokrasi Pancasila bertanggung jawab kepada Tuhan dan …|rakyat|negara asing|partai saja|pengusaha|Rakyat.
## PPK|Makna Pembukaan UUD 1945
Pembukaan UUD 1945 terdiri atas … alinea.|empat|tiga|lima|enam|Empat.
Tujuan negara terdapat pada alinea …|keempat|pertama|kedua|ketiga|Keempat.
=|Kemerdekaan adalah hak segala bangsa dinyatakan pada alinea …|pertama;1|Pertama.
=|Dasar negara Pancasila tercantum pada alinea …|keempat;4|Keempat.
B|Pembukaan UUD 1945 tidak boleh diubah.|Tetap.
S|Pembukaan UUD 1945 sudah diamandemen empat kali.|Pasal yang diamandemen.
Mencerdaskan kehidupan bangsa adalah tujuan negara yang ke …|tiga|satu|dua|empat|Ketiga.
Pernyataan kemerdekaan atas berkat rahmat Allah terdapat pada alinea …|ketiga|pertama|kedua|keempat|Ketiga.
## PPK|Kemerdekaan berpendapat
Kemerdekaan berpendapat dijamin Pasal … UUD 1945.|28E ayat 3|31 ayat 1|33 ayat 3|27 ayat 3|28E.
Pendapat sebaiknya disampaikan dengan …|sopan|menghina|berteriak kasar|berbohong|Sopan.
=|Pendapat dapat disampaikan secara lisan maupun …|tulisan;tertulis|Tulisan.
=|Menulis pendapat di koran disebut surat …|pembaca|Surat pembaca.
B|Pendapat harus berdasarkan fakta.|Fakta.
S|Kebebasan berpendapat boleh menghina orang lain.|Tidak boleh.
Kumpulan tanda tangan dukungan atas suatu usul disebut …|petisi|notulen|surat pembaca|kotak saran|Petisi.
Kotak saran merupakan saluran pendapat secara …|tulisan tertutup|lisan langsung|unjuk rasa|diskusi|Tertutup.
## PPK|Sistem pemerintahan Indonesia
Sistem pemerintahan Indonesia adalah …|presidensial|parlementer|monarki|komunis|Presidensial.
Menteri bertanggung jawab kepada …|presiden|DPR|MPR|rakyat langsung|Presiden.
=|Masa jabatan presiden adalah … tahun.|5;lima|Lima.
=|Presiden adalah kepala negara sekaligus kepala …|pemerintahan|Pemerintahan.
B|Presiden dipilih langsung oleh rakyat.|Pemilu.
S|Menteri bertanggung jawab kepada DPR.|Presiden.
Presiden hanya dapat menjabat paling lama …|dua periode|satu periode|tiga periode|seumur hidup|Dua periode.
Menteri diangkat dan diberhentikan oleh …|presiden|DPR|MA|rakyat|Presiden.
## PPK|Musyawarah dalam demokrasi
Musyawarah mencerminkan sila …|keempat|pertama|kedua|kelima|Sila keempat.
Jika mufakat tidak tercapai, keputusan diambil dengan …|pemungutan suara|paksaan|undian sembarang|kekerasan|Voting.
=|Orang yang mencatat hasil musyawarah disebut …|notulis|Notulis.
=|Pendengar yang baik menyimak tanpa …|memotong;menyela|Tidak memotong.
B|Semua anggota wajib melaksanakan hasil musyawarah.|Wajib.
S|Dalam musyawarah boleh memaksakan pendapat.|Tidak boleh.
Pemimpin musyawarah sebaiknya …|memberi kesempatan semua bicara|berbicara sendiri|memaksa peserta|mengabaikan usul|Adil.
Peserta yang kalah suara sebaiknya …|menerima keputusan|keluar ruangan|marah|menolak hasil|Menerima.
## PPK|Wawasan Nusantara
Dalam Wawasan Nusantara, laut dipandang sebagai …|pemersatu|pemisah|penghalang|batas negara lain|Pemersatu.
Deklarasi Djuanda dicetuskan pada tahun …|1957|1945|1982|1928|1957.
=|Hukum laut internasional yang mengakui negara kepulauan disebut …|UNCLOS|UNCLOS.
=|UNCLOS disepakati pada tahun …|1982|1982.
B|Indonesia disebut negara kepulauan.|Kepulauan.
S|Wawasan Nusantara memandang laut sebagai pemisah pulau.|Pemersatu.
Wawasan Nusantara mengutamakan persatuan wilayah dan …|bangsa|partai|agama tertentu|suku tertentu|Bangsa.
Hari Nusantara diperingati sejak tahun …|2001|1957|1945|1982|2001.
## PPK|Ketahanan nasional
Ketahanan nasional adalah kondisi bangsa yang ulet dan …|tangguh|lemah|malas|terpecah|Tangguh.
Membeli produk lokal memperkuat ketahanan bidang …|ekonomi|ideologi|politik|militer|Ekonomi.
=|Melestarikan budaya memperkuat ketahanan bidang sosial …|budaya|Sosial budaya.
=|Swasembada beras termasuk ketahanan …|pangan|Pangan.
B|Setiap warga negara dapat berperan menjaga ketahanan nasional.|Semua.
S|Ketahanan nasional hanya urusan tentara.|Semua bidang.
Memegang teguh Pancasila memperkuat ketahanan bidang …|ideologi|ekonomi|pangan|olahraga|Ideologi.
Menjaga perbatasan termasuk ketahanan bidang …|pertahanan|ekonomi|budaya|pendidikan|Pertahanan.
## PPK|Sikap terhadap budaya asing
Sikap yang tepat terhadap budaya asing adalah …|selektif|menerima semua|menolak semua|meniru tanpa berpikir|Selektif.
Budaya asing yang positif adalah …|disiplin waktu|gaya hidup boros|pergaulan bebas|individualisme|Positif.
=|Gaya hidup suka membeli barang berlebihan disebut …|konsumtif|Konsumtif.
=|Budaya asing masuk melalui proses …|globalisasi|Globalisasi.
B|Budaya antre dapat ditiru.|Positif.
S|Semua budaya asing harus diterima tanpa disaring.|Selektif.
Sikap mementingkan diri sendiri disebut …|individualisme|gotong royong|toleransi|patriotisme|Individualis.
Etos kerja keras dari budaya asing sebaiknya …|ditiru|ditolak|diabaikan|dilarang|Ditiru.
## PPK|Bangga produk dalam negeri
Mencintai produk dalam negeri adalah wujud …|cinta tanah air|egoisme|konsumtif|primordialisme|Cinta tanah air.
Membeli produk UMKM membantu …|usaha kecil tumbuh|perusahaan asing|harga impor naik|pengangguran bertambah|UMKM.
=|Gerakan pemerintah untuk produk lokal disebut Bangga Buatan …|Indonesia|Indonesia.
=|Membeli buah lokal menguntungkan …|petani|Petani.
B|Berwisata di dalam negeri membantu pariwisata berkembang.|Pariwisata.
S|Produk impor pasti lebih baik daripada produk lokal.|Belum tentu.
Memakai batik membantu kesejahteraan …|perajin batik|pabrik asing|importir|turis|Perajin.
Memakai aplikasi karya anak bangsa membantu kemajuan …|teknologi lokal|budaya asing|impor|monopoli|Teknologi.
## PPK|Hak-hak anak
Menurut undang-undang, anak adalah orang yang berusia di bawah … tahun.|18|12|15|21|18.
Akta kelahiran merupakan pemenuhan hak …|identitas|bermain|kesehatan|berpendapat|Identitas.
=|Imunisasi merupakan pemenuhan hak …|kesehatan|Kesehatan.
=|Bersekolah merupakan pemenuhan hak …|pendidikan|Pendidikan.
B|Anak berhak dilindungi dari kekerasan.|Perlindungan.
S|Hak anak hanyalah hak bermain.|Banyak hak.
Konvensi Hak Anak dibuat oleh …|PBB|ASEAN|DPR|OSIS|PBB.
Kewajiban anak antara lain …|menghormati orang tua dan guru|bekerja berat|tidak bersekolah|menuntut hak saja|Kewajiban.
## PPK|Organisasi kepemudaan
Organisasi siswa di sekolah disebut …|OSIS|Karang Taruna|PMI|KPU|OSIS.
Organisasi pemuda di kampung disebut …|Karang Taruna|OSIS|Paskibra|Rohis|Karang Taruna.
=|Organisasi kepanduan yang melatih kemandirian adalah …|Pramuka|Pramuka.
=|Palang Merah Remaja disingkat …|PMR|PMR.
B|Organisasi melatih kepemimpinan.|Kepemimpinan.
S|Organisasi pemuda tidak memberi manfaat apa pun.|Bermanfaat.
Paskibra bertugas …|mengibarkan bendera|memberi pertolongan pertama|mengurus kebun|berdagang|Bendera.
PMR berkegiatan dalam bidang …|pertolongan pertama|pengibaran bendera|olahraga|kesenian|PMR.
"""

SAS += """
## BIG 1
0|"They were at school." The sentence is in the ....|simple past tense|simple present tense|future tense|present continuous|Were.
1|The past form of "see" is ....|saw|seed|seen|sees|Saw.
2|"What a great idea!" is used to compliment someone's ....|idea|appearance|house|car|Gagasan.
3|"We are going to travel next week." The sentence expresses a ....|plan|habit|past event|command|Rencana.
4|"Happy wedding!" is written on a card for a ....|wedding|birthday|graduation|sick friend|Pernikahan.
5|"Our prayers are with them" is said when ....|a flood hits a village|a friend wins|a friend has a birthday|a friend graduates|Bencana.
## BIG 2
0|"Slim" means ....|langsing|tinggi|keriting|ramah|Slim.
1|"Often" is about ... percent.|60|100|0|10|Often.
2|"Milk" is a/an ... noun.|uncountable|countable|plural|proper|Milk.
3|"Let me help you" is used to ....|offer help|refuse help|ask for help|apologize|Offer.
4|"How about at four?" is used to suggest a ....|time|place|food|friend|Waktu.
5|"She won't be late" is a ... sentence.|negative|positive|question|command|Won't.
## PPK 1
0|Pancasila sebagai ideologi menekankan keseimbangan antara ....|individu dan masyarakat|negara dan partai|pasar dan modal|kaya dan miskin|Seimbang.
1|Contoh prinsip penghormatan HAM dalam demokrasi adalah ....|menghargai perbedaan|memaksa pendapat|melarang usul|mengabaikan hak|HAM.
2|Melindungi segenap bangsa Indonesia termasuk tujuan negara yang ....|pertama|kedua|ketiga|keempat|Pertama.
3|Diskusi termasuk saluran pendapat secara ....|lisan bersama|tulisan tertutup|tanda tangan|surat|Diskusi.
4|Menteri berkedudukan sebagai ....|pembantu presiden|kepala negara|wakil rakyat|hakim|Pembantu.
5|Tugas notulis dalam musyawarah adalah ....|mencatat hasil|memimpin rapat|memutuskan sendiri|membubarkan rapat|Notulis.
## PPK 2
0|Undang-undang tentang Wawasan Nusantara pertama kali disahkan tahun ....|1960|1957|1982|2001|1960.
1|Pemilu yang tertib memperkuat ketahanan bidang ....|politik|ekonomi|pangan|budaya|Politik.
2|Pergaulan bebas dari budaya asing sebaiknya ....|ditolak|ditiru|dibiarkan|diajarkan|Tolak.
3|Mempromosikan produk daerah membuat produk itu ....|dikenal luas|tidak laku|mahal sekali|dilarang|Promosi.
4|Didengar suaranya merupakan pemenuhan hak anak untuk ....|berpendapat|bermain|identitas|kesehatan|Berpendapat.
5|Organisasi kerohanian Islam di sekolah disebut ....|Rohis|OSIS|PMR|Paskibra|Rohis.
"""

TOPICS += """
## SBD
# 1|Seni Rupa dan Musik
@ Menggambar perspektif
min: 15
act: Gambar lorong rumah atau jalan dengan satu titik hilang di garis horizon.
mis: menarik garis benda ke arah yang berbeda-beda sehingga gambar tampak miring
exp: Perspektif adalah cara menggambar benda agar tampak tiga dimensi sesuai jarak pandang. Benda yang jauh tampak lebih kecil. Ada perspektif satu titik hilang, dua titik hilang, dan tiga titik hilang. Titik hilang terletak pada garis horizon, yaitu garis setinggi mata pengamat.
ex: Rel kereta tampak bertemu di kejauhan. // Gedung tinggi digambar dengan tiga titik hilang.
pt: Benda jauh tampak kecil ; Satu, dua, tiga titik hilang ; Titik hilang di garis horizon
sum: Perspektif membuat gambar tampak nyata dan berkedalaman.
fig: table Istilah | Arti ;; garis horizon | garis setinggi mata ;; titik hilang | titik pertemuan garis ;; satu titik hilang | tampak depan lurus ;; dua titik hilang | tampak sudut bangunan ;; tiga titik hilang | tampak dari atas atau bawah ;; perspektif warna | warna jauh lebih pudar ~ Istilah perspektif.
@ Menggambar model benda
min: 15
act: Susun tiga benda di meja, lalu gambar dengan memperhatikan proporsi dan bayangan.
mis: menggambar semua benda dengan ukuran sama tanpa melihat jaraknya
exp: Menggambar model adalah menggambar benda nyata yang diamati langsung, disebut juga still life. Hal yang perlu diperhatikan adalah komposisi, proporsi, gelap terang, dan bayangan. Langkahnya membuat sketsa bentuk dasar, memperbaiki proporsi, lalu memberi arsiran gelap terang.
ex: Gelas digambar dari bentuk dasar silinder. // Apel dan teko disusun berdekatan.
pt: Menggambar benda nyata ; Komposisi dan proporsi ; Gelap terang dan bayangan
sum: Pengamatan cermat menghasilkan gambar model yang mirip.
fig: table Benda | Bentuk dasar ;; gelas | silinder ;; apel | bola ;; kardus | balok ;; corong | kerucut ;; dadu | kubus ;; tenda | prisma ~ Bentuk dasar benda model.
@ Seni grafis cetak tinggi
min: 15
act: Buat cap dari potongan ubi atau karet penghapus, lalu cetak di kertas memakai tinta.
mis: mengukir gambar tanpa membalik sehingga hasil cetak terbalik
exp: Seni grafis adalah karya seni rupa yang dibuat dengan teknik cetak sehingga dapat diperbanyak. Teknik cetak tinggi memakai bagian yang menonjol sebagai bagian yang terkena tinta, misalnya cukil kayu dan cap karet. Teknik lain adalah cetak dalam, cetak datar, dan cetak saring atau sablon.
ex: Stempel termasuk cetak tinggi. // Sablon kaus termasuk cetak saring.
pt: Dibuat dengan teknik cetak ; Cetak tinggi bagian menonjol ; Cetak dalam, datar, saring
sum: Seni grafis memungkinkan karya diperbanyak.
fig: table Teknik grafis | Contoh ;; cetak tinggi | cukil kayu ;; cetak dalam | etsa logam ;; cetak datar | litografi ;; cetak saring | sablon kaus ;; cap sederhana | stempel karet ;; monoprint | cetak satu kali ~ Teknik seni grafis.
@ Komik strip
min: 15
act: Buat komik strip empat panel tentang kejadian lucu di sekolah.
mis: menulis dialog terlalu panjang sehingga panel penuh tulisan
exp: Komik strip adalah cerita bergambar pendek yang terdiri atas beberapa panel. Unsur komik meliputi panel, tokoh, balon kata, narasi, dan efek suara. Cerita komik strip singkat dan biasanya lucu atau berpesan. Tokoh perlu digambar konsisten di setiap panel.
ex: Balon kata berisi ucapan tokoh. // Tulisan BRAK menunjukkan efek suara.
pt: Cerita bergambar berpanel ; Panel, balon kata, narasi ; Tokoh konsisten
sum: Komik strip menyampaikan cerita secara singkat dan menarik.
fig: table Unsur komik | Fungsi ;; panel | kotak adegan ;; balon kata | ucapan tokoh ;; balon pikiran | isi pikiran tokoh ;; narasi | keterangan cerita ;; efek suara | tiruan bunyi ;; garis gerak | menunjukkan gerakan ~ Unsur komik strip.
@ Mozaik dan kolase
min: 15
act: Buat mozaik bergambar ikan dari potongan kertas warna yang ditempel rapat.
mis: menyamakan mozaik dengan kolase yang bahannya bebas
exp: Mozaik adalah karya seni yang dibuat dengan menempelkan kepingan kecil bahan sejenis secara rapat, misalnya kertas, keramik, atau biji-bijian. Kolase adalah karya tempel yang memakai berbagai bahan berbeda. Montase adalah karya tempel dari potongan gambar jadi seperti foto majalah.
ex: Mozaik dari pecahan keramik di dinding taman. // Kolase dari daun, kain, dan kancing.
pt: Mozaik kepingan sejenis ; Kolase bahan beragam ; Montase potongan gambar
sum: Teknik tempel menghasilkan karya yang unik.
fig: table Teknik tempel | Bahan ;; mozaik | kepingan sejenis ;; kolase | bahan beragam ;; montase | potongan gambar jadi ;; mozaik keramik | pecahan keramik ;; mozaik biji | biji-bijian ;; kolase alam | daun dan ranting ~ Teknik seni tempel.
@ Alat musik ritmis dan melodis
min: 15
act: Kelompokkan alat musik yang ada di sekolah menjadi ritmis dan melodis.
mis: menganggap gendang dapat memainkan melodi lagu
exp: Alat musik ritmis berfungsi mengatur irama dan tidak bernada, misalnya gendang, rebana, dan tamborin. Alat musik melodis dapat memainkan nada dan melodi lagu, misalnya pianika, suling, dan biola. Alat musik harmonis dapat memainkan beberapa nada bersamaan atau akor, misalnya gitar dan piano.
ex: Rebana mengiringi irama lagu. // Pianika memainkan melodi lagu.
pt: Ritmis mengatur irama ; Melodis memainkan melodi ; Harmonis memainkan akor
sum: Setiap jenis alat musik memiliki peran dalam ansambel.
fig: table Alat musik | Jenis ;; rebana | ritmis ;; tamborin | ritmis bergemerincing ;; pianika | melodis ;; suling | melodis tiup ;; gitar | harmonis ;; piano | harmonis tuts ~ Jenis alat musik.
@ Tangga nada mayor
min: 15
act: Mainkan tangga nada C mayor dengan pianika atau aplikasi piano, lalu nyanyikan do re mi.
mis: mengira semua jarak nada dalam tangga nada sama
exp: Tangga nada adalah susunan nada yang berurutan. Tangga nada mayor berkesan riang dan memiliki jarak nada 1 - 1 - ½ - 1 - 1 - 1 - ½. Tangga nada minor berkesan sedih. Tangga nada C mayor dimulai dari nada C atau do. Lagu Indonesia Raya memakai tangga nada mayor.
ex: Do re mi fa sol la si do adalah tangga nada mayor. // Jarak mi ke fa adalah setengah.
pt: Susunan nada berurutan ; Mayor riang ; Jarak 1 1 ½ 1 1 1 ½
sum: Tangga nada mayor memberi kesan gembira.
fig: table Solmisasi | Nada pada C mayor ;; do | C ;; re | D ;; mi | E ;; fa | F ;; sol | G ;; la | A ~ Solmisasi tangga nada C mayor.
@ Ansambel musik
min: 15
act: Bentuk ansambel kecil dengan keluarga memakai alat musik sederhana dan mainkan satu lagu.
mis: memainkan alat musik sendiri-sendiri tanpa memperhatikan pemain lain
exp: Ansambel musik adalah permainan musik bersama beberapa pemain dengan alat musik sejenis atau campuran. Ansambel sejenis memakai alat yang sama, misalnya ansambel suling. Ansambel campuran memakai berbagai alat. Kunci keberhasilan ansambel adalah kekompakan, tempo yang sama, dan saling mendengarkan.
ex: Ansambel angklung memainkan lagu daerah. // Ansambel campuran memakai pianika, gitar, dan gendang.
pt: Bermain musik bersama ; Ansambel sejenis atau campuran ; Kompak dan saling mendengarkan
sum: Ansambel melatih kerja sama dalam bermusik.
fig: table Ansambel | Jenis ;; ansambel suling | sejenis tiup ;; ansambel angklung | sejenis bambu ;; ansambel pianika | sejenis tuts ;; ansambel campuran | berbagai alat ;; orkestra | besar dan lengkap ;; band | gitar, bas, drum ~ Jenis ansambel musik.
# 2|Tari, Teater, dan Kriya
@ Tari kreasi
min: 15
act: Kembangkan satu gerak tari daerah menjadi gerak baru dengan iringan lagu modern.
mis: mengira tari kreasi tidak boleh berpijak pada tari tradisional
exp: Tari kreasi adalah tari yang dikembangkan dari tari tradisional atau diciptakan baru dengan gerak yang lebih bebas. Tari kreasi tetap dapat memakai unsur tradisi, tetapi dikemas dengan gerak, musik, dan kostum yang baru. Contohnya Tari Jaipong yang dikembangkan dari ketuk tilu.
ex: Jaipong diciptakan Gugum Gumbira. // Tari kreasi sering dipentaskan di acara sekolah.
pt: Dikembangkan dari tradisi atau baru ; Gerak lebih bebas ; Contoh Jaipong
sum: Tari kreasi menjaga tradisi tetap segar.
fig: table Tari kreasi | Asal pengembangan ;; Jaipong | ketuk tilu Jawa Barat ;; Tari Merak | gerak burung merak ;; Tari Kupu-kupu | gerak kupu-kupu ;; Tari Yapong | Betawi ;; Tari Ratoh Jaroe | tari duduk Aceh ;; Tari Nelayan | kehidupan nelayan ~ Contoh tari kreasi.
@ Rias dan busana tari
min: 15
act: Rancang kostum sederhana untuk tari tentang petani dari bahan di rumah.
mis: memakai busana tari yang menghalangi gerak
exp: Rias dan busana adalah unsur pendukung tari. Rias wajah memperjelas karakter dan ekspresi penari. Busana harus sesuai tema, nyaman dipakai, dan tidak menghalangi gerak. Unsur pendukung lain meliputi properti, iringan, tata cahaya, dan tempat pertunjukan.
ex: Tari Merak memakai sayap kain warna-warni. // Rias karakter tua memakai garis kerutan.
pt: Rias memperjelas karakter ; Busana sesuai tema dan nyaman ; Properti dan tata cahaya
sum: Rias dan busana memperkuat pesan tari.
fig: table Unsur pendukung | Fungsi ;; rias | memperjelas karakter ;; busana | mendukung tema ;; properti | alat yang dimainkan penari ;; iringan | memberi irama ;; tata cahaya | menciptakan suasana ;; panggung | tempat pertunjukan ~ Unsur pendukung tari.
@ Tari berpasangan
min: 15
act: Latih gerak tari berpasangan sederhana bersama saudara atau teman dengan delapan hitungan.
mis: bergerak sendiri tanpa menyesuaikan dengan pasangan
exp: Tari berpasangan ditarikan oleh dua orang atau lebih secara berpasangan dengan gerak yang saling merespons. Gerakannya bisa serempak, berselang, atau saling melengkapi. Contohnya Tari Serampang Dua Belas dari Sumatera Utara, Tari Payung dari Sumatera Barat, dan Tari Gending Sriwijaya yang ditarikan berkelompok.
ex: Tari Serampang Dua Belas ditarikan berpasangan. // Gerak berselang dilakukan bergantian.
pt: Ditarikan berpasangan ; Gerak saling merespons ; Serempak, berselang, melengkapi
sum: Tari berpasangan menuntut kekompakan.
fig: table Pola gerak | Keterangan ;; serempak | bergerak bersamaan ;; berselang | bergerak bergantian ;; berurutan | menyusul satu per satu ;; berlawanan | arah berbeda ;; saling melengkapi | gerak membentuk satu kesatuan ;; bertemu | penari saling mendekat ~ Pola gerak tari berpasangan.
@ Teater modern
min: 15
act: Tonton cuplikan pentas teater modern, lalu bandingkan dengan teater tradisional.
mis: mengira teater modern selalu tanpa naskah
exp: Teater modern adalah teater yang dipentaskan berdasarkan naskah tertulis dengan unsur pementasan yang tertata. Pemain menghafal dialog, dan pementasan dipimpin sutradara. Teater modern memakai tata panggung, tata cahaya, dan tata suara. Penonton biasanya tidak terlibat langsung dalam cerita.
ex: Pementasan drama di gedung kesenian. // Sutradara mengatur gerak pemain.
pt: Berdasarkan naskah tertulis ; Dipimpin sutradara ; Penonton tidak terlibat langsung
sum: Teater modern tertata dari naskah hingga panggung.
fig: table Unsur teater | Peran ;; naskah | cerita dan dialog ;; sutradara | memimpin pementasan ;; aktor | memerankan tokoh ;; penata panggung | mengatur dekorasi ;; penata cahaya | mengatur lampu ;; penonton | menikmati pertunjukan ~ Unsur teater modern.
@ Tata panggung
min: 15
act: Gambar denah panggung sederhana untuk pentas kelas dengan letak dekorasi dan pintu masuk.
mis: menempatkan dekorasi yang menutupi pemain dari penonton
exp: Tata panggung atau skenografi adalah pengaturan panggung untuk mendukung pementasan. Jenis panggung antara lain panggung proscenium yang dilihat dari depan, panggung arena yang dikelilingi penonton, dan panggung thrust yang dilihat dari tiga sisi. Dekorasi menunjukkan tempat dan waktu cerita.
ex: Dekorasi pohon menunjukkan latar hutan. // Panggung arena dikelilingi penonton.
pt: Pengaturan panggung ; Proscenium, arena, thrust ; Dekorasi menunjukkan latar
sum: Tata panggung membantu penonton memahami latar cerita.
fig: table Jenis panggung | Arah penonton ;; proscenium | dari depan ;; arena | mengelilingi panggung ;; thrust | dari tiga sisi ;; tapal kuda | melengkung di depan ;; terbuka | di ruang luar ;; pendopo | dari berbagai sisi bangunan Jawa ~ Jenis panggung.
@ Kerajinan tanah liat
min: 15
act: Buat mangkuk kecil dari tanah liat atau plastisin dengan teknik pilin.
mis: membakar karya tanah liat yang masih basah sehingga retak
exp: Tanah liat adalah bahan lunak yang mudah dibentuk. Teknik membentuknya antara lain teknik pijit, teknik pilin, teknik lempeng, teknik putar dengan alat putar, dan teknik cetak. Karya tanah liat dikeringkan lalu dibakar agar keras. Hasilnya disebut gerabah atau keramik.
ex: Teknik pilin dengan menyusun gulungan tanah liat. // Kasongan terkenal dengan gerabah.
pt: Bahan lunak mudah dibentuk ; Pijit, pilin, lempeng, putar ; Dikeringkan lalu dibakar
sum: Tanah liat dapat diolah menjadi kerajinan bernilai.
fig: table Teknik | Cara ;; pijit | dipijit dengan jari ;; pilin | menyusun gulungan ;; lempeng | menyambung lembaran ;; putar | memakai meja putar ;; cetak | memakai cetakan ;; butsir | menambah dan mengurangi ~ Teknik membentuk tanah liat.
@ Kerajinan bahan limbah
min: 15
act: Ubah botol plastik bekas menjadi pot tanaman atau tempat alat tulis.
mis: memakai limbah kotor tanpa dibersihkan
exp: Kerajinan bahan limbah memanfaatkan sampah menjadi benda berguna. Limbah anorganik antara lain plastik, kaleng, dan kertas bekas. Limbah organik antara lain kulit jagung dan pelepah pisang. Prinsipnya reduce, reuse, dan recycle. Bahan limbah harus dibersihkan dan dikeringkan sebelum dipakai.
ex: Tas dari bungkus kopi. // Bunga dari kulit jagung.
pt: Sampah jadi benda berguna ; Limbah organik dan anorganik ; Reduce, reuse, recycle
sum: Kerajinan limbah mengurangi sampah dan bernilai jual.
fig: table Limbah | Produk kerajinan ;; botol plastik | pot tanaman ;; bungkus kopi | tas anyaman ;; kulit jagung | bunga hias ;; kaleng bekas | tempat pensil ;; koran bekas | keranjang ;; pelepah pisang | lukisan tempel ~ Kerajinan dari limbah.
@ Wayang kulit
min: 15
act: Buat wayang sederhana dari kardus dan pertunjukkan bayangannya dengan senter.
mis: mengira wayang kulit hanya hiburan tanpa pesan
exp: Wayang kulit adalah seni pertunjukan tradisional yang memakai boneka dari kulit kerbau yang ditatah dan diwarnai. Pertunjukan dipimpin dalang dan diiringi gamelan serta pesinden. Cerita wayang banyak bersumber dari Mahabharata dan Ramayana. Wayang diakui UNESCO sebagai warisan budaya dunia pada 2003.
ex: Dalang memainkan wayang di balik kelir. // Blencong menjadi sumber cahaya.
pt: Boneka kulit ditatah ; Dipimpin dalang dan diiringi gamelan ; Diakui UNESCO 2003
sum: Wayang kulit sarat nilai dan pesan moral.
fig: table Istilah wayang | Arti ;; dalang | pemain dan pencerita ;; kelir | layar putih ;; blencong | lampu pertunjukan ;; gamelan | musik pengiring ;; sinden | penyanyi perempuan ;; gunungan | penanda awal dan akhir babak ~ Istilah wayang kulit.

## PJOK
# 1|Permainan dan Atletik
@ Teknik dasar sepak takraw
min: 15
act: Latih sepakan sila dengan bola plastik ringan sebanyak dua puluh kali.
mis: menyentuh bola takraw dengan tangan saat bermain
exp: Sepak takraw dimainkan dua regu, masing-masing tiga pemain, di lapangan seperti bulu tangkis dengan bola rotan atau plastik. Bola dimainkan dengan kaki, kepala, dada, dan paha, tetapi tidak boleh dengan tangan. Teknik dasarnya sepak sila, sepak kuda, sepak cungkil, heading, dan memaha.
ex: Sepak sila memakai kaki bagian dalam. // Tekong melakukan servis.
pt: Tiga pemain per regu ; Tidak boleh memakai tangan ; Sepak sila, sepak kuda, heading
sum: Sepak takraw melatih kelenturan dan koordinasi.
fig: table Teknik | Bagian tubuh ;; sepak sila | kaki bagian dalam ;; sepak kuda | punggung kaki ;; sepak cungkil | ujung kaki ;; heading | kepala ;; memaha | paha ;; mendada | dada ~ Teknik sepak takraw.
@ Teknik dasar tenis meja
min: 15
act: Latih pukulan forehand ke dinding dengan bet dan bola pingpong selama lima menit.
mis: memukul bola sebelum memantul di meja sendiri saat menerima servis
exp: Tenis meja atau pingpong dimainkan dengan bet dan bola ringan di atas meja yang dibatasi net. Cara memegang bet ada dua: shakehand seperti berjabat tangan dan penhold seperti memegang pena. Pukulan dasarnya forehand, backhand, push, dan smash. Satu gim dimenangkan dengan angka 11.
ex: Pegangan shakehand banyak dipakai pemula. // Smash dilakukan saat bola memantul tinggi.
pt: Bet dan bola ringan ; Shakehand dan penhold ; Gim sampai angka 11
sum: Tenis meja melatih kecepatan reaksi.
fig: table Istilah | Arti ;; shakehand | pegangan seperti berjabat tangan ;; penhold | pegangan seperti memegang pena ;; forehand | pukulan dari sisi kanan ;; backhand | pukulan punggung tangan ;; push | dorongan bola rendah ;; smash | pukulan keras menukik ~ Istilah tenis meja.
@ Lari jarak menengah
min: 15
act: Lari 800 meter dengan kecepatan stabil, lalu catat waktumu.
mis: berlari secepat mungkin sejak awal sehingga kehabisan tenaga
exp: Lari jarak menengah meliputi nomor 800 meter dan 1.500 meter. Lari ini memerlukan kecepatan dan daya tahan. Start yang dipakai adalah start berdiri. Pelari perlu mengatur kecepatan, napas, dan ayunan lengan yang rileks, lalu mempercepat lari menjelang garis finis.
ex: Start berdiri dengan aba-aba bersedia dan ya. // Pelari mempercepat lari pada 200 meter terakhir.
pt: Nomor 800 dan 1.500 meter ; Start berdiri ; Atur kecepatan dan napas
sum: Pengaturan tenaga menentukan keberhasilan lari jarak menengah.
fig: table Nomor lari | Jenis start ;; 100 meter | start jongkok ;; 400 meter | start jongkok di tikungan ;; 800 meter | start berdiri ;; 1.500 meter | start berdiri berkelompok ;; maraton | start berdiri massal ;; estafet 4 x 100 meter | start jongkok pelari pertama ~ Nomor lari dan jenis start.
@ Lempar lembing
min: 15
act: Peragakan gerakan lempar lembing memakai tongkat ringan di lapangan terbuka dengan pengawasan guru.
mis: melempar lembing dengan siku rendah sehingga lemparan tidak jauh
exp: Lempar lembing adalah nomor atletik melempar lembing sejauh mungkin. Teknik dasarnya cara memegang lembing, awalan berlari, gerakan melempar dengan siku tinggi, dan gerak lanjutan. Lembing harus jatuh di sektor lempar dengan mata lembing lebih dulu menyentuh tanah. Keselamatan harus selalu dijaga.
ex: Cara pegang Amerika memakai ibu jari dan telunjuk. // Pelempar tidak boleh melewati garis lengkung.
pt: Pegangan, awalan, melempar, gerak lanjutan ; Siku tinggi saat melempar ; Mata lembing menyentuh tanah lebih dulu
sum: Teknik yang benar menghasilkan lemparan jauh dan aman.
fig: table Cara memegang lembing | Jari penahan ;; cara Amerika | ibu jari dan telunjuk ;; cara Finlandia | ibu jari dan jari tengah ;; cara tang | telunjuk dan jari tengah ;; awalan | berlari mendekati garis ;; saat melempar | siku tinggi ;; gerak lanjutan | badan condong ke depan ~ Teknik lempar lembing.
@ Renang gaya dada
min: 15
act: Latih gerakan kaki gaya dada di tepi kolam dengan pendampingan orang dewasa.
mis: menendang lurus seperti gaya bebas saat gaya dada
exp: Renang gaya dada disebut juga gaya katak. Badan telungkup di permukaan air. Gerakan kaki ditekuk lalu ditendang ke samping dan dirapatkan seperti katak. Tangan didorong ke depan lalu dibuka ke samping. Napas diambil saat tangan menarik dan kepala terangkat. Gerakannya pelan dan hemat tenaga.
ex: Kaki membentuk gerakan seperti katak. // Kepala terangkat saat mengambil napas.
pt: Disebut gaya katak ; Kaki ditendang ke samping ; Napas saat kepala terangkat
sum: Gaya dada cocok untuk berenang jarak jauh dengan santai.
fig: table Tahap gaya dada | Gerakan ;; meluncur | tangan lurus ke depan ;; tarikan tangan | tangan dibuka ke samping ;; mengambil napas | kepala terangkat ;; tekuk kaki | tumit mendekati pantat ;; tendangan | kaki didorong ke samping ;; merapat | kedua kaki lurus kembali ~ Tahap renang gaya dada.
@ Latihan kekuatan otot
min: 15
act: Lakukan push-up, sit-up, dan squat masing-masing sepuluh kali, lalu catat perkembanganmu tiap minggu.
mis: berlatih kekuatan otot setiap hari tanpa istirahat
exp: Kekuatan otot adalah kemampuan otot mengerahkan tenaga untuk menahan beban. Latihan kekuatan antara lain push-up untuk otot lengan dan dada, sit-up untuk otot perut, back-up untuk otot punggung, dan squat untuk otot tungkai. Latihan dilakukan bertahap, dengan istirahat cukup agar otot pulih.
ex: Squat memperkuat otot paha. // Plank melatih otot perut dan punggung.
pt: Kemampuan menahan beban ; Push-up, sit-up, squat ; Bertahap dan istirahat cukup
sum: Otot kuat mendukung aktivitas sehari-hari.
fig: table Latihan | Otot yang dilatih ;; push-up | lengan dan dada ;; sit-up | perut ;; back-up | punggung ;; squat | tungkai ;; plank | inti tubuh ;; pull-up | lengan dan bahu ~ Latihan kekuatan otot.
@ Teknik dasar kasti
min: 15
act: Latih melempar dan menangkap bola kasti bersama teman sebanyak dua puluh kali.
mis: memukul bola dengan kayu dipegang satu tangan tanpa kuda-kuda
exp: Kasti adalah permainan bola kecil yang dimainkan dua regu, masing-masing dua belas pemain. Regu pemukul berusaha memukul bola dan berlari ke tiang hinggap, sedangkan regu penjaga berusaha mematikan pelari. Teknik dasarnya melempar, menangkap, memukul, dan berlari.
ex: Pelari aman jika sampai di tiang hinggap. // Penjaga mematikan pelari dengan lemparan bola.
pt: Dua regu dua belas pemain ; Memukul lalu berlari ke tiang hinggap ; Melempar, menangkap, memukul
sum: Kasti melatih kerja sama dan ketangkasan.
fig: table Istilah kasti | Arti ;; pemukul | regu yang memukul bola ;; penjaga | regu yang berjaga di lapangan ;; pelambung | pelempar bola ke pemukul ;; tiang hinggap | tempat pelari aman ;; ruang bebas | tempat menunggu giliran ;; mematikan | mengenai pelari dengan bola ~ Istilah permainan kasti.
@ Senam lantai lenting tangan
min: 15
act: Latih sikap kayang di atas matras dengan bantuan teman untuk persiapan lenting tangan.
mis: melakukan lenting tangan tanpa pemanasan dan matras
exp: Lenting tangan atau handspring adalah gerakan melenting dengan bertumpu pada kedua tangan, lalu mendarat dengan kedua kaki. Gerakan ini memerlukan kekuatan lengan, kelentukan punggung, dan keberanian. Latihan persiapan meliputi kayang, sikap lilin, dan guling depan. Lenting tangan harus dilakukan di atas matras dan dibantu teman.
ex: Kayang melatih kelentukan punggung. // Teman membantu menahan punggung saat melenting.
pt: Bertumpu pada kedua tangan ; Perlu kekuatan dan kelentukan ; Dilatih di matras dengan bantuan
sum: Latihan bertahap membuat lenting tangan aman.
fig: table Latihan persiapan | Manfaat ;; kayang | kelentukan punggung ;; sikap lilin | keseimbangan bahu ;; guling depan | keberanian berguling ;; push-up | kekuatan lengan ;; meroda | koordinasi tangan dan kaki ;; peregangan | mencegah cedera ~ Latihan persiapan lenting tangan.
# 2|Kebugaran dan Kesehatan
@ Senam aerobik
min: 15
act: Ikuti video senam aerobik selama lima belas menit bersama keluarga, lalu hitung denyut nadimu.
mis: langsung melakukan gerakan cepat tanpa pemanasan
exp: Senam aerobik adalah senam dengan gerakan berirama yang diiringi musik dan dilakukan terus-menerus. Senam ini melatih daya tahan jantung dan paru-paru. Rangkaian senam aerobik terdiri atas pemanasan, gerakan inti, dan pendinginan. Gerakan dasarnya antara lain march, jogging, step touch, dan grapevine.
ex: Step touch melangkah ke samping lalu merapat. // Denyut nadi naik setelah gerakan inti.
pt: Gerakan berirama dengan musik ; Melatih jantung dan paru-paru ; Pemanasan, inti, pendinginan
sum: Senam aerobik menyehatkan jantung.
fig: table Gerakan aerobik | Cara melakukan ;; march | jalan di tempat ;; jogging | lari kecil di tempat ;; step touch | melangkah ke samping lalu merapat ;; grapevine | melangkah silang ke samping ;; knee up | mengangkat lutut ;; v-step | melangkah membentuk huruf V ~ Gerakan dasar senam aerobik.
@ Lari gawang
min: 15
act: Latih melangkahi rintangan rendah dari kardus dengan langkah berirama.
mis: melompati gawang terlalu tinggi sehingga lari melambat
exp: Lari gawang adalah lari cepat sambil melewati rintangan berupa gawang. Teknik dasarnya start jongkok, lari menuju gawang, melewati gawang dengan kaki depan diluruskan, kaki belakang ditarik ke samping, dan mendarat lalu lari kembali. Langkah antargawang dibuat berirama, biasanya tiga langkah.
ex: Kaki depan diluruskan saat melewati gawang. // Tiga langkah di antara gawang.
pt: Lari cepat melewati gawang ; Kaki depan lurus, kaki belakang ke samping ; Tiga langkah antargawang
sum: Irama langkah yang teratur membuat lari gawang lancar.
fig: table Tahap | Gerakan ;; start | start jongkok ;; awalan | lari menuju gawang pertama ;; kaki depan | diluruskan melewati gawang ;; kaki belakang | ditarik ke samping ;; mendarat | kaki depan menapak ;; antargawang | tiga langkah berirama ~ Tahap lari gawang.
@ Lompat jangkit
min: 15
act: Latih rangkaian gerakan jingkat, langkah, dan lompat di halaman berpasir.
mis: mendarat dengan kaki yang salah pada tahap jingkat
exp: Lompat jangkit atau triple jump terdiri atas tiga gerakan berurutan: hop atau jingkat dengan kaki yang sama, step atau langkah dengan kaki berlawanan, dan jump atau lompat lalu mendarat di bak pasir dengan dua kaki. Awalan dilakukan dengan lari cepat. Irama dan keseimbangan sangat penting.
ex: Tumpuan kanan, jingkat mendarat kanan, langkah kiri, lompat. // Jarak diukur dari papan tumpuan.
pt: Hop, step, jump ; Jingkat dengan kaki sama ; Mendarat dua kaki di pasir
sum: Lompat jangkit memadukan kecepatan dan irama.
fig: table Tahap | Kaki pendarat ;; tumpuan | kaki terkuat ;; hop | kaki yang sama dengan tumpuan ;; step | kaki yang berlawanan ;; jump | dua kaki di bak pasir ;; awalan | lari cepat ;; pengukuran | dari papan tumpuan ~ Tahap lompat jangkit.
@ Teknik dasar softball
min: 15
act: Latih menangkap bola dengan glove dan melempar ke sasaran bersama teman.
mis: memegang pemukul terlalu ke ujung sehingga ayunan lemah
exp: Softball dimainkan dua regu masing-masing sembilan pemain di lapangan berbentuk intan dengan empat base. Teknik dasarnya melempar, menangkap dengan glove, memukul dengan bat, dan berlari antarbase. Pitcher melempar bola dari bawah atau underhand. Regu mendapat angka jika pelari kembali ke home base.
ex: Pitcher melempar dengan ayunan dari bawah. // Catcher berjaga di belakang pemukul.
pt: Sembilan pemain per regu ; Lapangan intan empat base ; Pitcher melempar underhand
sum: Softball melatih kerja sama dan ketepatan.
fig: table Posisi | Tugas ;; pitcher | melempar bola ke pemukul ;; catcher | menangkap di belakang pemukul ;; batter | memukul bola ;; baseman | menjaga base ;; shortstop | penjaga antara base 2 dan 3 ;; outfielder | menjaga daerah luar ~ Posisi pemain softball.
@ Pemanasan dan pendinginan
min: 15
act: Susun rangkaian pemanasan lima menit dan pendinginan tiga menit, lalu praktikkan sebelum dan sesudah olahraga.
mis: melewatkan pendinginan setelah berolahraga berat
exp: Pemanasan dilakukan sebelum olahraga untuk menaikkan suhu tubuh, melenturkan otot, dan mencegah cedera. Pemanasan terdiri atas peregangan dinamis dan gerakan ringan seperti jogging. Pendinginan dilakukan sesudah olahraga untuk menurunkan denyut jantung secara bertahap dan mengurangi pegal, misalnya dengan jalan santai dan peregangan statis.
ex: Jogging ringan sebelum bermain bola. // Peregangan statis setelah lari.
pt: Pemanasan mencegah cedera ; Peregangan dinamis sebelum olahraga ; Pendinginan menurunkan denyut jantung
sum: Pemanasan dan pendinginan membuat olahraga aman.
fig: table Kegiatan | Waktu dilakukan ;; jogging ringan | awal pemanasan ;; peregangan dinamis | pemanasan ;; gerakan inti | latihan utama ;; jalan santai | awal pendinginan ;; peregangan statis | pendinginan ;; minum air | setelah olahraga ~ Urutan pemanasan dan pendinginan.
@ Pola tidur sehat
min: 15
act: Catat jam tidur dan bangunmu selama seminggu, lalu hitung rata-rata lama tidurmu.
mis: bermain gawai sampai larut malam sebelum tidur
exp: Remaja usia 13 sampai 18 tahun membutuhkan tidur sekitar 8 sampai 10 jam setiap malam. Tidur cukup membantu pertumbuhan, daya ingat, konsentrasi, dan daya tahan tubuh. Kebiasaan tidur sehat antara lain tidur dan bangun pada jam yang sama, menjauhkan gawai sebelum tidur, dan menghindari minuman berkafein di malam hari.
ex: Tidur pukul 21.00 dan bangun pukul 05.00. // Cahaya layar gawai mengganggu rasa kantuk.
pt: Remaja 8 sampai 10 jam ; Membantu pertumbuhan dan daya ingat ; Jauhkan gawai sebelum tidur
sum: Tidur cukup adalah kunci belajar dan tumbuh optimal.
fig: table Kebiasaan | Dampak ;; tidur jam teratur | tubuh lebih segar ;; gawai sebelum tidur | sulit terlelap ;; minum kopi malam | tidur terganggu ;; kamar gelap dan tenang | tidur nyenyak ;; begadang | konsentrasi menurun ;; olahraga sore | lebih mudah tidur ~ Kebiasaan dan dampaknya pada tidur.
@ Penyakit tidak menular
min: 15
act: Diskusikan dengan keluarga kebiasaan makan yang dapat mencegah penyakit tidak menular.
mis: mengira penyakit tidak menular hanya menyerang orang tua
exp: Penyakit tidak menular adalah penyakit yang tidak ditularkan dari orang ke orang, misalnya diabetes, hipertensi, penyakit jantung, dan obesitas. Faktor risikonya antara lain kurang gerak, makan berlebihan gula, garam, dan lemak, serta merokok. Pencegahannya dengan aktivitas fisik teratur, makan bergizi seimbang, dan tidak merokok.
ex: Minuman manis berlebihan meningkatkan risiko diabetes. // Bersepeda membantu menjaga berat badan.
pt: Tidak menular antarorang ; Diabetes, hipertensi, jantung ; Cegah dengan gerak dan makan seimbang
sum: Gaya hidup sehat sejak remaja mencegah penyakit tidak menular.
fig: table Penyakit | Faktor risiko utama ;; diabetes | gula berlebihan ;; hipertensi | garam berlebihan ;; penyakit jantung | lemak jenuh dan rokok ;; obesitas | kurang gerak ;; kanker paru | merokok ;; gigi berlubang | jarang menyikat gigi ~ Penyakit tidak menular dan faktor risikonya.
@ Keselamatan di jalan raya
min: 15
act: Amati rambu lalu lintas di jalan menuju sekolah, lalu gambar dan tulis artinya.
mis: menyeberang jalan di sembarang tempat tanpa melihat kiri kanan
exp: Keselamatan di jalan raya dijaga dengan menaati rambu dan marka. Pejalan kaki memakai trotoar dan menyeberang di zebra cross atau jembatan penyeberangan. Pesepeda dan pengendara motor wajib memakai helm. Remaja di bawah 17 tahun belum boleh mengendarai sepeda motor karena belum memiliki SIM.
ex: Menyeberang di zebra cross setelah melihat kiri dan kanan. // Memakai helm saat bersepeda.
pt: Taati rambu dan marka ; Menyeberang di tempat penyeberangan ; Helm dan SIM
sum: Tertib berlalu lintas melindungi diri dan orang lain.
fig: table Warna lampu lalu lintas | Arti ;; merah | berhenti ;; kuning | hati-hati bersiap ;; hijau | boleh jalan ;; kuning berkedip | waspada perlambat ;; hijau pejalan kaki | boleh menyeberang ;; merah pejalan kaki | dilarang menyeberang ~ Arti lampu lalu lintas.
"""

BANK += """
## SBD|Menggambar perspektif
Titik pertemuan garis dalam perspektif disebut titik …|hilang|pusat|awal|tengah|Titik hilang.
Garis setinggi mata pengamat disebut garis …|horizon|vertikal|diagonal|kontur|Horizon.
=|Benda yang jauh tampak lebih …|kecil|Kecil.
=|Gedung tinggi dilihat dari bawah digambar dengan … titik hilang.|tiga;3|Tiga.
B|Rel kereta tampak bertemu di kejauhan.|Perspektif.
S|Benda yang jauh digambar lebih besar.|Lebih kecil.
Sudut bangunan digambar dengan perspektif … titik hilang.|dua|satu|tiga|nol|Dua.
Warna benda jauh tampak lebih pudar disebut perspektif …|warna|garis|titik|bayangan|Warna.
## SBD|Menggambar model benda
Menggambar benda nyata yang diamati langsung disebut juga …|still life|abstrak|karikatur|ilustrasi|Still life.
Bentuk dasar gelas adalah …|silinder|bola|kubus|kerucut|Silinder.
=|Bentuk dasar apel adalah …|bola|Bola.
=|Bentuk dasar dadu adalah …|kubus|Kubus.
B|Menggambar model memperhatikan gelap terang.|Gelap terang.
S|Semua benda model digambar sama besar tanpa melihat jarak.|Proporsi.
Perbandingan ukuran bagian benda disebut …|proporsi|kontras|irama|tekstur|Proporsi.
Bentuk dasar corong adalah …|kerucut|silinder|balok|bola|Kerucut.
## SBD|Seni grafis cetak tinggi
Seni grafis dibuat dengan teknik …|cetak|pahat|anyam|tenun|Cetak.
Stempel karet termasuk teknik cetak …|tinggi|dalam|datar|saring|Tinggi.
=|Sablon kaus termasuk teknik cetak …|saring|Saring.
=|Etsa logam termasuk teknik cetak …|dalam|Dalam.
B|Seni grafis dapat diperbanyak.|Diperbanyak.
S|Gambar pada cap tidak perlu dibalik saat diukir.|Dibalik.
Cukil kayu termasuk teknik cetak …|tinggi|datar|saring|dalam|Tinggi.
Litografi termasuk teknik cetak …|datar|tinggi|dalam|saring|Datar.
## SBD|Komik strip
Kotak adegan dalam komik disebut …|panel|balon|narasi|halaman|Panel.
Ucapan tokoh komik ditulis dalam balon …|kata|pikiran|suara|gambar|Balon kata.
=|Tulisan tiruan bunyi dalam komik disebut efek …|suara|Efek suara.
=|Keterangan cerita dalam komik disebut …|narasi|Narasi.
B|Tokoh komik digambar konsisten di setiap panel.|Konsisten.
S|Dialog komik sebaiknya sangat panjang.|Singkat.
Isi pikiran tokoh ditulis dalam balon …|pikiran|kata|narasi|efek|Pikiran.
Garis yang menunjukkan gerakan dalam komik disebut garis …|gerak|kontur|horizon|arsir|Gerak.
## SBD|Mozaik dan kolase
Karya tempel dari kepingan bahan sejenis disebut …|mozaik|kolase|montase|relief|Mozaik.
Karya tempel dari berbagai bahan berbeda disebut …|kolase|mozaik|montase|grafis|Kolase.
=|Karya tempel dari potongan gambar jadi disebut …|montase|Montase.
=|Mozaik di dinding taman sering memakai pecahan …|keramik|Keramik.
B|Kolase dapat memakai daun, kain, dan kancing.|Beragam.
S|Mozaik memakai bahan yang beragam jenisnya.|Sejenis.
Mozaik dari kacang hijau dan jagung termasuk mozaik …|biji|keramik|kertas|kaca|Biji.
Kepingan mozaik ditempel secara …|rapat|berjauhan|bertumpuk tinggi|acak tanpa pola|Rapat.
## SBD|Alat musik ritmis dan melodis
Alat musik yang mengatur irama dan tidak bernada disebut …|ritmis|melodis|harmonis|elektrik|Ritmis.
Pianika termasuk alat musik …|melodis|ritmis|harmonis|perkusi|Melodis.
=|Alat musik yang memainkan akor disebut alat musik …|harmonis|Harmonis.
=|Rebana termasuk alat musik …|ritmis|Ritmis.
B|Gitar termasuk alat musik harmonis.|Akor.
S|Gendang dapat memainkan melodi lagu dengan jelas.|Ritmis.
Suling termasuk alat musik melodis yang dimainkan dengan cara …|ditiup|dipukul|dipetik|digesek|Tiup.
Piano termasuk alat musik …|harmonis|ritmis|tiup|petik|Harmonis.
## SBD|Tangga nada mayor
Tangga nada mayor berkesan …|riang|sedih|seram|lambat|Riang.
Jarak nada mi ke fa adalah …|setengah|satu|satu setengah|dua|½.
=|Pada tangga nada C mayor, nada do adalah …|C|C.
=|Pada tangga nada C mayor, nada sol adalah …|G|G.
B|Lagu Indonesia Raya memakai tangga nada mayor.|Mayor.
S|Semua jarak nada dalam tangga nada mayor sama.|Ada setengah.
Tangga nada yang berkesan sedih adalah tangga nada …|minor|mayor|pentatonis riang|kromatis riang|Minor.
Jarak nada si ke do tinggi adalah …|setengah|satu|dua|tiga|½.
## SBD|Ansambel musik
Permainan musik bersama beberapa pemain disebut …|ansambel|solo|duet vokal|akapela|Ansambel.
Ansambel suling termasuk ansambel …|sejenis|campuran|orkestra|band|Sejenis.
=|Ansambel yang memakai berbagai jenis alat disebut ansambel …|campuran|Campuran.
=|Ansambel besar dan lengkap disebut …|orkestra|Orkestra.
B|Pemain ansambel harus saling mendengarkan.|Kompak.
S|Dalam ansambel, setiap pemain bebas memakai tempo sendiri.|Tempo sama.
Band biasanya terdiri atas gitar, bas, dan …|drum|angklung|suling|rebana saja|Drum.
Kunci keberhasilan ansambel adalah …|kekompakan|bermain paling keras|bermain sendiri|tempo berbeda|Kompak.
## SBD|Tari kreasi
Tari kreasi dikembangkan dari tari … atau diciptakan baru.|tradisional|asing saja|olahraga|militer|Tradisional.
Tari Jaipong dikembangkan dari …|ketuk tilu|tari Saman|tari Kecak|tari Piring|Ketuk tilu.
=|Pencipta Tari Jaipong adalah Gugum …|Gumbira|Gugum Gumbira.
=|Tari kreasi yang meniru gerak burung merak adalah Tari …|Merak|Merak.
B|Tari kreasi memiliki gerak yang lebih bebas.|Bebas.
S|Tari kreasi sama sekali tidak boleh memakai unsur tradisi.|Boleh.
Tari Yapong berasal dari …|Betawi|Aceh|Bali|Papua|Betawi.
Tari kreasi tentang kehidupan nelayan adalah Tari …|Nelayan|Merak|Kupu-kupu|Yapong|Nelayan.
## SBD|Rias dan busana tari
Rias wajah tari berfungsi memperjelas …|karakter|harga kostum|panggung|musik|Karakter.
Busana tari yang baik tidak boleh …|menghalangi gerak|sesuai tema|nyaman|berwarna|Menghalangi.
=|Alat yang dimainkan penari disebut …|properti|Properti.
=|Pengaturan lampu untuk suasana disebut tata …|cahaya|Cahaya.
B|Rias karakter tua dapat memakai garis kerutan.|Karakter.
S|Busana tari tidak perlu sesuai tema.|Sesuai tema.
Tari Merak memakai busana berupa …|sayap kain warna-warni|jas hujan|seragam sekolah|baju renang|Sayap.
Tempat pertunjukan tari disebut …|panggung|properti|rias|iringan|Panggung.
## SBD|Tari berpasangan
Tari yang ditarikan dua orang dengan gerak saling merespons disebut tari …|berpasangan|tunggal|massal|solo|Berpasangan.
Gerak yang dilakukan bergantian disebut gerak …|berselang|serempak|berlawanan|bertemu|Berselang.
=|Gerak yang dilakukan bersamaan disebut gerak …|serempak|Serempak.
=|Tari Serampang Dua Belas berasal dari Sumatera …|Utara|Sumatera Utara.
B|Tari berpasangan menuntut kekompakan.|Kompak.
S|Penari berpasangan bergerak tanpa menyesuaikan pasangan.|Menyesuaikan.
Tari Payung berasal dari …|Sumatera Barat|Bali|Papua|Jawa Timur|Sumbar.
Gerak penari dengan arah berbeda disebut gerak …|berlawanan|serempak|berurutan|bertemu|Berlawanan.
## SBD|Teater modern
Teater modern dipentaskan berdasarkan …|naskah tertulis|improvisasi saja|mimpi|undian|Naskah.
Orang yang memimpin pementasan teater adalah …|sutradara|aktor|penonton|penata rias|Sutradara.
=|Orang yang memerankan tokoh disebut …|aktor;pemeran|Aktor.
=|Orang yang mengatur lampu panggung disebut penata …|cahaya|Penata cahaya.
B|Pemain teater modern menghafal dialog.|Hafal.
S|Teater modern selalu tanpa naskah.|Pakai naskah.
Pada teater modern, penonton biasanya …|tidak terlibat langsung|ikut berdialog|naik panggung|menjadi pemain|Tidak terlibat.
Orang yang mengatur dekorasi panggung disebut penata …|panggung|cahaya|suara|rias|Panggung.
## SBD|Tata panggung
Nama lain tata panggung adalah …|skenografi|koreografi|kaligrafi|fotografi|Skenografi.
Panggung yang dikelilingi penonton disebut panggung …|arena|proscenium|thrust|tertutup|Arena.
=|Panggung yang dilihat dari depan saja disebut panggung …|proscenium|Proscenium.
=|Panggung yang dilihat dari tiga sisi disebut panggung …|thrust|Thrust.
B|Dekorasi pohon dapat menunjukkan latar hutan.|Latar.
S|Dekorasi sebaiknya menutupi pemain dari penonton.|Tidak.
Pendopo adalah panggung khas bangunan …|Jawa|Eropa|Cina|Arab|Jawa.
Dekorasi panggung berfungsi menunjukkan … cerita.|latar|harga tiket|nama penonton|jumlah kursi|Latar.
## SBD|Kerajinan tanah liat
Teknik membentuk tanah liat dengan menyusun gulungan disebut teknik …|pilin|pijit|lempeng|cetak|Pilin.
Karya tanah liat dibakar agar …|keras|lembek|basah|ringan sekali|Keras.
=|Teknik membentuk tanah liat dengan meja putar disebut teknik …|putar|Putar.
=|Teknik menyambung lembaran tanah liat disebut teknik …|lempeng|Lempeng.
B|Kasongan terkenal dengan gerabah.|Kasongan.
S|Karya tanah liat basah langsung dibakar agar kuat.|Dikeringkan.
Teknik membentuk tanah liat dengan jari disebut teknik …|pijit|pilin|cetak|putar|Pijit.
Hasil tanah liat yang dibakar disebut …|gerabah|anyaman|batik|tenun|Gerabah.
## SBD|Kerajinan bahan limbah
Botol plastik bekas dapat dibuat menjadi …|pot tanaman|makanan|obat|pupuk cair|Pot.
Kulit jagung dapat dibuat menjadi …|bunga hias|kaca|kabel|ban|Bunga.
=|Prinsip memakai kembali barang bekas disebut …|reuse|Reuse.
=|Prinsip mendaur ulang disebut …|recycle|Recycle.
B|Limbah perlu dibersihkan sebelum dibuat kerajinan.|Bersih.
S|Limbah kotor langsung dapat dipakai tanpa dibersihkan.|Dibersihkan.
Kaleng bekas dapat dibuat menjadi …|tempat pensil|piring makan|gelas minum|alat masak|Tempat pensil.
Pelepah pisang termasuk limbah …|organik|anorganik|logam|plastik|Organik.
## SBD|Wayang kulit
Pemain dan pencerita wayang disebut …|dalang|sinden|penabuh|penonton|Dalang.
Wayang kulit terbuat dari kulit …|kerbau|ikan|ular|kambing hutan|Kerbau.
=|Layar putih pertunjukan wayang disebut …|kelir|Kelir.
=|Lampu pertunjukan wayang disebut …|blencong|Blencong.
B|Wayang diakui UNESCO pada tahun 2003.|2003.
S|Wayang kulit tidak mengandung pesan moral.|Sarat pesan.
Penyanyi perempuan dalam pertunjukan wayang disebut …|sinden|dalang|penabuh|niyaga saja|Sinden.
Penanda awal dan akhir babak wayang disebut …|gunungan|kelir|blencong|kotak|Gunungan.
## PJOK|Teknik dasar sepak takraw
Jumlah pemain satu regu sepak takraw adalah …|tiga|lima|enam|sebelas|Tiga.
Sepak sila menggunakan kaki bagian …|dalam|luar|tumit|ujung|Dalam.
=|Menyundul bola dalam sepak takraw disebut …|heading|Heading.
=|Pemain yang melakukan servis dalam sepak takraw disebut …|tekong|Tekong.
B|Sepak takraw tidak boleh dimainkan dengan tangan.|Tangan.
S|Bola takraw boleh dipukul dengan tangan.|Tidak boleh.
Menyepak dengan punggung kaki disebut sepak …|kuda|sila|cungkil|badek|Kuda.
Menerima bola dengan paha disebut …|memaha|mendada|heading|sepak sila|Memaha.
## PJOK|Teknik dasar tenis meja
Pegangan bet seperti berjabat tangan disebut …|shakehand|penhold|backhand|forehand|Shakehand.
Satu gim tenis meja dimenangkan dengan angka …|11|21|15|25|11.
=|Pegangan bet seperti memegang pena disebut …|penhold|Penhold.
=|Pukulan keras menukik disebut …|smash|Smash.
B|Pukulan backhand memakai punggung tangan menghadap depan.|Backhand.
S|Satu gim tenis meja dimainkan sampai angka 21.|11.
Dorongan bola rendah dalam tenis meja disebut …|push|smash|lob|drive|Push.
Alat pemukul tenis meja disebut …|bet|raket|stik|pemukul kasti|Bet.
## PJOK|Lari jarak menengah
Nomor lari jarak menengah adalah …|800 meter|100 meter|200 meter|maraton|800 m.
Start pada lari jarak menengah adalah start …|berdiri|jongkok|melayang|duduk|Berdiri.
=|Nomor lari jarak menengah selain 800 meter adalah … meter.|1.500;1500|1.500.
=|Lari jarak menengah memerlukan kecepatan dan daya …|tahan|Daya tahan.
B|Pelari mempercepat lari menjelang finis.|Akhir.
S|Pelari jarak menengah sebaiknya sprint penuh sejak awal.|Atur tenaga.
Start lari 100 meter adalah start …|jongkok|berdiri|melayang|berkelompok|Jongkok.
Maraton memakai start …|berdiri massal|jongkok|melayang|duduk|Massal.
## PJOK|Lempar lembing
Saat melempar lembing, siku sebaiknya …|tinggi|rendah|lurus ke bawah|ditekuk ke perut|Tinggi.
Lembing sah jika yang lebih dulu menyentuh tanah adalah …|mata lembing|ekor lembing|tali lembing|pegangan|Mata.
=|Cara memegang lembing dengan ibu jari dan telunjuk disebut cara …|Amerika|Amerika.
=|Cara memegang lembing dengan ibu jari dan jari tengah disebut cara …|Finlandia|Finlandia.
B|Lembing harus jatuh di sektor lempar.|Sektor.
S|Pelempar boleh melewati garis lengkung batas lemparan.|Tidak boleh.
Cara memegang lembing dengan telunjuk dan jari tengah disebut cara …|tang|Amerika|Finlandia|biasa|Tang.
Gerak lanjutan setelah melempar dilakukan dengan badan condong ke …|depan|belakang|kiri|bawah|Depan.
## PJOK|Renang gaya dada
Nama lain renang gaya dada adalah gaya …|katak|bebas|kupu-kupu|punggung|Katak.
Napas pada gaya dada diambil saat kepala …|terangkat|menyelam|miring|diam di air|Terangkat.
=|Kaki gaya dada ditendang ke arah …|samping|Samping.
=|Saat meluncur, tangan diluruskan ke …|depan|Depan.
B|Gaya dada cocok untuk berenang santai jarak jauh.|Hemat tenaga.
S|Kaki gaya dada ditendang naik turun seperti gaya bebas.|Seperti katak.
Saat menekuk kaki gaya dada, tumit mendekati …|pantat|kepala|bahu|dada|Pantat.
Gaya dada memiliki gerakan yang …|pelan dan hemat tenaga|sangat cepat|tanpa napas|tanpa tangan|Hemat.
## PJOK|Latihan kekuatan otot
Push-up melatih otot …|lengan dan dada|perut|tungkai|punggung saja|Lengan.
Squat melatih otot …|tungkai|lengan|perut|leher|Tungkai.
=|Sit-up melatih otot …|perut|Perut.
=|Back-up melatih otot …|punggung|Punggung.
B|Latihan kekuatan perlu istirahat agar otot pulih.|Istirahat.
S|Latihan kekuatan otot tidak perlu istirahat sama sekali.|Perlu.
Plank melatih otot …|inti tubuh|jari|leher|mata|Inti.
Pull-up melatih otot …|lengan dan bahu|perut|betis|paha depan|Pull-up.
## PJOK|Teknik dasar kasti
Jumlah pemain satu regu kasti adalah …|dua belas|sembilan|enam|sebelas|12.
Tempat pelari aman dalam kasti disebut …|tiang hinggap|ruang bebas|garis pukul|ruang pelambung|Hinggap.
=|Pemain yang melempar bola kepada pemukul disebut …|pelambung|Pelambung.
=|Tempat menunggu giliran memukul disebut ruang …|bebas|Ruang bebas.
B|Penjaga dapat mematikan pelari dengan bola.|Mematikan.
S|Regu penjaga bertugas memukul bola.|Pemukul.
Teknik dasar kasti meliputi melempar, menangkap, memukul, dan …|berlari|menendang|menyundul|menggiring|Berlari.
Regu yang berjaga di lapangan disebut regu …|penjaga|pemukul|pelambung|cadangan|Penjaga.
## PJOK|Senam lantai lenting tangan
Nama lain lenting tangan adalah …|handspring|roll|kayang|split|Handspring.
Lenting tangan bertumpu pada …|kedua tangan|kepala|lutut|bahu|Tangan.
=|Latihan persiapan untuk kelentukan punggung adalah …|kayang|Kayang.
=|Lenting tangan dilakukan di atas …|matras|Matras.
B|Lenting tangan sebaiknya dibantu teman saat berlatih.|Bantuan.
S|Lenting tangan aman dilakukan tanpa pemanasan.|Pemanasan.
Latihan persiapan yang melatih kekuatan lengan adalah …|push-up|kayang|sikap lilin|meroda|Push-up.
Peregangan sebelum senam berfungsi …|mencegah cedera|membuat lelah|mengurangi kelentukan|memperlambat gerak|Cedera.
## PJOK|Senam aerobik
Senam aerobik melatih daya tahan …|jantung dan paru-paru|tulang|mata|kuku|Kardio.
Gerakan jalan di tempat dalam senam aerobik disebut …|march|jogging|grapevine|v-step|March.
=|Gerakan melangkah ke samping lalu merapat disebut step …|touch|Step touch.
=|Gerakan melangkah silang ke samping disebut …|grapevine|Grapevine.
B|Senam aerobik diawali pemanasan.|Pemanasan.
S|Senam aerobik dilakukan tanpa musik dan terputus-putus.|Berirama.
Gerakan mengangkat lutut disebut …|knee up|march|jogging|step touch|Knee up.
Rangkaian senam aerobik terakhir adalah …|pendinginan|pemanasan|gerakan inti|lompat tinggi|Pendinginan.
## PJOK|Lari gawang
Saat melewati gawang, kaki depan …|diluruskan|ditekuk ke dada|diangkat ke belakang|ditarik ke samping|Lurus.
Kaki belakang saat melewati gawang ditarik ke …|samping|depan|bawah|atas lurus|Samping.
=|Start lari gawang adalah start …|jongkok|Jongkok.
=|Jumlah langkah antargawang biasanya … langkah.|tiga;3|Tiga.
B|Irama langkah antargawang harus teratur.|Irama.
S|Gawang sebaiknya dilompati setinggi mungkin.|Rendah efisien.
Lari gawang adalah lari cepat sambil melewati …|rintangan|kolam|tali|bak pasir|Rintangan.
Setelah mendarat dari gawang, pelari …|lari kembali|berhenti|duduk|berbalik|Lari.
## PJOK|Lompat jangkit
Lompat jangkit terdiri atas hop, step, dan …|jump|run|walk|roll|Jump.
Pada tahap hop, pelompat mendarat dengan kaki yang …|sama dengan tumpuan|berlawanan|dua kaki|tangan|Sama.
=|Pada tahap step, pelompat mendarat dengan kaki yang …|berlawanan|Berlawanan.
=|Lompat jangkit dalam bahasa Inggris disebut … jump.|triple|Triple jump.
B|Pendaratan akhir lompat jangkit di bak pasir.|Pasir.
S|Lompat jangkit terdiri atas satu gerakan lompat saja.|Tiga.
Jarak lompat jangkit diukur dari …|papan tumpuan|garis start lari|ujung bak|tengah bak|Papan.
Awalan lompat jangkit dilakukan dengan …|lari cepat|jalan santai|merangkak|berdiri diam|Lari.
## PJOK|Teknik dasar softball
Jumlah pemain satu regu softball adalah …|sembilan|dua belas|lima|sebelas|Sembilan.
Pemain yang melempar bola kepada pemukul disebut …|pitcher|catcher|batter|shortstop|Pitcher.
=|Pemain yang menangkap bola di belakang pemukul disebut …|catcher|Catcher.
=|Alat pemukul softball disebut …|bat|Bat.
B|Pitcher softball melempar bola dari bawah.|Underhand.
S|Lapangan softball berbentuk lingkaran tanpa base.|Intan.
Regu mendapat angka jika pelari kembali ke …|home base|base pertama|ruang bebas|tribun|Home.
Sarung tangan penangkap bola disebut …|glove|bat|helm|base|Glove.
## PJOK|Pemanasan dan pendinginan
Pemanasan bertujuan mencegah …|cedera|lapar|kantuk|haus|Cedera.
Peregangan yang dilakukan saat pemanasan adalah peregangan …|dinamis|statis|pasif|diam|Dinamis.
=|Peregangan dengan menahan posisi saat pendinginan disebut peregangan …|statis|Statis.
=|Pendinginan menurunkan denyut … secara bertahap.|jantung;nadi|Jantung.
B|Jogging ringan termasuk pemanasan.|Pemanasan.
S|Pendinginan boleh dilewati setelah olahraga berat.|Penting.
Jalan santai setelah lari termasuk …|pendinginan|pemanasan|gerakan inti|latihan beban|Pendinginan.
Setelah olahraga sebaiknya …|minum air|langsung tidur|makan pedas|mandi air es|Minum.
## PJOK|Pola tidur sehat
Remaja membutuhkan tidur sekitar …|8–10 jam|3–4 jam|5 jam|12–14 jam|8–10.
Kebiasaan yang mengganggu tidur adalah …|bermain gawai sebelum tidur|tidur jam teratur|kamar gelap|olahraga sore|Gawai.
=|Kebiasaan tidak tidur sampai larut malam disebut …|begadang|Begadang.
=|Minuman yang sebaiknya dihindari malam hari mengandung …|kafein|Kafein.
B|Tidur cukup membantu daya ingat.|Memori.
S|Begadang meningkatkan konsentrasi belajar.|Menurun.
Kamar yang gelap dan tenang membuat tidur …|nyenyak|terganggu|singkat|gelisah|Nyenyak.
Tidur dan bangun pada jam yang sama membuat tubuh …|lebih segar|lemas|sakit|lapar|Segar.
## PJOK|Penyakit tidak menular
Contoh penyakit tidak menular adalah …|diabetes|flu|cacar air|TBC|Diabetes.
Konsumsi garam berlebihan meningkatkan risiko …|hipertensi|rabun|cacingan|kurap|Hipertensi.
=|Konsumsi gula berlebihan meningkatkan risiko …|diabetes|Diabetes.
=|Kelebihan berat badan karena kurang gerak disebut …|obesitas|Obesitas.
B|Merokok meningkatkan risiko kanker paru.|Rokok.
S|Penyakit tidak menular hanya menyerang orang tua.|Semua usia.
Cara mencegah penyakit tidak menular adalah …|aktivitas fisik teratur|makan gorengan setiap hari|merokok|tidur larut|Gerak.
Gigi berlubang dapat dicegah dengan …|menyikat gigi teratur|makan permen terus|jarang minum|tidur siang|Sikat gigi.
## PJOK|Keselamatan di jalan raya
Tempat menyeberang yang aman adalah …|zebra cross|tengah tikungan|di belakang bus|di antara mobil parkir|Zebra cross.
Lampu lalu lintas merah berarti …|berhenti|jalan|hati-hati|percepat|Berhenti.
=|Lampu lalu lintas hijau berarti boleh …|jalan|Jalan.
=|Pesepeda wajib memakai …|helm|Helm.
B|Remaja di bawah 17 tahun belum boleh mengendarai motor.|SIM.
S|Menyeberang boleh di sembarang tempat tanpa melihat kiri kanan.|Hati-hati.
Lampu kuning berarti …|hati-hati bersiap|boleh ngebut|berhenti total|putar balik|Kuning.
Pejalan kaki sebaiknya berjalan di …|trotoar|tengah jalan|jalur cepat|rel kereta|Trotoar.
"""

SAS += """
## SBD 1
0|Gambar jalan lurus dengan satu titik pertemuan di horizon memakai perspektif ....|satu titik hilang|dua titik hilang|tiga titik hilang|tanpa titik|Satu.
1|Bentuk dasar kardus adalah ....|balok|bola|kerucut|silinder|Balok.
2|Teknik cetak yang hanya menghasilkan satu kali cetakan disebut ....|monoprint|sablon|litografi|cukil|Monoprint.
3|Bagian komik berisi kotak adegan disebut ....|panel|balon kata|narasi|efek suara|Panel.
4|Kolase dari daun dan ranting disebut kolase ....|alam|keramik|kertas|kaca|Alam.
5|Tamborin termasuk alat musik ....|ritmis|melodis|harmonis|tiup|Ritmis.
6|Nada fa pada tangga nada C mayor adalah ....|F|E|G|D|F.
7|Ansambel angklung termasuk ansambel ....|sejenis|campuran|orkestra|band|Sejenis.
## SBD 2
0|Tari Ratoh Jaroe berasal dari tari duduk ....|Aceh|Bali|Papua|Betawi|Aceh.
1|Unsur pendukung tari berupa musik pengiring disebut ....|iringan|rias|busana|properti|Iringan.
2|Gerak penari yang menyusul satu per satu disebut gerak ....|berurutan|serempak|berlawanan|bertemu|Berurutan.
3|Penonton dalam teater modern berperan ....|menikmati pertunjukan|memimpin pementasan|menulis naskah|mengatur lampu|Penonton.
4|Panggung yang berada di ruang luar disebut panggung ....|terbuka|arena tertutup|proscenium|thrust|Terbuka.
5|Teknik tanah liat dengan menambah dan mengurangi bahan disebut ....|butsir|pilin|lempeng|putar|Butsir.
6|Koran bekas dapat dianyam menjadi ....|keranjang|piring keramik|gelas kaca|sendok logam|Keranjang.
7|Musik pengiring pertunjukan wayang kulit adalah ....|gamelan|band|orkestra|angklung|Gamelan.
## PJOK 1
0|Menyepak bola takraw dengan ujung kaki disebut sepak ....|cungkil|sila|kuda|badek|Cungkil.
1|Pukulan tenis meja dari sisi kanan untuk pemain tangan kanan disebut ....|forehand|backhand|push|chop|Forehand.
2|Lari 400 meter dimulai dengan start ....|jongkok|berdiri|melayang|massal|Jongkok.
3|Teknik memegang lembing yang memakai ibu jari dan jari tengah adalah cara ....|Finlandia|Amerika|tang|Jepang|Finlandia.
4|Tahap gaya dada ketika kedua kaki lurus kembali disebut ....|merapat|meluncur|tekuk|tarikan|Merapat.
5|Latihan kekuatan otot sebaiknya dilakukan ....|bertahap|sekaligus berat|tanpa istirahat|tanpa pemanasan|Bertahap.
6|Dalam kasti, mengenai pelari dengan bola disebut ....|mematikan|memukul|melambung|hinggap|Mematikan.
7|Meroda melatih koordinasi ....|tangan dan kaki|mata saja|telinga|jari kaki|Meroda.
## PJOK 2
0|Gerakan melangkah membentuk huruf V dalam senam aerobik disebut ....|v-step|march|jogging|knee up|V-step.
1|Kaki depan yang menapak setelah melewati gawang termasuk tahap ....|mendarat|start|awalan|antargawang|Mendarat.
2|Tahap terakhir lompat jangkit adalah ....|jump|hop|step|run|Jump.
3|Posisi pemain softball yang menjaga antara base 2 dan 3 adalah ....|shortstop|pitcher|catcher|batter|Shortstop.
4|Gerakan inti dalam olahraga dilakukan ....|setelah pemanasan|sebelum pemanasan|setelah tidur|tanpa pemanasan|Urutan.
5|Olahraga sore membuat seseorang ....|lebih mudah tidur|sulit tidur|lapar terus|pusing|Tidur.
6|Faktor risiko utama penyakit jantung adalah ....|lemak jenuh dan rokok|sayuran|buah|air putih|Jantung.
7|Lampu merah pejalan kaki berarti ....|dilarang menyeberang|boleh menyeberang|hati-hati|lari cepat|Dilarang.
"""

TOPICS += """
## INF
# 1|Data, Perangkat, dan Jaringan
@ Representasi data teks dan gambar
min: 15
act: Perbesar foto di HP sampai terlihat kotak-kotak kecil, lalu jelaskan apa itu piksel.
mis: mengira komputer menyimpan huruf dan gambar apa adanya
exp: Komputer menyimpan semua data dalam bentuk biner. Huruf disimpan sebagai kode angka, misalnya dengan standar ASCII atau Unicode, contohnya huruf A berkode 65. Gambar digital tersusun atas piksel, yaitu titik-titik kecil yang masing-masing memiliki nilai warna. Warna sering disusun dari campuran merah, hijau, dan biru atau RGB.
ex: Huruf A disimpan sebagai angka 65 dalam ASCII. // Foto 1.000 × 1.000 piksel berisi satu juta piksel.
pt: Data disimpan dalam biner ; Huruf memakai kode ASCII atau Unicode ; Gambar tersusun atas piksel RGB
sum: Teks dan gambar diubah menjadi angka agar dapat diolah komputer.
fig: table Data | Cara disimpan ;; huruf | kode ASCII atau Unicode ;; gambar | kumpulan piksel ;; warna | nilai RGB ;; suara | sampel gelombang ;; video | rangkaian gambar ;; emoji | kode Unicode ~ Representasi data.
@ Satuan penyimpanan data
min: 15
act: Periksa kapasitas memori HP atau laptop keluarga dan sisa ruang penyimpanannya.
mis: mengira 1 KB sama dengan 100 byte
exp: Satuan terkecil data adalah bit. Delapan bit membentuk satu byte. Satuan yang lebih besar adalah kilobyte (KB), megabyte (MB), gigabyte (GB), dan terabyte (TB). Dalam perhitungan komputer, 1 KB = 1.024 byte, 1 MB = 1.024 KB, dan seterusnya. Lagu sekitar 4 MB, sedangkan film dapat mencapai beberapa GB.
ex: Flashdisk 16 GB dapat menyimpan ribuan foto. // Pesan teks singkat hanya beberapa byte.
pt: 8 bit = 1 byte ; KB, MB, GB, TB ; 1 KB = 1.024 byte
sum: Satuan data membantu memperkirakan kebutuhan penyimpanan.
fig: table Satuan | Setara dengan ;; 1 byte | 8 bit ;; 1 KB | 1.024 byte ;; 1 MB | 1.024 KB ;; 1 GB | 1.024 MB ;; 1 TB | 1.024 GB ;; 1 PB | 1.024 TB ~ Satuan penyimpanan data.
@ Logika boolean
min: 15
act: Buat tabel kebenaran untuk pernyataan "boleh main jika PR selesai DAN kamar rapi".
mis: mengira OR bernilai benar hanya jika kedua syarat benar
exp: Logika boolean hanya memiliki dua nilai, yaitu benar (1) dan salah (0). Operator AND bernilai benar jika kedua masukan benar. Operator OR bernilai benar jika salah satu atau kedua masukan benar. Operator NOT membalik nilai. Logika boolean menjadi dasar kerja rangkaian komputer dan percabangan program.
ex: 1 AND 0 = 0. // 1 OR 0 = 1.
pt: Nilai benar dan salah ; AND, OR, NOT ; Dasar rangkaian komputer
sum: Logika boolean adalah dasar pengambilan keputusan komputer.
fig: table Operasi | Hasil ;; 1 AND 1 | 1 ;; 1 AND 0 | 0 ;; 0 OR 0 | salah ;; 1 OR 0 | benar ;; NOT 1 | nol ;; NOT 0 | satu ~ Contoh operasi boolean.
@ Komponen CPU dan memori
min: 15
act: Lihat informasi prosesor dan RAM pada pengaturan HP atau komputer keluarga.
mis: menyamakan RAM dengan penyimpanan internal
exp: CPU atau prosesor adalah otak komputer yang memproses perintah. CPU terdiri atas ALU untuk perhitungan dan logika, serta unit kendali untuk mengatur jalannya perintah. RAM adalah memori sementara tempat data diproses dan akan hilang jika komputer dimatikan. Penyimpanan seperti SSD dan HDD menyimpan data secara permanen.
ex: RAM besar membuat banyak aplikasi lancar dibuka bersamaan. // Foto disimpan di SSD agar tidak hilang.
pt: CPU otak komputer ; ALU dan unit kendali ; RAM sementara, SSD permanen
sum: CPU, RAM, dan penyimpanan bekerja sama memproses data.
fig: table Komponen | Fungsi ;; CPU | memproses perintah ;; ALU | menghitung dan membandingkan ;; unit kendali | mengatur perintah ;; RAM | memori kerja sementara ;; SSD | penyimpanan permanen cepat ;; GPU | memproses grafis ~ Komponen komputer.
@ Perangkat masukan dan keluaran
min: 15
act: Daftar perangkat di rumah, lalu kelompokkan menjadi masukan, keluaran, atau keduanya.
mis: menganggap monitor sebagai perangkat masukan
exp: Perangkat masukan atau input memasukkan data ke komputer, misalnya keyboard, mouse, mikrofon, kamera, dan pemindai. Perangkat keluaran atau output menampilkan hasil, misalnya monitor, printer, dan speaker. Ada perangkat yang berfungsi keduanya, misalnya layar sentuh dan headset dengan mikrofon.
ex: Mikrofon merekam suara (masukan). // Printer mencetak dokumen (keluaran).
pt: Input memasukkan data ; Output menampilkan hasil ; Layar sentuh berfungsi keduanya
sum: Perangkat masukan dan keluaran menghubungkan manusia dengan komputer.
fig: table Perangkat | Jenis ;; keyboard | masukan ;; pemindai | masukan gambar ;; monitor | keluaran ;; printer | keluaran cetak ;; speaker | keluaran suara ;; layar sentuh | masukan dan keluaran ~ Perangkat masukan dan keluaran.
@ Jaringan lokal
min: 15
act: Gambar denah jaringan Wi-Fi di rumah: router dan perangkat yang terhubung.
mis: mengira Wi-Fi sama dengan internet
exp: Jaringan lokal atau LAN adalah jaringan komputer dalam area kecil seperti rumah, sekolah, atau kantor. Perangkat terhubung melalui kabel atau nirkabel (Wi-Fi). Router menghubungkan jaringan lokal dengan internet. Wi-Fi hanya cara terhubung tanpa kabel ke router; internet tersedia jika router tersambung ke penyedia layanan.
ex: Laptop dan HP di rumah terhubung ke router Wi-Fi. // Laboratorium komputer sekolah memakai LAN kabel.
pt: LAN area kecil ; Kabel atau Wi-Fi ; Router menghubungkan ke internet
sum: Jaringan lokal memungkinkan perangkat saling berbagi.
fig: table Jenis jaringan | Cakupan ;; PAN | sekitar satu orang ;; LAN | satu gedung ;; MAN | satu kota ;; WAN | antarnegara ;; WLAN | lokal tanpa kabel ;; internet | seluruh dunia ~ Jenis jaringan menurut cakupan.
@ Topologi jaringan
min: 15
act: Gambar tiga bentuk topologi jaringan memakai benang dan kertas.
mis: mengira semua topologi sama tahannya bila satu kabel putus
exp: Topologi jaringan adalah bentuk susunan perangkat dalam jaringan. Topologi bus memakai satu kabel utama. Topologi star memusatkan semua perangkat pada satu switch atau hub. Topologi ring membentuk lingkaran. Topologi mesh menghubungkan setiap perangkat dengan banyak perangkat lain sehingga paling tahan gangguan.
ex: Laboratorium sekolah umumnya memakai topologi star. // Pada topologi bus, kabel utama putus membuat jaringan mati.
pt: Bentuk susunan perangkat ; Bus, star, ring, mesh ; Mesh paling tahan gangguan
sum: Topologi memengaruhi keandalan jaringan.
fig: table Topologi | Ciri ;; bus | satu kabel utama ;; star | terpusat pada switch ;; ring | membentuk lingkaran ;; mesh | saling terhubung banyak jalur ;; tree | gabungan bertingkat ;; hybrid | campuran beberapa topologi ~ Topologi jaringan.
@ Graf dan jalur terpendek
min: 15
act: Gambar peta jalan dari rumah ke sekolah sebagai titik dan garis, lalu cari jalur terpendek.
mis: memilih jalur dengan titik paling sedikit tanpa melihat jaraknya
exp: Graf adalah struktur data yang terdiri atas simpul atau node dan sisi atau edge yang menghubungkannya. Sisi dapat diberi bobot, misalnya jarak atau waktu. Graf dipakai untuk peta, jaringan pertemanan, dan rute pengiriman. Mencari jalur terpendek berarti mencari rute dengan jumlah bobot paling kecil.
ex: Aplikasi peta mencari rute tercepat dengan graf. // Kota sebagai simpul, jalan sebagai sisi.
pt: Simpul dan sisi ; Sisi berbobot jarak atau waktu ; Jalur terpendek bobot terkecil
sum: Graf membantu memecahkan masalah rute.
fig: table Contoh graf | Simpul ;; peta kota | persimpangan ;; jaringan pertemanan | orang ;; rute bus | halte ;; jaringan komputer | perangkat ;; silsilah keluarga | anggota keluarga ;; rute pengiriman | gudang dan alamat ~ Contoh penerapan graf.
# 2|Informasi, Data, dan Web
@ Verifikasi sumber informasi
min: 15
act: Pilih satu berita viral, lalu periksa kebenarannya di minimal dua sumber terpercaya.
mis: langsung percaya informasi karena banyak dibagikan
exp: Literasi informasi adalah kemampuan mencari, menilai, dan memakai informasi dengan tepat. Ciri sumber terpercaya antara lain jelas penulis atau lembaganya, mencantumkan tanggal, memiliki rujukan, dan tidak memakai judul provokatif. Bandingkan informasi dari beberapa sumber sebelum mempercayainya.
ex: Situs pemerintah berakhiran go.id. // Berita tanpa tanggal perlu diragukan.
pt: Mencari, menilai, memakai informasi ; Penulis, tanggal, rujukan jelas ; Bandingkan beberapa sumber
sum: Periksa sebelum percaya dan membagikan.
fig: table Ciri | Sumber terpercaya atau meragukan ;; penulis jelas | terpercaya ;; tanpa tanggal | meragukan ;; ada rujukan | terpercaya dan dapat dicek ;; judul provokatif | meragukan dan memancing emosi ;; situs resmi lembaga | terpercaya resmi ;; meminta segera disebarkan | meragukan dan mendesak ~ Ciri sumber informasi.
@ Hoaks dan cek fakta
min: 15
act: Gunakan situs cek fakta untuk memeriksa satu kabar yang beredar di grup keluarga.
mis: membagikan kabar dulu baru memeriksa kebenarannya
exp: Hoaks adalah informasi bohong yang sengaja dibuat seolah benar. Ciri hoaks antara lain judul sensasional, sumber tidak jelas, foto yang diambil dari kejadian lain, dan ajakan menyebarkan. Cek fakta dilakukan dengan mencari sumber asli, memeriksa foto dengan pencarian gambar terbalik, dan melihat situs cek fakta.
ex: Foto banjir lama disebarkan sebagai kejadian hari ini. // Pesan berantai meminta disebar ke sepuluh grup.
pt: Informasi bohong yang disengaja ; Judul sensasional dan sumber tidak jelas ; Cek sumber asli dan pencarian gambar
sum: Cek fakta menghentikan penyebaran hoaks.
fig: table Langkah cek fakta | Tujuan ;; baca utuh | tidak terkecoh judul ;; cari sumber asli | memastikan asal berita ;; pencarian gambar terbalik | mengecek foto lama ;; bandingkan media lain | memastikan kebenaran ;; situs cek fakta | melihat hasil verifikasi ;; tahan membagikan | mencegah penyebaran ~ Langkah cek fakta.
@ Basis data sederhana
min: 15
act: Buat tabel data buku di rak rumah berisi judul, penulis, tahun, dan jenis.
mis: mengisi satu kolom dengan jenis data yang berbeda-beda
exp: Basis data adalah kumpulan data yang tersusun rapi sehingga mudah dicari dan diolah. Data disusun dalam tabel yang terdiri atas baris atau record dan kolom atau field. Setiap record sebaiknya memiliki kunci unik, misalnya nomor induk siswa. Basis data dipakai di perpustakaan, toko, dan sekolah.
ex: Data siswa disimpan dengan NIS sebagai kunci. // Satu baris berisi data satu buku.
pt: Kumpulan data tersusun rapi ; Record dan field ; Kunci unik
sum: Basis data memudahkan pencarian informasi.
fig: table Istilah | Arti ;; record | satu baris data ;; field | satu kolom data ;; tabel | kumpulan record ;; kunci utama | penanda unik setiap record ;; kueri | perintah mencari data ;; basis data | kumpulan tabel ~ Istilah basis data.
@ Mengurutkan dan menyaring data
min: 15
act: Urutkan data nilai teman sekelas dari tertinggi, lalu saring yang nilainya di atas 80.
mis: mengurutkan satu kolom saja sehingga data antarkolom tertukar
exp: Lembar kerja dapat mengurutkan atau sort data dari kecil ke besar (ascending) atau besar ke kecil (descending). Fitur filter menyaring data sehingga hanya menampilkan data yang memenuhi syarat. Saat mengurutkan, seluruh baris harus ikut terurut agar data tidak tertukar.
ex: Mengurutkan nama siswa dari A ke Z. // Menyaring siswa yang berasal dari kelas 8A.
pt: Sort ascending dan descending ; Filter menampilkan data bersyarat ; Seluruh baris ikut terurut
sum: Sort dan filter mempercepat analisis data.
fig: table Fitur | Hasil ;; sort A ke Z | urutan abjad naik ;; sort Z ke A | urutan abjad turun ;; sort terkecil | angka naik ;; sort terbesar | angka turun ;; filter | hanya data bersyarat ;; hapus filter | semua data tampil ~ Fitur sort dan filter.
@ Membuat halaman web dengan HTML
min: 15
act: Tulis halaman HTML sederhana berisi judul, paragraf, dan gambar tentang hobimu.
mis: lupa menutup tag sehingga tampilan berantakan
exp: HTML atau HyperText Markup Language adalah bahasa untuk menyusun halaman web. HTML memakai tag yang biasanya berpasangan, yaitu tag pembuka dan tag penutup. Contohnya h1 untuk judul, p untuk paragraf, img untuk gambar, dan a untuk tautan. Halaman HTML dibuka dengan peramban.
ex: <h1>Hobiku</h1> menampilkan judul besar. // <a href="..."> membuat tautan.
pt: Bahasa penyusun halaman web ; Tag pembuka dan penutup ; h1, p, img, a
sum: HTML adalah dasar pembuatan situs web.
fig: table Tag HTML | Fungsi ;; h1 | judul utama ;; p | paragraf ;; img | gambar ;; a | tautan ;; ul | daftar berbutir ;; table | tabel ~ Tag HTML dasar.
@ Desain antarmuka pengguna
min: 15
act: Gambar rancangan layar aplikasi jadwal pelajaran dengan tombol yang mudah dipahami.
mis: memakai terlalu banyak warna dan tulisan kecil pada aplikasi
exp: Antarmuka pengguna atau user interface adalah tampilan yang dipakai orang untuk berinteraksi dengan aplikasi. Prinsip desain yang baik meliputi sederhana, konsisten, mudah dibaca, memberi umpan balik, dan mudah dipakai semua orang. Pengalaman pengguna atau user experience menilai seberapa nyaman aplikasi dipakai.
ex: Tombol hapus diberi warna merah agar jelas. // Ikon dan letak menu sama di setiap halaman.
pt: Tampilan untuk berinteraksi ; Sederhana, konsisten, mudah dibaca ; Umpan balik dan aksesibel
sum: Desain yang baik membuat aplikasi mudah dipakai.
fig: table Prinsip | Contoh ;; sederhana | sedikit tombol penting ;; konsisten | menu di posisi sama ;; mudah dibaca | huruf cukup besar ;; umpan balik | pesan tersimpan ;; kontras | teks gelap di latar terang ;; aksesibel | bisa dipakai tunanetra ~ Prinsip desain antarmuka.
@ Jejak digital dan reputasi daring
min: 15
act: Cari namamu di mesin pencari bersama orang tua, lalu lihat informasi apa yang muncul.
mis: mengira unggahan yang dihapus pasti hilang selamanya
exp: Jejak digital adalah rekam aktivitas seseorang di internet, seperti unggahan, komentar, dan riwayat pencarian. Jejak digital aktif sengaja kita buat, sedangkan jejak pasif terkumpul tanpa disadari. Jejak digital dapat disalin dan sulit dihapus sehingga memengaruhi reputasi, misalnya saat mendaftar sekolah atau bekerja.
ex: Komentar kasar dapat ditangkap layar orang lain. // Situs mencatat lokasi saat kita membukanya.
pt: Rekam aktivitas di internet ; Jejak aktif dan pasif ; Sulit dihapus dan memengaruhi reputasi
sum: Bangun jejak digital yang positif.
fig: table Aktivitas | Jenis jejak ;; mengunggah foto | aktif ;; menulis komentar | aktif publik ;; riwayat pencarian | pasif ;; data lokasi | pasif otomatis ;; mengisi formulir daring | aktif data pribadi ;; cookies situs | pasif peramban ~ Jenis jejak digital.

@ Kompresi data
min: 15
act: Kompres satu folder foto menjadi berkas ZIP, lalu bandingkan ukuran sebelum dan sesudah.
mis: mengira kompresi lossy dapat mengembalikan kualitas gambar seperti semula
exp: Kompresi data adalah cara memperkecil ukuran berkas agar hemat ruang dan cepat dikirim. Kompresi lossless tidak menghilangkan data sehingga berkas dapat dikembalikan utuh, misalnya ZIP dan PNG. Kompresi lossy membuang sebagian data yang kurang terasa sehingga ukuran jauh lebih kecil, misalnya JPG dan MP3.
ex: Folder tugas dikompres menjadi ZIP sebelum dikirim. // Foto JPG berukuran lebih kecil daripada foto asli.
pt: Memperkecil ukuran berkas ; Lossless dapat kembali utuh ; Lossy membuang sebagian data
sum: Kompresi menghemat ruang dan mempercepat pengiriman.
fig: table Format | Jenis kompresi ;; ZIP | lossless ;; PNG | lossless gambar ;; JPG | lossy ;; MP3 | lossy audio ;; MP4 | lossy video ;; FLAC | lossless audio ~ Format dan jenis kompresi.

## KKA
# 1|Pemrograman Lanjutan
@ Operator logika dalam program
min: 15
act: Tulis syarat masuk taman bermain: umur di atas 5 dan tinggi di atas 100 cm memakai and.
mis: memakai or padahal kedua syarat harus terpenuhi
exp: Operator logika menggabungkan beberapa syarat dalam program. Dalam Python dipakai and, or, dan not. Syarat dengan and benar jika semua syarat benar. Syarat dengan or benar jika salah satu syarat benar. not membalik nilai benar menjadi salah dan sebaliknya.
ex: if umur > 5 and tinggi > 100: print("Boleh") // if hujan or mendung: bawa payung.
pt: and, or, not ; and semua benar ; or salah satu benar
sum: Operator logika membuat syarat program lebih lengkap.
fig: table Ekspresi | Nilai ;; True and True | True ;; True and False | False ;; False or True | benar ;; False or False | salah ;; not True | False dibalik ;; not False | True dibalik ~ Operator logika Python.
@ Pengolahan string
min: 15
act: Buat program yang mengubah namamu menjadi huruf besar dan menghitung jumlah hurufnya.
mis: mengira indeks string dimulai dari 1
exp: String adalah teks dalam program. String dapat digabung dengan +, dihitung panjangnya dengan len, dan diambil hurufnya dengan indeks mulai 0. Metode string antara lain upper untuk huruf besar, lower untuk huruf kecil, dan replace untuk mengganti kata.
ex: "bobo".upper() menghasilkan BOBO. // len("kelas") menghasilkan 5.
pt: Teks dalam program ; Digabung dengan + ; upper, lower, replace
sum: Pengolahan string penting untuk program berbasis teks.
fig: table Perintah | Hasil ;; "bobo".upper() | BOBO ;; "BOBO".lower() | bobo ;; len("kelas") | 5 ;; "ab" + "cd" | abcd ;; "kucing"[0] | k ;; "aku suka".replace("suka", "senang") | aku senang ~ Pengolahan string Python.
@ Dictionary dalam Python
min: 15
act: Buat dictionary berisi nama teman dan hobinya, lalu tampilkan hobi salah satu teman.
mis: mengakses dictionary dengan indeks angka seperti list
exp: Dictionary adalah tipe data yang menyimpan pasangan kunci dan nilai, ditulis di dalam kurung kurawal. Nilai diambil dengan menyebut kuncinya, bukan indeks angka. Dictionary cocok untuk menyimpan data seperti kamus, kontak, atau nilai siswa.
ex: nilai = {"Budi": 85, "Sari": 90} // nilai["Sari"] menghasilkan 90.
pt: Pasangan kunci dan nilai ; Kurung kurawal ; Diakses dengan kunci
sum: Dictionary memudahkan mencari data dengan nama.
fig: table Perintah dictionary | Fungsi ;; d["kunci"] | mengambil nilai ;; d["baru"] = 5 | menambah pasangan ;; del d["kunci"] | menghapus pasangan ;; d.keys() | daftar kunci ;; d.values() | daftar nilai ;; len(d) | banyak pasangan ~ Perintah dictionary.
@ Perulangan bersarang
min: 15
act: Buat program yang mencetak tabel perkalian 1 sampai 5 memakai dua perulangan.
mis: salah menjorokkan perulangan dalam sehingga hasil tidak sesuai
exp: Perulangan bersarang adalah perulangan di dalam perulangan lain. Perulangan dalam dijalankan sampai selesai untuk setiap putaran perulangan luar. Perulangan bersarang dipakai untuk membuat tabel, pola bintang, atau memproses data berbentuk baris dan kolom.
ex: for i in range(3): for j in range(2): print(i, j) // Pola segitiga bintang.
pt: Perulangan di dalam perulangan ; Dalam selesai setiap putaran luar ; Untuk tabel dan pola
sum: Perulangan bersarang mengolah data dua dimensi.
fig: table Perulangan luar | Banyak putaran total jika dalam 3 kali ;; 1 kali | 3 ;; 2 kali | 6 ;; 3 kali | 9 ;; 4 kali | 12 ;; 5 kali | 15 ;; 10 kali | 30 ~ Banyak putaran perulangan bersarang.
@ Modul random dan math
min: 15
act: Buat program pelempar dadu yang menampilkan angka acak 1 sampai 6.
mis: memakai fungsi modul tanpa menulis import
exp: Modul adalah kumpulan fungsi siap pakai di Python. Modul dipanggil dengan import. Modul random menghasilkan bilangan acak, misalnya random.randint(1, 6). Modul math berisi fungsi matematika, misalnya math.sqrt untuk akar kuadrat dan math.pi untuk nilai pi.
ex: import random lalu random.randint(1, 6). // math.sqrt(16) menghasilkan 4.0.
pt: Kumpulan fungsi siap pakai ; Dipanggil dengan import ; random dan math
sum: Modul menghemat waktu menulis program.
fig: table Fungsi | Kegunaan ;; random.randint(1, 6) | angka acak 1 sampai 6 ;; random.choice(list) | memilih anggota acak ;; math.sqrt(x) | akar kuadrat ;; math.pi | nilai pi ;; math.floor(x) | pembulatan ke bawah ;; math.ceil(x) | pembulatan ke atas ~ Fungsi modul random dan math.
@ Membaca dan menulis berkas
min: 15
act: Buat program yang menyimpan daftar belanja ke berkas teks, lalu membacanya kembali.
mis: membuka berkas dengan mode w sehingga isi lama terhapus
exp: Program dapat menyimpan data ke berkas agar tidak hilang saat program ditutup. Dalam Python, berkas dibuka dengan open(nama, mode). Mode r untuk membaca, w untuk menulis ulang, dan a untuk menambah di akhir. Perintah with membuat berkas tertutup otomatis.
ex: with open("data.txt", "a") as f: f.write("apel") // with open("data.txt") as f: print(f.read())
pt: Menyimpan data agar tidak hilang ; Mode r, w, a ; with menutup berkas otomatis
sum: Berkas membuat data program tersimpan permanen.
fig: table Mode | Fungsi ;; r | membaca ;; w | menulis ulang ;; a | menambah di akhir ;; x | membuat berkas baru ;; r+ | membaca dan menulis ;; rb | membaca berkas biner ~ Mode membuka berkas.
@ Proyek tebak angka
min: 15
act: Buat permainan tebak angka 1 sampai 20 yang memberi petunjuk terlalu besar atau terlalu kecil.
mis: tidak mengubah tebakan menjadi angka sehingga perbandingan error
exp: Proyek tebak angka menggabungkan beberapa konsep: modul random untuk angka rahasia, input untuk tebakan, int untuk mengubah teks menjadi angka, perulangan while sampai tebakan benar, dan percabangan untuk memberi petunjuk. Proyek dibuat bertahap: rancang, tulis, uji, lalu perbaiki.
ex: rahasia = random.randint(1, 20) // if tebak > rahasia: print("Terlalu besar")
pt: random, input, int ; while sampai benar ; if memberi petunjuk
sum: Proyek kecil melatih menggabungkan konsep pemrograman.
fig: table Bagian program | Konsep ;; angka rahasia | modul random ;; meminta tebakan | input ;; mengubah ke angka | int ;; mengulang tebakan | while ;; memberi petunjuk | if elif else ;; menghitung percobaan | variabel penghitung ~ Bagian proyek tebak angka.
@ Pemrograman berbasis blok
min: 15
act: Buat animasi sederhana di Scratch: tokoh berjalan dan berbicara saat bendera hijau diklik.
mis: menyusun blok tanpa blok pemicu sehingga program tidak berjalan
exp: Pemrograman berbasis blok menyusun program dengan menyambung blok perintah seperti puzzle, misalnya di Scratch. Ada blok gerak, tampilan, suara, kendali, sensor, dan operator. Program dimulai dengan blok pemicu, misalnya ketika bendera hijau diklik. Konsep yang dipelajari sama dengan bahasa teks: urutan, perulangan, dan percabangan.
ex: Blok ulangi 10 kali untuk perulangan. // Blok jika-maka untuk percabangan.
pt: Menyambung blok seperti puzzle ; Blok gerak, kendali, sensor ; Dimulai blok pemicu
sum: Pemrograman blok memudahkan memahami logika program.
fig: table Kategori blok | Contoh ;; gerak | maju 10 langkah ;; tampilan | katakan halo ;; suara | mainkan suara ;; kendali | ulangi 10 kali ;; sensor | menyentuh tepi ;; peristiwa | ketika bendera hijau diklik ~ Kategori blok Scratch.
# 2|Kecerdasan Artifisial dalam Kehidupan
@ Visi komputer
min: 15
act: Coba fitur pencarian dengan kamera di HP untuk mengenali tanaman atau benda.
mis: mengira komputer melihat gambar seperti mata manusia
exp: Visi komputer atau computer vision adalah bidang KA yang membuat komputer dapat mengenali isi gambar dan video. Komputer membaca gambar sebagai kumpulan angka piksel, lalu model yang dilatih mengenali pola seperti bentuk dan warna. Penerapannya antara lain pengenalan wajah, deteksi plat nomor, dan pemindai dokumen.
ex: Kamera parkir membaca plat nomor kendaraan. // Aplikasi mengenali jenis bunga dari foto.
pt: Mengenali isi gambar dan video ; Gambar dibaca sebagai angka piksel ; Pengenalan wajah dan plat nomor
sum: Visi komputer membuat mesin dapat memahami gambar.
fig: table Penerapan | Tugas visi komputer ;; buka kunci wajah | pengenalan wajah ;; parkir otomatis | membaca plat nomor ;; pemindai dokumen | mengenali teks ;; mobil otonom | mendeteksi pejalan kaki ;; aplikasi tanaman | mengenali jenis daun ;; kamera pabrik | mendeteksi produk cacat ~ Penerapan visi komputer.
@ Pemrosesan bahasa alami
min: 15
act: Coba fitur terjemahan otomatis untuk satu kalimat, lalu periksa apakah artinya tepat.
mis: mengira mesin terjemahan selalu memahami konteks dengan benar
exp: Pemrosesan bahasa alami atau NLP adalah bidang KA yang membuat komputer memahami dan menghasilkan bahasa manusia. Penerapannya antara lain terjemahan otomatis, chatbot, pemeriksa ejaan, dan ringkasan teks otomatis. NLP masih dapat keliru memahami kata bermakna ganda, bahasa gaul, atau konteks budaya.
ex: Pemeriksa ejaan menandai kata salah tulis. // Chatbot menjawab pertanyaan pelanggan.
pt: Memahami dan menghasilkan bahasa ; Terjemahan, chatbot, pemeriksa ejaan ; Bisa keliru soal konteks
sum: NLP menjembatani bahasa manusia dan komputer.
fig: table Penerapan | Contoh ;; terjemahan otomatis | Indonesia ke Inggris ;; pemeriksa ejaan | menandai salah ketik ;; chatbot | layanan pelanggan ;; ringkasan otomatis | meringkas artikel ;; analisis sentimen | menilai ulasan positif atau negatif ;; pengetikan prediktif | usulan kata berikutnya ~ Penerapan NLP.
@ Sistem rekomendasi
min: 15
act: Perhatikan video atau produk yang disarankan aplikasi kepadamu, lalu tebak alasannya.
mis: mengira rekomendasi aplikasi selalu netral tanpa memengaruhi kita
exp: Sistem rekomendasi adalah KA yang menyarankan konten atau produk berdasarkan data pengguna, seperti riwayat tontonan, pencarian, dan suka. Rekomendasi memudahkan menemukan hal yang disukai, tetapi dapat membuat kita hanya melihat konten serupa atau terjebak dalam gelembung filter. Kita perlu sadar dan sesekali mencari sudut pandang lain.
ex: Toko daring menyarankan barang mirip yang pernah dilihat. // Aplikasi video menyarankan video bertema sama.
pt: Menyarankan berdasarkan data pengguna ; Memudahkan menemukan konten ; Waspada gelembung filter
sum: Gunakan rekomendasi dengan sadar dan kritis.
fig: table Data pengguna | Dipakai untuk ;; riwayat tontonan | menyarankan video serupa ;; pencarian | menyarankan produk terkait ;; tombol suka | mengetahui selera ;; lama menonton | mengukur minat ;; lokasi | menyarankan tempat terdekat ;; teman yang diikuti | menyarankan akun lain ~ Data untuk rekomendasi.
@ Jaringan saraf tiruan
min: 15
act: Bermain peran sebagai neuron: setiap teman meneruskan pesan jika jumlah sinyalnya cukup besar.
mis: mengira jaringan saraf tiruan adalah otak manusia sungguhan
exp: Jaringan saraf tiruan adalah model KA yang terinspirasi cara kerja sel saraf otak. Model ini terdiri atas lapisan masukan, lapisan tersembunyi, dan lapisan keluaran. Setiap sambungan memiliki bobot yang disesuaikan selama pelatihan. Jaringan yang memiliki banyak lapisan tersembunyi disebut deep learning.
ex: Model pengenal angka tulisan tangan memakai jaringan saraf. // Bobot diubah sedikit demi sedikit saat belajar.
pt: Terinspirasi sel saraf ; Lapisan masukan, tersembunyi, keluaran ; Banyak lapisan disebut deep learning
sum: Jaringan saraf tiruan belajar dengan menyesuaikan bobot.
fig: table Bagian | Fungsi ;; lapisan masukan | menerima data ;; lapisan tersembunyi | mengolah pola ;; lapisan keluaran | memberi hasil ;; bobot | kekuatan sambungan ;; pelatihan | menyesuaikan bobot ;; deep learning | banyak lapisan tersembunyi ~ Bagian jaringan saraf tiruan.
@ Deepfake dan cara mengenalinya
min: 15
act: Diskusikan dengan keluarga cara memeriksa video tokoh yang tampak janggal sebelum mempercayainya.
mis: langsung percaya video karena terlihat sangat nyata
exp: Deepfake adalah video, gambar, atau suara palsu buatan KA yang meniru wajah atau suara seseorang. Ciri deepfake antara lain kedipan mata tidak wajar, gerak bibir tidak sesuai suara, tepi wajah buram, dan pencahayaan janggal. Cara menghadapinya adalah memeriksa sumber resmi, tidak menyebarkan, dan melaporkan.
ex: Video tokoh mengucapkan hal aneh perlu dicek di akun resminya. // Suara tiruan dipakai penipu menelepon keluarga.
pt: Media palsu buatan KA ; Kedipan dan gerak bibir janggal ; Cek sumber resmi dan laporkan
sum: Waspadai media yang terlalu mengejutkan untuk dipercaya.
fig: table Ciri deepfake | Yang perlu diperhatikan ;; kedipan mata | jarang atau tidak wajar ;; gerak bibir | tidak sesuai suara ;; tepi wajah | buram atau bergetar ;; pencahayaan | bayangan janggal ;; suara | datar tanpa emosi ;; sumber | tidak ada di akun resmi ~ Ciri deepfake.
@ Privasi data dalam KA
min: 15
act: Periksa izin aplikasi di HP keluarga dan matikan izin yang tidak diperlukan.
mis: memberi semua izin aplikasi tanpa membaca
exp: Banyak layanan KA mengumpulkan data pribadi untuk melatih model atau memberi layanan. Data pribadi meliputi nama, wajah, suara, lokasi, dan riwayat penggunaan. Lindungi privasi dengan membaca izin aplikasi, tidak mengunggah data sensitif ke layanan KA, dan memakai pengaturan privasi.
ex: Aplikasi senter tidak perlu izin kontak. // Jangan unggah foto kartu identitas ke chatbot.
pt: Layanan KA mengumpulkan data ; Wajah, suara, lokasi termasuk data pribadi ; Periksa izin aplikasi
sum: Data pribadi perlu dijaga saat memakai KA.
fig: table Izin aplikasi | Perlu atau tidak untuk aplikasi kalkulator ;; kamera | tidak perlu ;; kontak | tidak perlu sama sekali ;; lokasi | tidak perlu untuk menghitung ;; mikrofon | tidak perlu bersuara ;; penyimpanan | tidak perlu menyimpan ;; tanpa izin khusus | cukup ~ Contoh pemeriksaan izin aplikasi.
@ KA untuk lingkungan
min: 15
act: Cari satu contoh pemanfaatan KA untuk menjaga lingkungan di Indonesia atau dunia.
mis: mengira KA tidak memakai energi sama sekali
exp: KA dapat membantu menjaga lingkungan, misalnya memprediksi cuaca ekstrem, memantau kebakaran hutan dari citra satelit, memilah sampah otomatis, dan menghemat listrik gedung. Namun, pusat data yang menjalankan KA memakai banyak listrik dan air pendingin, sehingga KA juga perlu dipakai secara bijak.
ex: Satelit dan KA mendeteksi titik panas kebakaran hutan. // Robot pemilah sampah mengenali botol plastik.
pt: Prediksi cuaca dan pemantauan hutan ; Pemilahan sampah dan hemat energi ; Pusat data memakai banyak listrik
sum: KA dapat membantu bumi bila dipakai bijak.
fig: table Penerapan | Manfaat lingkungan ;; citra satelit | mendeteksi kebakaran hutan ;; prakiraan cuaca | peringatan banjir ;; robot pemilah | daur ulang sampah ;; gedung pintar | hemat listrik ;; pertanian presisi | hemat air dan pupuk ;; pemantau satwa | melindungi hewan langka ~ KA untuk lingkungan.
@ Kebiasaan sehat memakai gawai
min: 15
act: Catat waktu layar harianmu selama seminggu dan buat target pengurangannya.
mis: memakai gawai sambil berbaring dalam gelap berjam-jam
exp: Pemakaian gawai berlebihan dapat menyebabkan mata lelah, kurang tidur, kurang gerak, dan sulit berkonsentrasi. Kebiasaan sehat antara lain aturan 20-20-20, yaitu setiap 20 menit melihat benda sejauh 20 kaki atau 6 meter selama 20 detik, menjaga jarak layar, mengatur waktu layar, dan menjauhkan gawai sebelum tidur.
ex: Istirahatkan mata setiap 20 menit. // Gawai disimpan di luar kamar saat tidur.
pt: Berlebihan merusak kesehatan ; Aturan 20-20-20 ; Atur waktu layar
sum: Gawai dipakai secukupnya agar tubuh tetap sehat.
fig: table Kebiasaan | Manfaat ;; aturan 20-20-20 | mata tidak lelah ;; jarak layar cukup | mata terlindungi ;; batas waktu layar | waktu untuk aktivitas lain ;; gawai jauh saat tidur | tidur nyenyak ;; duduk tegak | leher tidak pegal ;; mode gelap malam | silau berkurang ~ Kebiasaan sehat memakai gawai.
"""

BANK += """
## INF|Representasi data teks dan gambar
Titik kecil penyusun gambar digital disebut …|piksel|bit|byte|vektor|Piksel.
Huruf A dalam kode ASCII bernilai …|65|1|97|26|65.
=|Warna digital sering disusun dari merah, hijau, dan …|biru|RGB.
=|Standar kode huruf yang mendukung banyak bahasa dan emoji adalah …|Unicode|Unicode.
B|Komputer menyimpan semua data dalam bentuk biner.|Biner.
S|Komputer menyimpan gambar apa adanya tanpa angka.|Piksel angka.
Video tersusun atas rangkaian …|gambar|huruf|bit tunggal|suara saja|Gambar.
Foto berukuran 100 × 100 piksel berisi … piksel.|10.000|200|1.000|100|100 × 100.
## INF|Satuan penyimpanan data
Satuan terkecil data adalah …|bit|byte|kilobyte|megabyte|Bit.
1 byte sama dengan … bit.|8|10|16|1.024|8.
=|1 KB sama dengan … byte.|1.024;1024|1.024.
=|1 GB sama dengan … MB.|1.024;1024|1.024.
B|Terabyte lebih besar daripada gigabyte.|TB > GB.
S|1 KB sama dengan 100 byte.|1.024.
Satuan yang lebih besar dari gigabyte adalah …|terabyte|megabyte|kilobyte|byte|TB.
Urutan satuan dari kecil ke besar adalah …|KB, MB, GB, TB|GB, MB, KB, TB|MB, KB, TB, GB|TB, GB, MB, KB|Urutan.
## INF|Logika boolean
Logika boolean hanya memiliki nilai benar dan …|salah|mungkin|kosong|tiga|Dua nilai.
Hasil 1 AND 0 adalah …|0|1|2|10|AND.
=|Hasil 1 OR 0 adalah …|1|OR.
=|Hasil NOT 1 adalah …|0|NOT.
B|AND bernilai benar jika kedua masukan benar.|AND.
S|OR bernilai benar hanya jika kedua masukan benar.|Salah satu.
Hasil 0 OR 0 adalah …|0|1|2|benar|OR.
Hasil 1 AND 1 adalah …|1|0|2|11|AND.
## INF|Komponen CPU dan memori
Otak komputer yang memproses perintah adalah …|CPU|RAM|SSD|monitor|CPU.
Memori sementara yang hilang saat komputer dimatikan adalah …|RAM|SSD|HDD|flashdisk|RAM.
=|Bagian CPU untuk perhitungan dan logika disebut …|ALU|ALU.
=|Komponen untuk memproses grafis disebut …|GPU|GPU.
B|SSD menyimpan data secara permanen.|Permanen.
S|RAM sama dengan penyimpanan internal permanen.|Sementara.
Bagian CPU yang mengatur jalannya perintah adalah unit …|kendali|aritmetika|memori|grafis|Kendali.
RAM besar membuat banyak aplikasi …|lancar dibuka bersamaan|langsung terhapus|tidak bisa dibuka|lebih lambat|RAM.
## INF|Perangkat masukan dan keluaran
Contoh perangkat masukan adalah …|keyboard|monitor|printer|speaker|Input.
Contoh perangkat keluaran adalah …|printer|mouse|mikrofon|pemindai|Output.
=|Perangkat yang berfungsi sebagai masukan dan keluaran adalah layar …|sentuh|Layar sentuh.
=|Perangkat keluaran suara adalah …|speaker;pengeras suara|Speaker.
B|Mikrofon termasuk perangkat masukan.|Input.
S|Monitor termasuk perangkat masukan.|Output.
Pemindai atau scanner termasuk perangkat …|masukan|keluaran|penyimpanan|pemrosesan|Input.
Kamera web termasuk perangkat …|masukan|keluaran|pemrosesan|penyimpanan|Input.
## INF|Jaringan lokal
Jaringan dalam satu gedung disebut …|LAN|WAN|MAN|PAN|LAN.
Perangkat yang menghubungkan jaringan lokal ke internet adalah …|router|monitor|printer|mouse|Router.
=|Jaringan lokal tanpa kabel disebut …|WLAN;Wi-Fi|WLAN.
=|Jaringan antarnegara disebut …|WAN|WAN.
B|Laboratorium komputer sekolah dapat memakai LAN.|LAN.
S|Wi-Fi selalu sama dengan internet.|Berbeda.
Jaringan seluas satu kota disebut …|MAN|LAN|PAN|WLAN|MAN.
Jaringan di sekitar satu orang seperti Bluetooth disebut …|PAN|LAN|MAN|WAN|PAN.
## INF|Topologi jaringan
Topologi yang memakai satu kabel utama adalah topologi …|bus|star|ring|mesh|Bus.
Topologi yang terpusat pada switch adalah topologi …|star|bus|ring|mesh|Star.
=|Topologi yang membentuk lingkaran adalah topologi …|ring|Ring.
=|Topologi yang paling tahan gangguan adalah topologi …|mesh|Mesh.
B|Laboratorium sekolah umumnya memakai topologi star.|Star.
S|Pada topologi bus, kabel utama putus tidak berpengaruh.|Mati.
Topologi gabungan bertingkat disebut topologi …|tree|bus|ring|star|Tree.
Topologi campuran beberapa jenis disebut topologi …|hybrid|mesh|bus|ring|Hybrid.
## INF|Graf dan jalur terpendek
Graf terdiri atas simpul dan …|sisi|piksel|byte|tabel|Sisi.
Nilai jarak atau waktu pada sisi graf disebut …|bobot|simpul|label warna|indeks|Bobot.
=|Titik pada graf disebut simpul atau …|node|Node.
=|Garis penghubung simpul disebut sisi atau …|edge|Edge.
B|Aplikasi peta memakai graf untuk mencari rute.|Rute.
S|Jalur terpendek selalu jalur dengan simpul paling sedikit.|Bobot.
Pada graf rute bus, halte berperan sebagai …|simpul|sisi|bobot|label|Simpul.
Jalur terpendek adalah jalur dengan jumlah bobot …|paling kecil|paling besar|sama dengan nol|acak|Terkecil.
## INF|Verifikasi sumber informasi
Situs resmi pemerintah Indonesia berakhiran …|go.id|co.id|sch.id|ac.id|go.id.
Ciri sumber terpercaya adalah …|penulis jelas|tanpa tanggal|judul provokatif|meminta disebar|Penulis jelas.
=|Kemampuan mencari, menilai, dan memakai informasi disebut literasi …|informasi|Informasi.
=|Sebelum percaya, bandingkan informasi dari beberapa …|sumber|Sumber.
B|Berita tanpa tanggal perlu diragukan.|Ragukan.
S|Informasi yang banyak dibagikan pasti benar.|Belum tentu.
Judul yang memancing emosi berlebihan disebut judul …|provokatif|informatif|ilmiah|netral|Provokatif.
Situs perguruan tinggi di Indonesia berakhiran …|ac.id|go.id|or.id|co.id|ac.id.
## INF|Hoaks dan cek fakta
Informasi bohong yang sengaja dibuat seolah benar disebut …|hoaks|fakta|opini|data|Hoaks.
Cara memeriksa apakah foto itu foto lama adalah …|pencarian gambar terbalik|memperbesar foto|mengganti filter|mengirim ke teman|Reverse image.
=|Langkah pertama cek fakta adalah membaca berita secara …|utuh|Utuh.
=|Sebelum yakin benar, kita sebaiknya menahan diri untuk tidak …|membagikan;menyebarkan|Tahan.
B|Pesan berantai yang meminta disebar sering merupakan hoaks.|Ciri hoaks.
S|Kabar sebaiknya disebarkan dulu baru diperiksa.|Periksa dulu.
Ciri hoaks adalah …|sumber tidak jelas|ada rujukan resmi|penulis jelas|tanggal jelas|Hoaks.
Situs yang memuat hasil verifikasi kabar disebut situs …|cek fakta|belanja|permainan|musik|Cek fakta.
## INF|Basis data sederhana
Satu baris data dalam tabel disebut …|record|field|kueri|kunci|Record.
Satu kolom data dalam tabel disebut …|field|record|tabel|kueri|Field.
=|Penanda unik setiap record disebut kunci …|utama|Kunci utama.
=|Perintah untuk mencari data dalam basis data disebut …|kueri;query|Kueri.
B|Nomor induk siswa dapat menjadi kunci utama.|Unik.
S|Satu kolom basis data sebaiknya berisi jenis data campur aduk.|Seragam.
Kumpulan record membentuk …|tabel|field|kunci|kueri|Tabel.
Kumpulan data yang tersusun rapi disebut …|basis data|grafik|presentasi|surel|Basis data.
## INF|Mengurutkan dan menyaring data
Mengurutkan data dari kecil ke besar disebut …|ascending|descending|filter|merge|Ascending.
Fitur untuk menampilkan data yang memenuhi syarat saja adalah …|filter|sort|merge|print|Filter.
=|Mengurutkan dari besar ke kecil disebut …|descending|Descending.
=|Mengurutkan data dalam bahasa Inggris disebut …|sort|Sort.
B|Saat mengurutkan, seluruh baris harus ikut terurut.|Utuh.
S|Mengurutkan satu kolom saja tidak membuat data tertukar.|Tertukar.
Mengurutkan nama dari A ke Z termasuk urutan …|ascending|descending|acak|filter|Naik.
Setelah filter dihapus, data yang tampil adalah …|semua data|data kosong|satu baris|judul saja|Semua.
## INF|Membuat halaman web dengan HTML
Bahasa untuk menyusun halaman web adalah …|HTML|Python|SQL|Excel|HTML.
Tag HTML untuk paragraf adalah …|p|h1|img|a|p.
=|Tag HTML untuk judul utama adalah …|h1|h1.
=|Tag HTML untuk tautan adalah …|a|a.
B|Tag HTML biasanya berpasangan.|Pembuka dan penutup.
S|Halaman HTML hanya dapat dibuka dengan aplikasi kalkulator.|Peramban.
Tag HTML untuk menampilkan gambar adalah …|img|p|ul|h1|img.
Tag HTML untuk daftar berbutir adalah …|ul|table|img|h1|ul.
## INF|Desain antarmuka pengguna
Tampilan untuk berinteraksi dengan aplikasi disebut …|antarmuka pengguna|basis data|server|kode sumber|UI.
Prinsip menu di posisi yang sama di setiap halaman adalah …|konsisten|kontras|rumit|acak|Konsisten.
=|Singkatan antarmuka pengguna dalam bahasa Inggris adalah …|UI|UI.
=|Penilaian kenyamanan memakai aplikasi disebut pengalaman …|pengguna|UX.
B|Pesan "tersimpan" adalah contoh umpan balik.|Umpan balik.
S|Huruf sangat kecil membuat aplikasi mudah dibaca.|Besar cukup.
Aplikasi yang bisa dipakai tunanetra memenuhi prinsip …|aksesibel|rumit|acak|gelap|Aksesibel.
Teks gelap di latar terang menerapkan prinsip …|kontras|konsisten|sederhana|aksesibel|Kontras.
## INF|Jejak digital dan reputasi daring
Rekam aktivitas seseorang di internet disebut jejak …|digital|kaki|kertas|suara|Digital.
Mengunggah foto termasuk jejak digital …|aktif|pasif|hilang|rahasia|Aktif.
=|Jejak yang terkumpul tanpa disadari disebut jejak …|pasif|Pasif.
=|Data kecil yang disimpan situs di peramban disebut …|cookies|Cookies.
B|Jejak digital dapat memengaruhi reputasi.|Reputasi.
S|Unggahan yang dihapus pasti hilang selamanya.|Bisa tersalin.
Riwayat pencarian termasuk jejak digital …|pasif|aktif|positif|offline|Pasif.
Cara membangun jejak digital positif adalah …|mengunggah karya bermanfaat|berkomentar kasar|menyebar hoaks|mengunggah data pribadi|Positif.
## INF|Kompresi data
Kompresi data bertujuan … ukuran berkas.|memperkecil|memperbesar|menghapus|menggandakan|Kecil.
Format kompresi yang dapat dikembalikan utuh adalah …|ZIP|JPG|MP3|MP4|Lossless.
=|Kompresi yang membuang sebagian data disebut kompresi …|lossy|Lossy.
=|Kompresi tanpa kehilangan data disebut kompresi …|lossless|Lossless.
B|MP3 termasuk kompresi lossy.|Lossy.
S|Foto JPG dapat dikembalikan ke kualitas asli sepenuhnya.|Lossy.
Format gambar dengan kompresi lossless adalah …|PNG|JPG|MP3|MP4|PNG.
Manfaat kompresi adalah berkas lebih cepat …|dikirim|rusak|hilang|terhapus|Cepat.
## KKA|Operator logika dalam program
Operator logika yang benar jika semua syarat benar adalah …|and|or|not|if|and.
Operator logika yang benar jika salah satu syarat benar adalah …|or|and|not|else|or.
=|Operator logika yang membalik nilai adalah …|not|not.
=|Hasil True and False adalah …|False|False.
B|False or True bernilai True.|or.
S|True and False bernilai True.|False.
Hasil not False adalah …|True|False|None|0|Dibalik.
Syarat boleh masuk jika umur > 5 dan tinggi > 100 memakai operator …|and|or|not|elif|Keduanya.
## KKA|Pengolahan string
Metode untuk mengubah teks menjadi huruf besar adalah …|upper|lower|replace|len|upper.
Hasil len("kelas") adalah …|5|4|6|1|5 huruf.
=|Hasil "ab" + "cd" adalah …|abcd|abcd.
=|Metode untuk mengubah teks menjadi huruf kecil adalah …|lower|lower.
B|"kucing"[0] menghasilkan huruf k.|Indeks 0.
S|Indeks huruf pertama string adalah 1.|Nol.
Metode untuk mengganti kata dalam string adalah …|replace|upper|split|len|replace.
Hasil "bobo".upper() adalah …|BOBO|bobo|Bobo|bOBO|Upper.
## KKA|Dictionary dalam Python
Dictionary ditulis di dalam kurung …|kurawal|siku|biasa|sudut|Kurawal.
Dictionary menyimpan pasangan kunci dan …|nilai|indeks|baris|kolom|Nilai.
=|Jika nilai = {"Sari": 90}, maka nilai["Sari"] menghasilkan …|90|90.
=|Perintah untuk menghitung banyak pasangan dictionary adalah …|len|len.
B|Nilai dictionary diambil dengan menyebut kuncinya.|Kunci.
S|Dictionary diakses dengan indeks angka seperti list.|Kunci.
Perintah untuk menampilkan semua kunci dictionary adalah …|keys|values|items|len|keys.
Perintah untuk menghapus pasangan dari dictionary adalah …|del|add|sort|print|del.
## KKA|Perulangan bersarang
Perulangan di dalam perulangan lain disebut perulangan …|bersarang|tunggal|terbalik|acak|Bersarang.
Jika luar 2 kali dan dalam 3 kali, perintah dalam dijalankan … kali.|6|5|3|2|2 × 3.
=|Jika luar 4 kali dan dalam 3 kali, total putaran dalam adalah …|12|4 × 3.
=|Perulangan dalam dijalankan sampai selesai untuk setiap putaran perulangan …|luar|Luar.
B|Perulangan bersarang cocok untuk membuat tabel perkalian.|Tabel.
S|Indentasi tidak penting pada perulangan bersarang.|Penting.
Pola segitiga bintang biasanya dibuat dengan …|perulangan bersarang|satu print saja|dictionary|modul math|Bersarang.
Jika luar 5 kali dan dalam 3 kali, total putaran dalam adalah …|15|8|5|3|5 × 3.
## KKA|Modul random dan math
Perintah untuk memanggil modul di Python adalah …|import|include|using|open|import.
Fungsi untuk angka acak 1 sampai 6 adalah random.…|randint(1, 6)|sqrt(6)|pi(6)|floor(6)|randint.
=|Hasil math.sqrt(16) adalah …|4.0;4|Akar.
=|Fungsi untuk memilih anggota acak dari list adalah random.…|choice|choice.
B|Modul adalah kumpulan fungsi siap pakai.|Modul.
S|Fungsi modul dapat dipakai tanpa import.|Perlu import.
Fungsi pembulatan ke bawah adalah math.…|floor|ceil|sqrt|pi|floor.
Fungsi pembulatan ke atas adalah math.…|ceil|floor|sqrt|round_down|ceil.
## KKA|Membaca dan menulis berkas
Mode membuka berkas untuk membaca adalah …|r|w|a|x|r.
Mode untuk menambah isi di akhir berkas adalah …|a|w|r|x|a.
=|Mode untuk menulis ulang berkas adalah …|w|w.
=|Perintah yang membuat berkas tertutup otomatis adalah …|with|with.
B|Mode w menghapus isi lama berkas.|Tulis ulang.
S|Data dalam variabel tetap tersimpan setelah program ditutup.|Hilang.
Fungsi untuk membuka berkas di Python adalah …|open|read|file_go|start|open.
Mode untuk membuat berkas baru adalah …|x|a|r|w+|x.
## KKA|Proyek tebak angka
Untuk membuat angka rahasia dipakai modul …|random|math|time|os|random.
Tebakan dari input harus diubah dengan …|int|str|list|print|int.
=|Perulangan sampai tebakan benar memakai …|while|while.
=|Petunjuk terlalu besar atau kecil memakai …|if|if.
B|Proyek dibuat bertahap: rancang, tulis, uji, perbaiki.|Tahap.
S|Input dapat langsung dibandingkan dengan angka tanpa diubah.|int.
Untuk menghitung banyak percobaan dipakai variabel …|penghitung|rahasia|konstanta|modul|Counter.
Jika tebak < rahasia, petunjuk yang tepat adalah …|terlalu kecil|terlalu besar|benar|selesai|Kecil.
## KKA|Pemrograman berbasis blok
Contoh aplikasi pemrograman berbasis blok adalah …|Scratch|Word|Excel|Paint|Scratch.
Program Scratch sering dimulai dengan blok …|ketika bendera hijau diklik|maju 10 langkah|katakan halo|mainkan suara|Pemicu.
=|Blok ulangi 10 kali termasuk kategori …|kendali|Kendali.
=|Blok maju 10 langkah termasuk kategori …|gerak|Gerak.
B|Pemrograman blok mengajarkan urutan, perulangan, dan percabangan.|Konsep.
S|Program blok tetap berjalan tanpa blok pemicu.|Perlu pemicu.
Blok menyentuh tepi termasuk kategori …|sensor|suara|gerak|tampilan|Sensor.
Blok katakan halo termasuk kategori …|tampilan|gerak|kendali|operator|Tampilan.
## KKA|Visi komputer
Bidang KA yang membuat komputer mengenali isi gambar disebut …|visi komputer|NLP|basis data|jaringan lokal|Computer vision.
Komputer membaca gambar sebagai kumpulan angka …|piksel|huruf|suara|kata|Piksel.
=|Kamera parkir membaca … nomor kendaraan.|plat|Plat nomor.
=|Membuka kunci HP dengan wajah memakai pengenalan …|wajah|Wajah.
B|Mobil otonom memakai visi komputer.|Mendeteksi.
S|Komputer melihat gambar persis seperti mata manusia.|Angka.
Kamera pabrik dengan KA dapat mendeteksi produk …|cacat|mahal|baru|terjual|Cacat.
Pemindai dokumen dengan KA dapat mengenali …|teks|rasa|bau|suhu|Teks.
## KKA|Pemrosesan bahasa alami
Singkatan pemrosesan bahasa alami dalam bahasa Inggris adalah …|NLP|CPU|LAN|HTML|NLP.
Contoh penerapan NLP adalah …|terjemahan otomatis|pengenalan wajah|robot pemilah|sensor suhu|NLP.
=|Program yang menjawab pertanyaan secara otomatis disebut …|chatbot|Chatbot.
=|Menilai ulasan positif atau negatif disebut analisis …|sentimen|Sentimen.
B|NLP dapat keliru memahami bahasa gaul.|Konteks.
S|Mesin terjemahan selalu benar memahami konteks.|Bisa keliru.
Usulan kata berikutnya saat mengetik disebut pengetikan …|prediktif|manual|terbalik|acak|Prediktif.
Pemeriksa ejaan menandai kata yang …|salah tulis|benar|panjang|pendek|Salah tulis.
## KKA|Sistem rekomendasi
Sistem rekomendasi menyarankan konten berdasarkan … pengguna.|data|warna|tinggi badan|golongan darah|Data.
Terjebak hanya melihat konten serupa disebut …|gelembung filter|jejak pasif|deepfake|bias cahaya|Gelembung filter.
=|Tombol suka membantu aplikasi mengetahui … pengguna.|selera|Selera.
=|Data lokasi dipakai untuk menyarankan tempat …|terdekat|Terdekat.
B|Riwayat tontonan dipakai untuk menyarankan video serupa.|Riwayat.
S|Rekomendasi aplikasi tidak pernah memengaruhi pilihan kita.|Memengaruhi.
Cara menghindari gelembung filter adalah …|mencari sudut pandang lain|menonton satu jenis saja|menutup mata|menyukai semua konten|Beragam.
Lama menonton dipakai untuk mengukur …|minat|umur|alamat|nama|Minat.
## KKA|Jaringan saraf tiruan
Jaringan saraf tiruan terinspirasi dari sel …|saraf|darah|kulit|tulang|Saraf.
Lapisan yang menerima data disebut lapisan …|masukan|keluaran|tersembunyi|akhir|Masukan.
=|Lapisan yang memberi hasil disebut lapisan …|keluaran|Keluaran.
=|Jaringan dengan banyak lapisan tersembunyi disebut … learning.|deep|Deep learning.
B|Bobot disesuaikan selama pelatihan.|Bobot.
S|Jaringan saraf tiruan adalah otak manusia sungguhan.|Model.
Lapisan yang mengolah pola di tengah disebut lapisan …|tersembunyi|masukan|keluaran|luar|Tersembunyi.
Kekuatan sambungan antarneuron tiruan disebut …|bobot|piksel|byte|simpul|Bobot.
## KKA|Deepfake dan cara mengenalinya
Media palsu buatan KA yang meniru wajah atau suara disebut …|deepfake|chatbot|meme|stiker|Deepfake.
Ciri deepfake adalah gerak bibir yang …|tidak sesuai suara|sangat sesuai|tidak bergerak sama sekali|sempurna|Janggal.
=|Untuk memastikan video tokoh, cek akun …|resmi|Resmi.
=|Kedipan mata pada deepfake sering tidak …|wajar|Wajar.
B|Suara tiruan KA dapat dipakai penipu.|Penipuan.
S|Video yang tampak nyata pasti asli.|Bisa deepfake.
Sikap yang tepat terhadap deepfake adalah …|tidak menyebarkan dan melaporkan|langsung membagikan|mengeditnya lagi|memercayainya|Lapor.
Tepi wajah pada deepfake sering tampak …|buram|tajam sempurna|berwarna emas|bercahaya|Buram.
## KKA|Privasi data dalam KA
Contoh data pribadi adalah …|wajah dan suara|warna langit|nama planet|resep umum|Pribadi.
Aplikasi senter tidak memerlukan izin …|kontak|lampu kilat|layar|baterai|Kontak.
=|Sebelum memasang aplikasi, baca … aplikasi.|izin|Izin.
=|Foto kartu identitas termasuk data …|sensitif;pribadi|Sensitif.
B|Layanan KA dapat mengumpulkan data pengguna.|Data.
S|Memberi semua izin aplikasi tanpa membaca itu aman.|Periksa.
Cara melindungi privasi saat memakai KA adalah …|tidak mengunggah data sensitif|mengunggah semua dokumen|membagikan kata sandi|memberi semua izin|Privasi.
Aplikasi kalkulator sebaiknya tidak meminta izin …|lokasi|layar|tombol|angka|Lokasi.
## KKA|KA untuk lingkungan
KA dan citra satelit dapat mendeteksi …|kebakaran hutan|rasa makanan|nada lagu|nama orang|Satelit.
Pusat data yang menjalankan KA memakai banyak …|listrik|pasir|kertas|kayu bakar|Energi.
=|Robot pemilah membantu … ulang sampah.|daur|Daur ulang.
=|Gedung pintar dengan KA membantu hemat …|listrik;energi|Listrik.
B|Pertanian presisi membantu menghemat air dan pupuk.|Presisi.
S|KA tidak memakai energi sama sekali.|Pakai listrik.
Prakiraan cuaca dengan KA membantu memberi peringatan …|banjir|ujian|ulang tahun|diskon|Banjir.
Pemantau satwa dengan KA membantu melindungi hewan …|langka|peliharaan|ternak saja|mainan|Langka.
## KKA|Kebiasaan sehat memakai gawai
Aturan 20-20-20 bertujuan menjaga kesehatan …|mata|gigi|kuku|rambut|Mata.
Menurut aturan 20-20-20, setiap 20 menit melihat benda sejauh sekitar …|6 meter|20 cm|1 meter|100 meter|20 kaki.
=|Gawai sebaiknya dijauhkan sebelum …|tidur|Tidur.
=|Lama memakai gawai setiap hari disebut waktu …|layar|Waktu layar.
B|Duduk tegak membantu leher tidak pegal.|Postur.
S|Memakai gawai berjam-jam dalam gelap baik untuk mata.|Merusak.
Dampak pemakaian gawai berlebihan adalah …|mata lelah|mata lebih tajam|tidur lebih nyenyak|lebih banyak bergerak|Lelah.
Menurut aturan 20-20-20, mata diistirahatkan selama …|20 detik|20 menit|2 jam|20 jam|20 detik.
"""

SAS += """
## INF 1
0|Emoji disimpan komputer sebagai ....|kode Unicode|gambar piksel saja|suara|video|Unicode.
1|1 TB sama dengan ....|1.024 GB|1.000 MB|100 GB|1.024 KB|TB.
2|Hasil NOT 0 adalah ....|1|0|2|salah|NOT.
3|Komponen yang menyimpan data secara permanen dan cepat adalah ....|SSD|RAM|ALU|unit kendali|SSD.
4|Speaker termasuk perangkat ....|keluaran|masukan|pemrosesan|penyimpanan|Output.
5|Jaringan tanpa kabel dalam rumah termasuk ....|WLAN|WAN|MAN|PAN|WLAN.
6|Topologi yang paling banyak jalur penghubungnya adalah ....|mesh|bus|star|ring|Mesh.
7|Pada graf jaringan pertemanan, orang berperan sebagai ....|simpul|sisi|bobot|lapisan|Simpul.
## INF 2
0|Ciri informasi meragukan adalah ....|meminta segera disebarkan|penulis jelas|ada rujukan|tanggal jelas|Mendesak.
1|Foto banjir lama yang disebarkan sebagai kejadian baru termasuk ....|hoaks|fakta|opini|data valid|Hoaks.
2|Satu kolom data dalam tabel basis data disebut ....|field|record|kueri|kunci|Field.
3|Mengurutkan nilai dari terbesar ke terkecil disebut ....|descending|ascending|filter|merge|Descending.
4|Tag HTML untuk membuat tabel adalah ....|table|ul|p|img|table.
5|Menu yang selalu berada di posisi sama menerapkan prinsip ....|konsisten|kontras|aksesibel|sederhana|Konsisten.
6|Data lokasi yang tercatat otomatis termasuk jejak digital ....|pasif|aktif|positif|offline|Pasif.
7|Format audio dengan kompresi lossless adalah ....|FLAC|MP3|MP4|JPG|FLAC.
## KKA 1
0|Hasil False or False adalah ....|False|True|None|1|or.
1|Hasil "BOBO".lower() adalah ....|bobo|BOBO|Bobo|bOBO|lower.
2|Perintah untuk menampilkan semua nilai dictionary adalah ....|values|keys|items|len|values.
3|Jika luar 10 kali dan dalam 3 kali, total putaran dalam adalah ....|30|13|10|3|10 × 3.
4|Nilai math.pi kira-kira sama dengan ....|3,14|2,71|1,41|9,8|Pi.
5|Mode r+ dipakai untuk ....|membaca dan menulis|menghapus berkas|membuat folder|menutup program|r+.
6|Fungsi random.randint(1, 20) menghasilkan ....|angka acak 1 sampai 20|angka 20 saja|angka 1 saja|huruf acak|Randint.
7|Blok ketika bendera hijau diklik termasuk kategori ....|peristiwa|gerak|suara|operator|Peristiwa.
## KKA 2
0|Mendeteksi pejalan kaki pada mobil otonom memakai ....|visi komputer|NLP|basis data|topologi|Vision.
1|Meringkas artikel secara otomatis termasuk penerapan ....|NLP|visi komputer|robotika|jaringan lokal|NLP.
2|Teman yang diikuti dipakai sistem rekomendasi untuk menyarankan ....|akun lain|cuaca|harga emas|jadwal sekolah|Akun.
3|Proses menyesuaikan bobot jaringan saraf disebut ....|pelatihan|pengujian akhir|pencetakan|penghapusan|Pelatihan.
4|Suara deepfake sering terdengar ....|datar tanpa emosi|sangat alami selalu|bernyanyi|tanpa kata|Datar.
5|Aplikasi kalkulator yang baik cukup bekerja ....|tanpa izin khusus|dengan izin kamera|dengan izin kontak|dengan izin lokasi|Izin.
6|KA di gedung pintar membantu ....|hemat listrik|boros listrik|menambah sampah|menebang pohon|Hemat.
7|Mode gelap pada malam hari membantu mengurangi ....|silau|baterai penuh|sinyal|suara|Silau.
"""

TOPICS += """
## PAI
# 1|Al-Qur'an, Akidah, dan Fikih
@ Surah Az-Zalzalah
min: 15
act: Baca Surah Az-Zalzalah bersama keluarga, lalu diskusikan pesan ayat 7 dan 8.
mis: mengira kebaikan kecil tidak dihitung oleh Allah
exp: Surah Az-Zalzalah adalah surah ke-99 dan terdiri atas 8 ayat. Az-Zalzalah artinya kegoncangan. Surah ini menggambarkan bumi diguncang dahsyat pada hari kiamat dan bumi menceritakan perbuatan manusia. Ayat 7 dan 8 menegaskan bahwa kebaikan dan keburukan sebesar zarah pun akan dilihat balasannya.
ex: Senyum kepada teman termasuk kebaikan yang dihitung. // Keburukan kecil pun ada balasannya.
pt: Surah ke-99, terdiri atas 8 ayat ; Az-Zalzalah artinya kegoncangan ; Kebaikan sebesar zarah dibalas
sum: Az-Zalzalah mengajak kita tidak meremehkan amal sekecil apa pun.
fig: table Hal | Isi ;; nomor surah | 99 ;; jumlah ayat | 8 ;; arti nama surah | kegoncangan ;; ayat 1 | bumi diguncang dahsyat ;; ayat 4 | bumi menceritakan beritanya ;; ayat 7 | kebaikan sebesar zarah dilihat ~ Isi Surah Az-Zalzalah.
read: quran 99:1-8
@ Iman kepada rasul
min: 15
act: Tulis nama lima rasul ulul azmi dan satu keteladanan dari masing-masing.
mis: menyamakan nabi dan rasul tanpa perbedaan
exp: Iman kepada rasul adalah rukun iman keempat. Rasul adalah manusia pilihan yang menerima wahyu dan wajib menyampaikannya kepada umat. Nabi menerima wahyu untuk dirinya sendiri. Jumlah rasul yang wajib diketahui ada 25. Rasul ulul azmi adalah Nabi Nuh, Ibrahim, Musa, Isa, dan Muhammad saw. karena ketabahannya luar biasa.
ex: Nabi Muhammad saw. adalah rasul terakhir. // Nabi Nuh berdakwah ratusan tahun dengan sabar.
pt: Rukun iman keempat ; Rasul wajib menyampaikan wahyu ; Lima rasul ulul azmi
sum: Meneladani rasul adalah wujud iman kepada rasul.
fig: table Rasul ulul azmi | Keteladanan ;; Nabi Nuh | sabar berdakwah ;; Nabi Ibrahim | teguh bertauhid ;; Nabi Musa | berani melawan Firaun ;; Nabi Isa | lemah lembut ;; Nabi Muhammad | akhlak mulia ;; jumlah rasul wajib diketahui | 25 ~ Rasul ulul azmi.
@ Sifat wajib rasul
min: 15
act: Catat satu perilaku harianmu yang meneladani setiap sifat wajib rasul.
mis: menukar arti sifat tablig dan fatanah
exp: Rasul memiliki empat sifat wajib. Siddiq artinya jujur. Amanah artinya dapat dipercaya. Tablig artinya menyampaikan wahyu. Fatanah artinya cerdas. Lawannya adalah sifat mustahil, yaitu kizib atau dusta, khianat, kitman atau menyembunyikan, dan baladah atau bodoh. Sifat ini patut diteladani dalam kehidupan sehari-hari.
ex: Mengembalikan barang titipan (amanah). // Menyampaikan pesan guru kepada teman (tablig).
pt: Siddiq, amanah, tablig, fatanah ; Sifat mustahil kebalikannya ; Diteladani sehari-hari
sum: Sifat rasul adalah teladan akhlak terbaik.
fig: table Sifat wajib | Sifat mustahil ;; siddiq | kizib ;; amanah | khianat ;; tablig | kitman ;; fatanah | baladah ;; jujur | dusta ;; cerdas | bodoh ~ Sifat wajib dan mustahil rasul.
@ Asmaul Husna Al-'Adl dan Al-Hakim
min: 15
act: Tulis satu contoh sikap adil di rumah dan satu contoh sikap bijaksana di sekolah.
mis: mengira adil berarti membagi selalu sama rata
exp: Al-'Adl artinya Allah Maha Adil, yaitu menempatkan sesuatu sesuai tempatnya dan memberi balasan dengan tepat. Al-Hakim artinya Allah Maha Bijaksana, segala ketetapan-Nya mengandung hikmah. Meneladani kedua nama ini berarti berlaku adil, tidak berat sebelah, dan bertindak bijak setelah berpikir matang.
ex: Kakak membagi tugas sesuai kemampuan adik-adik. // Ketua kelas mendengar dua pihak sebelum memutuskan.
pt: Al-'Adl Maha Adil ; Al-Hakim Maha Bijaksana ; Adil sesuai tempatnya
sum: Adil dan bijaksana membawa kedamaian.
fig: table Asmaul Husna | Arti ;; Al-'Adl | Maha Adil ;; Al-Hakim | Maha Bijaksana ;; Al-Hakam | Maha Menetapkan Hukum ;; Al-Muqsit | Maha Pemberi Keadilan ;; Al-Haq | Maha Benar ;; Al-Hasib | Maha Membuat Perhitungan ~ Asmaul Husna tentang keadilan.
@ Makanan dan minuman halal
min: 15
act: Periksa label halal pada lima kemasan makanan di dapur.
mis: mengira makanan halal cukup dilihat dari bahannya saja
exp: Islam memerintahkan memakan makanan yang halal dan tayib atau baik. Halal berarti diperbolehkan syariat, dari zat, cara memperoleh, dan cara mengolahnya. Makanan haram antara lain bangkai, darah, daging babi, hewan yang disembelih tidak atas nama Allah, serta minuman memabukkan. Di Indonesia, sertifikat halal dikeluarkan oleh BPJPH.
ex: Daging ayam halal jika disembelih sesuai syariat. // Makanan dari uang curian tidak halal.
pt: Halal dan tayib ; Zat, cara memperoleh, cara mengolah ; Sertifikat halal BPJPH
sum: Makanan halal dan baik menyehatkan jasmani dan rohani.
fig: table Makanan | Hukum ;; sayur dan buah | halal ;; daging babi | haram ;; darah | haram dimakan ;; ikan | halal termasuk bangkainya ;; minuman keras | haram memabukkan ;; ayam disembelih syar'i | halal disembelih ~ Hukum makanan.
@ Adab berpakaian
min: 15
act: Diskusikan dengan orang tua pakaian yang sopan untuk ke sekolah, masjid, dan acara keluarga.
mis: mengira berpakaian islami harus mahal dan mewah
exp: Pakaian berfungsi menutup aurat, melindungi tubuh, dan memperindah diri. Islam mengajarkan berpakaian bersih, sopan, menutup aurat, tidak ketat dan tembus pandang, serta tidak berlebihan. Aurat laki-laki antara pusar sampai lutut, sedangkan aurat perempuan seluruh tubuh kecuali wajah dan telapak tangan. Berdoa saat memakai pakaian juga dianjurkan.
ex: Memakai pakaian bersih saat salat. // Mendahulukan bagian kanan saat berpakaian.
pt: Menutup aurat dan melindungi tubuh ; Bersih, sopan, tidak berlebihan ; Aurat laki-laki dan perempuan
sum: Berpakaian sopan adalah cermin akhlak.
fig: table Adab | Contoh ;; menutup aurat | pakaian longgar ;; bersih | dicuci teratur ;; tidak berlebihan | sederhana ;; mendahulukan kanan | memakai lengan kanan dulu ;; berdoa | membaca doa berpakaian ;; tidak menyerupai lawan jenis | sesuai jenis kelamin ~ Adab berpakaian.
# 2|Akhlak, Ibadah, dan Sejarah
@ Surah Al-Humazah
min: 15
act: Baca Surah Al-Humazah, lalu tulis tiga cara menghindari kebiasaan mengumpat.
mis: menganggap mengejek teman sebagai candaan biasa
exp: Surah Al-Humazah adalah surah ke-104 dan terdiri atas 9 ayat. Al-Humazah artinya pengumpat. Surah ini mengancam orang yang suka mengumpat, mencela, dan menumpuk harta karena mengira hartanya kekal. Balasannya dilemparkan ke neraka Hutamah. Pesannya adalah menjaga lisan dan tidak sombong dengan harta.
ex: Tidak mengejek fisik teman. // Harta dipakai untuk kebaikan, bukan untuk pamer.
pt: Surah ke-104, terdiri atas 9 ayat ; Al-Humazah artinya pengumpat ; Ancaman neraka Hutamah
sum: Al-Humazah mengajarkan menjaga lisan dan tidak serakah.
fig: table Hal | Isi ;; nomor surah | 104 ;; jumlah ayat | 9 ;; arti nama surah | pengumpat ;; ayat 1 | celaka pengumpat dan pencela ;; ayat 2 | mengumpulkan dan menghitung harta ;; ayat 4 | dilemparkan ke Hutamah ~ Isi Surah Al-Humazah.
read: quran 104:1-9
@ Menghindari ghibah dan namimah
min: 15
act: Buat kesepakatan dengan teman sekelompok untuk tidak membicarakan keburukan orang lain.
mis: mengira membicarakan keburukan yang benar bukan ghibah
exp: Ghibah adalah membicarakan keburukan orang lain yang jika ia mendengarnya tidak suka, walaupun keburukan itu benar. Namimah adalah mengadu domba dengan memindahkan perkataan untuk merusak hubungan. Keduanya dilarang dalam Surah Al-Hujurat ayat 12. Cara menghindarinya adalah menjaga lisan, menasihati secara langsung, dan berprasangka baik.
ex: Tidak ikut membicarakan kekurangan teman. // Tidak menyampaikan ucapan seseorang untuk memancing pertengkaran.
pt: Ghibah membicarakan keburukan ; Namimah mengadu domba ; Dilarang dalam Al-Hujurat 12
sum: Lisan yang terjaga menjaga persaudaraan.
fig: table Perbuatan tercela | Arti ;; ghibah | membicarakan keburukan orang ;; namimah | mengadu domba ;; buhtan | memfitnah ;; tajassus | mencari-cari kesalahan ;; su'uzan | berprasangka buruk ;; hasad | iri hati ~ Perbuatan tercela lisan dan hati.
@ Husnuzan
min: 15
act: Ingat satu kejadian ketika kamu salah sangka kepada teman, lalu tulis pelajarannya.
mis: langsung menuduh tanpa mencari kejelasan
exp: Husnuzan artinya berprasangka baik. Husnuzan kepada Allah berarti yakin bahwa semua ketetapan Allah mengandung kebaikan. Husnuzan kepada diri sendiri berarti percaya diri dan optimis. Husnuzan kepada sesama berarti tidak mudah menuduh dan mencari penjelasan dulu. Lawan husnuzan adalah su'uzan.
ex: Teman tidak membalas pesan, mungkin sedang sibuk. // Tetap bersyukur saat cita-cita belum tercapai.
pt: Berprasangka baik ; Kepada Allah, diri sendiri, sesama ; Lawannya su'uzan
sum: Husnuzan menenangkan hati dan menjaga hubungan.
fig: table Husnuzan kepada | Wujud ;; Allah | yakin setiap takdir ada hikmahnya ;; diri sendiri | percaya diri dan optimis ;; orang tua | yakin larangannya demi kebaikan ;; guru | menerima teguran dengan baik ;; teman | mencari penjelasan dulu ;; tetangga | tidak mudah curiga ~ Wujud husnuzan.
@ Zakat fitrah
min: 15
act: Tanyakan kepada orang tua berapa zakat fitrah yang dibayar keluarga dan kepada siapa diberikan.
mis: mengira zakat fitrah boleh dibayar setelah salat Idulfitri tanpa batas
exp: Zakat fitrah adalah zakat yang wajib dikeluarkan setiap muslim pada bulan Ramadan sampai sebelum salat Idulfitri. Besarnya sekitar 2,5 kg atau 3,5 liter makanan pokok, atau uang senilai itu sesuai ketetapan. Tujuannya menyucikan diri orang yang berpuasa dan membantu fakir miskin merayakan hari raya. Penerima zakat terdiri atas delapan golongan atau asnaf.
ex: Keluarga membayar beras zakat fitrah lewat amil di masjid. // Fakir miskin menerima zakat sebelum hari raya.
pt: Wajib bagi setiap muslim ; 2,5 kg makanan pokok ; Dibayar sebelum salat Idulfitri
sum: Zakat fitrah menyucikan diri dan berbagi kebahagiaan.
fig: table Golongan penerima | Keterangan ;; fakir | tidak punya penghasilan ;; miskin | penghasilan tidak cukup ;; amil | pengurus zakat ;; mualaf | baru masuk Islam ;; garim | berutang untuk kebaikan ;; ibnu sabil | musafir kehabisan bekal ~ Golongan penerima zakat.
@ Adab bertetangga
min: 15
act: Lakukan satu kebaikan untuk tetangga minggu ini, misalnya mengantar makanan atau menyapa.
mis: membunyikan musik keras sampai larut malam
exp: Rasulullah saw. bersabda bahwa orang yang beriman kepada Allah dan hari akhir hendaknya memuliakan tetangganya. Adab bertetangga antara lain menyapa, saling memberi, menjenguk yang sakit, membantu yang kesulitan, dan tidak mengganggu dengan suara atau sampah. Tetangga yang baik membuat lingkungan aman dan rukun.
ex: Mengantar masakan kepada tetangga. // Tidak membuang sampah di depan rumah tetangga.
pt: Memuliakan tetangga tanda iman ; Menyapa, memberi, menjenguk ; Tidak mengganggu
sum: Rukun bertetangga mencerminkan iman.
fig: table Situasi | Adab yang tepat ;; bertemu di jalan | menyapa dengan ramah ;; memasak banyak | berbagi makanan ;; tetangga sakit | menjenguk ;; tetangga pindahan | membantu mengangkat barang ;; malam hari | tidak membuat bising ;; ada kerja bakti | ikut membantu ~ Adab bertetangga.
@ Ilmuwan muslim dan karyanya
min: 15
act: Pilih satu ilmuwan muslim, lalu buat poster tentang penemuan dan pengaruhnya saat ini.
mis: mengira ilmu pengetahuan modern sama sekali tidak dipengaruhi ilmuwan muslim
exp: Pada masa keemasan Islam, banyak ilmuwan muslim berkarya di berbagai bidang. Ibnu Sina menulis Al-Qanun fit Tibb di bidang kedokteran. Al-Khawarizmi mengembangkan aljabar dan menjadi asal kata algoritma. Ibnu Haitham meneliti cahaya dan optika. Al-Biruni ahli astronomi dan geografi. Karya mereka memengaruhi ilmu pengetahuan dunia.
ex: Kata algoritma berasal dari nama Al-Khawarizmi. // Kitab Ibnu Sina dipakai di Eropa berabad-abad.
pt: Masa keemasan Islam ; Ibnu Sina, Al-Khawarizmi, Ibnu Haitham ; Memengaruhi ilmu dunia
sum: Ilmuwan muslim mewariskan semangat menuntut ilmu.
fig: table Ilmuwan | Bidang ;; Ibnu Sina | kedokteran ;; Al-Khawarizmi | matematika aljabar ;; Ibnu Haitham | optika ;; Al-Biruni | astronomi ;; Al-Farabi | filsafat dan musik ;; Al-Zahrawi | bedah ~ Ilmuwan muslim.

## SUN
# 1|Basa jeung Kaulinan
@ Kecap rajékan
min: 15
act: Kumpulkeun genep kecap rajékan tina obrolan sapopoé, tuluy tangtukeun jenisna.
mis: menganggap semua kata ulang dalam bahasa Sunda berbentuk sama
exp: Kecap rajékan adalah kata ulang dalam bahasa Sunda. Rajékan dwilingga mengulang seluruh kata, misalnya imah-imah. Dwimurni mengulang kata utuh tanpa perubahan bunyi, sedangkan dwireka mengulang dengan perubahan vokal, misalnya bulak-balik. Rajékan dwipurwa mengulang suku kata awal, misalnya tatangga dan lalaki.
ex: Barudak ulin bulak-balik di buruan. // Lalaki éta keur digawé.
pt: Kata ulang bahasa Sunda ; Dwilingga: dwimurni jeung dwireka ; Dwipurwa ngulang engang hareup
sum: Kecap rajékan nambahan harti jamak atawa terus-terusan.
fig: table Kecap rajékan | Jenis ;; imah-imah | dwimurni ;; bulak-balik | dwireka ;; lalaki | dwipurwa ;; tatangga | dwipurwa kecap tangga ;; tulas-tulis | dwireka sora vokal ;; budak-budak | dwimurni jamak ~ Jenis kecap rajékan.
@ Sisindiran paparikan
min: 15
act: Jieun dua pada paparikan anu eusina piwuruk ngeunaan diajar.
mis: menulis paparikan tanpa sampiran yang bunyinya mirip isi
exp: Sisindiran adalah puisi Sunda yang terdiri atas sampiran dan isi. Ada tiga jenis sisindiran: rarakitan, paparikan, dan wawangsalan. Paparikan memiliki sampiran yang bunyinya mirip dengan isi, tetapi kata awal setiap barisnya tidak harus sama. Eusi sisindiran bisa piwuruk, silih asih, atau sésébréd.
ex: Sampiran jeung eusi paparikan sorana sarua di tungtung. // Paparikan sering dipaké dina kawih.
pt: Sisindiran ngawengku cangkang jeung eusi ; Paparikan sorana mirip ; Eusi piwuruk, silih asih, sésébréd
sum: Paparikan ngajarkeun piwuruk kalawan éndah.
fig: table Jenis sisindiran | Ciri ;; rarakitan | kecap awal cangkang jeung eusi sarua ;; paparikan | sora cangkang mirip jeung eusi ;; wawangsalan | eusina kudu ditebak ;; eusi piwuruk | mere naséhat ;; eusi silih asih | ngeunaan kanyaah ;; eusi sésébréd | lulucon ~ Jenis sisindiran.
@ Wawancara basa Sunda
min: 15
act: Wawancara saurang tatangga ngeunaan pagawéanana maké basa hormat, tuluy catet jawabanana.
mis: bertanya dengan basa loma kepada orang yang lebih tua
exp: Wawancara adalah kegiatan tanya jawab untuk memperoleh informasi dari narasumber. Langkahnya menyiapkan daftar pertanyaan, membuat janji, melakukan wawancara dengan sopan, dan mencatat hasilnya. Pertanyaan yang baik memakai unsur 5W+1H. Kepada narasumber yang lebih tua dipakai basa hormat.
ex: Punten, Bapa, tiasa naroskeun sakedap? // Kumaha carana Bapa ngamimitian usaha?
pt: Tanya jawab jeung narasumber ; Nyiapkeun pananya jeung jangji ; Maké basa hormat
sum: Wawancara anu sopan ngahasilkeun informasi anu jelas.
fig: table Léngkah wawancara | Kagiatan ;; nangtukeun tujuan | milih jejer ;; milih narasumber | jalma anu ahli ;; nyusun pananya | 5W+1H ;; nyieun jangji | waktu jeung tempat ;; ngawawancara | sopan jeung basa hormat ;; nyieun laporan | nulis hasil ~ Léngkah wawancara.
@ Pedaran cara nyieun
min: 15
act: Tulis pedaran cara nyieun bajigur atawa kadaharan basajan di imah.
mis: menulis langkah tidak berurutan
exp: Pedaran cara nyieun adalah teks prosedur dalam bahasa Sunda yang menjelaskan langkah membuat sesuatu. Strukturnya terdiri atas judul, bahan, alat, dan léngkah-léngkah. Kata penghubung urutan yang dipakai antara lain mimitina, satuluyna, sanggeus éta, dan pamungkas.
ex: Mimitina, kulub cai nepi ka ngagolak. // Pamungkas, bajigur siap diinum.
pt: Teks prosedur basa Sunda ; Bahan, alat, léngkah ; Kecap mimitina, satuluyna, pamungkas
sum: Pedaran cara nyieun kudu runtut jeung jelas.
fig: table Kecap panghubung | Fungsi ;; mimitina | léngkah kahiji ;; satuluyna | léngkah saterusna ;; sanggeus éta | léngkah sanggeusna ;; tuluy | nuluykeun léngkah ;; saméméhna | léngkah saacanna ;; pamungkas | léngkah panungtung ~ Kecap panghubung dina pedaran.
@ Iklan basa Sunda
min: 15
act: Jieun iklan basa Sunda pikeun ngajual kadaharan has daérah.
mis: membuat iklan dengan kalimat panjang yang membosankan
exp: Iklan adalah pemberitahuan untuk menarik perhatian orang agar membeli barang atau melakukan sesuatu. Iklan basa Sunda memakai kalimat pondok, pikaresepeun, dan ngajak. Iklan niaga bertujuan menjual, sedangkan iklan layanan masyarakat mengajak kebaikan. Unsur iklan meliputi judul, gambar, slogan, dan informasi kontak.
ex: Hayu meuli peuyeum Bandung, amis jeung ngeunah! // Hayu miceun runtah kana tempatna.
pt: Narik perhatian ; Kalimat pondok jeung ngajak ; Iklan niaga jeung layanan masarakat
sum: Iklan basa Sunda kudu pondok jeung pikaresepeun.
fig: table Unsur iklan | Fungsi ;; judul | narik perhatian ;; gambar | ngajelaskeun barang ;; slogan | kalimah ngajak ;; harga | béja biaya ;; alamat | tempat meuli ;; kontak | nomer telepon ~ Unsur iklan.
@ Kaulinan barudak
min: 15
act: Ulin hiji kaulinan barudak Sunda jeung babaturan, tuluy tulis aturanana.
mis: menganggap kaulinan tradisional tidak bermanfaat dibanding permainan gawai
exp: Kaulinan barudak adalah permainan tradisional anak-anak Sunda. Contohnya oray-orayan, sondah, gatrik, ucing sumput, galah, dan bebentengan. Kaulinan melatih kerja sama, kejujuran, ketangkasan, dan kegembiraan. Banyak kaulinan diiringi kakawihan atau nyanyian.
ex: Oray-orayan diiringi kakawihan. // Sondah dimainkan dengan melompat di kotak-kotak.
pt: Kaulinan tradisional Sunda ; Oray-orayan, sondah, gatrik ; Ngalatih gawé bareng jeung jujur
sum: Kaulinan barudak ngawariskeun budaya jeung kabagjaan.
fig: table Kaulinan | Cara ulin ;; oray-orayan | ngabaris jiga oray ;; sondah | luncat dina kotak ;; gatrik | neunggeul iteuk leutik ;; ucing sumput | nyumput jeung néangan ;; galah | ngajaga garis ;; bebentengan | ngarebut benteng ~ Kaulinan barudak Sunda.
# 2|Carita jeung Budaya
@ Carita babad
min: 15
act: Baca ringkesan babad Cirebon atawa babad Sumedang, tuluy catet tokohna.
mis: menganggap carita babad seluruhnya fakta sejarah
exp: Carita babad adalah cerita tentang sejarah suatu daerah atau kerajaan yang bercampur dengan unsur khayalan. Babad ditulis dalam bentuk prosa atau wawacan. Contohnya Babad Cirebon, Babad Sumedang, dan Babad Galuh. Babad penting untuk mengenal asal-usul daerah, tetapi perlu dibandingkan dengan sumber sejarah lain.
ex: Babad Cirebon nyaritakeun Sunan Gunung Jati. // Babad Sumedang nyaritakeun Prabu Geusan Ulun.
pt: Sajarah daérah dicampur khayalan ; Prosa atawa wawacan ; Babad Cirebon, Sumedang, Galuh
sum: Babad ngenalkeun asal-usul daérah.
fig: table Babad | Tokoh ;; Babad Cirebon | Sunan Gunung Jati ;; Babad Sumedang | Prabu Geusan Ulun ;; Babad Galuh | Ciung Wanara ;; Babad Pajajaran | Prabu Siliwangi ;; Babad Banten | Sultan Hasanuddin ;; Babad Limbangan | Prabu Layakusumah ~ Carita babad jeung tokohna.
@ Dongéng sasakala
min: 15
act: Teangan dongéng sasakala ngeunaan ngaran tempat di daérah anjeun.
mis: menganggap sasakala hanya dongeng hewan
exp: Dongéng sasakala adalah dongeng tentang asal-usul suatu tempat, benda, atau kejadian. Contohnya Sasakala Gunung Tangkuban Parahu, Sasakala Situ Bagendit, dan Sasakala Kota Cianjur. Dongéng sasakala biasanya mengandung pesan moral, misalnya tidak serakah atau tidak durhaka.
ex: Tangkuban Parahu asal tina parahu Sangkuriang anu ditajong. // Situ Bagendit asal tina imah Nyi Bagendit anu korét.
pt: Dongéng asal-usul ; Tangkuban Parahu, Situ Bagendit ; Ngandung amanat
sum: Sasakala ngajarkeun ajén moral tina asal-usul tempat.
fig: table Sasakala | Asal-usul ;; Gunung Tangkuban Parahu | parahu Sangkuriang ;; Situ Bagendit | imah Nyi Bagendit ;; Gunung Burangrang | tutunggul kai ;; Talaga Warna | kalung Prabu Swarnalaya ;; Kota Cianjur | tempat cai jeung bérés ;; Curug Cikaso | wangkid cai ragrag ~ Conto dongéng sasakala.
@ Kadaharan has Sunda
min: 15
act: Masak hiji kadaharan has Sunda jeung kolot, tuluy tulis bahanna.
mis: mengira kadaharan Sunda hanya lalapan
exp: Masakan Sunda terkenal dengan lalapan, sambal, dan rasa yang segar. Kadaharan has Sunda antara lain nasi timbel, karedok, pepes, sayur asem, peuyeum, dan surabi. Kadaharan tradisional ini menggunakan bahan lokal dan menjadi bagian dari identitas budaya.
ex: Karedok dijieun tina sayuran atah jeung sambel suuk. // Peuyeum Bandung tina sampeu.
pt: Lalapan jeung sambel ; Nasi timbel, karedok, pepes ; Identitas budaya
sum: Kadaharan has Sunda kudu dimumulé.
fig: table Kadaharan | Bahan utama ;; karedok | sayuran atah ;; peuyeum | sampeu ;; surabi | tipung béas ;; pepes | lauk dibungkus daun ;; nasi timbel | sangu dibungkus daun cau ;; colenak | peuyeum dibakar ~ Kadaharan has Sunda.
@ Pakéan adat Sunda
min: 15
act: Teangan gambar pakéan adat Sunda, tuluy bandingkeun pakéan lalaki jeung awéwé.
mis: menganggap semua pakaian adat Sunda sama untuk semua acara
exp: Pakaian adat Sunda berbeda menurut acara dan kedudukan. Lalaki memakai baju takwa atau pangsi dengan iket atau bendo di kepala. Perempuan memakai kebaya, sinjang atau kain batik, dan selendang. Pada pernikahan adat, pengantin memakai pakaian siger Sunda. Pangsi biasa dipakai untuk pencak silat.
ex: Iket dipaké dina sirah lalaki. // Siger dipaké ku panganten awéwé.
pt: Lalaki: takwa, pangsi, iket ; Awéwé: kebaya, sinjang ; Siger dina nikahan
sum: Pakéan adat Sunda nembongkeun kaéndahan budaya.
fig: table Pakéan | Dipaké ku ;; baju takwa | lalaki dina acara resmi ;; pangsi | pamaén silat ;; iket | sirah lalaki ;; kebaya | awéwé ;; sinjang | awéwé dina handap ;; siger | panganten awéwé ~ Pakéan adat Sunda.
@ Rarangkén aksara Sunda
min: 15
act: Tulis ngaran sorangan maké aksara Sunda anu ngagunakeun rarangkén.
mis: lupa memakai pamaéh untuk menghilangkan vokal
exp: Aksara Sunda atau Kaganga terdiri atas aksara swara (vokal), aksara ngalagena (konsonan), dan rarangkén. Rarangkén adalah tanda untuk mengubah bunyi vokal aksara ngalagena. Misalnya panghulu untuk vokal i, panyuku untuk u, panéléng untuk é, dan pamaéh untuk mematikan vokal.
ex: Aksara ka ditambah panghulu jadi ki. // Pamaéh dipaké dina tungtung kecap.
pt: Aksara swara, ngalagena, rarangkén ; Rarangkén ngarobah sora vokal ; Pamaéh mareuman vokal
sum: Rarangkén ngajadikeun aksara Sunda bisa nulis rupa-rupa sora.
fig: table Rarangkén | Fungsi ;; panghulu | sora i ;; panyuku | sora u ;; panéléng | sora é ;; panolong | sora o ;; pamepet | sora e ;; pamaéh | mareuman vokal ~ Rarangkén aksara Sunda.
@ Imah adat Sunda
min: 15
act: Gambar hiji wangun imah adat Sunda, tuluy tulis ngaran bagian-bagianana.
mis: mengira semua rumah adat Sunda bentuk atapnya sama
exp: Imah adat Sunda biasanya berbentuk rumah panggung dari kayu dan bambu. Bentuk atapnya bermacam-macam, misalnya julang ngapak seperti sayap burung, jolopong yang memanjang, tagog anjing, dan badak heuay. Rumah panggung melindungi dari kelembapan dan binatang. Kampung Naga di Tasikmalaya masih mempertahankan rumah adat.
ex: Hateup julang ngapak mirip jangjang manuk. // Kampung Naga ngajaga imah adat.
pt: Imah panggung tina kai jeung awi ; Julang ngapak, jolopong, tagog anjing ; Kampung Naga
sum: Imah adat Sunda luyu jeung alam sabudeureunana.
fig: table Wangun hateup | Ciri ;; julang ngapak | jiga jangjang manuk ;; jolopong | manjang basajan ;; tagog anjing | jiga anjing diuk ;; badak heuay | jiga badak ngangang ;; parahu kumureb | jiga parahu nangkub ;; capit gunting | tungtung hateup meuntas ~ Wangun hateup imah adat Sunda.
"""

BANK += """
## PAI|Surah Az-Zalzalah
Surah Az-Zalzalah adalah surah ke …|99|98|100|101|99.
Arti Az-Zalzalah adalah …|kegoncangan|pengumpat|kemuliaan|hari kiamat|Kegoncangan.
=|Jumlah ayat Surah Az-Zalzalah adalah …|8|Delapan.
=|Kebaikan sebesar … pun akan dilihat balasannya.|zarah|Zarah.
B|Surah Az-Zalzalah menggambarkan bumi diguncang pada hari kiamat.|Kiamat.
S|Kebaikan kecil tidak dihitung oleh Allah.|Dihitung.
Pada ayat 4, bumi digambarkan …|menceritakan beritanya|diam saja|terbelah dua|menjadi emas|Ayat 4.
Pesan utama Surah Az-Zalzalah adalah …|tidak meremehkan amal sekecil apa pun|boleh berbuat buruk kecil|harta adalah segalanya|tidak perlu beramal|Amal.
## PAI|Iman kepada rasul
Iman kepada rasul adalah rukun iman ke …|empat|tiga|lima|dua|Keempat.
Jumlah rasul yang wajib diketahui adalah …|25|20|10|313|25.
=|Rasul yang memiliki ketabahan luar biasa disebut ulul …|azmi|Ulul azmi.
=|Rasul terakhir adalah Nabi …|Muhammad|Muhammad saw.
B|Rasul wajib menyampaikan wahyu kepada umat.|Rasul.
S|Nabi dan rasul sama persis tanpa perbedaan.|Berbeda.
Rasul ulul azmi yang berani melawan Firaun adalah Nabi …|Musa|Isa|Nuh|Ibrahim|Musa.
Rasul ulul azmi yang sabar berdakwah ratusan tahun adalah Nabi …|Nuh|Musa|Isa|Muhammad|Nuh.
## PAI|Sifat wajib rasul
Siddiq artinya …|jujur|dapat dipercaya|cerdas|menyampaikan|Jujur.
Fatanah artinya …|cerdas|jujur|amanah|menyampaikan|Cerdas.
=|Sifat rasul yang artinya menyampaikan disebut …|tablig|Tablig.
=|Sifat rasul yang artinya dapat dipercaya disebut …|amanah|Amanah.
B|Lawan sifat amanah adalah khianat.|Khianat.
S|Tablig artinya cerdas.|Menyampaikan.
Lawan sifat siddiq adalah …|kizib|khianat|kitman|baladah|Kizib.
Mengembalikan barang titipan meneladani sifat …|amanah|fatanah|tablig|siddiq saja|Amanah.
## PAI|Asmaul Husna Al-'Adl dan Al-Hakim
Al-'Adl artinya Allah Maha …|Adil|Bijaksana|Melihat|Kaya|Adil.
Al-Hakim artinya Allah Maha …|Bijaksana|Adil|Mendengar|Pengasih|Bijaksana.
=|Asmaul Husna yang artinya Maha Benar adalah Al- …|Haq|Al-Haq.
=|Asmaul Husna yang artinya Maha Membuat Perhitungan adalah Al- …|Hasib|Al-Hasib.
B|Adil berarti menempatkan sesuatu sesuai tempatnya.|Tempat.
S|Adil selalu berarti membagi sama rata.|Sesuai.
Ketua kelas yang mendengar dua pihak sebelum memutuskan meneladani sifat …|bijaksana|sombong|kikir|lalai|Al-Hakim.
Asmaul Husna yang artinya Maha Pemberi Keadilan adalah …|Al-Muqsit|Al-Latif|Al-Karim|Al-Basir|Al-Muqsit.
## PAI|Makanan dan minuman halal
Makanan yang baik dan bergizi disebut …|tayib|haram|syubhat|makruh|Tayib.
Lembaga yang mengeluarkan sertifikat halal di Indonesia adalah …|BPJPH|BPOM|KPU|BMKG|BPJPH.
=|Daging … hukumnya haram dimakan.|babi|Babi.
=|Minuman yang memabukkan hukumnya …|haram|Haram.
B|Bangkai ikan halal dimakan.|Ikan.
S|Makanan dari uang curian tetap halal.|Cara memperoleh.
Kehalalan makanan dilihat dari zat, cara memperoleh, dan cara …|mengolah|membungkus|menjual mahal|memamerkan|Mengolah.
Ayam halal dimakan jika …|disembelih sesuai syariat|mati sendiri|dicuri|tidak dicuci|Syariat.
## PAI|Adab berpakaian
Fungsi utama pakaian dalam Islam adalah …|menutup aurat|pamer kekayaan|mengikuti tren saja|menarik perhatian|Aurat.
Aurat laki-laki adalah antara pusar sampai …|lutut|mata kaki|dada|leher|Lutut.
=|Saat berpakaian dianjurkan mendahulukan bagian …|kanan|Kanan.
=|Pakaian sebaiknya tidak ketat dan tidak tembus …|pandang|Pandang.
B|Berdoa saat memakai pakaian dianjurkan.|Doa.
S|Pakaian islami harus mahal dan mewah.|Sederhana.
Aurat perempuan adalah seluruh tubuh kecuali wajah dan …|telapak tangan|kaki|rambut|leher|Telapak.
Pakaian saat salat harus …|bersih|mahal|baru setiap hari|berwarna gelap|Bersih.
## PAI|Surah Al-Humazah
Surah Al-Humazah adalah surah ke …|104|103|105|99|104.
Arti Al-Humazah adalah …|pengumpat|kegoncangan|kemuliaan|gajah|Pengumpat.
=|Jumlah ayat Surah Al-Humazah adalah …|9|Sembilan.
=|Neraka yang disebut dalam Surah Al-Humazah adalah …|Hutamah|Hutamah.
B|Al-Humazah mengancam orang yang suka mencela.|Mencela.
S|Mengejek fisik teman adalah candaan yang dibolehkan.|Dilarang.
Orang dalam Surah Al-Humazah mengira hartanya …|kekal|sedikit|hilang|haram|Kekal.
Pesan Surah Al-Humazah adalah …|menjaga lisan dan tidak sombong dengan harta|menumpuk harta|mengumpat|mencela orang|Pesan.
## PAI|Menghindari ghibah dan namimah
Membicarakan keburukan orang lain disebut …|ghibah|namimah|husnuzan|tawadu'|Ghibah.
Mengadu domba disebut …|namimah|ghibah|hasad|tajassus|Namimah.
=|Larangan ghibah terdapat dalam Surah Al-Hujurat ayat …|12|12.
=|Mencari-cari kesalahan orang lain disebut …|tajassus|Tajassus.
B|Ghibah tetap dilarang walaupun keburukannya benar.|Tetap.
S|Membicarakan keburukan yang benar bukan ghibah.|Tetap ghibah.
Menuduh orang tanpa bukti atau memfitnah disebut …|buhtan|ghibah|husnuzan|syukur|Buhtan.
Cara menghindari ghibah adalah …|menjaga lisan|ikut bergosip|menyebarkan cerita|mencari kesalahan|Lisan.
## PAI|Husnuzan
Husnuzan artinya …|berprasangka baik|berprasangka buruk|iri hati|sombong|Husnuzan.
Lawan husnuzan adalah …|su'uzan|tawadu'|qanaah|ikhlas|Su'uzan.
=|Husnuzan kepada diri sendiri berarti percaya diri dan …|optimis|Optimis.
=|Husnuzan kepada Allah berarti yakin setiap takdir ada …|hikmahnya;hikmah|Hikmah.
B|Husnuzan kepada teman berarti mencari penjelasan dulu.|Klarifikasi.
S|Langsung menuduh teman adalah sikap husnuzan.|Su'uzan.
Teman tidak membalas pesan, sikap husnuzan adalah berpikir …|mungkin ia sedang sibuk|ia membenci kita|ia sombong|ia berbohong|Baik sangka.
Menerima teguran guru dengan baik termasuk husnuzan kepada …|guru|tetangga|diri sendiri|benda|Guru.
## PAI|Zakat fitrah
Zakat fitrah dibayar paling lambat sebelum salat …|Idulfitri|Iduladha|Jumat|tarawih|Idulfitri.
Besar zakat fitrah sekitar … makanan pokok.|2,5 kg|1 kg|10 kg|0,5 kg|2,5 kg.
=|Pengurus zakat disebut …|amil|Amil.
=|Golongan penerima zakat berjumlah …|8;delapan|Asnaf.
B|Zakat fitrah wajib bagi setiap muslim.|Wajib.
S|Zakat fitrah boleh dibayar kapan saja setelah hari raya.|Sebelum salat.
Musafir yang kehabisan bekal termasuk golongan …|ibnu sabil|garim|amil|mualaf|Ibnu sabil.
Orang yang baru masuk Islam termasuk golongan …|mualaf|fakir|garim|amil|Mualaf.
## PAI|Adab bertetangga
Orang beriman hendaknya … tetangganya.|memuliakan|mengganggu|menjauhi|mengejek|Memuliakan.
Saat tetangga sakit, sebaiknya kita …|menjenguk|membiarkan|menertawakan|berisik|Menjenguk.
=|Memberi masakan kepada tetangga termasuk saling …|memberi;berbagi|Memberi.
=|Pada malam hari kita tidak boleh membuat …|bising;gaduh|Bising.
B|Ikut kerja bakti termasuk adab bertetangga.|Gotong royong.
S|Membunyikan musik keras sampai larut malam termasuk adab yang baik.|Mengganggu.
Saat tetangga pindahan, sikap yang baik adalah …|membantu mengangkat barang|menonton saja|mengeluh|pergi|Membantu.
Bertemu tetangga di jalan sebaiknya …|menyapa dengan ramah|pura-pura tidak melihat|berlari|memalingkan wajah|Menyapa.
## PAI|Ilmuwan muslim dan karyanya
Ilmuwan muslim penulis Al-Qanun fit Tibb adalah …|Ibnu Sina|Al-Khawarizmi|Ibnu Haitham|Al-Biruni|Ibnu Sina.
Kata algoritma berasal dari nama …|Al-Khawarizmi|Ibnu Sina|Al-Farabi|Al-Zahrawi|Al-Khawarizmi.
=|Ibnu Haitham terkenal dalam bidang …|optika;cahaya|Optika.
=|Ibnu Sina terkenal dalam bidang …|kedokteran|Kedokteran.
B|Al-Biruni ahli astronomi.|Astronomi.
S|Ilmu modern sama sekali tidak dipengaruhi ilmuwan muslim.|Berpengaruh.
Ilmuwan muslim yang ahli bedah adalah …|Al-Zahrawi|Al-Farabi|Al-Biruni|Al-Khawarizmi|Al-Zahrawi.
Al-Khawarizmi mengembangkan cabang matematika …|aljabar|geometri bola|statistika modern|kalkulus|Aljabar.
## SUN|Kecap rajékan
Kecap rajékan nyaéta kecap anu …|diulang|dihijikeun|disingget|dirobah hartina|Diulang.
Kecap imah-imah kaasup rajékan …|dwimurni|dwireka|dwipurwa|trilingga|Dwimurni.
=|Kecap bulak-balik kaasup rajékan …|dwireka|Dwireka.
=|Kecap lalaki kaasup rajékan …|dwipurwa|Dwipurwa.
B|Rajékan dwipurwa ngulang engang hareup.|Dwipurwa.
S|Kecap bulak-balik kaasup dwimurni.|Dwireka.
Kecap tulas-tulis kaasup rajékan …|dwireka|dwimurni|dwipurwa|trilingga|Dwireka.
Kecap budak-budak nuduhkeun harti …|loba|hiji|leutik|gedé|Jamak.
## SUN|Sisindiran paparikan
Sisindiran diwangun ku cangkang jeung …|eusi|judul|panutup|pangantét|Eusi.
Paparikan nyaéta sisindiran anu sora cangkangna … jeung eusi.|mirip|béda pisan|sarua kecapna|tanpa sora|Mirip.
=|Sisindiran anu eusina kudu ditebak disebut …|wawangsalan|Wawangsalan.
=|Sisindiran anu kecap awal cangkang jeung eusina sarua disebut …|rarakitan|Rarakitan.
B|Eusi sisindiran bisa piwuruk.|Piwuruk.
S|Paparikan teu boga cangkang.|Boga.
Sisindiran anu eusina lulucon disebut eusi …|sésébréd|piwuruk|silih asih|kasedih|Sésébréd.
Sisindiran anu eusina ngeunaan kanyaah disebut eusi …|silih asih|sésébréd|piwuruk|sindiran|Silih asih.
## SUN|Wawancara basa Sunda
Jalma anu diwawancara disebut …|narasumber|pewawancara|panongton|notulis|Narasumber.
Ka narasumber anu leuwih kolot maké basa …|hormat|kasar|loma|campuran|Hormat.
=|Pananya anu hadé ngagunakeun unsur 5W+ …|1H|1H.
=|Saméméh wawancara kudu nyieun … waktu jeung tempat.|jangji|Jangji.
B|Hasil wawancara kudu dicatet.|Catet.
S|Pananya wawancara teu kudu disiapkeun.|Disiapkeun.
Léngkah pamungkas wawancara nyaéta …|nyieun laporan|milih narasumber|nyusun pananya|nyieun jangji|Laporan.
Kalimah pangbuka wawancara anu sopan nyaéta …|Punten, tiasa naroskeun sakedap?|Héy, jawab!|Buru-buru siah!|Naon sia?|Sopan.
## SUN|Pedaran cara nyieun
Pedaran cara nyieun kaasup teks …|prosedur|narasi|déskripsi|warta|Prosedur.
Kecap panghubung pikeun léngkah kahiji nyaéta …|mimitina|pamungkas|satuluyna|tungtungna|Mimitina.
=|Kecap panghubung pikeun léngkah panungtung nyaéta …|pamungkas|Pamungkas.
=|Bagian anu eusina bahan-bahan disebut …|bahan|Bahan.
B|Léngkah dina pedaran kudu runtut.|Runtut.
S|Léngkah dina pedaran meunang acak.|Runtut.
Kecap panghubung satuluyna dipaké pikeun léngkah …|saterusna|kahiji|panungtung|saméméhna|Saterusna.
Wajan jeung sendok dina pedaran kaasup …|alat|bahan|léngkah|judul|Alat.
## SUN|Iklan basa Sunda
Kalimah dina iklan kudu … jeung pikaresepeun.|pondok|panjang pisan|hésé dihartikeun|kasar|Pondok.
Iklan anu tujuanana ngajual disebut iklan …|niaga|layanan masarakat|béja duka|lowongan|Niaga.
=|Kalimah ngajak dina iklan disebut …|slogan|Slogan.
=|Iklan anu ngajak kana kahadéan disebut iklan layanan …|masarakat;masyarakat|Layanan masarakat.
B|Iklan bisa maké gambar.|Gambar.
S|Iklan hadé maké kalimah panjang anu ngabosenkeun.|Pondok.
Unsur iklan anu nuduhkeun tempat meuli nyaéta …|alamat|slogan|judul|gambar|Alamat.
Conto iklan layanan masarakat nyaéta …|Hayu miceun runtah kana tempatna.|Diskon 50 persén!|Dijual imah murah.|Dipilarian pagawé.|Ngajak.
## SUN|Kaulinan barudak
Kaulinan ngabaris jiga oray disebut …|oray-orayan|sondah|gatrik|galah|Oray-orayan.
Kaulinan luncat dina kotak-kotak disebut …|sondah|ucing sumput|gatrik|bebentengan|Sondah.
=|Kaulinan nyumput jeung néangan disebut ucing …|sumput|Ucing sumput.
=|Kaulinan neunggeul iteuk leutik disebut …|gatrik|Gatrik.
B|Kaulinan barudak ngalatih gawé bareng.|Gawé bareng.
S|Kaulinan tradisional teu aya mangpaatna.|Aya mangpaat.
Kaulinan ngarebut benteng lawan disebut …|bebentengan|sondah|oray-orayan|gatrik|Bebentengan.
Kaulinan barudak sok dibarengan ku …|kakawihan|pidato|warta|surat|Kakawihan.
## SUN|Carita babad
Carita babad nyaritakeun … hiji daérah.|sajarah|kadaharan|kasenian wungkul|cuaca|Sajarah.
Babad Cirebon nyaritakeun tokoh …|Sunan Gunung Jati|Prabu Geusan Ulun|Ciung Wanara|Sultan Hasanuddin|Sunan Gunung Jati.
=|Babad Sumedang nyaritakeun Prabu Geusan …|Ulun|Geusan Ulun.
=|Carita babad sok ditulis dina wangun prosa atawa …|wawacan|Wawacan.
B|Babad dicampur ku unsur khayalan.|Khayalan.
S|Sakabéh eusi babad pasti fakta sajarah.|Dicampur.
Babad Banten nyaritakeun tokoh …|Sultan Hasanuddin|Prabu Siliwangi|Sangkuriang|Purbasari|Banten.
Babad Pajajaran nyaritakeun tokoh …|Prabu Siliwangi|Sunan Gunung Jati|Geusan Ulun|Hasanuddin|Siliwangi.
## SUN|Dongéng sasakala
Dongéng sasakala nyaritakeun … hiji tempat.|asal-usul|harga|cuaca|pangeusi wungkul|Asal-usul.
Gunung Tangkuban Parahu asalna tina parahu …|Sangkuriang|Si Kabayan|Lutung Kasarung|Mundinglaya|Sangkuriang.
=|Situ Bagendit asalna tina imah Nyi …|Bagendit|Bagendit.
=|Talaga Warna asalna tina kalung Prabu …|Swarnalaya|Swarnalaya.
B|Dongéng sasakala ngandung amanat.|Amanat.
S|Sasakala ngan ukur dongéng sato.|Asal-usul.
Amanat Sasakala Situ Bagendit nyaéta ulah …|korét|bageur|jujur|daék tutulung|Korét.
Gunung Burangrang dina dongéng asalna tina …|tutunggul kai|parahu|kalung|imah|Tutunggul.
## SUN|Kadaharan has Sunda
Karedok dijieun tina sayuran …|atah|digoréng|dibakar|direbus lila|Atah.
Peuyeum dijieun tina …|sampeu|béas|jagong|suuk|Sampeu.
=|Surabi dijieun tina tipung …|béas;beas|Tipung béas.
=|Sangu anu dibungkus daun cau disebut nasi …|timbel|Timbel.
B|Colenak dijieun tina peuyeum dibakar.|Colenak.
S|Kadaharan Sunda ngan ukur lalapan.|Loba.
Lauk anu dibungkus daun tuluy dikukus disebut …|pepes|karedok|surabi|peuyeum|Pepes.
Masakan Sunda kawentar ku lalapan jeung …|sambel|kéju|roti|mentéga|Sambel.
## SUN|Pakéan adat Sunda
Tutup sirah lalaki Sunda disebut …|iket|siger|kebaya|sinjang|Iket.
Pakéan awéwé Sunda nyaéta kebaya jeung …|sinjang|pangsi|takwa|iket|Sinjang.
=|Makuta panganten awéwé Sunda disebut …|siger|Siger.
=|Pakéan anu sok dipaké pamaén silat disebut …|pangsi|Pangsi.
B|Baju takwa dipaké lalaki dina acara resmi.|Takwa.
S|Sakabéh pakéan adat Sunda sarua pikeun unggal acara.|Béda.
Iket dipaké dina …|sirah|suku|leungeun|cangkéng|Sirah.
Sinjang dipaké dina awak bagian …|handap|luhur|sirah|leungeun|Handap.
## SUN|Rarangkén aksara Sunda
Rarangkén pikeun sora i disebut …|panghulu|panyuku|pamaéh|panéléng|Panghulu.
Rarangkén pikeun mareuman vokal disebut …|pamaéh|panghulu|panolong|pamepet|Pamaéh.
=|Rarangkén pikeun sora u disebut …|panyuku|Panyuku.
=|Rarangkén pikeun sora é disebut …|panéléng;paneleng|Panéléng.
B|Aksara Sunda disebut ogé Kaganga.|Kaganga.
S|Pamaéh dipaké pikeun sora o.|Panolong.
Aksara pikeun konsonan disebut aksara …|ngalagena|swara|rarangkén|angka|Ngalagena.
Rarangkén pikeun sora o disebut …|panolong|pamepet|panghulu|panyuku|Panolong.
## SUN|Imah adat Sunda
Imah adat Sunda biasana wangunna imah …|panggung|tembok gedong|apartemen|kapal|Panggung.
Hateup anu jiga jangjang manuk disebut …|julang ngapak|jolopong|tagog anjing|badak heuay|Julang ngapak.
=|Kampung anu ngajaga imah adat di Tasikmalaya nyaéta Kampung …|Naga|Naga.
=|Hateup anu manjang basajan disebut …|jolopong|Jolopong.
B|Imah panggung ngajaga tina kalembaban.|Panggung.
S|Sakabéh imah adat Sunda sarua wangun hateupna.|Rupa-rupa.
Hateup anu jiga badak ngangang disebut …|badak heuay|tagog anjing|jolopong|capit gunting|Badak heuay.
Bahan utama imah adat Sunda nyaéta kai jeung …|awi|beusi|kaca|plastik|Awi.
"""

SAS += """
## PAI 1
0|Pada ayat 1 Surah Az-Zalzalah, bumi digambarkan ....|diguncang dahsyat|tenang|subur|bersinar|Ayat 1.
1|Rasul ulul azmi yang teguh bertauhid adalah Nabi ....|Ibrahim|Nuh|Musa|Isa|Ibrahim.
2|Lawan sifat tablig adalah ....|kitman|kizib|khianat|baladah|Kitman.
3|Al-Hakam artinya Allah Maha ....|Menetapkan Hukum|Pengasih|Melihat|Kaya|Al-Hakam.
4|Hukum memakan sayur dan buah adalah ....|halal|haram|makruh|syubhat|Halal.
5|Pakaian yang tidak berlebihan berarti ....|sederhana|sangat mewah|serba emas|mengikuti tren saja|Sederhana.
## PAI 2
0|Ayat 2 Surah Al-Humazah menggambarkan orang yang ....|mengumpulkan dan menghitung harta|rajin bersedekah|berbuat baik|bersyukur|Ayat 2.
1|Iri hati disebut juga ....|hasad|husnuzan|tawadu'|syukur|Hasad.
2|Tidak mudah curiga kepada tetangga termasuk sikap ....|husnuzan|su'uzan|hasad|riya|Husnuzan.
3|Orang yang berutang untuk kebaikan termasuk golongan ....|garim|amil|mualaf|ibnu sabil|Garim.
4|Saat ada kerja bakti di lingkungan, sikap yang baik adalah ....|ikut membantu|pergi berlibur|menonton saja|mengeluh|Bantu.
5|Al-Farabi terkenal dalam bidang ....|filsafat dan musik|kedokteran|optika|astronomi|Al-Farabi.
## SUN 1
0|Kecap tatangga kaasup rajékan ....|dwipurwa|dwimurni|dwireka|trilingga|Dwipurwa.
1|Sisindiran anu mere naséhat disebut eusi ....|piwuruk|sésébréd|silih asih|lulucon|Piwuruk.
2|Léngkah wawancara milih jalma anu ahli disebut ....|milih narasumber|nyusun pananya|nyieun laporan|nyieun jangji|Narasumber.
3|Kecap panghubung pikeun léngkah saacanna nyaéta ....|saméméhna|pamungkas|satuluyna|mimitina|Saméméhna.
4|Unsur iklan anu nuduhkeun nomer telepon disebut ....|kontak|slogan|gambar|harga|Kontak.
5|Kaulinan ngajaga garis supaya lawan teu bisa meuntas disebut ....|galah|sondah|gatrik|ucing sumput|Galah.
## SUN 2
0|Babad Galuh nyaritakeun tokoh ....|Ciung Wanara|Sunan Gunung Jati|Geusan Ulun|Hasanuddin|Galuh.
1|Gunung Tangkuban Parahu kawentar dina dongéng tokoh ....|Sangkuriang|Si Kabayan|Purbasari|Lutung|Sangkuriang.
2|Kadaharan tina peuyeum anu dibakar disebut ....|colenak|karedok|pepes|surabi|Colenak.
3|Pakéan awéwé Sunda bagian luhur disebut ....|kebaya|sinjang|pangsi|iket|Kebaya.
4|Rarangkén pikeun sora e disebut ....|pamepet|panghulu|pamaéh|panyuku|Pamepet.
5|Hateup imah anu tungtungna meuntas disebut ....|capit gunting|julang ngapak|jolopong|badak heuay|Capit gunting.
"""
