TOPICS = ""
BANK = ""
SAS = ""

TOPICS += """
## MAT
# 1|Bilangan sampai 1.000 dan Operasi Hitung
@ Membandingkan bilangan sampai 1.000
min: 10
act: Bandingkan harga dua barang di struk belanja, lalu tulis tanda lebih besar atau lebih kecil.
mis: membandingkan angka satuan lebih dulu
exp: Untuk membandingkan bilangan, lihat angka dari nilai tempat paling besar, yaitu ratusan. Jika ratusannya sama, bandingkan puluhan. Jika puluhannya juga sama, bandingkan satuan. Tanda > berarti lebih besar, tanda < berarti lebih kecil, dan tanda = berarti sama dengan.
ex: 452 > 425 karena puluhan 5 lebih besar dari 2. // 318 < 381.
pt: Bandingkan mulai dari ratusan ; Lalu puluhan, lalu satuan ; Gunakan tanda >, <, atau =
sum: Bilangan dibandingkan mulai dari nilai tempat terbesar.
fig: table Perbandingan | Tanda ;; 452 dan 425 | 452 > 425 ;; 318 dan 381 | 318 < 381 ;; 700 dan 699 | 700 > 699 ;; 256 dan 265 | 256 < 265 ;; 999 dan 909 | 999 > 909 ;; 140 dan 104 | 140 > 104 ~ Membandingkan bilangan sampai 1.000.
@ Pola bilangan loncat
min: 10
act: Hitung uang koin dengan loncat Rp100, lalu tulis polanya.
mis: menambah dengan bilangan yang berbeda-beda pada satu pola
exp: Pola bilangan loncat adalah barisan bilangan yang bertambah atau berkurang dengan jumlah yang sama. Contohnya loncat 5: 5, 10, 15, 20. Loncat 100: 100, 200, 300. Untuk melanjutkan pola, cari dulu selisih dua bilangan yang berurutan.
ex: 20, 40, 60, ... bilangan berikutnya 80. // 900, 800, 700, ... bilangan berikutnya 600.
pt: Cari selisih bilangan berurutan ; Selisihnya selalu sama ; Pola bisa naik atau turun
sum: Pola bilangan loncat memiliki selisih yang tetap.
fig: table Pola | Bilangan berikutnya ;; 5, 10, 15, 20 | 25 ;; 20, 40, 60, 80 | 100 ;; 100, 200, 300, 400 | 500 ;; 1.000, 900, 800, 700 | 600 ;; 3, 6, 9, 12 | 15 ;; 50, 100, 150, 200 | 250 ~ Melanjutkan pola bilangan loncat.
@ Penjumlahan bersusun dengan menyimpan
min: 10
act: Jumlahkan tabungan dua minggu dengan cara bersusun, lalu periksa dengan kalkulator.
mis: lupa menambahkan angka simpanan ke puluhan
exp: Pada penjumlahan bersusun, satuan ditulis sejajar dengan satuan, puluhan sejajar dengan puluhan, dan ratusan sejajar dengan ratusan. Hitung mulai dari satuan. Jika hasilnya 10 atau lebih, tulis satuannya dan simpan 1 ke tempat sebelah kiri.
ex: 258 + 134: 8 + 4 = 12, tulis 2 simpan 1. Hasilnya 392. // 476 + 285 = 761.
pt: Sejajarkan nilai tempat ; Hitung dari satuan ; Simpan 1 jika hasil 10 atau lebih
sum: Menyimpan membuat penjumlahan bersusun tepat.
fig: table Soal | Hasil ;; 258 + 134 | 392 ;; 476 + 285 | 761 ;; 347 + 125 | 472 ;; 199 + 201 | 400 ;; 568 + 47 | 615 ;; 685 + 248 | 933 ~ Contoh penjumlahan dengan menyimpan.
@ Pengurangan bersusun dengan meminjam
min: 10
act: Hitung sisa uang jajan setelah membeli sesuatu dengan pengurangan bersusun.
mis: mengurangkan angka yang besar dengan yang kecil tanpa melihat posisi
exp: Pada pengurangan bersusun, hitung mulai dari satuan. Jika angka atas lebih kecil dari angka bawah, pinjam 1 dari tempat sebelah kiri. Satu puluhan yang dipinjam bernilai 10 satuan. Periksa hasilnya dengan penjumlahan.
ex: 532 − 218: 2 kurang 8 tidak bisa, pinjam 1 puluhan menjadi 12 − 8 = 4. Hasilnya 314. // 700 − 256 = 444.
pt: Hitung dari satuan ; Pinjam 1 jika angka atas lebih kecil ; Periksa dengan penjumlahan
sum: Meminjam membantu mengurangkan bilangan dengan benar.
fig: table Soal | Hasil ;; 532 − 218 | 314 ;; 700 − 256 | 444 ;; 451 − 127 | 324 ;; 620 − 315 | 305 ;; 843 − 459 | 384 ;; 305 − 108 | 197 ~ Contoh pengurangan dengan meminjam.
@ Membulatkan ke ratusan terdekat
min: 10
act: Bulatkan harga barang di toko ke ratusan terdekat untuk menaksir total belanja.
mis: melihat angka satuan, bukan puluhan, saat membulatkan ke ratusan
exp: Untuk membulatkan ke ratusan terdekat, lihat angka puluhan. Jika puluhannya 0 sampai 4, bulatkan ke bawah. Jika puluhannya 5 sampai 9, bulatkan ke atas. Pembulatan membantu menaksir hasil hitung dengan cepat.
ex: 342 dibulatkan menjadi 300. // 467 dibulatkan menjadi 500.
pt: Lihat angka puluhan ; Puluhan 0 sampai 4 ke bawah ; Puluhan 5 sampai 9 ke atas
sum: Membulatkan ke ratusan melihat angka puluhan.
fig: table Bilangan | Dibulatkan ke ratusan ;; 342 | 300 ;; 467 | 500 ;; 150 | 200 ;; 812 | 800 ;; 689 | 700 ;; 935 | 900 ~ Contoh pembulatan ke ratusan terdekat.
@ Menghitung uang kembalian
min: 10
act: Bermain jual beli di rumah, lalu hitung uang kembalian setiap pembelian.
mis: menjumlahkan harga dan uang bayar, bukan mengurangkan
exp: Uang kembalian adalah sisa uang setelah membayar. Kembalian dihitung dengan uang yang dibayarkan dikurangi harga barang. Jika membeli beberapa barang, jumlahkan dulu harganya, lalu kurangkan dari uang yang dibayar.
ex: Harga Rp3.500, dibayar Rp5.000, kembaliannya Rp1.500. // Harga Rp2.000 + Rp4.500 = Rp6.500, dibayar Rp10.000, kembaliannya Rp3.500.
pt: Kembalian = uang bayar − harga ; Jumlahkan harga beberapa barang dulu ; Periksa dengan penjumlahan
sum: Menghitung kembalian memakai pengurangan.
fig: table Harga dan uang bayar | Kembalian ;; Rp3.500 dibayar Rp5.000 | Rp1.500 ;; Rp7.000 dibayar Rp10.000 | Rp3.000 ;; Rp1.200 dibayar Rp2.000 | Rp800 ;; Rp4.500 dibayar Rp5.000 | Rp500 ;; Rp8.500 dibayar Rp20.000 | Rp11.500 ;; Rp6.000 dibayar Rp10.000 | Rp4.000 ~ Menghitung uang kembalian.
# 2|Perkalian, Pecahan, dan Pengukuran
@ Tabel perkalian sampai 10
min: 10
act: Buat kartu perkalian 6 sampai 9, lalu minta keluarga menguji hafalanmu.
mis: tertukar hasil 7 × 8 dengan 7 × 6
exp: Tabel perkalian membantu kita menghitung dengan cepat. Perkalian bisa dihafal dengan pola, misalnya perkalian 5 selalu berakhir 0 atau 5, dan perkalian 10 selalu berakhir 0. Perkalian 9 bisa diingat karena jumlah angka hasilnya selalu 9, misalnya 9 × 3 = 27 dan 2 + 7 = 9.
ex: 6 × 7 = 42. // 9 × 4 = 36.
pt: Hafalkan dengan pola ; Perkalian 5 berakhir 0 atau 5 ; Perkalian 9 jumlah angkanya 9
sum: Hafal perkalian membuat berhitung lebih cepat.
fig: table Perkalian | Hasil ;; 6 × 7 | 42 ;; 7 × 8 | 56 ;; 8 × 9 | 72 ;; 9 × 6 | 54 ;; 7 × 7 | 49 ;; 8 × 8 | 64 ~ Contoh tabel perkalian.
@ Sifat pertukaran perkalian
min: 10
act: Susun 12 tutup botol menjadi 3 baris berisi 4, lalu ubah menjadi 4 baris berisi 3.
mis: mengira 3 × 4 dan 4 × 3 hasilnya berbeda
exp: Sifat pertukaran pada perkalian artinya urutan bilangan yang dikalikan boleh ditukar dan hasilnya tetap sama. Contohnya 3 × 4 = 12 dan 4 × 3 = 12. Sifat ini memudahkan kita menghafal perkalian.
ex: 2 × 9 = 9 × 2 = 18. // 5 × 6 = 6 × 5 = 30.
pt: Urutan perkalian boleh ditukar ; Hasilnya tetap sama ; Membantu menghafal
sum: Perkalian tetap sama walaupun urutannya ditukar.
fig: table Perkalian | Pasangan tukarnya ;; 3 × 4 | 4 × 3 ;; 2 × 9 | 9 × 2 ;; 5 × 6 | 6 × 5 ;; 7 × 3 | 3 × 7 ;; 8 × 2 | 2 × 8 ;; 4 × 9 | 9 × 4 ~ Pasangan perkalian yang hasilnya sama.
@ Mengenal pecahan sederhana
min: 10
act: Potong kue atau roti menjadi beberapa bagian sama besar, lalu sebutkan pecahannya.
mis: mengira bagian tidak sama besar bisa disebut pecahan
exp: Pecahan menunjukkan bagian dari keseluruhan yang dibagi sama besar. Pecahan ditulis dengan pembilang di atas dan penyebut di bawah. Penyebut menunjukkan banyak bagian seluruhnya, pembilang menunjukkan bagian yang diambil. Satu dari empat bagian ditulis 1/4.
ex: Pizza dipotong 8, dimakan 3: 3/8. // Kertas dilipat 2, diwarnai 1: 1/2.
pt: Bagian harus sama besar ; Penyebut banyak bagian seluruhnya ; Pembilang bagian yang diambil
sum: Pecahan menunjukkan bagian yang sama besar.
fig: table Bagian yang diambil | Pecahan ;; 1 dari 2 bagian | 1/2 ;; 1 dari 4 bagian | 1/4 ;; 3 dari 4 bagian | 3/4 ;; 2 dari 3 bagian | 2/3 ;; 3 dari 8 bagian | 3/8 ;; 1 dari 5 bagian | 1/5 ~ Bagian sama besar dan pecahannya.
@ Keliling bangun datar
min: 10
act: Ukur sisi-sisi meja belajar dengan meteran, lalu jumlahkan untuk mencari kelilingnya.
mis: mengalikan sisi padahal keliling adalah jumlah semua sisi
exp: Keliling bangun datar adalah jumlah panjang semua sisi yang membatasi bangun itu. Keliling persegi sama dengan 4 kali panjang sisi. Keliling persegi panjang sama dengan dua kali panjang ditambah dua kali lebar. Keliling segitiga adalah jumlah ketiga sisinya.
ex: Persegi sisi 5 cm: keliling 20 cm. // Persegi panjang 6 cm dan 4 cm: keliling 20 cm.
pt: Keliling = jumlah semua sisi ; Persegi: 4 × sisi ; Persegi panjang: 2 × (panjang + lebar)
sum: Keliling dihitung dengan menjumlahkan semua sisi.
fig: table Bangun dan ukuran | Keliling ;; persegi sisi 5 cm | 20 cm ;; persegi sisi 3 cm | 12 cm ;; persegi panjang 7 cm dan 4 cm | 22 cm ;; persegi panjang 8 cm dan 1 cm | 18 cm ;; segitiga 4 cm, 5 cm, 6 cm | 15 cm ;; persegi sisi 10 cm | 40 cm ~ Menghitung keliling bangun datar.
@ Satuan waktu jam dan menit
min: 10
act: Catat lama perjalanan dari rumah ke sekolah dalam menit selama satu minggu.
mis: mengira 1 jam sama dengan 100 menit
exp: Satu jam sama dengan 60 menit dan satu menit sama dengan 60 detik. Setengah jam sama dengan 30 menit, seperempat jam sama dengan 15 menit. Lama kegiatan dihitung dari waktu mulai sampai waktu selesai.
ex: 2 jam = 120 menit. // Mulai 07.00 selesai 07.45, lamanya 45 menit.
pt: 1 jam = 60 menit ; Setengah jam = 30 menit ; Seperempat jam = 15 menit
sum: Jam dan menit dipakai untuk menghitung lama kegiatan.
fig: table Waktu | Sama dengan ;; 1 jam | 60 menit ;; 2 jam | 120 menit ;; setengah jam | 30 menit ;; seperempat jam | 15 menit ;; 1 menit | 60 detik ;; 3 jam | 180 menit ~ Hubungan satuan waktu.
@ Diagram gambar
min: 10
act: Catat hewan peliharaan teman sekelas, lalu buat diagram gambar dengan satu gambar mewakili satu anak.
mis: tidak memperhatikan keterangan nilai satu gambar
exp: Diagram gambar atau piktogram menyajikan data dengan gambar. Setiap gambar mewakili jumlah tertentu yang ditulis pada keterangan. Jika satu gambar mewakili 2 anak, maka 4 gambar berarti 8 anak. Diagram gambar memudahkan membandingkan data.
ex: Keterangan 1 gambar = 2 buku. Ada 5 gambar, berarti 10 buku. // Baris yang gambarnya paling banyak adalah data terbanyak.
pt: Gambar mewakili data ; Baca keterangan nilai gambar ; Kalikan banyak gambar dengan nilainya
sum: Diagram gambar membuat data mudah dibaca.
fig: table Hewan peliharaan | Banyak gambar 🐾 ;; kucing | 6 gambar ;; ikan | 4 gambar ;; burung | 3 gambar ;; kelinci | 2 gambar ;; ayam | 5 gambar ;; hamster | 1 gambar ~ Piktogram hewan peliharaan, 1 gambar mewakili 2 anak.
"""

BANK += """
## MAT|Membandingkan bilangan sampai 1.000
Tanda yang tepat untuk 563 … 536 adalah …|>|<|=|+|Puluhan 6 lebih besar dari 3.
Bilangan terbesar di antara bilangan berikut adalah …|902|900|899|890|902 paling besar.
=|Tanda untuk 400 … 400 adalah …|=|Sama besar.
=|Bilangan terkecil dari 345, 354, 435 adalah …|345|Ratusan 3 dan puluhan 4.
B|Bilangan 710 lebih besar dari 701.|Puluhan 1 lebih besar dari 0.
S|Bilangan 289 lebih besar dari 298.|289 < 298.
Urutan dari yang terkecil adalah …|128, 182, 218|218, 182, 128|182, 128, 218|128, 218, 182|Bandingkan ratusan lalu puluhan.
Bilangan yang terletak di antara 450 dan 460 adalah …|455|445|465|540|455 di antaranya.
## MAT|Pola bilangan loncat
Bilangan berikutnya dari 15, 20, 25, 30 adalah …|35|31|40|45|Loncat 5.
Bilangan berikutnya dari 400, 350, 300, 250 adalah …|200|150|225|300|Turun 50.
=|Bilangan berikutnya dari 2, 4, 6, 8 adalah …|10|Loncat 2.
=|Selisih pada pola 10, 20, 30, 40 adalah …|10|Selalu bertambah 10.
B|Pola 7, 14, 21, 28 adalah loncat 7.|Selisih 7.
S|Pola 10, 20, 35, 50 memiliki selisih yang sama.|Selisih 10 lalu 15.
Bilangan yang hilang pada 100, 200, …, 400 adalah …|300|250|350|500|Loncat 100.
Pola loncat 4 dimulai dari 4 adalah …|4, 8, 12, 16|4, 6, 8, 10|4, 9, 14, 19|4, 5, 6, 7|Bertambah 4.
## MAT|Penjumlahan bersusun dengan menyimpan
Hasil dari 367 + 245 adalah …|612|512|602|622|7 + 5 = 12 simpan 1, 6 + 4 + 1 = 11 simpan 1.
Hasil dari 189 + 128 adalah …|317|307|217|327|Menyimpan dua kali.
=|Hasil dari 456 + 237 adalah …|693|6 + 7 = 13 simpan 1.
=|Hasil dari 99 + 99 adalah …|198|99 + 99 = 198.
B|Pada 48 + 35, satuan 8 + 5 = 13 sehingga kita menyimpan 1.|Simpan 1 puluhan.
S|Hasil 275 + 125 adalah 390.|Hasilnya 400.
Ani punya 238 kelereng dan mendapat 175 lagi. Kelereng Ani sekarang …|413|313|403|423|238 + 175 = 413.
Penjumlahan dimulai dari nilai tempat …|satuan|ratusan|puluhan|ribuan|Mulai dari satuan.
## MAT|Pengurangan bersusun dengan meminjam
Hasil dari 625 − 348 adalah …|277|323|287|377|Meminjam dua kali.
Hasil dari 500 − 125 adalah …|375|425|385|475|500 − 125 = 375.
=|Hasil dari 452 − 236 adalah …|216|2 kurang 6, pinjam 1 puluhan.
=|Satu puluhan yang dipinjam sama dengan … satuan.|10;sepuluh|1 puluhan = 10 satuan.
B|Pengurangan dapat diperiksa dengan penjumlahan.|Hasil + pengurang = bilangan awal.
S|Hasil 300 − 150 adalah 250.|Hasilnya 150.
Di perpustakaan ada 410 buku. Dipinjam 165 buku. Sisa buku …|245|255|345|235|410 − 165 = 245.
Pemeriksaan 532 − 218 = 314 yang benar adalah …|314 + 218 = 532|314 − 218 = 96|532 + 218 = 750|314 + 532 = 846|Hasil ditambah pengurang.
## MAT|Membulatkan ke ratusan terdekat
Bilangan 278 dibulatkan ke ratusan terdekat menjadi …|300|200|280|270|Puluhan 7 ke atas.
Bilangan 731 dibulatkan ke ratusan terdekat menjadi …|700|800|730|740|Puluhan 3 ke bawah.
=|Bilangan 550 dibulatkan ke ratusan terdekat menjadi …|600|Puluhan 5 ke atas.
=|Bilangan 420 dibulatkan ke ratusan terdekat menjadi …|400|Puluhan 2 ke bawah.
B|Bilangan 849 dibulatkan menjadi 800.|Puluhan 4 ke bawah.
S|Bilangan 361 dibulatkan menjadi 300.|Puluhan 6 dibulatkan ke atas menjadi 400.
Taksiran 312 + 489 dengan pembulatan ratusan adalah …|300 + 500 = 800|300 + 400 = 700|400 + 500 = 900|300 + 490 = 790|312 ke 300, 489 ke 500.
Angka yang dilihat saat membulatkan ke ratusan adalah angka …|puluhan|satuan|ratusan|ribuan|Lihat puluhan.
## MAT|Menghitung uang kembalian
Harga buku Rp6.500. Dibayar Rp10.000. Kembaliannya …|Rp3.500|Rp4.500|Rp16.500|Rp3.000|10.000 − 6.500.
Beli roti Rp2.500 dan susu Rp3.000, dibayar Rp10.000. Kembaliannya …|Rp4.500|Rp5.500|Rp5.000|Rp4.000|10.000 − 5.500.
=|Harga pensil Rp1.500, dibayar Rp2.000. Kembaliannya Rp …|500|2.000 − 1.500 = 500.
=|Harga mainan Rp15.000, dibayar Rp20.000. Kembaliannya Rp …|5.000;5000|20.000 − 15.000.
B|Kembalian dihitung dengan pengurangan.|Uang bayar − harga.
S|Kembalian dihitung dengan menjumlahkan harga dan uang bayar.|Harus dikurangkan.
Ibu membayar Rp50.000 untuk belanja Rp37.500. Kembaliannya …|Rp12.500|Rp13.500|Rp22.500|Rp87.500|50.000 − 37.500.
Jika uang bayar sama dengan harga, kembaliannya …|Rp0|Rp1.000|sama dengan harga|dua kali harga|Tidak ada kembalian.
## MAT|Tabel perkalian sampai 10
Hasil dari 7 × 6 adalah …|42|48|36|49|7 × 6 = 42.
Hasil dari 9 × 8 adalah …|72|81|64|63|9 × 8 = 72.
=|Hasil dari 8 × 7 adalah …|56|8 × 7 = 56.
=|Hasil dari 10 × 9 adalah …|90|10 × 9 = 90.
B|Hasil perkalian 5 selalu berakhir 0 atau 5.|Pola perkalian 5.
S|Hasil 6 × 6 adalah 32.|6 × 6 = 36.
Ada 8 kotak berisi 6 kue. Banyak kue seluruhnya …|48|14|42|56|8 × 6 = 48.
Jumlah angka pada hasil 9 × 7 adalah …|9|7|6|16|63, 6 + 3 = 9.
## MAT|Sifat pertukaran perkalian
Perkalian yang hasilnya sama dengan 6 × 8 adalah …|8 × 6|6 + 8|8 + 6|6 × 6|Sifat pertukaran.
Jika 7 × 4 = 28, maka 4 × 7 = …|28|11|47|21|Hasilnya tetap sama.
=|Lengkapi: 5 × 9 = 9 × …|5|Ditukar urutannya.
=|Hasil 3 × 9 sama dengan hasil 9 × …|3|Sifat pertukaran.
B|2 × 7 sama dengan 7 × 2.|Hasilnya sama 14.
S|8 × 3 lebih besar dari 3 × 8.|Hasilnya sama 24.
Susunan 3 baris berisi 5 kursi sama banyak dengan …|5 baris berisi 3 kursi|3 baris berisi 3 kursi|5 baris berisi 5 kursi|8 baris berisi 1 kursi|3 × 5 = 5 × 3.
Sifat yang menyatakan a × b = b × a disebut sifat …|pertukaran|pengelompokan|penyebaran|pengurangan|Sifat pertukaran.
## MAT|Mengenal pecahan sederhana
Pada pecahan 2/5, angka 5 disebut …|penyebut|pembilang|hasil|sisa|5 di bawah adalah penyebut.
Kue dipotong 6 sama besar dan dimakan 1. Pecahan yang dimakan …|1/6|6/1|5/6|1/5|Satu dari enam bagian.
=|Pada pecahan 3/4, pembilangnya adalah …|3|Angka atas pembilang.
=|Setengah ditulis dalam pecahan …|1/2|Satu dari dua bagian.
B|Bagian pecahan harus sama besar.|Bagian sama besar.
S|Pada pecahan 1/3, angka 1 disebut penyebut.|1 adalah pembilang.
Lingkaran dibagi 4 sama besar, 3 bagian diwarnai. Pecahannya …|3/4|1/4|4/3|3/1|3 dari 4.
Pecahan yang lebih besar dari 1/4 adalah …|1/2|1/8|1/6|1/5|Penyebut lebih kecil, bagian lebih besar.
## MAT|Keliling bangun datar
Keliling persegi dengan sisi 6 cm adalah …|24 cm|12 cm|36 cm|18 cm|4 × 6.
Keliling persegi panjang 10 cm dan 5 cm adalah …|30 cm|15 cm|50 cm|25 cm|2 × (10 + 5).
=|Keliling segitiga dengan sisi 4 cm, 4 cm, dan 4 cm adalah … cm.|12|4 + 4 + 4.
=|Keliling persegi dengan sisi 7 cm adalah … cm.|28|4 × 7.
B|Keliling adalah jumlah panjang semua sisi.|Pengertian keliling.
S|Keliling persegi sisi 2 cm adalah 4 cm.|4 × 2 = 8 cm.
Pak Tani memagari kebun persegi bersisi 9 m. Panjang pagar …|36 m|18 m|81 m|27 m|4 × 9.
Rumus keliling persegi adalah …|4 × sisi|sisi × sisi|2 × sisi|sisi + sisi|4 × sisi.
## MAT|Satuan waktu jam dan menit
Setengah jam sama dengan … menit.|30|50|15|60|60 : 2.
Dua jam sama dengan … menit.|120|200|100|60|2 × 60.
=|Seperempat jam sama dengan … menit.|15|60 : 4.
=|Satu menit sama dengan … detik.|60|1 menit = 60 detik.
B|1 jam 30 menit sama dengan 90 menit.|60 + 30.
S|1 jam sama dengan 100 menit.|1 jam = 60 menit.
Rudi belajar mulai pukul 16.00 sampai 17.15. Lama Rudi belajar …|1 jam 15 menit|1 jam|45 menit|2 jam 15 menit|17.15 − 16.00.
Film berlangsung 90 menit. Lamanya sama dengan …|1 jam 30 menit|1 jam|2 jam|1 jam 50 menit|90 = 60 + 30.
## MAT|Diagram gambar
Diagram gambar disebut juga …|piktogram|diagram batang|tabel|grafik garis|Piktogram.
Keterangan 1 gambar = 2 buku. Ada 6 gambar. Banyak buku …|12|6|8|3|6 × 2.
=|Keterangan 1 gambar = 5 anak. Ada 3 gambar. Banyak anak …|15|3 × 5.
=|Keterangan 1 gambar = 10 kue. Ada 4 gambar. Banyak kue …|40|4 × 10.
B|Pada piktogram, gambar mewakili data.|Gambar mewakili jumlah.
S|Keterangan nilai gambar tidak perlu dibaca.|Keterangan harus dibaca.
Baris dengan gambar paling sedikit menunjukkan data …|paling sedikit|paling banyak|sama banyak|tidak ada|Gambar sedikit, data sedikit.
Keterangan 1 gambar = 2 apel. Untuk 8 apel diperlukan … gambar.|4|8|2|16|8 : 2.
"""

SAS += """
## MAT 1
0|Tanda yang tepat untuk 608 ... 680 adalah ....|<|>|=|+|Puluhan 0 lebih kecil dari 8.
1|Bilangan berikutnya dari 25, 50, 75, 100 adalah ....|125|110|150|105|Loncat 25.
2|Hasil dari 385 + 268 adalah ....|653|553|643|663|Menyimpan dua kali.
3|Hasil dari 800 − 365 adalah ....|435|535|445|465|800 − 365.
4|Bilangan 652 dibulatkan ke ratusan terdekat menjadi ....|700|600|650|660|Puluhan 5 ke atas.
5|Harga es krim Rp4.000. Dibayar Rp5.000. Kembaliannya ....|Rp1.000|Rp9.000|Rp4.000|Rp500|5.000 − 4.000.
## MAT 2
0|Hasil dari 8 × 6 adalah ....|48|56|42|54|8 × 6 = 48.
1|Perkalian yang hasilnya sama dengan 9 × 3 adalah ....|3 × 9|9 + 3|9 × 9|3 × 3|Sifat pertukaran.
2|Pita dipotong 5 sama panjang, diambil 2 bagian. Pecahannya ....|2/5|5/2|3/5|2/3|2 dari 5.
3|Keliling persegi panjang 7 cm dan 3 cm adalah ....|20 cm|10 cm|21 cm|14 cm|2 × (7 + 3).
4|Satu jam lebih 20 menit sama dengan ....|80 menit|120 menit|60 menit|100 menit|60 + 20.
5|Keterangan 1 gambar = 3 anak. Ada 5 gambar. Banyak anak ....|15|8|5|3|5 × 3.
"""

