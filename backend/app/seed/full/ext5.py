TOPICS = ""
BANK = ""
SAS = ""

TOPICS += """
## MAT
# 1|Pecahan, Desimal, dan Persen
@ Pecahan desimal
min: 12
act: Cari harga barang di brosur yang memakai koma, lalu baca nilai desimalnya.
mis: mengira 0,5 lebih kecil dari 0,25 karena angkanya lebih sedikit
exp: Pecahan desimal adalah pecahan yang ditulis dengan tanda koma. Angka setelah koma menunjukkan persepuluhan, perseratusan, dan seterusnya. Misalnya 0,5 artinya lima persepuluh atau 5/10, dan 0,25 artinya dua puluh lima perseratus atau 25/100. Untuk membandingkan desimal, samakan banyak angka di belakang koma.
ex: 0,5 = 5/10 = 1/2. // 0,50 lebih besar dari 0,25.
pt: Angka pertama setelah koma adalah persepuluhan ; Angka kedua adalah perseratusan ; Samakan banyak angka di belakang koma saat membandingkan
sum: Pecahan desimal ditulis dengan tanda koma.
fig: table Pecahan biasa | Desimal ;; 1/2 | 0,5 ;; 1/4 | 0,25 ;; 3/4 | 0,75 ;; 1/10 | 0,1 ;; 1/5 | 0,2 ;; 3/100 | 0,03 ~ Pecahan biasa dan bentuk desimalnya.
@ Persen
min: 12
act: Cari label diskon di toko atau iklan, lalu hitung potongan harganya bersama orang tua.
mis: mengira 50% dari 80 adalah 50
exp: Persen artinya per seratus dan ditulis dengan lambang %. Misalnya 25% sama dengan 25/100. Untuk mencari persen dari suatu bilangan, kalikan persennya dengan bilangan itu lalu bagi 100. Contohnya 10% dari 200 adalah 10 × 200 : 100 = 20.
ex: 50% dari 80 = 40. // Diskon 20% dari Rp50.000 = Rp10.000.
pt: Persen artinya per seratus ; 25% = 25/100 ; Persen dari bilangan = persen × bilangan : 100
sum: Persen menunjukkan bagian dari seratus.
fig: table Persen | Pecahan biasa ;; 50% | 1/2 ;; 25% | 1/4 ;; 75% | 3/4 ;; 10% | 1/10 ;; 20% | 1/5 ;; 100% | seluruhnya ~ Persen dan pecahan senilai.
@ Mengubah bentuk pecahan
min: 12
act: Buat kartu pasangan pecahan biasa, desimal, dan persen, lalu mainkan permainan memasangkan.
mis: menulis 3/4 sebagai 3,4
exp: Pecahan biasa, desimal, dan persen dapat saling diubah. Pecahan biasa diubah ke desimal dengan membagi pembilang oleh penyebut, atau mengubah penyebut menjadi 10 atau 100. Desimal diubah ke persen dengan mengalikan 100. Persen diubah ke pecahan dengan menulisnya per 100, lalu disederhanakan.
ex: 3/4 = 75/100 = 0,75 = 75%. // 40% = 40/100 = 2/5.
pt: Pecahan ke desimal: bagi pembilang dengan penyebut ; Desimal ke persen: kali 100 ; Persen ke pecahan: tulis per 100
sum: Satu nilai bisa ditulis dalam tiga bentuk.
fig: table Desimal | Persen ;; 0,5 | 50% ;; 0,25 | 25% ;; 0,75 | 75% ;; 0,4 | 40% ;; 0,1 | 10% ;; 0,05 | 5% ~ Desimal dan persen yang senilai.
@ Faktor dan kelipatan
min: 12
act: Susun 12 kancing dalam beberapa bentuk persegi panjang untuk menemukan faktor 12.
mis: tertukar antara faktor dan kelipatan
exp: Faktor adalah bilangan yang membagi habis suatu bilangan. Faktor dari 12 adalah 1, 2, 3, 4, 6, dan 12. Kelipatan adalah hasil kali suatu bilangan dengan 1, 2, 3, dan seterusnya. Kelipatan 4 adalah 4, 8, 12, 16, dan seterusnya. Bilangan prima hanya memiliki dua faktor, yaitu 1 dan bilangan itu sendiri.
ex: Faktor 10: 1, 2, 5, 10. // Kelipatan 3: 3, 6, 9, 12, 15.
pt: Faktor membagi habis ; Kelipatan hasil perkalian berurutan ; Bilangan prima punya dua faktor
sum: Faktor dan kelipatan dasar untuk KPK dan FPB.
fig: table Bilangan | Faktornya ;; 6 | 1, 2, 3, 6 ;; 8 | 1, 2, 4, 8 ;; 9 | 1, 3, 9 ;; 12 | 1, 2, 3, 4, 6, 12 ;; 7 | 1 dan 7 ;; 15 | 1, 3, 5, 15 ~ Faktor beberapa bilangan.
@ Operasi hitung campuran
min: 12
act: Tulis soal belanja keluarga yang memakai tambah, kurang, kali, dan bagi, lalu hitung bersama.
mis: mengerjakan dari kiri ke kanan tanpa mendahulukan perkalian
exp: Operasi hitung campuran mengikuti aturan urutan. Kerjakan dulu yang ada di dalam kurung. Lalu kerjakan perkalian dan pembagian dari kiri. Terakhir kerjakan penjumlahan dan pengurangan dari kiri.
ex: 5 + 3 × 4 = 5 + 12 = 17. // (5 + 3) × 4 = 8 × 4 = 32.
pt: Dahulukan tanda kurung ; Lalu kali dan bagi dari kiri ; Terakhir tambah dan kurang dari kiri
sum: Urutan operasi menentukan hasil yang benar.
fig: table Soal | Hasil ;; 5 + 3 × 4 | 17 ;; (5 + 3) × 4 | 32 ;; 24 − 12 : 4 | 21 ;; 6 × 5 − 10 | 20 ;; 18 : 3 + 7 | 13 ;; (10 − 4) × 2 | 12 ~ Contoh operasi hitung campuran.
@ Kecepatan, jarak, dan waktu
min: 12
act: Catat jarak dan waktu perjalanan ke sekolah, lalu hitung kecepatan rata-ratamu.
mis: membagi waktu dengan jarak untuk mencari kecepatan
exp: Kecepatan adalah jarak yang ditempuh dalam waktu tertentu. Rumusnya kecepatan = jarak : waktu. Jarak = kecepatan × waktu, dan waktu = jarak : kecepatan. Satuan kecepatan misalnya km/jam atau m/detik.
ex: Jarak 120 km ditempuh 2 jam, kecepatannya 60 km/jam. // Kecepatan 40 km/jam selama 3 jam, jaraknya 120 km.
pt: Kecepatan = jarak : waktu ; Jarak = kecepatan × waktu ; Waktu = jarak : kecepatan
sum: Kecepatan, jarak, dan waktu saling berhubungan.
fig: table Jarak dan waktu | Kecepatan ;; 120 km dalam 2 jam | 60 km/jam ;; 90 km dalam 3 jam | 30 km/jam ;; 200 km dalam 4 jam | 50 km/jam ;; 40 km dalam 1 jam | 40 km/jam ;; 150 km dalam 2 jam | 75 km/jam ;; 100 m dalam 20 detik | 5 m/detik ~ Menghitung kecepatan.
# 2|Luas, Volume, dan Data
@ Luas persegi dan persegi panjang
min: 12
act: Ukur panjang dan lebar lantai kamar, lalu hitung luasnya dalam meter persegi.
mis: menjumlahkan panjang dan lebar untuk mencari luas
exp: Luas adalah ukuran daerah di dalam bangun datar. Luas persegi panjang = panjang × lebar. Luas persegi = sisi × sisi. Satuan luas adalah satuan persegi, misalnya cm² dan m².
ex: Persegi panjang 8 cm × 5 cm, luasnya 40 cm². // Persegi sisi 6 cm, luasnya 36 cm².
pt: Luas persegi panjang = p × l ; Luas persegi = s × s ; Satuan luas berpangkat dua
sum: Luas dihitung dengan mengalikan, bukan menjumlahkan.
fig: table Bangun | Luas ;; persegi panjang 8 × 5 cm | 40 cm² ;; persegi sisi 6 cm | 36 cm² ;; persegi panjang 10 × 3 m | 30 m² ;; persegi sisi 9 m | 81 m² ;; persegi panjang 12 × 4 cm | 48 cm² ;; persegi sisi 5 cm | 25 cm² ~ Contoh menghitung luas.
@ Luas jajargenjang
min: 12
act: Gunting jajargenjang dari kertas, potong satu segitiganya, lalu pindahkan sehingga menjadi persegi panjang.
mis: mengalikan alas dengan sisi miring, bukan dengan tinggi
exp: Jajargenjang memiliki dua pasang sisi sejajar. Luas jajargenjang = alas × tinggi. Tinggi adalah garis tegak lurus dari alas ke sisi di depannya, bukan sisi miringnya. Jajargenjang dapat dipotong dan disusun menjadi persegi panjang dengan luas yang sama.
ex: Alas 10 cm dan tinggi 6 cm, luasnya 60 cm². // Alas 7 m dan tinggi 4 m, luasnya 28 m².
pt: Luas = alas × tinggi ; Tinggi tegak lurus dengan alas ; Bisa diubah menjadi persegi panjang
sum: Luas jajargenjang memakai alas dan tinggi.
fig: table Alas dan tinggi | Luas jajargenjang ;; 10 cm dan 6 cm | 60 cm² ;; 7 m dan 4 m | 28 m² ;; 12 cm dan 4 cm | 48 cm² ;; 8 cm dan 3 cm | 24 cm² ;; 9 m dan 9 m | 81 m² ;; 15 cm dan 2 cm | 30 cm² ~ Menghitung luas jajargenjang.
@ Luas trapesium
min: 12
act: Gambar trapesium di kertas berpetak, lalu hitung luasnya dengan rumus dan dengan menghitung petak.
mis: lupa membagi dua setelah menjumlahkan sisi sejajar dan mengalikan tinggi
exp: Trapesium memiliki sepasang sisi sejajar. Luas trapesium = (jumlah sisi sejajar × tinggi) : 2. Contohnya sisi sejajar 6 cm dan 10 cm dengan tinggi 4 cm, luasnya (6 + 10) × 4 : 2 = 32 cm².
ex: (6 + 10) × 4 : 2 = 32 cm². // (5 + 7) × 6 : 2 = 36 cm².
pt: Trapesium punya sepasang sisi sejajar ; Jumlahkan sisi sejajar ; Kali tinggi lalu bagi 2
sum: Luas trapesium = jumlah sisi sejajar × tinggi : 2.
fig: table Sisi sejajar dan tinggi | Luas trapesium ;; 6 dan 10, tinggi 4 | 32 cm² ;; 5 dan 7, tinggi 6 | 36 cm² ;; 8 dan 12, tinggi 5 | 50 cm² ;; 3 dan 9, tinggi 4 | 24 cm² ;; 10 dan 14, tinggi 10 | 120 cm² ;; 4 dan 6, tinggi 2 | 10 cm² ~ Menghitung luas trapesium.
@ Satuan volume dan debit
min: 12
act: Isi botol 1,5 liter dengan gelas ukur 250 ml, lalu hitung berapa gelas yang diperlukan.
mis: mengira 1 liter sama dengan 100 ml
exp: Satuan volume yang sering dipakai adalah liter dan mililiter. 1 liter = 1.000 ml = 1 dm³. 1 ml = 1 cm³. Debit adalah banyaknya air yang mengalir setiap satuan waktu, misalnya liter per menit. Debit = volume : waktu.
ex: 2 liter = 2.000 ml. // 60 liter dalam 5 menit, debitnya 12 liter/menit.
pt: 1 liter = 1.000 ml ; 1 liter = 1 dm³ ; Debit = volume : waktu
sum: Volume dan debit dipakai untuk mengukur zat cair.
fig: table Ukuran | Sama dengan ;; 1 liter | 1.000 ml ;; 1 dm³ | 1 liter ;; 1 cm³ | 1 ml ;; setengah liter | 500 ml ;; 2,5 liter | 2.500 ml ;; 1 m³ | 1.000 liter ~ Hubungan satuan volume.
@ Membaca diagram batang
min: 12
act: Catat jumlah buku yang dibaca anggota keluarga selama sebulan, lalu buat diagram batangnya.
mis: membaca tinggi batang tanpa melihat skala sumbu
exp: Diagram batang menyajikan data dengan batang-batang. Panjang atau tinggi batang menunjukkan banyaknya data. Baca judul, sumbu mendatar, sumbu tegak, dan skala. Dari diagram batang kita bisa mencari data terbanyak, tersedikit, selisih, dan jumlah.
ex: Batang tertinggi menunjukkan data terbanyak. // Selisih dua data dihitung dari nilai batangnya.
pt: Baca judul dan skala ; Tinggi batang menunjukkan banyak data ; Bandingkan batang untuk mencari selisih
sum: Diagram batang memudahkan membandingkan data.
fig: table Hari | Buku dipinjam ;; Senin | 12 buku ;; Selasa | 8 buku ;; Rabu | 15 buku ;; Kamis | 6 buku ;; Jumat | 10 buku ;; Sabtu | 4 buku ~ Data diagram batang buku yang dipinjam di perpustakaan.
@ Sifat-sifat bangun datar
min: 12
act: Gunting beberapa bangun datar dari kertas, lalu lipat untuk memeriksa sisi dan sudut yang sama.
mis: mengira semua sisi belah ketupat membentuk sudut siku-siku
exp: Setiap bangun datar memiliki sifat. Persegi memiliki 4 sisi sama panjang dan 4 sudut siku-siku. Persegi panjang memiliki 2 pasang sisi sama panjang dan 4 sudut siku-siku. Belah ketupat memiliki 4 sisi sama panjang dan diagonal yang saling tegak lurus. Layang-layang memiliki 2 pasang sisi berdekatan yang sama panjang.
ex: Ubin lantai berbentuk persegi. // Layang-layang mainan memiliki diagonal yang tegak lurus.
pt: Persegi: 4 sisi sama, 4 sudut siku-siku ; Belah ketupat: 4 sisi sama ; Layang-layang: 2 pasang sisi berdekatan sama
sum: Sifat sisi dan sudut membedakan bangun datar.
fig: table Bangun datar | Sifat khusus ;; persegi | 4 sisi sama dan 4 siku-siku ;; persegi panjang | sisi berhadapan sama dan 4 siku-siku ;; belah ketupat | 4 sisi sama tanpa siku-siku ;; jajargenjang | sisi berhadapan sejajar ;; trapesium | sepasang sisi sejajar ;; layang-layang | 2 pasang sisi berdekatan sama ~ Sifat-sifat bangun datar.
"""

BANK += """
## MAT|Pecahan desimal
Bentuk desimal dari 3/10 adalah …|0,3|3,10|0,03|30|Tiga persepuluh.
Bentuk pecahan biasa dari 0,25 adalah …|1/4|2/5|1/25|25/10|25/100 = 1/4.
=|Bentuk desimal dari 1/2 adalah …|0,5;0,50|1/2 = 5/10.
=|Bentuk desimal dari 7/100 adalah …|0,07|Tujuh perseratus.
B|0,5 lebih besar dari 0,25.|0,50 > 0,25.
S|0,3 lebih kecil dari 0,25.|0,30 > 0,25.
Urutan dari yang terkecil adalah …|0,2; 0,35; 0,5|0,5; 0,35; 0,2|0,35; 0,2; 0,5|0,2; 0,5; 0,35|Samakan angka di belakang koma.
Hasil 0,4 + 0,35 adalah …|0,75|0,39|0,7|7,5|Sejajarkan koma.
## MAT|Persen
Lambang persen adalah …|%|/|:|,|Persen ditulis %.
25% dari 80 adalah …|20|25|40|60|25 × 80 : 100.
=|50% dari 60 adalah …|30|Setengah dari 60.
=|10% dari 300 adalah …|30|10 × 300 : 100.
B|100% berarti seluruhnya.|Seratus per seratus.
S|20% sama dengan 1/2.|20% = 1/5.
Harga baju Rp100.000 diskon 30%. Besar diskonnya …|Rp30.000|Rp70.000|Rp3.000|Rp130.000|30 × 100.000 : 100.
Persen artinya per …|seratus|sepuluh|seribu|satu|Per seratus.
## MAT|Mengubah bentuk pecahan
Bentuk persen dari 0,6 adalah …|60%|6%|0,6%|600%|0,6 × 100.
Bentuk desimal dari 3/5 adalah …|0,6|0,35|3,5|0,53|3/5 = 6/10.
=|Bentuk persen dari 1/4 adalah …|25%;25|1/4 = 25/100.
=|Bentuk pecahan paling sederhana dari 20% adalah …|1/5|20/100 = 1/5.
B|0,75 sama dengan 75%.|0,75 × 100.
S|3/4 sama dengan 3,4.|3/4 = 0,75.
Pecahan yang nilainya sama dengan 0,8 adalah …|4/5|8/100|1/8|5/4|0,8 = 8/10 = 4/5.
Bentuk persen dari 7/10 adalah …|70%|7%|0,7%|17%|7/10 = 70/100.
## MAT|Faktor dan kelipatan
Faktor dari 10 adalah …|1, 2, 5, 10|1, 2, 3, 10|2, 4, 6, 10|10, 20, 30|Membagi habis 10.
Kelipatan 6 adalah …|6, 12, 18, 24|1, 2, 3, 6|6, 10, 14, 18|6, 16, 26, 36|6 × 1, 2, 3, 4.
=|Bilangan prima terkecil adalah …|2|2 hanya punya faktor 1 dan 2.
=|Banyak faktor dari 9 adalah …|3|1, 3, 9.
B|Bilangan 7 adalah bilangan prima.|Faktor 7 hanya 1 dan 7.
S|Bilangan 9 adalah bilangan prima.|9 punya faktor 3.
Kelipatan persekutuan 2 dan 3 yang terkecil adalah …|6|5|12|1|KPK 2 dan 3.
Faktor yang sama dari 8 dan 12 adalah …|1, 2, 4|1, 2, 3|2, 4, 8|1, 3, 4|Faktor persekutuan.
## MAT|Operasi hitung campuran
Hasil dari 4 + 6 × 2 adalah …|16|20|12|14|Kali dulu.
Hasil dari 30 − 18 : 3 adalah …|24|4|27|21|Bagi dulu.
=|Hasil dari (8 + 2) × 5 adalah …|50|Kurung dulu.
=|Hasil dari 7 × 3 − 6 adalah …|15|21 − 6.
B|Pada 9 − 2 × 3, perkalian dikerjakan lebih dulu.|Kali dulu.
S|Hasil 2 + 3 × 4 adalah 20.|Hasilnya 14.
Hasil dari 36 : (4 + 2) adalah …|6|11|9|15|36 : 6.
Ibu membeli 3 kg gula Rp15.000 per kg dan membayar Rp50.000. Kembaliannya …|Rp5.000|Rp35.000|Rp10.000|Rp15.000|50.000 − 3 × 15.000.
## MAT|Kecepatan, jarak, dan waktu
Rumus kecepatan adalah …|jarak : waktu|waktu : jarak|jarak × waktu|jarak + waktu|Kecepatan = jarak : waktu.
Mobil menempuh 180 km dalam 3 jam. Kecepatannya …|60 km/jam|90 km/jam|540 km/jam|30 km/jam|180 : 3.
=|Sepeda melaju 15 km/jam selama 2 jam. Jaraknya … km.|30|15 × 2.
=|Jarak 100 km ditempuh dengan kecepatan 50 km/jam. Waktunya … jam.|2|100 : 50.
B|Satuan km/jam adalah satuan kecepatan.|Kilometer per jam.
S|Jarak = kecepatan : waktu.|Jarak = kecepatan × waktu.
Bus melaju 40 km/jam selama 1,5 jam. Jarak tempuhnya …|60 km|40 km|80 km|55 km|40 × 1,5.
Pelari menempuh 400 m dalam 80 detik. Kecepatannya …|5 m/detik|4 m/detik|8 m/detik|320 m/detik|400 : 80.
## MAT|Luas persegi dan persegi panjang
Luas persegi panjang 9 cm × 4 cm adalah …|36 cm²|26 cm²|13 cm²|18 cm²|9 × 4.
Luas persegi bersisi 7 cm adalah …|49 cm²|28 cm²|14 cm²|21 cm²|7 × 7.
=|Rumus luas persegi panjang adalah panjang × …|lebar|Panjang × lebar.
=|Luas persegi bersisi 10 m adalah … m².|100|10 × 10.
B|Satuan luas misalnya cm².|Satuan persegi.
S|Luas persegi panjang dihitung dengan menjumlahkan panjang dan lebar.|Dikalikan.
Lantai kamar 4 m × 3 m dipasang karpet. Luas karpet …|12 m²|7 m²|14 m²|24 m²|4 × 3.
Persegi luasnya 64 cm². Panjang sisinya …|8 cm|16 cm|32 cm|6 cm|8 × 8 = 64.
## MAT|Luas jajargenjang
Rumus luas jajargenjang adalah …|alas × tinggi|alas + tinggi|2 × alas|sisi × sisi|Alas × tinggi.
Jajargenjang alas 11 cm dan tinggi 5 cm. Luasnya …|55 cm²|16 cm²|32 cm²|110 cm²|11 × 5.
=|Jajargenjang alas 6 m dan tinggi 4 m. Luasnya … m².|24|6 × 4.
=|Jajargenjang luasnya 40 cm² dan alasnya 8 cm. Tingginya … cm.|5|40 : 8.
B|Tinggi jajargenjang tegak lurus terhadap alas.|Tegak lurus.
S|Luas jajargenjang dihitung dengan alas × sisi miring.|Alas × tinggi.
Jajargenjang dapat dipotong dan disusun menjadi …|persegi panjang|lingkaran|segitiga sama sisi|trapesium siku|Persegi panjang.
Banyak pasang sisi sejajar pada jajargenjang adalah …|2|1|3|4|Dua pasang.
## MAT|Luas trapesium
Rumus luas trapesium adalah …|jumlah sisi sejajar × tinggi : 2|alas × tinggi|sisi × sisi|jumlah semua sisi|Rumus trapesium.
Trapesium sisi sejajar 4 cm dan 8 cm, tinggi 5 cm. Luasnya …|30 cm²|60 cm²|40 cm²|17 cm²|(4 + 8) × 5 : 2.
=|Trapesium sisi sejajar 10 cm dan 6 cm, tinggi 3 cm. Luasnya … cm².|24|(10 + 6) × 3 : 2.
=|Trapesium memiliki … pasang sisi sejajar.|1;satu;sepasang|Sepasang.
B|Rumus luas trapesium dibagi 2.|Dibagi 2.
S|Trapesium memiliki dua pasang sisi sejajar.|Hanya sepasang.
Trapesium sisi sejajar 7 m dan 9 m, tinggi 4 m. Luasnya …|32 m²|64 m²|20 m²|36 m²|(7 + 9) × 4 : 2.
Bentuk atap rumah yang dilihat dari samping sering berbentuk …|trapesium|lingkaran|bintang|segi enam|Trapesium.
## MAT|Satuan volume dan debit
1 liter sama dengan …|1.000 ml|100 ml|10 ml|10.000 ml|1 L = 1.000 ml.
3 liter sama dengan …|3.000 ml|300 ml|30 ml|30.000 ml|3 × 1.000.
=|1 dm³ sama dengan … liter.|1;satu|1 dm³ = 1 L.
=|500 ml sama dengan … liter.|0,5;setengah|500 : 1.000.
B|1 ml sama dengan 1 cm³.|1 ml = 1 cm³.
S|1 liter sama dengan 100 ml.|1 liter = 1.000 ml.
Keran mengalirkan 60 liter dalam 10 menit. Debitnya …|6 liter/menit|600 liter/menit|50 liter/menit|70 liter/menit|60 : 10.
Botol 1,5 liter diisi gelas 250 ml. Banyak gelas …|6|4|5|8|1.500 : 250.
## MAT|Membaca diagram batang
Pada diagram batang, data terbanyak ditunjukkan oleh batang …|tertinggi|terendah|paling kiri|paling tipis|Batang tertinggi.
Diagram batang: apel 12, jeruk 8. Selisihnya …|4|20|12|8|12 − 8.
=|Diagram batang: A 5, B 7, C 3. Jumlah seluruhnya …|15|5 + 7 + 3.
=|Garis tegak pada diagram batang disebut sumbu …|tegak;vertikal|Sumbu tegak.
B|Skala diagram batang harus dibaca dengan teliti.|Skala menentukan nilai.
S|Batang terendah menunjukkan data terbanyak.|Data tersedikit.
Diagram batang: kelas A 30, kelas B 25, kelas C 35 siswa. Kelas paling banyak …|C|A|B|sama banyak|35 terbanyak.
Manfaat diagram batang adalah …|memudahkan membandingkan data|menghitung luas|mengukur sudut|menulis cerita|Membandingkan.
## MAT|Sifat-sifat bangun datar
Bangun datar dengan 4 sisi sama panjang dan 4 sudut siku-siku adalah …|persegi|belah ketupat|jajargenjang|trapesium|Persegi.
Bangun yang memiliki 4 sisi sama panjang tetapi tidak bersudut siku-siku adalah …|belah ketupat|persegi|persegi panjang|trapesium|Belah ketupat.
=|Bangun datar dengan sepasang sisi sejajar adalah …|trapesium|Trapesium.
=|Banyak sudut siku-siku pada persegi panjang adalah …|4;empat|Empat.
B|Diagonal belah ketupat saling tegak lurus.|Tegak lurus.
S|Jajargenjang memiliki 4 sudut siku-siku.|Tidak siku-siku.
Bangun datar yang memiliki 2 pasang sisi berdekatan sama panjang adalah …|layang-layang|persegi panjang|trapesium|jajargenjang|Layang-layang.
Sisi-sisi yang berhadapan pada persegi panjang …|sama panjang dan sejajar|tidak sama panjang|saling tegak lurus|berpotongan|Sama dan sejajar.
"""

SAS += """
## MAT 1
0|Bentuk desimal dari 4/5 adalah ....|0,8|0,45|4,5|0,08|4/5 = 8/10.
1|40% dari 150 adalah ....|60|40|90|110|40 × 150 : 100.
2|Bentuk persen dari 0,35 adalah ....|35%|3,5%|0,35%|350%|0,35 × 100.
3|Faktor dari 18 adalah ....|1, 2, 3, 6, 9, 18|1, 2, 4, 8, 18|2, 4, 6, 18|1, 3, 5, 18|Membagi habis 18.
4|Hasil dari 50 − 4 × 8 adalah ....|18|368|32|42|Kali dulu.
5|Motor menempuh 150 km dengan kecepatan 50 km/jam. Waktunya ....|3 jam|2 jam|4 jam|5 jam|150 : 50.
## MAT 2
0|Luas persegi panjang 15 cm × 6 cm adalah ....|90 cm²|42 cm²|21 cm²|60 cm²|15 × 6.
1|Jajargenjang alas 14 cm dan tinggi 5 cm. Luasnya ....|70 cm²|19 cm²|35 cm²|140 cm²|14 × 5.
2|Trapesium sisi sejajar 8 cm dan 12 cm, tinggi 6 cm. Luasnya ....|60 cm²|120 cm²|26 cm²|48 cm²|(8 + 12) × 6 : 2.
3|Air 4 liter sama dengan ....|4.000 ml|400 ml|40 ml|40.000 ml|4 × 1.000.
4|Diagram batang: Senin 9, Selasa 14, Rabu 11 pengunjung. Hari paling ramai ....|Selasa|Senin|Rabu|sama ramai|14 terbanyak.
5|Bangun datar yang diagonalnya sama panjang dan keempat sudutnya siku-siku adalah ....|persegi panjang|belah ketupat|layang-layang|trapesium|Persegi panjang.
"""

TOPICS += """
## BIN
# 1|Cerita dan Kebahasaan
@ Tokoh protagonis dan antagonis
min: 12
act: Baca satu cerita rakyat, lalu tentukan tokoh protagonis dan antagonisnya beserta alasannya.
mis: mengira tokoh antagonis selalu jahat dalam penampilan fisik
exp: Dalam cerita ada tokoh protagonis, yaitu tokoh utama yang biasanya berwatak baik dan mendapat simpati pembaca. Tokoh antagonis adalah tokoh yang menentang tokoh utama dan menimbulkan masalah. Tokoh tritagonis adalah penengah atau penolong. Watak tokoh diketahui dari ucapan, perbuatan, dan pendapat tokoh lain.
ex: Bawang Putih protagonis, Bawang Merah antagonis. // Timun Mas protagonis, Buto Ijo antagonis.
pt: Protagonis tokoh utama yang baik ; Antagonis penentang tokoh utama ; Tritagonis penengah
sum: Tokoh cerita memiliki peran yang berbeda-beda.
fig: table Cerita | Tokoh antagonis ;; Bawang Merah Bawang Putih | Bawang Merah ;; Timun Mas | Buto Ijo ;; Malin Kundang | Malin Kundang yang durhaka ;; Kancil dan Buaya | buaya yang ingin memangsa ;; Keong Mas | penyihir jahat ;; Ande-Ande Lumut | Yuyu Kangkang ~ Tokoh antagonis dalam cerita rakyat.
@ Latar tempat, waktu, dan suasana
min: 12
act: Tulis latar tempat, waktu, dan suasana dari cerita yang kamu baca minggu ini.
mis: menyebut tokoh sebagai latar tempat
exp: Latar adalah keterangan tentang tempat, waktu, dan suasana dalam cerita. Latar tempat menunjukkan di mana peristiwa terjadi. Latar waktu menunjukkan kapan terjadi. Latar suasana menunjukkan keadaan perasaan, misalnya sedih, gembira, atau tegang.
ex: Di tepi sungai yang sepi (tempat). // Pada suatu malam yang gelap (waktu).
pt: Latar tempat menjawab di mana ; Latar waktu menjawab kapan ; Latar suasana menunjukkan perasaan
sum: Latar membuat cerita terasa nyata.
fig: table Kutipan | Jenis latar ;; di tepi sungai | latar tempat ;; pada malam hari | latar waktu ;; semua orang menangis | latar suasana sedih ;; di tengah hutan lebat | latar tempat hutan ;; ketika fajar menyingsing | latar waktu pagi ;; sorak-sorai penonton | latar suasana gembira ~ Contoh latar dalam cerita.
@ Kata berimbuhan ber- dan ter-
min: 12
act: Cari sepuluh kata berimbuhan ber- dan ter- di koran anak, lalu tulis artinya.
mis: mengartikan tertidur sama dengan sengaja tidur
exp: Imbuhan ber- dapat berarti mempunyai, memakai, atau melakukan, misalnya bersepeda dan bertopi. Imbuhan ter- dapat berarti tidak sengaja, paling, atau dapat di-, misalnya tertidur, tertinggi, dan terbaca. Arti imbuhan ditentukan oleh kalimatnya.
ex: Adik bersepeda ke taman (mengendarai sepeda). // Gunung itu tertinggi di pulau ini (paling tinggi).
pt: Ber- berarti mempunyai atau melakukan ; Ter- bisa berarti tidak sengaja ; Ter- juga bisa berarti paling
sum: Imbuhan ber- dan ter- memberi arti baru pada kata dasar.
fig: table Kata berimbuhan | Arti ;; bersepeda | mengendarai sepeda ;; bertopi | memakai topi ;; berkebun | melakukan kegiatan di kebun ;; tertidur | tidur tidak sengaja ;; tertinggi | paling tinggi ;; terbaca | dapat dibaca ~ Arti imbuhan ber- dan ter-.
@ Kalimat langsung dan tidak langsung
min: 12
act: Tulis ucapan anggota keluarga dalam bentuk kalimat langsung, lalu ubah menjadi kalimat tidak langsung.
mis: lupa memakai tanda petik pada kalimat langsung
exp: Kalimat langsung menirukan ucapan seseorang secara persis dan ditulis dengan tanda petik. Kalimat tidak langsung melaporkan ucapan orang lain tanpa tanda petik, biasanya memakai kata bahwa, agar, atau supaya. Kata ganti juga berubah, misalnya aku menjadi dia.
ex: Ibu berkata, "Aku pergi ke pasar." // Ibu berkata bahwa dia pergi ke pasar.
pt: Kalimat langsung memakai tanda petik ; Kalimat tidak langsung memakai bahwa ; Kata ganti berubah
sum: Kalimat langsung menirukan, kalimat tidak langsung melaporkan.
fig: table Ciri | Jenis kalimat ;; memakai tanda petik | kalimat langsung ;; memakai kata bahwa | kalimat tidak langsung ;; menirukan ucapan persis | langsung menirukan ;; melaporkan ucapan | tidak langsung melaporkan ;; huruf kapital di awal petikan | ciri petikan langsung ;; kata ganti aku menjadi dia | ciri perubahan tidak langsung ~ Ciri kalimat langsung dan tidak langsung.
@ Menyusun pertanyaan wawancara
min: 12
act: Susun lima pertanyaan wawancara untuk penjual di dekat rumah, lalu lakukan wawancaranya.
mis: membuat pertanyaan yang hanya bisa dijawab ya atau tidak
exp: Pertanyaan wawancara yang baik memakai kata tanya 5W+1H, yaitu apa, siapa, kapan, di mana, mengapa, dan bagaimana. Pertanyaan disusun berurutan, singkat, jelas, dan sopan. Hindari pertanyaan yang hanya bisa dijawab ya atau tidak supaya informasi lebih lengkap.
ex: Sejak kapan Bapak berjualan di sini? // Bagaimana cara Bapak menjaga mutu dagangan?
pt: Gunakan 5W+1H ; Pertanyaan singkat dan sopan ; Hindari pertanyaan ya atau tidak
sum: Pertanyaan yang baik menghasilkan informasi yang lengkap.
fig: table Kata tanya | Informasi yang dicari ;; apa | kejadian atau benda ;; siapa | orang ;; kapan | waktu ;; di mana | tempat ;; mengapa | alasan ;; bagaimana | cara atau proses ~ Kata tanya 5W+1H.
@ Pantun nasihat
min: 12
act: Buat dua pantun nasihat tentang rajin belajar, lalu bacakan di depan keluarga.
mis: menulis sampiran yang tidak berima dengan isi
exp: Pantun nasihat berisi pesan atau petuah. Pantun terdiri atas empat baris dengan sajak a-b-a-b. Baris pertama dan kedua adalah sampiran, baris ketiga dan keempat adalah isi. Setiap baris terdiri atas 8 sampai 12 suku kata.
ex: Pergi ke pasar membeli tomat, / pulangnya mampir membeli jamu. / Kalau kamu ingin selamat, / rajinlah belajar menuntut ilmu.
pt: Berisi nasihat ; Sajak a-b-a-b ; Setiap baris 8 sampai 12 suku kata
sum: Pantun nasihat menyampaikan pesan dengan indah.
fig: table Ciri pantun | Keterangan ;; jumlah baris | empat ;; sajak | a-b-a-b ;; baris 1 dan 2 | sampiran ;; baris 3 dan 4 | isi ;; suku kata per baris | 8 sampai 12 ;; pesan | terdapat pada isi ~ Ciri-ciri pantun.
# 2|Informasi dan Menulis
@ Fiksi dan nonfiksi
min: 12
act: Pilih dua buku di rumah, lalu tentukan mana yang fiksi dan mana yang nonfiksi.
mis: mengira semua buku bergambar adalah fiksi
exp: Teks fiksi adalah teks yang berisi cerita khayalan atau rekaan pengarang, misalnya dongeng, cerpen, dan novel. Teks nonfiksi berisi fakta dan informasi nyata, misalnya ensiklopedia, biografi, dan berita. Teks nonfiksi dapat dibuktikan kebenarannya.
ex: Dongeng Kancil termasuk fiksi. // Buku tentang tata surya termasuk nonfiksi.
pt: Fiksi berisi khayalan ; Nonfiksi berisi fakta ; Nonfiksi dapat dibuktikan
sum: Fiksi untuk hiburan, nonfiksi untuk informasi.
fig: table Bacaan | Jenis ;; dongeng | fiksi khayalan ;; cerpen | fiksi pendek ;; novel | fiksi panjang ;; ensiklopedia | nonfiksi pengetahuan ;; biografi | nonfiksi riwayat hidup ;; berita | nonfiksi peristiwa ~ Jenis bacaan fiksi dan nonfiksi.
@ Peta pikiran
min: 12
act: Buat peta pikiran tentang hobimu dengan gambar dan warna.
mis: menulis kalimat panjang di setiap cabang
exp: Peta pikiran adalah cara mencatat dengan gambar bercabang. Topik utama ditulis di tengah. Gagasan pendukung ditulis pada cabang-cabang di sekelilingnya dengan kata kunci singkat. Peta pikiran membantu memahami dan mengingat isi bacaan.
ex: Topik utama: hewan. Cabang: tempat hidup, makanan, cara berkembang biak. // Setiap cabang memakai kata kunci.
pt: Topik utama di tengah ; Cabang berisi kata kunci ; Membantu mengingat
sum: Peta pikiran membuat catatan lebih mudah diingat.
fig: table Bagian peta pikiran | Isi ;; tengah | topik utama ;; cabang utama | gagasan pokok ;; ranting | rincian ;; kata kunci | kata singkat ;; warna | membedakan cabang ;; gambar | memperkuat ingatan ~ Bagian-bagian peta pikiran.
@ Kata hubung antarkalimat
min: 12
act: Tulis paragraf tentang kegiatan pagimu memakai kata hubung kemudian, selain itu, dan akhirnya.
mis: memakai kata hubung dan di awal kalimat
exp: Kata hubung antarkalimat menghubungkan satu kalimat dengan kalimat berikutnya. Contohnya oleh karena itu, akan tetapi, selain itu, kemudian, dan akhirnya. Kata hubung antarkalimat diletakkan di awal kalimat dan diikuti tanda koma.
ex: Hujan turun deras. Oleh karena itu, kami tidak jadi pergi. // Rina pintar. Selain itu, ia juga rajin.
pt: Menghubungkan antarkalimat ; Diletakkan di awal kalimat ; Diikuti tanda koma
sum: Kata hubung antarkalimat membuat paragraf runtut.
fig: table Kata hubung | Hubungan ;; oleh karena itu | akibat ;; akan tetapi | pertentangan ;; selain itu | tambahan ;; kemudian | urutan waktu ;; akhirnya | penutup ;; misalnya | contoh ~ Kata hubung antarkalimat dan maknanya.
@ Iklan layanan masyarakat
min: 12
act: Buat poster iklan layanan masyarakat tentang hemat air untuk ditempel di rumah.
mis: mengira iklan layanan masyarakat menjual barang
exp: Iklan layanan masyarakat adalah iklan yang mengajak masyarakat melakukan hal baik, bukan menjual barang. Contohnya ajakan hemat energi, menjaga kebersihan, dan mencuci tangan. Iklan ini memakai kalimat ajakan yang singkat, menarik, dan mudah diingat.
ex: Ayo buang sampah pada tempatnya! // Hemat air, hemat kehidupan.
pt: Mengajak berbuat baik ; Tidak menjual barang ; Kalimat singkat dan menarik
sum: Iklan layanan masyarakat mengajak kita peduli.
fig: table Tema iklan | Contoh slogan ;; hemat air | matikan keran setelah dipakai ;; kebersihan | buang sampah pada tempatnya ;; kesehatan | cuci tangan pakai sabun ;; hemat listrik | matikan lampu yang tidak dipakai ;; lalu lintas | pakai helm demi keselamatan ;; lingkungan | tanam pohon untuk masa depan ~ Contoh iklan layanan masyarakat.
@ Menulis cerita fantasi
min: 12
act: Tulis cerita fantasi tentang hewan peliharaanmu yang bisa berbicara.
mis: menulis cerita tanpa konflik sehingga datar
exp: Cerita fantasi adalah cerita rekaan yang berisi hal-hal ajaib atau di luar kenyataan. Cerita fantasi tersusun atas orientasi atau pengenalan, komplikasi atau masalah, resolusi atau penyelesaian, dan koda atau pesan. Tokoh, latar, dan kejadiannya boleh ajaib.
ex: Pensil ajaib yang bisa menggambar benda menjadi nyata. // Anak yang bisa berbicara dengan burung.
pt: Berisi hal ajaib ; Ada orientasi, komplikasi, resolusi ; Imajinasi bebas
sum: Cerita fantasi menyalurkan imajinasi.
fig: table Bagian cerita | Isi ;; orientasi | pengenalan tokoh dan latar ;; komplikasi | munculnya masalah ;; klimaks | puncak masalah ;; resolusi | penyelesaian masalah ;; koda | pesan cerita ;; judul | nama cerita yang menarik ~ Struktur cerita fantasi.
@ Gurindam
min: 12
act: Baca satu bait gurindam, lalu jelaskan nasihatnya dengan kalimatmu sendiri.
mis: mengira gurindam terdiri atas empat baris seperti pantun
exp: Gurindam adalah puisi lama yang terdiri atas dua baris dalam satu bait. Baris pertama berisi syarat atau sebab, baris kedua berisi akibat atau jawaban. Gurindam bersajak a-a dan berisi nasihat. Gurindam yang terkenal adalah Gurindam Dua Belas karya Raja Ali Haji.
ex: Barang siapa rajin belajar, ilmunya pasti makin lebar. // Baris pertama sebab, baris kedua akibat.
pt: Dua baris dalam satu bait ; Baris pertama sebab, kedua akibat ; Sajak a-a
sum: Gurindam berisi nasihat dalam dua baris.
fig: table Jenis puisi lama | Ciri ;; pantun | empat baris sajak a-b-a-b ;; gurindam | dua baris sajak a-a ;; syair | empat baris sajak a-a-a-a ;; karmina | pantun kilat dua baris ;; talibun | lebih dari empat baris ;; seloka | pantun berkait ~ Jenis puisi lama dan cirinya.
"""

