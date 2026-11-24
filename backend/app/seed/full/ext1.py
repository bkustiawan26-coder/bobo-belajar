TOPICS = """
## MAT
# 1^|Bilangan sampai 10
@ Bilangan 1 sampai 10
min: 8
act: Hitung benda di rumah bersama Ayah atau Bunda, misalnya sendok, sandal, dan jeruk, sampai 10.
mis: melompati satu benda saat menghitung
exp: Kita menghitung benda satu per satu sambil menunjuk. Bilangan 1 sampai 10 dibaca satu, dua, tiga, empat, lima, enam, tujuh, delapan, sembilan, sepuluh. Benda terakhir yang dihitung menunjukkan banyaknya benda.
ex: Ada 🍎🍎🍎🍎🍎. Hitung: satu, dua, tiga, empat, lima. Ada 5 apel. // Angka 8 dibaca delapan.
pt: Hitung sambil menunjuk satu per satu ; Bilangan terakhir adalah banyaknya benda ; Angka 1 sampai 10 punya nama masing-masing
sum: Menghitung satu per satu membantu kita tahu banyaknya benda.
fig: count 8 🐤 ~ Hitung anak ayam satu per satu. Ada 8 anak ayam.
@ Bilangan sebelum dan sesudah
min: 8
act: Bermain tebak bilangan: Ayah menyebut bilangan, kamu menyebut bilangan sesudahnya.
mis: tertukar antara bilangan sebelum dan sesudah
exp: Bilangan sesudah adalah bilangan yang satu lebih banyak. Bilangan sebelum adalah bilangan yang satu lebih sedikit. Pada garis bilangan, bilangan sesudah ada di sebelah kanan dan bilangan sebelum ada di sebelah kiri.
ex: Sesudah 6 adalah 7. // Sebelum 6 adalah 5. // Di antara 4 dan 6 ada 5.
pt: Sesudah berarti satu lebih banyak ; Sebelum berarti satu lebih sedikit ; Garis bilangan membantu melihat urutan
sum: Urutan bilangan naik satu-satu: sebelum, bilangan itu, lalu sesudah.
fig: line 0..10 step 1 ; jump 4>5>6 ~ Dari 4 melompat ke 5, lalu ke 6. Sebelum 5 adalah 4, sesudah 5 adalah 6.
@ Penjumlahan sampai 10
min: 8
act: Gunakan kancing atau batu kecil: ambil 3, tambah 4, lalu hitung semuanya.
mis: menghitung ulang dari satu tanpa memakai cara melanjutkan hitungan
exp: Penjumlahan berarti menggabungkan dua kelompok benda. Tanda tambah ditulis +. Kita bisa menghitung semua benda, atau mulai dari bilangan pertama lalu melanjutkan hitungan.
ex: 3 + 4 = 7. Mulai dari 3, lanjutkan empat kali: 4, 5, 6, 7. // 5 + 5 = 10.
pt: Penjumlahan berarti menggabungkan ; Tanda tambah ditulis + ; Lanjutkan hitungan dari bilangan pertama
sum: Menjumlahkan sama dengan menggabungkan lalu menghitung semuanya.
fig: count 3 🍓 + 4 🍓 = 7 🍓 ~ 3 stroberi ditambah 4 stroberi menjadi 7 stroberi.
@ Pengurangan sampai 10
min: 8
act: Siapkan 9 kue mainan, makan pura-pura 4, lalu hitung sisanya.
mis: menambah, bukan mengurangi, saat soal bertanya sisa
exp: Pengurangan berarti mengambil sebagian benda dari kelompoknya. Tanda kurang ditulis −. Sisa benda adalah hasil pengurangan. Kita bisa menghitung mundur dari bilangan pertama.
ex: 9 − 4 = 5. Hitung mundur empat kali dari 9: 8, 7, 6, 5. // 7 − 7 = 0, tidak ada yang tersisa.
pt: Pengurangan berarti mengambil ; Tanda kurang ditulis − ; Hasilnya disebut sisa
sum: Mengurangi berarti mengambil, lalu menghitung sisa.
fig: count 9 🎈 − 4 🎈 = 5 🎈 ~ Ada 9 balon, 4 terbang, sisa 5 balon.
@ Bangun ruang di sekitarku
min: 8
act: Cari benda di rumah yang berbentuk kubus, balok, tabung, dan bola, lalu kelompokkan.
mis: menyebut bola sebagai lingkaran
exp: Bangun ruang adalah bentuk benda yang bisa dipegang dan punya isi. Contohnya kubus seperti dadu, balok seperti kardus, tabung seperti kaleng, bola seperti bola sepak, dan kerucut seperti topi ulang tahun.
ex: Dadu berbentuk kubus. // Kaleng susu berbentuk tabung. // Bola sepak berbentuk bola.
pt: Kubus seperti dadu ; Balok seperti kardus ; Tabung seperti kaleng dan bola seperti bola sepak
sum: Banyak benda di sekitar kita berbentuk bangun ruang.
fig: table Benda | Bentuk ;; dadu | kubus ;; kardus sepatu | balok ;; kaleng susu | tabung ;; bola sepak | bola ;; topi ulang tahun | kerucut ~ Benda di sekitar kita dan bentuk bangun ruangnya.
@ Pola gambar dan bilangan kecil
min: 8
act: Susun sendok dan garpu bergantian, lalu minta adik melanjutkan polanya.
mis: melanjutkan pola tanpa melihat bagian yang berulang
exp: Pola adalah susunan yang berulang dengan aturan yang sama. Pola gambar bisa berupa warna atau benda yang bergantian. Pola bilangan bisa naik satu-satu atau dua-dua.
ex: 🔴 🔵 🔴 🔵 🔴, berikutnya 🔵. // 2, 4, 6, 8, berikutnya 10.
pt: Pola adalah susunan berulang ; Cari bagian yang berulang ; Pola bilangan punya aturan tambah yang sama
sum: Kalau tahu aturannya, kita bisa melanjutkan pola.
fig: line 0..12 step 1 ; jump 2>4>6>8>10 ~ Pola melompat dua-dua: 2, 4, 6, 8, 10.
# 2|Bilangan Besar, Ukuran, dan Waktu
@ Puluhan dan satuan
min: 8
act: Ikat 10 lidi menjadi satu ikat. Buat bilangan 34 dengan 3 ikat dan 4 lidi lepas.
mis: menulis 3 puluhan 4 satuan sebagai 7
exp: Sepuluh satuan sama dengan satu puluhan. Bilangan dua angka terdiri atas puluhan dan satuan. Angka kiri menunjukkan puluhan, angka kanan menunjukkan satuan.
ex: 34 terdiri atas 3 puluhan dan 4 satuan. // 50 terdiri atas 5 puluhan dan 0 satuan.
pt: 10 satuan sama dengan 1 puluhan ; Angka kiri adalah puluhan ; Angka kanan adalah satuan
sum: Bilangan dua angka disusun dari puluhan dan satuan.
fig: place 34 ~ 3 puluhan dan 4 satuan membentuk 34.
@ Bilangan sampai 100
min: 8
act: Hitung loncat sepuluh-sepuluh sambil bertepuk tangan sampai 100.
mis: membaca 71 sebagai tujuh satu
exp: Setelah 20 ada 21, 22, sampai 29, lalu 30. Begitu seterusnya sampai 100. Bilangan puluhan dibaca sepuluh, dua puluh, tiga puluh, sampai sembilan puluh. Sepuluh puluhan sama dengan seratus.
ex: 47 dibaca empat puluh tujuh. // Sesudah 59 adalah 60. // 10, 20, 30, 40, 50 adalah hitungan loncat sepuluh.
pt: Bilangan dibaca puluhan dulu lalu satuan ; Sesudah 9 satuan, puluhannya bertambah ; Sepuluh puluhan sama dengan 100
sum: Kita bisa membaca dan mengurutkan bilangan sampai 100.
fig: line 0..100 step 10 ; jump 10>20>30>40>50 ~ Hitung loncat sepuluh-sepuluh di garis bilangan.
@ Mengukur panjang dengan jengkal
min: 8
act: Ukur panjang meja makan dengan jengkalmu, lalu bandingkan dengan jengkal Ayah.
mis: mengira hasil jengkal semua orang pasti sama
exp: Kita bisa mengukur panjang benda dengan jengkal, langkah kaki, atau depa. Satuan seperti ini disebut satuan tidak baku karena ukurannya berbeda untuk tiap orang. Saat mengukur, jengkal harus disambung rapat tanpa celah.
ex: Panjang meja 6 jengkal. // Panjang kelas 20 langkah. // Jengkal Ayah lebih panjang dari jengkal adik.
pt: Jengkal, langkah, dan depa adalah satuan tidak baku ; Sambung rapat saat mengukur ; Hasil tiap orang bisa berbeda
sum: Jengkal membantu mengukur, tetapi hasilnya bisa berbeda tiap orang.
fig: table Benda | Panjang ;; buku | 2 jengkal ;; pintu | 5 jengkal ;; meja | 6 jengkal ;; lemari | 7 jengkal ;; karpet | 9 jengkal ;; papan tulis | 12 jengkal ~ Hasil mengukur benda dengan jengkal.
@ Berat dan ringan benda
min: 8
act: Angkat dua benda di rumah, tebak mana yang lebih berat, lalu cek dengan timbangan.
mis: mengira benda besar pasti lebih berat
exp: Ada benda yang berat dan ada yang ringan. Kita bisa membandingkan dengan mengangkat atau memakai timbangan. Pada timbangan dua lengan, sisi yang lebih berat akan turun dan sisi yang lebih ringan akan naik.
ex: Semangka lebih berat dari anggur. // Bantal besar bisa lebih ringan dari batu kecil.
pt: Bandingkan dengan mengangkat atau menimbang ; Sisi yang turun lebih berat ; Benda besar belum tentu berat
sum: Timbangan membantu kita tahu mana yang lebih berat.
fig: balance 🍉 | 🍇 ~ Semangka lebih berat, jadi sisi semangka turun.
@ Membaca jam tepat
min: 8
act: Lihat jam dinding di rumah setiap kali waktunya makan, lalu sebutkan pukul berapa.
mis: tertukar antara jarum pendek dan jarum panjang
exp: Jam punya jarum pendek dan jarum panjang. Jarum pendek menunjukkan jam. Saat jarum panjang menunjuk angka 12, waktunya jam tepat, misalnya pukul 7 tepat.
ex: Jarum pendek di 7, jarum panjang di 12: pukul 7. // Jarum pendek di 12, jarum panjang di 12: pukul 12.
pt: Jarum pendek menunjukkan jam ; Jarum panjang di 12 berarti jam tepat ; Jam punya angka 1 sampai 12
sum: Lihat jarum pendek untuk tahu pukul berapa saat jam tepat.
fig: clock 7:00 ~ Jarum pendek di angka 7, jarum panjang di angka 12. Pukul 7 tepat.
@ Nama hari dalam seminggu
min: 8
act: Buat kalender kecil berisi kegiatanmu dari Senin sampai Minggu.
mis: salah urutan hari Kamis dan Jumat
exp: Satu minggu ada tujuh hari, yaitu Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, dan Minggu. Setelah Minggu, kembali lagi ke Senin. Kita sekolah pada hari Senin sampai Jumat atau Sabtu.
ex: Sesudah Rabu adalah Kamis. // Sebelum Senin adalah Minggu.
pt: Satu minggu ada tujuh hari ; Urutannya Senin sampai Minggu ; Sesudah Minggu kembali ke Senin
sum: Hafalkan urutan hari supaya tahu jadwal kegiatan.
fig: cycle 1️⃣ Senin > 2️⃣ Selasa > 3️⃣ Rabu > 4️⃣ Kamis > 5️⃣ Jumat > 6️⃣ Sabtu > 7️⃣ Minggu ~ Urutan hari berulang setiap minggu.

## BIN
# 1|Aku dan Bacaanku
@ Membaca huruf kapital dan huruf kecil
min: 8
act: Cari huruf kapital pada nama-nama di kemasan makanan di rumah.
mis: menulis nama orang diawali huruf kecil
exp: Setiap huruf punya dua bentuk, yaitu huruf kapital dan huruf kecil. Huruf kapital dipakai di awal kalimat dan di awal nama orang, nama kota, atau nama hari. Huruf kecil dipakai untuk huruf lainnya.
ex: A besar dan a kecil adalah huruf yang sama. // Nama Budi diawali huruf B kapital.
pt: Setiap huruf punya bentuk kapital dan kecil ; Huruf kapital di awal kalimat ; Nama orang dan tempat diawali huruf kapital
sum: Huruf kapital dipakai di awal kalimat dan nama.
fig: table Huruf kapital | Huruf kecil ;; A | a ;; B | b ;; D | d ;; G | g ;; M | m ;; R | r ~ Pasangan huruf kapital dan huruf kecil.
@ Kata benda di rumahku
min: 8
act: Tempelkan kertas bertuliskan nama benda pada benda di rumah, misalnya pintu, kursi, dan meja.
mis: menyebut kata kerja sebagai nama benda
exp: Kata benda adalah kata yang menunjukkan nama benda. Di rumah ada banyak benda, seperti kursi, meja, piring, sapu, dan lemari. Kita bisa membaca dan menulis nama benda itu.
ex: Kursi untuk duduk. // Piring untuk tempat makanan. // Sapu untuk membersihkan lantai.
pt: Kata benda adalah nama benda ; Benda di rumah punya nama dan kegunaan ; Membaca nama benda melatih membaca kata
sum: Kenali nama benda di rumah dan kegunaannya.
fig: table Benda | Kegunaan ;; kursi | tempat duduk ;; piring | tempat makanan ;; sapu | membersihkan lantai ;; lemari | menyimpan pakaian ;; bantal | alas kepala saat tidur ;; gelas | tempat minum ~ Benda di rumah dan kegunaannya.
@ Kata kerja sehari-hari
min: 8
act: Peragakan satu kegiatan, misalnya menyapu, lalu minta keluarga menebak kata kerjanya.
mis: menyebut nama benda saat diminta kata kerja
exp: Kata kerja adalah kata yang menunjukkan kegiatan atau perbuatan. Contohnya makan, minum, mandi, membaca, menulis, dan berlari. Kata kerja menjawab pertanyaan sedang apa.
ex: Adik sedang minum susu. // Kakak membaca buku. // Ibu memasak di dapur.
pt: Kata kerja menunjukkan kegiatan ; Kata kerja menjawab pertanyaan sedang apa ; Kita melakukan banyak kegiatan setiap hari
sum: Kata kerja menceritakan apa yang sedang dilakukan.
fig: icons 🍽️ makan ; 🥛 minum ; 🛁 mandi ; 📖 membaca ; ✏️ menulis ; 🏃 berlari ~ Contoh kata kerja sehari-hari.
@ Menyusun kata menjadi kalimat
min: 8
act: Tulis empat kata di kartu, misalnya adik, makan, nasi, dan goreng, lalu susun menjadi kalimat.
mis: menyusun kata tanpa urutan yang benar
exp: Kalimat adalah susunan kata yang punya arti. Kalimat diawali huruf kapital dan diakhiri tanda titik. Kata-kata harus disusun dengan urutan yang benar supaya artinya jelas.
ex: Kata ibu, pasar, ke, pergi disusun menjadi Ibu pergi ke pasar. // Kalimat Budi bermain bola diawali huruf B kapital.
pt: Kalimat adalah susunan kata yang punya arti ; Diawali huruf kapital ; Diakhiri tanda titik
sum: Susun kata dengan urutan benar supaya kalimat mudah dipahami.
fig: steps 👦 Budi > ⚽ bermain > 🟢 bola > 🌳 di lapangan ~ Kata-kata disusun menjadi kalimat: Budi bermain bola di lapangan.
@ Huruf ganda ng dan ny
min: 8
act: Cari benda di rumah yang namanya memakai ng atau ny, misalnya piring dan nyamuk.
mis: membaca ng sebagai n dan g terpisah
exp: Huruf ng dan ny adalah dua huruf yang dibaca menjadi satu bunyi. Ng ada pada kata bunga dan piring. Ny ada pada kata nyanyi dan nyamuk. Kita membacanya dengan satu bunyi, bukan terpisah.
ex: Bu-nga dibaca bunga. // Nya-mu-k dibaca nyamuk.
pt: Ng dan ny dibaca satu bunyi ; Contoh ng: bunga, piring ; Contoh ny: nyanyi, nyamuk
sum: Ng dan ny adalah huruf ganda yang dibaca menjadi satu bunyi.
fig: table Kata | Huruf ganda ;; bunga | ng ;; piring | ng ;; nyamuk | ny ;; nyanyi | ny ;; kancing | ng ;; banyak | ny ~ Kata yang memakai huruf ganda ng dan ny.
@ Membaca puisi anak
min: 8
act: Bacakan puisi pendek untuk keluarga dengan suara jelas dan ekspresi gembira.
mis: membaca puisi terlalu cepat tanpa jeda
exp: Puisi adalah karangan yang disusun dalam baris-baris dengan kata yang indah. Puisi dibaca dengan suara jelas, tidak terlalu cepat, dan memakai ekspresi sesuai isinya. Setiap baris puisi diberi jeda sebentar.
ex: Ibu, kasihmu sepanjang masa. // Bulan bersinar, bintang berkelip.
pt: Puisi disusun dalam baris ; Baca dengan suara jelas dan tidak terburu-buru ; Pakai ekspresi sesuai isi
sum: Membaca puisi dengan jelas dan berekspresi membuat pendengar senang.
fig: steps 📖 Baca dalam hati > 🗣️ Ucapkan dengan jelas > ⏸️ Beri jeda tiap baris > 😊 Pakai ekspresi ~ Langkah membaca puisi.
# 2|Bercerita dan Menulis
@ Kalimat perintah dan ajakan
min: 8
act: Buat tiga kalimat ajakan untuk mengajak keluarga membereskan rumah.
mis: menulis kalimat ajakan tanpa kata mari atau ayo
exp: Kalimat perintah meminta orang lain melakukan sesuatu, misalnya Tutup pintunya. Kalimat ajakan mengajak orang lain bersama-sama, biasanya memakai kata ayo atau mari. Kalimat perintah yang sopan memakai kata tolong.
ex: Tolong ambilkan buku itu. // Ayo kita bermain bersama. // Mari membuang sampah pada tempatnya.
pt: Kalimat perintah meminta orang melakukan sesuatu ; Kalimat ajakan memakai ayo atau mari ; Pakai kata tolong supaya sopan
sum: Gunakan kalimat perintah dan ajakan dengan sopan.
fig: compare 🙏 Perintah = tolong tutup pintu ; tolong ambilkan buku ; duduklah dengan rapi || 🤝 Ajakan = ayo bermain ; mari belajar ; ayo makan bersama ~ Contoh kalimat perintah dan kalimat ajakan.
@ Menceritakan gambar
min: 8
act: Pilih satu gambar di buku cerita, lalu ceritakan siapa, di mana, dan sedang apa.
mis: hanya menyebut nama benda tanpa menceritakan kegiatan
exp: Saat menceritakan gambar, kita melihat dengan teliti siapa yang ada, di mana tempatnya, dan apa yang sedang dilakukan. Lalu kita menyusunnya menjadi kalimat yang urut.
ex: Gambar: anak menyiram bunga di taman. // Ceritanya: Sinta menyiram bunga di taman setiap pagi.
pt: Lihat siapa yang ada di gambar ; Lihat tempat dan kegiatannya ; Susun menjadi kalimat urut
sum: Menceritakan gambar melatih kita berbicara dengan runtut.
fig: table Pertanyaan | Jawaban ;; siapa | Sinta ;; di mana | taman ;; sedang apa | menyiram bunga ;; kapan | pagi hari ;; memakai apa | gembor ;; perasaannya | senang ~ Pertanyaan untuk menceritakan gambar anak menyiram bunga.
@ Kosakata anggota keluarga
min: 8
act: Gambar pohon keluarga dan tulis nama panggilan setiap anggota keluarga.
mis: tertukar antara kakek dan paman
exp: Keluarga terdiri atas ayah, ibu, kakak, dan adik. Orang tua dari ayah atau ibu disebut kakek dan nenek. Saudara ayah atau ibu disebut paman dan bibi. Kita menyayangi dan menghormati semua anggota keluarga.
ex: Ayah dari ibuku adalah kakekku. // Adik laki-laki ayah adalah pamanku.
pt: Keluarga inti: ayah, ibu, kakak, adik ; Orang tua ayah dan ibu disebut kakek dan nenek ; Saudara orang tua disebut paman dan bibi
sum: Mengenal sebutan anggota keluarga membantu kita berbicara dengan sopan.
fig: table Sebutan | Artinya ;; kakek | ayah dari ayah atau ibu ;; nenek | ibu dari ayah atau ibu ;; paman | saudara laki-laki orang tua ;; bibi | saudara perempuan orang tua ;; kakak | saudara yang lebih tua ;; adik | saudara yang lebih muda ~ Sebutan anggota keluarga.
@ Menulis kalimat tentang diriku
min: 8
act: Tulis tiga kalimat tentang dirimu: nama, umur, dan hobi. Bacakan kepada keluarga.
mis: tidak memakai huruf kapital di awal nama sendiri
exp: Kita bisa menulis kalimat tentang diri sendiri, misalnya nama, umur, alamat, dan hobi. Setiap kalimat diawali huruf kapital dan diakhiri tanda titik. Nama sendiri juga ditulis dengan huruf kapital di awal.
ex: Namaku Rina. // Aku berumur tujuh tahun. // Hobiku menggambar.
pt: Tulis nama, umur, dan hobi ; Awali kalimat dengan huruf kapital ; Akhiri kalimat dengan tanda titik
sum: Menulis tentang diri sendiri melatih kita menulis kalimat dengan benar.
fig: steps 🙋 Namaku Rina > 🎂 Umurku tujuh tahun > 🏠 Rumahku di Cibodas > 🎨 Hobiku menggambar ~ Contoh kalimat tentang diriku.
@ Kata sifat dan lawan kata
min: 8
act: Cari pasangan benda di rumah yang bisa dibandingkan, misalnya gelas penuh dan gelas kosong.
mis: menyebut lawan kata yang tidak tepat, misalnya besar lawannya panjang
exp: Kata sifat menjelaskan keadaan benda atau orang, misalnya besar, kecil, panas, dingin. Lawan kata adalah kata yang artinya berkebalikan. Besar lawannya kecil, panas lawannya dingin.
ex: Gajah besar, semut kecil. // Es dingin, teh panas.
pt: Kata sifat menjelaskan keadaan ; Lawan kata artinya berkebalikan ; Contoh: tinggi dan rendah
sum: Kata sifat dan lawan kata membuat cerita lebih jelas.
fig: table Kata sifat | Lawan kata ;; besar | kecil ;; panas | dingin ;; tinggi | rendah ;; panjang | pendek ;; gelap | terang ;; cepat | lambat ~ Pasangan kata sifat dan lawan katanya.
@ Mendengarkan petunjuk
min: 8
act: Minta keluarga memberi tiga petunjuk berurutan, lalu lakukan sesuai urutan.
mis: melakukan petunjuk tidak sesuai urutan
exp: Petunjuk adalah keterangan tentang cara melakukan sesuatu. Saat mendengarkan petunjuk, kita harus fokus, mengingat urutannya, lalu melakukannya satu per satu. Jika belum jelas, kita boleh bertanya dengan sopan.
ex: Petunjuk mencuci tangan: basahi tangan, beri sabun, gosok, bilas, lalu keringkan.
pt: Dengarkan dengan fokus ; Ingat urutannya ; Bertanya dengan sopan jika belum jelas
sum: Mendengarkan petunjuk dengan baik membuat pekerjaan berhasil.
fig: steps 💧 Basahi tangan > 🧴 Beri sabun > 👐 Gosok sela jari > 🚿 Bilas dengan air > 🧻 Keringkan ~ Petunjuk mencuci tangan yang benar.

## PPK
# 1|Aku dan Pancasila
@ Simbol sila-sila Pancasila
min: 8
act: Gambar lima simbol Pancasila dan tempel di dinding kamar.
mis: tertukar simbol sila kedua dan sila ketiga
exp: Pancasila punya lima sila dengan simbol masing-masing. Sila pertama bintang, sila kedua rantai, sila ketiga pohon beringin, sila keempat kepala banteng, dan sila kelima padi dan kapas. Simbol itu ada pada perisai di dada Garuda Pancasila.
ex: Bintang adalah simbol sila pertama. // Padi dan kapas adalah simbol sila kelima.
pt: Pancasila punya lima sila ; Setiap sila punya simbol ; Simbol ada di perisai Garuda
sum: Mengenal simbol sila membantu kita mengingat Pancasila.
fig: table Sila | Simbol ;; pertama | bintang ;; kedua | rantai ;; ketiga | pohon beringin ;; keempat | kepala banteng ;; kelima | padi dan kapas ~ Simbol setiap sila Pancasila.
@ Garuda Pancasila
min: 8
act: Amati gambar Garuda Pancasila di kelas, lalu ceritakan kepada keluarga apa saja yang kamu lihat.
mis: mengira semboyan negara adalah Pancasila
exp: Garuda Pancasila adalah lambang negara Indonesia. Garuda mencengkeram pita bertuliskan Bhinneka Tunggal Ika yang artinya berbeda-beda tetapi tetap satu. Di dadanya ada perisai berisi lima simbol sila Pancasila.
ex: Lambang negara kita adalah Garuda Pancasila. // Bhinneka Tunggal Ika artinya berbeda-beda tetapi tetap satu.
pt: Garuda Pancasila adalah lambang negara ; Semboyannya Bhinneka Tunggal Ika ; Perisai di dada berisi simbol sila
sum: Garuda Pancasila adalah lambang negara yang kita hormati.
fig: table Bagian | Keterangan ;; burung garuda | lambang negara ;; perisai | berisi lima simbol sila ;; pita | bertuliskan semboyan ;; Bhinneka Tunggal Ika | berbeda-beda tetap satu ;; warna emas | lambang kejayaan ;; kepala menoleh ke kanan | arah kebaikan ~ Bagian-bagian Garuda Pancasila.
@ Bersyukur sebagai ciptaan Tuhan
min: 8
act: Tulis tiga hal yang kamu syukuri hari ini, lalu berdoa bersama keluarga.
mis: menganggap bersyukur cukup diucapkan tanpa dilakukan
exp: Kita semua ciptaan Tuhan Yang Maha Esa. Kita bersyukur dengan berdoa, merawat tubuh, dan menyayangi sesama. Ini sesuai dengan sila pertama Pancasila.
ex: Berdoa sebelum makan adalah tanda syukur. // Merawat tubuh dengan mandi dan makan sehat juga tanda syukur.
pt: Kita adalah ciptaan Tuhan ; Bersyukur dengan berdoa dan merawat diri ; Sesuai sila pertama Pancasila
sum: Bersyukur membuat hati senang dan dekat dengan Tuhan.
fig: icons 🤲 berdoa ; 🛁 merawat tubuh ; 🍎 makan sehat ; 🤗 menyayangi keluarga ; 🌱 merawat tanaman ; 😊 berterima kasih ~ Cara bersyukur sebagai ciptaan Tuhan.
@ Menyayangi teman
min: 8
act: Bantu satu teman atau saudara hari ini, lalu ceritakan perasaanmu.
mis: hanya mau bermain dengan teman tertentu saja
exp: Menyayangi teman berarti berbuat baik kepada semua teman. Kita meminjamkan barang, menolong teman yang jatuh, dan tidak mengejek. Ini sesuai dengan sila kedua Pancasila.
ex: Meminjamkan pensil kepada teman. // Menghibur teman yang sedih.
pt: Berbuat baik kepada semua teman ; Tidak mengejek atau memukul ; Sesuai sila kedua Pancasila
sum: Menyayangi teman membuat kelas terasa nyaman.
fig: compare 😊 Baik = meminjamkan pensil ; menolong teman ; mengajak bermain || 😢 Tidak baik = mengejek ; merebut mainan ; memukul ~ Perbuatan baik dan tidak baik kepada teman.
@ Disiplin waktu
min: 8
act: Buat jadwal harian bergambar dan tempel di kamar. Centang setiap kegiatan yang selesai.
mis: menunda kegiatan sampai terlambat
exp: Disiplin waktu berarti melakukan kegiatan tepat pada waktunya. Contohnya bangun pagi, berangkat sekolah tidak terlambat, dan tidur tepat waktu. Disiplin membuat kegiatan berjalan lancar.
ex: Bangun pukul 5 lalu bersiap ke sekolah. // Mengerjakan PR sebelum bermain.
pt: Disiplin berarti tepat waktu ; Buat jadwal kegiatan ; Disiplin membuat hidup teratur
sum: Disiplin waktu membantu kita tidak terlambat.
fig: time pukul 05.00 = bangun dan salat ; pukul 06.30 = berangkat sekolah ; pukul 13.00 = pulang dan makan ; pukul 15.00 = belajar ; pukul 20.00 = tidur ~ Contoh jadwal harian yang disiplin.
@ Hak dan kewajiban anak di rumah
min: 8
act: Tanyakan kepada orang tua tugas apa yang bisa kamu bantu setiap hari.
mis: hanya meminta hak tanpa melakukan kewajiban
exp: Hak adalah sesuatu yang boleh kita terima, misalnya kasih sayang, makanan, dan bermain. Kewajiban adalah sesuatu yang harus kita lakukan, misalnya membantu orang tua, merapikan mainan, dan belajar.
ex: Hak: mendapat makanan bergizi. // Kewajiban: merapikan tempat tidur sendiri.
pt: Hak adalah yang boleh kita terima ; Kewajiban adalah yang harus kita lakukan ; Lakukan kewajiban sebelum meminta hak
sum: Hak dan kewajiban harus seimbang.
fig: compare 🎁 Hak = kasih sayang ; makanan bergizi ; waktu bermain || 🧹 Kewajiban = merapikan mainan ; membantu orang tua ; belajar ~ Hak dan kewajiban anak di rumah.
# 2|Aku Cinta Indonesia
@ Lagu kebangsaan Indonesia Raya
min: 8
act: Nyanyikan Indonesia Raya bersama keluarga dengan sikap berdiri tegak.
mis: bercanda saat lagu kebangsaan dinyanyikan
exp: Indonesia Raya adalah lagu kebangsaan Indonesia ciptaan Wage Rudolf Supratman. Saat lagu ini dinyanyikan, kita berdiri tegak, tidak bercanda, dan bernyanyi dengan khidmat.
ex: Indonesia Raya dinyanyikan saat upacara bendera. // Pencipta lagu Indonesia Raya adalah W.R. Supratman.
pt: Indonesia Raya adalah lagu kebangsaan ; Diciptakan oleh W.R. Supratman ; Dinyanyikan dengan sikap tegak dan khidmat
sum: Menyanyikan Indonesia Raya dengan khidmat tanda cinta tanah air.
fig: steps 🧍 Berdiri tegak > 👀 Pandangan ke depan > 🎶 Bernyanyi dengan khidmat > 🤐 Tidak bercanda ~ Sikap saat menyanyikan lagu Indonesia Raya.
@ Upacara bendera
min: 8
act: Peragakan sikap hormat bendera di rumah bersama adik atau kakak.
mis: tidak hormat saat bendera dikibarkan
exp: Upacara bendera dilaksanakan di sekolah, biasanya setiap hari Senin. Saat bendera Merah Putih dikibarkan, kita memberi hormat. Petugas upacara antara lain pembina, pemimpin upacara, dan pengibar bendera.
ex: Saat bendera naik, peserta memberi hormat. // Upacara dilakukan dengan tertib dan tenang.
pt: Upacara bendera biasanya hari Senin ; Beri hormat saat bendera dikibarkan ; Ikuti upacara dengan tertib
sum: Mengikuti upacara dengan tertib tanda menghormati bendera.
fig: table Petugas | Tugas ;; pembina upacara | memberi amanat ;; pemimpin upacara | memimpin barisan ;; pengibar bendera | mengibarkan bendera ;; paduan suara | menyanyikan lagu ;; pembaca teks Pancasila | membacakan Pancasila ;; pembawa doa | memimpin doa ~ Petugas upacara bendera dan tugasnya.
@ Keragaman teman di kelas
min: 8
act: Tanyakan kepada tiga teman tentang makanan kesukaan dan asal daerah keluarganya.
mis: mengejek teman yang berbeda
exp: Teman di kelas berbeda-beda. Ada yang tinggi dan pendek, ada yang berbeda agama, suku, dan kesukaan. Perbedaan itu indah. Kita tetap berteman dan saling menghargai.
ex: Rina suka menggambar, Dodi suka sepak bola, mereka tetap bermain bersama.
pt: Setiap teman berbeda ; Perbedaan itu indah ; Saling menghargai dan tetap berteman
sum: Berbeda-beda tetapi tetap bersahabat.
fig: icons 🎨 suka menggambar ; ⚽ suka sepak bola ; 🎤 suka menyanyi ; 📚 suka membaca ; 🧩 suka puzzle ; 🏊 suka berenang ~ Kesukaan teman berbeda-beda.
@ Musyawarah di keluarga
min: 8
act: Ajak keluarga bermusyawarah memilih tempat jalan-jalan akhir pekan.
mis: memaksakan kemauan sendiri
exp: Musyawarah adalah berbicara bersama untuk mengambil keputusan. Setiap orang boleh menyampaikan pendapat. Hasil musyawarah dijalankan bersama walaupun berbeda dengan keinginan kita. Ini sesuai sila keempat.
ex: Keluarga bermusyawarah memilih menu makan malam. // Hasilnya dijalankan bersama dengan senang hati.
pt: Musyawarah berarti berbicara bersama ; Semua boleh berpendapat ; Hasilnya dijalankan bersama
sum: Musyawarah membuat keputusan adil untuk semua.
fig: steps 🗣️ Sampaikan pendapat > 👂 Dengarkan pendapat lain > 🤝 Ambil keputusan bersama > ✅ Jalankan hasilnya ~ Langkah musyawarah di keluarga.
@ Adil kepada saudara
min: 8
act: Bagikan camilan sama banyak kepada saudaramu.
mis: mengambil bagian lebih banyak untuk diri sendiri
exp: Adil berarti memberi sesuai haknya dan tidak berat sebelah. Kita bersikap adil kepada saudara dengan berbagi sama banyak, bergantian bermain, dan tidak mau menang sendiri. Ini sesuai sila kelima.
ex: Kue dibagi rata untuk kakak dan adik. // Mainan dipakai bergantian.
pt: Adil berarti tidak berat sebelah ; Berbagi sama banyak ; Bergantian bermain
sum: Bersikap adil membuat semua merasa senang.
fig: compare ⚖️ Adil = berbagi sama banyak ; bergantian bermain ; mendengarkan semua || 🙅 Tidak adil = mengambil lebih banyak ; tidak mau bergantian ; menang sendiri ~ Contoh sikap adil dan tidak adil.
@ Kekayaan alam Indonesia
min: 8
act: Cari gambar buah atau hewan khas Indonesia, lalu tempel di buku.
mis: membuang makanan karena tidak suka
exp: Indonesia punya kekayaan alam yang banyak, seperti hutan, laut, gunung, sawah, buah-buahan, dan hewan langka. Kita bersyukur dan menjaganya dengan tidak merusak alam dan tidak membuang sampah sembarangan.
ex: Komodo hanya ada di Indonesia. // Sawah menghasilkan padi untuk nasi.
pt: Indonesia kaya hutan, laut, dan gunung ; Ada hewan khas seperti komodo ; Jaga alam dengan tidak merusaknya
sum: Kekayaan alam Indonesia harus kita syukuri dan jaga.
fig: table Kekayaan alam | Hasilnya ;; sawah | padi ;; laut | ikan ;; hutan | kayu ;; kebun | buah-buahan ;; gunung | udara sejuk ;; Pulau Komodo | hewan komodo ~ Kekayaan alam Indonesia dan hasilnya.

## SBD
# 1|Rupa dan Bunyi di Sekitarku
@ Mengenal warna di alam
min: 8
act: Jalan-jalan di halaman rumah dan cari benda berwarna merah, hijau, kuning, dan biru.
mis: menyebut semua warna daun sama saja
exp: Alam punya banyak warna. Langit berwarna biru, daun berwarna hijau, matahari terlihat kuning, dan tanah berwarna cokelat. Warna-warna itu bisa kita pakai saat menggambar.
ex: Pisang matang berwarna kuning. // Daun muda berwarna hijau terang.
pt: Alam punya banyak warna ; Setiap benda punya warna khas ; Warna alam bisa dipakai saat menggambar
sum: Amati warna di alam supaya gambarmu lebih indah.
fig: table Benda alam | Warna ;; langit siang | biru ;; daun | hijau ;; pisang matang | kuning ;; tanah | cokelat ;; tomat | merah ;; awan | putih ~ Warna benda di alam.
@ Menggambar bentuk dasar
min: 8
act: Gambar rumah hanya dengan persegi, segitiga, dan lingkaran.
mis: menggambar tanpa melihat bentuk dasar benda
exp: Banyak benda bisa digambar dari bentuk dasar, yaitu lingkaran, segitiga, persegi, dan persegi panjang. Rumah dari persegi dan segitiga, matahari dari lingkaran, mobil dari persegi panjang dan lingkaran.
ex: Rumah: persegi untuk dinding, segitiga untuk atap. // Bunga: lingkaran di tengah, kelopak di sekeliling.
pt: Benda bisa digambar dari bentuk dasar ; Bentuk dasar: lingkaran, segitiga, persegi ; Gabungkan bentuk menjadi gambar
sum: Bentuk dasar membantu kita menggambar apa saja.
fig: table Gambar | Bentuk dasarnya ;; atap rumah | segitiga ;; matahari | lingkaran ;; dinding rumah | persegi ;; badan mobil | persegi panjang ;; roda | lingkaran kecil ;; layang-layang | belah ketupat ~ Gambar dari bentuk dasar.
@ Kolase dari kertas
min: 8
act: Buat kolase gambar ikan dari sobekan kertas warna-warni.
mis: menempel kertas bertumpuk terlalu tebal sehingga gambarnya tidak jelas
exp: Kolase adalah karya seni yang dibuat dengan menempelkan potongan bahan pada gambar. Bahannya bisa kertas warna, daun kering, kain perca, atau biji-bijian. Tempelkan potongan rapat-rapat mengikuti pola.
ex: Kolase ikan dari sobekan kertas warna. // Kolase pohon dari daun kering.
pt: Kolase dibuat dengan menempel potongan bahan ; Bahan bisa kertas, daun, atau biji ; Tempel rapat mengikuti pola
sum: Kolase membuat gambar menjadi bertekstur dan menarik.
fig: steps ✏️ Buat pola gambar > ✂️ Sobek kertas warna > 🧴 Oleskan lem > 🧩 Tempel rapat-rapat ~ Langkah membuat kolase.
@ Bunyi di sekitarku
min: 8
act: Tutup mata selama satu menit, lalu sebutkan semua bunyi yang kamu dengar.
mis: tidak bisa membedakan bunyi keras dan lembut
exp: Di sekitar kita ada banyak bunyi. Ada bunyi alam seperti hujan dan angin, bunyi hewan seperti kicau burung, dan bunyi benda seperti bel. Bunyi bisa keras atau lembut, cepat atau lambat.
ex: Guntur berbunyi keras. // Bisikan berbunyi lembut.
pt: Ada bunyi alam, hewan, dan benda ; Bunyi bisa keras atau lembut ; Bunyi bisa cepat atau lambat
sum: Mendengarkan bunyi melatih telinga kita peka.
fig: table Sumber bunyi | Jenis bunyi ;; guntur | keras ;; bisikan | lembut ;; kicau burung | merdu ;; bel sekolah | nyaring ;; detak jam | teratur ;; hujan rintik | pelan ~ Bunyi di sekitar kita.
@ Alat musik ritmis
min: 8
act: Buat alat musik dari botol berisi beras, lalu mainkan mengikuti lagu.
mis: memukul alat musik tidak mengikuti ketukan
exp: Alat musik ritmis adalah alat musik yang tidak bernada dan dipakai untuk mengatur irama. Contohnya gendang, rebana, tamborin, kastanyet, dan marakas. Alat musik ini dimainkan dengan dipukul, digoyang, atau dijepit.
ex: Rebana dimainkan dengan dipukul. // Marakas dimainkan dengan digoyang.
pt: Alat musik ritmis mengatur irama ; Tidak menghasilkan nada ; Dimainkan dengan dipukul atau digoyang
sum: Alat musik ritmis membuat lagu lebih bersemangat.
fig: table Alat musik | Cara memainkan ;; gendang | dipukul ;; rebana | dipukul ;; marakas | digoyang ;; tamborin | digoyang dan dipukul ;; kastanyet | dijepit ;; kentongan | dipukul dengan kayu ~ Alat musik ritmis dan cara memainkannya.
@ Lagu anak Nusantara
min: 8
act: Nyanyikan lagu Burung Kakatua atau Cublak-Cublak Suweng bersama keluarga.
mis: menyanyi terlalu keras sampai berteriak
exp: Indonesia punya banyak lagu anak dari berbagai daerah. Contohnya Cublak-Cublak Suweng dari Jawa Tengah, Ampar-Ampar Pisang dari Kalimantan Selatan, dan Burung Kakatua dari Maluku. Bernyanyi dengan suara jelas dan riang.
ex: Ampar-Ampar Pisang berasal dari Kalimantan Selatan. // Bernyanyi dengan suara merdu, tidak berteriak.
pt: Lagu anak berasal dari banyak daerah ; Kenali asal daerahnya ; Bernyanyi riang dan tidak berteriak
sum: Menyanyikan lagu daerah tanda cinta budaya Indonesia.
fig: table Lagu | Asal daerah ;; Cublak-Cublak Suweng | Jawa Tengah ;; Ampar-Ampar Pisang | Kalimantan Selatan ;; Burung Kakatua | Maluku ;; Manuk Dadali | Jawa Barat ;; Yamko Rambe Yamko | Papua ;; Kampuang Nan Jauh di Mato | Sumatra Barat ~ Lagu anak dari berbagai daerah.
# 2|Gerak dan Karya
@ Gerak menirukan hewan
min: 8
act: Tirukan gerak tiga hewan diiringi musik, lalu minta keluarga menebaknya.
mis: bergerak tanpa mengikuti irama
exp: Tari bisa dibuat dengan menirukan gerak hewan. Kita bisa melompat seperti kelinci, mengepakkan tangan seperti burung, atau berjalan pelan seperti kura-kura. Gerak dilakukan sesuai irama musik.
ex: Gerak burung: kedua tangan mengepak naik turun. // Gerak kelinci: melompat kecil dengan dua kaki.
pt: Tari bisa menirukan gerak hewan ; Setiap hewan punya gerak khas ; Bergerak sesuai irama
sum: Menirukan hewan membuat menari jadi menyenangkan.
fig: table Hewan | Gerakan ;; burung | mengepakkan tangan ;; kelinci | melompat kecil ;; kura-kura | berjalan pelan ;; gajah | mengayun tangan seperti belalai ;; ikan | meliukkan badan ;; kupu-kupu | mengepak lembut ~ Gerak tari menirukan hewan.
@ Pola lantai tari
min: 8
act: Bersama saudara, coba menari membentuk garis lurus lalu lingkaran.
mis: berdiri berdesakan sehingga pola tidak terlihat
exp: Pola lantai adalah garis yang dibentuk penari saat menari. Pola lantai bisa berupa garis lurus, lingkaran, huruf V, atau zig-zag. Penari harus menjaga jarak supaya polanya terlihat rapi.
ex: Penari berbaris lurus ke samping. // Penari bergandengan membentuk lingkaran.
pt: Pola lantai adalah garis yang dibentuk penari ; Bisa lurus, lingkaran, atau huruf V ; Jaga jarak supaya rapi
sum: Pola lantai membuat tarian terlihat indah.
fig: icons ➖ garis lurus ; ⭕ lingkaran ; ✔️ huruf V ; 〰️ zig-zag ; ⬛ persegi ; 🔺 segitiga ~ Macam-macam pola lantai tari.
@ Mencetak dengan pelepah dan daun
min: 8
act: Cetak daun dengan cat air di kertas, lalu jadikan gambar pohon.
mis: memakai cat terlalu banyak sehingga cetakan luber
exp: Mencetak adalah membuat gambar dengan menempelkan benda yang sudah diberi pewarna ke kertas. Kita bisa mencetak dengan daun, pelepah pisang, potongan sayur, atau jari. Hasil cetakan bisa disusun menjadi gambar.
ex: Cetakan daun menjadi pohon. // Cetakan jari menjadi bunga.
pt: Mencetak memakai benda yang diberi pewarna ; Bahan: daun, pelepah, sayur, atau jari ; Pakai cat secukupnya
sum: Mencetak membuat karya unik dari benda di sekitar.
fig: steps 🍃 Siapkan daun > 🎨 Oleskan cat > 📄 Tempel ke kertas > ✋ Tekan lalu angkat ~ Langkah mencetak dengan daun.
@ Membentuk dengan plastisin
min: 8
act: Buat buah-buahan dari plastisin, lalu susun di piring mainan.
mis: membiarkan plastisin terbuka sampai kering
exp: Plastisin adalah bahan lunak yang bisa dibentuk. Kita membentuk dengan cara memilin untuk membuat panjang, membulatkan untuk membuat bola, dan memipihkan untuk membuat lembaran. Setelah dipakai, simpan plastisin di wadah tertutup.
ex: Memilin plastisin menjadi ular. // Membulatkan plastisin menjadi jeruk.
pt: Plastisin bisa dibentuk ; Teknik: memilin, membulatkan, memipihkan ; Simpan di wadah tertutup
sum: Plastisin melatih jari kita membentuk karya.
fig: table Teknik | Hasil ;; memilin | bentuk panjang ;; membulatkan | bentuk bola ;; memipihkan | lembaran tipis ;; menekan | cekungan ;; menggulung | gulungan ;; mencubit | ujung lancip ~ Teknik membentuk plastisin.
@ Cepat lambat lagu
min: 8
act: Tepuk tangan cepat saat lagu ceria dan tepuk lambat saat lagu pengantar tidur.
mis: menyanyikan lagu sedih dengan tempo cepat
exp: Tempo adalah cepat atau lambatnya lagu. Lagu gembira biasanya bertempo cepat. Lagu tenang atau pengantar tidur biasanya bertempo lambat. Kita bertepuk mengikuti tempo lagu.
ex: Lagu Naik Kereta Api bertempo cepat. // Lagu Nina Bobo bertempo lambat.
pt: Tempo adalah cepat lambatnya lagu ; Lagu gembira bertempo cepat ; Lagu tenang bertempo lambat
sum: Mengikuti tempo membuat nyanyian lebih indah.
fig: compare 🏃 Cepat = Naik Kereta Api ; Balonku ; Lihat Kebunku || 🐢 Lambat = Nina Bobo ; Ibu Kita Kartini ; Bintang Kecil ~ Contoh lagu bertempo cepat dan lambat.
@ Menghias benda sederhana
min: 8
act: Hias kotak bekas menjadi tempat pensil dengan gambar dan kertas warna.
mis: membuang barang bekas yang masih bisa dihias
exp: Kita bisa menghias benda sederhana supaya lebih indah, misalnya kotak pensil, botol bekas, dan kipas kertas. Bahan hiasan bisa kertas warna, pita, manik-manik, dan gambar buatan sendiri.
ex: Botol bekas dihias menjadi pot bunga. // Kotak bekas dihias menjadi tempat pensil.
pt: Benda sederhana bisa dihias ; Pakai kertas warna, pita, dan gambar ; Barang bekas bisa dimanfaatkan
sum: Menghias benda melatih kreativitas dan mengurangi sampah.
fig: table Benda bekas | Dijadikan ;; botol plastik | pot bunga ;; kotak susu | tempat pensil ;; kardus | rumah boneka ;; tutup botol | roda mainan ;; kertas koran | topi ;; kaleng | celengan ~ Barang bekas yang bisa dihias.

## PJOK
# 1|Gerak Dasar dan Permainan
@ Berjalan maju mundur
min: 8
act: Berjalan maju lima langkah dan mundur lima langkah di halaman sambil berhitung.
mis: berjalan mundur tanpa melihat ke belakang
exp: Berjalan maju adalah melangkah ke depan dengan tumit menyentuh tanah lebih dulu. Berjalan mundur dilakukan pelan sambil sesekali menoleh agar tidak menabrak. Tangan diayun berlawanan dengan kaki.
ex: Kaki kanan maju, tangan kiri ke depan. // Saat mundur, langkah lebih pendek dan pelan.
pt: Tumit menyentuh tanah lebih dulu ; Ayun tangan berlawanan dengan kaki ; Mundur pelan dan hati-hati
sum: Berjalan dengan benar membuat tubuh seimbang.
fig: steps 🧍 Berdiri tegak > 🦶 Langkahkan kaki > 👐 Ayunkan tangan > 👀 Pandangan ke depan ~ Langkah berjalan maju yang benar.
@ Gerak keseimbangan
min: 8
act: Berdiri dengan satu kaki sambil berhitung sampai sepuluh, lalu ganti kaki.
mis: menahan napas saat berdiri satu kaki
exp: Keseimbangan adalah kemampuan menjaga tubuh supaya tidak jatuh. Latihan keseimbangan antara lain berdiri satu kaki, berjalan di atas garis lurus, dan sikap pesawat terbang. Pandangan lurus ke depan membantu tubuh seimbang.
ex: Sikap pesawat terbang: satu kaki diangkat ke belakang, kedua tangan direntangkan. // Berjalan di atas garis lurus seperti meniti.
pt: Keseimbangan menjaga tubuh tidak jatuh ; Pandangan lurus ke depan ; Bernapas biasa saat berlatih
sum: Latihan keseimbangan membuat tubuh lebih kuat dan stabil.
fig: icons 🦩 berdiri satu kaki ; ✈️ sikap pesawat terbang ; ➖ berjalan di garis lurus ; 🧘 duduk tegak ; 🌳 sikap pohon ; 🤸 berjinjit ~ Contoh gerak keseimbangan.
@ Mengayun dan memutar lengan
min: 8
act: Ayunkan lengan ke depan dan belakang sepuluh kali, lalu putar lengan ke depan sepuluh kali.
mis: memutar lengan terlalu cepat sampai bahu sakit
exp: Mengayun lengan adalah menggerakkan lengan ke depan dan ke belakang. Memutar lengan adalah menggerakkan lengan membentuk lingkaran. Gerakan ini melemaskan bahu sebelum berolahraga.
ex: Ayun kedua lengan ke depan dan belakang. // Putar lengan ke depan lalu ke belakang.
pt: Mengayun berarti ke depan dan belakang ; Memutar berarti membentuk lingkaran ; Lakukan pelan dan teratur
sum: Mengayun dan memutar lengan melemaskan tubuh.
fig: table Gerakan | Bagian tubuh ;; mengayun lengan | bahu dan lengan ;; memutar lengan | bahu ;; menekuk lutut | kaki ;; memutar pinggang | pinggang ;; menoleh | leher ;; menggeleng | kepala ~ Gerak dan bagian tubuh yang dilatih.
@ Permainan kucing dan tikus
min: 8
act: Mainkan kucing dan tikus bersama teman atau saudara di halaman.
mis: mendorong teman saat bermain
exp: Kucing dan tikus adalah permainan berlari. Pemain bergandengan membentuk lingkaran. Satu anak menjadi tikus di dalam lingkaran dan satu anak menjadi kucing di luar. Kucing berusaha menangkap tikus, sedangkan pemain lain melindungi tikus.
ex: Kucing berlari mengejar tikus. // Pemain yang bergandengan tidak boleh melepaskan tangan.
pt: Pemain membentuk lingkaran ; Kucing mengejar tikus ; Bermain sportif tanpa mendorong
sum: Permainan kucing dan tikus melatih kelincahan dan kerja sama.
fig: steps 🤝 Bentuk lingkaran > 🐭 Tikus di dalam > 🐱 Kucing di luar > 🏃 Kucing mengejar tikus ~ Cara bermain kucing dan tikus.
@ Gerak merangkak dan berguling
min: 8
act: Merangkak di atas kasur atau karpet, lalu berguling ke samping dengan hati-hati.
mis: berguling di lantai keras tanpa alas
exp: Merangkak adalah bergerak dengan kedua tangan dan lutut. Berguling ke samping adalah memutar badan di atas matras dengan tangan lurus di atas kepala. Latihan ini dilakukan di atas matras supaya aman.
ex: Merangkak maju seperti bayi. // Berguling ke samping seperti kayu menggelinding.
pt: Merangkak memakai tangan dan lutut ; Berguling ke samping di atas matras ; Selalu gunakan alas yang empuk
sum: Merangkak dan berguling melatih kekuatan dan kelenturan.
fig: steps 🧎 Posisi merangkak > 🖐️ Tangan dan lutut bergantian maju > 🛏️ Berbaring di matras > 🔄 Berguling ke samping ~ Langkah merangkak dan berguling.
@ Senam irama sederhana
min: 8
act: Ikuti senam anak dari lagu favoritmu bersama keluarga di pagi hari.
mis: bergerak tidak mengikuti hitungan
exp: Senam irama adalah senam yang diiringi musik. Gerakannya mengikuti hitungan, misalnya satu sampai delapan. Gerakan dasar senam irama antara lain langkah biasa, jalan di tempat, dan ayunan lengan.
ex: Jalan di tempat delapan hitungan. // Tepuk tangan di atas kepala empat hitungan.
pt: Senam irama diiringi musik ; Gerak mengikuti hitungan ; Gerak dasar: langkah dan ayunan lengan
sum: Senam irama menyehatkan dan menyenangkan.
fig: steps 🎵 Dengarkan musik > 🚶 Jalan di tempat > 👏 Tepuk tangan > 🙆 Ayun lengan > 🧍 Sikap akhir ~ Urutan gerak senam irama sederhana.
@ Bermain lompat tali
min: 8
act: Buat tali dari karet gelang, lalu bermain lompat tali bersama teman.
mis: melompat dengan kaki kaku sehingga mudah jatuh
exp: Lompat tali adalah permainan tradisional. Dua anak memegang tali, pemain lain melompatinya. Tinggi tali dinaikkan sedikit demi sedikit, mulai dari mata kaki sampai pinggang. Mendarat dengan lutut sedikit ditekuk supaya aman.
ex: Tali setinggi mata kaki dilompati dengan mudah. // Saat tali lebih tinggi, ambil awalan lari.
pt: Lompat tali adalah permainan tradisional ; Tinggi tali naik bertahap ; Mendarat dengan lutut ditekuk
sum: Lompat tali melatih kekuatan kaki dan keberanian.
fig: table Tinggi tali | Bagian tubuh ;; level satu | mata kaki ;; level dua | lutut ;; level tiga | paha ;; level empat | pinggang ;; level lima | dada ;; level enam | bahu ~ Tingkatan tinggi tali dalam lompat tali.
# 2|Kebugaran dan Kesehatan
@ Pemanasan sebelum olahraga
min: 8
act: Lakukan pemanasan dari kepala sampai kaki sebelum bermain sepeda.
mis: langsung berlari kencang tanpa pemanasan
exp: Pemanasan dilakukan sebelum berolahraga supaya otot siap dan tidak cedera. Pemanasan dimulai dari kepala, bahu, pinggang, lutut, sampai pergelangan kaki. Gerakannya pelan dan teratur.
ex: Menoleh ke kanan dan kiri. // Memutar pergelangan kaki.
pt: Pemanasan mencegah cedera ; Mulai dari kepala sampai kaki ; Lakukan pelan dan teratur
sum: Selalu lakukan pemanasan sebelum berolahraga.
fig: steps 🙆 Gerakan kepala > 💪 Putar bahu > 🔄 Putar pinggang > 🦵 Tekuk lutut > 🦶 Putar pergelangan kaki ~ Urutan pemanasan dari atas ke bawah.
@ Pendinginan setelah olahraga
min: 8
act: Setelah bermain, lakukan peregangan dan tarik napas dalam bersama keluarga.
mis: langsung duduk diam setelah berlari kencang
exp: Pendinginan dilakukan setelah olahraga supaya detak jantung dan napas kembali normal. Gerakannya pelan, seperti berjalan santai, meregangkan otot, dan menarik napas dalam.
ex: Berjalan pelan keliling lapangan. // Tarik napas lewat hidung, buang lewat mulut.
pt: Pendinginan setelah olahraga ; Membuat napas kembali normal ; Gerakan pelan dan santai
sum: Pendinginan membantu tubuh beristirahat dengan baik.
fig: steps 🚶 Jalan santai > 🙆 Regangkan otot > 🌬️ Tarik napas dalam > 🧘 Duduk rileks ~ Langkah pendinginan setelah olahraga.
@ Makanan sehat untuk tubuh
min: 8
act: Bantu Ibu menyiapkan bekal sehat berisi nasi, lauk, sayur, dan buah.
mis: lebih sering jajan makanan manis daripada makan sayur
exp: Makanan sehat membuat tubuh kuat dan tidak mudah sakit. Makanan sehat terdiri atas nasi atau makanan pokok, lauk pauk, sayur, buah, dan air putih. Kurangi makanan terlalu manis dan berminyak.
ex: Nasi memberi tenaga. // Sayur dan buah membuat tubuh sehat. // Ikan dan telur membantu tubuh tumbuh.
pt: Makanan sehat membuat tubuh kuat ; Ada makanan pokok, lauk, sayur, dan buah ; Kurangi makanan manis dan berminyak
sum: Makan beragam makanan sehat setiap hari.
fig: table Makanan | Gunanya ;; nasi | memberi tenaga ;; ikan | membantu tumbuh ;; telur | membantu tumbuh ;; bayam | menyehatkan tubuh ;; jeruk | menjaga daya tahan ;; air putih | mencegah haus ~ Makanan sehat dan gunanya.
@ Menjaga kebersihan gigi
min: 8
act: Sikat gigi pagi dan malam sebelum tidur selama dua menit dengan bimbingan orang tua.
mis: menyikat gigi terlalu keras atau terlalu sebentar
exp: Gigi harus dijaga supaya tidak berlubang. Sikat gigi minimal dua kali sehari, yaitu pagi setelah sarapan dan malam sebelum tidur. Gunakan pasta gigi secukupnya dan sikat dengan gerakan memutar.
ex: Sikat gigi pagi setelah sarapan. // Sikat gigi malam sebelum tidur.
pt: Sikat gigi dua kali sehari ; Gerakan memutar dan pelan ; Kurangi makanan manis
sum: Gigi bersih membuat senyum sehat.
fig: steps 🪥 Beri pasta gigi > 🔄 Sikat memutar > 👅 Bersihkan lidah > 💧 Berkumur > 😁 Gigi bersih ~ Langkah menyikat gigi yang benar.
@ Istirahat dan tidur cukup
min: 8
act: Buat jadwal tidur dan bangun yang sama setiap hari.
mis: bermain gawai sampai larut malam
exp: Tubuh perlu istirahat supaya segar. Anak seusiamu perlu tidur sekitar sepuluh jam setiap malam. Sebelum tidur, matikan gawai, cuci kaki, gosok gigi, dan berdoa.
ex: Tidur pukul 8 malam, bangun pukul 5 pagi. // Tidak bermain gawai sebelum tidur.
pt: Tidur cukup membuat tubuh segar ; Anak perlu tidur sekitar sepuluh jam ; Matikan gawai sebelum tidur
sum: Tidur cukup membuat kita semangat belajar.
fig: steps 📵 Matikan gawai > 🦶 Cuci kaki > 🪥 Gosok gigi > 🤲 Berdoa > 😴 Tidur ~ Kebiasaan sebelum tidur.
@ Bermain bola kecil
min: 8
act: Lempar bola kecil ke dinding dan tangkap kembali sepuluh kali.
mis: menangkap bola dengan tangan kaku
exp: Bola kecil seperti bola kasti atau bola tenis bisa dimainkan dengan dilempar, ditangkap, dan digelindingkan. Saat menangkap, mata melihat bola dan kedua tangan siap menangkap dengan lentur.
ex: Melempar bola ke teman dari bawah. // Menangkap bola dengan dua tangan.
pt: Bola kecil bisa dilempar, ditangkap, dan digelindingkan ; Mata selalu melihat bola ; Tangan lentur saat menangkap
sum: Bermain bola kecil melatih kerja sama mata dan tangan.
fig: table Gerakan | Cara ;; melempar bawah | ayun tangan dari bawah ;; melempar atas | ayun tangan dari atas kepala ;; menangkap | kedua tangan terbuka ;; menggelindingkan | dorong bola di lantai ;; memantulkan | lempar ke lantai ;; menggiring | dorong bola dengan kaki ~ Gerakan bermain bola kecil.
@ Aman saat bermain
min: 8
act: Bersama orang tua, periksa halaman tempat bermain dan singkirkan benda tajam.
mis: bermain di dekat jalan raya
exp: Kita harus bermain dengan aman. Pilih tempat bermain yang jauh dari jalan raya, tidak licin, dan bebas benda tajam. Pakai sepatu yang tepat dan ikuti aturan permainan. Jika ada teman terluka, segera beri tahu orang dewasa.
ex: Bermain di halaman, bukan di jalan. // Melepas jam tangan sebelum bermain bola.
pt: Pilih tempat bermain yang aman ; Pakai perlengkapan yang tepat ; Beri tahu orang dewasa jika ada yang terluka
sum: Bermain aman membuat semua tetap senang dan sehat.
fig: compare ✅ Aman = halaman rumah ; lapangan sekolah ; taman bermain || ⛔ Berbahaya = jalan raya ; lantai licin ; dekat kolam dalam ~ Tempat bermain yang aman dan berbahaya.

## PAI
# 1|Huruf Hijaiyah dan Harakat
@ Huruf hijaiyah alif sampai kha
min: 8
act: Tunjuk huruf alif sampai kha di papan huruf, lalu tirukan bacaan ustaz atau orang tua.
mis: tertukar bentuk huruf ba, ta, dan tsa
exp: Huruf hijaiyah adalah huruf Al-Qur'an. Huruf pertama sampai ketujuh adalah alif, ba, ta, tsa, jim, ḥa, dan kha. Ba, ta, dan tsa bentuknya mirip, bedanya pada jumlah dan letak titik. Ba bertitik satu di bawah, ta bertitik dua di atas, tsa bertitik tiga di atas.
ex: Ba titiknya satu di bawah. // Ta titiknya dua di atas. // Tsa titiknya tiga di atas.
pt: Huruf hijaiyah adalah huruf Al-Qur'an ; Ba, ta, tsa dibedakan dari titiknya ; Jim, ḥa, kha dibedakan dari titiknya juga
sum: Kenali bentuk dan titik setiap huruf supaya tidak tertukar.
fig: hijaiyah huruf ; ا ب ت ث ج ح خ ~ Ketuk huruf untuk mendengar bacaannya.
@ Huruf hijaiyah dal sampai dhad
min: 8
act: Tulis huruf dal sampai dhad dengan jari di atas pasir atau tepung.
mis: tertukar huruf sin dan syin
exp: Huruf berikutnya adalah dal, dzal, ra, zai, sin, syin, shad, dan dhad. Dal tanpa titik, dzal bertitik satu. Ra tanpa titik, zai bertitik satu. Sin tanpa titik, syin bertitik tiga. Shad tanpa titik, dhad bertitik satu.
ex: Dzal seperti dal ditambah satu titik. // Syin seperti sin ditambah tiga titik.
pt: Dal dan dzal dibedakan satu titik ; Ra dan zai dibedakan satu titik ; Sin dan syin dibedakan tiga titik
sum: Perhatikan titik untuk membedakan huruf yang mirip.
fig: hijaiyah huruf ; د ذ ر ز س ش ص ض ~ Ketuk huruf untuk mendengar bacaannya.
@ Huruf hijaiyah tha sampai qaf
min: 8
act: Buat kartu huruf tha sampai qaf, lalu bermain mencocokkan kartu bersama keluarga.
mis: tertukar huruf fa dan qaf
exp: Huruf berikutnya adalah tha, zha, 'ain, ghain, fa, dan qaf. Tha tanpa titik, zha bertitik satu. 'Ain tanpa titik, ghain bertitik satu. Fa bertitik satu di atas, qaf bertitik dua di atas.
ex: Zha seperti tha ditambah satu titik. // Qaf titiknya dua, fa titiknya satu.
pt: Tha dan zha dibedakan satu titik ; 'Ain dan ghain dibedakan satu titik ; Fa bertitik satu, qaf bertitik dua
sum: Huruf tha sampai qaf punya pasangan yang mirip.
fig: hijaiyah huruf ; ط ظ ع غ ف ق ~ Ketuk huruf untuk mendengar bacaannya.
@ Huruf hijaiyah kaf sampai ya
min: 8
act: Nyanyikan urutan huruf hijaiyah dari alif sampai ya bersama orang tua.
mis: lupa urutan huruf setelah lam
exp: Huruf terakhir adalah kaf, lam, mim, nun, wau, ha, lam alif, hamzah, dan ya. Nun bertitik satu di atas, ya bertitik dua di bawah. Lam alif adalah gabungan lam dan alif. Semuanya ada 30 huruf jika lam alif dan hamzah dihitung.
ex: Nun titiknya satu di atas. // Ya titiknya dua di bawah.
pt: Kaf, lam, mim, nun, wau, ha, lam alif, hamzah, ya ; Nun bertitik satu di atas ; Ya bertitik dua di bawah
sum: Hafalkan urutan huruf hijaiyah dari alif sampai ya.
fig: hijaiyah huruf ; ك ل م ن و ه لا ء ي ~ Ketuk huruf untuk mendengar bacaannya.
@ Harakat fathah
min: 8
act: Baca huruf berharakat fathah satu per satu, lalu dengarkan rekaman ustaz atau orang tua.
mis: membaca fathah dengan bunyi i
exp: Harakat adalah tanda baca pada huruf hijaiyah. Fathah adalah garis kecil miring di atas huruf. Huruf berharakat fathah dibaca dengan bunyi a, misalnya ba, ta, tsa.
ex: Ba dengan fathah dibaca ba. // Mim dengan fathah dibaca ma.
pt: Harakat adalah tanda baca ; Fathah ada di atas huruf ; Fathah dibaca a
sum: Fathah membuat huruf dibaca dengan bunyi a.
fig: hijaiyah fathah ; ا ب ت ث ج ح خ د ~ Ketuk huruf berharakat fathah untuk mendengar bacaannya.
@ Harakat kasrah
min: 8
act: Tunjuk huruf berharakat kasrah di buku Iqro, lalu baca bersama orang tua.
mis: menulis kasrah di atas huruf
exp: Kasrah adalah garis kecil miring di bawah huruf. Huruf berharakat kasrah dibaca dengan bunyi i, misalnya bi, ti, tsi.
ex: Ba dengan kasrah dibaca bi. // Lam dengan kasrah dibaca li.
pt: Kasrah ada di bawah huruf ; Kasrah dibaca i ; Bedakan letak fathah dan kasrah
sum: Kasrah membuat huruf dibaca dengan bunyi i.
fig: hijaiyah kasrah ; ب ت ث ج ر ز س ش ~ Ketuk huruf berharakat kasrah untuk mendengar bacaannya.
# 2|Harakat, Ibadah, dan Akhlak
@ Harakat dammah
min: 8
act: Baca huruf berharakat dammah, lalu buat kartu fathah, kasrah, dan dammah.
mis: tertukar dammah dengan fathah
exp: Dammah adalah tanda seperti huruf wau kecil di atas huruf. Huruf berharakat dammah dibaca dengan bunyi u, misalnya bu, tu, tsu.
ex: Ba dengan dammah dibaca bu. // Nun dengan dammah dibaca nu.
pt: Dammah seperti wau kecil di atas huruf ; Dammah dibaca u ; Fathah a, kasrah i, dammah u
sum: Dammah membuat huruf dibaca dengan bunyi u.
fig: hijaiyah dammah ; ف ق ك ل م ن و ي ~ Ketuk huruf berharakat dammah untuk mendengar bacaannya.
@ Tanwin
min: 8
act: Cari tanda tanwin di buku Iqro, lalu baca dengan bimbingan orang tua.
mis: membaca tanwin seperti harakat biasa tanpa bunyi n
exp: Tanwin adalah harakat ganda. Fathatain dibaca an, kasratain dibaca in, dan dammatain dibaca un. Contohnya ba dengan fathatain dibaca ban.
ex: Fathatain dibaca an. // Kasratain dibaca in. // Dammatain dibaca un.
pt: Tanwin adalah harakat ganda ; Fathatain an, kasratain in, dammatain un ; Tanwin menambah bunyi n
sum: Tanwin membuat bacaan berakhir dengan bunyi n.
fig: hijaiyah fathatain ; ب ت ج د ر س ~ Ketuk huruf bertanwin untuk mendengar bacaannya.
@ Doa sebelum dan sesudah belajar
min: 8
act: Biasakan berdoa sebelum belajar dan sesudah belajar di rumah.
mis: lupa berdoa karena terburu-buru
exp: Sebelum belajar kita berdoa supaya ilmunya mudah dipahami dan bermanfaat. Sesudah belajar kita bersyukur kepada Allah. Doa dibaca dengan tenang dan sungguh-sungguh.
ex: Minta Ayah, Bunda, atau ustaz merekam bacaan doanya pada kartu doa. // Berdoa dengan tangan menengadah dan hati tenang.
pt: Berdoa sebelum belajar ; Bersyukur sesudah belajar ; Berdoa dengan tenang
sum: Belajar diawali dan diakhiri dengan doa.
fig: steps 🤲 Berdoa sebelum belajar > 📖 Belajar dengan sungguh-sungguh > 🙏 Bersyukur sesudah belajar > 🎒 Merapikan buku ~ Kebiasaan belajar seorang muslim.
read: doa Doa sebelum belajar | Rabbi zidnī 'ilman warzuqnī fahmā | Ya Tuhanku, tambahkanlah ilmuku dan berilah aku pemahaman
@ Adab makan dan minum
min: 8
act: Praktikkan adab makan: berdoa, memakai tangan kanan, dan duduk saat makan bersama keluarga.
mis: makan sambil berjalan atau memakai tangan kiri
exp: Islam mengajarkan adab makan dan minum. Kita mencuci tangan, membaca basmalah, makan dengan tangan kanan, duduk, tidak berlebihan, dan berdoa setelah makan.
ex: Membaca basmalah sebelum makan. // Makan dan minum dengan tangan kanan sambil duduk.
pt: Cuci tangan dan baca basmalah ; Makan dengan tangan kanan sambil duduk ; Berdoa setelah makan
sum: Adab makan membuat makan menjadi berkah.
fig: steps 🧼 Cuci tangan > 🤲 Baca basmalah > 🍽️ Makan dengan tangan kanan > 🪑 Duduk dengan sopan > 🙏 Berdoa setelah makan ~ Urutan adab makan dan minum.
@ Salat lima waktu
min: 8
act: Buat tabel salat lima waktu dan centang setiap kali kamu ikut salat.
mis: tertukar urutan salat asar dan magrib
exp: Muslim wajib salat lima kali sehari. Salat subuh dilakukan pagi sebelum matahari terbit, zuhur siang hari, asar sore hari, magrib saat matahari terbenam, dan isya malam hari.
ex: Subuh dikerjakan dua rakaat. // Magrib dikerjakan tiga rakaat.
pt: Salat wajib lima waktu ; Subuh, zuhur, asar, magrib, isya ; Setiap salat punya waktu sendiri
sum: Salat lima waktu adalah kewajiban setiap muslim.
fig: table Salat | Jumlah rakaat ;; subuh | dua ;; zuhur | empat ;; asar | empat ;; magrib | tiga ;; isya | empat ;; jumat | dua ~ Salat wajib dan jumlah rakaatnya.
@ Kisah Nabi Nuh
min: 8
act: Ceritakan kembali kisah Nabi Nuh dan kapalnya kepada keluarga.
mis: mengira kaum Nabi Nuh semuanya ikut naik kapal
exp: Nabi Nuh mengajak kaumnya menyembah Allah, tetapi banyak yang menolak dan mengejeknya. Allah memerintahkan Nabi Nuh membuat kapal besar. Ketika banjir besar datang, orang-orang beriman dan hewan berpasangan selamat di dalam kapal.
ex: Nabi Nuh tetap sabar walaupun diejek. // Orang beriman selamat di kapal.
pt: Nabi Nuh mengajak kaumnya menyembah Allah ; Allah memerintahkan membuat kapal ; Orang beriman selamat dari banjir
sum: Kisah Nabi Nuh mengajarkan sabar dan taat kepada Allah.
fig: time awal = Nabi Nuh berdakwah ; kemudian = kaumnya mengejek ; lalu = membuat kapal besar ; akhirnya = banjir datang dan orang beriman selamat ~ Urutan kisah Nabi Nuh.

## SUN
# 1|Sapopoé di Imah jeung Sakola
@ Pakakas di sakola
min: 8
act: Sebutkan pakakas sakola dina basa Sunda bari nunjuk barangna di imah.
mis: menyebut alat tulis dengan bahasa Indonesia saja
exp: Di sekolah ada banyak alat yang dalam bahasa Sunda disebut pakakas sakola. Contohnya buku, patlot atau pensil, pamupus atau penghapus, panggaris atau penggaris, jeung tas. Kita belajar menyebut nama benda itu dalam bahasa Sunda.
ex: Patlot dipaké nulis. // Pamupus dipaké mupus tulisan.
pt: Patlot artinya pensil ; Pamupus artinya penghapus ; Panggaris artinya penggaris
sum: Kenali nama pakakas sakola dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; patlot | pensil ;; pamupus | penghapus ;; panggaris | penggaris ;; buku | buku ;; méja | meja ;; korsi | kursi ~ Nama pakakas sakola dalam bahasa Sunda.
@ Ngaran poé
min: 8
act: Sebutkeun ngaran poé ti Senén nepi ka Minggu dina basa Sunda.
mis: menyebut hari dengan bahasa Indonesia
exp: Dalam bahasa Sunda, nama hari adalah Senén, Salasa, Rebo, Kemis, Jumaah, Saptu, jeung Minggu. Poé artinya hari. Urutannya sama dengan bahasa Indonesia.
ex: Poé Rebo urang sakola. // Poé Minggu urang pakansi.
pt: Poé artinya hari ; Senén, Salasa, Rebo, Kemis ; Jumaah, Saptu, Minggu
sum: Hafalkan ngaran poé dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; Senén | Senin ;; Salasa | Selasa ;; Rebo | Rabu ;; Kemis | Kamis ;; Jumaah | Jumat ;; Saptu | Sabtu ~ Ngaran poé dalam bahasa Sunda.
@ Kadaharan jeung inuman
min: 8
act: Sebutkan makanan dan minuman di meja makan dalam bahasa Sunda.
mis: tertukar kata dahar dan nginum
exp: Kadaharan artinya makanan dan inuman artinya minuman. Dahar artinya makan dan nginum artinya minum. Contoh kadaharan: sangu atau nasi, lauk, sayur. Contoh inuman: cai atau air, susu, jeung entéh.
ex: Abdi dahar sangu. // Adi nginum cai.
pt: Dahar artinya makan ; Nginum artinya minum ; Sangu artinya nasi dan cai artinya air
sum: Kenali nama makanan dan minuman dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; sangu | nasi ;; cai | air ;; dahar | makan ;; nginum | minum ;; entéh | teh ;; bubur | bubur ~ Kecap kadaharan jeung inuman.
@ Bagian imah
min: 8
act: Ajak keluarga berkeliling rumah sambil menyebut nama ruangan dalam bahasa Sunda.
mis: menyebut dapur dengan kata lain
exp: Imah artinya rumah. Bagian imah antara lain tepas atau ruang tamu, kamar, dapur, kamar mandi, jeung buruan atau halaman. Panto artinya pintu dan jandéla artinya jendela.
ex: Indung masak di dapur. // Barudak ulin di buruan.
pt: Imah artinya rumah ; Tepas artinya ruang tamu ; Buruan artinya halaman
sum: Kenali nama bagian rumah dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; imah | rumah ;; tepas | ruang tamu ;; buruan | halaman ;; panto | pintu ;; jandéla | jendela ;; hateup | atap ~ Kecap bagian imah.
@ Kecap sopan ka kolot
min: 8
act: Ucapkan punten, mangga, jeung hatur nuhun ka kolot dina kahirupan sapopoé.
mis: berbicara kepada orang tua dengan kata kasar
exp: Dalam bahasa Sunda ada kata sopan untuk orang yang lebih tua. Punten diucapkan saat permisi, mangga saat mempersilakan, dan hatur nuhun saat berterima kasih. Abdi dipakai untuk menyebut diri sendiri dengan sopan.
ex: Punten, abdi badé ngaliwat. // Hatur nuhun, Bu.
pt: Punten untuk permisi ; Mangga untuk mempersilakan ; Hatur nuhun untuk berterima kasih
sum: Gunakan kata sopan saat berbicara kepada orang yang lebih tua.
fig: table Kecap | Dipakéna ;; punten | permisi ;; mangga | mempersilakan ;; hatur nuhun | berterima kasih ;; abdi | menyebut diri sendiri ;; sumuhun | menjawab ya ;; wilujeng énjing | selamat pagi ~ Kecap sopan dina basa Sunda.
@ Pakéan sapopoé
min: 8
act: Sebutkan pakaian yang sedang kamu pakai dalam bahasa Sunda.
mis: menyebut sendal dengan kata yang salah
exp: Pakéan artinya pakaian. Contoh pakéan sapopoé adalah baju, calana, rok, kaos kaki, sapatu, jeung topi. Kita memakai pakaian yang bersih dan rapi.
ex: Abdi maké baju bodas. // Sapatu dipaké ka sakola.
pt: Pakéan artinya pakaian ; Calana artinya celana ; Sapatu artinya sepatu
sum: Kenali nama pakaian dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; pakéan | pakaian ;; calana | celana ;; sapatu | sepatu ;; kaos kaki | kaus kaki ;; topi | topi ;; samping | kain sarung ~ Ngaran pakéan sapopoé.
# 2|Alam jeung Kabiasaan
@ Kembang jeung tatangkalan
min: 8
act: Sebutkan bunga dan tanaman di halaman rumah dalam bahasa Sunda.
mis: menyebut semua tumbuhan sebagai kembang
exp: Kembang artinya bunga dan tangkal artinya pohon. Contoh kembang: mawar, malati, jeung hampelas. Contoh tangkal: tangkal cau atau pohon pisang, tangkal kalapa, jeung tangkal mangga.
ex: Kembang mawar warnana beureum. // Tangkal kalapa jangkung pisan.
pt: Kembang artinya bunga ; Tangkal artinya pohon ; Cau artinya pisang
sum: Kenali nama bunga dan pohon dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; kembang | bunga ;; tangkal | pohon ;; cau | pisang ;; kalapa | kelapa ;; malati | melati ;; daun | daun ~ Kecap kembang jeung tatangkalan.
@ Cuaca
min: 8
act: Lihat langit hari ini lalu ucapkan keadaan cuaca dalam bahasa Sunda.
mis: tertukar kata panas dan tiris
exp: Keadaan cuaca dalam bahasa Sunda antara lain panas, hujan, tiris atau dingin, jeung angin. Langit artinya langit dan méga artinya awan. Saat hujan, kita memakai payung.
ex: Poé ieu panas pisan. // Ayeuna hujan, urang maké payung.
pt: Tiris artinya dingin ; Méga artinya awan ; Hujan dan panas sama dengan bahasa Indonesia
sum: Kenali kata cuaca dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; tiris | dingin ;; méga | awan ;; hujan | hujan ;; panas | panas ;; angin | angin ;; gelap | gelap ~ Kecap cuaca dina basa Sunda.
@ Kagiatan isuk-isuk
min: 8
act: Ceritakan kegiatan pagimu dalam bahasa Sunda dari bangun sampai berangkat sekolah.
mis: menyebut urutan kegiatan pagi yang terbalik
exp: Isuk-isuk artinya pagi hari. Kegiatan pagi antara lain hudang atau bangun, mandi, solat, sarapan, jeung indit ka sakola. Kita melakukan kegiatan pagi dengan urut supaya tidak terlambat.
ex: Abdi hudang isuk-isuk. // Saréngséna mandi, abdi sarapan.
pt: Isuk-isuk artinya pagi ; Hudang artinya bangun ; Indit artinya berangkat
sum: Ceritakan kegiatan pagi dengan urut dalam bahasa Sunda.
fig: steps 🛏️ Hudang > 🛁 Mandi > 🤲 Solat > 🍚 Sarapan > 🎒 Indit ka sakola ~ Kagiatan isuk-isuk.
@ Sato di kebon binatang
min: 8
act: Sebutkan hewan yang pernah kamu lihat di kebun binatang dalam bahasa Sunda.
mis: menyebut monyet dengan kata yang tidak tepat
exp: Di kebon binatang ada banyak sato atau hewan. Contohnya gajah, maung atau harimau, monyét, oray atau ular, jeung manuk atau burung. Kita melihat hewan tanpa mengganggunya.
ex: Maung téh galak. // Manuk hiber di langit.
pt: Sato artinya hewan ; Maung artinya harimau ; Oray artinya ular dan manuk artinya burung
sum: Kenali nama hewan dalam bahasa Sunda.
fig: table Basa Sunda | Basa Indonesia ;; maung | harimau ;; oray | ular ;; manuk | burung ;; monyét | monyet ;; gajah | gajah ;; lauk | ikan ~ Ngaran sato dina basa Sunda.
@ Wilangan sabelas nepi ka dua puluh
min: 8
act: Hitung kelereng dari sabelas sampai dua puluh dalam bahasa Sunda.
mis: menyebut sabelas sebagai sapuluh hiji
exp: Setelah sapuluh, bilangan dalam bahasa Sunda adalah sabelas, dua belas, tilu belas, opat belas, lima belas, genep belas, tujuh belas, dalapan belas, salapan belas, jeung dua puluh.
ex: Sabelas artinya sebelas. // Tilu belas artinya tiga belas.
pt: Sabelas artinya sebelas ; Tilu belas artinya tiga belas ; Genep belas artinya enam belas
sum: Hitung sampai dua puluh dalam bahasa Sunda.
fig: table Basa Sunda | Angka ;; sabelas | 11 ;; tilu belas | 13 ;; opat belas | 14 ;; genep belas | 16 ;; dalapan belas | 18 ;; salapan belas | 19 ~ Wilangan dina basa Sunda.
@ Babasan pondok
min: 8
act: Tanyakan kepada kakek atau nenek babasan Sunda yang mereka tahu.
mis: mengartikan babasan kata per kata
exp: Babasan adalah ungkapan Sunda yang artinya bukan arti kata sebenarnya. Contohnya gedé hulu artinya sombong, panjang leungeun artinya suka mencuri, dan hampang birit artinya rajin. Babasan dipakai supaya bahasa lebih halus.
ex: Budak éta hampang birit, artinya anak itu rajin. // Ulah gedé hulu, artinya jangan sombong.
pt: Babasan adalah ungkapan Sunda ; Artinya bukan arti kata sebenarnya ; Contoh: hampang birit artinya rajin
sum: Babasan memperindah bahasa Sunda.
fig: table Babasan | Hartina ;; gedé hulu | sombong ;; hampang birit | rajin ;; panjang leungeun | suka mencuri ;; gedé haté | sabar ;; hampang leungeun | ringan tangan memukul ;; leutik haté | penakut ~ Conto babasan jeung hartina.
"""