TOPICS += """
## BIN
# 1|Kata, Kalimat, dan Cerita
@ Kata depan di, ke, dan dari
min: 10
act: Tulis tiga kalimat tentang perjalananmu ke sekolah memakai kata depan di, ke, dan dari.
mis: menulis kata depan di serangkai dengan nama tempat, misalnya dipasar
exp: Kata depan di, ke, dan dari dipakai sebelum kata yang menunjukkan tempat. Di menunjukkan keberadaan, ke menunjukkan tujuan, dan dari menunjukkan asal. Kata depan ditulis terpisah dari kata yang mengikutinya, misalnya di sekolah, ke pasar, dan dari rumah.
ex: Ibu pergi ke pasar. // Adik pulang dari sekolah.
pt: Di untuk keberadaan ; Ke untuk tujuan, dari untuk asal ; Ditulis terpisah
sum: Kata depan menunjukkan tempat dan ditulis terpisah.
fig: table Kalimat | Kata depan ;; Buku ada di meja. | di ;; Kami pergi ke kebun. | ke ;; Ayah pulang dari kantor. | dari ;; Kucing tidur di bawah kursi. | di bawah ;; Bola menggelinding ke dalam selokan. | ke dalam ;; Air menetes dari atas genting. | dari atas ~ Pemakaian kata depan.
@ Kata berimbuhan me-
min: 10
act: Cari lima kata berimbuhan me- di buku cerita, lalu tulis kata dasarnya.
mis: menulis menyapu dari kata dasar menyapu
exp: Imbuhan me- ditambahkan pada kata dasar untuk membentuk kata kerja. Bentuknya bisa berubah menjadi mem-, men-, meng-, atau meny-, tergantung huruf awal kata dasar. Contohnya sapu menjadi menyapu, baca menjadi membaca, tulis menjadi menulis, dan gambar menjadi menggambar.
ex: Kakak membaca buku cerita. // Adik menggambar pemandangan.
pt: Me- membentuk kata kerja ; Bisa berubah menjadi mem-, men-, meng-, meny- ; Cari kata dasarnya
sum: Imbuhan me- mengubah kata dasar menjadi kata kerja.
fig: table Kata dasar | Berimbuhan me- ;; baca | membaca ;; tulis | menulis ;; sapu | menyapu ;; gambar | menggambar ;; lukis | melukis ;; dengar | mendengar ~ Kata dasar dan kata berimbuhan me-.
@ Kalimat seru
min: 10
act: Ucapkan tiga kalimat seru saat melihat hal yang menakjubkan di sekitar rumah.
mis: menulis kalimat seru dengan tanda titik
exp: Kalimat seru adalah kalimat yang mengungkapkan perasaan kuat, seperti kagum, terkejut, senang, atau sedih. Kalimat seru sering memakai kata wah, aduh, hore, dan alangkah. Kalimat seru diakhiri dengan tanda seru (!).
ex: Wah, indah sekali pelangi itu! // Aduh, kakiku terinjak!
pt: Mengungkapkan perasaan kuat ; Memakai kata wah, aduh, hore ; Diakhiri tanda seru
sum: Kalimat seru menunjukkan perasaan dengan tanda seru.
fig: table Kalimat seru | Perasaan ;; Wah, bagus sekali gambarmu! | kagum ;; Aduh, tanganku tergores! | sakit ;; Hore, kita menang! | senang ;; Astaga, rumahnya terbakar! | terkejut ;; Alangkah indahnya laut itu! | takjub ;; Sayang sekali, acaranya batal! | kecewa ~ Kalimat seru dan perasaannya.
@ Membaca nyaring
min: 10
act: Bacakan satu halaman cerita dengan nyaring untuk keluargamu, lalu minta mereka memberi nilai.
mis: membaca terlalu cepat tanpa berhenti di tanda baca
exp: Membaca nyaring adalah membaca dengan suara keras supaya didengar orang lain. Saat membaca nyaring, perhatikan lafal yang jelas, intonasi yang tepat, dan jeda pada tanda baca. Berhenti sebentar pada tanda koma dan lebih lama pada tanda titik.
ex: Suara naik pada kalimat tanya. // Berhenti sebentar pada tanda koma.
pt: Lafal jelas ; Intonasi tepat ; Jeda pada tanda baca
sum: Membaca nyaring yang baik mudah dipahami pendengar.
fig: table Hal yang diperhatikan | Penjelasan ;; lafal | pengucapan kata yang jelas ;; intonasi | naik turun suara ;; jeda | berhenti pada tanda baca ;; volume | suara cukup keras ;; tempo | tidak terlalu cepat ;; sikap | berdiri tegak memegang buku ~ Hal penting saat membaca nyaring.
@ Cerita rakyat Nusantara
min: 10
act: Minta kakek atau nenek menceritakan cerita rakyat dari daerahnya, lalu tulis tokohnya.
mis: mengira cerita rakyat adalah berita nyata
exp: Cerita rakyat adalah cerita yang berkembang di masyarakat dan diceritakan turun-temurun. Cerita rakyat sering menjelaskan asal-usul tempat atau mengajarkan nilai kebaikan. Contohnya Malin Kundang, Timun Mas, dan Sangkuriang.
ex: Malin Kundang mengajarkan berbakti kepada ibu. // Sangkuriang menceritakan asal-usul Gunung Tangkuban Perahu.
pt: Diceritakan turun-temurun ; Sering tentang asal-usul ; Mengandung pesan baik
sum: Cerita rakyat adalah warisan budaya yang berisi nasihat.
fig: table Cerita rakyat | Daerah asal ;; Malin Kundang | Sumatera Barat ;; Sangkuriang | Jawa Barat ;; Timun Mas | Jawa Tengah ;; Danau Toba | Sumatera Utara ;; Keong Mas | Jawa Timur ;; Batu Menangis | Kalimantan Barat ~ Cerita rakyat dan daerah asalnya.
@ Puisi dan rima
min: 10
act: Buat puisi empat baris tentang ibu dengan bunyi akhir yang sama.
mis: mengira puisi harus selalu panjang
exp: Puisi adalah karya sastra dengan bahasa yang indah. Puisi tersusun atas baris dan bait. Rima adalah persamaan bunyi, biasanya pada akhir baris. Rima membuat puisi enak didengar saat dibacakan.
ex: Bulan bersinar terang, hatiku pun senang. // Kata terang dan senang berima ang.
pt: Puisi terdiri atas baris dan bait ; Rima adalah persamaan bunyi ; Rima membuat puisi indah
sum: Rima membuat puisi enak didengar.
fig: table Kata | Kata yang berima ;; bulan | jalan ;; senang | tenang ;; hari | pagi ;; bunga | warna ;; sekolah | indah ;; ibu | rindu ~ Pasangan kata yang berima.
# 2|Informasi dan Pengalaman
@ Teks petunjuk penggunaan
min: 10
act: Baca petunjuk pada kemasan obat nyamuk atau sabun, lalu jelaskan kepada adik.
mis: melewatkan langkah karena tidak membaca petunjuk dengan urut
exp: Teks petunjuk penggunaan menjelaskan cara memakai suatu barang dengan aman. Teks ini berisi langkah-langkah yang berurutan dan sering memakai kata kerja perintah. Petunjuk biasanya ada pada kemasan barang atau buku panduan.
ex: Kocok dahulu sebelum diminum. // Simpan di tempat yang sejuk dan kering.
pt: Menjelaskan cara memakai barang ; Langkahnya berurutan ; Memakai kata kerja perintah
sum: Membaca petunjuk membuat kita memakai barang dengan benar.
fig: table Barang | Petunjuk ;; sirup obat | kocok dahulu ;; pasta gigi | tutup kembali setelah dipakai ;; senter | pasang baterai sesuai tanda ;; sabun cair | tekan pompa perlahan ;; payung | buka di luar ruangan ;; termometer | bersihkan sebelum dipakai ~ Contoh petunjuk penggunaan barang.
@ Wawancara sederhana
min: 10
act: Wawancarai ayah atau ibu tentang pekerjaannya dengan lima pertanyaan.
mis: bertanya tanpa menyiapkan daftar pertanyaan
exp: Wawancara adalah kegiatan tanya jawab untuk mendapatkan informasi dari narasumber. Sebelum wawancara, siapkan daftar pertanyaan dengan kata tanya apa, siapa, kapan, di mana, mengapa, dan bagaimana. Saat wawancara, bersikap sopan dan catat jawabannya.
ex: Sejak kapan Ibu menjadi guru? // Mengapa Ayah memilih menjadi petani?
pt: Wawancara adalah tanya jawab ; Siapkan pertanyaan ; Bersikap sopan dan mencatat
sum: Wawancara membantu kita mendapat informasi langsung.
fig: table Bagian wawancara | Kegiatan ;; sebelum | menyiapkan pertanyaan ;; pembuka | memberi salam ;; inti | bertanya dan mencatat ;; penutup | mengucapkan terima kasih ;; narasumber | orang yang ditanya ;; pewawancara | orang yang bertanya ~ Langkah dan istilah wawancara.
@ Kata baku dan tidak baku
min: 10
act: Cari kata tidak baku di percakapan sehari-hari, lalu tulis bentuk bakunya.
mis: menulis apotik padahal bentuk bakunya apotek
exp: Kata baku adalah kata yang sesuai dengan kaidah bahasa Indonesia dan tercantum dalam kamus. Kata tidak baku sering dipakai dalam percakapan sehari-hari. Dalam tulisan resmi, seperti surat dan laporan, kita memakai kata baku.
ex: Kata baku: apotek, bukan apotik. // Kata baku: nasihat, bukan nasehat.
pt: Kata baku sesuai kaidah ; Kata tidak baku untuk percakapan santai ; Tulisan resmi memakai kata baku
sum: Gunakan kata baku saat menulis resmi.
fig: table Tidak baku | Baku ;; apotik | apotek ;; nasehat | nasihat ;; sekedar | sekadar ;; karir | karier ;; jadual | jadwal ;; resiko | risiko ~ Kata tidak baku dan bentuk bakunya.
@ Ide pokok paragraf
min: 10
act: Baca satu paragraf di koran anak, lalu tulis ide pokoknya dalam satu kalimat.
mis: memilih kalimat contoh sebagai ide pokok
exp: Ide pokok adalah gagasan utama dalam paragraf. Ide pokok terdapat pada kalimat utama, yang biasanya ada di awal atau akhir paragraf. Kalimat lain disebut kalimat penjelas karena menjelaskan ide pokok.
ex: Paragraf tentang manfaat sayur, ide pokoknya sayur bermanfaat bagi tubuh. // Kalimat penjelas berisi contoh sayuran dan vitaminnya.
pt: Ide pokok gagasan utama ; Terdapat pada kalimat utama ; Kalimat lain menjelaskan
sum: Ide pokok adalah inti dari sebuah paragraf.
fig: table Istilah | Arti ;; ide pokok | gagasan utama paragraf ;; kalimat utama | kalimat berisi ide pokok ;; kalimat penjelas | kalimat pendukung ide pokok ;; paragraf | kumpulan kalimat satu gagasan ;; letak awal | kalimat utama di depan ;; letak akhir | kalimat utama di belakang ~ Istilah dalam paragraf.
@ Menulis buku harian
min: 10
act: Tulis buku harian setiap malam selama satu minggu tentang kegiatanmu.
mis: tidak menuliskan tanggal pada buku harian
exp: Buku harian adalah catatan pengalaman pribadi setiap hari. Buku harian ditulis dengan menyebut hari dan tanggal, kejadian penting, serta perasaan kita. Bahasanya bebas dan jujur karena ditulis untuk diri sendiri.
ex: Senin, 3 Maret. Hari ini aku belajar bersepeda. Aku senang sekali. // Rabu, 5 Maret. Aku menjenguk teman yang sakit.
pt: Tulis hari dan tanggal ; Ceritakan kejadian penting ; Ungkapkan perasaan dengan jujur
sum: Buku harian menyimpan kenangan dan melatih menulis.
fig: table Bagian buku harian | Contoh ;; hari dan tanggal | Senin, 3 Maret ;; sapaan | Dear diary ;; kejadian | belajar bersepeda ;; perasaan | senang sekali ;; harapan | besok bisa lebih lancar ;; penutup | sampai jumpa besok ~ Bagian-bagian buku harian.
@ Kalimat pujian dan ucapan selamat
min: 10
act: Tulis kartu ucapan selamat untuk teman yang berulang tahun.
mis: memberi pujian yang berlebihan dan tidak tulus
exp: Kalimat pujian diucapkan untuk menghargai kebaikan atau prestasi orang lain. Ucapan selamat diucapkan saat orang lain berbahagia, misalnya ulang tahun, juara lomba, atau naik kelas. Pujian dan ucapan selamat harus tulus dan sopan.
ex: Gambarmu bagus sekali! // Selamat ulang tahun, semoga sehat selalu.
pt: Pujian untuk menghargai ; Ucapan selamat saat berbahagia ; Ucapkan dengan tulus
sum: Pujian dan ucapan selamat membuat orang lain senang.
fig: table Peristiwa | Ucapan ;; ulang tahun | selamat ulang tahun ;; juara lomba | selamat atas kemenanganmu ;; naik kelas | selamat naik kelas ;; gambar bagus | gambarmu indah sekali ;; nilai tinggi | hebat, kamu rajin belajar ;; hari raya | selamat hari raya ~ Ucapan sesuai peristiwa.
"""

BANK += """
## BIN|Kata depan di, ke, dan dari
Penulisan kata depan yang benar adalah …|di sekolah|disekolah|di-sekolah|dsekolah|Kata depan ditulis terpisah.
Kata depan yang menunjukkan tujuan adalah …|ke|di|dari|pada|Ke menunjukkan tujuan.
=|Ayah baru pulang … kantor. Kata depan yang tepat adalah …|dari|Menunjukkan asal.
=|Kucing tidur … atas kasur. Kata depan yang tepat adalah …|di|Menunjukkan tempat.
B|Kata depan ke pada ke pasar ditulis terpisah.|Ditulis terpisah.
S|Penulisan dirumah sudah benar sebagai kata depan.|Seharusnya di rumah.
Kalimat yang penulisan kata depannya benar adalah …|Adik bermain di halaman.|Adik bermain dihalaman.|Adik bermain dari-halaman.|Adik bermain kehalaman.|Di halaman terpisah.
Kata depan yang menunjukkan asal adalah …|dari|ke|di|untuk|Dari menunjukkan asal.
## BIN|Kata berimbuhan me-
Kata dasar dari menulis adalah …|tulis|nulis|menulis|tulisan|Kata dasarnya tulis.
Kata sapu mendapat imbuhan me- menjadi …|menyapu|mensapu|mesapu|mengsapu|Huruf s luluh menjadi ny.
=|Kata baca mendapat imbuhan me- menjadi …|membaca|Me- menjadi mem-.
=|Kata dasar dari menggambar adalah …|gambar|Kata dasarnya gambar.
B|Imbuhan me- membentuk kata kerja.|Contoh membaca.
S|Kata dasar dari menyapu adalah nyapu.|Kata dasarnya sapu.
Kata dengar mendapat imbuhan me- menjadi …|mendengar|medengar|mengdengar|memdengar|Me- menjadi men-.
Kalimat yang memakai kata berimbuhan me- adalah …|Ibu memasak sayur.|Ibu ke pasar.|Ibu baik hati.|Ibu di dapur.|Memasak berimbuhan me-.
## BIN|Kalimat seru
Tanda baca di akhir kalimat seru adalah …|tanda seru|tanda tanya|tanda titik|tanda koma|Kalimat seru diakhiri !.
Kalimat seru yang menunjukkan rasa senang adalah …|Hore, aku juara!|Aduh, sakit!|Astaga, banjir!|Sayang sekali, gagal!|Hore menunjukkan senang.
=|Kata seru yang menunjukkan rasa sakit adalah …|aduh|Aduh untuk sakit.
=|Kalimat Wah, indah sekali! menunjukkan perasaan …|kagum|Kagum.
B|Kalimat seru mengungkapkan perasaan kuat.|Perasaan kuat.
S|Kalimat seru diakhiri dengan tanda tanya.|Diakhiri tanda seru.
Kalimat seru yang benar adalah …|Wah, besar sekali gajah itu!|Wah, besar sekali gajah itu?|wah besar sekali gajah itu.|Wah besar sekali, gajah itu|Diakhiri tanda seru.
Kata seru yang menunjukkan terkejut adalah …|astaga|hore|asyik|horee menang|Astaga untuk terkejut.
## BIN|Membaca nyaring
Membaca nyaring artinya membaca dengan suara …|keras dan jelas|dalam hati|berbisik|sambil bernyanyi|Keras dan jelas.
Naik turunnya suara saat membaca disebut …|intonasi|lafal|jeda|volume|Intonasi.
=|Pengucapan kata yang jelas disebut …|lafal|Lafal.
=|Berhenti sejenak pada tanda baca disebut …|jeda|Jeda.
B|Saat membaca nyaring kita berhenti sebentar pada tanda koma.|Jeda koma.
S|Membaca nyaring sebaiknya secepat mungkin.|Tempo tidak terlalu cepat.
Suara pada akhir kalimat tanya saat dibaca biasanya …|naik|turun|hilang|berbisik|Kalimat tanya naik.
Sikap yang baik saat membaca nyaring di depan kelas adalah …|berdiri tegak dan menghadap pendengar|menutup wajah dengan buku|membelakangi teman|duduk di lantai|Sikap tegak.
## BIN|Cerita rakyat Nusantara
Cerita rakyat Malin Kundang berasal dari …|Sumatera Barat|Jawa Barat|Bali|Papua|Malin Kundang dari Sumatera Barat.
Pesan cerita Malin Kundang adalah …|berbakti kepada ibu|boleh durhaka|suka berbohong|malas bekerja|Berbakti kepada ibu.
=|Cerita rakyat Sangkuriang berasal dari Jawa …|Barat|Sangkuriang dari Jawa Barat.
=|Cerita rakyat diceritakan secara turun- …|temurun|Turun-temurun.
B|Cerita rakyat sering menceritakan asal-usul suatu tempat.|Asal-usul tempat.
S|Cerita rakyat adalah berita dari koran hari ini.|Cerita rakyat warisan lama.
Cerita Sangkuriang menceritakan asal-usul …|Gunung Tangkuban Perahu|Danau Toba|Gunung Bromo|Pulau Bali|Tangkuban Perahu.
Tokoh yang melawan raksasa dengan biji mentimun adalah …|Timun Mas|Malin Kundang|Sangkuriang|Bawang Merah|Timun Mas.
## BIN|Puisi dan rima
Persamaan bunyi pada akhir baris puisi disebut …|rima|bait|judul|tema|Rima.
Kumpulan baris dalam puisi disebut …|bait|rima|paragraf|bab|Bait.
=|Kata yang berima dengan senang adalah …|tenang;menang;terang|Bunyi akhir ang.
=|Kata yang berima dengan hari adalah …|pagi;lari;nari|Bunyi akhir i.
B|Rima membuat puisi enak didengar.|Indah didengar.
S|Puisi harus terdiri atas sepuluh bait.|Panjang puisi bebas.
Pasangan kata yang berima adalah …|bulan dan jalan|bulan dan bintang|matahari dan pagi|air dan api|Akhiran an.
Bahasa dalam puisi biasanya …|indah|kasar|asal-asalan|membingungkan|Bahasa indah.
## BIN|Teks petunjuk penggunaan
Teks petunjuk penggunaan berisi …|cara memakai suatu barang|cerita dongeng|puisi|berita olahraga|Cara memakai barang.
Kata yang sering dipakai dalam teks petunjuk adalah kata …|perintah|seru|tanya|sapaan|Kata perintah.
=|Sirup obat biasanya harus … dahulu sebelum diminum.|dikocok|Kocok dahulu.
=|Langkah dalam teks petunjuk harus …|berurutan;urut|Berurutan.
B|Petunjuk penggunaan biasanya ada pada kemasan barang.|Pada kemasan.
S|Petunjuk penggunaan tidak perlu dibaca sebelum memakai barang.|Harus dibaca.
Contoh kalimat petunjuk adalah …|Simpan di tempat yang kering.|Aku suka sabun ini.|Sabun ini harum sekali!|Mengapa sabun berbusa?|Kalimat perintah.
Akibat tidak membaca petunjuk adalah …|barang bisa rusak|barang menjadi awet|kita menjadi pandai|barang bertambah|Salah pakai.
## BIN|Wawancara sederhana
Orang yang diwawancarai disebut …|narasumber|pewawancara|penonton|pembaca|Narasumber.
Sebelum wawancara, kita menyiapkan …|daftar pertanyaan|hadiah|makanan|mainan|Daftar pertanyaan.
=|Orang yang bertanya dalam wawancara disebut …|pewawancara|Pewawancara.
=|Wawancara ditutup dengan mengucapkan terima …|kasih|Terima kasih.
B|Saat wawancara kita mencatat jawaban narasumber.|Mencatat jawaban.
S|Pewawancara boleh memotong pembicaraan narasumber dengan kasar.|Harus sopan.
Pertanyaan wawancara yang menanyakan alasan memakai kata tanya …|mengapa|siapa|kapan|di mana|Mengapa.
Wawancara adalah kegiatan …|tanya jawab|menyanyi|menggambar|berolahraga|Tanya jawab.
## BIN|Kata baku dan tidak baku
Kata baku dari apotik adalah …|apotek|apotik|apotike|apotiks|Apotek.
Kata baku dari resiko adalah …|risiko|resiko|resikho|risikho|Risiko.
=|Kata baku dari nasehat adalah …|nasihat|Nasihat.
=|Kata baku dari jadual adalah …|jadwal|Jadwal.
B|Kata baku dipakai dalam tulisan resmi.|Tulisan resmi.
S|Karir adalah bentuk kata baku.|Bentuk baku karier.
Kalimat yang memakai kata baku adalah …|Ibu membeli obat di apotek.|Ibu membeli obat di apotik.|Ibu beli obat di apotik.|Ibu belanja obat di apotik.|Apotek baku.
Kata baku dari sekedar adalah …|sekadar|sekedar|sekedarnya|sekadarnya saja|Sekadar.
## BIN|Ide pokok paragraf
Gagasan utama sebuah paragraf disebut …|ide pokok|kalimat penjelas|judul buku|tanda baca|Ide pokok.
Ide pokok terdapat pada kalimat …|utama|penjelas|tanya|seru|Kalimat utama.
=|Kalimat yang menjelaskan ide pokok disebut kalimat …|penjelas|Kalimat penjelas.
=|Satu paragraf memiliki … ide pokok.|satu;1|Satu ide pokok.
B|Kalimat utama bisa terletak di akhir paragraf.|Awal atau akhir.
S|Kalimat penjelas berisi gagasan utama.|Kalimat utama berisi gagasan utama.
Paragraf berisi: Kucing hewan peliharaan yang lucu. Bulunya lembut. Matanya bulat. Ide pokoknya …|kucing hewan peliharaan yang lucu|bulu kucing lembut|mata kucing bulat|kucing suka ikan|Kalimat pertama.
Kalimat utama biasanya bersifat …|umum|sangat rinci|pertanyaan|seruan|Kalimat umum.
## BIN|Menulis buku harian
Buku harian berisi …|pengalaman pribadi sehari-hari|berita nasional|resep masakan|soal ulangan|Pengalaman pribadi.
Bagian yang ditulis paling awal dalam buku harian adalah …|hari dan tanggal|perasaan|harapan|penutup|Hari dan tanggal.
=|Buku harian ditulis dengan … karena untuk diri sendiri.|jujur|Ditulis jujur.
=|Selain kejadian, buku harian juga berisi … kita.|perasaan|Perasaan.
B|Menulis buku harian melatih kemampuan menulis.|Melatih menulis.
S|Buku harian harus ditulis dengan bahasa resmi seperti surat dinas.|Bahasanya bebas.
Kalimat buku harian yang mengungkapkan perasaan adalah …|Aku senang sekali hari ini.|Hari ini Senin.|Aku pergi ke pasar.|Tanggal 3 Maret.|Mengungkapkan perasaan.
Manfaat buku harian adalah …|menyimpan kenangan|menambah utang|membuat lupa|merusak buku|Menyimpan kenangan.
## BIN|Kalimat pujian dan ucapan selamat
Ucapan yang tepat untuk teman yang juara lomba adalah …|Selamat atas kemenanganmu!|Kasihan sekali kamu.|Kamu curang.|Biasa saja.|Ucapan selamat.
Kalimat pujian yang tepat adalah …|Tulisanmu rapi sekali!|Tulisanmu jelek.|Aku tidak peduli.|Kamu lambat.|Pujian menghargai.
=|Ucapan untuk teman yang berulang tahun adalah selamat ulang …|tahun|Selamat ulang tahun.
=|Pujian dan ucapan selamat harus diucapkan dengan …|tulus;sopan|Tulus.
B|Pujian membuat orang lain merasa dihargai.|Merasa dihargai.
S|Ucapan selamat diberikan saat teman bersedih.|Saat teman berbahagia.
Ucapan untuk teman yang naik kelas adalah …|Selamat naik kelas!|Selamat tidur!|Selamat jalan!|Selamat makan!|Naik kelas.
Respons yang baik saat dipuji adalah …|mengucapkan terima kasih|menyombongkan diri|mengejek teman|diam cemberut|Berterima kasih.
"""

SAS += """
## BIN 1
0|Kalimat yang penulisan kata depannya salah adalah ....|Kakak pergi kesekolah.|Kakak pergi ke sekolah.|Buku di atas meja.|Ibu datang dari pasar.|Ke sekolah harus terpisah.
1|Kata lukis mendapat imbuhan me- menjadi ....|melukis|menglukis|mempukis|mengukis|Melukis.
2|Kalimat seru yang menunjukkan rasa kecewa adalah ....|Sayang sekali, kita kalah!|Hore, kita menang!|Wah, hebat!|Asyik, liburan!|Kecewa.
3|Saat membaca nyaring, suara harus ....|cukup keras|berbisik|sangat pelan|ditahan|Volume cukup keras.
4|Cerita rakyat Batu Menangis berasal dari ....|Kalimantan Barat|Sumatera Barat|Jawa Barat|Papua|Batu Menangis dari Kalimantan Barat.
5|Kata yang berima dengan ibu adalah ....|rindu|ayah|kakak|adik|Bunyi akhir u.
## BIN 2
0|Petunjuk pada pasta gigi yang tepat adalah ....|tutup kembali setelah dipakai|kocok sebelum dipakai|simpan di kulkas|bakar sebelum dipakai|Tutup kembali.
1|Bagian penutup wawancara adalah ....|mengucapkan terima kasih|menyiapkan pertanyaan|bertanya|mencatat jawaban|Penutup.
2|Kata baku dari karir adalah ....|karier|kariir|karir|kareer|Karier.
3|Kalimat utama yang terletak di akhir paragraf disebut paragraf ....|induktif|deduktif|campuran|narasi|Induktif.
4|Buku harian ditulis untuk ....|diri sendiri|dijual|dilombakan|dibacakan di televisi|Untuk diri sendiri.
5|Ucapan yang tepat saat hari raya adalah ....|selamat hari raya|selamat tidur|selamat jalan|selamat ulang tahun|Hari raya.
"""