BANK += """
## BIN|Tokoh protagonis dan antagonis
Tokoh utama yang berwatak baik disebut tokoh …|protagonis|antagonis|tritagonis|figuran|Protagonis.
Tokoh yang menentang tokoh utama disebut …|antagonis|protagonis|tritagonis|narator|Antagonis.
=|Tokoh penengah atau penolong disebut tokoh …|tritagonis|Tritagonis.
=|Dalam cerita Timun Mas, tokoh protagonisnya adalah …|Timun Mas|Timun Mas.
B|Watak tokoh dapat diketahui dari ucapannya.|Dari ucapan.
S|Tokoh antagonis selalu tokoh utama yang baik.|Antagonis penentang.
Tokoh antagonis dalam cerita Ande-Ande Lumut adalah …|Yuyu Kangkang|Klething Kuning|Ande-Ande Lumut|Mbok Randa|Yuyu Kangkang.
Tokoh protagonis biasanya mendapat … pembaca.|simpati|kebencian|ejekan|amarah|Simpati.
## BIN|Latar tempat, waktu, dan suasana
Latar yang menjawab pertanyaan di mana disebut latar …|tempat|waktu|suasana|tokoh|Tempat.
Pada suatu pagi yang cerah termasuk latar …|waktu|tempat|suasana|alur|Waktu.
=|Latar yang menunjukkan perasaan sedih atau gembira disebut latar …|suasana|Suasana.
=|Kutipan di dalam gua yang gelap menunjukkan latar …|tempat|Tempat.
B|Latar membuat cerita terasa nyata.|Nyata.
S|Nama tokoh termasuk latar tempat.|Tokoh bukan latar.
Semua orang bersorak gembira menunjukkan latar …|suasana|tempat|waktu|tokoh|Suasana.
Kutipan ketika matahari terbenam menunjukkan latar waktu …|sore|pagi|siang|tengah malam|Sore.
## BIN|Kata berimbuhan ber- dan ter-
Arti imbuhan ber- pada kata bertopi adalah …|memakai|paling|tidak sengaja|dapat|Memakai topi.
Arti imbuhan ter- pada kata tertinggi adalah …|paling|memakai|melakukan|mempunyai|Paling tinggi.
=|Arti imbuhan ter- pada kata tertidur adalah tidak …|sengaja|Tidak sengaja.
=|Kata dasar dari bersepeda adalah …|sepeda|Sepeda.
B|Kata berkebun artinya melakukan kegiatan di kebun.|Melakukan.
S|Kata terbaca artinya membaca dengan sengaja.|Artinya dapat dibaca.
Kalimat yang memakai ter- berarti tidak sengaja adalah …|Kakinya terinjak di keramaian.|Gunung itu tertinggi.|Tulisannya terbaca jelas.|Dia termasuk murid rajin.|Tidak sengaja.
Kalimat yang memakai ber- berarti mempunyai adalah …|Kakak beranak dua.|Adik berlari.|Ayah bersepeda.|Ibu berbelanja.|Mempunyai anak.
## BIN|Kalimat langsung dan tidak langsung
Kalimat langsung ditandai dengan …|tanda petik|kata bahwa|tanda kurung|tanda hubung|Tanda petik.
Kalimat tidak langsung sering memakai kata …|bahwa|sangat|wah|hore|Bahwa.
=|Kalimat langsung menirukan ucapan secara …|persis|Persis.
=|Pada kalimat tidak langsung, kata aku berubah menjadi …|dia|Dia.
B|Kalimat Ayah berkata bahwa ia lelah adalah kalimat tidak langsung.|Tidak langsung.
S|Kalimat tidak langsung selalu memakai tanda petik.|Tanpa tanda petik.
Penulisan kalimat langsung yang benar adalah …|Guru berkata, "Kerjakan tugasmu."|Guru berkata, kerjakan tugasmu.|Guru berkata "kerjakan tugasmu"|Guru berkata bahwa "kerjakan tugasmu."|Tanda petik dan kapital.
Ubahan tidak langsung dari Ani berkata, "Aku sakit." adalah …|Ani berkata bahwa dia sakit.|Ani berkata, aku sakit.|Ani berkata bahwa aku sakit.|"Ani sakit," kata aku.|Kata ganti berubah.
## BIN|Menyusun pertanyaan wawancara
Kata tanya 5W+1H terdiri atas …|apa, siapa, kapan, di mana, mengapa, bagaimana|apa, ya, tidak, mungkin, boleh, harus|siapa, berapa, bagaimana saja|kapan dan di mana saja|5W+1H.
Pertanyaan wawancara yang baik bersifat …|singkat, jelas, dan sopan|panjang dan berbelit|kasar|menyindir|Singkat jelas sopan.
=|Kata tanya untuk menanyakan alasan adalah …|mengapa|Mengapa.
=|Kata tanya untuk menanyakan cara adalah …|bagaimana|Bagaimana.
B|Pertanyaan ya atau tidak membuat informasi kurang lengkap.|Kurang lengkap.
S|Pertanyaan wawancara sebaiknya menyinggung perasaan narasumber.|Harus sopan.
Pertanyaan yang tepat untuk mengetahui lama berjualan adalah …|Sejak kapan Bapak berjualan?|Apakah Bapak berjualan?|Bapak berjualan, ya?|Bapak suka berjualan?|Kapan.
Pertanyaan yang tepat untuk mengetahui tempat bahan dibeli adalah …|Di mana Ibu membeli bahan?|Siapa nama Ibu?|Kapan Ibu lahir?|Mengapa Ibu tersenyum?|Di mana.
## BIN|Pantun nasihat
Pantun nasihat berisi …|pesan atau petuah|lelucon saja|teka-teki|berita|Pesan.
Sajak pantun adalah …|a-b-a-b|a-a-a-a|a-a|a-b-b-a|A-b-a-b.
=|Banyak baris dalam satu bait pantun adalah …|4;empat|Empat baris.
=|Bagian isi pantun terdapat pada baris ketiga dan …|keempat|Keempat.
B|Setiap baris pantun terdiri atas 8 sampai 12 suku kata.|Suku kata.
S|Isi pantun terdapat pada baris pertama dan kedua.|Itu sampiran.
Baris kedua pantun termasuk bagian …|sampiran|isi|judul|amanat|Sampiran.
Kalau kamu ingin selamat, / rajinlah belajar menuntut ilmu. Nasihatnya adalah …|rajin belajar|rajin bermain|rajin tidur|rajin jajan|Rajin belajar.
## BIN|Fiksi dan nonfiksi
Teks yang berisi cerita khayalan disebut teks …|fiksi|nonfiksi|laporan|berita|Fiksi.
Contoh teks nonfiksi adalah …|ensiklopedia|dongeng|cerpen|fabel|Ensiklopedia.
=|Teks yang berisi fakta disebut teks …|nonfiksi|Nonfiksi.
=|Buku yang berisi riwayat hidup seseorang disebut …|biografi|Biografi.
B|Teks nonfiksi dapat dibuktikan kebenarannya.|Fakta.
S|Novel termasuk teks nonfiksi.|Novel fiksi.
Contoh teks fiksi adalah …|cerpen|berita|biografi|ensiklopedia|Cerpen.
Buku tentang cara menanam padi termasuk teks …|nonfiksi|fiksi|dongeng|fabel|Informasi nyata.
## BIN|Peta pikiran
Pada peta pikiran, topik utama ditulis di …|tengah|pojok kanan|bawah|belakang kertas|Di tengah.
Cabang peta pikiran berisi …|kata kunci|kalimat panjang|cerita lengkap|daftar nama|Kata kunci.
=|Peta pikiran membantu kita … isi bacaan.|mengingat;memahami|Mengingat.
=|Warna pada peta pikiran dipakai untuk membedakan …|cabang|Cabang.
B|Gambar pada peta pikiran memperkuat ingatan.|Gambar membantu.
S|Peta pikiran harus berisi paragraf panjang.|Kata kunci singkat.
Bagian peta pikiran yang berisi rincian adalah …|ranting|tengah|judul buku|halaman|Ranting.
Peta pikiran termasuk cara …|mencatat|bernyanyi|berolahraga|memasak|Mencatat.
## BIN|Kata hubung antarkalimat
Kata hubung antarkalimat yang menyatakan akibat adalah …|oleh karena itu|akan tetapi|selain itu|misalnya|Akibat.
Kata hubung antarkalimat yang menyatakan pertentangan adalah …|akan tetapi|oleh karena itu|kemudian|selain itu|Pertentangan.
=|Kata hubung antarkalimat diikuti tanda …|koma|Koma.
=|Kata hubung yang menyatakan tambahan adalah selain …|itu|Selain itu.
B|Kata hubung antarkalimat diletakkan di awal kalimat.|Awal kalimat.
S|Kata hubung antarkalimat diletakkan di akhir kalimat.|Di awal.
Rudi rajin belajar. …, ia selalu mendapat nilai bagus. Kata hubung yang tepat …|Oleh karena itu|Akan tetapi|Misalnya|Meskipun|Akibat.
Kata hubung antarkalimat yang menyatakan urutan waktu adalah …|kemudian|akan tetapi|bahkan|namun|Urutan.
## BIN|Iklan layanan masyarakat
Iklan layanan masyarakat bertujuan …|mengajak berbuat baik|menjual barang|mencari keuntungan|mengejek orang|Mengajak.
Contoh tema iklan layanan masyarakat adalah …|hemat air|promo sepatu|diskon pulsa|jual rumah|Hemat air.
=|Kalimat dalam iklan layanan masyarakat biasanya kalimat …|ajakan|Ajakan.
=|Iklan Pakai helm demi keselamatan bertema lalu …|lintas|Lalu lintas.
B|Iklan layanan masyarakat tidak menjual barang.|Tidak menjual.
S|Iklan layanan masyarakat bertujuan mencari keuntungan sebanyak-banyaknya.|Mengajak berbuat baik.
Slogan iklan layanan masyarakat sebaiknya …|singkat dan mudah diingat|panjang sekali|membingungkan|menghina|Singkat.
Contoh slogan hemat listrik adalah …|Matikan lampu yang tidak dipakai!|Beli lampu baru sekarang!|Lampu murah meriah!|Diskon lampu 50%!|Hemat listrik.
## BIN|Menulis cerita fantasi
Cerita fantasi berisi hal-hal yang …|ajaib atau di luar kenyataan|selalu nyata|berupa berita|berupa resep|Ajaib.
Bagian cerita yang memperkenalkan tokoh dan latar disebut …|orientasi|komplikasi|resolusi|koda|Orientasi.
=|Bagian cerita yang berisi munculnya masalah disebut …|komplikasi|Komplikasi.
=|Bagian cerita yang berisi penyelesaian masalah disebut …|resolusi|Resolusi.
B|Koda berisi pesan cerita.|Pesan.
S|Cerita fantasi harus berdasarkan kejadian nyata.|Rekaan.
Contoh ide cerita fantasi adalah …|sepatu yang bisa terbang|laporan banjir|resep kue|jadwal pelajaran|Ajaib.
Puncak masalah dalam cerita disebut …|klimaks|orientasi|koda|judul|Klimaks.
## BIN|Gurindam
Satu bait gurindam terdiri atas … baris.|2|4|3|6|Dua baris.
Sajak gurindam adalah …|a-a|a-b-a-b|a-a-a-a|a-b-b-a|A-a.
=|Baris pertama gurindam berisi syarat atau …|sebab|Sebab.
=|Gurindam Dua Belas dikarang oleh Raja Ali …|Haji|Raja Ali Haji.
B|Gurindam berisi nasihat.|Nasihat.
S|Gurindam terdiri atas empat baris seperti pantun.|Dua baris.
Baris kedua gurindam berisi …|akibat atau jawaban|sampiran|judul|pertanyaan|Akibat.
Puisi lama empat baris bersajak a-a-a-a disebut …|syair|pantun|gurindam|karmina|Syair.
"""

SAS += """
## BIN 1
0|Dalam cerita Bawang Merah Bawang Putih, tokoh protagonisnya adalah ....|Bawang Putih|Bawang Merah|ibu tiri|ikan mas|Bawang Putih.
1|Kalimat di tengah pasar yang ramai menunjukkan latar ....|tempat|waktu|suasana|tokoh|Tempat.
2|Imbuhan ber- pada kata berlari bermakna ....|melakukan|memakai|mempunyai|paling|Melakukan lari.
3|Ubahan langsung dari Kakak berkata bahwa ia lapar adalah ....|Kakak berkata, "Aku lapar."|Kakak berkata, kakak lapar.|"Kakak lapar," kata aku.|Kakak berkata bahwa "lapar."|Kalimat langsung.
4|Pertanyaan wawancara yang menanyakan tempat memakai kata tanya ....|di mana|siapa|kapan|mengapa|Di mana.
5|Bagian sampiran pantun terdapat pada baris ....|pertama dan kedua|ketiga dan keempat|pertama dan ketiga|kedua dan keempat|Sampiran.
## BIN 2
0|Buku ensiklopedia hewan termasuk teks ....|nonfiksi|fiksi|fantasi|dongeng|Nonfiksi.
1|Pada peta pikiran, gagasan pokok ditulis pada ....|cabang utama|tengah|ranting|judul halaman|Cabang utama.
2|Kata hubung antarkalimat yang menyatakan contoh adalah ....|misalnya|oleh karena itu|akan tetapi|akhirnya|Contoh.
3|Tujuan iklan Ayo tanam pohon untuk masa depan adalah mengajak ....|menjaga lingkungan|membeli pohon|menebang pohon|berjualan bibit|Lingkungan.
4|Bagian penutup cerita fantasi yang berisi pesan disebut ....|koda|orientasi|komplikasi|klimaks|Koda.
5|Puisi lama dua baris yang berisi pantun kilat disebut ....|karmina|gurindam|syair|seloka|Karmina.
"""

TOPICS += """
## IPAS
# 1|Tubuh, Ekosistem, dan Sejarah
@ Sistem peredaran darah
min: 12
act: Rasakan denyut nadi di pergelangan tangan sebelum dan sesudah melompat 20 kali, lalu bandingkan.
mis: mengira darah hanya mengalir ke jantung
exp: Sistem peredaran darah mengedarkan oksigen dan sari makanan ke seluruh tubuh. Alat peredaran darah terdiri atas jantung, pembuluh darah, dan darah. Jantung memompa darah. Pembuluh nadi membawa darah dari jantung, pembuluh balik membawa darah kembali ke jantung.
ex: Denyut nadi lebih cepat setelah berolahraga. // Sel darah merah mengangkut oksigen.
pt: Jantung memompa darah ; Pembuluh nadi keluar dari jantung ; Pembuluh balik menuju jantung
sum: Peredaran darah membawa oksigen ke seluruh tubuh.
fig: table Bagian | Fungsi ;; jantung | memompa darah ;; pembuluh nadi | membawa darah dari jantung ;; pembuluh balik | membawa darah ke jantung ;; sel darah merah | mengangkut oksigen ;; sel darah putih | melawan kuman ;; keping darah | membantu pembekuan darah ~ Bagian sistem peredaran darah.
@ Ekosistem
min: 12
act: Amati sebuah kolam atau taman, lalu catat makhluk hidup dan benda tak hidup di sana.
mis: mengira ekosistem hanya terdiri atas makhluk hidup
exp: Ekosistem adalah hubungan timbal balik antara makhluk hidup dan lingkungannya. Ekosistem terdiri atas komponen biotik, yaitu makhluk hidup, dan komponen abiotik, yaitu benda tak hidup seperti air, tanah, udara, dan cahaya. Contoh ekosistem adalah sawah, hutan, kolam, dan laut.
ex: Di sawah ada padi, belalang, dan katak sebagai biotik. // Air dan tanah sawah sebagai abiotik.
pt: Biotik makhluk hidup ; Abiotik benda tak hidup ; Saling berhubungan
sum: Makhluk hidup dan lingkungannya membentuk ekosistem.
fig: table Komponen | Jenis ;; padi | biotik tumbuhan ;; belalang | biotik hewan ;; air | abiotik cair ;; tanah | abiotik padat ;; cahaya matahari | abiotik energi ;; jamur | biotik pengurai ~ Komponen ekosistem sawah.
@ Rantai makanan
min: 12
act: Buat rantai makanan dari hewan dan tumbuhan yang ada di sekitar rumahmu.
mis: menempatkan hewan pemakan daging sebagai produsen
exp: Rantai makanan adalah peristiwa makan dan dimakan dengan urutan tertentu. Produsen adalah tumbuhan hijau yang membuat makanan sendiri. Konsumen adalah makhluk yang memakan makhluk lain. Pengurai menguraikan makhluk mati, misalnya bakteri dan jamur.
ex: Padi → tikus → ular → elang. // Rumput → kambing → harimau.
pt: Produsen tumbuhan hijau ; Konsumen memakan makhluk lain ; Pengurai bakteri dan jamur
sum: Rantai makanan menunjukkan aliran energi.
fig: table Makhluk | Peran ;; padi | produsen ;; tikus | konsumen tingkat satu ;; ular | konsumen tingkat dua ;; elang | konsumen puncak ;; jamur | pengurai ;; bakteri | pengurai mikroskopis ~ Peran makhluk dalam rantai makanan sawah.
@ Hubungan antarmakhluk hidup
min: 12
act: Amati kupu-kupu di bunga atau benalu di pohon, lalu tentukan jenis hubungannya.
mis: mengira semua hubungan makhluk hidup saling menguntungkan
exp: Simbiosis adalah hubungan erat antara dua makhluk hidup. Simbiosis mutualisme saling menguntungkan, misalnya lebah dan bunga. Simbiosis komensalisme menguntungkan satu pihak tanpa merugikan pihak lain, misalnya anggrek di pohon. Simbiosis parasitisme menguntungkan satu pihak dan merugikan pihak lain, misalnya benalu di pohon.
ex: Kerbau dan burung jalak: mutualisme. // Kutu di kepala manusia: parasitisme.
pt: Mutualisme saling untung ; Komensalisme satu untung, lain tidak rugi ; Parasitisme satu untung, lain rugi
sum: Makhluk hidup saling berhubungan dengan cara berbeda.
fig: table Pasangan | Jenis simbiosis ;; lebah dan bunga | mutualisme ;; anggrek dan pohon | komensalisme ;; benalu dan pohon | parasitisme ;; kerbau dan jalak | mutualisme pada hewan ;; ikan remora dan hiu | komensalisme di laut ;; kutu dan manusia | parasitisme pada manusia ~ Contoh simbiosis.
@ Kerajaan Hindu-Buddha di Indonesia
min: 12
act: Cari foto Candi Borobudur atau Prambanan, lalu ceritakan kerajaan yang membangunnya.
mis: mengira Candi Borobudur adalah candi Hindu
exp: Agama Hindu dan Buddha masuk ke Indonesia melalui perdagangan. Kerajaan Hindu-Buddha di Indonesia antara lain Kutai, Tarumanegara, Sriwijaya, Mataram Kuno, dan Majapahit. Peninggalannya berupa candi, prasasti, dan kitab, misalnya Candi Borobudur dan Prasasti Yupa.
ex: Kutai di Kalimantan Timur adalah kerajaan Hindu tertua. // Sriwijaya terkenal sebagai kerajaan maritim.
pt: Masuk melalui perdagangan ; Contoh Kutai, Sriwijaya, Majapahit ; Peninggalan candi dan prasasti
sum: Kerajaan Hindu-Buddha meninggalkan warisan budaya berharga.
fig: table Kerajaan | Peninggalan atau ciri ;; Kutai | Prasasti Yupa ;; Tarumanegara | Prasasti Ciaruteun ;; Sriwijaya | kerajaan maritim di Sumatra ;; Mataram Kuno | Candi Borobudur dan Prambanan ;; Majapahit | Sumpah Palapa Gajah Mada ;; Singasari | Candi Singasari ~ Kerajaan Hindu-Buddha dan peninggalannya.
@ Kerajaan Islam di Indonesia
min: 12
act: Kunjungi atau cari gambar masjid tua di daerahmu, lalu cari tahu sejarahnya.
mis: mengira Islam masuk ke Indonesia melalui perang
exp: Agama Islam masuk ke Indonesia melalui perdagangan, perkawinan, pendidikan, dan kesenian. Kerajaan Islam di Indonesia antara lain Samudera Pasai, Demak, Mataram Islam, Banten, Gowa-Tallo, dan Ternate. Peninggalannya berupa masjid, makam, dan karya sastra.
ex: Samudera Pasai di Aceh adalah kerajaan Islam pertama. // Masjid Agung Demak adalah peninggalan Kerajaan Demak.
pt: Islam masuk secara damai ; Contoh Samudera Pasai dan Demak ; Peninggalan masjid dan makam
sum: Kerajaan Islam berperan menyebarkan agama dan budaya.
fig: table Kerajaan | Wilayah ;; Samudera Pasai | Aceh ;; Demak | Jawa Tengah ;; Banten | Banten ;; Gowa-Tallo | Sulawesi Selatan ;; Ternate | Maluku Utara ;; Mataram Islam | Yogyakarta ~ Kerajaan Islam dan wilayahnya.
# 2|Bumi, Zat, dan Budaya
@ Lapisan bumi
min: 12
act: Buat model lapisan bumi dari plastisin berwarna, lalu potong menjadi dua.
mis: mengira inti bumi paling dekat dengan permukaan
exp: Bumi tersusun atas beberapa lapisan. Lapisan terluar adalah kerak bumi tempat kita tinggal. Di bawahnya ada mantel bumi yang panas dan berisi batuan cair atau magma. Lapisan paling dalam adalah inti bumi yang terdiri atas inti luar dan inti dalam.
ex: Gunung berapi mengeluarkan magma dari dalam bumi. // Inti bumi adalah bagian terpanas.
pt: Kerak bumi paling luar ; Mantel berisi magma ; Inti bumi paling dalam
sum: Bumi berlapis dari kerak sampai inti.
fig: table Lapisan | Ciri ;; kerak benua | membentuk daratan ;; kerak samudra | berada di bawah lautan ;; mantel bumi | berisi magma panas ;; inti luar | logam cair ;; inti dalam | logam padat paling panas ;; atmosfer | selimut udara di luar bumi ~ Lapisan bumi dan cirinya.
@ Sumber daya alam
min: 12
act: Catat barang di rumah dan tentukan sumber daya alam asal bahannya.
mis: mengira minyak bumi dapat diperbarui dengan cepat
exp: Sumber daya alam adalah segala sesuatu dari alam yang dapat dimanfaatkan manusia. Sumber daya alam yang dapat diperbarui, misalnya air, tumbuhan, dan hewan. Sumber daya alam yang tidak dapat diperbarui, misalnya minyak bumi, batu bara, dan logam. Kita harus memakainya dengan hemat.
ex: Kayu dari hutan dapat ditanam kembali. // Minyak bumi butuh jutaan tahun untuk terbentuk.
pt: Ada yang dapat diperbarui ; Ada yang tidak dapat diperbarui ; Gunakan dengan hemat
sum: Sumber daya alam harus dijaga untuk generasi mendatang.
fig: table Sumber daya alam | Jenis ;; air | dapat diperbarui ;; hutan | dapat diperbarui dengan reboisasi ;; ikan | dapat diperbarui jika dibudidayakan ;; minyak bumi | tidak dapat diperbarui ;; batu bara | tidak dapat diperbarui dan menjadi bahan bakar ;; emas | tidak dapat diperbarui dan berupa logam ~ Jenis sumber daya alam.
@ Kalor dan perpindahannya
min: 12
act: Celupkan sendok logam ke air panas, lalu rasakan ujung yang lain setelah beberapa saat.
mis: mengira kalor hanya berpindah melalui benda padat
exp: Kalor adalah energi panas yang berpindah dari benda bersuhu tinggi ke benda bersuhu rendah. Kalor berpindah dengan tiga cara. Konduksi adalah perpindahan melalui benda padat, konveksi melalui aliran zat cair atau gas, dan radiasi tanpa perantara, misalnya panas matahari.
ex: Sendok logam menjadi panas di air panas (konduksi). // Air mendidih bergerak naik turun (konveksi).
pt: Kalor berpindah dari panas ke dingin ; Konduksi melalui benda padat ; Konveksi melalui aliran, radiasi tanpa perantara
sum: Kalor berpindah dengan konduksi, konveksi, dan radiasi.
fig: table Peristiwa | Cara perpindahan kalor ;; sendok panas di dalam teh | konduksi ;; air direbus bergerak | konveksi ;; panas matahari sampai ke bumi | radiasi ;; menyetrika baju | konduksi setrika ;; angin laut | konveksi udara ;; menghangatkan badan di api unggun | radiasi api ~ Contoh perpindahan kalor.
@ Zat tunggal dan campuran
min: 12
act: Campurkan garam dan pasir dalam air, lalu pisahkan dengan menyaring dan menguapkan.
mis: mengira air laut adalah zat tunggal
exp: Zat tunggal tersusun atas satu jenis zat, misalnya emas murni, garam, dan air murni. Campuran tersusun atas dua zat atau lebih, misalnya udara, air laut, dan sirup. Campuran dapat dipisahkan dengan menyaring, menguapkan, menyublim, atau memakai magnet.
ex: Air garam dipisahkan dengan penguapan. // Serbuk besi dipisahkan dari pasir dengan magnet.
pt: Zat tunggal satu jenis zat ; Campuran dua zat atau lebih ; Campuran dapat dipisahkan
sum: Campuran dapat dipisahkan sesuai sifat zatnya.
fig: table Campuran | Cara memisahkan ;; pasir dan air | penyaringan ;; garam dan air | penguapan ;; serbuk besi dan pasir | magnet ;; kapur barus dan pasir | penyubliman ;; minyak dan air | corong pisah ;; beras dan kerikil | ditampi ~ Cara memisahkan campuran.
@ Membaca peta
min: 12
act: Buka peta digital daerahmu, lalu cari sekolah, pasar, dan sungai memakai legenda.
mis: mengira arah atas peta selalu barat
exp: Peta adalah gambaran permukaan bumi pada bidang datar yang diperkecil. Komponen peta antara lain judul, mata angin, skala, legenda, dan garis lintang bujur. Legenda menjelaskan arti simbol. Skala menunjukkan perbandingan jarak di peta dengan jarak sebenarnya.
ex: Simbol garis biru berarti sungai. // Skala 1 : 100.000 berarti 1 cm di peta sama dengan 1 km sebenarnya.
pt: Peta gambaran bumi yang diperkecil ; Legenda menjelaskan simbol ; Skala perbandingan jarak
sum: Komponen peta membantu kita membacanya.
fig: table Komponen peta | Fungsi ;; judul | menunjukkan isi peta ;; mata angin | menunjukkan arah ;; skala | perbandingan jarak ;; legenda | menjelaskan simbol ;; garis lintang dan bujur | menentukan letak ;; inset | peta kecil penunjuk lokasi ~ Komponen peta.
@ Keragaman budaya daerah
min: 12
act: Wawancarai orang tua tentang adat dan makanan khas daerah asal keluarga.
mis: menganggap budaya daerah sendiri paling baik
exp: Indonesia memiliki beragam budaya, seperti bahasa, rumah adat, pakaian adat, tarian, alat musik, makanan, dan upacara adat. Keragaman budaya terjadi karena perbedaan lingkungan alam dan sejarah. Keragaman ini adalah kekayaan yang harus kita lestarikan dan hormati.
ex: Upacara Ngaben di Bali. // Upacara Rambu Solo di Toraja.
pt: Budaya Indonesia beragam ; Dipengaruhi lingkungan dan sejarah ; Dilestarikan dan dihormati
sum: Keragaman budaya adalah kekayaan bangsa.
fig: table Upacara adat | Daerah ;; Ngaben | Bali ;; Rambu Solo | Sulawesi Selatan ;; Kasada | Jawa Timur ;; Tabuik | Sumatera Barat ;; Seren Taun | Jawa Barat ;; Bakar Batu | Papua ~ Upacara adat dari berbagai daerah.
"""

