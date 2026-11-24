TOPICS = ""
BANK = ""
SAS = ""

TOPICS += """
## MAT
# 1|Bilangan, Himpunan, dan Pertidaksamaan
@ Operasi bilangan bulat
min: 15
act: Catat suhu terendah dan tertinggi beberapa kota dunia, lalu hitung selisihnya.
mis: menganggap −5 − 3 hasilnya −2
exp: Bilangan bulat terdiri atas bilangan bulat negatif, nol, dan bilangan bulat positif. Pada penjumlahan, menambah bilangan negatif sama dengan mengurangi. Pada pengurangan, mengurangi bilangan negatif sama dengan menambah. Pada perkalian dan pembagian, tanda sama menghasilkan positif dan tanda berbeda menghasilkan negatif.
ex: −5 − 3 = −8. // 7 − (−2) = 9. // (−4) × (−3) = 12.
pt: Mengurangi negatif sama dengan menambah ; Tanda sama hasilnya positif ; Tanda berbeda hasilnya negatif
sum: Aturan tanda menentukan hasil operasi bilangan bulat.
fig: table Operasi | Hasil ;; −5 − 3 | −8 ;; 7 − (−2) | 9 ;; (−4) × (−3) | 12 ;; (−6) × 2 | −12 ;; (−20) : 4 | −5 ;; (−18) : (−3) | 6 ~ Contoh operasi bilangan bulat.
@ Bilangan berpangkat
min: 15
act: Hitung banyak sel bakteri yang membelah dua setiap jam selama 5 jam dengan bilangan berpangkat.
mis: mengira 2³ × 2² = 2⁶
exp: Bilangan berpangkat adalah perkalian berulang dari bilangan yang sama. Sifat-sifatnya: aᵐ × aⁿ = aᵐ⁺ⁿ, aᵐ : aⁿ = aᵐ⁻ⁿ, (aᵐ)ⁿ = aᵐˣⁿ, dan a⁰ = 1 untuk a bukan nol. Sifat ini memudahkan perhitungan bilangan yang sangat besar.
ex: 2³ × 2² = 2⁵ = 32. // 5⁰ = 1. // (3²)³ = 3⁶.
pt: Perkalian: pangkat dijumlahkan ; Pembagian: pangkat dikurangkan ; Pangkat nol hasilnya 1
sum: Sifat pangkat menyederhanakan perhitungan.
fig: table Bentuk | Hasil ;; 2³ × 2² | 2⁵ ;; 3⁵ : 3² | 3³ ;; (2²)³ | 2⁶ ;; 7⁰ | 1 ;; 10³ | 1.000 ;; 2⁴ | 16 ~ Sifat bilangan berpangkat.
@ Notasi ilmiah
min: 15
act: Cari jarak bumi ke matahari, lalu tulis dalam notasi ilmiah.
mis: menulis 3.500 sebagai 35 × 10²
exp: Notasi ilmiah adalah cara menulis bilangan sangat besar atau sangat kecil dalam bentuk a × 10ⁿ, dengan 1 ≤ a < 10. Contohnya 3.500 = 3,5 × 10³ dan 0,0042 = 4,2 × 10⁻³. Notasi ilmiah banyak dipakai dalam sains.
ex: 150.000.000 km = 1,5 × 10⁸ km. // 0,0005 = 5 × 10⁻⁴.
pt: Bentuk a × 10ⁿ ; 1 ≤ a < 10 ; Pangkat negatif untuk bilangan kecil
sum: Notasi ilmiah meringkas bilangan sangat besar dan kecil.
fig: table Bilangan | Notasi ilmiah ;; 3.500 | 3,5 × 10³ ;; 150.000.000 | 1,5 × 10⁸ ;; 0,0042 | 4,2 × 10⁻³ ;; 72.000 | 7,2 × 10⁴ ;; 0,0005 | 5 × 10⁻⁴ ;; 6.000.000 | 6 × 10⁶ ~ Contoh notasi ilmiah.
@ Himpunan
min: 15
act: Buat himpunan hobi teman-temanmu, lalu cari irisan dua himpunan hobi itu.
mis: menuliskan anggota yang sama dua kali dalam himpunan
exp: Himpunan adalah kumpulan benda yang dapat didefinisikan dengan jelas. Anggota himpunan ditulis di dalam kurung kurawal. Irisan A ∩ B adalah anggota yang ada di A dan B. Gabungan A ∪ B adalah semua anggota A atau B. Himpunan kosong ditulis { } atau ∅.
ex: A = {1, 2, 3}, B = {2, 3, 4}. A ∩ B = {2, 3}. // A ∪ B = {1, 2, 3, 4}.
pt: Kumpulan yang terdefinisi jelas ; Irisan: anggota sama ; Gabungan: semua anggota
sum: Himpunan membantu mengelompokkan dengan tepat.
fig: table Istilah | Lambang atau arti ;; irisan | ∩ ;; gabungan | ∪ ;; anggota | ∈ ;; bukan anggota | ∉ ;; himpunan kosong | ∅ ;; himpunan semesta | S ~ Lambang himpunan.
@ Pertidaksamaan linear satu variabel
min: 15
act: Tentukan berapa paling banyak buku seharga Rp8.000 yang bisa dibeli dengan Rp50.000.
mis: lupa membalik tanda saat mengalikan dengan bilangan negatif
exp: Pertidaksamaan linear satu variabel memakai tanda <, >, ≤, atau ≥ dengan satu variabel berpangkat satu. Penyelesaiannya mirip persamaan: tambah, kurang, kali, atau bagi kedua ruas. Jika dikali atau dibagi bilangan negatif, tanda pertidaksamaan dibalik.
ex: x + 3 > 7, maka x > 4. // −2x < 6, maka x > −3.
pt: Memakai tanda <, >, ≤, ≥ ; Operasi sama pada kedua ruas ; Balik tanda jika dikali negatif
sum: Pertidaksamaan menghasilkan himpunan penyelesaian.
fig: table Pertidaksamaan | Penyelesaian ;; x + 3 > 7 | x > 4 ;; 2x ≤ 10 | x ≤ 5 ;; x − 5 < 1 | x < 6 ;; −2x < 6 | x > −3 ;; 3x ≥ 12 | x ≥ 4 ;; x/2 > 3 | x > 6 ~ Contoh pertidaksamaan linear.
@ Operasi pecahan dan desimal
min: 15
act: Hitung bahan kue untuk setengah resep yang memakai takaran pecahan.
mis: mengalikan pecahan dengan menyamakan penyebut terlebih dahulu
exp: Penjumlahan dan pengurangan pecahan memerlukan penyebut yang sama. Perkalian pecahan dilakukan dengan mengalikan pembilang dengan pembilang dan penyebut dengan penyebut. Pembagian pecahan dilakukan dengan mengalikan kebalikan pembagi. Desimal dapat diubah menjadi pecahan untuk memudahkan.
ex: 2/3 × 3/4 = 6/12 = 1/2. // 1/2 : 1/4 = 1/2 × 4 = 2.
pt: Tambah kurang: samakan penyebut ; Kali: pembilang kali pembilang ; Bagi: kali kebalikan
sum: Setiap operasi pecahan punya aturan sendiri.
fig: table Operasi | Hasil ;; 1/2 + 1/3 | 5/6 ;; 3/4 − 1/2 | 1/4 ;; 2/3 × 3/4 | 1/2 ;; 1/2 : 1/4 | 2 ;; 0,5 × 0,4 | 0,2 ;; 1,2 : 0,3 | 4 ~ Contoh operasi pecahan dan desimal.
# 2|Aritmetika Sosial, Geometri, dan Data
@ Untung, rugi, dan persentase
min: 15
act: Hitung untung jika kamu membeli 10 gantungan kunci Rp5.000 dan menjualnya Rp7.000 per buah.
mis: menghitung persentase untung dari harga jual, bukan dari harga beli
exp: Untung terjadi jika harga jual lebih besar dari harga beli. Rugi terjadi jika harga jual lebih kecil. Persentase untung atau rugi dihitung dari harga beli: untung : harga beli × 100%. Aritmetika sosial membantu kegiatan jual beli sehari-hari.
ex: Beli Rp50.000, jual Rp60.000: untung Rp10.000 atau 20%. // Beli Rp40.000, jual Rp30.000: rugi Rp10.000 atau 25%.
pt: Untung: jual > beli ; Rugi: jual < beli ; Persentase dari harga beli
sum: Persentase untung dan rugi dihitung dari harga beli.
fig: table Harga beli dan jual | Hasil ;; beli 50.000 jual 60.000 | untung 20% ;; beli 40.000 jual 30.000 | rugi 25% ;; beli 100.000 jual 110.000 | untung 10% ;; beli 80.000 jual 60.000 | rugi 25% dari 80.000 ;; beli 20.000 jual 25.000 | untung 25% ;; beli 10.000 jual 10.000 | impas ~ Untung dan rugi.
@ Diskon dan bunga tunggal
min: 15
act: Hitung harga setelah diskon dari brosur toko, lalu bandingkan dua toko.
mis: menambahkan diskon ke harga awal
exp: Diskon adalah potongan harga. Harga setelah diskon = harga awal − (persen diskon × harga awal). Bunga tunggal adalah tambahan uang dari tabungan atau pinjaman yang dihitung dari modal awal. Bunga satu tahun = persen bunga × modal.
ex: Diskon 20% dari Rp150.000 = Rp30.000, harga menjadi Rp120.000. // Tabungan Rp1.000.000 bunga 5% per tahun, bunganya Rp50.000.
pt: Diskon mengurangi harga ; Bunga tunggal dari modal awal ; Bunga = persen × modal
sum: Diskon dan bunga dihitung dengan persen.
fig: table Kasus | Hasil ;; diskon 20% dari 150.000 | harga 120.000 ;; diskon 50% dari 80.000 | harga 40.000 ;; diskon 10% dari 200.000 | harga 180.000 ;; bunga 5% dari 1.000.000 | bunga 50.000 ;; bunga 10% dari 500.000 | bunga 50.000 per tahun ;; bunga 6% dari 2.000.000 | bunga 120.000 ~ Contoh diskon dan bunga tunggal.
@ Keliling dan luas segiempat
min: 15
act: Ukur halaman rumah berbentuk persegi panjang atau trapesium, lalu hitung luasnya.
mis: memakai rumus luas jajargenjang untuk belah ketupat tanpa diagonal
exp: Segiempat terdiri atas persegi, persegi panjang, jajargenjang, belah ketupat, layang-layang, dan trapesium. Luas belah ketupat dan layang-layang = diagonal 1 × diagonal 2 : 2. Luas trapesium = jumlah sisi sejajar × tinggi : 2. Keliling adalah jumlah semua sisi.
ex: Belah ketupat diagonal 6 dan 8 cm: luas 24 cm². // Layang-layang diagonal 10 dan 12 cm: luas 60 cm².
pt: Belah ketupat dan layang-layang memakai diagonal ; Trapesium memakai sisi sejajar ; Keliling jumlah semua sisi
sum: Setiap segiempat memiliki rumus luasnya.
fig: table Bangun | Rumus luas ;; persegi | s × s ;; persegi panjang | p × l ;; jajargenjang | a × t ;; belah ketupat | d1 × d2 : 2 ;; layang-layang | d1 × d2 : 2 untuk layang-layang ;; trapesium | jumlah sisi sejajar × t : 2 ~ Rumus luas segiempat.
@ Jenis dan sifat segitiga
min: 15
act: Gunting segitiga dari kertas, sobek ketiga sudutnya, lalu susun untuk membuktikan jumlahnya 180°.
mis: mengira jumlah sudut segitiga bergantung pada ukurannya
exp: Segitiga dapat dibedakan menurut sisinya, yaitu sama sisi, sama kaki, dan sembarang. Menurut sudutnya, ada segitiga lancip, siku-siku, dan tumpul. Jumlah ketiga sudut segitiga selalu 180°. Segitiga sama sisi memiliki tiga sudut sama besar, masing-masing 60°.
ex: Dua sudut 50° dan 60°, sudut ketiga 70°. // Segitiga siku-siku memiliki satu sudut 90°.
pt: Menurut sisi dan sudut ; Jumlah sudut 180° ; Sama sisi tiap sudut 60°
sum: Jumlah sudut segitiga selalu 180°.
fig: table Segitiga | Ciri ;; sama sisi | tiga sisi sama panjang ;; sama kaki | dua sisi sama panjang ;; sembarang | semua sisi berbeda ;; siku-siku | satu sudut 90° ;; tumpul | satu sudut lebih dari 90° ;; lancip | semua sudut kurang dari 90° ~ Jenis segitiga.
@ Ukuran pemusatan data
min: 15
act: Catat nilai ulangan lima mata pelajaranmu, lalu hitung rata-rata, median, dan modusnya.
mis: mencari median tanpa mengurutkan data
exp: Ukuran pemusatan data terdiri atas mean, median, dan modus. Mean atau rata-rata adalah jumlah data dibagi banyak data. Median adalah nilai tengah setelah data diurutkan. Modus adalah data yang paling sering muncul.
ex: Data 6, 7, 7, 8, 9: mean 7,4, median 7, modus 7. // Data 2, 4, 6, 8: median (4 + 6) : 2 = 5.
pt: Mean: jumlah dibagi banyak ; Median: nilai tengah data terurut ; Modus: paling sering muncul
sum: Ukuran pemusatan menggambarkan data dengan satu nilai.
fig: table Data | Ukuran ;; 6, 7, 7, 8, 9 rata-rata | 7,4 ;; 3, 5, 9 median | 5 ;; 2, 4, 6, 8 median | 5 dari dua nilai tengah ;; 4, 4, 5, 6 modus | 4 ;; 10, 20, 30 rata-rata | 20 ;; 1, 2, 2, 2, 3 modus | 2 ~ Contoh mean, median, dan modus.
@ Peluang empirik
min: 15
act: Lempar koin 50 kali, catat hasil angka dan gambar, lalu hitung peluang empiriknya.
mis: mengira peluang empirik selalu sama dengan peluang teoretis
exp: Peluang empirik adalah peluang yang diperoleh dari hasil percobaan. Rumusnya banyak kejadian yang muncul dibagi banyak percobaan. Makin banyak percobaan, peluang empirik makin mendekati peluang teoretis. Nilai peluang berada di antara 0 dan 1.
ex: Koin dilempar 50 kali, muncul angka 27 kali: peluang empirik 27/50. // Dadu dilempar 60 kali, muncul mata 6 sebanyak 9 kali: 9/60.
pt: Diperoleh dari percobaan ; Kejadian dibagi banyak percobaan ; Nilai 0 sampai 1
sum: Peluang empirik mendekati teori jika percobaan banyak.
fig: table Percobaan | Peluang empirik ;; angka 27 kali dari 50 | 27/50 ;; mata 6 muncul 9 kali dari 60 | 9/60 ;; hujan 12 hari dari 30 | 12/30 ;; gol 3 kali dari 10 tendangan | 3/10 ;; merah 5 kali dari 20 putaran | 5/20 ;; tidak pernah muncul | 0 ~ Contoh peluang empirik.
"""

BANK += """
## MAT|Operasi bilangan bulat
Hasil dari −8 + 5 adalah …|−3|3|−13|13|−8 + 5.
Hasil dari 4 − (−6) adalah …|10|−2|2|−10|Mengurangi negatif.
=|Hasil dari (−7) × (−2) adalah …|14|Tanda sama positif.
=|Hasil dari (−24) : 6 adalah …|−4|Tanda berbeda negatif.
B|Hasil (−3) × 5 adalah −15.|Tanda berbeda.
S|Hasil (−9) : (−3) adalah −3.|Hasilnya 3.
Suhu −3 °C naik 8 °C. Suhu sekarang …|5 °C|−11 °C|11 °C|−5 °C|−3 + 8.
Selisih suhu 25 °C dan −5 °C adalah …|30 °C|20 °C|−30 °C|5 °C|25 − (−5).
## MAT|Bilangan berpangkat
Hasil dari 3² × 3³ adalah …|3⁵|3⁶|9⁵|6⁵|Pangkat dijumlah.
Hasil dari 5⁴ : 5² adalah …|5²|5⁶|5⁸|1²|Pangkat dikurang.
=|Nilai dari 9⁰ adalah …|1|Pangkat nol.
=|Nilai dari 2⁵ adalah …|32|2 × 2 × 2 × 2 × 2.
B|(2³)² sama dengan 2⁶.|Pangkat dikali.
S|2³ × 2² sama dengan 2⁶.|2⁵.
Bentuk sederhana dari a³ × a⁴ adalah …|a⁷|a¹²|a|2a⁷|Dijumlah.
Bakteri membelah dua tiap jam. Dari 1 bakteri, setelah 4 jam menjadi …|16|8|4|32|2⁴.
## MAT|Notasi ilmiah
Notasi ilmiah dari 45.000 adalah …|4,5 × 10⁴|45 × 10³|0,45 × 10⁵|4,5 × 10³|a antara 1 dan 10.
Notasi ilmiah dari 0,003 adalah …|3 × 10⁻³|3 × 10³|0,3 × 10⁻²|30 × 10⁻⁴|Pangkat negatif.
=|Bilangan 2,5 × 10³ sama dengan …|2.500;2500|2,5 × 1.000.
=|Pada a × 10ⁿ, nilai a harus lebih dari atau sama dengan 1 dan kurang dari …|10|1 ≤ a < 10.
B|7 × 10² sama dengan 700.|700.
S|35 × 10² adalah bentuk notasi ilmiah yang benar.|3,5 × 10³.
Notasi ilmiah dari 980.000 adalah …|9,8 × 10⁵|98 × 10⁴|9,8 × 10⁴|0,98 × 10⁶|Benar.
Bilangan 1,2 × 10⁻² sama dengan …|0,012|0,12|120|0,0012|Geser koma dua kali.
## MAT|Himpunan
Lambang irisan himpunan adalah …|∩|∪|∈|∅|Irisan.
A = {1, 2, 3, 4}, B = {3, 4, 5}. A ∩ B adalah …|{3, 4}|{1, 2, 3, 4, 5}|{1, 2}|{5}|Anggota sama.
=|Lambang himpunan kosong adalah …|∅;{ }|Kosong.
=|A = {a, b}, B = {b, c}. Banyak anggota A ∪ B adalah …|3|{a, b, c}.
B|Lambang ∈ berarti anggota.|Anggota.
S|Kumpulan anak yang pintar adalah himpunan karena terdefinisi jelas.|Tidak jelas.
P = {bilangan genap kurang dari 10}. Anggota P adalah …|{2, 4, 6, 8}|{1, 3, 5, 7, 9}|{2, 4, 6, 8, 10}|{0, 10}|Genap < 10.
A = {1, 2}, B = {3, 4}. A ∪ B adalah …|{1, 2, 3, 4}|{ }|{1, 4}|{2, 3}|Gabungan.
## MAT|Pertidaksamaan linear satu variabel
Penyelesaian x + 5 > 9 adalah …|x > 4|x < 4|x > 14|x = 4|Kurangi 5.
Penyelesaian 3x ≤ 15 adalah …|x ≤ 5|x ≥ 5|x ≤ 45|x < 12|Bagi 3.
=|Penyelesaian x − 2 < 8 adalah x < …|10|Tambah 2.
=|Jika kedua ruas dikali bilangan negatif, tanda pertidaksamaan harus …|dibalik|Dibalik.
B|Penyelesaian −x > 3 adalah x < −3.|Dibalik.
S|Penyelesaian −3x < 9 adalah x < −3.|x > −3.
Uang Rp50.000 untuk membeli buku Rp8.000 per buah. Paling banyak buku …|6|7|5|8|8x ≤ 50.000.
Tanda ≥ dibaca …|lebih dari atau sama dengan|kurang dari|sama dengan|tidak sama dengan|≥.
## MAT|Operasi pecahan dan desimal
Hasil dari 1/4 + 1/2 adalah …|3/4|2/6|1/6|2/4|Samakan penyebut.
Hasil dari 3/5 × 10/9 adalah …|2/3|30/50|13/14|1/3|30/45 = 2/3.
=|Hasil dari 2 : 1/3 adalah …|6|2 × 3.
=|Hasil dari 0,6 × 0,5 adalah …|0,3|0,6 × 0,5.
B|Membagi dengan pecahan sama dengan mengalikan kebalikannya.|Kebalikan.
S|1/2 + 1/3 = 2/5.|5/6.
Hasil dari 2,4 : 0,6 adalah …|4|0,4|1,44|40|24 : 6.
Setengah resep dari 3/4 kg tepung adalah …|3/8 kg|3/2 kg|1/4 kg|1/2 kg|3/4 × 1/2.
## MAT|Untung, rugi, dan persentase
Untung terjadi jika harga jual … harga beli.|lebih besar dari|lebih kecil dari|sama dengan|setengah dari|Untung.
Beli Rp200.000, jual Rp250.000. Persentase untungnya …|25%|20%|50%|5%|50.000 : 200.000.
=|Beli Rp60.000, jual Rp45.000. Besar ruginya Rp …|15.000;15000|60.000 − 45.000.
=|Jika harga jual sama dengan harga beli, disebut …|impas|Impas.
B|Persentase untung dihitung dari harga beli.|Harga beli.
S|Rugi terjadi jika harga jual lebih besar dari harga beli.|Itu untung.
Pedagang membeli 10 buku seharga Rp30.000 dan menjual Rp4.000 per buku. Untungnya …|Rp10.000|Rp4.000|Rp40.000|Rp7.000|40.000 − 30.000.
Beli Rp80.000, rugi 10%. Harga jualnya …|Rp72.000|Rp88.000|Rp70.000|Rp8.000|80.000 − 8.000.
## MAT|Diskon dan bunga tunggal
Harga Rp200.000 diskon 25%. Harga setelah diskon …|Rp150.000|Rp50.000|Rp175.000|Rp250.000|200.000 − 50.000.
Tabungan Rp2.000.000 berbunga 4% per tahun. Bunga satu tahun …|Rp80.000|Rp8.000|Rp800.000|Rp40.000|4% × 2.000.000.
=|Diskon 10% dari Rp90.000 adalah Rp …|9.000;9000|10% × 90.000.
=|Bunga tunggal dihitung dari modal …|awal|Modal awal.
B|Diskon adalah potongan harga.|Potongan.
S|Harga setelah diskon lebih mahal dari harga awal.|Lebih murah.
Baju Rp120.000 diskon 50%. Harga baju menjadi …|Rp60.000|Rp70.000|Rp50.000|Rp100.000|Setengah harga.
Tabungan Rp500.000 bunga 10% per tahun. Setelah setahun menjadi …|Rp550.000|Rp510.000|Rp600.000|Rp505.000|500.000 + 50.000.
## MAT|Keliling dan luas segiempat
Luas belah ketupat dengan diagonal 10 cm dan 6 cm adalah …|30 cm²|60 cm²|16 cm²|32 cm²|10 × 6 : 2.
Luas layang-layang dengan diagonal 8 cm dan 12 cm adalah …|48 cm²|96 cm²|20 cm²|40 cm²|8 × 12 : 2.
=|Luas trapesium sisi sejajar 6 dan 10 cm, tinggi 5 cm adalah … cm².|40|16 × 5 : 2.
=|Keliling persegi panjang 9 cm × 4 cm adalah … cm.|26|2 × 13.
B|Rumus luas belah ketupat memakai kedua diagonal.|Diagonal.
S|Luas jajargenjang = alas × sisi miring.|Alas × tinggi.
Luas jajargenjang alas 12 cm dan tinggi 7 cm adalah …|84 cm²|19 cm²|42 cm²|38 cm²|12 × 7.
Keliling belah ketupat dengan sisi 5 cm adalah …|20 cm|25 cm|10 cm|15 cm|4 × 5.
## MAT|Jenis dan sifat segitiga
Jumlah ketiga sudut segitiga adalah …|180°|90°|360°|270°|180°.
Segitiga dengan dua sisi sama panjang disebut segitiga …|sama kaki|sama sisi|sembarang|siku-siku|Sama kaki.
=|Besar setiap sudut segitiga sama sisi adalah …|60°;60|180 : 3.
=|Dua sudut segitiga 40° dan 80°. Sudut ketiga …|60°;60|180 − 120.
B|Segitiga tumpul memiliki satu sudut lebih dari 90°.|Tumpul.
S|Segitiga siku-siku memiliki dua sudut 90°.|Satu sudut.
Segitiga yang semua sudutnya kurang dari 90° disebut segitiga …|lancip|tumpul|siku-siku|sembarang|Lancip.
Segitiga siku-siku dengan satu sudut 35°. Sudut yang lain …|55°|65°|45°|35°|180 − 90 − 35.
## MAT|Ukuran pemusatan data
Data yang paling sering muncul disebut …|modus|median|mean|jangkauan|Modus.
Rata-rata dari 4, 6, 8 adalah …|6|18|8|4|18 : 3.
=|Median dari 3, 9, 5, 7, 1 adalah …|5|Urutkan: 1, 3, 5, 7, 9.
=|Modus dari 2, 3, 3, 5, 3, 4 adalah …|3|Muncul tiga kali.
B|Median adalah nilai tengah data yang sudah diurutkan.|Urut.
S|Mean adalah data yang paling sering muncul.|Itu modus.
Median dari 10, 20, 30, 40 adalah …|25|20|30|100|(20 + 30) : 2.
Rata-rata nilai 5 siswa 80. Jumlah nilai mereka …|400|80|85|16|5 × 80.
## MAT|Peluang empirik
Peluang empirik diperoleh dari …|hasil percobaan|tebakan|rumus saja|cerita|Percobaan.
Koin dilempar 40 kali, muncul gambar 18 kali. Peluang empirik gambar …|18/40|18/22|22/40|1/2|18 dari 40.
=|Nilai peluang paling kecil adalah …|0|Nol.
=|Nilai peluang paling besar adalah …|1|Satu.
B|Makin banyak percobaan, peluang empirik makin mendekati peluang teoretis.|Mendekati.
S|Peluang empirik bisa bernilai 2.|Maksimal 1.
Dadu dilempar 30 kali, mata 3 muncul 6 kali. Peluang empiriknya …|1/5|1/6|6/24|3/30|6/30.
Peluang suatu kejadian yang pasti terjadi adalah …|1|0|1/2|100|Pasti.
"""

SAS += """
## MAT 1
0|Hasil dari (−15) + 7 − (−4) adalah ....|−4|4|−26|−18|−8 + 4.
1|Bentuk sederhana dari 4⁵ : 4³ × 4 adalah ....|4³|4²|4⁹|4|4² × 4.
2|Notasi ilmiah dari 0,00072 adalah ....|7,2 × 10⁻⁴|72 × 10⁻⁵|7,2 × 10⁴|0,72 × 10⁻³|7,2 × 10⁻⁴.
3|A = {2, 4, 6, 8} dan B = {4, 8, 12}. A ∩ B adalah ....|{4, 8}|{2, 4, 6, 8, 12}|{12}|{2, 6}|Irisan.
4|Penyelesaian 2x − 3 ≥ 7 adalah ....|x ≥ 5|x ≤ 5|x ≥ 2|x ≥ 10|2x ≥ 10.
5|Hasil dari 3/4 : 3/8 adalah ....|2|9/32|1/2|6|3/4 × 8/3.
## MAT 2
0|Beli Rp125.000, jual Rp150.000. Persentase untungnya ....|20%|25%|15%|10%|25.000 : 125.000.
1|Sepatu Rp300.000 diskon 15%. Harga setelah diskon ....|Rp255.000|Rp285.000|Rp45.000|Rp345.000|300.000 − 45.000.
2|Luas layang-layang dengan diagonal 14 cm dan 9 cm adalah ....|63 cm²|126 cm²|23 cm²|46 cm²|14 × 9 : 2.
3|Sudut-sudut segitiga 2x, 3x, dan 4x. Nilai x adalah ....|20°|30°|40°|10°|9x = 180.
4|Mean dari 7, 8, 8, 9, 10, 12 adalah ....|9|8|8,5|10|54 : 6.
5|Dari 100 kali lemparan, mata dadu genap muncul 52 kali. Peluang empirik muncul mata genap ....|0,52|0,5|0,48|52|52/100.
"""

TOPICS += """
## BIN
# 1|Kebahasaan dan Paragraf
@ Konjungsi temporal
min: 15
act: Tulis pengalaman liburanmu dalam satu paragraf memakai minimal empat konjungsi temporal.
mis: memakai konjungsi sebab-akibat untuk menyatakan urutan waktu
exp: Konjungsi temporal adalah kata hubung yang menyatakan urutan waktu. Contohnya sebelum, sesudah, kemudian, lalu, ketika, sejak, dan akhirnya. Konjungsi temporal banyak dipakai dalam teks narasi, teks prosedur, dan cerita pengalaman supaya urutan kejadian jelas.
ex: Sebelum berangkat, kami berdoa. // Ketika hujan turun, kami berteduh.
pt: Menyatakan urutan waktu ; Contoh sebelum, sesudah, ketika ; Membuat urutan jelas
sum: Konjungsi temporal menata urutan peristiwa.
fig: table Konjungsi | Makna waktu ;; sebelum | lebih dahulu ;; sesudah | setelah kejadian ;; ketika | bersamaan ;; sejak | awal waktu ;; kemudian | urutan berikutnya ;; akhirnya | penutup peristiwa ~ Konjungsi temporal.
@ Penulisan huruf kapital dan tanda baca
min: 15
act: Periksa satu halaman catatanmu, lalu perbaiki penulisan huruf kapital dan tanda bacanya.
mis: menulis nama hari, bulan, dan geografi tanpa huruf kapital
exp: Huruf kapital dipakai pada awal kalimat, nama orang, nama hari, bulan, tahun, nama geografi, nama lembaga, dan judul. Tanda titik dipakai di akhir kalimat berita. Tanda koma dipakai di antara unsur perincian dan setelah kata penghubung antarkalimat. Tanda tanya dipakai di akhir kalimat tanya.
ex: Pada hari Senin, 17 Agustus, kami ke Gunung Gede. // Saya membeli buku, pensil, dan penggaris.
pt: Kapital di awal kalimat dan nama diri ; Koma untuk perincian ; Titik dan tanda tanya di akhir kalimat
sum: Ejaan yang benar membuat tulisan mudah dipahami.
fig: table Contoh | Aturan ejaan ;; Gunung Merapi | kapital nama geografi ;; hari Senin | kapital nama hari ;; Badan Pusat Statistik | kapital nama lembaga ;; buku, pensil, dan penggaris | koma pada perincian ;; Oleh karena itu, | koma setelah konjungsi antarkalimat ;; Siapa namamu? | tanda tanya ~ Aturan huruf kapital dan tanda baca.
@ Paragraf deduktif dan induktif
min: 15
act: Ambil satu paragraf dari buku pelajaran, lalu tentukan letak kalimat utamanya.
mis: menentukan jenis paragraf dari panjangnya, bukan letak kalimat utama
exp: Paragraf deduktif memiliki kalimat utama di awal, lalu diikuti kalimat penjelas. Paragraf induktif memiliki kalimat utama di akhir, didahului kalimat penjelas. Paragraf campuran memiliki kalimat utama di awal dan diulang di akhir. Paragraf induktif sering diakhiri kata jadi atau dengan demikian.
ex: Deduktif: Olahraga bermanfaat bagi tubuh. Olahraga menguatkan otot... // Induktif: ... Jadi, olahraga bermanfaat bagi tubuh.
pt: Deduktif: kalimat utama di awal ; Induktif: kalimat utama di akhir ; Campuran: awal dan akhir
sum: Letak kalimat utama menentukan jenis paragraf.
fig: table Jenis paragraf | Letak kalimat utama ;; deduktif | awal paragraf ;; induktif | akhir paragraf ;; campuran | awal dan akhir ;; deskriptif | tersebar di seluruh paragraf ;; penanda induktif | kata jadi ;; penanda simpulan | dengan demikian ~ Jenis paragraf berdasarkan letak kalimat utama.
@ Sinopsis cerita
min: 15
act: Baca satu cerita pendek, lalu tulis sinopsisnya dalam satu paragraf.
mis: menulis sinopsis dengan mengubah alur cerita
exp: Sinopsis adalah ringkasan cerita yang memuat tokoh utama dan rangkaian peristiwa penting sesuai urutan alur. Sinopsis ditulis dengan bahasa sendiri, singkat, dan tidak mengubah isi cerita. Langkahnya membaca cerita, mencatat peristiwa penting, lalu menyusunnya menjadi ringkasan.
ex: Sinopsis Malin Kundang memuat kepergian Malin, kesuksesannya, dan kutukan ibunya. // Sinopsis tidak menambahkan pendapat penulis.
pt: Ringkasan cerita ; Memuat tokoh dan peristiwa penting ; Tidak mengubah isi
sum: Sinopsis menyajikan inti cerita secara singkat.
fig: table Langkah | Kegiatan ;; pertama | membaca seluruh cerita ;; kedua | mencatat tokoh utama ;; ketiga | mencatat peristiwa penting ;; keempat | mengurutkan sesuai alur ;; kelima | menulis dengan bahasa sendiri ;; keenam | memeriksa kesesuaian isi ~ Langkah menulis sinopsis.
@ Dialog dalam cerita fantasi
min: 15
act: Tulis percakapan antara dua tokoh ajaib dalam cerita fantasi buatanmu.
mis: menulis dialog tanpa tanda petik dan tanpa keterangan penutur
exp: Dialog dalam cerita fantasi memperlihatkan watak tokoh dan menghidupkan cerita. Dialog ditulis dengan tanda petik dan disertai keterangan penutur, misalnya kata si naga. Huruf pertama petikan ditulis kapital. Tanda koma memisahkan petikan dari keterangan penutur.
ex: "Ayo kita terbang ke bulan!" ajak si naga. // Peri berkata, "Hati-hati dengan sihirku."
pt: Dialog memperlihatkan watak ; Ditulis dengan tanda petik ; Ada keterangan penutur
sum: Dialog membuat cerita fantasi lebih hidup.
fig: table Unsur penulisan dialog | Aturan ;; tanda petik | mengapit ucapan ;; huruf kapital | awal petikan ;; tanda koma | memisahkan petikan dan penutur ;; keterangan penutur | menjelaskan siapa berbicara ;; tanda seru | petikan bernada perintah ;; tanda tanya | petikan bernada tanya ~ Aturan penulisan dialog.
@ Membaca buku fiksi dan nonfiksi
min: 15
act: Baca satu buku fiksi dan satu buku nonfiksi bulan ini, lalu buat jurnal membaca.
mis: membaca buku nonfiksi tanpa mencatat informasi penting
exp: Kegiatan literasi membiasakan kita membaca buku fiksi dan nonfiksi. Saat membaca fiksi, perhatikan tokoh, latar, alur, dan amanat. Saat membaca nonfiksi, catat gagasan utama dan informasi penting. Jurnal membaca membantu mengingat isi buku.
ex: Jurnal membaca memuat judul, pengarang, dan kesan. // Peta pikiran membantu meringkas buku nonfiksi.
pt: Fiksi: tokoh, latar, alur, amanat ; Nonfiksi: gagasan utama dan informasi ; Catat dalam jurnal membaca
sum: Membaca rutin memperluas wawasan.
fig: table Isi jurnal membaca | Contoh ;; judul buku | Laskar Pelangi ;; pengarang | nama penulis ;; jenis buku | fiksi atau nonfiksi ;; ringkasan | inti isi buku ;; kutipan menarik | kalimat favorit ;; kesan | perasaan setelah membaca ~ Isi jurnal membaca.
# 2|Puisi Lama, Prosedur, dan Media
@ Syair
min: 15
act: Baca satu bait syair dengan irama, lalu tentukan sajak dan isinya.
mis: mengira syair memiliki sampiran seperti pantun
exp: Syair adalah puisi lama yang setiap baitnya terdiri atas empat baris dengan sajak a-a-a-a. Semua baris dalam syair adalah isi, tidak ada sampiran. Syair biasanya berisi cerita, nasihat, atau ajaran agama. Syair terkenal antara lain Syair Ken Tambuhan dan Syair Abdul Muluk.
ex: Setiap baris syair berakhir dengan bunyi sama. // Syair dapat berisi kisah panjang.
pt: Empat baris sebait ; Sajak a-a-a-a ; Semua baris isi
sum: Syair adalah puisi lama tanpa sampiran.
fig: table Ciri | Syair ;; jumlah baris | empat ;; sajak | a-a-a-a ;; sampiran | tidak ada ;; isi | semua baris ;; tema | cerita atau nasihat ;; contoh judul | Syair Ken Tambuhan ~ Ciri-ciri syair.
@ Karmina dan talibun
min: 15
act: Buat satu karmina lucu dan bacakan di depan keluarga.
mis: menulis karmina lebih dari dua baris
exp: Karmina atau pantun kilat terdiri atas dua baris dengan sajak a-a. Baris pertama sampiran dan baris kedua isi. Talibun adalah pantun yang jumlah barisnya genap lebih dari empat, misalnya enam, delapan, atau sepuluh baris, dengan separuh awal sampiran dan separuh akhir isi.
ex: Karmina: Dahulu parang sekarang besi, / dahulu sayang sekarang benci. // Talibun enam baris: tiga sampiran, tiga isi.
pt: Karmina dua baris ; Talibun lebih dari empat baris ; Ada sampiran dan isi
sum: Karmina dan talibun adalah variasi pantun.
fig: table Puisi lama | Jumlah baris ;; karmina | dua ;; pantun | empat ;; syair | empat tanpa sampiran ;; gurindam | dua berisi sebab akibat ;; talibun | enam atau lebih ;; seloka | berkait antarbait ~ Puisi lama dan jumlah barisnya.
@ Kata kerja imperatif
min: 15
act: Tulis petunjuk membuat minuman favoritmu dengan kata kerja imperatif.
mis: menulis langkah prosedur dengan kalimat berita
exp: Kata kerja imperatif adalah kata kerja perintah yang menyuruh pembaca melakukan sesuatu. Kata kerja ini banyak dipakai dalam teks prosedur, misalnya campurkan, aduk, tuangkan, dan panaskan. Akhiran -kan dan -lah sering muncul pada kata kerja imperatif.
ex: Tuangkan air panas ke dalam gelas. // Aduklah hingga rata.
pt: Kata kerja perintah ; Banyak dalam teks prosedur ; Sering berakhiran -kan atau -lah
sum: Kata kerja imperatif memberi petunjuk yang jelas.
fig: table Kata kerja imperatif | Kegunaan ;; tuangkan | memasukkan cairan ;; aduk | mencampur rata ;; panaskan | memberi panas ;; potong | membagi bahan ;; tekan | memberi tekanan pada tombol ;; simpan | menaruh untuk nanti ~ Contoh kata kerja imperatif.
@ Ulasan buku
min: 15
act: Tulis ulasan buku favoritmu lengkap dengan kelebihan dan kekurangannya.
mis: menulis ulasan hanya berisi pujian tanpa alasan
exp: Ulasan adalah tulisan yang berisi penilaian terhadap sebuah karya, misalnya buku atau film. Struktur ulasan terdiri atas identitas karya, orientasi, tafsiran isi, evaluasi berisi kelebihan dan kekurangan, serta rangkuman. Penilaian harus objektif dan disertai alasan.
ex: Kelebihan: alurnya menegangkan. // Kekurangan: ada bagian yang terlalu panjang.
pt: Penilaian terhadap karya ; Ada evaluasi kelebihan dan kekurangan ; Objektif dan beralasan
sum: Ulasan membantu pembaca menilai sebuah karya.
fig: table Struktur ulasan | Isi ;; identitas | judul, pengarang, penerbit ;; orientasi | gambaran umum karya ;; tafsiran isi | pendapat tentang isi ;; evaluasi | kelebihan dan kekurangan ;; rangkuman | simpulan dan rekomendasi ;; rekomendasi | saran bagi pembaca ~ Struktur ulasan.
@ Teks wawancara
min: 15
act: Wawancarai pedagang di dekat rumah, lalu tulis hasilnya dalam bentuk teks wawancara.
mis: mengubah jawaban narasumber sesuai keinginan sendiri
exp: Teks wawancara memuat tanya jawab antara pewawancara dan narasumber. Strukturnya terdiri atas pembuka, isi berupa pertanyaan dan jawaban, serta penutup. Hasil wawancara dapat ditulis dalam bentuk dialog atau diubah menjadi teks laporan. Jawaban narasumber harus ditulis sesuai aslinya.
ex: Pembuka: salam dan perkenalan. // Penutup: ucapan terima kasih.
pt: Tanya jawab dua pihak ; Pembuka, isi, penutup ; Jawaban ditulis sesuai aslinya
sum: Teks wawancara menyajikan informasi dari narasumber.
fig: table Bagian | Isi ;; pembuka | salam dan perkenalan ;; tujuan | maksud wawancara ;; isi | pertanyaan dan jawaban ;; penutup | ucapan terima kasih ;; narasumber | orang yang memberi informasi ;; pewawancara | orang yang bertanya ~ Struktur teks wawancara.
@ Iklan, slogan, dan poster
min: 15
act: Rancang poster ajakan menjaga kebersihan sekolah dengan slogan yang menarik.
mis: membuat slogan panjang dan sulit diingat
exp: Iklan adalah pesan untuk memperkenalkan atau mengajak. Slogan adalah kalimat pendek, menarik, dan mudah diingat. Poster adalah karya grafis yang memadukan gambar dan tulisan singkat. Iklan dan poster memakai bahasa yang persuasif dan sering memanfaatkan rima.
ex: Slogan: Sekolah bersih, belajar jadi asyik. // Poster memakai gambar besar dan huruf jelas.
pt: Iklan memperkenalkan atau mengajak ; Slogan pendek dan mudah diingat ; Poster memadukan gambar dan tulisan
sum: Iklan, slogan, dan poster menyampaikan pesan dengan menarik.
fig: table Media | Ciri ;; iklan | memperkenalkan atau mengajak ;; slogan | kalimat pendek mudah diingat ;; poster | gambar dan tulisan singkat ;; spanduk | kain berisi pesan ;; brosur | lembaran berisi informasi ;; baliho | papan reklame besar ~ Media iklan dan cirinya.
"""

BANK += """
## BIN|Konjungsi temporal
Konjungsi temporal menyatakan hubungan …|waktu|sebab|syarat|tujuan|Waktu.
Contoh konjungsi temporal adalah …|sesudah|karena|agar|tetapi|Sesudah.
=|… makan, kita mencuci tangan. Konjungsi yang tepat adalah …|Sebelum|Sebelum.
=|Konjungsi temporal yang menyatakan penutup peristiwa adalah …|akhirnya|Akhirnya.
B|Ketika termasuk konjungsi temporal.|Temporal.
S|Karena termasuk konjungsi temporal.|Kausal.
Teks yang banyak memakai konjungsi temporal adalah teks …|narasi|iklan|puisi|slogan|Narasi.
Kami belajar di perpustakaan … pukul tujuh pagi. Konjungsi yang tepat adalah …|sejak|agar|namun|walaupun|Sejak.
## BIN|Penulisan huruf kapital dan tanda baca
Penulisan nama geografi yang benar adalah …|Gunung Rinjani|gunung rinjani|Gunung rinjani|gunung Rinjani|Kapital.
Tanda baca di antara unsur perincian adalah …|koma|titik|titik dua|tanda seru|Koma.
=|Kalimat tanya diakhiri dengan tanda …|tanya|Tanda tanya.
=|Nama bulan ditulis dengan huruf … di awal.|kapital|Kapital.
B|Nama lembaga ditulis dengan huruf kapital pada setiap unsur utamanya.|Lembaga.
S|Nama hari boleh ditulis dengan huruf kecil.|Kapital.
Kalimat dengan tanda baca yang benar adalah …|Ibu membeli apel, jeruk, dan mangga.|Ibu membeli apel jeruk, dan mangga.|Ibu, membeli apel jeruk dan mangga|ibu membeli apel, jeruk, dan mangga.|Benar.
Setelah konjungsi oleh karena itu di awal kalimat ditulis tanda …|koma|titik|tanya|seru|Koma.
## BIN|Paragraf deduktif dan induktif
Paragraf yang kalimat utamanya di awal disebut paragraf …|deduktif|induktif|campuran|naratif|Deduktif.
Paragraf yang kalimat utamanya di akhir disebut paragraf …|induktif|deduktif|campuran|deskriptif|Induktif.
=|Paragraf yang kalimat utamanya di awal dan akhir disebut paragraf …|campuran|Campuran.
=|Paragraf induktif sering diakhiri dengan kata …|jadi|Jadi.
B|Jenis paragraf ditentukan oleh letak kalimat utama.|Letak.
S|Paragraf deduktif diakhiri dengan kalimat utama.|Di awal.
Kalimat yang mendukung kalimat utama disebut kalimat …|penjelas|utama|tanya|perintah|Penjelas.
Kata penanda simpulan di akhir paragraf adalah …|dengan demikian|sebelum itu|misalnya|selain itu|Simpulan.
## BIN|Sinopsis cerita
Sinopsis adalah … cerita.|ringkasan|judul|salinan lengkap|kritik|Ringkasan.
Sinopsis memuat tokoh utama dan peristiwa …|penting|kecil-kecil|tambahan|baru|Penting.
=|Sinopsis ditulis dengan bahasa …|sendiri|Sendiri.
=|Peristiwa dalam sinopsis disusun sesuai urutan …|alur|Alur.
B|Sinopsis tidak boleh mengubah isi cerita.|Sesuai.
S|Sinopsis boleh menambahkan peristiwa baru agar menarik.|Tidak boleh.
Langkah pertama menulis sinopsis adalah …|membaca seluruh cerita|menulis kesimpulan|menebak isi|mengganti judul|Membaca.
Sinopsis sebaiknya ditulis …|singkat|sangat panjang|tanpa tokoh|tanpa urutan|Singkat.
## BIN|Dialog dalam cerita fantasi
Dialog dalam cerita ditulis dengan tanda …|petik|kurung|titik dua|garis miring|Petik.
Fungsi dialog dalam cerita adalah …|memperlihatkan watak tokoh|mengganti judul|menghapus latar|memperpanjang halaman saja|Watak.
=|Huruf pertama petikan langsung ditulis …|kapital|Kapital.
=|Petikan dan keterangan penutur dipisahkan tanda …|koma|Koma.
B|Kata si naga dalam dialog adalah keterangan penutur.|Penutur.
S|Dialog tidak perlu memakai tanda petik.|Perlu.
Penulisan dialog yang benar adalah …|"Ayo pulang," ajak Peri.|"ayo pulang" ajak Peri.|Ayo pulang, ajak Peri.|"Ayo pulang." Ajak Peri|Benar.
Petikan yang bernada perintah diakhiri tanda …|seru|tanya|titik koma|kurung|Seru.
## BIN|Membaca buku fiksi dan nonfiksi
Saat membaca buku fiksi, kita memperhatikan …|tokoh, latar, alur, dan amanat|daftar pustaka saja|harga buku|nomor halaman|Unsur fiksi.
Saat membaca buku nonfiksi, kita mencatat …|gagasan utama dan informasi penting|nama tokoh khayalan|alur cerita|konflik tokoh|Nonfiksi.
=|Catatan kegiatan membaca disebut jurnal …|membaca|Jurnal membaca.
=|Kalimat favorit dari buku disebut kutipan …|menarik|Kutipan.
B|Peta pikiran membantu meringkas buku nonfiksi.|Peta pikiran.
S|Kegiatan literasi hanya membaca buku fiksi.|Fiksi dan nonfiksi.
Bagian jurnal membaca yang berisi perasaan setelah membaca adalah …|kesan|judul|pengarang|jenis buku|Kesan.
Manfaat membaca rutin adalah …|memperluas wawasan|membuat malas|mengurangi kosakata|membuat bosan|Wawasan.
## BIN|Syair
Satu bait syair terdiri atas … baris.|empat|dua|enam|tiga|Empat.
Sajak syair adalah …|a-a-a-a|a-b-a-b|a-a|a-b-b-a|A-a-a-a.
=|Dalam syair, semua baris merupakan …|isi|Isi.
=|Syair tidak memiliki …|sampiran|Sampiran.
B|Syair dapat berisi cerita.|Cerita.
S|Syair memiliki sampiran seperti pantun.|Tidak.
Contoh judul syair adalah …|Syair Ken Tambuhan|Malin Kundang|Sangkuriang|Si Kancil|Syair.
Perbedaan syair dan pantun adalah syair …|tidak memiliki sampiran|bersajak a-b-a-b|terdiri atas dua baris|berisi teka-teki|Tanpa sampiran.
## BIN|Karmina dan talibun
Karmina disebut juga pantun …|kilat|berkait|panjang|jenaka|Kilat.
Karmina terdiri atas … baris.|dua|empat|enam|delapan|Dua.
=|Sajak karmina adalah …|a-a;aa|A-a.
=|Pantun dengan jumlah baris genap lebih dari empat disebut …|talibun|Talibun.
B|Talibun enam baris memiliki tiga baris sampiran.|Separuh awal.
S|Karmina terdiri atas enam baris.|Dua baris.
Puisi lama yang berkait antarbait disebut …|seloka|karmina|syair|gurindam|Seloka.
Pada karmina, baris kedua berisi …|isi|sampiran|judul|nama pengarang|Isi.
## BIN|Kata kerja imperatif
Kata kerja imperatif adalah kata kerja …|perintah|lampau|sifat|tanya|Perintah.
Teks yang banyak memakai kata kerja imperatif adalah teks …|prosedur|narasi|puisi|biografi|Prosedur.
=|Kata kerja imperatif untuk mencampur rata adalah …|aduk;aduklah|Aduk.
=|Akhiran yang sering ada pada kata kerja imperatif adalah -kan dan …|-lah;lah|-lah.
B|Tuangkan termasuk kata kerja imperatif.|Perintah.
S|Langkah prosedur sebaiknya ditulis dengan kalimat tanya.|Kalimat perintah.
Kalimat imperatif yang benar adalah …|Panaskan air hingga mendidih.|Air sedang mendidih.|Apakah air mendidih?|Air itu panas sekali!|Perintah.
Kata kerja imperatif untuk menaruh barang untuk nanti adalah …|simpan|tekan|potong|aduk|Simpan.
## BIN|Ulasan buku
Ulasan adalah tulisan yang berisi … terhadap karya.|penilaian|salinan|terjemahan|daftar isi|Penilaian.
Bagian ulasan yang berisi kelebihan dan kekurangan adalah …|evaluasi|identitas|orientasi|judul|Evaluasi.
=|Bagian ulasan yang berisi gambaran umum karya disebut …|orientasi|Orientasi.
=|Bagian akhir ulasan berisi simpulan disebut …|rangkuman|Rangkuman.
B|Penilaian dalam ulasan harus disertai alasan.|Beralasan.
S|Ulasan hanya boleh berisi pujian.|Objektif.
Judul, pengarang, dan penerbit termasuk bagian …|identitas|evaluasi|rangkuman|tafsiran isi|Identitas.
Ulasan yang baik bersifat …|objektif|berbohong|menghina|asal-asalan|Objektif.
## BIN|Teks wawancara
Orang yang memberi informasi dalam wawancara disebut …|narasumber|pewawancara|notulis|penonton|Narasumber.
Bagian pembuka wawancara berisi …|salam dan perkenalan|ucapan terima kasih|kesimpulan|daftar pustaka|Pembuka.
=|Bagian penutup wawancara berisi ucapan terima …|kasih|Terima kasih.
=|Orang yang mengajukan pertanyaan disebut …|pewawancara|Pewawancara.
B|Jawaban narasumber ditulis sesuai aslinya.|Sesuai.
S|Pewawancara boleh mengubah jawaban narasumber.|Tidak boleh.
Hasil wawancara dapat diubah menjadi teks …|laporan|puisi|pantun|lagu|Laporan.
Bagian isi teks wawancara berupa …|pertanyaan dan jawaban|salam saja|judul|tanda tangan|Isi.
## BIN|Iklan, slogan, dan poster
Slogan adalah kalimat yang …|pendek dan mudah diingat|panjang dan rumit|berisi angka saja|tanpa makna|Slogan.
Poster memadukan …|gambar dan tulisan singkat|angka dan tabel|cerita panjang|rumus|Poster.
=|Bahasa iklan bersifat …|persuasif;membujuk|Persuasif.
=|Kain yang dibentangkan berisi pesan disebut …|spanduk|Spanduk.
B|Iklan dapat memanfaatkan rima agar menarik.|Rima.
S|Slogan yang baik terdiri atas beberapa paragraf.|Pendek.
Lembaran berisi informasi produk yang dibagikan disebut …|brosur|baliho|spanduk|slogan|Brosur.
Papan reklame besar di pinggir jalan disebut …|baliho|brosur|pamflet kecil|kartu nama|Baliho.
"""

SAS += """
## BIN 1
0|Kalimat yang memakai konjungsi temporal adalah ....|Sesudah belajar, Rina tidur.|Rina tidur karena lelah.|Rina belajar agar pintar.|Rina pintar tetapi malas.|Temporal.
1|Penulisan yang sesuai ejaan adalah ....|Kami berlibur ke Danau Toba.|Kami berlibur ke danau toba.|kami berlibur ke Danau toba.|Kami Berlibur Ke Danau Toba.|Benar.
2|Paragraf yang diakhiri kalimat Jadi, menabung sangat bermanfaat termasuk paragraf ....|induktif|deduktif|campuran|naratif|Induktif.
3|Sinopsis yang baik tidak boleh ....|mengubah isi cerita|menyebut tokoh utama|memuat peristiwa penting|ditulis singkat|Tidak boleh.
4|Dalam dialog, kata ajak si naga berfungsi sebagai ....|keterangan penutur|petikan|judul|latar|Penutur.
5|Bagian jurnal membaca yang berisi nama penulis adalah ....|pengarang|kesan|ringkasan|kutipan|Pengarang.
## BIN 2
0|Puisi lama empat baris yang semua barisnya berisi isi adalah ....|syair|pantun|karmina|talibun|Syair.
1|Pantun kilat terdiri atas ....|dua baris|empat baris|enam baris|delapan baris|Dua.
2|Kata kerja imperatif yang tepat untuk menghidupkan alat adalah ....|tekan tombolnya|tombol ditekan|tombol itu|menekan-nekan|Imperatif.
3|Tafsiran isi dalam ulasan berisi ....|pendapat tentang isi karya|daftar harga|nama penerbit|ucapan terima kasih|Tafsiran.
4|Tujuan wawancara disampaikan pada bagian ....|pembuka|penutup|kesimpulan|lampiran|Pembuka.
5|Ciri slogan yang baik adalah ....|singkat dan menarik|panjang dan rumit|tanpa pesan|memakai bahasa asing|Singkat.
"""

TOPICS += """
## IPA
# 1|Pengukuran, Zat, dan Gerak
@ Alat ukur dan ketelitian
min: 15
act: Ukur panjang pensil dengan penggaris dan diameter koin dengan jangka sorong bila tersedia.
mis: membaca skala dari sudut miring sehingga hasil keliru
exp: Pengukuran membandingkan suatu besaran dengan satuannya. Alat ukur panjang antara lain penggaris dengan ketelitian 1 mm, jangka sorong 0,1 mm, dan mikrometer sekrup 0,01 mm. Massa diukur dengan neraca, waktu dengan stopwatch, dan suhu dengan termometer. Mata harus tegak lurus terhadap skala saat membaca.
ex: Tebal kertas diukur dengan mikrometer sekrup. // Diameter dalam gelas diukur dengan jangka sorong.
pt: Mengukur berarti membandingkan dengan satuan ; Alat ukur punya ketelitian berbeda ; Mata tegak lurus skala
sum: Pilih alat ukur sesuai ketelitian yang dibutuhkan.
fig: table Alat ukur | Ketelitian atau kegunaan ;; penggaris | 1 mm ;; jangka sorong | 0,1 mm ;; mikrometer sekrup | 0,01 mm ;; neraca | mengukur massa ;; stopwatch | mengukur waktu ;; termometer | mengukur suhu ~ Alat ukur dan kegunaannya.
@ Massa jenis
min: 15
act: Masukkan telur ke air tawar lalu ke air garam pekat, dan amati perbedaannya.
mis: mengira benda berat pasti tenggelam
exp: Massa jenis adalah massa benda dibagi volumenya, dirumuskan ρ = m : V. Satuannya kg/m³ atau g/cm³. Massa jenis air sekitar 1 g/cm³. Benda yang massa jenisnya lebih kecil dari air akan mengapung, sedangkan yang lebih besar akan tenggelam.
ex: Kayu mengapung karena massa jenisnya kurang dari air. // Besi tenggelam karena massa jenisnya lebih besar.
pt: ρ = m : V ; Massa jenis air 1 g/cm³ ; Lebih kecil dari air mengapung
sum: Massa jenis menentukan benda mengapung atau tenggelam.
fig: table Benda | Massa jenis ;; air | 1 g/cm³ ;; es | 0,92 g/cm³ ;; kayu jati | 0,7 g/cm³ ;; besi | 7,9 g/cm³ ;; aluminium | 2,7 g/cm³ ;; minyak goreng | 0,9 g/cm³ ~ Massa jenis beberapa benda.
@ Asam, basa, dan garam
min: 15
act: Uji cuka, air sabun, dan air garam dengan kertas lakmus atau air kunyit.
mis: mengira semua zat asam berbahaya dan tidak bisa dimakan
exp: Asam memiliki rasa masam dan pH kurang dari 7, misalnya cuka dan jeruk. Basa terasa pahit, licin, dan pH lebih dari 7, misalnya sabun dan pasta gigi. Garam terbentuk dari reaksi asam dan basa dan bersifat netral dengan pH 7. Lakmus merah berubah biru dalam basa, lakmus biru berubah merah dalam asam.
ex: Air jeruk bersifat asam. // Sabun bersifat basa.
pt: Asam pH < 7 ; Basa pH > 7 ; Garam netral pH 7
sum: Indikator membantu mengenali asam dan basa.
fig: table Zat | Sifat ;; cuka | asam ;; air jeruk | asam lemah ;; sabun | basa ;; pasta gigi | basa lemah ;; air murni | netral ;; air garam dapur | netral dari garam ~ Sifat zat di sekitar kita.
@ Indikator alami
min: 15
act: Buat indikator dari kol ungu, lalu uji perubahan warnanya pada cuka dan air sabun.
mis: mengira semua tumbuhan berwarna bisa menjadi indikator
exp: Indikator alami adalah bahan dari tumbuhan yang berubah warna dalam larutan asam atau basa. Contohnya kol ungu, kunyit, bunga sepatu, dan bunga mawar merah. Ekstrak kol ungu berwarna merah dalam asam dan hijau atau kuning dalam basa. Kunyit berubah merah kecokelatan dalam basa.
ex: Air kunyit menjadi merah kecokelatan saat ditetesi air sabun. // Ekstrak kol ungu memerah dalam cuka.
pt: Indikator berubah warna ; Dari kol ungu, kunyit, bunga sepatu ; Menunjukkan asam atau basa
sum: Tumbuhan tertentu dapat menunjukkan sifat asam basa.
fig: table Indikator alami | Warna dalam basa ;; kol ungu | hijau ;; kunyit | merah kecokelatan ;; bunga sepatu | hijau kekuningan ;; bunga mawar merah | hijau tua ;; kulit manggis | biru keunguan ;; bunga telang | hijau kebiruan ~ Indikator alami dan perubahan warnanya.
@ Gerak lurus
min: 15
act: Ukur waktu tempuh bola menggelinding sejauh 2 meter, lalu hitung kecepatannya.
mis: mengira kecepatan dan percepatan sama artinya
exp: Gerak lurus beraturan atau GLB adalah gerak lurus dengan kecepatan tetap. Gerak lurus berubah beraturan atau GLBB adalah gerak lurus dengan kecepatan yang berubah secara teratur, bisa dipercepat atau diperlambat. Kecepatan = jarak : waktu. Percepatan adalah perubahan kecepatan setiap waktu.
ex: Mobil melaju tetap 60 km/jam di jalan tol (GLB). // Bola menggelinding menuruni bukit makin cepat (GLBB dipercepat).
pt: GLB kecepatan tetap ; GLBB kecepatan berubah teratur ; Percepatan perubahan kecepatan
sum: Gerak lurus dibedakan dari perubahan kecepatannya.
fig: table Peristiwa | Jenis gerak ;; mobil di tol dengan kecepatan tetap | GLB ;; bola jatuh bebas | GLBB dipercepat ;; sepeda direm | GLBB diperlambat ;; kereta melaju tetap | GLB kereta ;; bola dilempar ke atas | GLBB diperlambat saat naik ;; benda menuruni bidang miring | GLBB dipercepat di bidang miring ~ Contoh gerak lurus.
@ Gaya dan hukum Newton
min: 15
act: Dorong troli kosong dan troli berisi barang dengan tenaga sama, lalu bandingkan geraknya.
mis: mengira benda diam tidak dipengaruhi gaya apa pun
exp: Hukum I Newton menyatakan benda cenderung mempertahankan keadaannya jika tidak ada gaya, disebut kelembaman. Hukum II Newton menyatakan percepatan sebanding dengan gaya dan berbanding terbalik dengan massa, F = m × a. Hukum III Newton menyatakan setiap aksi menimbulkan reaksi yang sama besar dan berlawanan arah.
ex: Penumpang terdorong ke depan saat bus mengerem (Hukum I). // Roket meluncur karena gas disemburkan ke bawah (Hukum III).
pt: Hukum I kelembaman ; Hukum II F = m × a ; Hukum III aksi reaksi
sum: Hukum Newton menjelaskan hubungan gaya dan gerak.
fig: table Peristiwa | Hukum Newton ;; penumpang terdorong saat bus mengerem | Hukum I ;; troli ringan lebih cepat bergerak | Hukum II ;; roket menyemburkan gas | Hukum III ;; taplak ditarik cepat gelas tetap | Hukum I kelembaman ;; menendang bola lebih keras bola lebih cepat | Hukum II gaya ;; perenang mendorong dinding kolam | Hukum III aksi reaksi ~ Contoh hukum Newton.
# 2|Kehidupan, Lingkungan, dan Bumi
@ Mikroskop
min: 15
act: Amati irisan tipis bawang merah di mikroskop sekolah atau lewat gambar mikroskop digital.
mis: langsung memakai lensa perbesaran terbesar
exp: Mikroskop adalah alat untuk melihat benda yang sangat kecil. Bagian mikroskop antara lain lensa okuler di dekat mata, lensa objektif di dekat benda, meja preparat, cermin atau lampu, serta makrometer dan mikrometer untuk mengatur fokus. Perbesaran total = perbesaran okuler × perbesaran objektif.
ex: Okuler 10× dan objektif 40× menghasilkan perbesaran 400×. // Mulai pengamatan dari perbesaran terkecil.
pt: Melihat benda sangat kecil ; Lensa okuler dan objektif ; Perbesaran = okuler × objektif
sum: Mikroskop membantu mengamati sel.
fig: table Bagian mikroskop | Fungsi ;; lensa okuler | dekat mata pengamat ;; lensa objektif | dekat benda ;; meja preparat | tempat kaca benda ;; makrometer | fokus kasar ;; mikrometer | fokus halus ;; cermin | memantulkan cahaya ~ Bagian mikroskop.
@ Tingkat organisasi kehidupan
min: 15
act: Buat diagram tingkatan dari sel sampai organisme memakai contoh tubuh manusia.
mis: menganggap jaringan lebih besar dari organ
exp: Makhluk hidup tersusun secara bertingkat. Sel adalah unit terkecil. Kumpulan sel yang sama membentuk jaringan. Beberapa jaringan membentuk organ. Beberapa organ bekerja sama membentuk sistem organ. Sistem-sistem organ membentuk organisme.
ex: Sel otot membentuk jaringan otot. // Lambung adalah organ dalam sistem pencernaan.
pt: Sel unit terkecil ; Sel, jaringan, organ ; Sistem organ dan organisme
sum: Kehidupan tersusun dari sel sampai organisme.
fig: table Tingkat | Contoh ;; sel | sel darah merah ;; jaringan | jaringan otot ;; organ | jantung ;; sistem organ | sistem peredaran darah ;; organisme | manusia ;; populasi | sekelompok rusa sejenis ~ Tingkat organisasi kehidupan.
@ Pencemaran lingkungan
min: 15
act: Amati sungai atau saluran air dekat rumah, lalu catat tanda-tanda pencemarannya.
mis: mengira pencemaran hanya disebabkan oleh pabrik
exp: Pencemaran lingkungan adalah masuknya zat atau energi yang merugikan ke lingkungan. Pencemaran air disebabkan limbah rumah tangga, pabrik, dan sampah. Pencemaran udara disebabkan asap kendaraan dan pembakaran. Pencemaran tanah disebabkan sampah plastik dan pestisida berlebihan.
ex: Deterjen berlebih membuat air sungai berbusa. // Asap kendaraan menyebabkan polusi udara.
pt: Zat merugikan masuk lingkungan ; Pencemaran air, udara, tanah ; Penyebab dari kegiatan manusia
sum: Mencegah pencemaran menjaga kesehatan bumi.
fig: table Pencemaran | Penyebab ;; air | limbah deterjen ;; udara | asap kendaraan ;; tanah | sampah plastik ;; suara | bunyi bising mesin ;; cahaya | lampu berlebihan di malam hari ;; laut | tumpahan minyak ~ Jenis pencemaran dan penyebabnya.
@ Struktur bumi dan lempeng tektonik
min: 15
act: Lihat peta lempeng dunia, lalu tandai pertemuan lempeng di sekitar Indonesia.
mis: mengira permukaan bumi diam tidak bergerak
exp: Kulit bumi atau litosfer terpecah menjadi lempeng-lempeng tektonik yang bergerak perlahan di atas astenosfer. Indonesia berada di pertemuan tiga lempeng besar, yaitu Lempeng Indo-Australia, Lempeng Eurasia, dan Lempeng Pasifik. Pergerakan lempeng menyebabkan gempa bumi dan gunung api.
ex: Pertemuan lempeng di selatan Jawa membentuk deretan gunung api. // Lempeng bergerak beberapa sentimeter per tahun.
pt: Kulit bumi terdiri atas lempeng ; Indonesia di pertemuan tiga lempeng ; Menyebabkan gempa dan gunung api
sum: Gerak lempeng membentuk permukaan bumi.
fig: table Istilah | Arti ;; litosfer | kulit bumi padat ;; astenosfer | lapisan lunak di bawah litosfer ;; Lempeng Eurasia | lempeng di utara Indonesia ;; Lempeng Indo-Australia | lempeng di selatan Indonesia ;; Lempeng Pasifik | lempeng di timur Indonesia ;; Cincin Api Pasifik | jalur gunung api ~ Struktur bumi dan lempeng.
@ Atmosfer bumi
min: 15
act: Cari tahu ketinggian pesawat terbang, lalu tentukan lapisan atmosfer tempatnya melintas.
mis: mengira atmosfer hanya satu lapisan udara
exp: Atmosfer adalah lapisan udara yang menyelimuti bumi. Lapisannya dari bawah adalah troposfer, stratosfer, mesosfer, termosfer, dan eksosfer. Cuaca terjadi di troposfer. Lapisan ozon di stratosfer melindungi bumi dari sinar ultraviolet. Meteor terbakar di mesosfer.
ex: Hujan terjadi di troposfer. // Ozon menyerap sinar ultraviolet.
pt: Lapisan udara penyelimut bumi ; Troposfer tempat cuaca ; Ozon di stratosfer
sum: Atmosfer melindungi kehidupan di bumi.
fig: table Lapisan | Ciri ;; troposfer | tempat terjadinya cuaca ;; stratosfer | lapisan ozon ;; mesosfer | meteor terbakar ;; termosfer | suhu sangat tinggi ;; eksosfer | lapisan terluar ;; ozon | menyerap sinar ultraviolet ~ Lapisan atmosfer.
@ Energi dan perubahannya
min: 15
act: Amati lima alat di rumah, lalu tulis perubahan energi yang terjadi pada setiap alat.
mis: mengira energi dapat habis atau hilang
exp: Energi adalah kemampuan untuk melakukan usaha. Bentuk energi antara lain energi kinetik, potensial, listrik, kimia, panas, cahaya, dan bunyi. Hukum kekekalan energi menyatakan energi tidak dapat diciptakan atau dimusnahkan, tetapi dapat berubah bentuk.
ex: Kipas angin mengubah energi listrik menjadi gerak. // Baterai mengubah energi kimia menjadi listrik.
pt: Energi kemampuan melakukan usaha ; Banyak bentuk energi ; Energi berubah bentuk, tidak hilang
sum: Energi selalu berubah bentuk.
fig: table Alat | Perubahan energi ;; kipas angin | listrik menjadi gerak ;; lampu | listrik menjadi cahaya ;; setrika | listrik menjadi panas ;; baterai | kimia menjadi listrik ;; panel surya | cahaya menjadi listrik ;; pengeras suara | listrik menjadi bunyi ~ Perubahan energi pada alat.
"""

BANK += """
## IPA|Alat ukur dan ketelitian
Ketelitian jangka sorong adalah …|0,1 mm|1 mm|0,01 mm|1 cm|Jangka sorong.
Alat yang tepat untuk mengukur tebal kertas adalah …|mikrometer sekrup|penggaris|meteran|neraca|Mikrometer.
=|Alat untuk mengukur massa adalah …|neraca;timbangan|Neraca.
=|Ketelitian mikrometer sekrup adalah … mm.|0,01|0,01 mm.
B|Saat membaca skala, mata harus tegak lurus.|Paralaks.
S|Penggaris memiliki ketelitian 0,01 mm.|1 mm.
Alat untuk mengukur suhu adalah …|termometer|stopwatch|neraca|jangka sorong|Termometer.
Mengukur adalah membandingkan suatu besaran dengan …|satuan|warna|bentuk|bau|Satuan.
## IPA|Massa jenis
Rumus massa jenis adalah …|ρ = m : V|ρ = m × V|ρ = V : m|ρ = m + V|Massa : volume.
Massa jenis air adalah …|1 g/cm³|10 g/cm³|0,1 g/cm³|100 g/cm³|1 g/cm³.
=|Benda bermassa 40 g dan bervolume 20 cm³ memiliki massa jenis … g/cm³.|2|40 : 20.
=|Benda yang massa jenisnya lebih kecil dari air akan …|mengapung|Mengapung.
B|Es mengapung karena massa jenisnya lebih kecil dari air.|0,92.
S|Benda yang berat pasti tenggelam.|Tergantung massa jenis.
Telur tenggelam di air tawar tetapi mengapung di air garam pekat karena …|massa jenis air garam lebih besar|air garam lebih dingin|telur menjadi ringan|air tawar lebih berat|Massa jenis.
Benda yang pasti tenggelam di air adalah …|besi|kayu jati|es|gabus|Besi.
## IPA|Asam, basa, dan garam
Zat yang memiliki pH kurang dari 7 bersifat …|asam|basa|netral|garam|Asam.
Contoh zat basa adalah …|sabun|cuka|air jeruk|asam lambung|Sabun.
=|Zat dengan pH 7 bersifat …|netral|Netral.
=|Lakmus biru dalam larutan asam berubah menjadi …|merah|Merah.
B|Garam terbentuk dari reaksi asam dan basa.|Netralisasi.
S|Sabun bersifat asam.|Basa.
Rasa khas zat asam adalah …|masam|pahit|manis|asin|Masam.
Lakmus merah dalam larutan basa berubah menjadi …|biru|merah|hijau|kuning|Biru.
## IPA|Indikator alami
Indikator alami berasal dari …|tumbuhan|batu|logam|plastik|Tumbuhan.
Contoh indikator alami adalah …|kunyit|garam|gula|tepung|Kunyit.
=|Ekstrak kol ungu dalam larutan basa berwarna …|hijau|Hijau.
=|Kunyit dalam larutan basa berubah menjadi merah …|kecokelatan|Kecokelatan.
B|Bunga telang dapat dipakai sebagai indikator alami.|Telang.
S|Semua tumbuhan berwarna pasti dapat menjadi indikator.|Tidak semua.
Ekstrak kol ungu yang ditetesi cuka berubah menjadi …|merah|hijau|biru tua|kuning|Asam merah.
Fungsi indikator adalah menunjukkan sifat …|asam atau basa|panas atau dingin|berat atau ringan|padat atau cair|Asam basa.
## IPA|Gerak lurus
Gerak lurus dengan kecepatan tetap disebut …|GLB|GLBB|gerak melingkar|gerak parabola|GLB.
Gerak lurus dengan kecepatan berubah teratur disebut …|GLBB|GLB|gerak diam|gerak acak|GLBB.
=|Perubahan kecepatan setiap waktu disebut …|percepatan|Percepatan.
=|Mobil menempuh 120 km dalam 2 jam. Kecepatannya … km/jam.|60|120 : 2.
B|Bola jatuh bebas termasuk GLBB dipercepat.|Dipercepat.
S|Sepeda yang direm termasuk GLB.|GLBB diperlambat.
Bola yang dilempar vertikal ke atas saat naik mengalami gerak …|GLBB diperlambat|GLB|GLBB dipercepat|diam|Diperlambat.
Satuan percepatan adalah …|m/s²|m/s|km|kg|m/s².
## IPA|Gaya dan hukum Newton
Hukum I Newton disebut juga hukum …|kelembaman|aksi reaksi|gravitasi|percepatan|Kelembaman.
Rumus Hukum II Newton adalah …|F = m × a|F = m : a|F = a : m|F = m + a|F = ma.
=|Hukum III Newton membahas aksi dan …|reaksi|Reaksi.
=|Gaya 20 N bekerja pada benda 4 kg. Percepatannya … m/s².|5|20 : 4.
B|Roket meluncur menerapkan Hukum III Newton.|Aksi reaksi.
S|Penumpang terdorong ke depan saat bus mengerem adalah contoh Hukum III.|Hukum I.
Satuan gaya adalah …|newton|joule|watt|kilogram|Newton.
Jika massa benda makin besar dengan gaya sama, percepatannya …|makin kecil|makin besar|tetap|nol|Berbanding terbalik.
## IPA|Mikroskop
Lensa mikroskop yang dekat dengan mata disebut lensa …|okuler|objektif|cembung biasa|cekung|Okuler.
Lensa okuler 10× dan objektif 40× menghasilkan perbesaran …|400×|50×|30×|4×|10 × 40.
=|Bagian mikroskop tempat kaca benda adalah meja …|preparat|Meja preparat.
=|Pengatur fokus halus pada mikroskop disebut …|mikrometer|Mikrometer.
B|Pengamatan mikroskop dimulai dari perbesaran terkecil.|Terkecil.
S|Lensa objektif terletak dekat mata pengamat.|Dekat benda.
Pengatur fokus kasar pada mikroskop disebut …|makrometer|mikrometer|revolver|diafragma|Makrometer.
Fungsi cermin pada mikroskop adalah …|memantulkan cahaya|memperbesar benda|menjepit kaca|mengatur fokus|Cahaya.
## IPA|Tingkat organisasi kehidupan
Unit terkecil penyusun makhluk hidup adalah …|sel|jaringan|organ|sistem organ|Sel.
Kumpulan sel yang sama membentuk …|jaringan|organ|organisme|populasi|Jaringan.
=|Jantung termasuk tingkat …|organ|Organ.
=|Kumpulan organ yang bekerja sama membentuk sistem …|organ|Sistem organ.
B|Lambung adalah organ dalam sistem pencernaan.|Organ.
S|Jaringan lebih besar daripada organ.|Organ lebih besar.
Urutan yang benar adalah …|sel, jaringan, organ, sistem organ, organisme|organ, sel, jaringan, organisme|jaringan, sel, organ, sistem|organisme, sel, organ|Urutan.
Sekelompok makhluk hidup sejenis di suatu tempat disebut …|populasi|organisme|jaringan|organ|Populasi.
## IPA|Pencemaran lingkungan
Penyebab pencemaran udara adalah …|asap kendaraan|menanam pohon|bersepeda|hujan|Asap.
Deterjen berlebih dapat menyebabkan pencemaran …|air|udara|suara|cahaya|Air.
=|Sampah plastik yang menumpuk menyebabkan pencemaran …|tanah|Tanah.
=|Bunyi bising mesin menyebabkan pencemaran …|suara|Suara.
B|Tumpahan minyak mencemari laut.|Laut.
S|Pencemaran hanya disebabkan oleh pabrik.|Juga rumah tangga.
Cara mengurangi pencemaran air adalah …|tidak membuang sampah ke sungai|membuang limbah ke sungai|memakai deterjen berlebihan|membakar sampah|Jaga sungai.
Pestisida berlebihan dapat mencemari …|tanah dan air|udara saja|suara|cahaya|Tanah.
## IPA|Struktur bumi dan lempeng tektonik
Kulit bumi yang padat disebut …|litosfer|astenosfer|atmosfer|hidrosfer|Litosfer.
Indonesia berada di pertemuan … lempeng besar.|tiga|dua|lima|satu|Tiga.
=|Lapisan lunak di bawah litosfer disebut …|astenosfer|Astenosfer.
=|Lempeng di sebelah utara Indonesia adalah Lempeng …|Eurasia|Eurasia.
B|Pergerakan lempeng dapat menyebabkan gempa bumi.|Gempa.
S|Lempeng tektonik tidak pernah bergerak.|Bergerak perlahan.
Lempeng di sebelah selatan Indonesia adalah Lempeng …|Indo-Australia|Eurasia|Pasifik|Filipina|Indo-Australia.
Jalur gunung api di sekitar Samudra Pasifik disebut …|Cincin Api Pasifik|Sabuk Asteroid|Garis Wallace|Khatulistiwa|Ring of Fire.
## IPA|Atmosfer bumi
Lapisan atmosfer tempat terjadinya cuaca adalah …|troposfer|stratosfer|mesosfer|termosfer|Troposfer.
Lapisan ozon terdapat di …|stratosfer|troposfer|eksosfer|mesosfer|Stratosfer.
=|Meteor terbakar di lapisan …|mesosfer|Mesosfer.
=|Lapisan atmosfer terluar adalah …|eksosfer|Eksosfer.
B|Ozon melindungi bumi dari sinar ultraviolet.|Ultraviolet.
S|Hujan terjadi di lapisan eksosfer.|Troposfer.
Urutan lapisan atmosfer dari bawah adalah …|troposfer, stratosfer, mesosfer|stratosfer, troposfer, mesosfer|mesosfer, troposfer, stratosfer|eksosfer, troposfer, stratosfer|Dari bawah.
Atmosfer adalah lapisan … yang menyelimuti bumi.|udara|air|tanah|batu|Udara.
## IPA|Energi dan perubahannya
Energi adalah kemampuan untuk melakukan …|usaha|istirahat|tidur|diam|Usaha.
Setrika listrik mengubah energi listrik menjadi energi …|panas|cahaya|bunyi|kimia|Panas.
=|Baterai mengubah energi kimia menjadi energi …|listrik|Listrik.
=|Panel surya mengubah energi cahaya menjadi energi …|listrik|Listrik.
B|Energi tidak dapat diciptakan atau dimusnahkan.|Kekekalan.
S|Energi dapat hilang begitu saja.|Berubah bentuk.
Energi yang dimiliki benda bergerak disebut energi …|kinetik|potensial|kimia|nuklir|Kinetik.
Energi yang dimiliki benda karena ketinggiannya disebut energi …|potensial|kinetik|listrik|bunyi|Potensial.
"""

SAS += """
## IPA 1
0|Alat ukur panjang dengan ketelitian 1 mm adalah ....|penggaris|jangka sorong|mikrometer sekrup|neraca|Penggaris.
1|Minyak goreng mengapung di atas air karena massa jenisnya ....|lebih kecil dari air|lebih besar dari air|sama dengan air|nol|Lebih kecil.
2|Pasta gigi bersifat ....|basa|asam|netral|garam asam|Basa lemah.
3|Bunga telang dalam larutan basa berubah menjadi ....|hijau kebiruan|merah|kuning|hitam|Telang.
4|Kereta yang melaju dengan kecepatan tetap mengalami gerak ....|lurus beraturan|lurus berubah beraturan|melingkar|jatuh bebas|GLB.
5|Perenang mendorong dinding kolam lalu meluncur menerapkan Hukum Newton ....|III|I|II|gravitasi|Aksi reaksi.
## IPA 2
0|Lensa mikroskop yang dekat dengan benda disebut lensa ....|objektif|okuler|cembung mata|reflektor|Objektif.
1|Sel darah merah termasuk tingkat organisasi ....|sel|jaringan|organ|sistem organ|Sel.
2|Lampu yang menyala berlebihan pada malam hari menyebabkan pencemaran ....|cahaya|suara|tanah|air|Cahaya.
3|Lempeng yang berada di sebelah timur Indonesia adalah Lempeng ....|Pasifik|Eurasia|Indo-Australia|Afrika|Pasifik.
4|Lapisan atmosfer yang suhunya sangat tinggi adalah ....|termosfer|troposfer|stratosfer|mesosfer|Termosfer.
5|Pengeras suara mengubah energi listrik menjadi energi ....|bunyi|cahaya|kimia|potensial|Bunyi.
"""

TOPICS += """
## IPS
# 1|Ruang, Penduduk, dan Masyarakat
@ Peta dan komponennya
min: 15
act: Buat peta sederhana lingkungan rumahmu lengkap dengan judul, mata angin, skala, dan legenda.
mis: menghitung jarak sebenarnya tanpa memakai skala
exp: Peta adalah gambaran permukaan bumi pada bidang datar yang diperkecil dengan skala. Komponen peta meliputi judul, skala, mata angin, legenda, garis astronomis, inset, dan sumber. Jarak sebenarnya dihitung dengan mengalikan jarak di peta dengan penyebut skala.
ex: Skala 1 : 1.000.000, jarak peta 3 cm berarti 30 km. // Legenda menjelaskan arti simbol.
pt: Gambaran bumi yang diperkecil ; Komponen judul, skala, legenda ; Jarak sebenarnya = jarak peta × skala
sum: Komponen peta membantu membaca dan menghitung jarak.
fig: table Skala dan jarak peta | Jarak sebenarnya ;; 1 : 100.000 dan 2 cm | 2 km ;; 1 : 1.000.000 dan 3 cm | 30 km ;; 1 : 500.000 dan 4 cm | 20 km ;; 1 : 250.000 dan 8 cm | 20 km dari skala 250.000 ;; 1 : 50.000 dan 10 cm | 5 km ;; 1 : 2.000.000 dan 5 cm | 100 km ~ Menghitung jarak dengan skala.
@ Iklim dan musim di Indonesia
min: 15
act: Catat bulan-bulan musim hujan dan kemarau di daerahmu, lalu bandingkan dengan daerah lain.
mis: mengira angin muson barat membawa musim kemarau
exp: Indonesia beriklim tropis karena terletak di sekitar khatulistiwa. Indonesia mengalami dua musim yang dipengaruhi angin muson. Angin muson barat bertiup sekitar Oktober sampai April dan membawa banyak uap air sehingga terjadi musim hujan. Angin muson timur bertiup sekitar April sampai Oktober dan menyebabkan musim kemarau.
ex: Muson barat membawa hujan dari Samudra Hindia dan Asia. // Muson timur bertiup dari Australia yang kering.
pt: Iklim tropis ; Muson barat musim hujan ; Muson timur musim kemarau
sum: Angin muson menentukan musim di Indonesia.
fig: table Istilah | Arti ;; iklim tropis | iklim daerah khatulistiwa ;; muson barat | penyebab musim hujan ;; muson timur | penyebab musim kemarau ;; musim pancaroba | peralihan musim ;; curah hujan | banyaknya air hujan ;; khatulistiwa | garis lintang 0° ~ Istilah iklim Indonesia.
@ Penduduk dan pertumbuhannya
min: 15
act: Hitung anggota keluarga besarmu yang lahir, meninggal, dan pindah dalam lima tahun terakhir.
mis: mengira pertumbuhan penduduk hanya dipengaruhi kelahiran
exp: Pertumbuhan penduduk dipengaruhi kelahiran, kematian, dan migrasi. Kelahiran dan migrasi masuk menambah penduduk, sedangkan kematian dan migrasi keluar mengurangi penduduk. Sensus penduduk adalah pencacahan penduduk yang dilakukan setiap sepuluh tahun di Indonesia.
ex: Transmigrasi adalah perpindahan penduduk dari pulau padat ke pulau jarang. // Urbanisasi adalah perpindahan dari desa ke kota.
pt: Dipengaruhi kelahiran, kematian, migrasi ; Sensus setiap sepuluh tahun ; Urbanisasi desa ke kota
sum: Pertumbuhan penduduk perlu dikendalikan dan direncanakan.
fig: table Istilah | Arti ;; natalitas | kelahiran ;; mortalitas | kematian ;; migrasi | perpindahan penduduk ;; urbanisasi | pindah dari desa ke kota ;; transmigrasi | pindah antarpulau di Indonesia ;; sensus | pencacahan penduduk ~ Istilah kependudukan.
@ Lembaga sosial
min: 15
act: Sebutkan lembaga sosial yang kamu ikuti dan fungsinya bagi dirimu.
mis: mengira lembaga sosial selalu berupa gedung atau kantor
exp: Lembaga sosial adalah sistem norma untuk memenuhi kebutuhan pokok masyarakat. Contohnya lembaga keluarga, pendidikan, agama, ekonomi, dan politik. Keluarga adalah lembaga sosial pertama dan utama. Setiap lembaga memiliki fungsi, misalnya lembaga pendidikan berfungsi mencerdaskan masyarakat.
ex: Sekolah termasuk lembaga pendidikan. // Pasar termasuk lembaga ekonomi.
pt: Sistem norma memenuhi kebutuhan ; Keluarga lembaga pertama ; Setiap lembaga punya fungsi
sum: Lembaga sosial mengatur kehidupan masyarakat.
fig: table Lembaga sosial | Fungsi ;; keluarga | mengasuh dan mendidik anak ;; pendidikan | mencerdaskan masyarakat ;; agama | membimbing keimanan ;; ekonomi | memenuhi kebutuhan barang ;; politik | mengatur kekuasaan ;; kesehatan | menjaga kesehatan warga ~ Lembaga sosial dan fungsinya.
@ Sosialisasi
min: 15
act: Catat nilai dan kebiasaan yang kamu pelajari dari keluarga, sekolah, dan teman.
mis: mengira sosialisasi hanya terjadi di sekolah
exp: Sosialisasi adalah proses belajar seseorang tentang nilai, norma, dan kebiasaan masyarakat. Media sosialisasi antara lain keluarga, sekolah, teman sebaya, dan media massa. Keluarga adalah media sosialisasi pertama. Sosialisasi membentuk kepribadian seseorang.
ex: Anak belajar sopan santun dari orang tua. // Remaja belajar bekerja sama dari teman sebaya.
pt: Proses belajar nilai dan norma ; Media keluarga, sekolah, teman, media massa ; Membentuk kepribadian
sum: Sosialisasi menjadikan kita anggota masyarakat.
fig: table Media sosialisasi | Contoh nilai yang dipelajari ;; keluarga | sopan santun ;; sekolah | disiplin ;; teman sebaya | kerja sama ;; media massa | informasi dan tren ;; tempat ibadah | ajaran agama ;; lingkungan kerja | tanggung jawab profesi ~ Media sosialisasi.
@ Zaman praaksara
min: 15
act: Kunjungi museum atau cari gambar alat batu zaman praaksara, lalu tebak kegunaannya.
mis: mengira manusia praaksara tidak memiliki kebudayaan
exp: Zaman praaksara adalah masa sebelum manusia mengenal tulisan. Manusia praaksara hidup berburu dan meramu, lalu mulai bercocok tanam dan menetap. Alat yang dipakai berkembang dari batu kasar, batu halus, sampai logam. Situs manusia purba di Indonesia antara lain Sangiran dan Trinil.
ex: Kapak genggam dipakai untuk berburu. // Situs Sangiran ada di Jawa Tengah.
pt: Masa sebelum tulisan ; Berburu lalu bercocok tanam ; Alat batu sampai logam
sum: Manusia praaksara sudah memiliki kebudayaan.
fig: table Masa | Ciri ;; paleolitikum | batu tua kasar ;; mesolitikum | batu madya ;; neolitikum | batu muda halus ;; megalitikum | batu besar ;; perundagian | zaman logam ;; Sangiran | situs manusia purba ~ Masa praaksara dan cirinya.
# 2|Ekonomi dan Sejarah
@ Pelaku kegiatan ekonomi
min: 15
act: Gambar alur uang dan barang antara rumah tangga dan perusahaan di sekitarmu.
mis: mengira rumah tangga hanya berperan sebagai konsumen
exp: Pelaku ekonomi terdiri atas rumah tangga konsumen, rumah tangga produsen atau perusahaan, pemerintah, dan masyarakat luar negeri. Rumah tangga menyediakan tenaga kerja dan membeli barang. Perusahaan memproduksi barang dan memberi upah. Pemerintah memungut pajak dan menyediakan layanan umum.
ex: Ayah bekerja di pabrik dan mendapat gaji. // Pemerintah membangun jalan dari pajak.
pt: Empat pelaku ekonomi ; Rumah tangga dan perusahaan saling membutuhkan ; Pemerintah memungut pajak
sum: Pelaku ekonomi saling berhubungan.
fig: table Pelaku ekonomi | Peran ;; rumah tangga konsumen | membeli barang dan jasa ;; perusahaan | memproduksi barang ;; pemerintah | memungut pajak ;; masyarakat luar negeri | ekspor dan impor ;; koperasi | usaha bersama ;; bank | menghimpun dana ~ Pelaku kegiatan ekonomi.
@ Pasar dan jenisnya
min: 15
act: Bandingkan cara berbelanja di pasar tradisional dan toko daring bersama orang tua.
mis: mengira pasar selalu berupa tempat fisik
exp: Pasar adalah tempat atau sarana bertemunya penjual dan pembeli. Menurut bentuknya, ada pasar konkret, misalnya pasar tradisional, dan pasar abstrak, misalnya bursa saham dan pasar daring. Pasar tradisional memungkinkan tawar-menawar, sedangkan pasar modern memakai harga pas.
ex: Belanja sayur di pasar tradisional sambil menawar. // Membeli buku lewat toko daring.
pt: Bertemunya penjual dan pembeli ; Pasar konkret dan abstrak ; Tradisional tawar-menawar
sum: Pasar memudahkan pertukaran barang dan jasa.
fig: table Jenis pasar | Ciri ;; pasar tradisional | ada tawar-menawar ;; pasar modern | harga pas ;; pasar daring | transaksi lewat internet ;; bursa saham | jual beli saham ;; pasar harian | buka setiap hari ;; pasar mingguan | buka seminggu sekali ~ Jenis pasar.
@ Koperasi
min: 15
act: Cari tahu koperasi di sekolah atau lingkunganmu, lalu tanyakan cara menjadi anggotanya.
mis: mengira koperasi sama dengan perusahaan perseorangan
exp: Koperasi adalah badan usaha yang beranggotakan orang-orang dengan asas kekeluargaan. Tokoh Bapak Koperasi Indonesia adalah Mohammad Hatta. Modal koperasi berasal dari simpanan pokok, simpanan wajib, dan simpanan sukarela. Keuntungan koperasi disebut sisa hasil usaha atau SHU dan dibagikan kepada anggota.
ex: Koperasi sekolah menjual alat tulis. // SHU dibagikan setiap akhir tahun.
pt: Asas kekeluargaan ; Bapak Koperasi Mohammad Hatta ; Keuntungan disebut SHU
sum: Koperasi menyejahterakan anggotanya.
fig: table Istilah koperasi | Arti ;; simpanan pokok | dibayar sekali saat menjadi anggota ;; simpanan wajib | dibayar rutin ;; simpanan sukarela | sesuai kemampuan ;; SHU | sisa hasil usaha ;; rapat anggota | kekuasaan tertinggi ;; Hari Koperasi | 12 Juli ~ Istilah dalam koperasi.
@ Uang dan fungsinya
min: 15
act: Catat cara keluargamu membayar sehari-hari: uang tunai, kartu, atau dompet digital.
mis: mengira uang hanya berfungsi sebagai alat tukar
exp: Uang adalah alat tukar yang diterima masyarakat. Fungsi uang antara lain alat tukar, satuan hitung, penyimpan nilai, dan alat pembayaran utang. Jenis uang ada uang kartal, yaitu uang kertas dan logam, serta uang giral dan uang elektronik. Uang rupiah dikeluarkan oleh Bank Indonesia.
ex: Menabung di bank adalah fungsi uang sebagai penyimpan nilai. // Dompet digital termasuk uang elektronik.
pt: Alat tukar yang diterima umum ; Fungsi alat tukar dan penyimpan nilai ; Dikeluarkan Bank Indonesia
sum: Uang memudahkan kegiatan ekonomi.
fig: table Istilah | Arti ;; uang kartal | uang kertas dan logam ;; uang giral | simpanan di bank dengan cek ;; uang elektronik | uang dalam bentuk digital ;; Bank Indonesia | pengedar rupiah ;; barter | tukar barang dengan barang ;; inflasi | harga barang naik terus ~ Istilah tentang uang.
@ Jalur rempah Nusantara
min: 15
act: Cari rempah di dapur, lalu cari tahu daerah asalnya di Indonesia.
mis: mengira rempah hanya dipakai untuk memasak
exp: Sejak dulu Nusantara terkenal sebagai penghasil rempah-rempah seperti cengkih, pala, lada, dan kayu manis. Rempah dibutuhkan bangsa lain untuk bumbu, obat, dan pengawet. Jalur perdagangan rempah menghubungkan Nusantara dengan India, Tiongkok, Arab, dan Eropa, sekaligus menyebarkan budaya dan agama.
ex: Pala dan cengkih berasal dari Maluku. // Lada banyak dihasilkan di Lampung.
pt: Nusantara penghasil rempah ; Rempah untuk bumbu, obat, pengawet ; Jalur rempah menyebarkan budaya
sum: Rempah menjadikan Nusantara pusat perdagangan dunia.
fig: table Rempah | Daerah penghasil ;; cengkih | Maluku ;; pala | Banda ;; lada | Lampung ;; kayu manis | Kerinci ;; kemiri | Nusa Tenggara ;; vanili | Papua ~ Rempah dan daerah penghasilnya.
@ Kewirausahaan
min: 15
act: Rancang usaha kecil seperti menjual kerajinan, lalu hitung modal dan perkiraan untungnya.
mis: mengira wirausaha hanya berarti punya toko besar
exp: Wirausaha adalah orang yang berani membuka usaha sendiri dengan kreatif dan inovatif. Ciri wirausaha antara lain percaya diri, berani mengambil risiko, kreatif, pantang menyerah, dan jujur. Wirausaha membuka lapangan kerja dan memajukan ekonomi.
ex: Menjual kue buatan sendiri di sekolah. // Membuat kerajinan dari barang bekas untuk dijual.
pt: Berani membuka usaha sendiri ; Kreatif dan inovatif ; Membuka lapangan kerja
sum: Jiwa wirausaha bisa dilatih sejak dini.
fig: table Ciri wirausaha | Contoh sikap ;; percaya diri | berani menawarkan produk ;; kreatif | membuat produk unik ;; berani mengambil risiko | mencoba usaha baru ;; pantang menyerah | bangkit setelah rugi ;; jujur | tidak menipu pembeli ;; disiplin | mencatat keuangan ~ Ciri wirausaha.
"""

BANK += """
## IPS|Peta dan komponennya
Komponen peta yang menjelaskan arti simbol adalah …|legenda|skala|judul|inset|Legenda.
Skala 1 : 200.000 dan jarak peta 5 cm. Jarak sebenarnya …|10 km|1 km|100 km|50 km|5 × 200.000 cm.
=|Komponen peta yang menunjukkan perbandingan jarak adalah …|skala|Skala.
=|Komponen peta yang menunjukkan arah adalah mata …|angin|Mata angin.
B|Inset adalah peta kecil yang menunjukkan lokasi daerah.|Inset.
S|Peta adalah gambaran bumi yang diperbesar.|Diperkecil.
Garis lintang dan bujur pada peta disebut garis …|astronomis|kontur|pantai|batas|Astronomis.
Skala 1 : 100.000 berarti 1 cm di peta sama dengan …|1 km|100 m|10 km|1 m|100.000 cm.
## IPS|Iklim dan musim di Indonesia
Indonesia beriklim …|tropis|subtropis|kutub|gurun|Tropis.
Angin yang menyebabkan musim hujan di Indonesia adalah muson …|barat|timur|utara|selatan|Barat.
=|Angin muson timur menyebabkan musim …|kemarau|Kemarau.
=|Masa peralihan antara dua musim disebut musim …|pancaroba|Pancaroba.
B|Angin muson timur bertiup dari Australia.|Australia.
S|Muson barat menyebabkan musim kemarau.|Musim hujan.
Muson barat biasanya bertiup sekitar bulan …|Oktober sampai April|April sampai Oktober|Januari saja|Juni sampai Juli|Oktober–April.
Indonesia beriklim tropis karena terletak di sekitar …|khatulistiwa|kutub utara|garis balik utara|kutub selatan|Khatulistiwa.
## IPS|Penduduk dan pertumbuhannya
Faktor yang menambah jumlah penduduk adalah …|kelahiran|kematian|migrasi keluar|bencana|Kelahiran.
Perpindahan penduduk dari desa ke kota disebut …|urbanisasi|transmigrasi|emigrasi|ruralisasi|Urbanisasi.
=|Kematian dalam istilah kependudukan disebut …|mortalitas|Mortalitas.
=|Sensus penduduk di Indonesia dilakukan setiap … tahun.|10;sepuluh|Sepuluh tahun.
B|Natalitas artinya kelahiran.|Natalitas.
S|Migrasi keluar menambah jumlah penduduk suatu daerah.|Mengurangi.
Perpindahan penduduk dari pulau padat ke pulau jarang penduduk di Indonesia disebut …|transmigrasi|urbanisasi|emigrasi|imigrasi|Transmigrasi.
Pencacahan penduduk disebut …|sensus|migrasi|natalitas|urbanisasi|Sensus.
## IPS|Lembaga sosial
Lembaga sosial pertama dan utama adalah lembaga …|keluarga|pendidikan|ekonomi|politik|Keluarga.
Sekolah termasuk lembaga …|pendidikan|ekonomi|agama|politik|Pendidikan.
=|Pasar termasuk lembaga …|ekonomi|Ekonomi.
=|Lembaga yang mengatur kekuasaan disebut lembaga …|politik|Politik.
B|Lembaga sosial adalah sistem norma untuk memenuhi kebutuhan masyarakat.|Pengertian.
S|Lembaga sosial selalu berupa gedung.|Sistem norma.
Fungsi lembaga agama adalah …|membimbing keimanan|mengatur pajak|memproduksi barang|mencetak uang|Agama.
Fungsi lembaga keluarga adalah …|mengasuh dan mendidik anak|mengatur negara|memungut pajak|menjual barang|Keluarga.
## IPS|Sosialisasi
Sosialisasi adalah proses belajar tentang …|nilai dan norma masyarakat|cara memasak|pelajaran matematika saja|olahraga|Nilai norma.
Media sosialisasi pertama adalah …|keluarga|sekolah|media massa|teman sebaya|Keluarga.
=|Kelompok teman seusia disebut teman …|sebaya|Sebaya.
=|Televisi dan internet termasuk media …|massa|Media massa.
B|Sosialisasi membentuk kepribadian seseorang.|Kepribadian.
S|Sosialisasi hanya terjadi di sekolah.|Banyak media.
Nilai disiplin banyak dipelajari dari …|sekolah|televisi saja|pasar|jalan raya|Sekolah.
Anak belajar sopan santun pertama kali dari …|orang tua|teman di internet|iklan|tetangga jauh|Keluarga.
## IPS|Zaman praaksara
Zaman praaksara adalah masa sebelum manusia mengenal …|tulisan|api|makanan|alat|Tulisan.
Situs manusia purba Sangiran terletak di …|Jawa Tengah|Papua|Bali|Sumatra|Jawa Tengah.
=|Zaman batu muda disebut …|neolitikum|Neolitikum.
=|Zaman batu besar disebut …|megalitikum|Megalitikum.
B|Manusia praaksara mula-mula hidup berburu dan meramu.|Berburu.
S|Manusia praaksara tidak memiliki kebudayaan.|Memiliki.
Zaman logam disebut juga masa …|perundagian|paleolitikum|mesolitikum|neolitikum|Perundagian.
Alat batu kasar banyak ditemukan pada masa …|paleolitikum|neolitikum|perundagian|megalitikum|Paleolitikum.
## IPS|Pelaku kegiatan ekonomi
Pelaku ekonomi yang memproduksi barang adalah …|perusahaan|rumah tangga konsumen|pemerintah|bank sentral|Perusahaan.
Pemerintah memperoleh pendapatan terutama dari …|pajak|gaji|upah|sewa rumah|Pajak.
=|Badan usaha bersama berasas kekeluargaan disebut …|koperasi|Koperasi.
=|Rumah tangga konsumen menyediakan tenaga …|kerja|Tenaga kerja.
B|Masyarakat luar negeri berperan dalam ekspor dan impor.|Luar negeri.
S|Rumah tangga hanya berperan sebagai produsen.|Konsumen juga.
Lembaga yang menghimpun dana masyarakat adalah …|bank|pasar|sekolah|rumah sakit|Bank.
Perusahaan memberi … kepada pekerja.|upah|pajak|subsidi|dividen negara|Upah.
## IPS|Pasar dan jenisnya
Pasar adalah tempat bertemunya …|penjual dan pembeli|guru dan murid|dokter dan pasien|polisi dan warga|Penjual pembeli.
Ciri pasar tradisional adalah …|ada tawar-menawar|harga pas|serba otomatis|hanya daring|Tawar.
=|Pasar yang transaksinya lewat internet disebut pasar …|daring;online|Daring.
=|Pasar jual beli saham disebut bursa …|saham;efek|Bursa saham.
B|Bursa saham termasuk pasar abstrak.|Abstrak.
S|Pasar modern biasanya memakai sistem tawar-menawar.|Harga pas.
Pasar yang buka seminggu sekali disebut pasar …|mingguan|harian|tahunan|bulanan|Mingguan.
Contoh pasar konkret adalah …|pasar tradisional|bursa saham|pasar valuta asing daring|pasar tenaga kerja|Konkret.
## IPS|Koperasi
Bapak Koperasi Indonesia adalah …|Mohammad Hatta|Soekarno|Ki Hajar Dewantara|Soepomo|Hatta.
Asas koperasi adalah …|kekeluargaan|persaingan|perseorangan|keuntungan pribadi|Kekeluargaan.
=|Keuntungan koperasi disebut sisa hasil …|usaha|SHU.
=|Hari Koperasi diperingati setiap tanggal 12 …|Juli|12 Juli.
B|Simpanan pokok dibayar sekali saat menjadi anggota.|Pokok.
S|Kekuasaan tertinggi koperasi ada di tangan ketua.|Rapat anggota.
Simpanan yang dibayar rutin oleh anggota disebut simpanan …|wajib|pokok|sukarela|hibah|Wajib.
Contoh koperasi di sekolah menjual …|alat tulis|mobil|rumah|tanah|Alat tulis.
## IPS|Uang dan fungsinya
Fungsi utama uang adalah sebagai alat …|tukar|hiasan|mainan|ukur panjang|Alat tukar.
Uang kertas dan logam disebut uang …|kartal|giral|elektronik|digital|Kartal.
=|Lembaga yang mengedarkan rupiah adalah Bank …|Indonesia|Bank Indonesia.
=|Tukar-menukar barang dengan barang disebut …|barter|Barter.
B|Menabung adalah fungsi uang sebagai penyimpan nilai.|Penyimpan nilai.
S|Uang elektronik tidak termasuk jenis uang.|Termasuk.
Kenaikan harga barang secara terus-menerus disebut …|inflasi|deflasi|barter|tabungan|Inflasi.
Dompet digital termasuk uang …|elektronik|kartal|logam|barter|Elektronik.
## IPS|Jalur rempah Nusantara
Cengkih dan pala terutama berasal dari …|Maluku|Jawa Barat|Aceh|Bali|Maluku.
Lada banyak dihasilkan di …|Lampung|Papua|Bali|Maluku Utara|Lampung.
=|Rempah dibutuhkan bangsa Eropa untuk bumbu, obat, dan …|pengawet|Pengawet.
=|Kayu manis banyak dihasilkan di …|Kerinci|Kerinci.
B|Jalur rempah turut menyebarkan budaya dan agama.|Budaya.
S|Rempah hanya dipakai untuk memasak.|Juga obat dan pengawet.
Kepulauan yang terkenal sebagai penghasil pala adalah Kepulauan …|Banda|Seribu|Riau|Karimunjawa|Banda.
Jalur rempah menghubungkan Nusantara dengan …|India, Tiongkok, Arab, dan Eropa|Amerika saja|Antartika|Australia saja|Jalur.
## IPS|Kewirausahaan
Wirausaha adalah orang yang berani …|membuka usaha sendiri|bekerja tanpa usaha|meminjam tanpa membayar|menghindari risiko|Usaha sendiri.
Ciri wirausaha adalah …|kreatif dan pantang menyerah|malas dan pasrah|takut mencoba|suka menipu|Ciri.
=|Wirausaha yang bangkit setelah rugi memiliki sikap pantang …|menyerah|Pantang menyerah.
=|Manfaat wirausaha adalah membuka lapangan …|kerja|Lapangan kerja.
B|Mencatat keuangan adalah sikap disiplin wirausaha.|Disiplin.
S|Wirausaha boleh menipu pembeli agar untung.|Harus jujur.
Membuat produk yang unik menunjukkan sikap …|kreatif|malas|curang|ragu|Kreatif.
Contoh wirausaha pelajar adalah …|menjual kerajinan buatan sendiri|bolos sekolah|menyontek|meminta uang terus|Usaha kecil.
"""

SAS += """
## IPS 1
0|Skala 1 : 300.000 dengan jarak peta 4 cm. Jarak sebenarnya adalah ....|12 km|1,2 km|120 km|7 km|4 × 3 km.
1|Musim hujan di Indonesia dipengaruhi angin muson ....|barat|timur|tenggara|selatan|Barat.
2|Perpindahan penduduk ke luar negeri disebut ....|emigrasi|urbanisasi|transmigrasi|imigrasi|Emigrasi.
3|Lembaga yang berfungsi menjaga kesehatan warga adalah lembaga ....|kesehatan|politik|ekonomi|agama|Kesehatan.
4|Nilai tanggung jawab profesi dipelajari melalui media sosialisasi ....|lingkungan kerja|keluarga inti|teman bermain|tempat ibadah|Kerja.
5|Masa praaksara ketika manusia mulai menetap dan bercocok tanam adalah ....|neolitikum|paleolitikum|mesolitikum|perundagian|Neolitikum.
## IPS 2
0|Pemerintah menyediakan layanan umum dengan dana dari ....|pajak|upah|SHU|tabungan pribadi|Pajak.
1|Pasar yang menggunakan harga pas umumnya adalah pasar ....|modern|tradisional|mingguan|tahunan|Modern.
2|Kekuasaan tertinggi dalam koperasi berada pada ....|rapat anggota|ketua|bendahara|pemerintah|Rapat anggota.
3|Cek merupakan alat pembayaran dengan uang ....|giral|kartal|logam|elektronik|Giral.
4|Vanili banyak dihasilkan di ....|Papua|Banda|Lampung|Kerinci|Vanili.
5|Wirausaha yang berani mencoba usaha baru menunjukkan ciri ....|berani mengambil risiko|takut gagal|pasrah|malas|Risiko.
"""

TOPICS += """
## BIG
# 1|Daily Communication
@ Greetings and leave-taking
min: 15
act: Practise formal and informal greetings with your family at different times of the day.
mis: memakai Good night saat bertemu orang pada malam hari
exp: Greetings dipakai saat bertemu dan leave-taking dipakai saat berpisah. Good morning, good afternoon, dan good evening dipakai saat bertemu. Good night dipakai saat berpisah pada malam hari atau sebelum tidur. Ungkapan informal antara lain Hi, Hello, See you, dan Bye.
ex: Good morning, Mrs. Rina. How are you? // See you tomorrow!
pt: Greetings saat bertemu ; Leave-taking saat berpisah ; Good night untuk berpisah malam
sum: Pilih salam sesuai waktu dan situasi.
fig: table Expression | Use ;; Good morning | meeting before noon ;; Good afternoon | meeting after noon ;; Good evening | meeting at night ;; Good night | leaving at night ;; See you later | informal leaving ;; Nice to meet you | first meeting ~ Greetings and leave-taking.
@ Telling the time
min: 15
act: Ask your family members what time they wake up and answer in English.
mis: membaca 7.15 sebagai seven fifteen past
exp: Untuk menyebut waktu, kita memakai o'clock untuk jam tepat, past untuk lewat, dan to untuk kurang. Quarter artinya seperempat atau 15 menit, dan half artinya setengah atau 30 menit. Waktu juga bisa dibaca langsung, misalnya 7.15 dibaca seven fifteen.
ex: It is half past seven (7.30). // It is a quarter to nine (8.45).
pt: O'clock untuk jam tepat ; Past lewat, to kurang ; Quarter 15 menit, half 30 menit
sum: Ada dua cara membaca jam dalam bahasa Inggris.
fig: table Time | How to say it ;; 7.00 | seven o'clock ;; 7.30 | half past seven ;; 7.15 | a quarter past seven ;; 8.45 | a quarter to nine ;; 9.10 | ten past nine ;; 10.50 | ten to eleven ~ Telling the time.
@ Days, months, and dates
min: 15
act: Write the dates of national holidays in English.
mis: menulis tanggal dengan bilangan biasa, bukan ordinal
exp: Days adalah nama hari, months adalah nama bulan. Tanggal dibaca dengan ordinal number, misalnya the seventeenth of August atau August seventeenth. Gunakan on untuk hari dan tanggal, in untuk bulan dan tahun.
ex: Indonesian Independence Day is on August 17th. // School starts in July.
pt: Days dan months diawali huruf kapital ; Tanggal memakai ordinal ; On untuk tanggal, in untuk bulan
sum: Tanggal dalam bahasa Inggris memakai ordinal number.
fig: table Date | Celebration ;; January 1st | New Year ;; April 21st | Kartini Day ;; May 2nd | National Education Day ;; August 17th | Independence Day ;; October 28th | Youth Pledge Day ;; November 10th | Heroes Day ~ Important dates in Indonesia.
@ Family tree
min: 15
act: Draw your family tree and label each member in English.
mis: menyebut saudara sepupu sebagai nephew
exp: Family tree adalah bagan keluarga. Grandparents adalah kakek nenek, parents adalah orang tua, uncle adalah paman, aunt adalah bibi, cousin adalah sepupu, nephew adalah keponakan laki-laki, dan niece adalah keponakan perempuan. Gunakan possessive 's, misalnya my father's brother.
ex: My father's brother is my uncle. // My uncle's son is my cousin.
pt: Uncle dan aunt ; Cousin artinya sepupu ; Nephew dan niece keponakan
sum: Family tree menunjukkan hubungan keluarga.
fig: table Relation | Name ;; father's father | grandfather ;; father's brother | uncle ;; mother's sister | aunt ;; uncle's child | cousin ;; brother's son | nephew ;; sister's daughter | niece ~ Family members.
@ Classroom instructions
min: 15
act: Give five instructions in English to your younger sibling and see if they follow them.
mis: menambahkan subjek you di depan setiap perintah
exp: Imperative sentences atau kalimat perintah dimulai dengan kata kerja dasar, misalnya Open your book. Kalimat larangan memakai Don't, misalnya Don't run in the classroom. Tambahkan please supaya terdengar sopan. Kalimat ajakan memakai Let's.
ex: Please close the window. // Don't make noise.
pt: Perintah dimulai kata kerja dasar ; Larangan memakai Don't ; Tambahkan please
sum: Kalimat perintah dipakai untuk memberi instruksi.
fig: table Instruction | Type ;; Open your book | command ;; Don't run | prohibition ;; Let's sing together | invitation ;; Please sit down | polite command ;; Don't be late | prohibition about time ;; Let's go to the library | invitation to a place ~ Types of instructions.
@ Describing animals
min: 15
act: Describe your favourite animal in English: its body, food, and where it lives.
mis: menulis The cat have four legs
exp: Untuk menggambarkan hewan, kita menyebut bentuk tubuh, warna, makanan, dan habitat. Gunakan has untuk he, she, it, dan have untuk I, you, we, they. Contohnya The elephant has a long trunk. Gunakan lives in untuk tempat tinggal.
ex: The giraffe has a long neck. // Fish live in water.
pt: Sebut bentuk, warna, makanan, habitat ; It has, they have ; Gunakan lives in
sum: Deskripsi hewan memakai has dan lives in.
fig: table Animal | Special feature ;; elephant | long trunk ;; giraffe | long neck ;; zebra | black and white stripes ;; tiger | sharp teeth ;; turtle | hard shell ;; peacock | colourful feathers ~ Describing animals.
# 2|My Surroundings
@ Possessive adjectives
min: 15
act: Point to things in your house and say whose they are using my, your, his, her, our, or their.
mis: memakai he untuk menyatakan milik laki-laki
exp: Possessive adjectives menunjukkan kepemilikan dan diletakkan sebelum kata benda. My untuk I, your untuk you, his untuk he, her untuk she, its untuk it, our untuk we, dan their untuk they.
ex: This is my bag. // Rina loves her cat.
pt: Diletakkan sebelum kata benda ; His untuk laki-laki, her untuk perempuan ; Our dan their untuk jamak
sum: Possessive adjectives menyatakan milik.
fig: table Subject | Possessive adjective ;; I | my ;; you | your ;; he | his ;; she | her ;; we | our ;; they | their ~ Possessive adjectives.
@ Present continuous tense
min: 15
act: Look around your house and describe what each person is doing now.
mis: menulis She is cook tanpa -ing
exp: Present continuous tense menyatakan kegiatan yang sedang berlangsung. Rumusnya subject + am/is/are + verb-ing. Kata keterangan waktu yang sering dipakai adalah now, right now, dan at the moment. Kalimat negatif memakai not, misalnya She is not sleeping.
ex: My mother is cooking now. // They are playing football at the moment.
pt: Kegiatan sedang berlangsung ; am/is/are + verb-ing ; Keterangan now dan at the moment
sum: Present continuous menceritakan apa yang sedang terjadi.
fig: table Subject | Sentence ;; I | I am studying now ;; She | She is cooking ;; He | He is reading a comic ;; We | We are watching TV ;; They | They are playing football ;; It | It is raining ~ Present continuous sentences.
@ Public places
min: 15
act: List five public places in your town and what people do there in English.
mis: menyebut library sebagai toko buku
exp: Public places adalah tempat umum. Library adalah perpustakaan, hospital adalah rumah sakit, post office adalah kantor pos, police station adalah kantor polisi, bank adalah bank, dan market adalah pasar. Kita menyebut kegiatan di sana, misalnya We borrow books at the library.
ex: We borrow books at the library. // Doctors work at the hospital.
pt: Library artinya perpustakaan ; Hospital artinya rumah sakit ; Sebut kegiatan di tempat itu
sum: Public places adalah tempat umum di sekitar kita.
fig: table Place | Activity ;; library | borrowing books ;; hospital | treating patients ;; post office | sending letters ;; police station | reporting a problem ;; bank | saving money ;; market | buying vegetables ~ Public places and activities.
@ Asking and giving directions
min: 15
act: Draw a simple map of your neighbourhood and give directions to a friend in English.
mis: tertukar turn left dan turn right
exp: Untuk menanyakan arah, gunakan Excuse me, where is the ...? atau How can I get to ...? Untuk memberi arah, gunakan go straight, turn left, turn right, next to, opposite, dan between. Ucapkan terima kasih setelah dibantu.
ex: Go straight and turn left. The bank is next to the school. // The hospital is opposite the park.
pt: Bertanya dengan Excuse me ; Go straight, turn left, turn right ; Next to, opposite, between
sum: Petunjuk arah harus jelas dan berurutan.
fig: table Expression | Meaning ;; go straight | jalan lurus ;; turn left | belok kiri ;; turn right | belok kanan ;; next to | di sebelah ;; opposite | di seberang ;; between | di antara ~ Expressions for directions.
@ Hobbies and free time
min: 15
act: Interview three friends about their hobbies and write a short report in English.
mis: menulis My hobby is swim tanpa -ing
exp: Hobby adalah kegiatan yang disukai pada waktu luang. Untuk menyebut hobi, gunakan My hobby is reading atau I like playing football. Untuk bertanya, gunakan What is your hobby? atau What do you do in your free time?
ex: My hobby is drawing. // In my free time, I play the guitar.
pt: Hobi kegiatan waktu luang ; My hobby is + verb-ing ; Tanya What is your hobby?
sum: Hobi membuat waktu luang bermanfaat.
fig: table Hobby | Thing we need ;; drawing | pencil and paper ;; swimming | swimsuit ;; reading | books ;; gardening | seeds and soil ;; cooking | pan and stove ;; photography | camera ~ Hobbies and things we need.
@ Notices and signs
min: 15
act: Take photos of signs in public places and explain their meaning in English.
mis: mengira No parking berarti boleh parkir
exp: Notice atau sign adalah tulisan singkat yang memberi informasi, larangan, atau peringatan. Contohnya No smoking (dilarang merokok), Keep quiet (harap tenang), Wet floor (lantai basah), dan Exit (pintu keluar). Notice biasanya dipasang di tempat umum.
ex: Keep quiet is put in the library. // Wet floor means be careful, the floor is slippery.
pt: Memberi informasi, larangan, peringatan ; Kalimat singkat ; Dipasang di tempat umum
sum: Notice membantu kita bersikap tertib.
fig: table Notice | Meaning ;; No smoking | dilarang merokok ;; Keep quiet | harap tenang ;; Wet floor | lantai basah ;; Exit | pintu keluar ;; No parking | dilarang parkir ;; Keep off the grass | dilarang menginjak rumput ~ Notices and their meaning.
"""

BANK += """
## BIG|Greetings and leave-taking
Salam yang tepat saat bertemu pukul 08.00 pagi adalah …|Good morning|Good night|Good evening|Good afternoon|Pagi.
Good night diucapkan saat …|berpisah pada malam hari|bertemu pagi hari|makan siang|bertemu sore|Berpisah malam.
=|Salam saat bertemu orang pertama kali adalah Nice to … you.|meet|Nice to meet you.
=|Salam saat bertemu pukul 14.00 adalah Good …|afternoon|Afternoon.
B|See you later adalah ungkapan berpisah.|Leave-taking.
S|Good night dipakai saat bertemu orang pada malam hari.|Good evening.
How are you? Jawaban yang tepat adalah …|I'm fine, thank you.|I'm twelve years old.|I'm a student.|Goodbye.|Kabar.
Ungkapan berpisah yang informal adalah …|Bye!|Good morning!|How do you do?|Nice to meet you!|Bye.
## BIG|Telling the time
7.30 dibaca …|half past seven|half past eight|seven thirteen|a quarter to seven|Setengah.
8.45 dibaca …|a quarter to nine|a quarter past eight|half past nine|eight forty-five past|Kurang 15.
=|Kata untuk jam tepat adalah …|o'clock|O'clock.
=|Quarter artinya … menit.|15;lima belas|15 menit.
B|9.10 dapat dibaca ten past nine.|Lewat 10.
S|10.50 dibaca ten past eleven.|Ten to eleven.
6.15 dibaca …|a quarter past six|a quarter to six|half past six|six forty-five|Lewat 15.
What time is it? Jawaban yang tepat adalah …|It is five o'clock.|It is Monday.|It is sunny.|It is my book.|Jam.
## BIG|Days, months, and dates
Hari Kemerdekaan Indonesia jatuh pada …|August 17th|May 2nd|April 21st|October 28th|17 Agustus.
Kata depan untuk tanggal adalah …|on|in|at|by|On.
=|Kata depan untuk bulan adalah …|in|In.
=|Kartini Day is on April … (21st)|21st;twenty-first|21st.
B|Nama hari dalam bahasa Inggris diawali huruf kapital.|Kapital.
S|Youth Pledge Day is on November 10th.|October 28th.
Heroes Day in Indonesia is on …|November 10th|August 17th|May 2nd|January 1st|10 November.
National Education Day is on …|May 2nd|April 21st|October 28th|August 17th|2 Mei.
## BIG|Family tree
My father's brother is my …|uncle|aunt|cousin|nephew|Uncle.
My mother's sister is my …|aunt|uncle|niece|grandmother|Aunt.
=|My uncle's child is my …|cousin|Cousin.
=|My brother's son is my …|nephew|Nephew.
B|My sister's daughter is my niece.|Niece.
S|My father's father is my uncle.|Grandfather.
Grandparents artinya …|kakek dan nenek|paman dan bibi|ayah dan ibu|sepupu|Kakek nenek.
Bagan keluarga dalam bahasa Inggris disebut …|family tree|family car|family time|family name|Family tree.
## BIG|Classroom instructions
Kalimat perintah dimulai dengan …|kata kerja dasar|kata benda|kata sifat|kata ganti|Verb.
Kalimat larangan memakai kata …|Don't|Let's|Please|Can|Don't.
=|Kata supaya perintah terdengar sopan adalah …|please|Please.
=|Kalimat ajakan dimulai dengan kata …|Let's;let's|Let's.
B|Don't run in the classroom adalah kalimat larangan.|Larangan.
S|Let's sing together adalah kalimat larangan.|Ajakan.
Guru berkata Please be quiet. Artinya …|tolong tenang|tolong bernyanyi|tolong berdiri|tolong keluar|Be quiet.
Kalimat perintah yang benar adalah …|Close the door, please.|You closes the door.|Closing the door.|The door close.|Perintah.
## BIG|Describing animals
The elephant … a long trunk.|has|have|is|are|It has.
Fish … in water.|live|lives|living|is live|They live.
=|The giraffe has a long …|neck|Neck.
=|A turtle has a hard …|shell|Shell.
B|The zebra has black and white stripes.|Stripes.
S|A tiger has a long trunk.|Elephant.
Hewan yang memiliki bulu ekor berwarna-warni adalah …|peacock|turtle|zebra|elephant|Peacock.
Kata untuk tempat hidup hewan adalah …|habitat|hobby|holiday|hospital|Habitat.
## BIG|Possessive adjectives
Possessive adjective untuk she adalah …|her|his|its|their|Her.
Possessive adjective untuk they adalah …|their|our|your|his|Their.
=|Possessive adjective untuk he adalah …|his|His.
=|Possessive adjective untuk we adalah …|our|Our.
B|This is my bag adalah kalimat yang benar.|My.
S|Budi loves her bicycle (milik Budi).|His.
Rina and I love … school.|our|their|my|his|We → our.
The cat is licking … paw.|its|it|his|their|It → its.
## BIG|Present continuous tense
She … cooking now.|is|am|are|be|She is.
They … playing football at the moment.|are|is|am|be|They are.
=|I am … a book now. (read)|reading|Read + ing.
=|Keterangan waktu untuk present continuous adalah …|now;at the moment;right now|Now.
B|It is raining adalah kalimat present continuous.|Benar.
S|He are sleeping adalah kalimat yang benar.|He is.
Kalimat negatif yang benar adalah …|She is not sleeping.|She not is sleeping.|She is sleeping not.|She does not sleeping.|Negatif.
What are you doing? Jawaban yang tepat adalah …|I am doing my homework.|I do my homework yesterday.|I did my homework.|I will homework.|Present continuous.
## BIG|Public places
Library artinya …|perpustakaan|toko buku|rumah sakit|kantor pos|Library.
Tempat untuk mengirim surat adalah …|post office|hospital|library|bank|Post office.
=|Tempat dokter merawat pasien adalah …|hospital|Hospital.
=|Tempat menabung uang adalah …|bank|Bank.
B|Police station adalah kantor polisi.|Police.
S|We borrow books at the hospital.|Library.
We buy vegetables at the …|market|library|police station|post office|Market.
Kita melapor masalah keamanan ke …|police station|bakery|library|stadium|Police station.
## BIG|Asking and giving directions
Turn left artinya …|belok kiri|belok kanan|jalan lurus|berhenti|Turn left.
Opposite artinya …|di seberang|di sebelah|di antara|di belakang|Opposite.
=|Go … artinya jalan lurus.|straight|Straight.
=|Between artinya di …|antara|Di antara.
B|Next to artinya di sebelah.|Next to.
S|Turn right artinya belok kiri.|Belok kanan.
Ungkapan sopan untuk menanyakan arah dimulai dengan …|Excuse me|Go away|Hurry up|Be quiet|Excuse me.
How can I get to the bank? adalah pertanyaan tentang …|arah|harga|waktu|cuaca|Arah.
## BIG|Hobbies and free time
My hobby is … (membaca)|reading|read|reads|to reading|Verb-ing.
Pertanyaan untuk menanyakan hobi adalah …|What is your hobby?|Where is your hobby?|How old is your hobby?|When is your hobby?|What.
=|Hobi berkebun dalam bahasa Inggris adalah …|gardening|Gardening.
=|Hobi memotret membutuhkan …|camera;kamera|Camera.
B|In my free time, I play the guitar adalah kalimat tentang hobi.|Free time.
S|My hobby is swim adalah kalimat yang benar.|Swimming.
Hobby artinya kegiatan yang disukai pada waktu …|luang|sekolah|tidur|ujian|Luang.
Hobi yang membutuhkan buku adalah …|reading|swimming|cooking|cycling|Reading.
## BIG|Notices and signs
No smoking artinya …|dilarang merokok|boleh merokok|tempat merokok|rokok murah|Dilarang.
Keep quiet biasanya dipasang di …|perpustakaan|pasar|stadion|lapangan|Library.
=|Notice Exit menunjukkan pintu …|keluar|Keluar.
=|Wet floor artinya lantai …|basah|Basah.
B|No parking berarti dilarang parkir.|Larangan.
S|Keep off the grass berarti silakan duduk di rumput.|Dilarang menginjak.
Notice memberi informasi, larangan, atau …|peringatan|hiburan|resep|cerita|Peringatan.
Notice Wet floor mengingatkan kita agar …|berhati-hati karena licin|berlari|duduk di lantai|membuang sampah|Hati-hati.
"""

SAS += """
## BIG 1
0|Good evening diucapkan saat ....|bertemu pada malam hari|berpisah malam hari|bertemu pagi hari|bertemu siang hari|Evening.
1|10.30 dibaca ....|half past ten|half past eleven|ten thirty past|a quarter to ten|Setengah.
2|New Year is on ....|January 1st|December 25th|August 17th|May 2nd|Tahun Baru.
3|My aunt's son is my ....|cousin|nephew|uncle|brother|Cousin.
4|Don't be late artinya ....|jangan terlambat|ayo terlambat|tolong cepat pulang|silakan masuk|Larangan.
5|The tiger has sharp ....|teeth|neck|shell|trunk|Teeth.
## BIG 2
0|Possessive adjective untuk you adalah ....|your|you|yours|yourself|Your.
1|Listen! The baby ... .|is crying|cries|cried|cry|Present continuous.
2|Tempat meminjam buku adalah ....|library|market|hospital|bank|Library.
3|The bank is ... the school and the park.|between|opposite|turn left|go straight|Between.
4|Hobi memasak membutuhkan ....|pan and stove|camera|swimsuit|seeds|Cooking.
5|Notice Keep off the grass artinya ....|dilarang menginjak rumput|silakan bermain di rumput|potong rumput|siram rumput|Notice.
"""

TOPICS += """
## PPK
# 1|Pancasila, Norma, dan Lembaga Negara
@ Pancasila sebagai dasar negara
min: 15
act: Diskusikan dengan keluarga contoh aturan negara yang sesuai dengan nilai Pancasila.
mis: mengira Pancasila hanya berfungsi sebagai simbol
exp: Pancasila berkedudukan sebagai dasar negara, pandangan hidup bangsa, dan ideologi negara. Sebagai dasar negara, Pancasila menjadi sumber dari segala sumber hukum di Indonesia. Semua peraturan perundang-undangan tidak boleh bertentangan dengan Pancasila.
ex: Undang-undang dibuat sesuai nilai Pancasila. // Pancasila menjadi pedoman perilaku warga.
pt: Dasar negara dan pandangan hidup ; Sumber dari segala sumber hukum ; Peraturan tidak boleh bertentangan
sum: Pancasila menjadi landasan kehidupan bernegara.
fig: table Kedudukan Pancasila | Arti ;; dasar negara | landasan penyelenggaraan negara ;; pandangan hidup | pedoman perilaku warga ;; ideologi negara | cita-cita bangsa ;; sumber hukum | sumber dari segala sumber hukum ;; kepribadian bangsa | ciri khas bangsa Indonesia ;; perjanjian luhur | kesepakatan para pendiri bangsa ~ Kedudukan Pancasila.
@ Nilai Pancasila dalam kehidupan
min: 15
act: Catat satu perilaku sesuai setiap sila yang kamu lakukan di rumah dan sekolah selama seminggu.
mis: mengira nilai Pancasila hanya berlaku saat upacara
exp: Nilai Pancasila terdiri atas nilai ketuhanan, kemanusiaan, persatuan, kerakyatan, dan keadilan. Nilai ini diterapkan dalam kehidupan sehari-hari, misalnya beribadah, menolong sesama, menjaga persatuan, bermusyawarah, dan berlaku adil. Penerapan nilai Pancasila membentuk warga negara yang baik.
ex: Menghormati teman yang berbeda agama (ketuhanan). // Bermusyawarah memilih ketua OSIS (kerakyatan).
pt: Lima nilai dasar ; Diterapkan sehari-hari ; Membentuk warga negara baik
sum: Nilai Pancasila menjadi pedoman perilaku.
fig: table Nilai | Contoh perilaku ;; ketuhanan | beribadah sesuai agama ;; kemanusiaan | menolong korban bencana ;; persatuan | menggunakan produk dalam negeri ;; kerakyatan | bermusyawarah memilih ketua OSIS ;; keadilan | membagi tugas secara adil ;; toleransi | menghormati teman berbeda agama ~ Penerapan nilai Pancasila.
@ Norma dalam kehidupan
min: 15
act: Buat tabel norma yang berlaku di rumah, sekolah, dan masyarakat beserta sanksinya.
mis: mengira norma hukum dan norma kesopanan memiliki sanksi yang sama
exp: Norma adalah aturan yang mengatur perilaku manusia dalam masyarakat. Ada empat norma: norma agama, kesusilaan, kesopanan, dan hukum. Norma agama bersumber dari Tuhan, kesusilaan dari hati nurani, kesopanan dari kebiasaan masyarakat, dan hukum dari negara. Norma hukum memiliki sanksi paling tegas.
ex: Tidak mencontek termasuk norma kesusilaan. // Mematuhi lampu lalu lintas termasuk norma hukum.
pt: Empat jenis norma ; Sumber berbeda-beda ; Sanksi hukum paling tegas
sum: Norma menciptakan ketertiban dalam masyarakat.
fig: table Norma | Sanksi ;; agama | dosa ;; kesusilaan | rasa bersalah ;; kesopanan | celaan masyarakat ;; hukum | denda atau penjara ;; kebiasaan | dianggap aneh ;; tata tertib sekolah | teguran atau poin pelanggaran ~ Jenis norma dan sanksinya.
@ Hak dan kewajiban warga negara
min: 15
act: Cari pasal UUD 1945 tentang hak pendidikan dan kewajiban bela negara.
mis: menuntut hak tanpa menjalankan kewajiban
exp: Hak warga negara antara lain mendapat pendidikan, pekerjaan yang layak, perlindungan hukum, dan kebebasan beragama. Kewajiban warga negara antara lain menaati hukum, membayar pajak, membela negara, dan menghormati hak orang lain. Hak dan kewajiban harus seimbang.
ex: Pasal 31 UUD 1945 mengatur hak mendapat pendidikan. // Pasal 30 mengatur hak dan kewajiban pertahanan negara.
pt: Hak pendidikan dan pekerjaan ; Kewajiban menaati hukum dan pajak ; Hak dan kewajiban seimbang
sum: Warga negara yang baik menjalankan hak dan kewajibannya.
fig: table Hal | Hak atau kewajiban ;; mendapat pendidikan | hak ;; membayar pajak | kewajiban ;; memeluk agama | hak beragama ;; membela negara | hak dan kewajiban ;; menaati hukum | kewajiban hukum ;; mendapat perlindungan hukum | hak perlindungan ~ Hak dan kewajiban warga negara.
@ Lembaga negara
min: 15
act: Cari tahu nama ketua lembaga negara saat ini, lalu buat bagan sederhananya.
mis: mengira DPR adalah lembaga yang menjalankan undang-undang
exp: Lembaga negara menjalankan tugas negara. Presiden menjalankan pemerintahan. MPR mengubah dan menetapkan UUD. DPR membuat undang-undang bersama presiden, menyusun anggaran, dan mengawasi pemerintah. DPD mewakili daerah. Mahkamah Agung dan Mahkamah Konstitusi menjalankan kekuasaan kehakiman. BPK memeriksa keuangan negara.
ex: DPR membahas rancangan undang-undang. // BPK memeriksa penggunaan uang negara.
pt: Presiden menjalankan pemerintahan ; DPR membuat undang-undang ; MA dan MK kekuasaan kehakiman
sum: Lembaga negara saling bekerja sama dan mengawasi.
fig: table Lembaga | Tugas ;; Presiden | menjalankan pemerintahan ;; MPR | mengubah UUD ;; DPR | membuat undang-undang ;; DPD | mewakili daerah ;; Mahkamah Konstitusi | menguji undang-undang terhadap UUD ;; BPK | memeriksa keuangan negara ~ Lembaga negara dan tugasnya.
@ Pemilihan umum
min: 15
act: Tanyakan kepada orang tua pengalaman mereka mengikuti pemilu, lalu catat asas pemilunya.
mis: mengira pilihan dalam pemilu boleh diberitahukan dan dipaksakan
exp: Pemilihan umum atau pemilu adalah sarana rakyat memilih wakilnya dan pemimpin negara. Pemilu di Indonesia berasas langsung, umum, bebas, rahasia, jujur, dan adil atau disingkat luber jurdil. Pemilu diselenggarakan oleh Komisi Pemilihan Umum atau KPU setiap lima tahun.
ex: Pemilih datang langsung ke TPS. // Pilihan setiap pemilih dirahasiakan.
pt: Sarana memilih wakil dan pemimpin ; Asas luber jurdil ; Diselenggarakan KPU
sum: Pemilu adalah wujud kedaulatan rakyat.
fig: table Asas pemilu | Arti ;; langsung | memilih sendiri tanpa perantara ;; umum | semua warga yang memenuhi syarat ;; bebas | tanpa paksaan ;; rahasia | pilihan tidak diketahui orang lain ;; jujur | sesuai aturan tanpa curang ;; adil | perlakuan sama bagi semua ~ Asas pemilu.
# 2|Persatuan dan Kebangsaan
@ Makna Bhinneka Tunggal Ika
min: 15
act: Buat poster yang menunjukkan keberagaman teman sekelasmu dengan semboyan Bhinneka Tunggal Ika.
mis: mengira Bhinneka Tunggal Ika berarti semua harus seragam
exp: Bhinneka Tunggal Ika adalah semboyan bangsa Indonesia yang berarti berbeda-beda tetapi tetap satu. Semboyan ini berasal dari Kitab Sutasoma karya Mpu Tantular pada masa Majapahit. Semboyan ini mengajarkan bahwa keberagaman suku, agama, ras, dan budaya adalah kekuatan pemersatu.
ex: Semboyan tertulis pada pita Garuda Pancasila. // Siswa dari berbagai suku belajar bersama.
pt: Berbeda-beda tetapi tetap satu ; Dari Kitab Sutasoma karya Mpu Tantular ; Keberagaman sebagai kekuatan
sum: Bhinneka Tunggal Ika menyatukan keberagaman.
fig: table Hal | Keterangan ;; arti | berbeda-beda tetapi tetap satu ;; sumber | Kitab Sutasoma ;; pengarang | Mpu Tantular ;; masa | Kerajaan Majapahit ;; letak | pita Garuda Pancasila ;; bahasa | Jawa Kuno ~ Tentang Bhinneka Tunggal Ika.
@ Kebangkitan nasional
min: 15
act: Buat garis waktu pergerakan nasional dari Budi Utomo sampai Sumpah Pemuda.
mis: mengira perjuangan setelah 1908 masih bersifat kedaerahan
exp: Kebangkitan nasional ditandai berdirinya Budi Utomo pada 20 Mei 1908. Sejak itu perjuangan melawan penjajah dilakukan melalui organisasi dan bersifat nasional. Organisasi lain yang muncul antara lain Sarekat Islam, Indische Partij, Muhammadiyah, dan Taman Siswa. Tanggal 20 Mei diperingati sebagai Hari Kebangkitan Nasional.
ex: Budi Utomo didirikan oleh dr. Soetomo dan kawan-kawan. // Taman Siswa didirikan Ki Hajar Dewantara.
pt: Budi Utomo 20 Mei 1908 ; Perjuangan melalui organisasi ; 20 Mei Hari Kebangkitan Nasional
sum: Kebangkitan nasional mengubah cara perjuangan bangsa.
fig: table Organisasi | Tokoh pendiri ;; Budi Utomo | dr. Soetomo ;; Sarekat Islam | H.O.S. Tjokroaminoto ;; Indische Partij | Tiga Serangkai ;; Muhammadiyah | K.H. Ahmad Dahlan ;; Taman Siswa | Ki Hajar Dewantara ;; Nahdlatul Ulama | K.H. Hasyim Asy'ari ~ Organisasi pergerakan nasional.
@ Persatuan dan kesatuan
min: 15
act: Ikut kegiatan kerja kelompok bersama teman dari latar belakang berbeda, lalu tulis kesanmu.
mis: menganggap perbedaan sebagai alasan untuk bermusuhan
exp: Persatuan adalah gabungan dari berbagai unsur yang berbeda menjadi satu. Kesatuan adalah keadaan utuh dan tidak terpecah. Persatuan dan kesatuan dijaga dengan sikap toleransi, cinta tanah air, mengutamakan kepentingan bersama, dan menghindari perpecahan.
ex: Bekerja sama membersihkan lingkungan tanpa membedakan suku. // Tidak menyebarkan berita yang memecah belah.
pt: Persatuan gabungan unsur berbeda ; Kesatuan keadaan utuh ; Dijaga dengan toleransi dan cinta tanah air
sum: Persatuan dan kesatuan adalah kekuatan bangsa.
fig: table Sikap | Dampak ;; toleransi | hidup rukun ;; cinta tanah air | bangga sebagai bangsa ;; mengutamakan kepentingan bersama | tidak egois ;; menghindari hoaks | tidak mudah diadu domba ;; gotong royong | pekerjaan ringan ;; menghargai perbedaan | persatuan kuat ~ Sikap menjaga persatuan.
@ Konflik dan penyelesaiannya
min: 15
act: Ingat satu perselisihan dengan teman, lalu tulis cara damai menyelesaikannya.
mis: menyelesaikan masalah dengan kekerasan
exp: Konflik adalah pertentangan antara individu atau kelompok karena perbedaan kepentingan, pendapat, atau salah paham. Konflik dapat diselesaikan dengan musyawarah, mediasi melalui pihak ketiga, kompromi, atau jalur hukum. Kekerasan tidak menyelesaikan masalah.
ex: Dua siswa berselisih lalu didamaikan oleh wali kelas (mediasi). // Kelompok sepakat saling mengalah (kompromi).
pt: Konflik karena perbedaan ; Diselesaikan dengan musyawarah atau mediasi ; Hindari kekerasan
sum: Konflik diselesaikan dengan cara damai.
fig: table Cara penyelesaian | Arti ;; musyawarah | berunding mencapai mufakat ;; mediasi | dibantu pihak ketiga netral ;; kompromi | saling mengalah ;; arbitrase | diputuskan juru damai ;; jalur hukum | diselesaikan di pengadilan ;; rekonsiliasi | berdamai kembali ~ Cara menyelesaikan konflik.
@ Menghargai keputusan bersama
min: 15
act: Ikut rapat kelas atau keluarga, lalu laksanakan keputusan yang disepakati walaupun berbeda dengan usulmu.
mis: menolak melaksanakan keputusan karena usulnya tidak dipilih
exp: Keputusan bersama diambil melalui musyawarah mufakat atau pemungutan suara. Setelah keputusan diambil, semua peserta wajib menghargai dan melaksanakannya dengan tanggung jawab. Pendapat yang kalah tetap dihargai, dan keputusan dapat dievaluasi kembali melalui musyawarah.
ex: Ketua OSIS terpilih melalui pemungutan suara. // Semua anggota melaksanakan jadwal piket yang disepakati.
pt: Diambil dengan musyawarah atau voting ; Wajib dilaksanakan ; Evaluasi melalui musyawarah
sum: Menghargai keputusan bersama adalah sikap demokratis.
fig: table Situasi | Sikap yang tepat ;; usul tidak dipilih | menerima dengan lapang dada ;; keputusan disepakati | melaksanakan dengan tanggung jawab ;; ada keberatan | menyampaikan dengan sopan ;; voting seimbang | musyawarah ulang ;; tugas dibagi | mengerjakan bagian sendiri ;; hasil kurang baik | evaluasi bersama ~ Sikap terhadap keputusan bersama.
@ Bela negara bagi pelajar
min: 15
act: Buat daftar lima kegiatan bela negara yang bisa kamu lakukan di sekolah.
mis: mengira bela negara hanya kewajiban tentara
exp: Bela negara adalah sikap dan perilaku warga negara yang dijiwai kecintaan kepada Indonesia. Bela negara adalah hak dan kewajiban setiap warga negara sesuai Pasal 27 ayat 3 UUD 1945. Bagi pelajar, bela negara dilakukan dengan belajar sungguh-sungguh, menaati aturan, menjaga lingkungan, dan berprestasi.
ex: Mengikuti upacara bendera dengan khidmat. // Mengharumkan nama sekolah lewat lomba.
pt: Dijiwai cinta tanah air ; Hak dan kewajiban setiap warga ; Pelajar: belajar dan berprestasi
sum: Bela negara dapat dilakukan setiap warga sesuai perannya.
fig: table Peran | Contoh bela negara ;; pelajar | belajar sungguh-sungguh ;; atlet | membela Indonesia di pertandingan ;; petani | menjaga ketahanan pangan ;; guru | mendidik generasi muda ;; tentara | menjaga kedaulatan ;; warga digital | melawan hoaks ~ Bela negara sesuai peran.
"""

BANK += """
## PPK|Pancasila sebagai dasar negara
Pancasila sebagai sumber dari segala sumber … di Indonesia.|hukum|uang|budaya asing|pajak|Hukum.
Peraturan perundang-undangan tidak boleh bertentangan dengan …|Pancasila|peraturan desa|keputusan RT|adat asing|Pancasila.
=|Pancasila sebagai pedoman perilaku warga disebut pandangan …|hidup|Pandangan hidup.
=|Pancasila sebagai cita-cita bangsa disebut …|ideologi;ideologi negara|Ideologi.
B|Pancasila disebut perjanjian luhur bangsa.|Kesepakatan.
S|Pancasila hanya simbol tanpa fungsi.|Dasar negara.
Pancasila sebagai ciri khas bangsa disebut …|kepribadian bangsa|lagu kebangsaan|bahasa nasional|lambang daerah|Kepribadian.
Contoh fungsi Pancasila sebagai dasar negara adalah …|undang-undang dibuat sesuai nilai Pancasila|menghias kelas|menjadi lagu|menjadi tarian|Dasar hukum.
## PPK|Nilai Pancasila dalam kehidupan
Beribadah sesuai agama mencerminkan nilai …|ketuhanan|persatuan|keadilan|kerakyatan|Ketuhanan.
Bermusyawarah memilih ketua OSIS mencerminkan nilai …|kerakyatan|ketuhanan|kemanusiaan|persatuan|Kerakyatan.
=|Menolong korban bencana mencerminkan nilai …|kemanusiaan|Kemanusiaan.
=|Membagi tugas secara adil mencerminkan nilai …|keadilan|Keadilan.
B|Menggunakan produk dalam negeri mencerminkan nilai persatuan.|Persatuan.
S|Nilai Pancasila hanya diterapkan saat upacara.|Setiap hari.
Menghormati teman berbeda agama mencerminkan nilai …|ketuhanan dan toleransi|keadilan ekonomi|kerakyatan|persatuan saja|Toleransi.
Penerapan nilai Pancasila membentuk …|warga negara yang baik|warga yang egois|masyarakat yang terpecah|budaya asing|Warga baik.
## PPK|Norma dalam kehidupan
Norma yang bersumber dari Tuhan adalah norma …|agama|kesopanan|hukum|kesusilaan|Agama.
Norma yang sanksinya paling tegas adalah norma …|hukum|kesopanan|kebiasaan|kesusilaan|Hukum.
=|Norma yang bersumber dari hati nurani adalah norma …|kesusilaan|Kesusilaan.
=|Sanksi norma kesopanan berupa … masyarakat.|celaan|Celaan.
B|Mematuhi lampu lalu lintas termasuk norma hukum.|Hukum.
S|Sanksi norma agama berupa denda dari polisi.|Dosa.
Tidak mencontek saat ulangan termasuk norma …|kesusilaan|hukum|kebiasaan|adat|Kesusilaan.
Norma adalah aturan yang mengatur … manusia.|perilaku|makanan|pakaian saja|cuaca|Perilaku.
## PPK|Hak dan kewajiban warga negara
Pasal UUD 1945 yang mengatur hak pendidikan adalah Pasal …|31|27|30|33|Pasal 31.
Contoh kewajiban warga negara adalah …|membayar pajak|mendapat pendidikan|memeluk agama|mendapat pekerjaan|Pajak.
=|Mendapat perlindungan hukum termasuk … warga negara.|hak|Hak.
=|Menaati hukum termasuk … warga negara.|kewajiban|Kewajiban.
B|Hak dan kewajiban harus seimbang.|Seimbang.
S|Warga negara boleh menuntut hak tanpa menjalankan kewajiban.|Seimbang.
Membela negara merupakan … warga negara.|hak dan kewajiban|hak saja|kewajiban tentara saja|pilihan|Pasal 27 ayat 3.
Memeluk agama sesuai keyakinan termasuk hak …|beragama|pendidikan|pekerjaan|politik|Beragama.
## PPK|Lembaga negara
Lembaga negara yang membuat undang-undang bersama presiden adalah …|DPR|MA|BPK|KPU|DPR.
Lembaga negara yang memeriksa keuangan negara adalah …|BPK|MPR|DPD|MK|BPK.
=|Lembaga yang mengubah dan menetapkan UUD adalah …|MPR|MPR.
=|Lembaga yang mewakili daerah adalah …|DPD|DPD.
B|Mahkamah Konstitusi menguji undang-undang terhadap UUD.|MK.
S|DPR bertugas menjalankan pemerintahan sehari-hari.|Presiden.
Kekuasaan kehakiman dijalankan oleh Mahkamah Agung dan …|Mahkamah Konstitusi|DPR|MPR|BPK|MK.
Presiden menjalankan kekuasaan …|pemerintahan|kehakiman|legislatif|pemeriksaan keuangan|Eksekutif.
## PPK|Pemilihan umum
Asas pemilu di Indonesia disingkat …|luber jurdil|jurdil saja|luber|bebas aktif|Luber jurdil.
Penyelenggara pemilu di Indonesia adalah …|KPU|DPR|BPK|MA|KPU.
=|Pemilu di Indonesia diadakan setiap … tahun.|5;lima|Lima tahun.
=|Tempat pemilih memberikan suara disebut …|TPS|TPS.
B|Asas rahasia berarti pilihan tidak diketahui orang lain.|Rahasia.
S|Dalam pemilu, pemilih boleh dipaksa memilih calon tertentu.|Asas bebas.
Asas yang berarti semua warga yang memenuhi syarat boleh memilih adalah asas …|umum|langsung|rahasia|adil|Umum.
Pemilu adalah wujud kedaulatan …|rakyat|presiden|partai|tentara|Rakyat.
## PPK|Makna Bhinneka Tunggal Ika
Arti Bhinneka Tunggal Ika adalah …|berbeda-beda tetapi tetap satu|bersatu kita teguh|maju terus|merdeka atau mati|Arti.
Semboyan Bhinneka Tunggal Ika berasal dari Kitab …|Sutasoma|Negarakertagama|Pararaton|Arjunawiwaha|Sutasoma.
=|Kitab Sutasoma dikarang oleh Mpu …|Tantular|Mpu Tantular.
=|Semboyan Bhinneka Tunggal Ika tertulis pada pita …|Garuda Pancasila;Garuda|Garuda.
B|Kitab Sutasoma ditulis pada masa Majapahit.|Majapahit.
S|Bhinneka Tunggal Ika berarti semua harus seragam.|Beragam tetapi satu.
Bahasa asal semboyan Bhinneka Tunggal Ika adalah bahasa …|Jawa Kuno|Melayu|Sanskerta modern|Belanda|Jawa Kuno.
Semboyan Bhinneka Tunggal Ika mengajarkan bahwa keberagaman adalah …|kekuatan|kelemahan|ancaman|hambatan|Kekuatan.
## PPK|Kebangkitan nasional
Hari Kebangkitan Nasional diperingati setiap tanggal …|20 Mei|28 Oktober|17 Agustus|10 November|20 Mei.
Budi Utomo didirikan pada tahun …|1908|1928|1945|1912|1908.
=|Pendiri Budi Utomo adalah dr. …|Soetomo;Sutomo|dr. Soetomo.
=|Pendiri Muhammadiyah adalah K.H. Ahmad …|Dahlan|Ahmad Dahlan.
B|Taman Siswa didirikan oleh Ki Hajar Dewantara.|Taman Siswa.
S|Sarekat Islam didirikan oleh dr. Soetomo.|H.O.S. Tjokroaminoto.
Indische Partij didirikan oleh …|Tiga Serangkai|Wali Songo|Panitia Sembilan|BPUPKI|Tiga Serangkai.
Sejak 1908 perjuangan bangsa dilakukan melalui …|organisasi|perang kedaerahan saja|diam|kerja sama dengan penjajah|Organisasi.
## PPK|Persatuan dan kesatuan
Persatuan adalah gabungan dari unsur yang …|berbeda menjadi satu|sama semua|terpecah|bermusuhan|Persatuan.
Kesatuan berarti keadaan …|utuh tidak terpecah|tercerai berai|kacau|terpisah|Utuh.
=|Sikap menghargai perbedaan agama disebut …|toleransi|Toleransi.
=|Bekerja bersama untuk kepentingan umum disebut gotong …|royong|Gotong royong.
B|Menghindari hoaks membantu menjaga persatuan.|Hoaks.
S|Perbedaan suku adalah alasan untuk bermusuhan.|Kekayaan.
Sikap yang mengancam persatuan adalah …|mengutamakan kepentingan kelompok sendiri|bergotong royong|bertoleransi|cinta tanah air|Egois.
Bangga sebagai bangsa Indonesia mencerminkan sikap …|cinta tanah air|egois|primordial|apatis|Cinta tanah air.
## PPK|Konflik dan penyelesaiannya
Penyelesaian konflik dengan bantuan pihak ketiga yang netral disebut …|mediasi|kompromi|kekerasan|voting|Mediasi.
Penyelesaian konflik dengan saling mengalah disebut …|kompromi|mediasi|arbitrase|jalur hukum|Kompromi.
=|Berunding untuk mencapai mufakat disebut …|musyawarah|Musyawarah.
=|Berdamai kembali setelah konflik disebut …|rekonsiliasi|Rekonsiliasi.
B|Kekerasan tidak menyelesaikan masalah.|Damai.
S|Konflik sebaiknya diselesaikan dengan berkelahi.|Damai.
Penyebab konflik dapat berupa …|perbedaan kepentingan|kesamaan hobi|kerja sama|gotong royong|Perbedaan.
Penyelesaian konflik yang diputuskan oleh juru damai disebut …|arbitrase|kompromi|rekonsiliasi|mediasi|Arbitrase.
## PPK|Menghargai keputusan bersama
Keputusan bersama dapat diambil melalui musyawarah atau …|pemungutan suara|undian sembarang|paksaan|kekerasan|Voting.
Sikap ketika usul kita tidak dipilih adalah …|menerima dengan lapang dada|marah dan pergi|menolak melaksanakan|mengejek pemenang|Lapang dada.
=|Keputusan yang telah disepakati wajib …|dilaksanakan|Dilaksanakan.
=|Jika ada keberatan, sampaikan dengan …|sopan;santun|Sopan.
B|Pendapat yang kalah tetap perlu dihargai.|Dihargai.
S|Keputusan bersama boleh diabaikan jika kita tidak setuju.|Wajib dilaksanakan.
Jika hasil voting seimbang, sebaiknya dilakukan …|musyawarah ulang|kekerasan|pembatalan sepihak|pengunduran diri massal|Musyawarah.
Menghargai keputusan bersama mencerminkan sikap …|demokratis|otoriter|egois|apatis|Demokratis.
## PPK|Bela negara bagi pelajar
Dasar hukum bela negara terdapat dalam Pasal 27 ayat …|3|1|2|4|Ayat 3.
Contoh bela negara bagi pelajar adalah …|belajar sungguh-sungguh|membolos|tawuran|mencoret fasilitas|Belajar.
=|Bela negara dijiwai kecintaan kepada …|Indonesia;tanah air|Tanah air.
=|Melawan berita bohong di internet termasuk bela negara warga …|digital|Digital.
B|Bela negara adalah hak dan kewajiban setiap warga negara.|Setiap warga.
S|Bela negara hanya kewajiban tentara.|Semua warga.
Atlet membela negara dengan cara …|berprestasi di pertandingan|tidak berlatih|curang|menolak bertanding|Prestasi.
Petani turut membela negara dengan menjaga ketahanan …|pangan|militer|politik luar negeri|teknologi nuklir|Pangan.
"""

SAS += """
## PPK 1
0|Kedudukan Pancasila sebagai kesepakatan para pendiri bangsa disebut ....|perjanjian luhur|ideologi asing|pandangan kelompok|peraturan daerah|Perjanjian luhur.
1|Menolong korban bencana tanpa membedakan suku mencerminkan nilai ....|kemanusiaan|ketuhanan|kerakyatan|keadilan|Kemanusiaan.
2|Sanksi melanggar norma kebiasaan adalah ....|dianggap aneh|penjara|denda|dosa|Kebiasaan.
3|Pasal 30 UUD 1945 mengatur tentang ....|pertahanan dan keamanan negara|pendidikan|agama|perekonomian|Pasal 30.
4|Lembaga yang mengawasi jalannya pemerintahan dan menyusun anggaran bersama presiden adalah ....|DPR|MA|BPK|KPU|DPR.
5|Asas pemilu yang berarti pemilih memilih tanpa paksaan adalah ....|bebas|rahasia|umum|langsung|Bebas.
## PPK 2
0|Kitab Sutasoma ditulis pada masa Kerajaan ....|Majapahit|Sriwijaya|Mataram Islam|Demak|Majapahit.
1|Nahdlatul Ulama didirikan oleh ....|K.H. Hasyim Asy'ari|K.H. Ahmad Dahlan|dr. Soetomo|Ki Hajar Dewantara|NU.
2|Gotong royong membuat pekerjaan menjadi ....|ringan|berat|lambat|kacau|Ringan.
3|Konflik yang diselesaikan di pengadilan disebut melalui ....|jalur hukum|mediasi|kompromi|rekonsiliasi|Jalur hukum.
4|Jika tugas kelompok dibagi, sikap yang tepat adalah ....|mengerjakan bagian sendiri|menyerahkan kepada teman|tidak mengerjakan|mengeluh|Tanggung jawab.
5|Guru turut membela negara dengan cara ....|mendidik generasi muda|menolak mengajar|membolos|menyebarkan hoaks|Mendidik.
"""

TOPICS += """
## SBD
# 1|Seni Rupa dan Musik
@ Teknik arsir
min: 15
act: Gambar sebuah apel dengan pensil, lalu beri arsiran untuk menunjukkan gelap terang.
mis: mengarsir semua bagian dengan tekanan yang sama
exp: Arsir adalah teknik memberi gelap terang dengan garis-garis. Ada arsir sejajar, arsir silang, dan arsir dengan titik atau pointilis. Bagian yang terkena cahaya diarsir tipis atau dibiarkan terang, sedangkan bagian bayangan diarsir rapat dan tebal.
ex: Bagian bawah apel diarsir lebih gelap. // Arsir silang membuat bayangan lebih pekat.
pt: Memberi gelap terang dengan garis ; Sejajar, silang, titik ; Bayangan diarsir rapat
sum: Arsiran membuat gambar tampak bervolume.
fig: table Jenis arsir | Ciri ;; arsir sejajar | garis searah ;; arsir silang | garis bersilangan ;; pointilis | titik-titik ;; arsir lengkung | mengikuti bentuk benda ;; arsir acak | coretan bebas ;; gradasi | terang ke gelap halus ~ Jenis teknik arsir.
@ Gambar ilustrasi
min: 15
act: Buat gambar ilustrasi untuk satu halaman cerita pendek yang kamu sukai.
mis: membuat ilustrasi yang tidak sesuai isi cerita
exp: Gambar ilustrasi adalah gambar yang menjelaskan atau memperindah sebuah teks atau cerita. Ilustrasi dipakai pada buku cerita, majalah, komik, dan sampul buku. Ilustrasi harus sesuai tema, komunikatif, dan menarik.
ex: Ilustrasi kancil pada buku dongeng. // Ilustrasi sampul majalah anak.
pt: Menjelaskan isi teks ; Dipakai di buku dan majalah ; Sesuai tema dan komunikatif
sum: Ilustrasi membantu pembaca memahami cerita.
fig: table Jenis ilustrasi | Contoh penggunaan ;; ilustrasi buku cerita | gambar dongeng ;; komik | cerita bergambar berpanel ;; karikatur | gambar lucu dilebih-lebihkan ;; kartun | tokoh sederhana dan lucu ;; ilustrasi sampul | halaman depan buku ;; infografis | gambar data dan informasi ~ Jenis gambar ilustrasi.
@ Desain motif
min: 15
act: Buat motif berulang dari bentuk daun pada kertas berpetak, lalu warnai.
mis: menyusun motif tanpa pengulangan yang teratur
exp: Motif adalah gambar dasar yang diulang untuk membentuk pola hias. Motif dapat berupa bentuk geometris, tumbuhan, hewan, atau manusia. Penyusunan motif dapat beraturan, berselang-seling, simetris, atau memusat. Motif banyak dipakai pada kain, keramik, dan dinding.
ex: Motif kawung pada batik tersusun berulang. // Motif bunga disusun berselang-seling.
pt: Gambar dasar yang diulang ; Geometris atau organis ; Disusun teratur
sum: Motif yang tersusun rapi membentuk ragam hias indah.
fig: table Susunan motif | Ciri ;; beraturan | motif sama diulang ;; berselang-seling | dua motif bergantian ;; simetris | kanan kiri seimbang ;; memusat | berpusat di tengah ;; menyebar | motif tersebar merata ;; bebas | tidak terikat aturan ~ Susunan motif.
@ Kaligrafi
min: 15
act: Tulis namamu dengan huruf indah memakai spidol berujung pipih.
mis: menulis kaligrafi tanpa memperhatikan ketebalan dan proporsi huruf
exp: Kaligrafi adalah seni menulis indah. Kaligrafi Arab dikenal dengan berbagai gaya, seperti naskhi, tsuluts, dan diwani. Kaligrafi Latin juga ada, misalnya gaya italic. Alat kaligrafi antara lain kalam, pena berujung pipih, dan kuas. Proporsi dan ketebalan garis menentukan keindahan kaligrafi.
ex: Kaligrafi ayat Al-Qur'an menghiasi dinding masjid. // Kartu ucapan ditulis dengan huruf italic.
pt: Seni menulis indah ; Ada gaya naskhi, tsuluts, diwani ; Perhatikan proporsi dan ketebalan
sum: Kaligrafi memadukan tulisan dan keindahan.
fig: table Gaya kaligrafi Arab | Ciri ;; naskhi | jelas dan mudah dibaca ;; tsuluts | lengkung indah untuk hiasan ;; diwani | miring dan bertumpuk ;; kufi | bersudut tegas ;; riq'ah | sederhana untuk tulisan cepat ;; farisi | condong khas Persia ~ Gaya kaligrafi Arab.
@ Merancang poster
min: 15
act: Rancang poster digital atau di kertas tentang hemat energi dengan gambar dan tulisan singkat.
mis: memenuhi poster dengan tulisan panjang yang sulit dibaca
exp: Poster adalah gambar pada kertas besar yang berisi ajakan atau informasi. Poster yang baik memiliki gambar menarik, tulisan singkat dan jelas, warna kontras, serta tata letak yang mudah dibaca dari jauh. Poster dapat bersifat kegiatan, pendidikan, atau niaga.
ex: Poster ajakan cuci tangan di sekolah. // Poster pentas seni memuat tanggal dan tempat.
pt: Berisi ajakan atau informasi ; Gambar menarik dan tulisan singkat ; Warna kontras dan mudah dibaca
sum: Poster menyampaikan pesan secara cepat.
fig: table Unsur poster | Fungsi ;; judul | menarik perhatian ;; gambar | memperjelas pesan ;; slogan | ajakan singkat ;; warna kontras | mudah terbaca ;; informasi | waktu dan tempat ;; logo | menunjukkan penyelenggara ~ Unsur-unsur poster.
@ Lagu daerah dan karakteristiknya
min: 15
act: Dengarkan tiga lagu daerah, lalu bandingkan tempo, bahasa, dan suasananya.
mis: mengira semua lagu daerah bertempo lambat
exp: Lagu daerah memiliki karakteristik sesuai budaya asalnya, misalnya bahasa daerah, tangga nada, tempo, dan alat musik pengiring. Lagu Ampar-Ampar Pisang bertempo riang, sedangkan Bengawan Solo bertempo lambat. Lagu daerah sering berisi nasihat, cerita kehidupan, atau keindahan alam.
ex: Rasa Sayange dinyanyikan riang. // Yamko Rambe Yamko bersemangat.
pt: Berbahasa daerah ; Tempo dan nada berbeda ; Berisi nasihat atau keindahan alam
sum: Lagu daerah mencerminkan budaya asalnya.
fig: table Lagu daerah | Asal ;; Bengawan Solo | Jawa Tengah ;; Yamko Rambe Yamko | Papua ;; Sinanggar Tulo | Sumatera Utara ;; Anging Mamiri | Sulawesi Selatan ;; Bubuy Bulan | Jawa Barat ;; Cublak-Cublak Suweng | Jawa Tengah dolanan ~ Lagu daerah dan asalnya.
@ Teknik pernapasan bernyanyi
min: 15
act: Latih pernapasan diafragma dengan menghirup napas, menahan, lalu menghembuskan perlahan selama sepuluh detik.
mis: mengangkat bahu saat menghirup napas
exp: Pernapasan yang baik membuat suara stabil dan kuat. Ada pernapasan dada, perut, dan diafragma. Pernapasan diafragma paling baik untuk bernyanyi karena menyimpan udara lebih banyak dan mudah dikendalikan. Saat menghirup napas, perut mengembang dan bahu tetap rileks.
ex: Hirup napas lewat hidung, perut mengembang. // Hembuskan perlahan sambil bersenandung.
pt: Pernapasan dada, perut, diafragma ; Diafragma terbaik untuk bernyanyi ; Bahu tetap rileks
sum: Pernapasan diafragma membuat suara lebih kuat.
fig: table Teknik vokal | Arti ;; pernapasan | cara mengambil napas ;; artikulasi | kejelasan pengucapan ;; intonasi | ketepatan nada ;; resonansi | gema suara ;; phrasering | pemenggalan kalimat lagu ;; vibrato | getaran suara ~ Teknik vokal.
@ Bernyanyi kanon
min: 15
act: Nyanyikan lagu Burung Kakaktua secara kanon bersama keluarga dengan selisih satu birama.
mis: memulai bagian kedua pada saat yang sama dengan bagian pertama
exp: Kanon adalah cara bernyanyi dengan melodi yang sama tetapi dimulai pada waktu berbeda, sehingga terdengar saling menyusul. Unisono adalah bernyanyi bersama dengan nada yang sama. Paduan suara dapat memakai dua suara atau lebih yang berbeda nada.
ex: Kelompok kedua mulai satu birama setelah kelompok pertama. // Lagu Pelangi dapat dinyanyikan secara kanon.
pt: Melodi sama, mulai berbeda ; Unisono nada sama ; Dua suara nada berbeda
sum: Kanon membuat lagu terdengar berlapis.
fig: table Cara bernyanyi | Ciri ;; unisono | satu suara nada sama ;; kanon | melodi sama saling menyusul ;; dua suara | dua nada berbeda harmonis ;; solo | dinyanyikan satu orang ;; duet | dinyanyikan dua orang ;; vokal grup | empat sampai sepuluh penyanyi ~ Cara bernyanyi bersama.
# 2|Tari, Teater, dan Kriya
@ Ragam gerak tari tradisional
min: 15
act: Tirukan gerak tangan dan kaki satu tarian tradisional dari video, lalu sebutkan maknanya.
mis: menarikan gerak tradisional tanpa memahami maknanya
exp: Tari tradisional memiliki ragam gerak yang khas. Gerak maknawi memiliki arti tertentu, misalnya gerak menanam padi. Gerak murni hanya mementingkan keindahan. Ada pula gerak berpindah tempat atau lokomotor dan gerak di tempat. Setiap daerah memiliki ciri gerak, misalnya gerak tangan cepat pada Tari Saman.
ex: Gerak ngigel pada tari Bali. // Gerak tangan menyembah pada tari Jawa.
pt: Gerak maknawi dan murni ; Gerak berpindah dan di tempat ; Setiap daerah punya ciri
sum: Ragam gerak menunjukkan ciri tari daerah.
fig: table Jenis gerak | Arti ;; gerak maknawi | memiliki arti ;; gerak murni | hanya keindahan ;; gerak lokomotor | berpindah tempat ;; gerak di tempat | tanpa berpindah ;; gerak imitatif | menirukan alam atau hewan ;; gerak simbolis | mengandung lambang ~ Jenis gerak tari.
@ Pola lantai tari kelompok
min: 15
act: Rancang pola lantai untuk lima penari di kertas, lalu praktikkan bersama teman.
mis: menyusun penari tanpa memperhatikan penonton dapat melihat semua penari
exp: Pola lantai adalah garis yang dilalui penari di atas panggung. Pada tari kelompok, pola lantai mengatur posisi dan perpindahan penari supaya terlihat indah. Pola lantai garis lurus memberi kesan tegas, sedangkan garis lengkung memberi kesan lembut. Contohnya pola V, pola lingkaran, dan pola diagonal.
ex: Tari Saman memakai pola lantai garis lurus mendatar. // Tari Kecak memakai pola lantai lingkaran.
pt: Garis yang dilalui penari ; Garis lurus kesan tegas ; Garis lengkung kesan lembut
sum: Pola lantai membuat tari kelompok lebih menarik.
fig: table Pola lantai | Kesan ;; garis lurus horizontal | tegas dan sejajar ;; garis lurus vertikal | memanjang ke belakang ;; diagonal | dinamis ;; huruf V | menonjolkan penari depan ;; lingkaran | lembut dan bersatu ;; zigzag | bersemangat ~ Pola lantai dan kesannya.
@ Iringan tari
min: 15
act: Iringi gerak tari sederhana dengan tepukan dan ketukan meja bersama teman.
mis: mengira tari tidak dapat diiringi selain musik
exp: Iringan tari berfungsi memberi irama, membangun suasana, dan memperjelas gerak. Iringan internal berasal dari penari sendiri, seperti tepukan, hentakan kaki, atau nyanyian. Iringan eksternal berasal dari luar penari, seperti gamelan atau musik rekaman.
ex: Tari Saman diiringi tepukan dan nyanyian penari (internal). // Tari Jaipong diiringi kendang (eksternal).
pt: Memberi irama dan suasana ; Internal dari penari ; Eksternal dari luar penari
sum: Iringan membuat tari lebih hidup.
fig: table Iringan | Jenis ;; tepukan tangan penari | internal ;; hentakan kaki | internal dari gerak ;; nyanyian penari | internal suara ;; gamelan | eksternal ;; kendang | eksternal perkusi ;; musik rekaman | eksternal modern ~ Jenis iringan tari.
@ Teater tradisional Nusantara
min: 15
act: Tonton cuplikan lenong, ketoprak, atau randai, lalu catat ciri pertunjukannya.
mis: mengira teater tradisional selalu memakai naskah tertulis
exp: Teater tradisional adalah teater yang tumbuh dari budaya daerah dan diwariskan turun-temurun. Teater tradisional sering tidak memakai naskah tertulis, mengandung humor, melibatkan penonton, dan diiringi musik daerah. Contohnya lenong dari Betawi, ketoprak dari Jawa Tengah, ludruk dari Jawa Timur, randai dari Sumatera Barat, dan makyong dari Riau.
ex: Lenong sering melibatkan penonton dalam canda. // Randai memadukan silat, tari, dan nyanyian.
pt: Tumbuh dari budaya daerah ; Sering tanpa naskah tertulis ; Ada humor dan musik daerah
sum: Teater tradisional adalah warisan budaya daerah.
fig: table Teater tradisional | Asal daerah ;; lenong | Betawi ;; ketoprak | Jawa Tengah ;; ludruk | Jawa Timur ;; randai | Sumatera Barat ;; makyong | Riau ;; mamanda | Kalimantan Selatan ~ Teater tradisional Nusantara.
@ Menulis naskah teater
min: 15
act: Tulis naskah teater pendek tiga adegan tentang persahabatan.
mis: menulis naskah tanpa konflik sehingga cerita datar
exp: Naskah teater berisi dialog dan petunjuk laku. Unsur naskah meliputi tema, tokoh, alur, latar, dialog, dan amanat. Alur teater biasanya terdiri atas pengenalan, konflik, klimaks, penyelesaian, dan penutup. Petunjuk laku ditulis dalam kurung untuk menjelaskan gerak atau suasana.
ex: Adegan 1: dua sahabat bertengkar. // (Rina menunduk sedih) Maafkan aku.
pt: Berisi dialog dan petunjuk laku ; Ada konflik dan klimaks ; Petunjuk laku dalam kurung
sum: Naskah yang baik memiliki konflik yang menarik.
fig: table Bagian alur | Isi ;; pengenalan | memperkenalkan tokoh ;; konflik | munculnya masalah ;; klimaks | puncak masalah ;; penyelesaian | masalah terpecahkan ;; penutup | akhir cerita ;; amanat | pesan untuk penonton ~ Bagian alur naskah teater.
@ Kerajinan dari bahan alam
min: 15
act: Kumpulkan biji-bijian, kerang, atau daun kering, lalu buat hiasan dinding.
mis: memakai bahan alam basah sehingga cepat berjamur
exp: Kerajinan bahan alam memanfaatkan bahan dari alam seperti kayu, bambu, rotan, serat, kerang, batu, dan biji-bijian. Bahan alam perlu dikeringkan dan dibersihkan sebelum dipakai. Kerajinan bahan alam bernilai guna dan bernilai hias.
ex: Tas dari serat eceng gondok. // Bingkai foto dari kerang.
pt: Memanfaatkan bahan dari alam ; Keringkan dan bersihkan dulu ; Bernilai guna dan hias
sum: Bahan alam dapat diolah menjadi kerajinan bernilai.
fig: table Bahan alam | Contoh kerajinan ;; eceng gondok | tas ;; kerang | bingkai foto ;; batok kelapa | gayung ;; rotan | kursi ;; pandan | tikar ;; tempurung dan biji | gantungan kunci ~ Kerajinan dari bahan alam.
@ Kerajinan anyaman bambu
min: 15
act: Buat anyaman sederhana dari bilah bambu tipis atau potongan kertas dengan pola kepang.
mis: memakai bilah bambu yang belum dihaluskan sehingga melukai tangan
exp: Anyaman bambu dibuat dengan menyilangkan bilah bambu secara bergantian. Pola anyaman antara lain anyaman tunggal, ganda, kepang, dan silang. Hasil anyaman bambu antara lain bakul, tampah, besek, dan dinding gedek. Bilah bambu harus dihaluskan dan direndam agar lentur.
ex: Tampah dipakai untuk menampi beras. // Besek dipakai sebagai wadah makanan.
pt: Menyilangkan bilah bambu ; Pola tunggal, ganda, kepang ; Bilah dihaluskan dan direndam
sum: Anyaman bambu adalah kerajinan tradisional yang berguna.
fig: table Hasil anyaman | Kegunaan ;; bakul | wadah nasi ;; tampah | menampi beras ;; besek | wadah makanan ;; gedek | dinding rumah ;; caping | topi petani ;; kukusan | mengukus nasi ~ Hasil anyaman bambu.
@ Seni patung
min: 15
act: Buat patung kecil dari tanah liat atau plastisin berbentuk hewan kesukaanmu.
mis: mengira semua patung dibuat dengan dipahat
exp: Patung adalah karya seni rupa tiga dimensi. Teknik membuat patung antara lain teknik pahat untuk kayu dan batu, teknik butsir untuk tanah liat, teknik cor untuk logam, dan teknik konstruksi atau merakit. Patung dapat berfungsi sebagai monumen, hiasan, atau sarana upacara.
ex: Patung Garuda Wisnu Kencana di Bali. // Patung Asmat dari Papua dipahat dari kayu.
pt: Karya tiga dimensi ; Teknik pahat, butsir, cor, konstruksi ; Monumen, hiasan, upacara
sum: Patung dibuat dengan berbagai teknik dan bahan.
fig: table Teknik | Bahan ;; pahat | kayu atau batu ;; butsir | tanah liat ;; cor | logam ;; konstruksi | rangkaian bahan ;; cetak | gips ;; ukir | sabun atau kayu lunak ~ Teknik dan bahan patung.
"""

BANK += """
## SBD|Teknik arsir
Arsir adalah teknik memberi gelap terang dengan …|garis-garis|warna cat|tempelan kertas|lilin|Garis.
Arsir dengan garis yang bersilangan disebut arsir …|silang|sejajar|lengkung|titik|Silang.
=|Arsir dengan titik-titik disebut …|pointilis|Pointilis.
=|Bagian bayangan diarsir lebih …|rapat;tebal;gelap|Rapat.
B|Arsiran membuat gambar tampak bervolume.|Volume.
S|Bagian yang terkena cahaya diarsir paling gelap.|Terang.
Arsir yang mengikuti bentuk benda disebut arsir …|lengkung|sejajar|acak|silang|Lengkung.
Perubahan dari terang ke gelap secara halus disebut …|gradasi|kontras|tekstur|irama|Gradasi.
## SBD|Gambar ilustrasi
Gambar ilustrasi berfungsi …|menjelaskan isi teks|mengganti teks|menghapus cerita|menyembunyikan pesan|Menjelaskan.
Gambar lucu yang melebih-lebihkan bentuk disebut …|karikatur|ilustrasi buku|infografis|poster|Karikatur.
=|Cerita bergambar yang tersusun dalam panel disebut …|komik|Komik.
=|Gambar yang menyajikan data dan informasi disebut …|infografis|Infografis.
B|Ilustrasi harus sesuai tema cerita.|Sesuai.
S|Ilustrasi boleh tidak berhubungan dengan isi teks.|Harus sesuai.
Gambar tokoh sederhana dan lucu disebut …|kartun|potret|sketsa arsitek|denah|Kartun.
Ilustrasi pada halaman depan buku disebut ilustrasi …|sampul|isi|lampiran|catatan kaki|Sampul.
## SBD|Desain motif
Motif adalah gambar dasar yang …|diulang membentuk pola|digambar sekali|dihapus|disembunyikan|Diulang.
Susunan dua motif yang bergantian disebut …|berselang-seling|beraturan|memusat|bebas|Selang-seling.
=|Susunan motif yang berpusat di tengah disebut …|memusat|Memusat.
=|Susunan motif kanan kiri seimbang disebut …|simetris|Simetris.
B|Motif kawung pada batik tersusun berulang.|Kawung.
S|Motif hanya dapat berupa bentuk manusia.|Banyak jenis.
Motif berbentuk segitiga dan lingkaran disebut motif …|geometris|flora|fauna|manusia|Geometris.
Motif sering dipakai untuk menghias …|kain dan keramik|udara|air minum|suara|Kain.
## SBD|Kaligrafi
Kaligrafi adalah seni …|menulis indah|melukis pemandangan|memahat batu|menganyam bambu|Menulis indah.
Gaya kaligrafi Arab yang jelas dan mudah dibaca adalah …|naskhi|diwani|kufi|tsuluts|Naskhi.
=|Gaya kaligrafi Arab yang bersudut tegas adalah …|kufi|Kufi.
=|Alat tulis kaligrafi tradisional disebut …|kalam|Kalam.
B|Kaligrafi Latin juga ada, misalnya gaya italic.|Latin.
S|Kaligrafi hanya ditulis dalam huruf Arab.|Ada Latin.
Gaya kaligrafi yang miring dan bertumpuk adalah …|diwani|naskhi|riq'ah|kufi|Diwani.
Keindahan kaligrafi ditentukan oleh proporsi dan …|ketebalan garis|harga tinta|ukuran meja|warna kertas saja|Garis.
## SBD|Merancang poster
Poster yang baik memiliki tulisan yang …|singkat dan jelas|panjang sekali|kecil sekali|tanpa makna|Singkat.
Warna kontras pada poster berfungsi agar …|mudah terbaca|sulit dilihat|tampak kusam|lebih murah|Terbaca.
=|Unsur poster yang menarik perhatian pertama kali adalah …|judul|Judul.
=|Ajakan singkat dalam poster disebut …|slogan|Slogan.
B|Poster pentas seni memuat waktu dan tempat.|Informasi.
S|Poster yang baik dipenuhi paragraf panjang.|Singkat.
Logo pada poster menunjukkan …|penyelenggara|harga|cuaca|jumlah penonton|Penyelenggara.
Poster yang menawarkan produk disebut poster …|niaga|kegiatan|pendidikan|layanan|Niaga.
## SBD|Lagu daerah dan karakteristiknya
Lagu Bengawan Solo berasal dari …|Jawa Tengah|Papua|Sumatera Utara|Sulawesi Selatan|Jawa Tengah.
Lagu Anging Mamiri berasal dari …|Sulawesi Selatan|Jawa Barat|Papua|Bali|Sulawesi Selatan.
=|Lagu Sinanggar Tulo berasal dari Sumatera …|Utara|Sumatera Utara.
=|Lagu Bubuy Bulan berasal dari Jawa …|Barat|Jawa Barat.
B|Lagu daerah biasanya memakai bahasa daerah.|Bahasa daerah.
S|Semua lagu daerah bertempo lambat.|Beragam.
Lagu Yamko Rambe Yamko berasal dari …|Papua|Aceh|Bali|Riau|Papua.
Lagu dolanan Cublak-Cublak Suweng berasal dari …|Jawa Tengah|Papua|Maluku|Kalimantan|Jawa.
## SBD|Teknik pernapasan bernyanyi
Pernapasan terbaik untuk bernyanyi adalah pernapasan …|diafragma|dada|bahu|hidung saja|Diafragma.
Saat menghirup napas, bahu sebaiknya …|rileks|terangkat tinggi|tegang|maju|Rileks.
=|Kejelasan pengucapan kata dalam bernyanyi disebut …|artikulasi|Artikulasi.
=|Ketepatan nada dalam bernyanyi disebut …|intonasi|Intonasi.
B|Pernapasan diafragma menyimpan udara lebih banyak.|Lebih banyak.
S|Saat menghirup napas, bahu harus diangkat.|Rileks.
Gema atau pantulan suara dalam bernyanyi disebut …|resonansi|artikulasi|intonasi|phrasering|Resonansi.
Pemenggalan kalimat lagu disebut …|phrasering|vibrato|resonansi|intonasi|Phrasering.
## SBD|Bernyanyi kanon
Kanon adalah bernyanyi dengan melodi sama tetapi dimulai …|pada waktu berbeda|bersamaan|tanpa melodi|dengan nada berbeda|Menyusul.
Bernyanyi bersama dengan nada yang sama disebut …|unisono|kanon|dua suara|duet|Unisono.
=|Lagu yang dinyanyikan dua orang disebut …|duet|Duet.
=|Lagu yang dinyanyikan satu orang disebut …|solo|Solo.
B|Pada kanon, kelompok kedua mulai setelah kelompok pertama.|Menyusul.
S|Pada kanon, semua kelompok mulai bersamaan.|Berbeda waktu.
Kelompok penyanyi empat sampai sepuluh orang disebut …|vokal grup|solo|duet|trio|Vokal grup.
Bernyanyi dua suara berarti memakai dua … berbeda yang harmonis.|nada|lagu|bahasa|panggung|Nada.
## SBD|Ragam gerak tari tradisional
Gerak tari yang memiliki arti tertentu disebut gerak …|maknawi|murni|lokomotor|acak|Maknawi.
Gerak tari yang hanya mementingkan keindahan disebut gerak …|murni|maknawi|simbolis|imitatif|Murni.
=|Gerak berpindah tempat disebut gerak …|lokomotor|Lokomotor.
=|Gerak yang menirukan alam atau hewan disebut gerak …|imitatif|Imitatif.
B|Gerak menanam padi termasuk gerak maknawi.|Maknawi.
S|Semua tari daerah memiliki gerak yang sama.|Beragam.
Tari Saman terkenal dengan gerak … yang cepat.|tangan|kaki melompat|kepala saja|berlari|Tangan.
Gerak yang mengandung lambang disebut gerak …|simbolis|murni|lokomotor|di tempat|Simbolis.
## SBD|Pola lantai tari kelompok
Pola lantai adalah garis yang dilalui … di panggung.|penari|penonton|pemusik|sutradara|Penari.
Pola lantai garis lurus memberi kesan …|tegas|lembut|lemah|sedih|Tegas.
=|Pola lantai garis lengkung memberi kesan …|lembut|Lembut.
=|Tari Kecak memakai pola lantai …|lingkaran|Lingkaran.
B|Pola huruf V menonjolkan penari bagian depan.|V.
S|Pola lantai tidak penting dalam tari kelompok.|Penting.
Pola lantai miring dari sudut ke sudut disebut …|diagonal|horizontal|vertikal|lingkaran|Diagonal.
Pola lantai yang memberi kesan bersemangat adalah …|zigzag|lingkaran|garis lurus diam|titik|Zigzag.
## SBD|Iringan tari
Iringan yang berasal dari penari sendiri disebut iringan …|internal|eksternal|elektronik|rekaman|Internal.
Gamelan termasuk iringan …|eksternal|internal|tepukan|hentakan|Eksternal.
=|Tari Saman diiringi tepukan dan … penari.|nyanyian|Nyanyian.
=|Fungsi iringan adalah memberi …|irama|Irama.
B|Hentakan kaki penari termasuk iringan internal.|Internal.
S|Tari tidak dapat diiringi selain alat musik.|Bisa internal.
Tari Jaipong diiringi alat musik perkusi bernama …|kendang|biola|piano|gitar listrik|Kendang.
Iringan tari dapat membangun …|suasana|panggung|kostum|penonton|Suasana.
## SBD|Teater tradisional Nusantara
Lenong berasal dari …|Betawi|Jawa Timur|Riau|Sumatera Barat|Betawi.
Randai berasal dari …|Sumatera Barat|Riau|Betawi|Jawa Tengah|Sumatera Barat.
=|Ludruk berasal dari Jawa …|Timur|Jawa Timur.
=|Makyong berasal dari …|Riau|Riau.
B|Teater tradisional sering melibatkan penonton.|Interaktif.
S|Teater tradisional selalu memakai naskah tertulis yang baku.|Sering improvisasi.
Ketoprak berasal dari …|Jawa Tengah|Kalimantan Selatan|Betawi|Riau|Jawa Tengah.
Mamanda berasal dari …|Kalimantan Selatan|Jawa Barat|Bali|Papua|Kalimantan Selatan.
## SBD|Menulis naskah teater
Petunjuk laku dalam naskah ditulis di dalam …|kurung|petik|garis bawah|kolom tabel|Kurung.
Puncak masalah dalam alur teater disebut …|klimaks|pengenalan|penutup|konflik awal|Klimaks.
=|Munculnya masalah dalam alur disebut …|konflik|Konflik.
=|Pesan untuk penonton disebut …|amanat|Amanat.
B|Naskah yang baik memiliki konflik.|Konflik.
S|Naskah teater hanya berisi nama tokoh tanpa dialog.|Berisi dialog.
Bagian alur yang memperkenalkan tokoh adalah …|pengenalan|klimaks|penyelesaian|konflik|Pengenalan.
Bagian alur ketika masalah terpecahkan adalah …|penyelesaian|klimaks|konflik|pengenalan|Penyelesaian.
## SBD|Kerajinan dari bahan alam
Tas dapat dibuat dari serat …|eceng gondok|plastik|kaca|besi|Eceng gondok.
Batok kelapa dapat dibuat menjadi …|gayung|kaca jendela|kabel|ban|Gayung.
=|Sebelum dipakai, bahan alam perlu di …|keringkan|Dikeringkan.
=|Kursi tradisional sering dibuat dari …|rotan|Rotan.
B|Kerajinan bahan alam bernilai guna dan hias.|Guna dan hias.
S|Bahan alam basah lebih awet untuk kerajinan.|Mudah berjamur.
Bingkai foto dapat dihias dengan …|kerang|logam berkarat|kaca pecah|paku|Kerang.
Tikar banyak dianyam dari daun …|pandan|jati|pisang kering saja|mangga|Pandan.
## SBD|Kerajinan anyaman bambu
Anyaman bambu dibuat dengan … bilah bambu.|menyilangkan|menempelkan|membakar|mencetak|Menyilang.
Alat untuk menampi beras adalah …|tampah|besek|gedek|caping|Tampah.
=|Wadah nasi dari anyaman bambu disebut …|bakul|Bakul.
=|Topi petani dari anyaman bambu disebut …|caping|Caping.
B|Bilah bambu direndam agar lentur.|Lentur.
S|Bilah bambu yang kasar aman dipakai tanpa dihaluskan.|Dihaluskan.
Dinding rumah dari anyaman bambu disebut …|gedek|tampah|besek|bakul|Gedek.
Alat untuk mengukus nasi dari anyaman bambu disebut …|kukusan|caping|besek|tampah|Kukusan.
## SBD|Seni patung
Patung termasuk karya seni rupa …|tiga dimensi|dua dimensi|satu dimensi|datar|Tiga dimensi.
Teknik membuat patung dari logam adalah teknik …|cor|butsir|pahat kayu|anyam|Cor.
=|Teknik membentuk tanah liat disebut teknik …|butsir|Butsir.
=|Teknik membuat patung kayu disebut teknik …|pahat|Pahat.
B|Patung dapat berfungsi sebagai monumen.|Monumen.
S|Semua patung dibuat dengan teknik pahat.|Banyak teknik.
Patung Asmat berasal dari …|Papua|Bali|Jawa|Sumatra|Papua.
Patung yang dibuat dengan merangkai bahan disebut teknik …|konstruksi|cor|butsir|pahat|Konstruksi.
"""

SAS += """
## SBD 1
0|Coretan bebas untuk memberi bayangan disebut arsir ....|acak|sejajar|silang|lengkung|Acak.
1|Gambar ilustrasi pada buku dongeng berfungsi ....|memperjelas isi cerita|mengganti teks|membuat buku mahal|mengurangi halaman|Ilustrasi.
2|Susunan motif yang tersebar merata disebut ....|menyebar|memusat|simetris|beraturan|Menyebar.
3|Gaya kaligrafi sederhana untuk tulisan cepat adalah ....|riq'ah|tsuluts|kufi|diwani|Riq'ah.
4|Unsur poster yang memperjelas pesan adalah ....|gambar|logo|tanggal|nomor halaman|Gambar.
5|Lagu Bubuy Bulan berasal dari ....|Jawa Barat|Jawa Tengah|Papua|Sumatera Utara|Jawa Barat.
6|Getaran suara saat bernyanyi disebut ....|vibrato|artikulasi|resonansi|phrasering|Vibrato.
7|Lagu yang dinyanyikan tiga orang disebut ....|trio|duet|solo|kanon|Trio.
## SBD 2
0|Gerak tari yang dilakukan tanpa berpindah tempat disebut gerak ....|di tempat|lokomotor|imitatif|murni|Di tempat.
1|Pola lantai garis lurus memanjang ke belakang disebut ....|vertikal|horizontal|diagonal|lingkaran|Vertikal.
2|Musik rekaman termasuk iringan tari ....|eksternal|internal|tepukan|hentakan|Eksternal.
3|Teater tradisional yang memadukan silat, tari, dan nyanyian dari Sumatera Barat adalah ....|randai|lenong|ludruk|ketoprak|Randai.
4|Bagian alur sesudah klimaks adalah ....|penyelesaian|pengenalan|konflik|prolog|Penyelesaian.
5|Gantungan kunci dapat dibuat dari ....|tempurung dan biji|plastik bekas saja|kaca|besi|Bahan alam.
6|Wadah makanan dari anyaman bambu disebut ....|besek|gedek|caping|tampah|Besek.
7|Patung dari gips dibuat dengan teknik ....|cetak|pahat|butsir|cor logam|Cetak.
"""

TOPICS += """
## PJOK
# 1|Permainan dan Atletik
@ Teknik dasar bola voli
min: 15
act: Latih passing bawah ke dinding sebanyak dua puluh kali dengan posisi lutut ditekuk.
mis: memukul bola dengan telapak tangan saat passing bawah
exp: Teknik dasar bola voli meliputi servis, passing bawah, passing atas, smash, dan bendungan atau block. Passing bawah dilakukan dengan kedua lengan dirapatkan lurus dan bola dikenakan pada lengan bawah. Passing atas memakai jari-jari tangan di atas dahi. Satu tim bola voli terdiri atas enam pemain.
ex: Passing bawah untuk menerima servis lawan. // Smash untuk menyerang dengan pukulan keras.
pt: Servis, passing, smash, block ; Passing bawah dengan lengan bawah ; Enam pemain per tim
sum: Penguasaan teknik dasar membuat permainan voli lancar.
fig: table Teknik | Fungsi ;; servis | memulai permainan ;; passing bawah | menerima bola rendah ;; passing atas | mengumpan bola tinggi ;; smash | menyerang dengan keras ;; block | membendung serangan lawan ;; dig | menyelamatkan bola smash ~ Teknik dasar bola voli.
@ Teknik dasar bulu tangkis
min: 15
act: Latih pukulan lob dan servis pendek bersama keluarga memakai raket dan kok.
mis: memegang raket seperti memegang panci sehingga pukulan lemah
exp: Teknik dasar bulu tangkis meliputi cara memegang raket, servis, lob, dropshot, smash, dan netting. Pegangan forehand seperti berjabat tangan dengan raket. Lob memukul kok tinggi ke belakang lapangan lawan, sedangkan dropshot menjatuhkan kok dekat net.
ex: Servis pendek pada permainan ganda. // Smash untuk mematikan lawan.
pt: Pegangan seperti berjabat tangan ; Lob tinggi ke belakang ; Dropshot dekat net
sum: Variasi pukulan membuat lawan sulit menebak.
fig: table Pukulan | Arah kok ;; lob | tinggi ke belakang lapangan ;; dropshot | jatuh dekat net ;; smash | tajam menukik ;; netting | tipis melewati net ;; drive | datar dan cepat ;; servis pendek | rendah melewati net ~ Pukulan bulu tangkis.
@ Lompat jauh
min: 15
act: Ukur lompatanmu di bak pasir sebanyak tiga kali, lalu catat lompatan terjauh.
mis: menginjak melewati papan tumpuan sehingga lompatan didiskualifikasi
exp: Lompat jauh terdiri atas empat tahap: awalan, tumpuan, melayang di udara, dan mendarat. Awalan berupa lari secepat mungkin. Tumpuan dilakukan dengan satu kaki terkuat di papan tumpuan. Gaya melayang ada tiga: jongkok, menggantung, dan berjalan di udara. Pendaratan dengan kedua kaki dan badan condong ke depan.
ex: Gaya jongkok cocok untuk pemula. // Jarak diukur dari papan tumpuan ke bekas pendaratan terdekat.
pt: Awalan, tumpuan, melayang, mendarat ; Tumpuan satu kaki terkuat ; Gaya jongkok, menggantung, berjalan
sum: Kecepatan awalan menentukan jauhnya lompatan.
fig: table Tahap | Gerakan ;; awalan | lari secepat mungkin ;; tumpuan | menolak dengan satu kaki ;; melayang | badan di udara ;; mendarat | kedua kaki di pasir ;; pengukuran | dari papan ke bekas terdekat ;; gaya jongkok | lutut ditarik ke dada ~ Tahap lompat jauh.
@ Tolak peluru gaya menyamping
min: 15
act: Peragakan gerakan tolak peluru memakai bola plastik berisi pasir di halaman.
mis: melempar peluru seperti melempar bola sehingga siku cedera
exp: Tolak peluru adalah gerakan menolak atau mendorong peluru sejauh mungkin, bukan melempar. Peluru diletakkan di pangkal jari dan menempel di leher. Pada gaya menyamping, badan menyamping ke arah tolakan, lalu peluru didorong dengan sudut sekitar 45 derajat. Penolak tidak boleh keluar dari lingkaran.
ex: Peluru ditempelkan di bawah dagu. // Lingkaran tolak peluru berdiameter 2,135 meter.
pt: Didorong, bukan dilempar ; Peluru menempel di leher ; Sudut tolakan sekitar 45 derajat
sum: Tolakan yang benar menghasilkan jarak jauh dan aman.
fig: table Bagian | Keterangan ;; pegangan | peluru di pangkal jari ;; posisi awal | peluru menempel di leher ;; sikap badan | menyamping ke arah tolakan ;; sudut tolakan | sekitar 45 derajat ;; lingkaran | diameter 2,135 meter ;; sektor | daerah jatuhnya peluru ~ Bagian tolak peluru.
@ Teknik dasar pencak silat
min: 15
act: Latih kuda-kuda depan dan pukulan lurus masing-masing sepuluh kali di depan cermin.
mis: berlatih tendangan tanpa pemanasan sehingga otot tegang
exp: Pencak silat adalah bela diri asli Indonesia. Teknik dasarnya meliputi kuda-kuda, sikap pasang, pola langkah, pukulan, tendangan, tangkisan, dan elakan. Kuda-kuda adalah posisi kaki yang kokoh sebagai dasar gerakan. Pencak silat diakui UNESCO sebagai warisan budaya tak benda pada 2019.
ex: Kuda-kuda depan untuk menyerang. // Elakan untuk menghindari serangan.
pt: Bela diri asli Indonesia ; Kuda-kuda dasar gerakan ; Warisan budaya UNESCO 2019
sum: Pencak silat melatih fisik dan sikap sportif.
fig: table Teknik | Fungsi ;; kuda-kuda | dasar berdiri kokoh ;; sikap pasang | siap menyerang atau bertahan ;; pola langkah | berpindah posisi ;; pukulan | menyerang dengan tangan ;; tangkisan | menahan serangan ;; elakan | menghindari serangan ~ Teknik dasar pencak silat.
@ Senam lantai guling
min: 15
act: Latih guling depan di atas matras dengan dagu menempel ke dada, dibantu teman.
mis: menumpu dengan kepala bagian atas sehingga leher cedera
exp: Senam lantai dilakukan di atas matras. Guling depan dilakukan dengan jongkok, kedua tangan menumpu matras, dagu menempel dada, lalu berguling ke depan dengan tengkuk sebagai tumpuan. Guling belakang dilakukan dengan berguling ke belakang, tangan di samping telinga untuk menolak. Gerakan ini melatih kelentukan dan keberanian.
ex: Guling depan diawali sikap jongkok. // Kaki rapat saat berguling.
pt: Dilakukan di atas matras ; Dagu menempel dada ; Tangan di samping telinga saat guling belakang
sum: Teknik yang benar mencegah cedera leher.
fig: table Gerakan senam lantai | Tumpuan utama ;; guling depan | tengkuk ;; guling belakang | punggung dan tangan ;; lenting tangan | kedua tangan ;; meroda | tangan bergantian ;; kayang | tangan dan kaki ;; sikap lilin | bahu ~ Gerakan senam lantai.
@ Latihan kelincahan dan kecepatan
min: 15
act: Lakukan lari bolak-balik 4 x 10 meter dan catat waktumu dengan stopwatch.
mis: melakukan latihan kecepatan tanpa istirahat cukup
exp: Kelincahan adalah kemampuan mengubah arah dengan cepat tanpa kehilangan keseimbangan. Kecepatan adalah kemampuan bergerak secepat-cepatnya dalam waktu singkat. Latihan kelincahan antara lain lari bolak-balik, lari zigzag, dan lari melewati tangga kelincahan. Latihan kecepatan antara lain lari cepat 30 meter.
ex: Lari zigzag melewati kerucut. // Lari cepat 30 meter dari start berdiri.
pt: Kelincahan mengubah arah ; Kecepatan bergerak cepat ; Lari zigzag dan lari cepat
sum: Kelincahan dan kecepatan penting dalam banyak cabang olahraga.
fig: table Latihan | Komponen kebugaran ;; lari bolak-balik | kelincahan ;; lari zigzag | kelincahan mengubah arah ;; lari cepat 30 meter | kecepatan ;; push-up | kekuatan otot lengan ;; sit-up | kekuatan otot perut ;; lari 12 menit | daya tahan jantung ~ Latihan dan komponen kebugaran.
@ Renang gaya bebas
min: 15
act: Latih gerakan kaki gaya bebas sambil berpegangan di tepi kolam dengan pendampingan orang dewasa.
mis: mengangkat kepala terus-menerus sehingga kaki tenggelam
exp: Renang gaya bebas atau crawl adalah gaya renang tercepat. Badan telungkup lurus di permukaan air. Kaki digerakkan naik turun bergantian dari pangkal paha. Tangan mengayuh bergantian ke depan. Napas diambil dengan memiringkan kepala ke samping. Berenang harus selalu diawasi orang dewasa atau penjaga kolam.
ex: Kepala dimiringkan ke kanan saat mengambil napas. // Kaki lurus dan lentur saat menendang.
pt: Gaya renang tercepat ; Kaki naik turun bergantian ; Napas dengan memiringkan kepala
sum: Koordinasi tangan, kaki, dan napas membuat renang efisien.
fig: table Gaya renang | Ciri ;; gaya bebas | tangan mengayuh bergantian ;; gaya dada | gerakan kaki seperti katak ;; gaya punggung | badan telentang ;; gaya kupu-kupu | kedua tangan bersamaan ;; gaya samping | badan miring ;; mengapung | badan diam di permukaan ~ Gaya renang.
# 2|Kebugaran dan Kesehatan
@ Senam irama
min: 15
act: Rangkai empat gerakan senam irama dengan iringan lagu bertempo sedang di rumah.
mis: bergerak tanpa mengikuti ketukan musik
exp: Senam irama adalah senam yang dilakukan dengan iringan musik. Gerakannya harus sesuai irama dan hitungan. Senam irama dapat memakai alat seperti pita, bola, simpai, dan tali. Unsur senam irama meliputi kelentukan, keseimbangan, kontinuitas gerak, dan ketepatan irama.
ex: Langkah rapat dengan hitungan satu sampai delapan. // Senam pita mengikuti alunan musik.
pt: Diiringi musik ; Sesuai irama dan hitungan ; Dapat memakai alat
sum: Senam irama melatih koordinasi dan keindahan gerak.
fig: table Langkah senam irama | Gerakan kaki ;; langkah keseimbangan | jinjit bergantian ;; langkah rapat | kaki dirapatkan ;; langkah depan | melangkah ke depan ;; langkah silang | kaki menyilang ;; langkah samping | bergeser ke samping ;; langkah keper | menekuk lutut sambil melangkah ~ Langkah senam irama.
@ Permainan bola tangan
min: 15
act: Latih mengoper bola ke teman dengan operan setinggi dada dan operan pantul.
mis: membawa bola lebih dari tiga langkah tanpa memantulkan
exp: Bola tangan dimainkan dua tim, masing-masing tujuh pemain termasuk penjaga gawang. Bola dimainkan dengan tangan dan dimasukkan ke gawang lawan. Pemain boleh membawa bola paling banyak tiga langkah dan memegang bola paling lama tiga detik. Teknik dasarnya mengoper, menangkap, menggiring, dan menembak.
ex: Operan setinggi dada ke teman. // Menembak sambil melompat ke gawang.
pt: Tujuh pemain per tim ; Maksimal tiga langkah ; Mengoper, menangkap, menggiring, menembak
sum: Bola tangan melatih kerja sama tim.
fig: table Aturan bola tangan | Ketentuan ;; jumlah pemain | tujuh per tim ;; langkah maksimal | tiga langkah ;; memegang bola | paling lama tiga detik ;; lama permainan | dua babak ;; daerah gawang | hanya penjaga gawang ;; gol | bola melewati garis gawang ~ Aturan bola tangan.
@ Teknik dasar futsal
min: 15
act: Latih menghentikan bola dengan telapak kaki dan mengoper dengan kaki bagian dalam.
mis: mengira aturan futsal sama persis dengan sepak bola
exp: Futsal dimainkan dua tim masing-masing lima pemain di lapangan lebih kecil. Teknik dasarnya passing, control dengan telapak kaki, dribbling, chipping, dan shooting. Bola futsal lebih kecil dan tidak mudah memantul. Tidak ada aturan offside dalam futsal, dan lemparan ke dalam diganti tendangan ke dalam.
ex: Menghentikan bola dengan telapak kaki. // Chipping mencungkil bola melewati lawan.
pt: Lima pemain per tim ; Control dengan telapak kaki ; Tidak ada offside
sum: Futsal menuntut kecepatan dan ketepatan.
fig: table Perbedaan | Futsal ;; jumlah pemain | lima orang ;; bola | kecil dan kurang memantul ;; offside | tidak ada ;; bola keluar samping | tendangan ke dalam ;; lama babak | dua kali dua puluh menit ;; pergantian pemain | tidak terbatas ~ Ciri khas futsal.
@ Lari estafet
min: 15
act: Latih menerima tongkat estafet dengan cara visual dan non-visual bersama tiga teman.
mis: menoleh ke belakang saat menerima tongkat sehingga lari melambat
exp: Lari estafet adalah lari bersambung yang dilakukan empat pelari secara bergantian membawa tongkat. Nomor estafet yang umum adalah 4 x 100 meter dan 4 x 400 meter. Pergantian tongkat dilakukan di zona pergantian. Cara menerima tongkat ada dua: visual dengan melihat dan non-visual tanpa melihat.
ex: Estafet 4 x 100 meter memakai cara non-visual. // Tongkat jatuh di luar zona membuat tim didiskualifikasi.
pt: Empat pelari bergantian ; Pergantian di zona khusus ; Visual dan non-visual
sum: Pergantian tongkat yang mulus menentukan kemenangan.
fig: table Istilah estafet | Arti ;; tongkat | benda yang dibawa bergantian ;; zona pergantian | daerah serah terima ;; visual | menerima sambil melihat ;; non-visual | menerima tanpa melihat ;; pelari pertama | start jongkok ;; pelari terakhir | finis ~ Istilah lari estafet.
@ Pertolongan pertama pada cedera
min: 15
act: Praktikkan metode RICE pada boneka atau teman dengan kompres dingin dan pembalut.
mis: memijat langsung bagian yang terkilir sehingga bengkak bertambah
exp: Cedera olahraga yang umum adalah memar, keseleo, kram, dan luka lecet. Pertolongan pertama cedera ringan memakai metode RICE: Rest atau istirahat, Ice atau kompres dingin, Compression atau dibalut tekan, dan Elevation atau ditinggikan. Cedera berat harus segera ditangani tenaga medis.
ex: Kaki keseleo dikompres es dan ditinggikan. // Kram diatasi dengan peregangan pelan.
pt: Memar, keseleo, kram, lecet ; Metode RICE ; Cedera berat ke tenaga medis
sum: Pertolongan pertama yang tepat mencegah cedera memburuk.
fig: table Huruf RICE | Tindakan ;; R | istirahatkan bagian cedera ;; I | kompres dingin ;; C | balut tekan ;; E | tinggikan dari jantung ;; luka lecet | bersihkan dan tutup ;; kram | regangkan perlahan ~ Pertolongan pertama cedera.
@ Bahaya rokok dan alkohol
min: 15
act: Buat poster ajakan menjauhi rokok dan minuman beralkohol untuk mading sekolah.
mis: mengira rokok elektrik aman bagi remaja
exp: Rokok mengandung nikotin, tar, dan karbon monoksida. Nikotin menyebabkan kecanduan, tar merusak paru-paru, dan karbon monoksida mengurangi oksigen dalam darah. Rokok elektrik juga mengandung nikotin. Alkohol merusak hati, mengganggu kerja otak, dan membahayakan keselamatan. Menolak dengan tegas adalah cara terbaik melindungi diri.
ex: Perokok pasif ikut menghirup asap berbahaya. // Menolak ajakan teman untuk merokok dengan tegas.
pt: Nikotin, tar, karbon monoksida ; Rokok elektrik juga berbahaya ; Alkohol merusak hati dan otak
sum: Menjauhi rokok dan alkohol menjaga kesehatan masa depan.
fig: table Zat | Dampak ;; nikotin | kecanduan ;; tar | merusak paru-paru ;; karbon monoksida | mengurangi oksigen darah ;; alkohol | merusak hati ;; asap rokok pasif | gangguan pernapasan orang sekitar ;; uap rokok elektrik | iritasi saluran napas ~ Zat berbahaya dan dampaknya.
@ Kebersihan lingkungan dan kesehatan
min: 15
act: Periksa tempat air tergenang di rumah, lalu lakukan 3M Plus bersama keluarga.
mis: membiarkan air tergenang di wadah bekas
exp: Lingkungan kotor menjadi sarang penyakit, misalnya demam berdarah, diare, dan tifus. Pencegahan demam berdarah dilakukan dengan 3M Plus: menguras, menutup, dan mendaur ulang barang bekas, ditambah memakai lotion antinyamuk atau menanam tanaman pengusir nyamuk. Cuci tangan pakai sabun mencegah diare.
ex: Menguras bak mandi seminggu sekali. // Membuang sampah pada tempatnya.
pt: Lingkungan kotor sarang penyakit ; 3M Plus cegah demam berdarah ; Cuci tangan cegah diare
sum: Lingkungan bersih mencegah penyakit.
fig: table Penyakit | Penyebab ;; demam berdarah | gigitan nyamuk Aedes aegypti ;; diare | makanan dan air tercemar ;; tifus | bakteri Salmonella typhi ;; malaria | nyamuk Anopheles ;; leptospirosis | air tercemar urine tikus ;; cacingan | tidak memakai alas kaki ~ Penyakit akibat lingkungan kotor.
@ Aktivitas fisik dan kesehatan mental
min: 15
act: Catat suasana hatimu sebelum dan sesudah berolahraga tiga puluh menit selama seminggu.
mis: mengira olahraga hanya bermanfaat bagi tubuh
exp: Aktivitas fisik membantu tubuh menghasilkan endorfin yang membuat perasaan lebih senang. Olahraga teratur mengurangi stres, membantu tidur lebih nyenyak, dan meningkatkan konsentrasi belajar. Remaja dianjurkan beraktivitas fisik sedang sampai berat sekitar 60 menit setiap hari. Olahraga bersama teman juga mempererat hubungan sosial.
ex: Bersepeda sore membuat pikiran segar. // Bermain bola bersama teman mempererat persahabatan.
pt: Menghasilkan endorfin ; Mengurangi stres dan memperbaiki tidur ; Remaja 60 menit sehari
sum: Tubuh aktif membantu pikiran sehat.
fig: table Manfaat | Penjelasan ;; endorfin | perasaan lebih senang ;; stres | berkurang ;; tidur | lebih nyenyak ;; konsentrasi | belajar lebih fokus ;; hubungan sosial | persahabatan erat ;; percaya diri | bangga pada kemampuan diri ~ Manfaat olahraga bagi kesehatan mental.
"""

BANK += """
## PJOK|Teknik dasar bola voli
Jumlah pemain satu tim bola voli adalah …|enam|lima|tujuh|sebelas|Enam.
Passing bawah dilakukan dengan bola dikenakan pada …|lengan bawah|telapak tangan|kepala|jari kaki|Lengan bawah.
=|Pukulan keras untuk menyerang dalam voli disebut …|smash|Smash.
=|Pukulan untuk memulai permainan voli disebut …|servis|Servis.
B|Block berfungsi membendung serangan lawan.|Block.
S|Passing atas dilakukan dengan lengan bawah dirapatkan.|Jari.
Teknik menyelamatkan bola smash lawan disebut …|dig|servis|smash|block|Dig.
Passing atas dilakukan dengan jari-jari tangan di atas …|dahi|perut|lutut|pinggang|Dahi.
## PJOK|Teknik dasar bulu tangkis
Pegangan raket forehand seperti …|berjabat tangan|memegang panci|mengepal|mencubit|Berjabat tangan.
Pukulan yang menjatuhkan kok dekat net disebut …|dropshot|lob|smash|drive|Dropshot.
=|Pukulan kok tinggi ke belakang lapangan disebut …|lob|Lob.
=|Pukulan kok datar dan cepat disebut …|drive|Drive.
B|Smash membuat kok menukik tajam.|Smash.
S|Netting adalah pukulan tinggi ke belakang lapangan.|Dekat net.
Servis pendek banyak dipakai pada permainan …|ganda|tunggal saja|sepak bola|voli|Ganda.
Pukulan tipis melewati net disebut …|netting|lob|smash|drive|Netting.
## PJOK|Lompat jauh
Tahap pertama lompat jauh adalah …|awalan|mendarat|melayang|tumpuan|Awalan.
Tumpuan lompat jauh dilakukan dengan …|satu kaki terkuat|dua kaki|tangan|lutut|Satu kaki.
=|Lompat jauh mendarat di bak …|pasir|Pasir.
=|Gaya lompat jauh yang cocok untuk pemula adalah gaya …|jongkok|Jongkok.
B|Jarak lompatan diukur dari papan tumpuan ke bekas pendaratan terdekat.|Pengukuran.
S|Menginjak melewati papan tumpuan tetap dihitung sah.|Diskualifikasi.
Gaya lompat jauh dengan kaki seperti melangkah di udara adalah gaya …|berjalan di udara|jongkok|menggantung|guling|Berjalan.
Pendaratan lompat jauh yang benar dengan badan condong ke …|depan|belakang|samping kiri|atas|Depan.
## PJOK|Tolak peluru gaya menyamping
Peluru dalam tolak peluru harus …|didorong|dilempar|ditendang|dipukul|Didorong.
Sudut tolakan peluru yang baik sekitar …|45 derajat|90 derajat|10 derajat|180 derajat|45 derajat.
=|Sebelum ditolak, peluru menempel di …|leher;dagu|Leher.
=|Peluru dipegang dengan pangkal …|jari|Jari.
B|Penolak tidak boleh keluar dari lingkaran.|Lingkaran.
S|Peluru dilempar dengan ayunan tangan seperti melempar bola.|Didorong.
Diameter lingkaran tolak peluru adalah …|2,135 meter|5 meter|1 meter|10 meter|2,135 m.
Daerah jatuhnya peluru disebut …|sektor|zona estafet|bak pasir|garis start|Sektor.
## PJOK|Teknik dasar pencak silat
Pencak silat adalah bela diri asli …|Indonesia|Jepang|Korea|Cina|Indonesia.
Posisi kaki kokoh sebagai dasar gerakan silat disebut …|kuda-kuda|elakan|tangkisan|pukulan|Kuda-kuda.
=|Gerakan menghindari serangan disebut …|elakan|Elakan.
=|Gerakan menahan serangan disebut …|tangkisan|Tangkisan.
B|Pencak silat diakui UNESCO sebagai warisan budaya tak benda.|UNESCO 2019.
S|Latihan tendangan sebaiknya tanpa pemanasan.|Pemanasan.
Sikap siap menyerang atau bertahan disebut sikap …|pasang|tidur|duduk|santai|Pasang.
Pencak silat diakui UNESCO pada tahun …|2019|2009|1999|2023|2019.
## PJOK|Senam lantai guling
Senam lantai dilakukan di atas …|matras|aspal|pasir|rumput basah|Matras.
Saat guling depan, dagu menempel ke …|dada|lutut|lantai|bahu|Dada.
=|Tumpuan utama guling depan adalah …|tengkuk|Tengkuk.
=|Gerakan membentuk lengkungan dengan tangan dan kaki disebut …|kayang|Kayang.
B|Guling depan diawali sikap jongkok.|Jongkok.
S|Guling depan menumpu pada kepala bagian atas.|Tengkuk.
Gerakan berputar menyamping dengan tangan bergantian disebut …|meroda|kayang|sikap lilin|guling depan|Meroda.
Sikap lilin bertumpu pada …|bahu|tangan|lutut|kepala|Bahu.
## PJOK|Latihan kelincahan dan kecepatan
Kemampuan mengubah arah dengan cepat disebut …|kelincahan|kekuatan|kelentukan|daya tahan|Kelincahan.
Lari zigzag melatih …|kelincahan|kekuatan lengan|kelentukan|daya tahan otot perut|Kelincahan.
=|Push-up melatih kekuatan otot …|lengan|Lengan.
=|Sit-up melatih kekuatan otot …|perut|Perut.
B|Lari cepat 30 meter melatih kecepatan.|Kecepatan.
S|Latihan kecepatan tidak memerlukan istirahat.|Perlu istirahat.
Lari 12 menit melatih …|daya tahan jantung|kelincahan|kelentukan|kekuatan jari|Daya tahan.
Lari bolak-balik melatih …|kelincahan|kelentukan|kekuatan|keseimbangan statis|Kelincahan.
## PJOK|Renang gaya bebas
Gaya renang tercepat adalah gaya …|bebas|dada|punggung|samping|Bebas.
Pada gaya bebas, napas diambil dengan …|memiringkan kepala|mengangkat kepala tinggi|menyelam|berhenti|Miring.
=|Gaya renang dengan badan telentang disebut gaya …|punggung|Punggung.
=|Gaya renang dengan kaki seperti katak disebut gaya …|dada|Dada.
B|Berenang harus diawasi orang dewasa.|Keselamatan.
S|Pada gaya bebas, kepala diangkat terus-menerus.|Kaki tenggelam.
Gaya renang dengan kedua tangan bersamaan adalah gaya …|kupu-kupu|bebas|punggung|samping|Kupu-kupu.
Gerakan kaki gaya bebas berasal dari pangkal …|paha|lutut|jari|pergelangan saja|Paha.
## PJOK|Senam irama
Senam irama dilakukan dengan iringan …|musik|peluit saja|tepuk tangan penonton|sirene|Musik.
Alat yang dapat dipakai dalam senam irama adalah …|pita|raket|peluru|tongkat estafet|Pita.
=|Langkah dengan kaki menyilang disebut langkah …|silang|Silang.
=|Langkah dengan menekuk lutut sambil melangkah disebut langkah …|keper|Keper.
B|Gerakan senam irama harus sesuai hitungan.|Hitungan.
S|Senam irama boleh tidak mengikuti ketukan musik.|Irama.
Langkah dengan berjinjit bergantian disebut langkah …|keseimbangan|silang|rapat|samping|Keseimbangan.
Alat senam irama berbentuk lingkaran disebut …|simpai|pita|tali|bola|Simpai.
## PJOK|Permainan bola tangan
Jumlah pemain satu tim bola tangan adalah …|tujuh|lima|enam|sebelas|Tujuh.
Pemain bola tangan boleh membawa bola paling banyak …|tiga langkah|lima langkah|sepuluh langkah|satu langkah|Tiga langkah.
=|Bola tangan dimainkan dengan …|tangan|Tangan.
=|Pemain memegang bola paling lama … detik.|3;tiga|Tiga detik.
B|Daerah gawang hanya boleh dimasuki penjaga gawang.|Gawang.
S|Bola tangan dimainkan dengan kaki.|Tangan.
Permainan bola tangan terdiri atas …|dua babak|empat babak|lima set|tiga babak|Dua babak.
Operan setinggi dada disebut operan …|dada|pantul|lambung|samping|Dada.
## PJOK|Teknik dasar futsal
Jumlah pemain satu tim futsal adalah …|lima|tujuh|sebelas|enam|Lima.
Menghentikan bola dalam futsal sering memakai …|telapak kaki|lutut|kepala|tangan|Telapak.
=|Teknik mencungkil bola melewati lawan disebut …|chipping|Chipping.
=|Bola keluar samping dalam futsal diganti tendangan ke …|dalam|Dalam.
B|Futsal tidak mengenal aturan offside.|Tanpa offside.
S|Aturan futsal sama persis dengan sepak bola.|Berbeda.
Lama satu babak futsal adalah …|20 menit|45 menit|10 menit|30 menit|20 menit.
Bola futsal bersifat …|kecil dan kurang memantul|besar dan sangat memantul|ringan seperti voli|berbentuk lonjong|Kurang memantul.
## PJOK|Lari estafet
Jumlah pelari dalam satu tim estafet adalah …|empat|tiga|lima|enam|Empat.
Serah terima tongkat dilakukan di zona …|pergantian|start|finis|penonton|Zona pergantian.
=|Menerima tongkat sambil melihat disebut cara …|visual|Visual.
=|Menerima tongkat tanpa melihat disebut cara …|non-visual;nonvisual|Non-visual.
B|Estafet 4 x 100 meter biasa memakai cara non-visual.|Non-visual.
S|Pelari boleh menyerahkan tongkat di mana saja.|Zona.
Pelari pertama estafet memakai start …|jongkok|berdiri|melayang|duduk|Jongkok.
Nomor estafet yang umum dilombakan adalah …|4 x 100 meter|2 x 50 meter|3 x 1.000 meter|5 x 5 meter|4 x 100.
## PJOK|Pertolongan pertama pada cedera
Huruf I dalam RICE berarti …|kompres dingin|istirahat|balut tekan|tinggikan|Ice.
Huruf E dalam RICE berarti …|tinggikan bagian cedera|istirahat|kompres hangat|lari pelan|Elevation.
=|Huruf R dalam RICE berarti …|istirahat;rest|Rest.
=|Huruf C dalam RICE berarti balut …|tekan|Compression.
B|Cedera berat harus segera ditangani tenaga medis.|Medis.
S|Bagian yang terkilir sebaiknya langsung dipijat keras.|Memperparah.
Kram otot diatasi dengan …|meregangkan perlahan|memukul otot|berlari lagi|kompres panas langsung|Peregangan.
Luka lecet ditangani dengan …|dibersihkan dan ditutup|dibiarkan kotor|ditaburi pasir|digaruk|Bersihkan.
## PJOK|Bahaya rokok dan alkohol
Zat dalam rokok yang menyebabkan kecanduan adalah …|nikotin|vitamin|oksigen|kalsium|Nikotin.
Zat dalam rokok yang merusak paru-paru adalah …|tar|nikotin saja|air|garam|Tar.
=|Karbon monoksida mengurangi … dalam darah.|oksigen|Oksigen.
=|Alkohol merusak organ …|hati|Hati.
B|Perokok pasif ikut menghirup asap berbahaya.|Pasif.
S|Rokok elektrik aman bagi remaja.|Mengandung nikotin.
Cara terbaik menolak ajakan merokok adalah …|menolak dengan tegas|mencoba sedikit|diam saja|ikut supaya diterima|Tegas.
Alkohol dapat mengganggu kerja …|otak|kuku|rambut|gigi saja|Otak.
## PJOK|Kebersihan lingkungan dan kesehatan
Demam berdarah ditularkan oleh nyamuk …|Aedes aegypti|Anopheles|Culex saja|lalat|Aedes.
Malaria ditularkan oleh nyamuk …|Anopheles|Aedes aegypti|kecoak|tikus|Anopheles.
=|3M Plus terdiri atas menguras, menutup, dan … ulang.|mendaur|Mendaur ulang.
=|Leptospirosis ditularkan melalui air tercemar urine …|tikus|Tikus.
B|Cuci tangan pakai sabun mencegah diare.|Diare.
S|Air tergenang di wadah bekas tidak berbahaya.|Sarang nyamuk.
Cacingan dapat dicegah dengan memakai …|alas kaki|topi|kacamata|sarung tangan saja|Alas kaki.
Tifus disebabkan oleh bakteri …|Salmonella typhi|Aedes|Anopheles|ragi|Salmonella.
## PJOK|Aktivitas fisik dan kesehatan mental
Zat yang membuat perasaan senang setelah berolahraga adalah …|endorfin|nikotin|tar|karbon monoksida|Endorfin.
Remaja dianjurkan beraktivitas fisik sekitar …|60 menit setiap hari|5 menit seminggu|sekali sebulan|10 jam sehari|60 menit.
=|Olahraga teratur membantu tidur lebih …|nyenyak|Nyenyak.
=|Olahraga teratur mengurangi …|stres|Stres.
B|Olahraga bersama teman mempererat hubungan sosial.|Sosial.
S|Olahraga hanya bermanfaat bagi tubuh, tidak bagi pikiran.|Pikiran juga.
Olahraga teratur meningkatkan … belajar.|konsentrasi|kemalasan|kantuk|kecemasan|Konsentrasi.
Bangga pada kemampuan diri setelah berolahraga meningkatkan …|percaya diri|rasa takut|stres|rasa malas|Percaya diri.
"""

SAS += """
## PJOK 1
0|Teknik voli untuk mengumpan bola tinggi kepada smasher adalah ....|passing atas|servis|block|dig|Passing atas.
1|Pukulan bulu tangkis yang mengarahkan kok tajam menukik adalah ....|smash|lob|netting|servis pendek|Smash.
2|Gaya lompat jauh dengan badan melenting di udara disebut gaya ....|menggantung|jongkok|berjalan|guling|Menggantung.
3|Sikap badan pada tolak peluru gaya menyamping adalah ....|menyamping ke arah tolakan|membelakangi sektor|telentang|melompat tinggi|Menyamping.
4|Teknik pencak silat untuk berpindah posisi disebut ....|pola langkah|kuda-kuda|tangkisan|pukulan|Pola langkah.
5|Gerakan senam lantai yang bertumpu pada kedua tangan dengan kaki melenting adalah ....|lenting tangan|sikap lilin|guling depan|kayang|Lenting tangan.
6|Komponen kebugaran yang dilatih dengan sit-up adalah ....|kekuatan otot perut|kelincahan|kecepatan|kelentukan|Sit-up.
7|Gaya renang dengan badan miring disebut gaya ....|samping|bebas|dada|kupu-kupu|Samping.
## PJOK 2
0|Langkah senam irama dengan bergeser ke samping disebut langkah ....|samping|silang|keper|rapat|Samping.
1|Dalam bola tangan, gol terjadi jika bola ....|melewati garis gawang|keluar lapangan|ditendang|dipantulkan dua kali|Gol.
2|Pergantian pemain dalam futsal bersifat ....|tidak terbatas|hanya tiga kali|tidak boleh|sekali saja|Tak terbatas.
3|Pelari terakhir dalam lari estafet bertugas ....|mencapai garis finis|memulai lomba|menunggu di start|menjadi wasit|Finis.
4|Tujuan meninggikan bagian yang cedera adalah ....|mengurangi bengkak|mempercepat lari|menambah nyeri|memanaskan otot|Elevation.
5|Asap rokok elektrik dapat menyebabkan ....|iritasi saluran napas|tulang kuat|mata tajam|otot besar|Iritasi.
6|Penyakit yang ditularkan nyamuk Aedes aegypti adalah ....|demam berdarah|malaria|tifus|cacingan|DBD.
7|Manfaat olahraga bagi kesehatan mental adalah ....|mengurangi stres|menambah cemas|mengganggu tidur|menurunkan konsentrasi|Stres.
"""

TOPICS += """
## INF
# 1|Komputer dan Pengolahan Dokumen
@ Berpikir komputasional
min: 15
act: Tuliskan langkah-langkah membuat teh manis dalam urutan algoritma yang jelas.
mis: mengira berpikir komputasional hanya untuk pemrogram
exp: Berpikir komputasional adalah cara menyelesaikan masalah secara sistematis. Ada empat fondasinya: dekomposisi atau memecah masalah, pengenalan pola, abstraksi atau memilih informasi penting, dan algoritma atau langkah penyelesaian berurutan. Cara berpikir ini berguna dalam kehidupan sehari-hari.
ex: Memecah tugas kliping menjadi mencari, menggunting, dan menempel (dekomposisi). // Menyusun resep langkah demi langkah (algoritma).
pt: Dekomposisi dan pengenalan pola ; Abstraksi dan algoritma ; Berguna sehari-hari
sum: Berpikir komputasional membantu menyelesaikan masalah dengan teratur.
fig: table Fondasi | Arti ;; dekomposisi | memecah masalah menjadi bagian kecil ;; pengenalan pola | menemukan kesamaan ;; abstraksi | memilih informasi penting ;; algoritma | langkah penyelesaian berurutan ;; evaluasi | memeriksa solusi ;; generalisasi | menerapkan solusi ke masalah serupa ~ Fondasi berpikir komputasional.
@ Sistem operasi
min: 15
act: Periksa sistem operasi di HP atau komputer keluargamu beserta versinya.
mis: mengira sistem operasi sama dengan aplikasi biasa
exp: Sistem operasi adalah perangkat lunak utama yang mengatur perangkat keras dan menjalankan aplikasi. Tugasnya mengelola memori, berkas, proses, dan perangkat masukan keluaran. Contoh sistem operasi komputer adalah Windows, macOS, dan Linux. Contoh sistem operasi HP adalah Android dan iOS.
ex: Android menjalankan aplikasi di HP. // Windows mengatur printer yang terpasang.
pt: Mengatur perangkat keras ; Mengelola memori dan berkas ; Windows, Linux, Android
sum: Tanpa sistem operasi, komputer tidak dapat dipakai.
fig: table Sistem operasi | Perangkat ;; Windows | komputer pribadi ;; macOS | komputer Apple ;; Linux | komputer dan server ;; Android | HP berbagai merek ;; iOS | iPhone ;; ChromeOS | Chromebook ~ Contoh sistem operasi.
@ Bilangan biner
min: 15
act: Ubah tanggal lahirmu menjadi bilangan biner memakai tabel nilai tempat 16, 8, 4, 2, 1.
mis: membaca bilangan biner seperti bilangan desimal
exp: Komputer menyimpan data dalam bilangan biner yang hanya memakai angka 0 dan 1. Setiap angka biner disebut bit, dan delapan bit membentuk satu byte. Nilai tempat biner dari kanan adalah 1, 2, 4, 8, 16, dan seterusnya. Contohnya biner 101 sama dengan 4 + 0 + 1 = 5.
ex: Biner 110 = 4 + 2 + 0 = 6. // Desimal 9 = biner 1001.
pt: Hanya angka 0 dan 1 ; 8 bit = 1 byte ; Nilai tempat 1, 2, 4, 8, 16
sum: Bilangan biner adalah bahasa dasar komputer.
fig: table Desimal | Biner ;; 1 | 1 ;; 2 | 10 ;; 3 | 11 ;; 4 | 100 ;; 5 | 101 ;; 8 | 1000 ~ Desimal dan biner.
@ Mengelola berkas dan folder
min: 15
act: Rapikan berkas tugas di komputer atau HP ke dalam folder per mata pelajaran.
mis: menyimpan semua berkas di satu tempat dengan nama acak
exp: Berkas atau file adalah kumpulan data yang disimpan dengan nama dan ekstensi tertentu. Folder adalah wadah untuk mengelompokkan berkas. Pengelolaan berkas meliputi membuat folder, memberi nama yang jelas, menyalin, memindahkan, dan menghapus. Ekstensi menunjukkan jenis berkas, misalnya .docx untuk dokumen dan .jpg untuk gambar.
ex: Folder Matematika berisi tugas_aljabar.docx. // Berkas foto berekstensi .jpg.
pt: Berkas punya nama dan ekstensi ; Folder mengelompokkan berkas ; Ekstensi menunjukkan jenis
sum: Berkas yang tertata mudah dicari.
fig: table Ekstensi | Jenis berkas ;; .docx | dokumen pengolah kata ;; .xlsx | lembar kerja ;; .pptx | presentasi ;; .jpg | gambar foto ;; .mp3 | audio ;; .pdf | dokumen siap cetak ~ Ekstensi berkas.
@ Pengolah kata
min: 15
act: Ketik satu paragraf tentang sekolahmu, lalu atur judul tebal, rata kiri kanan, dan beri gambar.
mis: menekan spasi berkali-kali untuk merapikan teks
exp: Pengolah kata adalah aplikasi untuk membuat dan mengedit dokumen, misalnya Microsoft Word, Google Docs, dan LibreOffice Writer. Fitur utamanya meliputi format huruf, perataan paragraf, penomoran, menyisipkan gambar dan tabel, serta mengatur ukuran kertas dan margin. Perataan teks dilakukan dengan tombol perataan, bukan dengan spasi.
ex: Judul dibuat tebal dengan Ctrl+B. // Paragraf diratakan kiri kanan atau justify.
pt: Word, Google Docs, Writer ; Format huruf dan paragraf ; Sisipkan gambar dan tabel
sum: Pengolah kata memudahkan membuat dokumen rapi.
fig: table Pintasan | Fungsi ;; Ctrl+B | huruf tebal ;; Ctrl+I | huruf miring ;; Ctrl+U | garis bawah ;; Ctrl+C | menyalin ;; Ctrl+V | menempel ;; Ctrl+Z | membatalkan ~ Pintasan pengolah kata.
@ Aplikasi presentasi
min: 15
act: Buat presentasi lima salindia tentang hobimu dengan sedikit teks dan banyak gambar.
mis: memenuhi salindia dengan paragraf panjang
exp: Aplikasi presentasi dipakai untuk membuat salindia atau slide yang ditampilkan saat menyampaikan materi, misalnya PowerPoint, Google Slides, dan LibreOffice Impress. Presentasi yang baik memakai teks singkat berupa poin, gambar pendukung, warna kontras, dan ukuran huruf yang mudah dibaca. Animasi dipakai secukupnya.
ex: Satu salindia berisi tiga sampai lima poin. // Transisi antar salindia memakai efek sederhana.
pt: PowerPoint, Slides, Impress ; Teks singkat dan gambar ; Animasi secukupnya
sum: Presentasi yang baik membantu pendengar memahami materi.
fig: table Istilah presentasi | Arti ;; salindia | satu halaman presentasi ;; transisi | efek pergantian salindia ;; animasi | efek gerak pada objek ;; tema | gaya desain keseluruhan ;; tata letak | susunan isi salindia ;; catatan pembicara | catatan untuk penyaji ~ Istilah aplikasi presentasi.
@ Keamanan perangkat dan virus
min: 15
act: Periksa apakah HP atau komputermu memakai kata sandi dan pembaruan sistem terbaru.
mis: membuka lampiran dari pengirim tidak dikenal
exp: Malware adalah perangkat lunak jahat, misalnya virus, worm, trojan, dan ransomware. Malware dapat merusak data, mencuri informasi, atau mengunci perangkat. Cara melindungi perangkat antara lain memasang antivirus, memperbarui sistem, memakai kata sandi kuat, dan tidak mengunduh aplikasi dari sumber tidak resmi.
ex: Ransomware mengunci data dan meminta tebusan. // Aplikasi diunduh hanya dari toko resmi.
pt: Virus, worm, trojan, ransomware ; Merusak atau mencuri data ; Antivirus dan pembaruan sistem
sum: Kebiasaan aman melindungi perangkat dari malware.
fig: table Jenis malware | Cara kerja ;; virus | menempel pada berkas lain ;; worm | menyebar sendiri lewat jaringan ;; trojan | menyamar sebagai program berguna ;; ransomware | mengunci data minta tebusan ;; spyware | memata-matai pengguna ;; adware | menampilkan iklan mengganggu ~ Jenis malware.
@ Sejarah perkembangan komputer
min: 15
act: Buat garis waktu perkembangan komputer dari generasi pertama sampai sekarang.
mis: mengira komputer sejak awal berukuran kecil seperti laptop
exp: Komputer berkembang melalui beberapa generasi. Generasi pertama memakai tabung hampa dan berukuran sebesar ruangan, contohnya ENIAC. Generasi kedua memakai transistor, generasi ketiga memakai IC atau sirkuit terpadu, generasi keempat memakai mikroprosesor, dan generasi kelima mengembangkan kecerdasan artifisial.
ex: ENIAC dibuat tahun 1946. // Mikroprosesor membuat komputer pribadi menjadi kecil.
pt: Tabung hampa, transistor, IC ; Mikroprosesor generasi keempat ; Generasi kelima kecerdasan artifisial
sum: Komputer semakin kecil, cepat, dan pintar.
fig: table Generasi | Teknologi utama ;; pertama | tabung hampa ;; kedua | transistor ;; ketiga | IC sirkuit terpadu ;; keempat | mikroprosesor ;; kelima | kecerdasan artifisial ;; masa kini | komputasi awan dan perangkat bergerak ~ Generasi komputer.
# 2|Internet dan Lembar Kerja
@ Cara kerja internet
min: 15
act: Gambarkan perjalanan data saat kamu membuka sebuah situs web dari HP sampai server.
mis: mengira internet sama dengan satu komputer besar
exp: Internet adalah jaringan komputer yang saling terhubung di seluruh dunia. Data dikirim dalam potongan kecil bernama paket. Setiap perangkat memiliki alamat IP. Saat membuka situs web, browser menghubungi DNS untuk mengubah nama domain menjadi alamat IP, lalu meminta halaman dari server.
ex: Nama domain sekolah.sch.id diubah menjadi alamat IP oleh DNS. // Halaman web dikirim dari server ke browser.
pt: Jaringan seluruh dunia ; Data dikirim dalam paket ; DNS mengubah domain menjadi IP
sum: Internet bekerja dengan alamat dan paket data.
fig: table Istilah internet | Arti ;; alamat IP | alamat perangkat di jaringan ;; DNS | penerjemah nama domain ;; server | penyedia layanan dan data ;; browser | aplikasi penjelajah web ;; paket data | potongan data yang dikirim ;; ISP | penyedia layanan internet ~ Istilah cara kerja internet.
@ Mesin pencari
min: 15
act: Cari informasi tentang candi Borobudur memakai kata kunci yang berbeda, lalu bandingkan hasilnya.
mis: memakai kalimat panjang tanpa kata kunci saat mencari
exp: Mesin pencari adalah layanan untuk mencari informasi di internet, misalnya Google dan Bing. Pencarian efektif memakai kata kunci yang tepat. Tanda kutip mencari frasa persis, tanda minus mengecualikan kata, dan site: membatasi pencarian pada situs tertentu. Hasil pencarian perlu diperiksa kebenaran sumbernya.
ex: "Candi Borobudur" mencari frasa persis. // banjir site:bmkg.go.id mencari di situs BMKG.
pt: Google dan Bing ; Kata kunci tepat ; Kutip, minus, site:
sum: Teknik pencarian yang tepat menghemat waktu.
fig: table Teknik pencarian | Fungsi ;; tanda kutip | mencari frasa persis ;; tanda minus | mengecualikan kata ;; site: | membatasi pada situs tertentu ;; filetype: | mencari jenis berkas ;; OR | salah satu kata ;; kata kunci singkat | hasil lebih relevan ~ Teknik mesin pencari.
@ Surel
min: 15
act: Tulis draf surel sopan kepada guru untuk mengirim tugas lengkap dengan subjek dan lampiran.
mis: mengirim surel tanpa subjek dan salam
exp: Surel atau email adalah surat elektronik yang dikirim lewat internet. Alamat surel terdiri atas nama pengguna, tanda @, dan nama domain. Bagian surel meliputi penerima, CC, subjek, isi, dan lampiran. Surel resmi ditulis dengan sopan, ada salam, isi jelas, dan penutup.
ex: siswa@sekolah.sch.id adalah contoh alamat surel. // Subjek: Tugas IPA Kelas 7A.
pt: Surat elektronik lewat internet ; Nama pengguna, @, domain ; Sopan dan bersubjek
sum: Surel yang baik jelas dan sopan.
fig: table Bagian surel | Fungsi ;; penerima | alamat tujuan ;; CC | tembusan terlihat ;; BCC | tembusan tersembunyi ;; subjek | judul singkat surel ;; isi | pesan utama ;; lampiran | berkas yang dikirim ~ Bagian surel.
@ Komputasi awan
min: 15
act: Simpan satu berkas tugas di layanan penyimpanan awan, lalu buka dari perangkat lain.
mis: mengira berkas di awan tersimpan di udara tanpa server
exp: Komputasi awan adalah layanan komputer yang diakses lewat internet, misalnya penyimpanan, aplikasi, dan server. Data sebenarnya disimpan di pusat data milik penyedia. Keuntungannya data dapat diakses dari mana saja dan mudah dibagikan. Kekurangannya memerlukan internet dan perlu menjaga keamanan akun.
ex: Google Drive menyimpan berkas di awan. // Dokumen dapat diedit bersama secara daring.
pt: Layanan lewat internet ; Data di pusat data ; Akses dari mana saja
sum: Komputasi awan memudahkan berbagi dan menyimpan data.
fig: table Layanan awan | Contoh ;; penyimpanan berkas | Google Drive ;; surel | Gmail ;; dokumen daring | Google Docs ;; rapat video | Google Meet ;; penyimpanan foto | Google Photos ;; kelas daring | Google Classroom ~ Contoh layanan awan.
@ Bijak bermedia sosial
min: 15
act: Periksa pengaturan privasi akun media sosial keluarga, lalu diskusikan informasi yang tidak boleh dibagikan.
mis: membagikan alamat rumah dan nomor HP di unggahan publik
exp: Media sosial memudahkan berkomunikasi, tetapi perlu dipakai dengan bijak. Jaga data pribadi, seperti alamat, nomor HP, dan kata sandi. Berpikir sebelum mengunggah, hormati orang lain, dan jangan menyebarkan hoaks. Jejak digital sulit dihapus dan dapat memengaruhi masa depan.
ex: Tidak mengunggah foto tiket yang memuat kode pemesanan. // Melaporkan akun yang melakukan perundungan.
pt: Jaga data pribadi ; Berpikir sebelum mengunggah ; Jejak digital sulit dihapus
sum: Bijak bermedia sosial melindungi diri dan orang lain.
fig: table Perilaku | Bijak atau tidak ;; mengunggah alamat rumah | tidak bijak ;; menyebarkan hoaks | tidak bijak dan merugikan ;; mengatur privasi akun | bijak ;; melaporkan perundungan | bijak dan peduli ;; berkomentar kasar | tidak sopan ;; mengecek fakta sebelum membagikan | bijak dan kritis ~ Perilaku bermedia sosial.
@ Hak cipta dan lisensi
min: 15
act: Cari gambar berlisensi bebas pakai, lalu tulis sumbernya pada tugasmu.
mis: memakai karya orang lain tanpa menyebutkan sumber
exp: Hak cipta adalah hak eksklusif pencipta atas karyanya, seperti tulisan, lagu, gambar, dan program. Memakai karya orang lain harus seizin pencipta atau sesuai lisensinya. Lisensi Creative Commons mengizinkan pemakaian dengan syarat tertentu. Plagiarisme adalah mengaku karya orang lain sebagai milik sendiri.
ex: Mencantumkan sumber gambar pada presentasi. // Perangkat lunak bajakan melanggar hak cipta.
pt: Hak eksklusif pencipta ; Pakai sesuai izin atau lisensi ; Plagiarisme dilarang
sum: Menghargai hak cipta berarti menghargai pencipta.
fig: table Istilah | Arti ;; hak cipta | hak eksklusif pencipta ;; lisensi | izin pemakaian karya ;; Creative Commons | lisensi berbagi bersyarat ;; domain publik | bebas dipakai siapa saja ;; plagiarisme | mengaku karya orang lain ;; pembajakan | menggandakan tanpa izin ~ Istilah hak cipta.
@ Grafik di lembar kerja
min: 15
act: Masukkan data jumlah buku yang dibaca anggota keluarga ke lembar kerja, lalu buat grafik batang.
mis: memakai grafik lingkaran untuk data perubahan dari waktu ke waktu
exp: Lembar kerja dapat mengubah data menjadi grafik agar mudah dibaca. Grafik batang untuk membandingkan jumlah, grafik garis untuk perubahan dari waktu ke waktu, dan grafik lingkaran untuk menunjukkan bagian dari keseluruhan. Grafik perlu diberi judul, label sumbu, dan keterangan.
ex: Grafik garis menunjukkan suhu harian selama seminggu. // Grafik lingkaran menunjukkan persentase hobi siswa.
pt: Batang membandingkan ; Garis perubahan waktu ; Lingkaran bagian keseluruhan
sum: Grafik yang tepat membuat data mudah dipahami.
fig: table Jenis grafik | Cocok untuk ;; batang | membandingkan jumlah ;; garis | perubahan dari waktu ke waktu ;; lingkaran | bagian dari keseluruhan ;; area | jumlah kumulatif ;; sebar | hubungan dua data ;; batang bertumpuk | komposisi tiap kategori ~ Jenis grafik lembar kerja.
@ Rumus dan fungsi lembar kerja
min: 15
act: Hitung total dan rata-rata nilai ulanganmu memakai fungsi SUM dan AVERAGE.
mis: menulis rumus tanpa tanda sama dengan di awal
exp: Lembar kerja seperti Excel dan Google Sheets dapat menghitung otomatis dengan rumus dan fungsi. Rumus selalu diawali tanda sama dengan. Fungsi umum meliputi SUM untuk menjumlah, AVERAGE untuk rata-rata, MAX untuk nilai terbesar, MIN untuk nilai terkecil, dan COUNT untuk menghitung banyak data.
ex: =SUM(B2:B6) menjumlah sel B2 sampai B6. // =MAX(C2:C10) mencari nilai tertinggi.
pt: Diawali tanda sama dengan ; SUM, AVERAGE, MAX, MIN ; COUNT menghitung banyak data
sum: Fungsi lembar kerja mempercepat perhitungan.
fig: table Fungsi | Kegunaan ;; SUM | menjumlahkan ;; AVERAGE | rata-rata ;; MAX | nilai terbesar ;; MIN | nilai terkecil ;; COUNT | banyak data angka ;; IF | memilih hasil berdasarkan syarat ~ Fungsi lembar kerja.
"""

BANK += """
## INF|Berpikir komputasional
Memecah masalah besar menjadi bagian kecil disebut …|dekomposisi|abstraksi|algoritma|evaluasi|Dekomposisi.
Memilih informasi penting dan mengabaikan yang tidak perlu disebut …|abstraksi|dekomposisi|pengenalan pola|generalisasi|Abstraksi.
=|Langkah penyelesaian masalah yang berurutan disebut …|algoritma|Algoritma.
=|Menemukan kesamaan antar masalah disebut pengenalan …|pola|Pola.
B|Berpikir komputasional berguna dalam kehidupan sehari-hari.|Sehari-hari.
S|Berpikir komputasional hanya untuk pemrogram.|Semua orang.
Menerapkan solusi ke masalah serupa disebut …|generalisasi|dekomposisi|abstraksi|evaluasi|Generalisasi.
Menyusun resep langkah demi langkah termasuk …|algoritma|abstraksi|pengenalan pola|dekomposisi|Algoritma.
## INF|Sistem operasi
Sistem operasi untuk iPhone adalah …|iOS|Android|Windows|Linux|iOS.
Contoh sistem operasi komputer adalah …|Windows|WhatsApp|Chrome|Excel|Windows.
=|Sistem operasi HP berbagai merek yang paling banyak dipakai adalah …|Android|Android.
=|Sistem operasi untuk Chromebook adalah …|ChromeOS|ChromeOS.
B|Sistem operasi mengelola memori dan berkas.|Tugas.
S|Sistem operasi sama dengan aplikasi permainan.|Perangkat lunak utama.
Sistem operasi yang banyak dipakai di server adalah …|Linux|iOS|Paint|Word|Linux.
Sistem operasi untuk komputer Apple adalah …|macOS|Android|Windows|ChromeOS|macOS.
## INF|Bilangan biner
Bilangan biner hanya memakai angka …|0 dan 1|1 sampai 9|0 sampai 7|1 dan 2|0 dan 1.
Delapan bit sama dengan satu …|byte|kilobyte|megabyte|digit|Byte.
=|Bilangan biner 101 dalam desimal adalah …|5|Lima.
=|Bilangan desimal 4 dalam biner adalah …|100|100.
B|Biner 110 sama dengan 6.|4+2.
S|Biner 10 sama dengan sepuluh dalam desimal.|Dua.
Bilangan desimal 9 dalam biner adalah …|1001|1010|111|1100|1001.
Bilangan biner 1000 dalam desimal adalah …|8|1000|4|16|Delapan.
## INF|Mengelola berkas dan folder
Wadah untuk mengelompokkan berkas disebut …|folder|ekstensi|aplikasi|ikon|Folder.
Ekstensi berkas gambar foto adalah …|.jpg|.docx|.mp3|.xlsx|.jpg.
=|Ekstensi berkas lembar kerja Excel adalah …|.xlsx;xlsx|.xlsx.
=|Ekstensi berkas audio musik adalah …|.mp3;mp3|.mp3.
B|Ekstensi menunjukkan jenis berkas.|Jenis.
S|Semua berkas sebaiknya disimpan di satu tempat dengan nama acak.|Tertata.
Ekstensi berkas dokumen siap cetak adalah …|.pdf|.jpg|.mp3|.exe|.pdf.
Ekstensi berkas presentasi adalah …|.pptx|.docx|.xlsx|.jpg|.pptx.
## INF|Pengolah kata
Pintasan untuk membuat huruf tebal adalah …|Ctrl+B|Ctrl+I|Ctrl+U|Ctrl+Z|Ctrl+B.
Contoh aplikasi pengolah kata adalah …|Google Docs|Google Sheets|Paint|Photoshop|Docs.
=|Pintasan untuk membatalkan perintah adalah Ctrl+ …|Z|Ctrl+Z.
=|Pintasan untuk huruf miring adalah Ctrl+ …|I|Ctrl+I.
B|Perataan teks sebaiknya memakai tombol perataan.|Tombol.
S|Spasi berkali-kali adalah cara terbaik merapikan teks.|Perataan.
Pintasan untuk menempel adalah …|Ctrl+V|Ctrl+C|Ctrl+B|Ctrl+Z|Ctrl+V.
Perataan teks rata kiri kanan disebut …|justify|left|center|right|Justify.
## INF|Aplikasi presentasi
Satu halaman presentasi disebut …|salindia|sel|folder|tab|Salindia.
Efek pergantian antar salindia disebut …|transisi|animasi|tema|tata letak|Transisi.
=|Efek gerak pada objek di salindia disebut …|animasi|Animasi.
=|Gaya desain keseluruhan presentasi disebut …|tema|Tema.
B|Presentasi yang baik memakai teks singkat.|Singkat.
S|Salindia sebaiknya dipenuhi paragraf panjang.|Poin.
Contoh aplikasi presentasi adalah …|PowerPoint|Excel|Paint|Notepad|PowerPoint.
Catatan yang hanya dilihat penyaji disebut …|catatan pembicara|tema|transisi|animasi|Catatan.
## INF|Keamanan perangkat dan virus
Malware yang mengunci data dan meminta tebusan adalah …|ransomware|adware|worm|spyware|Ransomware.
Malware yang menyamar sebagai program berguna adalah …|trojan|virus|worm|adware|Trojan.
=|Malware yang memata-matai pengguna disebut …|spyware|Spyware.
=|Malware yang menampilkan iklan mengganggu disebut …|adware|Adware.
B|Aplikasi sebaiknya diunduh dari toko resmi.|Resmi.
S|Membuka lampiran dari pengirim tak dikenal selalu aman.|Berbahaya.
Malware yang menyebar sendiri lewat jaringan adalah …|worm|trojan|adware|ransomware|Worm.
Program untuk melindungi perangkat dari malware adalah …|antivirus|malware|spyware|trojan|Antivirus.
## INF|Sejarah perkembangan komputer
Komputer generasi pertama memakai …|tabung hampa|mikroprosesor|transistor|IC|Tabung hampa.
Contoh komputer generasi pertama adalah …|ENIAC|laptop|tablet|HP pintar|ENIAC.
=|Komputer generasi kedua memakai …|transistor|Transistor.
=|Komputer generasi keempat memakai …|mikroprosesor|Mikroprosesor.
B|Komputer generasi pertama berukuran sebesar ruangan.|Besar.
S|Komputer sejak awal berukuran sebesar laptop.|Besar.
Komputer generasi ketiga memakai …|IC sirkuit terpadu|tabung hampa|kecerdasan artifisial|transistor saja|IC.
Komputer generasi kelima mengembangkan …|kecerdasan artifisial|tabung hampa|kartu berlubang|transistor|KA.
## INF|Cara kerja internet
Penerjemah nama domain menjadi alamat IP adalah …|DNS|ISP|browser|router|DNS.
Data di internet dikirim dalam potongan kecil bernama …|paket|bit tunggal|folder|halaman|Paket.
=|Alamat setiap perangkat di jaringan disebut alamat …|IP|IP.
=|Aplikasi untuk menjelajah web disebut …|browser;peramban|Browser.
B|Internet adalah jaringan komputer seluruh dunia.|Global.
S|Internet adalah satu komputer besar.|Jaringan.
Penyedia layanan internet disebut …|ISP|DNS|IP|server lokal|ISP.
Komputer yang menyediakan halaman web disebut …|server|klien|browser|monitor|Server.
## INF|Mesin pencari
Contoh mesin pencari adalah …|Google|Word|Excel|Paint|Google.
Tanda untuk mencari frasa persis adalah …|tanda kutip|tanda minus|tanda tanya|tanda seru|Kutip.
=|Tanda untuk mengecualikan kata dalam pencarian adalah tanda …|minus|Minus.
=|Perintah untuk membatasi pencarian pada situs tertentu adalah …|site:;site|site:.
B|Hasil pencarian perlu diperiksa kebenaran sumbernya.|Periksa.
S|Kalimat panjang tanpa kata kunci memberi hasil paling tepat.|Kata kunci.
Perintah untuk mencari jenis berkas tertentu adalah …|filetype:|site:|OR|tanda kutip|filetype.
Perintah untuk mencari salah satu kata adalah …|OR|AND NOT|minus|kutip|OR.
## INF|Surel
Alamat surel selalu memuat tanda …|@|#|&|%|@.
Bagian surel yang berisi judul singkat adalah …|subjek|lampiran|CC|isi|Subjek.
=|Berkas yang dikirim bersama surel disebut …|lampiran|Lampiran.
=|Tembusan surel yang tersembunyi disebut …|BCC|BCC.
B|Surel resmi sebaiknya ada salam dan penutup.|Sopan.
S|Surel kepada guru tidak perlu subjek.|Perlu.
Tembusan surel yang terlihat oleh penerima lain disebut …|CC|BCC|subjek|lampiran|CC.
Contoh alamat surel yang benar adalah …|siswa@sekolah.sch.id|siswa.sekolah.sch.id|@siswa|siswa#sekolah|Format.
## INF|Komputasi awan
Data komputasi awan sebenarnya disimpan di …|pusat data penyedia|udara|awan di langit|flashdisk pengguna|Pusat data.
Contoh layanan penyimpanan awan adalah …|Google Drive|Paint|Notepad|Kalkulator|Drive.
=|Komputasi awan diakses melalui …|internet|Internet.
=|Layanan rapat video Google disebut Google …|Meet|Meet.
B|Data di awan dapat diakses dari mana saja.|Akses.
S|Komputasi awan tidak memerlukan internet.|Perlu internet.
Kekurangan komputasi awan adalah …|memerlukan internet|tidak bisa berbagi|tidak bisa disimpan|hanya satu perangkat|Internet.
Layanan kelas daring dari Google adalah …|Google Classroom|Google Maps|Google Translate|Google Earth|Classroom.
## INF|Bijak bermedia sosial
Informasi yang tidak boleh dibagikan di unggahan publik adalah …|alamat rumah|hobi umum|makanan favorit|warna kesukaan|Data pribadi.
Jejak digital bersifat …|sulit dihapus|hilang sendiri|tidak penting|tidak terlihat siapa pun|Sulit dihapus.
=|Berita bohong yang disebarkan disebut …|hoaks|Hoaks.
=|Mengatur siapa yang dapat melihat unggahan disebut pengaturan …|privasi|Privasi.
B|Melaporkan akun perundung termasuk perilaku bijak.|Peduli.
S|Membagikan nomor HP di unggahan publik itu aman.|Berbahaya.
Sebelum membagikan berita, kita sebaiknya …|mengecek fakta|langsung membagikan|menambah bumbu|menyebarkan ke semua grup|Cek fakta.
Berkomentar kasar di media sosial termasuk perilaku …|tidak sopan|bijak|kritis|peduli|Tidak sopan.
## INF|Hak cipta dan lisensi
Mengaku karya orang lain sebagai milik sendiri disebut …|plagiarisme|lisensi|domain publik|hak cipta|Plagiarisme.
Lisensi berbagi bersyarat yang populer adalah …|Creative Commons|ransomware|DNS|IP|CC.
=|Izin pemakaian suatu karya disebut …|lisensi|Lisensi.
=|Karya yang bebas dipakai siapa saja disebut domain …|publik|Domain publik.
B|Mencantumkan sumber gambar menghargai pencipta.|Sumber.
S|Perangkat lunak bajakan boleh dipakai bebas.|Melanggar.
Menggandakan karya tanpa izin disebut …|pembajakan|lisensi|kutipan|parafrase|Pembajakan.
Hak eksklusif pencipta atas karyanya disebut …|hak cipta|hak pakai|hak suara|hak milik tanah|Hak cipta.
## INF|Grafik di lembar kerja
Grafik untuk menunjukkan perubahan dari waktu ke waktu adalah grafik …|garis|lingkaran|batang bertumpuk|sebar|Garis.
Grafik untuk menunjukkan bagian dari keseluruhan adalah grafik …|lingkaran|garis|sebar|area|Lingkaran.
=|Grafik untuk membandingkan jumlah adalah grafik …|batang|Batang.
=|Grafik untuk menunjukkan hubungan dua data adalah grafik …|sebar|Sebar.
B|Grafik perlu diberi judul dan label sumbu.|Judul.
S|Grafik lingkaran paling tepat untuk suhu harian seminggu.|Garis.
Grafik yang menunjukkan komposisi tiap kategori adalah grafik …|batang bertumpuk|garis|sebar|lingkaran tunggal|Bertumpuk.
Grafik yang menunjukkan jumlah kumulatif adalah grafik …|area|sebar|lingkaran|batang tunggal|Area.
## INF|Rumus dan fungsi lembar kerja
Rumus di lembar kerja selalu diawali tanda …|sama dengan|tambah|kurung|bintang|=.
Fungsi untuk menjumlahkan adalah …|SUM|AVERAGE|MAX|COUNT|SUM.
=|Fungsi untuk mencari rata-rata adalah …|AVERAGE|AVERAGE.
=|Fungsi untuk mencari nilai terbesar adalah …|MAX|MAX.
B|=SUM(B2:B6) menjumlah sel B2 sampai B6.|Rentang.
S|Rumus lembar kerja tidak perlu diawali tanda sama dengan.|Perlu.
Fungsi untuk mencari nilai terkecil adalah …|MIN|MAX|SUM|IF|MIN.
Fungsi untuk menghitung banyak data angka adalah …|COUNT|SUM|AVERAGE|MAX|COUNT.
"""

SAS += """
## INF 1
0|Memeriksa apakah solusi sudah benar termasuk fondasi ....|evaluasi|dekomposisi|abstraksi|pengenalan pola|Evaluasi.
1|Sistem operasi yang dipakai pada iPhone adalah ....|iOS|Android|Linux|ChromeOS|iOS.
2|Bilangan desimal 3 dalam biner adalah ....|11|10|100|111|11.
3|Ekstensi .docx menunjukkan berkas ....|dokumen pengolah kata|gambar|audio|video|Dokumen.
4|Pintasan Ctrl+C berfungsi untuk ....|menyalin|menempel|membatalkan|menebalkan|Menyalin.
5|Susunan isi pada satu salindia disebut ....|tata letak|transisi|animasi|tema|Tata letak.
6|Virus komputer bekerja dengan cara ....|menempel pada berkas lain|menampilkan iklan saja|mempercepat komputer|membersihkan data|Virus.
7|Generasi komputer masa kini ditandai dengan ....|komputasi awan dan perangkat bergerak|tabung hampa|kartu berlubang|transistor saja|Masa kini.
## INF 2
0|Paket data dikirim melalui internet dalam bentuk ....|potongan kecil|satu berkas utuh|kertas|gelombang suara|Paket.
1|Pencarian "harimau sumatra" -kebun binatang berarti ....|mengecualikan kata kebun binatang|hanya kebun binatang|mencari gambar|mencari video|Minus.
2|Bagian surel berisi pesan utama disebut ....|isi|subjek|CC|lampiran|Isi.
3|Layanan menyimpan foto di awan dari Google adalah ....|Google Photos|Google Maps|Google Meet|Google Forms|Photos.
4|Mengecek fakta sebelum membagikan berita termasuk sikap ....|bijak dan kritis|tidak sopan|merugikan|egois|Bijak.
5|Karya yang masa hak ciptanya sudah habis menjadi ....|domain publik|bajakan|plagiat|rahasia|Domain publik.
6|Data persentase hobi siswa paling tepat disajikan dengan grafik ....|lingkaran|garis|sebar|area|Lingkaran.
7|Fungsi IF pada lembar kerja dipakai untuk ....|memilih hasil berdasarkan syarat|menjumlahkan|mencari rata-rata|menghitung data|IF.
"""

TOPICS += """
## KKA
# 1|Dasar Pemrograman
@ Tipe data
min: 15
act: Tulis lima data tentang dirimu, lalu tentukan tipe datanya: bilangan bulat, desimal, teks, atau boolean.
mis: menyimpan angka sebagai teks lalu mencoba menjumlahkannya
exp: Tipe data menentukan jenis nilai yang disimpan dalam variabel. Tipe data dasar dalam Python antara lain integer untuk bilangan bulat, float untuk bilangan desimal, string untuk teks, dan boolean untuk nilai benar atau salah. Teks ditulis di antara tanda kutip.
ex: umur = 13 bertipe integer. // nama = "Sari" bertipe string.
pt: Integer dan float ; String di antara tanda kutip ; Boolean True atau False
sum: Tipe data yang tepat membuat program bekerja benar.
fig: table Contoh nilai | Tipe data ;; 13 | integer ;; 1.65 | float ;; "Sari" | string ;; True | boolean ;; [1, 2, 3] | list ;; "13" | string berisi angka ~ Contoh tipe data Python.
@ Operator aritmetika
min: 15
act: Hitung 17 dibagi 5 memakai operator /, //, dan % di Python atau kalkulator, lalu bandingkan.
mis: mengira operator % menghitung persen
exp: Operator aritmetika dipakai untuk menghitung. Dalam Python, + untuk tambah, - untuk kurang, * untuk kali, / untuk bagi menghasilkan desimal, // untuk pembagian bulat, % untuk sisa bagi, dan ** untuk pangkat. Urutan operasi mengikuti aturan matematika, yaitu pangkat, kali bagi, lalu tambah kurang.
ex: 17 // 5 = 3. // 17 % 5 = 2.
pt: + - * / ; // pembagian bulat ; % sisa bagi dan ** pangkat
sum: Operator membuat program dapat menghitung.
fig: table Operasi | Hasil ;; 7 + 3 | 10 ;; 7 * 3 | 21 ;; 7 / 2 | 3.5 ;; 7 // 2 | 3 ;; 7 % 2 | 1 ;; 2 ** 3 | 8 ~ Operator aritmetika Python.
@ Percabangan if-else
min: 15
act: Tulis aturan rumah dalam bentuk jika-maka-selain itu, misalnya jika hujan maka bawa payung.
mis: lupa menulis titik dua dan indentasi setelah if
exp: Percabangan membuat program memilih tindakan berdasarkan syarat. Dalam Python ditulis dengan if, elif, dan else. Jika syarat if benar, perintah di bawahnya dijalankan. Jika salah, program memeriksa elif atau menjalankan else. Setiap baris if diakhiri titik dua dan perintah di dalamnya ditulis menjorok.
ex: if nilai >= 75: print("Lulus") // else: print("Remedial")
pt: Memilih tindakan berdasarkan syarat ; if, elif, else ; Titik dua dan indentasi
sum: Percabangan membuat program dapat mengambil keputusan.
fig: table Operator pembanding | Arti ;; == | sama dengan ;; != | tidak sama dengan ;; > | lebih dari ;; < | kurang dari ;; >= | lebih dari atau sama dengan ;; <= | kurang dari atau sama dengan ~ Operator pembanding.
@ Perulangan for dan while
min: 15
act: Tulis algoritma mencetak angka 1 sampai 10 memakai perulangan, lalu jalankan di Python.
mis: membuat while tanpa mengubah syarat sehingga berulang terus
exp: Perulangan menjalankan perintah berulang kali. Perulangan for dipakai jika banyak ulangan sudah diketahui, misalnya for i in range(5). Perulangan while dipakai selama syarat masih benar. Pada while, syarat harus berubah agar perulangan berhenti; jika tidak, terjadi perulangan tanpa akhir.
ex: for i in range(1, 11): print(i) // while n > 0: n = n - 1
pt: For jika banyak ulangan diketahui ; While selama syarat benar ; Hindari perulangan tanpa akhir
sum: Perulangan menghemat penulisan perintah yang sama.
fig: table Perintah | Hasil ;; range(5) | 0 sampai 4 ;; range(1, 6) | 1 sampai 5 ;; range(0, 10, 2) | 0 2 4 6 8 ;; range(3) | 0 1 2 ;; range(5, 0, -1) | 5 sampai 1 ;; break | menghentikan perulangan ~ Perintah perulangan.
@ List dalam Python
min: 15
act: Buat list nama lima teman, lalu cetak nama pertama dan terakhir.
mis: mengira indeks list dimulai dari 1
exp: List adalah kumpulan data yang disimpan dalam satu variabel dan ditulis di dalam kurung siku. Setiap anggota list memiliki indeks yang dimulai dari 0. Anggota dapat ditambah dengan append, dihapus dengan remove, dan banyak anggota dihitung dengan len.
ex: buah = ["apel", "jeruk", "mangga"] // buah[0] menghasilkan "apel".
pt: Ditulis dalam kurung siku ; Indeks mulai dari 0 ; append, remove, len
sum: List memudahkan mengelola banyak data.
fig: table Perintah list | Fungsi ;; append | menambah di akhir ;; remove | menghapus anggota ;; len | menghitung banyak anggota ;; sort | mengurutkan ;; insert | menyisipkan di posisi tertentu ;; pop | mengambil anggota terakhir ~ Perintah list Python.
@ Fungsi dalam program
min: 15
act: Buat fungsi luas_persegi yang menerima sisi dan mengembalikan luasnya.
mis: mendefinisikan fungsi tetapi tidak pernah memanggilnya
exp: Fungsi adalah kumpulan perintah yang diberi nama dan dapat dipanggil berulang kali. Dalam Python, fungsi dibuat dengan def, diikuti nama fungsi, parameter dalam kurung, dan titik dua. Perintah return mengembalikan hasil. Fungsi membuat program lebih rapi dan tidak berulang.
ex: def sapa(nama): return "Halo " + nama // sapa("Budi") menghasilkan Halo Budi.
pt: Dibuat dengan def ; Parameter dalam kurung ; return mengembalikan hasil
sum: Fungsi membuat program rapi dan dapat dipakai ulang.
fig: table Bagian fungsi | Contoh ;; kata kunci | def ;; nama fungsi | luas_persegi ;; parameter | sisi ;; badan fungsi | baris menjorok ;; nilai kembali | return sisi * sisi ;; pemanggilan | luas_persegi(4) ~ Bagian fungsi Python.
@ Program pertama dengan Python
min: 15
act: Tulis program yang menanyakan nama lalu menampilkan salam memakai input dan print.
mis: lupa tanda kutip pada teks sehingga program error
exp: Python adalah bahasa pemrograman yang mudah dibaca. Perintah print menampilkan teks ke layar, sedangkan input meminta masukan dari pengguna. Hasil input bertipe string, sehingga perlu diubah dengan int untuk dihitung. Komentar dalam Python diawali tanda pagar dan tidak dijalankan.
ex: print("Halo dunia") // umur = int(input("Umur: "))
pt: print menampilkan teks ; input meminta masukan ; int mengubah teks menjadi bilangan
sum: Program sederhana adalah langkah awal belajar coding.
fig: table Perintah Python | Fungsi ;; print | menampilkan ke layar ;; input | meminta masukan pengguna ;; int | mengubah ke bilangan bulat ;; str | mengubah ke teks ;; # | menandai komentar ;; type | melihat tipe data ~ Perintah dasar Python.
@ Debugging dan pengujian
min: 15
act: Cari dan perbaiki kesalahan pada program print("Halo) yang diberikan guru atau teman.
mis: mengira program yang berjalan tanpa error pasti benar hasilnya
exp: Debugging adalah proses mencari dan memperbaiki kesalahan atau bug dalam program. Jenis kesalahan meliputi syntax error karena salah penulisan, runtime error saat program berjalan, dan logic error ketika hasil tidak sesuai harapan. Pengujian dilakukan dengan mencoba berbagai masukan, termasuk nilai batas.
ex: print("Halo) kurang tanda kutip penutup (syntax error). // Rumus rata-rata salah membagi (logic error).
pt: Mencari dan memperbaiki bug ; Syntax, runtime, logic error ; Uji dengan nilai batas
sum: Debugging membuat program bekerja sesuai harapan.
fig: table Jenis kesalahan | Contoh ;; syntax error | tanda kutip tidak ditutup ;; runtime error | membagi dengan nol ;; logic error | rumus rata-rata salah ;; name error | variabel belum dibuat ;; type error | menjumlah teks dan angka ;; indentation error | baris tidak menjorok ~ Jenis kesalahan program.
# 2|Kecerdasan Artifisial dan Keamanan
@ Pembelajaran mesin
min: 15
act: Kelompokkan gambar kucing dan anjing dari majalah, lalu jelaskan ciri yang kamu pakai seperti cara mesin belajar.
mis: mengira mesin belajar sendiri tanpa data
exp: Pembelajaran mesin atau machine learning adalah cabang kecerdasan artifisial yang membuat komputer belajar dari data. Komputer menemukan pola dari banyak contoh, lalu memakai pola itu untuk memprediksi data baru. Ada pembelajaran terawasi yang memakai data berlabel dan pembelajaran tak terawasi yang mengelompokkan data tanpa label.
ex: Filter spam belajar dari contoh surel spam. // Aplikasi musik merekomendasikan lagu dari kebiasaan pendengar.
pt: Komputer belajar dari data ; Menemukan pola untuk memprediksi ; Terawasi dan tak terawasi
sum: Semakin baik datanya, semakin baik hasil belajar mesin.
fig: table Penerapan | Tugas pembelajaran mesin ;; filter spam | mengenali surel sampah ;; rekomendasi video | menebak kesukaan pengguna ;; pengenalan wajah | mencocokkan wajah ;; terjemahan otomatis | mengubah bahasa ;; prakiraan cuaca | memprediksi cuaca ;; deteksi penipuan bank | mengenali transaksi mencurigakan ~ Penerapan pembelajaran mesin.
@ Data latih dan data uji
min: 15
act: Bagi 20 kartu bergambar buah menjadi 16 kartu latih dan 4 kartu uji, lalu coba tebak kartu uji.
mis: menguji model dengan data yang sama dengan data latih
exp: Dalam pembelajaran mesin, data dibagi menjadi data latih dan data uji. Data latih dipakai untuk mengajari model, sedangkan data uji dipakai untuk mengukur ketepatan model pada data yang belum pernah dilihat. Data yang tidak seimbang atau sedikit dapat membuat model bias dan kurang akurat.
ex: 80 persen data untuk latih dan 20 persen untuk uji. // Model hanya dilatih foto kucing hitam sehingga salah mengenali kucing putih.
pt: Data latih untuk mengajari ; Data uji mengukur ketepatan ; Data tidak seimbang menimbulkan bias
sum: Pembagian data yang baik membuat model dapat dipercaya.
fig: table Istilah | Arti ;; data latih | data untuk mengajari model ;; data uji | data untuk mengukur model ;; label | jawaban benar pada data ;; akurasi | persentase tebakan benar ;; bias | kecenderungan tidak adil ;; model | hasil belajar mesin ~ Istilah data pembelajaran mesin.
@ Menulis prompt yang baik
min: 15
act: Bandingkan jawaban asisten KA untuk prompt singkat dan prompt yang lengkap dengan konteks.
mis: menulis prompt sangat singkat tanpa konteks lalu kecewa dengan hasilnya
exp: Prompt adalah perintah atau pertanyaan yang diberikan kepada KA generatif. Prompt yang baik memuat tujuan yang jelas, konteks, format jawaban yang diinginkan, dan batasan. Hasil KA tetap perlu diperiksa karena bisa keliru. Jangan memasukkan data pribadi ke dalam prompt.
ex: Jelaskan fotosintesis untuk siswa kelas 7 dalam lima poin singkat. // Tambahkan contoh dari kehidupan sehari-hari.
pt: Tujuan dan konteks jelas ; Sebutkan format dan batasan ; Periksa hasil dan jaga data pribadi
sum: Prompt yang jelas menghasilkan jawaban yang lebih berguna.
fig: table Unsur prompt | Contoh ;; tujuan | jelaskan fotosintesis ;; sasaran | untuk siswa kelas 7 ;; format | dalam lima poin ;; batasan | maksimal seratus kata ;; gaya | bahasa sederhana ;; contoh | sertakan contoh sehari-hari ~ Unsur prompt yang baik.
@ Pengenalan suara
min: 15
act: Coba fitur ketik dengan suara di HP, lalu catat kata yang sering salah dikenali.
mis: mengira asisten suara selalu memahami semua ucapan dengan benar
exp: Pengenalan suara adalah teknologi KA yang mengubah ucapan menjadi teks atau perintah. Mikrofon menangkap suara, lalu sistem mencocokkan pola bunyi dengan kata. Ketepatan dipengaruhi kebisingan, kejelasan ucapan, logat, dan kualitas mikrofon. Contohnya asisten suara dan fitur dikte.
ex: Mengetik pesan dengan suara. // Asisten suara menyalakan alarm atas perintah.
pt: Mengubah ucapan menjadi teks ; Mencocokkan pola bunyi ; Dipengaruhi kebisingan dan logat
sum: Pengenalan suara memudahkan interaksi dengan perangkat.
fig: table Faktor | Pengaruh pada pengenalan suara ;; kebisingan | menurunkan ketepatan ;; ucapan jelas | menaikkan ketepatan ;; logat daerah | kadang salah dikenali ;; mikrofon bagus | suara tertangkap baik ;; jarak terlalu jauh | suara lemah ;; bahasa didukung | dapat dikenali sistem ~ Faktor pengenalan suara.
@ Robot dan sensor
min: 15
act: Amati perangkat di rumah yang memakai sensor, seperti lampu otomatis atau pintu otomatis.
mis: mengira semua robot berbentuk manusia
exp: Robot adalah mesin yang dapat bekerja otomatis berdasarkan program. Robot memakai sensor untuk menerima informasi dari lingkungan, prosesor untuk mengolah, dan aktuator seperti motor untuk bergerak. Bentuk robot bermacam-macam, misalnya lengan robot di pabrik, robot penyedot debu, dan drone.
ex: Robot penyedot debu memakai sensor jarak agar tidak menabrak. // Lengan robot merakit mobil di pabrik.
pt: Bekerja otomatis berdasarkan program ; Sensor, prosesor, aktuator ; Bentuk bermacam-macam
sum: Sensor membuat robot dapat merasakan lingkungannya.
fig: table Sensor | Mendeteksi ;; sensor cahaya | terang gelap ;; sensor suhu | panas dingin ;; sensor jarak | benda di depan ;; sensor gerak | gerakan orang ;; sensor sentuh | tekanan atau sentuhan ;; sensor suara | bunyi ~ Jenis sensor robot.
@ Dampak KA pada pekerjaan
min: 15
act: Wawancarai satu orang dewasa tentang pemakaian teknologi KA di tempat kerjanya.
mis: mengira KA akan menggantikan semua pekerjaan manusia
exp: KA dapat mengotomatisasi pekerjaan berulang, seperti memilah data atau menjawab pertanyaan sederhana. Di sisi lain, KA menciptakan pekerjaan baru, seperti ilmuwan data dan pengembang KA. Kemampuan manusia seperti kreativitas, empati, dan berpikir kritis tetap dibutuhkan. Belajar sepanjang hayat membantu menghadapi perubahan.
ex: Chatbot menjawab pertanyaan pelanggan. // Dokter memakai KA untuk membantu membaca hasil rontgen.
pt: Mengotomatisasi pekerjaan berulang ; Menciptakan pekerjaan baru ; Kreativitas dan empati tetap penting
sum: KA mengubah pekerjaan, bukan menghapus peran manusia.
fig: table Bidang | Contoh pemakaian KA ;; kesehatan | membantu membaca rontgen ;; pertanian | memantau tanaman dengan drone ;; perbankan | mendeteksi penipuan ;; transportasi | navigasi rute tercepat ;; pendidikan | latihan soal adaptif ;; layanan pelanggan | chatbot ~ Pemakaian KA di berbagai bidang.
@ Autentikasi dua langkah
min: 15
act: Bersama orang tua, periksa apakah akun surel keluarga sudah memakai verifikasi dua langkah.
mis: membagikan kode OTP kepada orang yang mengaku petugas
exp: Autentikasi dua langkah adalah cara masuk akun yang memerlukan dua bukti, misalnya kata sandi dan kode sekali pakai atau OTP. Walaupun kata sandi bocor, akun tetap aman karena penyerang tidak memiliki kode kedua. Kode OTP bersifat rahasia dan tidak boleh diberikan kepada siapa pun.
ex: Kode OTP dikirim melalui SMS. // Aplikasi autentikator membuat kode baru setiap 30 detik.
pt: Dua bukti untuk masuk ; Melindungi saat kata sandi bocor ; OTP rahasia
sum: Autentikasi dua langkah menambah lapisan keamanan akun.
fig: table Jenis bukti | Contoh ;; sesuatu yang diketahui | kata sandi ;; sesuatu yang dimiliki | HP penerima OTP ;; ciri tubuh | sidik jari ;; kode sekali pakai | OTP lewat SMS ;; aplikasi autentikator | kode berganti tiap 30 detik ;; kunci keamanan | perangkat USB khusus ~ Jenis bukti autentikasi.
@ Etika memakai konten KA
min: 15
act: Diskusikan dengan teman kapan boleh dan tidak boleh memakai KA untuk mengerjakan tugas sekolah.
mis: menyerahkan tulisan buatan KA sebagai karya sendiri tanpa izin guru
exp: Memakai KA secara etis berarti jujur, bertanggung jawab, dan menghormati orang lain. Beri tahu jika suatu konten dibuat dengan bantuan KA. Jangan membuat konten KA yang meniru wajah atau suara orang lain tanpa izin. Periksa kebenaran hasil KA dan ikuti aturan sekolah tentang pemakaian KA.
ex: Mencantumkan keterangan gambar dibuat dengan KA. // Memakai KA untuk menjelaskan materi, bukan mencontek.
pt: Jujur menyebutkan bantuan KA ; Jangan meniru orang tanpa izin ; Periksa kebenaran hasil
sum: KA dipakai untuk membantu belajar, bukan untuk berbuat curang.
fig: table Perilaku | Etis atau tidak ;; mencantumkan bantuan KA | etis ;; mengaku karya KA buatan sendiri | tidak jujur ;; meniru suara orang tanpa izin | melanggar privasi ;; memeriksa fakta hasil KA | bertanggung jawab ;; memakai KA saat ujian tanpa izin | curang ;; bertanya KA untuk memahami materi | membantu belajar ~ Etika memakai KA.
"""

BANK += """
## KKA|Tipe data
Tipe data untuk bilangan bulat adalah …|integer|float|string|boolean|Integer.
Tipe data untuk teks adalah …|string|integer|float|boolean|String.
=|Tipe data untuk bilangan desimal adalah …|float|Float.
=|Tipe data bernilai True atau False adalah …|boolean;bool|Boolean.
B|Teks dalam Python ditulis di antara tanda kutip.|Kutip.
S|"13" dan 13 memiliki tipe data yang sama.|String dan integer.
Nilai 1.65 bertipe data …|float|integer|string|boolean|Float.
Kumpulan data dalam kurung siku bertipe …|list|integer|boolean|float|List.
## KKA|Operator aritmetika
Hasil 17 // 5 dalam Python adalah …|3|3.4|2|4|Pembagian bulat.
Hasil 17 % 5 dalam Python adalah …|2|3|3.4|85|Sisa bagi.
=|Hasil 2 ** 3 dalam Python adalah …|8|Delapan.
=|Hasil 7 / 2 dalam Python adalah …|3.5|3,5.
B|Operator % menghasilkan sisa pembagian.|Sisa.
S|Operator % dipakai untuk menghitung persen.|Sisa bagi.
Operator untuk perkalian dalam Python adalah …|*|x|.|:|Bintang.
Hasil 2 + 3 * 4 dalam Python adalah …|14|20|24|9|Kali dulu.
## KKA|Percabangan if-else
Perintah Python untuk syarat tambahan setelah if adalah …|elif|else if|then|when|elif.
Operator pembanding untuk sama dengan adalah …|==|=|!=|>=|==.
=|Operator pembanding untuk tidak sama dengan adalah …|!=|!=.
=|Baris if dalam Python diakhiri tanda …|titik dua;:|Titik dua.
B|Perintah di dalam if ditulis menjorok.|Indentasi.
S|else dijalankan ketika syarat if benar.|Salah.
Jika nilai = 80, maka if nilai >= 75 menghasilkan syarat …|benar|salah|error|kosong|Benar.
Operator pembanding untuk kurang dari atau sama dengan adalah …|<=|=<|<|>=|<=.
## KKA|Perulangan for dan while
range(5) menghasilkan angka …|0 sampai 4|1 sampai 5|0 sampai 5|1 sampai 4|0-4.
Perulangan yang berjalan selama syarat benar adalah …|while|for|if|def|while.
=|Perintah untuk menghentikan perulangan adalah …|break|break.
=|range(1, 6) menghasilkan angka 1 sampai …|5|Lima.
B|For cocok jika banyak ulangan sudah diketahui.|For.
S|While tanpa perubahan syarat pasti berhenti sendiri.|Tanpa akhir.
range(0, 10, 2) menghasilkan …|0 2 4 6 8|0 2 4 6 8 10|2 4 6 8 10|1 3 5 7 9|Langkah 2.
range(3) menghasilkan …|0 1 2|1 2 3|0 1 2 3|3|0-2.
## KKA|List dalam Python
Indeks list dalam Python dimulai dari …|0|1|-1|10|Nol.
List ditulis di dalam kurung …|siku|kurawal|biasa|sudut|Siku.
=|Perintah untuk menambah anggota di akhir list adalah …|append|append.
=|Perintah untuk menghitung banyak anggota list adalah …|len|len.
B|buah[0] mengambil anggota pertama list.|Indeks 0.
S|Indeks anggota pertama list adalah 1.|Nol.
Perintah untuk mengurutkan list adalah …|sort|pop|len|insert|sort.
Perintah untuk menghapus anggota tertentu dari list adalah …|remove|append|sort|len|remove.
## KKA|Fungsi dalam program
Kata kunci untuk membuat fungsi dalam Python adalah …|def|func|function|make|def.
Perintah untuk mengembalikan hasil fungsi adalah …|return|print|input|break|return.
=|Nilai yang diterima fungsi di dalam kurung disebut …|parameter|Parameter.
=|Menjalankan fungsi dengan menulis namanya disebut … fungsi.|memanggil;pemanggilan|Memanggil.
B|Fungsi dapat dipanggil berulang kali.|Dipakai ulang.
S|Fungsi berjalan otomatis walaupun tidak pernah dipanggil.|Harus dipanggil.
Jika def kali2(x): return x * 2, maka kali2(5) menghasilkan …|10|7|25|52|10.
Manfaat fungsi adalah program menjadi …|rapi dan tidak berulang|lebih panjang|sulit dibaca|lambat|Rapi.
## KKA|Program pertama dengan Python
Perintah untuk menampilkan teks ke layar adalah …|print|input|int|def|print.
Perintah untuk meminta masukan pengguna adalah …|input|print|return|range|input.
=|Fungsi untuk mengubah teks menjadi bilangan bulat adalah …|int|int.
=|Komentar dalam Python diawali tanda …|pagar;#|Pagar.
B|Hasil input bertipe string.|String.
S|Komentar dalam Python dijalankan sebagai perintah.|Tidak dijalankan.
Fungsi untuk melihat tipe data adalah …|type|print|int|str|type.
Fungsi untuk mengubah bilangan menjadi teks adalah …|str|int|float|len|str.
## KKA|Debugging dan pengujian
Proses mencari dan memperbaiki kesalahan program disebut …|debugging|coding|compiling|downloading|Debugging.
Kesalahan karena salah penulisan perintah disebut …|syntax error|logic error|runtime error|bug cuaca|Syntax.
=|Kesalahan saat hasil tidak sesuai harapan disebut … error.|logic|Logic.
=|Kesalahan dalam program disebut juga …|bug|Bug.
B|Pengujian sebaiknya memakai nilai batas.|Nilai batas.
S|Program yang berjalan tanpa error pasti hasilnya benar.|Logic error.
Membagi dengan nol menyebabkan …|runtime error|syntax error|indentation error|name error|Runtime.
Memakai variabel yang belum dibuat menyebabkan …|name error|type error|syntax error|logic error|Name.
## KKA|Pembelajaran mesin
Pembelajaran mesin membuat komputer belajar dari …|data|listrik|udara|layar|Data.
Pembelajaran dengan data berlabel disebut pembelajaran …|terawasi|tak terawasi|acak|manual|Terawasi.
=|Pembelajaran yang mengelompokkan data tanpa label disebut pembelajaran tak …|terawasi|Tak terawasi.
=|Pembelajaran mesin adalah cabang dari kecerdasan …|artifisial;buatan|Artifisial.
B|Filter spam memakai pembelajaran mesin.|Spam.
S|Mesin dapat belajar tanpa data apa pun.|Perlu data.
Rekomendasi video menebak …|kesukaan pengguna|cuaca|harga emas|nama pengguna saja|Kesukaan.
Pembelajaran mesin menemukan … dari banyak contoh.|pola|kabel|layar|tombol|Pola.
## KKA|Data latih dan data uji
Data untuk mengajari model disebut data …|latih|uji|label|bias|Latih.
Data untuk mengukur ketepatan model disebut data …|uji|latih|mentah|cadangan|Uji.
=|Jawaban benar pada data disebut …|label|Label.
=|Persentase tebakan benar model disebut …|akurasi|Akurasi.
B|Data tidak seimbang dapat membuat model bias.|Bias.
S|Model sebaiknya diuji dengan data yang sama persis dengan data latih.|Data baru.
Pembagian data yang umum adalah 80 persen latih dan … persen uji.|20|50|80|5|20 persen.
Kecenderungan tidak adil pada model disebut …|bias|akurasi|label|algoritma|Bias.
## KKA|Menulis prompt yang baik
Perintah atau pertanyaan kepada KA generatif disebut …|prompt|kode|bug|virus|Prompt.
Prompt yang baik memuat tujuan yang …|jelas|samar|panjang tanpa arah|rahasia|Jelas.
=|Hasil KA tetap perlu di …|periksa;cek|Diperiksa.
=|Data yang tidak boleh dimasukkan ke prompt adalah data …|pribadi|Pribadi.
B|Menyebutkan format jawaban membuat hasil lebih sesuai.|Format.
S|Prompt singkat tanpa konteks selalu memberi hasil terbaik.|Perlu konteks.
Kalimat "untuk siswa kelas 7" dalam prompt menunjukkan …|sasaran pembaca|format|batasan kata|warna|Sasaran.
Kalimat "maksimal seratus kata" dalam prompt menunjukkan …|batasan|tujuan|sasaran|contoh|Batasan.
## KKA|Pengenalan suara
Pengenalan suara mengubah ucapan menjadi …|teks atau perintah|gambar|video|warna|Teks.
Alat yang menangkap suara adalah …|mikrofon|speaker|layar|keyboard|Mikrofon.
=|Suara bising di sekitar membuat ketepatan …|menurun;turun|Menurun.
=|Fitur mengetik dengan suara disebut …|dikte|Dikte.
B|Logat daerah kadang membuat kata salah dikenali.|Logat.
S|Asisten suara selalu memahami semua ucapan dengan benar.|Bisa salah.
Ucapan yang jelas membuat ketepatan pengenalan suara …|naik|turun|hilang|sama saja|Naik.
Jarak terlalu jauh dari mikrofon membuat suara …|lemah|keras|jernih|cepat|Lemah.
## KKA|Robot dan sensor
Bagian robot untuk menerima informasi dari lingkungan adalah …|sensor|aktuator|baterai|roda|Sensor.
Motor penggerak robot disebut …|aktuator|sensor|prosesor|program|Aktuator.
=|Sensor yang mendeteksi terang gelap adalah sensor …|cahaya|Cahaya.
=|Sensor yang mendeteksi panas dingin adalah sensor …|suhu|Suhu.
B|Robot penyedot debu memakai sensor jarak.|Jarak.
S|Semua robot berbentuk seperti manusia.|Beragam.
Lampu otomatis yang menyala saat ada orang lewat memakai sensor …|gerak|suhu|suara|sentuh|Gerak.
Bagian robot yang mengolah informasi adalah …|prosesor|aktuator|roda|sensor|Prosesor.
## KKA|Dampak KA pada pekerjaan
KA dapat mengotomatisasi pekerjaan yang …|berulang|kreatif sepenuhnya|penuh empati|tidak terduga|Berulang.
Contoh pekerjaan baru yang muncul karena KA adalah …|ilmuwan data|tukang pos surat|operator telegraf|juru ketik manual|Baru.
=|Program yang menjawab pertanyaan pelanggan secara otomatis disebut …|chatbot|Chatbot.
=|Belajar terus untuk menghadapi perubahan disebut belajar sepanjang …|hayat|Hayat.
B|Kreativitas dan empati manusia tetap dibutuhkan.|Manusia.
S|KA pasti menggantikan semua pekerjaan manusia.|Tidak semua.
Di bidang kesehatan, KA membantu dokter membaca …|hasil rontgen|koran|novel|peta wisata|Rontgen.
Di bidang perbankan, KA dipakai untuk mendeteksi …|penipuan|cuaca|lagu|gempa|Penipuan.
## KKA|Autentikasi dua langkah
Autentikasi dua langkah memerlukan … bukti untuk masuk akun.|dua|satu|lima|nol|Dua.
Kode sekali pakai disebut …|OTP|PIN tetap|URL|IP|OTP.
=|Kode OTP tidak boleh diberikan kepada …|siapa pun;siapapun|Rahasia.
=|Sidik jari termasuk bukti berupa ciri …|tubuh|Ciri tubuh.
B|Akun tetap aman walaupun kata sandi bocor jika memakai dua langkah.|Lapisan.
S|Kode OTP boleh diberikan kepada orang yang mengaku petugas bank.|Penipuan.
Aplikasi autentikator membuat kode baru setiap …|30 detik|30 hari|setahun|seminggu|30 detik.
Kata sandi termasuk bukti berupa sesuatu yang …|diketahui|dimiliki|dicium|dilihat orang lain|Diketahui.
## KKA|Etika memakai konten KA
Memakai KA secara etis berarti …|jujur menyebutkan bantuan KA|mengaku karya KA buatan sendiri|meniru suara orang|mencontek|Jujur.
Meniru suara orang lain dengan KA tanpa izin melanggar …|privasi|aturan lalu lintas|tata bahasa|hukum fisika|Privasi.
=|Hasil KA perlu diperiksa … nya.|kebenaran;fakta|Kebenaran.
=|Memakai KA saat ujian tanpa izin termasuk perbuatan …|curang|Curang.
B|Bertanya kepada KA untuk memahami materi dapat membantu belajar.|Membantu.
S|Menyerahkan tulisan KA sebagai karya sendiri tanpa izin guru itu jujur.|Tidak jujur.
Mencantumkan keterangan gambar dibuat dengan KA termasuk sikap …|etis|curang|egois|lalai|Etis.
Pemakaian KA di sekolah harus mengikuti …|aturan sekolah|keinginan sendiri saja|ajakan teman|iklan|Aturan.
"""

SAS += """
## KKA 1
0|Nilai False termasuk tipe data ....|boolean|string|integer|float|Boolean.
1|Hasil 10 % 3 dalam Python adalah ....|1|3|3.33|0|Sisa bagi.
2|Operator pembanding lebih dari atau sama dengan adalah ....|>=|=>|>|==|>=.
3|range(5, 0, -1) menghasilkan angka ....|5 sampai 1|0 sampai 5|1 sampai 5|5 sampai 0|Mundur.
4|Perintah list untuk menyisipkan anggota di posisi tertentu adalah ....|insert|append|pop|len|insert.
5|Pada def luas(s): return s * s, bagian s disebut ....|parameter|nama fungsi|nilai kembali|kata kunci|Parameter.
6|Hasil int("7") + 3 adalah ....|10|73|"73"|error|int.
7|Menjumlahkan teks dengan angka menyebabkan ....|type error|syntax error|name error|indentation error|Type.
## KKA 2
0|Aplikasi musik yang menyarankan lagu berdasarkan kebiasaan memakai ....|pembelajaran mesin|sensor suhu|aktuator|kabel data|ML.
1|Model hanya dilatih dengan foto kucing hitam sehingga salah mengenali kucing putih. Ini contoh ....|bias data|akurasi tinggi|data uji|label benar|Bias.
2|Kalimat "sertakan contoh sehari-hari" dalam prompt termasuk unsur ....|contoh|batasan|sasaran|tujuan|Contoh.
3|Mikrofon yang bagus membuat suara ....|tertangkap baik|hilang|bising|lemah|Mikrofon.
4|Sensor yang mendeteksi bunyi adalah sensor ....|suara|cahaya|suhu|gerak|Suara.
5|Pemakaian KA di bidang pertanian contohnya ....|memantau tanaman dengan drone|membaca rontgen|mendeteksi penipuan bank|menjawab pelanggan|Pertanian.
6|Perangkat USB khusus untuk masuk akun disebut ....|kunci keamanan|flashdisk biasa|kabel data|mouse|Kunci.
7|Memeriksa fakta hasil KA termasuk sikap ....|bertanggung jawab|curang|tidak jujur|melanggar privasi|Tanggung jawab.
"""

TOPICS += """
## PAI
# 1|Al-Qur'an, Akhlak, dan Fikih
@ Surah Al-Qadr
min: 15
act: Baca Surah Al-Qadr bersama keluarga, lalu tulis artinya di buku catatan.
mis: mengira Lailatul Qadar terjadi di luar bulan Ramadan
exp: Surah Al-Qadr adalah surah ke-97 dan terdiri atas 5 ayat. Surah ini termasuk golongan Makkiyah. Al-Qadr artinya kemuliaan. Surah ini menjelaskan bahwa Al-Qur'an diturunkan pada malam Lailatul Qadar, malam yang lebih baik daripada seribu bulan. Pada malam itu malaikat dan Jibril turun membawa kedamaian sampai terbit fajar.
ex: Lailatul Qadar terjadi pada bulan Ramadan. // Beribadah pada malam itu lebih baik dari seribu bulan.
pt: Surah ke-97, terdiri atas 5 ayat ; Al-Qadr artinya kemuliaan ; Lailatul Qadar lebih baik dari seribu bulan
sum: Al-Qadr mengajak kita menghidupkan malam-malam Ramadan.
fig: table Hal | Isi ;; nomor surah | 97 ;; jumlah ayat | 5 ;; arti nama surah | kemuliaan ;; ayat 1 | Al-Qur'an diturunkan pada Lailatul Qadar ;; ayat 3 | lebih baik dari seribu bulan ;; ayat 5 | kedamaian sampai terbit fajar ~ Isi Surah Al-Qadr.
read: quran 97:1-5
@ Asmaul Husna As-Sami' dan Al-Basir
min: 15
act: Tulis dua perilaku yang mencerminkan keyakinan bahwa Allah Maha Mendengar dan Maha Melihat.
mis: berbuat curang saat tidak ada orang yang melihat
exp: As-Sami' artinya Allah Maha Mendengar, sedangkan Al-Basir artinya Allah Maha Melihat. Allah mendengar setiap ucapan dan doa, serta melihat setiap perbuatan, baik yang tampak maupun tersembunyi. Meyakini kedua nama ini membuat kita menjaga lisan, berdoa dengan sungguh-sungguh, dan berbuat jujur walaupun tidak ada yang melihat.
ex: Menjaga lisan dari kata kasar (As-Sami'). // Tidak mencontek walaupun guru keluar kelas (Al-Basir).
pt: As-Sami' Maha Mendengar ; Al-Basir Maha Melihat ; Menjaga lisan dan berbuat jujur
sum: Allah selalu mendengar dan melihat, maka jagalah ucapan dan perbuatan.
fig: table Asmaul Husna | Arti ;; As-Sami' | Maha Mendengar ;; Al-Basir | Maha Melihat ;; Al-'Alim | Maha Mengetahui ;; Al-Khabir | Maha Teliti ;; Ar-Raqib | Maha Mengawasi ;; Al-Latif | Maha Lembut ~ Asmaul Husna yang berkaitan.
@ Sikap tawadu'
min: 15
act: Catat satu pengalaman ketika kamu berhasil tetapi tetap rendah hati kepada teman.
mis: menganggap tawadu' sama dengan merendahkan diri berlebihan
exp: Tawadu' artinya rendah hati, yaitu tidak merasa lebih tinggi dari orang lain. Orang yang tawadu' menghargai pendapat orang lain, mau menerima nasihat, dan tidak memamerkan kelebihannya. Lawan tawadu' adalah takabur atau sombong. Rasulullah saw. adalah teladan sikap tawadu'.
ex: Juara kelas tetap mau membantu teman belajar. // Menerima kritik dengan lapang dada.
pt: Tawadu' rendah hati ; Menghargai orang lain ; Lawannya takabur
sum: Rendah hati membuat kita disukai Allah dan sesama.
fig: table Perilaku | Tawadu' atau takabur ;; menghargai pendapat teman | tawadu' ;; memamerkan prestasi | takabur ;; menerima nasihat | tawadu' dan terbuka ;; meremehkan orang lain | takabur dan merendahkan ;; menyapa petugas kebersihan | tawadu' kepada semua ;; merasa paling pintar | takabur dalam ilmu ~ Tawadu' dan takabur.
@ Hadas dan cara bersuci
min: 15
act: Praktikkan urutan wudu yang benar di rumah dan minta orang tua memeriksa.
mis: mengira hadas besar cukup dihilangkan dengan wudu
exp: Hadas adalah keadaan tidak suci yang menghalangi ibadah seperti salat. Hadas kecil, misalnya buang air atau buang angin, dihilangkan dengan wudu. Hadas besar, misalnya haid atau junub, dihilangkan dengan mandi wajib. Najis adalah kotoran yang harus dibersihkan, dibagi menjadi najis mukhaffafah, mutawassitah, dan mughallazah.
ex: Setelah buang air kecil, berwudu sebelum salat. // Najis air kencing bayi laki-laki cukup dipercik air.
pt: Hadas kecil dengan wudu ; Hadas besar dengan mandi wajib ; Najis ringan, sedang, berat
sum: Bersuci adalah syarat sah salat.
fig: table Najis | Cara membersihkan ;; mukhaffafah | dipercik air ;; mutawassitah | dicuci sampai hilang bau, rasa, warna ;; mughallazah | dicuci tujuh kali salah satunya dengan tanah ;; hadas kecil | berwudu ;; hadas besar | mandi wajib ;; tanpa air | tayamum ~ Cara bersuci.
@ Tata cara tayamum
min: 15
act: Peragakan gerakan tayamum dengan debu bersih dan sebutkan sebab yang membolehkannya.
mis: mengusap seluruh anggota wudu saat tayamum
exp: Tayamum adalah bersuci dengan debu yang suci sebagai pengganti wudu atau mandi wajib. Tayamum dibolehkan jika tidak ada air, sakit yang tidak boleh terkena air, atau air hanya cukup untuk minum. Rukun tayamum adalah niat, mengusap wajah, dan mengusap kedua tangan sampai pergelangan atau siku. Tayamum batal jika menemukan air.
ex: Musafir di gurun tanpa air bertayamum. // Orang sakit kulit bertayamum atas saran dokter.
pt: Bersuci dengan debu suci ; Pengganti wudu atau mandi ; Usap wajah dan tangan
sum: Tayamum menunjukkan kemudahan dalam Islam.
fig: table Hal tayamum | Keterangan ;; bahan | debu yang suci ;; rukun pertama | niat ;; usapan pertama | wajah ;; usapan kedua | kedua tangan ;; sebab boleh | tidak ada air ;; pembatal | menemukan air ~ Ketentuan tayamum.
@ Islam masuk ke Nusantara
min: 15
act: Cari tahu nama kerajaan Islam yang pernah ada di provinsimu.
mis: mengira Islam menyebar di Nusantara dengan peperangan
exp: Islam masuk ke Nusantara melalui jalur perdagangan, pernikahan, pendidikan, dan kesenian. Para pedagang dari Gujarat, Persia, dan Arab berdagang sekaligus berdakwah. Kerajaan Islam pertama di Nusantara adalah Samudra Pasai di Aceh. Wali Songo menyebarkan Islam di Jawa dengan cara damai, misalnya melalui wayang dan gamelan.
ex: Sunan Kalijaga berdakwah melalui wayang. // Pesantren menjadi pusat pendidikan Islam.
pt: Jalur dagang, nikah, pendidikan, seni ; Samudra Pasai kerajaan pertama ; Wali Songo berdakwah damai
sum: Islam menyebar di Nusantara secara damai.
fig: table Kerajaan Islam | Daerah ;; Samudra Pasai | Aceh ;; Demak | Jawa Tengah ;; Mataram Islam | Yogyakarta ;; Gowa Tallo | Sulawesi Selatan ;; Ternate | Maluku Utara ;; Banten | Banten ~ Kerajaan Islam di Nusantara.
# 2|Syukur, Ibadah, dan Sejarah
@ Syukur dalam An-Nahl ayat 114
min: 15
act: Tulis lima nikmat Allah hari ini dan cara mensyukurinya.
mis: mengira bersyukur cukup dengan ucapan tanpa perbuatan
exp: Surah An-Nahl ayat 114 memerintahkan manusia memakan rezeki yang halal dan baik dari Allah, serta mensyukuri nikmat-Nya jika benar-benar menyembah-Nya. Syukur dilakukan dengan hati yang mengakui nikmat dari Allah, lisan yang mengucapkan alhamdulillah, dan perbuatan yang memakai nikmat untuk kebaikan.
ex: Mengucapkan alhamdulillah setelah makan. // Memakai kesehatan untuk belajar dan menolong orang.
pt: Makan yang halal dan baik ; Syukur dengan hati dan lisan ; Syukur dengan perbuatan
sum: Bersyukur membuat nikmat terasa cukup dan bertambah.
fig: table Cara syukur | Contoh ;; hati | mengakui nikmat dari Allah ;; lisan | mengucapkan alhamdulillah ;; perbuatan | memakai nikmat untuk kebaikan ;; makanan | memilih yang halal dan baik ;; kesehatan | rajin belajar dan beribadah ;; harta | bersedekah ~ Cara bersyukur.
read: quran 16:114
@ Puasa wajib dan sunah
min: 15
act: Buat jadwal puasa sunah Senin Kamis atau Ayyamul Bid yang ingin kamu coba bersama keluarga.
mis: berpuasa pada hari raya Idulfitri
exp: Puasa adalah menahan diri dari makan, minum, dan hal yang membatalkan sejak terbit fajar sampai terbenam matahari dengan niat. Puasa wajib adalah puasa Ramadan, puasa qada, dan puasa nazar. Puasa sunah antara lain Senin Kamis, Arafah, Asyura, Ayyamul Bid, dan enam hari Syawal. Puasa diharamkan pada dua hari raya dan hari tasyrik.
ex: Puasa Arafah pada 9 Zulhijah. // Ayyamul Bid pada tanggal 13, 14, 15 bulan hijriah.
pt: Menahan diri dari fajar sampai magrib ; Wajib: Ramadan, qada, nazar ; Haram pada hari raya
sum: Puasa melatih kesabaran dan ketakwaan.
fig: table Puasa | Waktu ;; Ramadan | sebulan penuh bulan Ramadan ;; Arafah | 9 Zulhijah ;; Asyura | 10 Muharam ;; Ayyamul Bid | 13, 14, 15 bulan hijriah ;; Syawal | enam hari bulan Syawal ;; Senin Kamis | setiap Senin dan Kamis ~ Waktu puasa wajib dan sunah.
@ Sujud syukur, sahwi, dan tilawah
min: 15
act: Peragakan sujud syukur ketika mendapat kabar gembira dan sebutkan bedanya dengan sujud sahwi.
mis: mengira sujud tilawah dilakukan karena lupa dalam salat
exp: Sujud syukur dilakukan ketika mendapat nikmat atau terhindar dari bahaya. Sujud sahwi dilakukan karena lupa dalam salat, misalnya lupa jumlah rakaat atau lupa tasyahud awal, dilakukan sebelum salam. Sujud tilawah dilakukan ketika membaca atau mendengar ayat sajdah. Ketiganya dilakukan dengan satu kali sujud.
ex: Sujud syukur setelah lulus ujian. // Sujud tilawah saat membaca ayat sajdah.
pt: Syukur saat mendapat nikmat ; Sahwi karena lupa dalam salat ; Tilawah karena ayat sajdah
sum: Sujud adalah bentuk ketundukan kepada Allah.
fig: table Jenis sujud | Sebab ;; sujud syukur | mendapat nikmat ;; sujud sahwi | lupa dalam salat ;; sujud tilawah | membaca ayat sajdah ;; sujud dalam salat | rukun salat ;; jumlah sujud syukur | satu kali ;; waktu sujud sahwi | sebelum salam ~ Jenis sujud.
@ Hormat kepada orang tua dan guru
min: 15
act: Lakukan tiga perbuatan baik untuk orang tua dan satu untuk guru minggu ini, lalu catat.
mis: berkata "ah" atau membentak ketika disuruh orang tua
exp: Islam memerintahkan berbakti kepada orang tua atau birrul walidain. Allah melarang berkata kasar, bahkan mengucapkan "ah", kepada orang tua. Guru juga wajib dihormati karena mengajarkan ilmu. Cara menghormati antara lain berkata sopan, menaati nasihat yang baik, mendoakan, dan membantu pekerjaan.
ex: Membantu ibu menyiapkan makanan. // Mendoakan guru setelah salat.
pt: Birrul walidain ; Larangan berkata kasar ; Guru dihormati karena mengajarkan ilmu
sum: Rida Allah ada pada rida orang tua.
fig: table Perbuatan | Termasuk ;; berkata sopan | adab berbicara ;; membantu pekerjaan rumah | bakti dengan tenaga ;; mendoakan orang tua | bakti dengan doa ;; menaati nasihat baik | patuh ;; mendengarkan guru menjelaskan | adab menuntut ilmu ;; mengucapkan salam | adab bertemu ~ Cara menghormati orang tua dan guru.
@ Empati dan peduli sosial
min: 15
act: Ikut kegiatan berbagi makanan atau menjenguk teman yang sakit bersama keluarga.
mis: menertawakan teman yang sedang mendapat musibah
exp: Empati adalah kemampuan merasakan apa yang dirasakan orang lain. Rasulullah saw. menggambarkan orang beriman seperti satu tubuh; jika satu bagian sakit, bagian lain ikut merasakan. Wujud empati antara lain menjenguk orang sakit, menghibur yang sedih, bersedekah, dan menolong korban bencana.
ex: Menjenguk teman yang dirawat di rumah sakit. // Menyisihkan uang jajan untuk korban banjir.
pt: Merasakan perasaan orang lain ; Orang beriman seperti satu tubuh ; Menjenguk, menghibur, bersedekah
sum: Empati menumbuhkan kasih sayang antar sesama.
fig: table Situasi | Sikap empati ;; teman sakit | menjenguk dan mendoakan ;; teman sedih | menghibur ;; korban bencana | berdonasi ;; tetangga kesulitan | menolong ;; teman baru | mengajak bergabung ;; anak yatim | menyantuni ~ Wujud empati.
@ Masa Khulafaurrasyidin
min: 15
act: Buat tabel empat khalifah beserta jasa utama masing-masing.
mis: menukar urutan khalifah setelah Rasulullah wafat
exp: Khulafaurrasyidin adalah empat khalifah yang memimpin umat Islam setelah Rasulullah saw. wafat. Abu Bakar as-Siddiq mengumpulkan Al-Qur'an dalam satu mushaf. Umar bin Khattab menetapkan kalender hijriah. Usman bin Affan menyeragamkan penulisan mushaf Al-Qur'an. Ali bin Abi Talib dikenal sebagai khalifah yang sangat berilmu.
ex: Mushaf Usmani dipakai hingga kini. // Kalender hijriah dimulai dari peristiwa hijrah.
pt: Empat khalifah setelah Rasulullah ; Abu Bakar dan Umar ; Usman dan Ali
sum: Khulafaurrasyidin meneladankan kepemimpinan yang adil.
fig: table Khalifah | Jasa utama ;; Abu Bakar as-Siddiq | mengumpulkan Al-Qur'an ;; Umar bin Khattab | menetapkan kalender hijriah ;; Usman bin Affan | menyeragamkan mushaf ;; Ali bin Abi Talib | ahli ilmu dan hukum ;; julukan Abu Bakar | as-Siddiq yang membenarkan ;; julukan Umar | al-Faruq pembeda benar dan salah ~ Khulafaurrasyidin.
"""

BANK += """
## PAI|Surah Al-Qadr
Surah Al-Qadr adalah surah ke …|97|96|98|99|97.
Arti Al-Qadr adalah …|kemuliaan|kegoncangan|bermegah-megahan|kuda perang|Kemuliaan.
=|Jumlah ayat Surah Al-Qadr adalah …|5|Lima.
=|Malam yang lebih baik dari seribu bulan disebut Lailatul …|Qadar|Qadar.
B|Lailatul Qadar terjadi pada bulan Ramadan.|Ramadan.
S|Lailatul Qadar lebih baik dari seratus tahun saja.|Seribu bulan.
Surah Al-Qadr termasuk golongan …|Makkiyah|Madaniyah|Yaumiyah|Nabawiyah|Makkiyah.
Pada malam Lailatul Qadar, kedamaian berlangsung sampai …|terbit fajar|tengah hari|magrib|isya|Fajar.
## PAI|Asmaul Husna As-Sami' dan Al-Basir
As-Sami' artinya Allah Maha …|Mendengar|Melihat|Mengetahui|Lembut|Mendengar.
Al-Basir artinya Allah Maha …|Melihat|Mendengar|Teliti|Mengawasi|Melihat.
=|Asmaul Husna yang artinya Maha Mengawasi adalah Ar- …|Raqib|Ar-Raqib.
=|Asmaul Husna yang artinya Maha Mengetahui adalah Al- …|'Alim;Alim|Al-'Alim.
B|Meyakini Al-Basir membuat kita jujur walaupun tidak ada yang melihat.|Al-Basir.
S|Allah hanya mendengar doa yang diucapkan keras.|Semua.
Tidak mencontek saat guru keluar kelas mencerminkan keyakinan kepada …|Al-Basir|Al-Latif|Al-Karim|Al-Wakil|Al-Basir.
Menjaga lisan dari kata kasar mencerminkan keyakinan kepada …|As-Sami'|Al-Matin|Al-Mu'min|Al-Karim|As-Sami'.
## PAI|Sikap tawadu'
Tawadu' artinya …|rendah hati|sombong|malas|pemarah|Rendah hati.
Lawan sikap tawadu' adalah …|takabur|jujur|amanah|sabar|Takabur.
=|Sikap sombong disebut juga …|takabur|Takabur.
=|Teladan utama sikap tawadu' adalah Rasulullah …|saw.;saw|Rasulullah.
B|Orang tawadu' mau menerima nasihat.|Terbuka.
S|Memamerkan prestasi termasuk sikap tawadu'.|Takabur.
Juara kelas yang tetap mau membantu teman menunjukkan sikap …|tawadu'|takabur|kikir|iri|Tawadu'.
Merasa paling pintar dan meremehkan teman termasuk sikap …|takabur|tawadu'|qanaah|syukur|Takabur.
## PAI|Hadas dan cara bersuci
Hadas kecil dihilangkan dengan …|wudu|mandi wajib|tayamum saja|mencuci tangan|Wudu.
Hadas besar dihilangkan dengan …|mandi wajib|wudu|berkumur|mencuci kaki|Mandi.
=|Najis ringan disebut najis …|mukhaffafah|Mukhaffafah.
=|Najis berat disebut najis …|mughallazah|Mughallazah.
B|Najis mughallazah dicuci tujuh kali salah satunya dengan tanah.|Tujuh kali.
S|Hadas besar cukup dihilangkan dengan wudu.|Mandi wajib.
Najis sedang disebut najis …|mutawassitah|mukhaffafah|mughallazah|ma'fu|Mutawassitah.
Air kencing bayi laki-laki yang hanya minum ASI termasuk najis …|mukhaffafah|mughallazah|mutawassitah|berat|Ringan.
## PAI|Tata cara tayamum
Tayamum adalah bersuci dengan …|debu yang suci|air sabun|pasir basah|minyak wangi|Debu.
Tayamum menjadi batal jika …|menemukan air|melihat debu|duduk|berjalan|Air.
=|Rukun tayamum yang pertama adalah …|niat|Niat.
=|Anggota yang diusap pertama dalam tayamum adalah …|wajah|Wajah.
B|Tayamum dibolehkan jika tidak ada air.|Sebab.
S|Tayamum mengusap seluruh anggota wudu termasuk kaki.|Wajah dan tangan.
Orang yang boleh bertayamum adalah …|orang sakit yang tidak boleh terkena air|orang yang malas berwudu|orang yang terburu-buru|orang yang dekat sungai|Sakit.
Tayamum dapat menggantikan wudu dan …|mandi wajib|salat|puasa|zakat|Mandi wajib.
## PAI|Islam masuk ke Nusantara
Kerajaan Islam pertama di Nusantara adalah …|Samudra Pasai|Demak|Mataram Islam|Banten|Samudra Pasai.
Penyebar Islam di Jawa dikenal dengan sebutan …|Wali Songo|Khulafaurrasyidin|Tiga Serangkai|Panitia Sembilan|Wali Songo.
=|Samudra Pasai terletak di …|Aceh|Aceh.
=|Sunan Kalijaga berdakwah melalui …|wayang|Wayang.
B|Islam masuk ke Nusantara melalui jalur perdagangan.|Dagang.
S|Islam menyebar di Nusantara terutama dengan peperangan.|Damai.
Kerajaan Gowa Tallo terletak di …|Sulawesi Selatan|Jawa Tengah|Aceh|Maluku Utara|Sulsel.
Kerajaan Islam di Maluku Utara adalah …|Ternate|Demak|Banten|Pasai|Ternate.
## PAI|Syukur dalam An-Nahl ayat 114
Surah An-Nahl ayat 114 memerintahkan memakan rezeki yang …|halal dan baik|banyak dan mahal|enak saja|apa saja|Halal.
Ucapan syukur dengan lisan adalah …|alhamdulillah|astagfirullah|innalillahi|subhanallah saja|Alhamdulillah.
=|An-Nahl adalah surah ke …|16|16.
=|Memakai nikmat untuk kebaikan adalah syukur dengan …|perbuatan|Perbuatan.
B|Bersyukur juga dilakukan dengan hati.|Hati.
S|Bersyukur cukup diucapkan tanpa perbuatan.|Perbuatan.
Bersyukur atas harta dapat dilakukan dengan …|bersedekah|menghambur-hamburkan|menyombongkan|menyimpan untuk pamer|Sedekah.
An-Nahl artinya …|lebah|sapi betina|semut|laba-laba|Lebah.
## PAI|Puasa wajib dan sunah
Puasa Arafah dilaksanakan pada tanggal …|9 Zulhijah|10 Muharam|1 Syawal|15 Syakban|9 Zulhijah.
Puasa wajib selain Ramadan adalah puasa …|qada dan nazar|Senin Kamis|Arafah|Asyura|Wajib.
=|Puasa Asyura dilaksanakan tanggal 10 bulan …|Muharam|Muharam.
=|Puasa Ayyamul Bid dilaksanakan tanggal 13, 14, dan …|15|15.
B|Puasa diharamkan pada hari raya Idulfitri.|Haram.
S|Puasa Senin Kamis termasuk puasa wajib.|Sunah.
Puasa sunah enam hari dilaksanakan pada bulan …|Syawal|Rajab|Ramadan|Muharam|Syawal.
Puasa dimulai sejak terbit fajar sampai …|terbenam matahari|tengah malam|zuhur|asar|Magrib.
## PAI|Sujud syukur, sahwi, dan tilawah
Sujud karena lupa dalam salat disebut sujud …|sahwi|syukur|tilawah|tahiyat|Sahwi.
Sujud ketika membaca ayat sajdah disebut sujud …|tilawah|sahwi|syukur|salat|Tilawah.
=|Sujud ketika mendapat nikmat disebut sujud …|syukur|Syukur.
=|Sujud sahwi dilakukan sebelum …|salam|Salam.
B|Sujud syukur dilakukan satu kali sujud.|Satu kali.
S|Sujud tilawah dilakukan karena lupa jumlah rakaat.|Sahwi.
Lupa tasyahud awal dalam salat diganti dengan sujud …|sahwi|tilawah|syukur|tambahan rakaat|Sahwi.
Lulus ujian dengan baik dapat disyukuri dengan sujud …|syukur|sahwi|tilawah|tahiyat|Syukur.
## PAI|Hormat kepada orang tua dan guru
Berbakti kepada orang tua disebut …|birrul walidain|takabur|ghibah|tabzir|Birrul walidain.
Allah melarang berkata … kepada orang tua.|"ah"|terima kasih|salam|maaf|Larangan.
=|Guru dihormati karena mengajarkan …|ilmu|Ilmu.
=|Bakti kepada orang tua yang dilakukan setelah salat adalah …|mendoakan;doa|Mendoakan.
B|Membantu pekerjaan rumah termasuk bakti kepada orang tua.|Bakti.
S|Membentak orang tua dibolehkan jika kita lelah.|Dilarang.
Mendengarkan guru menjelaskan termasuk adab …|menuntut ilmu|makan|tidur|bermain|Adab ilmu.
Rida Allah terletak pada rida …|orang tua|teman|tetangga|diri sendiri|Orang tua.
## PAI|Empati dan peduli sosial
Kemampuan merasakan perasaan orang lain disebut …|empati|egois|iri|takabur|Empati.
Rasulullah menggambarkan orang beriman seperti satu …|tubuh|rumah|pohon|bintang|Tubuh.
=|Memberi bantuan kepada anak yatim disebut … anak yatim.|menyantuni|Menyantuni.
=|Mengunjungi orang sakit disebut …|menjenguk|Menjenguk.
B|Menyisihkan uang jajan untuk korban banjir termasuk empati.|Empati.
S|Menertawakan teman yang tertimpa musibah termasuk empati.|Tidak.
Sikap empati kepada teman baru adalah …|mengajaknya bergabung|mengabaikannya|mengejeknya|menjauhinya|Mengajak.
Sikap empati kepada teman yang sedih adalah …|menghibur|menertawakan|meninggalkan|memarahi|Menghibur.
## PAI|Masa Khulafaurrasyidin
Khalifah pertama setelah Rasulullah wafat adalah …|Abu Bakar as-Siddiq|Umar bin Khattab|Usman bin Affan|Ali bin Abi Talib|Abu Bakar.
Khalifah yang menetapkan kalender hijriah adalah …|Umar bin Khattab|Abu Bakar|Usman bin Affan|Ali bin Abi Talib|Umar.
=|Khalifah yang menyeragamkan mushaf Al-Qur'an adalah Usman bin …|Affan|Usman bin Affan.
=|Khalifah keempat adalah Ali bin Abi …|Talib;Thalib|Ali.
B|Abu Bakar mengumpulkan Al-Qur'an dalam satu mushaf.|Abu Bakar.
S|Usman bin Affan adalah khalifah pertama.|Ketiga.
Julukan al-Faruq diberikan kepada …|Umar bin Khattab|Abu Bakar|Usman|Ali|Umar.
Jumlah Khulafaurrasyidin adalah …|empat|tiga|lima|enam|Empat.
"""

SAS += """
## PAI 1
0|Pada malam Lailatul Qadar, turun para malaikat dan ....|Jibril|Mikail|Israfil|Izrail|Jibril.
1|Al-Khabir artinya Allah Maha ....|Teliti|Melihat|Mendengar|Lembut|Al-Khabir.
2|Menyapa petugas kebersihan dengan ramah mencerminkan sikap ....|tawadu'|takabur|riya|hasad|Tawadu'.
3|Cara membersihkan najis mutawassitah adalah ....|dicuci sampai hilang bau, rasa, dan warna|dipercik air|dicuci tujuh kali dengan tanah|didiamkan|Sedang.
4|Usapan kedua dalam tayamum dilakukan pada ....|kedua tangan|kepala|telinga|kaki|Tangan.
5|Kerajaan Demak terletak di ....|Jawa Tengah|Aceh|Sulawesi Selatan|Maluku Utara|Demak.
## PAI 2
0|Bersyukur atas kesehatan dapat dilakukan dengan ....|rajin belajar dan beribadah|bermalas-malasan|begadang|menyombongkan diri|Syukur.
1|Puasa sunah setiap pekan dilakukan pada hari ....|Senin dan Kamis|Selasa dan Jumat|Sabtu dan Ahad|Rabu dan Jumat|Senin Kamis.
2|Sujud dalam salat termasuk ....|rukun salat|sunah salat|pembatal salat|makruh salat|Rukun.
3|Mengucapkan salam kepada guru termasuk adab ....|bertemu|makan|tidur|berpakaian|Salam.
4|Menolong tetangga yang kesulitan merupakan wujud ....|empati|takabur|kikir|iri|Empati.
5|Umar bin Khattab mendapat julukan al-Faruq yang artinya ....|pembeda benar dan salah|yang membenarkan|pintu ilmu|pemilik dua cahaya|Al-Faruq.
"""

TOPICS += """
## SUN
# 1|Basa, Sastra, jeung Tokoh
@ Kecap kantetan
min: 15
act: Kumpulkeun genep kecap kantetan tina koran atawa buku basa Sunda, tuluy tulis hartina.
mis: menganggap kecap kantetan sama dengan kecap rajékan
exp: Kecap kantetan adalah dua kata atau lebih yang digabung dan membentuk arti baru, mirip kata majemuk dalam bahasa Indonesia. Contohnya imah makan, rumah sakit, panjang leungeun, dan amis budi. Arti kecap kantetan bisa sebenarnya atau kiasan. Kecap kantetan berbeda dengan kecap rajékan yang berupa pengulangan kata.
ex: Panjang leungeun hartina resep maling. // Amis budi hartina someah atawa ramah.
pt: Gabungan dua kata atau lebih ; Membentuk arti baru ; Berbeda dengan kata ulang
sum: Kecap kantetan memperkaya kosakata bahasa Sunda.
fig: table Kecap kantetan | Harti ;; panjang leungeun | resep maling ;; amis budi | someah atawa ramah ;; gedé hulu | sombong ;; hampang birit | gancang dititah ;; beurat birit | hésé dititah ;; leutik haté | gampang sieun ~ Conto kecap kantetan.
@ Guguritan
min: 15
act: Tembangkeun hiji pada guguritan pupuh Kinanti babarengan jeung kulawarga.
mis: menulis guguritan tanpa mengikuti aturan pupuh
exp: Guguritan adalah karangan puisi berbahasa Sunda yang terikat aturan pupuh. Setiap pupuh memiliki guru wilangan atau jumlah suku kata tiap baris, guru lagu atau bunyi vokal akhir baris, dan jumlah baris tiap bait. Ada 17 pupuh, misalnya Kinanti, Sinom, Asmarandana, dan Dangdanggula. Guguritan biasanya ditembangkan.
ex: Pupuh Kinanti cocok untuk suasana menanti. // Pupuh Asmarandana bersuasana kasih sayang.
pt: Puisi terikat aturan pupuh ; Guru wilangan dan guru lagu ; Ada 17 pupuh
sum: Guguritan adalah puisi Sunda yang ditembangkan.
fig: table Pupuh | Watek ;; Kinanti | nungguan atawa prihatin ;; Sinom | gumbira ;; Asmarandana | kasmaran atawa kanyaah ;; Dangdanggula | tengtrem jeung agung ;; Mijil | sedih ;; Durma | ambek atawa sumanget perang ~ Pupuh jeung watekna.
@ Surat ondangan
min: 15
act: Jieun surat ondangan rapat kelas dina basa Sunda anu sopan.
mis: lupa mencantumkan waktu dan tempat acara dalam undangan
exp: Surat ondangan adalah surat untuk mengundang seseorang menghadiri acara. Bagian surat ondangan meliputi kop atau tanggal surat, nomor dan perihal, alamat yang diundang, salam pembuka, isi berupa hari, tanggal, waktu, tempat, dan acara, salam penutup, serta tanda tangan pengundang. Bahasa yang dipakai adalah basa hormat atau lemes.
ex: Dina poé Saptu, kaping 5 Désémber. // Wassalam, hormat kami, Pupuhu Kelas.
pt: Mengundang menghadiri acara ; Memuat hari, waktu, tempat, acara ; Memakai basa lemes
sum: Surat ondangan harus jelas dan sopan.
fig: table Bagian surat | Eusi ;; titimangsa | tempat jeung tanggal surat ;; perkawis | maksud surat ;; alamat | jalma nu diondang ;; salam bubuka | Assalamu'alaikum ;; eusi | poé, waktu, tempat, acara ;; panutup | hatur nuhun jeung tapak asma ~ Bagian surat ondangan.
@ Maca warta
min: 15
act: Baca warta basa Sunda tina radio atawa koran, tuluy catet unsur 5W+1H-na.
mis: membaca berita dengan intonasi datar dan cepat sekali
exp: Warta adalah berita, yaitu laporan tentang peristiwa yang benar-benar terjadi. Warta yang baik memenuhi unsur 5W+1H, dalam bahasa Sunda disebut naon, saha, iraha, di mana, naha, jeung kumaha. Saat membaca warta, perhatikan lafal, intonasi, jeda, dan ekspresi agar pendengar mudah memahami.
ex: Saha: barudak SMP. // Di mana: di alun-alun Bandung.
pt: Laporan peristiwa nyata ; Unsur naon, saha, iraha, di mana, naha, kumaha ; Lafal dan intonasi jelas
sum: Warta yang dibaca jelas mudah dipahami pendengar.
fig: table Unsur warta | Patalina ;; naon | kajadian ;; saha | palaku ;; iraha | waktu ;; di mana | tempat ;; naha | sabab ;; kumaha | prosés kajadian ~ Unsur warta 5W+1H.
@ Tatakrama di sakola
min: 15
act: Latihan ngobrol jeung guru maké basa hormat, tuluy catet kecap lemes nu dipaké.
mis: memakai basa loma kepada guru
exp: Tatakrama adalah aturan sopan santun dalam bersikap dan berbicara. Di sekolah, siswa memakai basa hormat kepada guru, mengucapkan salam, meminta izin sebelum keluar kelas, dan menghargai teman. Contoh kecap hormat antara lain sumping untuk datang, tuang untuk makan, dan angkat untuk pergi.
ex: Bapa guru parantos sumping. // Punten, abdi badé ka cai heula.
pt: Aturan sopan santun ; Basa hormat kepada guru ; Salam dan izin
sum: Tatakrama menunjukkan budi pekerti yang baik.
fig: table Basa loma | Basa hormat ka batur ;; datang | sumping ;; dahar | tuang ;; indit | angkat ;; saré | kulem ;; imah | bumi ;; ngomong | nyarios ~ Basa loma jeung basa hormat.
@ Pahlawan ti Jawa Barat
min: 15
act: Pilih hiji pahlawan ti Jawa Barat, tuluy jieun karangan pondok ngeunaan jasana.
mis: mengira semua pahlawan Jawa Barat berjuang dengan senjata
exp: Jawa Barat memiliki banyak pahlawan nasional. Dewi Sartika mendirikan Sakola Istri untuk pendidikan perempuan. Otto Iskandar Dinata dijuluki Si Jalak Harupat. Ir. H. Djuanda mencetuskan Deklarasi Djuanda tentang wilayah laut Indonesia. K.H. Zainal Mustafa memimpin perlawanan di Sukamanah, Tasikmalaya. Mohammad Toha dikenal dalam peristiwa Bandung Lautan Api.
ex: Dewi Sartika berjuang melalui pendidikan. // Wajah Otto Iskandar Dinata ada pada uang kertas.
pt: Dewi Sartika pendidikan perempuan ; Djuanda wilayah laut ; Mohammad Toha Bandung Lautan Api
sum: Pahlawan Jawa Barat berjuang dengan berbagai cara.
fig: table Pahlawan | Jasa ;; Dewi Sartika | ngadegkeun Sakola Istri ;; Otto Iskandar Dinata | Si Jalak Harupat ;; Ir. H. Djuanda | Deklarasi Djuanda ;; K.H. Zainal Mustafa | ngalawan Jepang di Sukamanah ;; Mohammad Toha | Bandung Lautan Api ;; R.A. Lasminingrat | pelopor atikan awéwé ~ Pahlawan ti Jawa Barat.
# 2|Carita, Média, jeung Kaarifan Lokal
@ Carita pantun
min: 15
act: Dengekeun rékaman carita pantun atawa baca ringkesan Lutung Kasarung, tuluy catet tokohna.
mis: mengira carita pantun sama dengan pantun Melayu empat baris
exp: Carita pantun adalah cerita lisan Sunda yang dibawakan juru pantun sambil diiringi kacapi. Carita pantun berkisah tentang kerajaan Pajajaran dan para menak. Pertunjukannya dilakukan semalam suntuk. Contohnya Lutung Kasarung, Mundinglaya di Kusumah, dan Ciung Wanara. Carita pantun berbeda dengan pantun Melayu.
ex: Juru pantun memetik kacapi sambil bercerita. // Lutung Kasarung berkisah tentang Purbasari.
pt: Cerita lisan diiringi kacapi ; Kisah kerajaan Pajajaran ; Dibawakan juru pantun
sum: Carita pantun adalah warisan sastra lisan Sunda.
fig: table Carita pantun | Tokoh ;; Lutung Kasarung | Purbasari ;; Mundinglaya di Kusumah | Mundinglaya ;; Ciung Wanara | Ciung Wanara jeung Hariangbanga ;; Badak Pamalang | Raden Tegalarang ;; Panggung Karaton | Ratu Pakuan ;; Sri Sadana | Dewi Sri ~ Conto carita pantun.
@ Novel Sunda
min: 15
act: Baca hiji bab novel Sunda di perpustakaan, tuluy caritakeun deui eusina.
mis: mengira novel Sunda baru muncul setelah kemerdekaan
exp: Novel Sunda pertama adalah Baruang ka nu Ngarora karya D.K. Ardiwinata yang terbit tahun 1914. Novel adalah karangan prosa panjang dengan tokoh dan alur yang kompleks. Unsur intrinsik novel meliputi tema, tokoh, alur, latar, sudut pandang, dan amanat. Novel Sunda lainnya antara lain Pangéran Kornél karya R. Memed Sastrahadiprawira.
ex: Baruang ka nu Ngarora artinya racun bagi kaum muda. // Pangéran Kornél berlatar zaman Daendels.
pt: Novel pertama Baruang ka nu Ngarora 1914 ; Prosa panjang dan kompleks ; Unsur intrinsik
sum: Novel Sunda memiliki sejarah panjang.
fig: table Unsur intrinsik | Harti ;; téma | jejer carita ;; palaku | tokoh dina carita ;; galur | runtuyan kajadian ;; latar | tempat jeung waktu ;; puseur sawangan | sudut pandang pangarang ;; amanat | pesen pangarang ~ Unsur intrinsik novel.
@ Média basa Sunda
min: 15
act: Teangan conto majalah, koran, radio, atawa kanal video basa Sunda, tuluy jieun daptarna.
mis: mengira bahasa Sunda tidak ada di media modern
exp: Bahasa Sunda hadir di berbagai media. Majalah Manglé terbit sejak 1957 dan menjadi majalah berbahasa Sunda tertua yang masih terbit. Ada juga koran Galura, majalah Cupumanik, radio dan televisi lokal yang menyiarkan acara berbahasa Sunda, serta kanal video di internet. Media ini membantu melestarikan bahasa Sunda.
ex: Majalah Manglé memuat carita pondok. // Siaran warta basa Sunda di televisi lokal.
pt: Majalah Manglé sejak 1957 ; Koran Galura dan Cupumanik ; Radio, televisi, internet
sum: Media membantu melestarikan bahasa Sunda.
fig: table Média | Jenis ;; Manglé | majalah mingguan ;; Galura | koran ;; Cupumanik | majalah bulanan ;; radio lokal | siaran sora ;; televisi lokal | siaran gambar ;; kanal vidéo | média internét ~ Média basa Sunda.
@ Laporan observasi
min: 15
act: Titénan hiji tutuwuhan di buruan imah, tuluy tulis laporan observasi pondok.
mis: memasukkan pendapat pribadi ke dalam laporan observasi
exp: Laporan observasi adalah tulisan yang berisi hasil pengamatan langsung terhadap suatu objek secara objektif. Strukturnya terdiri atas pernyataan umum atau klasifikasi, deskripsi bagian, dan kesimpulan. Laporan observasi memakai bahasa baku dan fakta, bukan pendapat pribadi.
ex: Tangkal cau kaasup tutuwuhan nu teu boga dahan. // Daunna lébar sarta panjang.
pt: Hasil pengamatan langsung ; Pernyataan umum, deskripsi, kesimpulan ; Fakta bukan pendapat
sum: Laporan observasi disusun berdasarkan fakta.
fig: table Bagian laporan | Eusi ;; judul | objék nu dititénan ;; pernyataan umum | klasifikasi objék ;; déskripsi bagian | ciri-ciri objék ;; kacindekan | hasil panitén ;; basa | baku jeung objektif ;; sumber | panitén langsung ~ Bagian laporan observasi.
@ Karajinan has Jawa Barat
min: 15
act: Teangan hiji karajinan has daérah anjeun, tuluy jieun poster ngeunaan bahan jeung gunana.
mis: mengira kerajinan Jawa Barat hanya angklung
exp: Jawa Barat memiliki banyak kerajinan khas. Angklung dari bambu berasal dari daerah Sunda dan diakui UNESCO pada 2010. Kerajinan anyaman bambu terkenal dari Tasikmalaya, keramik dari Plered Purwakarta, payung geulis dari Tasikmalaya, dan wayang golek dari kayu. Kerajinan ini menjadi sumber penghasilan dan identitas budaya.
ex: Payung geulis dihias lukisan bunga. // Keramik Plered dipakai sebagai pot hias.
pt: Angklung diakui UNESCO 2010 ; Anyaman dan payung geulis Tasikmalaya ; Keramik Plered
sum: Kerajinan khas memperkuat budaya dan ekonomi daerah.
fig: table Karajinan | Daérah ;; payung geulis | Tasikmalaya ;; kéramik | Plered Purwakarta ;; wayang golék | Bogor jeung Bandung ;; angklung | Saung Udjo Bandung ;; anyaman awi | Rajapolah Tasikmalaya ;; batik | Trusmi Cirebon ~ Karajinan has Jawa Barat.
@ Tutuwuhan ubar
min: 15
act: Tanyakeun ka kolot ngeunaan tutuwuhan ubar nu aya di buruan, tuluy catet gunana.
mis: memakai tanaman obat sembarangan tanpa bertanya kepada orang dewasa
exp: Tutuwuhan ubar adalah tanaman yang dimanfaatkan sebagai obat tradisional. Orang Sunda sejak dulu memakai tanaman di sekitar rumah, misalnya jahé untuk menghangatkan badan, koneng atau kunyit untuk perut, sereh untuk minuman hangat, dan daun jambu batu untuk sakit perut. Pemakaian tanaman obat sebaiknya dengan pengawasan orang dewasa.
ex: Wedang jahé diinum mun keur tiris. // Koneng dijieun jamu.
pt: Tanaman sebagai obat tradisional ; Jahé, koneng, sereh ; Pakai dengan pengawasan orang dewasa
sum: Tutuwuhan ubar adalah kearifan lokal Sunda.
fig: table Tutuwuhan | Bahasa Indonésia ;; jahé | jahe ;; koneng | kunyit ;; sereh | serai ;; cikur | kencur ;; laja | lengkuas ;; jambu batu | jambu biji ~ Ngaran tutuwuhan ubar.
"""

BANK += """
## SUN|Kecap kantetan
Kecap kantetan nyaéta gabungan dua kecap atawa leuwih nu ngawangun harti …|anyar|sarua|leungit|tibalik|Harti anyar.
Panjang leungeun hartina …|resep maling|resep nulung|leungeunna panjang|gancang digawé|Kiasan.
=|Amis budi hartina …|someah;ramah|Someah.
=|Gedé hulu hartina …|sombong|Sombong.
B|Hampang birit hartina gancang dititah.|Hampang birit.
S|Kecap kantetan sarua jeung kecap rajékan.|Béda.
Beurat birit hartina …|hésé dititah|gancang dititah|beurat awakna|resep diuk|Hésé dititah.
Leutik haté hartina …|gampang sieun|bageur pisan|haténa leutik|sombong|Gampang sieun.
## SUN|Guguritan
Guguritan nyaéta karangan puisi anu kauger ku aturan …|pupuh|wawacan|sajak bébas|carpon|Pupuh.
Jumlah engang dina unggal padalisan pupuh disebut guru …|wilangan|lagu|gatra|pada|Guru wilangan.
=|Sora vokal panungtung unggal padalisan disebut guru …|lagu|Guru lagu.
=|Jumlah pupuh aya …|17;tujuh belas|17.
B|Pupuh Sinom watekna gumbira.|Sinom.
S|Guguritan teu kauger ku aturan naon waé.|Pupuh.
Pupuh anu watekna sedih nyaéta …|Mijil|Sinom|Durma|Dangdanggula|Mijil.
Pupuh anu watekna ambek atawa sumanget perang nyaéta …|Durma|Kinanti|Asmarandana|Mijil|Durma.
## SUN|Surat ondangan
Surat ondangan dipaké pikeun … batur kana hiji acara.|ngondang|ngusir|nyarék|ngabéjaan harga|Ngondang.
Basa anu dipaké dina surat ondangan nyaéta basa …|lemes|kasar|loma ka sobat|Indonésia campur|Lemes.
=|Tempat jeung tanggal surat disebut …|titimangsa|Titimangsa.
=|Maksud surat disebut …|perkawis|Perkawis.
B|Surat ondangan kudu nyebutkeun waktu jeung tempat acara.|Eusi.
S|Surat ondangan teu perlu tapak asma pangondang.|Perlu.
Eusi surat ondangan ngawengku poé, waktu, tempat, jeung …|acara|harga|resép|cuaca|Acara.
Salam bubuka dina surat ondangan biasana …|Assalamu'alaikum|Wassalam|hatur nuhun|punten tos|Bubuka.
## SUN|Maca warta
Warta nyaéta béja ngeunaan kajadian anu …|bener-bener kajadian|rékaan|ngimpi|dongéng|Fakta.
Unsur warta anu nanyakeun palaku nyaéta …|saha|iraha|di mana|naha|Saha.
=|Unsur warta anu nanyakeun waktu nyaéta …|iraha|Iraha.
=|Unsur warta anu nanyakeun sabab nyaéta …|naha|Naha.
B|Maca warta kudu merhatikeun lafal jeung intonasi.|Lafal.
S|Warta hadé dibaca gancang pisan tanpa jeda.|Jeda.
Unsur warta anu nanyakeun tempat nyaéta …|di mana|saha|naon|kumaha|Tempat.
Unsur warta anu nanyakeun prosés kajadian nyaéta …|kumaha|naon|saha|iraha|Kumaha.
## SUN|Tatakrama di sakola
Basa hormat tina kecap datang pikeun batur nyaéta …|sumping|dongkap|datang|indit|Sumping.
Basa hormat tina kecap dahar pikeun batur nyaéta …|tuang|neda|emam|nyatu|Tuang.
=|Basa hormat tina kecap saré pikeun batur nyaéta …|kulem|Kulem.
=|Basa hormat tina kecap imah nyaéta …|bumi|Bumi.
B|Ka guru urang kudu maké basa hormat.|Hormat.
S|Ka guru hadé maké basa loma kawas ka sobat.|Hormat.
Basa hormat tina kecap indit pikeun batur nyaéta …|angkat|mios|leumpang|mulang|Angkat.
Basa hormat tina kecap ngomong pikeun batur nyaéta …|nyarios|ngomong|nyarita|ngobrol|Nyarios.
## SUN|Pahlawan ti Jawa Barat
Pahlawan anu ngadegkeun Sakola Istri nyaéta …|Dewi Sartika|Mohammad Toha|Ir. H. Djuanda|Otto Iskandar Dinata|Dewi Sartika.
Otto Iskandar Dinata dijuluki …|Si Jalak Harupat|Si Kabayan|Si Lutung|Si Kancil|Jalak Harupat.
=|Deklarasi ngeunaan wilayah laut Indonésia dicetuskeun ku Ir. H. …|Djuanda;Juanda|Djuanda.
=|K.H. Zainal Mustafa ngalawan Jepang di …|Sukamanah|Sukamanah.
B|Mohammad Toha dipikawanoh dina kajadian Bandung Lautan Api.|Toha.
S|Dewi Sartika berjuang ngaliwatan perang bedil.|Atikan.
R.A. Lasminingrat dipikawanoh salaku pelopor atikan …|awéwé|tentara|tatanén|perdagangan|Awéwé.
Sukamanah perenahna di …|Tasikmalaya|Bogor|Cirebon|Sukabumi|Tasikmalaya.
## SUN|Carita pantun
Carita pantun dibawakeun ku …|juru pantun|dalang wayang|pangarang novel|penyiar radio|Juru pantun.
Carita pantun diiringan ku …|kacapi|angklung|gitar|drum|Kacapi.
=|Carita pantun nyaritakeun karajaan …|Pajajaran|Pajajaran.
=|Tokoh awéwé dina Lutung Kasarung nyaéta …|Purbasari|Purbasari.
B|Pagelaran carita pantun dilaksanakeun sapeuting jeput.|Sapeuting.
S|Carita pantun sarua jeung pantun Melayu opat padalisan.|Béda.
Conto carita pantun nyaéta …|Mundinglaya di Kusumah|Si Kabayan|Malin Kundang|Timun Mas|Mundinglaya.
Carita pantun kaasup sastra …|lisan|tulisan modern|digital|terjemahan|Lisan.
## SUN|Novel Sunda
Novel Sunda munggaran nyaéta …|Baruang ka nu Ngarora|Pangéran Kornél|Si Kabayan|Lutung Kasarung|Baruang.
Novel Baruang ka nu Ngarora dikarang ku …|D.K. Ardiwinata|R. Memed Sastrahadiprawira|Ajip Rosidi|Dewi Sartika|Ardiwinata.
=|Novel Baruang ka nu Ngarora medal taun …|1914|1914.
=|Runtuyan kajadian dina novel disebut …|galur;alur|Galur.
B|Novel kaasup karangan prosa anu panjang.|Prosa.
S|Novel Sunda munggaran medal sanggeus kamerdékaan.|1914.
Novel Pangéran Kornél dikarang ku …|R. Memed Sastrahadiprawira|D.K. Ardiwinata|Moh. Ambri|Ajip Rosidi|Memed.
Tokoh dina carita disebut …|palaku|latar|amanat|téma|Palaku.
## SUN|Média basa Sunda
Majalah basa Sunda anu medal ti taun 1957 nyaéta …|Manglé|Galura|Cupumanik|Bobo|Manglé.
Galura kaasup média …|koran|radio|majalah bulanan|televisi|Koran.
=|Cupumanik nyaéta majalah …|bulanan|Bulanan.
=|Manglé kaasup majalah …|mingguan|Mingguan.
B|Média ngabantu ngamumulé basa Sunda.|Mumulé.
S|Basa Sunda teu aya dina média modéren.|Aya.
Kanal vidéo basa Sunda kaasup média …|internét|citak|koran|majalah|Internét.
Siaran warta basa Sunda bisa didangukeun dina …|radio lokal|kalénder|buku tulis|papan tulis|Radio.
## SUN|Laporan observasi
Laporan observasi eusina hasil … langsung.|panitén|lamunan|dongéng|impian|Panitén.
Basa dina laporan observasi kudu … jeung objektif.|baku|kasar|loma|rékaan|Baku.
=|Bagian panutup laporan observasi disebut …|kacindekan|Kacindekan.
=|Bagian anu nétélakeun ciri-ciri objék disebut … bagian.|déskripsi;deskripsi|Déskripsi.
B|Laporan observasi dumasar kana fakta.|Fakta.
S|Laporan observasi eusina pamadegan pribadi.|Fakta.
Bagian anu eusina klasifikasi objék disebut …|pernyataan umum|kacindekan|judul|sumber|Pernyataan umum.
Sumber laporan observasi nyaéta …|panitén langsung|carita babaturan|impian|gosip|Langsung.
## SUN|Karajinan has Jawa Barat
Payung geulis asalna ti …|Tasikmalaya|Cirebon|Purwakarta|Bogor|Tasikmalaya.
Kéramik kawentar ti Plered …|Purwakarta|Garut|Ciamis|Sumedang|Purwakarta.
=|Angklung dijieun tina …|awi;bambu|Awi.
=|Angklung diaku ku UNESCO taun …|2010|2010.
B|Batik Trusmi asalna ti Cirebon.|Trusmi.
S|Karajinan Jawa Barat ngan ukur angklung.|Loba.
Anyaman awi kawentar ti Rajapolah …|Tasikmalaya|Bandung|Bogor|Cirebon|Rajapolah.
Wayang golék dijieun tina …|kai|beusi|kertas|plastik|Kai.
## SUN|Tutuwuhan ubar
Koneng dina basa Indonésia nyaéta …|kunyit|jahe|kencur|serai|Kunyit.
Jahé biasana dipaké pikeun …|ngahaneutkeun awak|ngaréndéngkeun huntu|ngelirkeun buuk|ngabersihan lanté|Haneut.
=|Sereh dina basa Indonésia nyaéta …|serai|Serai.
=|Cikur dina basa Indonésia nyaéta …|kencur|Kencur.
B|Maké tutuwuhan ubar sabaiknya diawaskeun ku kolot.|Kolot.
S|Tutuwuhan ubar meunang dipaké sambarangan tanpa nanya.|Nanya heula.
Laja dina basa Indonésia nyaéta …|lengkuas|kunyit|jahe|kencur|Lengkuas.
Jambu batu dina basa Indonésia nyaéta …|jambu biji|jambu air|jambu mete|jambu bol|Jambu biji.
"""

SAS += """
## SUN 1
0|Kecap kantetan anu hartina sombong nyaéta ....|gedé hulu|amis budi|hampang birit|leutik haté|Gedé hulu.
1|Pupuh anu watekna tengtrem jeung agung nyaéta ....|Dangdanggula|Mijil|Durma|Sinom|Dangdanggula.
2|Bagian surat ondangan anu eusina hatur nuhun jeung tapak asma nyaéta ....|panutup|perkawis|titimangsa|alamat|Panutup.
3|Unsur warta naon patali jeung ....|kajadian|palaku|waktu|tempat|Naon.
4|Basa hormat tina kecap imah nyaéta ....|bumi|rorompok|saung|pondok|Bumi.
5|Pahlawan anu dijuluki Si Jalak Harupat nyaéta ....|Otto Iskandar Dinata|Mohammad Toha|Ir. H. Djuanda|Dewi Sartika|Otto.
## SUN 2
0|Carita pantun anu nyaritakeun Ciung Wanara jeung Hariangbanga nyaéta ....|Ciung Wanara|Lutung Kasarung|Mundinglaya di Kusumah|Sri Sadana|Ciung Wanara.
1|Pesen pangarang dina novel disebut ....|amanat|téma|latar|galur|Amanat.
2|Majalah basa Sunda anu medal unggal bulan nyaéta ....|Cupumanik|Manglé|Galura|Pikiran Rakyat|Cupumanik.
3|Bagian laporan observasi anu nétélakeun objék nu dititénan nyaéta ....|judul|kacindekan|sumber|basa|Judul.
4|Batik Trusmi asalna ti ....|Cirebon|Tasikmalaya|Purwakarta|Bogor|Cirebon.
5|Wedang jahé diinum mun keur ....|tiris|panas|lapar|bungah|Tiris.
"""