TOPICS += """
## IPAS
# 1|Makhluk Hidup di Sekitarku
@ Kebutuhan makhluk hidup
min: 10
act: Rawat satu tanaman di pot selama seminggu dan catat apa saja yang dibutuhkannya.
mis: mengira tumbuhan tidak membutuhkan udara
exp: Semua makhluk hidup membutuhkan makanan, air, udara, dan tempat tinggal. Manusia dan hewan mendapat makanan dari tumbuhan atau hewan lain. Tumbuhan membutuhkan air, cahaya matahari, udara, dan tanah yang subur. Jika kebutuhannya tidak terpenuhi, makhluk hidup tidak dapat tumbuh dengan baik.
ex: Ikan membutuhkan air sebagai tempat hidup. // Tanaman di tempat gelap tumbuh pucat.
pt: Butuh makanan dan air ; Butuh udara ; Butuh tempat tinggal yang sesuai
sum: Makhluk hidup dapat bertahan jika kebutuhannya terpenuhi.
fig: table Makhluk hidup | Tempat tinggal ;; ikan | air ;; burung | sarang ;; kelinci | liang ;; lebah | sarang lebah ;; manusia | rumah ;; padi | sawah ~ Tempat tinggal makhluk hidup.
@ Jenis makanan hewan
min: 10
act: Amati hewan di sekitar rumah dan catat makanannya, lalu kelompokkan.
mis: mengira ayam hanya memakan biji-bijian
exp: Berdasarkan makanannya, hewan dibagi menjadi tiga kelompok. Herbivora adalah pemakan tumbuhan, misalnya sapi dan kambing. Karnivora adalah pemakan daging, misalnya harimau dan elang. Omnivora adalah pemakan tumbuhan dan daging, misalnya ayam dan beruang.
ex: Kambing memakan rumput, jadi herbivora. // Kucing memakan daging dan ikan, jadi karnivora.
pt: Herbivora pemakan tumbuhan ; Karnivora pemakan daging ; Omnivora pemakan segala
sum: Hewan dikelompokkan berdasarkan jenis makanannya.
fig: table Hewan | Kelompok makanan ;; sapi | herbivora pemakan rumput ;; harimau | karnivora pemakan daging ;; ayam | omnivora pemakan biji dan cacing ;; kupu-kupu | herbivora pengisap nektar ;; elang | karnivora pemakan tikus ;; beruang | omnivora pemakan madu dan ikan ~ Hewan dan jenis makanannya.
@ Cara hewan bergerak
min: 10
act: Tirukan cara bergerak lima hewan, lalu minta keluarga menebak hewannya.
mis: mengira semua burung bisa terbang
exp: Hewan bergerak dengan cara yang berbeda sesuai tempat hidup dan bentuk tubuhnya. Burung terbang dengan sayap, ikan berenang dengan sirip, kuda berlari dengan kaki, ular melata dengan sisik perut, dan katak melompat dengan kaki belakang yang kuat.
ex: Ikan menggunakan sirip dan ekor untuk berenang. // Kanguru melompat dengan kaki belakangnya.
pt: Cara bergerak sesuai bentuk tubuh ; Alat gerak berbeda-beda ; Disesuaikan dengan tempat hidup
sum: Setiap hewan memiliki alat gerak sesuai tempat hidupnya.
fig: table Hewan | Cara bergerak ;; burung | terbang ;; ikan | berenang ;; ular | melata ;; katak | melompat ;; kuda | berlari ;; siput | merayap dengan lendir ~ Cara hewan bergerak.
@ Perkembangbiakan hewan
min: 10
act: Cari gambar hewan yang bertelur dan yang melahirkan, lalu tempel dalam dua kelompok.
mis: mengira semua hewan bertelur
exp: Hewan berkembang biak untuk melestarikan jenisnya. Ada hewan yang bertelur atau ovipar, misalnya ayam, ikan, dan penyu. Ada hewan yang melahirkan atau vivipar, misalnya kucing, sapi, dan paus. Ada juga hewan yang bertelur dan melahirkan atau ovovivipar, misalnya kadal tertentu dan ikan hiu.
ex: Penyu bertelur di pasir pantai. // Kucing melahirkan anak dan menyusuinya.
pt: Ovipar bertelur ; Vivipar melahirkan ; Ovovivipar bertelur dan melahirkan
sum: Hewan berkembang biak dengan bertelur, melahirkan, atau keduanya.
fig: table Hewan | Cara berkembang biak ;; ayam | bertelur dan mengerami ;; kucing | melahirkan dan menyusui ;; penyu | bertelur di pasir ;; paus | melahirkan di laut ;; ikan hiu | bertelur dan melahirkan ;; kambing | melahirkan di kandang ~ Cara hewan berkembang biak.
@ Tumbuhan membuat makanan
min: 10
act: Letakkan satu pot di tempat terang dan satu pot di tempat gelap, lalu bandingkan daunnya setelah seminggu.
mis: mengira tumbuhan mengambil makanan jadi dari tanah
exp: Tumbuhan hijau dapat membuat makanannya sendiri. Proses ini disebut fotosintesis dan terjadi di daun. Tumbuhan memerlukan air dari akar, udara, dan cahaya matahari. Zat hijau daun membantu menangkap cahaya. Hasilnya berupa makanan untuk tumbuhan dan udara segar untuk kita.
ex: Daun berwarna hijau karena ada zat hijau daun. // Tanaman di tempat gelap menjadi pucat.
pt: Fotosintesis terjadi di daun ; Butuh air, udara, dan cahaya ; Menghasilkan makanan dan udara segar
sum: Tumbuhan membuat makanan sendiri dengan bantuan cahaya matahari.
fig: table Bahan atau hasil | Asal atau kegunaan ;; air | diserap oleh akar ;; cahaya | berasal dari matahari ;; zat hijau daun | menangkap cahaya ;; udara | masuk lewat daun ;; makanan | disimpan di batang, buah, atau umbi ;; udara segar | dilepaskan ke lingkungan ~ Bahan dan hasil fotosintesis.
@ Merawat tumbuhan dan hewan
min: 10
act: Buat jadwal merawat tanaman atau hewan peliharaan di rumah, lalu jalankan selama seminggu.
mis: menyiram tanaman terlalu banyak sehingga akarnya busuk
exp: Tumbuhan dan hewan perlu dirawat supaya sehat. Tanaman disiram, diberi pupuk, dan dibersihkan dari rumput liar. Hewan peliharaan diberi makan dan minum, kandangnya dibersihkan, dan dibawa ke dokter hewan jika sakit.
ex: Menyiram tanaman pagi dan sore. // Membersihkan kandang kelinci setiap hari.
pt: Tanaman disiram dan dipupuk ; Hewan diberi makan dan kandangnya dibersihkan ; Rawat dengan kasih sayang
sum: Merawat tumbuhan dan hewan adalah tanggung jawab kita.
fig: table Kegiatan | Tujuan ;; menyiram tanaman | tanaman tidak layu ;; memberi pupuk | tanah subur ;; mencabut rumput liar | tanaman tumbuh baik ;; memberi makan hewan | hewan sehat ;; membersihkan kandang | hewan tidak sakit ;; membawa ke dokter hewan | hewan sakit sembuh ~ Kegiatan merawat tumbuhan dan hewan.
# 2|Benda, Bumi, dan Lingkungan
@ Gaya tarik dan dorong
min: 10
act: Cari lima kegiatan di rumah yang memakai tarikan dan lima yang memakai dorongan.
mis: mengira membuka laci adalah dorongan
exp: Gaya adalah tarikan atau dorongan. Gaya dapat membuat benda diam menjadi bergerak, benda bergerak menjadi berhenti, mengubah arah gerak, dan mengubah bentuk benda. Contohnya menarik laci, mendorong meja, dan menendang bola.
ex: Membuka laci adalah tarikan. // Menutup pintu dengan tangan bisa dorongan.
pt: Gaya berupa tarikan atau dorongan ; Membuat benda bergerak atau berhenti ; Bisa mengubah bentuk benda
sum: Gaya dapat menggerakkan dan mengubah bentuk benda.
fig: table Kegiatan | Gaya ;; membuka laci | tarikan ;; mendorong gerobak | dorongan ;; menimba air | tarikan tali ;; menendang bola | dorongan kaki ;; meremas tanah liat | mengubah bentuk ;; menangkap bola | menghentikan gerak ~ Contoh gaya dalam kegiatan sehari-hari.
@ Sumber panas
min: 10
act: Rasakan suhu benda di halaman pada pagi dan siang hari, lalu catat perbedaannya.
mis: mengira benda gelap lebih lambat panas dari benda terang
exp: Panas adalah energi yang dapat berpindah. Sumber panas terbesar adalah matahari. Sumber panas lain adalah api, kompor, dan gesekan. Panas dapat mengubah benda, misalnya es mencair dan air mendidih. Benda berwarna gelap lebih cepat panas.
ex: Kedua telapak tangan digosok terasa hangat. // Pakaian dijemur di bawah sinar matahari menjadi kering.
pt: Matahari sumber panas utama ; Gesekan menghasilkan panas ; Panas dapat mengubah benda
sum: Panas berasal dari berbagai sumber dan bermanfaat bagi kita.
fig: table Sumber panas | Contoh manfaat ;; matahari | mengeringkan pakaian ;; api | memasak makanan ;; gesekan tangan | menghangatkan tangan ;; setrika listrik | merapikan pakaian ;; kompor | merebus air ;; tubuh manusia | menjaga suhu badan ~ Sumber panas dan manfaatnya.
@ Cuaca dan musim
min: 10
act: Catat cuaca setiap hari selama dua minggu dengan gambar matahari, awan, atau hujan.
mis: mengira cuaca dan musim artinya sama
exp: Cuaca adalah keadaan udara pada waktu dan tempat tertentu dalam waktu singkat, misalnya cerah, berawan, hujan, dan berangin. Musim adalah keadaan cuaca dalam waktu yang lama. Indonesia memiliki dua musim, yaitu musim hujan dan musim kemarau.
ex: Pagi ini cerah, sore hujan. // Musim hujan biasanya sekitar Oktober sampai Maret.
pt: Cuaca berubah dalam waktu singkat ; Musim berlangsung lama ; Indonesia punya musim hujan dan kemarau
sum: Cuaca berubah cepat, musim berlangsung beberapa bulan.
fig: table Cuaca | Ciri ;; cerah | matahari bersinar terang ;; berawan | langit tertutup awan ;; hujan | air turun dari awan ;; berangin | angin bertiup kencang ;; mendung | awan gelap ;; badai | hujan dan angin sangat kencang ~ Macam-macam cuaca.
@ Bentuk muka bumi
min: 10
act: Buat model gunung, lembah, dan sungai dari tanah liat atau pasir.
mis: mengira dataran tinggi selalu berbentuk gunung yang runcing
exp: Permukaan bumi tidak rata. Ada gunung, pegunungan, bukit, dataran tinggi, dataran rendah, lembah, dan pantai. Gunung adalah bagian bumi yang menjulang tinggi. Dataran rendah berada dekat dengan permukaan laut dan sering dijadikan sawah serta kota.
ex: Dataran tinggi Dieng berhawa sejuk. // Pantai adalah daratan yang berbatasan dengan laut.
pt: Permukaan bumi tidak rata ; Ada gunung, lembah, dan dataran ; Bentuk muka bumi memengaruhi kegiatan manusia
sum: Bumi memiliki bentuk muka yang beragam.
fig: table Bentuk muka bumi | Ciri ;; gunung | menjulang sangat tinggi ;; bukit | lebih rendah dari gunung ;; lembah | daerah rendah di antara gunung ;; dataran rendah | dekat permukaan laut ;; dataran tinggi | daerah datar yang tinggi ;; pantai | berbatasan dengan laut ~ Bentuk muka bumi.
@ Jenis pekerjaan
min: 10
act: Tanyakan pekerjaan tiga tetangga, lalu tulis barang atau jasa yang mereka hasilkan.
mis: mengira hanya pekerjaan yang menghasilkan barang yang penting
exp: Pekerjaan adalah kegiatan untuk memenuhi kebutuhan hidup. Ada pekerjaan yang menghasilkan barang, seperti petani, nelayan, dan penjahit. Ada pekerjaan yang menghasilkan jasa, seperti guru, dokter, dan sopir. Semua pekerjaan yang baik patut dihargai.
ex: Petani menghasilkan padi. // Dokter memberi jasa memeriksa pasien.
pt: Pekerjaan memenuhi kebutuhan hidup ; Ada penghasil barang dan jasa ; Semua pekerjaan dihargai
sum: Setiap pekerjaan bermanfaat bagi masyarakat.
fig: table Pekerjaan | Hasil ;; petani | padi dan sayur ;; nelayan | ikan ;; penjahit | pakaian ;; guru | jasa mengajar ;; dokter | jasa mengobati ;; sopir | jasa mengantar ~ Pekerjaan dan hasilnya.
@ Sampah organik dan anorganik
min: 10
act: Sediakan dua tempat sampah di rumah, lalu pilah sampah organik dan anorganik selama seminggu.
mis: memasukkan botol plastik ke sampah organik
exp: Sampah organik berasal dari makhluk hidup dan mudah membusuk, misalnya sisa makanan, daun, dan kulit buah. Sampah anorganik sulit membusuk, misalnya plastik, kaleng, dan kaca. Sampah organik bisa dijadikan kompos, sedangkan sampah anorganik bisa didaur ulang.
ex: Kulit pisang dijadikan kompos. // Botol plastik dijadikan pot bunga.
pt: Organik mudah membusuk ; Anorganik sulit membusuk ; Pilah sampah untuk diolah
sum: Memilah sampah membantu menjaga lingkungan.
fig: table Sampah | Jenis dan pengolahan ;; daun kering | organik dijadikan kompos ;; botol plastik | anorganik didaur ulang ;; kulit pisang | organik untuk pupuk ;; kaleng minuman | anorganik dijual ke pengepul ;; sisa sayur | organik untuk kompos rumah ;; kantong plastik | anorganik dipakai ulang ~ Jenis sampah dan pengolahannya.
"""

BANK += """
## IPAS|Kebutuhan makhluk hidup
Kebutuhan yang dimiliki semua makhluk hidup adalah …|air dan udara|mainan|uang|televisi|Air dan udara.
Tumbuhan membutuhkan cahaya dari …|matahari|lampu tidur|televisi|bulan purnama saja|Cahaya matahari.
=|Tempat tinggal ikan adalah …|air|Ikan hidup di air.
=|Manusia bernapas untuk mendapatkan …|udara;oksigen|Udara.
B|Tanaman yang tidak disiram akan layu.|Butuh air.
S|Hewan dapat hidup tanpa makanan.|Hewan butuh makanan.
Akibat tanaman diletakkan di tempat gelap terus-menerus adalah …|daunnya pucat|daunnya makin hijau|cepat berbuah|tumbuh lebih subur|Kurang cahaya.
Tempat tinggal burung adalah …|sarang|liang|kandang ikan|air|Sarang.
## IPAS|Jenis makanan hewan
Hewan pemakan tumbuhan disebut …|herbivora|karnivora|omnivora|ovipar|Herbivora.
Contoh hewan karnivora adalah …|harimau|sapi|kambing|kelinci|Harimau makan daging.
=|Hewan pemakan segala disebut …|omnivora|Omnivora.
=|Hewan pemakan daging disebut …|karnivora|Karnivora.
B|Kambing termasuk herbivora.|Kambing makan rumput.
S|Elang termasuk herbivora.|Elang karnivora.
Contoh hewan omnivora adalah …|ayam|sapi|harimau|kuda|Ayam makan biji dan cacing.
Kupu-kupu memakan …|nektar bunga|daging|ikan|tulang|Nektar.
## IPAS|Cara hewan bergerak
Ikan bergerak dengan cara …|berenang|terbang|melata|melompat|Berenang.
Ular bergerak dengan cara …|melata|terbang|berenang saja|berlari|Melata.
=|Alat gerak burung untuk terbang adalah …|sayap|Sayap.
=|Katak bergerak di darat dengan cara …|melompat|Melompat.
B|Siput bergerak dengan bantuan lendir.|Siput merayap.
S|Kuda bergerak dengan cara terbang.|Kuda berlari.
Alat gerak ikan untuk berenang adalah …|sirip dan ekor|sayap|kaki|paruh|Sirip dan ekor.
Hewan yang bergerak dengan melompat menggunakan kaki belakang adalah …|kanguru|ikan|ular|siput|Kanguru melompat.
## IPAS|Perkembangbiakan hewan
Hewan yang berkembang biak dengan bertelur disebut …|ovipar|vivipar|ovovivipar|herbivora|Ovipar.
Contoh hewan vivipar adalah …|kucing|ayam|penyu|ikan mas|Kucing melahirkan.
=|Hewan yang berkembang biak dengan melahirkan disebut …|vivipar|Vivipar.
=|Hewan yang bertelur dan melahirkan disebut …|ovovivipar|Ovovivipar.
B|Penyu bertelur di pasir pantai.|Penyu ovipar.
S|Ayam berkembang biak dengan melahirkan.|Ayam bertelur.
Contoh hewan ovovivipar adalah …|ikan hiu|kucing|sapi|ayam|Hiu.
Paus berkembang biak dengan cara …|melahirkan|bertelur|membelah diri|bertunas|Paus vivipar.
## IPAS|Tumbuhan membuat makanan
Proses tumbuhan membuat makanan disebut …|fotosintesis|penguapan|pencernaan|pernapasan|Fotosintesis.
Bagian tumbuhan tempat fotosintesis adalah …|daun|akar|bunga|biji|Daun.
=|Zat yang membuat daun berwarna hijau disebut zat … daun.|hijau|Zat hijau daun.
=|Air untuk fotosintesis diserap oleh …|akar|Akar menyerap air.
B|Fotosintesis membutuhkan cahaya matahari.|Butuh cahaya.
S|Tumbuhan mengambil makanan jadi dari tanah.|Tumbuhan membuat makanan sendiri.
Hasil fotosintesis yang bermanfaat bagi manusia untuk bernapas adalah …|udara segar|asap|debu|air laut|Udara segar.
Wortel menyimpan makanan pada …|akar|daun|bunga|batang|Wortel akar.
## IPAS|Merawat tumbuhan dan hewan
Tujuan menyiram tanaman adalah …|tanaman tidak layu|tanaman mati|daun rontok|tanaman kering|Tidak layu.
Supaya hewan peliharaan tidak sakit, kandangnya harus …|dibersihkan|dibiarkan kotor|ditutup rapat tanpa udara|dibakar|Dibersihkan.
=|Hewan peliharaan yang sakit dibawa ke dokter …|hewan|Dokter hewan.
=|Supaya tanah subur, tanaman diberi …|pupuk|Pupuk.
B|Rumput liar di sekitar tanaman sebaiknya dicabut.|Rumput liar mengganggu.
S|Menyiram tanaman sebanyak-banyaknya selalu baik.|Terlalu banyak membuat busuk.
Waktu yang baik untuk menyiram tanaman adalah …|pagi atau sore|tengah malam|siang yang sangat terik|tidak perlu|Pagi atau sore.
Contoh merawat ikan di akuarium adalah …|mengganti air secara teratur|memberi makanan berlebihan|tidak memberi makan|membiarkan air keruh|Ganti air.
## IPAS|Gaya tarik dan dorong
Gaya berupa …|tarikan atau dorongan|cahaya dan bunyi|warna dan bentuk|panas dan dingin|Tarikan atau dorongan.
Membuka laci termasuk gaya …|tarikan|dorongan|gesekan saja|magnet|Tarikan.
=|Menendang bola termasuk gaya …|dorongan|Dorongan.
=|Meremas tanah liat dapat mengubah … benda.|bentuk|Bentuk.
B|Gaya dapat membuat benda diam menjadi bergerak.|Pengaruh gaya.
S|Gaya tidak dapat mengubah bentuk benda.|Gaya bisa mengubah bentuk.
Menangkap bola yang dilempar menunjukkan gaya dapat …|menghentikan benda bergerak|membuat bola mencair|mengubah warna|membuat bola berat|Menghentikan gerak.
Contoh dorongan adalah …|mendorong troli belanja|menarik tali layang-layang|membuka pintu dengan tarikan|menimba air|Mendorong troli.
## IPAS|Sumber panas
Sumber panas terbesar bagi bumi adalah …|matahari|bulan|bintang kecil|lampu senter|Matahari.
Menggosokkan kedua telapak tangan menghasilkan panas dari …|gesekan|air|angin|bayangan|Gesekan.
=|Es yang terkena panas akan …|mencair|Es mencair.
=|Alat dapur sumber panas untuk memasak adalah …|kompor|Kompor.
B|Benda berwarna gelap lebih cepat panas.|Gelap menyerap panas.
S|Bulan adalah sumber panas utama bumi.|Matahari sumber utama.
Manfaat panas matahari adalah …|mengeringkan pakaian|membuat es batu|membekukan air|mendinginkan ruangan|Mengeringkan.
Air yang dipanaskan terus akan …|mendidih|membeku|mengeras|menjadi es|Mendidih.
## IPAS|Cuaca dan musim
Keadaan udara pada waktu singkat disebut …|cuaca|musim|iklim|tahun|Cuaca.
Indonesia memiliki dua musim, yaitu …|hujan dan kemarau|panas dan salju|semi dan gugur|dingin dan salju|Hujan dan kemarau.
=|Cuaca saat langit tertutup awan gelap disebut …|mendung|Mendung.
=|Musim saat jarang turun hujan disebut musim …|kemarau|Kemarau.
B|Cuaca dapat berubah dalam satu hari.|Cuaca berubah cepat.
S|Indonesia memiliki musim salju.|Indonesia tropis.
Benda yang perlu dibawa saat cuaca hujan adalah …|payung|kacamata hitam|kipas angin|es batu|Payung.
Cuaca saat angin bertiup sangat kencang disertai hujan lebat disebut …|badai|cerah|berawan|mendung tipis|Badai.
## IPAS|Bentuk muka bumi
Daerah rendah di antara dua gunung disebut …|lembah|bukit|pantai|dataran tinggi|Lembah.
Bagian bumi yang menjulang sangat tinggi disebut …|gunung|lembah|pantai|sungai|Gunung.
=|Daratan yang berbatasan dengan laut disebut …|pantai|Pantai.
=|Bagian bumi yang lebih rendah dari gunung disebut …|bukit|Bukit.
B|Dataran rendah sering dijadikan sawah dan kota.|Dataran rendah.
S|Permukaan bumi seluruhnya rata.|Permukaan bumi tidak rata.
Daerah dataran tinggi biasanya berhawa …|sejuk|sangat panas|bersalju|kering sekali|Sejuk.
Kumpulan gunung yang berderet disebut …|pegunungan|dataran|lembah|pantai|Pegunungan.
## IPAS|Jenis pekerjaan
Pekerjaan yang menghasilkan ikan adalah …|nelayan|petani|guru|penjahit|Nelayan.
Contoh pekerjaan penghasil jasa adalah …|guru|petani|nelayan|peternak|Guru memberi jasa.
=|Pekerjaan yang membuat pakaian adalah …|penjahit|Penjahit.
=|Petani menghasilkan padi dan …|sayur;sayuran|Petani menghasilkan sayur.
B|Dokter memberikan jasa mengobati.|Jasa.
S|Hanya pekerjaan penghasil barang yang penting.|Semua pekerjaan penting.
Pekerjaan yang mengantar penumpang adalah …|sopir|guru|petani|penjahit|Sopir.
Tujuan orang bekerja adalah …|memenuhi kebutuhan hidup|menghabiskan waktu|membuat lelah|bermain|Memenuhi kebutuhan.
## IPAS|Sampah organik dan anorganik
Contoh sampah organik adalah …|kulit buah|botol plastik|kaleng|pecahan kaca|Kulit buah mudah membusuk.
Contoh sampah anorganik adalah …|kaleng minuman|daun kering|sisa nasi|kulit pisang|Kaleng sulit membusuk.
=|Sampah organik dapat diolah menjadi …|kompos;pupuk|Kompos.
=|Sampah anorganik dapat di … ulang.|daur|Didaur ulang.
B|Sampah organik mudah membusuk.|Mudah membusuk.
S|Botol plastik termasuk sampah organik.|Plastik anorganik.
Manfaat memilah sampah adalah …|sampah mudah diolah|sampah menumpuk|lingkungan kotor|banyak lalat|Mudah diolah.
Botol plastik bekas dapat dijadikan …|pot bunga|pupuk|makanan ternak|kompos|Daur ulang.
"""

SAS += """
## IPAS 1
0|Tempat tinggal kelinci adalah ....|liang|sarang lebah|air|sawah|Kelinci di liang.
1|Beruang memakan madu dan ikan sehingga termasuk ....|omnivora|herbivora|karnivora|vivipar|Omnivora.
2|Hewan yang bergerak dengan merayap dan mengeluarkan lendir adalah ....|siput|burung|kuda|ikan|Siput.
3|Kambing berkembang biak dengan cara ....|melahirkan|bertelur|bertunas|membelah diri|Kambing vivipar.
4|Makanan hasil fotosintesis disimpan, misalnya di ....|umbi singkong|asap|batu|air hujan|Umbi.
5|Tujuan memberi pupuk pada tanaman adalah ....|tanah subur|tanaman layu|daun gugur|akar busuk|Tanah subur.
## IPAS 2
0|Menimba air dari sumur menggunakan gaya ....|tarikan|dorongan|magnet|panas|Menarik tali.
1|Contoh pemanfaatan panas setrika adalah ....|merapikan pakaian|memasak nasi|mendinginkan air|mengeringkan rambut|Merapikan pakaian.
2|Cuaca saat matahari bersinar terang disebut ....|cerah|mendung|badai|hujan|Cerah.
3|Daerah datar yang letaknya tinggi disebut ....|dataran tinggi|dataran rendah|lembah|pantai|Dataran tinggi.
4|Pekerjaan yang menghasilkan jasa mengobati adalah ....|dokter|petani|nelayan|penjahit|Dokter.
5|Sisa sayur di dapur termasuk sampah ....|organik|anorganik|berbahaya|logam|Organik.
"""

TOPICS += """
## PPK
# 1|Mengamalkan Pancasila
@ Pengamalan sila pertama
min: 10
act: Catat kegiatan ibadah keluargamu selama seminggu dan cara kalian menghormati tetangga yang berbeda agama.
mis: mengira sila pertama hanya tentang beribadah di rumah ibadah
exp: Sila pertama berbunyi Ketuhanan Yang Maha Esa. Contoh pengamalannya adalah beribadah sesuai agama, berdoa sebelum kegiatan, menghormati teman yang berbeda agama, dan tidak mengganggu orang yang sedang beribadah.
ex: Berdoa sebelum belajar. // Menjaga ketenangan saat tetangga beribadah.
pt: Beribadah sesuai agama ; Menghormati agama lain ; Tidak mengganggu orang beribadah
sum: Sila pertama mengajarkan beriman dan saling menghormati.
fig: table Kegiatan | Sikap sesuai sila pertama ;; sebelum belajar | berdoa ;; waktu salat atau ibadah | beribadah tepat waktu ;; teman beribadah | tidak mengganggu ;; hari raya agama lain | menghormati ;; menerima rezeki | bersyukur ;; teman berbeda agama | tetap berteman ~ Pengamalan sila pertama.
@ Pengamalan sila kedua
min: 10
act: Lakukan satu kebaikan untuk orang yang membutuhkan, lalu ceritakan kepada keluarga.
mis: membantu hanya kepada teman dekat
exp: Sila kedua berbunyi Kemanusiaan yang Adil dan Beradab. Contoh pengamalannya adalah menyayangi sesama, menolong orang yang kesusahan, tidak membeda-bedakan teman, dan bersikap sopan kepada siapa pun.
ex: Menjenguk teman yang sakit. // Menyumbang untuk korban bencana.
pt: Menyayangi sesama manusia ; Menolong tanpa membeda-bedakan ; Bersikap sopan dan adil
sum: Sila kedua mengajarkan sikap peduli dan adil.
fig: table Keadaan | Sikap sesuai sila kedua ;; teman sakit | menjenguk ;; korban bencana | menyumbang ;; teman baru | mengajak berteman ;; orang tua menyeberang | membantu menyeberang ;; teman berbuat salah | memaafkan ;; berbicara dengan siapa pun | bersikap sopan ~ Pengamalan sila kedua.
@ Pengamalan sila ketiga
min: 10
act: Ikut kegiatan tujuh belasan atau kerja bakti di lingkungan rumah bersama keluarga.
mis: hanya mau berteman dengan yang satu suku
exp: Sila ketiga berbunyi Persatuan Indonesia. Contoh pengamalannya adalah bermain dengan semua teman tanpa membedakan suku, cinta tanah air, memakai produk dalam negeri, dan ikut memperingati hari kemerdekaan.
ex: Mengikuti upacara bendera dengan khidmat. // Bangga memakai batik.
pt: Rukun dengan semua teman ; Cinta tanah air ; Mengutamakan persatuan
sum: Sila ketiga mengajarkan persatuan dalam keberagaman.
fig: table Kegiatan | Sikap sesuai sila ketiga ;; upacara bendera | mengikuti dengan khidmat ;; lomba tujuh belasan | ikut memeriahkan ;; teman beda suku | bermain bersama ;; membeli barang | memilih produk dalam negeri ;; lagu nasional | menyanyikan dengan bangga ;; kerja kelompok | bekerja sama ~ Pengamalan sila ketiga.
@ Pengamalan sila keempat
min: 10
act: Adakan musyawarah keluarga untuk menentukan tempat liburan, lalu catat hasilnya.
mis: memaksakan pendapat sendiri dalam musyawarah
exp: Sila keempat berbunyi Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan. Contoh pengamalannya adalah bermusyawarah untuk mengambil keputusan, menghargai pendapat orang lain, dan menerima hasil keputusan bersama.
ex: Memilih ketua kelas dengan musyawarah. // Menerima keputusan walau berbeda dengan pendapat kita.
pt: Utamakan musyawarah ; Hargai pendapat orang lain ; Terima keputusan bersama
sum: Sila keempat mengajarkan musyawarah.
fig: table Keadaan | Sikap sesuai sila keempat ;; memilih ketua kelas | bermusyawarah ;; teman berpendapat | mendengarkan ;; pendapat berbeda | menghargai ;; keputusan diambil | menerima dengan lapang dada ;; ingin berbicara | mengangkat tangan ;; musyawarah buntu | melakukan pemungutan suara ~ Pengamalan sila keempat.
@ Pengamalan sila kelima
min: 10
act: Bagi tugas rumah secara adil bersama saudara, lalu jalankan selama seminggu.
mis: mengambil bagian lebih banyak dari teman
exp: Sila kelima berbunyi Keadilan Sosial bagi Seluruh Rakyat Indonesia. Contoh pengamalannya adalah bersikap adil, tidak serakah, suka bekerja keras, menghargai hasil karya orang lain, dan menggunakan barang milik bersama dengan baik.
ex: Membagi kue sama rata kepada adik dan kakak. // Bergiliran memakai alat permainan.
pt: Bersikap adil ; Tidak serakah ; Menghargai hasil karya orang lain
sum: Sila kelima mengajarkan keadilan untuk semua.
fig: table Keadaan | Sikap sesuai sila kelima ;; membagi kue | sama rata ;; memakai ayunan | bergiliran ;; tugas piket | dikerjakan bersama ;; karya teman | dihargai ;; barang milik bersama | dirawat ;; meminjam buku | dikembalikan tepat waktu ~ Pengamalan sila kelima.
@ Mematuhi rambu lalu lintas
min: 10
act: Saat berjalan dengan orang tua, tunjukkan rambu lalu lintas yang kamu lihat dan sebutkan artinya.
mis: menyeberang saat lampu pejalan kaki berwarna merah
exp: Rambu lalu lintas adalah tanda yang mengatur pengguna jalan supaya selamat. Lampu merah berarti berhenti, kuning berarti hati-hati, dan hijau berarti jalan. Pejalan kaki menyeberang di zebra cross atau jembatan penyeberangan. Mematuhi rambu mencegah kecelakaan.
ex: Berhenti saat lampu merah menyala. // Menyeberang di zebra cross.
pt: Merah berhenti, kuning hati-hati, hijau jalan ; Menyeberang di zebra cross ; Mematuhi rambu mencegah kecelakaan
sum: Rambu lalu lintas menjaga keselamatan di jalan.
fig: table Tanda | Arti ;; lampu merah | berhenti ;; lampu kuning | hati-hati ;; lampu hijau | boleh jalan ;; zebra cross | tempat menyeberang ;; rambu huruf P dicoret | dilarang parkir ;; rambu sekolah | hati-hati banyak anak ~ Tanda lalu lintas dan artinya.
# 2|Keberagaman Indonesia
@ Keberagaman agama di Indonesia
min: 10
act: Cari tahu nama rumah ibadah agama-agama di Indonesia, lalu cari yang ada di dekat rumahmu.
mis: mengira semua orang Indonesia harus beragama sama
exp: Di Indonesia ada enam agama yang dianut masyarakat, yaitu Islam, Kristen Protestan, Katolik, Hindu, Buddha, dan Khonghucu. Setiap agama memiliki tempat ibadah dan kitab suci. Kita hidup rukun dengan saling menghormati.
ex: Umat Hindu beribadah di pura. // Umat Buddha beribadah di wihara.
pt: Ada enam agama ; Setiap agama punya tempat ibadah ; Hidup rukun dan saling menghormati
sum: Keberagaman agama adalah kekayaan bangsa yang harus dijaga.
fig: table Agama | Tempat ibadah ;; Islam | masjid ;; Kristen Protestan | gereja Protestan ;; Katolik | gereja Katolik ;; Hindu | pura ;; Buddha | wihara ;; Khonghucu | kelenteng ~ Agama dan tempat ibadahnya.
@ Bahasa daerah di Indonesia
min: 10
act: Tanyakan kepada orang tua ucapan terima kasih dalam bahasa daerah keluargamu.
mis: menertawakan teman yang berbicara dengan bahasa daerahnya
exp: Indonesia memiliki ratusan bahasa daerah. Contohnya bahasa Jawa, Sunda, Batak, Minang, Bugis, dan Bali. Bahasa daerah dipakai dalam keluarga dan acara adat. Bahasa Indonesia menjadi bahasa persatuan yang dipakai semua suku.
ex: Terima kasih dalam bahasa Jawa: matur nuwun. // Terima kasih dalam bahasa Sunda: hatur nuhun.
pt: Ada ratusan bahasa daerah ; Bahasa daerah dijaga dan dilestarikan ; Bahasa Indonesia bahasa persatuan
sum: Bahasa daerah adalah kekayaan budaya yang perlu dilestarikan.
fig: table Bahasa daerah | Ucapan terima kasih ;; Jawa | matur nuwun ;; Sunda | hatur nuhun ;; Bali | suksma ;; Minang | tarimo kasih ;; Batak Toba | mauliate ;; Bugis | tarima kasi ~ Ucapan terima kasih dalam bahasa daerah.
@ Tarian daerah Nusantara
min: 10
act: Tonton video tari daerah bersama keluarga, lalu tirukan satu gerakannya.
mis: mengira tari daerah hanya berasal dari Jawa
exp: Setiap daerah di Indonesia memiliki tarian khas. Tari Saman dari Aceh, Tari Kecak dari Bali, Tari Jaipong dari Jawa Barat, Tari Piring dari Sumatera Barat, dan Tari Pendet dari Bali adalah contohnya. Tarian daerah sering ditampilkan dalam upacara adat dan penyambutan tamu.
ex: Tari Saman ditarikan dengan gerak tangan yang cepat. // Tari Piring memakai piring sebagai properti.
pt: Setiap daerah punya tarian ; Ditampilkan dalam acara adat ; Kekayaan budaya bangsa
sum: Tarian daerah menunjukkan keindahan budaya Nusantara.
fig: table Tarian | Daerah asal ;; Tari Saman | Aceh ;; Tari Kecak | Bali ;; Tari Jaipong | Jawa Barat ;; Tari Piring | Sumatera Barat ;; Tari Tor-Tor | Sumatera Utara ;; Tari Yospan | Papua ~ Tarian daerah dan asalnya.
@ Provinsi di Indonesia
min: 10
act: Cari provinsi tempat tinggalmu di peta, lalu sebutkan ibu kotanya.
mis: tertukar antara nama provinsi dan nama ibu kotanya
exp: Indonesia terdiri atas banyak provinsi. Setiap provinsi memiliki ibu kota sebagai pusat pemerintahan. Provinsi dipimpin oleh gubernur. Contohnya Provinsi Jawa Barat beribu kota Bandung dan Provinsi Bali beribu kota Denpasar.
ex: Ibu kota Jawa Timur adalah Surabaya. // Ibu kota Sumatera Utara adalah Medan.
pt: Indonesia terdiri atas banyak provinsi ; Setiap provinsi punya ibu kota ; Provinsi dipimpin gubernur
sum: Mengenal provinsi menumbuhkan cinta tanah air.
fig: table Provinsi | Ibu kota ;; Jawa Barat | Bandung ;; Jawa Timur | Surabaya ;; Bali | Denpasar ;; Sumatera Utara | Medan ;; Sulawesi Selatan | Makassar ;; Kalimantan Barat | Pontianak ~ Provinsi dan ibu kotanya.
@ Sikap cinta tanah air
min: 10
act: Tulis lima produk buatan Indonesia yang ada di rumahmu.
mis: menganggap barang buatan luar negeri selalu lebih baik
exp: Cinta tanah air adalah rasa sayang dan bangga kepada Indonesia. Contohnya memakai produk dalam negeri, menjaga lingkungan, mengenal budaya daerah, belajar dengan rajin, dan mengikuti upacara bendera dengan khidmat.
ex: Bangga memakai batik di hari Jumat. // Belajar rajin agar bisa memajukan bangsa.
pt: Bangga kepada Indonesia ; Memakai produk dalam negeri ; Melestarikan budaya dan lingkungan
sum: Cinta tanah air ditunjukkan dengan perbuatan nyata.
fig: icons 🇮🇩 hormat bendera ; 👕 memakai batik ; 📚 belajar rajin ; 🌳 menjaga lingkungan ; 🛒 membeli produk lokal ; 💃 melestarikan tarian daerah ~ Contoh sikap cinta tanah air.
@ Menghargai perbedaan pendapat
min: 10
act: Diskusikan dengan keluarga menu makan malam, lalu dengarkan pendapat setiap orang.
mis: marah ketika pendapat kita tidak dipilih
exp: Setiap orang boleh memiliki pendapat yang berbeda. Kita menghargai perbedaan pendapat dengan mendengarkan, tidak memotong pembicaraan, tidak mengejek, dan menerima keputusan bersama. Perbedaan pendapat bisa membuat keputusan lebih baik.
ex: Mendengarkan usul teman sampai selesai. // Menerima keputusan kelompok walaupun berbeda.
pt: Setiap orang boleh berpendapat ; Dengarkan dan jangan mengejek ; Terima keputusan bersama
sum: Menghargai pendapat membuat kita rukun.
fig: table Situasi | Sikap menghargai ;; teman sedang berbicara | mendengarkan sampai selesai ;; usul teman berbeda | tidak mengejek ;; ingin menyampaikan pendapat | menunggu giliran ;; pendapatku tidak dipilih | menerima dengan lapang dada ;; teman pemalu | diberi kesempatan bicara ;; pendapat yang kurang tepat | diberi masukan dengan sopan ~ Cara menghargai perbedaan pendapat.
"""