BANK += """
## IPAS|Sistem peredaran darah
Alat yang memompa darah ke seluruh tubuh adalah …|jantung|paru-paru|lambung|ginjal|Jantung.
Sel darah yang mengangkut oksigen adalah sel darah …|merah|putih|keping darah|plasma|Sel darah merah.
=|Sel darah yang melawan kuman adalah sel darah …|putih|Sel darah putih.
=|Pembuluh yang membawa darah kembali ke jantung disebut pembuluh …|balik;vena|Pembuluh balik.
B|Keping darah membantu pembekuan darah saat luka.|Pembekuan.
S|Pembuluh nadi membawa darah menuju jantung.|Keluar dari jantung.
Setelah berlari, denyut nadi menjadi …|lebih cepat|lebih lambat|berhenti|sama saja|Lebih cepat.
Makanan yang membantu pembentukan sel darah merah adalah …|sayuran hijau dan daging merah|permen|minuman bersoda|keripik|Zat besi.
## IPAS|Ekosistem
Hubungan timbal balik makhluk hidup dengan lingkungannya disebut …|ekosistem|habitat|populasi|komunitas|Ekosistem.
Contoh komponen abiotik adalah …|tanah|katak|padi|cacing|Tanah tak hidup.
=|Komponen makhluk hidup dalam ekosistem disebut …|biotik|Biotik.
=|Komponen benda tak hidup dalam ekosistem disebut …|abiotik|Abiotik.
B|Cahaya matahari termasuk komponen abiotik.|Abiotik.
S|Air termasuk komponen biotik.|Air abiotik.
Contoh ekosistem buatan adalah …|sawah|hutan alami|laut|danau alami|Sawah dibuat manusia.
Contoh komponen biotik di kolam adalah …|ikan|batu|air|lumpur|Ikan hidup.
## IPAS|Rantai makanan
Makhluk hidup yang dapat membuat makanan sendiri disebut …|produsen|konsumen|pengurai|predator|Produsen.
Contoh pengurai adalah …|jamur|elang|kambing|padi|Jamur.
=|Pada rantai padi, tikus, ular, elang, produsennya adalah …|padi|Padi.
=|Hewan pemakan tumbuhan dalam rantai makanan disebut konsumen tingkat …|satu;pertama;I|Konsumen I.
B|Bakteri berperan sebagai pengurai.|Pengurai.
S|Elang berperan sebagai produsen.|Elang konsumen.
Jika ular punah, populasi tikus akan …|bertambah|berkurang|tetap|hilang|Tidak ada pemangsa.
Rantai makanan yang benar adalah …|rumput, belalang, katak, ular|ular, katak, belalang, rumput|katak, rumput, ular, belalang|belalang, ular, rumput, katak|Mulai produsen.
## IPAS|Hubungan antarmakhluk hidup
Simbiosis yang saling menguntungkan disebut …|mutualisme|komensalisme|parasitisme|predasi|Mutualisme.
Hubungan benalu dengan pohon inangnya adalah …|parasitisme|mutualisme|komensalisme|netralisme|Benalu merugikan.
=|Hubungan anggrek dengan pohon tempatnya menempel adalah …|komensalisme|Komensalisme.
=|Hubungan lebah dengan bunga adalah …|mutualisme|Saling untung.
B|Kutu rambut dan manusia termasuk parasitisme.|Parasitisme.
S|Benalu dan pohon termasuk mutualisme.|Parasitisme.
Pada hubungan kerbau dan burung jalak, burung jalak mendapat …|makanan berupa kutu|tempat tidur|air minum|perlindungan saja|Kutu di tubuh kerbau.
Simbiosis artinya …|hubungan erat antara dua makhluk hidup|makhluk hidup sendirian|makhluk mati|hubungan dengan benda mati|Hubungan erat.
## IPAS|Kerajaan Hindu-Buddha di Indonesia
Kerajaan Hindu tertua di Indonesia adalah …|Kutai|Majapahit|Sriwijaya|Demak|Kutai.
Candi Borobudur adalah candi agama …|Buddha|Hindu|Islam|Kristen|Borobudur candi Buddha.
=|Peninggalan Kerajaan Kutai adalah Prasasti …|Yupa|Yupa.
=|Patih Majapahit yang terkenal dengan Sumpah Palapa adalah …|Gajah Mada|Gajah Mada.
B|Sriwijaya terkenal sebagai kerajaan maritim.|Maritim.
S|Kerajaan Kutai terletak di Jawa Barat.|Kalimantan Timur.
Agama Hindu dan Buddha masuk ke Indonesia melalui …|perdagangan|perang|penjajahan|olahraga|Perdagangan.
Candi Prambanan adalah candi agama …|Hindu|Buddha|Islam|Khonghucu|Hindu.
## IPAS|Kerajaan Islam di Indonesia
Kerajaan Islam pertama di Indonesia adalah …|Samudera Pasai|Demak|Banten|Mataram Islam|Samudera Pasai.
Masjid Agung Demak adalah peninggalan Kerajaan …|Demak|Banten|Ternate|Gowa|Demak.
=|Kerajaan Gowa-Tallo berada di Sulawesi …|Selatan|Sulawesi Selatan.
=|Kerajaan Ternate berada di Maluku …|Utara|Maluku Utara.
B|Islam masuk ke Indonesia melalui perdagangan.|Damai.
S|Islam masuk ke Indonesia dengan cara perang.|Secara damai.
Samudera Pasai terletak di …|Aceh|Jawa Tengah|Banten|Papua|Aceh.
Contoh peninggalan kerajaan Islam adalah …|masjid dan makam|candi Buddha|prasasti Yupa|pura|Masjid.
## IPAS|Lapisan bumi
Lapisan bumi paling luar adalah …|kerak bumi|mantel bumi|inti luar|inti dalam|Kerak bumi.
Lapisan bumi yang berisi magma adalah …|mantel bumi|kerak bumi|atmosfer|inti dalam|Mantel.
=|Lapisan bumi paling dalam adalah inti …|dalam|Inti dalam.
=|Batuan cair yang panas di dalam bumi disebut …|magma|Magma.
B|Manusia tinggal di lapisan kerak bumi.|Kerak.
S|Inti bumi adalah lapisan paling luar.|Paling dalam.
Magma yang keluar ke permukaan bumi disebut …|lava|kerak|inti|lumpur|Lava.
Bagian bumi yang paling panas adalah …|inti bumi|kerak bumi|lautan|gunung|Inti bumi.
## IPAS|Sumber daya alam
Contoh sumber daya alam yang dapat diperbarui adalah …|air|minyak bumi|batu bara|emas|Air.
Contoh sumber daya alam yang tidak dapat diperbarui adalah …|minyak bumi|hutan|ikan|air|Minyak bumi.
=|Menanam kembali hutan yang gundul disebut …|reboisasi|Reboisasi.
=|Sumber daya alam harus dipakai dengan …|hemat;bijak|Hemat.
B|Batu bara dipakai sebagai bahan bakar.|Bahan bakar.
S|Minyak bumi dapat terbentuk kembali dalam satu tahun.|Jutaan tahun.
Cara menghemat sumber daya alam di rumah adalah …|mematikan keran setelah dipakai|membiarkan lampu menyala|membuang kertas yang masih bisa dipakai|membakar sampah|Hemat air.
Emas termasuk sumber daya alam berupa …|logam|tumbuhan|hewan|air|Logam.
## IPAS|Kalor dan perpindahannya
Kalor berpindah dari benda bersuhu …|tinggi ke rendah|rendah ke tinggi|sama ke sama|tidak berpindah|Tinggi ke rendah.
Perpindahan kalor melalui benda padat disebut …|konduksi|konveksi|radiasi|evaporasi|Konduksi.
=|Perpindahan kalor melalui aliran zat cair atau gas disebut …|konveksi|Konveksi.
=|Perpindahan kalor tanpa perantara disebut …|radiasi|Radiasi.
B|Panas matahari sampai ke bumi secara radiasi.|Radiasi.
S|Gagang panci dibuat dari logam supaya tidak panas.|Dibuat dari kayu atau plastik.
Bahan yang baik menghantarkan panas disebut …|konduktor|isolator|magnet|kertas|Konduktor.
Gagang panci biasanya dibuat dari kayu karena kayu bersifat …|isolator|konduktor|magnet|cair|Isolator.
## IPAS|Zat tunggal dan campuran
Contoh zat tunggal adalah …|emas murni|air laut|udara|sirup|Emas murni.
Contoh campuran adalah …|air laut|emas murni|garam murni|air suling|Air laut.
=|Garam dapat dipisahkan dari air laut dengan cara …|penguapan|Penguapan.
=|Serbuk besi dapat dipisahkan dari pasir dengan …|magnet|Magnet.
B|Pasir dan air dapat dipisahkan dengan penyaringan.|Menyaring.
S|Udara termasuk zat tunggal.|Udara campuran.
Kapur barus dapat dipisahkan dari pasir dengan cara …|penyubliman|penyaringan|magnet|penguapan air|Menyublim.
Pembuatan garam di tepi pantai memakai cara …|penguapan|penyaringan|magnet|penyubliman|Penguapan.
## IPAS|Membaca peta
Komponen peta yang menjelaskan arti simbol adalah …|legenda|skala|judul|inset|Legenda.
Komponen peta yang menunjukkan arah adalah …|mata angin|legenda|skala|judul|Mata angin.
=|Perbandingan jarak di peta dengan jarak sebenarnya disebut …|skala|Skala.
=|Simbol garis biru pada peta biasanya menunjukkan …|sungai|Sungai.
B|Peta adalah gambaran bumi yang diperkecil.|Diperkecil.
S|Legenda peta berisi cerita rakyat daerah.|Legenda menjelaskan simbol.
Skala 1 : 100.000 artinya 1 cm di peta sama dengan … sebenarnya.|1 km|100 m|10 km|1 m|100.000 cm = 1 km.
Peta kecil yang menunjukkan letak daerah dalam wilayah lebih luas disebut …|inset|legenda|skala|judul|Inset.
## IPAS|Keragaman budaya daerah
Upacara Ngaben berasal dari …|Bali|Papua|Aceh|Jawa Barat|Bali.
Upacara Rambu Solo berasal dari …|Toraja, Sulawesi Selatan|Bali|Papua|Sumatera Barat|Toraja.
=|Upacara Tabuik berasal dari Sumatera …|Barat|Sumatera Barat.
=|Upacara Bakar Batu berasal dari …|Papua|Papua.
B|Keragaman budaya dipengaruhi lingkungan alam.|Lingkungan.
S|Kita boleh menganggap budaya daerah lain jelek.|Harus menghormati.
Upacara Kasada dilaksanakan masyarakat Tengger di …|Jawa Timur|Bali|Papua|Aceh|Jawa Timur.
Sikap terhadap keragaman budaya adalah …|melestarikan dan menghormati|mengejek|melarang|mengabaikan|Menghormati.
"""

SAS += """
## IPAS 1
0|Bagian darah yang membantu menutup luka adalah ....|keping darah|sel darah putih|sel darah merah|plasma|Keping darah.
1|Contoh komponen biotik di hutan adalah ....|harimau|batu|udara|tanah|Harimau.
2|Pada rantai makanan rumput, kambing, harimau, konsumen tingkat dua adalah ....|harimau|kambing|rumput|jamur|Harimau.
3|Hubungan ikan remora dan ikan hiu adalah ....|komensalisme|mutualisme|parasitisme|predasi|Komensalisme.
4|Prasasti Ciaruteun adalah peninggalan Kerajaan ....|Tarumanegara|Kutai|Sriwijaya|Majapahit|Tarumanegara.
5|Kerajaan Islam yang berada di Jawa Tengah adalah ....|Demak|Samudera Pasai|Ternate|Gowa-Tallo|Demak.
## IPAS 2
0|Lapisan bumi yang terletak di bawah kerak bumi adalah ....|mantel bumi|inti dalam|atmosfer|samudra|Mantel.
1|Ikan termasuk sumber daya alam yang ....|dapat diperbarui|tidak dapat diperbarui|berupa logam|berupa batuan|Dapat diperbarui.
2|Angin laut termasuk perpindahan kalor secara ....|konveksi|konduksi|radiasi|isolasi|Konveksi.
3|Beras dan kerikil dapat dipisahkan dengan cara ....|ditampi|dimagnet|diuapkan|disublim|Ditampi.
4|Garis lintang dan bujur pada peta berguna untuk ....|menentukan letak|menjelaskan simbol|menunjukkan judul|mengukur suhu|Letak.
5|Upacara Seren Taun berasal dari ....|Jawa Barat|Bali|Papua|Sumatera Barat|Seren Taun.
"""

TOPICS += """
## PPK
# 1|Pancasila, Norma, dan Kewajiban
@ Tokoh perumus Pancasila
min: 12
act: Cari foto tokoh perumus Pancasila, lalu tulis satu jasa setiap tokoh.
mis: mengira Pancasila dirumuskan oleh satu orang saja
exp: Pancasila dirumuskan dalam sidang BPUPKI tahun 1945. Tokoh yang menyampaikan usulan dasar negara adalah Mohammad Yamin pada 29 Mei 1945, Soepomo pada 31 Mei 1945, dan Soekarno pada 1 Juni 1945. Tanggal 1 Juni diperingati sebagai Hari Lahir Pancasila.
ex: Soekarno pertama kali memakai istilah Pancasila. // Panitia Sembilan merumuskan Piagam Jakarta.
pt: Dirumuskan dalam sidang BPUPKI ; Usulan Yamin, Soepomo, Soekarno ; 1 Juni Hari Lahir Pancasila
sum: Pancasila lahir dari musyawarah para pendiri bangsa.
fig: table Tokoh atau peristiwa | Keterangan ;; Mohammad Yamin | berpidato 29 Mei 1945 ;; Soepomo | berpidato 31 Mei 1945 ;; Soekarno | berpidato 1 Juni 1945 ;; Panitia Sembilan | menyusun Piagam Jakarta ;; BPUPKI | badan penyelidik persiapan kemerdekaan ;; 18 Agustus 1945 | Pancasila disahkan PPKI ~ Tokoh dan peristiwa perumusan Pancasila.
@ Penerapan Pancasila di sekolah
min: 12
act: Catat satu contoh penerapan setiap sila yang kamu lakukan di sekolah selama seminggu.
mis: mengira Pancasila hanya dihafalkan saat upacara
exp: Pancasila diterapkan dalam kegiatan sehari-hari di sekolah. Berdoa sebelum belajar sesuai sila pertama. Menolong teman sesuai sila kedua. Bermain dengan teman dari suku berbeda sesuai sila ketiga. Memilih ketua kelas dengan musyawarah sesuai sila keempat. Bergiliran piket sesuai sila kelima.
ex: Menjenguk teman yang sakit adalah penerapan sila kedua. // Musyawarah kelas adalah penerapan sila keempat.
pt: Pancasila diterapkan setiap hari ; Setiap sila punya contoh ; Mulai dari diri sendiri
sum: Pancasila menjadi pedoman perilaku di sekolah.
fig: table Kegiatan di sekolah | Sila ;; berdoa sebelum belajar | sila pertama ;; menjenguk teman sakit | sila kedua ;; berteman dengan semua suku | sila ketiga ;; musyawarah kelas | sila keempat ;; bergiliran piket | sila kelima ;; menghormati teman yang beribadah | sila pertama tentang toleransi ~ Penerapan Pancasila di sekolah.
@ Norma agama dan kesusilaan
min: 12
act: Tulis tiga contoh norma kesusilaan yang berlaku di rumahmu.
mis: tertukar antara norma kesusilaan dan norma hukum
exp: Norma agama adalah aturan yang berasal dari Tuhan, misalnya perintah beribadah dan larangan mencuri. Sanksinya berupa dosa. Norma kesusilaan berasal dari hati nurani manusia, misalnya berkata jujur dan tidak menyakiti orang lain. Sanksinya berupa rasa bersalah atau menyesal.
ex: Beribadah sesuai agama adalah norma agama. // Berkata jujur adalah norma kesusilaan.
pt: Norma agama dari Tuhan ; Norma kesusilaan dari hati nurani ; Sanksinya dosa dan rasa bersalah
sum: Norma agama dan kesusilaan membimbing perilaku baik.
fig: table Contoh perilaku | Jenis norma ;; menjalankan ibadah | norma agama ;; tidak mencuri | norma agama tentang larangan ;; berkata jujur | norma kesusilaan ;; menolong orang kesusahan | norma kesusilaan tentang peduli ;; menghormati orang tua | norma kesusilaan tentang hormat ;; berpuasa sesuai ajaran agama | norma agama tentang ibadah ~ Contoh norma agama dan kesusilaan.
@ Norma kesopanan dan hukum
min: 12
act: Amati perilaku sopan di rumah dan aturan lalu lintas di jalan, lalu bedakan jenis normanya.
mis: mengira melanggar norma kesopanan dihukum penjara
exp: Norma kesopanan berasal dari kebiasaan masyarakat, misalnya memberi salam dan berpakaian sopan. Sanksinya berupa celaan atau dikucilkan. Norma hukum dibuat oleh lembaga resmi negara dan bersifat memaksa, misalnya aturan lalu lintas. Sanksinya tegas berupa denda atau penjara.
ex: Berbicara sopan kepada orang tua adalah norma kesopanan. // Memakai helm saat berkendara adalah norma hukum.
pt: Norma kesopanan dari kebiasaan masyarakat ; Norma hukum dari negara ; Sanksi hukum tegas
sum: Norma kesopanan dan hukum menjaga ketertiban.
fig: table Contoh perilaku | Jenis norma dan sanksi ;; memberi salam | kesopanan dengan sanksi celaan ;; berpakaian sopan | kesopanan dengan sanksi dikucilkan ;; makan tanpa berdecak | kesopanan saat makan ;; memakai helm | hukum dengan sanksi denda ;; membayar pajak | hukum yang wajib ;; tidak mencuri barang orang | hukum pidana dengan sanksi penjara ~ Norma kesopanan dan norma hukum.
@ Tata tertib dan sanksi di sekolah
min: 12
act: Baca tata tertib sekolahmu, lalu diskusikan alasan setiap aturan bersama keluarga.
mis: menganggap sanksi sebagai balas dendam
exp: Tata tertib sekolah adalah aturan yang wajib ditaati warga sekolah. Tata tertib dibuat agar kegiatan belajar tertib, aman, dan nyaman. Pelanggaran tata tertib diberi sanksi yang mendidik, misalnya teguran, membersihkan kelas, atau pemanggilan orang tua.
ex: Terlambat masuk diberi teguran. // Mencoret meja diminta membersihkannya.
pt: Tata tertib wajib ditaati ; Membuat sekolah tertib ; Sanksi bersifat mendidik
sum: Tata tertib dan sanksi membuat sekolah tertib.
fig: table Pelanggaran | Sanksi mendidik ;; terlambat masuk | teguran ;; mencoret meja | membersihkan meja ;; membuang sampah sembarangan | memungut sampah ;; tidak mengerjakan tugas | mengerjakan ulang ;; berkelahi | pemanggilan orang tua ;; tidak memakai seragam lengkap | dicatat dalam buku pelanggaran ~ Contoh pelanggaran dan sanksi di sekolah.
@ Kewajiban sebagai pelajar
min: 12
act: Buat jadwal harian yang memuat kewajibanmu sebagai pelajar, lalu jalankan.
mis: mengutamakan hak tanpa melaksanakan kewajiban
exp: Kewajiban adalah sesuatu yang harus dilakukan dengan penuh tanggung jawab. Kewajiban pelajar antara lain belajar dengan sungguh-sungguh, menaati tata tertib, menghormati guru, menjaga kebersihan sekolah, dan mengerjakan tugas. Kewajiban harus dilaksanakan sebelum menuntut hak.
ex: Mengerjakan PR tepat waktu. // Menjaga kebersihan kelas.
pt: Kewajiban harus dilakukan ; Belajar sungguh-sungguh ; Laksanakan sebelum menuntut hak
sum: Pelajar yang baik melaksanakan kewajibannya.
fig: table Kewajiban | Contoh ;; belajar | mengulang pelajaran di rumah ;; menaati tata tertib | datang tepat waktu ;; menghormati guru | mendengarkan penjelasan ;; menjaga kebersihan | piket kelas ;; mengerjakan tugas | menyerahkan PR tepat waktu ;; menjaga fasilitas | merawat buku perpustakaan ~ Kewajiban pelajar.
# 2|NKRI dan Persatuan
@ Batas wilayah Indonesia
min: 12
act: Lihat peta Indonesia, lalu sebutkan negara tetangga di utara, selatan, timur, dan barat.
mis: mengira Indonesia berbatasan darat dengan Australia
exp: Indonesia berbatasan dengan banyak negara. Di utara berbatasan dengan Malaysia, Singapura, Filipina, dan Laut Cina Selatan. Di selatan berbatasan dengan Australia dan Samudra Hindia. Di timur berbatasan dengan Papua Nugini. Di barat berbatasan dengan Samudra Hindia. Batas darat Indonesia ada dengan Malaysia, Papua Nugini, dan Timor Leste.
ex: Kalimantan berbatasan darat dengan Malaysia. // Pulau Timor berbatasan darat dengan Timor Leste.
pt: Utara: Malaysia, Singapura, Filipina ; Selatan: Australia ; Timur: Papua Nugini
sum: Batas wilayah menunjukkan kedaulatan Indonesia.
fig: table Arah atau pulau | Berbatasan dengan ;; utara | Malaysia, Singapura, Filipina ;; selatan | Australia ;; timur | Papua Nugini ;; barat | Samudra Hindia ;; Kalimantan | darat dengan Malaysia ;; Pulau Timor | darat dengan Timor Leste ~ Batas wilayah Indonesia.
@ Pulau-pulau besar Indonesia
min: 12
act: Gambar peta lima pulau besar Indonesia, lalu tulis satu kota besar di setiap pulau.
mis: mengira Pulau Bali termasuk lima pulau terbesar
exp: Indonesia adalah negara kepulauan dengan lebih dari 17.000 pulau. Lima pulau besar di Indonesia adalah Papua, Kalimantan, Sumatra, Sulawesi, dan Jawa. Pulau-pulau ini dihubungkan oleh laut dan selat, sehingga laut menjadi pemersatu bangsa.
ex: Pulau Jawa paling padat penduduknya. // Pulau Papua adalah pulau terbesar di Indonesia.
pt: Lebih dari 17.000 pulau ; Lima pulau besar ; Laut sebagai pemersatu
sum: Pulau-pulau Indonesia dipersatukan oleh laut.
fig: table Pulau | Contoh kota ;; Sumatra | Medan ;; Jawa | Jakarta ;; Kalimantan | Balikpapan ;; Sulawesi | Makassar ;; Papua | Jayapura ;; Bali | Denpasar ~ Pulau dan kota di Indonesia.
@ Sikap toleransi
min: 12
act: Ceritakan pengalamanmu bermain atau belajar bersama teman yang berbeda agama atau suku.
mis: mengira toleransi berarti harus ikut beribadah agama lain
exp: Toleransi adalah sikap menghargai dan menghormati perbedaan. Toleransi beragama berarti menghormati teman yang beribadah, tidak mengganggu, dan tidak memaksakan keyakinan. Toleransi juga berlaku untuk perbedaan suku, bahasa, dan pendapat. Toleransi membuat hidup rukun.
ex: Menjaga ketenangan saat tetangga beribadah. // Mengucapkan selamat hari raya kepada teman.
pt: Menghargai perbedaan ; Tidak mengganggu dan tidak memaksa ; Membuat hidup rukun
sum: Toleransi adalah kunci kerukunan.
fig: table Situasi | Sikap toleran ;; teman sedang beribadah | tidak mengganggu ;; teman merayakan hari raya | mengucapkan selamat ;; teman berbahasa daerah | tidak menertawakan ;; teman berbeda pendapat | mendengarkan ;; teman berbeda suku | tetap berteman ;; kegiatan sosial lintas agama | ikut bergotong royong ~ Sikap toleransi sehari-hari.
@ Kerja sama di masyarakat
min: 12
act: Ikut kerja bakti di lingkungan rumah dan catat siapa saja yang ikut membantu.
mis: menganggap kerja sama hanya tugas orang dewasa
exp: Kerja sama adalah bekerja bersama untuk mencapai tujuan. Di masyarakat ada kerja bakti, ronda malam, membangun tempat ibadah, dan membantu tetangga yang terkena musibah. Kerja sama membuat pekerjaan berat terasa ringan dan mempererat persaudaraan.
ex: Kerja bakti membersihkan selokan. // Warga bergiliran ronda malam.
pt: Bekerja bersama untuk tujuan ; Contohnya kerja bakti dan ronda ; Pekerjaan berat menjadi ringan
sum: Kerja sama memperkuat persatuan masyarakat.
fig: table Kegiatan | Manfaat ;; kerja bakti | lingkungan bersih ;; ronda malam | lingkungan aman ;; membangun tempat ibadah | ibadah nyaman ;; membantu korban bencana | meringankan beban ;; posyandu | kesehatan anak terjaga ;; arisan warga | mempererat persaudaraan ~ Kerja sama di masyarakat.
@ Pahlawan nasional
min: 12
act: Pilih satu pahlawan nasional, lalu buat poster tentang jasa dan sifat teladannya.
mis: mengira pahlawan hanya berjuang dengan senjata
exp: Pahlawan nasional adalah orang yang berjasa besar bagi bangsa Indonesia. Ada pahlawan yang berjuang dengan senjata, seperti Pangeran Diponegoro dan Cut Nyak Dhien. Ada pula yang berjuang lewat pendidikan dan organisasi, seperti Ki Hajar Dewantara dan R.A. Kartini. Kita meneladani semangat dan pengorbanan mereka.
ex: Ki Hajar Dewantara disebut Bapak Pendidikan. // R.A. Kartini memperjuangkan pendidikan perempuan.
pt: Pahlawan berjasa bagi bangsa ; Berjuang dengan senjata atau pendidikan ; Teladani semangatnya
sum: Jasa pahlawan menjadi teladan bagi kita.
fig: table Pahlawan | Jasa ;; Ki Hajar Dewantara | memajukan pendidikan ;; R.A. Kartini | memperjuangkan pendidikan perempuan ;; Pangeran Diponegoro | memimpin Perang Jawa ;; Cut Nyak Dhien | berjuang di Aceh ;; Bung Tomo | membakar semangat arek-arek Surabaya ;; Pattimura | berjuang di Maluku ~ Pahlawan nasional dan jasanya.
@ Sumpah Pemuda
min: 12
act: Bacakan teks Sumpah Pemuda bersama keluarga, lalu jelaskan maknanya.
mis: mengira Sumpah Pemuda diikrarkan setelah kemerdekaan
exp: Sumpah Pemuda diikrarkan pada 28 Oktober 1928 dalam Kongres Pemuda II di Jakarta. Para pemuda dari berbagai daerah bersumpah mengaku bertumpah darah satu, berbangsa satu, dan menjunjung bahasa persatuan, yaitu Indonesia. Pada kongres itu lagu Indonesia Raya diperdengarkan pertama kali oleh W.R. Supratman.
ex: 28 Oktober diperingati sebagai Hari Sumpah Pemuda. // Bahasa Indonesia menjadi bahasa persatuan.
pt: Diikrarkan 28 Oktober 1928 ; Satu tanah air, satu bangsa, satu bahasa ; Indonesia Raya diperdengarkan pertama kali
sum: Sumpah Pemuda menyatukan pemuda dari berbagai daerah.
fig: table Hal | Keterangan ;; tanggal | 28 Oktober 1928 ;; peristiwa | Kongres Pemuda II ;; tempat | Jakarta ;; ikrar pertama | bertumpah darah satu ;; ikrar ketiga | bahasa persatuan Indonesia ;; lagu yang diperdengarkan | Indonesia Raya ~ Peristiwa Sumpah Pemuda.
"""

BANK += """
## PPK|Tokoh perumus Pancasila
Pancasila dirumuskan dalam sidang …|BPUPKI|PBB|ASEAN|DPR|BPUPKI.
Hari Lahir Pancasila diperingati setiap tanggal …|1 Juni|17 Agustus|28 Oktober|10 November|1 Juni.
=|Tokoh yang berpidato pada 29 Mei 1945 adalah Mohammad …|Yamin|Mohammad Yamin.
=|Panitia Sembilan menyusun Piagam …|Jakarta|Piagam Jakarta.
B|Soekarno berpidato tentang dasar negara pada 1 Juni 1945.|1 Juni.
S|Pancasila dirumuskan oleh satu orang saja.|Banyak tokoh.
Pancasila disahkan sebagai dasar negara pada tanggal …|18 Agustus 1945|17 Agustus 1945|1 Juni 1945|29 Mei 1945|Disahkan PPKI.
Tokoh yang berpidato pada 31 Mei 1945 adalah …|Soepomo|Soekarno|Moh. Hatta|Ki Hajar Dewantara|Soepomo.
## PPK|Penerapan Pancasila di sekolah
Berdoa sebelum belajar merupakan penerapan sila …|pertama|kedua|ketiga|kelima|Sila pertama.
Musyawarah memilih ketua kelas merupakan penerapan sila …|keempat|pertama|kedua|kelima|Sila keempat.
=|Bergiliran piket kelas merupakan penerapan sila …|kelima;ke-5|Keadilan.
=|Berteman dengan teman dari berbagai suku merupakan penerapan sila …|ketiga;ke-3|Persatuan.
B|Menjenguk teman yang sakit merupakan penerapan sila kedua.|Kemanusiaan.
S|Pancasila cukup dihafalkan tanpa diamalkan.|Harus diamalkan.
Meminjamkan alat tulis kepada teman merupakan penerapan sila …|kedua|keempat|ketiga|pertama|Kemanusiaan.
Menghargai hasil keputusan rapat kelas merupakan penerapan sila …|keempat|pertama|kedua|ketiga|Musyawarah.
## PPK|Norma agama dan kesusilaan
Norma yang berasal dari Tuhan disebut norma …|agama|kesusilaan|kesopanan|hukum|Norma agama.
Norma yang berasal dari hati nurani disebut norma …|kesusilaan|agama|hukum|kesopanan|Kesusilaan.
=|Sanksi melanggar norma agama adalah …|dosa|Dosa.
=|Sanksi melanggar norma kesusilaan adalah rasa …|bersalah;menyesal|Rasa bersalah.
B|Berkata jujur termasuk norma kesusilaan.|Kesusilaan.
S|Sanksi norma agama berupa denda dari polisi.|Sanksinya dosa.
Contoh norma agama adalah …|menjalankan ibadah|memakai helm|memberi salam|membayar pajak|Ibadah.
Contoh norma kesusilaan adalah …|menolong orang yang kesusahan|membayar pajak|memakai seragam|mengurus SIM|Kesusilaan.
## PPK|Norma kesopanan dan hukum
Norma yang berasal dari kebiasaan masyarakat disebut norma …|kesopanan|hukum|agama|kesusilaan|Kesopanan.
Norma yang dibuat oleh negara dan bersifat memaksa disebut norma …|hukum|kesopanan|kesusilaan|agama|Hukum.
=|Sanksi melanggar norma hukum dapat berupa denda atau …|penjara|Penjara.
=|Sanksi melanggar norma kesopanan dapat berupa …|celaan;dikucilkan|Celaan.
B|Memakai helm saat berkendara termasuk norma hukum.|Hukum lalu lintas.
S|Melanggar norma kesopanan pasti dihukum penjara.|Sanksinya celaan.
Contoh norma kesopanan adalah …|memberi salam kepada orang tua|membayar pajak|memakai sabuk pengaman|mematuhi lampu merah|Kesopanan.
Norma yang sanksinya paling tegas adalah norma …|hukum|kesopanan|kesusilaan|kebiasaan|Hukum.
## PPK|Tata tertib dan sanksi di sekolah
Tata tertib sekolah dibuat agar sekolah …|tertib, aman, dan nyaman|ramai dan kacau|kotor|sepi|Tertib.
Sanksi di sekolah sebaiknya bersifat …|mendidik|menyakiti|mempermalukan|menakutkan|Mendidik.
=|Siswa yang mencoret meja diminta … meja itu.|membersihkan|Membersihkan.
=|Tata tertib wajib ditaati oleh seluruh warga …|sekolah|Warga sekolah.
B|Sanksi membantu siswa memperbaiki perilaku.|Mendidik.
S|Tata tertib hanya berlaku saat ada guru.|Setiap saat.
Contoh pelanggaran tata tertib adalah …|membuang sampah sembarangan|datang tepat waktu|memakai seragam lengkap|mengerjakan PR|Pelanggaran.
Sikap yang benar saat mendapat sanksi adalah …|menerima dan memperbaiki diri|marah|membalas|mengulanginya|Memperbaiki diri.
## PPK|Kewajiban sebagai pelajar
Kewajiban utama pelajar adalah …|belajar dengan sungguh-sungguh|bermain sepanjang hari|menonton televisi|tidur siang|Belajar.
Kewajiban dilaksanakan dengan penuh …|tanggung jawab|keterpaksaan|kemarahan|kemalasan|Tanggung jawab.
=|Sesuatu yang harus dilakukan disebut …|kewajiban|Kewajiban.
=|Kewajiban harus dilaksanakan sebelum menuntut …|hak|Hak.
B|Menjaga kebersihan kelas adalah kewajiban pelajar.|Kewajiban.
S|Pelajar boleh menuntut hak tanpa melaksanakan kewajiban.|Kewajiban dulu.
Contoh kewajiban pelajar di perpustakaan adalah …|merawat buku|mencoret buku|menyobek halaman|membawa pulang tanpa izin|Merawat.
Mendengarkan penjelasan guru termasuk kewajiban …|menghormati guru|piket|berolahraga|bermain|Menghormati guru.
## PPK|Batas wilayah Indonesia
Negara yang berbatasan darat dengan Indonesia di Pulau Kalimantan adalah …|Malaysia|Australia|Filipina|Singapura|Malaysia.
Negara yang berbatasan dengan Indonesia di sebelah selatan adalah …|Australia|Filipina|Malaysia|Thailand|Australia.
=|Negara yang berbatasan darat dengan Indonesia di Pulau Papua adalah Papua …|Nugini|Papua Nugini.
=|Negara yang berbatasan darat dengan Indonesia di Pulau Timor adalah Timor …|Leste|Timor Leste.
B|Di sebelah barat Indonesia terdapat Samudra Hindia.|Samudra Hindia.
S|Indonesia berbatasan darat dengan Australia.|Berbatasan laut.
Negara tetangga di sebelah utara Indonesia adalah …|Filipina|Australia|Papua Nugini|Timor Leste|Filipina.
Batas wilayah penting untuk menjaga …|kedaulatan negara|harga barang|cuaca|nilai ujian|Kedaulatan.
## PPK|Pulau-pulau besar Indonesia
Pulau terbesar di Indonesia adalah …|Papua|Jawa|Bali|Sumatra|Papua.
Indonesia memiliki lebih dari … pulau.|17.000|1.700|170|170.000|Lebih dari 17.000.
=|Kota Makassar terletak di Pulau …|Sulawesi|Sulawesi.
=|Kota Medan terletak di Pulau …|Sumatra;Sumatera|Sumatra.
B|Pulau Jawa adalah pulau terpadat penduduknya.|Terpadat.
S|Bali termasuk lima pulau terbesar di Indonesia.|Bali pulau kecil.
Kota Jayapura terletak di Pulau …|Papua|Kalimantan|Sulawesi|Jawa|Papua.
Penghubung antarpulau di Indonesia adalah …|laut dan selat|gunung|gurun|hutan|Laut.
## PPK|Sikap toleransi
Toleransi adalah sikap …|menghargai perbedaan|memaksakan pendapat|mengejek teman|menjauhi tetangga|Menghargai perbedaan.
Contoh sikap toleransi beragama adalah …|tidak mengganggu teman yang beribadah|mengejek ibadah teman|memaksa teman ikut agama kita|membuat keributan|Tidak mengganggu.
=|Toleransi membuat kehidupan menjadi …|rukun;damai|Rukun.
=|Saat teman merayakan hari raya, kita dapat mengucapkan …|selamat|Mengucapkan selamat.
B|Toleransi juga berlaku untuk perbedaan pendapat.|Perbedaan pendapat.
S|Toleransi berarti harus ikut beribadah agama lain.|Menghormati, tidak ikut.
Teman berbicara dengan bahasa daerahnya. Sikap toleran kita adalah …|menghargainya|menertawakannya|menegurnya keras|menjauhinya|Menghargai.
Lawan dari sikap toleransi adalah sikap …|egois dan memaksakan kehendak|ramah|peduli|sopan|Egois.
## PPK|Kerja sama di masyarakat
Contoh kerja sama di masyarakat adalah …|kerja bakti|bermain gim sendiri|menonton televisi|tidur siang|Kerja bakti.
Manfaat ronda malam adalah lingkungan menjadi …|aman|kotor|sepi|ramai|Aman.
=|Kerja sama membuat pekerjaan berat menjadi …|ringan|Ringan.
=|Kegiatan kesehatan balita di lingkungan disebut …|posyandu|Posyandu.
B|Membantu korban bencana termasuk kerja sama.|Kerja sama sosial.
S|Kerja sama hanya tugas orang dewasa.|Anak juga bisa ikut.
Peran anak dalam kerja bakti adalah …|membantu menyapu dan mengumpulkan sampah|bermain di jalan|menonton saja|mengganggu warga|Membantu.
Kerja sama di masyarakat mempererat …|persaudaraan|permusuhan|persaingan|perselisihan|Persaudaraan.
## PPK|Pahlawan nasional
Tokoh yang disebut Bapak Pendidikan Nasional adalah …|Ki Hajar Dewantara|Bung Tomo|Pattimura|Diponegoro|Ki Hajar Dewantara.
Pahlawan perempuan dari Aceh adalah …|Cut Nyak Dhien|R.A. Kartini|Dewi Sartika|Martha Christina Tiahahu|Cut Nyak Dhien.
=|Pangeran Diponegoro memimpin Perang …|Jawa|Perang Jawa.
=|Pahlawan yang memperjuangkan pendidikan perempuan adalah R.A. …|Kartini|Kartini.
B|Pattimura berjuang di Maluku.|Maluku.
S|Pahlawan hanya berjuang dengan senjata.|Ada yang lewat pendidikan.
Bung Tomo membakar semangat rakyat dalam pertempuran di …|Surabaya|Bandung|Medan|Makassar|Surabaya 10 November.
Cara meneladani pahlawan sebagai pelajar adalah …|belajar dengan rajin|bermalas-malasan|membolos|bertengkar|Rajin belajar.
## PPK|Sumpah Pemuda
Sumpah Pemuda diikrarkan pada tanggal …|28 Oktober 1928|17 Agustus 1945|1 Juni 1945|20 Mei 1908|28 Oktober 1928.
Sumpah Pemuda diikrarkan dalam …|Kongres Pemuda II|sidang BPUPKI|sidang PPKI|Konferensi Asia Afrika|Kongres Pemuda II.
=|Bahasa persatuan menurut Sumpah Pemuda adalah bahasa …|Indonesia|Bahasa Indonesia.
=|Lagu yang pertama kali diperdengarkan dalam Kongres Pemuda II adalah Indonesia …|Raya|Indonesia Raya.
B|Sumpah Pemuda menyatukan pemuda dari berbagai daerah.|Persatuan.
S|Sumpah Pemuda diikrarkan setelah proklamasi kemerdekaan.|Sebelum, tahun 1928.
Isi Sumpah Pemuda yang kedua adalah …|berbangsa satu, bangsa Indonesia|berbahasa satu|bertumpah darah satu|bersatu dalam olahraga|Ikrar kedua.
Sumpah Pemuda diikrarkan di kota …|Jakarta|Bandung|Yogyakarta|Surabaya|Jakarta.
"""