BANK = """
## BIN|Membaca huruf kapital dan huruf kecil
Huruf kapital dipakai di awal …|kalimat|kata kedua|tengah kalimat|akhir kalimat|Huruf kapital di awal kalimat.
Penulisan nama orang yang benar adalah …|Rina|rina|rINA|riNa|Nama orang diawali huruf kapital.
Nama kota yang ditulis dengan benar adalah …|Bandung|bandung|bANDUNG|banDung|Nama kota diawali huruf kapital.
B|Nama hari diawali huruf kapital, misalnya Senin.|Nama hari ditulis dengan huruf kapital di awal.
S|Huruf kapital hanya dipakai di akhir kalimat.|Huruf kapital dipakai di awal kalimat dan nama.
=|Huruf kecil dari huruf B adalah …|b|Huruf kecil B adalah b.
Kalimat yang ditulis dengan benar adalah …|Adik makan nasi.|adik makan nasi.|Adik makan nasi|adik Makan nasi.|Diawali huruf kapital dan diakhiri titik.
Huruf kapital dari huruf e adalah …|E|e|F|É|Huruf kapital e adalah E.
## BIN|Kata benda di rumahku
Benda untuk tempat duduk adalah …|kursi|piring|sapu|bantal|Kursi untuk duduk.
Benda untuk menyimpan pakaian adalah …|lemari|gelas|kompor|ember|Lemari untuk menyimpan pakaian.
Kata berikut yang merupakan nama benda adalah …|meja|berlari|makan|tidur|Meja adalah nama benda.
B|Piring dipakai sebagai tempat makanan.|Piring tempat makanan.
S|Sapu dipakai untuk tempat minum.|Sapu untuk membersihkan lantai.
=|Benda untuk alas kepala saat tidur disebut …|bantal|Bantal untuk alas kepala.
Benda untuk memasak di dapur adalah …|kompor|bantal|lemari|kursi|Kompor untuk memasak.
Kata benda adalah kata yang menunjukkan …|nama benda|kegiatan|keadaan|perasaan|Kata benda adalah nama benda.
## BIN|Kata kerja sehari-hari
Kata berikut yang termasuk kata kerja adalah …|berlari|meja|merah|besar|Berlari adalah kegiatan.
Kakak sedang … buku cerita.|membaca|meja|bersih|tinggi|Membaca adalah kata kerja.
Kegiatan membersihkan badan dengan air disebut …|mandi|makan|tidur|menulis|Mandi membersihkan badan.
B|Menulis termasuk kata kerja.|Menulis adalah kegiatan.
S|Kursi termasuk kata kerja.|Kursi adalah kata benda.
=|Ibu … di dapur menyiapkan makan siang.|memasak;masak|Memasak adalah kegiatan di dapur.
Kata kerja menjawab pertanyaan …|sedang apa|di mana|berapa|warna apa|Kata kerja menjawab sedang apa.
Adik … susu sebelum tidur.|minum|meja|manis|besar|Minum adalah kata kerja.
## BIN|Menyusun kata menjadi kalimat
Susunan kata yang benar adalah …|Ayah membaca koran.|Koran ayah membaca.|Membaca koran ayah.|Ayah koran membaca.|Subjek, kegiatan, lalu benda.
Kalimat diakhiri dengan tanda …|titik|koma|kurung|petik|Kalimat berita diakhiri titik.
Kata pergi, ke, Ani, sekolah disusun menjadi …|Ani pergi ke sekolah.|Sekolah ke pergi Ani.|Pergi Ani sekolah ke.|Ke sekolah Ani pergi.|Ani pergi ke sekolah.
B|Kalimat diawali huruf kapital.|Awal kalimat memakai huruf kapital.
S|Kalimat tidak perlu disusun dengan urutan yang benar.|Urutan kata menentukan arti.
=|Kata adik, bola, bermain disusun menjadi Adik bermain …|bola|Adik bermain bola.
Kalimat adalah susunan kata yang …|punya arti|acak|tidak bermakna|hanya satu huruf|Kalimat punya arti.
Kalimat yang lengkap adalah …|Sinta menyiram bunga.|Sinta menyiram.|Menyiram bunga.|Bunga Sinta.|Kalimat lengkap: siapa, melakukan apa.
## BIN|Huruf ganda ng dan ny
Kata yang memakai huruf ng adalah …|bunga|nyamuk|buku|meja|Bunga memakai ng.
Kata yang memakai huruf ny adalah …|nyanyi|bunga|piring|kancing|Nyanyi memakai ny.
Huruf ng dan ny dibaca …|menjadi satu bunyi|terpisah dua bunyi|tidak dibaca|seperti huruf a|Huruf ganda dibaca satu bunyi.
B|Kata piring memakai huruf ng.|Pi-ring berakhir dengan ng.
S|Kata buku memakai huruf ny.|Buku tidak memakai huruf ganda.
=|Hewan kecil yang suka menggigit dan memakai huruf ny adalah …|nyamuk|Nyamuk memakai ny.
Suku kata pertama kata nyanyi adalah …|nya|nyi|na|ya|Nya-nyi.
Kata yang memakai ng di akhir adalah …|kancing|nyala|bunga|banyak|Kan-cing berakhir ng.
## BIN|Membaca puisi anak
Puisi disusun dalam bentuk …|baris-baris|kolom angka|tabel|gambar saja|Puisi disusun dalam baris.
Saat membaca puisi, suara harus …|jelas|berbisik|berteriak|terlalu cepat|Suara jelas saat membaca puisi.
Setiap baris puisi sebaiknya diberi …|jeda sebentar|tanda tambah|angka|warna|Beri jeda tiap baris.
B|Membaca puisi memakai ekspresi sesuai isinya.|Ekspresi membuat puisi hidup.
S|Puisi dibaca secepat mungkin.|Puisi dibaca tidak terburu-buru.
=|Karangan yang disusun dalam baris-baris dengan kata indah disebut …|puisi|Puisi.
Puisi tentang ibu sebaiknya dibaca dengan ekspresi …|penuh kasih sayang|marah|takut|bosan|Sesuai isi puisi.
Sebelum membacakan puisi, sebaiknya kita …|membacanya dalam hati dulu|langsung berteriak|menutup buku|tidur|Baca dalam hati dulu.
## BIN|Kalimat perintah dan ajakan
Kalimat ajakan biasanya memakai kata …|ayo|tolong|jangan|siapa|Ayo atau mari untuk ajakan.
Kalimat perintah yang sopan memakai kata …|tolong|ayo|mari|mengapa|Tolong membuat perintah sopan.
Kalimat ajakan adalah …|Mari kita belajar bersama.|Tolong tutup pintunya.|Siapa namamu?|Adik sedang tidur.|Mari menunjukkan ajakan.
B|Tolong ambilkan buku itu termasuk kalimat perintah.|Meminta orang melakukan sesuatu.
S|Ayo kita bermain termasuk kalimat tanya.|Itu kalimat ajakan.
=|… kita membuang sampah pada tempatnya. (kata ajakan)|Ayo;Mari|Ayo atau mari.
Kalimat perintah meminta orang lain …|melakukan sesuatu|menjawab pertanyaan|bercerita|tertawa|Perintah meminta melakukan sesuatu.
Kalimat ajakan mengajak orang lain …|melakukan bersama-sama|diam|pergi sendiri|marah|Ajakan untuk bersama-sama.
## BIN|Menceritakan gambar
Saat menceritakan gambar, kita perlu melihat …|siapa, di mana, dan sedang apa|warna kertas saja|harga buku|nomor halaman|Tiga hal penting.
Gambar anak menyiram bunga di taman. Kegiatannya adalah …|menyiram bunga|tidur|makan|berenang|Menyiram bunga.
Cerita gambar sebaiknya disusun …|urut|acak|terbalik|dengan satu kata|Cerita disusun urut.
B|Menceritakan gambar melatih kita berbicara runtut.|Runtut artinya urut.
S|Menceritakan gambar cukup dengan menyebut warna.|Ceritakan siapa, di mana, dan kegiatannya.
=|Pertanyaan untuk mengetahui tempat adalah …|di mana;dimana|Di mana menanyakan tempat.
Pertanyaan untuk mengetahui pelaku adalah …|siapa|kapan|berapa|mengapa|Siapa menanyakan pelaku.
Pertanyaan untuk mengetahui waktu adalah …|kapan|siapa|di mana|apa|Kapan menanyakan waktu.
## BIN|Kosakata anggota keluarga
Ayah dari ibu disebut …|kakek|paman|kakak|adik|Ayah dari ibu adalah kakek.
Saudara perempuan ibu disebut …|bibi|nenek|kakak|adik|Saudara perempuan orang tua adalah bibi.
Saudara yang lebih muda disebut …|adik|kakak|paman|kakek|Adik lebih muda.
B|Ibu dari ayah disebut nenek.|Nenek adalah ibu dari ayah atau ibu.
S|Paman adalah ayah dari ayah.|Ayah dari ayah adalah kakek.
=|Saudara laki-laki ayah disebut …|paman|Paman.
Keluarga inti terdiri atas …|ayah, ibu, dan anak|kakek dan tetangga|guru dan murid|paman dan teman|Keluarga inti.
Kepada kakek dan nenek kita harus …|menghormati|mengejek|membentak|meninggalkan|Hormati kakek dan nenek.
## BIN|Menulis kalimat tentang diriku
Kalimat tentang diri yang benar adalah …|Namaku Rina.|namaku rina.|Namaku rina|namaku Rina|Kapital di awal dan pada nama, diakhiri titik.
Kalimat Aku berumur tujuh tahun menceritakan …|umur|hobi|alamat|cita-cita|Berumur menunjukkan umur.
Kalimat Hobiku menggambar menceritakan …|hobi|nama|umur|alamat|Hobi adalah kegemaran.
B|Nama sendiri ditulis dengan huruf kapital di awal.|Nama orang diawali kapital.
S|Kalimat tentang diri tidak perlu tanda titik.|Setiap kalimat diakhiri titik.
=|Kegiatan yang kita sukai disebut …|hobi;kegemaran|Hobi.
Kalimat Rumahku di Cibodas menceritakan …|alamat|hobi|umur|makanan|Rumah menunjukkan alamat.
Kalimat Aku ingin menjadi dokter menceritakan …|cita-cita|umur|nama|alamat|Cita-cita.
## BIN|Kata sifat dan lawan kata
Lawan kata panas adalah …|dingin|besar|tinggi|cepat|Panas lawannya dingin.
Lawan kata tinggi adalah …|rendah|panjang|gelap|kecil|Tinggi lawannya rendah.
Gajah badannya …|besar|kecil|pendek|ringan|Gajah besar.
B|Lawan kata gelap adalah terang.|Gelap lawannya terang.
S|Lawan kata cepat adalah tinggi.|Cepat lawannya lambat.
=|Lawan kata panjang adalah …|pendek|Panjang lawannya pendek.
Kata sifat menjelaskan …|keadaan benda|kegiatan|jumlah|nama tempat|Kata sifat menjelaskan keadaan.
Semut bertubuh …|kecil|besar|tinggi|berat|Semut kecil.
## BIN|Mendengarkan petunjuk
Saat mendengarkan petunjuk, kita harus …|fokus|bermain|mengobrol|tidur|Fokus agar paham.
Jika petunjuk belum jelas, kita sebaiknya …|bertanya dengan sopan|diam saja|marah|pergi|Bertanya dengan sopan.
Langkah pertama mencuci tangan adalah …|membasahi tangan|mengeringkan tangan|membilas|menggosok sela jari|Basahi tangan dulu.
B|Petunjuk dilakukan sesuai urutan.|Urutan penting.
S|Petunjuk boleh dilakukan secara acak.|Harus urut.
=|Keterangan tentang cara melakukan sesuatu disebut …|petunjuk|Petunjuk.
Langkah terakhir mencuci tangan adalah …|mengeringkan tangan|memberi sabun|membasahi tangan|menggosok|Terakhir keringkan.
Mendengarkan petunjuk dengan baik membuat pekerjaan …|berhasil|gagal|lama|rusak|Pekerjaan berhasil.

## PPK|Simbol sila-sila Pancasila
Simbol sila pertama adalah …|bintang|rantai|pohon beringin|padi dan kapas|Sila pertama bintang.
Simbol sila ketiga adalah …|pohon beringin|kepala banteng|bintang|rantai|Sila ketiga pohon beringin.
Simbol padi dan kapas untuk sila ke …|lima|satu|dua|tiga|Sila kelima padi dan kapas.
B|Rantai adalah simbol sila kedua.|Sila kedua rantai.
S|Kepala banteng adalah simbol sila pertama.|Kepala banteng sila keempat.
=|Pancasila terdiri atas … sila.|lima;5|Lima sila.
Simbol-simbol sila terdapat pada … Garuda.|perisai|sayap|kaki|ekor|Di perisai Garuda.
Simbol kepala banteng untuk sila ke …|empat|satu|dua|lima|Sila keempat.
## PPK|Garuda Pancasila
Lambang negara Indonesia adalah …|Garuda Pancasila|bendera|lagu Indonesia Raya|Monas|Garuda Pancasila lambang negara.
Semboyan pada pita Garuda adalah …|Bhinneka Tunggal Ika|Merdeka|Indonesia Raya|Pancasila|Bhinneka Tunggal Ika.
Bhinneka Tunggal Ika artinya …|berbeda-beda tetapi tetap satu|sama semua|merdeka selamanya|cinta damai|Berbeda-beda tetapi tetap satu.
B|Garuda mencengkeram pita bertuliskan semboyan negara.|Kaki Garuda mencengkeram pita.
S|Perisai Garuda berisi gambar hewan peliharaan.|Perisai berisi simbol sila.
=|Garuda Pancasila adalah … negara Indonesia.|lambang|Lambang negara.
Warna Garuda Pancasila adalah …|emas|hijau|ungu|abu-abu|Warna emas.
Sikap kita terhadap lambang negara adalah …|menghormati|mencoret|merusak|membuang|Kita menghormati lambang negara.
## PPK|Bersyukur sebagai ciptaan Tuhan
Kita semua adalah ciptaan …|Tuhan Yang Maha Esa|manusia|robot|alam|Ciptaan Tuhan.
Cara bersyukur adalah …|berdoa|mengeluh|marah|merusak|Berdoa tanda syukur.
Bersyukur sesuai dengan sila ke …|satu|dua|tiga|lima|Sila pertama ketuhanan.
B|Merawat tubuh termasuk bersyukur.|Menjaga ciptaan Tuhan.
S|Bersyukur cukup diucapkan tanpa dilakukan.|Bersyukur juga dengan perbuatan.
=|Sebelum makan kita … sebagai tanda syukur.|berdoa|Berdoa sebelum makan.
Mandi dan makan sehat termasuk cara …|merawat tubuh|merusak tubuh|bermalas-malasan|mengeluh|Merawat tubuh.
Menyiram tanaman termasuk menyayangi …|ciptaan Tuhan|diri sendiri saja|mainan|gawai|Tanaman ciptaan Tuhan.
## PPK|Menyayangi teman
Contoh menyayangi teman adalah …|meminjamkan pensil|mengejek|merebut mainan|memukul|Meminjamkan pensil.
Jika teman jatuh, kita sebaiknya …|menolongnya|menertawakan|meninggalkan|diam saja|Menolong teman.
Menyayangi teman sesuai dengan sila ke …|dua|satu|tiga|empat|Sila kedua kemanusiaan.
B|Menghibur teman yang sedih termasuk menyayangi teman.|Perbuatan baik.
S|Mengejek teman termasuk perbuatan baik.|Mengejek tidak baik.
=|Kita berteman dengan … teman, tidak memilih-milih.|semua|Semua teman.
Merebut mainan teman adalah perbuatan …|tidak baik|baik|terpuji|sopan|Tidak baik.
Mengajak teman yang sendirian untuk bermain adalah sikap …|peduli|egois|sombong|malas|Peduli.
## PPK|Disiplin waktu
Disiplin waktu artinya …|tepat waktu|terlambat|menunda|bermalas-malasan|Tepat waktu.
Contoh disiplin waktu adalah …|bangun pagi|tidur larut malam|terlambat sekolah|bermain terus|Bangun pagi.
Mengerjakan PR sebaiknya …|sebelum bermain|sesudah tidur|tidak dikerjakan|di sekolah saja|Sebelum bermain.
B|Jadwal kegiatan membantu kita disiplin.|Jadwal membantu teratur.
S|Disiplin membuat kegiatan berantakan.|Disiplin membuat teratur.
=|Datang ke sekolah tepat waktu artinya tidak …|terlambat|Tidak terlambat.
Akibat tidak disiplin waktu adalah …|terlambat|selalu tepat waktu|pujian|rapi|Bisa terlambat.
Kegiatan malam sebelum tidur adalah …|gosok gigi|berangkat sekolah|sarapan|upacara|Gosok gigi sebelum tidur.
## PPK|Hak dan kewajiban anak di rumah
Contoh hak anak adalah …|mendapat kasih sayang|merapikan mainan|mencuci piring|menyapu|Kasih sayang adalah hak.
Contoh kewajiban anak adalah …|merapikan tempat tidur|bermain sepanjang hari|menonton televisi|jajan|Merapikan tempat tidur.
Hak dan kewajiban harus …|seimbang|dilupakan|dipilih satu|ditukar|Seimbang.
B|Belajar adalah kewajiban anak.|Kewajiban.
S|Membantu orang tua termasuk hak anak.|Itu kewajiban.
=|Sesuatu yang harus kita lakukan disebut …|kewajiban|Kewajiban.
Sesuatu yang boleh kita terima disebut …|hak|kewajiban|tugas|larangan|Hak.
Sebaiknya kita melakukan kewajiban … meminta hak.|sebelum|tanpa|tidak pernah|sambil marah|Kewajiban dulu.
## PPK|Lagu kebangsaan Indonesia Raya
Lagu kebangsaan Indonesia adalah …|Indonesia Raya|Garuda Pancasila|Hari Merdeka|Tanah Airku|Indonesia Raya.
Pencipta lagu Indonesia Raya adalah …|W.R. Supratman|Ibu Sud|Ismail Marzuki|C. Simanjuntak|W.R. Supratman.
Saat menyanyikan Indonesia Raya kita …|berdiri tegak|duduk santai|bercanda|tiduran|Sikap tegak.
B|Indonesia Raya dinyanyikan dengan khidmat.|Khidmat artinya sungguh-sungguh.
S|Boleh bercanda saat lagu Indonesia Raya dinyanyikan.|Tidak boleh bercanda.
=|Lagu kebangsaan Indonesia berjudul Indonesia …|Raya|Indonesia Raya.
Indonesia Raya biasa dinyanyikan saat …|upacara bendera|tidur|makan|bermain|Saat upacara.
Menyanyikan lagu kebangsaan dengan khidmat adalah tanda …|cinta tanah air|malas|bosan|takut|Cinta tanah air.
## PPK|Upacara bendera
Upacara bendera di sekolah biasanya hari …|Senin|Rabu|Jumat|Minggu|Senin.
Saat bendera dikibarkan, peserta …|memberi hormat|duduk|berlari|mengobrol|Memberi hormat.
Petugas yang memberi amanat adalah …|pembina upacara|pengibar bendera|paduan suara|pembawa doa|Pembina upacara.
B|Upacara diikuti dengan tertib.|Tertib dan tenang.
S|Pengibar bendera bertugas memberi amanat.|Pengibar mengibarkan bendera.
=|Bendera Indonesia berwarna merah dan …|putih|Merah Putih.
Petugas yang memimpin barisan adalah …|pemimpin upacara|paduan suara|pembina|penonton|Pemimpin upacara.
Mengikuti upacara bendera melatih sikap …|disiplin|malas|nakal|sombong|Disiplin.
## PPK|Keragaman teman di kelas
Teman di kelas memiliki kesukaan yang …|berbeda-beda|selalu sama|tidak ada|dilarang|Berbeda-beda.
Sikap kita terhadap teman yang berbeda adalah …|menghargai|mengejek|menjauhi|memusuhi|Menghargai.
Perbedaan di kelas itu …|indah|buruk|memalukan|menakutkan|Perbedaan itu indah.
B|Teman berbeda agama tetap bisa bermain bersama.|Tetap berteman.
S|Kita hanya boleh berteman dengan yang sama kesukaannya.|Berteman dengan semua.
=|Berbeda-beda tetapi tetap satu disebut Bhinneka Tunggal …|Ika|Bhinneka Tunggal Ika.
Rina suka menggambar dan Dodi suka sepak bola. Mereka sebaiknya …|tetap bermain bersama|bermusuhan|saling mengejek|berpisah|Tetap bersahabat.
Mengejek teman karena berbeda adalah sikap …|tidak terpuji|terpuji|sopan|baik|Tidak terpuji.
## PPK|Musyawarah di keluarga
Musyawarah artinya …|berbicara bersama untuk mengambil keputusan|bertengkar|memaksa|diam saja|Musyawarah.
Dalam musyawarah, semua anggota boleh …|berpendapat|memaksa|marah|berteriak|Semua boleh berpendapat.
Musyawarah sesuai dengan sila ke …|empat|satu|dua|tiga|Sila keempat.
B|Hasil musyawarah dijalankan bersama.|Dijalankan bersama.
S|Dalam musyawarah kita boleh memaksakan kemauan sendiri.|Tidak boleh memaksa.
=|Hasil musyawarah harus … bersama.|dijalankan;dilaksanakan|Dijalankan bersama.
Saat orang lain berpendapat, kita sebaiknya …|mendengarkan|memotong|tertawa|pergi|Mendengarkan.
Jika pendapat kita tidak dipilih, kita …|menerima dengan senang hati|marah|menangis|mengejek|Menerima keputusan.
## PPK|Adil kepada saudara
Adil artinya …|tidak berat sebelah|mengambil lebih banyak|menang sendiri|pilih kasih|Tidak berat sebelah.
Contoh sikap adil kepada saudara adalah …|berbagi kue sama banyak|mengambil kue lebih banyak|tidak mau berbagi|menyembunyikan kue|Berbagi sama banyak.
Bersikap adil sesuai dengan sila ke …|lima|satu|dua|tiga|Sila kelima.
B|Mainan dipakai bergantian termasuk sikap adil.|Bergantian.
S|Mengambil bagian lebih banyak termasuk sikap adil.|Tidak adil.
=|Mainan yang hanya satu sebaiknya dipakai secara …|bergantian|Bergantian.
Sikap adil membuat semua orang merasa …|senang|sedih|marah|kecewa|Senang.
Kakak dan adik mendapat permen. Bagian yang adil adalah …|sama banyak|kakak semua|adik semua|dibuang|Sama banyak.
## PPK|Kekayaan alam Indonesia
Hewan yang hanya ada di Indonesia adalah …|komodo|singa|pinguin|kanguru|Komodo.
Sawah menghasilkan …|padi|ikan|kayu|garam|Padi dari sawah.
Laut menghasilkan …|ikan|padi|kayu|jagung|Ikan dari laut.
B|Menjaga alam dengan tidak membuang sampah sembarangan.|Menjaga alam.
S|Kekayaan alam boleh dirusak sesuka hati.|Harus dijaga.
=|Hutan menghasilkan …|kayu|Kayu dari hutan.
Sikap kita terhadap kekayaan alam adalah …|mensyukuri dan menjaganya|merusaknya|membuangnya|mengabaikannya|Syukuri dan jaga.
Indonesia memiliki banyak gunung, laut, dan …|hutan|gurun salju|kutub|gunung es|Hutan.

## SBD|Mengenal warna di alam
Warna langit siang yang cerah adalah …|biru|merah|hitam|ungu|Langit biru.
Warna daun yang segar adalah …|hijau|biru|ungu|abu-abu|Daun hijau.
Warna pisang matang adalah …|kuning|hijau tua|biru|hitam|Pisang matang kuning.
B|Tomat matang berwarna merah.|Tomat merah.
S|Awan biasanya berwarna hijau.|Awan putih.
=|Warna tanah biasanya …|cokelat;coklat|Tanah cokelat.
Warna di alam bisa kita pakai saat …|menggambar|tidur|makan|mandi|Saat menggambar.
Warna arang adalah …|hitam|putih|kuning|merah muda|Arang hitam.
## SBD|Menggambar bentuk dasar
Atap rumah bisa digambar dengan bentuk …|segitiga|lingkaran|bintang|hati|Atap segitiga.
Matahari bisa digambar dengan bentuk …|lingkaran|segitiga|persegi|garis lurus|Matahari lingkaran.
Roda mobil digambar dengan bentuk …|lingkaran|segitiga|persegi panjang|belah ketupat|Roda lingkaran.
B|Banyak benda bisa digambar dari bentuk dasar.|Bentuk dasar.
S|Lingkaran memiliki tiga sudut.|Lingkaran tidak bersudut.
=|Dinding rumah biasanya digambar dengan bentuk …|persegi;persegi panjang|Persegi.
Bentuk dasar terdiri atas lingkaran, segitiga, dan …|persegi|awan|bintang|hati|Persegi.
Layang-layang berbentuk …|belah ketupat|lingkaran|segitiga|tabung|Belah ketupat.
## SBD|Kolase dari kertas
Kolase dibuat dengan cara …|menempel potongan bahan|melukis dengan cat|menyanyi|menari|Menempel potongan bahan.
Bahan kolase yang mudah didapat adalah …|kertas warna|besi|kaca|batu besar|Kertas warna.
Langkah pertama membuat kolase adalah …|membuat pola gambar|menempel kertas|mengoleskan lem|membingkai|Buat pola dulu.
B|Daun kering bisa dipakai sebagai bahan kolase.|Bahan alam.
S|Kolase dibuat dengan cara bernyanyi.|Kolase ditempel.
=|Alat untuk merekatkan potongan kertas adalah …|lem|Lem.
Potongan kertas sebaiknya ditempel …|rapat|berjauhan|bertumpuk tinggi|di luar pola|Rapat mengikuti pola.
Kolase membuat gambar menjadi …|bertekstur|hilang|basah|rusak|Bertekstur.
## SBD|Bunyi di sekitarku
Bunyi guntur termasuk bunyi yang …|keras|lembut|pelan sekali|tidak terdengar|Guntur keras.
Kicau burung termasuk bunyi …|hewan|benda|mesin|alat musik|Bunyi hewan.
Bunyi bisikan termasuk bunyi yang …|lembut|keras|nyaring|menggelegar|Bisikan lembut.
B|Bunyi hujan termasuk bunyi alam.|Bunyi alam.
S|Bunyi bel termasuk bunyi hewan.|Bel adalah benda.
=|Bunyi bel sekolah terdengar …|nyaring;keras|Nyaring.
Detak jam berbunyi secara …|teratur|acak|sangat keras|tidak pernah|Teratur.
Mendengarkan bunyi melatih … kita.|telinga|kaki|rambut|kuku|Telinga.
## SBD|Alat musik ritmis
Alat musik ritmis berfungsi mengatur …|irama|warna|bentuk|cahaya|Mengatur irama.
Rebana dimainkan dengan cara …|dipukul|ditiup|dipetik|digesek|Dipukul.
Marakas dimainkan dengan cara …|digoyang|ditiup|dipetik|digesek|Digoyang.
B|Alat musik ritmis tidak menghasilkan nada.|Tidak bernada.
S|Gendang dimainkan dengan cara ditiup.|Gendang dipukul.
=|Kastanyet dimainkan dengan cara …|dijepit|Dijepit.
Contoh alat musik ritmis adalah …|tamborin|seruling|gitar|biola|Tamborin.
Alat musik dari botol berisi beras dimainkan dengan …|digoyang|ditiup|dipetik|digesek|Digoyang seperti marakas.
## SBD|Lagu anak Nusantara
Lagu Ampar-Ampar Pisang berasal dari …|Kalimantan Selatan|Papua|Jawa Barat|Maluku|Kalimantan Selatan.
Lagu Manuk Dadali berasal dari …|Jawa Barat|Papua|Maluku|Sumatra Barat|Jawa Barat.
Lagu Yamko Rambe Yamko berasal dari …|Papua|Jawa Tengah|Kalimantan|Bali|Papua.
B|Cublak-Cublak Suweng berasal dari Jawa Tengah.|Jawa Tengah.
S|Burung Kakatua berasal dari Papua.|Dari Maluku.
=|Lagu Kampuang Nan Jauh di Mato berasal dari Sumatra …|Barat|Sumatra Barat.
Saat menyanyi lagu anak, suara kita sebaiknya …|riang dan jelas|berteriak|berbisik|marah|Riang dan jelas.
Menyanyikan lagu daerah adalah tanda cinta …|budaya Indonesia|budaya asing|gawai|mainan|Cinta budaya.
## SBD|Gerak menirukan hewan
Gerak burung dalam tari dilakukan dengan …|mengepakkan tangan|melompat|merangkak|berguling|Mengepakkan tangan.
Gerak kelinci dilakukan dengan …|melompat kecil|berjalan pelan|mengepak|meliuk|Melompat kecil.
Gerak kura-kura dilakukan dengan …|berjalan pelan|berlari kencang|melompat tinggi|terbang|Berjalan pelan.
B|Gerak tari dilakukan sesuai irama musik.|Sesuai irama.
S|Gerak ikan dilakukan dengan melompat tinggi.|Ikan meliukkan badan.
=|Gerak gajah dilakukan dengan mengayun tangan seperti …|belalai|Belalai.
Tari menirukan hewan melatih kita …|berekspresi|tidur|diam|makan|Berekspresi.
Gerak kupu-kupu dilakukan dengan mengepak …|lembut|kasar|cepat sekali|keras|Lembut.
## SBD|Pola lantai tari
Pola lantai adalah …|garis yang dibentuk penari|warna baju penari|lagu pengiring|nama tari|Garis yang dibentuk penari.
Penari bergandengan membentuk …|lingkaran|segitiga tajam|bintang|titik|Lingkaran.
Supaya pola lantai rapi, penari harus …|menjaga jarak|berdesakan|berlari acak|duduk|Menjaga jarak.
B|Pola lantai bisa berbentuk huruf V.|Pola V.
S|Pola lantai hanya ada satu macam.|Banyak macam.
=|Penari berbaris ke samping membentuk pola garis …|lurus|Garis lurus.
Pola lantai membuat tarian terlihat …|indah|berantakan|membosankan|kacau|Indah.
Pola lantai yang berbelok-belok disebut …|zig-zag|lingkaran|lurus|titik|Zig-zag.
## SBD|Mencetak dengan pelepah dan daun
Mencetak adalah membuat gambar dengan …|menempelkan benda yang diberi pewarna|menyanyi|melipat kertas|menggunting|Menempelkan benda berpewarna.
Bahan untuk mencetak adalah …|daun|batu besar|besi|kaca|Daun.
Saat mencetak, cat dipakai …|secukupnya|sebanyak-banyaknya|tidak dipakai|dicampur air banyak|Secukupnya.
B|Jari bisa dipakai untuk mencetak.|Cetak jari.
S|Mencetak tidak memakai pewarna.|Memakai pewarna.
=|Cetakan daun bisa disusun menjadi gambar …|pohon|Pohon.
Langkah setelah mengoleskan cat pada daun adalah …|menempelkan ke kertas|membuang daun|mencuci daun|menjemur daun|Tempel ke kertas.
Potongan sayur seperti wortel bisa dipakai untuk …|mencetak|menyanyi|menari|menulis|Mencetak.
## SBD|Membentuk dengan plastisin
Plastisin adalah bahan yang …|lunak dan bisa dibentuk|keras seperti batu|cair seperti air|tajam|Lunak.
Teknik membuat bentuk panjang adalah …|memilin|membulatkan|memipihkan|mencubit|Memilin.
Teknik membuat bentuk bola adalah …|membulatkan|memilin|memipihkan|menggulung|Membulatkan.
B|Plastisin disimpan di wadah tertutup.|Supaya tidak kering.
S|Memipihkan menghasilkan bentuk bola.|Memipihkan menghasilkan lembaran.
=|Teknik membuat lembaran tipis disebut …|memipihkan|Memipihkan.
Membentuk plastisin melatih … kita.|jari|telinga|mata|rambut|Melatih jari.
Buah jeruk dari plastisin dibuat dengan teknik …|membulatkan|memilin|menggunting|melipat|Membulatkan.
## SBD|Cepat lambat lagu
Cepat lambatnya lagu disebut …|tempo|nada|warna|lirik|Tempo.
Lagu Nina Bobo bertempo …|lambat|cepat|sangat cepat|berubah-ubah|Lambat.
Lagu Naik Kereta Api bertempo …|cepat|lambat|sangat lambat|tidak bertempo|Cepat.
B|Lagu gembira biasanya bertempo cepat.|Gembira cepat.
S|Lagu pengantar tidur biasanya bertempo cepat.|Lambat.
=|Saat lagu cepat, tepuk tangan kita juga …|cepat|Cepat.
Lagu Ibu Kita Kartini dinyanyikan dengan tempo …|sedang agak lambat|sangat cepat|terburu-buru|asal|Agak lambat.
Mengikuti tempo membuat nyanyian lebih …|indah|kacau|jelek|berantakan|Indah.
## SBD|Menghias benda sederhana
Botol plastik bekas bisa dihias menjadi …|pot bunga|sepatu|baju|buku|Pot bunga.
Bahan hiasan antara lain …|pita|batu bata|semen|pasir|Pita.
Menghias barang bekas membantu mengurangi …|sampah|teman|waktu bermain|nilai|Sampah.
B|Kotak susu bekas bisa dijadikan tempat pensil.|Barang bekas.
S|Barang bekas tidak bisa dihias.|Bisa dihias.
=|Kaleng bekas bisa dijadikan …|celengan|Celengan.
Menghias benda melatih …|kreativitas|kemalasan|kemarahan|kesombongan|Kreativitas.
Kardus bekas bisa dijadikan …|rumah boneka|nasi|air minum|pakaian|Rumah boneka.

## PJOK|Berjalan maju mundur
Saat berjalan maju, bagian kaki yang menyentuh tanah lebih dulu adalah …|tumit|jari kaki|lutut|paha|Tumit dulu.
Saat berjalan, tangan diayun …|berlawanan dengan kaki|bersamaan dengan kaki|tidak diayun|ke atas kepala|Berlawanan.
Berjalan mundur dilakukan dengan …|pelan dan hati-hati|cepat sekali|mata tertutup|melompat|Pelan.
B|Saat berjalan maju, pandangan ke depan.|Pandangan ke depan.
S|Berjalan mundur sebaiknya sambil berlari kencang.|Harus pelan.
=|Saat berjalan mundur, sesekali kita … ke belakang.|menoleh|Menoleh agar tidak menabrak.
Berjalan dengan benar membuat tubuh …|seimbang|lelah sekali|sakit|kaku|Seimbang.
Saat kaki kanan maju, tangan yang ke depan adalah …|tangan kiri|tangan kanan|kedua tangan|tidak ada|Tangan kiri.
## PJOK|Gerak keseimbangan
Keseimbangan adalah kemampuan menjaga tubuh supaya …|tidak jatuh|cepat lelah|tidur|lapar|Tidak jatuh.
Contoh latihan keseimbangan adalah …|berdiri satu kaki|berlari kencang|melempar bola|menendang|Berdiri satu kaki.
Saat latihan keseimbangan, pandangan sebaiknya …|lurus ke depan|ke bawah terus|memejamkan mata|menoleh-noleh|Lurus ke depan.
B|Sikap pesawat terbang melatih keseimbangan.|Melatih keseimbangan.
S|Saat berdiri satu kaki kita harus menahan napas.|Bernapas biasa.
=|Berjalan di atas garis lurus melatih …|keseimbangan|Keseimbangan.
Sikap pesawat terbang dilakukan dengan kedua tangan …|direntangkan|di saku|di kepala|di belakang|Direntangkan.
Latihan keseimbangan membuat tubuh lebih …|stabil|lemah|mudah jatuh|kaku|Stabil.
## PJOK|Mengayun dan memutar lengan
Mengayun lengan artinya menggerakkan lengan ke …|depan dan belakang|atas saja|bawah saja|samping saja|Depan dan belakang.
Memutar lengan membentuk gerakan …|lingkaran|garis lurus|segitiga|zig-zag|Lingkaran.
Mengayun dan memutar lengan melemaskan …|bahu|perut|telinga|jari kaki|Bahu.
B|Gerakan memutar lengan dilakukan pelan dan teratur.|Pelan dan teratur.
S|Memutar lengan sebaiknya secepat mungkin.|Pelan agar tidak sakit.
=|Gerakan menoleh ke kanan dan kiri melatih …|leher|Leher.
Memutar pinggang melatih bagian …|pinggang|kepala|tangan|kaki|Pinggang.
Menekuk lutut melatih bagian …|kaki|leher|bahu|kepala|Kaki.
## PJOK|Permainan kucing dan tikus
Dalam permainan kucing dan tikus, pemain membentuk …|lingkaran|garis lurus|segitiga|barisan panjang|Lingkaran.
Tugas kucing adalah …|menangkap tikus|melindungi tikus|diam di tengah|bernyanyi|Menangkap tikus.
Pemain yang bergandengan bertugas …|melindungi tikus|menangkap tikus|duduk|pergi|Melindungi tikus.
B|Permainan kucing dan tikus melatih kelincahan.|Lincah.
S|Saat bermain boleh mendorong teman.|Harus sportif.
=|Anak yang berada di dalam lingkaran berperan sebagai …|tikus|Tikus.
Permainan ini juga melatih …|kerja sama|kemalasan|kesombongan|kecurangan|Kerja sama.
Saat bermain, kita harus bersikap …|sportif|curang|kasar|egois|Sportif.
## PJOK|Gerak merangkak dan berguling
Merangkak dilakukan dengan …|tangan dan lutut|kepala|satu kaki|perut saja|Tangan dan lutut.
Berguling sebaiknya dilakukan di atas …|matras|lantai keras|aspal|batu|Matras.
Saat berguling ke samping, tangan diluruskan …|di atas kepala|di saku|di belakang|ke samping badan|Di atas kepala.
B|Merangkak dan berguling melatih kekuatan.|Melatih kekuatan.
S|Berguling aman dilakukan di jalan raya.|Harus di matras.
=|Alas empuk untuk latihan berguling disebut …|matras|Matras.
Berguling ke samping seperti … menggelinding.|kayu|bola basket|air|angin|Seperti kayu.
Merangkak maju seperti gerakan …|bayi|burung|ikan|kuda lari|Seperti bayi.
## PJOK|Senam irama sederhana
Senam irama adalah senam yang diiringi …|musik|diam|tepuk tangan saja|peluit saja|Musik.
Gerakan senam irama mengikuti …|hitungan|warna|bentuk|cuaca|Hitungan.
Jalan di tempat termasuk gerakan …|dasar senam irama|berenang|melempar|menangkap|Gerak dasar.
B|Senam irama menyehatkan tubuh.|Menyehatkan.
S|Senam irama dilakukan tanpa mengikuti hitungan.|Mengikuti hitungan.
=|Senam irama biasanya dihitung satu sampai …|delapan;8|Delapan hitungan.
Senam pagi bersama keluarga membuat tubuh …|segar|lemas|sakit|ngantuk|Segar.
Gerakan terakhir senam disebut sikap …|akhir|awal|tengah|lari|Sikap akhir.
## PJOK|Bermain lompat tali
Lompat tali termasuk permainan …|tradisional|modern elektronik|berenang|catur|Tradisional.
Tali untuk lompat tali bisa dibuat dari …|karet gelang|kaca|besi|kertas tipis|Karet gelang.
Saat mendarat, lutut sebaiknya …|sedikit ditekuk|lurus kaku|diangkat tinggi|dilipat penuh|Ditekuk.
B|Tinggi tali dinaikkan bertahap.|Bertahap.
S|Lompat tali dimulai dari tali setinggi bahu.|Dimulai dari mata kaki.
=|Level pertama lompat tali setinggi mata …|kaki|Mata kaki.
Lompat tali melatih kekuatan …|kaki|telinga|mata|rambut|Kaki.
Saat tali tinggi, kita mengambil … dulu.|awalan lari|tidur|duduk|makan|Awalan lari.
## PJOK|Pemanasan sebelum olahraga
Pemanasan dilakukan … olahraga.|sebelum|sesudah|tanpa|selama tidur|Sebelum.
Tujuan pemanasan adalah …|mencegah cedera|membuat lelah|membuat lapar|membuat ngantuk|Mencegah cedera.
Pemanasan dimulai dari bagian …|kepala|kaki|tangan saja|perut|Dari kepala.
B|Gerakan pemanasan dilakukan pelan dan teratur.|Pelan dan teratur.
S|Pemanasan tidak perlu dilakukan sebelum berlari.|Perlu pemanasan.
=|Gerakan terakhir pemanasan adalah memutar pergelangan …|kaki|Pergelangan kaki.
Langsung berlari kencang tanpa pemanasan bisa menyebabkan …|cedera|sehat|kuat|senang|Cedera.
Menoleh ke kanan dan kiri adalah pemanasan bagian …|leher|kaki|perut|tangan|Leher.
## PJOK|Pendinginan setelah olahraga
Pendinginan dilakukan … olahraga.|sesudah|sebelum|tanpa|saat tidur|Sesudah.
Pendinginan membuat napas kembali …|normal|cepat|berhenti|sesak|Normal.
Contoh gerakan pendinginan adalah …|jalan santai|lari kencang|melompat tinggi|push up cepat|Jalan santai.
B|Menarik napas dalam termasuk pendinginan.|Menenangkan tubuh.
S|Setelah lari kencang sebaiknya langsung tidur.|Lakukan pendinginan dulu.
=|Saat pendinginan, kita menarik napas lewat …|hidung|Hidung.
Gerakan pendinginan dilakukan secara …|pelan|cepat|kasar|terburu-buru|Pelan.
Peregangan otot setelah olahraga termasuk …|pendinginan|pemanasan|lomba|permainan|Pendinginan.
## PJOK|Makanan sehat untuk tubuh
Makanan yang memberi tenaga adalah …|nasi|permen|keripik|soda|Nasi.
Ikan dan telur membantu tubuh …|tumbuh|lemas|sakit|ngantuk|Tumbuh.
Minuman paling sehat adalah …|air putih|soda|sirup manis|kopi|Air putih.
B|Sayur dan buah membuat tubuh sehat.|Sehat.
S|Sering jajan makanan manis membuat tubuh lebih sehat.|Kurangi makanan manis.
=|Buah yang banyak mengandung vitamin C adalah …|jeruk|Jeruk.
Bekal sehat berisi nasi, lauk, sayur, dan …|buah|permen|soda|keripik|Buah.
Makanan berminyak sebaiknya …|dikurangi|ditambah|dimakan terus|diminum|Dikurangi.
## PJOK|Menjaga kebersihan gigi
Sikat gigi minimal … sehari.|dua kali|sekali seminggu|sekali sebulan|tidak perlu|Dua kali sehari.
Waktu menyikat gigi yang tepat adalah …|pagi dan malam sebelum tidur|siang saja|saat lapar|saat bermain|Pagi dan malam.
Gerakan menyikat gigi yang benar adalah …|memutar dan pelan|keras dan cepat|diam saja|hanya ke kiri|Memutar dan pelan.
B|Makanan manis bisa membuat gigi berlubang.|Kurangi yang manis.
S|Sikat gigi cukup sekali seminggu.|Dua kali sehari.
=|Alat untuk membersihkan gigi disebut sikat …|gigi|Sikat gigi.
Setelah menyikat gigi, kita …|berkumur|makan permen|tidur tanpa berkumur|minum soda|Berkumur.
Gigi yang bersih membuat senyum …|sehat|kotor|sakit|bau|Sehat.
## PJOK|Istirahat dan tidur cukup
Anak seusiamu perlu tidur sekitar … jam.|sepuluh|dua|empat|dua puluh|Sekitar sepuluh jam.
Sebelum tidur sebaiknya …|mematikan gawai|bermain gawai|makan permen|berlari|Matikan gawai.
Tidur cukup membuat tubuh …|segar|lemas|sakit|lelah|Segar.
B|Berdoa sebelum tidur adalah kebiasaan baik.|Kebiasaan baik.
S|Bermain gawai sampai larut malam membuat tubuh segar.|Membuat lelah.
=|Sebelum tidur kita menggosok …|gigi|Gigi.
Jika kurang tidur, di sekolah kita akan …|mengantuk|bersemangat|segar|ceria|Mengantuk.
Jadwal tidur sebaiknya … setiap hari.|sama|berubah-ubah|tidak ada|larut malam|Sama setiap hari.
## PJOK|Bermain bola kecil
Contoh bola kecil adalah …|bola kasti|bola basket|bola sepak|bola voli|Bola kasti.
Saat menangkap bola, mata harus …|melihat bola|terpejam|melihat ke atas|melihat teman lain|Melihat bola.
Menangkap bola dilakukan dengan …|dua tangan terbuka|kaki|kepala|satu jari|Dua tangan.
B|Bola kecil bisa digelindingkan.|Digelindingkan.
S|Saat menangkap bola, tangan harus kaku.|Tangan lentur.
=|Melempar bola dengan ayunan tangan dari bawah disebut lemparan …|bawah|Lemparan bawah.
Bermain bola kecil melatih kerja sama mata dan …|tangan|telinga|rambut|hidung|Tangan.
Mendorong bola di lantai disebut …|menggelindingkan|melempar|menendang|menangkap|Menggelindingkan.
## PJOK|Aman saat bermain
Tempat bermain yang aman adalah …|halaman rumah|jalan raya|pinggir sungai|lantai licin|Halaman rumah.
Jika teman terluka, kita segera …|memberi tahu orang dewasa|meninggalkannya|menertawakan|diam saja|Beri tahu orang dewasa.
Sebelum bermain bola sebaiknya melepas …|jam tangan|sepatu|baju|kaus kaki|Lepas jam tangan.
B|Mengikuti aturan permainan membuat bermain aman.|Aman.
S|Bermain di jalan raya itu aman.|Berbahaya.
=|Tempat bermain harus jauh dari jalan …|raya|Jalan raya.
Lantai licin bisa membuat kita …|terpeleset|sehat|kuat|senang|Terpeleset.
Saat bermain di lapangan, sebaiknya memakai …|sepatu yang tepat|sandal jepit rusak|tanpa alas kaki di batu|sepatu hak tinggi|Sepatu yang tepat.

## PAI|Huruf hijaiyah alif sampai kha
Huruf hijaiyah adalah huruf …|Al-Qur'an|Latin|Jawa|Sunda|Huruf Al-Qur'an.
Huruf ba bertitik … di bawah.|satu|dua|tiga|empat|Satu titik di bawah.
Huruf tsa bertitik … di atas.|tiga|satu|dua|empat|Tiga titik di atas.
B|Huruf ta bertitik dua di atas.|Ta dua titik di atas.
S|Huruf alif memiliki tiga titik.|Alif tanpa titik.
=|Huruf hijaiyah yang pertama adalah …|alif|Alif.
## PAI|Huruf hijaiyah dal sampai dhad
Perbedaan dal dan dzal ada pada …|satu titik|warna|ukuran|harakat|Dzal bertitik satu.
Huruf syin bertitik …|tiga|satu|dua|nol|Tiga titik.
Huruf yang tidak bertitik adalah …|sin|syin|zai|dhad|Sin tanpa titik.
B|Huruf zai bertitik satu.|Zai satu titik.
S|Huruf ra bertitik tiga.|Ra tanpa titik.
=|Huruf yang bentuknya seperti sin ditambah tiga titik adalah …|syin|Syin.
## PAI|Huruf hijaiyah tha sampai qaf
Huruf qaf bertitik …|dua|satu|tiga|nol|Qaf dua titik.
Huruf fa bertitik …|satu|dua|tiga|nol|Fa satu titik.
Pasangan huruf 'ain adalah …|ghain|qaf|fa|tha|'Ain dan ghain.
B|Huruf zha bertitik satu.|Zha satu titik.
S|Huruf tha bertitik dua.|Tha tanpa titik.
=|Huruf yang seperti 'ain ditambah satu titik adalah …|ghain|Ghain.
## PAI|Huruf hijaiyah kaf sampai ya
Huruf nun bertitik satu di …|atas|bawah|samping|tengah|Nun di atas.
Huruf ya bertitik dua di …|bawah|atas|samping|tengah|Ya di bawah.
Huruf hijaiyah yang terakhir adalah …|ya|alif|nun|wau|Ya terakhir.
B|Lam alif adalah gabungan huruf lam dan alif.|Gabungan.
S|Huruf mim bertitik tiga.|Mim tanpa titik.
=|Gabungan huruf lam dan alif disebut lam …|alif|Lam alif.
## PAI|Harakat fathah
Fathah terletak di … huruf.|atas|bawah|samping|dalam|Di atas.
Huruf berharakat fathah dibaca dengan bunyi …|a|i|u|o|Bunyi a.
Tanda baca pada huruf hijaiyah disebut …|harakat|titik|koma|garis|Harakat.
B|Ba berharakat fathah dibaca ba.|Ba.
S|Fathah dibaca dengan bunyi u.|Fathah bunyi a.
=|Mim berharakat fathah dibaca …|ma|Ma.
## PAI|Harakat kasrah
Kasrah terletak di … huruf.|bawah|atas|samping|tengah|Di bawah.
Huruf berharakat kasrah dibaca dengan bunyi …|i|a|u|e|Bunyi i.
Ba berharakat kasrah dibaca …|bi|ba|bu|be|Bi.
B|Lam berharakat kasrah dibaca li.|Li.
S|Kasrah ditulis di atas huruf.|Di bawah.
=|Sin berharakat kasrah dibaca …|si|Si.
## PAI|Harakat dammah
Dammah bentuknya seperti huruf … kecil.|wau|alif|ba|ya|Wau kecil.
Huruf berharakat dammah dibaca dengan bunyi …|u|a|i|o|Bunyi u.
Nun berharakat dammah dibaca …|nu|na|ni|ne|Nu.
B|Ba berharakat dammah dibaca bu.|Bu.
S|Dammah dibaca dengan bunyi i.|Dammah bunyi u.
=|Harakat fathah, kasrah, dan dammah dibaca a, i, dan …|u|U.
## PAI|Tanwin
Tanwin adalah harakat …|ganda|tunggal|kosong|panjang|Harakat ganda.
Fathatain dibaca …|an|in|un|a|An.
Kasratain dibaca …|in|an|un|i|In.
B|Dammatain dibaca un.|Un.
S|Tanwin tidak memiliki bunyi n.|Tanwin berbunyi n.
=|Ba berharakat fathatain dibaca …|ban|Ban.
## PAI|Doa sebelum dan sesudah belajar
Sebelum belajar kita sebaiknya …|berdoa|bermain|tidur|makan permen|Berdoa.
Doa sebelum belajar memohon agar ilmu …|mudah dipahami|cepat lupa|hilang|sulit|Mudah dipahami.
Sesudah belajar kita …|bersyukur kepada Allah|marah|membuang buku|langsung tidur|Bersyukur.
B|Berdoa dilakukan dengan tenang dan sungguh-sungguh.|Tenang.
S|Berdoa sebelum belajar tidak perlu dilakukan.|Perlu berdoa.
=|Arti rabbi zidni ilma adalah Ya Tuhanku, tambahkanlah …|ilmuku|Ilmuku.
Saat berdoa, tangan kita …|menengadah|di saku|memegang mainan|bertepuk|Menengadah.
Setelah belajar, buku sebaiknya …|dirapikan|dibuang|dicoret|ditinggal di lantai|Dirapikan.
## PAI|Adab makan dan minum
Sebelum makan kita membaca …|basmalah|hamdalah|istighfar|takbir|Basmalah.
Makan dan minum sebaiknya dengan tangan …|kanan|kiri|kaki|siku|Tangan kanan.
Setelah makan kita …|berdoa|langsung lari|membuang makanan|berteriak|Berdoa.
B|Makan sambil duduk termasuk adab makan.|Duduk.
S|Makan sambil berjalan adalah adab yang baik.|Duduk saat makan.
=|Sebelum makan kita mencuci …|tangan|Tangan.
Makan secukupnya artinya tidak …|berlebihan|sedikit|bersyukur|duduk|Tidak berlebihan.
Membuang-buang makanan termasuk sikap …|mubazir|hemat|terpuji|bersyukur|Mubazir.
## PAI|Salat lima waktu
Salat wajib dalam sehari ada … waktu.|lima|tiga|dua|tujuh|Lima waktu.
Salat yang dikerjakan saat matahari terbenam adalah …|magrib|subuh|zuhur|asar|Magrib.
Salat subuh dikerjakan … rakaat.|dua|tiga|empat|lima|Dua rakaat.
B|Salat magrib dikerjakan tiga rakaat.|Tiga.
S|Salat zuhur dikerjakan pada malam hari.|Siang hari.
=|Salat yang dikerjakan pada malam hari adalah …|isya|Isya.
Salat yang dikerjakan pada sore hari adalah …|asar|subuh|isya|magrib|Asar.
Salat zuhur dikerjakan … rakaat.|empat|dua|tiga|lima|Empat rakaat.
## PAI|Kisah Nabi Nuh
Nabi Nuh mengajak kaumnya menyembah …|Allah|patung|matahari|bulan|Allah.
Allah memerintahkan Nabi Nuh membuat …|kapal|rumah|masjid|jembatan|Kapal.
Orang yang selamat dari banjir adalah orang yang …|beriman|mengejek|sombong|ingkar|Beriman.
B|Nabi Nuh tetap sabar walaupun diejek kaumnya.|Sabar.
S|Semua kaum Nabi Nuh ikut naik kapal.|Hanya yang beriman.
=|Bencana yang menimpa kaum Nabi Nuh adalah banjir …|besar|Banjir besar.
Hewan yang dibawa ke kapal Nabi Nuh adalah hewan …|berpasangan|satu jenis saja|hanya burung|hanya ikan|Berpasangan.
Pelajaran dari kisah Nabi Nuh adalah …|sabar dan taat kepada Allah|suka mengejek|sombong|malas|Sabar dan taat.

## SUN|Pakakas di sakola
Patlot dalam bahasa Indonesia artinya …|pensil|penghapus|penggaris|buku|Patlot pensil.
Pamupus artinya …|penghapus|pensil|meja|tas|Pamupus penghapus.
Panggaris artinya …|penggaris|pensil|kursi|tas|Panggaris penggaris.
B|Korsi artinya kursi.|Korsi kursi.
S|Méja artinya buku.|Méja meja.
=|Pakakas pikeun nulis disebut …|patlot|Patlot.
Pamupus dipaké pikeun …|mupus tulisan|nulis|maca|dahar|Menghapus tulisan.
Tempat nyimpen buku nalika indit ka sakola nyaéta …|tas|méja|korsi|papan|Tas.
## SUN|Ngaran poé
Rebo dalam bahasa Indonesia artinya …|Rabu|Selasa|Kamis|Sabtu|Rebo Rabu.
Kemis artinya …|Kamis|Senin|Jumat|Minggu|Kemis Kamis.
Saptu artinya …|Sabtu|Senin|Rabu|Selasa|Saptu Sabtu.
B|Salasa artinya Selasa.|Salasa Selasa.
S|Jumaah artinya Senin.|Jumaah Jumat.
=|Poé dina basa Indonesia hartina …|hari|Poé artinya hari.
Poé sanggeus Senén nyaéta …|Salasa|Rebo|Minggu|Kemis|Salasa.
Poé saméméh Saptu nyaéta …|Jumaah|Kemis|Minggu|Rebo|Jumaah.
## SUN|Kadaharan jeung inuman
Dahar artinya …|makan|minum|tidur|mandi|Dahar makan.
Nginum artinya …|minum|makan|duduk|berlari|Nginum minum.
Sangu artinya …|nasi|air|teh|susu|Sangu nasi.
B|Cai artinya air.|Cai air.
S|Entéh artinya nasi.|Entéh teh.
=|Kadaharan dina basa Indonesia hartina …|makanan|Makanan.
Abdi … sangu. (makan)|dahar|nginum|saré|mandi|Dahar sangu.
Adi … cai. (minum)|nginum|dahar|indit|ulin|Nginum cai.
## SUN|Bagian imah
Imah artinya …|rumah|sekolah|pasar|kebun|Imah rumah.
Buruan artinya …|halaman|dapur|kamar|atap|Buruan halaman.
Panto artinya …|pintu|jendela|atap|lantai|Panto pintu.
B|Jandéla artinya jendela.|Jandéla jendela.
S|Hateup artinya pintu.|Hateup atap.
=|Tepas dina basa Indonesia hartina ruang …|tamu|Ruang tamu.
Indung masak di …|dapur|buruan|tepas|hateup|Masak di dapur.
Barudak ulin di …|buruan|dapur|hateup|panto|Main di halaman.
## SUN|Kecap sopan ka kolot
Punten diucapkan saat …|permisi|makan|tidur|marah|Permisi.
Hatur nuhun artinya …|terima kasih|maaf|selamat tinggal|permisi|Terima kasih.
Mangga diucapkan untuk …|mempersilakan|menolak|marah|bertanya|Mempersilakan.
B|Abdi dipakai untuk menyebut diri sendiri dengan sopan.|Abdi sopan.
S|Kata kasar boleh dipakai kepada orang tua.|Harus sopan.
=|Wilujeng énjing artinya selamat …|pagi|Selamat pagi.
Sumuhun dipakai untuk menjawab …|ya|tidak|siapa|kapan|Sumuhun ya.
Lamun dibéré barang ku Ibu Guru, urang ngucapkeun …|hatur nuhun|punten|mangga|wilujeng|Hatur nuhun.
## SUN|Pakéan sapopoé
Pakéan artinya …|pakaian|makanan|rumah|sekolah|Pakéan pakaian.
Calana artinya …|celana|baju|sepatu|topi|Calana celana.
Sapatu artinya …|sepatu|sandal|kaus kaki|topi|Sapatu sepatu.
B|Samping artinya kain sarung.|Samping sarung.
S|Topi artinya celana.|Topi topi.
=|Pakéan nu dipaké dina suku pikeun ka sakola disebut …|sapatu|Sapatu.
Pakéan nu dipaké dina sirah disebut …|topi|calana|sapatu|kaos kaki|Topi.
Urang maké pakéan nu beresih jeung …|rapih|kotor|soék|baseuh|Rapih.
## SUN|Kembang jeung tatangkalan
Kembang artinya …|bunga|pohon|daun|buah|Kembang bunga.
Tangkal artinya …|pohon|bunga|rumput|batu|Tangkal pohon.
Cau artinya …|pisang|kelapa|mangga|jeruk|Cau pisang.
B|Malati artinya melati.|Malati melati.
S|Kalapa artinya pisang.|Kalapa kelapa.
=|Tangkal kalapa dina basa Indonesia hartina pohon …|kelapa|Kelapa.
Kembang mawar warnana …|beureum|bodas|hideung|héjo|Mawar merah.
Tangkal nu jangkung pisan jeung buahna dijieun santen nyaéta tangkal …|kalapa|cau|mangga|jambu|Kelapa.
## SUN|Cuaca
Tiris artinya …|dingin|panas|hujan|angin|Tiris dingin.
Méga artinya …|awan|langit|hujan|bintang|Méga awan.
Lamun hujan, urang maké …|payung|kacamata|topi pantai|sendal|Payung.
B|Poé ieu panas pisan artinya hari ini sangat panas.|Panas.
S|Tiris artinya panas.|Tiris dingin.
=|Cai nu turun ti langit disebut …|hujan|Hujan.
Lamun tiris, urang maké …|jaket|baju renang|topi pantai|kacamata hideung|Jaket.
Angin artinya …|angin|awan|hujan|petir|Angin.
## SUN|Kagiatan isuk-isuk
Isuk-isuk artinya …|pagi|siang|sore|malam|Isuk-isuk pagi.
Hudang artinya …|bangun|tidur|mandi|makan|Hudang bangun.
Indit artinya …|berangkat|pulang|duduk|makan|Indit berangkat.
B|Saréngséna mandi, abdi sarapan.|Urutan benar.
S|Hudang artinya tidur.|Hudang bangun.
=|Kagiatan munggaran isuk-isuk nyaéta …|hudang|Hudang.
Saméméh indit ka sakola, urang …|sarapan|saré deui|ulin wae|nonton|Sarapan.
Indit ka sakola mawa …|tas|bantal|sapu|piring|Tas.
## SUN|Sato di kebon binatang
Maung artinya …|harimau|ular|burung|ikan|Maung harimau.
Oray artinya …|ular|harimau|monyet|gajah|Oray ular.
Manuk artinya …|burung|ikan|ular|kucing|Manuk burung.
B|Lauk artinya ikan.|Lauk ikan.
S|Monyét artinya gajah.|Monyét monyet.
=|Sato artinya …|hewan;binatang|Hewan.
Sato nu bisa hiber nyaéta …|manuk|oray|lauk|maung|Burung terbang.
Sato nu hirup di cai nyaéta …|lauk|maung|manuk|monyét|Ikan.
## SUN|Wilangan sabelas nepi ka dua puluh
Sabelas artinya …|sebelas|dua belas|sepuluh|tiga belas|Sabelas 11.
Tilu belas artinya …|tiga belas|dua belas|empat belas|lima belas|13.
Genep belas artinya …|enam belas|tujuh belas|lima belas|delapan belas|16.
B|Salapan belas artinya sembilan belas.|19.
S|Opat belas artinya dua belas.|Opat belas 14.
=|Sanggeus salapan belas nyaéta dua …|puluh|Dua puluh.
Wilangan sanggeus sabelas nyaéta …|dua belas|tilu belas|sapuluh|opat belas|12.
Dalapan belas artinya …|delapan belas|tujuh belas|sembilan belas|enam belas|18.
## SUN|Babasan pondok
Babasan gedé hulu artinya …|sombong|rajin|sabar|penakut|Sombong.
Hampang birit artinya …|rajin|malas|sombong|penakut|Rajin.
Babasan adalah ungkapan yang artinya …|bukan arti kata sebenarnya|sama dengan arti kata|selalu lucu|tidak ada artinya|Bukan arti sebenarnya.
B|Gedé haté artinya sabar.|Sabar.
S|Panjang leungeun artinya rajin.|Panjang leungeun suka mencuri.
=|Babasan leutik haté hartina …|penakut|Penakut.
Ulah gedé hulu artinya jangan …|sombong|rajin|sabar|makan|Jangan sombong.
Budak nu sok mantuan kolot disebut …|hampang birit|gedé hulu|panjang leungeun|leutik haté|Rajin.
"""