BANK += """
## PPK|Pengamalan sila pertama
Bunyi sila pertama Pancasila adalah …|Ketuhanan Yang Maha Esa|Persatuan Indonesia|Kemanusiaan yang Adil dan Beradab|Keadilan Sosial bagi Seluruh Rakyat Indonesia|Sila pertama.
Contoh pengamalan sila pertama adalah …|berdoa sebelum belajar|membagi kue sama rata|bermusyawarah|memakai batik|Berdoa.
=|Lambang sila pertama adalah …|bintang|Bintang.
=|Saat teman beribadah, kita tidak boleh …|mengganggu;membuat keributan|Tidak mengganggu.
B|Menghormati teman yang berbeda agama sesuai dengan sila pertama.|Toleransi.
S|Mengejek ibadah teman sesuai dengan sila pertama.|Itu melanggar.
Bersyukur atas rezeki termasuk pengamalan sila …|pertama|kedua|ketiga|kelima|Sila pertama.
Sikap terhadap teman yang berbeda agama adalah …|tetap berteman dengan baik|menjauhinya|mengejeknya|memaksanya pindah agama|Tetap berteman.
## PPK|Pengamalan sila kedua
Bunyi sila kedua Pancasila adalah …|Kemanusiaan yang Adil dan Beradab|Persatuan Indonesia|Ketuhanan Yang Maha Esa|Keadilan Sosial bagi Seluruh Rakyat Indonesia|Sila kedua.
Contoh pengamalan sila kedua adalah …|menolong korban bencana|ikut lomba tujuh belasan|berdoa|bermusyawarah|Menolong sesama.
=|Lambang sila kedua adalah rantai …|emas|Rantai emas.
=|Teman yang sakit sebaiknya kita …|jenguk;tengok|Menjenguk.
B|Tidak membeda-bedakan teman sesuai dengan sila kedua.|Adil.
S|Hanya menolong teman yang kaya sesuai dengan sila kedua.|Menolong tanpa membedakan.
Memaafkan teman yang berbuat salah termasuk pengamalan sila …|kedua|keempat|kelima|ketiga|Sila kedua.
Contoh sikap tidak sesuai sila kedua adalah …|mengejek teman yang kurang mampu|menjenguk teman|menyumbang|membantu orang tua menyeberang|Mengejek.
## PPK|Pengamalan sila ketiga
Bunyi sila ketiga Pancasila adalah …|Persatuan Indonesia|Ketuhanan Yang Maha Esa|Kemanusiaan yang Adil dan Beradab|Keadilan Sosial bagi Seluruh Rakyat Indonesia|Sila ketiga.
Contoh pengamalan sila ketiga adalah …|bermain dengan teman beda suku|berdoa sebelum makan|membagi kue rata|bermusyawarah|Persatuan.
=|Lambang sila ketiga adalah pohon …|beringin|Pohon beringin.
=|Kain khas Indonesia yang kita banggakan adalah …|batik|Batik.
B|Mengikuti upacara bendera termasuk pengamalan sila ketiga.|Cinta tanah air.
S|Memilih teman hanya yang satu suku sesuai sila ketiga.|Harus rukun dengan semua.
Memilih produk dalam negeri termasuk pengamalan sila …|ketiga|pertama|kedua|keempat|Sila ketiga.
Sikap saat kerja kelompok yang sesuai sila ketiga adalah …|bekerja sama|bekerja sendiri|bertengkar|mengejek teman|Bekerja sama.
## PPK|Pengamalan sila keempat
Lambang sila keempat adalah …|kepala banteng|bintang|rantai|padi dan kapas|Kepala banteng.
Contoh pengamalan sila keempat adalah …|memilih ketua kelas dengan musyawarah|berdoa|menyumbang|menanam pohon|Musyawarah.
=|Cara mengambil keputusan bersama dengan berdiskusi disebut …|musyawarah|Musyawarah.
=|Jika musyawarah tidak mencapai kata sepakat, dilakukan pemungutan …|suara|Pemungutan suara.
B|Menerima hasil musyawarah dengan lapang dada sesuai sila keempat.|Menerima keputusan.
S|Memaksakan pendapat sendiri sesuai sila keempat.|Melanggar.
Sebelum berbicara dalam musyawarah, kita sebaiknya …|mengangkat tangan|berteriak|memotong pembicaraan|keluar kelas|Mengangkat tangan.
Sikap saat pendapat kita tidak diterima adalah …|menerima keputusan bersama|marah|mogok|mengejek|Menerima.
## PPK|Pengamalan sila kelima
Bunyi sila kelima Pancasila adalah …|Keadilan Sosial bagi Seluruh Rakyat Indonesia|Persatuan Indonesia|Ketuhanan Yang Maha Esa|Kemanusiaan yang Adil dan Beradab|Sila kelima.
Lambang sila kelima adalah …|padi dan kapas|bintang|rantai|kepala banteng|Padi dan kapas.
=|Saat bermain ayunan bersama, kita memakai secara …|bergiliran|Bergiliran.
=|Kue dibagi kepada saudara secara sama …|rata|Sama rata.
B|Menghargai hasil karya teman sesuai dengan sila kelima.|Menghargai karya.
S|Bersikap serakah sesuai dengan sila kelima.|Tidak serakah.
Contoh pengamalan sila kelima adalah …|mengembalikan buku pinjaman tepat waktu|bermusyawarah|berdoa|mengikuti upacara|Adil dan bertanggung jawab.
Sikap yang tidak sesuai sila kelima adalah …|mengambil bagian lebih banyak|bergiliran|berbagi|merawat barang bersama|Serakah.
## PPK|Mematuhi rambu lalu lintas
Lampu lalu lintas berwarna merah berarti …|berhenti|jalan|hati-hati|parkir|Berhenti.
Tempat menyeberang bagi pejalan kaki adalah …|zebra cross|tengah jalan tol|trotoar|halte|Zebra cross.
=|Lampu kuning berarti …|hati-hati|Hati-hati.
=|Lampu hijau berarti boleh …|jalan;berjalan|Boleh jalan.
B|Mematuhi rambu lalu lintas mencegah kecelakaan.|Keselamatan.
S|Pejalan kaki boleh menyeberang di mana saja walaupun lampu merah.|Harus di tempat dan waktunya.
Rambu huruf P yang dicoret artinya …|dilarang parkir|boleh parkir|parkir gratis|tempat penyeberangan|Dilarang parkir.
Saat naik sepeda motor bersama ayah, kita harus memakai …|helm|topi pesta|kacamata renang|sandal jepit saja|Helm.
## PPK|Keberagaman agama di Indonesia
Tempat ibadah umat Hindu adalah …|pura|masjid|gereja|wihara|Pura.
Tempat ibadah umat Buddha adalah …|wihara|pura|kelenteng|masjid|Wihara.
=|Tempat ibadah umat Islam adalah …|masjid|Masjid.
=|Tempat ibadah umat Khonghucu adalah …|kelenteng;klenteng|Kelenteng.
B|Di Indonesia ada enam agama yang dianut masyarakat.|Enam agama.
S|Semua orang Indonesia wajib beragama sama.|Bebas memeluk agama.
Sikap terhadap teman yang berbeda agama adalah …|saling menghormati|saling mengejek|saling menjauh|saling memusuhi|Menghormati.
Gereja adalah tempat ibadah umat …|Kristen dan Katolik|Hindu|Buddha|Islam|Gereja.
## PPK|Bahasa daerah di Indonesia
Bahasa persatuan bangsa Indonesia adalah bahasa …|Indonesia|Jawa|Sunda|Inggris|Bahasa Indonesia.
Ucapan terima kasih dalam bahasa Sunda adalah …|hatur nuhun|matur nuwun|suksma|mauliate|Hatur nuhun.
=|Ucapan terima kasih dalam bahasa Jawa adalah matur …|nuwun|Matur nuwun.
=|Ucapan terima kasih dalam bahasa Bali adalah …|suksma|Suksma.
B|Bahasa daerah perlu dilestarikan.|Kekayaan budaya.
S|Teman yang memakai bahasa daerah boleh ditertawakan.|Harus dihargai.
Mauliate adalah ucapan terima kasih dalam bahasa …|Batak Toba|Jawa|Bugis|Minang|Batak Toba.
Bahasa daerah biasanya dipakai di …|keluarga dan acara adat|rapat PBB|siaran internasional|soal ujian nasional|Keluarga dan adat.
## PPK|Tarian daerah Nusantara
Tari Saman berasal dari …|Aceh|Bali|Papua|Jawa Barat|Saman dari Aceh.
Tari Kecak berasal dari …|Bali|Aceh|Sumatera Barat|Papua|Kecak dari Bali.
=|Tari Jaipong berasal dari Jawa …|Barat|Jaipong dari Jawa Barat.
=|Tari yang memakai piring sebagai properti adalah Tari …|Piring|Tari Piring.
B|Tari Tor-Tor berasal dari Sumatera Utara.|Batak.
S|Tari Yospan berasal dari Aceh.|Yospan dari Papua.
Tari Piring berasal dari …|Sumatera Barat|Bali|Papua|Aceh|Minangkabau.
Tarian daerah sering ditampilkan saat …|penyambutan tamu dan acara adat|ulangan harian|tidur siang|olahraga pagi|Acara adat.
## PPK|Provinsi di Indonesia
Ibu kota Provinsi Bali adalah …|Denpasar|Bandung|Medan|Makassar|Denpasar.
Ibu kota Provinsi Jawa Barat adalah …|Bandung|Surabaya|Semarang|Serang|Bandung.
=|Ibu kota Provinsi Jawa Timur adalah …|Surabaya|Surabaya.
=|Provinsi dipimpin oleh seorang …|gubernur|Gubernur.
B|Ibu kota Sumatera Utara adalah Medan.|Medan.
S|Ibu kota Sulawesi Selatan adalah Pontianak.|Ibu kotanya Makassar.
Makassar adalah ibu kota Provinsi …|Sulawesi Selatan|Kalimantan Barat|Bali|Jawa Timur|Makassar.
Pontianak adalah ibu kota Provinsi …|Kalimantan Barat|Sulawesi Selatan|Sumatera Utara|Bali|Pontianak.
## PPK|Sikap cinta tanah air
Contoh sikap cinta tanah air adalah …|memakai produk dalam negeri|merusak fasilitas umum|mengejek budaya daerah|membuang sampah sembarangan|Produk dalam negeri.
Belajar dengan rajin menunjukkan cinta tanah air karena …|kelak bisa memajukan bangsa|supaya bisa bermain|supaya mendapat hadiah saja|supaya cepat libur|Memajukan bangsa.
=|Kain khas Indonesia yang dipakai sebagai wujud cinta tanah air adalah …|batik|Batik.
=|Saat upacara bendera kita bersikap …|khidmat;tertib|Khidmat.
B|Melestarikan tarian daerah adalah sikap cinta tanah air.|Melestarikan budaya.
S|Merusak fasilitas umum menunjukkan cinta tanah air.|Merusak itu salah.
Menjaga kebersihan lingkungan termasuk sikap …|cinta tanah air|malas|tidak peduli|egois|Cinta tanah air.
Lagu yang dinyanyikan sebagai wujud cinta tanah air adalah lagu …|nasional|tanpa makna|ejekan|asal-asalan|Lagu nasional.
## PPK|Menghargai perbedaan pendapat
Saat teman menyampaikan pendapat, kita sebaiknya …|mendengarkan sampai selesai|memotongnya|mengejeknya|meninggalkannya|Mendengarkan.
Jika pendapat kita tidak dipilih, sikap kita …|menerima dengan lapang dada|marah|mogok bicara|merusak barang|Lapang dada.
=|Sebelum menyampaikan pendapat, kita menunggu …|giliran|Menunggu giliran.
=|Perbedaan pendapat bisa membuat keputusan lebih …|baik|Lebih baik.
B|Setiap orang boleh memiliki pendapat berbeda.|Hak berpendapat.
S|Pendapat yang berbeda harus diejek.|Harus dihargai.
Teman yang pemalu sebaiknya …|diberi kesempatan berbicara|ditertawakan|diabaikan|dipaksa diam|Diberi kesempatan.
Pendapat teman yang kurang tepat sebaiknya …|diberi masukan dengan sopan|diejek|dimarahi|diabaikan|Masukan sopan.
"""

SAS += """
## PPK 1
0|Tidak mengganggu tetangga yang sedang beribadah merupakan pengamalan sila ....|pertama|kedua|ketiga|kelima|Sila pertama.
1|Membantu orang tua menyeberang jalan merupakan pengamalan sila ....|kedua|pertama|keempat|kelima|Sila kedua.
2|Ikut memeriahkan lomba tujuh belasan merupakan pengamalan sila ....|ketiga|pertama|kedua|kelima|Sila ketiga.
3|Mendengarkan teman yang berpendapat dalam musyawarah merupakan pengamalan sila ....|keempat|pertama|kedua|ketiga|Sila keempat.
4|Merawat barang milik bersama merupakan pengamalan sila ....|kelima|pertama|kedua|ketiga|Sila kelima.
5|Rambu bergambar anak sekolah berarti ....|hati-hati banyak anak|dilarang lewat|boleh ngebut|tempat parkir|Hati-hati.
## PPK 2
0|Pura adalah tempat ibadah umat ....|Hindu|Buddha|Islam|Khonghucu|Pura umat Hindu.
1|Ucapan terima kasih dalam bahasa Minang adalah ....|tarimo kasih|matur nuwun|hatur nuhun|suksma|Tarimo kasih.
2|Tari Tor-Tor berasal dari ....|Sumatera Utara|Bali|Aceh|Papua|Tor-Tor dari Sumatera Utara.
3|Ibu kota Provinsi Kalimantan Barat adalah ....|Pontianak|Makassar|Medan|Denpasar|Pontianak.
4|Contoh sikap cinta tanah air di sekolah adalah ....|mengikuti upacara bendera dengan khidmat|membolos|mencoret tembok|berkelahi|Upacara khidmat.
5|Saat teman berbeda pendapat dengan kita, sikap yang tepat adalah ....|menghargai pendapatnya|mengejeknya|memusuhinya|memaksanya setuju|Menghargai.
"""

TOPICS += """
## BIG
# 1|Things Around Me
@ Shapes
min: 10
act: Find things at home with different shapes and say their names in English.
mis: menyebut square untuk bentuk lingkaran
exp: Shapes artinya bentuk. Circle adalah lingkaran, square adalah persegi, triangle adalah segitiga, rectangle adalah persegi panjang, star adalah bintang, dan heart adalah hati. Kita bisa bertanya What shape is it? dan menjawab It is a circle.
ex: What shape is the clock? It is a circle. // The window is a square.
pt: Circle artinya lingkaran ; Triangle artinya segitiga ; Rectangle artinya persegi panjang
sum: Shapes membantu kita menyebut bentuk benda dalam bahasa Inggris.
fig: icons ⚪ circle ; 🟥 square ; 🔺 triangle ; ⭐ star ; ❤️ heart ; 🔷 diamond ~ Shapes in English.
@ Fruits
min: 10
act: Look at the fruits in your kitchen and name them in English with your family.
mis: menyebut grape untuk buah jeruk
exp: Fruits artinya buah-buahan. Apple adalah apel, banana adalah pisang, orange adalah jeruk, mango adalah mangga, grape adalah anggur, dan watermelon adalah semangka. Kita bisa berkata I like mangoes untuk menyatakan buah kesukaan.
ex: I like bananas. // Do you like apples? Yes, I do.
pt: Apple artinya apel ; Orange artinya jeruk ; Watermelon artinya semangka
sum: Fruits adalah nama buah-buahan dalam bahasa Inggris.
fig: icons 🍎 apple ; 🍌 banana ; 🍊 orange ; 🥭 mango ; 🍇 grapes ; 🍉 watermelon ~ Fruits in English.
@ Toys
min: 10
act: Put your toys on the floor and say I have a ... for each toy.
mis: mengucapkan I has a ball
exp: Toys artinya mainan. Ball adalah bola, doll adalah boneka, kite adalah layang-layang, car adalah mobil-mobilan, robot adalah robot, dan teddy bear adalah boneka beruang. Untuk menyebut mainan milik kita, gunakan I have a ball.
ex: I have a kite. // My sister has a doll.
pt: Toys artinya mainan ; Gunakan I have untuk aku punya ; Gunakan She has untuk dia perempuan punya
sum: Toys adalah nama mainan dalam bahasa Inggris.
fig: icons ⚽ ball ; 🪁 kite ; 🧸 teddy bear ; 🚗 toy car ; 🤖 robot ; 🪀 yo-yo ~ Toys in English.
@ Feelings
min: 10
act: Draw faces showing different feelings and write the English word under each face.
mis: menyebut sad untuk perasaan senang
exp: Feelings artinya perasaan. Happy adalah senang, sad adalah sedih, angry adalah marah, scared adalah takut, tired adalah lelah, dan sleepy adalah mengantuk. Kita bisa bertanya How do you feel? dan menjawab I am happy.
ex: How do you feel today? I am happy. // He is tired after playing football.
pt: Happy artinya senang ; Sad artinya sedih ; Tanyakan How do you feel?
sum: Feelings membantu kita mengungkapkan perasaan dalam bahasa Inggris.
fig: icons 😀 happy ; 😢 sad ; 😠 angry ; 😨 scared ; 😴 sleepy ; 😲 surprised ~ Feelings in English.
@ Clothes
min: 10
act: Open your wardrobe and name your clothes in English.
mis: menyebut shoes untuk kaos kaki
exp: Clothes artinya pakaian. Shirt adalah kemeja, T-shirt adalah kaus, trousers adalah celana panjang, skirt adalah rok, hat adalah topi, dan shoes adalah sepatu. Kita bisa berkata I am wearing a hat untuk menyatakan pakaian yang sedang dipakai.
ex: I am wearing a blue T-shirt. // Put on your shoes, please.
pt: Shirt artinya kemeja ; Hat artinya topi ; Shoes artinya sepatu
sum: Clothes adalah nama pakaian dalam bahasa Inggris.
fig: icons 👕 T-shirt ; 👗 dress ; 👖 trousers ; 🧢 cap ; 👟 shoes ; 🧦 socks ~ Clothes in English.
@ Classroom instructions
min: 10
act: Play Simon Says at home using English classroom instructions.
mis: tertukar antara stand up dan sit down
exp: Classroom instructions adalah perintah yang sering diucapkan guru di kelas. Stand up artinya berdiri, sit down artinya duduk, open your book artinya buka bukumu, close the door artinya tutup pintu, listen artinya dengarkan, dan be quiet artinya tenanglah.
ex: Please sit down. // Open your book, please.
pt: Stand up artinya berdiri ; Sit down artinya duduk ; Tambahkan please supaya sopan
sum: Memahami perintah di kelas membantu kita mengikuti pelajaran.
fig: table Instruction | Artinya ;; stand up | berdiri ;; sit down | duduk ;; open your book | buka bukumu ;; close the door | tutup pintu ;; listen | dengarkan ;; be quiet | tenanglah ~ Classroom instructions.
# 2|My Daily Life
@ Food and drinks
min: 10
act: Tell your family what you eat for breakfast in English.
mis: menyebut milk untuk air putih
exp: Food artinya makanan dan drinks artinya minuman. Rice adalah nasi, bread adalah roti, egg adalah telur, noodles adalah mi, milk adalah susu, dan water adalah air. Kita bisa berkata I eat rice dan I drink milk.
ex: I eat bread and egg for breakfast. // I drink water every day.
pt: Rice artinya nasi ; Bread artinya roti ; Gunakan eat untuk makanan dan drink untuk minuman
sum: Food and drinks adalah nama makanan dan minuman dalam bahasa Inggris.
fig: icons 🍚 rice ; 🍞 bread ; 🥚 egg ; 🍜 noodles ; 🥛 milk ; 💧 water ~ Food and drinks in English.
@ Months of the year
min: 10
act: Make a birthday calendar of your family and write the months in English.
mis: menulis nama bulan dengan huruf kecil di awal
exp: Ada dua belas bulan dalam setahun. Dalam bahasa Inggris: January, February, March, April, May, June, July, August, September, October, November, dan December. Nama bulan selalu diawali huruf kapital. Kita bertanya When is your birthday? dan menjawab It is in May.
ex: My birthday is in August. // Independence Day is in August.
pt: Ada dua belas bulan ; Diawali huruf kapital ; Tanyakan When is your birthday?
sum: Months of the year membantu menyebut bulan dalam bahasa Inggris.
fig: table Month | Urutan ;; January | bulan ke-1 ;; March | bulan ke-3 ;; May | bulan ke-5 ;; August | bulan ke-8 ;; October | bulan ke-10 ;; December | bulan ke-12 ~ Months of the year.
@ Weather
min: 10
act: Look out of the window every morning and say the weather in English.
mis: menyebut sunny saat hujan
exp: Weather artinya cuaca. Sunny artinya cerah, rainy artinya hujan, cloudy artinya berawan, windy artinya berangin, hot artinya panas, dan cold artinya dingin. Kita bertanya What is the weather like today? dan menjawab It is sunny.
ex: It is rainy. Bring your umbrella. // It is hot today.
pt: Sunny artinya cerah ; Rainy artinya hujan ; Tanyakan What is the weather like?
sum: Weather membantu kita menyebut cuaca dalam bahasa Inggris.
fig: icons ☀️ sunny ; 🌧️ rainy ; ☁️ cloudy ; 🌬️ windy ; 🔥 hot ; 🥶 cold ~ Weather in English.
@ Rooms in my house
min: 10
act: Walk around your house and say the name of each room in English.
mis: menyebut kitchen untuk kamar mandi
exp: Rooms artinya ruangan. Living room adalah ruang tamu, bedroom adalah kamar tidur, kitchen adalah dapur, bathroom adalah kamar mandi, dining room adalah ruang makan, dan garage adalah garasi. Kita bertanya Where is Mom? dan menjawab She is in the kitchen.
ex: I sleep in my bedroom. // Mom cooks in the kitchen.
pt: Bedroom artinya kamar tidur ; Kitchen artinya dapur ; Bathroom artinya kamar mandi
sum: Rooms in my house adalah nama ruangan di rumah.
fig: table Room | Activity ;; bedroom | sleeping ;; kitchen | cooking ;; bathroom | taking a bath ;; living room | watching TV ;; dining room | eating together ;; garage | parking the car ~ Rooms and activities.
@ Numbers 21–100
min: 10
act: Count the steps from your house to the gate in English.
mis: membaca 30 sebagai thirteen
exp: Bilangan puluhan dalam bahasa Inggris adalah twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, dan one hundred. Untuk bilangan seperti 25, gabungkan twenty dan five menjadi twenty-five. Perhatikan bedanya thirteen (13) dan thirty (30).
ex: 25 is twenty-five. // 100 is one hundred.
pt: Puluhan berakhiran -ty ; Gabungkan puluhan dan satuan ; Thirteen berbeda dengan thirty
sum: Numbers 21–100 membantu kita berhitung dalam bahasa Inggris.
fig: table Number | In English ;; 21 | twenty-one ;; 30 | thirty ;; 45 | forty-five ;; 50 | fifty ;; 78 | seventy-eight ;; 100 | one hundred ~ Numbers 21–100.
@ Transportation
min: 10
act: Watch the road with your parents and name the vehicles in English.
mis: menyebut ship untuk pesawat
exp: Transportation artinya alat transportasi. Car adalah mobil, bus adalah bus, bicycle adalah sepeda, motorcycle adalah sepeda motor, train adalah kereta, plane adalah pesawat, dan ship adalah kapal. Kita bisa berkata I go to school by bicycle.
ex: I go to school by bus. // My father goes to work by motorcycle.
pt: Bicycle artinya sepeda ; Train artinya kereta ; Gunakan by untuk menyebut kendaraan
sum: Transportation adalah nama kendaraan dalam bahasa Inggris.
fig: icons 🚗 car ; 🚌 bus ; 🚲 bicycle ; 🚆 train ; ✈️ plane ; 🚢 ship ~ Transportation in English.
"""