SAS += """
## PPK 1
0|Piagam Jakarta disusun oleh ....|Panitia Sembilan|BPUPKI seluruhnya|PPKI|DPR|Panitia Sembilan.
1|Menghormati teman yang sedang beribadah di sekolah merupakan penerapan sila ....|pertama|ketiga|keempat|kelima|Sila pertama.
2|Larangan mencuri termasuk norma agama dengan sanksi ....|dosa|denda|teguran guru|celaan tetangga|Dosa.
3|Makan tanpa berdecak termasuk norma ....|kesopanan|hukum|agama|kesusilaan|Kesopanan.
4|Sanksi yang tepat untuk siswa yang membuang sampah sembarangan adalah ....|memungut sampah|dipukul|dikurung|tidak boleh pulang|Mendidik.
5|Menyerahkan PR tepat waktu merupakan kewajiban pelajar dalam hal ....|mengerjakan tugas|menjaga kebersihan|berolahraga|beribadah|Tugas.
## PPK 2
0|Negara yang berbatasan dengan Indonesia di sebelah timur adalah ....|Papua Nugini|Malaysia|Singapura|Filipina|Papua Nugini.
1|Kota Balikpapan terletak di Pulau ....|Kalimantan|Jawa|Sulawesi|Papua|Kalimantan.
2|Ikut bergotong royong dalam kegiatan sosial lintas agama merupakan sikap ....|toleransi|egois|diskriminatif|acuh|Toleransi.
3|Manfaat arisan warga adalah ....|mempererat persaudaraan|membuat lingkungan kotor|menimbulkan pertengkaran|menambah sampah|Persaudaraan.
4|Pahlawan yang berjuang di Maluku adalah ....|Pattimura|Cut Nyak Dhien|Diponegoro|Bung Tomo|Pattimura.
5|Isi pertama Sumpah Pemuda adalah ....|bertumpah darah satu, tanah air Indonesia|berbahasa satu|berbangsa satu|bersatu kita teguh|Ikrar pertama.
"""

TOPICS += """
## BIG
# 1|Me and My Activities
@ What are you doing?
min: 12
act: Ask your family members What are you doing? and write their answers in English.
mis: menulis I am cook tanpa akhiran -ing
exp: Present continuous dipakai untuk kegiatan yang sedang dilakukan sekarang. Rumusnya subject + am/is/are + kata kerja-ing. I am reading. She is cooking. They are playing. Pertanyaannya What are you doing?
ex: What are you doing? I am drawing. // My mother is cooking in the kitchen.
pt: Dipakai untuk kegiatan sekarang ; am/is/are + kata kerja-ing ; Tanyakan What are you doing?
sum: Present continuous menceritakan kegiatan yang sedang berlangsung.
fig: table Subject | Example ;; I | I am reading ;; She | She is cooking ;; He | He is swimming ;; They | They are playing ;; We | We are studying ;; It | It is sleeping ~ Present continuous with different subjects.
@ Can and can't
min: 12
act: Write five things you can do and three things you can't do yet.
mis: menulis I can swims dengan akhiran -s
exp: Can dipakai untuk menyatakan kemampuan. Can't atau cannot dipakai untuk menyatakan ketidakmampuan. Setelah can selalu memakai kata kerja dasar tanpa -s atau -ing. Pertanyaannya Can you ...? dan jawabannya Yes, I can atau No, I can't.
ex: I can ride a bicycle. // Can you swim? No, I can't.
pt: Can untuk kemampuan ; Can't untuk ketidakmampuan ; Setelah can memakai kata kerja dasar
sum: Can dan can't menyatakan bisa dan tidak bisa.
fig: table Animal | Ability ;; fish | can swim ;; bird | can fly ;; kangaroo | can jump high ;; cheetah | can run fast ;; snake | can't walk ;; penguin | can't fly ~ What animals can and can't do.
@ How much and how many
min: 12
act: Look in your kitchen and ask How many eggs? and How much rice? with your family.
mis: memakai how many untuk benda yang tidak dapat dihitung
exp: How many dipakai untuk benda yang dapat dihitung, misalnya apples, eggs, dan books. How much dipakai untuk benda yang tidak dapat dihitung, misalnya water, rice, sugar, dan milk. How much juga dipakai untuk menanyakan harga.
ex: How many apples are there? There are five apples. // How much milk do you need?
pt: How many untuk benda terhitung ; How much untuk benda tak terhitung ; How much untuk harga
sum: Pilih how many atau how much sesuai jenis benda.
fig: table Noun | Question word ;; apples | how many ;; water | how much ;; eggs | how many eggs ;; sugar | how much sugar ;; books | how many books ;; milk | how much milk ~ Countable and uncountable nouns.
@ Ordinal numbers
min: 12
act: Line up your family by height and say who is first, second, and third in English.
mis: menulis second sebagai twoth
exp: Ordinal numbers adalah bilangan tingkat atau urutan. Contohnya first (pertama), second (kedua), third (ketiga), fourth (keempat), dan fifth (kelima). Sebagian besar ordinal number berakhiran -th, misalnya sixth dan tenth. Singkatannya 1st, 2nd, 3rd, 4th.
ex: I am the first child in my family. // My classroom is on the second floor.
pt: First, second, third tidak beraturan ; Lainnya berakhiran -th ; Singkatan 1st, 2nd, 3rd
sum: Ordinal numbers menunjukkan urutan.
fig: table Number | Ordinal ;; 1 | first ;; 2 | second ;; 3 | third ;; 4 | fourth ;; 5 | fifth ;; 10 | tenth ~ Ordinal numbers.
@ Dates and birthdays
min: 12
act: Write the birthdays of your family members in English, for example March 5th.
mis: membaca tanggal 3 sebagai three, bukan third
exp: Dalam bahasa Inggris, tanggal dibaca dengan ordinal number. Contohnya 17 Agustus dibaca August seventeenth atau the seventeenth of August. Untuk menanyakan ulang tahun, gunakan When is your birthday? Jawabannya My birthday is on May 5th.
ex: When is your birthday? It is on June 2nd. // Independence Day is on August 17th.
pt: Tanggal dibaca dengan ordinal number ; Gunakan on sebelum tanggal ; Tanyakan When is your birthday?
sum: Membaca tanggal memakai bilangan urutan.
fig: table Date | Read as ;; 1 January | January first ;; 2 May | May second ;; 3 March | March third ;; 17 August | August seventeenth ;; 21 April | April twenty-first ;; 25 December | December twenty-fifth ~ How to read dates.
@ Musical instruments
min: 12
act: Listen to a song and guess which musical instruments are played, then say them in English.
mis: menyebut drum sebagai flute
exp: Musical instruments artinya alat musik. Guitar adalah gitar, piano adalah piano, drum adalah drum, violin adalah biola, flute adalah seruling, dan trumpet adalah terompet. Kita bisa berkata I can play the guitar.
ex: I can play the piano. // My brother plays the drum.
pt: Violin artinya biola ; Flute artinya seruling ; Gunakan play the + alat musik
sum: Musical instruments adalah nama alat musik dalam bahasa Inggris.
fig: icons 🎸 guitar ; 🎹 piano ; 🥁 drum ; 🎻 violin ; 🪈 flute ; 🎺 trumpet ~ Musical instruments.
# 2|My School and Friends
@ Sports
min: 12
act: Ask three friends What sport do you like? and write their answers.
mis: menulis I like play football tanpa -ing
exp: Sports artinya olahraga. Football adalah sepak bola, badminton adalah bulu tangkis, basketball adalah bola basket, swimming adalah renang, volleyball adalah bola voli, dan cycling adalah bersepeda. Kita bisa berkata I like playing badminton.
ex: What sport do you like? I like swimming. // We play football every Sunday.
pt: Badminton artinya bulu tangkis ; Swimming artinya renang ; Gunakan like + kata kerja-ing
sum: Sports adalah nama olahraga dalam bahasa Inggris.
fig: icons ⚽ football ; 🏸 badminton ; 🏀 basketball ; 🏊 swimming ; 🏐 volleyball ; 🚴 cycling ~ Sports in English.
@ Describing people
min: 12
act: Describe one family member in English: tall or short, and kind or funny.
mis: menulis She is tall girl tanpa a
exp: Untuk menggambarkan orang, kita memakai adjective atau kata sifat. Untuk fisik, ada tall (tinggi), short (pendek), thin (kurus), dan curly hair (rambut keriting). Untuk sifat, ada kind (baik hati), funny (lucu), smart (pintar), dan friendly (ramah).
ex: My father is tall and kind. // She has long curly hair.
pt: Tall dan short untuk tinggi badan ; Kind dan friendly untuk sifat ; Gunakan is atau has
sum: Adjective dipakai untuk menggambarkan orang.
fig: table Adjective | Artinya ;; tall | tinggi ;; short | pendek ;; kind | baik hati ;; funny | lucu ;; smart | pintar ;; friendly | ramah ~ Adjectives to describe people.
@ Things in the kitchen
min: 12
act: Label things in your kitchen with English words on small paper.
mis: menyebut spoon sebagai garpu
exp: Things in the kitchen adalah benda di dapur. Plate adalah piring, spoon adalah sendok, fork adalah garpu, glass adalah gelas, knife adalah pisau, dan stove adalah kompor. Kita bisa bertanya Where is the spoon? dan menjawab It is on the table.
ex: Please give me a plate. // The knife is sharp. Be careful!
pt: Spoon artinya sendok ; Fork artinya garpu ; Stove artinya kompor
sum: Kita mengenal nama benda dapur dalam bahasa Inggris.
fig: icons 🍽️ plate ; 🥄 spoon ; 🍴 fork ; 🥛 glass ; 🔪 knife ; 🍳 frying pan ~ Things in the kitchen.
@ School subjects
min: 12
act: Write your school timetable in English for one week.
mis: menulis Science untuk pelajaran Matematika
exp: School subjects adalah mata pelajaran. Math adalah matematika, Science adalah IPA, English adalah bahasa Inggris, Art adalah seni, Music adalah musik, dan Physical Education adalah olahraga. Kita bertanya What is your favorite subject? dan menjawab My favorite subject is Math.
ex: We have English on Monday. // My favorite subject is Art.
pt: Math artinya matematika ; Science artinya IPA ; Tanyakan What is your favorite subject?
sum: School subjects adalah nama mata pelajaran dalam bahasa Inggris.
fig: table Subject | Activity ;; Math | counting numbers ;; Science | doing experiments ;; English | learning new words ;; Art | drawing pictures ;; Music | singing songs ;; Physical Education | playing sports ~ School subjects and activities.
@ Asking permission
min: 12
act: Practice asking permission in English before borrowing something at home.
mis: berkata Give me your pen! tanpa meminta izin
exp: Untuk meminta izin dengan sopan, gunakan May I ...? atau Can I ...?. Contohnya May I go to the toilet? Jawaban jika mengizinkan adalah Yes, you may atau Sure. Jawaban jika tidak mengizinkan adalah Sorry, you can't.
ex: May I borrow your pencil? Sure, here you are. // Can I open the window? Yes, you can.
pt: Gunakan May I atau Can I ; Jawaban izin: Yes, you may ; Jawaban tidak: Sorry, you can't
sum: Meminta izin dengan sopan memakai May I.
fig: table Situation | Asking permission ;; need to go out | May I go to the toilet? ;; need a pencil | May I borrow your pencil? ;; room is hot | Can I open the window? ;; want to come in | May I come in? ;; want to ask | May I ask a question? ;; want to sit | Can I sit here? ~ Asking permission politely.
@ Invitations
min: 12
act: Write an invitation card in English for your birthday party.
mis: menolak undangan tanpa memberi alasan
exp: Untuk mengundang, gunakan Would you like to ...? atau Let's .... Untuk menerima undangan, katakan Yes, I'd love to. Untuk menolak dengan sopan, katakan I'm sorry, I can't dan berikan alasan.
ex: Would you like to come to my party? Yes, I'd love to. // Let's play football. Sorry, I can't. I have to study.
pt: Mengundang: Would you like to ...? ; Menerima: Yes, I'd love to ; Menolak: Sorry, I can't + alasan
sum: Undangan diterima atau ditolak dengan sopan.
fig: table Expression | Function ;; Would you like to come? | inviting ;; Let's go swimming. | inviting a friend ;; Yes, I'd love to. | accepting ;; Sure, that sounds fun. | accepting happily ;; Sorry, I can't. | refusing ;; Maybe next time. | refusing politely ~ Expressions for invitations.
"""

BANK += """
## BIG|What are you doing?
I … reading a book now.|am|is|are|be|I am.
She … cooking in the kitchen.|is|am|are|be|She is.
=|They are … football now. (play)|playing|Play + ing.
=|We … studying English. (am/is/are)|are|We are.
B|He is swimming adalah kalimat present continuous.|Is + swimming.
S|I am cook in the kitchen adalah kalimat yang benar.|I am cooking.
Pertanyaan untuk menanyakan kegiatan sekarang adalah …|What are you doing?|What is your name?|How old are you?|Where do you live?|What are you doing.
Look! The baby … .|is sleeping|sleeps|are sleeping|sleeping is|Is sleeping.
## BIG|Can and can't
Can artinya …|bisa|tidak bisa|harus|sedang|Can = bisa.
Kalimat yang benar adalah …|I can swim.|I can swims.|I can swimming.|I cans swim.|Kata kerja dasar.
=|Lawan dari can adalah …|can't;cannot|Can't.
=|Can you ride a bike? Jawaban jika bisa: Yes, I …|can|Yes, I can.
B|A bird can fly.|Burung bisa terbang.
S|A fish can walk.|Ikan tidak bisa berjalan.
Penguins … fly.|can't|can|is|are|Penguin tidak bisa terbang.
Can she sing? Jawaban jika tidak bisa adalah …|No, she can't.|No, she can.|Yes, she can't.|No, she isn't.|No, she can't.
## BIG|How much and how many
… apples are there?|How many|How much|How old|How long|Apples terhitung.
… water do you drink?|How much|How many|How old|How far|Water tak terhitung.
=|Untuk menanyakan harga, kita memakai How …|much|How much.
=|… many books do you have? Kata yang tepat adalah …|How|How many.
B|Rice adalah benda yang tidak dapat dihitung.|Uncountable.
S|How many dipakai untuk menanyakan banyaknya susu.|How much milk.
How … sugar do we need?|much|many|old|far|Sugar tak terhitung.
How many eggs are there? There are … eggs.|six|much|many|any|Jawaban angka.
## BIG|Ordinal numbers
First artinya …|pertama|kedua|ketiga|satu|First = pertama.
Ordinal number dari 3 adalah …|third|three|threeth|thirdth|Third.
=|Ordinal number dari 2 adalah …|second|Second.
=|Ordinal number dari 5 adalah …|fifth|Fifth.
B|Tenth artinya kesepuluh.|Tenth.
S|Ordinal number dari 1 adalah oneth.|First.
Singkatan dari second adalah …|2nd|2st|2rd|2th|2nd.
My classroom is on the … floor (lantai ketiga).|third|three|thirty|threeth|Third.
## BIG|Dates and birthdays
17 Agustus dibaca …|August seventeenth|August seventeen|seventeen August|August one seven|Ordinal.
When is your birthday? Jawaban yang tepat adalah …|It is on May 5th.|I am ten years old.|It is sunny.|I like cake.|Tanggal.
=|Kata depan sebelum tanggal adalah …|on|On.
=|1 January dibaca January …|first|First.
B|Tanggal dalam bahasa Inggris dibaca dengan ordinal number.|Ordinal.
S|25 December dibaca December twenty-five.|December twenty-fifth.
Independence Day of Indonesia is on …|August 17th|May 2nd|April 21st|December 25th|17 Agustus.
Kartini Day is on …|April 21st|August 17th|May 2nd|October 28th|21 April.
## BIG|Musical instruments
Violin artinya …|biola|gitar|seruling|terompet|Violin = biola.
Bahasa Inggris dari seruling adalah …|flute|drum|piano|guitar|Flute.
=|Bahasa Inggris dari gitar adalah …|guitar|Guitar.
=|Bahasa Inggris dari terompet adalah …|trumpet|Trumpet.
B|Drum dimainkan dengan dipukul.|Drum dipukul.
S|Piano dimainkan dengan ditiup.|Piano ditekan.
I can play … guitar.|the|a|an|on|Play the guitar.
Alat musik yang dimainkan dengan ditiup adalah …|flute|piano|drum|violin|Flute ditiup.
## BIG|Sports
Badminton artinya …|bulu tangkis|sepak bola|bola basket|renang|Badminton.
Bahasa Inggris dari renang adalah …|swimming|cycling|running|skipping|Swimming.
=|Bahasa Inggris dari sepak bola adalah …|football;soccer|Football.
=|Bahasa Inggris dari bersepeda adalah …|cycling|Cycling.
B|Volleyball artinya bola voli.|Volleyball.
S|Basketball artinya bulu tangkis.|Basketball = bola basket.
I like … badminton.|playing|play|plays|played|Like + ing.
What sport do you like? Jawaban yang tepat adalah …|I like swimming.|I am twelve.|It is Monday.|I like rice.|Olahraga.
## BIG|Describing people
Tall artinya …|tinggi|pendek|kurus|gemuk|Tall = tinggi.
Bahasa Inggris dari ramah adalah …|friendly|funny|smart|short|Friendly.
=|Bahasa Inggris dari baik hati adalah …|kind|Kind.
=|Bahasa Inggris dari pintar adalah …|smart;clever|Smart.
B|Funny artinya lucu.|Funny.
S|Short artinya tinggi.|Short = pendek.
My sister … long curly hair.|has|is|are|have|She has.
My father is tall … kind.|and|or|but|so|And.
## BIG|Things in the kitchen
Spoon artinya …|sendok|garpu|pisau|piring|Spoon = sendok.
Bahasa Inggris dari kompor adalah …|stove|plate|glass|fork|Stove.
=|Bahasa Inggris dari piring adalah …|plate|Plate.
=|Bahasa Inggris dari garpu adalah …|fork|Fork.
B|Knife artinya pisau.|Knife.
S|Glass artinya kompor.|Glass = gelas.
We cut vegetables with a …|knife|spoon|glass|plate|Pisau untuk memotong.
We drink water from a …|glass|knife|fork|stove|Gelas.
## BIG|School subjects
Math artinya …|matematika|IPA|seni|musik|Math.
Bahasa Inggris dari IPA adalah …|Science|Art|Music|English|Science.
=|Pelajaran menggambar dalam bahasa Inggris adalah …|Art|Art.
=|Pelajaran bernyanyi dalam bahasa Inggris adalah …|Music|Music.
B|Physical Education artinya pelajaran olahraga.|PE.
S|English artinya pelajaran matematika.|English = bahasa Inggris.
What is your favorite subject? Jawaban yang tepat adalah …|My favorite subject is Math.|I am fine.|It is red.|I go by bus.|Pelajaran.
In … class, we do experiments.|Science|Art|Music|English|Eksperimen di IPA.
## BIG|Asking permission
Ungkapan meminta izin adalah …|May I come in?|Come in!|Go away!|Sit down!|May I.
Jawaban jika mengizinkan adalah …|Yes, you may.|No, I don't.|I am sorry.|Thank you.|Yes, you may.
=|May I … your pencil? (meminjam)|borrow|Borrow.
=|Jawaban menolak izin dengan sopan adalah Sorry, you …|can't;cannot|Sorry, you can't.
B|Can I open the window? adalah kalimat meminta izin.|Meminta izin.
S|Give me your book! adalah cara meminta izin yang sopan.|Itu perintah.
Kamu ingin ke toilet saat pelajaran. Ucapan yang tepat adalah …|May I go to the toilet?|I go to the toilet.|Toilet, please!|You go to the toilet.|Meminta izin.
Sure, here you are. adalah jawaban untuk …|meminjam barang|menolak undangan|menanyakan umur|menanyakan cuaca|Memberikan barang.
## BIG|Invitations
Ungkapan untuk mengundang adalah …|Would you like to come?|I'm sorry, I can't.|Yes, I'd love to.|Thank you very much.|Mengundang.
Ungkapan untuk menerima undangan adalah …|Yes, I'd love to.|Sorry, I can't.|Maybe next time.|No, thanks.|Menerima.
=|Ungkapan mengajak dimulai dengan kata …|Let's|Let's.
=|Saat menolak undangan, kita sebaiknya memberi …|alasan|Alasan.
B|Sorry, I can't. I have to study. adalah penolakan yang sopan.|Ada alasan.
S|Yes, I'd love to. adalah ungkapan menolak undangan.|Menerima.
Let's go swimming! Jawaban menerima adalah …|Sure, that sounds fun.|Sorry, I can't.|No way!|I don't know you.|Menerima.
Would you like to come to my party? Jawaban menolak yang sopan adalah …|Sorry, I can't. I'm sick.|No!|Go away!|I don't like you.|Sopan dengan alasan.
"""

SAS += """
## BIG 1
0|Look! The cats ... playing in the garden.|are|is|am|be|They are.
1|A cheetah ... run very fast.|can|can't|is|are|Cheetah can run fast.
2|How ... milk is in the glass?|much|many|old|long|Milk tak terhitung.
3|Ordinal number dari 4 adalah ....|fourth|four|forth|fourty|Fourth.
4|2 May dibaca ....|May second|May two|second May two|May twoth|May second.
5|Alat musik yang dimainkan dengan digesek adalah ....|violin|drum|flute|trumpet|Biola digesek.
## BIG 2
0|Cycling artinya ....|bersepeda|berenang|berlari|mendaki|Cycling.
1|Smart artinya ....|pintar|lucu|ramah|tinggi|Smart.
2|We fry eggs in a ....|frying pan|glass|spoon|fork|Wajan.
3|In ... class, we sing songs.|Music|Math|Science|English|Music.
4|May I come in? Jawaban mengizinkan adalah ....|Yes, please come in.|No, I am not.|I don't know.|Goodbye.|Mengizinkan.
5|Maybe next time. adalah ungkapan untuk ....|menolak undangan|menerima undangan|mengundang|meminta izin|Menolak.
"""

TOPICS += """
## SBD
# 1|Seni Rupa dan Musik
@ Unsur-unsur seni rupa
min: 12
act: Cari contoh titik, garis, bidang, warna, dan tekstur pada benda-benda di kamarmu.
mis: mengira tekstur hanya bisa dilihat, tidak bisa diraba
exp: Karya seni rupa tersusun atas unsur-unsur. Titik adalah unsur terkecil. Garis adalah titik yang bersambung. Bidang terbentuk dari garis yang bertemu. Warna memberi kesan, dan tekstur adalah sifat permukaan yang dapat diraba atau dilihat, misalnya kasar dan halus.
ex: Kulit jeruk bertekstur kasar. // Lukisan pointilis tersusun dari titik-titik.
pt: Titik unsur terkecil ; Garis dan bidang membentuk gambar ; Tekstur sifat permukaan
sum: Unsur seni rupa adalah bahan dasar karya seni.
fig: table Unsur | Penjelasan ;; titik | unsur terkecil ;; garis | titik yang bersambung ;; bidang | ruang yang dibatasi garis ;; warna | kesan cahaya pada mata ;; tekstur | sifat permukaan benda ;; ruang | kesan jauh dekat ~ Unsur-unsur seni rupa.
@ Prinsip seni rupa
min: 12
act: Susun barang di meja belajarmu supaya terlihat seimbang dan rapi.
mis: mengira keseimbangan harus selalu sama persis kanan dan kiri
exp: Prinsip seni rupa adalah cara menyusun unsur supaya karya indah. Prinsip itu antara lain kesatuan, keseimbangan, irama, proporsi, dan pusat perhatian. Keseimbangan ada yang simetris atau sama kanan kiri dan asimetris atau tidak sama tetapi tetap seimbang.
ex: Batik dengan motif berulang menunjukkan irama. // Bunga paling besar di tengah lukisan menjadi pusat perhatian.
pt: Kesatuan dan keseimbangan ; Irama dan proporsi ; Pusat perhatian
sum: Prinsip seni rupa membuat karya tertata indah.
fig: table Prinsip | Arti ;; kesatuan | semua unsur terpadu ;; keseimbangan | bobot karya seimbang ;; irama | pengulangan unsur ;; proporsi | perbandingan ukuran yang serasi ;; pusat perhatian | bagian paling menonjol ;; kontras | perbedaan yang mencolok ~ Prinsip-prinsip seni rupa.
@ Gambar perspektif sederhana
min: 12
act: Gambar jalan lurus yang makin jauh makin kecil dengan satu titik hilang.
mis: menggambar benda jauh sama besar dengan benda dekat
exp: Gambar perspektif menunjukkan kesan jauh dan dekat pada bidang datar. Benda yang jauh digambar lebih kecil dan benda dekat digambar lebih besar. Garis-garis sejajar tampak bertemu di satu titik yang disebut titik hilang pada garis cakrawala.
ex: Rel kereta tampak menyempit di kejauhan. // Tiang listrik makin jauh makin pendek.
pt: Benda jauh lebih kecil ; Garis sejajar bertemu di titik hilang ; Titik hilang ada di garis cakrawala
sum: Perspektif membuat gambar terlihat nyata.
fig: table Istilah | Arti ;; perspektif | kesan jauh dan dekat ;; titik hilang | titik pertemuan garis ;; garis cakrawala | batas langit dan bumi ;; latar depan | bagian paling dekat ;; latar belakang | bagian paling jauh ;; satu titik hilang | perspektif paling sederhana ~ Istilah dalam gambar perspektif.
@ Teknik mewarnai
min: 12
act: Warnai tiga gambar yang sama dengan krayon, cat air, dan pensil warna, lalu bandingkan hasilnya.
mis: memakai banyak air pada krayon
exp: Ada beberapa teknik mewarnai. Teknik gradasi adalah perpaduan warna dari terang ke gelap. Teknik dussel adalah menggosok krayon lalu meratakannya dengan jari atau tisu. Teknik plakat memakai cat kental sehingga warna menutup rata. Teknik aquarel memakai cat encer sehingga warna tampak transparan.
ex: Langit sore diwarnai gradasi jingga ke ungu. // Cat air encer memberi kesan transparan.
pt: Gradasi terang ke gelap ; Plakat cat kental ; Aquarel cat encer
sum: Teknik mewarnai memberi kesan berbeda pada gambar.
fig: table Teknik | Ciri ;; gradasi | terang ke gelap ;; dussel | digosok dan diratakan ;; plakat | cat kental menutup rata ;; aquarel | cat encer transparan ;; arsir | garis-garis rapat ;; pointilis | titik-titik warna ~ Teknik mewarnai.
@ Tangga nada
min: 12
act: Nyanyikan do re mi fa sol la si do naik lalu turun dengan suara jelas.
mis: mengira tangga nada hanya bisa dinyanyikan naik
exp: Tangga nada adalah susunan nada yang berjenjang. Tangga nada diatonis mayor terdiri atas do, re, mi, fa, sol, la, si, do dan terdengar riang. Tangga nada minor terdengar sedih. Tangga nada pentatonis terdiri atas lima nada dan dipakai pada musik daerah seperti gamelan.
ex: Lagu Indonesia Raya memakai tangga nada mayor. // Gamelan Jawa memakai tangga nada pelog dan slendro.
pt: Tangga nada susunan nada berjenjang ; Mayor riang, minor sedih ; Pentatonis lima nada
sum: Tangga nada menentukan suasana lagu.
fig: table Tangga nada | Ciri ;; diatonis mayor | riang dan bersemangat ;; diatonis minor | sedih dan syahdu ;; pentatonis | terdiri atas lima nada ;; pelog | tangga nada gamelan Jawa ;; slendro | lima nada gamelan ;; kromatis | berjarak setengah nada ~ Jenis tangga nada.
@ Paduan suara
min: 12
act: Nyanyikan lagu bersama keluarga dengan suara tinggi dan rendah yang berbeda.
mis: bernyanyi paling keras supaya terdengar sendiri
exp: Paduan suara adalah kelompok penyanyi yang bernyanyi bersama dengan suara yang berbeda-beda tetapi selaras. Paduan suara dipimpin oleh dirigen. Suara dibagi menjadi sopran, alto, tenor, dan bas. Kekompakan dan saling mendengarkan sangat penting.
ex: Paduan suara menyanyikan lagu wajib saat upacara. // Dirigen memberi aba-aba mulai bernyanyi.
pt: Bernyanyi bersama dan selaras ; Dipimpin dirigen ; Suara sopran, alto, tenor, bas
sum: Paduan suara mengutamakan keselarasan.
fig: table Jenis suara | Ciri ;; sopran | suara perempuan tinggi ;; alto | suara perempuan rendah ;; tenor | suara laki-laki tinggi ;; bas | suara laki-laki rendah ;; dirigen | pemimpin paduan suara ;; unisono | semua menyanyikan nada sama ~ Jenis suara dalam paduan suara.
@ Alat musik melodis
min: 12
act: Mainkan lagu Balonku dengan pianika atau aplikasi piano di ponsel.
mis: mengira alat musik melodis hanya untuk mengatur irama
exp: Alat musik melodis adalah alat musik yang dapat memainkan nada-nada sehingga membentuk melodi lagu. Contohnya pianika, recorder, gitar, piano, angklung, dan kolintang. Berbeda dengan alat musik ritmis yang hanya mengatur irama.
ex: Pianika dimainkan dengan ditiup sambil menekan tuts. // Recorder dimainkan dengan ditiup dan menutup lubang.
pt: Dapat memainkan melodi ; Contohnya pianika dan recorder ; Berbeda dengan alat ritmis
sum: Alat musik melodis memainkan nada lagu.
fig: table Alat musik | Cara memainkan ;; pianika | ditiup sambil menekan tuts ;; recorder | ditiup dan menutup lubang ;; gitar | dipetik ;; piano | ditekan tutsnya ;; biola | digesek ;; kolintang | dipukul ~ Alat musik melodis dan cara memainkannya.
@ Membuat karya grafis cetak
min: 12
act: Cetak motif dari potongan pelepah pisang atau kentang dengan cat, lalu cap di kertas.
mis: memakai cat terlalu encer sehingga cetakan tidak jelas
exp: Karya grafis cetak dibuat dengan mencetak gambar dari klise atau cetakan. Ada cetak tinggi, misalnya cetak dari kentang atau stempel. Ada cetak saring atau sablon. Klise bisa dibuat dari kentang, pelepah pisang, karet, atau kayu. Satu klise dapat menghasilkan banyak cetakan.
ex: Kentang dipotong dan diukir menjadi bentuk bintang. // Sablon dipakai untuk mencetak gambar kaus.
pt: Dicetak dari klise ; Ada cetak tinggi dan cetak saring ; Satu klise banyak cetakan
sum: Karya grafis dapat diperbanyak dengan cetakan.
fig: table Bahan klise | Hasil cetakan ;; kentang | motif sederhana ;; pelepah pisang | motif garis ;; daun | motif tulang daun ;; karet sandal | stempel bentuk ;; kayu | cukil kayu ;; screen sablon | gambar pada kaus ~ Bahan klise dan hasil cetaknya.
# 2|Tari, Teater, dan Kriya
@ Unsur pendukung tari
min: 12
act: Pilih satu tarian daerah, lalu cari tahu kostum, musik, dan properti yang dipakai.
mis: mengira tari hanya berupa gerakan tanpa unsur lain
exp: Tari didukung oleh beberapa unsur selain gerak. Iringan musik memberi irama, tata busana atau kostum menunjukkan karakter, tata rias memperjelas wajah penari, properti mendukung gerak, dan tata panggung serta tata cahaya membuat pertunjukan menarik.
ex: Tari Saman diiringi tepukan dan nyanyian. // Penari Bali memakai riasan mata yang tegas.
pt: Musik memberi irama ; Kostum dan rias menunjukkan karakter ; Properti dan panggung mendukung
sum: Unsur pendukung membuat tari lebih indah.
fig: table Unsur pendukung | Fungsi ;; iringan musik | memberi irama ;; kostum | menunjukkan karakter ;; tata rias | memperjelas wajah ;; properti | mendukung gerak ;; tata cahaya | memperindah suasana ;; panggung | tempat menari ~ Unsur pendukung tari.
@ Tari berpasangan
min: 12
act: Latih gerakan sederhana bersama saudara dengan gerak saling berhadapan dan bergantian.
mis: menari sendiri tanpa memperhatikan gerak pasangan
exp: Tari berpasangan ditarikan oleh dua orang atau lebih yang saling merespons gerak pasangannya. Contohnya Tari Serampang Dua Belas dari Sumatera Utara dan Tari Jaipong berpasangan. Kekompakan dan saling memperhatikan sangat penting dalam tari berpasangan.
ex: Penari bergerak saling berhadapan. // Gerak tangan bergantian antara dua penari.
pt: Ditarikan berpasangan ; Saling merespons gerak ; Butuh kekompakan
sum: Tari berpasangan mengutamakan kerja sama.
fig: table Jenis tari | Jumlah penari ;; tari tunggal | satu orang ;; tari berpasangan | dua orang ;; tari kelompok | lebih dari dua ;; tari massal | sangat banyak penari ;; Serampang Dua Belas | berpasangan dari Sumatera Utara ;; Saman | kelompok dari Aceh ~ Jenis tari berdasarkan jumlah penari.
@ Tata rias dan busana tari
min: 12
act: Buat sketsa kostum tari untuk tokoh kupu-kupu dengan warna cerah.
mis: memakai kostum yang terlalu ketat sehingga sulit bergerak
exp: Tata rias tari memperjelas garis wajah dan menunjukkan karakter tokoh. Tata busana tari disesuaikan dengan tema dan karakter, nyaman dipakai, dan tidak mengganggu gerak. Warna kostum juga memberi makna, misalnya merah untuk berani dan putih untuk suci.
ex: Rias tokoh raksasa dibuat tegas. // Kostum kupu-kupu diberi sayap kain warna-warni.
pt: Rias memperjelas karakter ; Busana sesuai tema ; Nyaman dan tidak mengganggu gerak
sum: Rias dan busana memperkuat penampilan penari.
fig: table Warna kostum | Kesan ;; merah | berani ;; putih | suci ;; kuning | ceria dan agung ;; hijau | kesejukan alam ;; hitam | tegas dan misterius ;; biru | tenang ~ Warna kostum dan kesannya.
@ Naskah drama
min: 12
act: Tulis naskah drama pendek tentang kejadian lucu di rumah dengan tiga tokoh.
mis: menulis naskah tanpa petunjuk laku
exp: Naskah drama adalah teks yang berisi dialog dan petunjuk untuk dipentaskan. Naskah drama memiliki judul, daftar tokoh, dialog, dan petunjuk laku yang ditulis dalam kurung. Petunjuk laku menjelaskan gerak, ekspresi, atau suasana yang harus diperankan.
ex: Ibu: (tersenyum) Ayo makan bersama. // Ani: (berlari masuk) Aku datang!
pt: Berisi dialog ; Ada daftar tokoh ; Petunjuk laku dalam kurung
sum: Naskah drama adalah panduan pementasan.
fig: table Bagian naskah | Isi ;; judul | nama drama ;; daftar tokoh | siapa saja pemerannya ;; prolog | pengantar cerita ;; dialog | percakapan antartokoh ;; petunjuk laku | gerak dalam kurung ;; epilog | penutup cerita ~ Bagian-bagian naskah drama.
@ Ekspresi dalam teater
min: 12
act: Tirukan ekspresi senang, sedih, marah, dan terkejut di depan cermin.
mis: berdialog dengan wajah datar padahal tokohnya sedih
exp: Ekspresi adalah ungkapan perasaan yang terlihat dari wajah, suara, dan gerak tubuh. Dalam teater, pemain harus berekspresi sesuai tokoh dan suasana. Selain ekspresi, pemain perlu memperhatikan vokal atau suara yang jelas dan penghayatan.
ex: Tokoh sedih berbicara pelan dengan wajah murung. // Tokoh marah bersuara keras dan tegas.
pt: Ekspresi lewat wajah, suara, gerak ; Sesuai tokoh dan suasana ; Vokal jelas
sum: Ekspresi membuat penonton merasakan cerita.
fig: table Perasaan | Ekspresi ;; senang | tersenyum lebar ;; sedih | wajah murung ;; marah | alis berkerut ;; terkejut | mata membelalak ;; takut | badan gemetar ;; bingung | menggaruk kepala ~ Perasaan dan ekspresinya.
@ Makrame
min: 12
act: Buat gantungan kunci makrame dari tali kur dengan simpul dasar.
mis: menarik simpul terlalu longgar sehingga mudah lepas
exp: Makrame adalah seni menyimpul tali menjadi benda hias atau benda pakai. Bahannya tali kur, tali rami, atau benang tebal. Simpul dasar makrame antara lain simpul kepala, simpul pipih, dan simpul spiral. Contoh hasilnya gantungan kunci, gelang, dan tempat pot gantung.
ex: Gelang dari simpul pipih. // Tempat pot gantung dari tali rami.
pt: Seni menyimpul tali ; Simpul kepala, pipih, spiral ; Hasilnya benda hias dan pakai
sum: Makrame mengubah tali menjadi karya indah.
fig: table Simpul | Kegunaan ;; simpul kepala | mengikat tali di awal ;; simpul pipih | membuat bentuk datar ;; simpul spiral | membuat bentuk berpilin ;; simpul kordon | membuat garis timbul ;; simpul mati | mengunci ujung tali ;; simpul jangkar | menahan beban ~ Jenis simpul makrame.
@ Anyaman
min: 12
act: Anyam potongan kertas warna menjadi tikar kecil dengan pola selang-seling.
mis: menyusun lungsin dan pakan tanpa selang-seling
exp: Anyaman dibuat dengan menyilangkan bahan secara bergantian. Bahan yang dipasang tegak disebut lungsin, dan yang disisipkan mendatar disebut pakan. Bahan anyaman bisa bambu, rotan, pandan, daun kelapa, atau kertas. Hasilnya tikar, keranjang, topi, dan tas.
ex: Ketupat dianyam dari janur atau daun kelapa muda. // Tikar dianyam dari daun pandan.
pt: Menyilangkan bahan bergantian ; Lungsin tegak, pakan mendatar ; Bahan dari alam atau kertas
sum: Anyaman adalah kerajinan menyilang bahan.
fig: table Bahan anyaman | Contoh hasil ;; bambu | keranjang ;; rotan | kursi ;; pandan | tikar ;; janur | ketupat ;; mendong | topi ;; kertas | hiasan dinding ~ Bahan anyaman dan hasilnya.
@ Patung dari sabun
min: 12
act: Ukir sabun batang menjadi bentuk ikan memakai sendok plastik dengan pendampingan orang tua.
mis: mengukir terlalu dalam sekaligus sehingga sabun patah
exp: Patung adalah karya seni tiga dimensi yang memiliki panjang, lebar, dan tinggi. Patung sederhana bisa dibuat dari sabun batang dengan teknik pahat atau ukir. Gambar pola di sabun, kurangi bagian yang tidak dipakai sedikit demi sedikit, lalu haluskan.
ex: Sabun diukir menjadi kura-kura. // Sisa kerokan sabun bisa dipakai mencuci.
pt: Patung karya tiga dimensi ; Dibuat dengan mengurangi bahan ; Kerjakan sedikit demi sedikit
sum: Sabun bisa dipahat menjadi patung kecil.
fig: table Bahan patung | Teknik ;; sabun | ukir atau pahat ;; tanah liat | butsir ;; kayu | pahat ;; batu | pahat keras ;; logam | cor ;; lilin | dibentuk saat lunak ~ Bahan dan teknik membuat patung.
"""