SAS = """
## MAT 1
0|Ada 🐟🐟🐟🐟🐟🐟. Banyak ikan ada ....|6|5|7|8|Hitung satu per satu.
0|Bilangan enam ditulis ....|6|9|3|8|Enam ditulis 6.
1|Bilangan di antara 4 dan 6 adalah ....|5|3|7|8|Di antara 4 dan 6 ada 5.
1|Urutan bilangan yang benar adalah ....|3, 4, 5, 6|3, 5, 4, 6|6, 4, 5, 3|4, 3, 6, 5|Naik satu-satu.
2|Ani punya 4 apel. Ibu memberi 3 apel. Apel Ani sekarang ada ....|7|6|8|1|4 + 3 = 7.
2|5 + 4 = ....|9|8|10|1|Lima tambah empat.
3|Ada 8 burung. Terbang 3 ekor. Sisa burung ada ....|5|4|6|11|8 − 3 = 5.
3|10 − 6 = ....|4|3|5|6|Sepuluh kurang enam.
4|Kaleng susu berbentuk ....|tabung|kubus|bola|kerucut|Kaleng berbentuk tabung.
4|Topi ulang tahun berbentuk ....|kerucut|kubus|balok|tabung|Kerucut.
5|🔺 🟦 🔺 🟦 🔺 .... Gambar berikutnya adalah ....|🟦|🔺|⭕|⭐|Bergantian.
5|1, 3, 5, 7, .... Bilangan berikutnya adalah ....|9|8|10|11|Bertambah dua.
=0|Bilangan sesudah sembilan adalah ....|10;sepuluh|Sepuluh.
=2|3 + 3 = ....|6;enam|Enam.
=3|9 − 2 = ....|7;tujuh|Tujuh.
=4|Dadu berbentuk ....|kubus|Kubus.
=5|2, 4, 6, ..., 10. Bilangan yang hilang adalah ....|8;delapan|Delapan.
## MAT 2
0|Angka 3 pada bilangan 38 menempati tempat ....|puluhan|satuan|ratusan|ribuan|3 puluhan.
0|5 puluhan dan 2 satuan adalah ....|52|25|7|502|52.
1|Bilangan tujuh puluh satu ditulis ....|71|17|701|70|Tujuh puluh satu.
1|Bilangan sesudah 59 adalah ....|60|58|69|50|Sesudah 59 adalah 60.
2|Satuan berikut yang tidak baku adalah ....|jengkal|meter|sentimeter|kilogram|Jengkal tidak baku.
2|Panjang meja 6 jengkal dan papan 12 jengkal. Yang lebih panjang adalah ....|papan|meja|sama panjang|tidak tahu|12 lebih dari 6.
3|Alat untuk menimbang benda adalah ....|timbangan|penggaris|jam|gunting|Timbangan.
3|Pada timbangan, sisi yang turun berarti bendanya lebih ....|berat|ringan|kecil|pendek|Lebih berat.
4|Jarum pendek di angka 9, jarum panjang di angka 12. Pukul ....|9|12|3|6|Pukul 9.
4|Jarum yang menunjukkan jam adalah jarum ....|pendek|panjang|detik|merah|Jarum pendek.
5|Hari sesudah Kamis adalah ....|Jumat|Rabu|Sabtu|Selasa|Jumat.
5|Satu minggu ada ... hari.|7|5|6|10|Tujuh hari.
=0|Sepuluh satuan sama dengan satu ....|puluhan|Puluhan.
=1|Sepuluh puluhan sama dengan ....|100;seratus|Seratus.
=3|Mana yang lebih ringan, kapas atau batu?|kapas|Kapas.
=4|Saat jam tepat, jarum panjang menunjuk angka ....|12;dua belas|12.
=5|Hari sebelum Senin adalah ....|Minggu|Minggu.
## BIN 1
0|Penulisan nama kota yang benar adalah ....|Jakarta|jakarta|jAKARTA|jakartA|Nama kota diawali kapital.
0|Huruf kecil dari huruf G adalah ....|g|q|j|y|G kecil g.
1|Benda untuk menyimpan pakaian adalah ....|lemari|piring|gelas|sapu|Lemari.
1|Gelas dipakai untuk ....|tempat minum|tempat duduk|menyapu|tidur|Gelas tempat minum.
2|Kata kerja pada kalimat Kakak menulis surat adalah ....|menulis|kakak|surat|kalimat|Menulis.
2|Kata yang menunjukkan kegiatan adalah ....|berenang|kursi|merah|bulan|Berenang.
3|Kata sekolah, Rina, ke, berangkat disusun menjadi ....|Rina berangkat ke sekolah.|Sekolah ke Rina berangkat.|Ke Rina sekolah berangkat.|Berangkat sekolah ke Rina.|Urutan benar.
3|Kalimat diakhiri dengan tanda ....|titik|koma|tanya ganda|petik|Titik.
4|Kata berikut yang memakai huruf ng adalah ....|piring|nyamuk|meja|batu|Piring.
4|Kata berikut yang memakai huruf ny adalah ....|banyak|bunga|pisang|kancing|Banyak.
5|Puisi dibaca dengan suara ....|jelas|berbisik|berteriak|tergesa-gesa|Jelas.
5|Puisi disusun dalam ....|baris|tabel|angka|kotak|Baris.
=0|Huruf di awal kalimat ditulis dengan huruf ....|kapital;besar|Kapital.
=1|Benda untuk tempat makanan adalah ....|piring|Piring.
=2|Adik sedang ... susu. (kegiatan minum)|minum|Minum.
=4|Hewan kecil yang suka menggigit dan memakai ny adalah ....|nyamuk|Nyamuk.
=5|Setiap baris puisi diberi ... sebentar.|jeda|Jeda.
## BIN 2
0|Kalimat ajakan yang benar adalah ....|Ayo kita membaca buku.|Tolong tutup pintu.|Siapa namamu?|Adik sedang tidur.|Ayo menunjukkan ajakan.
0|Kalimat perintah yang sopan diawali kata ....|tolong|ayo|mari|siapa|Tolong.
1|Gambar anak bermain layang-layang di lapangan. Tempatnya adalah ....|lapangan|kamar|dapur|kelas|Lapangan.
1|Pertanyaan untuk mengetahui kegiatan adalah ....|sedang apa|siapa|di mana|kapan|Sedang apa.
2|Ibu dari ayah disebut ....|nenek|bibi|kakak|adik|Nenek.
2|Saudara laki-laki ibu disebut ....|paman|kakek|kakak|adik|Paman.
3|Kalimat Hobiku membaca menceritakan ....|hobi|nama|umur|alamat|Hobi.
3|Penulisan kalimat tentang diri yang benar adalah ....|Namaku Dodi.|namaku dodi.|Namaku dodi|namaku Dodi|Kapital dan titik.
4|Lawan kata besar adalah ....|kecil|tinggi|panas|cepat|Kecil.
4|Lawan kata terang adalah ....|gelap|besar|dingin|lambat|Gelap.
5|Langkah kedua mencuci tangan adalah ....|memberi sabun|mengeringkan tangan|membilas|menggosok sela jari|Beri sabun.
5|Jika petunjuk kurang jelas, kita ....|bertanya dengan sopan|marah|diam|pergi|Bertanya.
=0|Kata ajakan yang lain selain ayo adalah ....|mari|Mari.
=1|Pertanyaan untuk mengetahui waktu adalah ....|kapan|Kapan.
=2|Ayah dari ayah disebut ....|kakek|Kakek.
=4|Lawan kata dingin adalah ....|panas|Panas.
=5|Langkah terakhir mencuci tangan adalah mengeringkan ....|tangan|Tangan.
## PPK 1
0|Simbol sila kedua adalah ....|rantai|bintang|padi dan kapas|kepala banteng|Rantai.
0|Pohon beringin adalah simbol sila ke ....|tiga|satu|dua|lima|Sila ketiga.
1|Bhinneka Tunggal Ika tertulis pada ... Garuda.|pita|sayap|perisai|ekor|Pita.
1|Lambang negara Indonesia adalah ....|Garuda Pancasila|Merah Putih|Indonesia Raya|Monas|Garuda Pancasila.
2|Contoh bersyukur kepada Tuhan adalah ....|berdoa sebelum tidur|mengeluh|membuang makanan|marah|Berdoa.
2|Bersyukur sebagai ciptaan Tuhan sesuai sila ke ....|satu|dua|tiga|empat|Sila pertama.
3|Teman meminjam penghapus. Sikap kita adalah ....|meminjamkan|menolak sambil mengejek|menyembunyikan|marah|Meminjamkan.
3|Menolong teman yang jatuh sesuai sila ke ....|dua|satu|tiga|lima|Sila kedua.
4|Contoh disiplin waktu adalah ....|datang ke sekolah tepat waktu|tidur larut malam|menunda PR|terlambat upacara|Tepat waktu.
4|Jadwal kegiatan membantu kita ....|disiplin|malas|terlambat|lupa|Disiplin.
5|Mendapat makanan bergizi termasuk ... anak.|hak|kewajiban|larangan|hukuman|Hak.
5|Merapikan mainan sendiri termasuk ... anak.|kewajiban|hak|hadiah|larangan|Kewajiban.
=0|Simbol sila keempat adalah kepala ....|banteng|Banteng.
=1|Arti Bhinneka Tunggal Ika adalah berbeda-beda tetapi tetap ....|satu|Satu.
=3|Mengejek teman adalah perbuatan yang tidak ....|baik;terpuji|Tidak baik.
=4|Bangun pagi dan tidur tepat waktu adalah contoh sikap ....|disiplin|Disiplin.
=5|Hak dan kewajiban harus ....|seimbang|Seimbang.
## PPK 2
0|Pencipta lagu Indonesia Raya adalah ....|W.R. Supratman|Ismail Marzuki|Ibu Sud|Kusbini|W.R. Supratman.
0|Sikap saat menyanyikan Indonesia Raya adalah ....|berdiri tegak|berlari|duduk santai|bercanda|Berdiri tegak.
1|Saat bendera dikibarkan, peserta upacara ....|memberi hormat|duduk|mengobrol|bermain|Memberi hormat.
1|Petugas yang mengibarkan bendera disebut ....|pengibar bendera|pembina upacara|paduan suara|pembawa doa|Pengibar bendera.
2|Teman di kelas berbeda suku dan agama. Sikap kita adalah ....|tetap berteman dan menghargai|menjauhi|mengejek|memusuhi|Menghargai.
2|Perbedaan di kelas membuat kelas menjadi ....|beragam dan indah|kacau|buruk|sepi|Indah.
3|Berbicara bersama untuk mengambil keputusan disebut ....|musyawarah|bertengkar|bermain|bernyanyi|Musyawarah.
3|Musyawarah sesuai sila ke ....|empat|satu|dua|lima|Sila keempat.
4|Contoh sikap adil kepada saudara adalah ....|bergantian memakai mainan|merebut mainan|mengambil kue lebih banyak|tidak mau berbagi|Bergantian.
4|Bersikap adil sesuai sila ke ....|lima|satu|dua|tiga|Sila kelima.
5|Komodo adalah hewan khas dari ....|Indonesia|Australia|Afrika|Amerika|Indonesia.
5|Cara menjaga kekayaan alam adalah ....|tidak membuang sampah sembarangan|menebang hutan sembarangan|membakar hutan|merusak terumbu karang|Jaga alam.
=0|Lagu kebangsaan Indonesia adalah Indonesia ....|Raya|Raya.
=1|Upacara bendera di sekolah biasanya dilaksanakan hari ....|Senin|Senin.
=3|Hasil musyawarah dijalankan secara ....|bersama|Bersama.
=4|Kue untuk kakak dan adik dibagi sama ....|banyak;rata|Sama banyak.
=5|Sawah menghasilkan ....|padi|Padi.
## SBD 1
0|Warna daun segar adalah ....|hijau|merah|biru|ungu|Hijau.
0|Warna langit cerah adalah ....|biru|hitam|cokelat|merah|Biru.
1|Bentuk dasar untuk menggambar matahari adalah ....|lingkaran|segitiga|persegi|garis|Lingkaran.
1|Atap rumah digambar dengan bentuk ....|segitiga|lingkaran|bintang|hati|Segitiga.
2|Karya seni dengan menempel potongan bahan disebut ....|kolase|lukisan|patung|tari|Kolase.
2|Bahan kolase dari alam adalah ....|daun kering|plastik keras|besi|kaca|Daun kering.
3|Bunyi guntur terdengar ....|keras|lembut|pelan|sunyi|Keras.
3|Contoh bunyi alam adalah ....|hujan|bel|klakson|televisi|Hujan.
4|Rebana dimainkan dengan cara ....|dipukul|ditiup|dipetik|digesek|Dipukul.
4|Contoh alat musik ritmis adalah ....|marakas|seruling|piano|gitar|Marakas.
5|Lagu Manuk Dadali berasal dari ....|Jawa Barat|Papua|Maluku|Bali|Jawa Barat.
5|Lagu Ampar-Ampar Pisang berasal dari ....|Kalimantan Selatan|Jawa Tengah|Papua|Sumatra Barat|Kalimantan Selatan.
=0|Warna pisang matang adalah ....|kuning|Kuning.
=2|Untuk menempelkan kertas pada kolase kita memakai ....|lem|Lem.
=3|Bunyi bisikan terdengar ....|lembut;pelan|Lembut.
=4|Marakas dimainkan dengan cara ....|digoyang;digoyangkan|Digoyang.
=5|Lagu Yamko Rambe Yamko berasal dari ....|Papua|Papua.
## SBD 2
0|Gerak tari menirukan burung dilakukan dengan ....|mengepakkan tangan|melompat|merangkak|berguling|Mengepak.
0|Gerak tari dilakukan sesuai ....|irama musik|warna baju|cuaca|jam|Irama.
1|Garis yang dibentuk penari saat menari disebut ....|pola lantai|kostum|iringan|properti|Pola lantai.
1|Penari bergandengan membentuk pola ....|lingkaran|zig-zag|titik|garis miring|Lingkaran.
2|Bahan untuk mencetak gambar adalah ....|daun|batu besar|besi|kaca|Daun.
2|Saat mencetak, cat dipakai ....|secukupnya|sebanyak mungkin|tidak dipakai|diminum|Secukupnya.
3|Teknik membentuk plastisin menjadi panjang disebut ....|memilin|membulatkan|memipihkan|mencubit|Memilin.
3|Plastisin disimpan di wadah ... supaya tidak kering.|tertutup|terbuka|basah|panas|Tertutup.
4|Lagu Nina Bobo bertempo ....|lambat|cepat|sangat cepat|berubah-ubah|Lambat.
4|Cepat lambatnya lagu disebut ....|tempo|nada|lirik|judul|Tempo.
5|Botol bekas bisa dihias menjadi ....|pot bunga|sepatu|makanan|baju|Pot bunga.
5|Menghias barang bekas membantu mengurangi ....|sampah|teman|nilai|waktu|Sampah.
=0|Gerak tari menirukan kelinci dilakukan dengan ....|melompat|Melompat.
=1|Pola lantai yang berbelok-belok disebut ....|zig-zag;zigzag|Zig-zag.
=3|Teknik membentuk plastisin menjadi bola disebut ....|membulatkan|Membulatkan.
=4|Lagu gembira biasanya bertempo ....|cepat|Cepat.
=5|Kaleng bekas bisa dijadikan ....|celengan|Celengan.
## PJOK 1
0|Saat berjalan maju, tangan diayun ....|berlawanan dengan kaki|bersamaan dengan kaki|ke atas|tidak diayun|Berlawanan.
0|Berjalan mundur dilakukan dengan ....|pelan dan hati-hati|cepat sekali|mata terpejam|melompat|Pelan.
1|Contoh gerak keseimbangan adalah ....|sikap pesawat terbang|berlari kencang|melempar bola|menendang bola|Pesawat terbang.
1|Berdiri dengan satu kaki melatih ....|keseimbangan|kecepatan|kekuatan tangan|pernapasan|Keseimbangan.
2|Menggerakkan lengan membentuk lingkaran disebut ....|memutar lengan|mengayun lengan|menekuk lengan|meluruskan lengan|Memutar.
2|Mengayun lengan dilakukan ke arah ....|depan dan belakang|atas dan bawah saja|kanan saja|kiri saja|Depan belakang.
3|Dalam permainan kucing dan tikus, kucing bertugas ....|menangkap tikus|melindungi tikus|diam|bernyanyi|Menangkap.
3|Permainan kucing dan tikus melatih ....|kelincahan|kemalasan|ketakutan|kesombongan|Kelincahan.
4|Merangkak dilakukan dengan ....|tangan dan lutut|kepala|perut|satu kaki|Tangan dan lutut.
4|Latihan berguling dilakukan di atas ....|matras|lantai keras|aspal|batu|Matras.
5|Senam irama diiringi ....|musik|peluit|lonceng|sirene|Musik.
5|Gerakan senam irama mengikuti ....|hitungan|warna|cuaca|bentuk|Hitungan.
6|Tali untuk lompat tali bisa dibuat dari ....|karet gelang|kaca|besi|kayu|Karet gelang.
6|Saat mendarat dalam lompat tali, lutut sebaiknya ....|sedikit ditekuk|lurus kaku|diangkat|dikunci|Ditekuk.
=0|Saat berjalan maju, bagian kaki yang menyentuh tanah lebih dulu adalah ....|tumit|Tumit.
=1|Saat latihan keseimbangan, pandangan lurus ke ....|depan|Depan.
=3|Saat bermain kita harus bersikap ....|sportif|Sportif.
=5|Senam irama biasanya dihitung satu sampai ....|delapan;8|Delapan.
=6|Lompat tali termasuk permainan ....|tradisional|Tradisional.
## PJOK 2
0|Pemanasan dilakukan ... olahraga.|sebelum|sesudah|tanpa|saat tidur|Sebelum.
0|Pemanasan bertujuan untuk ....|mencegah cedera|membuat lapar|membuat lelah|membuat ngantuk|Mencegah cedera.
1|Contoh gerakan pendinginan adalah ....|jalan santai|lari cepat|lompat tinggi|lempar bola|Jalan santai.
1|Pendinginan membuat napas kembali ....|normal|cepat|berhenti|terengah-engah|Normal.
2|Makanan yang membantu tubuh tumbuh adalah ....|telur|permen|soda|keripik|Telur.
2|Minuman yang paling sehat adalah ....|air putih|sirup|soda|kopi|Air putih.
3|Sikat gigi sebaiknya dilakukan ....|pagi dan malam sebelum tidur|seminggu sekali|siang saja|saat bermain|Pagi dan malam.
3|Makanan yang bisa membuat gigi berlubang jika berlebihan adalah ....|permen|sayur|ikan|air putih|Permen.
4|Sebelum tidur sebaiknya kita ....|mematikan gawai|bermain gawai|makan permen|minum kopi|Matikan gawai.
4|Anak seusia kelas 1 perlu tidur sekitar ....|10 jam|2 jam|4 jam|20 jam|Sekitar 10 jam.
5|Contoh bola kecil adalah ....|bola tenis|bola basket|bola voli|bola sepak|Bola tenis.
5|Saat menangkap bola, mata selalu melihat ....|bola|langit|tanah|teman lain|Bola.
6|Tempat bermain yang aman adalah ....|lapangan sekolah|jalan raya|pinggir sungai|atap rumah|Lapangan sekolah.
6|Jika ada teman terluka saat bermain, kita ....|memberi tahu orang dewasa|meninggalkannya|tertawa|diam|Beri tahu orang dewasa.
=0|Pemanasan dimulai dari bagian ....|kepala|Kepala.
=1|Pendinginan dilakukan ... olahraga.|sesudah;setelah|Sesudah.
=3|Alat untuk membersihkan gigi adalah sikat ....|gigi|Gigi.
=5|Menangkap bola dilakukan dengan ... tangan.|dua;kedua|Dua tangan.
=6|Tempat bermain harus jauh dari jalan ....|raya|Raya.
## PAI 1
0|Huruf hijaiyah yang bertitik satu di bawah adalah ....|ba|ta|tsa|jim|Ba.
0|Huruf hijaiyah yang pertama adalah ....|alif|ba|ta|ya|Alif.
1|Huruf yang seperti dal ditambah satu titik adalah ....|dzal|ra|zai|sin|Dzal.
1|Huruf syin memiliki ... titik.|tiga|satu|dua|empat|Tiga.
2|Huruf qaf memiliki ... titik.|dua|satu|tiga|empat|Dua.
2|Huruf yang seperti tha ditambah satu titik adalah ....|zha|'ain|ghain|fa|Zha.
3|Huruf ya bertitik dua di ....|bawah|atas|samping|tengah|Bawah.
3|Gabungan huruf lam dan alif disebut ....|lam alif|lam mim|alif lam|mim alif|Lam alif.
4|Harakat fathah terletak di ... huruf.|atas|bawah|samping|tengah|Atas.
4|Huruf berharakat fathah dibaca dengan bunyi ....|a|i|u|e|Bunyi a.
5|Harakat kasrah terletak di ... huruf.|bawah|atas|samping|tengah|Bawah.
5|Ta berharakat kasrah dibaca ....|ti|ta|tu|te|Ti.
=0|Huruf ta bertitik dua di ....|atas|Atas.
=1|Huruf ra bertitik ....|nol;tidak ada;tidak bertitik|Tanpa titik.
=3|Huruf hijaiyah yang terakhir adalah ....|ya|Ya.
=4|Tanda baca pada huruf hijaiyah disebut ....|harakat|Harakat.
=5|Huruf berharakat kasrah dibaca dengan bunyi ....|i|I.
## PAI 2
0|Huruf berharakat dammah dibaca dengan bunyi ....|u|a|i|o|Bunyi u.
0|Mim berharakat dammah dibaca ....|mu|ma|mi|me|Mu.
1|Fathatain dibaca ....|an|in|un|a|An.
1|Tanwin adalah harakat ....|ganda|tunggal|panjang|mati|Ganda.
2|Sebelum belajar sebaiknya kita ....|berdoa|bermain|tidur|marah|Berdoa.
2|Doa sebelum belajar memohon agar ilmu ....|bertambah dan mudah dipahami|cepat lupa|hilang|sulit|Ilmu bertambah.
3|Makan dan minum sebaiknya memakai tangan ....|kanan|kiri|kaki|siku|Kanan.
3|Sebelum makan kita membaca ....|basmalah|hamdalah|takbir|tasbih|Basmalah.
4|Salat yang dikerjakan saat matahari terbenam adalah ....|magrib|subuh|zuhur|isya|Magrib.
4|Salat subuh dikerjakan ... rakaat.|dua|tiga|empat|lima|Dua.
5|Allah memerintahkan Nabi Nuh membuat ....|kapal|rumah|masjid|sumur|Kapal.
5|Orang yang selamat dari banjir pada masa Nabi Nuh adalah orang yang ....|beriman|sombong|mengejek|ingkar|Beriman.
=0|Dammah bentuknya seperti huruf ... kecil.|wau|Wau.
=1|Kasratain dibaca ....|in|In.
=3|Setelah makan kita ....|berdoa|Berdoa.
=4|Salat wajib dalam sehari ada ... waktu.|lima;5|Lima.
=5|Kisah Nabi Nuh mengajarkan sikap sabar dan ... kepada Allah.|taat|Taat.
## SUN 1
0|Patlot dina basa Indonesia hartina ....|pensil|penghapus|penggaris|buku|Pensil.
0|Pamupus hartina ....|penghapus|pensil|tas|meja|Penghapus.
1|Rebo dina basa Indonesia hartina ....|Rabu|Selasa|Kamis|Jumat|Rabu.
1|Poé sanggeus Senén nyaéta ....|Salasa|Rebo|Kemis|Minggu|Salasa.
2|Dahar hartina ....|makan|minum|tidur|mandi|Makan.
2|Sangu hartina ....|nasi|air|teh|susu|Nasi.
3|Buruan hartina ....|halaman|dapur|kamar|atap|Halaman.
3|Indung masak di ....|dapur|buruan|tepas|hateup|Dapur.
4|Hatur nuhun hartina ....|terima kasih|maaf|permisi|selamat pagi|Terima kasih.
4|Kecap nu diucapkeun waktu permisi nyaéta ....|punten|mangga|sumuhun|hatur nuhun|Punten.
5|Calana hartina ....|celana|baju|sepatu|topi|Celana.
5|Sapatu hartina ....|sepatu|sandal|kaus kaki|celana|Sepatu.
=0|Panggaris dina basa Indonesia hartina ....|penggaris|Penggaris.
=1|Poé dina basa Indonesia hartina ....|hari|Hari.
=2|Nginum hartina ....|minum|Minum.
=3|Imah dina basa Indonesia hartina ....|rumah|Rumah.
=4|Kecap mangga dipaké pikeun ....|mempersilakan|Mempersilakan.
## SUN 2
0|Kembang hartina ....|bunga|pohon|daun|buah|Bunga.
0|Cau hartina ....|pisang|kelapa|mangga|jeruk|Pisang.
1|Tiris hartina ....|dingin|panas|hujan|angin|Dingin.
1|Lamun hujan, urang maké ....|payung|kacamata|topi pantai|sendal|Payung.
2|Hudang hartina ....|bangun|tidur|mandi|makan|Bangun.
2|Isuk-isuk hartina ....|pagi|siang|sore|malam|Pagi.
3|Maung hartina ....|harimau|ular|burung|monyet|Harimau.
3|Manuk hartina ....|burung|ikan|ular|kucing|Burung.
4|Sabelas hartina ....|sebelas|dua belas|sepuluh|tiga belas|Sebelas.
4|Tilu belas hartina ....|tiga belas|dua belas|empat belas|lima belas|Tiga belas.
5|Babasan gedé hulu hartina ....|sombong|rajin|sabar|penakut|Sombong.
5|Babasan hampang birit hartina ....|rajin|malas|sombong|penakut|Rajin.
=0|Tangkal hartina ....|pohon|Pohon.
=1|Méga hartina ....|awan|Awan.
=2|Indit hartina ....|berangkat|Berangkat.
=3|Oray hartina ....|ular|Ular.
=5|Babasan leutik haté hartina ....|penakut|Penakut.
"""