BANK += """
## BIG|Shapes
Triangle artinya …|segitiga|lingkaran|persegi|bintang|Triangle = segitiga.
The clock is round. Its shape is …|a circle|a square|a triangle|a star|Jam dinding berbentuk lingkaran.
=|Bahasa Inggris dari persegi adalah …|square|Square.
=|Bahasa Inggris dari persegi panjang adalah …|rectangle|Rectangle.
B|Star artinya bintang.|Star = bintang.
S|Heart artinya lingkaran.|Heart = hati.
What shape is a slice of pizza? It is a …|triangle|circle|square|rectangle|Potongan pizza segitiga.
Pertanyaan untuk menanyakan bentuk adalah …|What shape is it?|What color is it?|How old are you?|Where is it?|What shape.
## BIG|Fruits
Banana artinya …|pisang|apel|mangga|anggur|Banana = pisang.
Bahasa Inggris dari semangka adalah …|watermelon|grape|mango|orange|Watermelon.
=|Bahasa Inggris dari apel adalah …|apple|Apple.
=|Bahasa Inggris dari jeruk adalah …|orange|Orange.
B|Mango artinya mangga.|Mango = mangga.
S|Grape artinya pisang.|Grape = anggur.
Do you like apples? Jawaban yang tepat jika suka adalah …|Yes, I do.|No, I am.|Yes, I am.|Yes, it is.|Yes, I do.
Kalimat untuk menyatakan buah kesukaan adalah …|I like mangoes.|I am mangoes.|I have mangoes like.|I mangoes like.|I like.
## BIG|Toys
Kite artinya …|layang-layang|boneka|bola|robot|Kite = layang-layang.
Bahasa Inggris dari boneka adalah …|doll|ball|kite|car|Doll.
=|Bahasa Inggris dari bola adalah …|ball|Ball.
=|Bahasa Inggris dari mainan adalah …|toy;toys|Toy.
B|Teddy bear artinya boneka beruang.|Teddy bear.
S|Toy car artinya layang-layang.|Toy car = mobil-mobilan.
Kalimat yang benar adalah …|I have a robot.|I has a robot.|I having robot.|I is a robot.|I have.
My sister … a doll.|has|have|having|is have|She/my sister has.
## BIG|Feelings
Sad artinya …|sedih|senang|marah|takut|Sad = sedih.
Bahasa Inggris dari marah adalah …|angry|happy|sleepy|tired|Angry.
=|Bahasa Inggris dari senang adalah …|happy|Happy.
=|Bahasa Inggris dari mengantuk adalah …|sleepy|Sleepy.
B|Scared artinya takut.|Scared = takut.
S|Happy artinya sedih.|Happy = senang.
How do you feel? Jawaban yang tepat adalah …|I am happy.|I am ten.|I am Budi.|I am fine, thank you, goodbye.|I am happy.
He played football all day. Now he is …|tired|angry|scared|sad|Lelah setelah bermain.
## BIG|Clothes
Hat artinya …|topi|sepatu|celana|baju|Hat = topi.
Bahasa Inggris dari sepatu adalah …|shoes|socks|shirt|skirt|Shoes.
=|Bahasa Inggris dari kaos kaki adalah …|socks|Socks.
=|Bahasa Inggris dari rok adalah …|skirt|Skirt.
B|Trousers artinya celana panjang.|Trousers.
S|Dress artinya sepatu.|Dress = gaun.
I am … a blue T-shirt.|wearing|eating|drinking|reading|Wearing = memakai.
Pakaian yang dipakai di kaki adalah …|shoes|hat|cap|T-shirt|Shoes di kaki.
## BIG|Classroom instructions
Stand up artinya …|berdiri|duduk|diam|menulis|Stand up = berdiri.
Sit down artinya …|duduk|berdiri|berlari|membaca|Sit down = duduk.
=|Perintah untuk membuka buku adalah … your book.|open|Open your book.
=|Perintah supaya tenang adalah be …|quiet|Be quiet.
B|Listen artinya dengarkan.|Listen.
S|Close the door artinya buka pintu.|Close = tutup.
Kata yang membuat perintah lebih sopan adalah …|please|sorry|hello|bye|Please.
Guru berkata Write your name. Artinya …|tulis namamu|baca namamu|sebut namamu|hapus namamu|Write = tulis.
## BIG|Food and drinks
Rice artinya …|nasi|roti|mi|telur|Rice = nasi.
Bahasa Inggris dari susu adalah …|milk|water|juice|tea|Milk.
=|Bahasa Inggris dari roti adalah …|bread|Bread.
=|Bahasa Inggris dari telur adalah …|egg|Egg.
B|Noodles artinya mi.|Noodles.
S|Water artinya susu.|Water = air.
Kalimat yang benar adalah …|I drink milk.|I eat milk.|I drink bread.|I eat water.|Drink untuk minuman.
I eat … for breakfast.|bread|water|milk|juice|Eat untuk makanan.
## BIG|Months of the year
Bulan pertama dalam bahasa Inggris adalah …|January|December|March|May|January.
Bulan kedelapan dalam bahasa Inggris adalah …|August|October|April|June|August.
=|Bulan terakhir dalam bahasa Inggris adalah …|December|December.
=|Bulan sesudah April adalah …|May|May.
B|Nama bulan dalam bahasa Inggris diawali huruf kapital.|Kapital.
S|Ada sepuluh bulan dalam setahun.|Dua belas bulan.
When is your birthday? Jawaban yang tepat adalah …|It is in June.|It is a cat.|I am nine.|It is sunny.|Menyebut bulan.
Bulan sebelum March adalah …|February|April|January|May|February.
## BIG|Weather
Rainy artinya …|hujan|cerah|berangin|berawan|Rainy = hujan.
Bahasa Inggris dari cerah adalah …|sunny|cloudy|windy|cold|Sunny.
=|Bahasa Inggris dari berangin adalah …|windy|Windy.
=|Bahasa Inggris dari dingin adalah …|cold|Cold.
B|Cloudy artinya berawan.|Cloudy.
S|Hot artinya dingin.|Hot = panas.
It is rainy. You need …|an umbrella|sunglasses|a fan|ice cream|Bawa payung.
Pertanyaan untuk menanyakan cuaca adalah …|What is the weather like today?|What time is it?|How old are you?|What is your name?|Weather.
## BIG|Rooms in my house
Kitchen artinya …|dapur|kamar tidur|kamar mandi|garasi|Kitchen = dapur.
Bahasa Inggris dari kamar tidur adalah …|bedroom|bathroom|kitchen|garage|Bedroom.
=|Bahasa Inggris dari kamar mandi adalah …|bathroom|Bathroom.
=|Bahasa Inggris dari ruang tamu adalah living …|room|Living room.
B|Garage adalah tempat menyimpan mobil.|Garasi.
S|We sleep in the kitchen.|Tidur di bedroom.
Where is Mom? She is cooking in the …|kitchen|bathroom|garage|bedroom|Memasak di dapur.
We eat together in the …|dining room|garage|bathroom|garden shed|Ruang makan.
## BIG|Numbers 21–100
Thirty adalah angka …|30|13|3|33|Thirty = 30.
Angka 45 dalam bahasa Inggris adalah …|forty-five|fourteen-five|fifty-four|four-five|45.
=|Angka 50 dalam bahasa Inggris adalah …|fifty|Fifty.
=|Angka 100 dalam bahasa Inggris adalah one …|hundred|One hundred.
B|Twenty-one adalah 21.|21.
S|Thirteen sama dengan thirty.|13 dan 30 berbeda.
Ninety adalah angka …|90|19|9|99|Ninety = 90.
Twenty plus ten is …|thirty|twelve|forty|twenty-ten|20 + 10 = 30.
## BIG|Transportation
Bicycle artinya …|sepeda|sepeda motor|mobil|kereta|Bicycle = sepeda.
Bahasa Inggris dari pesawat adalah …|plane|ship|train|bus|Plane.
=|Bahasa Inggris dari kapal adalah …|ship|Ship.
=|Bahasa Inggris dari kereta adalah …|train|Train.
B|Motorcycle artinya sepeda motor.|Motorcycle.
S|Bus artinya pesawat.|Bus = bus.
I go to school … bicycle.|by|in|on the|at|By bicycle.
Kendaraan yang berjalan di laut adalah …|ship|car|train|bicycle|Ship.
"""

SAS += """
## BIG 1
0|Diamond shape is like a ....|belah ketupat|lingkaran|segitiga|bintang|Diamond = belah ketupat.
1|Grapes artinya ....|anggur|jeruk|apel|pisang|Grapes.
2|Robot dalam bahasa Inggris adalah ....|robot|kite|doll|ball|Robot.
3|I see a ghost. I am ....|scared|happy|sleepy|hungry|Takut.
4|Socks are worn on your ....|feet|head|hands|ears|Kaus kaki di kaki.
5|Teacher says, Close your book. Artinya ....|tutup bukumu|buka bukumu|baca bukumu|tulis bukumu|Close = tutup.
## BIG 2
0|I am thirsty. I want to drink ....|water|rice|bread|egg|Haus, minum air.
1|Bulan Oktober dalam bahasa Inggris adalah ....|October|August|November|September|October.
2|It is cloudy artinya ....|berawan|cerah|hujan|berangin|Cloudy.
3|We take a bath in the ....|bathroom|kitchen|garage|living room|Mandi di kamar mandi.
4|Seventy-eight adalah angka ....|78|87|17|70|78.
5|My father goes to Bali by ....|plane|bicycle|kite|doll|Ke Bali naik pesawat.
"""

TOPICS += """
## SBD
# 1|Rupa dan Musik
@ Mozaik
min: 10
act: Buat mozaik bergambar ikan dari potongan kertas warna yang ditempel rapat.
mis: menempel potongan mozaik saling bertumpuk seperti kolase
exp: Mozaik adalah karya seni yang dibuat dengan menempelkan potongan kecil bahan pada bidang gambar. Potongan disusun rapat dan tidak saling menumpuk, tetapi diberi sedikit celah. Bahan mozaik bisa kertas, biji-bijian, kulit telur, atau keramik.
ex: Mozaik bunga dari potongan kertas warna. // Mozaik dari biji jagung dan kacang hijau.
pt: Potongan kecil ditempel rapat ; Tidak saling menumpuk ; Bahan bisa kertas atau biji-bijian
sum: Mozaik tersusun dari potongan kecil yang ditempel rapi.
fig: table Bahan mozaik | Warna yang dihasilkan ;; biji jagung | kuning ;; kacang hijau | hijau ;; kacang merah | merah ;; beras | putih ;; kulit telur | putih krem ;; kacang kedelai hitam | hitam ~ Bahan alam untuk mozaik.
@ Menggambar flora dan fauna
min: 10
act: Gambar satu tanaman dan satu hewan yang ada di sekitar rumah, lalu warnai.
mis: menggambar hewan tanpa memperhatikan bentuk dasarnya
exp: Flora adalah tumbuhan dan fauna adalah hewan. Menggambar flora dan fauna bisa dimulai dari bentuk dasar, misalnya lingkaran untuk kepala kucing dan oval untuk badannya. Setelah itu tambahkan detail seperti telinga, ekor, daun, atau kelopak bunga, lalu warnai.
ex: Kepala kucing digambar dengan lingkaran. // Daun digambar dengan bentuk oval runcing.
pt: Flora tumbuhan, fauna hewan ; Mulai dari bentuk dasar ; Tambahkan detail dan warna
sum: Bentuk dasar memudahkan menggambar flora dan fauna.
fig: table Objek | Bentuk dasar ;; kepala kucing | lingkaran ;; badan ikan | oval ;; atap rumah burung | segitiga ;; daun mangga | oval runcing ;; batang pohon | persegi panjang ;; kelopak bunga matahari | tetes air ~ Bentuk dasar untuk menggambar flora dan fauna.
@ Ragam hias
min: 10
act: Cari motif ragam hias pada batik, piring, atau taplak meja di rumah.
mis: mengira ragam hias hanya ada pada kain batik
exp: Ragam hias adalah gambar hiasan yang dipakai untuk memperindah benda. Ragam hias bisa bermotif tumbuhan atau flora, hewan atau fauna, bentuk geometris, dan manusia. Ragam hias dibuat berulang dan teratur.
ex: Motif bunga pada taplak meja. // Motif garis zigzag pada anyaman.
pt: Ragam hias memperindah benda ; Motif flora, fauna, geometris, manusia ; Dibuat berulang dan teratur
sum: Ragam hias membuat benda lebih indah.
fig: table Motif | Contoh ;; flora | bunga dan daun ;; fauna | burung dan ikan ;; geometris | segitiga dan garis ;; manusia | wayang ;; alam | awan dan ombak ;; bintang | segi lima berulang ~ Jenis motif ragam hias.
@ Tempo lagu
min: 10
act: Nyanyikan satu lagu dengan cepat lalu dengan lambat, dan rasakan perbedaannya.
mis: mengira tempo adalah keras lembutnya lagu
exp: Tempo adalah cepat lambatnya lagu dinyanyikan atau dimainkan. Lagu gembira biasanya bertempo cepat, sedangkan lagu sedih atau lagu nina bobo bertempo lambat. Tempo yang tepat membuat perasaan lagu tersampaikan.
ex: Lagu Naik Delman dinyanyikan cepat dan riang. // Lagu nina bobo dinyanyikan lambat.
pt: Tempo cepat lambatnya lagu ; Lagu gembira cepat ; Lagu sedih atau tenang lambat
sum: Tempo membuat lagu terasa riang atau tenang.
fig: table Istilah tempo | Arti ;; allegro | cepat ;; moderato | sedang ;; andante | agak lambat ;; largo | sangat lambat ;; presto | sangat cepat ;; ritardando | makin lambat ~ Istilah tempo dalam musik.
@ Dinamika lagu
min: 10
act: Nyanyikan lagu Balonku dengan bagian awal pelan lalu makin keras.
mis: tertukar antara tempo dan dinamika
exp: Dinamika adalah keras lembutnya lagu dinyanyikan. Lagu bisa dinyanyikan lembut, sedang, atau keras sesuai perasaannya. Dalam musik, tanda p berarti lembut dan tanda f berarti keras. Dinamika membuat lagu tidak membosankan.
ex: Lagu semangat dinyanyikan keras. // Lagu tidur dinyanyikan lembut.
pt: Dinamika keras lembutnya lagu ; Tanda p lembut ; Tanda f keras
sum: Dinamika membuat lagu lebih hidup.
fig: table Tanda dinamika | Arti ;; p | lembut ;; pp | sangat lembut ;; mf | agak keras ;; f | keras ;; ff | sangat keras ;; cresc | makin keras ~ Tanda dinamika lagu.
@ Mengenal not angka
min: 10
act: Mainkan nada do re mi di pianika atau aplikasi piano, lalu tulis not angkanya.
mis: membaca not angka 5 sebagai fa
exp: Not angka adalah lambang nada yang ditulis dengan angka. Angka 1 dibaca do, 2 dibaca re, 3 dibaca mi, 4 dibaca fa, 5 dibaca sol, 6 dibaca la, dan 7 dibaca si. Titik di atas angka menunjukkan nada lebih tinggi.
ex: 1 2 3 dibaca do re mi. // 5 6 7 dibaca sol la si.
pt: 1 do, 2 re, 3 mi ; 4 fa, 5 sol ; 6 la, 7 si
sum: Not angka memudahkan kita membaca lagu.
fig: table Not angka | Dibaca ;; 1 | do ;; 2 | re ;; 3 | mi ;; 4 | fa ;; 5 | sol ;; 6 | la ~ Not angka dan cara membacanya.
@ Sikap bernyanyi yang benar
min: 10
act: Bernyanyi di depan cermin dengan sikap berdiri tegak dan mulut terbuka lebar.
mis: bernyanyi sambil membungkuk
exp: Sikap bernyanyi yang benar membuat suara terdengar jelas dan merdu. Berdiri atau duduk tegak, bahu rileks, pandangan ke depan, mulut terbuka sesuai vokal, dan bernapas dengan baik. Ambil napas di akhir kalimat lagu.
ex: Berdiri tegak saat menyanyikan lagu wajib. // Ambil napas di akhir kalimat lagu.
pt: Badan tegak dan bahu rileks ; Mulut terbuka sesuai vokal ; Ambil napas di akhir kalimat
sum: Sikap yang benar membuat suara bernyanyi lebih baik.
fig: table Bagian | Sikap benar ;; badan | tegak ;; bahu | rileks ;; pandangan | ke depan ;; mulut | terbuka sesuai vokal ;; napas | diambil di akhir kalimat ;; tangan | di samping badan ~ Sikap bernyanyi yang benar.
# 2|Tari, Teater, dan Kriya
@ Pola lantai tari
min: 10
act: Gambar pola lantai lurus dan lengkung di kertas, lalu praktikkan berjalan mengikuti polanya.
mis: mengira pola lantai adalah lantai panggung yang dihias
exp: Pola lantai adalah garis yang dilalui penari saat menari di panggung. Ada pola lantai garis lurus, seperti garis horizontal, vertikal, dan diagonal. Ada juga pola lantai garis lengkung, seperti lingkaran, angka delapan, dan spiral.
ex: Penari membentuk lingkaran. // Penari berbaris lurus ke belakang.
pt: Pola lantai garis yang dilalui penari ; Ada pola lurus dan lengkung ; Membuat tari lebih indah
sum: Pola lantai mengatur posisi penari di panggung.
fig: table Pola lantai | Jenis garis ;; berbaris ke samping | horizontal ;; berbaris ke belakang | vertikal ;; berbaris miring | diagonal ;; membentuk bundar | lingkaran ;; bergerak seperti angka 8 | angka delapan ;; berputar ke tengah | spiral ~ Contoh pola lantai tari.
@ Properti tari
min: 10
act: Buat selendang atau kipas dari kertas untuk properti menari.
mis: mengira properti tari sama dengan kostum
exp: Properti tari adalah benda yang dipakai penari untuk mendukung gerakan. Contohnya selendang, kipas, piring, payung, dan tongkat. Properti membuat tarian lebih menarik dan menunjukkan ciri khas tarian.
ex: Tari Piring memakai piring. // Tari Kipas memakai kipas.
pt: Properti mendukung gerakan ; Contohnya selendang dan kipas ; Menunjukkan ciri khas tarian
sum: Properti membuat tarian lebih menarik.
fig: table Tarian | Properti ;; Tari Piring | piring ;; Tari Kipas Pakarena | kipas ;; Tari Payung | payung ;; Tari Jaranan | kuda kepang ;; Tari Gambyong | selendang ;; Tari Lilin | lilin ~ Tarian dan propertinya.
@ Tari kreasi anak
min: 10
act: Buat empat gerakan tari sendiri menirukan kupu-kupu, lalu tampilkan di depan keluarga.
mis: mengira tari kreasi tidak boleh memakai gerak tradisional
exp: Tari kreasi adalah tari yang gerakannya dikembangkan secara bebas dan baru. Tari kreasi bisa terinspirasi dari alam, hewan, atau kegiatan sehari-hari. Gerakannya bisa memakai unsur tari tradisional yang dikembangkan.
ex: Tari kupu-kupu dengan gerak tangan mengepak. // Tari petani menirukan gerak menanam padi.
pt: Gerakan dikembangkan bebas ; Terinspirasi alam dan kegiatan ; Boleh memakai unsur tradisional
sum: Tari kreasi mengasah kreativitas.
fig: table Inspirasi | Gerak tari ;; kupu-kupu | tangan mengepak ;; pohon | badan meliuk ;; petani | menanam padi ;; ombak | tangan bergelombang ;; burung | merentang tangan ;; hujan | jari bergetar turun ~ Inspirasi gerak tari kreasi.
@ Unsur pertunjukan teater
min: 10
act: Mainkan drama pendek bersama keluarga dengan naskah tiga baris dialog.
mis: mengira teater hanya berupa tarian
exp: Teater adalah seni pertunjukan yang menampilkan cerita melalui dialog dan gerak pemain. Unsur teater antara lain naskah, pemain, sutradara, panggung, kostum, dan penonton. Pemain memerankan tokoh sesuai naskah.
ex: Sutradara mengatur jalannya pertunjukan. // Pemain menghafal dialog dalam naskah.
pt: Teater menampilkan cerita ; Ada naskah, pemain, sutradara ; Pemain memerankan tokoh
sum: Teater membutuhkan kerja sama banyak orang.
fig: table Unsur teater | Peran ;; naskah | berisi cerita dan dialog ;; pemain | memerankan tokoh ;; sutradara | mengatur pertunjukan ;; panggung | tempat bermain ;; kostum | pakaian tokoh ;; penonton | menyaksikan pertunjukan ~ Unsur pertunjukan teater.
@ Boneka tangan
min: 10
act: Buat boneka tangan dari kaus kaki bekas, lalu gunakan untuk bercerita.
mis: menggerakkan mulut boneka tidak sesuai dengan dialog
exp: Boneka tangan adalah boneka yang dimainkan dengan memasukkan tangan ke dalamnya. Boneka tangan dipakai untuk bercerita atau bermain drama. Boneka tangan bisa dibuat dari kaus kaki bekas, kain flanel, atau kantong kertas.
ex: Boneka kancil dari kain flanel. // Mulut boneka bergerak saat tokoh berbicara.
pt: Dimainkan dengan tangan di dalamnya ; Dipakai untuk bercerita ; Bisa dari bahan bekas
sum: Boneka tangan membuat cerita lebih menarik.
fig: table Bahan | Bagian boneka ;; kaus kaki bekas | badan boneka ;; kancing | mata ;; kain flanel merah | lidah ;; benang wol | rambut ;; spidol | alis ;; lem kain | perekat ~ Bahan membuat boneka tangan.
@ Kerajinan dari bahan bekas
min: 10
act: Buat tempat pensil dari kaleng atau botol bekas, lalu hias dengan kertas warna.
mis: memakai bahan bekas yang tajam tanpa dirapikan
exp: Kerajinan bahan bekas adalah karya yang dibuat dari barang yang sudah tidak terpakai. Contohnya botol plastik, kardus, kaleng, dan koran. Membuat kerajinan dari bahan bekas mengurangi sampah dan melatih kreativitas. Bahan harus dibersihkan dan bagian tajam dirapikan.
ex: Pot bunga dari botol plastik. // Rumah-rumahan dari kardus.
pt: Memakai barang tidak terpakai ; Mengurangi sampah ; Bersihkan dan rapikan bahan
sum: Bahan bekas bisa menjadi karya yang berguna.
fig: table Bahan bekas | Hasil kerajinan ;; botol plastik | pot bunga ;; kardus | rumah-rumahan ;; kaleng | tempat pensil ;; koran | keranjang anyaman ;; tutup botol | mainan roda ;; kain perca | keset ~ Bahan bekas dan hasil kerajinannya.
@ Jumputan
min: 10
act: Ikat kain putih dengan karet, celupkan ke pewarna, lalu buka ikatannya dan lihat motifnya.
mis: membuka ikatan sebelum kain kering
exp: Jumputan adalah teknik menghias kain dengan cara diikat lalu dicelup ke pewarna. Bagian yang diikat tidak terkena warna sehingga membentuk motif. Jumputan bisa memakai karet, tali rafia, atau kelereng yang dibungkus kain.
ex: Kain diikat dengan karet membentuk lingkaran. // Kelereng dibungkus kain untuk motif bulat.
pt: Kain diikat lalu dicelup ; Bagian terikat tidak berwarna ; Bisa memakai karet atau kelereng
sum: Jumputan menghasilkan motif dari ikatan kain.
fig: table Bahan atau alat | Kegunaan ;; kain putih | bahan yang dihias ;; karet gelang | mengikat kain ;; pewarna | mewarnai kain ;; ember | tempat mencelup ;; kelereng | membuat motif bulat ;; sarung tangan plastik | melindungi tangan ~ Bahan dan alat jumputan.
@ Membentuk tanah liat
min: 10
act: Buat celengan atau mangkuk kecil dari tanah liat dengan teknik pilin.
mis: membiarkan tanah liat terlalu kering sehingga retak saat dibentuk
exp: Tanah liat dapat dibentuk menjadi berbagai benda, seperti gerabah, celengan, dan patung. Ada teknik pijit, teknik pilin, dan teknik lempeng. Teknik pijit dengan cara memijit tanah liat, teknik pilin dengan menyusun pilinan, dan teknik lempeng dengan menyusun lembaran tanah liat.
ex: Mangkuk kecil dibuat dengan teknik pijit. // Vas dibuat dengan menyusun pilinan.
pt: Teknik pijit, pilin, dan lempeng ; Tanah liat dijaga tetap lembap ; Hasilnya dikeringkan
sum: Tanah liat bisa dibentuk dengan berbagai teknik.
fig: table Teknik | Cara membentuk ;; pijit | memijit dengan jari ;; pilin | menyusun gulungan memanjang ;; lempeng | menyusun lembaran pipih ;; putar | memakai meja putar ;; cetak | memakai cetakan ;; butsir | menambah dan mengurangi tanah liat ~ Teknik membentuk tanah liat.
"""

BANK += """
## SBD|Mozaik
Mozaik dibuat dengan cara …|menempel potongan kecil bahan|melipat kertas|menjahit kain|melukis dengan kuas|Menempel potongan kecil.
Potongan mozaik ditempel …|rapat dengan sedikit celah|saling bertumpuk|asal-asalan|di luar gambar|Rapat dan tidak bertumpuk.
=|Biji yang berwarna kuning untuk mozaik adalah biji …|jagung|Biji jagung kuning.
=|Kacang hijau memberi warna … pada mozaik.|hijau|Hijau.
B|Kulit telur dapat dipakai untuk membuat mozaik.|Bahan mozaik.
S|Potongan mozaik harus saling bertumpuk.|Tidak bertumpuk.
Perbedaan mozaik dan kolase adalah potongan mozaik …|tidak saling bertumpuk|lebih berwarna|lebih besar|tidak memakai lem|Kolase boleh bertumpuk.
Alat untuk menempel bahan mozaik adalah …|lem|penggaris|jangka|penghapus|Lem.
## SBD|Menggambar flora dan fauna
Flora artinya …|tumbuhan|hewan|batu|air|Flora tumbuhan.
Fauna artinya …|hewan|tumbuhan|bangunan|kendaraan|Fauna hewan.
=|Kepala kucing dapat digambar dari bentuk dasar …|lingkaran|Lingkaran.
=|Badan ikan dapat digambar dari bentuk dasar …|oval;lonjong|Oval.
B|Menggambar dimulai dari bentuk dasar.|Bentuk dasar.
S|Bentuk dasar tidak membantu menggambar hewan.|Sangat membantu.
Contoh flora adalah …|bunga mawar|kucing|ikan|burung|Mawar tumbuhan.
Contoh fauna adalah …|kupu-kupu|pohon mangga|rumput|bunga melati|Kupu-kupu hewan.
## SBD|Ragam hias
Ragam hias berfungsi untuk …|memperindah benda|membuat benda berat|merusak benda|menyembunyikan benda|Memperindah.
Motif ragam hias berbentuk bunga dan daun disebut motif …|flora|fauna|geometris|manusia|Flora.
=|Motif ragam hias berbentuk hewan disebut motif …|fauna|Fauna.
=|Motif segitiga dan garis disebut motif …|geometris|Geometris.
B|Ragam hias dibuat berulang dan teratur.|Berulang.
S|Ragam hias hanya ada pada kain batik.|Ada pada banyak benda.
Contoh motif manusia pada ragam hias adalah …|wayang|bunga|ikan|segitiga|Wayang.
Benda yang sering dihias ragam hias adalah …|taplak meja|air minum|udara|tanah|Taplak.
## SBD|Tempo lagu
Tempo adalah … lagu.|cepat lambatnya|keras lembutnya|tinggi rendahnya|panjang pendeknya kata|Tempo cepat lambat.
Lagu gembira biasanya bertempo …|cepat|sangat lambat|diam|lambat sekali|Cepat.
=|Istilah tempo allegro artinya …|cepat|Allegro cepat.
=|Istilah tempo largo artinya sangat …|lambat|Largo sangat lambat.
B|Lagu nina bobo dinyanyikan dengan tempo lambat.|Lambat.
S|Tempo adalah keras lembutnya lagu.|Itu dinamika.
Istilah tempo yang artinya sedang adalah …|moderato|allegro|largo|presto|Moderato.
Ritardando artinya …|makin lambat|makin cepat|makin keras|makin lembut|Makin lambat.
## SBD|Dinamika lagu
Dinamika adalah … lagu.|keras lembutnya|cepat lambatnya|tinggi rendahnya|judul|Dinamika keras lembut.
Tanda dinamika f artinya …|keras|lembut|lambat|cepat|f = forte.
=|Tanda dinamika p artinya …|lembut|p = piano.
=|Tanda ff artinya sangat …|keras|Fortissimo.
B|Dinamika membuat lagu tidak membosankan.|Lebih hidup.
S|Tanda pp artinya sangat keras.|pp sangat lembut.
Lagu semangat seperti lagu perjuangan biasanya dinyanyikan …|keras|sangat lembut|berbisik|diam|Keras.
Tanda mf artinya …|agak keras|sangat lembut|sangat cepat|lambat|mf agak keras.
## SBD|Mengenal not angka
Not angka 1 dibaca …|do|re|mi|fa|1 = do.
Not angka 5 dibaca …|sol|fa|la|si|5 = sol.
=|Not angka 3 dibaca …|mi|3 = mi.
=|Not angka 7 dibaca …|si|7 = si.
B|Not angka 4 dibaca fa.|4 = fa.
S|Not angka 6 dibaca re.|6 = la.
Titik di atas not angka menunjukkan nada …|lebih tinggi|lebih rendah|lebih pelan|diam|Lebih tinggi.
Urutan do re mi ditulis dengan not angka …|1 2 3|3 2 1|1 3 5|5 6 7|1 2 3.
## SBD|Sikap bernyanyi yang benar
Saat bernyanyi, badan sebaiknya …|tegak|membungkuk|berbaring|bersandar malas|Tegak.
Napas saat bernyanyi diambil di …|akhir kalimat lagu|tengah kata|setiap huruf|tidak pernah|Akhir kalimat.
=|Saat bernyanyi, bahu dibuat …|rileks;santai|Rileks.
=|Saat bernyanyi, pandangan diarahkan ke …|depan|Ke depan.
B|Mulut dibuka sesuai vokal saat bernyanyi.|Sesuai vokal.
S|Bernyanyi sambil membungkuk membuat suara lebih jelas.|Suara tertahan.
Sikap bernyanyi yang benar membuat suara …|jelas dan merdu|serak|hilang|tertahan|Jelas dan merdu.
Posisi tangan saat bernyanyi berdiri adalah …|di samping badan|di saku|menutup mulut|menutup telinga|Di samping badan.
## SBD|Pola lantai tari
Pola lantai adalah garis yang dilalui … di panggung.|penari|penonton|pemusik|kursi|Penari.
Pola lantai berbaris ke samping disebut …|horizontal|vertikal|diagonal|lingkaran|Horizontal.
=|Pola lantai berbaris ke belakang disebut …|vertikal|Vertikal.
=|Pola lantai berbaris miring disebut …|diagonal|Diagonal.
B|Lingkaran termasuk pola lantai garis lengkung.|Lengkung.
S|Pola lantai adalah hiasan lantai panggung.|Pola lantai adalah garis gerak penari.
Pola lantai yang bergerak seperti angka delapan termasuk garis …|lengkung|lurus|putus-putus|zigzag|Lengkung.
Manfaat pola lantai adalah …|tarian lebih indah dan rapi|penari bertabrakan|panggung kotor|musik berhenti|Lebih rapi.
## SBD|Properti tari
Properti tari adalah benda yang …|mendukung gerakan penari|dipakai penonton|dijual di panggung|menutup panggung|Mendukung gerakan.
Tari Piring memakai properti …|piring|kipas|payung|selendang|Piring.
=|Tari Jaranan memakai properti kuda …|kepang|Kuda kepang.
=|Tari Gambyong memakai properti …|selendang|Selendang.
B|Properti membuat tarian lebih menarik.|Lebih menarik.
S|Properti tari sama dengan kostum penari.|Properti benda pendukung.
Tari Kipas Pakarena berasal dari …|Sulawesi Selatan|Bali|Aceh|Papua|Pakarena dari Sulawesi Selatan.
Kipas dari kertas dapat dipakai sebagai …|properti tari|alat makan|alas kaki|topi|Properti.
## SBD|Tari kreasi anak
Tari kreasi adalah tari yang gerakannya …|dikembangkan secara bebas|tidak boleh diubah|sangat kuno|selalu sama|Bebas dan baru.
Gerak tangan mengepak cocok untuk tari kreasi bertema …|kupu-kupu|ikan|ular|kura-kura|Kupu-kupu.
=|Gerak badan meliuk dapat menirukan … tertiup angin.|pohon|Pohon.
=|Tari kreasi melatih …|kreativitas|Kreativitas.
B|Tari kreasi boleh memakai unsur gerak tradisional.|Boleh.
S|Tari kreasi tidak boleh terinspirasi dari alam.|Boleh terinspirasi alam.
Gerak menanam padi dalam tari kreasi menirukan kegiatan …|petani|nelayan|dokter|guru|Petani.
Gerak tangan bergelombang dapat menirukan …|ombak|batu|gunung|rumah|Ombak.
## SBD|Unsur pertunjukan teater
Orang yang mengatur jalannya pertunjukan teater disebut …|sutradara|penonton|pemain|penata lampu|Sutradara.
Naskah teater berisi …|cerita dan dialog|daftar harga|resep|lagu kebangsaan|Cerita dan dialog.
=|Tempat pemain teater bermain disebut …|panggung|Panggung.
=|Orang yang memerankan tokoh disebut …|pemain;aktor|Pemain.
B|Penonton termasuk unsur pertunjukan teater.|Penonton.
S|Teater tidak memerlukan naskah sama sekali.|Teater memakai naskah.
Pakaian yang dikenakan pemain sesuai tokoh disebut …|kostum|naskah|properti panggung|tiket|Kostum.
Teater menampilkan cerita melalui …|dialog dan gerak|lukisan saja|tulisan saja|foto|Dialog dan gerak.
## SBD|Boneka tangan
Boneka tangan dimainkan dengan cara …|memasukkan tangan ke dalam boneka|ditarik tali|ditiup|diputar mesin|Tangan di dalam.
Bahan bekas untuk boneka tangan adalah …|kaus kaki bekas|kaca|besi|batu|Kaus kaki bekas.
=|Mata boneka tangan dapat dibuat dari …|kancing|Kancing.
=|Rambut boneka dapat dibuat dari benang …|wol|Benang wol.
B|Boneka tangan dapat dipakai untuk bercerita.|Bercerita.
S|Mulut boneka bergerak saat tokohnya diam.|Bergerak saat berbicara.
Kain merah flanel pada boneka tangan dapat dijadikan …|lidah|mata|telinga|rambut|Lidah.
Manfaat boneka tangan dalam bercerita adalah …|cerita lebih menarik|cerita membosankan|penonton takut|cerita lebih pendek|Lebih menarik.
## SBD|Kerajinan dari bahan bekas
Kerajinan bahan bekas dibuat dari …|barang yang tidak terpakai|barang baru mahal|makanan|air|Barang tidak terpakai.
Botol plastik bekas dapat dibuat menjadi …|pot bunga|roti|baju baru|sepatu kulit|Pot bunga.
=|Kaleng bekas dapat dibuat menjadi tempat …|pensil|Tempat pensil.
=|Kardus bekas dapat dibuat menjadi rumah- …|rumahan|Rumah-rumahan.
B|Membuat kerajinan dari bahan bekas mengurangi sampah.|Mengurangi sampah.
S|Bahan bekas yang tajam boleh dipakai tanpa dirapikan.|Harus dirapikan.
Kain perca dapat dibuat menjadi …|keset|gelas|pot tanah liat|piring|Keset.
Sebelum dipakai, bahan bekas sebaiknya …|dibersihkan|dibakar|dibuang|direndam lumpur|Dibersihkan.
## SBD|Jumputan
Jumputan dibuat dengan cara kain …|diikat lalu dicelup pewarna|dijahit lalu dilukis|digunting lalu ditempel|dilipat lalu disetrika|Diikat dan dicelup.
Bagian kain yang diikat saat jumputan akan …|tidak terkena warna|berwarna paling gelap|robek|hilang|Tidak terkena warna.
=|Alat untuk mengikat kain jumputan adalah karet …|gelang|Karet gelang.
=|Untuk membuat motif bulat, kain dapat dibungkuskan pada …|kelereng|Kelereng.
B|Sarung tangan plastik melindungi tangan dari pewarna.|Melindungi tangan.
S|Ikatan jumputan dibuka sebelum dicelup.|Dibuka setelah dicelup dan kering.
Bahan kain yang cocok untuk jumputan adalah kain …|putih|plastik|kertas|karet|Kain putih.
Tempat untuk mencelup kain jumputan adalah …|ember|piring kecil|botol|kantong kertas|Ember.
## SBD|Membentuk tanah liat
Teknik membentuk tanah liat dengan memijit disebut teknik …|pijit|pilin|lempeng|cetak|Pijit.
Teknik menyusun gulungan memanjang tanah liat disebut teknik …|pilin|pijit|lempeng|butsir|Pilin.
=|Teknik menyusun lembaran tanah liat pipih disebut teknik …|lempeng|Lempeng.
=|Supaya tidak retak, tanah liat dijaga tetap …|lembap|Lembap.
B|Tanah liat dapat dibentuk menjadi celengan.|Celengan.
S|Tanah liat yang sangat kering mudah dibentuk.|Mudah retak.
Benda dari tanah liat disebut …|gerabah|anyaman|batik|tenun|Gerabah.
Teknik membentuk tanah liat memakai meja putar disebut teknik …|putar|pilin|pijit|lempeng|Putar.
"""