BANK += """
## SBD|Unsur-unsur seni rupa
Unsur seni rupa yang paling kecil adalah …|titik|garis|bidang|warna|Titik.
Sifat permukaan benda yang dapat diraba disebut …|tekstur|warna|bidang|irama|Tekstur.
=|Titik-titik yang bersambung membentuk …|garis|Garis.
=|Kulit jeruk memiliki tekstur …|kasar|Kasar.
B|Bidang terbentuk dari garis yang bertemu.|Bidang.
S|Tekstur hanya bisa dilihat dan tidak bisa diraba.|Bisa diraba.
Kesan jauh dan dekat pada gambar termasuk unsur …|ruang|titik|tekstur|warna|Ruang.
Contoh benda bertekstur halus adalah …|kaca|amplas|batu kali|kulit nanas|Kaca halus.
## SBD|Prinsip seni rupa
Pengulangan unsur dalam karya seni disebut prinsip …|irama|kesatuan|proporsi|kontras|Irama.
Bagian yang paling menonjol dalam karya disebut …|pusat perhatian|latar|tekstur|bidang|Pusat perhatian.
=|Perbandingan ukuran yang serasi disebut …|proporsi|Proporsi.
=|Keseimbangan yang sama antara kanan dan kiri disebut keseimbangan …|simetris|Simetris.
B|Motif batik yang berulang menunjukkan irama.|Irama.
S|Keseimbangan asimetris berarti kanan dan kiri sama persis.|Tidak sama tetapi seimbang.
Perpaduan semua unsur menjadi satu karya terpadu disebut …|kesatuan|irama|kontras|tekstur|Kesatuan.
Warna hitam di samping putih menunjukkan prinsip …|kontras|kesatuan|proporsi|irama|Kontras.
## SBD|Gambar perspektif sederhana
Gambar perspektif menunjukkan kesan …|jauh dan dekat|panas dan dingin|kasar dan halus|terang dan gelap saja|Jauh dekat.
Titik pertemuan garis sejajar dalam perspektif disebut …|titik hilang|titik pusat|titik awal|titik akhir|Titik hilang.
=|Batas antara langit dan bumi dalam gambar disebut garis …|cakrawala|Garis cakrawala.
=|Benda yang dekat digambar lebih …|besar|Besar.
B|Rel kereta tampak menyempit di kejauhan.|Perspektif.
S|Benda jauh digambar lebih besar dari benda dekat.|Lebih kecil.
Bagian gambar yang paling dekat dengan pengamat disebut …|latar depan|latar belakang|cakrawala|titik hilang|Latar depan.
Perspektif paling sederhana memakai … titik hilang.|satu|tiga|lima|sepuluh|Satu.
## SBD|Teknik mewarnai
Teknik mewarnai dari terang ke gelap disebut …|gradasi|plakat|dussel|pointilis|Gradasi.
Teknik mewarnai dengan cat kental sehingga menutup rata disebut …|plakat|aquarel|gradasi|arsir|Plakat.
=|Teknik mewarnai dengan cat encer dan transparan disebut …|aquarel;akuarel|Aquarel.
=|Teknik mewarnai dengan titik-titik disebut …|pointilis|Pointilis.
B|Teknik dussel memakai krayon yang digosok dan diratakan.|Dussel.
S|Teknik aquarel memakai cat yang sangat kental.|Cat encer.
Teknik mewarnai dengan garis-garis rapat disebut …|arsir|plakat|gradasi|dussel|Arsir.
Alat yang cocok untuk teknik dussel adalah …|krayon|cat minyak|tinta|spidol|Krayon.
## SBD|Tangga nada
Susunan nada yang berjenjang disebut …|tangga nada|tempo|dinamika|birama|Tangga nada.
Tangga nada yang terdengar riang adalah …|mayor|minor|pentatonis sedih|kromatis|Mayor.
=|Tangga nada yang terdengar sedih adalah …|minor|Minor.
=|Tangga nada pentatonis terdiri atas … nada.|lima;5|Lima nada.
B|Pelog dan slendro adalah tangga nada gamelan.|Gamelan.
S|Tangga nada mayor selalu terdengar sedih.|Riang.
Urutan tangga nada diatonis yang benar adalah …|do re mi fa sol la si do|do mi re fa la sol si do|re do mi fa sol la si|do re fa mi sol si la|Urutan benar.
Lagu Indonesia Raya memakai tangga nada …|mayor|minor|pelog|slendro|Mayor.
## SBD|Paduan suara
Pemimpin paduan suara disebut …|dirigen|solois|penonton|pemain gitar|Dirigen.
Suara perempuan yang tinggi disebut …|sopran|alto|tenor|bas|Sopran.
=|Suara laki-laki yang rendah disebut …|bas|Bas.
=|Suara perempuan yang rendah disebut …|alto|Alto.
B|Paduan suara mengutamakan keselarasan suara.|Selaras.
S|Dalam paduan suara, setiap orang bernyanyi sekeras mungkin.|Selaras.
Suara laki-laki yang tinggi disebut …|tenor|bas|sopran|alto|Tenor.
Bernyanyi bersama dengan nada yang sama disebut …|unisono|kanon|solo|duet|Unisono.
## SBD|Alat musik melodis
Alat musik melodis dapat memainkan …|melodi lagu|irama saja|ketukan saja|suara gong saja|Melodi.
Pianika dimainkan dengan cara …|ditiup sambil menekan tuts|dipetik|digesek|dipukul|Ditiup dan tuts.
=|Biola dimainkan dengan cara …|digesek|Digesek.
=|Gitar dimainkan dengan cara …|dipetik|Dipetik.
B|Recorder termasuk alat musik melodis.|Melodis.
S|Marakas termasuk alat musik melodis.|Marakas ritmis.
Alat musik melodis dari Sulawesi Utara adalah …|kolintang|tifa|rebana|gong|Kolintang.
Piano dimainkan dengan cara …|menekan tuts|meniup|menggesek|mengocok|Tuts ditekan.
## SBD|Membuat karya grafis cetak
Karya grafis cetak dibuat dengan cara …|mencetak dari klise|melipat kertas|menganyam|menyimpul tali|Klise.
Cetakan untuk karya grafis disebut …|klise|kanvas|palet|kuas|Klise.
=|Teknik cetak saring disebut juga …|sablon|Sablon.
=|Klise sederhana dapat dibuat dari umbi …|kentang|Kentang.
B|Satu klise dapat menghasilkan banyak cetakan.|Banyak cetakan.
S|Karya grafis hanya bisa dibuat satu kali.|Bisa diperbanyak.
Teknik cetak dari kayu yang dicukil disebut …|cukil kayu|sablon|batik|mozaik|Cukil kayu.
Cat untuk cetak sebaiknya …|cukup kental|sangat encer|kering|dicampur pasir|Cukup kental.
## SBD|Unsur pendukung tari
Unsur pendukung tari yang memberi irama adalah …|iringan musik|kostum|tata rias|properti|Musik.
Tata rias tari berfungsi untuk …|memperjelas wajah penari|menutup panggung|memberi irama|membuat lantai licin|Rias.
=|Pakaian yang dikenakan penari disebut …|kostum;busana|Kostum.
=|Benda yang dipegang penari untuk mendukung gerak disebut …|properti|Properti.
B|Tata cahaya dapat memperindah suasana pertunjukan.|Cahaya.
S|Tari tidak membutuhkan unsur pendukung apa pun.|Butuh unsur pendukung.
Tari Saman diiringi oleh …|tepukan dan nyanyian|gamelan|biola|gitar listrik|Saman.
Tempat penari menampilkan tarian adalah …|panggung|kostum|properti|naskah|Panggung.
## SBD|Tari berpasangan
Tari yang ditarikan dua orang disebut tari …|berpasangan|tunggal|massal|kelompok besar|Berpasangan.
Tari Serampang Dua Belas berasal dari …|Sumatera Utara|Bali|Papua|Jawa Timur|Sumatera Utara.
=|Tari yang ditarikan satu orang disebut tari …|tunggal|Tunggal.
=|Tari yang ditarikan banyak sekali penari disebut tari …|massal|Massal.
B|Tari berpasangan membutuhkan kekompakan.|Kompak.
S|Dalam tari berpasangan, penari tidak perlu memperhatikan pasangannya.|Harus saling merespons.
Tari Saman termasuk tari …|kelompok|tunggal|berpasangan|massal kerajaan|Kelompok.
Kunci keberhasilan tari berpasangan adalah …|saling memperhatikan gerak|bergerak sendiri|tidak berlatih|menari secepatnya|Saling memperhatikan.
## SBD|Tata rias dan busana tari
Busana tari sebaiknya …|nyaman dan tidak mengganggu gerak|sangat ketat|sangat berat|asal-asalan|Nyaman.
Warna merah pada kostum memberi kesan …|berani|suci|tenang|sedih|Berani.
=|Warna putih pada kostum memberi kesan …|suci|Suci.
=|Tata rias tari menunjukkan … tokoh.|karakter;watak|Karakter.
B|Kostum tari disesuaikan dengan tema tarian.|Sesuai tema.
S|Kostum tari harus sesempit mungkin.|Nyaman.
Warna biru pada kostum memberi kesan …|tenang|berani|ceria|misterius|Tenang.
Rias untuk tokoh raksasa biasanya dibuat …|tegas dan tajam|pucat polos|tanpa warna|lembut sekali|Tegas.
## SBD|Naskah drama
Petunjuk laku dalam naskah drama ditulis di dalam …|tanda kurung|tanda petik|tanda seru|tanda tanya|Kurung.
Percakapan antartokoh dalam naskah disebut …|dialog|prolog|epilog|judul|Dialog.
=|Bagian pengantar cerita drama disebut …|prolog|Prolog.
=|Bagian penutup cerita drama disebut …|epilog|Epilog.
B|Naskah drama memiliki daftar tokoh.|Daftar tokoh.
S|Petunjuk laku diucapkan oleh pemain.|Petunjuk laku diperagakan.
Fungsi naskah drama adalah …|panduan pementasan|daftar belanja|resep|peta|Panduan.
Ibu: (tersenyum) Ayo makan. Kata tersenyum adalah …|petunjuk laku|dialog|judul|nama tokoh|Petunjuk laku.
## SBD|Ekspresi dalam teater
Ekspresi adalah ungkapan …|perasaan|harga|alamat|nama|Perasaan.
Ekspresi senang ditunjukkan dengan …|tersenyum lebar|alis berkerut|wajah murung|badan gemetar|Senyum.
=|Ekspresi terkejut ditunjukkan dengan mata …|membelalak;terbelalak|Membelalak.
=|Ekspresi bingung dapat ditunjukkan dengan menggaruk …|kepala|Kepala.
B|Ekspresi dapat terlihat dari suara pemain.|Suara.
S|Tokoh sedih sebaiknya diperankan sambil tertawa.|Wajah murung.
Ekspresi marah ditunjukkan dengan …|alis berkerut|tersenyum|mata sayu|tertawa|Alis berkerut.
Suara pemain teater harus …|jelas|berbisik|tidak terdengar|tertahan|Jelas.
## SBD|Makrame
Makrame adalah seni …|menyimpul tali|menganyam bambu|melipat kertas|membentuk tanah liat|Menyimpul.
Bahan utama makrame adalah …|tali|tanah liat|kertas lipat|cat air|Tali.
=|Simpul untuk mengikat tali di awal disebut simpul …|kepala|Simpul kepala.
=|Simpul yang membentuk bentuk berpilin disebut simpul …|spiral|Spiral.
B|Gantungan kunci dapat dibuat dengan makrame.|Gantungan kunci.
S|Makrame dibuat dengan cara menganyam bambu.|Menyimpul tali.
Simpul yang membentuk bentuk datar disebut simpul …|pipih|spiral|kepala|mati|Pipih.
Contoh hasil makrame adalah …|tempat pot gantung|piring keramik|lukisan cat minyak|patung batu|Pot gantung.
## SBD|Anyaman
Bahan anyaman yang dipasang tegak disebut …|lungsin|pakan|simpul|klise|Lungsin.
Bahan anyaman yang disisipkan mendatar disebut …|pakan|lungsin|tali|benang jahit|Pakan.
=|Ketupat dianyam dari …|janur;daun kelapa muda|Janur.
=|Tikar biasanya dianyam dari daun …|pandan|Pandan.
B|Anyaman dibuat dengan menyilangkan bahan bergantian.|Selang-seling.
S|Anyaman dibuat dengan menempel potongan kertas bertumpuk.|Disilangkan.
Kursi anyaman biasanya dibuat dari …|rotan|plastik keras|kaca|besi|Rotan.
Keranjang anyaman biasanya dibuat dari …|bambu|kaca|batu|logam|Bambu.
## SBD|Patung dari sabun
Patung adalah karya seni …|tiga dimensi|dua dimensi|satu dimensi|datar|Tiga dimensi.
Teknik membuat patung dari sabun adalah …|ukir atau pahat|anyam|lipat|cetak saring|Ukir.
=|Patung dari tanah liat dibuat dengan teknik …|butsir|Butsir.
=|Patung dari logam dibuat dengan teknik …|cor|Cor.
B|Patung dibuat dengan mengurangi bahan sedikit demi sedikit.|Bertahap.
S|Patung adalah karya seni yang datar tanpa tinggi.|Tiga dimensi.
Alat aman untuk mengukir sabun bagi anak adalah …|sendok plastik|pisau besar|gergaji|kapak|Aman.
Langkah pertama membuat patung sabun adalah …|menggambar pola di sabun|menghaluskan|mengecat|menjemur|Pola dulu.
"""

SAS += """
## SBD 1
0|Unsur seni rupa yang memberi kesan jauh dekat adalah ....|ruang|titik|garis|tekstur|Ruang.
1|Bunga paling besar di tengah lukisan menunjukkan prinsip ....|pusat perhatian|irama|kesatuan|proporsi|Pusat perhatian.
2|Tiang listrik yang makin jauh digambar makin pendek menunjukkan gambar ....|perspektif|dekoratif|ilustrasi|karikatur|Perspektif.
3|Teknik mewarnai dengan menggosok krayon lalu meratakan dengan tisu adalah ....|dussel|plakat|aquarel|pointilis|Dussel.
4|Tangga nada yang berjarak setengah nada disebut ....|kromatis|pelog|mayor|pentatonis|Kromatis.
5|Paduan suara yang menyanyikan nada sama disebut ....|unisono|kanon|trio|kuartet|Unisono.
6|Recorder dimainkan dengan cara ....|ditiup dan menutup lubang|dipetik|digesek|dipukul|Recorder.
7|Sablon termasuk teknik cetak ....|saring|tinggi|dalam|datar|Cetak saring.
## SBD 2
0|Unsur pendukung tari yang memperindah suasana dengan lampu adalah ....|tata cahaya|tata rias|kostum|properti|Tata cahaya.
1|Tari yang ditarikan lebih dari dua orang disebut tari ....|kelompok|tunggal|berpasangan|solo|Kelompok.
2|Warna kuning pada kostum tari memberi kesan ....|ceria dan agung|sedih|misterius|tenang|Kuning.
3|Bagian naskah yang berisi siapa saja pemerannya adalah ....|daftar tokoh|dialog|epilog|petunjuk laku|Daftar tokoh.
4|Ekspresi takut ditunjukkan dengan ....|badan gemetar|tersenyum lebar|alis berkerut marah|menggaruk kepala|Takut.
5|Simpul makrame untuk mengunci ujung tali adalah simpul ....|mati|kepala|spiral|pipih|Simpul mati.
6|Topi anyaman sering dibuat dari ....|mendong|kaca|plastik keras|besi|Mendong.
7|Patung dari kayu dibuat dengan teknik ....|pahat|cor|butsir|anyam|Pahat.
"""

TOPICS += """
## PJOK
# 1|Atletik, Permainan, dan Bela Diri
@ Lompat jauh gaya jongkok
min: 12
act: Latih awalan dan tolakan lompat jauh di bak pasir atau halaman berumput bersama teman.
mis: menolak dengan kaki yang berada jauh di belakang papan tolakan
exp: Lompat jauh gaya jongkok terdiri atas empat tahap, yaitu awalan, tolakan, melayang, dan mendarat. Awalan berupa lari dengan kecepatan meningkat. Tolakan dilakukan dengan satu kaki terkuat di papan tolakan. Saat melayang, kedua lutut ditekuk seperti jongkok. Pendaratan dengan dua kaki dan badan condong ke depan.
ex: Tolakan dengan kaki terkuat di papan. // Saat melayang lutut ditarik ke dada.
pt: Awalan, tolakan, melayang, mendarat ; Tolakan satu kaki terkuat ; Melayang dengan sikap jongkok
sum: Gaya jongkok adalah gaya lompat jauh paling sederhana.
fig: table Tahap | Gerakan ;; awalan | lari makin cepat ;; tolakan | satu kaki di papan ;; melayang | lutut ditekuk seperti jongkok ;; mendarat | dua kaki di pasir ;; posisi badan saat mendarat | condong ke depan ;; pengukuran | dari papan ke bekas terdekat ~ Tahapan lompat jauh gaya jongkok.
@ Lari jarak menengah
min: 12
act: Lari mengelilingi lapangan beberapa kali dengan kecepatan tetap tanpa berhenti.
mis: berlari sangat cepat di awal sehingga cepat kelelahan
exp: Lari jarak menengah adalah lari dengan jarak 800 sampai 1.500 meter. Lari ini membutuhkan daya tahan. Pelari harus mengatur kecepatan dan napas, tidak terlalu cepat di awal, lalu mempercepat lari menjelang garis finis. Start yang dipakai adalah start berdiri.
ex: Lari 800 meter mengelilingi lintasan dua kali. // Atur napas dengan teratur.
pt: Jarak 800 sampai 1.500 meter ; Butuh daya tahan ; Start berdiri dan atur kecepatan
sum: Lari jarak menengah melatih daya tahan.
fig: table Jenis lari | Jarak ;; lari jarak pendek | 100 sampai 400 meter ;; lari jarak menengah | 800 sampai 1.500 meter ;; lari jarak jauh | lebih dari 3.000 meter ;; lari estafet | 4 × 100 meter ;; maraton | 42,195 km ;; lari gawang | memakai rintangan ~ Jenis lari dan jaraknya.
@ Menggiring bola dalam sepak bola
min: 12
act: Susun beberapa botol berjarak, lalu giring bola melewatinya dengan kaki bagian dalam dan luar.
mis: menendang bola terlalu jauh saat menggiring
exp: Menggiring bola adalah membawa bola dengan kaki sambil berlari. Bola didorong pelan supaya tetap dekat dengan kaki. Menggiring dapat memakai kaki bagian dalam, luar, atau punggung kaki. Pandangan sesekali ke depan untuk melihat lawan dan teman.
ex: Menggiring bola zig-zag melewati kerucut. // Bola didorong pelan dengan kaki bagian dalam.
pt: Bola tetap dekat kaki ; Bisa memakai kaki dalam, luar, atau punggung ; Pandangan sesekali ke depan
sum: Menggiring bola membantu melewati lawan.
fig: table Teknik dasar sepak bola | Tujuan ;; menggiring | membawa bola sambil berlari ;; mengoper | memberi bola kepada teman ;; menghentikan | menguasai bola ;; menendang ke gawang | mencetak gol ;; menyundul | memainkan bola dengan kepala ;; lemparan ke dalam | memulai permainan dari pinggir ~ Teknik dasar sepak bola.
@ Passing atas bola voli
min: 12
act: Lambungkan bola ke atas lalu pantulkan dengan jari-jari kedua tangan di atas dahi.
mis: memukul bola dengan telapak tangan yang kaku
exp: Passing atas adalah memainkan bola voli dengan jari-jari kedua tangan di atas dahi. Jari-jari membentuk seperti mangkuk, lutut sedikit ditekuk, lalu bola didorong ke atas dengan meluruskan lutut dan lengan. Passing atas dipakai untuk mengumpan bola kepada teman.
ex: Jari-jari membentuk mangkuk di atas dahi. // Dorongan berasal dari lutut dan lengan.
pt: Bola dimainkan di atas dahi ; Jari membentuk mangkuk ; Dorong dengan meluruskan lutut dan lengan
sum: Passing atas dipakai untuk mengumpan.
fig: table Teknik bola voli | Kegunaan ;; servis | memulai permainan ;; passing bawah | menerima bola rendah ;; passing atas | mengumpan bola ;; smash | memukul bola keras ke lawan ;; blok | menahan smash lawan ;; set up | mengumpan untuk smash ~ Teknik dasar bola voli.
@ Menembak bola basket
min: 12
act: Lempar bola ke dalam keranjang atau ember di dinding sebanyak sepuluh kali dan hitung yang masuk.
mis: melempar bola hanya dengan kekuatan tangan tanpa menekuk lutut
exp: Menembak atau shooting adalah memasukkan bola ke dalam keranjang lawan. Bola dipegang dengan tangan terkuat di bawah bola dan tangan lain di samping. Lutut ditekuk, lalu bola didorong ke atas ke arah keranjang sambil meluruskan lutut dan lengan. Pandangan tertuju ke ring.
ex: Shooting dari dekat ring. // Lay-up dilakukan sambil melangkah dua kali.
pt: Pegang bola dengan benar ; Tekuk lalu luruskan lutut ; Pandangan ke ring
sum: Tembakan yang tepat menghasilkan poin.
fig: table Istilah bola basket | Arti ;; shooting | menembak ke ring ;; dribbling | menggiring bola ;; passing | mengoper bola ;; lay-up | tembakan sambil melangkah ;; ring | keranjang bola ;; free throw | tembakan hukuman ~ Istilah dalam bola basket.
@ Permainan rounders
min: 12
act: Bermain rounders sederhana dengan pemukul plastik dan bola tenis bersama teman.
mis: berlari ke tiang hinggap tanpa memukul bola lebih dulu
exp: Rounders adalah permainan bola kecil yang dimainkan oleh dua regu, yaitu regu pemukul dan regu penjaga. Pemukul memukul bola lalu berlari mengelilingi tiang-tiang hinggap. Regu penjaga berusaha menangkap bola atau mematikan pelari. Permainan ini mirip dengan kasti.
ex: Pemukul berlari ke tiang hinggap setelah memukul bola. // Penjaga menangkap bola langsung untuk mematikan pemukul.
pt: Dua regu pemukul dan penjaga ; Pukul lalu lari ke tiang hinggap ; Penjaga menangkap atau mematikan
sum: Rounders melatih memukul, berlari, dan menangkap.
fig: table Posisi atau istilah | Tugas ;; pemukul | memukul bola ;; pelambung | melempar bola kepada pemukul ;; penjaga lapangan | menangkap bola ;; tiang hinggap | tempat pelari berhenti ;; pelari | mengelilingi tiang hinggap ;; penjaga belakang | berdiri di belakang pemukul ~ Posisi dalam permainan rounders.
@ Gerak dasar pencak silat
min: 12
act: Latih kuda-kuda depan dan sikap pasang dengan pendampingan orang dewasa.
mis: melakukan gerakan silat untuk bercanda memukul teman
exp: Pencak silat adalah bela diri asli Indonesia. Gerak dasarnya antara lain kuda-kuda, sikap pasang, pukulan, tendangan, tangkisan, dan elakan. Kuda-kuda adalah posisi kaki yang kokoh. Pencak silat melatih kekuatan, kelincahan, disiplin, dan sikap sportif.
ex: Kuda-kuda depan dengan kaki depan ditekuk. // Tangkisan untuk menahan serangan.
pt: Bela diri asli Indonesia ; Kuda-kuda dan sikap pasang ; Melatih disiplin dan sportivitas
sum: Pencak silat adalah warisan budaya yang menyehatkan.
fig: table Gerak dasar | Tujuan ;; kuda-kuda | posisi kaki kokoh ;; sikap pasang | siap bertahan dan menyerang ;; pukulan | menyerang dengan tangan ;; tendangan | menyerang dengan kaki ;; tangkisan | menahan serangan ;; elakan | menghindari serangan ~ Gerak dasar pencak silat.
@ Lompat tinggi gaya gunting
min: 12
act: Pasang tali rendah di antara dua kursi, lalu latih lompatan gaya gunting dengan aman.
mis: menolak dengan kedua kaki bersamaan
exp: Lompat tinggi gaya gunting dilakukan dengan awalan dari samping mistar. Tolakan memakai satu kaki terjauh dari mistar. Saat melewati mistar, kaki diayun bergantian seperti gerakan gunting. Pendaratan dengan kaki yang lebih dulu melewati mistar.
ex: Awalan menyamping dari mistar. // Kaki diayun bergantian di atas mistar.
pt: Awalan dari samping ; Tolakan satu kaki ; Kaki bergantian seperti gunting
sum: Gaya gunting cocok untuk belajar lompat tinggi.
fig: table Tahap | Gerakan ;; awalan | lari dari samping mistar ;; tolakan | satu kaki terjauh dari mistar ;; ayunan | kaki dekat mistar diayun ke atas ;; melewati mistar | kaki bergantian seperti gunting ;; mendarat | kaki yang pertama melewati mistar ;; alas mendarat | matras atau bak pasir ~ Tahapan lompat tinggi gaya gunting.
# 2|Senam, Renang, dan Kesehatan
@ Meroda
min: 12
act: Latih gerakan meroda di atas matras dengan tangan dan kaki membentuk garis lurus.
mis: membengkokkan lutut saat badan terbalik
exp: Meroda adalah gerakan memutar badan ke samping seperti roda dengan bertumpu pada kedua tangan dan kaki secara bergantian. Mulai dari berdiri dengan tangan di atas, letakkan tangan satu per satu di matras, ayunkan kaki melewati atas kepala, lalu mendarat dengan kaki bergantian.
ex: Tangan kanan, tangan kiri, kaki kiri, kaki kanan. // Kaki lurus saat di atas.
pt: Tumpuan tangan dan kaki bergantian ; Kaki lurus di atas ; Lakukan di atas matras
sum: Meroda melatih keseimbangan dan kekuatan lengan.
fig: table Urutan | Gerakan meroda ;; awal | berdiri tangan di atas ;; tumpuan pertama | tangan pertama di matras ;; tumpuan kedua | tangan kedua di matras ;; ayunan | kaki lurus melewati atas ;; pendaratan | kaki bergantian ;; akhir | berdiri tegak ~ Urutan gerakan meroda.
@ Kayang
min: 12
act: Dengan bantuan orang dewasa, latih kayang dari posisi berbaring di atas matras.
mis: melakukan kayang tanpa pemanasan dan tanpa matras
exp: Kayang adalah sikap tubuh melengkung ke belakang seperti busur dengan bertumpu pada kedua tangan dan kaki. Kayang dapat dimulai dari posisi berbaring, telapak tangan di samping telinga, lalu dorong badan ke atas. Kayang melatih kelenturan punggung dan kekuatan lengan.
ex: Kayang dari posisi berbaring. // Perut didorong ke atas.
pt: Tubuh melengkung seperti busur ; Tumpuan tangan dan kaki ; Melatih kelenturan punggung
sum: Kayang melatih kelenturan tubuh.
fig: table Bagian tubuh | Posisi saat kayang ;; telapak tangan | di samping telinga ;; kaki | dibuka selebar bahu ;; perut | didorong ke atas ;; punggung | melengkung ;; kepala | menggantung rileks ;; alas | matras ~ Posisi tubuh saat kayang.
@ Senam ritmik dengan alat
min: 12
act: Buat gerakan senam sederhana dengan pita atau simpai sambil diiringi lagu.
mis: bergerak tidak mengikuti irama musik
exp: Senam ritmik adalah senam yang dilakukan mengikuti irama musik. Senam ritmik dapat memakai alat seperti pita, simpai, bola, gada, atau tali. Gerakannya mengayun, memutar, dan melempar alat dengan indah. Senam ritmik melatih koordinasi dan keluwesan.
ex: Mengayunkan pita membentuk spiral. // Memutar simpai di pinggang.
pt: Mengikuti irama musik ; Memakai pita, simpai, bola ; Melatih keluwesan
sum: Senam ritmik memadukan gerak, alat, dan musik.
fig: table Alat senam ritmik | Gerakan ;; pita | diayun membentuk spiral ;; simpai | diputar di pinggang ;; bola | dilempar dan ditangkap ;; gada | diayun bergantian ;; tali | dilompati ;; selendang | dikibaskan ~ Alat senam ritmik dan gerakannya.
@ Renang gaya dada
min: 12
act: Di kolam dangkal dengan pengawasan, latih gerakan kaki seperti katak sambil berpegangan.
mis: menggerakkan kaki naik turun seperti gaya bebas
exp: Renang gaya dada atau gaya katak dilakukan dengan posisi badan telungkup. Gerakan kaki ditekuk lalu ditendang ke samping dan belakang seperti katak. Gerakan tangan membuka ke samping lalu kembali ke depan dada. Pengambilan napas dilakukan dengan mengangkat kepala ke depan.
ex: Kaki menendang seperti katak. // Napas diambil saat kepala diangkat.
pt: Badan telungkup ; Kaki seperti katak ; Napas dengan mengangkat kepala
sum: Gaya dada mudah dipelajari pemula.
fig: table Gaya renang | Ciri ;; gaya dada | kaki seperti katak ;; gaya bebas | kaki naik turun bergantian ;; gaya punggung | badan telentang ;; gaya kupu-kupu | kedua tangan diayun bersamaan ;; meluncur | dasar sebelum gaya ;; mengapung | badan diam di permukaan air ~ Gaya renang dan cirinya.
@ Latihan daya tahan
min: 12
act: Lari santai atau naik turun tangga selama 10 menit tiga kali seminggu.
mis: berlatih terlalu berat sekali saja lalu berhenti lama
exp: Daya tahan adalah kemampuan tubuh melakukan kegiatan dalam waktu lama tanpa cepat lelah. Daya tahan jantung dan paru dilatih dengan lari santai, bersepeda, berenang, dan lompat tali. Latihan dilakukan secara teratur, bertahap, dan diawali pemanasan.
ex: Lari santai 10 menit setiap pagi. // Bersepeda keliling kompleks.
pt: Daya tahan berarti tidak cepat lelah ; Latihan lari, sepeda, renang ; Teratur dan bertahap
sum: Daya tahan yang baik membuat tubuh bugar.
fig: table Latihan | Unsur kebugaran ;; lari santai | daya tahan jantung ;; push-up | kekuatan lengan ;; lari zig-zag | kelincahan ;; sprint | kecepatan ;; peregangan | kelenturan ;; berdiri satu kaki | keseimbangan ~ Latihan dan unsur kebugaran.
@ Gizi seimbang dan sarapan
min: 12
act: Catat menu sarapanmu selama seminggu, lalu periksa apakah ada karbohidrat, protein, sayur, dan buah.
mis: tidak sarapan karena terburu-buru
exp: Gizi seimbang berarti makan beragam makanan dalam jumlah cukup. Isi Piringku menganjurkan makanan pokok, lauk pauk, sayuran, dan buah. Sarapan memberi tenaga untuk belajar di pagi hari. Minum air putih yang cukup dan batasi gula, garam, serta lemak.
ex: Sarapan nasi, telur, sayur bayam, dan pisang. // Minum air putih delapan gelas sehari.
pt: Makan beragam dan cukup ; Isi Piringku: pokok, lauk, sayur, buah ; Sarapan memberi tenaga
sum: Gizi seimbang membuat kita sehat dan cerdas.
fig: table Zat gizi | Contoh makanan ;; karbohidrat | nasi ;; protein | telur ;; vitamin | jeruk ;; mineral | sayur bayam ;; lemak | alpukat ;; serat | pepaya ~ Zat gizi dan contoh makanannya.
@ Mencegah cedera saat berolahraga
min: 12
act: Periksa sepatu dan pakaian olahragamu sebelum berlatih, lalu lakukan pemanasan.
mis: tetap berolahraga keras saat merasa nyeri
exp: Cedera saat berolahraga bisa dicegah dengan pemanasan, memakai perlengkapan yang sesuai, berlatih bertahap, dan istirahat cukup. Jika terjadi memar atau keseleo, hentikan olahraga, istirahatkan bagian yang sakit, kompres dengan es, dan beri tahu orang dewasa.
ex: Memakai sepatu olahraga yang pas. // Mengompres pergelangan kaki yang keseleo dengan es.
pt: Pemanasan sebelum olahraga ; Perlengkapan sesuai ; Hentikan dan kompres saat cedera
sum: Olahraga yang aman mencegah cedera.
fig: table Cara mencegah | Alasan ;; pemanasan | otot siap ;; sepatu yang pas | kaki tidak lecet ;; latihan bertahap | otot tidak kaget ;; minum cukup | tidak dehidrasi ;; istirahat cukup | otot pulih ;; lapangan aman | tidak tersandung ~ Cara mencegah cedera.
@ Menolak ajakan negatif
min: 12
act: Latih kalimat untuk menolak ajakan merokok atau mencoba zat berbahaya bersama orang tua.
mis: ikut mencoba karena takut dijauhi teman
exp: Anak bisa mendapat ajakan negatif, misalnya merokok, mencoba minuman beralkohol, atau zat berbahaya. Kita berhak menolak dengan tegas dan sopan. Caranya katakan tidak dengan jelas, beri alasan, menjauh dari tempat itu, dan ceritakan kepada orang tua atau guru.
ex: Tidak, terima kasih. Aku ingin tetap sehat. // Segera pergi dan ceritakan kepada guru.
pt: Berhak menolak ; Katakan tidak dengan tegas ; Ceritakan kepada orang dewasa
sum: Menolak ajakan negatif melindungi kesehatan kita.
fig: table Langkah menolak | Contoh ;; katakan tidak | Tidak, terima kasih ;; beri alasan | aku ingin tetap sehat ;; tawarkan kegiatan lain | ayo main bola saja ;; menjauh | pergi dari tempat itu ;; cari teman yang baik | bergaul dengan teman sehat ;; ceritakan | lapor kepada orang tua ~ Langkah menolak ajakan negatif.
"""