BANK += """
## MAT|Berat dan ringan benda
Benda yang lebih ringan dari batu bata adalah …|kertas|meja|lemari|batu besar|Kertas ringan.
B|Benda yang kecil belum tentu ringan.|Kelereng besi kecil tetapi berat.
## MAT|Membaca jam tepat
Pukul 6 pagi biasanya kita …|bangun tidur|tidur siang|makan malam|pulang sekolah|Bangun pagi.
Jarum panjang menunjuk angka 12 dan jarum pendek menunjuk angka 3. Pukul …|3|12|6|9|Pukul 3.
B|Pada jam tepat, jarum panjang berada di angka 12.|Jam tepat.
S|Jarum panjang menunjukkan jam.|Jarum pendek menunjukkan jam.
=|Jarum pendek di angka 10, jarum panjang di angka 12. Pukul …|10;sepuluh|Pukul 10.
## BIN|Menyusun kata menjadi kalimat
Kata kucing, minum, susu disusun menjadi …|Kucing minum susu.|Susu minum kucing.|Minum susu kucing.|Kucing susu minum.|Siapa, kegiatan, benda.
Kata pertama dalam kalimat ditulis dengan huruf …|kapital|kecil|miring|tebal|Huruf kapital.
Kalimat yang benar susunannya adalah …|Ibu membeli sayur.|Sayur membeli ibu.|Membeli ibu sayur.|Ibu sayur membeli.|Ibu membeli sayur.
B|Kalimat Adik tidur di kamar susunannya benar.|Susunannya benar.
S|Kalimat Bola menendang Dodi susunannya benar.|Yang benar Dodi menendang bola.
=|Kata ayah, mobil, mencuci disusun menjadi Ayah mencuci …|mobil|Ayah mencuci mobil.
Jumlah kata pada kalimat Rina makan roti adalah …|tiga|dua|empat|lima|Rina, makan, roti.
## BIN|Huruf ganda ng dan ny
Kata yang memakai ng di tengah adalah …|bunga|nyanyi|meja|kursi|Bu-nga.
Kata yang diawali ny adalah …|nyamuk|kancing|pisang|bunga|Nyamuk.
Kata yang diakhiri ng adalah …|piring|nyanyi|buku|bola|Pi-ring.
Kata banyak memakai huruf ganda …|ny|ng|kh|sy|Ba-nyak.
Kata pisang memakai huruf ganda …|ng|ny|kh|sy|Pi-sang.
B|Kata kancing memakai huruf ng.|Kan-cing.
S|Kata nyala memakai huruf ng.|Nyala memakai ny.
B|Kata bunga dibaca bu-nga.|Bu-nga.
=|Buah berwarna kuning yang memakai ng adalah …|pisang|Pisang.
=|Kegiatan bernyanyi berasal dari kata …|nyanyi|Nyanyi.
Hewan yang memakai ng adalah …|angsa|nyamuk|kucing besar|sapi|Angsa memakai ng.
Kata yang tidak memakai huruf ganda adalah …|meja|bunga|nyamuk|piring|Meja.
## BIN|Membaca puisi anak
Puisi tentang bintang sebaiknya dibaca dengan ekspresi …|kagum dan gembira|marah|takut|bosan|Kagum dan gembira.
Bagian puisi yang ditulis dalam satu deretan disebut …|baris|halaman|judul|paragraf|Baris.
Judul puisi ditulis di bagian …|atas|bawah|tengah baris|samping|Atas.
B|Puisi bisa bercerita tentang ibu, alam, atau sekolah.|Tema puisi beragam.
S|Membaca puisi harus dengan suara sangat pelan sampai tidak terdengar.|Suara jelas.
=|Puisi Ibu biasanya berisi rasa … kepada ibu.|sayang;kasih sayang|Sayang.
Membacakan puisi di depan kelas melatih rasa …|percaya diri|malas|takut|marah|Percaya diri.
## BIN|Kalimat perintah dan ajakan
Kalimat perintah adalah …|Tutup pintunya, ya.|Ayo kita bermain.|Aku suka apel.|Siapa namamu?|Meminta melakukan sesuatu.
Kalimat ajakan untuk membersihkan kelas adalah …|Ayo kita membersihkan kelas.|Kelas itu bersih.|Siapa yang menyapu?|Kelas sangat kotor.|Ayo mengajak.
Kata tolong membuat kalimat perintah menjadi …|sopan|kasar|lucu|panjang|Sopan.
B|Mari kita makan bersama termasuk kalimat ajakan.|Ajakan.
S|Tolong ambilkan air termasuk kalimat ajakan.|Kalimat perintah.
=|Tolong … sampah itu ke tempat sampah. (kata kerja membuang)|buang;buanglah|Buang.
## BIN|Menulis kalimat tentang diriku
Kalimat yang menceritakan alamat adalah …|Rumahku di Jalan Melati.|Aku suka berenang.|Umurku tujuh tahun.|Namaku Sinta.|Alamat.
Kalimat yang menceritakan umur adalah …|Umurku tujuh tahun.|Namaku Sinta.|Aku suka apel.|Rumahku di Bogor.|Umur.
Kalimat yang menceritakan makanan kesukaan adalah …|Aku suka nasi goreng.|Umurku tujuh tahun.|Namaku Dodi.|Rumahku di Bandung.|Kesukaan.
B|Kalimat tentang diri ditulis dengan rapi.|Rapi.
S|Nama sendiri boleh ditulis dengan huruf kecil semua.|Diawali huruf kapital.
=|Kalimat tentang diri diawali huruf …|kapital;besar|Kapital.
Setelah menulis kalimat tentang diri, kita bisa … kepada keluarga.|membacakannya|menyobeknya|membuangnya|menyembunyikannya|Membacakan.
## BIN|Mendengarkan petunjuk
Petunjuk menyikat gigi dimulai dengan …|memberi pasta gigi pada sikat|berkumur|menyimpan sikat|tidur|Pasta gigi dulu.
Saat guru memberi petunjuk, kita sebaiknya …|memperhatikan|mengobrol|bermain|menggambar sendiri|Memperhatikan.
Kata yang menunjukkan urutan dalam petunjuk adalah …|pertama|merah|besar|cantik|Pertama.
B|Kata lalu dan kemudian menunjukkan urutan.|Penanda urutan.
S|Kita tidak perlu mengingat urutan petunjuk.|Urutan perlu diingat.
=|Kata penanda urutan terakhir adalah …|terakhir;akhirnya|Terakhir.
## PPK|Simbol sila-sila Pancasila
Sila yang bersimbol rantai adalah sila ke …|dua|satu|tiga|empat|Rantai sila kedua.
B|Bintang adalah simbol sila pertama.|Sila pertama.
## PPK|Menyayangi teman
Teman lupa membawa bekal. Sikap kita adalah …|berbagi bekal|menertawakan|pindah tempat|diam saja|Berbagi.
Teman sedang sedih. Sebaiknya kita …|menghiburnya|mengejeknya|menjauhinya|membiarkannya|Menghibur.
Kata yang baik diucapkan kepada teman adalah …|terima kasih|bodoh|pergi sana|jelek|Terima kasih.
B|Mengajak teman baru bermain termasuk menyayangi teman.|Peduli.
S|Memukul teman yang tidak mau meminjamkan mainan boleh dilakukan.|Tidak boleh memukul.
=|Jika kita salah kepada teman, kita meminta …|maaf|Maaf.
## PPK|Disiplin waktu
Bel masuk berbunyi. Sikap disiplin adalah …|segera masuk kelas|terus bermain|pulang|bersembunyi|Segera masuk.
Waktu untuk bermain sebaiknya …|setelah tugas selesai|sebelum bangun|saat pelajaran|saat upacara|Setelah tugas.
Benda yang membantu kita tepat waktu adalah …|jam|bantal|bola|sendok|Jam.
B|Orang yang disiplin tidak menunda pekerjaan.|Tidak menunda.
S|Terlambat datang ke sekolah adalah sikap disiplin.|Tidak disiplin.
=|Sebelum tidur, kita menyiapkan buku untuk … besok.|sekolah|Sekolah.
## PPK|Hak dan kewajiban anak di rumah
Mendapat waktu bermain termasuk …|hak|kewajiban|hukuman|tugas|Hak.
Membantu menyiram tanaman termasuk …|kewajiban|hak|hadiah|larangan|Kewajiban.
Orang tua memberi kita kasih sayang. Kita membalasnya dengan …|patuh dan membantu|membantah|malas|marah|Patuh dan membantu.
B|Merapikan mainan sendiri adalah kewajiban anak.|Kewajiban.
S|Anak hanya punya hak tanpa kewajiban.|Ada hak dan kewajiban.
=|Mendapat makanan bergizi adalah … anak.|hak|Hak.
## PPK|Lagu kebangsaan Indonesia Raya
Lagu Indonesia Raya dinyanyikan pertama kali pada peristiwa …|Sumpah Pemuda|Hari Ibu|Hari Pendidikan|Tahun Baru|Sumpah Pemuda 1928.
Saat Indonesia Raya dinyanyikan, sikap tangan yang benar adalah …|lurus di samping badan|di saku|di kepala|bertepuk|Lurus di samping.
Indonesia Raya adalah lagu …|kebangsaan|daerah|anak-anak|pop|Lagu kebangsaan.
B|Kita bangga menyanyikan lagu Indonesia Raya.|Bangga.
S|Indonesia Raya dinyanyikan sambil duduk santai.|Berdiri tegak.
=|Menyanyikan Indonesia Raya dengan sungguh-sungguh disebut …|khidmat|Khidmat.
Lagu Indonesia Raya dinyanyikan saat … bendera.|upacara|makan|tidur|bermain|Upacara.
## PPK|Musyawarah di keluarga
Contoh musyawarah di keluarga adalah …|memilih tempat liburan bersama|bertengkar memilih acara televisi|memaksa ikut kemauan adik|diam saja|Memilih bersama.
Pendapat orang lain sebaiknya …|dihargai|ditertawakan|diabaikan|dibantah keras|Dihargai.
Musyawarah membuat keputusan menjadi …|adil|kacau|curang|lama sekali|Adil.
B|Anak juga boleh menyampaikan pendapat dalam musyawarah keluarga.|Boleh berpendapat.
S|Musyawarah dilakukan sambil berteriak.|Dengan sopan.
=|Musyawarah sesuai dengan sila ke …|empat;keempat;4|Sila keempat.
Orang yang memimpin musyawarah di keluarga biasanya …|ayah atau ibu|tetangga|teman|orang asing|Orang tua.
## PPK|Adil kepada saudara
Jika ada dua anak dan satu sepeda, cara yang adil adalah …|bergantian memakai sepeda|kakak saja yang memakai|adik saja yang memakai|sepeda disimpan selamanya|Bergantian.
Membagi tugas rumah secara adil artinya …|semua mendapat bagian|satu orang mengerjakan semua|tidak ada yang bekerja|pilih yang disukai|Semua dapat bagian.
Sikap tidak adil membuat saudara merasa …|kecewa|senang|bangga|bersyukur|Kecewa.
B|Orang tua yang adil menyayangi semua anaknya.|Adil.
S|Adil berarti mengambil yang paling besar untuk diri sendiri.|Tidak adil.
=|Bermain bergantian adalah contoh sikap …|adil|Adil.
## SBD|Kolase dari kertas
Bahan kolase dari biji-bijian contohnya …|biji jagung|batu bata|paku|kaca|Biji jagung.
Kolase ikan bisa dibuat dari sobekan kertas …|warna-warni|hitam saja|transparan|tisu basah|Warna-warni.
Setelah kolase selesai, kita sebaiknya …|merapikan sisa bahan|membuang lem sembarangan|merobek karya|menginjaknya|Merapikan.
B|Kain perca bisa dipakai untuk kolase.|Kain perca.
S|Kolase harus dibuat dengan cat minyak.|Kolase ditempel.
=|Karya seni dengan menempel potongan bahan disebut …|kolase|Kolase.
Lem dioleskan pada …|pola gambar|tangan teman|meja guru|lantai|Pola gambar.
## SBD|Alat musik ritmis
Alat musik ritmis yang dimainkan dengan dipukul adalah …|gendang|marakas|kastanyet|tamborin digoyang|Gendang dipukul.
Kentongan dimainkan dengan cara …|dipukul dengan kayu|ditiup|dipetik|digesek|Dipukul.
Tamborin dimainkan dengan cara …|digoyang dan dipukul|ditiup|dipetik|digesek|Digoyang dan dipukul.
Alat musik ritmis berbeda dengan alat musik melodis karena …|tidak menghasilkan nada|lebih besar|lebih mahal|harus ditiup|Tidak bernada.
Contoh alat musik melodis adalah …|seruling|gendang|kastanyet|marakas|Seruling melodis.
B|Rebana termasuk alat musik ritmis.|Ritmis.
S|Seruling termasuk alat musik ritmis.|Seruling melodis.
B|Marakas bisa dibuat dari botol berisi beras.|Marakas buatan.
=|Gendang dimainkan dengan cara …|dipukul|Dipukul.
=|Alat musik ritmis berfungsi mengatur …|irama;ritme|Irama.
Alat musik dari kayu yang dipakai untuk tanda di pos ronda adalah …|kentongan|biola|piano|gitar|Kentongan.
Bunyi alat musik ritmis harus mengikuti … lagu.|ketukan|warna|judul|bahasa|Ketukan.
## SBD|Mencetak dengan pelepah dan daun
Mencetak dengan jari menghasilkan gambar …|sidik jari|lukisan cat minyak|patung|kolase|Sidik jari.
Pelepah pisang bisa dipakai untuk …|mencetak|menulis|menyanyi|menari|Mencetak.
Hasil cetakan sebaiknya dikeringkan dengan cara …|diangin-anginkan|dicuci|dilipat basah|dimasukkan ke air|Diangin-anginkan.
B|Mencetak bisa memakai potongan sayur.|Potongan sayur.
S|Daun yang dipakai mencetak harus dibakar dulu.|Tidak perlu dibakar.
=|Benda diberi pewarna lalu ditempelkan ke kertas. Kegiatan ini disebut …|mencetak|Mencetak.
Setelah mencetak, tangan kita sebaiknya …|dicuci|dibiarkan kotor|dilap ke baju|dijilat|Dicuci.
## SBD|Cepat lambat lagu
Lagu Balonku dinyanyikan dengan tempo …|cepat|lambat|sangat lambat|berhenti|Cepat.
Lagu Bintang Kecil dinyanyikan dengan tempo …|lambat|cepat|sangat cepat|terburu-buru|Lambat.
Untuk lagu yang tenang, kita bertepuk …|lambat|cepat sekali|tidak teratur|keras sekali|Lambat.
B|Tempo lagu bisa cepat atau lambat.|Tempo.
S|Semua lagu harus dinyanyikan dengan tempo cepat.|Tempo berbeda.
=|Lagu untuk menidurkan adik biasanya bertempo …|lambat|Lambat.
## PJOK|Berjalan maju mundur
Saat berjalan, badan sebaiknya …|tegak|membungkuk|miring|berjongkok|Tegak.
Berjalan mundur sebaiknya dilakukan di tempat yang …|lapang dan aman|ramai kendaraan|licin|banyak batu|Lapang dan aman.
Langkah saat berjalan mundur sebaiknya …|pendek dan pelan|panjang dan cepat|melompat|berlari|Pendek dan pelan.
B|Ayunan tangan membantu tubuh seimbang saat berjalan.|Seimbang.
S|Saat berjalan maju, pandangan ke bawah terus.|Pandangan ke depan.
=|Berjalan ke arah belakang disebut berjalan …|mundur|Mundur.
Berjalan termasuk gerak …|lokomotor|nonlokomotor|manipulatif|diam|Lokomotor berpindah tempat.
## PJOK|Permainan kucing dan tikus
Jika kucing berhasil menangkap tikus, maka …|berganti peran|permainan berhenti selamanya|kucing dihukum|semua pulang|Berganti peran.
Permainan kucing dan tikus sebaiknya dimainkan di …|lapangan|jalan raya|dapur|kamar sempit|Lapangan.
Gerakan utama dalam permainan kucing dan tikus adalah …|berlari dan menghindar|duduk|berenang|melempar|Berlari dan menghindar.
B|Sebelum bermain, kita menyepakati aturan permainan.|Aturan.
S|Pemain lingkaran boleh melepas tangan kapan saja.|Tetap bergandengan.
=|Anak yang mengejar dalam permainan ini berperan sebagai …|kucing|Kucing.
Bermain bersama teman membuat kita …|senang dan akrab|bermusuhan|sedih|kesepian|Senang.
## PJOK|Gerak merangkak dan berguling
Saat merangkak, punggung sebaiknya …|lurus|membungkuk tajam|miring|berputar|Lurus.
Hewan yang bergerak merangkak contohnya …|kucing berjalan|burung terbang|ikan berenang|kanguru melompat|Kucing.
Sebelum berguling, sebaiknya kita …|melakukan pemanasan|makan banyak|tidur|berlari kencang|Pemanasan.
B|Latihan berguling memerlukan pengawasan guru atau orang tua.|Pengawasan.
S|Berguling sebaiknya dilakukan di lantai berbatu.|Di matras.
=|Merangkak memakai kedua tangan dan kedua …|lutut|Lutut.
Gerak berguling melatih … tubuh.|kelenturan|kemalasan|kekakuan|ketakutan|Kelenturan.
## PJOK|Senam irama sederhana
Gerakan menepuk tangan di atas kepala termasuk gerakan …|tangan|kaki|kepala saja|perut|Gerakan tangan.
Senam irama sebaiknya dilakukan dengan …|gembira|cemberut|malas|terburu-buru|Gembira.
Sebelum senam irama sebaiknya kita …|pemanasan|makan banyak|tidur|minum soda|Pemanasan.
B|Senam irama melatih kekompakan saat dilakukan bersama.|Kompak.
S|Musik pada senam irama tidak berguna.|Musik mengatur gerak.
=|Senam yang diiringi musik disebut senam …|irama|Irama.
## PJOK|Pemanasan sebelum olahraga
Gerakan memutar bahu termasuk …|pemanasan|pendinginan|permainan|lomba|Pemanasan.
Pemanasan membuat otot menjadi …|siap|kaku|sakit|tegang|Siap.
Lama pemanasan sebaiknya …|beberapa menit|satu jam|satu detik|seharian|Beberapa menit.
B|Pemanasan dilakukan dari kepala sampai kaki.|Atas ke bawah.
S|Pemanasan dilakukan dengan gerakan sangat cepat dan kasar.|Pelan dan teratur.
=|Gerakan menekuk lutut termasuk … sebelum olahraga.|pemanasan|Pemanasan.
## PJOK|Pendinginan setelah olahraga
Pendinginan dilakukan supaya detak jantung kembali …|normal|cepat sekali|berhenti|naik|Normal.
Setelah pendinginan, kita sebaiknya …|minum air putih|minum soda|langsung tidur|berlari lagi|Minum air.
Gerakan pendinginan berbeda dari pemanasan karena dilakukan …|setelah olahraga|sebelum olahraga|tanpa olahraga|saat tidur|Setelah.
B|Duduk rileks sambil menarik napas termasuk pendinginan.|Rileks.
S|Pendinginan dilakukan dengan berlari secepatnya.|Gerakan pelan.
=|Gerakan meregangkan otot setelah olahraga disebut …|pendinginan;peregangan|Pendinginan.
Membuang napas pada pendinginan dilakukan lewat …|mulut|telinga|mata|hidung saja ditahan|Mulut.
## PJOK|Makanan sehat untuk tubuh
Makanan pokok orang Indonesia adalah …|nasi|keripik|permen|cokelat|Nasi.
Sayuran berwarna hijau contohnya …|bayam|wortel|tomat|terong|Bayam.
Buah yang berwarna kuning contohnya …|pisang|anggur ungu|semangka merah|apel merah|Pisang.
Lauk dari hewan contohnya …|ikan|tempe|tahu|bayam|Ikan.
Lauk dari tumbuhan contohnya …|tempe|ikan|ayam|telur|Tempe.
Sebelum makan kita mencuci …|tangan|kaki|rambut|baju|Tangan.
B|Sarapan pagi memberi tenaga untuk belajar.|Sarapan penting.
S|Minuman bersoda lebih sehat dari air putih.|Air putih lebih sehat.
B|Wortel baik untuk kesehatan mata.|Wortel.
=|Sayuran berwarna oranye yang baik untuk mata adalah …|wortel|Wortel.
=|Minum air putih yang cukup membuat tubuh tidak …|haus;dehidrasi|Tidak haus.
Jajan sembarangan bisa membuat …|sakit perut|sehat|kuat|pintar|Sakit perut.
## PJOK|Menjaga kebersihan gigi
Sikat gigi yang baik memiliki bulu yang …|lembut|keras sekali|tajam|panjang sekali|Lembut.
Pasta gigi dipakai …|secukupnya|sebanyak-banyaknya|tidak dipakai|ditelan|Secukupnya.
Kita sebaiknya memeriksakan gigi ke …|dokter gigi|tukang cukur|penjual sayur|montir|Dokter gigi.
B|Mengganti sikat gigi jika bulunya sudah rusak.|Ganti sikat.
S|Gigi tidak perlu disikat sebelum tidur.|Perlu disikat.
=|Gigi yang tidak dirawat bisa menjadi …|berlubang|Berlubang.
## PJOK|Istirahat dan tidur cukup
Kegiatan yang tepat sebelum tidur adalah …|membaca doa|bermain gawai|makan permen|berlari|Berdoa.
Tidur siang sebentar membuat tubuh …|segar kembali|lemas|sakit|lapar|Segar.
Kamar tidur sebaiknya …|bersih dan rapi|kotor|berantakan|banyak sampah|Bersih.
B|Bangun pagi membuat kita tidak terlambat sekolah.|Bangun pagi.
S|Tidur larut malam membuat kita segar di sekolah.|Mengantuk.
=|Waktu yang tepat untuk tidur malam bagi anak adalah sekitar pukul …|8;delapan;20.00|Sekitar pukul 8 malam.
## PJOK|Aman saat bermain
Sebelum bermain, kita memeriksa tempat bermain dari …|benda tajam|bunga|rumput|pohon rindang|Benda tajam.
Bermain di dekat kolam dalam tanpa orang dewasa itu …|berbahaya|aman|seru|wajib|Berbahaya.
Saat bermain, kita harus mengikuti …|aturan permainan|kemauan sendiri|keinginan teman nakal|orang asing|Aturan.
B|Bermain dengan aman membuat semua tetap sehat.|Aman.
S|Bermain lempar batu itu aman.|Berbahaya.
=|Jika ada teman terluka, kita memberi tahu orang …|dewasa;tua|Orang dewasa.
## PAI|Huruf hijaiyah tha sampai qaf
Huruf 'ain tidak memiliki …|titik|bentuk|nama|bunyi|Tanpa titik.
B|Huruf fa bertitik satu di atas.|Fa satu titik.
## PAI|Harakat fathah
Huruf ta berharakat fathah dibaca …|ta|ti|tu|te|Ta.
Huruf jim berharakat fathah dibaca …|ja|ji|ju|je|Ja.
Huruf dal berharakat fathah dibaca …|da|di|du|de|Da.
B|Fathah berbentuk garis kecil miring.|Garis miring di atas.
S|Fathah ditulis di bawah huruf.|Di atas.
=|Huruf kha berharakat fathah dibaca …|kha|Kha.
## PAI|Harakat kasrah
Huruf ra berharakat kasrah dibaca …|ri|ra|ru|re|Ri.
Huruf jim berharakat kasrah dibaca …|ji|ja|ju|je|Ji.
Huruf zai berharakat kasrah dibaca …|zi|za|zu|ze|Zi.
B|Kasrah berbentuk garis kecil miring di bawah huruf.|Di bawah.
S|Kasrah dibaca dengan bunyi a.|Kasrah bunyi i.
=|Huruf syin berharakat kasrah dibaca …|syi|Syi.
## PAI|Harakat dammah
Huruf fa berharakat dammah dibaca …|fu|fa|fi|fe|Fu.
Huruf lam berharakat dammah dibaca …|lu|la|li|le|Lu.
Huruf kaf berharakat dammah dibaca …|ku|ka|ki|ke|Ku.
B|Dammah ditulis di atas huruf.|Di atas.
S|Dammah dibaca dengan bunyi a.|Dammah bunyi u.
=|Huruf ya berharakat dammah dibaca …|yu|Yu.
## PAI|Tanwin
Huruf ta berharakat dammatain dibaca …|tun|tan|tin|tu|Tun.
Huruf ba berharakat kasratain dibaca …|bin|ban|bun|bi|Bin.
Huruf dal berharakat fathatain dibaca …|dan|din|dun|da|Dan.
Fathatain bentuknya seperti dua …|fathah|kasrah|titik|sukun|Dua fathah.
B|Kasratain berbentuk dua garis di bawah huruf.|Dua kasrah.
S|Dammatain dibaca in.|Dammatain un.
B|Tanwin selalu ada di huruf terakhir kata.|Di akhir kata.
=|Huruf jim berharakat fathatain dibaca …|jan|Jan.
## PAI|Doa sebelum dan sesudah belajar
Doa sebelum belajar dibaca …|sebelum belajar dimulai|setelah tidur siang|saat makan|saat bermain|Sebelum belajar.
Rabbi zidni ilma artinya Ya Tuhanku, tambahkanlah …|ilmuku|hartaku|mainanku|makananku|Ilmuku.
Orang yang rajin belajar dan berdoa akan mendapat ilmu yang …|bermanfaat|sia-sia|hilang|buruk|Bermanfaat.
B|Ilmu yang bermanfaat adalah ilmu yang diamalkan.|Diamalkan.
S|Berdoa dilakukan sambil bercanda.|Dengan tenang.
=|Sesudah belajar kita mengucapkan alhamdulillah sebagai tanda …|syukur|Syukur.
Sebelum belajar, sebaiknya kita membaca …|basmalah|istighfar saja|takbir|tasbih|Basmalah.
## PAI|Adab makan dan minum
Doa setelah makan diawali dengan …|alhamdulillah|bismillah|astaghfirullah|subhanallah|Alhamdulillah.
Minum sebaiknya dilakukan sambil …|duduk|berlari|berbaring|melompat|Duduk.
Makanan yang jatuh sebaiknya …|dibersihkan jika masih bersih|diinjak|ditertawakan|dilempar|Tidak mubazir.
B|Makan sambil berbicara keras tidak sopan.|Tidak sopan.
S|Makan dengan tangan kiri adalah adab yang baik.|Tangan kanan.
=|Bacaan sebelum makan adalah …|bismillah;basmalah|Bismillah.
## PAI|Salat lima waktu
Salat asar dikerjakan … rakaat.|empat|dua|tiga|lima|Empat.
Salat isya dikerjakan … rakaat.|empat|dua|tiga|lima|Empat.
Salat yang dikerjakan siang hari adalah …|zuhur|subuh|magrib|isya|Zuhur.
Salat yang dikerjakan pagi hari adalah …|subuh|asar|isya|magrib|Subuh.
Salat jumat dikerjakan oleh laki-laki pada hari …|Jumat|Senin|Rabu|Minggu|Jumat.
Sebelum salat kita harus …|berwudu|makan|tidur|bermain|Berwudu.
B|Salat lima waktu wajib bagi setiap muslim.|Wajib.
S|Salat magrib dikerjakan empat rakaat.|Tiga rakaat.
B|Salat subuh dikerjakan sebelum matahari terbit.|Sebelum terbit.
=|Salat yang dikerjakan saat matahari terbenam adalah …|magrib|Magrib.
=|Jumlah rakaat salat subuh adalah …|dua;2|Dua.
Urutan salat lima waktu dari pagi adalah subuh, zuhur, asar, magrib, dan …|isya|jumat|duha|tarawih|Isya.
## PAI|Kisah Nabi Nuh
Kaum Nabi Nuh yang tidak beriman …|tenggelam|selamat|naik kapal|ikut berdakwah|Tenggelam.
Nabi Nuh membuat kapal atas perintah …|Allah|raja|kaumnya|anaknya|Allah.
Sikap kaum Nabi Nuh saat melihat Nabi Nuh membuat kapal adalah …|mengejek|membantu|memuji|ikut beriman semua|Mengejek.
B|Nabi Nuh berdakwah dalam waktu yang sangat lama.|Lama sekali.
S|Nabi Nuh marah dan membalas ejekan kaumnya.|Nabi Nuh sabar.
=|Nabi Nuh adalah … Allah.|nabi;rasul|Nabi Allah.
Kita meneladani Nabi Nuh dengan bersikap …|sabar|sombong|pemarah|malas|Sabar.
## SUN|Kagiatan isuk-isuk
Saréngséna hudang, urang …|mandi|saré deui|ulin|nonton|Mandi.
Sarapan dina basa Indonesia hartina …|makan pagi|makan malam|tidur|mandi|Makan pagi.
Mandi isuk-isuk matak awak …|seger|kesel|gering|tunduh|Segar.
B|Abdi indit ka sakola sanggeus sarapan.|Urutan benar.
S|Indit ka sakola dilakukeun saméméh hudang.|Hudang heula.
=|Kagiatan nu terakhir isuk-isuk nyaéta … ka sakola.|indit|Indit.
"""

BANK += """
## PPK|Musyawarah di keluarga
B|Musyawarah melatih kita menghargai pendapat orang lain.|Menghargai pendapat.
S|Hasil musyawarah boleh dilanggar jika kita tidak suka.|Hasil dijalankan bersama.
## SBD|Alat musik ritmis
B|Kastanyet termasuk alat musik ritmis.|Ritmis.
S|Gitar termasuk alat musik ritmis.|Gitar melodis.
## PAI|Salat lima waktu
B|Salat zuhur dikerjakan empat rakaat.|Empat.
S|Salat isya dikerjakan pada pagi hari.|Malam hari.
"""