SAS += """
## SBD 1
0|Mozaik dari beras akan berwarna ....|putih|hijau|merah|hitam|Beras putih.
1|Batang pohon dapat digambar dari bentuk dasar ....|persegi panjang|lingkaran|segitiga|bintang|Persegi panjang.
2|Ragam hias bermotif awan dan ombak termasuk motif ....|alam|fauna|manusia|wayang|Motif alam.
3|Istilah tempo presto artinya ....|sangat cepat|sangat lambat|sedang|agak lambat|Presto sangat cepat.
4|Tanda cresc dalam lagu artinya ....|makin keras|makin lembut|makin lambat|makin cepat|Crescendo.
5|Not angka 2 dibaca ....|re|do|mi|sol|2 = re.
6|Saat bernyanyi, posisi badan yang benar adalah ....|tegak|membungkuk|miring|berbaring|Tegak.
## SBD 2
0|Pola lantai berputar ke tengah disebut pola ....|spiral|horizontal|vertikal|diagonal|Spiral.
1|Tari Lilin menggunakan properti ....|lilin|piring|kipas|payung|Lilin.
2|Tari kreasi bertema hujan dapat memakai gerak ....|jari bergetar turun|melompat jauh|berbaring diam|berlari keluar|Hujan turun.
3|Unsur teater yang berupa pakaian tokoh disebut ....|kostum|naskah|panggung|sutradara|Kostum.
4|Bahan perekat bagian boneka tangan adalah ....|lem kain|air|tepung kering|pasir|Lem kain.
5|Tutup botol bekas dapat dijadikan ....|mainan roda|pot bunga|keset|keranjang|Roda mainan.
6|Kain jumputan diikat sebelum ....|dicelup pewarna|dijahit|digunting|dijemur|Diikat lalu dicelup.
7|Teknik membentuk tanah liat dengan menambah dan mengurangi bahan disebut ....|butsir|pilin|lempeng|pijit|Butsir.
"""

TOPICS += """
## PJOK
# 1|Atletik dan Permainan Bola
@ Lari jarak pendek
min: 10
act: Berlomba lari 30 meter bersama saudara dengan aba-aba bersedia, siap, ya.
mis: mengangkat kepala ke atas saat berlari cepat
exp: Lari jarak pendek atau sprint adalah lari secepat-cepatnya dalam jarak pendek. Lari dimulai dengan aba-aba bersedia, siap, ya. Saat berlari, badan condong ke depan, lengan diayun, dan pandangan lurus ke depan. Pelari tidak boleh pindah lintasan.
ex: Start jongkok saat aba-aba bersedia. // Ayunan lengan membantu lari lebih cepat.
pt: Lari secepatnya ; Aba-aba bersedia, siap, ya ; Badan condong dan lengan diayun
sum: Teknik yang benar membuat lari lebih cepat.
fig: table Bagian | Teknik ;; aba-aba pertama | bersedia ;; aba-aba kedua | siap ;; aba-aba terakhir | ya ;; badan | condong ke depan ;; lengan | diayun bergantian ;; pandangan | lurus ke garis finis ~ Teknik lari jarak pendek.
@ Lompat jauh tanpa awalan
min: 10
act: Lakukan lompat jauh dari garis di halaman, lalu ukur jarak lompatanmu dengan meteran.
mis: mendarat dengan badan jatuh ke belakang
exp: Lompat jauh tanpa awalan dilakukan dari posisi berdiri di belakang garis. Tekuk lutut, ayunkan kedua lengan ke belakang lalu ke depan, tolak dengan kedua kaki, dan mendarat dengan dua kaki. Saat mendarat, badan condong ke depan supaya tidak jatuh ke belakang.
ex: Ayunkan lengan untuk membantu lompatan. // Jarak diukur dari garis sampai bekas kaki terdekat.
pt: Tekuk lutut dan ayun lengan ; Tolak dengan dua kaki ; Mendarat dengan badan condong ke depan
sum: Ayunan lengan dan tolakan kuat membuat lompatan lebih jauh.
fig: table Tahap | Gerakan ;; awalan | berdiri di belakang garis ;; persiapan | menekuk lutut ;; ayunan | lengan ke belakang lalu ke depan ;; tolakan | dua kaki menolak bersamaan ;; melayang | badan di udara ;; mendarat | dua kaki dan badan condong ~ Tahapan lompat jauh tanpa awalan.
@ Menggiring bola basket
min: 10
act: Pantulkan bola sambil berjalan mengelilingi halaman tanpa melihat bola terus-menerus.
mis: memukul bola dengan telapak tangan yang kaku
exp: Menggiring bola basket atau dribbling adalah memantulkan bola ke lantai sambil bergerak. Bola didorong dengan jari-jari tangan yang lentur, bukan dipukul. Bola dipantulkan setinggi pinggang dan pandangan sesekali ke depan.
ex: Dribel bola sambil berjalan lurus. // Dribel bola dengan tangan kanan dan kiri bergantian.
pt: Pantulkan bola dengan jari-jari ; Setinggi pinggang ; Pandangan ke depan
sum: Menggiring bola basket melatih koordinasi tangan dan mata.
fig: table Bagian | Petunjuk ;; tangan | jari-jari lentur ;; tinggi bola | setinggi pinggang ;; pandangan | ke depan ;; lutut | sedikit ditekuk ;; gerakan | mendorong bukan memukul ;; tangan bergantian | kanan dan kiri ~ Petunjuk menggiring bola basket.
@ Mengoper bola dalam sepak bola
min: 10
act: Berlatih mengoper bola kepada teman dari jarak lima langkah sebanyak sepuluh kali.
mis: mengoper bola terlalu keras kepada teman yang dekat
exp: Mengoper bola adalah mengirim bola kepada teman satu tim. Mengoper jarak dekat memakai kaki bagian dalam. Kaki tumpu diletakkan di samping bola, pandangan ke arah teman, dan bola ditendang dengan tenaga secukupnya. Teman menerima bola dengan menghentikannya memakai kaki bagian dalam.
ex: Mengoper mendatar kepada teman di samping. // Menghentikan bola dengan telapak kaki.
pt: Gunakan kaki bagian dalam ; Lihat teman sebelum mengoper ; Tenaga secukupnya
sum: Operan yang tepat membuat tim bermain kompak.
fig: table Gerakan | Bagian kaki ;; mengoper jarak dekat | kaki bagian dalam ;; mengoper jarak jauh | punggung kaki ;; menghentikan bola | telapak kaki ;; menggiring | kaki bagian luar dan dalam ;; menendang ke gawang | punggung kaki penuh ;; menahan bola menggelinding | sisi dalam kaki ~ Bagian kaki dalam permainan sepak bola.
@ Passing bawah bola voli
min: 10
act: Lambungkan bola plastik dan pantulkan dengan kedua lengan yang dirapatkan.
mis: memukul bola dengan kepalan tangan terbuka satu tangan
exp: Passing bawah adalah memantulkan bola voli dengan kedua lengan bagian bawah yang dirapatkan. Kedua tangan saling menggenggam, lutut ditekuk, dan bola dipantulkan dengan dorongan kaki ke atas. Passing bawah biasanya dipakai untuk menerima bola dari lawan.
ex: Tangan kanan menggenggam tangan kiri. // Bola mengenai lengan bawah, bukan telapak tangan.
pt: Kedua lengan dirapatkan ; Lutut ditekuk ; Dorong dengan kaki ke atas
sum: Passing bawah dipakai untuk menerima bola rendah.
fig: table Bagian | Posisi ;; tangan | saling menggenggam ;; lengan | lurus dan rapat ;; lutut | ditekuk ;; badan | condong ke depan ;; kaki | dibuka selebar bahu ;; perkenaan bola | lengan bawah ~ Posisi tubuh saat passing bawah.
@ Permainan bentengan
min: 10
act: Ajak teman bermain bentengan dengan dua tiang sebagai benteng.
mis: menyentuh benteng lawan tanpa memperhatikan lawan yang lebih baru keluar
exp: Bentengan adalah permainan tradisional berkelompok. Setiap kelompok memiliki benteng berupa tiang atau pohon. Pemain berusaha menyentuh benteng lawan dan menangkap pemain lawan. Pemain yang lebih baru keluar dari benteng bisa menangkap pemain lawan yang lebih dulu keluar.
ex: Tim menang jika menyentuh benteng lawan. // Pemain yang tertangkap menjadi tawanan.
pt: Dimainkan berkelompok ; Sentuh benteng lawan ; Kerja sama dan strategi
sum: Bentengan melatih kecepatan dan kerja sama.
fig: table Istilah bentengan | Arti ;; benteng | tiang markas tim ;; tawanan | pemain yang tertangkap ;; penjaga | menjaga benteng sendiri ;; penyerang | berusaha menyentuh benteng lawan ;; menang | menyentuh benteng lawan ;; membebaskan | menyentuh teman yang ditawan ~ Istilah dalam permainan bentengan.
@ Lari zig-zag
min: 10
act: Susun lima botol berjajar, lalu lari berkelok di antaranya secepat mungkin.
mis: menyentuh atau menjatuhkan rintangan saat berbelok
exp: Lari zig-zag adalah lari berkelok-kelok melewati rintangan. Lari zig-zag melatih kelincahan, yaitu kemampuan mengubah arah dengan cepat tanpa kehilangan keseimbangan. Saat berbelok, turunkan sedikit badan dan langkahkan kaki pendek-pendek.
ex: Lari melewati kerucut yang disusun berselang. // Berbelok tanpa menyentuh botol.
pt: Lari berkelok melewati rintangan ; Melatih kelincahan ; Langkah pendek saat berbelok
sum: Lari zig-zag melatih kelincahan.
fig: table Unsur kebugaran | Latihan ;; kelincahan | lari zig-zag ;; kecepatan | lari 30 meter ;; kekuatan kaki | lompat katak ;; daya tahan | lari santai 5 menit ;; keseimbangan | berdiri satu kaki ;; kelenturan | menyentuh ujung kaki ~ Unsur kebugaran dan latihannya.
# 2|Senam, Air, dan Kesehatan
@ Guling belakang
min: 10
act: Dengan bantuan orang dewasa, lakukan guling belakang di atas kasur atau matras.
mis: menahan berat badan dengan kepala, bukan dengan tangan
exp: Guling belakang dilakukan dari posisi jongkok membelakangi matras. Dagu ditempelkan ke dada, kedua tangan di samping telinga dengan telapak menghadap ke atas. Badan digulingkan ke belakang, tangan menolak matras, lalu kembali ke posisi jongkok.
ex: Dagu menempel di dada supaya leher aman. // Tangan menolak matras saat badan berguling.
pt: Mulai dari jongkok ; Dagu menempel dada ; Tangan menolak matras
sum: Guling belakang dilakukan dengan bantuan tangan dan di atas matras.
fig: table Tahap | Gerakan ;; awal | jongkok membelakangi matras ;; kepala | dagu menempel dada ;; tangan | di samping telinga ;; guling | badan bulat ke belakang ;; tolakan | tangan menolak matras ;; akhir | kembali jongkok ~ Tahapan guling belakang.
@ Sikap lilin
min: 10
act: Latih sikap lilin di atas matras selama hitungan sepuluh sambil dibantu keluarga.
mis: menekuk kaki saat sikap lilin
exp: Sikap lilin adalah sikap tubuh tegak terbalik bertumpu pada bahu dan tangan menyangga pinggang. Mulai dari berbaring, angkat kedua kaki lurus ke atas, tangan menyangga pinggang, dan pertahankan beberapa hitungan. Sikap lilin melatih kekuatan dan keseimbangan.
ex: Kaki lurus ke atas seperti batang lilin. // Siku menempel di matras.
pt: Bertumpu pada bahu ; Tangan menyangga pinggang ; Kaki lurus ke atas
sum: Sikap lilin melatih keseimbangan tubuh.
fig: table Bagian tubuh | Posisi sikap lilin ;; bahu | menjadi tumpuan ;; tangan | menyangga pinggang ;; siku | menempel matras ;; kaki | lurus ke atas ;; ujung kaki | menunjuk ke langit-langit ;; kepala | tetap di matras ~ Posisi tubuh saat sikap lilin.
@ Kelenturan tubuh
min: 10
act: Lakukan gerakan duduk berselonjor dan menyentuh ujung kaki setiap pagi selama seminggu.
mis: menyentak gerakan peregangan dengan keras
exp: Kelenturan adalah kemampuan tubuh untuk bergerak luas tanpa rasa sakit. Kelenturan dilatih dengan gerakan peregangan, misalnya menyentuh ujung kaki, meliukkan badan, dan merentangkan tangan. Peregangan dilakukan perlahan dan ditahan beberapa hitungan.
ex: Duduk berselonjor lalu menyentuh ujung kaki. // Berdiri lalu meliukkan badan ke samping.
pt: Kelenturan membuat gerak luas ; Dilatih dengan peregangan ; Lakukan perlahan dan tahan
sum: Tubuh yang lentur terhindar dari cedera.
fig: table Latihan | Bagian yang dilenturkan ;; menyentuh ujung kaki | otot paha belakang ;; meliukkan badan | pinggang ;; merentangkan tangan | bahu ;; memutar leher pelan | leher ;; menarik tumit ke belakang | paha depan ;; mendorong dinding | betis ~ Latihan kelenturan.
@ Kekuatan otot
min: 10
act: Hitung berapa kali kamu bisa melakukan push-up dan sit-up dalam satu menit.
mis: melakukan sit-up dengan menarik leher memakai tangan
exp: Kekuatan otot adalah kemampuan otot untuk mengangkat, menarik, atau menahan beban. Latihan kekuatan untuk anak antara lain push-up untuk otot lengan, sit-up untuk otot perut, dan squat untuk otot kaki. Latihan dilakukan bertahap dan dengan teknik yang benar.
ex: Push-up dengan lutut menempel lantai untuk pemula. // Sit-up dengan kaki ditekuk.
pt: Push-up untuk lengan ; Sit-up untuk perut ; Squat untuk kaki
sum: Otot yang kuat membantu kita bergerak dengan baik.
fig: table Latihan | Otot yang dilatih ;; push-up | lengan dan dada ;; sit-up | perut ;; squat | paha ;; back-up | punggung ;; jinjit naik turun | betis ;; bergantung di palang | genggaman tangan ~ Latihan kekuatan otot.
@ Meluncur di air
min: 10
act: Di kolam dangkal dengan pengawasan orang dewasa, dorong dinding kolam dan meluncur sejauh mungkin.
mis: mengangkat kepala tinggi saat meluncur
exp: Meluncur adalah gerakan maju di air dengan mendorong dinding kolam memakai kaki. Kedua tangan lurus di depan kepala, badan lurus, wajah masuk ke air, dan kaki rapat. Meluncur adalah dasar sebelum belajar gaya renang.
ex: Tolak dinding kolam dengan kedua kaki. // Badan lurus seperti anak panah.
pt: Tolak dinding dengan kaki ; Tangan lurus di depan kepala ; Badan lurus dan wajah di air
sum: Meluncur adalah dasar belajar berenang.
fig: table Bagian tubuh | Posisi meluncur ;; tangan | lurus di depan kepala ;; badan | lurus seperti anak panah ;; wajah | masuk ke air ;; kaki | rapat dan lurus ;; tolakan | dari dinding kolam ;; napas | ditahan sebentar ~ Posisi tubuh saat meluncur.
@ Gerakan kaki renang gaya bebas
min: 10
act: Berpegangan di tepi kolam dangkal, lalu latih gerakan kaki naik turun bergantian.
mis: menekuk lutut terlalu banyak saat menendang air
exp: Gerakan kaki gaya bebas dilakukan dengan menggerakkan kedua kaki naik turun bergantian. Gerakan berasal dari pangkal paha, lutut sedikit lentur, dan ujung kaki lurus ke belakang. Gerakan kaki membantu tubuh tetap mengapung dan maju.
ex: Berpegangan di pinggir kolam sambil menendang air. // Memakai papan pelampung untuk latihan kaki.
pt: Kaki naik turun bergantian ; Gerakan dari pangkal paha ; Ujung kaki lurus
sum: Gerakan kaki yang benar membuat renang lebih ringan.
fig: table Alat latihan renang | Kegunaan ;; papan pelampung | latihan gerak kaki ;; kacamata renang | melindungi mata ;; topi renang | melindungi rambut ;; pelampung lengan | membantu mengapung ;; tepi kolam | tempat berpegangan ;; peluit pelatih | memberi aba-aba ~ Alat bantu latihan renang.
@ Memilih jajanan sehat
min: 10
act: Saat jajan, periksa kemasan makanan: tanggal kedaluwarsa, warna, dan kebersihannya.
mis: memilih jajanan karena warnanya mencolok
exp: Jajanan sehat adalah makanan yang bersih, bergizi, dan aman. Pilih jajanan yang tertutup, tidak berwarna mencolok, tidak berbau aneh, dan belum kedaluwarsa. Hindari jajanan yang dihinggapi lalat atau dijual di tempat kotor.
ex: Membeli buah potong yang tertutup plastik bersih. // Memeriksa tanggal kedaluwarsa pada kemasan.
pt: Pilih yang bersih dan tertutup ; Hindari warna mencolok ; Periksa tanggal kedaluwarsa
sum: Jajanan sehat menjaga tubuh dari penyakit.
fig: table Ciri jajanan | Sehat atau tidak ;; tertutup rapi | sehat ;; warna sangat mencolok | tidak sehat karena pewarna ;; dihinggapi lalat | tidak sehat karena kuman ;; belum kedaluwarsa | aman dimakan ;; berbau tengik | tidak layak makan ;; dari buah dan sayur segar | bergizi ~ Ciri jajanan sehat dan tidak sehat.
@ Pertolongan pertama luka ringan
min: 10
act: Bersama orang tua, siapkan kotak P3K di rumah dan kenali isinya.
mis: menutup luka kotor tanpa membersihkannya
exp: Luka ringan seperti lecet atau tergores perlu ditangani supaya tidak infeksi. Cuci tangan, bersihkan luka dengan air mengalir, keringkan dengan kain bersih, beri obat antiseptik, lalu tutup dengan plester. Jika luka besar atau berdarah banyak, segera minta bantuan orang dewasa.
ex: Lutut lecet dibersihkan dengan air bersih. // Luka kecil ditutup plester.
pt: Bersihkan luka dengan air mengalir ; Beri antiseptik ; Tutup dengan plester
sum: Pertolongan pertama mencegah luka menjadi infeksi.
fig: table Isi kotak P3K | Kegunaan ;; plester | menutup luka kecil ;; kain kasa | menutup luka lebih besar ;; antiseptik | mencegah infeksi ;; gunting | memotong kasa ;; kapas | membersihkan sekitar luka ;; perban | membalut luka ~ Isi kotak P3K dan kegunaannya.
"""