BANK += """
## PJOK|Lompat jauh gaya jongkok
Tahapan lompat jauh yang pertama adalah …|awalan|tolakan|melayang|mendarat|Awalan.
Saat melayang pada gaya jongkok, lutut …|ditekuk seperti jongkok|lurus kaku|dibuka lebar|diluruskan ke belakang|Jongkok.
=|Tolakan lompat jauh dilakukan di papan …|tolakan;tumpuan|Papan tolakan.
=|Pendaratan lompat jauh menggunakan … kaki.|dua;kedua|Dua kaki.
B|Awalan lompat jauh berupa lari yang makin cepat.|Makin cepat.
S|Tolakan lompat jauh menggunakan kedua tangan.|Satu kaki.
Tempat mendarat lompat jauh adalah …|bak pasir|kolam|lantai keramik|aspal|Bak pasir.
Jarak lompatan diukur dari papan tolakan sampai bekas …|terdekat|terjauh|tangan|kepala|Terdekat.
## PJOK|Lari jarak menengah
Lari jarak menengah berjarak …|800 sampai 1.500 meter|100 meter|42 km|50 meter|Jarak menengah.
Start pada lari jarak menengah adalah start …|berdiri|jongkok|duduk|berbaring|Berdiri.
=|Lari jarak menengah membutuhkan … tubuh.|daya tahan|Daya tahan.
=|Lari maraton berjarak sekitar … km.|42;42,195|Maraton 42,195 km.
B|Pelari jarak menengah harus mengatur napas.|Atur napas.
S|Pada lari jarak menengah, berlari secepatnya sejak awal adalah strategi terbaik.|Cepat lelah.
Lari dengan rintangan disebut lari …|gawang|estafet|maraton|sprint|Gawang.
Lari 4 × 100 meter disebut lari …|estafet|gawang|maraton|menengah|Estafet.
## PJOK|Menggiring bola dalam sepak bola
Menggiring bola artinya …|membawa bola dengan kaki sambil berlari|menendang bola ke gawang|menangkap bola|melempar bola|Menggiring.
Saat menggiring, bola harus tetap … kaki.|dekat dengan|jauh dari|di atas|di belakang|Dekat.
=|Memainkan bola dengan kepala disebut …|menyundul|Menyundul.
=|Memulai permainan dari pinggir lapangan dengan tangan disebut lemparan ke …|dalam|Lemparan ke dalam.
B|Menggiring bisa memakai kaki bagian luar.|Bagian luar.
S|Saat menggiring, bola ditendang sejauh mungkin.|Didorong pelan.
Saat menggiring, pandangan sesekali ke …|depan|langit|penonton|belakang|Depan.
Teknik untuk menguasai bola yang datang disebut …|menghentikan bola|menyundul|lemparan ke dalam|menendang|Menghentikan.
## PJOK|Passing atas bola voli
Passing atas dilakukan dengan …|jari-jari kedua tangan|lengan bawah|kepala|kaki|Jari-jari.
Saat passing atas, bola dimainkan di atas …|dahi|perut|lutut|pinggang|Dahi.
=|Passing atas biasanya dipakai untuk … bola.|mengumpan|Mengumpan.
=|Pukulan keras ke daerah lawan disebut …|smash|Smash.
B|Saat passing atas, jari membentuk seperti mangkuk.|Mangkuk.
S|Passing atas dilakukan dengan kepalan tangan.|Jari-jari.
Teknik untuk menahan smash lawan di depan net disebut …|blok|servis|passing bawah|lay-up|Blok.
Teknik untuk memulai permainan bola voli adalah …|servis|smash|blok|passing atas|Servis.
## PJOK|Menembak bola basket
Memasukkan bola ke ring disebut …|shooting|dribbling|passing|blocking|Shooting.
Tembakan sambil melangkah dua kali disebut …|lay-up|free throw|dribble|pivot|Lay-up.
=|Tembakan hukuman dalam bola basket disebut free …|throw|Free throw.
=|Keranjang bola basket disebut …|ring|Ring.
B|Saat menembak, lutut ditekuk lalu diluruskan.|Dorongan lutut.
S|Saat menembak, pandangan ke arah penonton.|Ke ring.
Menggiring bola basket disebut …|dribbling|shooting|passing|lay-up|Dribbling.
Saat shooting, tangan terkuat berada di … bola.|bawah|atas|depan|tidak memegang|Di bawah bola.
## PJOK|Permainan rounders
Rounders dimainkan oleh … regu.|dua|satu|tiga|empat|Dua regu.
Regu yang memukul bola disebut regu …|pemukul|penjaga|pelambung|wasit|Pemukul.
=|Pemain yang melempar bola kepada pemukul disebut …|pelambung|Pelambung.
=|Tempat pelari berhenti dalam rounders disebut tiang …|hinggap|Tiang hinggap.
B|Rounders mirip dengan permainan kasti.|Mirip kasti.
S|Dalam rounders, pemukul berlari sebelum memukul bola.|Pukul dulu.
Regu penjaga berusaha …|menangkap bola dan mematikan pelari|memukul bola|menendang bola|menembak ring|Penjaga.
Rounders melatih kemampuan memukul, berlari, dan …|menangkap|berenang|menyundul|mendribel|Menangkap.
## PJOK|Gerak dasar pencak silat
Pencak silat adalah bela diri asli …|Indonesia|Jepang|Cina|Korea|Indonesia.
Posisi kaki yang kokoh dalam silat disebut …|kuda-kuda|sikap pasang|tangkisan|elakan|Kuda-kuda.
=|Gerakan menahan serangan disebut …|tangkisan|Tangkisan.
=|Gerakan menghindari serangan disebut …|elakan|Elakan.
B|Pencak silat melatih disiplin.|Disiplin.
S|Gerakan silat boleh dipakai untuk memukul teman bercanda.|Tidak boleh.
Sikap siap bertahan dan menyerang disebut …|sikap pasang|kuda-kuda|elakan|tendangan|Sikap pasang.
Serangan dengan kaki dalam silat disebut …|tendangan|pukulan|tangkisan|elakan|Tendangan.
## PJOK|Lompat tinggi gaya gunting
Awalan lompat tinggi gaya gunting dilakukan dari … mistar.|samping|depan lurus|belakang|bawah|Samping.
Saat melewati mistar, kaki digerakkan seperti …|gunting|katak|kupu-kupu|bebek|Gunting.
=|Tolakan lompat tinggi memakai … kaki.|satu|Satu kaki.
=|Palang yang dilompati dalam lompat tinggi disebut …|mistar|Mistar.
B|Pendaratan lompat tinggi sebaiknya di matras.|Matras.
S|Tolakan lompat tinggi gaya gunting memakai dua kaki bersamaan.|Satu kaki.
Kaki tolakan pada gaya gunting adalah kaki yang … dari mistar.|terjauh|terdekat|di atas|tidak ada|Terjauh.
Lompat tinggi melatih kekuatan …|tungkai|telinga|jari|leher|Tungkai.
## PJOK|Meroda
Meroda adalah gerakan memutar badan ke …|samping|depan|belakang|atas|Samping.
Saat meroda, tumpuan dilakukan oleh tangan dan kaki secara …|bergantian|bersamaan|tidak ada|sekali|Bergantian.
=|Saat badan terbalik, kaki dalam keadaan …|lurus|Lurus.
=|Meroda dilakukan di atas …|matras|Matras.
B|Meroda melatih kekuatan lengan.|Lengan.
S|Saat meroda, lutut ditekuk sebanyak mungkin.|Kaki lurus.
Posisi awal meroda adalah berdiri dengan tangan …|di atas|di saku|di belakang|di pinggang|Di atas.
Meroda menirukan gerakan …|roda berputar|katak melompat|ikan berenang|burung terbang|Roda.
## PJOK|Kayang
Kayang adalah sikap tubuh melengkung ke …|belakang|depan|samping|bawah|Belakang.
Tumpuan saat kayang adalah …|kedua tangan dan kaki|kepala saja|perut|satu tangan|Tangan dan kaki.
=|Saat kayang, tubuh melengkung seperti …|busur;jembatan|Busur.
=|Kayang melatih kelenturan …|punggung|Punggung.
B|Kayang perlu pemanasan sebelum dilakukan.|Pemanasan.
S|Kayang aman dilakukan tanpa matras di lantai keras.|Pakai matras.
Saat kayang, perut didorong ke …|atas|bawah|samping|depan|Atas.
Saat memulai kayang dari berbaring, telapak tangan diletakkan di samping …|telinga|pinggang|lutut|kaki|Telinga.
## PJOK|Senam ritmik dengan alat
Senam ritmik dilakukan mengikuti …|irama musik|aba-aba lari|peluit wasit|bel sekolah|Irama.
Alat senam ritmik yang diputar di pinggang adalah …|simpai|pita|gada|bola|Simpai.
=|Alat senam ritmik yang diayun membentuk spiral adalah …|pita|Pita.
=|Senam ritmik melatih koordinasi dan …|keluwesan|Keluwesan.
B|Bola dapat dipakai dalam senam ritmik.|Bola.
S|Senam ritmik dilakukan tanpa memperhatikan musik.|Mengikuti irama.
Alat senam ritmik yang berbentuk seperti botol dan diayun disebut …|gada|pita|simpai|tali|Gada.
Gerakan dengan tali dalam senam ritmik biasanya …|melompati tali|menarik tali tambang|mengikat tali|melempar tali jauh|Melompati.
## PJOK|Renang gaya dada
Renang gaya dada disebut juga gaya …|katak|bebas|punggung|kupu-kupu|Gaya katak.
Posisi badan saat gaya dada adalah …|telungkup|telentang|miring|tegak|Telungkup.
=|Renang dengan badan telentang disebut gaya …|punggung|Gaya punggung.
=|Saat gaya dada, napas diambil dengan mengangkat … ke depan.|kepala|Kepala.
B|Gerakan kaki gaya dada seperti katak.|Seperti katak.
S|Gerakan kaki gaya dada naik turun bergantian.|Itu gaya bebas.
Gaya renang yang kedua tangannya diayun bersamaan di atas air adalah …|gaya kupu-kupu|gaya dada|gaya punggung|gaya bebas|Kupu-kupu.
Berenang harus selalu didampingi …|orang dewasa atau pelatih|adik kecil|hewan peliharaan|tidak siapa pun|Pengawasan.
## PJOK|Latihan daya tahan
Daya tahan adalah kemampuan tubuh beraktivitas lama tanpa …|cepat lelah|bernapas|bergerak|makan|Tidak cepat lelah.
Contoh latihan daya tahan adalah …|lari santai|push-up sekali|berdiri diam|tidur|Lari santai.
=|Latihan daya tahan dilakukan secara teratur dan …|bertahap|Bertahap.
=|Latihan peregangan melatih unsur …|kelenturan|Kelenturan.
B|Bersepeda dapat melatih daya tahan jantung.|Sepeda.
S|Latihan sangat berat sekali sebulan lebih baik dari latihan teratur.|Teratur lebih baik.
Latihan push-up melatih unsur kebugaran …|kekuatan lengan|kelincahan|kelenturan|keseimbangan|Kekuatan.
Sebelum latihan daya tahan kita melakukan …|pemanasan|tidur|makan banyak|pendinginan dulu|Pemanasan.
## PJOK|Gizi seimbang dan sarapan
Panduan makan seimbang di Indonesia disebut Isi …|Piringku|Gelasku|Sendokku|Mangkukku|Isi Piringku.
Zat gizi utama dalam nasi adalah …|karbohidrat|protein|vitamin C|lemak|Karbohidrat.
=|Telur banyak mengandung zat gizi …|protein|Protein.
=|Makan di pagi hari sebelum beraktivitas disebut …|sarapan|Sarapan.
B|Sarapan memberi tenaga untuk belajar.|Tenaga.
S|Melewatkan sarapan membuat kita lebih fokus belajar.|Kurang tenaga.
Yang perlu dibatasi dalam makanan adalah …|gula, garam, dan lemak|sayur|buah|air putih|Batasi.
Buah jeruk banyak mengandung …|vitamin C|lemak|karbohidrat utama|garam|Vitamin C.
## PJOK|Mencegah cedera saat berolahraga
Cara mencegah cedera saat olahraga adalah …|melakukan pemanasan|tidak memakai sepatu|langsung berlatih berat|bermain di lantai licin|Pemanasan.
Pergelangan kaki yang keseleo sebaiknya dikompres dengan …|es|air panas|minyak goreng|pasir|Es.
=|Saat terjadi cedera, olahraga harus …|dihentikan|Dihentikan.
=|Minum cukup air mencegah …|dehidrasi|Dehidrasi.
B|Sepatu yang pas mencegah kaki lecet.|Sepatu pas.
S|Saat merasa nyeri, olahraga harus diteruskan lebih keras.|Dihentikan.
Latihan sebaiknya dilakukan secara …|bertahap|mendadak berat|tanpa istirahat|tanpa pemanasan|Bertahap.
Jika teman cedera saat olahraga, kita segera …|memberi tahu guru atau orang dewasa|menertawakannya|meninggalkannya|menyuruhnya terus bermain|Memberi tahu.
## PJOK|Menolak ajakan negatif
Jika diajak merokok oleh teman, sikap kita adalah …|menolak dengan tegas|ikut mencoba sekali|menerima supaya tidak dijauhi|diam saja|Menolak.
Kalimat menolak yang baik adalah …|Tidak, terima kasih. Aku ingin tetap sehat.|Boleh, sekali saja.|Nanti aku coba.|Terserah kamu.|Menolak tegas.
=|Ajakan negatif sebaiknya diceritakan kepada orang tua atau …|guru|Guru.
=|Setelah menolak, kita sebaiknya … dari tempat itu.|menjauh;pergi|Menjauh.
B|Kita berhak menolak ajakan yang membahayakan diri.|Berhak menolak.
S|Mencoba rokok sekali tidak berbahaya bagi anak.|Berbahaya.
Cara menolak dengan menawarkan kegiatan lain adalah …|Ayo kita main bola saja.|Ayo kita coba.|Aku ikut saja.|Kamu duluan.|Kegiatan lain.
Teman yang baik adalah teman yang mengajak …|hidup sehat|merokok|membolos|berkelahi|Hidup sehat.
"""

SAS += """
## PJOK 1
0|Tahapan lompat jauh setelah tolakan adalah ....|melayang|awalan|lari|pemanasan|Melayang.
1|Lari jarak jauh berjarak lebih dari ....|3.000 meter|100 meter|400 meter|800 meter|Jarak jauh.
2|Teknik sepak bola untuk mencetak gol adalah ....|menendang ke gawang|menggiring|menghentikan|lemparan ke dalam|Menendang ke gawang.
3|Teknik bola voli untuk menerima bola rendah adalah ....|passing bawah|passing atas|smash|blok|Passing bawah.
4|Istilah untuk mengoper bola dalam bola basket adalah ....|passing|shooting|dribbling|lay-up|Passing.
5|Pemain rounders yang berdiri di belakang pemukul disebut ....|penjaga belakang|pelambung|pelari|pemukul|Penjaga belakang.
6|Gerakan menyerang dengan tangan dalam pencak silat disebut ....|pukulan|tendangan|elakan|kuda-kuda|Pukulan.
7|Pada lompat tinggi gaya gunting, pendaratan menggunakan ....|kaki yang pertama melewati mistar|kedua tangan|punggung|kepala|Kaki pertama.
## PJOK 2
0|Posisi akhir gerakan meroda adalah ....|berdiri tegak|berbaring|jongkok|duduk|Berdiri tegak.
1|Saat kayang, kaki dibuka selebar ....|bahu|lapangan|jengkal|kepala|Bahu.
2|Selendang dalam senam ritmik digerakkan dengan cara ....|dikibaskan|dilempar jauh|diikat|dilipat|Dikibaskan.
3|Gaya renang dengan kaki naik turun bergantian adalah gaya ....|bebas|dada|katak|kupu-kupu tangan|Gaya bebas.
4|Lari zig-zag melatih unsur kebugaran ....|kelincahan|kekuatan|kelenturan|daya tahan otot perut|Kelincahan.
5|Pepaya baik dimakan karena mengandung banyak ....|serat|lemak|garam|gula|Serat.
6|Supaya otot pulih setelah berlatih, kita perlu ....|istirahat cukup|begadang|berlatih tanpa henti|tidak minum|Istirahat.
7|Langkah menolak ajakan negatif yang terakhir adalah ....|menceritakan kepada orang tua|ikut mencoba|merahasiakan|membalas ajakan|Lapor.
"""

TOPICS += """
## KKA
# 1|Berpikir Komputasional dan Komputer
@ Abstraksi
min: 12
act: Gambar denah rute dari rumah ke sekolah hanya dengan jalan dan belokan penting.
mis: memasukkan semua detail yang tidak penting
exp: Abstraksi adalah memilih informasi yang penting dan mengabaikan detail yang tidak diperlukan. Contohnya peta kereta hanya menunjukkan stasiun dan jalur, tidak menunjukkan rumah dan pohon. Abstraksi membuat masalah lebih mudah dipahami dan diselesaikan.
ex: Peta rute bus hanya berisi halte. // Ikon toilet hanya menampilkan bentuk orang sederhana.
pt: Pilih informasi penting ; Abaikan detail yang tidak perlu ; Masalah jadi lebih sederhana
sum: Abstraksi menyederhanakan masalah.
fig: table Contoh | Informasi penting ;; peta kereta | stasiun dan jalur ;; resep kue | bahan dan langkah ;; ikon toilet | bentuk orang sederhana ;; denah sekolah | letak ruangan ;; jadwal pelajaran | hari dan mata pelajaran ;; rambu lalu lintas | gambar dan warna ~ Contoh abstraksi.
@ Diagram alir
min: 12
act: Buat diagram alir langkah menyikat gigi dengan bentuk oval, persegi, dan belah ketupat.
mis: memakai simbol persegi untuk pertanyaan ya atau tidak
exp: Diagram alir atau flowchart adalah gambar langkah-langkah algoritma dengan simbol tertentu. Oval untuk mulai dan selesai, persegi panjang untuk proses, belah ketupat untuk keputusan atau pertanyaan, dan anak panah untuk arah alur.
ex: Mulai → ambil sikat → apakah ada pasta gigi? → ya: sikat gigi → selesai. // Belah ketupat berisi pertanyaan ya atau tidak.
pt: Oval mulai dan selesai ; Persegi panjang proses ; Belah ketupat keputusan
sum: Diagram alir menggambarkan algoritma dengan simbol.
fig: table Simbol | Arti ;; oval | mulai atau selesai ;; persegi panjang | proses ;; belah ketupat | keputusan ;; jajargenjang | masukan atau keluaran ;; anak panah | arah alur ;; lingkaran kecil | penghubung ~ Simbol diagram alir.
@ Bagian-bagian komputer
min: 12
act: Tunjukkan bagian komputer atau laptop di rumah dan sebutkan fungsinya.
mis: mengira monitor adalah tempat menyimpan data
exp: Komputer terdiri atas perangkat keras dan perangkat lunak. Perangkat keras dapat disentuh, misalnya monitor, keyboard, mouse, CPU, dan printer. Perangkat lunak adalah program, misalnya sistem operasi dan aplikasi. Keduanya bekerja sama supaya komputer berfungsi.
ex: Keyboard untuk mengetik huruf. // Printer untuk mencetak dokumen.
pt: Perangkat keras dapat disentuh ; Perangkat lunak berupa program ; Bekerja sama
sum: Komputer bekerja dengan perangkat keras dan lunak.
fig: table Perangkat | Fungsi ;; monitor | menampilkan gambar ;; keyboard | mengetik ;; mouse | menggerakkan penunjuk ;; CPU | memproses data ;; printer | mencetak ;; speaker | mengeluarkan suara ~ Bagian komputer dan fungsinya.
@ Input, proses, dan output
min: 12
act: Amati kalkulator: tombol yang ditekan, perhitungan, dan hasil di layar.
mis: mengira layar adalah alat input
exp: Komputer bekerja dengan alur input, proses, dan output. Input adalah data yang dimasukkan, misalnya lewat keyboard atau mikrofon. Proses adalah pengolahan data oleh CPU. Output adalah hasil yang ditampilkan, misalnya di layar, printer, atau speaker. Data juga bisa disimpan di media penyimpanan.
ex: Mengetik angka di kalkulator adalah input. // Hasil di layar adalah output.
pt: Input memasukkan data ; Proses mengolah data ; Output menampilkan hasil
sum: Komputer mengubah input menjadi output.
fig: table Perangkat | Jenis ;; keyboard | input ;; mikrofon | input suara ;; CPU | proses ;; monitor | output ;; printer | output cetak ;; flashdisk | penyimpanan ~ Perangkat input, proses, output.
@ Pemrograman blok
min: 12
act: Coba aplikasi pemrograman blok untuk menggerakkan tokoh ke depan, belok, dan melompat.
mis: menyusun blok tanpa memperhatikan urutan
exp: Pemrograman blok adalah cara membuat program dengan menyusun blok-blok perintah seperti puzzle. Setiap blok berisi satu perintah, misalnya maju, belok kanan, atau ulangi. Blok disusun berurutan dari atas ke bawah. Contoh aplikasinya Scratch dan Blockly.
ex: Blok maju 10 langkah lalu belok kanan. // Blok ulangi 4 kali untuk membuat persegi.
pt: Program dari blok perintah ; Disusun berurutan ; Contoh Scratch
sum: Pemrograman blok memudahkan belajar koding.
fig: table Blok | Perintah ;; maju | bergerak ke depan ;; belok kanan | berputar ke kanan ;; belok kiri | berputar ke kiri ;; ulangi | melakukan berulang ;; jika | memeriksa syarat ;; tunggu | berhenti sejenak ~ Contoh blok perintah.
@ Debugging
min: 12
act: Tulis langkah membuat teh, lalu minta keluarga mencari langkah yang salah atau hilang.
mis: langsung menyerah ketika program tidak berjalan
exp: Bug adalah kesalahan dalam program atau algoritma. Debugging adalah proses mencari dan memperbaiki kesalahan itu. Caranya jalankan program, amati hasilnya, bandingkan dengan yang diharapkan, temukan langkah yang salah, perbaiki, lalu uji lagi.
ex: Robot berbelok kiri padahal seharusnya kanan, maka perintahnya diperbaiki. // Langkah menuang air terlupa, maka ditambahkan.
pt: Bug adalah kesalahan ; Debugging mencari dan memperbaiki ; Uji lagi setelah diperbaiki
sum: Debugging membuat program berjalan benar.
fig: table Langkah debugging | Kegiatan ;; pertama | jalankan program ;; kedua | amati hasilnya ;; ketiga | bandingkan dengan harapan ;; keempat | temukan kesalahan ;; kelima | perbaiki perintah ;; keenam | uji lagi ~ Langkah debugging.
@ Bilangan biner
min: 12
act: Nyalakan dan matikan lampu senter untuk menunjukkan angka 1 dan 0.
mis: mengira komputer menyimpan angka seperti manusia menulis
exp: Komputer menyimpan data dengan bilangan biner, yaitu hanya angka 0 dan 1. Angka 1 seperti saklar menyala, angka 0 seperti saklar mati. Satu angka biner disebut bit, dan delapan bit disebut satu byte. Dengan susunan 0 dan 1, komputer dapat menyimpan huruf, gambar, dan suara.
ex: Bilangan 2 dalam biner adalah 10. // Bilangan 5 dalam biner adalah 101.
pt: Biner hanya 0 dan 1 ; Satu angka disebut bit ; 8 bit = 1 byte
sum: Komputer bekerja dengan bilangan biner.
fig: table Desimal | Biner ;; 0 | 0 ;; 1 | 1 ;; 2 | 10 ;; 3 | 11 ;; 4 | 100 ;; 5 | 101 ~ Bilangan desimal dan biner.
@ Jaringan internet
min: 12
act: Tanyakan kepada orang tua bagaimana ponsel di rumah terhubung ke internet.
mis: mengira internet hanya ada di satu komputer
exp: Jaringan komputer adalah beberapa komputer yang saling terhubung untuk berbagi data. Internet adalah jaringan raksasa yang menghubungkan komputer di seluruh dunia. Perangkat terhubung ke internet lewat kabel, Wi-Fi, atau jaringan seluler. Situs web disimpan di komputer khusus yang disebut server.
ex: Ponsel terhubung internet lewat Wi-Fi. // Video yang kita tonton dikirim dari server.
pt: Jaringan menghubungkan komputer ; Internet jaringan seluruh dunia ; Terhubung lewat kabel, Wi-Fi, seluler
sum: Internet menghubungkan komputer di seluruh dunia.
fig: table Istilah | Arti ;; internet | jaringan seluruh dunia ;; Wi-Fi | koneksi tanpa kabel ;; server | komputer penyimpan situs ;; router | pembagi sinyal jaringan ;; peramban | aplikasi membuka situs ;; situs web | halaman informasi di internet ~ Istilah jaringan internet.
# 2|Data, KA, dan Keamanan Digital
@ Data dan informasi
min: 12
act: Catat suhu udara setiap pagi selama seminggu, lalu simpulkan hari terpanas.
mis: mengira data dan informasi adalah hal yang sama
exp: Data adalah fakta mentah berupa angka, huruf, gambar, atau suara yang belum diolah. Informasi adalah data yang sudah diolah sehingga bermakna. Contohnya catatan nilai ulangan adalah data, sedangkan rata-rata kelas adalah informasi.
ex: Data: suhu 28, 30, 31 derajat. // Informasi: hari Rabu paling panas.
pt: Data fakta mentah ; Informasi data yang diolah ; Informasi membantu mengambil keputusan
sum: Data diolah menjadi informasi.
fig: table Data | Informasi ;; daftar nilai ulangan | rata-rata kelas ;; catatan suhu harian | hari terpanas ;; daftar buah kesukaan | buah paling disukai ;; catatan tinggi badan | siswa tertinggi ;; data pengunjung perpustakaan | hari paling ramai ;; struk belanja | total pengeluaran ~ Data dan informasi.
@ Mengelompokkan data
min: 12
act: Kelompokkan mainan di rumah berdasarkan warna, ukuran, atau jenis.
mis: mengelompokkan tanpa aturan yang jelas
exp: Mengelompokkan data berarti memisahkan data berdasarkan ciri yang sama. Ciri pengelompokan misalnya warna, bentuk, ukuran, atau jenis. Data yang dikelompokkan lebih mudah dicari dan dianalisis. Komputer juga mengelompokkan data, misalnya foto berdasarkan tanggal.
ex: Buah dikelompokkan berdasarkan warna. // Buku dikelompokkan berdasarkan pelajaran.
pt: Kelompokkan berdasarkan ciri sama ; Pilih aturan yang jelas ; Data lebih mudah dicari
sum: Pengelompokan membuat data teratur.
fig: table Benda | Kelompok ;; apel | buah merah ;; pisang | buah kuning ;; bayam | sayur hijau ;; wortel | sayur jingga ;; ayam | lauk hewani ;; tahu | lauk nabati ~ Mengelompokkan bahan makanan.
@ Contoh KA di sekitar kita
min: 12
act: Cari tiga aplikasi di ponsel keluarga yang memakai kecerdasan artifisial.
mis: mengira kecerdasan artifisial adalah robot berbentuk manusia saja
exp: Kecerdasan artifisial atau KA adalah kemampuan mesin meniru cara berpikir manusia. KA ada di sekitar kita, misalnya asisten suara, penerjemah otomatis, rekomendasi video, pengenal wajah untuk membuka ponsel, dan peta yang menyarankan rute tercepat.
ex: Asisten suara menjawab pertanyaan. // Penerjemah mengubah bahasa Inggris ke Indonesia.
pt: KA meniru cara berpikir manusia ; Ada di banyak aplikasi ; Tidak selalu berbentuk robot
sum: KA sudah banyak membantu kehidupan sehari-hari.
fig: table Aplikasi KA | Kegunaan ;; asisten suara | menjawab pertanyaan ;; penerjemah otomatis | mengubah bahasa ;; rekomendasi video | menyarankan tontonan ;; pengenal wajah | membuka kunci ponsel ;; peta digital | menyarankan rute ;; penyaring spam | memilah surel sampah ~ Contoh KA di sekitar kita.
@ Pengenalan gambar oleh KA
min: 12
act: Coba fitur pencarian gambar di ponsel bersama orang tua, lalu lihat hasil tebakannya.
mis: mengira KA selalu benar mengenali gambar
exp: KA dapat mengenali gambar setelah belajar dari banyak contoh gambar yang sudah diberi label. Misalnya KA melihat ribuan foto kucing berlabel kucing sehingga bisa mengenali kucing baru. KA bisa salah jika contoh yang dipelajari sedikit atau tidak beragam.
ex: Aplikasi mengenali jenis bunga dari foto. // KA bisa salah menebak anjing berbulu mirip kucing.
pt: KA belajar dari contoh berlabel ; Makin banyak contoh makin pintar ; KA bisa salah
sum: KA mengenali gambar dari pola yang dipelajari.
fig: table Istilah | Arti ;; data latih | contoh untuk belajar ;; label | nama pada contoh ;; pola | ciri yang dikenali ;; prediksi | tebakan KA ;; akurasi | seberapa sering benar ;; data uji | contoh untuk menguji ~ Istilah pengenalan gambar.
@ Kata sandi yang kuat
min: 12
act: Bersama orang tua, periksa apakah kata sandi akun keluarga sudah cukup kuat.
mis: memakai tanggal lahir sebagai kata sandi
exp: Kata sandi melindungi akun dari orang lain. Kata sandi yang kuat panjangnya minimal 8 karakter dan mencampur huruf besar, huruf kecil, angka, dan simbol. Jangan memakai nama, tanggal lahir, atau 123456. Jangan memberitahukan kata sandi kepada orang lain kecuali orang tua.
ex: Kata sandi lemah: 123456. // Kata sandi kuat: Kucing#Hijau72.
pt: Minimal 8 karakter ; Campur huruf, angka, simbol ; Rahasiakan kata sandi
sum: Kata sandi kuat menjaga akun tetap aman.
fig: table Kata sandi | Kekuatan ;; 123456 | sangat lemah ;; budi2012 | lemah karena nama dan tahun ;; password | sangat mudah ditebak ;; Kucing#Hijau72 | kuat ;; Matahari!Pagi9 | kuat dan panjang ;; qwerty | lemah karena urutan keyboard ~ Contoh kekuatan kata sandi.
@ Sopan santun di internet
min: 12
act: Baca komentar di sebuah video anak bersama orang tua, lalu pilih komentar yang sopan.
mis: menulis komentar kasar karena merasa tidak dikenali
exp: Sopan santun di internet disebut netiket. Kita menulis dengan bahasa yang sopan, tidak menghina, tidak menyebarkan hal pribadi orang lain, dan menghargai pendapat berbeda. Pesan dengan huruf kapital semua bisa dianggap berteriak. Ingat bahwa di balik layar ada manusia.
ex: Menulis Terima kasih, videonya bermanfaat. // Tidak mengejek foto teman di grup.
pt: Gunakan bahasa sopan ; Jangan menghina atau menyebarkan data pribadi ; Huruf kapital semua seperti berteriak
sum: Netiket membuat internet nyaman untuk semua.
fig: table Perilaku | Sopan atau tidak ;; memberi komentar membangun | sopan ;; mengejek foto teman | tidak sopan ;; menulis huruf kapital semua | dianggap berteriak ;; mengucapkan terima kasih | sopan dan ramah ;; menyebarkan nomor telepon orang | melanggar privasi ;; menghargai pendapat berbeda | sopan dan dewasa ~ Netiket di internet.
@ Mengenali berita bohong
min: 12
act: Pilih satu berita yang beredar di grup keluarga, lalu periksa sumbernya bersama orang tua.
mis: langsung membagikan berita karena judulnya mengejutkan
exp: Berita bohong atau hoaks adalah informasi palsu yang sengaja disebarkan. Ciri hoaks antara lain judulnya berlebihan, tidak ada sumber jelas, meminta segera disebarkan, dan isinya membuat panik. Sebelum membagikan, periksa sumber, bandingkan dengan media terpercaya, dan tanyakan kepada orang dewasa.
ex: Pesan berantai Sebarkan segera! patut dicurigai. // Cek kebenaran di situs resmi.
pt: Hoaks informasi palsu ; Cek sumber dan bandingkan ; Jangan langsung membagikan
sum: Saring sebelum sharing.
fig: table Ciri | Keterangan ;; judul berlebihan | memancing emosi ;; tanpa sumber | tidak jelas asalnya ;; minta disebarkan | ada kata sebarkan segera ;; membuat panik | menakut-nakuti ;; foto lama | dipakai untuk kejadian baru ;; banyak salah ketik | tidak ditulis rapi ~ Ciri-ciri berita bohong.
@ Mengatur waktu layar
min: 12
act: Buat jadwal waktu layar harian bersama orang tua dan tempel di dinding.
mis: bermain gawai sampai larut malam
exp: Waktu layar adalah lamanya kita memakai gawai seperti ponsel, tablet, televisi, dan komputer. Terlalu lama di depan layar dapat membuat mata lelah, kurang tidur, dan kurang bergerak. Atur waktu layar bersama orang tua, istirahatkan mata setiap 20 menit, dan matikan gawai sebelum tidur.
ex: Aturan 20-20-20: setiap 20 menit lihat benda sejauh 6 meter selama 20 detik. // Gawai dimatikan satu jam sebelum tidur.
pt: Batasi waktu layar ; Istirahatkan mata ; Matikan gawai sebelum tidur
sum: Waktu layar yang seimbang menjaga kesehatan.
fig: table Kebiasaan | Akibat ;; bermain gawai sampai larut | kurang tidur ;; menatap layar terus | mata lelah ;; duduk terlalu lama | kurang bergerak ;; istirahat tiap 20 menit | mata segar ;; bermain di luar | badan sehat ;; matikan gawai sebelum tidur | tidur nyenyak ~ Kebiasaan waktu layar dan akibatnya.
"""