BANK += """
## PJOK|Lari jarak pendek
Lari jarak pendek disebut juga …|sprint|maraton|estafet|jogging|Sprint.
Aba-aba lari jarak pendek adalah …|bersedia, siap, ya|satu, dua, tiga, empat|mulai, henti|ayo, cepat, lari|Aba-aba sprint.
=|Saat lari cepat, badan condong ke …|depan|Ke depan.
=|Saat lari, kedua lengan …|diayun|Diayun bergantian.
B|Pelari tidak boleh pindah lintasan.|Tetap di lintasan.
S|Saat lari cepat, kepala menengadah ke atas.|Pandangan lurus ke depan.
Start yang biasa dipakai pada lari jarak pendek adalah start …|jongkok|berdiri santai|duduk|tiduran|Start jongkok.
Garis akhir lomba lari disebut garis …|finis|start|tengah|samping|Finis.
## PJOK|Lompat jauh tanpa awalan
Lompat jauh tanpa awalan dimulai dari posisi …|berdiri di belakang garis|berlari kencang|duduk|berbaring|Berdiri.
Tolakan pada lompat jauh tanpa awalan memakai …|dua kaki|satu kaki|tangan|lutut|Dua kaki.
=|Untuk membantu lompatan, kedua … diayunkan.|lengan;tangan|Lengan.
=|Saat mendarat, badan condong ke …|depan|Ke depan.
B|Jarak lompatan diukur dari garis sampai bekas kaki terdekat.|Bekas terdekat.
S|Mendarat dengan badan jatuh ke belakang membuat lompatan lebih jauh.|Mengurangi jarak.
Tahap setelah tolakan adalah …|melayang|awalan|persiapan|berdiri|Melayang.
Alat untuk mengukur jarak lompatan adalah …|meteran|timbangan|jam|termometer|Meteran.
## PJOK|Menggiring bola basket
Menggiring bola basket disebut juga …|dribbling|shooting|passing|blocking|Dribbling.
Bola basket dipantulkan dengan …|jari-jari tangan|kepalan tangan|kaki|kepala|Jari-jari.
=|Tinggi pantulan bola saat menggiring sekitar setinggi …|pinggang|Pinggang.
=|Saat menggiring, lutut sedikit …|ditekuk|Ditekuk.
B|Bola didorong, bukan dipukul, saat menggiring.|Didorong.
S|Saat menggiring, pandangan harus selalu ke bola.|Sesekali ke depan.
Menggiring bola dengan tangan bergantian melatih …|kedua tangan|kaki saja|suara|mata saja|Kedua tangan.
Permainan yang memakai teknik dribel tangan adalah …|bola basket|sepak bola|bulu tangkis|renang|Bola basket.
## PJOK|Mengoper bola dalam sepak bola
Mengoper jarak dekat memakai kaki bagian …|dalam|luar|tumit|lutut|Bagian dalam.
Menghentikan bola dapat memakai …|telapak kaki|siku|kepala saja|punggung|Telapak kaki.
=|Mengoper adalah mengirim bola kepada teman … tim.|satu;sesama|Satu tim.
=|Sebelum mengoper, kita melihat ke arah …|teman|Melihat teman.
B|Operan jarak jauh dapat memakai punggung kaki.|Punggung kaki.
S|Operan untuk teman yang dekat harus sekeras mungkin.|Tenaga secukupnya.
Letak kaki tumpu saat mengoper adalah …|di samping bola|di atas bola|di belakang jauh|di depan bola|Di samping.
Operan yang baik membuat tim bermain …|kompak|kacau|lambat|sendiri-sendiri|Kompak.
## PJOK|Passing bawah bola voli
Passing bawah memakai bagian tubuh …|lengan bawah|telapak kaki|kepala|punggung|Lengan bawah.
Saat passing bawah, kedua tangan …|saling menggenggam|dibuka lebar|dikepal terpisah|disembunyikan|Menggenggam.
=|Saat passing bawah, lutut …|ditekuk|Ditekuk.
=|Passing bawah adalah teknik dalam permainan bola …|voli|Bola voli.
B|Passing bawah dipakai untuk menerima bola rendah.|Menerima bola.
S|Passing bawah dilakukan dengan satu tangan mengepal.|Dua lengan rapat.
Kaki saat passing bawah dibuka selebar …|bahu|lapangan|kepala|jengkal|Selebar bahu.
Bola untuk latihan passing anak sebaiknya bola …|ringan dan lunak|besi|batu|bowling|Bola ringan.
## PJOK|Permainan bentengan
Bentengan dimainkan secara …|berkelompok|sendirian|berpasangan saja|diam|Berkelompok.
Tim menang bentengan jika …|menyentuh benteng lawan|duduk diam|keluar lapangan|membawa bola|Menyentuh benteng lawan.
=|Pemain yang tertangkap disebut …|tawanan|Tawanan.
=|Benteng biasanya berupa tiang atau …|pohon|Pohon.
B|Bentengan melatih kerja sama dan strategi.|Kerja sama.
S|Bentengan dimainkan sendirian.|Dimainkan berkelompok.
Pemain yang menjaga benteng sendiri disebut …|penjaga|penyerang|tawanan|wasit|Penjaga.
Teman yang ditawan dapat dibebaskan dengan …|disentuh teman satu tim|menunggu sampai pulang|bernyanyi|menangis|Disentuh teman.
## PJOK|Lari zig-zag
Lari zig-zag melatih …|kelincahan|kekuatan lengan|kelenturan|ketajaman mata|Kelincahan.
Lari zig-zag dilakukan dengan cara …|berkelok melewati rintangan|lurus tanpa belok|mundur|melompat di tempat|Berkelok.
=|Kemampuan mengubah arah dengan cepat disebut …|kelincahan|Kelincahan.
=|Saat berbelok, langkah kaki dibuat …|pendek;pendek-pendek|Pendek.
B|Saat lari zig-zag, rintangan tidak boleh tersentuh.|Hindari rintangan.
S|Lari zig-zag dilakukan lurus tanpa berbelok.|Harus berkelok.
Latihan untuk melatih daya tahan adalah …|lari santai 5 menit|berdiri satu kaki|menyentuh ujung kaki|push-up sekali|Daya tahan.
Rintangan lari zig-zag dapat dibuat dari …|botol plastik|kaca|pisau|api|Botol aman.
## PJOK|Guling belakang
Guling belakang dimulai dari posisi …|jongkok membelakangi matras|berdiri menghadap matras|tiduran|berlari|Jongkok membelakangi.
Saat guling belakang, dagu …|menempel di dada|menengadah|ke samping|ke belakang|Menempel dada.
=|Saat guling belakang, tangan diletakkan di samping …|telinga|Samping telinga.
=|Guling belakang dilakukan di atas …|matras;kasur|Matras.
B|Tangan menolak matras saat badan berguling ke belakang.|Tolakan tangan.
S|Berat badan ditahan dengan kepala saat guling belakang.|Ditahan tangan.
Posisi akhir guling belakang adalah …|jongkok|berbaring|berdiri dengan tangan|duduk bersila|Jongkok.
Saat guling belakang, badan dibuat …|bulat|lurus kaku|terlentang|tengkurap|Bulat.
## PJOK|Sikap lilin
Sikap lilin bertumpu pada …|bahu|kepala|lutut|perut|Bahu.
Saat sikap lilin, kaki …|lurus ke atas|ditekuk|di lantai|menyilang|Lurus.
=|Saat sikap lilin, tangan menyangga …|pinggang|Pinggang.
=|Sikap lilin melatih kekuatan dan …|keseimbangan|Keseimbangan.
B|Siku menempel di matras saat sikap lilin.|Siku menempel.
S|Sikap lilin dimulai dari posisi berlari.|Dimulai dari berbaring.
Posisi awal sikap lilin adalah …|berbaring telentang|berdiri|jongkok|tengkurap|Berbaring.
Ujung kaki saat sikap lilin menunjuk ke …|langit-langit|lantai|samping|belakang|Ke atas.
## PJOK|Kelenturan tubuh
Kelenturan dilatih dengan gerakan …|peregangan|lari cepat|angkat beban berat|lompat tinggi|Peregangan.
Peregangan sebaiknya dilakukan …|perlahan dan ditahan|cepat dan menyentak|sambil melompat|sambil berlari|Perlahan.
=|Menyentuh ujung kaki saat duduk melatih kelenturan otot paha …|belakang|Paha belakang.
=|Meliukkan badan melatih kelenturan …|pinggang|Pinggang.
B|Tubuh yang lentur terhindar dari cedera.|Mencegah cedera.
S|Peregangan harus dilakukan dengan menyentak keras.|Perlahan.
Mendorong dinding sambil satu kaki di belakang melatih kelenturan …|betis|leher|jari|telinga|Betis.
Kelenturan adalah kemampuan tubuh untuk …|bergerak luas|mengangkat berat|berlari cepat|melompat tinggi|Bergerak luas.
## PJOK|Kekuatan otot
Push-up melatih otot …|lengan dan dada|perut|telinga|leher saja|Lengan dan dada.
Sit-up melatih otot …|perut|lengan|betis|jari|Perut.
=|Squat melatih otot …|paha;kaki|Paha.
=|Latihan kekuatan dilakukan secara …|bertahap|Bertahap.
B|Push-up pemula boleh dengan lutut menempel lantai.|Variasi pemula.
S|Sit-up dilakukan dengan menarik leher memakai tangan kuat-kuat.|Bisa cedera leher.
Back-up melatih otot …|punggung|perut|lengan|leher|Punggung.
Latihan jinjit naik turun melatih otot …|betis|perut|lengan|punggung|Betis.
## PJOK|Meluncur di air
Meluncur dilakukan dengan menolak … kolam memakai kaki.|dinding|dasar|air|tali|Dinding kolam.
Saat meluncur, tangan …|lurus di depan kepala|di samping badan|memeluk lutut|di belakang|Lurus di depan.
=|Saat meluncur, badan lurus seperti anak …|panah|Anak panah.
=|Saat meluncur, wajah masuk ke …|air|Ke air.
B|Meluncur adalah dasar belajar berenang.|Dasar renang.
S|Meluncur sebaiknya dilakukan di kolam dalam tanpa pengawasan.|Kolam dangkal dan diawasi.
Saat meluncur, kedua kaki …|rapat dan lurus|terbuka lebar|ditekuk|bergerak cepat|Rapat.
Napas saat meluncur …|ditahan sebentar|dihembuskan terus|dihirup di air|tidak penting|Ditahan.
## PJOK|Gerakan kaki renang gaya bebas
Gerakan kaki gaya bebas adalah …|naik turun bergantian|membuka seperti katak|diam|melingkar bersamaan|Naik turun.
Gerakan kaki gaya bebas berasal dari …|pangkal paha|lutut saja|jari kaki|tumit|Pangkal paha.
=|Alat bantu latihan gerak kaki renang adalah papan …|pelampung|Papan pelampung.
=|Alat untuk melindungi mata saat berenang adalah kacamata …|renang|Kacamata renang.
B|Gerakan kaki membantu tubuh tetap mengapung.|Mengapung.
S|Lutut harus ditekuk sebanyak mungkin saat gaya bebas.|Lutut sedikit lentur.
Saat latihan kaki di tepi kolam, tangan …|berpegangan pada tepi kolam|di atas kepala|di saku|menutup mata|Berpegangan.
Topi renang berguna untuk melindungi …|rambut|kaki|tangan|perut|Rambut.
## PJOK|Memilih jajanan sehat
Ciri jajanan sehat adalah …|bersih dan tertutup|berwarna sangat mencolok|dihinggapi lalat|berbau tengik|Bersih tertutup.
Sebelum membeli makanan kemasan, kita memeriksa tanggal …|kedaluwarsa|lahir|libur|ulangan|Kedaluwarsa.
=|Jajanan yang dihinggapi lalat mengandung …|kuman|Kuman.
=|Jajanan dari buah dan sayur segar bersifat …|bergizi;sehat|Bergizi.
B|Jajanan yang berbau tengik tidak layak dimakan.|Tidak layak.
S|Jajanan berwarna sangat mencolok pasti sehat.|Bisa mengandung pewarna berbahaya.
Contoh jajanan sehat adalah …|buah potong yang tertutup|gorengan yang dihinggapi lalat|minuman berwarna menyala|permen kedaluwarsa|Buah tertutup.
Tempat membeli jajanan yang baik adalah tempat yang …|bersih|kotor|dekat selokan terbuka|banyak lalat|Bersih.
## PJOK|Pertolongan pertama luka ringan
Langkah pertama menangani luka lecet adalah …|membersihkan luka dengan air mengalir|langsung menutup plester|meniup luka|membiarkan saja|Bersihkan dulu.
Obat untuk mencegah infeksi pada luka adalah …|antiseptik|sirup batuk|vitamin|obat tidur|Antiseptik.
=|Luka kecil ditutup dengan …|plester|Plester.
=|Kotak berisi alat pertolongan pertama disebut kotak …|P3K|P3K.
B|Sebelum menyentuh luka, kita mencuci tangan.|Cuci tangan.
S|Luka besar yang berdarah banyak cukup ditiup saja.|Minta bantuan orang dewasa.
Alat untuk membalut luka adalah …|perban|sendok|penggaris|pensil|Perban.
Kapas dalam kotak P3K berguna untuk …|membersihkan sekitar luka|menulis|bermain|makan|Membersihkan.
"""

SAS += """
## PJOK 1
0|Aba-aba kedua pada lari jarak pendek adalah ....|siap|bersedia|ya|mulai|Siap.
1|Pada lompat jauh tanpa awalan, mendarat menggunakan ....|dua kaki|satu tangan|lutut|pantat|Dua kaki.
2|Saat menggiring bola basket, gerakan tangan adalah ....|mendorong bola|memukul bola keras|menangkap bola|melempar bola tinggi|Mendorong.
3|Menendang bola ke gawang dengan keras memakai ....|punggung kaki|telapak kaki|tumit|lutut|Punggung kaki.
4|Pada passing bawah, bola mengenai ....|lengan bawah|telapak tangan|kepala|dada|Lengan bawah.
5|Pemain yang berusaha menyentuh benteng lawan disebut ....|penyerang|penjaga|tawanan|wasit|Penyerang.
6|Latihan berdiri satu kaki melatih ....|keseimbangan|kecepatan|kekuatan lengan|daya tahan|Keseimbangan.
## PJOK 2
0|Saat guling belakang, telapak tangan menghadap ....|ke atas|ke bawah|ke samping|ke depan|Menghadap ke atas di samping telinga.
1|Pada sikap lilin, bagian tubuh yang menjadi tumpuan adalah ....|bahu|kaki|perut|tangan saja|Bahu.
2|Gerakan memutar leher pelan melatih kelenturan ....|leher|betis|pinggang|perut|Leher.
3|Bergantung di palang melatih kekuatan ....|genggaman tangan|perut|kaki|leher|Genggaman.
4|Saat meluncur di air, tolakan berasal dari ....|dinding kolam|dasar kolam|tangan teman|pelampung|Dinding kolam.
5|Pelampung lengan berguna untuk ....|membantu mengapung|melindungi mata|melindungi rambut|memberi aba-aba|Membantu mengapung.
6|Ciri jajanan yang tidak sehat adalah ....|warnanya sangat mencolok|tertutup rapi|belum kedaluwarsa|bersih|Pewarna mencolok.
7|Kain kasa dalam kotak P3K berguna untuk ....|menutup luka lebih besar|memotong kasa|mencegah infeksi|menulis catatan|Kasa.
"""

TOPICS += """
## PAI
# 1|Al-Qur'an, Akidah, dan Akhlak
@ Surah At-Tin
min: 10
act: Dengarkan bacaan Surah At-Tin dari qari, lalu hafalkan dua ayat setiap hari.
mis: mengira At-Tin menceritakan kisah nabi
exp: Surah At-Tin adalah surah ke-95 dan terdiri atas 8 ayat. At-Tin artinya buah tin. Surah ini menjelaskan bahwa Allah menciptakan manusia dalam bentuk yang sebaik-baiknya. Manusia yang beriman dan beramal saleh akan mendapat pahala yang tidak putus.
ex: Dengarkan rekaman qari pada kartu bacaan. // Kita bersyukur diciptakan dalam bentuk terbaik.
pt: Surah ke-95, terdiri atas 8 ayat ; At-Tin artinya buah tin ; Manusia diciptakan dalam bentuk terbaik
sum: At-Tin mengajarkan kita bersyukur dan beramal saleh.
fig: table Hal | Isi ;; nomor surah | 95 ;; jumlah ayat | 8 ;; arti nama surah | buah tin ;; ayat 4 | manusia diciptakan sebaik-baiknya ;; ayat 6 | orang beriman mendapat pahala ;; golongan | Makkiyah ~ Isi Surah At-Tin.
read: quran 95:1-8
@ Bacaan izhar halqi
min: 10
act: Dengarkan contoh bacaan izhar dari ustaz, lalu tirukan dengan nun yang jelas.
mis: mendengungkan nun mati saat bertemu huruf izhar
exp: Izhar halqi artinya jelas. Bacaan izhar terjadi jika nun mati atau tanwin bertemu salah satu huruf izhar, yaitu hamzah, ha, 'ain, ha besar, gain, dan kha. Huruf-huruf ini keluar dari tenggorokan. Nun mati atau tanwin dibaca jelas tanpa dengung.
ex: مِنْ هَادٍ dibaca min haadin dengan nun jelas. // عَلِيْمٌ حَكِيْمٌ dibaca jelas pada tanwin.
pt: Izhar artinya jelas ; Huruf izhar ada enam ; Dibaca tanpa dengung
sum: Izhar dibaca jelas tanpa dengung.
fig: table Huruf izhar | Nama ;; ء | hamzah ;; ه | ha ;; ع | 'ain ;; ح | ha besar ;; غ | gain ;; خ | kha ~ Enam huruf izhar halqi.
@ Sifat mustahil Allah
min: 10
act: Buat kartu pasangan sifat wajib dan sifat mustahil Allah, lalu cocokkan bersama keluarga.
mis: mengira sifat mustahil adalah sifat yang dimiliki Allah
exp: Sifat mustahil Allah adalah sifat yang tidak mungkin dimiliki Allah. Sifat mustahil adalah lawan dari sifat wajib. Contohnya Allah wujud atau ada, mustahil 'adam atau tidak ada. Allah qidam atau terdahulu, mustahil hudus atau baru. Allah baqa atau kekal, mustahil fana atau binasa.
ex: Allah Maha Esa, mustahil berbilang. // Allah berdiri sendiri, mustahil membutuhkan yang lain.
pt: Sifat mustahil tidak mungkin dimiliki Allah ; Lawan dari sifat wajib ; Contohnya 'adam lawan wujud
sum: Allah Mahasempurna dan tidak mungkin memiliki kekurangan.
fig: table Sifat wajib | Sifat mustahil ;; wujud atau ada | 'adam atau tidak ada ;; qidam atau terdahulu | hudus atau baru ;; baqa atau kekal | fana atau binasa ;; berbeda dengan makhluk | sama dengan makhluk ;; berdiri sendiri | membutuhkan yang lain ;; wahdaniyah atau esa | berbilang ~ Sifat wajib dan sifat mustahil Allah.
@ Asmaul Husna Al-Khaliq, Ar-Razzaq, dan Al-Ghaffar
min: 10
act: Sebutkan tiga makhluk ciptaan Allah di sekitarmu dan rezeki yang kamu terima hari ini.
mis: tertukar arti Al-Khaliq dan Ar-Razzaq
exp: Al-Khaliq artinya Maha Pencipta, Allah menciptakan seluruh alam. Ar-Razzaq artinya Maha Pemberi Rezeki, Allah memberi rezeki kepada semua makhluk. Al-Ghaffar artinya Maha Pengampun, Allah mengampuni hamba yang bertobat. Kita meneladaninya dengan berkarya, berbagi, dan memaafkan.
ex: Meneladani Ar-Razzaq dengan berbagi makanan. // Meneladani Al-Ghaffar dengan memaafkan teman.
pt: Al-Khaliq Maha Pencipta ; Ar-Razzaq Maha Pemberi Rezeki ; Al-Ghaffar Maha Pengampun
sum: Meneladani Asmaul Husna membuat kita berakhlak baik.
fig: table Asmaul Husna | Arti ;; Al-Khaliq | Maha Pencipta ;; Ar-Razzaq | Maha Pemberi Rezeki ;; Al-Ghaffar | Maha Pengampun ;; Al-Wahhab | Maha Pemberi Karunia ;; Al-Fattah | Maha Pembuka Rahmat ;; Al-Basir | Maha Melihat ~ Asmaul Husna dan artinya.
@ Jujur dan amanah
min: 10
act: Terima satu titipan dari orang tua, misalnya uang belanja, lalu kembalikan sisanya dengan jujur.
mis: menganggap titipan boleh dipakai tanpa izin
exp: Jujur artinya berkata dan berbuat sesuai kenyataan. Amanah artinya dapat dipercaya menjaga titipan atau tugas. Nabi Muhammad dijuluki Al-Amin karena sangat jujur dan dapat dipercaya. Orang yang jujur dan amanah disukai Allah dan sesama manusia.
ex: Mengembalikan uang kembalian belanja kepada ibu. // Menjaga barang yang dititipkan teman.
pt: Jujur sesuai kenyataan ; Amanah menjaga titipan ; Nabi Muhammad bergelar Al-Amin
sum: Jujur dan amanah membuat kita dipercaya.
fig: table Keadaan | Sikap jujur dan amanah ;; dititipi buku | menjaganya dengan baik ;; diberi tugas piket | mengerjakannya ;; kembalian belanja | dikembalikan ;; berbuat salah | mengakuinya ;; ulangan | mengerjakan sendiri ;; berjanji | menepatinya ~ Contoh sikap jujur dan amanah.
@ Adab bertamu
min: 10
act: Praktikkan adab bertamu saat berkunjung ke rumah nenek atau tetangga.
mis: masuk rumah orang tanpa mengucapkan salam
exp: Bertamu adalah berkunjung ke rumah orang lain. Adab bertamu antara lain mengucapkan salam dan mengetuk pintu paling banyak tiga kali, masuk setelah dipersilakan, duduk dengan sopan, berbicara dengan santun, dan tidak terlalu lama. Pulang dengan berpamitan.
ex: Assalamualaikum, Bu. Boleh saya masuk? // Berpamitan sebelum pulang.
pt: Ucapkan salam dan ketuk pintu ; Masuk setelah dipersilakan ; Sopan dan tidak terlalu lama
sum: Adab bertamu membuat tuan rumah senang.
fig: table Waktu | Adab bertamu ;; sampai di depan rumah | mengucapkan salam ;; mengetuk pintu | paling banyak tiga kali ;; masuk | setelah dipersilakan ;; duduk | dengan sopan ;; disuguhi makanan | berterima kasih ;; pulang | berpamitan ~ Adab bertamu.
# 2|Ibadah, Kisah, dan Kebersihan
@ Surah Al-Insyirah
min: 10
act: Dengarkan bacaan Surah Al-Insyirah, lalu tulis satu kesulitan yang pernah kamu atasi.
mis: mengira Al-Insyirah berisi larangan
exp: Surah Al-Insyirah adalah surah ke-94 dan terdiri atas 8 ayat. Al-Insyirah artinya kelapangan. Surah ini mengajarkan bahwa sesudah kesulitan pasti ada kemudahan. Kita diajak untuk terus berusaha dan berharap hanya kepada Allah.
ex: Dengarkan rekaman qari pada kartu bacaan. // Ayat 5 dan 6: bersama kesulitan ada kemudahan.
pt: Surah ke-94, terdiri atas 8 ayat ; Al-Insyirah artinya kelapangan ; Bersama kesulitan ada kemudahan
sum: Al-Insyirah mengajarkan kita tidak mudah putus asa.
fig: table Hal | Isi ;; nomor surah | 94 ;; jumlah ayat | 8 ;; arti nama surah | kelapangan ;; ayat 5 dan 6 | bersama kesulitan ada kemudahan ;; ayat 7 | terus bekerja keras ;; ayat 8 | berharap hanya kepada Allah ~ Isi Surah Al-Insyirah.
read: quran 94:1-8
@ Zakat fitrah
min: 10
act: Tanyakan kepada orang tua kapan dan kepada siapa keluarga membayar zakat fitrah.
mis: mengira zakat fitrah boleh dibayar setelah salat Idulfitri
exp: Zakat fitrah adalah zakat yang wajib dikeluarkan setiap muslim pada bulan Ramadan sampai sebelum salat Idulfitri. Besarnya sekitar 2,5 kilogram makanan pokok, misalnya beras. Zakat fitrah membersihkan diri dan membantu fakir miskin supaya ikut berbahagia di hari raya.
ex: Ayah membayar zakat fitrah untuk seluruh keluarga. // Zakat diberikan kepada fakir miskin.
pt: Wajib bagi setiap muslim ; Sekitar 2,5 kg makanan pokok ; Dibayar sebelum salat Idulfitri
sum: Zakat fitrah menyucikan diri dan membantu sesama.
fig: table Hal | Keterangan ;; hukum | wajib bagi setiap muslim ;; waktu | Ramadan sampai sebelum salat Id ;; besarnya | sekitar 2,5 kg makanan pokok ;; contoh bahan | beras ;; penerima | fakir miskin ;; tujuan | menyucikan diri ~ Ketentuan zakat fitrah.
@ Salat berjamaah
min: 10
act: Ajak keluarga salat berjamaah di rumah dengan ayah sebagai imam.
mis: mendahului gerakan imam
exp: Salat berjamaah adalah salat yang dikerjakan bersama-sama. Orang yang memimpin disebut imam dan yang mengikuti disebut makmum. Makmum mengikuti gerakan imam dan tidak boleh mendahuluinya. Saf atau barisan dibuat lurus dan rapat. Pahala salat berjamaah lebih besar daripada salat sendiri.
ex: Makmum mengucapkan amin setelah imam membaca Al-Fatihah. // Saf anak di belakang saf orang dewasa laki-laki.
pt: Imam memimpin, makmum mengikuti ; Tidak mendahului imam ; Saf lurus dan rapat
sum: Salat berjamaah mempererat persaudaraan.
fig: table Istilah | Arti ;; imam | pemimpin salat ;; makmum | pengikut imam ;; saf | barisan salat ;; berjamaah | salat bersama ;; munfarid | salat sendirian ;; masbuk | makmum yang tertinggal ~ Istilah dalam salat berjamaah.
@ Kisah Nabi Musa
min: 10
act: Ceritakan kembali kisah Nabi Musa membelah laut kepada adik atau teman.
mis: mengira Nabi Musa menerima kitab Injil
exp: Nabi Musa diutus Allah untuk mengajak Firaun yang zalim beriman kepada Allah. Allah memberi mukjizat kepada Nabi Musa, di antaranya tongkat yang bisa menjadi ular dan dapat membelah laut. Nabi Musa menerima kitab Taurat dan dibantu oleh saudaranya, Nabi Harun.
ex: Tongkat Nabi Musa membelah Laut Merah. // Firaun tenggelam karena sombong.
pt: Nabi Musa melawan Firaun yang zalim ; Mukjizat tongkat ; Menerima kitab Taurat
sum: Kisah Nabi Musa mengajarkan keberanian membela kebenaran.
fig: table Tokoh atau hal | Keterangan ;; Nabi Musa | rasul yang menerima Taurat ;; Firaun | raja Mesir yang zalim ;; Nabi Harun | saudara Nabi Musa ;; tongkat | menjadi ular dan membelah laut ;; Laut Merah | terbelah atas izin Allah ;; pelajaran | berani membela kebenaran ~ Kisah Nabi Musa.
@ Masa kecil Nabi Muhammad
min: 10
act: Buat garis waktu masa kecil Nabi Muhammad dengan gambar sederhana.
mis: mengira Nabi Muhammad diasuh ayahnya sejak kecil
exp: Nabi Muhammad lahir di Makkah pada Tahun Gajah. Ayahnya, Abdullah, wafat sebelum beliau lahir. Ibunya bernama Aminah. Beliau disusui oleh Halimah As-Sa'diyah. Setelah ibunya wafat, beliau diasuh kakeknya, Abdul Muthalib, lalu pamannya, Abu Thalib. Sejak kecil beliau jujur dan rajin bekerja menggembala kambing.
ex: Nabi Muhammad menjadi yatim sejak dalam kandungan. // Beliau menggembala kambing saat kecil.
pt: Lahir di Makkah pada Tahun Gajah ; Diasuh kakek lalu paman ; Sejak kecil jujur dan rajin
sum: Masa kecil Nabi Muhammad mengajarkan kesabaran dan kerja keras.
fig: table Tokoh | Hubungan dengan Nabi ;; Abdullah | ayah ;; Aminah | ibu ;; Halimah As-Sa'diyah | ibu susu ;; Abdul Muthalib | kakek ;; Abu Thalib | paman ;; Ummu Aiman | pengasuh ~ Orang-orang di masa kecil Nabi Muhammad.
@ Bersuci dari najis
min: 10
act: Bersama orang tua, praktikkan cara membersihkan lantai yang terkena kotoran hewan.
mis: mengira semua najis dibersihkan dengan cara yang sama
exp: Najis adalah kotoran yang harus dibersihkan sebelum beribadah. Najis ringan atau mukhaffafah dibersihkan dengan memercikkan air. Najis sedang atau mutawassitah dicuci sampai hilang warna, bau, dan rasanya. Najis berat atau mughallazah dicuci tujuh kali dan salah satunya dengan air bercampur tanah.
ex: Air kencing bayi laki-laki yang hanya minum ASI cukup dipercik air. // Darah dicuci sampai bersih.
pt: Najis ringan dipercik air ; Najis sedang dicuci sampai hilang ; Najis berat dicuci tujuh kali
sum: Bersuci dari najis membuat ibadah kita sah.
fig: table Jenis najis | Cara membersihkan ;; mukhaffafah | dipercik air ;; mutawassitah | dicuci sampai bersih ;; mughallazah | dicuci tujuh kali dengan tanah ;; darah | dicuci dengan air mengalir ;; kotoran hewan di lantai | dibuang lalu dipel ;; air liur anjing | dicuci tujuh kali salah satunya dengan tanah ~ Jenis najis dan cara membersihkannya.
"""

BANK += """
## PAI|Surah At-Tin
Surah At-Tin terdiri atas … ayat.|8|5|6|11|At-Tin 8 ayat.
At-Tin adalah surah ke- …|95|94|96|97|Surah ke-95.
=|At-Tin artinya buah …|tin|Buah tin.
=|Surah At-Tin termasuk golongan surah …|Makkiyah|Makkiyah.
B|Surah At-Tin menjelaskan manusia diciptakan dalam bentuk terbaik.|Ayat 4.
S|Surah At-Tin terdiri atas 3 ayat.|8 ayat.
Orang yang mendapat pahala tidak putus menurut At-Tin adalah orang yang …|beriman dan beramal saleh|malas beribadah|sombong|suka berbohong|Ayat 6.
Surah sesudah At-Tin dalam Al-Qur'an adalah …|Al-'Alaq|Al-Insyirah|Ad-Duha|Al-Qadr|95 lalu 96.
## PAI|Bacaan izhar halqi
Izhar artinya …|jelas|samar|dengung|memantul|Izhar jelas.
Banyak huruf izhar halqi adalah …|6|4|2|15|Enam huruf.
=|Izhar terjadi saat nun mati atau tanwin bertemu huruf …|izhar|Huruf izhar.
=|Huruf izhar keluar dari …|tenggorokan|Tenggorokan.
B|Huruf ع termasuk huruf izhar.|'Ain huruf izhar.
S|Bacaan izhar dibaca dengan dengung.|Dibaca jelas.
Huruf berikut yang termasuk huruf izhar adalah …|خ|ب|م|ن|Kha huruf izhar.
Cara membaca nun mati bertemu huruf ه adalah …|jelas tanpa dengung|dengung panjang|dilebur|dipantulkan|Izhar.
## PAI|Sifat mustahil Allah
Sifat mustahil Allah adalah sifat yang … dimiliki Allah.|tidak mungkin|pasti|kadang-kadang|boleh|Tidak mungkin.
Lawan dari sifat wujud adalah …|'adam|fana|hudus|ta'addud|'Adam tidak ada.
=|Lawan dari sifat baqa adalah …|fana|Fana binasa.
=|Lawan dari sifat qidam adalah …|hudus|Hudus baru.
B|Allah mustahil sama dengan makhluk.|Berbeda dengan makhluk.
S|Allah mungkin membutuhkan bantuan makhluk.|Allah berdiri sendiri.
Sifat mustahil ta'addud artinya …|berbilang|binasa|baru|tidak ada|Berbilang.
Sifat mustahil adalah lawan dari sifat …|wajib|jaiz|terpuji|tercela|Lawan sifat wajib.
## PAI|Asmaul Husna Al-Khaliq, Ar-Razzaq, dan Al-Ghaffar
Al-Khaliq artinya …|Maha Pencipta|Maha Pengampun|Maha Pemberi Rezeki|Maha Melihat|Al-Khaliq.
Ar-Razzaq artinya …|Maha Pemberi Rezeki|Maha Pencipta|Maha Pengampun|Maha Suci|Ar-Razzaq.
=|Al-Ghaffar artinya Maha …|Pengampun|Maha Pengampun.
=|Al-Basir artinya Maha …|Melihat|Maha Melihat.
B|Meneladani Ar-Razzaq dapat dilakukan dengan berbagi.|Berbagi.
S|Al-Ghaffar artinya Maha Pencipta.|Maha Pengampun.
Meneladani Al-Ghaffar dilakukan dengan …|memaafkan teman|mendendam|mengejek|marah|Memaafkan.
Allah yang menciptakan langit dan bumi menunjukkan sifat …|Al-Khaliq|Al-Ghaffar|Ar-Razzaq|Al-Basir|Pencipta.
## PAI|Jujur dan amanah
Amanah artinya …|dapat dipercaya|suka berbohong|pelit|pemalas|Dapat dipercaya.
Gelar Nabi Muhammad karena sangat jujur adalah …|Al-Amin|Al-Khaliq|Al-Ghaffar|Al-Basir|Al-Amin.
=|Berkata sesuai kenyataan disebut …|jujur|Jujur.
=|Janji yang diucapkan harus …|ditepati|Ditepati.
B|Mengembalikan uang kembalian kepada ibu adalah sikap jujur.|Jujur.
S|Barang titipan boleh dipakai tanpa izin.|Harus izin.
Contoh sikap amanah adalah …|menjaga barang titipan teman|menghilangkan barang titipan|meminjam tanpa mengembalikan|mengingkari janji|Menjaga titipan.
Orang yang jujur dan amanah akan …|dipercaya orang lain|dijauhi teman|dimarahi Allah|tidak punya teman|Dipercaya.
## PAI|Adab bertamu
Saat bertamu, pintu diketuk paling banyak …|tiga kali|sepuluh kali|terus-menerus|satu kali saja keras|Tiga kali.
Tamu masuk ke rumah setelah …|dipersilakan|ketuk sekali|pintu terbuka sendiri|tuan rumah tidur|Dipersilakan.
=|Sebelum masuk rumah orang, kita mengucapkan …|salam;assalamualaikum|Salam.
=|Sebelum pulang dari bertamu, kita …|berpamitan|Berpamitan.
B|Tamu sebaiknya tidak bertamu terlalu lama.|Tidak terlalu lama.
S|Tamu boleh membuka lemari tuan rumah tanpa izin.|Tidak sopan.
Saat disuguhi makanan oleh tuan rumah, kita …|berterima kasih|menolak dengan kasar|mengambil semuanya|mengeluh|Berterima kasih.
Waktu bertamu yang kurang tepat adalah …|saat tuan rumah beristirahat malam|siang hari|sore hari|pagi hari|Mengganggu istirahat.
## PAI|Surah Al-Insyirah
Surah Al-Insyirah terdiri atas … ayat.|8|6|5|7|Al-Insyirah 8 ayat.
Al-Insyirah adalah surah ke- …|94|95|93|92|Surah ke-94.
=|Al-Insyirah artinya …|kelapangan|Kelapangan.
=|Menurut Al-Insyirah, bersama kesulitan ada …|kemudahan|Kemudahan.
B|Surah Al-Insyirah mengajarkan kita tidak mudah putus asa.|Optimis.
S|Surah Al-Insyirah menyuruh kita berhenti berusaha.|Terus berusaha.
Ayat 8 Surah Al-Insyirah mengajarkan kita berharap hanya kepada …|Allah|teman|harta|diri sendiri|Allah.
Surah sebelum Al-Insyirah dalam Al-Qur'an adalah …|Ad-Duha|At-Tin|Al-'Alaq|Al-Qadr|93 lalu 94.
## PAI|Zakat fitrah
Zakat fitrah wajib bagi …|setiap muslim|orang kaya saja|orang dewasa saja|orang tua saja|Setiap muslim.
Batas akhir membayar zakat fitrah adalah …|sebelum salat Idulfitri|sesudah salat Idulfitri|akhir tahun|bulan Syawal|Sebelum salat Id.
=|Besar zakat fitrah sekitar 2,5 kg makanan …|pokok|Makanan pokok.
=|Zakat fitrah diberikan kepada fakir …|miskin|Fakir miskin.
B|Zakat fitrah dapat berupa beras.|Beras.
S|Zakat fitrah dibayar pada bulan Zulhijah.|Bulan Ramadan.
Tujuan zakat fitrah adalah …|menyucikan diri dan membantu sesama|menambah kekayaan|pamer harta|menghabiskan beras|Menyucikan diri.
Zakat fitrah dikeluarkan pada bulan …|Ramadan|Muharam|Rajab|Safar|Ramadan.
## PAI|Salat berjamaah
Pemimpin salat berjamaah disebut …|imam|makmum|saf|muazin|Imam.
Orang yang mengikuti imam disebut …|makmum|imam|khatib|bilal|Makmum.
=|Barisan dalam salat berjamaah disebut …|saf|Saf.
=|Makmum tidak boleh … gerakan imam.|mendahului|Tidak mendahului.
B|Saf salat dibuat lurus dan rapat.|Lurus dan rapat.
S|Salat sendirian disebut berjamaah.|Salat sendiri disebut munfarid.
Makmum yang tertinggal rakaat disebut …|masbuk|munfarid|imam|muazin|Masbuk.
Setelah imam selesai membaca Al-Fatihah, makmum mengucapkan …|amin|alhamdulillah|subhanallah|allahu akbar|Amin.
## PAI|Kisah Nabi Musa
Kitab yang diterima Nabi Musa adalah …|Taurat|Injil|Zabur|Al-Qur'an|Taurat.
Raja zalim yang dihadapi Nabi Musa adalah …|Firaun|Namrud|Abrahah|Jalut|Firaun.
=|Saudara yang membantu Nabi Musa adalah Nabi …|Harun|Nabi Harun.
=|Tongkat Nabi Musa dapat berubah menjadi …|ular|Ular.
B|Tongkat Nabi Musa dapat membelah laut atas izin Allah.|Mukjizat.
S|Firaun beriman kepada Nabi Musa sejak awal.|Firaun ingkar.
Pelajaran dari kisah Nabi Musa adalah …|berani membela kebenaran|takut kepada orang zalim|sombong|berbohong|Berani.
Laut yang terbelah dalam kisah Nabi Musa adalah Laut …|Merah|Mati|Jawa|Hitam|Laut Merah.
## PAI|Masa kecil Nabi Muhammad
Nabi Muhammad lahir di kota …|Makkah|Madinah|Thaif|Yerusalem|Makkah.
Ibu Nabi Muhammad bernama …|Aminah|Halimah|Khadijah|Fatimah|Aminah.
=|Ayah Nabi Muhammad bernama …|Abdullah|Abdullah.
=|Ibu susu Nabi Muhammad adalah Halimah As- …|Sa'diyah;Sadiyah|Halimah As-Sa'diyah.
B|Nabi Muhammad lahir pada Tahun Gajah.|Tahun Gajah.
S|Ayah Nabi Muhammad mengasuhnya sampai dewasa.|Ayahnya wafat sebelum beliau lahir.
Setelah kakeknya wafat, Nabi Muhammad diasuh oleh pamannya bernama …|Abu Thalib|Abu Jahal|Abu Lahab|Hamzah|Abu Thalib.
Pekerjaan Nabi Muhammad saat kecil adalah …|menggembala kambing|berdagang emas|menjadi raja|menjadi nelayan|Menggembala.
## PAI|Bersuci dari najis
Najis ringan disebut najis …|mukhaffafah|mutawassitah|mughallazah|ma'fu|Mukhaffafah.
Najis berat disebut najis …|mughallazah|mukhaffafah|mutawassitah|ringan|Mughallazah.
=|Najis ringan cukup dibersihkan dengan … air.|dipercik;memercikkan|Dipercik air.
=|Najis berat dicuci sebanyak … kali.|tujuh;7|Tujuh kali.
B|Darah termasuk najis sedang.|Mutawassitah.
S|Najis berat cukup dipercik air sekali.|Dicuci tujuh kali dengan tanah.
Contoh najis berat adalah …|air liur anjing|air kencing bayi laki-laki ASI|darah|debu|Mughallazah.
Najis sedang dicuci sampai hilang …|warna, bau, dan rasanya|sebagian saja|warnanya saja|tidak perlu dicuci|Hilang semuanya.
"""