BANK += """
## KKA|Abstraksi
Abstraksi artinya …|memilih informasi penting dan mengabaikan detail|menulis semua detail|menghapus semua data|menggambar secara rinci|Abstraksi.
Peta jalur kereta hanya menampilkan stasiun dan jalur. Ini contoh …|abstraksi|dekomposisi|debugging|enkripsi|Abstraksi.
=|Abstraksi membuat masalah lebih …|sederhana;mudah|Sederhana.
=|Detail yang tidak penting dalam abstraksi sebaiknya …|diabaikan|Diabaikan.
B|Ikon toilet adalah contoh abstraksi.|Bentuk sederhana.
S|Abstraksi berarti memasukkan semua detail sekecil apa pun.|Mengabaikan detail.
Informasi penting dalam resep kue adalah …|bahan dan langkah|warna piring|nama tetangga|cuaca hari itu|Bahan dan langkah.
Pada denah sekolah, informasi penting adalah …|letak ruangan|warna cat dinding|jumlah daun pohon|merek kursi|Letak ruangan.
## KKA|Diagram alir
Simbol diagram alir untuk mulai dan selesai adalah …|oval|persegi panjang|belah ketupat|jajargenjang|Oval.
Simbol diagram alir untuk keputusan adalah …|belah ketupat|oval|persegi panjang|lingkaran|Belah ketupat.
=|Simbol diagram alir untuk proses adalah persegi …|panjang|Persegi panjang.
=|Arah alur dalam diagram alir ditunjukkan oleh anak …|panah|Anak panah.
B|Belah ketupat berisi pertanyaan ya atau tidak.|Keputusan.
S|Oval dipakai untuk menuliskan proses.|Untuk mulai dan selesai.
Simbol untuk masukan atau keluaran adalah …|jajargenjang|oval|belah ketupat|segitiga|Jajargenjang.
Nama lain diagram alir adalah …|flowchart|spreadsheet|desktop|browser|Flowchart.
## KKA|Bagian-bagian komputer
Bagian komputer yang menampilkan gambar adalah …|monitor|keyboard|mouse|CPU|Monitor.
Bagian komputer yang dipakai untuk mengetik adalah …|keyboard|printer|speaker|monitor|Keyboard.
=|Perangkat untuk mencetak dokumen adalah …|printer|Printer.
=|Perangkat komputer yang dapat disentuh disebut perangkat …|keras|Perangkat keras.
B|Sistem operasi termasuk perangkat lunak.|Perangkat lunak.
S|Mouse dipakai untuk mencetak dokumen.|Menggerakkan penunjuk.
Bagian komputer yang memproses data adalah …|CPU|monitor|speaker|keyboard|CPU.
Bagian komputer yang mengeluarkan suara adalah …|speaker|mouse|printer|keyboard|Speaker.
## KKA|Input, proses, dan output
Keyboard termasuk perangkat …|input|output|proses|penyimpanan|Input.
Monitor termasuk perangkat …|output|input|proses|penyimpanan|Output.
=|Bagian komputer yang melakukan proses adalah …|CPU|CPU.
=|Mikrofon termasuk perangkat …|input|Input suara.
B|Printer termasuk perangkat output.|Output cetak.
S|Monitor termasuk perangkat input.|Monitor output.
Flashdisk berfungsi sebagai …|media penyimpanan|alat input|alat output|pemroses|Penyimpanan.
Hasil hitungan yang tampil di layar kalkulator disebut …|output|input|proses|kabel|Output.
## KKA|Pemrograman blok
Pemrograman blok disusun seperti …|puzzle|lukisan|lagu|surat|Puzzle.
Contoh aplikasi pemrograman blok adalah …|Scratch|kalkulator|kamera|peta|Scratch.
=|Blok untuk melakukan perintah berulang adalah blok …|ulangi|Ulangi.
=|Blok untuk memeriksa syarat adalah blok …|jika|Jika.
B|Blok-blok perintah disusun berurutan.|Berurutan.
S|Urutan blok tidak memengaruhi hasil program.|Sangat memengaruhi.
Untuk membuat persegi, tokoh perlu maju lalu belok kanan sebanyak … kali.|4|2|3|6|Empat sisi.
Blok tunggu dipakai untuk …|berhenti sejenak|maju|belok kanan|mengulang|Berhenti sejenak.
## KKA|Debugging
Kesalahan dalam program disebut …|bug|blok|byte|bit|Bug.
Proses mencari dan memperbaiki kesalahan disebut …|debugging|coding|browsing|typing|Debugging.
=|Setelah memperbaiki kesalahan, program harus di … lagi.|uji|Diuji.
=|Langkah pertama debugging adalah … program.|jalankan;menjalankan|Jalankan.
B|Debugging dilakukan dengan membandingkan hasil dan harapan.|Bandingkan.
S|Jika program salah, sebaiknya langsung menyerah.|Cari kesalahannya.
Robot belok kiri padahal seharusnya kanan. Yang perlu dilakukan adalah …|memperbaiki perintah belok|membuang robot|menambah baterai|mematikan komputer|Perbaiki perintah.
Langkah membuat teh tanpa menuang air adalah contoh …|bug|output|input|data|Ada kesalahan.
## KKA|Bilangan biner
Bilangan biner hanya terdiri atas angka …|0 dan 1|1 dan 2|0 sampai 9|1 sampai 10|0 dan 1.
Bilangan 3 dalam biner adalah …|11|3|10|111|3 = 11.
=|Satu angka biner disebut …|bit|Bit.
=|Delapan bit sama dengan satu …|byte|Byte.
B|Bilangan 2 dalam biner adalah 10.|Benar.
S|Bilangan 4 dalam biner adalah 4.|100.
Angka 1 dalam biner dapat diibaratkan saklar yang …|menyala|mati|rusak|hilang|Menyala.
Bilangan biner 101 sama dengan bilangan desimal …|5|101|3|10|4 + 1.
## KKA|Jaringan internet
Jaringan komputer di seluruh dunia disebut …|internet|intranet|bluetooth|kabel data|Internet.
Koneksi internet tanpa kabel disebut …|Wi-Fi|flashdisk|printer|keyboard|Wi-Fi.
=|Komputer khusus penyimpan situs web disebut …|server|Server.
=|Aplikasi untuk membuka situs web disebut …|peramban;browser|Peramban.
B|Ponsel dapat terhubung ke internet lewat jaringan seluler.|Seluler.
S|Internet hanya dapat dipakai di satu komputer.|Seluruh dunia.
Alat yang membagi sinyal jaringan di rumah adalah …|router|printer|monitor|speaker|Router.
Kumpulan halaman informasi di internet disebut …|situs web|aplikasi kalkulator|dokumen cetak|folder|Situs web.
## KKA|Data dan informasi
Fakta mentah yang belum diolah disebut …|data|informasi|kesimpulan|grafik|Data.
Data yang sudah diolah sehingga bermakna disebut …|informasi|data mentah|bit|kabel|Informasi.
=|Rata-rata nilai kelas termasuk …|informasi|Informasi.
=|Catatan suhu harian termasuk …|data|Data.
B|Informasi membantu mengambil keputusan.|Keputusan.
S|Data dan informasi artinya sama persis.|Berbeda.
Total pengeluaran dari struk belanja termasuk …|informasi|data mentah|bug|kode|Informasi.
Daftar nama buah kesukaan siswa termasuk …|data|informasi|kesimpulan|program|Data.
## KKA|Mengelompokkan data
Mengelompokkan data berarti memisahkan data berdasarkan …|ciri yang sama|warna saja|urutan acak|nama terpanjang|Ciri sama.
Manfaat mengelompokkan data adalah …|mudah dicari|makin berantakan|hilang|rusak|Mudah dicari.
=|Apel dan stroberi dapat dikelompokkan sebagai buah berwarna …|merah|Merah.
=|Tahu dan tempe dikelompokkan sebagai lauk …|nabati|Nabati.
B|Komputer dapat mengelompokkan foto berdasarkan tanggal.|Tanggal.
S|Mengelompokkan data tidak perlu aturan.|Perlu aturan jelas.
Buku pelajaran dapat dikelompokkan berdasarkan …|mata pelajaran|berat kertas|jumlah coretan|warna lem|Mata pelajaran.
Ayam dan ikan dikelompokkan sebagai lauk …|hewani|nabati|sayur|buah|Hewani.
## KKA|Contoh KA di sekitar kita
KA adalah singkatan dari …|kecerdasan artifisial|komputer aktif|kabel antena|kode angka|Kecerdasan artifisial.
Contoh penggunaan KA adalah …|penerjemah otomatis|penggaris|pensil|meja|Penerjemah.
=|KA meniru cara berpikir …|manusia|Manusia.
=|Fitur membuka ponsel dengan wajah disebut pengenal …|wajah|Pengenal wajah.
B|Penyaring spam memakai KA.|Memilah surel.
S|KA selalu berbentuk robot manusia.|Ada di aplikasi.
Fitur yang menyarankan video untuk ditonton memakai KA berupa …|rekomendasi|kalkulator|penghapus|pengetik|Rekomendasi.
Peta digital memakai KA untuk menyarankan …|rute tercepat|warna baju|lagu sedih|harga emas|Rute.
## KKA|Pengenalan gambar oleh KA
KA belajar mengenali gambar dari …|banyak contoh berlabel|satu foto saja|tebakan acak|suara|Contoh berlabel.
Nama yang diberikan pada contoh gambar disebut …|label|bug|byte|kabel|Label.
=|Contoh yang dipakai KA untuk belajar disebut data …|latih|Data latih.
=|Tebakan yang dibuat KA disebut …|prediksi|Prediksi.
B|KA bisa salah mengenali gambar.|Bisa salah.
S|KA selalu benar dalam mengenali gambar.|Bisa salah.
Supaya KA lebih pintar mengenali kucing, KA perlu …|banyak foto kucing yang beragam|satu foto kucing|foto anjing saja|tanpa foto|Banyak contoh.
Seberapa sering tebakan KA benar disebut …|akurasi|label|data|pola|Akurasi.
## KKA|Kata sandi yang kuat
Kata sandi yang kuat sebaiknya minimal … karakter.|8|2|3|4|Minimal 8.
Contoh kata sandi yang kuat adalah …|Kucing#Hijau72|123456|password|budi2012|Campuran.
=|Kata sandi sebaiknya hanya diberitahukan kepada …|orang tua|Orang tua.
=|Kata sandi kuat mencampur huruf, angka, dan …|simbol|Simbol.
B|Tanggal lahir bukan kata sandi yang aman.|Mudah ditebak.
S|Kata sandi 123456 sangat kuat.|Sangat lemah.
Kata sandi qwerty lemah karena …|berupa urutan keyboard|terlalu panjang|memakai simbol|memakai angka|Mudah ditebak.
Jika teman meminta kata sandimu, kamu sebaiknya …|menolak memberikannya|memberikannya|menuliskannya di papan|mengumumkannya|Rahasiakan.
## KKA|Sopan santun di internet
Sopan santun di internet disebut …|netiket|internet|email|website|Netiket.
Pesan dengan huruf kapital semua dapat dianggap …|berteriak|berbisik|sopan|lucu|Berteriak.
=|Di balik layar internet ada …|manusia|Manusia.
=|Komentar yang baik bersifat …|membangun;sopan|Membangun.
B|Mengucapkan terima kasih di kolom komentar termasuk netiket.|Sopan.
S|Menyebarkan nomor telepon teman tanpa izin itu sopan.|Melanggar privasi.
Contoh komentar yang sopan adalah …|Terima kasih, videonya bermanfaat.|Jelek sekali!|Kamu bodoh.|HUH!!!|Sopan.
Jika ada teman yang diejek di grup, sikap kita adalah …|tidak ikut mengejek dan memberi tahu orang dewasa|ikut mengejek|menyebarkan|menertawakan|Tidak ikut.
## KKA|Mengenali berita bohong
Berita bohong disebut juga …|hoaks|fakta|data|informasi resmi|Hoaks.
Ciri berita bohong adalah …|meminta segera disebarkan|ada sumber resmi|ditulis rapi oleh media terpercaya|dapat dibuktikan|Minta disebarkan.
=|Sebelum membagikan berita, kita periksa …|sumbernya;sumber|Sumber.
=|Semboyan menghadapi hoaks adalah saring sebelum …|sharing;membagikan|Saring sebelum sharing.
B|Hoaks sering membuat orang panik.|Panik.
S|Berita dengan judul berlebihan pasti benar.|Patut dicurigai.
Cara memeriksa kebenaran berita adalah …|membandingkan dengan media terpercaya|langsung membagikannya|percaya judulnya saja|menambah bumbu|Bandingkan.
Foto lama yang dipakai untuk kejadian baru adalah ciri …|hoaks|berita resmi|data|netiket|Hoaks.
## KKA|Mengatur waktu layar
Waktu layar adalah lamanya kita memakai …|gawai|sepeda|buku tulis|bola|Gawai.
Akibat bermain gawai sampai larut malam adalah …|kurang tidur|mata segar|badan bugar|tidur nyenyak|Kurang tidur.
=|Mata sebaiknya diistirahatkan setiap … menit.|20;dua puluh|Aturan 20-20-20.
=|Gawai sebaiknya dimatikan sebelum …|tidur|Sebelum tidur.
B|Bermain di luar rumah membuat badan sehat.|Bergerak.
S|Menatap layar terus-menerus membuat mata segar.|Mata lelah.
Aturan waktu layar sebaiknya dibuat bersama …|orang tua|teman di internet|orang asing|tidak siapa pun|Orang tua.
Duduk terlalu lama di depan layar membuat tubuh kurang …|bergerak|makan|minum|tidur siang|Kurang bergerak.
"""

SAS += """
## KKA 1
0|Rambu lalu lintas yang hanya memakai gambar sederhana adalah contoh ....|abstraksi|debugging|enkripsi|biner|Abstraksi.
1|Simbol diagram alir berbentuk jajargenjang berarti ....|masukan atau keluaran|mulai|keputusan|proses|Jajargenjang.
2|Bagian komputer untuk menggerakkan penunjuk di layar adalah ....|mouse|monitor|printer|speaker|Mouse.
3|Printer termasuk perangkat ....|output|input|proses|penyimpanan|Output.
4|Blok untuk membuat tokoh berputar ke kiri adalah blok ....|belok kiri|maju|ulangi|tunggu|Belok kiri.
5|Langkah debugging setelah menemukan kesalahan adalah ....|memperbaiki perintah|membuang program|menyerah|mematikan komputer|Perbaiki.
6|Bilangan desimal 4 dalam biner adalah ....|100|4|11|1000|4 = 100.
7|Aplikasi yang dipakai untuk membuka situs web disebut ....|peramban|router|server|printer|Peramban.
## KKA 2
0|Siswa tertinggi di kelas yang diketahui dari catatan tinggi badan termasuk ....|informasi|data mentah|bug|bit|Informasi.
1|Wortel dikelompokkan sebagai sayur berwarna ....|jingga|hijau|merah|ungu|Wortel jingga.
2|Penyaring spam pada surel menggunakan ....|kecerdasan artifisial|printer|flashdisk|keyboard|KA.
3|Contoh gambar yang dipakai untuk menguji KA disebut data ....|uji|latih|label|mentah|Data uji.
4|Kata sandi yang paling kuat adalah ....|Matahari!Pagi9|matahari|12345678|abcdefg|Campuran panjang.
5|Menghargai pendapat berbeda di internet termasuk ....|netiket|hoaks|bug|spam|Netiket.
6|Berita yang tidak jelas asal sumbernya patut ....|dicurigai|langsung dibagikan|dipercaya|disebarkan ke semua grup|Dicurigai.
7|Aturan 20-20-20 bertujuan menjaga kesehatan ....|mata|kaki|perut|telinga|Mata.
"""

TOPICS += """
## PAI
# 1|Al-Qur'an, Iman, dan Sejarah
@ Surah Quraisy
min: 12
act: Dengarkan bacaan Surah Quraisy, lalu tulis dua nikmat Allah yang membuatmu merasa aman.
mis: mengira Surah Quraisy menceritakan pasukan bergajah
exp: Surah Quraisy adalah surah ke-106 dan terdiri atas 4 ayat. Quraisy adalah nama suku Nabi Muhammad. Surah ini menceritakan kebiasaan suku Quraisy berdagang pada musim dingin dan musim panas. Allah memerintahkan mereka menyembah Tuhan pemilik Ka'bah yang memberi makan dan rasa aman.
ex: Dengarkan rekaman qari pada kartu bacaan. // Kita bersyukur atas makanan dan rasa aman.
pt: Surah ke-106, terdiri atas 4 ayat ; Quraisy suku Nabi Muhammad ; Allah memberi makan dan rasa aman
sum: Surah Quraisy mengajak bersyukur atas nikmat Allah.
fig: table Hal | Isi ;; nomor surah | 106 ;; jumlah ayat | 4 ;; arti nama surah | suku Quraisy ;; perjalanan musim dingin | ke Yaman ;; perjalanan musim panas | ke Syam ;; nikmat yang disebut | makanan dan rasa aman ~ Isi Surah Quraisy.
read: quran 106:1-4
@ Hukum bacaan idgam
min: 12
act: Dengarkan contoh bacaan idgam dari ustaz, lalu tandai di mushaf bersama orang tua.
mis: membaca nun mati dengan jelas saat bertemu huruf idgam
exp: Idgam artinya memasukkan atau meleburkan. Idgam terjadi jika nun mati atau tanwin bertemu huruf ي ن م و (idgam bigunnah atau dengan dengung) dan huruf ل ر (idgam bilagunnah atau tanpa dengung). Huruf idgam ada enam, dikumpulkan dalam kata yarmalun.
ex: مَنْ يَقُوْلُ dibaca mayyaqulu dengan dengung. // مِنْ رَبِّهِمْ dibaca mirrabbihim tanpa dengung.
pt: Idgam artinya melebur ; Bigunnah: ي ن م و ; Bilagunnah: ل ر
sum: Idgam dibaca dengan meleburkan nun ke huruf berikutnya.
fig: table Huruf | Jenis idgam ;; ي | bigunnah dengan ya ;; ن | bigunnah dengan nun ;; م | bigunnah dengan mim ;; و | bigunnah dengan wau ;; ل | bilagunnah dengan lam ;; ر | bilagunnah dengan ra ~ Huruf idgam dan jenisnya.
@ Iman kepada rasul
min: 12
act: Hafalkan nama lima rasul ulul azmi bersama keluarga.
mis: mengira semua nabi adalah rasul
exp: Iman kepada rasul adalah rukun iman keempat. Rasul adalah manusia pilihan Allah yang menerima wahyu dan wajib menyampaikannya kepada umatnya. Jumlah rasul yang wajib diketahui ada 25. Lima di antaranya disebut ulul azmi karena sangat sabar, yaitu Nabi Nuh, Ibrahim, Musa, Isa, dan Muhammad.
ex: Nabi Muhammad adalah rasul terakhir. // Nabi Nuh termasuk ulul azmi.
pt: Rukun iman keempat ; 25 rasul wajib diketahui ; Ulul azmi lima rasul yang sangat sabar
sum: Kita meneladani kesabaran dan perjuangan para rasul.
fig: table Rasul ulul azmi | Keteladanan ;; Nabi Nuh | sabar berdakwah ratusan tahun ;; Nabi Ibrahim | teguh melawan berhala ;; Nabi Musa | berani menghadapi Firaun ;; Nabi Isa | penyayang dan rendah hati ;; Nabi Muhammad | akhlak paling mulia ;; jumlah ulul azmi | lima rasul ~ Rasul ulul azmi.
@ Sifat wajib rasul
min: 12
act: Pilih satu sifat wajib rasul, lalu praktikkan sepanjang minggu ini.
mis: tertukar arti tablig dan fatanah
exp: Rasul memiliki empat sifat wajib. Siddiq artinya jujur. Amanah artinya dapat dipercaya. Tablig artinya menyampaikan wahyu kepada umat. Fatanah artinya cerdas. Sifat mustahilnya adalah kizib atau dusta, khianat, kitman atau menyembunyikan, dan baladah atau bodoh.
ex: Nabi Muhammad tidak pernah berbohong karena bersifat siddiq. // Rasul menyampaikan semua wahyu karena bersifat tablig.
pt: Siddiq jujur, amanah dapat dipercaya ; Tablig menyampaikan ; Fatanah cerdas
sum: Sifat wajib rasul menjadi teladan bagi kita.
fig: table Sifat wajib | Arti ;; siddiq | jujur ;; amanah | dapat dipercaya ;; tablig | menyampaikan wahyu ;; fatanah | cerdas ;; kizib | dusta, sifat mustahil ;; khianat | tidak dapat dipercaya, sifat mustahil ~ Sifat wajib dan mustahil rasul.
@ Toleransi menurut ajaran Islam
min: 12
act: Cari ayat lakum dinukum waliyadin dan jelaskan maknanya kepada keluarga.
mis: mengira toleransi berarti mencampurkan ibadah agama yang berbeda
exp: Islam mengajarkan toleransi, yaitu menghormati pemeluk agama lain, tidak memaksakan agama, dan tetap berbuat baik dalam urusan sosial. Dalam hal ibadah dan keyakinan, setiap umat menjalankan agamanya masing-masing, seperti ayat terakhir Surah Al-Kafirun: untukmu agamamu dan untukku agamaku.
ex: Bekerja sama membersihkan lingkungan dengan tetangga berbeda agama. // Tidak mengganggu tetangga yang beribadah.
pt: Hormati pemeluk agama lain ; Tidak memaksakan agama ; Ibadah dijalankan masing-masing
sum: Toleransi membuat kehidupan beragama rukun.
fig: table Situasi | Sikap toleran ;; tetangga beribadah | tidak mengganggu ;; kerja bakti lingkungan | bekerja sama ;; teman berbeda agama sakit | menjenguk ;; teman berhari raya | menghormati ;; urusan ibadah | dijalankan masing-masing ;; berbeda keyakinan | tidak memaksa ~ Toleransi dalam ajaran Islam.
@ Hijrah ke Madinah
min: 12
act: Buat peta sederhana perjalanan hijrah dari Makkah ke Madinah dengan Gua Tsur.
mis: mengira Nabi hijrah sendirian tanpa sahabat
exp: Hijrah adalah perpindahan Nabi Muhammad dan kaum muslimin dari Makkah ke Madinah pada tahun 622 Masehi. Nabi ditemani Abu Bakar dan bersembunyi di Gua Tsur. Di Quba, Nabi membangun Masjid Quba. Penduduk Madinah yang menolong disebut kaum Ansar, sedangkan pendatang dari Makkah disebut kaum Muhajirin.
ex: Masjid Quba adalah masjid pertama yang dibangun Nabi. // Kaum Ansar menolong kaum Muhajirin.
pt: Hijrah tahun 622 Masehi ; Ditemani Abu Bakar ; Muhajirin dan Ansar bersaudara
sum: Hijrah menjadi awal kejayaan Islam.
fig: table Tokoh atau tempat | Peran ;; Abu Bakar | menemani Nabi hijrah ;; Gua Tsur | tempat bersembunyi ;; Masjid Quba | masjid pertama ;; Madinah | kota tujuan hijrah ;; kaum Ansar | penduduk Madinah yang menolong ;; kaum Muhajirin | pendatang dari Makkah ~ Peristiwa hijrah ke Madinah.
# 2|Al-Qur'an, Ibadah, dan Akhlak
@ Surah Al-Fil
min: 12
act: Dengarkan bacaan Surah Al-Fil, lalu ceritakan kembali kisah pasukan bergajah.
mis: mengira pasukan bergajah berhasil menghancurkan Ka'bah
exp: Surah Al-Fil adalah surah ke-105 dan terdiri atas 5 ayat. Al-Fil artinya gajah. Surah ini menceritakan pasukan bergajah pimpinan Abrahah yang ingin menghancurkan Ka'bah. Allah mengirim burung Ababil yang melempari mereka dengan batu dari tanah yang terbakar sehingga pasukan itu hancur.
ex: Dengarkan rekaman qari pada kartu bacaan. // Peristiwa ini terjadi pada Tahun Gajah.
pt: Surah ke-105, terdiri atas 5 ayat ; Al-Fil artinya gajah ; Allah melindungi Ka'bah dengan burung Ababil
sum: Al-Fil menunjukkan kekuasaan Allah menjaga Ka'bah.
fig: table Hal | Isi ;; nomor surah | 105 ;; jumlah ayat | 5 ;; arti nama surah | gajah ;; pemimpin pasukan | Abrahah ;; burung yang dikirim | Ababil ;; tahun peristiwa | Tahun Gajah ~ Isi Surah Al-Fil.
read: quran 105:1-5
@ Hukum bacaan ikhfa
min: 12
act: Dengarkan bacaan ikhfa dari ustaz, lalu latih dengung samar pada contoh kata.
mis: membaca nun mati terlalu jelas saat bertemu huruf ikhfa
exp: Ikhfa artinya samar. Ikhfa terjadi jika nun mati atau tanwin bertemu salah satu dari 15 huruf ikhfa, misalnya ت, ث, ج, د, س, ش, ص, ف, ق, dan ك. Nun mati atau tanwin dibaca samar antara jelas dan dengung, sekitar dua harakat.
ex: مِنْ قَبْلِ dibaca dengan nun samar. // أَنْتُمْ dibaca dengan nun samar mendengung.
pt: Ikhfa artinya samar ; Huruf ikhfa ada 15 ; Dibaca samar dengan dengung
sum: Ikhfa dibaca samar dengan dengung.
fig: table Hukum bacaan | Cara membaca ;; izhar | jelas tanpa dengung ;; idgam bigunnah | melebur dengan dengung ;; idgam bilagunnah | melebur tanpa dengung ;; iqlab | nun berubah menjadi mim ;; ikhfa | samar dengan dengung ;; jumlah huruf ikhfa | lima belas ~ Hukum bacaan nun mati dan tanwin.
@ Salat Jumat
min: 12
act: Tanyakan kepada ayah atau kakak laki-laki tentang tata cara salat Jumat di masjid.
mis: mengira salat Jumat terdiri atas empat rakaat
exp: Salat Jumat adalah salat wajib bagi laki-laki muslim yang balig dan berakal pada hari Jumat di waktu zuhur. Salat Jumat dikerjakan berjamaah di masjid sebanyak dua rakaat dan didahului dua khutbah. Saat khatib berkhutbah, jamaah mendengarkan dengan tenang.
ex: Salat Jumat dua rakaat setelah khutbah. // Jamaah tidak berbicara saat khutbah.
pt: Wajib bagi laki-laki muslim balig ; Dua rakaat berjamaah ; Didahului dua khutbah
sum: Salat Jumat adalah ibadah mingguan yang wajib.
fig: table Hal | Keterangan ;; hukum | wajib bagi laki-laki balig ;; waktu | waktu zuhur hari Jumat ;; jumlah rakaat | dua rakaat ;; khutbah | dua khutbah sebelum salat ;; tempat | masjid ;; sikap saat khutbah | mendengarkan dengan tenang ~ Ketentuan salat Jumat.
@ Salat jamak dan qasar
min: 12
act: Tanyakan kepada orang tua bagaimana mereka salat saat perjalanan jauh mudik.
mis: mengira salat magrib boleh diqasar
exp: Salat jamak adalah menggabungkan dua salat fardu dalam satu waktu, yaitu zuhur dengan asar atau magrib dengan isya. Salat qasar adalah meringkas salat empat rakaat menjadi dua rakaat, yaitu zuhur, asar, dan isya. Keringanan ini diberikan bagi orang yang sedang dalam perjalanan jauh.
ex: Jamak takdim: zuhur dan asar dikerjakan di waktu zuhur. // Isya diqasar menjadi dua rakaat.
pt: Jamak menggabungkan dua salat ; Qasar meringkas empat menjadi dua rakaat ; Keringanan saat perjalanan
sum: Islam memberi keringanan beribadah saat bepergian.
fig: table Istilah | Arti ;; jamak | menggabungkan dua salat ;; qasar | meringkas rakaat ;; jamak takdim | dikerjakan di waktu pertama ;; jamak takhir | dikerjakan di waktu kedua ;; musafir | orang dalam perjalanan ;; salat yang boleh diqasar | zuhur, asar, isya ~ Istilah salat jamak dan qasar.
@ Kisah Nabi Yusuf
min: 12
act: Ceritakan kembali kisah Nabi Yusuf dan nilai pemaafnya kepada keluarga.
mis: mengira Nabi Yusuf membalas dendam kepada saudaranya
exp: Nabi Yusuf adalah putra Nabi Yakub. Karena iri, saudara-saudaranya membuangnya ke dalam sumur. Nabi Yusuf kemudian dibawa ke Mesir. Allah memberinya mukjizat dapat menafsirkan mimpi. Ia menjadi pejabat penting di Mesir dan akhirnya memaafkan saudara-saudaranya.
ex: Nabi Yusuf menafsirkan mimpi raja tentang tujuh sapi. // Nabi Yusuf memaafkan saudaranya.
pt: Putra Nabi Yakub ; Mukjizat menafsirkan mimpi ; Pemaaf kepada saudaranya
sum: Kisah Nabi Yusuf mengajarkan sabar dan pemaaf.
fig: table Tokoh atau peristiwa | Keterangan ;; Nabi Yakub | ayah Nabi Yusuf ;; sumur | tempat Yusuf dibuang ;; Mesir | tempat Yusuf menjadi pejabat ;; mimpi raja | tujuh sapi gemuk dan kurus ;; mukjizat | menafsirkan mimpi ;; akhir kisah | memaafkan saudaranya ~ Kisah Nabi Yusuf.
@ Menjaga lisan
min: 12
act: Selama sehari, hitung berapa kali kamu berkata baik dan berhenti sebelum berkata kasar.
mis: mengira membicarakan keburukan teman yang benar tidak apa-apa
exp: Menjaga lisan artinya menjaga ucapan dari kata-kata buruk. Nabi Muhammad bersabda agar orang beriman berkata baik atau diam. Kita tidak boleh berbohong, mencela, mengadu domba, dan bergunjing atau ghibah, yaitu membicarakan keburukan orang lain.
ex: Mengucapkan terima kasih dan maaf. // Tidak ikut membicarakan keburukan teman.
pt: Berkata baik atau diam ; Hindari bohong, mencela, ghibah ; Ucapan mencerminkan akhlak
sum: Lisan yang terjaga membuat kita disenangi.
fig: table Perbuatan lisan | Hukum atau sikap ;; berkata jujur | terpuji ;; berbohong | tercela ;; ghibah | membicarakan keburukan orang ;; mengadu domba | memecah persaudaraan ;; memberi salam | menyebarkan kedamaian ;; berkata baik atau diam | pesan Nabi ~ Perbuatan lisan.
"""