SAS += """
## PAI 1
0|Ayat keempat Surah At-Tin menjelaskan bahwa manusia ....|diciptakan dalam bentuk terbaik|diciptakan dari api|tidak perlu beribadah|akan hidup selamanya|Ayat 4.
1|Huruf izhar yang bernama gain adalah ....|غ|ع|ه|ء|Gain.
2|Lawan dari sifat wahdaniyah adalah ....|ta'addud|'adam|fana|hudus|Ta'addud berbilang.
3|Al-Wahhab artinya ....|Maha Pemberi Karunia|Maha Pencipta|Maha Melihat|Maha Pengampun|Al-Wahhab.
4|Contoh sikap amanah saat diberi tugas piket adalah ....|mengerjakannya dengan baik|meninggalkannya|menyuruh teman|berpura-pura sakit|Amanah.
5|Saat sampai di depan rumah orang, tamu terlebih dahulu ....|mengucapkan salam|langsung masuk|berteriak|membuka jendela|Salam.
## PAI 2
0|Ayat ketujuh Surah Al-Insyirah mengajak kita ....|terus bekerja keras|bermalas-malasan|putus asa|tidur|Ayat 7.
1|Penerima zakat fitrah yang utama adalah ....|fakir miskin|orang kaya|pejabat|pedagang besar|Fakir miskin.
2|Saf anak-anak dalam salat berjamaah berada di belakang saf ....|laki-laki dewasa|perempuan|imam|tidak ada|Urutan saf.
3|Mukjizat Nabi Musa adalah ....|tongkat yang dapat membelah laut|tidak terbakar api|membuat kapal|menyembuhkan orang buta|Tongkat.
4|Kakek yang mengasuh Nabi Muhammad bernama ....|Abdul Muthalib|Abu Thalib|Abdullah|Hamzah|Abdul Muthalib.
5|Air kencing bayi laki-laki yang hanya minum ASI termasuk najis ....|mukhaffafah|mughallazah|mutawassitah|berat|Najis ringan.
"""

TOPICS += """
## SUN
# 1|Kecap jeung Budaya Sunda
@ Kecap pagawéan
min: 10
act: Lakukeun hiji pagawéan, tuluy babaturan atawa kulawarga nebak kecap pagawéanana dina basa Sunda.
mis: tertukar antara maca dan nulis
exp: Kecap pagawéan adalah kata kerja, yaitu kata yang menunjukkan kegiatan. Dalam bahasa Sunda, makan disebut dahar, minum disebut nginum, membaca disebut maca, menulis disebut nulis, berlari disebut lumpat, dan duduk disebut diuk.
ex: Adi keur maca buku. // Barudak lumpat di buruan.
pt: Kecap pagawéan artinya kata kerja ; Maca artinya membaca ; Lumpat artinya berlari
sum: Mengenal kata kerja dalam bahasa Sunda.
fig: table Basa Indonésia | Basa Sunda ;; makan | dahar ;; minum | nginum ;; membaca | maca ;; menulis | nulis ;; berlari | lumpat ;; duduk | diuk ~ Kecap pagawéan.
@ Kecap sipat
min: 10
act: Sebutkeun sipat lima barang di imah, contona méja gedé atawa gelas leutik.
mis: menyebut gedé untuk benda kecil
exp: Kecap sipat adalah kata sifat, yaitu kata yang menjelaskan keadaan benda atau orang. Dalam bahasa Sunda, besar disebut gedé, kecil disebut leutik, cantik disebut geulis, tampan disebut kasép, baik hati disebut bageur, dan pandai disebut pinter.
ex: Gajah mah gedé. // Si Ujang bageur pisan.
pt: Kecap sipat artinya kata sifat ; Gedé artinya besar ; Bageur artinya baik hati
sum: Mengenal kata sifat dalam bahasa Sunda.
fig: table Basa Indonésia | Basa Sunda ;; besar | gedé ;; kecil | leutik ;; cantik | geulis ;; tampan | kasép ;; baik hati | bageur ;; pandai | pinter ~ Kecap sipat.
@ Parabot dapur
min: 10
act: Asupkeun ka dapur jeung indung, tuluy sebutkeun ngaran parabot dapur dina basa Sunda.
mis: menyebut coét untuk alat menanak nasi
exp: Parabot dapur adalah alat-alat dapur. Dalam bahasa Sunda, dandang disebut sééng, kukusan bambu disebut aseupan, cobek disebut coét, ulekan disebut mutu, wajan disebut katél, dan kipas bambu disebut hihid. Parabot dapur dipakai untuk memasak.
ex: Ema ngulek sambel dina coét. // Sangu diakeul maké hihid.
pt: Sééng artinya dandang ; Coét artinya cobek ; Hihid artinya kipas bambu
sum: Mengenal nama alat dapur tradisional Sunda.
fig: table Basa Indonésia | Basa Sunda ;; dandang | sééng ;; kukusan bambu | aseupan ;; cobek | coét ;; ulekan | mutu ;; wajan | katél ;; kipas bambu | hihid ~ Parabot dapur.
@ Paparikan
min: 10
act: Dangukeun paparikan ti kolot, tuluy cobaan nyieun hiji paparikan babarengan.
mis: mengira cangkang berisi maksud utama paparikan
exp: Paparikan adalah jenis sisindiran atau pantun Sunda. Paparikan terdiri atas empat baris. Dua baris pertama disebut cangkang atau sampiran, dan dua baris terakhir disebut eusi atau isi. Bunyi cangkang dan eusi mirip sehingga enak didengar.
ex: Hayam jago kongkorongok, // Cangkang. Barudak gancang hudang, ulah ngedul, isukan sakola, // Eusi berisi nasihat.
pt: Paparikan bagian dari sisindiran ; Cangkang dua baris pertama ; Eusi dua baris terakhir
sum: Paparikan berisi pesan pada bagian eusi.
fig: table Istilah | Hartina ;; sisindiran | pantun Sunda ;; paparikan | sisindiran nu sorana mirip ;; cangkang | dua padalisan mimiti ;; eusi | dua padalisan ahir ;; padalisan | baris ;; rarakitan | sisindiran nu kecap awalna sarua ~ Istilah dalam sisindiran.
@ Seni Sunda
min: 10
act: Tonton video angklung atawa wayang golék babarengan jeung kulawarga.
mis: mengira angklung dimainkan dengan dipukul
exp: Masyarakat Sunda memiliki banyak kesenian. Angklung adalah alat musik dari bambu yang digoyangkan. Kacapi adalah alat musik petik. Wayang golék adalah boneka kayu untuk bercerita. Jaipongan adalah tarian khas Sunda. Kesenian ini harus kita lestarikan.
ex: Angklung dimainkan bari dieundeukkeun. // Wayang golék dimainkan ku dalang.
pt: Angklung digoyangkan ; Wayang golék boneka kayu ; Jaipongan tarian Sunda
sum: Seni Sunda adalah warisan budaya yang perlu dilestarikan.
fig: table Kasenian | Jenisna ;; angklung | alat musik awi digoyang ;; kacapi | alat musik dipetik ;; suling | alat musik ditiup ;; wayang golék | boneka kai ;; jaipongan | tarian ;; calung | alat musik awi ditakol ~ Kesenian Sunda.
@ Ngaran tutuwuhan
min: 10
act: Leumpang di kebon atawa sawah, tuluy sebutkeun ngaran tutuwuhan dina basa Sunda.
mis: menyebut awi untuk pohon kelapa
exp: Tutuwuhan artinya tumbuh-tumbuhan. Dalam bahasa Sunda, padi disebut paré, bambu disebut awi, rumput disebut jukut, pohon disebut tangkal, bunga disebut kembang, dan jagung disebut jagong. Tutuwuhan memberi kita makanan dan udara segar.
ex: Pak Tani melak paré di sawah. // Kembang mawar warnana beureum.
pt: Paré artinya padi ; Awi artinya bambu ; Kembang artinya bunga
sum: Mengenal nama tumbuhan dalam bahasa Sunda.
fig: table Basa Indonésia | Basa Sunda ;; padi | paré ;; bambu | awi ;; rumput | jukut ;; pohon | tangkal ;; bunga | kembang ;; jagung | jagong ~ Ngaran tutuwuhan.
# 2|Kahirupan Sapopoé
@ Di pasar
min: 10
act: Ilu balanja ka pasar, tuluy cobaan nawar harga maké basa Sunda nu sopan.
mis: menyebut meuli untuk menjual
exp: Pasar adalah tempat jual beli. Dalam bahasa Sunda, membeli disebut meuli, menjual disebut ngajual, uang disebut duit, menawar disebut nawar, dan pedagang disebut padagang. Saat berbelanja kita memakai bahasa yang sopan.
ex: Sabaraha hargana, Bu? // Abdi badé meuli cau sasisir.
pt: Meuli artinya membeli ; Ngajual artinya menjual ; Duit artinya uang
sum: Mengenal kata-kata jual beli dalam bahasa Sunda.
fig: table Basa Indonésia | Basa Sunda ;; membeli | meuli ;; menjual | ngajual ;; uang | duit ;; menawar | nawar ;; pedagang | padagang ;; berapa harganya | sabaraha hargana ~ Kecap di pasar.
@ Kandaraan
min: 10
act: Itung kandaraan nu ngaliwat di hareupeun imah salila lima menit, tuluy sebutkeun ngaranna.
mis: menyebut parahu untuk kendaraan darat
exp: Kandaraan artinya kendaraan. Dalam bahasa Sunda, sepeda disebut sapédah, perahu disebut parahu, kereta api disebut karéta api, pesawat disebut kapal udara, dan delman disebut sado. Kendaraan dipakai untuk bepergian dan mengangkut barang.
ex: Abdi indit ka sakola tumpak sapédah. // Pamayang ngala lauk maké parahu.
pt: Sapédah artinya sepeda ; Parahu artinya perahu ; Sado artinya delman
sum: Mengenal nama kendaraan dalam bahasa Sunda.
fig: table Basa Indonésia | Basa Sunda ;; sepeda | sapédah ;; perahu | parahu ;; kereta api | karéta api ;; pesawat | kapal udara ;; delman | sado ;; naik kendaraan | tumpak ~ Ngaran kandaraan.
@ Kabersihan lingkungan
min: 10
act: Ilu kerja bakti di lingkungan imah, tuluy caritakeun pangalamanana dina basa Sunda.
mis: membuang sampah ke selokan
exp: Lingkungan yang bersih membuat hidup sehat. Dalam bahasa Sunda, sampah disebut runtah, selokan disebut solokan, membuang disebut miceun, dan kerja bakti disebut gotong royong. Kita tidak boleh miceun runtah sambarangan atau membuang sampah sembarangan.
ex: Tong miceun runtah ka solokan. // Urang gotong royong ngabersihan lembur.
pt: Runtah artinya sampah ; Miceun artinya membuang ; Jaga kabersihan babarengan
sum: Menjaga kebersihan lingkungan adalah tanggung jawab bersama.
fig: table Basa Indonésia | Basa Sunda ;; sampah | runtah ;; selokan | solokan ;; membuang | miceun ;; tempat sampah | tong runtah ;; bersih | beresih ;; sembarangan | sambarangan ~ Kecap ngeunaan kabersihan.
@ Kecap pananya
min: 10
act: Tanyakeun lima hal ka kolot maké kecap pananya basa Sunda.
mis: menyebut iraha untuk menanyakan tempat
exp: Kecap pananya adalah kata tanya. Dalam bahasa Sunda, siapa disebut saha, apa disebut naon, kapan disebut iraha, mengapa disebut naha, bagaimana disebut kumaha, dan berapa disebut sabaraha. Kata tanya dipakai untuk mencari keterangan.
ex: Saha ngaran manéh? // Iraha urang indit ka Bandung?
pt: Saha artinya siapa ; Iraha artinya kapan ; Kumaha artinya bagaimana
sum: Mengenal kata tanya dalam bahasa Sunda.
fig: table Basa Indonésia | Basa Sunda ;; siapa | saha ;; apa | naon ;; kapan | iraha ;; mengapa | naha ;; bagaimana | kumaha ;; berapa | sabaraha ~ Kecap pananya.
@ Nyaritakeun pangalaman
min: 10
act: Caritakeun pangalaman liburan ka kulawarga maké basa Sunda.
mis: bercerita tanpa urutan waktu yang jelas
exp: Nyaritakeun pangalaman artinya menceritakan pengalaman. Cerita yang baik menyebutkan kapan terjadi, di mana, dengan siapa, apa kejadiannya, dan bagaimana perasaan kita. Gunakan urutan waktu supaya pendengar mudah mengerti.
ex: Kamari abdi ka kebon binatang jeung bapa. // Abdi bungah pisan ningali gajah.
pt: Sebutkan waktu dan tempat ; Ceritakan kejadian berurutan ; Ungkapkan perasaan
sum: Pengalaman diceritakan dengan urutan yang jelas.
fig: table Bagian carita | Conto ;; iraha | kamari ;; di mana | di kebon binatang ;; jeung saha | jeung bapa ;; naon kajadianana | ningali gajah ;; kumaha rasana | bungah pisan ;; pangajaran | nyaah ka sato ~ Bagian dalam nyaritakeun pangalaman.
@ Imah adat Sunda
min: 10
act: Néangan gambar imah adat Sunda, tuluy bandingkeun wangun hateupna.
mis: mengira semua rumah adat Sunda berbentuk sama
exp: Rumah adat Sunda dibedakan dari bentuk atapnya atau hateup. Ada Julang Ngapak yang seperti burung mengepakkan sayap, Tagog Anjing yang seperti anjing duduk, Badak Heuay yang seperti badak menguap, dan Parahu Kumureb yang seperti perahu terbalik. Rumah adat Sunda biasanya berupa rumah panggung.
ex: Julang Ngapak hateupna siga manuk keur ngapak. // Imah panggung ngajaga imah tina caah.
pt: Dibedakan dari bentuk atap ; Biasanya rumah panggung ; Contohnya Julang Ngapak
sum: Rumah adat Sunda memiliki bentuk atap yang khas.
fig: table Ngaran imah | Wangun hateup ;; Julang Ngapak | siga manuk ngapak jangjang ;; Tagog Anjing | siga anjing keur diuk ;; Badak Heuay | siga badak keur heuay ;; Parahu Kumureb | siga parahu nangkub ;; Jolopong | manjang ngajolopong ;; Capit Gunting | tungtungna siga gunting ~ Imah adat Sunda jeung hateupna.
"""

BANK += """
## SUN|Kecap pagawéan
Kecap Sunda pikeun membaca nyaéta …|maca|nulis|dahar|diuk|Membaca = maca.
Kecap Sunda pikeun berlari nyaéta …|lumpat|diuk|nginum|saré|Berlari = lumpat.
=|Kecap Sunda pikeun makan nyaéta …|dahar|Makan = dahar.
=|Kecap Sunda pikeun menulis nyaéta …|nulis|Menulis = nulis.
B|Diuk artinya duduk.|Diuk = duduk.
S|Nginum artinya makan.|Nginum = minum.
Adi keur … buku. Kecap nu merenah nyaéta …|maca|dahar|lumpat|nginum|Membaca buku.
Kecap pagawéan téh hartina …|kata kerja|kata sifat|kata tanya|kata benda|Kata kerja.
## SUN|Kecap sipat
Kecap Sunda pikeun besar nyaéta …|gedé|leutik|geulis|pinter|Besar = gedé.
Kecap Sunda pikeun pandai nyaéta …|pinter|bageur|kasép|leutik|Pandai = pinter.
=|Kecap Sunda pikeun kecil nyaéta …|leutik|Kecil = leutik.
=|Kecap Sunda pikeun cantik nyaéta …|geulis|Cantik = geulis.
B|Bageur artinya baik hati.|Bageur.
S|Kasép artinya cantik.|Kasép = tampan.
Gajah mah sato nu …|gedé|leutik|pinter|geulis|Gajah besar.
Kecap sipat téh hartina …|kata sifat|kata kerja|kata tanya|kata bilangan|Kata sifat.
## SUN|Parabot dapur
Kecap Sunda pikeun cobek nyaéta …|coét|sééng|katél|hihid|Cobek = coét.
Kecap Sunda pikeun wajan nyaéta …|katél|coét|mutu|aseupan|Wajan = katél.
=|Kecap Sunda pikeun dandang nyaéta …|sééng;seeng|Dandang = sééng.
=|Kecap Sunda pikeun ulekan nyaéta …|mutu|Ulekan = mutu.
B|Hihid nyaéta kipas tina awi.|Kipas bambu.
S|Aseupan dipaké pikeun ngulek sambel.|Aseupan kukusan.
Parabot pikeun ngulek sambel nyaéta coét jeung …|mutu|katél|sééng|aseupan|Coét dan mutu.
Parabot pikeun ngakeul sangu nyaéta …|hihid|katél|mutu|coét|Hihid.
## SUN|Paparikan
Paparikan kaasup kana …|sisindiran|dongéng|kawih|wawacan|Sisindiran.
Dua padalisan mimiti dina paparikan disebut …|cangkang|eusi|judul|amanat|Cangkang.
=|Dua padalisan ahir dina paparikan disebut …|eusi|Eusi.
=|Paparikan diwangun ku … padalisan.|opat;4|Empat baris.
B|Eusi paparikan ngandung maksud.|Isi berisi pesan.
S|Paparikan diwangun ku dalapan padalisan.|Opat padalisan.
Padalisan hartina …|baris|bait|judul|sajak|Padalisan = baris.
Sisindiran nu kecap awalna sarua disebut …|rarakitan|paparikan|wawangsalan|kawih|Rarakitan.
## SUN|Seni Sunda
Angklung dijieun tina …|awi|beusi|kai jati|plastik|Angklung dari bambu.
Kacapi dimaénkeun ku cara …|dipetik|ditiup|digoyang|ditakol|Dipetik.
=|Boneka kai pikeun nyarita disebut wayang …|golék;golek|Wayang golék.
=|Tarian khas Sunda nyaéta …|jaipongan|Jaipongan.
B|Angklung dimaénkeun ku cara digoyang.|Digoyang.
S|Suling dimaénkeun ku cara dipetik.|Ditiup.
Nu maénkeun wayang golék disebut …|dalang|sinden|penari|juragan|Dalang.
Calung dimaénkeun ku cara …|ditakol|ditiup|dipetik|digesek|Ditakol.
## SUN|Ngaran tutuwuhan
Kecap Sunda pikeun padi nyaéta …|paré|jukut|awi|jagong|Padi = paré.
Kecap Sunda pikeun bambu nyaéta …|awi|tangkal|kembang|paré|Bambu = awi.
=|Kecap Sunda pikeun bunga nyaéta …|kembang|Bunga = kembang.
=|Kecap Sunda pikeun rumput nyaéta …|jukut|Rumput = jukut.
B|Tangkal artinya pohon.|Tangkal = pohon.
S|Jagong artinya padi.|Jagong = jagung.
Tutuwuhan nu dipelak di sawah nyaéta …|paré|awi|kembang mawar|jukut|Padi di sawah.
Tutuwuhan méré urang hawa nu …|seger|kotor|panas|bau|Udara segar.
## SUN|Di pasar
Kecap Sunda pikeun membeli nyaéta …|meuli|ngajual|nawar|duit|Membeli = meuli.
Kecap Sunda pikeun uang nyaéta …|duit|meuli|padagang|pasar|Uang = duit.
=|Kecap Sunda pikeun menjual nyaéta …|ngajual|Menjual = ngajual.
=|Kecap Sunda pikeun menawar nyaéta …|nawar|Menawar = nawar.
B|Padagang artinya pedagang.|Pedagang.
S|Meuli artinya menjual.|Meuli = membeli.
Pananya harga nu sopan nyaéta …|Sabaraha hargana, Bu?|Naon ieu?|Saha manéh?|Iraha indit?|Menanyakan harga.
Pasar téh tempat …|jual beuli|sakola|ibadah|saré|Jual beli.
## SUN|Kandaraan
Kecap Sunda pikeun sepeda nyaéta …|sapédah|parahu|sado|karéta|Sepeda = sapédah.
Kecap Sunda pikeun perahu nyaéta …|parahu|sapédah|kapal udara|sado|Perahu = parahu.
=|Kecap Sunda pikeun delman nyaéta …|sado|Delman = sado.
=|Kecap Sunda pikeun naik kendaraan nyaéta …|tumpak|Naik = tumpak.
B|Karéta api artinya kereta api.|Kereta api.
S|Kapal udara artinya perahu.|Kapal udara = pesawat.
Kandaraan nu ngapung di langit nyaéta …|kapal udara|parahu|sado|sapédah|Pesawat.
Pamayang ngala lauk tumpak …|parahu|sapédah|sado|karéta api|Perahu.
## SUN|Kabersihan lingkungan
Kecap Sunda pikeun sampah nyaéta …|runtah|solokan|miceun|beresih|Sampah = runtah.
Kecap Sunda pikeun selokan nyaéta …|solokan|runtah|tong|walungan|Selokan = solokan.
=|Kecap Sunda pikeun membuang nyaéta …|miceun|Membuang = miceun.
=|Kecap Sunda pikeun bersih nyaéta …|beresih|Bersih = beresih.
B|Runtah kudu dipiceun kana tong runtah.|Tempat sampah.
S|Miceun runtah ka solokan téh kalakuan nu alus.|Membuang ke selokan buruk.
Kerja bakti dina basa Sunda disebut …|gotong royong|miceun runtah|ulin|saré|Gotong royong.
Mun miceun runtah sambarangan, lingkungan jadi …|kotor|beresih|endah|seger|Kotor.
## SUN|Kecap pananya
Kecap pananya pikeun siapa nyaéta …|saha|naon|iraha|naha|Siapa = saha.
Kecap pananya pikeun kapan nyaéta …|iraha|kumaha|saha|sabaraha|Kapan = iraha.
=|Kecap pananya pikeun apa nyaéta …|naon|Apa = naon.
=|Kecap pananya pikeun berapa nyaéta …|sabaraha|Berapa = sabaraha.
B|Kumaha artinya bagaimana.|Kumaha.
S|Naha artinya siapa.|Naha = mengapa.
… ngaran manéh? Kecap pananya nu merenah nyaéta …|Saha|Iraha|Sabaraha|Naha|Menanyakan nama.
… urang indit ka Bandung? Kecap pananya pikeun waktu nyaéta …|Iraha|Saha|Naon|Kumaha|Menanyakan waktu.
## SUN|Nyaritakeun pangalaman
Nyaritakeun pangalaman artinya …|menceritakan pengalaman|membaca puisi|menyanyikan kawih|menulis surat|Menceritakan pengalaman.
Bagian carita nu nétélakeun waktu nyaéta …|iraha|di mana|jeung saha|kumaha rasana|Waktu.
=|Kamari artinya …|kemarin|Kamari = kemarin.
=|Bungah artinya …|senang;gembira|Bungah = senang.
B|Carita pangalaman kudu runtut.|Berurutan.
S|Nyaritakeun pangalaman teu kudu nyebutkeun tempat.|Tempat perlu disebut.
Bagian carita nu nétélakeun tempat nyaéta …|di mana|iraha|jeung saha|naon|Tempat.
Kecap nu nuduhkeun perasaan nyaéta …|bungah|kamari|bapa|gajah|Perasaan.
## SUN|Imah adat Sunda
Imah adat Sunda dibédakeun tina wangun …|hateup|panto|jandéla|tihang|Bentuk atap.
Imah adat nu hateupna siga manuk ngapak nyaéta …|Julang Ngapak|Tagog Anjing|Badak Heuay|Parahu Kumureb|Julang Ngapak.
=|Imah adat nu hateupna siga parahu nangkub nyaéta Parahu …|Kumureb|Parahu Kumureb.
=|Imah adat Sunda biasana mangrupa imah …|panggung|Rumah panggung.
B|Badak Heuay hateupna siga badak keur heuay.|Badak menguap.
S|Sakabéh imah adat Sunda wangunna sarua.|Berbeda-beda.
Imah adat nu hateupna siga anjing keur diuk nyaéta …|Tagog Anjing|Jolopong|Capit Gunting|Julang Ngapak|Tagog Anjing.
Hateup hartina …|atap|pintu|jendela|lantai|Hateup = atap.
"""

SAS += """
## SUN 1
0|Nginum artinya ....|minum|makan|membaca|tidur|Nginum = minum.
1|Geulis artinya ....|cantik|besar|kecil|pandai|Geulis = cantik.
2|Katél dipaké pikeun ....|ngagoréng|ngulek|ngakeul|nyimpen cai|Wajan untuk menggoreng.
3|Cangkang dina paparikan aya dina padalisan ....|kahiji jeung kadua|katilu jeung kaopat|kahiji wungkul|kaopat wungkul|Cangkang baris 1-2.
4|Jaipongan téh kasenian Sunda mangrupa ....|tarian|alat musik|kadaharan|imah adat|Tarian.
5|Awi artinya ....|bambu|padi|rumput|bunga|Awi = bambu.
## SUN 2
0|Sabaraha hargana artinya ....|berapa harganya|di mana pasarnya|siapa penjualnya|kapan tutupnya|Berapa harganya.
1|Abdi indit ka sakola tumpak sapédah. Sapédah artinya ....|sepeda|perahu|delman|kereta|Sepeda.
2|Tong runtah artinya ....|tempat sampah|selokan|sapu|halaman|Tempat sampah.
3|Kumaha artinya ....|bagaimana|siapa|kapan|berapa|Kumaha.
4|Jeung saha dina carita pangalaman nuduhkeun ....|batur nu milu|waktu kajadian|tempat kajadian|perasaan|Dengan siapa.
5|Imah adat Sunda nu hateupna manjang disebut ....|Jolopong|Julang Ngapak|Badak Heuay|Tagog Anjing|Jolopong.
"""