BANK += """
## PAI|Surah Quraisy
Surah Quraisy terdiri atas … ayat.|4|5|3|6|Quraisy 4 ayat.
Surah Quraisy adalah surah ke- …|106|105|107|104|Surah ke-106.
=|Quraisy adalah nama … Nabi Muhammad.|suku|Suku.
=|Suku Quraisy berdagang ke Yaman pada musim …|dingin|Musim dingin.
B|Surah Quraisy menyebut nikmat makanan dan rasa aman.|Nikmat.
S|Surah Quraisy menceritakan pasukan bergajah.|Itu Al-Fil.
Suku Quraisy berdagang ke Syam pada musim …|panas|dingin|hujan|semi|Musim panas.
Surah sesudah Quraisy dalam Al-Qur'an adalah …|Al-Ma'un|Al-Fil|Al-Kautsar|Al-Humazah|106 lalu 107.
## PAI|Hukum bacaan idgam
Idgam artinya …|melebur|jelas|samar|memantul|Idgam melebur.
Huruf idgam bigunnah adalah …|ي ن م و|ل ر|ء ه ع|ب|Bigunnah.
=|Idgam tanpa dengung disebut idgam …|bilagunnah|Bilagunnah.
=|Huruf idgam dikumpulkan dalam kata …|yarmalun|Yarmalun.
B|Huruf ر termasuk huruf idgam bilagunnah.|Bilagunnah.
S|Idgam bigunnah dibaca tanpa dengung.|Dengan dengung.
Banyak huruf idgam adalah …|6|4|2|15|Enam huruf.
Nun mati bertemu huruf ل dibaca …|melebur tanpa dengung|jelas|samar|berubah menjadi mim|Bilagunnah.
## PAI|Iman kepada rasul
Iman kepada rasul adalah rukun iman ke- …|4|2|5|6|Keempat.
Jumlah rasul yang wajib diketahui adalah …|25|20|10|99|25 rasul.
=|Rasul yang sangat sabar disebut ulul …|azmi|Ulul azmi.
=|Rasul terakhir adalah Nabi …|Muhammad|Muhammad.
B|Nabi Nuh termasuk rasul ulul azmi.|Ulul azmi.
S|Jumlah rasul ulul azmi ada sepuluh.|Lima.
Rasul ulul azmi yang menghadapi Firaun adalah Nabi …|Musa|Nuh|Isa|Ibrahim|Musa.
Rasul adalah manusia pilihan yang wajib … wahyu.|menyampaikan|menyembunyikan|mengubah|melupakan|Menyampaikan.
## PAI|Sifat wajib rasul
Siddiq artinya …|jujur|cerdas|menyampaikan|dapat dipercaya|Siddiq.
Fatanah artinya …|cerdas|jujur|dapat dipercaya|menyampaikan|Fatanah.
=|Sifat rasul yang artinya menyampaikan adalah …|tablig;tabligh|Tablig.
=|Sifat rasul yang artinya dapat dipercaya adalah …|amanah|Amanah.
B|Kizib adalah sifat mustahil rasul yang artinya dusta.|Kizib.
S|Rasul mungkin menyembunyikan wahyu.|Mustahil kitman.
Lawan sifat fatanah adalah …|baladah|kizib|khianat|kitman|Baladah bodoh.
Sikap meneladani sifat siddiq adalah …|selalu berkata jujur|suka berbohong|menyembunyikan tugas|malas belajar|Jujur.
## PAI|Toleransi menurut ajaran Islam
Toleransi artinya …|menghormati pemeluk agama lain|memaksakan agama|mencampur ibadah|menjauhi tetangga|Menghormati.
Ayat untukmu agamamu dan untukku agamaku terdapat dalam Surah …|Al-Kafirun|Al-Fil|Quraisy|Al-Ikhlas|Al-Kafirun.
=|Dalam urusan ibadah, setiap umat menjalankan agamanya …|masing-masing|Masing-masing.
=|Islam melarang … orang memeluk agama.|memaksa|Tidak ada paksaan.
B|Bekerja sama dalam kerja bakti dengan tetangga berbeda agama adalah toleransi.|Toleransi sosial.
S|Toleransi berarti ikut beribadah agama lain.|Tidak mencampur ibadah.
Sikap toleran saat tetangga beribadah adalah …|tidak mengganggu|membuat keributan|mengejek|menghalangi|Tidak mengganggu.
Menjenguk teman berbeda agama yang sakit termasuk …|toleransi|intoleransi|ghibah|riya|Toleransi.
## PAI|Hijrah ke Madinah
Hijrah Nabi Muhammad terjadi pada tahun …|622 Masehi|570 Masehi|610 Masehi|632 Masehi|622 M.
Sahabat yang menemani Nabi hijrah adalah …|Abu Bakar|Umar|Ali|Usman|Abu Bakar.
=|Gua tempat Nabi bersembunyi saat hijrah adalah Gua …|Tsur|Tsur.
=|Masjid pertama yang dibangun Nabi adalah Masjid …|Quba|Quba.
B|Penduduk Madinah yang menolong disebut kaum Ansar.|Ansar.
S|Kaum Muhajirin adalah penduduk asli Madinah.|Pendatang dari Makkah.
Kota Madinah sebelumnya bernama …|Yatsrib|Thaif|Mesir|Syam|Yatsrib.
Peristiwa hijrah menjadi awal perhitungan tahun …|Hijriah|Masehi|Saka|Jawa|Hijriah.
## PAI|Surah Al-Fil
Surah Al-Fil terdiri atas … ayat.|5|4|3|7|Al-Fil 5 ayat.
Al-Fil artinya …|gajah|burung|batu|unta|Gajah.
=|Pemimpin pasukan bergajah adalah …|Abrahah|Abrahah.
=|Burung yang dikirim Allah bernama burung …|Ababil|Ababil.
B|Pasukan bergajah ingin menghancurkan Ka'bah.|Ka'bah.
S|Pasukan bergajah berhasil menghancurkan Ka'bah.|Mereka hancur.
Peristiwa pasukan bergajah terjadi pada tahun kelahiran Nabi yang disebut Tahun …|Gajah|Hijrah|Duka|Baru|Tahun Gajah.
Al-Fil adalah surah ke- …|105|106|104|107|Surah ke-105.
## PAI|Hukum bacaan ikhfa
Ikhfa artinya …|samar|jelas|melebur|mengganti|Ikhfa samar.
Banyak huruf ikhfa adalah …|15|6|2|1|Lima belas huruf.
=|Hukum bacaan nun mati bertemu ب disebut …|iqlab|Iqlab.
=|Hukum bacaan nun mati bertemu huruf tenggorokan disebut …|izhar|Izhar.
B|Huruf ك termasuk huruf ikhfa.|Ikhfa.
S|Ikhfa dibaca jelas tanpa dengung.|Samar dengan dengung.
Pada iqlab, bunyi nun berubah menjadi …|mim|lam|ra|wau|Menjadi mim.
Nun mati bertemu huruf ت dibaca …|samar dengan dengung|jelas|melebur tanpa dengung|berubah menjadi mim|Ikhfa.
## PAI|Salat Jumat
Salat Jumat wajib bagi …|laki-laki muslim balig|anak kecil|semua hewan|perempuan saja|Laki-laki balig.
Jumlah rakaat salat Jumat adalah …|2|4|3|1|Dua rakaat.
=|Salat Jumat didahului dua …|khutbah|Khutbah.
=|Orang yang menyampaikan khutbah disebut …|khatib|Khatib.
B|Saat khutbah, jamaah mendengarkan dengan tenang.|Tenang.
S|Salat Jumat dikerjakan pada waktu subuh.|Waktu zuhur.
Salat Jumat dilaksanakan secara …|berjamaah|sendirian|di rumah sendiri|tanpa imam|Berjamaah.
Salat Jumat menggantikan salat … pada hari Jumat.|zuhur|asar|subuh|isya|Zuhur.
## PAI|Salat jamak dan qasar
Salat jamak artinya …|menggabungkan dua salat dalam satu waktu|meringkas rakaat|salat sendirian|salat sunah|Jamak.
Salat qasar artinya …|meringkas salat empat rakaat menjadi dua|menggabungkan dua salat|menambah rakaat|salat di masjid|Qasar.
=|Salat zuhur dan asar dikerjakan di waktu zuhur disebut jamak …|takdim|Jamak takdim.
=|Orang yang sedang dalam perjalanan disebut …|musafir|Musafir.
B|Salat isya boleh diqasar menjadi dua rakaat.|Isya empat rakaat.
S|Salat magrib boleh diqasar.|Magrib tiga rakaat tidak diqasar.
Pasangan salat yang boleh dijamak adalah …|magrib dan isya|subuh dan zuhur|asar dan magrib|isya dan subuh|Magrib isya.
Keringanan jamak dan qasar diberikan bagi orang yang …|bepergian jauh|malas|tidur|bermain|Perjalanan.
## PAI|Kisah Nabi Yusuf
Nabi Yusuf adalah putra Nabi …|Yakub|Ibrahim|Musa|Nuh|Yakub.
Saudara-saudara Nabi Yusuf membuangnya ke dalam …|sumur|laut|hutan|gua|Sumur.
=|Mukjizat Nabi Yusuf adalah dapat menafsirkan …|mimpi|Mimpi.
=|Nabi Yusuf menjadi pejabat penting di negeri …|Mesir|Mesir.
B|Nabi Yusuf memaafkan saudara-saudaranya.|Pemaaf.
S|Nabi Yusuf membalas dendam kepada saudaranya.|Memaafkan.
Mimpi raja Mesir yang ditafsirkan Nabi Yusuf tentang …|tujuh sapi gemuk dan kurus|burung terbang|bintang jatuh|banjir besar|Tujuh sapi.
Pelajaran dari kisah Nabi Yusuf adalah …|sabar dan pemaaf|pendendam|iri hati|sombong|Sabar pemaaf.
## PAI|Menjaga lisan
Nabi Muhammad berpesan agar orang beriman berkata baik atau …|diam|berteriak|berbohong|mengejek|Atau diam.
Membicarakan keburukan orang lain disebut …|ghibah|tablig|syukur|zikir|Ghibah.
=|Memecah persaudaraan dengan omongan disebut mengadu …|domba|Mengadu domba.
=|Ucapan yang menyebarkan kedamaian adalah …|salam|Salam.
B|Berkata jujur termasuk menjaga lisan.|Terpuji.
S|Mencela teman termasuk perbuatan terpuji.|Tercela.
Contoh menjaga lisan adalah …|mengucapkan terima kasih|mengejek teman|berbohong kepada guru|bergunjing|Terima kasih.
Teman mengajak membicarakan keburukan orang lain. Sikap kita adalah …|menolak dan mengalihkan pembicaraan|ikut bergunjing|menambah cerita|menyebarkannya|Menolak.
"""

SAS += """
## PAI 1
0|Surah Quraisy memerintahkan menyembah Tuhan pemilik ....|Ka'bah|gunung|laut|pasar|Ka'bah.
1|Nun mati bertemu huruf م dibaca ....|melebur dengan dengung|jelas|samar|berubah menjadi lam|Idgam bigunnah.
2|Rasul ulul azmi yang teguh melawan berhala adalah Nabi ....|Ibrahim|Nuh|Isa|Musa|Ibrahim.
3|Sifat mustahil rasul yang artinya menyembunyikan adalah ....|kitman|kizib|baladah|khianat|Kitman.
4|Menurut ajaran Islam, dalam urusan sosial kita tetap ....|berbuat baik kepada semua orang|menjauhi pemeluk agama lain|memaksa orang lain|bermusuhan|Berbuat baik.
5|Penduduk Madinah yang menolong kaum Muhajirin disebut kaum ....|Ansar|Quraisy|Badui|Yahudi|Ansar.
## PAI 2
0|Burung Ababil melempari pasukan bergajah dengan ....|batu dari tanah yang terbakar|air|api|kayu|Batu.
1|Hukum bacaan yang nun matinya berubah menjadi mim adalah ....|iqlab|ikhfa|izhar|idgam|Iqlab.
2|Saat khatib menyampaikan khutbah, jamaah sebaiknya ....|mendengarkan dengan tenang|bercakap-cakap|bermain ponsel|tidur|Tenang.
3|Magrib dan isya dikerjakan di waktu isya disebut jamak ....|takhir|takdim|qasar|munfarid|Takhir.
4|Nabi Yusuf dibawa ke negeri ....|Mesir|Syam|Yaman|Persia|Mesir.
5|Mengucapkan salam termasuk perbuatan lisan yang ....|terpuji|tercela|dilarang|sia-sia|Terpuji.
"""

TOPICS += """
## SUN
# 1|Aksara, Pupuh, jeung Carita
@ Aksara swara
min: 12
act: Tulis lima kecap nu dimimitian ku aksara swara, contona awi jeung ucing.
mis: mengira aksara swara sama dengan aksara ngalagena
exp: Aksara swara adalah aksara vokal dalam aksara Sunda. Jumlahnya ada tujuh, yaitu a, é, i, o, u, e, dan eu. Aksara swara dipakai untuk menulis suku kata yang hanya berupa vokal, misalnya awal kata awi, iga, dan ucing. Berbeda dengan aksara ngalagena yang berupa konsonan.
ex: Kecap awi dimimitian ku aksara swara a. // Kecap eusi dimimitian ku aksara swara eu.
pt: Aksara swara aksara vokal ; Jumlahnya tujuh ; Dipakai untuk suku kata vokal
sum: Aksara swara melambangkan bunyi vokal.
fig: table Aksara swara | Conto kecap ;; a | awi ;; i | iga ;; u | ucing ;; é | éta ;; o | oray ;; eu | eusi ~ Aksara swara jeung conto kecapna.
@ Watek pupuh
min: 12
act: Dangukeun hiji pupuh, tuluy tebak wateknya: gumbira, sedih, atawa ambek.
mis: menyanyikan pupuh Maskumambang dengan nada gembira
exp: Setiap pupuh memiliki watek atau sifat yang sesuai isi ceritanya. Pupuh Kinanti berwatak prihatin atau menunggu, Sinom berwatak gembira, Asmarandana berwatak kasih sayang, Dangdanggula berwatak tenteram, Maskumambang berwatak sedih, dan Durma berwatak marah.
ex: Pupuh Sinom cocok untuk cerita gembira. // Pupuh Maskumambang cocok untuk cerita sedih.
pt: Setiap pupuh punya watek ; Sinom gembira, Maskumambang sedih ; Pilih pupuh sesuai isi
sum: Watek pupuh menyesuaikan perasaan cerita.
fig: table Pupuh | Watek ;; Kinanti | prihatin ;; Sinom | gumbira ;; Asmarandana | kanyaah ;; Dangdanggula | tengtrem ;; Maskumambang | nalangsa ;; Durma | ambek ~ Pupuh jeung watekna.
@ Kecap rajékan
min: 12
act: Kumpulkeun lima kecap rajékan tina bacaan basa Sunda, tuluy golongkeun jenisna.
mis: mengira semua kata ulang Sunda diulang utuh
exp: Kecap rajékan adalah kata ulang dalam bahasa Sunda. Ada rajékan dwimurni, yaitu kata diulang utuh seperti imah-imah. Ada dwireka, yaitu diulang dengan perubahan bunyi seperti bulak-balik. Ada dwipurwa, yaitu suku kata pertama diulang seperti tatanya. Ada trilingga, yaitu diulang tiga kali dengan bunyi berubah seperti dar-der-dor.
ex: Barudak ulin di imah-imah tatangga. // Sora bedil dar-der-dor.
pt: Dwimurni diulang utuh ; Dwireka berubah bunyi ; Dwipurwa suku kata pertama diulang
sum: Kecap rajékan memiliki beberapa jenis.
fig: table Kecap rajékan | Jenisna ;; imah-imah | dwimurni ;; bulak-balik | dwireka ;; tatanya | dwipurwa ;; dar-der-dor | trilingga ;; sasapu | dwipurwa tina sapu ;; dag-dig-dug | trilingga sora haté ~ Conto kecap rajékan.
@ Unsur dongéng
min: 12
act: Baca hiji dongéng Sunda, tuluy tulis palaku, latar, jeung amanatna.
mis: menganggap amanat sama dengan judul
exp: Dongéng adalah cerita rekaan dari zaman dulu. Unsur dongéng meliputi palaku atau tokoh, latar atau tempat dan waktu, galur atau alur, jejer atau tema, dan amanat atau pesan. Ada juga jenis dongéng sasakala yang menceritakan asal-usul tempat.
ex: Palaku dina dongéng Sangkuriang nyaéta Sangkuriang jeung Dayang Sumbi. // Amanatna: kudu ngajenan kolot.
pt: Palaku, latar, galur ; Jejer dan amanat ; Sasakala tentang asal-usul
sum: Unsur dongéng membantu memahami cerita.
fig: table Unsur | Hartina ;; palaku | tokoh dina carita ;; latar | tempat jeung waktu ;; galur | jalan carita ;; jejer | téma carita ;; amanat | pesen carita ;; sasakala | dongéng asal-usul tempat ~ Unsur-unsur dongéng.
@ Nulis surat pribadi
min: 12
act: Tulis surat pondok dina basa Sunda keur nini atawa aki.
mis: lupa menuliskan tanggal dan tempat surat
exp: Surat pribadi adalah surat untuk keluarga atau teman. Bagian surat dalam bahasa Sunda adalah titimangsa atau tempat dan tanggal, salam bubuka, bubuka, eusi, panutup, salam panutup, dan ngaran nu ngirim. Bahasanya disesuaikan dengan orang yang dikirimi surat.
ex: Bandung, 5 Méi 2026. // Wassalam, putu anjeun, Asep.
pt: Diawali titimangsa ; Ada bubuka, eusi, panutup ; Bahasa disesuaikan penerima
sum: Surat pribadi tersusun dari bagian-bagian tertentu.
fig: table Bagian surat | Conto ;; titimangsa | Bandung, 5 Méi 2026 ;; salam bubuka | Assalamualaikum ;; bubuka | kumaha damang, Nini? ;; eusi | carita kagiatan di sakola ;; panutup | sakitu heula seratan ti abdi ;; ngaran nu ngirim | putu anjeun, Asep ~ Bagian surat pribadi.
@ Paguneman
min: 12
act: Latih paguneman jeung kolot ngagunakeun basa lemes.
mis: memakai basa loma kepada orang tua saat bercakap-cakap
exp: Paguneman adalah percakapan antara dua orang atau lebih. Dalam paguneman, kita memakai bahasa yang sesuai dengan lawan bicara, mendengarkan dengan baik, dan bergantian berbicara. Kepada orang tua dan guru dipakai bahasa lemes.
ex: Wilujeng énjing, Bu. // Kumaha damang, Pa?
pt: Percakapan dua orang atau lebih ; Bahasa sesuai lawan bicara ; Bergantian berbicara
sum: Paguneman yang sopan memakai bahasa yang tepat.
fig: table Kaayaan | Ucapan ;; papanggih isuk-isuk | wilujeng énjing ;; nganuhunkeun | hatur nuhun ;; menta dihampura | hapunten ;; nanyakeun kaayaan | kumaha damang ;; ngabagéakeun sémah | wilujeng sumping ;; liwat di hareupeun kolot | punten ~ Ucapan dina paguneman.
# 2|Basa jeung Budaya Jawa Barat
@ Carita pondok
min: 12
act: Baca hiji carpon basa Sunda, tuluy caritakeun deui ku basa sorangan.
mis: mengira carpon sama dengan dongéng
exp: Carita pondok atau carpon adalah cerita rekaan yang pendek dan masuk akal. Berbeda dengan dongéng yang sering berisi hal ajaib, carpon menceritakan kejadian yang bisa terjadi dalam kehidupan sehari-hari. Carpon memiliki palaku, latar, galur, dan amanat.
ex: Carpon ngeunaan budak nu leungiteun sapédahna. // Dongéng ngeunaan sato nu bisa nyarita.
pt: Carpon cerita pendek ; Masuk akal ; Punya palaku, latar, galur, amanat
sum: Carpon menceritakan kehidupan sehari-hari.
fig: table Jenis carita | Ciri ;; carpon | carita pondok nu asup akal ;; dongéng | carita rékaan baheula ;; novel | carita panjang ;; sasakala | asal-usul tempat ;; fabel | dongéng sato ;; legénda | carita tokoh jaman baheula ~ Jenis carita dina sastra Sunda.
@ Wawangsalan
min: 12
act: Dangukeun wawangsalan ti kolot, tuluy tebak maksud nu disumputkeun.
mis: mengira wawangsalan sama dengan paparikan
exp: Wawangsalan adalah salah satu jenis sisindiran. Dalam wawangsalan, maksud atau eusi disembunyikan seperti tebak-tebakan, sehingga pendengar harus menebak kata yang dimaksud dari cangkangnya. Jenis sisindiran lain adalah rarakitan dan paparikan.
ex: Wawangsalan ngandung tatarucingan. // Paparikan sorana mirip antara cangkang jeung eusi.
pt: Wawangsalan jenis sisindiran ; Maksudnya disumputkeun ; Mirip tebak-tebakan
sum: Wawangsalan melatih kecerdasan menebak.
fig: table Istilah | Hartina ;; sisindiran | wangun puisi Sunda heubeul ;; rarakitan | kecap awal cangkang jeung eusi sarua ;; paparikan | sora cangkang jeung eusi mirip ;; wawangsalan | maksud disumputkeun ;; cangkang | bagian kahiji ;; eusi | bagian maksud ~ Jenis jeung istilah sisindiran.
@ Tempat wisata di Jawa Barat
min: 12
act: Pilih hiji tempat wisata di Jawa Barat, tuluy jieun poster promosi basa Sunda.
mis: tertukar lokasi Kawah Putih dan Pangandaran
exp: Jawa Barat memiliki banyak tempat wisata alam dan budaya. Contohnya Tangkuban Parahu dan Kawah Putih di daerah Bandung, Pantai Pangandaran di selatan, Kebun Raya di Bogor, dan Gedung Saté di Kota Bandung. Saat berwisata kita menjaga kebersihan dan kelestarian tempatnya.
ex: Kawah Putih aya di Ciwidéy. // Kebun Raya aya di Bogor.
pt: Banyak wisata alam dan budaya ; Contoh Kawah Putih dan Pangandaran ; Jaga kebersihan saat berwisata
sum: Tempat wisata Jawa Barat perlu dijaga kelestariannya.
fig: table Tempat wisata | Ayana ;; Kawah Putih | Kabupatén Bandung ;; Pangandaran | basisir kidul Jawa Barat ;; Kebun Raya | Bogor ;; Gedung Saté | Kota Bandung ;; Tangkuban Parahu | wates Bandung Barat jeung Subang ;; Ujung Genteng | Sukabumi ~ Tempat wisata di Jawa Barat.
@ Pakéan adat Sunda
min: 12
act: Tingali poto kawinan atawa acara adat Sunda, tuluy sebutkeun pakéan nu dipaké.
mis: menyebut iket sebagai pakaian perempuan
exp: Pakaian adat Sunda antara lain kebaya untuk perempuan, beskap untuk laki-laki dalam acara resmi, dan pangsi yang berupa baju dan celana hitam. Laki-laki biasanya memakai iket atau ikat kepala, dan bagian bawah memakai samping atau sinjang berupa kain batik.
ex: Bapa maké iket jeung beskap. // Ibu maké kebaya jeung sinjang.
pt: Kebaya untuk perempuan ; Beskap dan iket untuk laki-laki ; Pangsi baju hitam sehari-hari
sum: Pakaian adat Sunda menunjukkan kekayaan budaya.
fig: table Pakéan | Katerangan ;; iket | tutup sirah lalaki ;; kebaya | baju awéwé ;; beskap | baju resmi lalaki ;; samping | kain dina cangkéng ;; pangsi | baju jeung calana hideung ;; sinjang | kain panjang batik ~ Pakéan adat Sunda.
@ Kalimah paréntah
min: 12
act: Tulis lima kalimah paréntah sopan pikeun di imah, contona Mangga calik.
mis: memakai kalimah paréntah kasar kepada orang tua
exp: Kalimah paréntah adalah kalimat untuk menyuruh, mengajak, atau melarang. Paréntah lemes dipakai kepada orang yang dihormati, misalnya Mangga calik. Paréntah loma dipakai kepada teman, misalnya Geura dahar. Larangan memakai kata ulah atau tong, dan ajakan memakai kata hayu.
ex: Hayu urang diajar babarengan. // Ulah ngaganggu adi nu keur saré.
pt: Kalimah paréntah untuk menyuruh ; Hayu untuk ajakan ; Ulah atau tong untuk larangan
sum: Pilih kalimah paréntah sesuai lawan bicara.
fig: table Kalimah | Jenisna ;; Mangga calik | paréntah lemes ;; Geura dahar | paréntah loma ;; Hayu urang ulin | ajakan ;; Ulah ngaganggu | larangan ;; Punten, tutupkeun pantona | paménta sopan ;; Tong miceun runtah | larangan loma ~ Jenis kalimah paréntah.
@ Kota di Jawa Barat
min: 12
act: Cari kota di Jawa Barat dina peta, tuluy sebutkeun kakhasanana.
mis: menyebut Bogor sebagai ibu kota Jawa Barat
exp: Jawa Barat terdiri atas banyak kabupaten dan kota. Ibu kota Provinsi Jawa Barat adalah Bandung. Setiap kota memiliki ciri khas, misalnya Bogor dikenal sebagai kota hujan, Garut terkenal dengan dodol, Cirebon dikenal sebagai kota udang, dan Tasikmalaya terkenal dengan kerajinan bordir.
ex: Bandung téh ibukota Jawa Barat. // Garut kawentar ku dodolna.
pt: Ibu kota Jawa Barat Bandung ; Setiap kota punya ciri khas ; Bogor kota hujan
sum: Mengenal kota di Jawa Barat menumbuhkan rasa cinta daerah.
fig: table Kota | Kawentar ku ;; Bandung | ibukota Jawa Barat ;; Bogor | kota hujan ;; Garut | dodol ;; Cirebon | kota udang ;; Tasikmalaya | kerajinan bordir ;; Sukabumi | mochi ~ Kota di Jawa Barat jeung kakhasanana.
"""

BANK += """
## SUN|Aksara swara
Aksara swara nyaéta aksara …|vokal|konsonan|angka|tanda baca|Aksara vokal.
Jumlah aksara swara aya …|7|18|5|20|Tujuh.
=|Aksara swara nu dipaké dina awal kecap ucing nyaéta …|u|U.
=|Aksara swara nu dipaké dina awal kecap awi nyaéta …|a|A.
B|Eu kaasup aksara swara.|Eu aksara swara.
S|Aksara swara sarua jeung aksara ngalagena.|Ngalagena konsonan.
Kecap nu dimimitian ku aksara swara i nyaéta …|iga|ucing|awi|oray|Iga.
Kecap oray dimimitian ku aksara swara …|o|a|u|eu|O.
## SUN|Watek pupuh
Pupuh nu watekna gumbira nyaéta …|Sinom|Maskumambang|Durma|Kinanti|Sinom.
Pupuh nu watekna sedih atawa nalangsa nyaéta …|Maskumambang|Sinom|Dangdanggula|Asmarandana|Maskumambang.
=|Pupuh nu watekna ambek nyaéta …|Durma|Durma.
=|Pupuh nu watekna tengtrem nyaéta …|Dangdanggula|Dangdanggula.
B|Asmarandana watekna kanyaah atawa kasih sayang.|Kanyaah.
S|Durma watekna gumbira.|Durma ambek.
Pupuh nu watekna prihatin atawa ngadagoan nyaéta …|Kinanti|Sinom|Durma|Dangdanggula|Kinanti.
Carita ngeunaan perang cocok ditembangkeun maké pupuh …|Durma|Kinanti|Asmarandana|Sinom|Ambek.
## SUN|Kecap rajékan
Kecap rajékan hartina …|kata ulang|kata sifat|kata tanya|kata bilangan|Kata ulang.
Kecap imah-imah kaasup rajékan …|dwimurni|dwireka|dwipurwa|trilingga|Diulang utuh.
=|Kecap bulak-balik kaasup rajékan …|dwireka|Dwireka.
=|Kecap tatanya kaasup rajékan …|dwipurwa|Dwipurwa.
B|Dar-der-dor kaasup rajékan trilingga.|Trilingga.
S|Kecap sasapu kaasup rajékan dwimurni.|Dwipurwa.
Rajékan nu diulang tilu kali bari robah sora disebut …|trilingga|dwimurni|dwipurwa|dwireka|Trilingga.
Conto rajékan dwimurni nyaéta …|budak-budak|bulak-balik|tatanya|dag-dig-dug|Diulang utuh.
## SUN|Unsur dongéng
Tokoh dina carita disebut …|palaku|latar|galur|amanat|Palaku.
Pesen nu aya dina carita disebut …|amanat|jejer|latar|galur|Amanat.
=|Tempat jeung waktu dina carita disebut …|latar|Latar.
=|Jalan carita disebut …|galur|Galur.
B|Jejer hartina téma carita.|Jejer téma.
S|Amanat sarua jeung judul carita.|Amanat pesan.
Dongéng nu nyaritakeun asal-usul hiji tempat disebut …|sasakala|fabel|carpon|novel|Sasakala.
Dina dongéng Sangkuriang, palakuna nyaéta Sangkuriang jeung …|Dayang Sumbi|Si Kabayan|Lutung Kasarung|Purbasari|Dayang Sumbi.
## SUN|Nulis surat pribadi
Tempat jeung tanggal dina surat disebut …|titimangsa|eusi|panutup|bubuka|Titimangsa.
Bagian surat nu ngandung maksud utama nyaéta …|eusi|titimangsa|salam|ngaran|Eusi.
=|Bagian surat sanggeus salam bubuka nyaéta …|bubuka|Bubuka.
=|Surat keur kulawarga atawa babaturan disebut surat …|pribadi|Surat pribadi.
B|Basa surat disaluyukeun jeung nu dikirim surat.|Disaluyukeun.
S|Titimangsa ditulis di tungtung surat sanggeus ngaran.|Di awal.
Kalimah sakitu heula seratan ti abdi kaasup bagian …|panutup|bubuka|eusi|titimangsa|Panutup.
Surat keur nini sabaiknya maké basa …|lemes|kasar|loma pisan|Inggris|Lemes.
## SUN|Paguneman
Paguneman hartina …|percakapan|nyanyian|tulisan|gambar|Percakapan.
Ucapan pikeun nganuhunkeun nyaéta …|hatur nuhun|hapunten|punten|wilujeng|Hatur nuhun.
=|Ucapan menta dihampura nyaéta …|hapunten|Hapunten.
=|Ucapan papanggih isuk-isuk nyaéta wilujeng …|énjing;enjing|Wilujeng énjing.
B|Dina paguneman urang kudu silih ganti nyarita.|Bergantian.
S|Ka kolot leuwih alus maké basa kasar.|Basa lemes.
Ucapan ngabagéakeun sémah nyaéta …|wilujeng sumping|hapunten|hatur nuhun|mangga ah|Wilujeng sumping.
Kumaha damang dipaké pikeun …|nanyakeun kaayaan|pamitan|menta dihampura|nganuhunkeun|Menanyakan kabar.
## SUN|Carita pondok
Carpon mangrupa singgetan tina …|carita pondok|carita panjang|carita pantun|carita sato|Carita pondok.
Bédana carpon jeung dongéng nyaéta carpon …|asup akal|loba kajadian gaib|tokohna sato wungkul|teu boga amanat|Asup akal.
=|Carita panjang dina sastra Sunda disebut …|novel|Novel.
=|Dongéng nu tokohna sato disebut …|fabel|Fabel.
B|Carpon boga palaku jeung amanat.|Unsur carita.
S|Carpon salawasna nyaritakeun hal gaib.|Asup akal.
Carita ngeunaan budak nu leungiteun sapédah kaasup …|carpon|fabel|sasakala|legénda|Carpon.
Carita tokoh jaman baheula disebut …|legénda|carpon|novel|warta|Legénda.
## SUN|Wawangsalan
Wawangsalan kaasup kana …|sisindiran|pupuh|carpon|warta|Sisindiran.
Dina wawangsalan, maksudna …|disumputkeun|ditulis jelas|teu aya|dihapus|Disumputkeun.
=|Sisindiran nu sora cangkang jeung eusina mirip disebut …|paparikan|Paparikan.
=|Sisindiran nu kecap awal cangkang jeung eusina sarua disebut …|rarakitan|Rarakitan.
B|Wawangsalan mirip tatarucingan.|Tebak-tebakan.
S|Wawangsalan sarua jeung pupuh.|Sisindiran.
Bagian kahiji sisindiran disebut …|cangkang|eusi|amanat|judul|Cangkang.
Bagian sisindiran nu ngandung maksud disebut …|eusi|cangkang|sora|padalisan|Eusi.
## SUN|Tempat wisata di Jawa Barat
Kawah Putih aya di …|Kabupatén Bandung|Bogor|Cirebon|Garut|Ciwidéy.
Kebun Raya aya di kota …|Bogor|Bandung|Sukabumi|Cirebon|Bogor.
=|Pantai di basisir kidul Jawa Barat nu kawentar nyaéta …|Pangandaran|Pangandaran.
=|Gedung Saté aya di kota …|Bandung|Bandung.
B|Ujung Genteng aya di Sukabumi.|Sukabumi.
S|Pangandaran téh gunung di Bogor.|Pantai di kidul.
Gunung nu aya patalina jeung dongéng Sangkuriang nyaéta …|Tangkuban Parahu|Gedé|Papandayan|Ciremai|Tangkuban Parahu.
Sikep nu hadé waktu wisata nyaéta …|ngajaga kabersihan|miceun runtah sambarangan|ngaruksak tutuwuhan|nyoréat batu|Kabersihan.
## SUN|Pakéan adat Sunda
Tutup sirah lalaki dina pakéan adat Sunda disebut …|iket|kebaya|samping|beskap|Iket.
Baju awéwé dina pakéan adat Sunda nyaéta …|kebaya|beskap|pangsi|iket|Kebaya.
=|Baju resmi lalaki dina pakéan adat Sunda nyaéta …|beskap|Beskap.
=|Baju jeung calana hideung urang lembur disebut …|pangsi|Pangsi.
B|Sinjang nyaéta kain panjang batik.|Sinjang.
S|Iket dipaké ku awéwé dina sirah.|Dipaké lalaki.
Kain nu dipaké dina cangkéng disebut …|samping|iket|kebaya|pangsi|Samping.
Pakéan adat nuduhkeun … budaya.|kabeungharan|kamiskinan|kasedih|kaambek|Kekayaan.
## SUN|Kalimah paréntah
Kalimah paréntah dipaké pikeun …|nitah, ngajak, atawa ngalarang|nanya|ngabéjakeun|nyaritakeun|Fungsi.
Kecap pikeun ngajak nyaéta …|hayu|ulah|tong|mangga|Hayu.
=|Kecap pikeun ngalarang nyaéta ulah atawa …|tong|Tong.
=|Paréntah lemes pikeun diuk nyaéta Mangga …|calik|Mangga calik.
B|Geura dahar kaasup paréntah loma.|Loma.
S|Hayu urang ulin kaasup larangan.|Ajakan.
Kalimah larangan nu merenah nyaéta …|Ulah ngaganggu adi nu keur saré.|Hayu urang ulin.|Mangga calik.|Geura dahar.|Larangan.
Ka kolot, urang sabaiknya maké paréntah …|lemes|kasar|loma|ambek|Lemes.
## SUN|Kota di Jawa Barat
Ibukota Jawa Barat nyaéta …|Bandung|Bogor|Cirebon|Garut|Bandung.
Kota nu disebut kota hujan nyaéta …|Bogor|Garut|Cirebon|Sukabumi|Bogor.
=|Garut kawentar ku kadaharan …|dodol|Dodol.
=|Kota nu disebut kota udang nyaéta …|Cirebon|Cirebon.
B|Tasikmalaya kawentar ku kerajinan bordir.|Bordir.
S|Sukabumi téh ibukota Jawa Barat.|Bandung.
Mochi téh kadaharan has ti …|Sukabumi|Garut|Bogor|Cirebon|Sukabumi.
Jawa Barat diwangun ku loba kabupatén jeung …|kota|nagara|pulo|buana|Kota.
"""

SAS += """
## SUN 1
0|Kecap éta dimimitian ku aksara swara ....|é|a|o|eu|É.
1|Pupuh Asmarandana watekna ....|kanyaah|ambek|nalangsa|gumbira|Kanyaah.
2|Kecap dag-dig-dug kaasup rajékan ....|trilingga|dwimurni|dwipurwa|dwireka|Trilingga.
3|Téma carita disebut ....|jejer|latar|palaku|galur|Jejer.
4|Kalimah Assalamualaikum dina surat kaasup ....|salam bubuka|eusi|titimangsa|panutup|Salam bubuka.
5|Ucapan waktu liwat di hareupeun kolot nyaéta ....|punten|hatur nuhun|wilujeng sumping|hapunten|Punten.
## SUN 2
0|Novel nyaéta carita nu ....|panjang|pondok pisan|teu boga palaku|ngan saalinéa|Panjang.
1|Sisindiran nu maksudna disumputkeun disebut ....|wawangsalan|rarakitan|paparikan|pupuh|Wawangsalan.
2|Tangkuban Parahu ayana di wates Bandung Barat jeung ....|Subang|Garut|Cirebon|Bogor|Subang.
3|Pangsi warnana ....|hideung|bodas|konéng|beureum|Hideung.
4|Punten, tutupkeun pantona kaasup kalimah ....|paménta sopan|larangan|ajakan|pananya|Paménta sopan.
5|Kota nu kawentar ku dodol nyaéta ....|Garut|Bogor|Cirebon|Sukabumi|Garut.
"""
