TOPICS = ""
BANK = ""
SAS = ""

TOPICS += """
## MAT
# 1|Akar, SPLDV, dan Transformasi
@ Merasionalkan penyebut
min: 15
act: Rasionalkan 6/√3 dan 4/√2, lalu periksa hasilnya dengan kalkulator.
mis: hanya mengalikan penyebut dengan akar tanpa mengalikan pembilang
exp: Merasionalkan penyebut berarti mengubah pecahan berpenyebut bentuk akar menjadi penyebut bilangan rasional. Caranya mengalikan pembilang dan penyebut dengan akar yang sama. Contohnya a/√b = (a√b)/b. Hasil akhir disederhanakan jika memungkinkan.
ex: 6/√3 = 6√3/3 = 2√3. // 4/√2 = 4√2/2 = 2√2.
pt: Penyebut akar diubah rasional ; Kalikan pembilang dan penyebut dengan akar sama ; a/√b = a√b/b
sum: Penyebut rasional memudahkan perhitungan.
fig: table Bentuk awal | Hasil rasional ;; 6/√3 | 2√3 ;; 4/√2 | 2√2 ;; 10/√5 | 2√5 ;; 1/√2 | ½√2 ;; 3/√3 | √3 ;; 14/√7 | 2√7 ~ Merasionalkan penyebut.
@ Soal cerita SPLDV
min: 15
act: Buat soal cerita tentang harga dua jenis jajanan, lalu selesaikan dengan eliminasi.
mis: memisalkan variabel tanpa menuliskan artinya
exp: Soal cerita SPLDV diselesaikan dengan langkah: memisalkan besaran yang belum diketahui dengan variabel, menyusun dua persamaan dari informasi soal, menyelesaikan dengan eliminasi atau substitusi, lalu menjawab pertanyaan. Hasil perlu diperiksa dengan memasukkan ke persamaan awal.
ex: 2 pensil + 1 buku = Rp7.000 dan 1 pensil + 1 buku = Rp5.000, maka pensil Rp2.000. // Buku = Rp3.000.
pt: Misalkan variabel ; Susun dua persamaan ; Eliminasi atau substitusi lalu periksa
sum: SPLDV membantu memecahkan masalah dua besaran.
fig: table Persamaan | Penyelesaian ;; x + y = 5 dan x - y = 1 | x = 3, y = 2 ;; x + y = 10 dan x - y = 4 | x = 7, y = 3 ;; 2x + y = 7 dan x + y = 5 | x = 2, y = 3 ;; x + 2y = 8 dan x = 2 | y = 3, x = 2 ;; x + y = 6 dan 2x = 8 | x = 4, y = 2 ;; 3x + y = 10 dan x + y = 4 | x = 3, y = 1 ~ Contoh penyelesaian SPLDV.
@ Refleksi
min: 15
act: Gambar segitiga di kertas berpetak, lalu cerminkan terhadap sumbu X dan sumbu Y.
mis: menukar tanda koordinat yang salah saat refleksi
exp: Refleksi atau pencerminan memindahkan setiap titik bangun ke posisi bayangannya terhadap garis cermin. Bentuk dan ukuran bangun tidak berubah. Refleksi terhadap sumbu X: (x, y) → (x, -y). Terhadap sumbu Y: (x, y) → (-x, y). Terhadap garis y = x: (x, y) → (y, x).
ex: A(2, 3) dicerminkan terhadap sumbu X menjadi (2, -3). // A(2, 3) terhadap sumbu Y menjadi (-2, 3).
pt: Pencerminan terhadap garis ; Bentuk dan ukuran tetap ; Rumus sumbu X, sumbu Y, y = x
sum: Refleksi menghasilkan bayangan seperti di cermin.
fig: table Cermin | Bayangan titik (x, y) ;; sumbu X | (x, -y) ;; sumbu Y | (-x, y) ;; garis y = x | (y, x) ;; garis y = -x | (-y, -x) ;; titik asal | (-x, -y) ;; garis x = h | (2h - x, y) ~ Rumus refleksi.
@ Translasi
min: 15
act: Geser sebuah bidak catur tiga kotak ke kanan dan dua kotak ke atas, lalu tulis vektor pergeserannya.
mis: mengurangkan komponen translasi yang seharusnya dijumlahkan
exp: Translasi atau pergeseran memindahkan setiap titik bangun dengan jarak dan arah yang sama. Translasi ditulis T(a, b), dengan a pergeseran mendatar dan b pergeseran tegak. Rumusnya (x, y) → (x + a, y + b). Bentuk, ukuran, dan arah bangun tidak berubah.
ex: A(1, 2) ditranslasi T(3, 4) menjadi (4, 6). // T(-2, 0) berarti geser 2 satuan ke kiri.
pt: Pergeseran sama jarak dan arah ; Ditulis T(a, b) ; (x, y) → (x + a, y + b)
sum: Translasi hanya menggeser letak bangun.
fig: table Titik dan translasi | Bayangan ;; (1, 2) oleh T(3, 4) | (4, 6) ;; (0, 0) oleh T(2, 5) | (2, 5) ;; (5, 1) oleh T(-2, 3) | (3, 4) ;; (-1, 4) oleh T(1, -4) | (0, 0) ;; (3, -2) oleh T(0, 2) | (3, 0) ;; (2, 2) oleh T(-5, -5) | (-3, -3) ~ Contoh translasi.
@ Rotasi
min: 15
act: Putar sebuah buku 90° searah jarum jam di atas meja, lalu amati posisinya.
mis: menukar rotasi searah dan berlawanan arah jarum jam
exp: Rotasi atau perputaran memutar bangun terhadap titik pusat dengan sudut tertentu. Sudut positif berarti berlawanan arah jarum jam. Rotasi 90° terhadap titik asal: (x, y) → (-y, x). Rotasi 180°: (x, y) → (-x, -y). Rotasi -90° atau 270°: (x, y) → (y, -x).
ex: A(2, 1) dirotasi 90° menjadi (-1, 2). // A(2, 1) dirotasi 180° menjadi (-2, -1).
pt: Memutar terhadap titik pusat ; Sudut positif berlawanan jarum jam ; Rumus 90°, 180°, 270°
sum: Rotasi mengubah arah hadap bangun tanpa mengubah ukurannya.
fig: table Rotasi terhadap O | Bayangan titik (x, y) ;; 90° | (-y, x) ;; 180° | (-x, -y) ;; 270° | (y, -x) ;; -90° | (y, -x) searah jarum jam ;; 360° | (x, y) kembali ;; -180° | (-x, -y) searah ~ Rumus rotasi.
@ Dilatasi
min: 15
act: Perbesar gambar persegi di kertas berpetak dengan faktor skala 2 dari titik pojoknya.
mis: mengira faktor skala negatif memperbesar ke arah yang sama
exp: Dilatasi adalah perbesaran atau pengecilan bangun terhadap titik pusat dengan faktor skala k. Dilatasi terhadap titik asal: (x, y) → (kx, ky). Jika k > 1, bangun diperbesar. Jika 0 < k < 1, bangun diperkecil. Jika k negatif, bayangan berada di sisi berlawanan dari pusat.
ex: A(2, 3) dengan k = 2 menjadi (4, 6). // A(4, 8) dengan k = ½ menjadi (2, 4).
pt: Perbesaran atau pengecilan ; (x, y) → (kx, ky) ; k > 1 diperbesar, 0 < k < 1 diperkecil
sum: Dilatasi mengubah ukuran tetapi bentuk tetap sebangun.
fig: table Titik dan skala | Bayangan ;; (2, 3) dengan k = 2 | (4, 6) ;; (4, 8) dengan k = ½ | (2, 4) ;; (1, -2) dengan k = 3 | (3, -6) ;; (3, 1) dengan k = -1 | (-3, -1) ;; (6, 9) dengan k = ⅓ | (2, 3) ;; (-2, 5) dengan k = 2 | (-4, 10) ~ Contoh dilatasi.
# 2|Kuadrat, Kesebangunan, dan Peluang
@ Rumus abc persamaan kuadrat
min: 15
act: Selesaikan x² - 5x + 6 = 0 dengan pemfaktoran dan dengan rumus abc, lalu bandingkan.
mis: lupa tanda minus pada -b dalam rumus abc
exp: Persamaan kuadrat ax² + bx + c = 0 dapat diselesaikan dengan rumus abc: x = (-b ± √(b² - 4ac)) / 2a. Nilai b² - 4ac disebut diskriminan (D). Jika D > 0 ada dua akar real berbeda, D = 0 ada dua akar kembar, dan D < 0 tidak ada akar real.
ex: x² - 5x + 6 = 0 memiliki akar 2 dan 3. // x² + 2x + 1 = 0 memiliki D = 0.
pt: x = (-b ± √D) / 2a ; D = b² - 4ac ; D menentukan jenis akar
sum: Rumus abc dapat menyelesaikan semua persamaan kuadrat.
fig: table Persamaan | Akar-akar ;; x² - 5x + 6 = 0 | 2 dan 3 ;; x² - 4 = 0 | 2 dan -2 ;; x² + 2x + 1 = 0 | -1 kembar ;; x² - 7x + 12 = 0 | 3 dan 4 ;; x² - x - 6 = 0 | 3 dan -2 ;; x² - 6x + 9 = 0 | 3 kembar ~ Akar persamaan kuadrat.
@ Grafik fungsi kuadrat
min: 15
act: Buat tabel nilai f(x) = x² untuk x = -3 sampai 3, lalu gambar grafiknya.
mis: menghubungkan titik fungsi kuadrat dengan garis lurus
exp: Fungsi kuadrat berbentuk f(x) = ax² + bx + c dan grafiknya berupa parabola. Jika a > 0, parabola terbuka ke atas. Jika a < 0, parabola terbuka ke bawah. Nilai c adalah titik potong dengan sumbu Y. Titik potong dengan sumbu X diperoleh dari akar f(x) = 0.
ex: f(x) = x² terbuka ke atas. // f(x) = -x² + 4 terbuka ke bawah dan memotong sumbu Y di 4.
pt: Grafik parabola ; a > 0 terbuka ke atas ; c titik potong sumbu Y
sum: Tanda a menentukan arah parabola.
fig: table x | f(x) = x² ;; -3 | 9 ;; -2 | 4 ;; -1 | 1 ;; 0 | 0 ;; 2 | 4 di kanan ;; 3 | 9 di kanan ~ Tabel nilai f(x) = x².
@ Sumbu simetri dan titik puncak
min: 15
act: Tentukan titik puncak f(x) = x² - 4x + 3 dan gambarkan sumbu simetrinya.
mis: lupa membagi dengan 2a saat mencari sumbu simetri
exp: Parabola memiliki sumbu simetri yang membaginya menjadi dua bagian sama. Persamaan sumbu simetri adalah x = -b/2a. Titik puncak atau titik balik berada pada sumbu simetri, dengan nilai y = f(-b/2a). Jika a > 0, titik puncak adalah titik minimum; jika a < 0, titik maksimum.
ex: f(x) = x² - 4x + 3 memiliki sumbu x = 2 dan puncak (2, -1). // f(x) = -x² + 6x memiliki puncak maksimum (3, 9).
pt: Sumbu simetri x = -b/2a ; Puncak (-b/2a, f(-b/2a)) ; Minimum atau maksimum
sum: Titik puncak menunjukkan nilai terkecil atau terbesar fungsi.
fig: table Fungsi | Sumbu simetri ;; x² - 4x + 3 | x = 2 ;; x² + 6x | x = -3 ;; -x² + 6x | x = 3 ;; x² - 2x + 5 | x = 1 ;; 2x² - 8x | x = 2 dengan a = 2 ;; x² | x = 0 ~ Sumbu simetri fungsi kuadrat.
@ Kesebangunan dan kekongruenan
min: 15
act: Ukur foto dan hasil cetak perbesarannya, lalu tentukan faktor skalanya.
mis: menganggap dua bangun sebangun cukup karena sudutnya sama tanpa memeriksa sisi
exp: Dua bangun sebangun jika sudut-sudut yang bersesuaian sama besar dan sisi-sisi yang bersesuaian sebanding. Dua bangun kongruen jika bentuk dan ukurannya sama persis. Syarat segitiga kongruen antara lain sisi-sisi-sisi, sisi-sudut-sisi, dan sudut-sisi-sudut. Kesebangunan dipakai untuk mengukur tinggi pohon dengan bayangan.
ex: Foto 4 × 6 dan 8 × 12 sebangun. // Tinggi pohon dihitung dari perbandingan bayangan.
pt: Sebangun: sudut sama, sisi sebanding ; Kongruen: sama persis ; Syarat sss, ss-sd-ss, sd-ss-sd
sum: Kesebangunan membantu mengukur benda yang sulit dijangkau.
fig: table Pasangan ukuran | Sebangun atau tidak ;; 4 × 6 dan 8 × 12 | sebangun ;; 3 × 5 dan 6 × 10 | sebangun skala 2 ;; 2 × 3 dan 4 × 5 | tidak sebangun ;; 5 × 5 dan 7 × 7 | sebangun persegi ;; 6 × 8 dan 3 × 4 | sebangun skala ½ ;; 2 × 4 dan 3 × 5 | tidak sebangun sisi ~ Pemeriksaan kesebangunan persegi panjang.
@ Luas permukaan kerucut dan bola
min: 15
act: Ukur jari-jari bola plastik, lalu hitung luas permukaannya.
mis: memakai tinggi kerucut sebagai garis pelukis
exp: Luas permukaan kerucut = πr(r + s), dengan s garis pelukis yang dihitung dari s² = r² + t². Luas selimut kerucut = πrs. Luas permukaan bola = 4πr². Luas belahan bola padat = 3πr².
ex: Kerucut r = 3, t = 4 memiliki s = 5. // Bola r = 7 cm, luas = 4 × 22/7 × 49 = 616 cm².
pt: Kerucut πr(r + s) ; s² = r² + t² ; Bola 4πr²
sum: Garis pelukis penting dalam rumus kerucut.
fig: table Jari-jari bola | Luas permukaan ;; 7 cm | 616 cm² ;; 14 cm | 2.464 cm² ;; 10 cm | 1.256 cm² ;; 21 cm | 5.544 cm² ;; 3,5 cm | 154 cm² ;; 5 cm | 314 cm² ~ Luas permukaan bola.
@ Ruang sampel dan titik sampel
min: 15
act: Tulis semua hasil pelemparan dua koin, lalu hitung banyak ruang sampelnya.
mis: menghitung hasil (A, G) dan (G, A) sebagai satu titik sampel
exp: Ruang sampel adalah himpunan semua hasil yang mungkin dari suatu percobaan. Setiap anggota ruang sampel disebut titik sampel. Ruang sampel dapat disusun dengan mendaftar, tabel, atau diagram pohon. Pelemparan satu dadu memiliki 6 titik sampel, sedangkan dua koin memiliki 4 titik sampel.
ex: Dua koin: AA, AG, GA, GG. // Dua dadu memiliki 36 titik sampel.
pt: Himpunan semua hasil ; Anggotanya titik sampel ; Daftar, tabel, diagram pohon
sum: Ruang sampel adalah dasar menghitung peluang.
fig: table Percobaan | Banyak titik sampel ;; satu koin | 2 ;; dua koin | 4 ;; tiga koin | 8 ;; satu dadu | 6 ;; dua dadu | 36 ;; satu koin dan satu dadu | 12 ~ Banyak titik sampel.

## BIN
# 1|Kebahasaan dan Teks Fungsional
@ Kalimat majemuk bertingkat
min: 15
act: Ubah lima kalimat tunggal menjadi kalimat majemuk bertingkat memakai konjungsi yang berbeda.
mis: menyamakan kalimat majemuk bertingkat dengan setara
exp: Kalimat majemuk bertingkat terdiri atas induk kalimat dan anak kalimat yang kedudukannya tidak setara. Anak kalimat dihubungkan dengan konjungsi seperti karena, ketika, jika, agar, dan meskipun. Kalimat majemuk setara memakai konjungsi dan, atau, tetapi.
ex: Ia tidak masuk sekolah karena sakit. // Jika hujan, kami belajar di rumah.
pt: Induk dan anak kalimat ; Konjungsi karena, jika, agar ; Berbeda dengan majemuk setara
sum: Kalimat majemuk bertingkat menghubungkan gagasan pokok dan keterangan.
fig: table Konjungsi | Hubungan ;; karena | sebab ;; ketika | waktu ;; jika | syarat ;; agar | tujuan ;; meskipun | konsesif ;; seperti | perbandingan ~ Konjungsi kalimat majemuk bertingkat.
@ Istilah ilmiah
min: 15
act: Kumpulkan sepuluh istilah ilmiah dari buku IPA, lalu tulis artinya dengan bahasamu.
mis: memakai istilah ilmiah tanpa memahami artinya
exp: Istilah ilmiah adalah kata atau gabungan kata yang maknanya khusus dalam bidang ilmu tertentu. Istilah dipakai dalam teks laporan, eksplanasi, dan karya ilmiah agar tepat. Contohnya fotosintesis, evaporasi, dan inflasi. Banyak istilah berasal dari bahasa Latin, Yunani, atau Inggris yang disesuaikan.
ex: Evaporasi berarti penguapan. // Inflasi berarti kenaikan harga secara umum.
pt: Makna khusus bidang ilmu ; Dipakai dalam teks ilmiah ; Banyak berasal dari bahasa asing
sum: Istilah ilmiah membuat tulisan tepat dan jelas.
fig: table Istilah | Arti ;; evaporasi | penguapan ;; kondensasi | pengembunan ;; inflasi | kenaikan harga umum ;; vertebrata | hewan bertulang belakang ;; fotosintesis | pembuatan makanan tumbuhan ;; demografi | ilmu kependudukan ~ Istilah ilmiah.
@ Debat
min: 15
act: Ikuti debat kecil bersama keluarga tentang perlu tidaknya pelajar membawa HP ke sekolah.
mis: menyerang pribadi lawan, bukan argumennya
exp: Debat adalah adu argumen antara pihak afirmasi yang setuju dan pihak oposisi yang tidak setuju terhadap suatu mosi, dengan netral sebagai penengah. Argumen disampaikan dengan data dan alasan logis. Debat dipimpin moderator dan dinilai juri. Sikap yang baik adalah sopan, menghargai waktu, dan menyanggah argumen, bukan pribadi.
ex: Mosi: pelajar boleh membawa HP ke sekolah. // Tim oposisi menyanggah dengan data.
pt: Afirmasi, oposisi, netral ; Argumen dengan data ; Sanggah argumen, bukan pribadi
sum: Debat melatih berpikir kritis dan santun.
fig: table Peran debat | Tugas ;; mosi | topik yang diperdebatkan ;; afirmasi | mendukung mosi ;; oposisi | menolak mosi ;; netral | penengah ;; moderator | memimpin jalannya debat ;; juri | menilai debat ~ Peran dalam debat.
@ Surat lamaran
min: 15
act: Tulis surat lamaran untuk menjadi pengurus perpustakaan sekolah.
mis: tidak melampirkan dokumen yang disebutkan dalam surat
exp: Surat lamaran adalah surat resmi untuk mengajukan diri dalam suatu posisi atau kegiatan. Bagiannya meliputi tempat dan tanggal, perihal, alamat tujuan, salam pembuka, identitas pelamar, isi, lampiran, salam penutup, dan tanda tangan. Bahasanya baku, sopan, dan meyakinkan.
ex: Perihal: Lamaran pengurus perpustakaan. // Bersama ini saya lampirkan rapor terakhir.
pt: Mengajukan diri secara resmi ; Identitas, isi, lampiran ; Bahasa baku dan meyakinkan
sum: Surat lamaran yang rapi memberi kesan baik.
fig: table Bagian surat lamaran | Isi ;; perihal | maksud surat ;; alamat tujuan | penerima lamaran ;; identitas | data diri pelamar ;; isi | alasan dan kemampuan ;; lampiran | dokumen pendukung ;; penutup | harapan dan terima kasih ~ Bagian surat lamaran.
@ Teks negosiasi
min: 15
act: Praktikkan tawar-menawar harga barang dengan sopan bersama anggota keluarga.
mis: memaksa pihak lain menerima tawaran tanpa mencari jalan tengah
exp: Teks negosiasi adalah teks berisi interaksi dua pihak untuk mencapai kesepakatan yang saling menguntungkan. Strukturnya terdiri atas orientasi, pengajuan, penawaran, persetujuan, pembelian, dan penutup. Bahasanya sopan, persuasif, dan memakai kalimat tanya serta ajakan.
ex: Bisakah harganya dikurangi sedikit? // Baiklah, kita sepakat pada harga ini.
pt: Mencapai kesepakatan bersama ; Orientasi, pengajuan, penawaran, persetujuan ; Sopan dan persuasif
sum: Negosiasi yang baik menguntungkan kedua pihak.
fig: table Struktur negosiasi | Contoh ;; orientasi | salam pembuka ;; pengajuan | menanyakan barang ;; penawaran | tawar-menawar harga ;; persetujuan | sepakat harga ;; pembelian | membayar ;; penutup | ucapan terima kasih ~ Struktur teks negosiasi.
@ Meresensi buku nonfiksi
min: 15
act: Baca buku pengetahuan pilihanmu, lalu tulis resensinya dengan kelebihan dan kekurangan.
mis: menulis resensi yang hanya berisi pujian
exp: Resensi adalah ulasan tentang sebuah karya untuk memberi penilaian. Resensi buku nonfiksi memuat identitas buku, ikhtisar isi, kelebihan, kekurangan, dan rekomendasi. Penilaian harus objektif dan berdasarkan isi buku. Resensi membantu pembaca menentukan apakah buku layak dibaca.
ex: Identitas: judul, penulis, penerbit, tahun, tebal. // Kekurangan: gambar kurang jelas.
pt: Ulasan dan penilaian karya ; Identitas, ikhtisar, kelebihan, kekurangan ; Objektif
sum: Resensi yang jujur membantu pembaca memilih buku.
fig: table Bagian resensi | Isi ;; judul resensi | kalimat menarik ;; identitas buku | judul, penulis, penerbit ;; ikhtisar | ringkasan isi ;; kelebihan | hal yang baik ;; kekurangan | hal yang perlu diperbaiki ;; rekomendasi | saran untuk pembaca ~ Bagian resensi buku.
# 2|Sastra dan Komunikasi
@ Unsur ekstrinsik cerpen
min: 15
act: Cari latar belakang pengarang satu cerpen, lalu hubungkan dengan isi ceritanya.
mis: menyamakan unsur ekstrinsik dengan tokoh dan alur
exp: Unsur ekstrinsik adalah unsur dari luar karya yang memengaruhi isi cerita. Unsur ekstrinsik meliputi latar belakang pengarang, nilai-nilai dalam cerita seperti nilai moral, sosial, budaya, dan agama, serta kondisi masyarakat saat cerita ditulis. Unsur intrinsik adalah unsur dari dalam cerita.
ex: Cerpen tentang desa nelayan ditulis pengarang yang lahir di pesisir. // Nilai gotong royong termasuk nilai sosial.
pt: Unsur dari luar karya ; Latar belakang pengarang dan nilai ; Berbeda dengan unsur intrinsik
sum: Unsur ekstrinsik membantu memahami makna cerpen lebih dalam.
fig: table Nilai | Contoh dalam cerpen ;; moral | tokoh jujur mengembalikan dompet ;; sosial | warga gotong royong ;; budaya | upacara adat panen ;; agama | tokoh rajin beribadah ;; pendidikan | semangat belajar ;; ekonomi | perjuangan mencari nafkah ~ Nilai dalam cerpen.
@ Menulis cerpen
min: 15
act: Tulis cerpen satu halaman tentang pengalaman yang mengubah sikapmu.
mis: menulis cerpen tanpa konflik
exp: Menulis cerpen diawali menentukan tema, tokoh, latar, dan alur. Struktur cerpen meliputi abstrak, orientasi, komplikasi, evaluasi, resolusi, dan koda. Cerpen yang menarik memiliki konflik yang jelas, dialog yang hidup, dan amanat yang tersirat. Setelah selesai, cerpen dibaca ulang dan disunting.
ex: Komplikasi: tokoh kehilangan uang kas kelas. // Koda: pesan untuk selalu jujur.
pt: Tema, tokoh, latar, alur ; Abstrak sampai koda ; Konflik jelas dan disunting
sum: Konflik membuat cerpen hidup.
fig: table Struktur cerpen | Isi ;; abstrak | gambaran awal cerita ;; orientasi | pengenalan tokoh dan latar ;; komplikasi | munculnya masalah ;; evaluasi | masalah memuncak ;; resolusi | penyelesaian ;; koda | amanat penutup ~ Struktur cerpen.
@ Jenis puisi baru
min: 15
act: Tulis satu distikon dan satu kuatrin tentang sekolah.
mis: mengira puisi baru tidak memiliki bait
exp: Puisi baru lebih bebas daripada puisi lama, tetapi tetap dapat dikelompokkan menurut jumlah baris setiap bait. Distikon terdiri atas dua baris, terzina tiga baris, kuatrin empat baris, kuint lima baris, sektet enam baris, septime tujuh baris, stanza delapan baris, dan soneta empat belas baris.
ex: Kuatrin memiliki empat baris setiap bait. // Soneta terdiri atas empat belas baris.
pt: Lebih bebas dari puisi lama ; Dikelompokkan menurut jumlah baris ; Distikon sampai soneta
sum: Jumlah baris menentukan jenis puisi baru.
fig: table Jenis puisi | Jumlah baris per bait ;; distikon | 2 ;; terzina | 3 ;; kuatrin | 4 ;; kuint | 5 ;; sektet | 6 ;; soneta | 14 seluruhnya ~ Jenis puisi baru.
@ Kohesi dan koherensi paragraf
min: 15
act: Perbaiki paragraf acak dengan menambahkan kata penghubung dan mengurutkan kalimatnya.
mis: menulis kalimat yang tidak saling berhubungan dalam satu paragraf
exp: Paragraf yang baik memiliki kohesi dan koherensi. Kohesi adalah kepaduan bentuk, yaitu hubungan antarkalimat melalui kata penghubung, kata ganti, dan pengulangan kata kunci. Koherensi adalah kepaduan makna, yaitu kalimat-kalimat membahas satu gagasan utama secara runtut dan logis.
ex: Budi rajin belajar. Oleh karena itu, ia juara kelas. // Kata ia merujuk pada Budi.
pt: Kohesi kepaduan bentuk ; Koherensi kepaduan makna ; Kata penghubung dan kata ganti
sum: Paragraf padu mudah dipahami.
fig: table Penanda kohesi | Contoh ;; kata ganti | ia, mereka ;; konjungsi antarkalimat | oleh karena itu ;; pengulangan kata kunci | sampah disebut berulang ;; sinonim | murid dan siswa ;; kata penunjuk | hal itu ;; konjungsi urutan | selanjutnya ~ Penanda kohesi.
@ Esai pendek
min: 15
act: Tulis esai pendek tiga paragraf tentang cita-citamu dan alasannya.
mis: menulis esai tanpa pendapat pribadi yang jelas
exp: Esai adalah karangan pendek yang berisi pandangan pribadi penulis tentang suatu topik, didukung alasan dan contoh. Struktur esai terdiri atas pendahuluan yang memuat gagasan utama, isi yang berisi argumen dan contoh, serta penutup yang menegaskan pendapat. Esai ditulis dengan bahasa yang lugas dan runtut.
ex: Pendahuluan: aku ingin menjadi dokter. // Isi: alasanku karena ingin menolong orang sakit.
pt: Pandangan pribadi penulis ; Pendahuluan, isi, penutup ; Lugas dan runtut
sum: Esai menyampaikan gagasan pribadi secara terarah.
fig: table Bagian esai | Fungsi ;; judul | menarik minat pembaca ;; pendahuluan | memperkenalkan gagasan ;; tesis | pendapat utama ;; isi | argumen dan contoh ;; penutup | menegaskan pendapat ;; refleksi | pesan penulis ~ Bagian esai.
@ Presentasi lisan
min: 15
act: Presentasikan hasil kerja kelompok selama tiga menit di depan keluarga.
mis: membaca salindia kata per kata tanpa menatap pendengar
exp: Presentasi lisan adalah menyampaikan informasi atau gagasan secara lisan di depan pendengar. Persiapannya meliputi menyusun materi, membuat media pendukung, dan berlatih. Saat presentasi, perhatikan kontak mata, volume suara, intonasi, bahasa tubuh, dan waktu. Akhiri dengan kesimpulan dan sesi tanya jawab.
ex: Membuka dengan salam dan pertanyaan menarik. // Menjawab pertanyaan dengan sopan.
pt: Menyampaikan gagasan secara lisan ; Siapkan materi dan berlatih ; Kontak mata, suara, bahasa tubuh
sum: Persiapan matang membuat presentasi meyakinkan.
fig: table Aspek | Cara yang baik ;; kontak mata | menatap pendengar ;; volume suara | terdengar jelas ;; intonasi | bervariasi tidak datar ;; bahasa tubuh | tenang dan terbuka ;; waktu | sesuai batas ;; tanya jawab | menjawab dengan sopan ~ Aspek presentasi lisan.
"""

BANK += """
## MAT|Merasionalkan penyebut
Bentuk rasional dari 6/√3 adalah …|2√3|6√3|3√2|√3|6√3/3.
Bentuk rasional dari 4/√2 adalah …|2√2|4√2|√2|8|4√2/2.
=|Bentuk rasional dari 10/√5 adalah …√5.|2|2√5.
=|Untuk merasionalkan 1/√7, pembilang dan penyebut dikalikan …|√7|√7.
B|3/√3 sama dengan √3.|3√3/3.
S|Merasionalkan penyebut cukup mengalikan penyebutnya saja.|Keduanya.
Bentuk rasional dari 14/√7 adalah …|2√7|7√2|14√7|√7|14√7/7.
Bentuk rasional dari 1/√2 adalah …|½√2|√2|2√2|2|√2/2.
## MAT|Soal cerita SPLDV
Jika x + y = 5 dan x - y = 1, maka x = …|3|2|4|1|Eliminasi.
Jika x + y = 10 dan x - y = 4, maka y = …|3|7|4|6|y = 3.
=|Jika 2x + y = 7 dan x + y = 5, maka x = …|2|Kurangkan.
=|Jika 3x + y = 10 dan x + y = 4, maka x = …|3|2x = 6.
B|Hasil SPLDV perlu diperiksa ke persamaan awal.|Periksa.
S|Soal cerita SPLDV cukup memakai satu persamaan.|Dua.
2 pensil + 1 buku = Rp7.000 dan 1 pensil + 1 buku = Rp5.000. Harga 1 pensil …|Rp2.000|Rp3.000|Rp1.000|Rp5.000|Selisih.
Langkah pertama menyelesaikan soal cerita SPLDV adalah …|memisalkan variabel|langsung menebak|menggambar grafik saja|membagi semua angka|Misalkan.
## MAT|Refleksi
Titik (2, 3) dicerminkan terhadap sumbu X menjadi …|(2, -3)|(-2, 3)|(3, 2)|(-2, -3)|(x, -y).
Titik (2, 3) dicerminkan terhadap sumbu Y menjadi …|(-2, 3)|(2, -3)|(3, 2)|(-3, -2)|(-x, y).
=|Titik (4, 1) dicerminkan terhadap garis y = x menjadi (1, …)|4|(y, x).
=|Titik (5, 2) dicerminkan terhadap titik asal menjadi (-5, …)|-2|(-x, -y).
B|Refleksi tidak mengubah ukuran bangun.|Kongruen.
S|Refleksi terhadap sumbu X mengubah tanda x.|Tanda y.
Titik (3, -1) dicerminkan terhadap sumbu X menjadi …|(3, 1)|(-3, -1)|(-3, 1)|(1, 3)|(x, -y).
Titik (1, 2) dicerminkan terhadap garis y = -x menjadi …|(-2, -1)|(2, 1)|(-1, -2)|(2, -1)|(-y, -x).
## MAT|Translasi
Titik (1, 2) ditranslasi T(3, 4) menjadi …|(4, 6)|(3, 8)|(-2, -2)|(4, 2)|Jumlahkan.
Translasi T(-2, 0) berarti geser 2 satuan ke …|kiri|kanan|atas|bawah|Negatif mendatar.
=|Titik (5, 1) ditranslasi T(-2, 3) menjadi (3, …)|4|1 + 3.
=|Titik (0, 0) ditranslasi T(2, 5) menjadi (2, …)|5|(2, 5).
B|Translasi tidak mengubah bentuk dan ukuran bangun.|Tetap.
S|Translasi memutar bangun terhadap titik pusat.|Rotasi.
Titik (3, -2) ditranslasi T(0, 2) menjadi …|(3, 0)|(3, -4)|(5, -2)|(0, 0)|y + 2.
Titik A ditranslasi T(1, 1) menjadi (4, 5). Titik A adalah …|(3, 4)|(5, 6)|(4, 5)|(1, 1)|Kurangkan.
## MAT|Rotasi
Titik (2, 1) dirotasi 90° terhadap O menjadi …|(-1, 2)|(1, -2)|(-2, -1)|(2, -1)|(-y, x).
Titik (2, 1) dirotasi 180° terhadap O menjadi …|(-2, -1)|(1, 2)|(-1, 2)|(2, -1)|(-x, -y).
=|Rotasi dengan sudut positif berarti berputar … arah jarum jam.|berlawanan|Berlawanan.
=|Rotasi 360° mengembalikan titik ke posisi …|semula;awal|Semula.
B|Rotasi -90° sama dengan rotasi 270°.|Setara.
S|Rotasi mengubah ukuran bangun.|Tetap.
Titik (3, 0) dirotasi 90° terhadap O menjadi …|(0, 3)|(0, -3)|(-3, 0)|(3, 0)|(-0, 3).
Titik (1, 4) dirotasi 270° terhadap O menjadi …|(4, -1)|(-4, 1)|(-1, -4)|(1, -4)|(y, -x).
## MAT|Dilatasi
Titik (2, 3) didilatasi dengan k = 2 terhadap O menjadi …|(4, 6)|(2, 6)|(4, 3)|(1, 1,5)|(kx, ky).
Jika 0 < k < 1, bangun hasil dilatasi …|diperkecil|diperbesar|tetap|terbalik saja|Kecil.
=|Titik (4, 8) didilatasi dengan k = ½ menjadi (2, …)|4|4.
=|Titik (1, -2) didilatasi dengan k = 3 menjadi (3, …)|-6|-6.
B|Dilatasi menghasilkan bangun yang sebangun.|Sebangun.
S|Dilatasi dengan k = 2 memperkecil bangun.|Memperbesar.
Titik (3, 1) didilatasi dengan k = -1 menjadi …|(-3, -1)|(3, 1)|(-3, 1)|(3, -1)|k negatif.
Faktor skala yang memperbesar bangun tiga kali adalah …|3|⅓|-⅓|0|k = 3.
## MAT|Rumus abc persamaan kuadrat
Akar-akar x² - 5x + 6 = 0 adalah …|2 dan 3|-2 dan -3|1 dan 6|5 dan 6|(x - 2)(x - 3).
Diskriminan dirumuskan …|b² - 4ac|b² + 4ac|4ac - b²|2a|D.
=|Diskriminan x² + 2x + 1 = 0 adalah …|0|4 - 4.
=|Akar positif x² - 4 = 0 adalah …|2|±2.
B|Jika D < 0, persamaan kuadrat tidak memiliki akar real.|D negatif.
S|Jika D = 0, ada dua akar real berbeda.|Kembar.
Akar-akar x² - 7x + 12 = 0 adalah …|3 dan 4|2 dan 6|-3 dan -4|1 dan 12|(x - 3)(x - 4).
Jika D > 0, persamaan kuadrat memiliki …|dua akar real berbeda|akar kembar|tidak ada akar|satu akar saja|D positif.
## MAT|Grafik fungsi kuadrat
Grafik fungsi kuadrat berbentuk …|parabola|garis lurus|lingkaran|zigzag|Parabola.
Jika a > 0, parabola terbuka ke …|atas|bawah|kiri|kanan|Atas.
=|Nilai f(x) = x² untuk x = -3 adalah …|9|9.
=|f(x) = -x² + 4 memotong sumbu Y di titik (0, …)|4|c = 4.
B|f(x) = -x² terbuka ke bawah.|a < 0.
S|Titik fungsi kuadrat dihubungkan dengan garis lurus.|Lengkung.
Nilai c pada fungsi kuadrat menunjukkan titik potong dengan sumbu …|Y|X|Z|simetri|Sumbu Y.
Titik potong parabola dengan sumbu X diperoleh dari …|akar f(x) = 0|nilai c|nilai a saja|nilai b saja|Akar.
## MAT|Sumbu simetri dan titik puncak
Rumus sumbu simetri parabola adalah x = …|-b/2a|b/2a|-2a/b|c/a|Rumus.
Sumbu simetri f(x) = x² - 4x + 3 adalah x = …|2|-2|4|3|4/2.
=|Sumbu simetri f(x) = x² + 6x adalah x = …|-3|-6/2.
=|Titik puncak f(x) = x² - 4x + 3 memiliki nilai y = …|-1|f(2).
B|Jika a > 0, titik puncak adalah titik minimum.|Minimum.
S|Jika a < 0, titik puncak adalah titik minimum.|Maksimum.
Titik puncak f(x) = -x² + 6x adalah …|(3, 9)|(-3, 9)|(3, -9)|(6, 0)|f(3) = 9.
Sumbu simetri f(x) = x² adalah x = …|0|1|-1|2|b = 0.
## MAT|Kesebangunan dan kekongruenan
Dua bangun sebangun jika sudut bersesuaian sama dan sisi bersesuaian …|sebanding|sama panjang|berbeda|tegak lurus|Sebanding.
Dua bangun yang bentuk dan ukurannya sama persis disebut …|kongruen|sebangun saja|simetris|sejajar|Kongruen.
=|Foto 4 × 6 diperbesar dengan skala 2 menjadi 8 × …|12|12.
=|Syarat kongruen sisi-sisi-sisi disingkat …|sss|sss.
B|Persegi panjang 3 × 5 dan 6 × 10 sebangun.|Skala 2.
S|Persegi panjang 2 × 3 dan 4 × 5 sebangun.|Tidak sebanding.
Bayangan tiang 2 m adalah 1 m, bayangan pohon 4 m. Tinggi pohon …|8 m|2 m|4 m|6 m|Perbandingan.
Persegi 5 × 5 dan 7 × 7 pasti …|sebangun|kongruen|tidak sebangun|sejajar|Persegi.
## MAT|Luas permukaan kerucut dan bola
Rumus luas permukaan bola adalah …|4πr²|πr²|2πr²|⅔πr³|4πr².
Kerucut dengan r = 3 dan t = 4 memiliki garis pelukis …|5|7|12|1|3-4-5.
=|Luas permukaan bola berjari-jari 7 cm dengan π = 22/7 adalah … cm².|616|4 × 154.
=|Luas selimut kerucut dirumuskan π × r × …|s|πrs.
B|Luas permukaan kerucut = πr(r + s).|Rumus.
S|Garis pelukis kerucut sama dengan tingginya.|Berbeda.
Luas permukaan bola berjari-jari 10 cm dengan π = 3,14 adalah …|1.256 cm²|314 cm²|628 cm²|3.140 cm²|4 × 314.
Luas belahan bola padat dirumuskan …|3πr²|2πr²|4πr²|πr²|3πr².
## MAT|Ruang sampel dan titik sampel
Himpunan semua hasil yang mungkin dari percobaan disebut …|ruang sampel|titik sampel|peluang|frekuensi|Ruang sampel.
Banyak titik sampel pelemparan dua koin adalah …|4|2|6|8|2².
=|Banyak titik sampel pelemparan satu dadu adalah …|6|6.
=|Banyak titik sampel pelemparan dua dadu adalah …|36|6 × 6.
B|Diagram pohon dapat dipakai menyusun ruang sampel.|Pohon.
S|AG dan GA dihitung sebagai satu titik sampel.|Dua.
Banyak titik sampel pelemparan tiga koin adalah …|8|6|3|9|2³.
Banyak titik sampel satu koin dan satu dadu adalah …|12|8|6|36|2 × 6.
## BIN|Kalimat majemuk bertingkat
Kalimat majemuk bertingkat terdiri atas induk kalimat dan …|anak kalimat|dua induk kalimat|keterangan saja|subjek saja|Anak kalimat.
Konjungsi yang menyatakan syarat adalah …|jika|karena|ketika|meskipun|Syarat.
=|Konjungsi yang menyatakan tujuan adalah …|agar;supaya|Agar.
=|Konjungsi yang menyatakan waktu adalah …|ketika;saat|Ketika.
B|Ia tidak masuk karena sakit termasuk kalimat majemuk bertingkat.|Bertingkat.
S|Konjungsi dan menandai kalimat majemuk bertingkat.|Setara.
Konjungsi meskipun menyatakan hubungan …|konsesif|sebab|tujuan|waktu|Konsesif.
Kalimat majemuk setara memakai konjungsi …|tetapi|karena|agar|jika|Setara.
## BIN|Istilah ilmiah
Evaporasi berarti …|penguapan|pengembunan|pembekuan|pencairan|Evaporasi.
Inflasi berarti …|kenaikan harga umum|penurunan harga|banyak penduduk|kekurangan air|Inflasi.
=|Kondensasi berarti …|pengembunan|Pengembunan.
=|Hewan bertulang belakang disebut …|vertebrata|Vertebrata.
B|Istilah ilmiah memiliki makna khusus dalam bidang ilmu.|Khusus.
S|Istilah ilmiah boleh dipakai tanpa memahami artinya.|Pahami.
Ilmu tentang kependudukan disebut …|demografi|geologi|biologi|astronomi|Demografi.
Istilah ilmiah banyak dipakai dalam teks …|laporan percobaan|pantun|dongeng|surat pribadi|Ilmiah.
## BIN|Debat
Pihak yang setuju terhadap mosi disebut …|afirmasi|oposisi|netral|juri|Afirmasi.
Pihak yang menolak mosi disebut …|oposisi|afirmasi|moderator|notulis|Oposisi.
=|Topik yang diperdebatkan disebut …|mosi|Mosi.
=|Orang yang memimpin jalannya debat disebut …|moderator|Moderator.
B|Juri bertugas menilai debat.|Juri.
S|Dalam debat boleh menyerang pribadi lawan.|Argumen.
Argumen debat yang kuat didukung …|data|teriakan|ejekan|gosip|Data.
Pihak penengah dalam debat disebut …|netral|oposisi|afirmasi|pendukung|Netral.
## BIN|Surat lamaran
Surat lamaran termasuk surat …|resmi|pribadi|niaga biasa|undangan|Resmi.
Dokumen pendukung surat lamaran disebut …|lampiran|perihal|kop|salam|Lampiran.
=|Maksud surat lamaran ditulis pada bagian …|perihal|Perihal.
=|Data diri pelamar ditulis pada bagian …|identitas|Identitas.
B|Bahasa surat lamaran harus baku dan sopan.|Baku.
S|Dokumen yang disebut dalam surat tidak perlu dilampirkan.|Perlu.
Isi surat lamaran memuat alasan dan … pelamar.|kemampuan|alamat teman|hobi keluarga|nomor rekening|Kemampuan.
Bagian penutup surat lamaran berisi harapan dan …|terima kasih|ancaman|keluhan|lelucon|Terima kasih.
## BIN|Teks negosiasi
Tujuan negosiasi adalah mencapai …|kesepakatan|pertengkaran|kemenangan sepihak|kekalahan|Sepakat.
Bagian negosiasi saat tawar-menawar harga disebut …|penawaran|orientasi|penutup|pembelian|Penawaran.
=|Bagian awal negosiasi berupa salam pembuka disebut …|orientasi|Orientasi.
=|Bagian negosiasi ketika kedua pihak sepakat disebut …|persetujuan|Persetujuan.
B|Negosiasi yang baik menguntungkan kedua pihak.|Saling untung.
S|Negosiasi berarti memaksa pihak lain menerima tawaran.|Kesepakatan.
Kalimat yang tepat dalam negosiasi adalah …|Bisakah harganya dikurangi sedikit?|Pokoknya harus murah!|Saya tidak peduli.|Terserah kamu saja!|Sopan.
Bahasa dalam negosiasi bersifat …|sopan dan persuasif|kasar|memaksa|mengancam|Persuasif.
## BIN|Meresensi buku nonfiksi
Resensi adalah ulasan untuk memberi … terhadap karya.|penilaian|hiasan|terjemahan|salinan|Penilaian.
Bagian resensi yang berisi ringkasan isi disebut …|ikhtisar|identitas|rekomendasi|judul|Ikhtisar.
=|Judul, penulis, dan penerbit termasuk … buku.|identitas|Identitas.
=|Saran untuk pembaca dalam resensi disebut …|rekomendasi|Rekomendasi.
B|Penilaian dalam resensi harus objektif.|Objektif.
S|Resensi yang baik hanya berisi pujian.|Seimbang.
Gambar kurang jelas dalam buku termasuk bagian … dalam resensi.|kekurangan|kelebihan|identitas|ikhtisar|Kekurangan.
Resensi membantu pembaca menentukan apakah buku …|layak dibaca|harus dibakar|mahal|tebal|Layak.
## BIN|Unsur ekstrinsik cerpen
Unsur ekstrinsik adalah unsur dari … karya.|luar|dalam|tengah|akhir|Luar.
Contoh unsur ekstrinsik adalah …|latar belakang pengarang|tokoh|alur|sudut pandang|Ekstrinsik.
=|Nilai gotong royong dalam cerpen termasuk nilai …|sosial|Sosial.
=|Tokoh jujur mengembalikan dompet mencerminkan nilai …|moral|Moral.
B|Kondisi masyarakat saat cerpen ditulis termasuk unsur ekstrinsik.|Ekstrinsik.
S|Tokoh dan alur termasuk unsur ekstrinsik.|Intrinsik.
Upacara adat panen dalam cerpen mencerminkan nilai …|budaya|ekonomi|agama|pendidikan|Budaya.
Unsur yang berasal dari dalam cerita disebut unsur …|intrinsik|ekstrinsik|eksternal|tambahan|Intrinsik.
## BIN|Menulis cerpen
Bagian cerpen yang memperkenalkan tokoh dan latar adalah …|orientasi|komplikasi|resolusi|koda|Orientasi.
Bagian cerpen ketika masalah muncul adalah …|komplikasi|orientasi|abstrak|koda|Komplikasi.
=|Bagian cerpen yang berisi penyelesaian disebut …|resolusi|Resolusi.
=|Bagian penutup cerpen yang berisi amanat disebut …|koda|Koda.
B|Cerpen yang menarik memiliki konflik.|Konflik.
S|Cerpen tidak perlu dibaca ulang setelah ditulis.|Disunting.
Gambaran awal cerita dalam cerpen disebut …|abstrak|koda|resolusi|evaluasi|Abstrak.
Bagian cerpen ketika masalah memuncak adalah …|evaluasi|orientasi|koda|abstrak|Evaluasi.
## BIN|Jenis puisi baru
Puisi dengan dua baris setiap bait disebut …|distikon|terzina|kuatrin|sektet|Distikon.
Puisi dengan empat baris setiap bait disebut …|kuatrin|kuint|distikon|stanza|Kuatrin.
=|Puisi yang terdiri atas empat belas baris disebut …|soneta|Soneta.
=|Puisi dengan tiga baris setiap bait disebut …|terzina|Terzina.
B|Sektet memiliki enam baris setiap bait.|Enam.
S|Puisi baru sama sekali tidak memiliki bait.|Ada bait.
Puisi dengan lima baris setiap bait disebut …|kuint|kuatrin|septime|stanza|Kuint.
Puisi dengan delapan baris setiap bait disebut …|stanza|soneta|septime|sektet|Stanza.
## BIN|Kohesi dan koherensi paragraf
Kepaduan bentuk antarkalimat disebut …|kohesi|koherensi|ambiguitas|diksi|Kohesi.
Kepaduan makna dalam paragraf disebut …|koherensi|kohesi|majas|rima|Koherensi.
=|Kata ia dan mereka termasuk kata …|ganti|Kata ganti.
=|Murid dan siswa merupakan …|sinonim|Sinonim.
B|Konjungsi oleh karena itu membantu kohesi.|Penanda.
S|Kalimat dalam paragraf tidak perlu saling berhubungan.|Padu.
Kata hal itu termasuk penanda kohesi berupa kata …|penunjuk|kerja|sifat|bilangan|Penunjuk.
Paragraf yang membahas satu gagasan utama secara runtut memiliki …|koherensi|ambiguitas|kerancuan|pleonasme|Koherensi.
## BIN|Esai pendek
Esai berisi … pribadi penulis.|pandangan|biodata|daftar harga|resep|Pandangan.
Bagian esai yang memperkenalkan gagasan adalah …|pendahuluan|isi|penutup|lampiran|Pendahuluan.
=|Pendapat utama dalam esai disebut …|tesis|Tesis.
=|Bagian esai yang menegaskan pendapat adalah …|penutup|Penutup.
B|Isi esai memuat argumen dan contoh.|Isi.
S|Esai tidak memerlukan pendapat penulis.|Perlu.
Bahasa esai sebaiknya …|lugas dan runtut|berbelit-belit|kasar|acak|Lugas.
Esai termasuk karangan …|pendek|sangat panjang|puisi|drama|Pendek.
## BIN|Presentasi lisan
Saat presentasi, sebaiknya kita … pendengar.|menatap|membelakangi|mengabaikan|memarahi|Kontak mata.
Intonasi presentasi yang baik adalah …|bervariasi|datar|berteriak terus|berbisik|Bervariasi.
=|Presentasi biasanya diakhiri dengan kesimpulan dan sesi tanya …|jawab|Tanya jawab.
=|Sebelum presentasi, kita perlu ber …|latih;berlatih|Berlatih.
B|Volume suara harus terdengar jelas.|Jelas.
S|Membaca salindia kata per kata adalah cara terbaik presentasi.|Kontak mata.
Bahasa tubuh yang baik saat presentasi adalah …|tenang dan terbuka|melipat tangan terus|membelakangi|gelisah|Terbuka.
Presentasi yang baik memperhatikan … yang tersedia.|waktu|warna baju|merek laptop|jumlah kursi|Waktu.
"""

SAS += """
## MAT 1
0|Bentuk rasional dari 3/√3 adalah ....|√3|3√3|1|9|3√3/3.
1|Jika x + y = 6 dan 2x = 8, maka y = ....|2|4|6|8|x = 4.
2|Titik (-2, 5) dicerminkan terhadap sumbu Y menjadi ....|(2, 5)|(-2, -5)|(5, -2)|(2, -5)|(-x, y).
3|Titik (2, 2) ditranslasi T(-5, -5) menjadi ....|(-3, -3)|(7, 7)|(-3, 7)|(3, 3)|Jumlahkan.
4|Titik (4, 2) dirotasi 180° terhadap O menjadi ....|(-4, -2)|(2, 4)|(-2, 4)|(4, -2)|(-x, -y).
5|Titik (6, 9) didilatasi dengan k = ⅓ terhadap O menjadi ....|(2, 3)|(18, 27)|(3, 2)|(6, 3)|kx, ky.
## MAT 2
0|Akar-akar x² - x - 6 = 0 adalah ....|3 dan -2|-3 dan 2|6 dan -1|1 dan 6|(x - 3)(x + 2).
1|Nilai f(x) = x² untuk x = 2 adalah ....|4|2|8|-4|2².
2|Sumbu simetri f(x) = x² - 2x + 5 adalah ....|x = 1|x = -1|x = 2|x = 5|2/2.
3|Persegi panjang 6 × 8 sebangun dengan ....|3 × 4|4 × 5|2 × 3|6 × 9|Skala ½.
4|Luas permukaan bola berjari-jari 3,5 cm dengan π = 22/7 adalah ....|154 cm²|38,5 cm²|44 cm²|616 cm²|4πr².
5|Banyak titik sampel pada pelemparan satu koin adalah ....|2|1|4|6|A dan G.
## BIN 1
0|Konjungsi seperti dalam kalimat majemuk bertingkat menyatakan hubungan ....|perbandingan|sebab|syarat|waktu|Seperti.
1|Fotosintesis berarti ....|pembuatan makanan tumbuhan|penguapan air|pengembunan|ilmu kependudukan|Fotosintesis.
2|Orang yang menilai jalannya debat disebut ....|juri|moderator|afirmasi|oposisi|Juri.
3|Bagian surat lamaran yang menyebut penerima lamaran adalah ....|alamat tujuan|lampiran|penutup|perihal|Alamat.
4|Bagian negosiasi saat pembeli membayar disebut ....|pembelian|orientasi|pengajuan|penawaran|Pembelian.
5|Hal yang baik dari buku ditulis pada bagian ....|kelebihan|kekurangan|identitas|ikhtisar|Kelebihan.
## BIN 2
0|Perjuangan tokoh mencari nafkah dalam cerpen mencerminkan nilai ....|ekonomi|agama|budaya|pendidikan|Ekonomi.
1|Bagian cerpen yang berisi pengenalan tokoh disebut ....|orientasi|koda|resolusi|komplikasi|Orientasi.
2|Puisi baru dengan enam baris setiap bait disebut ....|sektet|kuint|septime|stanza|Sektet.
3|Konjungsi selanjutnya termasuk penanda kohesi berupa konjungsi ....|urutan|sebab|syarat|tujuan|Urutan.
4|Pesan penulis di akhir esai disebut ....|refleksi|judul|pendahuluan|tesis|Refleksi.
5|Menjawab pertanyaan pendengar sebaiknya dengan ....|sopan|marah|mengabaikan|bercanda kasar|Sopan.
"""

TOPICS += """
## IPA
# 1|Listrik, Magnet, dan Perkembangbiakan
@ Listrik statis
min: 15
act: Gosokkan penggaris plastik ke rambut kering, lalu dekatkan ke potongan kertas kecil.
mis: mengira muatan sejenis saling tarik-menarik
exp: Listrik statis adalah muatan listrik yang diam pada suatu benda. Benda bermuatan karena kelebihan atau kekurangan elektron, misalnya akibat digosok. Muatan sejenis tolak-menolak, sedangkan muatan berbeda jenis tarik-menarik. Petir adalah pelepasan listrik statis dalam jumlah sangat besar.
ex: Penggaris yang digosok menarik kertas. // Rambut berdiri setelah melepas sweter.
pt: Muatan listrik diam ; Sejenis tolak-menolak ; Berbeda jenis tarik-menarik
sum: Listrik statis terjadi karena perpindahan elektron.
fig: table Peristiwa | Penjelasan ;; penggaris menarik kertas | penggaris bermuatan ;; rambut berdiri | muatan sejenis tolak-menolak ;; kejutan saat memegang gagang pintu | pelepasan muatan ;; petir | pelepasan muatan besar ;; balon menempel di dinding | induksi muatan ;; debu menempel di layar | layar bermuatan ~ Contoh listrik statis.
@ Kemagnetan
min: 15
act: Uji benda di rumah yang dapat ditarik magnet, lalu kelompokkan menjadi magnetik dan nonmagnetik.
mis: mengira semua logam dapat ditarik magnet
exp: Magnet memiliki dua kutub, yaitu kutub utara dan selatan. Kutub sejenis tolak-menolak, kutub berbeda tarik-menarik. Benda magnetik dapat ditarik magnet, misalnya besi, baja, nikel, dan kobalt. Aluminium, tembaga, dan emas tidak ditarik magnet. Magnet dapat dibuat dengan cara menggosok, induksi, dan elektromagnet.
ex: Paku besi ditarik magnet. // Sendok aluminium tidak ditarik magnet.
pt: Kutub utara dan selatan ; Sejenis tolak, berbeda tarik ; Besi, nikel, kobalt magnetik
sum: Tidak semua logam bersifat magnetik.
fig: table Benda | Sifat terhadap magnet ;; paku besi | magnetik ;; jarum baja | magnetik kuat ;; koin nikel | magnetik lemah ;; sendok aluminium | nonmagnetik ;; kabel tembaga | nonmagnetik logam ;; penghapus karet | nonmagnetik bukan logam ~ Benda magnetik dan nonmagnetik.
@ Induksi elektromagnetik
min: 15
act: Amati dinamo sepeda atau senter kocok, lalu jelaskan bagaimana listrik dihasilkan.
mis: mengira magnet diam di dalam kumparan menghasilkan listrik terus-menerus
exp: Induksi elektromagnetik adalah timbulnya arus listrik pada kumparan karena perubahan medan magnet, misalnya magnet digerakkan keluar masuk kumparan. Prinsip ini ditemukan Michael Faraday. Penerapannya pada generator, dinamo sepeda, dan transformator. Transformator mengubah tegangan listrik bolak-balik.
ex: Dinamo sepeda menyalakan lampu saat roda berputar. // Trafo menurunkan tegangan untuk pengisi daya HP.
pt: Perubahan medan magnet menimbulkan arus ; Ditemukan Faraday ; Generator, dinamo, transformator
sum: Gerak magnet dapat menghasilkan listrik.
fig: table Alat | Fungsi ;; generator | mengubah energi gerak menjadi listrik ;; dinamo sepeda | menyalakan lampu sepeda ;; transformator step-up | menaikkan tegangan ;; transformator step-down | menurunkan tegangan ;; motor listrik | mengubah listrik menjadi gerak ;; senter kocok | menghasilkan listrik dari goyangan ~ Penerapan elektromagnetik.
@ Perkembangbiakan tumbuhan
min: 15
act: Tanam potongan batang singkong atau daun cocor bebek, lalu amati pertumbuhannya seminggu.
mis: mengira semua tumbuhan berkembang biak dengan biji
exp: Tumbuhan berkembang biak secara generatif dan vegetatif. Generatif melalui penyerbukan dan pembuahan sehingga menghasilkan biji. Vegetatif alami tanpa biji, misalnya umbi, tunas, geragih, dan tunas adventif daun. Vegetatif buatan dilakukan manusia, misalnya stek, cangkok, okulasi, dan kultur jaringan.
ex: Cocor bebek tumbuh dari tunas daun. // Mangga diperbanyak dengan cangkok.
pt: Generatif dengan biji ; Vegetatif alami: umbi, tunas, geragih ; Vegetatif buatan: stek, cangkok
sum: Tumbuhan memiliki banyak cara berkembang biak.
fig: table Tumbuhan | Cara berkembang biak ;; cocor bebek | tunas adventif daun ;; stroberi | geragih ;; kentang | umbi batang ;; pisang | tunas ;; singkong | stek batang ;; jagung | biji ~ Cara perkembangbiakan tumbuhan.
@ Perkembangbiakan hewan
min: 15
act: Buat tabel hewan di sekitarmu dan cara berkembang biaknya.
mis: mengira semua hewan bertelur
exp: Hewan berkembang biak secara generatif dan vegetatif. Generatif melalui pertemuan sel kelamin, dengan cara bertelur (ovipar), melahirkan (vivipar), atau bertelur-melahirkan (ovovivipar). Vegetatif terjadi pada hewan tingkat rendah, misalnya membelah diri pada amoeba, tunas pada hydra, dan fragmentasi pada cacing pipih.
ex: Ayam bertelur (ovipar). // Kucing melahirkan (vivipar).
pt: Ovipar, vivipar, ovovivipar ; Vegetatif pada hewan tingkat rendah ; Membelah, tunas, fragmentasi
sum: Cara berkembang biak menjaga kelangsungan jenis hewan.
fig: table Hewan | Cara berkembang biak ;; ayam | ovipar ;; kucing | vivipar ;; hiu | ovovivipar ;; amoeba | membelah diri ;; hydra | tunas ;; planaria | fragmentasi ~ Cara perkembangbiakan hewan.
@ Sistem indra manusia
min: 15
act: Tutup mata, lalu tebak benda dengan meraba, mencium, dan mengecap rasanya.
mis: mengira lidah hanya dapat merasakan rasa manis di ujungnya saja
exp: Manusia memiliki lima indra. Mata untuk melihat, telinga untuk mendengar dan menjaga keseimbangan, hidung untuk membau, lidah untuk mengecap, dan kulit untuk merasakan sentuhan, suhu, dan nyeri. Reseptor rasa tersebar di seluruh permukaan lidah. Indra perlu dijaga, misalnya dengan tidak mendengarkan suara terlalu keras.
ex: Kulit merasakan panasnya air. // Hidung tersumbat membuat makanan terasa hambar.
pt: Lima indra ; Reseptor rasa tersebar di lidah ; Jaga kesehatan indra
sum: Indra menghubungkan kita dengan lingkungan.
fig: table Indra | Rangsangan ;; mata | cahaya ;; telinga | bunyi ;; hidung | bau ;; lidah | rasa ;; kulit | sentuhan dan suhu ;; telinga dalam | keseimbangan ~ Indra dan rangsangannya.
# 2|Bumi, Kesehatan, dan Teknologi
@ Tanah dan organisme tanah
min: 15
act: Ambil segenggam tanah kebun, lalu amati hewan kecil dan bahan yang ada di dalamnya.
mis: menganggap cacing tanah merusak kesuburan tanah
exp: Tanah terbentuk dari pelapukan batuan dan bahan organik. Tanah tersusun atas mineral, bahan organik, air, dan udara. Lapisan teratas atau humus paling subur. Organisme tanah seperti cacing, rayap, jamur, dan bakteri membantu menguraikan bahan organik dan menggemburkan tanah.
ex: Cacing tanah membuat lubang sehingga udara masuk. // Daun busuk menjadi humus.
pt: Dari pelapukan batuan dan bahan organik ; Mineral, organik, air, udara ; Organisme tanah menyuburkan
sum: Tanah sehat menopang kehidupan tumbuhan.
fig: table Organisme tanah | Peran ;; cacing tanah | menggemburkan tanah ;; bakteri | mengurai bahan organik ;; jamur | mengurai kayu dan daun ;; rayap | menghancurkan kayu mati ;; semut | mengaduk lapisan tanah ;; akar tumbuhan | menahan tanah dari erosi ~ Peran organisme tanah.
@ Sistem imun
min: 15
act: Catat jadwal imunisasi yang pernah kamu terima dari buku kesehatan anak.
mis: mengira antibiotik dapat menyembuhkan flu karena virus
exp: Sistem imun atau kekebalan tubuh melindungi tubuh dari kuman penyakit. Pertahanan pertama berupa kulit, air mata, dan lendir. Pertahanan berikutnya dilakukan sel darah putih yang melawan kuman dan membentuk antibodi. Vaksin melatih tubuh membentuk kekebalan. Pola hidup sehat menjaga sistem imun tetap kuat.
ex: Vaksin campak mencegah penyakit campak. // Tidur cukup membantu sistem imun.
pt: Melindungi dari kuman ; Kulit, lendir, sel darah putih ; Vaksin membentuk kekebalan
sum: Sistem imun kuat menjaga tubuh tetap sehat.
fig: table Bagian pertahanan | Fungsi ;; kulit | penghalang kuman ;; air mata | membunuh kuman di mata ;; lendir hidung | menangkap debu dan kuman ;; sel darah putih | melawan kuman ;; antibodi | mengenali kuman ;; vaksin | melatih kekebalan ~ Bagian sistem imun.
@ Energi terbarukan
min: 15
act: Buat poster perbandingan sumber energi terbarukan dan tidak terbarukan.
mis: menganggap batu bara sebagai energi terbarukan
exp: Energi terbarukan berasal dari sumber yang tidak habis atau cepat pulih, seperti matahari, angin, air, panas bumi, dan biomassa. Energi tidak terbarukan berasal dari bahan bakar fosil seperti minyak bumi, batu bara, dan gas alam. Energi terbarukan lebih ramah lingkungan karena menghasilkan sedikit emisi karbon.
ex: Panel surya mengubah cahaya matahari menjadi listrik. // PLTA memakai aliran air bendungan.
pt: Tidak habis atau cepat pulih ; Matahari, angin, air, panas bumi ; Lebih sedikit emisi
sum: Energi terbarukan menjaga bumi untuk masa depan.
fig: table Pembangkit | Sumber energi ;; PLTS | matahari ;; PLTB | angin ;; PLTA | air ;; PLTP | panas bumi ;; PLTU | batu bara ;; PLTBm | biomassa ~ Pembangkit listrik dan sumbernya.
@ Atom, ion, dan molekul
min: 15
act: Buat model molekul air dari plastisin dengan dua warna berbeda.
mis: mengira atom adalah partikel terkecil yang tidak memiliki bagian
exp: Benda tersusun atas partikel sangat kecil. Atom adalah partikel terkecil unsur yang terdiri atas proton, neutron, dan elektron. Ion adalah atom bermuatan karena melepas atau menangkap elektron. Molekul adalah gabungan dua atom atau lebih, misalnya molekul air H2O dan oksigen O2.
ex: Molekul air terdiri atas dua atom hidrogen dan satu atom oksigen. // Ion natrium bermuatan positif.
pt: Atom: proton, neutron, elektron ; Ion atom bermuatan ; Molekul gabungan atom
sum: Semua materi tersusun atas partikel.
fig: table Partikel | Muatan ;; proton | positif ;; elektron | negatif ;; neutron | netral ;; kation | ion positif ;; anion | ion negatif ;; molekul air | netral gabungan atom ~ Partikel penyusun materi.
@ Gerhana matahari dan bulan
min: 15
act: Peragakan gerhana dengan senter, bola besar, dan bola kecil di ruangan gelap.
mis: melihat gerhana matahari langsung tanpa pelindung mata
exp: Gerhana matahari terjadi saat bulan berada di antara matahari dan bumi sehingga bayangan bulan jatuh ke bumi. Gerhana bulan terjadi saat bumi berada di antara matahari dan bulan sehingga bulan masuk bayangan bumi. Gerhana matahari tidak boleh dilihat langsung karena dapat merusak mata.
ex: Gerhana matahari total membuat siang tampak gelap. // Gerhana bulan terjadi saat bulan purnama.
pt: Gerhana matahari: bulan di tengah ; Gerhana bulan: bumi di tengah ; Jangan melihat matahari langsung
sum: Gerhana terjadi karena posisi matahari, bumi, dan bulan segaris.
fig: table Jenis gerhana | Posisi di tengah ;; gerhana matahari | bulan ;; gerhana bulan | bumi ;; gerhana matahari total | bulan menutup seluruh matahari ;; gerhana matahari cincin | bulan lebih kecil dari matahari ;; gerhana bulan total | bulan masuk umbra bumi ;; gerhana sebagian | tertutup sebagian ~ Jenis gerhana.
@ Teknologi ramah lingkungan
min: 15
act: Cari tiga teknologi ramah lingkungan yang bisa diterapkan di rumahmu.
mis: mengira teknologi ramah lingkungan selalu mahal dan rumit
exp: Teknologi ramah lingkungan adalah teknologi yang mengurangi dampak buruk bagi lingkungan. Contohnya lampu LED hemat energi, biopori untuk resapan air, komposter untuk sampah organik, kendaraan listrik, dan pemanen air hujan. Banyak teknologi ini sederhana dan murah.
ex: Lubang biopori membantu air meresap ke tanah. // Lampu LED lebih hemat listrik.
pt: Mengurangi dampak buruk lingkungan ; LED, biopori, komposter ; Banyak yang sederhana
sum: Teknologi hijau dapat dimulai dari rumah.
fig: table Teknologi | Manfaat ;; lampu LED | hemat listrik ;; biopori | resapan air ;; komposter | mengolah sampah organik ;; pemanen air hujan | hemat air bersih ;; kendaraan listrik | mengurangi asap ;; panel surya atap | listrik bersih ~ Teknologi ramah lingkungan.

## IPS
# 1|Sejarah Indonesia dan Dunia
@ Masa Demokrasi Liberal
min: 15
act: Buat garis waktu kabinet pada masa Demokrasi Liberal 1950–1959.
mis: mengira Demokrasi Liberal berlangsung stabil dan lama
exp: Masa Demokrasi Liberal atau Demokrasi Parlementer berlangsung 1950–1959. Pemerintahan dipimpin perdana menteri dan kabinet yang bertanggung jawab kepada parlemen. Kabinet sering berganti sehingga pembangunan terhambat. Peristiwa penting adalah Pemilu 1955 dan Konferensi Asia Afrika 1955 di Bandung.
ex: Pemilu 1955 adalah pemilu pertama Indonesia. // KAA 1955 diselenggarakan di Bandung.
pt: 1950–1959 parlementer ; Kabinet sering berganti ; Pemilu 1955 dan KAA
sum: Demokrasi Liberal diwarnai pergantian kabinet.
fig: table Peristiwa | Tahun ;; pemilu pertama | 1955 ;; Konferensi Asia Afrika | April 1955 ;; Dekrit Presiden | 1959 ;; pembentukan NKRI kembali | 1950 ;; Kabinet Natsir | 1950–1951 ;; Kabinet Djuanda | 1957–1959 ~ Peristiwa masa Demokrasi Liberal.
@ Masa Demokrasi Terpimpin
min: 15
act: Cari isi Dekrit Presiden 5 Juli 1959, lalu tulis tiga poin utamanya.
mis: mengira Demokrasi Terpimpin memperkuat peran parlemen
exp: Masa Demokrasi Terpimpin berlangsung 1959–1965, diawali Dekrit Presiden 5 Juli 1959 yang membubarkan Konstituante dan memberlakukan kembali UUD 1945. Kekuasaan terpusat pada presiden. Peristiwa penting antara lain pembebasan Irian Barat melalui Trikora dan konfrontasi dengan Malaysia. Masa ini berakhir setelah peristiwa G30S 1965.
ex: Trikora diumumkan untuk membebaskan Irian Barat. // Konstituante dibubarkan lewat dekrit.
pt: 1959–1965 ; Diawali Dekrit 5 Juli 1959 ; Kekuasaan terpusat pada presiden
sum: Demokrasi Terpimpin memusatkan kekuasaan pada presiden.
fig: table Isi Dekrit 5 Juli 1959 | Keterangan ;; pembubaran Konstituante | badan penyusun UUD dibubarkan ;; berlaku kembali UUD 1945 | UUDS 1950 tidak berlaku ;; pembentukan MPRS | dalam waktu singkat ;; pembentukan DPAS | dewan pertimbangan ;; Trikora | 1961 ;; Irian Barat masuk Indonesia | 1963 ~ Peristiwa Demokrasi Terpimpin.
@ Masa Orde Baru
min: 15
act: Tanyakan kepada orang tua atau kakek nenek pengalaman mereka pada masa Orde Baru.
mis: mengira Orde Baru tidak memiliki pembangunan maupun masalah
exp: Orde Baru berlangsung 1966–1998 di bawah Presiden Soeharto. Pemerintah fokus pada pembangunan ekonomi melalui Repelita, swasembada beras, dan program Keluarga Berencana. Namun, kebebasan politik dan pers dibatasi serta korupsi, kolusi, dan nepotisme meningkat. Krisis moneter 1997–1998 menyebabkan Orde Baru berakhir.
ex: Indonesia swasembada beras pada 1984. // Krisis moneter 1998 memicu tuntutan reformasi.
pt: 1966–1998 Presiden Soeharto ; Repelita dan swasembada beras ; Pembatasan politik dan KKN
sum: Orde Baru membawa pembangunan sekaligus masalah.
fig: table Kebijakan Orde Baru | Keterangan ;; Repelita | rencana pembangunan lima tahun ;; swasembada beras | 1984 ;; Keluarga Berencana | mengendalikan penduduk ;; transmigrasi | pemerataan penduduk ;; Supersemar | awal kekuasaan Soeharto ;; krisis moneter | 1997–1998 ~ Kebijakan dan peristiwa Orde Baru.
@ Masa Reformasi
min: 15
act: Buat tabel perubahan sesudah reformasi dibanding masa sebelumnya.
mis: mengira reformasi hanya pergantian presiden
exp: Reformasi dimulai 1998 setelah Presiden Soeharto mengundurkan diri pada 21 Mei 1998. Tuntutan reformasi antara lain amandemen UUD 1945, pemberantasan KKN, otonomi daerah, kebebasan pers, dan penegakan hukum. Hasilnya antara lain pemilihan presiden langsung sejak 2004 dan pembentukan KPK.
ex: Presiden dipilih langsung oleh rakyat sejak 2004. // KPK dibentuk untuk memberantas korupsi.
pt: Dimulai Mei 1998 ; Amandemen UUD, berantas KKN, otonomi ; Pemilu presiden langsung sejak 2004
sum: Reformasi membawa perubahan besar dalam kehidupan bernegara.
fig: table Presiden | Masa jabatan ;; B.J. Habibie | 1998–1999 ;; Abdurrahman Wahid | 1999–2001 ;; Megawati Soekarnoputri | 2001–2004 ;; Susilo Bambang Yudhoyono | 2004–2014 ;; Joko Widodo | 2014–2024 ;; Prabowo Subianto | 2024–sekarang ~ Presiden masa Reformasi.
@ Pembagian benua di dunia
min: 15
act: Warnai peta dunia berdasarkan benua, lalu tulis satu negara di setiap benua.
mis: mengira Australia hanya nama negara, bukan benua
exp: Dunia terbagi menjadi tujuh benua: Asia, Afrika, Amerika Utara, Amerika Selatan, Antartika, Eropa, dan Australia. Asia adalah benua terluas dan berpenduduk terbanyak. Antartika adalah benua terdingin yang hampir tidak berpenghuni. Samudra terluas adalah Samudra Pasifik.
ex: Indonesia terletak di Benua Asia. // Mesir terletak di Benua Afrika.
pt: Tujuh benua ; Asia terluas ; Antartika terdingin
sum: Mengenal benua membantu memahami keragaman dunia.
fig: table Benua | Ciri khas ;; Asia | terluas dan terpadat ;; Afrika | Gurun Sahara ;; Eropa | banyak negara maju ;; Amerika Selatan | hutan Amazon ;; Australia | benua terkecil ;; Antartika | terdingin ~ Benua di dunia.
@ Negara maju dan berkembang
min: 15
act: Bandingkan data pendapatan dan harapan hidup dua negara dari sumber terpercaya.
mis: mengira negara berkembang tidak memiliki kemajuan sama sekali
exp: Negara maju memiliki pendapatan per kapita tinggi, teknologi maju, tingkat pendidikan dan kesehatan baik, serta pertumbuhan penduduk rendah. Negara berkembang sedang meningkatkan pembangunan, dengan pendapatan per kapita menengah atau rendah. Indikator pembangunan manusia diukur dengan Indeks Pembangunan Manusia atau IPM.
ex: Jepang termasuk negara maju. // Indonesia termasuk negara berkembang berpendapatan menengah.
pt: Maju: pendapatan dan teknologi tinggi ; Berkembang: sedang membangun ; Diukur dengan IPM
sum: Setiap negara berupaya meningkatkan kesejahteraan.
fig: table Ciri | Negara maju ;; pendapatan per kapita | tinggi ;; teknologi | maju ;; harapan hidup | panjang ;; pertumbuhan penduduk | rendah ;; sektor utama | industri dan jasa ;; tingkat pendidikan | tinggi rata-rata ~ Ciri negara maju.
# 2|Ekonomi dan Kerja Sama Global
@ Ekspor dan impor
min: 15
act: Periksa label negara pembuat lima barang di rumahmu.
mis: mengira impor selalu merugikan negara
exp: Ekspor adalah menjual barang ke luar negeri, sedangkan impor adalah membeli barang dari luar negeri. Ekspor menambah devisa negara. Impor memenuhi kebutuhan yang belum dapat diproduksi sendiri. Komoditas ekspor Indonesia antara lain kelapa sawit, batu bara, karet, dan tekstil. Selisih ekspor dan impor disebut neraca perdagangan.
ex: Indonesia mengekspor minyak sawit. // Indonesia mengimpor gandum.
pt: Ekspor menjual, impor membeli ; Ekspor menambah devisa ; Neraca perdagangan
sum: Ekspor dan impor menghubungkan ekonomi antarnegara.
fig: table Komoditas | Ekspor atau impor Indonesia ;; minyak sawit | ekspor utama ;; batu bara | ekspor tambang ;; karet | ekspor perkebunan ;; gandum | impor pangan ;; kedelai | impor bahan tempe ;; mesin industri | impor teknologi ~ Komoditas ekspor dan impor.
@ Kurs mata uang
min: 15
act: Cari kurs rupiah terhadap dolar Amerika hari ini, lalu hitung harga barang seharga 10 dolar.
mis: mengira kurs mata uang selalu tetap
exp: Kurs adalah nilai tukar mata uang suatu negara terhadap mata uang negara lain. Kurs dapat naik atau turun dipengaruhi permintaan dan penawaran, inflasi, dan kondisi ekonomi. Kurs beli adalah harga saat bank membeli valuta asing, sedangkan kurs jual saat bank menjual. Mata uang asing disebut valuta asing atau valas.
ex: Jika 1 dolar = Rp16.000, maka 10 dolar = Rp160.000. // Rupiah melemah berarti butuh lebih banyak rupiah untuk 1 dolar.
pt: Nilai tukar antarmata uang ; Naik turun karena permintaan dan penawaran ; Kurs beli dan jual
sum: Kurs memengaruhi harga barang impor dan ekspor.
fig: table Negara | Mata uang ;; Amerika Serikat | dolar ;; Jepang | yen ;; Malaysia | ringgit ;; Arab Saudi | riyal ;; Inggris | pound sterling ;; Korea Selatan | won ~ Mata uang negara lain.
@ Menabung dan investasi
min: 15
act: Buat rencana menabung untuk membeli barang impianmu dalam enam bulan.
mis: tergiur investasi yang menjanjikan untung besar tanpa risiko
exp: Menabung adalah menyisihkan sebagian uang untuk kebutuhan masa depan. Investasi adalah menanam uang atau modal agar berkembang, misalnya deposito, emas, reksa dana, atau saham. Setiap investasi memiliki risiko. Waspadai investasi bodong yang menjanjikan keuntungan sangat tinggi dan tidak terdaftar di OJK.
ex: Menabung di bank aman karena dijamin LPS. // Investasi resmi terdaftar di OJK.
pt: Menabung menyisihkan uang ; Investasi menanam modal ; Waspadai investasi bodong
sum: Menabung dan investasi bijak menyiapkan masa depan.
fig: table Jenis simpanan atau investasi | Ciri ;; tabungan | mudah diambil ;; deposito | jangka waktu tertentu ;; emas | nilai cenderung stabil ;; reksa dana | dikelola manajer investasi ;; saham | kepemilikan perusahaan ;; investasi bodong | untung tidak wajar ~ Jenis simpanan dan investasi.
@ Perserikatan Bangsa-Bangsa
min: 15
act: Cari satu badan PBB yang bekerja di Indonesia, lalu tulis kegiatannya.
mis: mengira PBB hanya mengurus perang
exp: Perserikatan Bangsa-Bangsa atau PBB berdiri pada 24 Oktober 1945 dan bermarkas di New York. Tujuannya menjaga perdamaian, mengembangkan hubungan antarbangsa, dan memajukan kesejahteraan. Indonesia menjadi anggota PBB pada 28 September 1950. PBB memiliki badan khusus seperti UNICEF, UNESCO, WHO, dan FAO.
ex: UNICEF membantu kesehatan dan pendidikan anak. // Pasukan Garuda bertugas dalam misi perdamaian PBB.
pt: Berdiri 24 Oktober 1945 ; Menjaga perdamaian dan kesejahteraan ; Badan UNICEF, UNESCO, WHO
sum: PBB adalah wadah kerja sama bangsa-bangsa dunia.
fig: table Badan PBB | Bidang ;; UNICEF | anak-anak ;; UNESCO | pendidikan dan kebudayaan ;; WHO | kesehatan ;; FAO | pangan dan pertanian ;; ILO | ketenagakerjaan ;; UNHCR | pengungsi ~ Badan khusus PBB.
@ Pelestarian budaya lokal
min: 15
act: Pilih satu budaya daerahmu, lalu buat konten singkat untuk memperkenalkannya.
mis: menganggap budaya lokal kuno dan tidak perlu dilestarikan
exp: Budaya lokal adalah kebudayaan yang tumbuh di suatu daerah, seperti bahasa, tarian, makanan, pakaian, dan upacara adat. Globalisasi dapat menggeser budaya lokal jika tidak dilestarikan. Cara melestarikan antara lain mempelajari dan mempraktikkan budaya, mendokumentasikan, memperkenalkan melalui media digital, dan bangga memakainya.
ex: Memakai bahasa daerah di rumah. // Mengunggah video tari daerah di media sosial.
pt: Bahasa, tari, makanan, adat ; Tergeser bila tidak dilestarikan ; Pelajari, dokumentasikan, promosikan
sum: Budaya lokal adalah identitas yang harus dijaga.
fig: table Bentuk pelestarian | Contoh ;; culture experience | ikut menari tradisional ;; culture knowledge | mendokumentasikan budaya ;; promosi digital | video budaya di internet ;; pendidikan | muatan lokal di sekolah ;; festival | pentas seni daerah ;; pemakaian sehari-hari | berbahasa daerah ~ Cara melestarikan budaya lokal.
@ Pembangunan berkelanjutan
min: 15
act: Pilih satu tujuan pembangunan berkelanjutan, lalu tulis aksi kecil yang dapat kamu lakukan.
mis: mengira pembangunan berkelanjutan hanya urusan pemerintah
exp: Pembangunan berkelanjutan adalah pembangunan yang memenuhi kebutuhan sekarang tanpa mengorbankan kebutuhan generasi mendatang. PBB menetapkan 17 Tujuan Pembangunan Berkelanjutan atau SDGs, antara lain tanpa kemiskinan, pendidikan berkualitas, air bersih, dan penanganan perubahan iklim. Setiap orang dapat berperan melalui aksi sehari-hari.
ex: Menghemat air mendukung tujuan air bersih. // Belajar sungguh-sungguh mendukung pendidikan berkualitas.
pt: Kebutuhan sekarang tanpa merugikan masa depan ; 17 tujuan SDGs ; Semua orang berperan
sum: Aksi kecil mendukung masa depan yang lestari.
fig: table Tujuan SDGs | Aksi pelajar ;; tanpa kemiskinan | berbagi kepada yang membutuhkan ;; tanpa kelaparan | tidak membuang makanan ;; pendidikan berkualitas | belajar sungguh-sungguh ;; air bersih | menghemat air ;; energi bersih | mematikan lampu tak terpakai ;; penanganan iklim | menanam pohon ~ Tujuan SDGs dan aksi pelajar.
"""

BANK += """
## IPA|Listrik statis
Listrik statis adalah muatan listrik yang …|diam|mengalir|berputar|menghilang|Diam.
Muatan sejenis akan saling …|tolak-menolak|tarik-menarik|diam|menghilang|Tolak.
=|Muatan berbeda jenis akan saling …|tarik-menarik|Tarik.
=|Pelepasan listrik statis besar di awan disebut …|petir|Petir.
B|Penggaris yang digosok dapat menarik kertas.|Bermuatan.
S|Muatan sejenis saling tarik-menarik.|Tolak.
Benda menjadi bermuatan karena perpindahan …|elektron|proton|neutron|inti atom|Elektron.
Rambut berdiri setelah melepas sweter karena muatan …|sejenis tolak-menolak|berbeda tarik-menarik|hilang|netral|Sejenis.
## IPA|Kemagnetan
Kutub magnet sejenis akan …|tolak-menolak|tarik-menarik|diam|menyatu|Tolak.
Benda yang dapat ditarik magnet adalah …|paku besi|sendok aluminium|kabel tembaga|penghapus karet|Besi.
=|Magnet memiliki dua kutub, yaitu utara dan …|selatan|Selatan.
=|Magnet yang dibuat dengan arus listrik disebut …|elektromagnet|Elektromagnet.
B|Nikel termasuk benda magnetik.|Nikel.
S|Semua logam dapat ditarik magnet.|Tidak semua.
Logam yang tidak ditarik magnet adalah …|aluminium|besi|baja|kobalt|Aluminium.
Cara membuat magnet dengan menggosok, induksi, dan …|elektromagnet|membakar|memukul keras|membekukan|Elektromagnet.
## IPA|Induksi elektromagnetik
Penemu prinsip induksi elektromagnetik adalah …|Michael Faraday|Isaac Newton|Galileo|Thomas Edison|Faraday.
Alat yang mengubah energi gerak menjadi listrik adalah …|generator|motor listrik|setrika|kipas|Generator.
=|Alat untuk mengubah tegangan listrik bolak-balik disebut …|transformator;trafo|Trafo.
=|Transformator yang menaikkan tegangan disebut transformator step- …|up|Step-up.
B|Dinamo sepeda menyalakan lampu saat roda berputar.|Dinamo.
S|Magnet yang diam di dalam kumparan terus menghasilkan arus.|Harus bergerak.
Pengisi daya HP memakai transformator …|step-down|step-up|generator|dinamo|Turun.
Alat yang mengubah energi listrik menjadi gerak adalah …|motor listrik|generator|dinamo|trafo|Motor.
## IPA|Perkembangbiakan tumbuhan
Cocor bebek berkembang biak dengan …|tunas adventif daun|geragih|umbi|biji|Daun.
Stroberi berkembang biak dengan …|geragih|umbi lapis|cangkok|spora|Geragih.
=|Perkembangbiakan tumbuhan dengan biji disebut …|generatif|Generatif.
=|Singkong diperbanyak dengan … batang.|stek|Stek.
B|Mangga dapat diperbanyak dengan cangkok.|Cangkok.
S|Semua tumbuhan berkembang biak dengan biji.|Vegetatif juga.
Kentang berkembang biak dengan …|umbi batang|geragih|tunas daun|spora|Umbi.
Contoh vegetatif buatan adalah …|okulasi|geragih|umbi|tunas alami|Okulasi.
## IPA|Perkembangbiakan hewan
Hewan yang berkembang biak dengan bertelur disebut …|ovipar|vivipar|ovovivipar|vegetatif|Ovipar.
Kucing berkembang biak dengan cara …|melahirkan|bertelur|membelah diri|tunas|Vivipar.
=|Hewan yang bertelur dan melahirkan disebut …|ovovivipar|Ovovivipar.
=|Amoeba berkembang biak dengan … diri.|membelah|Membelah.
B|Hydra berkembang biak dengan tunas.|Tunas.
S|Semua hewan berkembang biak dengan bertelur.|Beragam.
Planaria berkembang biak dengan …|fragmentasi|bertelur|melahirkan|spora|Fragmentasi.
Contoh hewan ovovivipar adalah …|hiu|ayam|kucing|sapi|Hiu.
## IPA|Sistem indra manusia
Indra untuk membau adalah …|hidung|lidah|kulit|telinga|Hidung.
Selain mendengar, telinga juga berfungsi menjaga …|keseimbangan|penglihatan|rasa|suhu|Keseimbangan.
=|Indra untuk mengecap rasa adalah …|lidah|Lidah.
=|Indra yang merasakan sentuhan dan suhu adalah …|kulit|Kulit.
B|Hidung tersumbat membuat makanan terasa hambar.|Bau dan rasa.
S|Lidah hanya merasakan manis di ujungnya saja.|Tersebar.
Rangsangan bagi mata adalah …|cahaya|bunyi|bau|rasa|Cahaya.
Cara menjaga kesehatan telinga adalah …|tidak mendengar suara terlalu keras|memasukkan benda tajam|mendengar musik keras terus|membiarkan kotor|Telinga.
## IPA|Tanah dan organisme tanah
Lapisan tanah paling subur adalah …|humus|batuan induk|pasir dalam|kerikil|Humus.
Hewan yang menggemburkan tanah adalah …|cacing tanah|ular|tikus|burung|Cacing.
=|Tanah terbentuk dari … batuan.|pelapukan|Pelapukan.
=|Mikroorganisme yang mengurai bahan organik adalah …|bakteri|Bakteri.
B|Akar tumbuhan membantu menahan erosi.|Akar.
S|Cacing tanah merusak kesuburan tanah.|Menyuburkan.
Tanah tersusun atas mineral, bahan organik, air, dan …|udara|plastik|kaca|logam murni|Udara.
Rayap berperan menghancurkan …|kayu mati|batu|plastik|besi|Rayap.
## IPA|Sistem imun
Sel yang melawan kuman di dalam tubuh adalah sel darah …|putih|merah|keping|plasma|Leukosit.
Zat yang mengenali kuman tertentu disebut …|antibodi|antibiotik|hormon|enzim|Antibodi.
=|Pertahanan pertama tubuh dari kuman adalah …|kulit|Kulit.
=|Pemberian vaksin disebut …|imunisasi;vaksinasi|Imunisasi.
B|Tidur cukup membantu sistem imun.|Istirahat.
S|Antibiotik dapat menyembuhkan flu karena virus.|Bakteri.
Lendir hidung berfungsi …|menangkap debu dan kuman|mencerna makanan|mengalirkan darah|menghasilkan suara|Lendir.
Vaksin bekerja dengan cara …|melatih tubuh membentuk kekebalan|membunuh semua sel|menambah gula darah|menghentikan napas|Vaksin.
## IPA|Energi terbarukan
Contoh energi terbarukan adalah …|matahari|batu bara|minyak bumi|gas alam|Terbarukan.
Pembangkit listrik tenaga air disingkat …|PLTA|PLTU|PLTS|PLTB|PLTA.
=|Pembangkit listrik tenaga surya disingkat …|PLTS|PLTS.
=|Pembangkit listrik tenaga panas bumi disingkat …|PLTP|PLTP.
B|Energi terbarukan menghasilkan sedikit emisi karbon.|Ramah.
S|Batu bara termasuk energi terbarukan.|Fosil.
PLTU umumnya memakai bahan bakar …|batu bara|angin|matahari|air|PLTU.
Panel surya mengubah cahaya matahari menjadi energi …|listrik|kimia makanan|bunyi|gerak angin|Listrik.
## IPA|Atom, ion, dan molekul
Partikel atom yang bermuatan positif adalah …|proton|elektron|neutron|ion negatif|Proton.
Partikel atom yang bermuatan negatif adalah …|elektron|proton|neutron|kation|Elektron.
=|Partikel atom yang tidak bermuatan adalah …|neutron|Neutron.
=|Ion bermuatan positif disebut …|kation|Kation.
B|Molekul air terdiri atas dua atom hidrogen dan satu atom oksigen.|H2O.
S|Atom adalah partikel yang tidak memiliki bagian apa pun.|Ada proton dll.
Gabungan dua atom atau lebih disebut …|molekul|ion|proton|elektron|Molekul.
Ion bermuatan negatif disebut …|anion|kation|proton|neutron|Anion.
## IPA|Gerhana matahari dan bulan
Gerhana matahari terjadi saat … berada di tengah.|bulan|bumi|matahari|Mars|Bulan.
Gerhana bulan terjadi saat … berada di tengah.|bumi|bulan|matahari|Venus|Bumi.
=|Gerhana bulan terjadi pada fase bulan …|purnama|Purnama.
=|Gerhana matahari saat bulan tampak lebih kecil dari matahari disebut gerhana …|cincin|Cincin.
B|Gerhana matahari tidak boleh dilihat langsung.|Mata.
S|Gerhana bulan terjadi saat bulan berada di antara matahari dan bumi.|Bumi di tengah.
Gerhana terjadi karena matahari, bumi, dan bulan …|segaris|berjauhan|berputar acak|diam|Segaris.
Gerhana bulan total terjadi saat bulan masuk ke … bumi.|umbra|penumbra saja|atmosfer|orbit|Umbra.
## IPA|Teknologi ramah lingkungan
Lubang resapan air di tanah disebut …|biopori|sumur bor|selokan|kolam|Biopori.
Lampu yang hemat listrik adalah lampu …|LED|pijar|minyak|petromaks|LED.
=|Alat pengolah sampah organik menjadi pupuk disebut …|komposter|Komposter.
=|Menampung air hujan untuk dipakai disebut pemanen air …|hujan|Hujan.
B|Kendaraan listrik mengurangi asap kendaraan.|Asap.
S|Teknologi ramah lingkungan selalu mahal dan rumit.|Banyak sederhana.
Panel surya di atap rumah menghasilkan listrik yang …|bersih|kotor|beracun|berasap|Bersih.
Tujuan teknologi ramah lingkungan adalah …|mengurangi dampak buruk lingkungan|menambah polusi|memperbanyak sampah|boros energi|Tujuan.
## IPS|Masa Demokrasi Liberal
Masa Demokrasi Liberal berlangsung tahun …|1950–1959|1945–1949|1959–1965|1966–1998|1950–1959.
Pemilu pertama Indonesia dilaksanakan tahun …|1955|1945|1971|1999|1955.
=|Konferensi Asia Afrika 1955 diselenggarakan di kota …|Bandung|Bandung.
=|Pada masa Demokrasi Liberal, pemerintahan dipimpin perdana …|menteri|Perdana menteri.
B|Kabinet sering berganti pada masa Demokrasi Liberal.|Tidak stabil.
S|Masa Demokrasi Liberal berlangsung sangat stabil.|Sering berganti.
Masa Demokrasi Liberal berakhir dengan …|Dekrit Presiden 1959|Proklamasi|Supersemar|Reformasi|Dekrit.
Kabinet yang bertanggung jawab kepada parlemen menunjukkan sistem …|parlementer|presidensial|monarki|otoriter|Parlementer.
## IPS|Masa Demokrasi Terpimpin
Demokrasi Terpimpin diawali dengan Dekrit Presiden tanggal …|5 Juli 1959|17 Agustus 1945|11 Maret 1966|21 Mei 1998|5 Juli 1959.
Dekrit Presiden 1959 membubarkan …|Konstituante|DPR|MPR|kabinet|Konstituante.
=|Komando untuk membebaskan Irian Barat disebut …|Trikora|Trikora.
=|Dekrit memberlakukan kembali UUD …|1945|1945.
B|Pada Demokrasi Terpimpin kekuasaan terpusat pada presiden.|Terpusat.
S|Demokrasi Terpimpin memperkuat peran parlemen.|Presiden.
Irian Barat resmi masuk Indonesia pada tahun …|1963|1945|1950|1998|1963.
Demokrasi Terpimpin berakhir setelah peristiwa …|G30S 1965|KAA 1955|Pemilu 1955|Reformasi 1998|1965.
## IPS|Masa Orde Baru
Presiden pada masa Orde Baru adalah …|Soeharto|Soekarno|Habibie|Megawati|Soeharto.
Rencana pembangunan lima tahun disebut …|Repelita|Trikora|Supersemar|Nawacita|Repelita.
=|Indonesia mencapai swasembada beras pada tahun …|1984|1984.
=|Program pengendalian jumlah penduduk disebut Keluarga …|Berencana|KB.
B|Krisis moneter 1997–1998 menyebabkan Orde Baru berakhir.|Krisis.
S|Masa Orde Baru tidak memiliki masalah sama sekali.|KKN.
Program pemindahan penduduk ke pulau lain disebut …|transmigrasi|urbanisasi|emigrasi|imigrasi|Transmigrasi.
Masa Orde Baru berlangsung tahun …|1966–1998|1950–1959|1959–1965|1998–sekarang|1966–1998.
## IPS|Masa Reformasi
Presiden Soeharto mengundurkan diri pada tanggal …|21 Mei 1998|5 Juli 1959|17 Agustus 1945|11 Maret 1966|21 Mei 1998.
Presiden pertama masa Reformasi adalah …|B.J. Habibie|Abdurrahman Wahid|Megawati|Soeharto|Habibie.
=|Pemilihan presiden secara langsung dimulai tahun …|2004|2004.
=|Lembaga yang dibentuk untuk memberantas korupsi disingkat …|KPK|KPK.
B|Amandemen UUD 1945 termasuk tuntutan reformasi.|Amandemen.
S|Reformasi hanya berarti pergantian presiden.|Banyak perubahan.
Presiden Indonesia yang menjabat 2004–2014 adalah …|Susilo Bambang Yudhoyono|Joko Widodo|Megawati|Habibie|SBY.
Kepanjangan KKN adalah korupsi, kolusi, dan …|nepotisme|nasionalisme|normalisasi|naturalisasi|Nepotisme.
## IPS|Pembagian benua di dunia
Jumlah benua di dunia adalah …|tujuh|lima|enam|delapan|Tujuh.
Benua terluas di dunia adalah …|Asia|Afrika|Eropa|Amerika|Asia.
=|Benua terdingin di dunia adalah …|Antartika|Antartika.
=|Samudra terluas di dunia adalah Samudra …|Pasifik|Pasifik.
B|Indonesia terletak di Benua Asia.|Asia.
S|Australia hanya nama negara, bukan benua.|Juga benua.
Gurun Sahara terdapat di Benua …|Afrika|Asia|Australia|Eropa|Afrika.
Hutan Amazon terdapat di Benua …|Amerika Selatan|Afrika|Asia|Eropa|Amazon.
## IPS|Negara maju dan berkembang
Ciri negara maju adalah pendapatan per kapita …|tinggi|rendah|tidak ada|sangat kecil|Tinggi.
Indikator pembangunan manusia disingkat …|IPM|IHK|APBN|PDB|IPM.
=|Pertumbuhan penduduk negara maju umumnya …|rendah|Rendah.
=|Sektor utama ekonomi negara maju adalah industri dan …|jasa|Jasa.
B|Jepang termasuk negara maju.|Jepang.
S|Negara berkembang sama sekali tidak mengalami kemajuan.|Sedang membangun.
Indonesia termasuk negara …|berkembang|maju|terbelakang|miskin total|Berkembang.
Harapan hidup di negara maju umumnya …|panjang|pendek|sama dengan nol|tidak terukur|Panjang.
## IPS|Ekspor dan impor
Menjual barang ke luar negeri disebut …|ekspor|impor|distribusi|konsumsi|Ekspor.
Membeli barang dari luar negeri disebut …|impor|ekspor|produksi|investasi|Impor.
=|Ekspor menambah … negara.|devisa|Devisa.
=|Selisih nilai ekspor dan impor disebut neraca …|perdagangan|Neraca perdagangan.
B|Minyak sawit adalah komoditas ekspor utama Indonesia.|Sawit.
S|Impor selalu merugikan negara.|Memenuhi kebutuhan.
Komoditas yang banyak diimpor Indonesia untuk bahan tempe adalah …|kedelai|karet|batu bara|kopi|Kedelai.
Gandum termasuk komoditas … Indonesia.|impor|ekspor utama|tambang|perkebunan ekspor|Impor.
## IPS|Kurs mata uang
Nilai tukar mata uang disebut …|kurs|devisa|inflasi|pajak|Kurs.
Jika 1 dolar = Rp16.000, maka 10 dolar = …|Rp160.000|Rp16.000|Rp1.600|Rp1.600.000|16.000 × 10.
=|Mata uang Jepang adalah …|yen|Yen.
=|Mata uang asing disebut valuta …|asing|Valas.
B|Kurs dapat naik atau turun.|Berubah.
S|Kurs mata uang selalu tetap.|Berubah.
Mata uang Malaysia adalah …|ringgit|baht|won|riyal|Ringgit.
Harga saat bank membeli valuta asing disebut kurs …|beli|jual|tengah|tetap|Kurs beli.
## IPS|Menabung dan investasi
Menyisihkan sebagian uang untuk masa depan disebut …|menabung|berbelanja|berutang|membuang|Menabung.
Lembaga yang mengawasi investasi resmi di Indonesia adalah …|OJK|KPU|BMKG|BPOM|OJK.
=|Investasi palsu yang menjanjikan untung tidak wajar disebut investasi …|bodong|Bodong.
=|Simpanan bank dengan jangka waktu tertentu disebut …|deposito|Deposito.
B|Setiap investasi memiliki risiko.|Risiko.
S|Investasi yang menjanjikan untung sangat tinggi tanpa risiko pasti aman.|Bodong.
Membeli saham berarti memiliki sebagian …|perusahaan|bank sentral|negara|pasar|Saham.
Reksa dana dikelola oleh …|manajer investasi|guru|kepala desa|ketua RT|Manajer.
## IPS|Perserikatan Bangsa-Bangsa
PBB berdiri pada tanggal …|24 Oktober 1945|17 Agustus 1945|28 September 1950|1 Juni 1945|24 Oktober.
Markas besar PBB berada di …|New York|Jenewa|Jakarta|London|New York.
=|Badan PBB untuk anak-anak adalah …|UNICEF|UNICEF.
=|Badan PBB untuk kesehatan adalah …|WHO|WHO.
B|Indonesia menjadi anggota PBB pada 1950.|1950.
S|PBB hanya mengurus perang.|Banyak bidang.
Badan PBB yang mengurus pendidikan dan kebudayaan adalah …|UNESCO|FAO|ILO|UNHCR|UNESCO.
Badan PBB yang mengurus pengungsi adalah …|UNHCR|UNICEF|WHO|FAO|UNHCR.
## IPS|Pelestarian budaya lokal
Contoh budaya lokal adalah …|tari daerah|aplikasi asing|merek luar negeri|film impor|Lokal.
Budaya lokal dapat tergeser oleh …|globalisasi|gotong royong|musyawarah|toleransi|Globalisasi.
=|Ikut menari tradisional termasuk pelestarian culture …|experience|Experience.
=|Mendokumentasikan budaya termasuk pelestarian culture …|knowledge|Knowledge.
B|Mengunggah video tari daerah membantu pelestarian.|Digital.
S|Budaya lokal kuno sehingga tidak perlu dilestarikan.|Identitas.
Memakai bahasa daerah di rumah termasuk pelestarian melalui …|pemakaian sehari-hari|festival|promosi asing|larangan|Sehari-hari.
Pentas seni daerah yang meriah disebut …|festival|seminar|rapat|ujian|Festival.
## IPS|Pembangunan berkelanjutan
Singkatan Tujuan Pembangunan Berkelanjutan dalam bahasa Inggris adalah …|SDGs|PBB|IPM|APBN|SDGs.
Jumlah Tujuan Pembangunan Berkelanjutan adalah …|17|10|5|25|17.
=|Menghemat air mendukung tujuan air …|bersih|Air bersih.
=|Menanam pohon mendukung penanganan perubahan …|iklim|Iklim.
B|Setiap orang dapat berperan dalam pembangunan berkelanjutan.|Semua.
S|Pembangunan berkelanjutan hanya urusan pemerintah.|Semua orang.
Tidak membuang makanan mendukung tujuan …|tanpa kelaparan|energi bersih|kota berkelanjutan|kehidupan laut|Pangan.
Pembangunan berkelanjutan memperhatikan kebutuhan generasi …|mendatang|lalu saja|sekarang saja|tertentu|Mendatang.
"""

SAS += """
## IPA 1
0|Kejutan saat memegang gagang pintu terjadi karena ....|pelepasan muatan listrik statis|arus listrik PLN|magnet|panas|Statis.
1|Kabel tembaga termasuk benda ....|nonmagnetik|magnetik kuat|magnetik lemah|elektromagnet|Tembaga.
2|Senter kocok menghasilkan listrik dari ....|goyangan magnet dalam kumparan|baterai saja|cahaya matahari|panas tangan|Induksi.
3|Pisang berkembang biak secara vegetatif dengan ....|tunas|geragih|umbi lapis|biji|Tunas.
4|Hewan yang melahirkan disebut ....|vivipar|ovipar|ovovivipar|vegetatif|Vivipar.
5|Bagian telinga dalam berfungsi menjaga ....|keseimbangan|penciuman|perasa|penglihatan|Keseimbangan.
## IPA 2
0|Semut berperan dalam tanah dengan ....|mengaduk lapisan tanah|menahan erosi|mengurai kayu|membuat batuan|Semut.
1|Air mata berfungsi ....|membunuh kuman di mata|mencerna makanan|menghasilkan antibodi|mengatur suhu|Air mata.
2|PLTB memakai energi ....|angin|air|matahari|batu bara|PLTB.
3|Molekul air bermuatan ....|netral|positif|negatif|ganda|Netral.
4|Gerhana yang hanya menutup sebagian disebut gerhana ....|sebagian|total|cincin|purnama|Sebagian.
5|Pemanen air hujan bermanfaat untuk ....|hemat air bersih|menambah banjir|membuang air|mengeringkan sumur|Hemat.
## IPS 1
0|Dekrit Presiden yang mengakhiri Demokrasi Liberal dikeluarkan tahun ....|1959|1955|1950|1965|1959.
1|Dewan Pertimbangan Agung Sementara dibentuk pada masa ....|Demokrasi Terpimpin|Orde Baru|Reformasi|Demokrasi Liberal|DPAS.
2|Surat perintah yang menjadi awal kekuasaan Soeharto adalah ....|Supersemar|Trikora|Dekrit|Repelita|Supersemar.
3|Presiden Indonesia periode 1999–2001 adalah ....|Abdurrahman Wahid|Habibie|Megawati|SBY|Gus Dur.
4|Benua terkecil di dunia adalah ....|Australia|Eropa|Antartika|Asia|Australia.
5|Tingkat pendidikan rata-rata negara maju umumnya ....|tinggi|rendah|tidak ada|sangat kurang|Tinggi.
## IPS 2
0|Mesin industri termasuk komoditas ... Indonesia.|impor|ekspor utama|perkebunan|tambang|Impor.
1|Mata uang Korea Selatan adalah ....|won|yen|ringgit|riyal|Won.
2|Tabungan memiliki ciri ....|mudah diambil|tidak boleh diambil|tanpa bunga sama sekali|harus lima tahun|Tabungan.
3|Badan PBB yang mengurus pangan dan pertanian adalah ....|FAO|ILO|WHO|UNICEF|FAO.
4|Muatan lokal di sekolah termasuk pelestarian budaya melalui ....|pendidikan|festival|promosi asing|pariwisata|Pendidikan.
5|Mematikan lampu yang tidak terpakai mendukung tujuan ....|energi bersih|tanpa kelaparan|air bersih|pendidikan|Energi.
"""

TOPICS += """
## BIG
# 1|Grammar and Functional Texts
@ Present perfect tense
min: 15
act: Write five sentences about things you have done this year using the present perfect tense.
mis: memakai keterangan waktu lampau spesifik seperti yesterday dengan present perfect
exp: Present perfect tense menyatakan pengalaman atau kejadian yang sudah terjadi dan masih berhubungan dengan sekarang. Polanya subjek + have atau has + kata kerja bentuk ketiga. Kata yang sering dipakai antara lain already, yet, ever, never, since, dan for.
ex: I have visited Bali. // She has already finished her homework.
pt: Pengalaman yang berhubungan dengan sekarang ; Subjek + have/has + verb 3 ; Already, yet, since, for
sum: Present perfect menghubungkan masa lalu dan sekarang.
fig: table Subject | Auxiliary ;; I | have ;; you | have dengan you ;; she | has ;; he | has dengan he ;; we | have dengan we ;; it | has dengan it ~ Pasangan subjek dan have/has.
@ Giving suggestions
min: 15
act: Give three suggestions to a friend who feels tired before an exam.
mis: menambahkan to setelah should
exp: Giving suggestions adalah memberi saran. Ungkapannya antara lain You should..., Why don't you...?, How about + verb-ing?, dan I suggest that.... Respons menerima: That's a good idea. Respons menolak dengan sopan: Thanks, but I don't think so.
ex: You should get enough sleep. // How about studying together?
pt: Memberi saran ; Should, why don't you, how about ; Menerima atau menolak sopan
sum: Saran yang sopan mudah diterima.
fig: table Expression | Pattern ;; You should rest. | should + verb 1 ;; Why don't you rest? | why don't you + verb 1 ;; How about resting? | how about + verb-ing ;; I suggest you rest. | suggest + clause ;; Let's rest. | let's + verb 1 ;; That's a good idea. | accepting a suggestion ~ Ungkapan memberi saran.
@ Expressing hopes and wishes
min: 15
act: Write your hopes for this school year and a wish card for a friend.
mis: memakai wish untuk harapan yang mungkin terjadi
exp: Hope dipakai untuk harapan yang mungkin terjadi, misalnya I hope I pass the exam. Wish dipakai untuk keinginan yang sulit atau tidak mungkin terjadi, misalnya I wish I could fly. Wish juga dipakai untuk mendoakan orang, misalnya I wish you all the best.
ex: I hope it doesn't rain tomorrow. // I wish I had a pet dragon.
pt: Hope: mungkin terjadi ; Wish: sulit atau tidak mungkin ; Wish you all the best
sum: Hope dan wish dipakai pada situasi yang berbeda.
fig: table Sentence | Meaning ;; I hope I pass. | harapan mungkin terjadi ;; I wish I could fly. | khayalan tidak mungkin ;; I wish you luck. | mendoakan orang ;; Hopefully, it will be sunny. | semoga ;; I hope so. | setuju dengan harapan ;; I hope not. | berharap tidak terjadi ~ Hope dan wish.
@ Relative pronouns
min: 15
act: Combine pairs of sentences about your classmates using who, which, or that.
mis: memakai which untuk orang
exp: Relative pronouns menghubungkan dua kalimat dengan menjelaskan kata benda. Who dipakai untuk orang, which untuk benda atau hewan, that untuk orang maupun benda, whose untuk kepemilikan, dan where untuk tempat.
ex: The girl who sits next to me is smart. // The book which I bought is interesting.
pt: Menjelaskan kata benda ; Who orang, which benda ; Whose milik, where tempat
sum: Relative pronouns membuat kalimat lebih padat.
fig: table Relative pronoun | Used for ;; who | people ;; which | things or animals ;; that | people or things ;; whose | possession ;; where | places ;; when | time ~ Relative pronouns.
@ Gerunds
min: 15
act: Write five sentences about your hobbies using gerunds after like, enjoy, and love.
mis: memakai to infinitive setelah enjoy
exp: Gerund adalah kata kerja berakhiran -ing yang berfungsi sebagai kata benda. Gerund dapat menjadi subjek, objek, atau sesudah preposisi. Kata kerja yang diikuti gerund antara lain enjoy, finish, avoid, dan mind. Contoh: Swimming is fun.
ex: I enjoy reading comics. // She is good at drawing.
pt: Verb-ing sebagai kata benda ; Subjek, objek, sesudah preposisi ; Enjoy, finish, avoid + gerund
sum: Gerund mengubah kegiatan menjadi kata benda.
fig: table Sentence | Function of gerund ;; Swimming is fun. | subject ;; I enjoy reading. | object ;; She is good at drawing. | after preposition ;; My hobby is cooking. | complement ;; Stop talking, please. | object of stop ;; Thank you for coming. | after for ~ Fungsi gerund.
@ Writing formal emails
min: 15
act: Write a formal email to your teacher asking for permission to submit homework late.
mis: memakai bahasa gaul dan singkatan dalam email resmi
exp: Email resmi memiliki subjek yang jelas, salam pembuka resmi seperti Dear Mr. or Ms., isi yang singkat dan sopan, salam penutup seperti Best regards atau Sincerely, serta nama pengirim. Hindari singkatan gaul dan emoji. Periksa ejaan sebelum mengirim.
ex: Subject: Permission to submit homework late. // Dear Ms. Rina, I am writing to ask...
pt: Subjek jelas ; Dear dan Best regards ; Sopan tanpa singkatan gaul
sum: Email resmi yang rapi memberi kesan baik.
fig: table Part of email | Example ;; subject | Permission request ;; greeting | Dear Ms. Rina, ;; opening line | I am writing to ask... ;; body | the main message ;; closing | Best regards, ;; signature | your full name ~ Bagian email resmi.
# 2|Communication and Texts
@ Agreeing and disagreeing
min: 15
act: Discuss with a partner whether students should wear uniforms, agreeing or disagreeing politely.
mis: menyatakan tidak setuju dengan kasar seperti You are wrong!
exp: Agreeing adalah menyatakan setuju, misalnya I agree with you atau That's right. Disagreeing adalah menyatakan tidak setuju dengan sopan, misalnya I'm afraid I disagree atau I see your point, but.... Sertakan alasan agar pendapat lebih kuat.
ex: I agree because uniforms make us look neat. // I see your point, but uniforms can be expensive.
pt: Agreeing menyatakan setuju ; Disagreeing dengan sopan ; Sertakan alasan
sum: Berbeda pendapat tetap harus sopan.
fig: table Expression | Function ;; I agree with you. | agreeing ;; That's exactly right. | strong agreeing ;; I think so too. | agreeing softly ;; I'm afraid I disagree. | polite disagreeing ;; I see your point, but... | partial disagreeing ;; I don't think so. | disagreeing ~ Ungkapan setuju dan tidak setuju.
@ Reported speech
min: 15
act: Report three things your teacher said today using reported speech.
mis: tidak mengubah kata ganti dan tense saat melaporkan ucapan
exp: Reported speech atau kalimat tidak langsung melaporkan ucapan orang lain tanpa kutipan. Biasanya tense mundur satu langkah, misalnya present menjadi past, serta kata ganti dan keterangan waktu disesuaikan. Contoh: She said, "I am tired." menjadi She said that she was tired.
ex: He said that he liked pizza. // She told me that she would come.
pt: Melaporkan ucapan tanpa kutipan ; Tense mundur satu langkah ; Kata ganti dan waktu disesuaikan
sum: Reported speech menceritakan ulang ucapan orang lain.
fig: table Direct | Reported ;; "I am tired." | she was tired ;; "I like pizza." | he liked pizza ;; "I will come." | she would come ;; "I can swim." | he could swim ;; today | that day ;; tomorrow | the next day ~ Perubahan dalam reported speech.
@ Modals should and might
min: 15
act: Write three advice sentences with should and three possibility sentences with might.
mis: menambahkan -s pada kata kerja setelah modal
exp: Modal should dipakai untuk memberi saran atau kewajiban ringan, misalnya You should drink water. Modal might dipakai untuk kemungkinan kecil, misalnya It might rain later. Setelah modal selalu memakai kata kerja bentuk dasar tanpa to dan tanpa -s.
ex: You should wear a helmet. // She might come to the party.
pt: Should untuk saran ; Might untuk kemungkinan ; Modal + verb dasar
sum: Modal mengubah makna kalimat.
fig: table Modal | Meaning ;; should | saran ;; might | kemungkinan kecil ;; must | keharusan ;; can | kemampuan ;; may | izin atau kemungkinan ;; could | kemampuan lampau ~ Makna modal.
@ Biography text
min: 15
act: Write a short biography of a national hero in English.
mis: menulis biografi dengan present tense untuk peristiwa lampau
exp: Biography text menceritakan kisah hidup seseorang yang ditulis oleh orang lain. Strukturnya terdiri atas orientation yang memperkenalkan tokoh, events yang menceritakan peristiwa penting secara berurutan, dan reorientation berisi penutup. Biografi memakai simple past tense dan keterangan waktu.
ex: B.J. Habibie was born in Parepare in 1936. // He became the third president of Indonesia.
pt: Kisah hidup ditulis orang lain ; Orientation, events, reorientation ; Simple past tense
sum: Biografi menginspirasi lewat kisah nyata.
fig: table Part | Content ;; orientation | introducing the person ;; event 1 | early life ;; event 2 | education ;; event 3 | achievements ;; reorientation | closing comment ;; language feature | simple past tense ~ Struktur biography text.
@ Explanation text
min: 15
act: Explain how rain happens in English using a simple diagram.
mis: menulis explanation text seperti cerita pribadi
exp: Explanation text menjelaskan bagaimana atau mengapa suatu peristiwa alam atau sosial terjadi. Strukturnya terdiri atas general statement, sequence of explanation, dan closing. Ciri bahasanya memakai simple present tense, kata urutan seperti first, then, finally, serta hubungan sebab akibat.
ex: First, the sun heats the water. // Then, the vapor forms clouds.
pt: Menjelaskan bagaimana atau mengapa ; General statement dan sequence ; Present tense dan kata urutan
sum: Explanation text menerangkan proses dengan runtut.
fig: table Word | Use ;; first | langkah pertama ;; then | langkah berikutnya ;; after that | sesudahnya ;; finally | langkah terakhir ;; because | sebab ;; as a result | akibat ~ Kata penghubung explanation text.
@ Prepositions of place and time
min: 15
act: Describe your room and daily schedule using in, on, at, under, and next to.
mis: memakai in untuk jam seperti in 7 o'clock
exp: Prepositions of place menunjukkan letak, misalnya in, on, under, next to, between, dan behind. Prepositions of time menunjukkan waktu: at untuk jam dan waktu tertentu, on untuk hari dan tanggal, in untuk bulan, tahun, dan bagian hari.
ex: The cat is under the table. // I wake up at 5 a.m. on Monday.
pt: Preposition tempat ; At jam, on hari, in bulan ; Under, next to, between
sum: Preposition yang tepat membuat keterangan jelas.
fig: table Phrase | Preposition used ;; 7 o'clock | at ;; Monday | on ;; July | in ;; 2026 | in a year ;; the morning | in part of day ;; night | at night ~ Preposition of time.

## PPK
# 1|Hak Asasi dan Hukum
@ Pelanggaran HAM dan penegakannya
min: 15
act: Cari satu contoh pelanggaran hak di lingkungan sekolah, lalu tulis cara mencegahnya.
mis: mengira perundungan bukan pelanggaran hak
exp: Pelanggaran HAM adalah perbuatan yang mengurangi, menghalangi, atau mencabut hak asasi orang lain. Contoh di lingkungan sekitar antara lain perundungan, diskriminasi, dan kekerasan. Penegakan HAM dilakukan melalui upaya pencegahan, seperti pendidikan dan aturan, serta penindakan melalui proses hukum.
ex: Mengejek teman karena fisiknya melanggar hak atas rasa aman. // Sekolah membuat aturan antiperundungan.
pt: Mengurangi atau mencabut hak orang lain ; Perundungan, diskriminasi, kekerasan ; Pencegahan dan penindakan
sum: Menghormati hak orang lain mencegah pelanggaran HAM.
fig: table Perbuatan | Hak yang dilanggar ;; perundungan | hak atas rasa aman ;; melarang beribadah | hak beragama ;; mempekerjakan anak | hak pendidikan anak ;; diskriminasi suku | hak diperlakukan sama ;; menyebar data pribadi | hak privasi ;; membungkam pendapat | hak berpendapat ~ Contoh pelanggaran hak.
@ Lembaga perlindungan HAM
min: 15
act: Cari tahu tugas Komnas HAM dan KPAI, lalu buat bagan perbandingannya.
mis: mengira hanya polisi yang menangani masalah HAM
exp: Indonesia memiliki lembaga perlindungan HAM. Komnas HAM melakukan penyelidikan dan pemantauan pelanggaran HAM. KPAI melindungi hak anak. Komnas Perempuan menangani kekerasan terhadap perempuan. Pengadilan HAM mengadili pelanggaran HAM berat. LPSK melindungi saksi dan korban.
ex: KPAI menerima laporan kekerasan terhadap anak. // LPSK melindungi saksi dalam persidangan.
pt: Komnas HAM menyelidiki ; KPAI melindungi anak ; Pengadilan HAM mengadili pelanggaran berat
sum: Lembaga HAM menjaga hak setiap warga.
fig: table Lembaga | Tugas ;; Komnas HAM | menyelidiki pelanggaran HAM ;; KPAI | melindungi hak anak ;; Komnas Perempuan | menangani kekerasan terhadap perempuan ;; Pengadilan HAM | mengadili pelanggaran berat ;; LPSK | melindungi saksi dan korban ;; Ombudsman | mengawasi pelayanan publik ~ Lembaga perlindungan HAM.
@ Supremasi hukum
min: 15
act: Diskusikan contoh sikap taat hukum yang bisa dilakukan pelajar setiap hari.
mis: mengira orang berkuasa boleh kebal hukum
exp: Indonesia adalah negara hukum sesuai Pasal 1 ayat 3 UUD 1945. Supremasi hukum berarti hukum menjadi kekuasaan tertinggi dan berlaku sama bagi semua orang tanpa kecuali. Asas persamaan di depan hukum menjamin setiap warga diperlakukan adil. Warga wajib menaati hukum, misalnya aturan lalu lintas.
ex: Pejabat yang korupsi tetap diadili. // Pelajar menaati aturan lalu lintas.
pt: Negara hukum Pasal 1 ayat 3 ; Hukum berlaku sama bagi semua ; Persamaan di depan hukum
sum: Tidak ada yang kebal hukum.
fig: table Ciri negara hukum | Keterangan ;; supremasi hukum | hukum tertinggi ;; persamaan di depan hukum | semua warga sama ;; perlindungan HAM | hak dijamin ;; peradilan bebas | hakim tidak diintervensi ;; asas legalitas | tindakan berdasarkan aturan ;; pembagian kekuasaan | lembaga saling mengawasi ~ Ciri negara hukum.
@ Peradilan di Indonesia
min: 15
act: Buat bagan tingkatan peradilan dari pengadilan negeri sampai Mahkamah Agung.
mis: mengira semua perkara langsung dibawa ke Mahkamah Agung
exp: Kekuasaan kehakiman di Indonesia dijalankan Mahkamah Agung dan Mahkamah Konstitusi. Di bawah Mahkamah Agung ada empat lingkungan peradilan: peradilan umum, agama, militer, dan tata usaha negara. Tingkatannya pengadilan tingkat pertama, banding di pengadilan tinggi, dan kasasi di Mahkamah Agung.
ex: Perkara pencurian diadili di pengadilan negeri. // Perkara warisan muslim diadili di pengadilan agama.
pt: MA dan MK ; Empat lingkungan peradilan ; Tingkat pertama, banding, kasasi
sum: Peradilan berjenjang menjamin keadilan.
fig: table Lingkungan peradilan | Perkara ;; peradilan umum | pidana dan perdata ;; peradilan agama | perkawinan dan warisan muslim ;; peradilan militer | perkara anggota TNI ;; peradilan tata usaha negara | sengketa keputusan pejabat ;; Mahkamah Konstitusi | uji undang-undang ;; Mahkamah Agung | kasasi ~ Lingkungan peradilan.
@ Pemberantasan korupsi
min: 15
act: Cari berita upaya pencegahan korupsi, lalu tulis dampak korupsi bagi masyarakat.
mis: mengira korupsi hanya dilakukan pejabat besar
exp: Korupsi adalah penyalahgunaan wewenang atau kepercayaan untuk keuntungan pribadi yang merugikan orang banyak. Bentuknya antara lain suap, penggelapan, pemerasan, dan gratifikasi. Korupsi merugikan negara dan menghambat pembangunan. Pemberantasan dilakukan KPK, kepolisian, dan kejaksaan, serta pendidikan antikorupsi.
ex: Suap kepada petugas agar urusan cepat. // Dana bantuan diambil untuk diri sendiri.
pt: Penyalahgunaan wewenang ; Suap, penggelapan, gratifikasi ; KPK, polisi, jaksa
sum: Korupsi merugikan semua orang.
fig: table Bentuk korupsi | Contoh ;; suap | memberi uang agar diluluskan ;; penggelapan | memakai uang kas pribadi ;; pemerasan | memaksa minta uang ;; gratifikasi | hadiah karena jabatan ;; kolusi | kerja sama curang ;; nepotisme | mengutamakan keluarga ~ Bentuk korupsi.
@ Sikap antikorupsi
min: 15
act: Buat komitmen kelas tentang kejujuran saat ujian dan pengelolaan uang kas.
mis: menganggap mencontek dan titip absen sebagai hal sepele
exp: Sikap antikorupsi dibangun sejak dini melalui sembilan nilai antikorupsi: jujur, peduli, mandiri, disiplin, tanggung jawab, kerja keras, sederhana, berani, dan adil. Contoh di sekolah antara lain tidak mencontek, tidak titip absen, mengelola uang kas secara terbuka, dan datang tepat waktu.
ex: Bendahara kelas melaporkan uang kas setiap bulan. // Mengerjakan ujian sendiri.
pt: Sembilan nilai antikorupsi ; Jujur, disiplin, tanggung jawab ; Dibangun sejak dini
sum: Antikorupsi dimulai dari kejujuran kecil.
fig: table Nilai antikorupsi | Contoh di sekolah ;; jujur | tidak mencontek ;; disiplin | datang tepat waktu ;; tanggung jawab | mengerjakan piket ;; sederhana | tidak pamer barang ;; adil | membagi tugas merata ;; berani | menolak ajakan curang ~ Nilai antikorupsi.
# 2|Negara Kesatuan dan Hubungan Internasional
@ Bentuk negara kesatuan
min: 15
act: Bandingkan negara kesatuan dan negara federal dengan contoh negaranya.
mis: mengira Indonesia berbentuk negara federal
exp: Indonesia adalah negara kesatuan berbentuk republik sesuai Pasal 1 ayat 1 UUD 1945. Dalam negara kesatuan hanya ada satu pemerintahan pusat, satu konstitusi, dan satu kepala negara. Bentuk negara kesatuan tidak dapat diubah sesuai Pasal 37 ayat 5. Indonesia pernah menjadi RIS pada 1949–1950.
ex: Pemerintah pusat berkedudukan di ibu kota negara. // Amerika Serikat adalah negara federal.
pt: Negara kesatuan berbentuk republik ; Satu pemerintahan pusat dan konstitusi ; Tidak dapat diubah
sum: NKRI adalah bentuk final negara Indonesia.
fig: table Ciri | Negara kesatuan ;; pemerintahan | satu pusat ;; konstitusi | satu UUD ;; kepala negara | satu presiden ;; daerah | provinsi dan kabupaten ;; kedaulatan | di tangan pusat ;; contoh negara | Indonesia ~ Ciri negara kesatuan.
@ Pembagian wilayah administratif
min: 15
act: Tulis nama provinsi, kabupaten atau kota, kecamatan, dan desa atau kelurahan tempat tinggalmu.
mis: menyamakan kelurahan dengan desa
exp: Wilayah Indonesia dibagi menjadi provinsi, lalu kabupaten dan kota, kecamatan, serta desa dan kelurahan. Provinsi dipimpin gubernur, kabupaten dipimpin bupati, kota dipimpin wali kota, kecamatan dipimpin camat, desa dipimpin kepala desa yang dipilih warga, dan kelurahan dipimpin lurah yang diangkat.
ex: Kota Bandung dipimpin wali kota. // Kepala desa dipilih langsung oleh warga.
pt: Provinsi, kabupaten/kota, kecamatan, desa/kelurahan ; Gubernur, bupati, wali kota, camat ; Kepala desa dipilih, lurah diangkat
sum: Pembagian wilayah memudahkan pelayanan masyarakat.
fig: table Wilayah | Pemimpin ;; provinsi | gubernur ;; kabupaten | bupati ;; kota | wali kota ;; kecamatan | camat ;; desa | kepala desa ;; kelurahan | lurah ~ Wilayah administratif dan pemimpinnya.
@ Integrasi nasional
min: 15
act: Diskusikan faktor pendorong persatuan di daerahmu yang beragam suku dan agama.
mis: menganggap integrasi berarti menyeragamkan budaya
exp: Integrasi nasional adalah penyatuan berbagai kelompok budaya dan sosial menjadi satu bangsa yang utuh. Faktor pendorongnya antara lain Pancasila, bahasa Indonesia, sejarah perjuangan bersama, dan semboyan Bhinneka Tunggal Ika. Faktor penghambatnya antara lain primordialisme berlebihan, kesenjangan, dan hoaks.
ex: Bahasa Indonesia menyatukan warga dari berbagai daerah. // Hoaks SARA dapat memecah persatuan.
pt: Penyatuan kelompok menjadi bangsa ; Pancasila dan bahasa Indonesia ; Hambatan primordialisme dan hoaks
sum: Integrasi nasional menghargai perbedaan dalam persatuan.
fig: table Faktor | Pendorong atau penghambat ;; Pancasila | pendorong ;; bahasa Indonesia | pendorong pemersatu ;; sejarah perjuangan bersama | pendorong rasa senasib ;; primordialisme berlebihan | penghambat ;; kesenjangan ekonomi | penghambat kecemburuan ;; hoaks SARA | penghambat perpecahan ~ Faktor integrasi nasional.
@ Politik luar negeri bebas aktif
min: 15
act: Cari satu peran Indonesia dalam forum internasional, lalu hubungkan dengan politik bebas aktif.
mis: mengira bebas berarti Indonesia tidak peduli urusan dunia
exp: Politik luar negeri Indonesia bebas aktif. Bebas berarti tidak memihak blok kekuatan mana pun. Aktif berarti ikut serta menciptakan perdamaian dunia sesuai Pembukaan UUD 1945 alinea keempat. Prinsip ini dicetuskan Mohammad Hatta dalam pidato Mendayung di Antara Dua Karang tahun 1948.
ex: Indonesia memprakarsai Gerakan Non-Blok. // Indonesia mengirim pasukan perdamaian PBB.
pt: Bebas tidak memihak blok ; Aktif menjaga perdamaian ; Dicetuskan Mohammad Hatta 1948
sum: Bebas aktif menjadikan Indonesia sahabat semua bangsa.
fig: table Peran Indonesia | Wujud bebas aktif ;; KAA 1955 | solidaritas Asia Afrika ;; Gerakan Non-Blok | tidak memihak blok ;; ASEAN | kerja sama kawasan ;; Pasukan Garuda | misi perdamaian PBB ;; Jakarta Informal Meeting | perdamaian Kamboja ;; bantuan kemanusiaan | menolong korban bencana dunia ~ Wujud politik bebas aktif.
@ Diplomasi Indonesia
min: 15
act: Cari nama kedutaan besar Indonesia di tiga negara dan tugas duta besar.
mis: mengira duta besar hanya bertugas berlibur di luar negeri
exp: Diplomasi adalah cara negara menjalin hubungan dengan negara lain melalui perundingan. Perwakilan diplomatik dipimpin duta besar di kedutaan besar, sedangkan perwakilan konsuler dipimpin konsul yang mengurus warga dan perdagangan. Diplomasi berperan dalam pengakuan kemerdekaan Indonesia, misalnya melalui Konferensi Meja Bundar 1949.
ex: KBRI melindungi WNI di luar negeri. // Konferensi Meja Bundar menghasilkan pengakuan kedaulatan.
pt: Hubungan negara melalui perundingan ; Duta besar dan konsul ; Konferensi Meja Bundar 1949
sum: Diplomasi memperjuangkan kepentingan bangsa secara damai.
fig: table Perwakilan | Tugas ;; duta besar | mewakili negara secara politik ;; konsul | mengurus warga dan dagang ;; atase pendidikan | urusan pendidikan ;; atase pertahanan | urusan militer ;; KBRI | kantor kedutaan ;; KJRI | kantor konsulat ~ Perwakilan diplomatik.
@ Pemuda menghadapi globalisasi
min: 15
act: Buat rencana satu kegiatan positif untuk mengenalkan budaya Indonesia di internet.
mis: menganggap globalisasi hanya membawa dampak buruk
exp: Globalisasi membuka peluang dan tantangan bagi pemuda. Peluangnya antara lain akses ilmu pengetahuan, teknologi, dan pasar dunia. Tantangannya antara lain budaya konsumtif, hoaks, dan lunturnya budaya lokal. Pemuda perlu menguasai teknologi, berpikir kritis, berbahasa asing, dan tetap berjati diri Indonesia.
ex: Pemuda menjual kerajinan daerah secara daring ke luar negeri. // Menyaring informasi sebelum membagikan.
pt: Peluang ilmu, teknologi, pasar ; Tantangan konsumtif dan hoaks ; Kuasai teknologi dan tetap berjati diri
sum: Pemuda yang cakap mampu bersaing tanpa kehilangan jati diri.
fig: table Bekal pemuda | Manfaat ;; menguasai teknologi | bersaing di era digital ;; berbahasa asing | berkomunikasi global ;; berpikir kritis | menyaring informasi ;; kewirausahaan | menciptakan lapangan kerja ;; cinta budaya | menjaga jati diri ;; kolaborasi | bekerja dalam tim ~ Bekal pemuda di era global.
"""

BANK += """
## BIG|Present perfect tense
The pattern of the present perfect tense is subject + have/has + …|verb 3|verb 1|verb 2|verb-ing|V3.
Complete: She … already finished her homework.|has|have|is|did|She has.
=|Complete: I … visited Bali.|have|I have.
=|The past participle of eat is …|eaten|Eaten.
B|"I have never seen snow" is in the present perfect tense.|Never.
S|"I have visited Bali yesterday" is correct.|Yesterday is past.
Which word is often used in the present perfect tense?|already|yesterday|last week|ago|Already.
"We have lived here … 2020."|since|for|ago|at|Since.
## BIG|Giving suggestions
"You should rest" is used to …|give a suggestion|apologize|complain|congratulate|Saran.
After "how about" we use …|verb-ing|verb 2|to + verb|verb 3|How about + -ing.
=|Complete: Why … you go to the doctor?|don't|Why don't you.
=|To accept a suggestion: That's a good …|idea|Good idea.
B|"Let's study together" is a suggestion.|Let's.
S|"You should to rest" is correct.|Should rest.
Which sentence gives a suggestion?|How about studying together?|I studied yesterday.|She is studying.|Did you study?|Saran.
A polite way to refuse a suggestion is …|Thanks, but I don't think so.|No way!|Shut up!|Never!|Sopan.
## BIG|Expressing hopes and wishes
"I hope I pass the exam" expresses something that is …|possible|impossible|in the past|a command|Hope.
"I wish I could fly" expresses something that is …|impossible|very likely|certain|a fact|Wish.
=|Complete: I … you all the best.|wish|Wish you.
=|"Hopefully" means …|semoga|Semoga.
B|"I hope not" means you hope it does not happen.|Hope not.
S|We use "wish" for things that will surely happen.|Hope.
Which sentence is a wish?|I wish I had a pet dragon.|I hope it is sunny.|I play football.|I went home.|Wish.
"I hope so" is used to …|agree with a hope|refuse|apologize|complain|Setuju.
## BIG|Relative pronouns
We use "who" for …|people|things|places|time|Who.
We use "which" for …|things or animals|people only|places|time|Which.
=|The relative pronoun for places is …|where|Where.
=|The relative pronoun for possession is …|whose|Whose.
B|"That" can be used for people or things.|That.
S|"The man which helped me" is correct.|Who.
Complete: The book … I bought is interesting.|which|who|where|whose|Which.
Complete: The girl … sits next to me is smart.|who|which|where|when|Who.
## BIG|Gerunds
A gerund is a verb ending in …|-ing|-ed|-s|-ly|-ing.
Complete: I enjoy … comics.|reading|to read|read|reads|Enjoy + -ing.
=|Complete: … is fun. (swim)|Swimming|Swimming.
=|Complete: She is good at … (draw)|drawing|Drawing.
B|A gerund can be the subject of a sentence.|Subject.
S|"I enjoy to read" is correct.|Enjoy reading.
Complete: Thank you for … (come)|coming|come|came|to come|After for.
Which verb is followed by a gerund?|finish|want|decide|hope|Finish.
## BIG|Writing formal emails
A formal email usually begins with …|Dear Ms. Rina,|Hey Rina!|Yo!|Hi bro,|Dear.
A good closing for a formal email is …|Best regards,|See ya!|Bye bye!|LOL|Formal.
=|The short title of an email is called the …|subject|Subject.
=|"I am … to ask for permission."|writing|Writing.
B|We should check spelling before sending an email.|Check.
S|Emojis and slang are good in formal emails.|Hindari.
The main message of an email is in the …|body|subject|signature|greeting|Body.
Your full name at the end of an email is the …|signature|subject|greeting|body|Signature.
## BIG|Agreeing and disagreeing
"I agree with you" expresses …|agreement|disagreement|apology|gratitude|Setuju.
A polite way to disagree is …|I'm afraid I disagree.|You are wrong!|That's stupid!|No, shut up!|Sopan.
=|Complete: I think so …|too|Too.
=|Complete: I see your …, but uniforms are expensive.|point|Point.
B|Giving reasons makes an opinion stronger.|Alasan.
S|"You are wrong!" is a polite way to disagree.|Kasar.
"That's exactly right" shows …|strong agreement|disagreement|doubt|apology|Kuat.
"I don't think so" shows …|disagreement|agreement|thanks|hope|Tidak setuju.
## BIG|Reported speech
She said, "I am tired." In reported speech: She said that she … tired.|was|is|were|be|Mundur.
He said, "I like pizza." In reported speech: He said that he … pizza.|liked|likes|like|liking|Past.
=|"I will come" becomes she said she … come.|would|Would.
=|"I can swim" becomes he said he … swim.|could|Could.
B|In reported speech, the tense usually moves back.|Mundur.
S|Pronouns never change in reported speech.|Berubah.
"Tomorrow" in reported speech becomes …|the next day|yesterday|today|the day before|Next day.
"Today" in reported speech becomes …|that day|tomorrow|yesterday|now|That day.
## BIG|Modals should and might
"You should drink water" expresses …|advice|possibility|ability|past habit|Should.
"It might rain later" expresses …|possibility|obligation|ability|permission|Might.
=|The modal for strong obligation is …|must|Must.
=|The modal for ability is …|can|Can.
B|After a modal we use the base form of a verb.|Base form.
S|"She might comes" is correct.|Might come.
Which sentence is correct?|You should wear a helmet.|You should wears a helmet.|You should to wear a helmet.|You shoulds wear a helmet.|Pola.
"May I go out?" uses "may" for …|permission|ability|advice|obligation|Izin.
## BIG|Biography text
A biography is written by …|another person|the person himself|a computer only|nobody|Orang lain.
The tense used in a biography is mostly …|simple past tense|simple present tense|future tense|present continuous|Past.
=|The part that introduces the person is the …|orientation|Orientation.
=|The closing part of a biography is the …|reorientation|Reorientation.
B|A biography tells events in order.|Kronologis.
S|A biography is a fictional story about animals.|Nyata.
B.J. Habibie was born in …|Parepare|Bandung|Jakarta|Medan|Parepare.
"He became the third president of Indonesia" belongs to the part …|events|orientation|title|reference|Events.
## BIG|Explanation text
An explanation text explains how or … something happens.|why|who|where only|whom|Why.
The first part of an explanation text is the …|general statement|closing|resolution|coda|General.
=|The word for the last step is …|finally|Finally.
=|"As a …" shows a result.|result|As a result.
B|Explanation texts use the simple present tense.|Present.
S|An explanation text is a personal diary.|Proses.
Which word shows a cause?|because|then|finally|first|Because.
"First, the sun heats the water" is part of the …|sequence of explanation|general statement|closing|title|Sequence.
## BIG|Prepositions of place and time
We use "at" for …|clock times|months|years|days|At.
We use "on" for …|days|years|months|clock times|On.
=|Complete: I was born … July.|in|In.
=|Complete: The cat is … the table. (below)|under|Under.
B|"At night" is correct.|At night.
S|"In 7 o'clock" is correct.|At 7.
Complete: My birthday is … Monday.|on|in|at|for|On.
Complete: The bank is … the school and the market.|between|on|at|in|Between.
## PPK|Pelanggaran HAM dan penegakannya
Perundungan melanggar hak atas …|rasa aman|pekerjaan|pajak|kewarganegaraan|Rasa aman.
Melarang orang beribadah melanggar hak …|beragama|pendidikan|berpendapat|ekonomi|Beragama.
=|Membeda-bedakan orang karena sukunya disebut …|diskriminasi|Diskriminasi.
=|Penegakan HAM melalui pendidikan dan aturan termasuk upaya …|pencegahan|Pencegahan.
B|Menyebar data pribadi orang lain melanggar hak privasi.|Privasi.
S|Perundungan bukan pelanggaran hak.|Melanggar.
Penegakan HAM melalui proses hukum termasuk upaya …|penindakan|pencegahan|sosialisasi|pendidikan|Penindakan.
Mempekerjakan anak usia sekolah melanggar hak …|pendidikan anak|beragama|berpendapat|politik|Pendidikan.
## PPK|Lembaga perlindungan HAM
Lembaga yang menyelidiki pelanggaran HAM adalah …|Komnas HAM|KPU|BPK|DPD|Komnas HAM.
Lembaga yang melindungi hak anak adalah …|KPAI|LPSK|Ombudsman|KPK|KPAI.
=|Lembaga yang melindungi saksi dan korban disingkat …|LPSK|LPSK.
=|Pelanggaran HAM berat diadili di Pengadilan …|HAM|Pengadilan HAM.
B|Komnas Perempuan menangani kekerasan terhadap perempuan.|Perempuan.
S|Hanya polisi yang menangani masalah HAM.|Banyak lembaga.
Lembaga yang mengawasi pelayanan publik adalah …|Ombudsman|KPAI|Komnas HAM|LPSK|Ombudsman.
Laporan kekerasan terhadap anak dapat disampaikan kepada …|KPAI|BMKG|KPU|BPS|KPAI.
## PPK|Supremasi hukum
Indonesia adalah negara hukum menurut Pasal 1 ayat …|3|1|2|4|Ayat 3.
Supremasi hukum berarti hukum menjadi kekuasaan …|tertinggi|terendah|pilihan|sementara|Tertinggi.
=|Asas semua warga diperlakukan sama di depan hukum disebut asas … di depan hukum.|persamaan|Persamaan.
=|Tindakan pemerintah harus berdasarkan aturan disebut asas …|legalitas|Legalitas.
B|Pejabat yang korupsi tetap diadili.|Tidak kebal.
S|Orang berkuasa boleh kebal hukum.|Sama.
Hakim yang tidak diintervensi mencerminkan …|peradilan bebas|supremasi raja|kekuasaan mutlak|diskriminasi|Bebas.
Contoh sikap taat hukum pelajar adalah …|menaati aturan lalu lintas|melanggar rambu|tawuran|mencoret fasilitas|Taat.
## PPK|Peradilan di Indonesia
Perkara pencurian diadili di pengadilan …|negeri|agama|militer|tata usaha negara|Negeri.
Perkara warisan muslim diadili di pengadilan …|agama|negeri|militer|tata usaha negara|Agama.
=|Upaya hukum ke pengadilan tinggi disebut …|banding|Banding.
=|Upaya hukum ke Mahkamah Agung disebut …|kasasi|Kasasi.
B|Perkara anggota TNI diadili di peradilan militer.|Militer.
S|Semua perkara langsung dibawa ke Mahkamah Agung.|Berjenjang.
Sengketa keputusan pejabat diadili di peradilan …|tata usaha negara|agama|militer|umum|PTUN.
Kekuasaan kehakiman dijalankan oleh Mahkamah Agung dan …|Mahkamah Konstitusi|DPR|MPR|Komnas HAM|MK.
## PPK|Pemberantasan korupsi
Memberi uang kepada petugas agar urusan dipermudah disebut …|suap|gratifikasi|nepotisme|penggelapan|Suap.
Lembaga khusus pemberantasan korupsi adalah …|KPK|KPU|KPAI|BPS|KPK.
=|Hadiah yang diterima karena jabatan disebut …|gratifikasi|Gratifikasi.
=|Memakai uang kas untuk kepentingan pribadi disebut …|penggelapan|Penggelapan.
B|Korupsi menghambat pembangunan.|Dampak.
S|Korupsi hanya dilakukan pejabat besar.|Siapa saja.
Mengutamakan keluarga dalam jabatan disebut …|nepotisme|kolusi|suap|pemerasan|Nepotisme.
Memaksa orang lain memberi uang disebut …|pemerasan|gratifikasi|nepotisme|hibah|Pemerasan.
## PPK|Sikap antikorupsi
Jumlah nilai antikorupsi adalah …|sembilan|lima|tujuh|sepuluh|Sembilan.
Tidak mencontek saat ujian mencerminkan nilai …|jujur|sederhana|berani|mandiri|Jujur.
=|Datang tepat waktu mencerminkan nilai …|disiplin|Disiplin.
=|Tidak pamer barang mewah mencerminkan nilai …|sederhana|Sederhana.
B|Bendahara kelas yang melaporkan uang kas bersikap antikorupsi.|Terbuka.
S|Titip absen adalah hal sepele yang boleh dilakukan.|Tidak jujur.
Menolak ajakan curang mencerminkan nilai …|berani|malas|egois|boros|Berani.
Mengerjakan piket kelas mencerminkan nilai …|tanggung jawab|sederhana|adil|berani|Tanggung jawab.
## PPK|Bentuk negara kesatuan
Bentuk negara Indonesia adalah negara …|kesatuan|federal|serikat|kerajaan|Kesatuan.
Bentuk pemerintahan Indonesia adalah …|republik|monarki|federasi|teokrasi|Republik.
=|Bentuk negara kesatuan ditegaskan dalam Pasal 1 ayat …|1|Ayat 1.
=|Pasal yang menyatakan bentuk NKRI tidak dapat diubah adalah Pasal 37 ayat …|5|Ayat 5.
B|Negara kesatuan memiliki satu pemerintahan pusat.|Pusat.
S|Indonesia sekarang berbentuk negara federal.|Kesatuan.
Indonesia pernah menjadi Republik Indonesia Serikat pada tahun …|1949–1950|1945–1946|1959–1965|1998–1999|RIS.
Contoh negara federal adalah …|Amerika Serikat|Indonesia|Jepang|Thailand|Federal.
## PPK|Pembagian wilayah administratif
Provinsi dipimpin oleh …|gubernur|bupati|camat|lurah|Gubernur.
Kecamatan dipimpin oleh …|camat|bupati|lurah|gubernur|Camat.
=|Kabupaten dipimpin oleh …|bupati|Bupati.
=|Kelurahan dipimpin oleh …|lurah|Lurah.
B|Kepala desa dipilih langsung oleh warga.|Dipilih.
S|Kelurahan sama persis dengan desa.|Berbeda.
Kota dipimpin oleh …|wali kota|bupati|camat|lurah|Wali kota.
Lurah menjabat karena …|diangkat|dipilih warga|diwariskan|diundi|Diangkat.
## PPK|Integrasi nasional
Penyatuan berbagai kelompok menjadi satu bangsa disebut …|integrasi nasional|disintegrasi|primordialisme|separatisme|Integrasi.
Faktor pendorong integrasi adalah …|bahasa Indonesia|hoaks SARA|kesenjangan|primordialisme|Pendorong.
=|Sikap mengutamakan kelompok sendiri secara berlebihan disebut …|primordialisme|Primordialisme.
=|Semboyan pemersatu bangsa adalah Bhinneka Tunggal …|Ika|Ika.
B|Hoaks SARA dapat memecah persatuan.|Penghambat.
S|Integrasi berarti menyeragamkan semua budaya.|Menghargai perbedaan.
Kesenjangan ekonomi menjadi faktor … integrasi.|penghambat|pendorong|pengganti|penentu tunggal|Penghambat.
Sejarah perjuangan bersama menumbuhkan rasa …|senasib sepenanggungan|permusuhan|curiga|iri|Senasib.
## PPK|Politik luar negeri bebas aktif
Bebas dalam politik luar negeri berarti …|tidak memihak blok mana pun|tidak peduli dunia|bebas berperang|bebas menjajah|Bebas.
Pencetus politik bebas aktif adalah …|Mohammad Hatta|Soekarno|Soeharto|Habibie|Hatta.
=|Pidato Hatta berjudul Mendayung di Antara Dua …|Karang|Karang.
=|Gerakan yang tidak memihak blok mana pun disebut Gerakan …|Non-Blok;Nonblok|Non-Blok.
B|Pasukan Garuda bertugas dalam misi perdamaian PBB.|Garuda.
S|Bebas aktif berarti Indonesia tidak peduli urusan dunia.|Aktif.
Aktif dalam politik luar negeri berarti ikut serta …|menciptakan perdamaian dunia|menjajah negara lain|memihak blok|menutup diri|Aktif.
Dasar politik bebas aktif terdapat dalam Pembukaan UUD 1945 alinea …|keempat|pertama|kedua|ketiga|Keempat.
## PPK|Diplomasi Indonesia
Pemimpin perwakilan diplomatik adalah …|duta besar|konsul|camat|gubernur|Duta besar.
Konsul bertugas mengurus warga dan …|perdagangan|militer saja|pemilu|pajak daerah|Dagang.
=|Kantor kedutaan besar Indonesia disingkat …|KBRI|KBRI.
=|Konferensi yang menghasilkan pengakuan kedaulatan tahun 1949 adalah Konferensi Meja …|Bundar|KMB.
B|KBRI melindungi WNI di luar negeri.|KBRI.
S|Duta besar hanya bertugas berlibur di luar negeri.|Mewakili.
Kantor konsulat jenderal Indonesia disingkat …|KJRI|KBRI|KPU|KPK|KJRI.
Atase pendidikan mengurus urusan …|pendidikan|militer|perdagangan|pajak|Pendidikan.
## PPK|Pemuda menghadapi globalisasi
Peluang globalisasi bagi pemuda adalah …|akses ilmu pengetahuan|budaya konsumtif|hoaks|lunturnya budaya|Peluang.
Tantangan globalisasi adalah …|hoaks|akses ilmu|pasar dunia|teknologi|Tantangan.
=|Kemampuan menyaring informasi disebut berpikir …|kritis|Kritis.
=|Menciptakan usaha sendiri disebut …|kewirausahaan;wirausaha|Wirausaha.
B|Pemuda perlu tetap berjati diri Indonesia.|Jati diri.
S|Globalisasi hanya membawa dampak buruk.|Ada peluang.
Menguasai bahasa asing membantu pemuda …|berkomunikasi global|melupakan budaya|menyebar hoaks|berperilaku konsumtif|Komunikasi.
Menjual kerajinan daerah secara daring ke luar negeri memanfaatkan …|teknologi digital|budaya konsumtif|hoaks|primordialisme|Digital.
"""

SAS += """
## BIG 1
0|"It has rained since morning." The sentence is in the ....|present perfect tense|simple past tense|future tense|simple present tense|Has rained.
1|"I suggest you rest." The expression is used to ....|give a suggestion|apologize|congratulate|complain|Saran.
2|"I wish you luck" is used to ....|wish someone well|refuse|complain|order|Wish.
3|We use "when" as a relative pronoun for ....|time|people|things|possession|When.
4|"My hobby is cooking." The word cooking functions as a ....|complement|verb|adjective|adverb|Gerund.
5|"I am writing to ask..." is a good ... in a formal email.|opening line|closing|signature|subject|Opening.
## BIG 2
0|"I think so too" expresses ....|agreement|disagreement|apology|surprise|Setuju.
1|"I can swim," he said. In reported speech: He said that he ... swim.|could|can|will|would|Could.
2|"You must wear a seatbelt." The modal must shows ....|obligation|possibility|ability|permission|Must.
3|The early life of a person in a biography belongs to ....|events|orientation only|title|closing|Event.
4|"Then, the vapor forms clouds" belongs to the ....|sequence of explanation|general statement|closing|title|Sequence.
5|Complete: I usually study ... the morning.|in|on|at|for|In.
## PPK 1
0|Membungkam pendapat orang lain melanggar hak ....|berpendapat|beragama|pendidikan|kesehatan|Berpendapat.
1|Lembaga yang menangani kekerasan terhadap perempuan adalah ....|Komnas Perempuan|KPU|BPK|DPD|Komnas Perempuan.
2|Lembaga negara saling mengawasi mencerminkan ciri negara hukum berupa ....|pembagian kekuasaan|kekuasaan mutlak|supremasi raja|diskriminasi|Pembagian.
3|Uji undang-undang terhadap UUD dilakukan oleh ....|Mahkamah Konstitusi|Mahkamah Agung|pengadilan negeri|pengadilan agama|MK.
4|Kerja sama curang antara pihak-pihak disebut ....|kolusi|nepotisme|suap|gratifikasi|Kolusi.
5|Membagi tugas kelompok secara merata mencerminkan nilai antikorupsi ....|adil|sederhana|berani|mandiri|Adil.
## PPK 2
0|Kedaulatan dalam negara kesatuan berada di tangan ....|pemerintah pusat|setiap provinsi|kepala desa|negara lain|Pusat.
1|Desa dipimpin oleh ....|kepala desa|lurah|camat|bupati|Kades.
2|Pancasila merupakan faktor ... integrasi nasional.|pendorong|penghambat|pengganti|perusak|Pendorong.
3|Jakarta Informal Meeting membantu perdamaian di negara ....|Kamboja|Malaysia|Filipina|Jepang|Kamboja.
4|Atase pertahanan mengurus urusan ....|militer|pendidikan|perdagangan|kebudayaan|Militer.
5|Bekerja dalam tim merupakan bekal pemuda berupa ....|kolaborasi|konsumtif|primordial|individualis|Kolaborasi.
"""

TOPICS += """
## SBD
# 1|Desain, Fotografi, dan Musik
@ Desain grafis
min: 15
act: Rancang sampul buku tugas memakai aplikasi desain sederhana atau kertas dan spidol.
mis: memakai terlalu banyak jenis huruf dan warna dalam satu desain
exp: Desain grafis adalah seni menyampaikan pesan melalui gambar, huruf, dan warna. Prinsip desain meliputi kesatuan, keseimbangan, irama, penekanan, dan proporsi. Desain grafis dipakai pada poster, logo, kemasan, dan media sosial. Desain yang baik sederhana, jelas, dan sesuai tujuan.
ex: Logo sekolah dibuat sederhana agar mudah diingat. // Judul poster diberi penekanan warna terang.
pt: Pesan lewat gambar, huruf, warna ; Kesatuan, keseimbangan, penekanan ; Sederhana dan jelas
sum: Desain grafis yang baik menyampaikan pesan dengan cepat.
fig: table Prinsip desain | Arti ;; kesatuan | semua unsur padu ;; keseimbangan | berat visual setara ;; irama | pengulangan teratur ;; penekanan | bagian paling menonjol ;; proporsi | perbandingan ukuran ;; ruang kosong | memberi napas desain ~ Prinsip desain grafis.
@ Tipografi
min: 15
act: Tulis namamu dengan tiga jenis huruf berbeda, lalu bandingkan kesannya.
mis: memakai huruf hias yang sulit dibaca untuk paragraf panjang
exp: Tipografi adalah seni menata huruf agar indah dan mudah dibaca. Jenis huruf antara lain serif yang berkait di ujung, sans serif tanpa kait, script seperti tulisan tangan, dan dekoratif. Hal yang diperhatikan meliputi ukuran, jarak antarhuruf, jarak antarbaris, dan kontras warna.
ex: Koran memakai huruf serif. // Papan petunjuk memakai huruf sans serif agar jelas.
pt: Menata huruf ; Serif, sans serif, script ; Ukuran, jarak, kontras
sum: Tipografi yang tepat membuat tulisan nyaman dibaca.
fig: table Jenis huruf | Ciri ;; serif | berkait di ujung ;; sans serif | tanpa kait ;; script | seperti tulisan tangan ;; dekoratif | penuh hiasan ;; monospace | lebar huruf sama ;; slab serif | kait tebal persegi ~ Jenis huruf.
@ Fotografi dasar
min: 15
act: Ambil tiga foto objek di rumah dengan aturan sepertiga, lalu pilih yang terbaik.
mis: selalu menempatkan objek tepat di tengah tanpa mempertimbangkan komposisi
exp: Fotografi adalah seni menangkap gambar dengan kamera. Hal penting dalam fotografi meliputi pencahayaan, komposisi, dan fokus. Aturan sepertiga membagi bidang foto menjadi sembilan kotak dan menempatkan objek pada titik pertemuan garis. Sudut pengambilan antara lain sejajar mata, dari atas, dan dari bawah.
ex: Foto dari bawah membuat gedung tampak megah. // Cahaya pagi memberi kesan lembut.
pt: Pencahayaan, komposisi, fokus ; Aturan sepertiga ; Sudut pengambilan
sum: Komposisi yang baik membuat foto lebih menarik.
fig: table Sudut pengambilan | Kesan ;; sejajar mata | wajar ;; dari atas | objek tampak kecil ;; dari bawah | objek tampak megah ;; close up | detail jelas ;; long shot | suasana luas ;; dari samping | menunjukkan profil ~ Sudut pengambilan foto.
@ Seni instalasi
min: 15
act: Rancang seni instalasi kecil dari barang bekas di sudut kamar dengan tema lingkungan.
mis: mengira seni instalasi hanya tumpukan barang tanpa makna
exp: Seni instalasi adalah karya seni rupa yang ditata dalam ruang dengan menggabungkan berbagai benda dan media sehingga penonton dapat mengalaminya. Seni instalasi biasanya membawa pesan atau gagasan tertentu, misalnya tentang lingkungan atau sosial. Instalasi dapat memakai cahaya, suara, dan benda sehari-hari.
ex: Instalasi botol plastik bertema sampah laut. // Instalasi cahaya di taman kota.
pt: Ditata dalam ruang ; Gabungan benda dan media ; Membawa pesan
sum: Seni instalasi mengajak penonton mengalami gagasan seniman.
fig: table Unsur instalasi | Contoh ;; benda | botol bekas ;; cahaya | lampu warna ;; suara | rekaman ombak ;; ruang | sudut galeri ;; gerak | kincir angin ;; teks | tulisan pesan ~ Unsur seni instalasi.
@ Kritik karya seni rupa
min: 15
act: Pilih satu lukisan di buku, lalu tulis kritik dengan empat tahap.
mis: langsung menilai bagus atau jelek tanpa mendeskripsikan karya
exp: Kritik seni adalah kegiatan menilai karya seni secara objektif. Tahapannya deskripsi atau menjelaskan apa yang terlihat, analisis formal atau menguraikan unsur dan prinsip seni, interpretasi atau menafsirkan makna, dan evaluasi atau memberi penilaian. Kritik disampaikan dengan sopan dan membangun.
ex: Deskripsi: lukisan menampilkan sawah saat senja. // Evaluasi: warna hangat berhasil membangun suasana tenang.
pt: Menilai karya secara objektif ; Deskripsi, analisis, interpretasi, evaluasi ; Sopan dan membangun
sum: Kritik seni membantu memahami dan menghargai karya.
fig: table Tahap kritik | Kegiatan ;; deskripsi | menjelaskan yang terlihat ;; analisis formal | menguraikan unsur seni ;; interpretasi | menafsirkan makna ;; evaluasi | memberi penilaian ;; saran | masukan membangun ;; sikap | sopan dan objektif ~ Tahap kritik seni.
@ Notasi balok
min: 15
act: Tulis lima nada pertama lagu sederhana di garis paranada.
mis: menukar nilai not penuh dan not setengah
exp: Notasi balok adalah penulisan nada musik pada garis paranada yang terdiri atas lima garis. Kunci G menandai letak nada G. Nilai not menunjukkan panjang nada: not penuh 4 ketuk, not setengah 2 ketuk, not seperempat 1 ketuk, dan not seperdelapan setengah ketuk. Tanda diam menunjukkan jeda.
ex: Not penuh berbentuk bulat kosong tanpa tangkai. // Not seperempat berbentuk bulat penuh bertangkai.
pt: Ditulis di paranada lima garis ; Kunci G ; Not penuh 4 ketuk, seperempat 1 ketuk
sum: Notasi balok memudahkan membaca musik secara tepat.
fig: table Not | Nilai ketuk ;; not penuh | 4 ;; not setengah | 2 ;; not seperempat | 1 ;; not seperdelapan | ½ ;; not seperenambelas | ¼ ;; not setengah bertitik | 3 ~ Nilai not balok.
@ Akor dasar gitar
min: 15
act: Latih akor C, G, dan Am pada gitar atau aplikasi gitar, lalu iringi lagu sederhana.
mis: menekan senar tidak tepat di belakang fret sehingga bunyi sumbang
exp: Akor adalah gabungan tiga nada atau lebih yang dibunyikan bersamaan. Akor mayor berkesan cerah, sedangkan akor minor berkesan sedih. Akor C mayor tersusun atas nada C, E, dan G. Pada gitar, akor dimainkan dengan menekan senar pada fret tertentu sambil memetik atau menggenjreng.
ex: Lagu riang banyak memakai akor mayor. // Akor Am tersusun atas A, C, dan E.
pt: Gabungan tiga nada atau lebih ; Mayor cerah, minor sedih ; C mayor = C, E, G
sum: Akor membuat iringan lagu lebih harmonis.
fig: table Akor | Susunan nada ;; C | C E G ;; G | G B D ;; F | F A C ;; Am | A C E ;; Dm | D F A ;; Em | E G B ~ Susunan nada akor dasar.
@ Lagu populer dan unsurnya
min: 15
act: Dengarkan satu lagu populer Indonesia, lalu tentukan bagian intro, bait, dan reff.
mis: mengira reff adalah bagian awal lagu
exp: Lagu populer memiliki struktur yang umum, yaitu intro, bait atau verse, pre-chorus, reff atau chorus, bridge, dan outro. Reff adalah bagian yang paling mudah diingat dan biasanya diulang. Unsur musik dalam lagu meliputi melodi, irama, harmoni, tempo, dan dinamika.
ex: Intro dimainkan sebelum penyanyi mulai. // Reff diulang beberapa kali.
pt: Intro, bait, reff, bridge, outro ; Reff paling mudah diingat ; Melodi, irama, harmoni, tempo
sum: Struktur lagu membuat musik mudah dinikmati.
fig: table Bagian lagu | Fungsi ;; intro | pembuka musik ;; bait | bercerita ;; pre-chorus | jembatan ke reff ;; reff | bagian utama diulang ;; bridge | variasi menjelang akhir ;; outro | penutup ~ Struktur lagu populer.
# 2|Tari, Teater, dan Kriya
@ Tari kontemporer
min: 15
act: Ciptakan gerak bebas selama satu menit untuk mengekspresikan perasaan senang.
mis: mengira tari kontemporer tidak memiliki konsep
exp: Tari kontemporer adalah tari masa kini yang bebas dalam gerak, musik, dan kostum, tetapi tetap memiliki konsep dan pesan. Tari kontemporer sering memadukan unsur tradisi dengan gaya modern. Koreografer Indonesia yang terkenal antara lain Sardono W. Kusumo dan Eko Supriyanto.
ex: Gerak tari terinspirasi kehidupan nelayan. // Musik pengiring memakai bunyi alam.
pt: Bebas gerak, musik, kostum ; Tetap berkonsep ; Memadukan tradisi dan modern
sum: Tari kontemporer adalah ekspresi seni masa kini.
fig: table Unsur | Tari kontemporer ;; gerak | bebas dan eksploratif ;; musik | beragam termasuk bunyi alam ;; kostum | tidak terikat aturan ;; konsep | pesan seniman ;; ruang | panggung atau ruang publik ;; durasi | sesuai konsep ~ Ciri tari kontemporer.
@ Komposisi tari
min: 15
act: Susun komposisi tari kelompok dengan level tinggi, sedang, dan rendah.
mis: membuat semua penari bergerak dengan level yang sama sepanjang tarian
exp: Komposisi tari adalah penataan unsur tari agar indah. Unsurnya meliputi gerak, ruang, waktu, dan tenaga. Ruang mencakup level tinggi, sedang, dan rendah serta pola lantai. Waktu mencakup tempo dan ritme. Tenaga menentukan kuat lemahnya gerakan. Komposisi yang baik memiliki variasi dan kontras.
ex: Penari depan duduk, penari belakang berdiri (level berbeda). // Gerak cepat lalu lambat (variasi tempo).
pt: Gerak, ruang, waktu, tenaga ; Level tinggi, sedang, rendah ; Variasi dan kontras
sum: Komposisi yang tertata membuat tari kelompok memikat.
fig: table Unsur komposisi | Contoh ;; level tinggi | melompat atau berdiri jinjit ;; level sedang | berdiri biasa ;; level rendah | duduk atau berlutut ;; tempo | cepat lambat ;; tenaga | gerak kuat lembut ;; pola lantai | garis dan lingkaran ~ Unsur komposisi tari.
@ Tata rias karakter teater
min: 15
act: Rias wajah teman menjadi tokoh kakek memakai pensil alis untuk garis keriput.
mis: memakai rias yang sama untuk semua tokoh
exp: Tata rias teater berfungsi memperkuat karakter tokoh dan membantu ekspresi terlihat dari jauh. Rias korektif mempercantik wajah, rias karakter mengubah wajah sesuai tokoh, misalnya tua atau jahat, dan rias fantasi untuk tokoh khayalan. Rias harus menyesuaikan tata cahaya panggung.
ex: Garis keriput untuk tokoh tua. // Rias wajah hijau untuk tokoh peri hutan.
pt: Memperkuat karakter tokoh ; Rias korektif, karakter, fantasi ; Sesuai tata cahaya
sum: Rias yang tepat menghidupkan tokoh.
fig: table Jenis rias | Contoh tokoh ;; rias korektif | putri cantik ;; rias karakter tua | kakek nenek ;; rias karakter jahat | penyihir ;; rias fantasi | peri hutan ;; rias luka | korban kecelakaan ;; rias badut | pelawak ~ Jenis rias teater.
@ Manajemen pementasan
min: 15
act: Buat struktur panitia pentas kelas lengkap dengan tugasnya.
mis: tidak menyusun jadwal latihan dan anggaran sebelum pentas
exp: Manajemen pementasan adalah pengelolaan pertunjukan dari persiapan sampai evaluasi. Tim produksi dipimpin produser yang mengatur dana dan kepanitiaan, sedangkan sutradara mengurus artistik. Tahapannya perencanaan, latihan, gladi resik, pementasan, dan evaluasi. Promosi dan pengelolaan tiket juga penting.
ex: Gladi resik dilakukan sehari sebelum pentas. // Seksi publikasi membuat poster.
pt: Persiapan sampai evaluasi ; Produser dan sutradara ; Latihan, gladi resik, pentas
sum: Manajemen yang baik membuat pentas berjalan lancar.
fig: table Peran | Tugas ;; produser | mengatur dana dan panitia ;; sutradara | mengarahkan pemain ;; stage manager | mengatur jalannya panggung ;; publikasi | promosi pentas ;; bendahara | mengelola keuangan ;; penata artistik | dekorasi dan properti ~ Peran dalam manajemen pementasan.
@ Kriya ikat celup
min: 15
act: Buat kaus ikat celup dengan karet gelang dan pewarna pakaian bersama orang dewasa.
mis: tidak mengikat kain dengan kencang sehingga motif tidak terbentuk
exp: Ikat celup atau jumputan adalah teknik menghias kain dengan mengikat bagian tertentu lalu mencelupkannya ke pewarna. Bagian yang diikat tidak terkena warna sehingga membentuk motif. Teknik ini dikenal di berbagai daerah, misalnya kain jumputan Palembang dan sasirangan Kalimantan Selatan.
ex: Ikatan melingkar menghasilkan motif bulatan. // Sasirangan berasal dari Banjarmasin.
pt: Kain diikat lalu dicelup ; Bagian terikat tidak berwarna ; Jumputan dan sasirangan
sum: Ikat celup menghasilkan motif unik dan indah.
fig: table Kain ikat celup | Daerah ;; jumputan | Palembang ;; sasirangan | Kalimantan Selatan ;; tritik | Jawa Tengah ;; pelangi | Sumatera Selatan ;; jumputan Yogyakarta | Yogyakarta ;; ikat celup modern | berbagai kota ~ Kain ikat celup Nusantara.
@ Kriya kayu
min: 15
act: Amplas dan warnai potongan kayu kecil menjadi gantungan kunci berbentuk sederhana.
mis: memakai alat ukir tajam tanpa pengawasan orang dewasa
exp: Kriya kayu adalah kerajinan berbahan kayu, misalnya ukiran, mebel, topeng, dan mainan. Teknik pengerjaannya antara lain memotong, mengukir, membubut, mengamplas, dan mengecat atau memelitur. Jepara terkenal dengan ukiran kayu, Bali dengan patung kayu, dan Cirebon dengan topeng.
ex: Ukiran Jepara menghiasi lemari. // Topeng Cirebon dibuat dari kayu.
pt: Kerajinan berbahan kayu ; Memotong, mengukir, mengamplas ; Jepara, Bali, Cirebon
sum: Kriya kayu memadukan keterampilan dan seni.
fig: table Teknik | Alat ;; memotong | gergaji ;; mengukir | pahat ukir ;; membubut | mesin bubut ;; menghaluskan | amplas ;; mewarnai | kuas dan pelitur ;; melubangi | bor ~ Teknik dan alat kriya kayu.
@ Kemasan produk kerajinan
min: 15
act: Rancang kemasan untuk kerajinan buatanmu lengkap dengan merek dan informasi produk.
mis: membuat kemasan menarik tetapi tidak melindungi produk
exp: Kemasan berfungsi melindungi produk, memberi informasi, dan menarik pembeli. Kemasan yang baik kuat, sesuai ukuran produk, memuat merek, nama produk, bahan, cara perawatan, dan identitas pembuat. Kemasan ramah lingkungan memakai bahan yang dapat didaur ulang.
ex: Kotak karton melindungi gerabah dari benturan. // Label memuat nama perajin dan alamat.
pt: Melindungi, memberi informasi, menarik ; Memuat merek dan informasi ; Ramah lingkungan
sum: Kemasan yang baik meningkatkan nilai jual kerajinan.
fig: table Fungsi kemasan | Contoh ;; melindungi | busa di dalam kotak ;; memberi informasi | label bahan ;; menarik pembeli | warna cerah ;; identitas | merek dan logo ;; memudahkan dibawa | tas jinjing kertas ;; ramah lingkungan | kertas daur ulang ~ Fungsi kemasan.
@ Seni digital
min: 15
act: Buat gambar sederhana dengan aplikasi gambar di HP atau komputer.
mis: mengira seni digital tidak memerlukan keterampilan menggambar
exp: Seni digital adalah karya seni yang dibuat dengan perangkat digital seperti komputer, tablet, atau HP. Bentuknya antara lain lukisan digital, ilustrasi vektor, animasi, dan desain 3D. Seni digital memakai lapisan atau layer, kuas digital, dan fitur undo. Hak cipta karya digital tetap harus dihormati.
ex: Ilustrasi buku dibuat dengan tablet gambar. // Animasi pendek dibuat dengan aplikasi.
pt: Dibuat dengan perangkat digital ; Lukisan digital, vektor, animasi ; Layer, kuas digital, undo
sum: Seni digital membuka cara baru berkarya.
fig: table Istilah | Arti ;; layer | lapisan gambar ;; vektor | gambar berbasis garis matematis ;; piksel | titik penyusun gambar ;; kuas digital | alat gores virtual ;; undo | membatalkan langkah ;; animasi | gambar bergerak ~ Istilah seni digital.

## PJOK
# 1|Permainan dan Atletik
@ Strategi permainan sepak bola
min: 15
act: Gambar formasi 4-4-2 di kertas dan jelaskan tugas setiap lini.
mis: semua pemain mengejar bola tanpa menjaga posisi
exp: Strategi sepak bola meliputi formasi, penyerangan, dan pertahanan. Formasi menunjukkan susunan pemain bertahan, tengah, dan depan, misalnya 4-4-2 atau 4-3-3. Strategi menyerang antara lain umpan pendek dan serangan sayap. Strategi bertahan antara lain pertahanan zona dan satu lawan satu.
ex: Formasi 4-3-3 memakai tiga penyerang. // Pertahanan zona menjaga daerah tertentu.
pt: Formasi, penyerangan, pertahanan ; Contoh 4-4-2 dan 4-3-3 ; Zona dan satu lawan satu
sum: Strategi yang tepat membuat tim bermain kompak.
fig: table Formasi | Jumlah penyerang ;; 4-4-2 | dua ;; 4-3-3 | tiga ;; 4-5-1 | satu ;; 3-5-2 | dua dengan tiga bek ;; 5-3-2 | dua dengan lima bek ;; 4-2-4 | empat ~ Formasi sepak bola.
@ Strategi permainan bola basket
min: 15
act: Latih pola give and go bersama teman di lapangan.
mis: menahan bola terlalu lama tanpa mengoper
exp: Strategi bola basket meliputi penyerangan dan pertahanan. Strategi menyerang antara lain give and go, fast break atau serangan cepat, dan pick and roll. Strategi bertahan antara lain man to man atau satu lawan satu dan zone defense. Satu tim basket bermain dengan lima pemain di lapangan.
ex: Fast break dilakukan setelah merebut bola. // Zone defense menjaga daerah dekat ring.
pt: Give and go, fast break ; Man to man dan zone defense ; Lima pemain di lapangan
sum: Kerja sama tim menentukan keberhasilan strategi basket.
fig: table Strategi | Keterangan ;; give and go | mengoper lalu lari menerima kembali ;; fast break | serangan cepat ;; pick and roll | menghalangi lalu bergerak ke ring ;; man to man | menjaga satu lawan ;; zone defense | menjaga daerah ;; press | menekan sejak lapangan lawan ~ Strategi bola basket.
@ Strategi permainan bola voli
min: 15
act: Peragakan rotasi pemain voli searah jarum jam bersama lima teman.
mis: tidak berotasi setelah tim mendapatkan hak servis
exp: Strategi bola voli meliputi pola penyerangan dan pertahanan. Pola serangan umum adalah passing, umpan dari tosser, lalu smash. Pertahanan dilakukan dengan block di depan net dan posisi siap menerima di belakang. Pemain berotasi searah jarum jam setiap kali timnya merebut servis dari lawan.
ex: Tosser mengumpan bola untuk smash. // Libero bertugas bertahan di belakang.
pt: Passing, umpan, smash ; Block dan bertahan di belakang ; Rotasi searah jarum jam
sum: Kerja sama dan rotasi membuat tim voli seimbang.
fig: table Posisi | Tugas ;; tosser | mengumpan bola ;; spiker | melakukan smash ;; libero | bertahan di belakang ;; blocker | membendung di net ;; server | melakukan servis ;; universal | serba bisa ~ Posisi pemain bola voli.
@ Lempar cakram
min: 15
act: Peragakan putaran lempar cakram memakai piring plastik di lapangan terbuka.
mis: melepas cakram terlalu cepat sebelum putaran selesai
exp: Lempar cakram adalah nomor atletik melempar cakram sejauh mungkin dari dalam lingkaran. Teknik dasarnya cara memegang cakram dengan ruas jari, sikap awal menyamping, putaran badan, melempar, dan gerak lanjutan. Cakram harus jatuh di sektor lemparan dan pelempar tidak boleh keluar lingkaran depan.
ex: Cakram dipegang dengan ruas jari pertama. // Putaran membantu menambah tenaga lemparan.
pt: Dilempar dari lingkaran ; Pegangan, putaran, lemparan ; Jatuh di sektor
sum: Putaran yang benar membuat lemparan cakram jauh.
fig: table Tahap | Gerakan ;; pegangan | ruas jari pertama ;; sikap awal | menyamping arah lemparan ;; ayunan awal | lengan diayun ke belakang ;; putaran | badan berputar satu setengah kali ;; pelepasan | cakram dilepas lewat telunjuk ;; gerak lanjutan | menjaga keseimbangan ~ Tahap lempar cakram.
@ Lari jarak jauh
min: 15
act: Lari 2 kilometer dengan kecepatan stabil dan catat waktunya.
mis: tidak minum cukup selama berlatih lari jarak jauh
exp: Lari jarak jauh meliputi nomor 5.000 meter, 10.000 meter, dan maraton 42,195 km. Lari ini mengutamakan daya tahan. Start memakai start berdiri. Pelari harus mengatur kecepatan, napas, langkah yang efisien, dan cukup minum. Latihan dilakukan bertahap untuk meningkatkan daya tahan jantung dan paru-paru.
ex: Maraton berjarak 42,195 km. // Pelari minum di pos minum selama maraton.
pt: 5.000 m, 10.000 m, maraton ; Mengutamakan daya tahan ; Atur kecepatan dan cukup minum
sum: Lari jarak jauh melatih ketahanan fisik dan mental.
fig: table Nomor lari | Jarak ;; lari 5K | 5.000 meter ;; lari 10K | 10.000 meter ;; setengah maraton | 21,0975 km ;; maraton | 42,195 km ;; ultramaraton | lebih dari 42,195 km ;; lari lintas alam | medan alam terbuka ~ Nomor lari jarak jauh.
@ Rangkaian senam lantai
min: 15
act: Rangkai guling depan, sikap lilin, dan kayang menjadi satu gerakan berurutan di atas matras.
mis: menyambung gerakan tanpa jeda keseimbangan sehingga jatuh
exp: Rangkaian senam lantai adalah gabungan beberapa gerakan senam yang dilakukan berurutan secara luwes. Contohnya guling depan, guling belakang, sikap lilin, kayang, dan meroda. Rangkaian dinilai dari ketepatan teknik, kelenturan, keseimbangan, dan kelancaran perpindahan antargerak.
ex: Guling depan dilanjutkan berdiri lalu meroda. // Rangkaian diakhiri sikap berdiri tegak.
pt: Gabungan gerakan berurutan ; Guling, kayang, meroda ; Dinilai teknik dan kelancaran
sum: Rangkaian senam melatih koordinasi dan keluwesan.
fig: table Gerakan | Komponen yang dilatih ;; guling depan | keberanian ;; guling belakang | koordinasi ;; sikap lilin | keseimbangan ;; kayang | kelentukan ;; meroda | koordinasi tangan dan kaki ;; berdiri dengan kepala | kekuatan bahu ~ Gerakan dalam rangkaian senam lantai.
@ Renang gaya punggung
min: 15
act: Latih mengapung telentang di kolam dangkal dengan pendampingan orang dewasa.
mis: mengangkat kepala terlalu tinggi sehingga pinggul tenggelam
exp: Renang gaya punggung dilakukan dengan posisi badan telentang di permukaan air. Kaki digerakkan naik turun bergantian seperti gaya bebas. Tangan mengayuh bergantian dari atas kepala ke samping paha. Wajah selalu di atas air sehingga mudah bernapas. Start gaya punggung dilakukan dari dalam kolam.
ex: Telinga berada di permukaan air. // Start dilakukan dengan berpegangan pada dinding kolam.
pt: Badan telentang ; Kaki naik turun bergantian ; Wajah di atas air
sum: Gaya punggung memudahkan bernapas saat berenang.
fig: table Bagian gerakan | Cara ;; posisi badan | telentang lurus ;; kepala | telinga di permukaan air ;; kaki | naik turun bergantian ;; tangan | mengayuh bergantian ;; napas | wajah selalu di atas air ;; start | dari dalam kolam ~ Teknik gaya punggung.
@ Tendangan dan elakan pencak silat
min: 15
act: Latih tendangan depan dan elakan ke samping masing-masing sepuluh kali.
mis: menendang tanpa kuda-kuda yang kokoh
exp: Tendangan dalam pencak silat antara lain tendangan depan, tendangan samping atau T, tendangan sabit, dan tendangan belakang. Elakan adalah gerakan menghindari serangan tanpa menyentuh lawan, misalnya elakan samping, bawah, dan belakang. Semua gerakan diawali kuda-kuda yang kokoh dan dilakukan dengan sikap sportif.
ex: Tendangan sabit berlintasan melengkung. // Elakan bawah dengan merendahkan badan.
pt: Tendangan depan, samping, sabit ; Elakan menghindari serangan ; Kuda-kuda kokoh
sum: Tendangan dan elakan melatih kecepatan dan ketepatan.
fig: table Teknik | Ciri ;; tendangan depan | lurus ke depan ;; tendangan samping | menyamping seperti huruf T ;; tendangan sabit | melengkung dari samping ;; tendangan belakang | membelakangi lawan ;; elakan bawah | merendahkan badan ;; elakan samping | bergeser ke samping ~ Teknik tendangan dan elakan.
# 2|Kebugaran dan Kesehatan
@ Senam irama dengan alat
min: 15
act: Rangkai gerak senam irama memakai pita dari kertas krep dengan iringan musik.
mis: memainkan alat tanpa mengikuti irama musik
exp: Senam irama dapat dilakukan dengan alat seperti pita, bola, simpai, tali, dan gada. Gerakan alat harus padu dengan gerak tubuh dan irama musik. Contoh gerak pita adalah ayunan, putaran, spiral, dan ular-ularan. Senam irama dengan alat melatih koordinasi dan keluwesan.
ex: Pita digerakkan membentuk spiral. // Bola dilambungkan lalu ditangkap sesuai hitungan.
pt: Pita, bola, simpai, tali, gada ; Padu dengan gerak dan musik ; Melatih koordinasi
sum: Alat membuat senam irama lebih indah.
fig: table Alat | Contoh gerakan ;; pita | spiral dan ular-ularan ;; bola | melambung dan menggelinding ;; simpai | memutar di pinggang ;; tali | melompat ;; gada | ayunan berpasangan ;; selendang | mengayun lembut ~ Alat senam irama.
@ Tes kebugaran jasmani
min: 15
act: Lakukan tes lari 40 meter, gantung siku tekuk, dan baring duduk, lalu catat hasilnya.
mis: melakukan tes kebugaran tanpa pemanasan
exp: Tes Kebugaran Jasmani Indonesia atau TKJI untuk usia 13 sampai 15 tahun meliputi lari 50 meter, gantung siku tekuk atau angkat tubuh, baring duduk, loncat tegak, dan lari jarak menengah. Setiap tes mengukur komponen kebugaran tertentu. Hasil tes dipakai untuk menyusun program latihan.
ex: Lari 50 meter mengukur kecepatan. // Loncat tegak mengukur daya ledak otot tungkai.
pt: TKJI lima tes ; Mengukur komponen kebugaran ; Hasil untuk program latihan
sum: Tes kebugaran menunjukkan kondisi fisik kita.
fig: table Tes | Komponen yang diukur ;; lari 50 meter | kecepatan ;; gantung siku tekuk | kekuatan lengan ;; baring duduk | kekuatan otot perut ;; loncat tegak | daya ledak tungkai ;; lari 1.000 meter | daya tahan jantung ;; duduk raih | kelentukan ~ Tes kebugaran dan komponennya.
@ Indeks massa tubuh
min: 15
act: Hitung indeks massa tubuh anggota keluarga dewasa dengan rumus berat dibagi tinggi kuadrat.
mis: menilai berat badan ideal hanya dari angka timbangan
exp: Indeks massa tubuh atau IMT adalah ukuran untuk memperkirakan proporsi berat badan terhadap tinggi badan. Rumusnya berat badan dalam kilogram dibagi kuadrat tinggi badan dalam meter. Untuk remaja, IMT dibandingkan dengan grafik pertumbuhan sesuai usia dan jenis kelamin. IMT hanya perkiraan dan perlu ditafsirkan tenaga kesehatan.
ex: Berat 50 kg, tinggi 1,6 m: IMT = 50 : 2,56 ≈ 19,5. // Remaja memakai grafik IMT sesuai umur.
pt: Berat dibagi tinggi kuadrat ; Remaja memakai grafik sesuai usia ; Hanya perkiraan
sum: IMT membantu memantau pertumbuhan secara sederhana.
fig: table Berat dan tinggi | IMT ;; 50 kg dan 1,6 m | 19,5 ;; 45 kg dan 1,5 m | 20,0 ;; 60 kg dan 1,7 m | 20,8 ;; 40 kg dan 1,5 m | 17,8 ;; 64 kg dan 1,6 m | 25,0 ;; 55 kg dan 1,65 m | 20,2 ~ Contoh perhitungan IMT.
@ Gizi untuk aktivitas fisik
min: 15
act: Susun menu sarapan bergizi seimbang sebelum hari olahraga.
mis: berolahraga berat dalam keadaan perut kosong
exp: Aktivitas fisik membutuhkan energi dari makanan bergizi seimbang. Karbohidrat menjadi sumber energi utama, protein membangun dan memperbaiki otot, lemak cadangan energi, serta vitamin dan mineral mengatur kerja tubuh. Air sangat penting untuk mengganti cairan yang hilang lewat keringat. Makan sebaiknya 1 sampai 2 jam sebelum olahraga.
ex: Nasi dan roti sumber karbohidrat. // Minum air sebelum, selama, dan sesudah olahraga.
pt: Karbohidrat energi utama ; Protein membangun otot ; Air mengganti keringat
sum: Gizi seimbang mendukung performa olahraga.
fig: table Zat gizi | Sumber makanan ;; karbohidrat | nasi dan ubi ;; protein | telur dan tempe ;; lemak | alpukat dan kacang ;; vitamin | buah dan sayur ;; mineral | susu dan ikan ;; air | air putih ~ Zat gizi dan sumbernya.
@ Pertolongan pertama luka
min: 15
act: Praktikkan cara membersihkan dan membalut luka pada boneka memakai kotak P3K.
mis: menekan luka dengan tangan kotor
exp: Luka adalah rusaknya jaringan kulit. Pertolongan pertama luka ringan adalah mencuci tangan, membersihkan luka dengan air mengalir, mengoleskan antiseptik, dan menutup dengan plester atau kasa steril. Perdarahan dihentikan dengan menekan luka memakai kasa bersih dan meninggikan bagian yang luka. Luka dalam atau perdarahan hebat perlu segera ke tenaga medis.
ex: Luka lecet dibersihkan dengan air mengalir. // Mimisan ditangani dengan duduk menunduk dan menekan hidung.
pt: Cuci tangan dan bersihkan luka ; Antiseptik dan tutup steril ; Tekan untuk hentikan perdarahan
sum: Pertolongan pertama yang benar mencegah infeksi.
fig: table Isi kotak P3K | Kegunaan ;; kasa steril | menutup luka ;; plester | merekatkan penutup luka ;; antiseptik | membunuh kuman ;; perban gulung | membalut ;; gunting | memotong perban ;; sarung tangan | melindungi penolong ~ Isi kotak P3K.
@ Mengelola stres
min: 15
act: Catat tiga hal yang membuatmu tertekan dan satu cara sehat untuk menghadapi masing-masing.
mis: memendam masalah sendiri tanpa bercerita kepada orang yang dipercaya
exp: Stres adalah reaksi tubuh dan pikiran terhadap tekanan, misalnya ujian atau masalah pertemanan. Stres ringan dapat memotivasi, tetapi stres berlebihan mengganggu kesehatan. Cara mengelola stres antara lain berolahraga, tidur cukup, mengatur waktu, latihan napas dalam, melakukan hobi, dan bercerita kepada orang tua, guru, atau konselor.
ex: Napas dalam membantu tenang sebelum presentasi. // Membuat jadwal belajar mengurangi panik menjelang ujian.
pt: Reaksi terhadap tekanan ; Ringan memotivasi, berlebihan mengganggu ; Olahraga, tidur, bercerita
sum: Mengelola stres menjaga kesehatan fisik dan mental.
fig: table Cara | Manfaat ;; olahraga | melepaskan ketegangan ;; tidur cukup | memulihkan tenaga ;; napas dalam | menenangkan diri ;; jadwal belajar | mengurangi panik ;; bercerita kepada orang dewasa | mendapat dukungan ;; hobi | menyegarkan pikiran ~ Cara mengelola stres.
@ Kegiatan alam terbuka
min: 15
act: Rencanakan hiking singkat bersama keluarga lengkap dengan daftar perlengkapannya.
mis: berkemah tanpa memberi tahu orang dewasa dan tanpa perlengkapan keselamatan
exp: Kegiatan alam terbuka antara lain hiking, berkemah, dan menjelajah. Kegiatan ini melatih kebugaran, kemandirian, dan kerja sama. Persiapan meliputi perencanaan rute, perlengkapan seperti tas, air, makanan, jas hujan, dan P3K, serta izin dari orang tua. Prinsip penting adalah keselamatan dan tidak merusak alam.
ex: Membawa kembali sampah saat turun gunung. // Memberi tahu rute kepada keluarga.
pt: Hiking, berkemah, menjelajah ; Rencana rute dan perlengkapan ; Keselamatan dan jaga alam
sum: Kegiatan alam terbuka menyenangkan bila aman dan bertanggung jawab.
fig: table Perlengkapan | Fungsi ;; tas punggung | membawa barang ;; air minum | mencegah dehidrasi ;; jas hujan | melindungi dari hujan ;; senter | penerangan malam ;; kotak P3K | pertolongan pertama ;; kantong sampah | membawa pulang sampah ~ Perlengkapan kegiatan alam.
@ Sportivitas
min: 15
act: Ingat satu pertandingan yang kamu tonton, lalu tulis contoh sikap sportif dan tidak sportif.
mis: memprotes wasit dengan kasar ketika kalah
exp: Sportivitas atau fair play adalah sikap jujur dan menghormati aturan, wasit, lawan, dan teman dalam olahraga. Contohnya bersalaman sebelum dan sesudah bertanding, menerima kekalahan dengan lapang dada, tidak curang, dan menolong lawan yang cedera. Sikap sportif juga berguna dalam kehidupan sehari-hari.
ex: Pemain menendang bola keluar agar lawan yang cedera ditolong. // Tim yang kalah memberi selamat kepada pemenang.
pt: Jujur dan menghormati aturan ; Menerima kekalahan ; Tidak curang
sum: Sportivitas lebih penting daripada kemenangan.
fig: table Perilaku | Sportif atau tidak ;; bersalaman dengan lawan | sportif ;; memprotes wasit dengan kasar | tidak sportif ;; menolong lawan cedera | sportif dan peduli ;; pura-pura jatuh | tidak sportif dan curang ;; menerima kekalahan | sportif lapang dada ;; mengejek lawan | tidak sportif dan kasar ~ Perilaku dalam olahraga.
"""

BANK += """
## SBD|Desain grafis
Desain grafis menyampaikan pesan melalui gambar, huruf, dan …|warna|bau|rasa|suara saja|Warna.
Prinsip desain yang menonjolkan bagian tertentu disebut …|penekanan|kesatuan|irama|proporsi|Penekanan.
=|Prinsip desain berupa pengulangan teratur disebut …|irama|Irama.
=|Prinsip desain berupa perbandingan ukuran disebut …|proporsi|Proporsi.
B|Logo sebaiknya sederhana agar mudah diingat.|Sederhana.
S|Desain yang baik memakai sebanyak mungkin jenis huruf.|Sederhana.
Prinsip desain ketika semua unsur tampak padu disebut …|kesatuan|kontras|irama|ruang|Kesatuan.
Ruang kosong dalam desain berfungsi …|memberi napas desain|menghabiskan kertas|membuat bingung|menyembunyikan pesan|Ruang.
## SBD|Tipografi
Seni menata huruf disebut …|tipografi|kaligrafi|fotografi|koreografi|Tipografi.
Huruf yang berkait di ujungnya disebut …|serif|sans serif|script|monospace|Serif.
=|Huruf tanpa kait disebut …|sans serif|Sans serif.
=|Huruf yang menyerupai tulisan tangan disebut …|script|Script.
B|Papan petunjuk sebaiknya memakai huruf yang mudah dibaca.|Jelas.
S|Huruf hias paling cocok untuk paragraf panjang.|Sulit dibaca.
Huruf dengan lebar setiap huruf sama disebut …|monospace|serif|script|dekoratif|Monospace.
Koran umumnya memakai huruf jenis …|serif|dekoratif|graffiti|script|Serif.
## SBD|Fotografi dasar
Aturan yang membagi bidang foto menjadi sembilan kotak disebut aturan …|sepertiga|setengah|seperempat|sepersepuluh|Rule of thirds.
Foto dari bawah membuat objek tampak …|megah|kecil|kabur|gelap|Megah.
=|Pengambilan gambar dekat untuk detail disebut …|close up|Close up.
=|Pengambilan gambar jauh untuk suasana luas disebut long …|shot|Long shot.
B|Pencahayaan penting dalam fotografi.|Cahaya.
S|Objek foto harus selalu tepat di tengah.|Komposisi.
Foto dari atas membuat objek tampak …|kecil|megah|tinggi|besar sekali|Kecil.
Cahaya pagi memberi kesan …|lembut|keras|seram|panas terik|Lembut.
## SBD|Seni instalasi
Seni instalasi adalah karya seni yang ditata dalam …|ruang|buku|kanvas kecil saja|lagu|Ruang.
Seni instalasi biasanya membawa …|pesan atau gagasan|harga murah|rumus matematika|resep|Pesan.
=|Instalasi botol plastik bertema sampah laut membawa pesan tentang …|lingkungan|Lingkungan.
=|Lampu warna dalam instalasi termasuk unsur …|cahaya|Cahaya.
B|Seni instalasi dapat memakai suara.|Suara.
S|Seni instalasi hanya tumpukan barang tanpa makna.|Bermakna.
Penonton seni instalasi dapat …|mengalami karya|tidak boleh melihat|hanya membaca|wajib membeli|Mengalami.
Rekaman suara ombak dalam instalasi termasuk unsur …|suara|cahaya|gerak|teks|Suara.
## SBD|Kritik karya seni rupa
Tahap kritik yang menjelaskan apa yang terlihat adalah …|deskripsi|evaluasi|interpretasi|analisis|Deskripsi.
Tahap kritik yang menafsirkan makna karya adalah …|interpretasi|deskripsi|evaluasi|analisis formal|Interpretasi.
=|Tahap kritik yang memberi penilaian disebut …|evaluasi|Evaluasi.
=|Tahap kritik yang menguraikan unsur seni disebut analisis …|formal|Analisis formal.
B|Kritik seni disampaikan dengan sopan.|Sopan.
S|Kritik seni langsung menilai jelek tanpa menjelaskan karya.|Deskripsi dulu.
Kritik yang baik bersifat …|objektif dan membangun|menghina|asal-asalan|memihak tanpa alasan|Objektif.
Kalimat "lukisan menampilkan sawah saat senja" termasuk tahap …|deskripsi|evaluasi|interpretasi|saran|Deskripsi.
## SBD|Notasi balok
Paranada terdiri atas … garis.|lima|empat|enam|tiga|Lima.
Not penuh bernilai … ketuk.|4|2|1|½|Empat.
=|Not setengah bernilai … ketuk.|2|Dua.
=|Not seperempat bernilai … ketuk.|1|Satu.
B|Kunci G menandai letak nada G.|Kunci G.
S|Not seperdelapan bernilai dua ketuk.|Setengah ketuk.
Not setengah bertitik bernilai …|3 ketuk|2 ketuk|4 ketuk|1 ketuk|2 + 1.
Tanda yang menunjukkan jeda dalam musik disebut tanda …|diam|kunci|birama|titik|Diam.
## SBD|Akor dasar gitar
Akor adalah gabungan tiga nada atau lebih yang dibunyikan …|bersamaan|bergantian jauh|satu per satu|tanpa suara|Bersamaan.
Akor C mayor tersusun atas nada …|C E G|C D E|A C E|G B D|Trinada.
=|Akor mayor berkesan …|cerah;riang|Cerah.
=|Akor minor berkesan …|sedih|Sedih.
B|Akor Am tersusun atas nada A, C, dan E.|Am.
S|Akor minor selalu berkesan riang.|Sedih.
Akor G tersusun atas nada …|G B D|G A B|C E G|D F A|G mayor.
Akor Dm tersusun atas nada …|D F A|D E F|C E G|E G B|Dm.
## SBD|Lagu populer dan unsurnya
Bagian lagu yang paling mudah diingat dan diulang adalah …|reff|intro|bait|outro|Reff.
Bagian pembuka musik sebelum penyanyi mulai adalah …|intro|bridge|reff|outro|Intro.
=|Bagian penutup lagu disebut …|outro|Outro.
=|Bagian lagu yang bercerita disebut …|bait|Bait.
B|Bridge memberi variasi menjelang akhir lagu.|Bridge.
S|Reff selalu menjadi bagian paling awal lagu.|Intro.
Bagian jembatan menuju reff disebut …|pre-chorus|outro|intro|coda|Pre-chorus.
Unsur musik yang menunjukkan cepat lambat lagu adalah …|tempo|harmoni|melodi|dinamika|Tempo.
## SBD|Tari kontemporer
Tari kontemporer adalah tari …|masa kini|kerajaan kuno|keraton saja|purba|Masa kini.
Tari kontemporer bebas, tetapi tetap memiliki …|konsep|aturan baku keraton|kostum wajib|musik gamelan saja|Konsep.
=|Koreografer kontemporer Indonesia Sardono W. …|Kusumo|Kusumo.
=|Tari kontemporer sering memadukan tradisi dengan gaya …|modern|Modern.
B|Musik tari kontemporer dapat memakai bunyi alam.|Beragam.
S|Tari kontemporer tidak memiliki konsep apa pun.|Berkonsep.
Kostum tari kontemporer bersifat …|tidak terikat aturan|harus seragam keraton|wajib hitam|selalu mewah|Bebas.
Tari kontemporer dapat dipentaskan di …|panggung atau ruang publik|museum saja|rumah ibadah saja|tidak di mana pun|Ruang.
## SBD|Komposisi tari
Unsur utama komposisi tari adalah gerak, ruang, waktu, dan …|tenaga|harga|kostum saja|penonton|Tenaga.
Penari yang duduk atau berlutut menggunakan level …|rendah|tinggi|sedang|melayang|Rendah.
=|Penari yang melompat menggunakan level …|tinggi|Tinggi.
=|Cepat lambatnya gerak tari disebut …|tempo|Tempo.
B|Komposisi yang baik memiliki variasi.|Variasi.
S|Semua penari sebaiknya selalu memakai level yang sama.|Variasi.
Kuat lembutnya gerak tari ditentukan oleh …|tenaga|tempo|pola lantai|level|Tenaga.
Berdiri biasa termasuk level …|sedang|rendah|tinggi|melayang|Sedang.
## SBD|Tata rias karakter teater
Tata rias teater berfungsi memperkuat …|karakter tokoh|harga tiket|ukuran panggung|suara musik|Karakter.
Rias untuk tokoh tua termasuk rias …|karakter|korektif|fantasi|badut|Karakter.
=|Rias untuk tokoh khayalan seperti peri disebut rias …|fantasi|Fantasi.
=|Rias untuk mempercantik wajah disebut rias …|korektif|Korektif.
B|Rias teater perlu menyesuaikan tata cahaya.|Cahaya.
S|Semua tokoh teater memakai rias yang sama.|Sesuai tokoh.
Garis keriput dibuat untuk tokoh …|kakek|putri muda|bayi|peri|Tua.
Rias wajah penyihir termasuk rias karakter …|jahat|korektif|cantik|bayi|Jahat.
## SBD|Manajemen pementasan
Orang yang mengatur dana dan kepanitiaan pentas adalah …|produser|aktor|penonton|penata rias|Produser.
Latihan terakhir sebelum pentas disebut …|gladi resik|evaluasi|audisi|promosi|Gladi resik.
=|Orang yang mengarahkan pemain disebut …|sutradara|Sutradara.
=|Seksi yang membuat poster pentas adalah seksi …|publikasi|Publikasi.
B|Evaluasi dilakukan setelah pementasan.|Evaluasi.
S|Jadwal latihan dan anggaran tidak perlu disusun.|Perlu.
Orang yang mengatur jalannya panggung saat pentas adalah …|stage manager|bendahara|penonton|kritikus|Stage manager.
Bendahara pentas bertugas mengelola …|keuangan|dekorasi|kostum|lampu|Keuangan.
## SBD|Kriya ikat celup
Teknik menghias kain dengan diikat lalu dicelup disebut …|ikat celup|batik tulis|sulam|tenun|Ikat celup.
Bagian kain yang diikat menjadi …|tidak berwarna|lebih gelap|berlubang|basah terus|Tidak berwarna.
=|Kain ikat celup dari Kalimantan Selatan disebut …|sasirangan|Sasirangan.
=|Nama lain ikat celup adalah …|jumputan|Jumputan.
B|Ikatan melingkar menghasilkan motif bulatan.|Bulatan.
S|Ikatan longgar menghasilkan motif paling tajam.|Kencang.
Kain jumputan terkenal berasal dari …|Palembang|Jepara|Toraja|Bali|Palembang.
Alat sederhana untuk mengikat kain ikat celup adalah …|karet gelang|canting|lilin malam|jarum sulam|Karet.
## SBD|Kriya kayu
Daerah yang terkenal dengan ukiran kayu adalah …|Jepara|Kasongan|Pekalongan|Garut|Jepara.
Alat untuk menghaluskan kayu adalah …|amplas|gergaji|bor|pahat|Amplas.
=|Alat untuk memotong kayu adalah …|gergaji|Gergaji.
=|Topeng kayu terkenal dari daerah …|Cirebon|Cirebon.
B|Pelitur dipakai untuk mengkilapkan kayu.|Pelitur.
S|Alat ukir tajam aman dipakai anak tanpa pengawasan.|Pengawasan.
Teknik membuat bentuk silinder pada kayu dengan mesin disebut …|membubut|mengukir|mengamplas|mengecat|Bubut.
Alat untuk melubangi kayu adalah …|bor|amplas|kuas|pelitur|Bor.
## SBD|Kemasan produk kerajinan
Fungsi utama kemasan adalah …|melindungi produk|membuat produk rusak|menyembunyikan merek|menambah berat|Melindungi.
Label kemasan memuat …|merek dan informasi produk|resep rahasia|nomor rekening pribadi|gosip|Label.
=|Kemasan dari kertas daur ulang bersifat ramah …|lingkungan|Lingkungan.
=|Busa di dalam kotak berfungsi … produk.|melindungi|Melindungi.
B|Kemasan yang baik sesuai ukuran produk.|Sesuai.
S|Kemasan cukup menarik walaupun tidak melindungi produk.|Melindungi.
Warna cerah pada kemasan berfungsi …|menarik pembeli|membuat produk berat|menyembunyikan isi|mengurangi informasi|Menarik.
Tas jinjing kertas memudahkan produk …|dibawa|rusak|hilang|basah|Dibawa.
## SBD|Seni digital
Seni digital dibuat dengan perangkat …|digital|kayu|tanah liat|logam cor|Digital.
Lapisan gambar dalam aplikasi digital disebut …|layer|piksel|undo|vektor|Layer.
=|Fitur untuk membatalkan langkah disebut …|undo|Undo.
=|Gambar bergerak disebut …|animasi|Animasi.
B|Hak cipta karya digital harus dihormati.|Hak cipta.
S|Seni digital tidak memerlukan keterampilan menggambar.|Perlu.
Gambar berbasis garis matematis disebut gambar …|vektor|piksel|layer|raster|Vektor.
Alat gores virtual dalam aplikasi gambar disebut kuas …|digital|kayu|cat minyak|ijuk|Digital.
## PJOK|Strategi permainan sepak bola
Formasi 4-3-3 memakai … penyerang.|tiga|dua|empat|satu|Tiga.
Pertahanan yang menjaga daerah tertentu disebut pertahanan …|zona|satu lawan satu|total|ganda|Zona.
=|Formasi 4-4-2 memakai … penyerang.|dua;2|Dua.
=|Pertahanan menjaga satu pemain lawan disebut pertahanan satu lawan …|satu|Satu.
B|Formasi menunjukkan susunan pemain.|Formasi.
S|Semua pemain sebaiknya mengejar bola tanpa menjaga posisi.|Posisi.
Formasi 4-5-1 memakai … penyerang.|satu|dua|tiga|lima|Satu.
Serangan yang memanfaatkan sisi lapangan disebut serangan …|sayap|tengah|bertahan|mundur|Sayap.
## PJOK|Strategi permainan bola basket
Serangan cepat setelah merebut bola disebut …|fast break|zone defense|man to man|pivot|Fast break.
Pertahanan menjaga satu lawan disebut …|man to man|zone defense|fast break|give and go|Man to man.
=|Pertahanan menjaga daerah disebut … defense.|zone|Zone.
=|Jumlah pemain basket di lapangan untuk satu tim adalah …|5;lima|Lima.
B|Give and go adalah mengoper lalu lari menerima kembali.|Give and go.
S|Menahan bola terlalu lama adalah strategi yang baik.|Oper.
Strategi menekan lawan sejak lapangan lawan disebut …|press|fast break|pick and roll|zone|Press.
Menghalangi lawan lalu bergerak ke ring disebut …|pick and roll|fast break|press|man to man|Pick and roll.
## PJOK|Strategi permainan bola voli
Pemain yang mengumpan bola untuk smash disebut …|tosser|libero|server|blocker|Tosser.
Pemain bertahan khusus di belakang disebut …|libero|tosser|spiker|server|Libero.
=|Rotasi pemain voli dilakukan searah jarum …|jam|Jam.
=|Pemain yang melakukan smash disebut …|spiker|Spiker.
B|Block dilakukan di depan net.|Block.
S|Tim tidak perlu berotasi setelah merebut servis.|Berotasi.
Pola serangan voli yang umum adalah passing, umpan, lalu …|smash|servis|block|rotasi|Smash.
Pemain yang membendung serangan di net disebut …|blocker|libero|tosser|server|Blocker.
## PJOK|Lempar cakram
Cakram dilempar dari dalam …|lingkaran|bak pasir|garis lurus|kolam|Lingkaran.
Cakram dipegang dengan ruas jari …|pertama|kedua|ketiga|telapak|Pertama.
=|Cakram dilepas melalui jari …|telunjuk|Telunjuk.
=|Cakram harus jatuh di … lemparan.|sektor|Sektor.
B|Putaran badan menambah tenaga lemparan.|Putaran.
S|Cakram sebaiknya dilepas sebelum putaran selesai.|Setelah putaran.
Sikap awal lempar cakram adalah …|menyamping arah lemparan|menghadap depan|jongkok|tiduran|Menyamping.
Gerak lanjutan setelah melempar cakram bertujuan menjaga …|keseimbangan|kecepatan lari|tinggi lompatan|napas|Keseimbangan.
## PJOK|Lari jarak jauh
Jarak lari maraton adalah …|42,195 km|21 km|10 km|5 km|Maraton.
Lari jarak jauh mengutamakan …|daya tahan|kekuatan lengan|kelentukan|kecepatan reaksi|Daya tahan.
=|Start lari jarak jauh adalah start …|berdiri|Berdiri.
=|Lari 10.000 meter disebut juga lari … K.|10|10K.
B|Pelari jarak jauh perlu cukup minum.|Cairan.
S|Pelari jarak jauh tidak perlu mengatur kecepatan.|Atur.
Jarak setengah maraton sekitar …|21,0975 km|42,195 km|10 km|5 km|Setengah.
Lari di medan alam terbuka disebut lari …|lintas alam|estafet|gawang|sprint|Lintas alam.
## PJOK|Rangkaian senam lantai
Rangkaian senam lantai adalah gabungan gerakan yang dilakukan …|berurutan|terpisah jauh|tanpa matras|sambil berlari|Berurutan.
Sikap lilin melatih …|keseimbangan|kecepatan|daya tahan|kekuatan kaki|Keseimbangan.
=|Kayang melatih …|kelentukan|Kelentukan.
=|Meroda melatih koordinasi tangan dan …|kaki|Kaki.
B|Rangkaian senam dinilai dari kelancaran perpindahan gerak.|Kelancaran.
S|Rangkaian senam dilakukan tanpa memperhatikan keseimbangan.|Keseimbangan.
Berdiri dengan kepala melatih kekuatan …|bahu|jari kaki|telinga|mata|Bahu.
Rangkaian senam biasanya diakhiri sikap …|berdiri tegak|berbaring|duduk lesu|jongkok|Berdiri.
## PJOK|Renang gaya punggung
Posisi badan pada gaya punggung adalah …|telentang|telungkup|miring|tegak|Telentang.
Pada gaya punggung, wajah selalu …|di atas air|di dalam air|menghadap dasar|tertutup|Atas.
=|Start gaya punggung dilakukan dari dalam …|kolam|Kolam.
=|Gerakan kaki gaya punggung adalah naik turun …|bergantian|Bergantian.
B|Telinga berada di permukaan air saat gaya punggung.|Telinga.
S|Mengangkat kepala tinggi membuat gaya punggung lebih baik.|Pinggul tenggelam.
Tangan gaya punggung mengayuh secara …|bergantian|bersamaan|diam|di bawah dada|Bergantian.
Keuntungan gaya punggung adalah mudah …|bernapas|tenggelam|melihat dasar|menyelam|Napas.
## PJOK|Tendangan dan elakan pencak silat
Tendangan yang lurus ke depan disebut tendangan …|depan|sabit|samping|belakang|Depan.
Tendangan dengan lintasan melengkung disebut tendangan …|sabit|depan|lurus|T|Sabit.
=|Gerakan menghindari serangan tanpa menyentuh lawan disebut …|elakan|Elakan.
=|Tendangan samping disebut juga tendangan …|T|T.
B|Elakan bawah dilakukan dengan merendahkan badan.|Bawah.
S|Tendangan sebaiknya dilakukan tanpa kuda-kuda.|Kuda-kuda.
Tendangan yang dilakukan dengan membelakangi lawan adalah tendangan …|belakang|depan|sabit|samping|Belakang.
Semua gerakan silat diawali dengan …|kuda-kuda kokoh|berlari|melompat tinggi|berbaring|Kuda-kuda.
## PJOK|Senam irama dengan alat
Alat senam irama berbentuk lingkaran adalah …|simpai|pita|tali|gada|Simpai.
Gerakan pita membentuk lingkaran berputar disebut …|spiral|lompat|guling|kayang|Spiral.
=|Alat senam irama untuk melompat adalah …|tali|Tali.
=|Gerakan alat harus padu dengan irama …|musik|Musik.
B|Senam irama dengan alat melatih koordinasi.|Koordinasi.
S|Alat senam irama dimainkan tanpa mengikuti irama.|Irama.
Bola dalam senam irama dapat dilambungkan dan …|digelindingkan|ditendang keras|dipukul|dilempar ke penonton|Gelinding.
Simpai dapat diputar di …|pinggang|kepala orang lain|lantai saja|udara tanpa tangan|Pinggang.
## PJOK|Tes kebugaran jasmani
Singkatan Tes Kebugaran Jasmani Indonesia adalah …|TKJI|IMT|PJOK|P3K|TKJI.
Lari 50 meter mengukur …|kecepatan|kelentukan|daya tahan|kekuatan perut|Kecepatan.
=|Baring duduk mengukur kekuatan otot …|perut|Perut.
=|Loncat tegak mengukur daya ledak otot …|tungkai|Tungkai.
B|Hasil tes kebugaran dipakai untuk menyusun program latihan.|Program.
S|Tes kebugaran sebaiknya dilakukan tanpa pemanasan.|Pemanasan.
Gantung siku tekuk mengukur kekuatan …|lengan|perut|tungkai|leher|Lengan.
Duduk raih mengukur …|kelentukan|kecepatan|daya tahan|kekuatan lengan|Kelentukan.
## PJOK|Indeks massa tubuh
Singkatan indeks massa tubuh adalah …|IMT|TKJI|BMR|APBN|IMT.
Rumus IMT adalah berat badan dibagi … tinggi badan.|kuadrat|setengah|dua kali|akar|Kuadrat.
=|Berat badan dalam rumus IMT memakai satuan …|kilogram;kg|Kilogram.
=|Tinggi badan dalam rumus IMT memakai satuan …|meter;m|Meter.
B|Remaja membandingkan IMT dengan grafik sesuai usia.|Grafik.
S|IMT adalah ukuran pasti kesehatan seseorang.|Perkiraan.
Berat 64 kg dan tinggi 1,6 m memiliki IMT …|25|40|16|10|64 : 2,56.
IMT sebaiknya ditafsirkan oleh …|tenaga kesehatan|teman sebaya|pedagang|penjual baju|Ahli.
## PJOK|Gizi untuk aktivitas fisik
Sumber energi utama saat berolahraga adalah …|karbohidrat|vitamin|mineral|serat|Karbohidrat.
Zat gizi yang membangun otot adalah …|protein|karbohidrat|lemak|air|Protein.
=|Telur dan tempe adalah sumber …|protein|Protein.
=|Cairan yang hilang lewat keringat diganti dengan minum …|air|Air.
B|Makan sebaiknya 1–2 jam sebelum olahraga.|Waktu.
S|Olahraga berat paling baik dilakukan dengan perut kosong.|Perlu energi.
Nasi dan ubi merupakan sumber …|karbohidrat|protein|vitamin|mineral|Karbohidrat.
Buah dan sayur merupakan sumber …|vitamin|lemak|protein utama|karbohidrat utama|Vitamin.
## PJOK|Pertolongan pertama luka
Langkah pertama sebelum menolong luka adalah …|mencuci tangan|menekan dengan tangan kotor|meniup luka|memijat|Cuci tangan.
Luka ringan dibersihkan dengan …|air mengalir|lumpur|minyak goreng|pasir|Air.
=|Cairan pembunuh kuman pada luka disebut …|antiseptik|Antiseptik.
=|Kain steril penutup luka disebut …|kasa|Kasa.
B|Perdarahan dihentikan dengan menekan luka memakai kasa bersih.|Tekan.
S|Luka dalam cukup ditutup plester tanpa ke tenaga medis.|Medis.
Saat mimisan, posisi yang benar adalah …|duduk menunduk|berbaring telentang|mendongak ke atas|berlari|Menunduk.
Sarung tangan dalam kotak P3K berfungsi melindungi …|penolong|luka saja|kotak|obat|Penolong.
## PJOK|Mengelola stres
Stres adalah reaksi tubuh dan pikiran terhadap …|tekanan|makanan|cuaca cerah|tidur|Tekanan.
Cara sehat mengelola stres adalah …|berolahraga|memendam sendiri|begadang|marah-marah|Olahraga.
=|Latihan yang membantu menenangkan diri adalah napas …|dalam|Napas dalam.
=|Membuat … belajar mengurangi panik menjelang ujian.|jadwal|Jadwal.
B|Bercerita kepada orang dewasa yang dipercaya membantu mengelola stres.|Dukungan.
S|Memendam masalah sendiri adalah cara terbaik mengelola stres.|Bercerita.
Stres ringan dapat …|memotivasi|menyembuhkan penyakit|menghilangkan lapar|membuat tinggi|Motivasi.
Tidur cukup membantu …|memulihkan tenaga|menambah stres|melemahkan tubuh|mengganggu belajar|Pulih.
## PJOK|Kegiatan alam terbuka
Contoh kegiatan alam terbuka adalah …|hiking|bermain gim|menonton TV|tidur siang|Hiking.
Perlengkapan yang mencegah dehidrasi adalah …|air minum|senter|jas hujan|tas kosong|Air.
=|Sebelum berkemah, kita perlu meminta izin kepada …|orang tua|Orang tua.
=|Sampah saat hiking sebaiknya dibawa …|pulang|Pulang.
B|Kegiatan alam terbuka melatih kemandirian.|Mandiri.
S|Berkemah boleh tanpa memberi tahu orang dewasa.|Izin.
Senter berfungsi sebagai …|penerangan malam|penahan hujan|tempat minum|alat masak|Senter.
Prinsip penting kegiatan alam terbuka adalah keselamatan dan …|tidak merusak alam|membuang sampah sembarangan|menebang pohon|memburu satwa|Jaga alam.
## PJOK|Sportivitas
Nama lain sportivitas adalah …|fair play|foul|offside|time out|Fair play.
Contoh sikap sportif adalah …|bersalaman dengan lawan|mengejek lawan|pura-pura jatuh|memprotes kasar|Sportif.
=|Menerima kekalahan sebaiknya dengan lapang …|dada|Lapang dada.
=|Pura-pura jatuh untuk mendapat hadiah tendangan termasuk perilaku …|curang;tidak sportif|Curang.
B|Menolong lawan yang cedera termasuk sikap sportif.|Peduli.
S|Memprotes wasit dengan kasar adalah sikap sportif.|Tidak sportif.
Tim yang kalah sebaiknya …|memberi selamat kepada pemenang|merusak fasilitas|menolak bersalaman|mengejek wasit|Sportif.
Sportivitas juga berguna dalam …|kehidupan sehari-hari|olahraga saja|tidak ada gunanya|pertandingan internasional saja|Sehari-hari.
"""

SAS += """
## SBD 1
0|Prinsip desain berupa berat visual yang setara disebut ....|keseimbangan|irama|penekanan|proporsi|Keseimbangan.
1|Huruf penuh hiasan disebut huruf ....|dekoratif|serif|sans serif|monospace|Dekoratif.
2|Foto dari samping objek berguna untuk menunjukkan ....|profil|suasana luas|detail kecil|kesan megah|Profil.
3|Kincir angin dalam seni instalasi termasuk unsur ....|gerak|teks|cahaya|suara|Gerak.
4|Memberi masukan membangun dalam kritik seni termasuk ....|saran|deskripsi|interpretasi|analisis|Saran.
5|Not seperenambelas bernilai ... ketuk.|¼|1|2|4|Seperenambelas.
6|Akor Em tersusun atas nada ....|E G B|E F G|C E G|A C E|Em.
7|Unsur musik yang menunjukkan keras lembut lagu adalah ....|dinamika|tempo|melodi|harmoni|Dinamika.
## SBD 2
0|Koreografer kontemporer Indonesia selain Sardono adalah ....|Eko Supriyanto|Gugum Gumbira|Ki Hajar Dewantara|Raja Ali Haji|Eko.
1|Pola lantai garis dan lingkaran termasuk unsur ....|ruang|tenaga|waktu|tempo|Ruang.
2|Rias untuk tokoh pelawak disebut rias ....|badut|korektif|fantasi peri|karakter tua|Badut.
3|Penata artistik bertugas mengurus ....|dekorasi dan properti|keuangan|promosi|tiket|Artistik.
4|Kain ikat celup tritik dikenal dari ....|Jawa Tengah|Papua|Aceh|Maluku|Tritik.
5|Pelitur dioleskan dengan alat ....|kuas|gergaji|bor|pahat|Kuas.
6|Identitas kemasan berupa ....|merek dan logo|busa|lem|tali|Identitas.
7|Titik penyusun gambar digital disebut ....|piksel|layer|vektor|undo|Piksel.
## PJOK 1
0|Formasi 3-5-2 memakai ... bek.|tiga|dua|lima|empat|3-5-2.
1|Strategi basket mengoper lalu lari menerima bola kembali disebut ....|give and go|fast break|press|zone|Give and go.
2|Pemain voli yang serba bisa disebut ....|universal|libero|tosser|server|Universal.
3|Pada lempar cakram, badan berputar sekitar ....|satu setengah kali|lima kali|setengah kali|sepuluh kali|Putaran.
4|Lari dengan jarak lebih dari maraton disebut ....|ultramaraton|sprint|estafet|lari gawang|Ultra.
5|Guling depan dalam rangkaian senam melatih ....|keberanian|kecepatan lari|daya tahan|kekuatan jari|Guling.
6|Pada gaya punggung, posisi badan lurus ....|telentang|telungkup|tegak|miring|Telentang.
7|Elakan dengan bergeser ke samping disebut elakan ....|samping|bawah|belakang|depan|Samping.
## PJOK 2
0|Gada dalam senam irama dimainkan dengan gerakan ....|ayunan|guling|lompat jauh|kayang|Gada.
1|Lari 1.000 meter dalam tes kebugaran mengukur ....|daya tahan jantung|kelentukan|kekuatan perut|daya ledak|Daya tahan.
2|Berat 45 kg dan tinggi 1,5 m memiliki IMT sekitar ....|20|30|15|45|45 : 2,25.
3|Alpukat dan kacang merupakan sumber ....|lemak|protein utama|vitamin C|air|Lemak.
4|Perban gulung dalam kotak P3K berfungsi untuk ....|membalut|membersihkan luka|membunuh kuman|memotong|Perban.
5|Melakukan hobi membantu ....|menyegarkan pikiran|menambah stres|merusak tidur|melemahkan tubuh|Hobi.
6|Jas hujan dalam kegiatan alam berfungsi ....|melindungi dari hujan|penerangan|menyimpan air|memasak|Jas hujan.
7|Mengejek lawan termasuk perilaku ....|tidak sportif|sportif|peduli|lapang dada|Tidak sportif.
"""

TOPICS += """
## INF
# 1|Keamanan, Sistem, dan Masyarakat Digital
@ Kriptografi sederhana
min: 15
act: Kirim pesan rahasia kepada teman memakai sandi Caesar dengan geseran 3.
mis: mengira pesan terenkripsi dapat dibaca tanpa kunci
exp: Kriptografi adalah ilmu mengamankan pesan dengan mengubahnya menjadi bentuk yang tidak terbaca. Proses mengubah pesan asli menjadi sandi disebut enkripsi, sedangkan mengembalikannya disebut dekripsi. Sandi Caesar menggeser setiap huruf sejumlah langkah tertentu. Kriptografi modern melindungi data perbankan dan pesan daring.
ex: Dengan geseran 3, kata ABC menjadi DEF. // Aplikasi pesan memakai enkripsi ujung ke ujung.
pt: Mengamankan pesan ; Enkripsi dan dekripsi ; Sandi Caesar menggeser huruf
sum: Kriptografi menjaga kerahasiaan informasi.
fig: table Huruf asli | Sandi Caesar geser 3 ;; A | D ;; B | E ;; C | F ;; X | A ;; Y | B ;; Z | C ~ Sandi Caesar geseran 3.
@ Phishing dan rekayasa sosial
min: 15
act: Periksa contoh pesan berhadiah palsu bersama orang tua, lalu tandai ciri penipuannya.
mis: mengklik tautan dari pesan berhadiah tanpa memeriksa pengirimnya
exp: Phishing adalah penipuan untuk mencuri data pribadi, kata sandi, atau kode OTP dengan menyamar sebagai pihak terpercaya. Rekayasa sosial memanfaatkan rasa takut, panik, atau senang korban. Cirinya antara lain pesan mendesak, hadiah tidak wajar, alamat situs mirip asli, dan permintaan kode rahasia.
ex: Pesan mengaku dari bank meminta kode OTP. // Tautan palsu mirip nama situs resmi.
pt: Mencuri data dengan menyamar ; Memanfaatkan emosi ; Mendesak, hadiah, tautan mirip
sum: Waspada dan periksa sebelum mengklik.
fig: table Ciri phishing | Contoh ;; mendesak | akun diblokir dalam 1 jam ;; hadiah tidak wajar | menang undian tanpa ikut ;; tautan mirip | bankk-resmi.com ;; meminta kode | minta OTP ;; tata bahasa aneh | banyak salah ketik ;; pengirim asing | nomor tidak dikenal ~ Ciri pesan phishing.
@ Kata sandi kuat
min: 15
act: Buat contoh kata sandi kuat dari kalimat favorit, tetapi jangan dipakai untuk akun sungguhan.
mis: memakai tanggal lahir sebagai kata sandi
exp: Kata sandi kuat panjangnya minimal 12 karakter dan memadukan huruf besar, huruf kecil, angka, dan simbol. Hindari data pribadi seperti nama dan tanggal lahir. Gunakan kata sandi berbeda untuk setiap akun. Pengelola kata sandi membantu menyimpan banyak kata sandi dengan aman, dan verifikasi dua langkah menambah perlindungan.
ex: Frasa panjang lebih sulit ditebak. // Satu kata sandi bocor tidak membahayakan akun lain jika berbeda.
pt: Minimal 12 karakter campuran ; Hindari data pribadi ; Berbeda untuk setiap akun
sum: Kata sandi kuat adalah kunci keamanan akun.
fig: table Kata sandi | Kekuatan ;; 123456 | sangat lemah ;; nama dan tanggal lahir | lemah mudah ditebak ;; password | sangat lemah umum ;; frasa panjang dengan simbol | kuat ;; campuran 16 karakter acak | sangat kuat ;; kata sandi sama di semua akun | berisiko ~ Contoh kekuatan kata sandi.
@ Internet of Things
min: 15
act: Cari perangkat di rumah atau sekitar yang dapat dikendalikan lewat aplikasi.
mis: mengira IoT hanya berupa robot
exp: Internet of Things atau IoT adalah jaringan benda sehari-hari yang dilengkapi sensor dan terhubung ke internet sehingga dapat bertukar data dan dikendalikan dari jauh. Contohnya lampu pintar, CCTV daring, jam tangan pintar, dan sensor pertanian. IoT memudahkan hidup tetapi perlu dijaga keamanannya.
ex: Lampu dinyalakan dari HP. // Sensor tanah memberi tahu kapan tanaman perlu disiram.
pt: Benda bersensor terhubung internet ; Bertukar data dan dikendalikan jarak jauh ; Perlu keamanan
sum: IoT menghubungkan benda di sekitar kita.
fig: table Perangkat IoT | Fungsi ;; lampu pintar | dinyalakan dari HP ;; CCTV daring | memantau rumah ;; jam tangan pintar | mencatat langkah ;; sensor tanah | mengukur kelembapan ;; meteran listrik pintar | memantau pemakaian ;; kunci pintu pintar | membuka dengan aplikasi ~ Contoh perangkat IoT.
@ Sistem informasi
min: 15
act: Gambarkan alur sistem informasi perpustakaan sekolah dari peminjaman sampai pengembalian.
mis: menganggap sistem informasi hanya berupa komputer
exp: Sistem informasi adalah gabungan manusia, perangkat keras, perangkat lunak, data, dan prosedur untuk mengumpulkan, mengolah, dan menyajikan informasi. Contohnya sistem informasi akademik, kasir toko, dan perpustakaan. Alurnya terdiri atas masukan, proses, keluaran, dan penyimpanan.
ex: Kasir memindai barang lalu mencetak struk. // Sistem akademik menampilkan nilai siswa.
pt: Manusia, perangkat, data, prosedur ; Masukan, proses, keluaran ; Akademik, kasir, perpustakaan
sum: Sistem informasi mengubah data menjadi informasi berguna.
fig: table Komponen | Contoh pada kasir toko ;; manusia | petugas kasir ;; perangkat keras | pemindai kode batang ;; perangkat lunak | aplikasi kasir ;; data | harga barang ;; prosedur | langkah pembayaran ;; keluaran | struk belanja ~ Komponen sistem informasi.
@ Big data
min: 15
act: Diskusikan data apa saja yang kamu hasilkan dalam sehari saat memakai internet.
mis: mengira big data hanya berarti data yang besar ukurannya
exp: Big data adalah kumpulan data yang sangat besar, beragam, dan bertambah cepat sehingga perlu teknologi khusus untuk mengolahnya. Ciri big data dikenal dengan volume, variety atau keragaman, dan velocity atau kecepatan. Big data dipakai untuk prakiraan cuaca, rekomendasi belanja, dan pengaturan lalu lintas.
ex: Aplikasi peta mengolah data lalu lintas jutaan pengguna. // Toko daring menganalisis pola belanja.
pt: Sangat besar, beragam, cepat ; Volume, variety, velocity ; Cuaca, belanja, lalu lintas
sum: Big data membantu mengambil keputusan berbasis data.
fig: table Ciri big data | Arti ;; volume | jumlah sangat besar ;; variety | jenis data beragam ;; velocity | bertambah sangat cepat ;; veracity | kebenaran data ;; value | nilai manfaat ;; visualisasi | penyajian mudah dipahami ~ Ciri big data.
@ Karier di bidang informatika
min: 15
act: Wawancarai seseorang yang bekerja dengan komputer tentang tugas sehari-harinya.
mis: mengira semua pekerjaan informatika hanya pemrogram
exp: Bidang informatika menawarkan banyak karier, misalnya pengembang perangkat lunak, analis data, desainer UI/UX, ahli keamanan siber, administrator jaringan, dan pengembang gim. Keterampilan yang dibutuhkan antara lain berpikir logis, pemecahan masalah, kerja tim, dan belajar sepanjang hayat.
ex: Analis data mengolah data penjualan. // Ahli keamanan siber melindungi sistem dari serangan.
pt: Banyak jenis karier ; Pengembang, analis, desainer, keamanan ; Logika dan belajar terus
sum: Informatika membuka banyak peluang karier.
fig: table Karier | Tugas ;; pengembang perangkat lunak | membuat aplikasi ;; analis data | mengolah data ;; desainer UI/UX | merancang tampilan ;; ahli keamanan siber | melindungi sistem ;; administrator jaringan | mengelola jaringan ;; pengembang gim | membuat permainan ~ Karier informatika.
@ Inklusi digital
min: 15
act: Cari fitur aksesibilitas di HP, misalnya pembaca layar atau ukuran huruf besar.
mis: mengira teknologi digital otomatis dapat dipakai semua orang
exp: Inklusi digital adalah upaya agar semua orang dapat mengakses dan memanfaatkan teknologi digital, termasuk lansia, penyandang disabilitas, dan masyarakat di daerah terpencil. Kesenjangan digital terjadi karena perbedaan akses internet, perangkat, dan keterampilan. Fitur aksesibilitas seperti pembaca layar dan teks besar membantu inklusi.
ex: Pembaca layar membantu tunanetra memakai HP. // Mengajari kakek nenek memakai aplikasi panggilan video.
pt: Teknologi untuk semua ; Kesenjangan akses dan keterampilan ; Fitur aksesibilitas
sum: Teknologi yang baik dapat dipakai semua orang.
fig: table Fitur aksesibilitas | Membantu ;; pembaca layar | tunanetra ;; teks besar | penglihatan lemah ;; teks otomatis | tunarungu ;; perintah suara | kesulitan menyentuh layar ;; kontras tinggi | buta warna ;; mode sederhana | lansia ~ Fitur aksesibilitas.
# 2|Pengolahan Data dan Pengembangan Aplikasi
@ Tabel pivot
min: 15
act: Buat tabel pivot dari data pengeluaran keluarga untuk melihat total per kategori.
mis: menjumlahkan data satu per satu secara manual padahal datanya banyak
exp: Tabel pivot adalah fitur lembar kerja untuk meringkas data besar dengan cepat. Data dapat dikelompokkan berdasarkan kategori, lalu dihitung jumlah, rata-rata, atau banyaknya. Tabel pivot memudahkan melihat pola tanpa mengubah data asli.
ex: Total penjualan per bulan. // Jumlah siswa per kelas dan jenis ekstrakurikuler.
pt: Meringkas data besar ; Kelompokkan per kategori ; Jumlah, rata-rata, banyak data
sum: Tabel pivot mempercepat analisis data.
fig: table Bagian pivot | Fungsi ;; baris | kategori yang dikelompokkan ;; kolom | kategori tambahan ;; nilai | angka yang dihitung ;; filter | menyaring data ;; jumlah | menjumlahkan nilai ;; rata-rata | menghitung rerata ~ Bagian tabel pivot.
@ Simulasi dan pemodelan
min: 15
act: Simulasikan antrean kantin memakai dadu untuk menentukan waktu datang siswa.
mis: menganggap hasil simulasi pasti sama dengan kenyataan
exp: Pemodelan adalah membuat gambaran sederhana dari sistem nyata. Simulasi adalah menjalankan model untuk melihat apa yang terjadi dalam berbagai kondisi. Simulasi dipakai untuk prakiraan cuaca, latihan pilot, dan perencanaan lalu lintas. Hasil simulasi bergantung pada asumsi model.
ex: Simulator penerbangan melatih pilot. // Simulasi penyebaran penyakit membantu perencanaan kesehatan.
pt: Model gambaran sederhana ; Simulasi menjalankan model ; Hasil bergantung asumsi
sum: Simulasi membantu mencoba tanpa risiko nyata.
fig: table Simulasi | Kegunaan ;; simulator penerbangan | melatih pilot ;; prakiraan cuaca | memperkirakan hujan ;; simulasi lalu lintas | mengatur lampu jalan ;; simulasi gempa | merancang bangunan aman ;; simulasi antrean | mengatur kasir ;; simulasi ekonomi | merencanakan kebijakan ~ Kegunaan simulasi.
@ CSS untuk tampilan web
min: 15
act: Ubah warna latar dan ukuran huruf halaman HTML sederhana memakai CSS.
mis: menulis semua gaya langsung di setiap tag HTML
exp: CSS atau Cascading Style Sheets adalah bahasa untuk mengatur tampilan halaman web, seperti warna, huruf, jarak, dan tata letak. Aturan CSS terdiri atas selektor, properti, dan nilai, misalnya h1 { color: blue; }. CSS memisahkan isi dan tampilan sehingga halaman lebih rapi dan mudah diubah.
ex: p { font-size: 16px; } mengatur ukuran huruf paragraf. // body { background-color: white; }
pt: Mengatur tampilan web ; Selektor, properti, nilai ; Memisahkan isi dan tampilan
sum: CSS membuat halaman web menarik dan rapi.
fig: table Properti CSS | Fungsi ;; color | warna teks ;; background-color | warna latar ;; font-size | ukuran huruf ;; margin | jarak luar ;; padding | jarak dalam ;; text-align | perataan teks ~ Properti CSS.
@ Basis data relasional
min: 15
act: Rancang dua tabel, siswa dan peminjaman buku, yang dihubungkan dengan nomor induk.
mis: menulis data siswa berulang-ulang di setiap baris peminjaman
exp: Basis data relasional menyimpan data dalam beberapa tabel yang saling berhubungan melalui kunci. Kunci utama atau primary key mengenali setiap baris secara unik. Kunci tamu atau foreign key menghubungkan ke tabel lain. Data diambil dengan bahasa kueri SQL.
ex: Tabel peminjaman menyimpan NIS sebagai kunci tamu. // SELECT nama FROM siswa;
pt: Beberapa tabel saling berhubungan ; Primary key dan foreign key ; Kueri SQL
sum: Basis data relasional mengurangi data ganda.
fig: table Istilah | Arti ;; tabel | kumpulan data sejenis ;; primary key | penanda unik baris ;; foreign key | penghubung ke tabel lain ;; relasi | hubungan antartabel ;; SQL | bahasa kueri ;; SELECT | perintah mengambil data ~ Istilah basis data relasional.
@ Kolaborasi kode dengan Git
min: 15
act: Tonton penjelasan Git, lalu buat diagram alur commit dan push bersama teman.
mis: menyimpan banyak salinan berkas dengan nama final, final2, final3
exp: Git adalah sistem kendali versi untuk mencatat perubahan kode. Setiap simpanan perubahan disebut commit. Repositori menyimpan seluruh riwayat proyek. Cabang atau branch memungkinkan bekerja tanpa mengganggu kode utama. Layanan seperti GitHub memudahkan kolaborasi tim.
ex: git commit menyimpan perubahan dengan pesan. // Branch dipakai untuk mencoba fitur baru.
pt: Sistem kendali versi ; Commit, repositori, branch ; Kolaborasi tim
sum: Git membuat kerja kode bersama lebih teratur.
fig: table Istilah Git | Arti ;; repositori | tempat menyimpan proyek ;; commit | simpanan perubahan ;; branch | cabang pengembangan ;; merge | menggabungkan cabang ;; push | mengirim ke server ;; pull | mengambil perubahan ~ Istilah Git.
@ Pengujian perangkat lunak
min: 15
act: Uji aplikasi kalkulator HP dengan angka besar, nol, dan desimal, lalu catat hasilnya.
mis: hanya menguji dengan masukan yang biasa
exp: Pengujian perangkat lunak memastikan program bekerja sesuai harapan. Kasus uji berisi masukan, langkah, dan hasil yang diharapkan. Pengujian mencakup nilai normal, nilai batas, dan masukan tidak valid. Pengujian unit memeriksa bagian kecil, sedangkan pengujian sistem memeriksa keseluruhan aplikasi.
ex: Menguji pembagian dengan nol. // Kasus uji: masukan 2 + 2, hasil diharapkan 4.
pt: Memastikan program sesuai harapan ; Kasus uji ; Nilai normal, batas, tidak valid
sum: Pengujian menemukan kesalahan sebelum pengguna menemukannya.
fig: table Jenis pengujian | Fokus ;; pengujian unit | bagian kecil program ;; pengujian integrasi | gabungan bagian ;; pengujian sistem | keseluruhan aplikasi ;; pengujian penerimaan | kebutuhan pengguna ;; uji nilai batas | masukan ekstrem ;; uji regresi | fitur lama tetap jalan ~ Jenis pengujian perangkat lunak.
@ Antarmuka pemrograman aplikasi
min: 15
act: Amati bagaimana aplikasi cuaca menampilkan data dari layanan prakiraan.
mis: mengira setiap aplikasi membuat semua datanya sendiri
exp: API atau Application Programming Interface adalah perantara yang memungkinkan dua aplikasi saling bertukar data. Aplikasi mengirim permintaan atau request ke API, lalu API mengirim tanggapan atau response, biasanya dalam format JSON. Contohnya aplikasi ojek memakai API peta dan aplikasi cuaca memakai API prakiraan.
ex: Aplikasi belanja memakai API pembayaran. // Data cuaca dikirim dalam format JSON.
pt: Perantara antaraplikasi ; Request dan response ; Format JSON
sum: API membuat aplikasi dapat saling bekerja sama.
fig: table Istilah API | Arti ;; request | permintaan data ;; response | tanggapan data ;; endpoint | alamat layanan ;; JSON | format data teks ;; kunci API | tanda izin akses ;; batas permintaan | jumlah akses maksimum ~ Istilah API.
@ Pengembangan aplikasi seluler
min: 15
act: Rancang sketsa layar aplikasi daftar tugas sekolah untuk HP.
mis: merancang aplikasi HP dengan tombol terlalu kecil
exp: Aplikasi seluler adalah aplikasi untuk HP dan tablet, berjalan pada sistem operasi seperti Android dan iOS. Pengembangannya meliputi perancangan kebutuhan, desain antarmuka, pemrograman, pengujian, dan rilis ke toko aplikasi. Desain harus memperhatikan layar kecil, sentuhan jari, dan hemat baterai.
ex: Aplikasi Android dirilis di Google Play. // Tombol dibuat cukup besar untuk jari.
pt: Untuk HP dan tablet ; Rancang, desain, program, uji, rilis ; Layar kecil dan hemat baterai
sum: Aplikasi seluler yang baik nyaman dipakai dengan satu tangan.
fig: table Tahap | Kegiatan ;; analisis kebutuhan | menentukan fitur ;; desain antarmuka | merancang layar ;; pemrograman | menulis kode ;; pengujian | mencari kesalahan ;; rilis | unggah ke toko aplikasi ;; pembaruan | memperbaiki dan menambah fitur ~ Tahap pengembangan aplikasi seluler.

## KKA
# 1|Pemrograman Data dan Algoritma
@ Membaca berkas CSV
min: 15
act: Simpan data nilai teman dalam format CSV, lalu baca dengan program Python.
mis: mengira CSV hanya bisa dibuka dengan aplikasi lembar kerja
exp: CSV atau Comma Separated Values adalah format berkas teks yang menyimpan data tabel, dengan setiap kolom dipisahkan koma. Python membaca CSV dengan modul csv. Setiap baris dibaca sebagai list atau dictionary. CSV mudah dipakai untuk bertukar data antaraplikasi.
ex: nama,nilai lalu Budi,85 pada baris berikutnya. // import csv lalu csv.reader(f).
pt: Data tabel dipisah koma ; Dibaca dengan modul csv ; Mudah bertukar data
sum: CSV adalah format data sederhana yang serbaguna.
fig: table Baris CSV | Isi ;; baris 1 | judul kolom ;; baris 2 | data pertama ;; pemisah | koma ;; ekstensi | .csv ;; modul Python | csv ;; fungsi baca | csv.reader ~ Struktur berkas CSV.
@ Pencarian biner
min: 15
act: Main tebak angka 1–100 dan selalu tebak angka tengah, lalu hitung berapa kali sampai benar.
mis: memakai pencarian biner pada data yang belum terurut
exp: Pencarian biner mencari data pada daftar yang sudah terurut dengan cara membagi dua bagian berulang kali. Bandingkan nilai yang dicari dengan nilai tengah; jika lebih kecil cari di setengah kiri, jika lebih besar cari di setengah kanan. Pencarian biner jauh lebih cepat daripada pencarian linear untuk data besar.
ex: Mencari kata di kamus dengan membuka bagian tengah. // 100 data cukup sekitar 7 langkah.
pt: Data harus terurut ; Bandingkan dengan nilai tengah ; Lebih cepat dari linear
sum: Pencarian biner menghemat langkah pada data besar.
fig: table Banyak data | Langkah maksimum pencarian biner ;; 8 | 3 ;; 16 | 4 ;; 100 | 7 ;; 1.000 | 10 ;; 1.000.000 | 20 ;; 2 | 1 ~ Efisiensi pencarian biner.
@ Rekursi
min: 15
act: Tulis fungsi faktorial rekursif di Python dan uji untuk angka 5.
mis: membuat fungsi rekursif tanpa kasus dasar sehingga tidak berhenti
exp: Rekursi adalah fungsi yang memanggil dirinya sendiri untuk menyelesaikan masalah yang lebih kecil. Fungsi rekursif harus memiliki kasus dasar agar berhenti. Contohnya faktorial: n! = n × (n - 1)!, dengan 0! = 1 sebagai kasus dasar. Rekursi cocok untuk struktur bertingkat seperti folder.
ex: def faktorial(n): return 1 if n == 0 else n * faktorial(n - 1) // faktorial(5) = 120.
pt: Fungsi memanggil dirinya ; Wajib kasus dasar ; Contoh faktorial
sum: Rekursi memecah masalah besar menjadi kecil yang serupa.
fig: table n | Faktorial ;; 0 | 1 ;; 1 | 1 dari 1 × 0! ;; 2 | 2 ;; 3 | 6 ;; 4 | 24 ;; 5 | 120 ~ Nilai faktorial.
@ Kelas dan objek
min: 15
act: Buat kelas Hewan dengan atribut nama dan metode bersuara di Python.
mis: menyamakan kelas dengan objek
exp: Pemrograman berorientasi objek menyusun program dari objek. Kelas adalah cetak biru, sedangkan objek adalah wujud nyata dari kelas. Kelas memiliki atribut yang menyimpan data dan metode yang berupa fungsi. Dalam Python, kelas dibuat dengan class dan inisialisasi memakai __init__.
ex: class Kucing: lalu objek kitty = Kucing("Kitty"). // kitty.bersuara() memanggil metode.
pt: Kelas cetak biru, objek wujud nyata ; Atribut dan metode ; class dan __init__
sum: Kelas dan objek membuat program terstruktur.
fig: table Istilah | Contoh ;; kelas | Kucing ;; objek | kitty ;; atribut | nama dan warna ;; metode | bersuara() ;; konstruktor | __init__ ;; self | merujuk objek itu sendiri ~ Istilah pemrograman berorientasi objek.
@ Validasi masukan
min: 15
act: Buat program yang menolak umur negatif atau bukan angka, lalu uji dengan beberapa masukan.
mis: langsung memakai masukan pengguna tanpa memeriksa
exp: Validasi masukan adalah memeriksa data dari pengguna sebelum dipakai agar program tidak error dan aman. Pemeriksaan meliputi jenis data, rentang nilai, panjang teks, dan format. Dalam Python, try dan except dipakai untuk menangani masukan yang tidak dapat diubah menjadi angka.
ex: try: umur = int(input()) except ValueError: print("Harus angka") // Tolak umur di bawah 0.
pt: Periksa data sebelum dipakai ; Jenis, rentang, panjang, format ; try dan except
sum: Validasi membuat program kuat dan aman.
fig: table Jenis validasi | Contoh ;; jenis data | umur harus angka ;; rentang | nilai 0 sampai 100 ;; panjang | kata sandi minimal 8 ;; format | alamat surel berisi @ ;; wajib diisi | nama tidak kosong ;; pilihan | jawaban ya atau tidak ~ Jenis validasi masukan.
@ Pohon keputusan
min: 15
act: Buat pohon keputusan untuk menentukan pakaian berdasarkan cuaca.
mis: membuat cabang pertanyaan yang tidak berujung pada keputusan
exp: Pohon keputusan adalah model yang memecah keputusan menjadi serangkaian pertanyaan bercabang. Setiap simpul berisi pertanyaan, cabang berisi jawaban, dan daun berisi keputusan akhir. Pohon keputusan dipakai dalam pembelajaran mesin untuk klasifikasi karena mudah dipahami manusia.
ex: Apakah hujan? Ya → bawa payung. // Model memprediksi buah dari warna dan ukuran.
pt: Pertanyaan bercabang ; Simpul, cabang, daun ; Untuk klasifikasi
sum: Pohon keputusan membuat logika keputusan terlihat jelas.
fig: table Bagian | Isi ;; akar | pertanyaan pertama ;; simpul | pertanyaan lanjutan ;; cabang | jawaban ;; daun | keputusan akhir ;; kedalaman | banyak tingkat ;; klasifikasi | menentukan kelompok ~ Bagian pohon keputusan.
@ Visualisasi data dengan Python
min: 15
act: Buat grafik batang jumlah buku yang dibaca anggota keluarga memakai Python.
mis: memilih jenis grafik yang tidak sesuai data
exp: Python dapat membuat grafik dengan pustaka matplotlib. Data disiapkan dalam list, lalu digambar dengan fungsi seperti bar untuk grafik batang, plot untuk grafik garis, dan pie untuk grafik lingkaran. Grafik diberi judul dan label sumbu agar mudah dibaca.
ex: plt.bar(nama, jumlah) membuat grafik batang. // plt.title("Buku dibaca") memberi judul.
pt: Pustaka matplotlib ; bar, plot, pie ; Judul dan label sumbu
sum: Visualisasi membuat data mudah dipahami.
fig: table Fungsi matplotlib | Hasil ;; plt.bar | grafik batang ;; plt.plot | grafik garis ;; plt.pie | grafik lingkaran ;; plt.title | judul grafik ;; plt.xlabel | label sumbu X ;; plt.show | menampilkan grafik ~ Fungsi matplotlib.
@ Proyek kalkulator nilai
min: 15
act: Buat program yang menerima lima nilai, lalu menampilkan rata-rata dan predikat.
mis: membagi total nilai dengan angka yang salah
exp: Proyek kalkulator nilai menggabungkan list, perulangan, fungsi, percabangan, dan validasi. Program meminta beberapa nilai, menyimpannya dalam list, menghitung rata-rata dengan sum dibagi len, lalu menentukan predikat dengan if-elif. Program diuji dengan berbagai masukan.
ex: rata = sum(nilai) / len(nilai) // if rata >= 90: predikat = "A"
pt: List, perulangan, fungsi ; Rata-rata sum dibagi len ; Predikat dengan if-elif
sum: Proyek kecil melatih berpikir sistematis.
fig: table Rata-rata | Predikat ;; 90 sampai 100 | A ;; 80 sampai 89 | B ;; 70 sampai 79 | C ;; 60 sampai 69 | D ;; di bawah 60 | E ;; bukan angka | ditolak ~ Aturan predikat nilai.
# 2|Kecerdasan Artifisial dan Masyarakat
@ Model bahasa besar
min: 15
act: Bandingkan jawaban asisten KA untuk pertanyaan sejarah dengan buku pelajaran.
mis: mengira model bahasa benar-benar memahami seperti manusia
exp: Model bahasa besar atau LLM adalah model KA yang dilatih dengan sangat banyak teks sehingga dapat menghasilkan tulisan, menjawab pertanyaan, dan meringkas. LLM bekerja dengan memprediksi kata berikutnya berdasarkan pola. LLM berguna untuk belajar, tetapi jawabannya perlu diperiksa.
ex: Asisten KA membantu menjelaskan konsep sulit. // LLM dapat meringkas artikel panjang.
pt: Dilatih dengan banyak teks ; Memprediksi kata berikutnya ; Jawaban perlu diperiksa
sum: LLM adalah alat bantu, bukan sumber kebenaran mutlak.
fig: table Kemampuan LLM | Contoh ;; menjawab pertanyaan | menjelaskan fotosintesis ;; meringkas | merangkum artikel ;; menerjemahkan | Indonesia ke Inggris ;; menulis draf | membuat kerangka esai ;; menjelaskan kode | membaca program Python ;; bertukar ide | curah gagasan proyek ~ Kemampuan model bahasa besar.
@ Halusinasi KA
min: 15
act: Minta asisten KA menyebut sumber, lalu periksa apakah sumber itu benar ada.
mis: langsung mengutip fakta dari KA tanpa memeriksa
exp: Halusinasi KA terjadi ketika KA menghasilkan informasi yang terdengar meyakinkan tetapi salah atau dibuat-buat, misalnya kutipan atau sumber palsu. Ini terjadi karena KA memprediksi pola, bukan memeriksa fakta. Cara mengatasinya adalah memeriksa ke sumber terpercaya dan meminta rujukan yang dapat dicek.
ex: KA menyebut judul buku yang ternyata tidak ada. // Tanggal peristiwa dari KA dicek di buku sejarah.
pt: Informasi meyakinkan tetapi salah ; Karena memprediksi pola ; Periksa ke sumber terpercaya
sum: Selalu periksa fakta dari KA.
fig: table Bentuk halusinasi | Cara memeriksa ;; sumber palsu | cari di perpustakaan atau internet ;; angka keliru | cek data resmi ;; kutipan palsu | cari kutipan asli ;; tanggal salah | cek buku sejarah ;; tokoh tertukar | bandingkan beberapa sumber ;; istilah dibuat-buat | cek kamus ~ Halusinasi KA dan cara memeriksanya.
@ KA pembuat gambar
min: 15
act: Diskusikan kapan gambar buatan KA perlu diberi label agar tidak menyesatkan.
mis: menganggap semua gambar realistis di internet pasti foto asli
exp: KA pembuat gambar menghasilkan gambar dari perintah teks. Teknologi ini membantu desain dan ilustrasi, tetapi dapat disalahgunakan untuk membuat gambar palsu. Pemakaian yang etis berarti memberi label buatan KA, tidak meniru orang nyata tanpa izin, dan menghormati karya seniman.
ex: Ilustrasi buku cerita dibuat dengan bantuan KA dan diberi keterangan. // Gambar tokoh palsu dapat menyebarkan hoaks.
pt: Gambar dari perintah teks ; Membantu desain, bisa disalahgunakan ; Beri label dan hormati seniman
sum: KA pembuat gambar harus dipakai jujur dan bertanggung jawab.
fig: table Pemakaian | Etis atau tidak ;; ilustrasi tugas diberi label | etis ;; gambar palsu tokoh untuk hoaks | tidak etis ;; meniru wajah teman tanpa izin | melanggar privasi ;; konsep desain awal | membantu kreativitas ;; mengaku karya KA buatan tangan | tidak jujur ;; poster acara kelas berlabel | etis dan terbuka ~ Pemakaian KA pembuat gambar.
@ Regulasi KA
min: 15
act: Cari berita tentang aturan pemakaian KA di Indonesia atau negara lain.
mis: mengira KA boleh dipakai tanpa aturan apa pun
exp: Regulasi KA adalah aturan yang mengatur pengembangan dan pemakaian KA agar aman, adil, dan bertanggung jawab. Aturan biasanya mengatur perlindungan data pribadi, transparansi, keamanan, dan tanggung jawab jika terjadi kerugian. Indonesia memiliki Undang-Undang Pelindungan Data Pribadi yang berkaitan dengan pemakaian data oleh KA.
ex: Aplikasi wajib meminta izin sebelum memakai data pribadi. // Pengguna berhak tahu jika berinteraksi dengan KA.
pt: Aturan agar KA aman dan adil ; Data pribadi, transparansi, keamanan ; UU Pelindungan Data Pribadi
sum: Regulasi melindungi masyarakat dari risiko KA.
fig: table Prinsip regulasi | Arti ;; transparansi | pengguna tahu cara kerja KA ;; akuntabilitas | ada pihak bertanggung jawab ;; privasi | data pribadi terlindungi ;; keamanan | KA tidak membahayakan ;; keadilan | tidak diskriminatif ;; pengawasan manusia | manusia tetap mengendalikan ~ Prinsip regulasi KA.
@ Keadilan algoritma
min: 15
act: Diskusikan contoh keputusan otomatis yang bisa merugikan kelompok tertentu.
mis: mengira keputusan mesin selalu netral
exp: Keadilan algoritma berarti sistem KA tidak memperlakukan kelompok tertentu secara tidak adil. Ketidakadilan dapat muncul dari data latih yang bias, misalnya data yang hanya mewakili satu kelompok. Cara mengatasinya adalah memakai data beragam, menguji hasil untuk berbagai kelompok, dan melibatkan pengawasan manusia.
ex: Pengenal wajah kurang akurat untuk warna kulit tertentu karena datanya kurang. // Seleksi otomatis perlu diperiksa manusia.
pt: Tidak memperlakukan kelompok secara tidak adil ; Bias dari data latih ; Data beragam dan pengawasan manusia
sum: Algoritma adil membutuhkan data dan pengujian yang adil.
fig: table Sumber bias | Cara mengurangi ;; data kurang beragam | tambah data berbagai kelompok ;; label keliru | periksa ulang label ;; tujuan sempit | rumuskan tujuan adil ;; tanpa pengujian | uji per kelompok ;; tanpa pengawasan | libatkan manusia ;; data lama | perbarui data ~ Sumber bias algoritma.
@ KA dalam keamanan siber
min: 15
act: Cari tahu bagaimana layanan surel menyaring surel spam secara otomatis.
mis: mengira KA hanya dipakai untuk menyerang sistem
exp: KA dipakai dalam keamanan siber untuk mendeteksi serangan, menyaring spam dan phishing, serta mengenali aktivitas mencurigakan. Di sisi lain, penjahat juga dapat memakai KA untuk membuat penipuan yang lebih meyakinkan. Karena itu pengguna tetap harus waspada dan menjaga kebiasaan aman.
ex: Bank mendeteksi transaksi aneh secara otomatis. // Surel phishing buatan KA terlihat lebih rapi.
pt: Mendeteksi serangan dan spam ; Penjahat juga memakai KA ; Pengguna tetap waspada
sum: KA adalah alat yang dapat melindungi maupun disalahgunakan.
fig: table Pemakaian KA | Tujuan ;; filter spam | menyaring surel sampah ;; deteksi penipuan | mengenali transaksi aneh ;; deteksi malware | mengenali program jahat ;; pemantauan jaringan | mencari aktivitas mencurigakan ;; verifikasi wajah | memastikan pemilik akun ;; phishing buatan KA | disalahgunakan penjahat ~ KA dalam keamanan siber.
@ KA dalam kesehatan
min: 15
act: Cari contoh aplikasi kesehatan yang memakai KA dan tulis manfaatnya.
mis: memakai jawaban aplikasi KA sebagai pengganti dokter
exp: KA membantu bidang kesehatan, misalnya membaca hasil rontgen, memprediksi wabah, mempercepat penemuan obat, dan mengingatkan jadwal minum obat. Namun, keputusan medis tetap ditentukan dokter. Data kesehatan termasuk data sensitif yang harus dilindungi.
ex: KA membantu mendeteksi tanda penyakit pada foto paru. // Aplikasi mengingatkan jadwal imunisasi.
pt: Membaca rontgen dan memprediksi wabah ; Keputusan tetap oleh dokter ; Data kesehatan sensitif
sum: KA membantu tenaga kesehatan, bukan menggantikan.
fig: table Penerapan | Manfaat ;; analisis rontgen | membantu deteksi dini ;; prediksi wabah | persiapan layanan ;; penemuan obat | riset lebih cepat ;; pengingat obat | pasien teratur minum obat ;; asisten rekam medis | dokter hemat waktu ;; telemedisin | konsultasi jarak jauh ~ KA dalam kesehatan.
@ Belajar cerdas dengan KA
min: 15
act: Gunakan asisten KA untuk membuat soal latihan, lalu kerjakan sendiri tanpa melihat jawabannya.
mis: menyalin jawaban KA untuk tugas tanpa memahami
exp: KA dapat menjadi teman belajar jika dipakai dengan benar, misalnya untuk menjelaskan ulang konsep, membuat soal latihan, atau memberi umpan balik pada tulisan. Pemakaian yang baik tetap melibatkan usaha berpikir sendiri, memeriksa kebenaran, dan mengikuti aturan sekolah. Menyalin jawaban tanpa memahami merugikan diri sendiri.
ex: Meminta KA menjelaskan pecahan dengan contoh kue. // Menulis esai sendiri lalu meminta saran perbaikan.
pt: Jelaskan konsep, buat soal, beri umpan balik ; Tetap berpikir sendiri ; Ikuti aturan sekolah
sum: KA membantu belajar bila kita tetap aktif berpikir.
fig: table Cara memakai KA | Baik atau tidak ;; meminta penjelasan ulang | baik ;; membuat soal latihan | baik untuk berlatih ;; menyalin jawaban tugas | tidak baik ;; meminta umpan balik tulisan | baik untuk perbaikan ;; memakai saat ujian tanpa izin | curang ;; memeriksa ulang fakta | bertanggung jawab ~ Cara memakai KA untuk belajar.
"""

BANK += """
## INF|Kriptografi sederhana
Proses mengubah pesan asli menjadi sandi disebut …|enkripsi|dekripsi|kompresi|transmisi|Enkripsi.
Proses mengembalikan sandi menjadi pesan asli disebut …|dekripsi|enkripsi|kompresi|indeksasi|Dekripsi.
=|Dengan sandi Caesar geseran 3, huruf A menjadi …|D|D.
=|Dengan sandi Caesar geseran 3, huruf X menjadi …|A|A.
B|Kriptografi melindungi data perbankan.|Bank.
S|Pesan terenkripsi mudah dibaca tanpa kunci.|Perlu kunci.
Dengan geseran 3, kata ABC menjadi …|DEF|BCD|XYZ|CBA|Geser 3.
Aplikasi pesan yang hanya dapat dibaca pengirim dan penerima memakai enkripsi …|ujung ke ujung|terbuka|tanpa kunci|publik|End-to-end.
## INF|Phishing dan rekayasa sosial
Penipuan untuk mencuri data dengan menyamar disebut …|phishing|hacking etis|enkripsi|backup|Phishing.
Rekayasa sosial memanfaatkan … korban.|emosi|kode|jaringan|baterai|Emosi.
=|Kode rahasia sekali pakai yang sering diminta penipu disebut …|OTP|OTP.
=|Pesan yang meminta tindakan segera bersifat …|mendesak|Mendesak.
B|Tautan bankk-resmi.com patut dicurigai.|Mirip.
S|Pesan berhadiah dari nomor tak dikenal pasti aman diklik.|Waspada.
Ciri phishing adalah …|hadiah tidak wajar|pengirim jelas resmi|tata bahasa rapi|tanpa permintaan data|Hadiah.
Jika menerima pesan mencurigakan, sebaiknya …|tidak mengklik dan melaporkan|langsung mengklik|membagikan ke teman|memberi kode OTP|Lapor.
## INF|Kata sandi kuat
Kata sandi kuat panjangnya minimal sekitar … karakter.|12|4|6|2|12.
Kata sandi yang lemah adalah …|123456|frasa panjang dengan simbol|campuran acak 16 karakter|kalimat unik panjang|Lemah.
=|Aplikasi untuk menyimpan banyak kata sandi disebut pengelola kata …|sandi|Pengelola kata sandi.
=|Pengamanan masuk akun dengan dua bukti disebut verifikasi dua …|langkah|Dua langkah.
B|Setiap akun sebaiknya memakai kata sandi berbeda.|Berbeda.
S|Tanggal lahir adalah kata sandi yang kuat.|Mudah ditebak.
Kata sandi kuat memadukan huruf besar, huruf kecil, angka, dan …|simbol|nama sendiri|tanggal lahir|nama hewan|Simbol.
Memakai satu kata sandi untuk semua akun bersifat …|berisiko|sangat aman|wajib|disarankan|Risiko.
## INF|Internet of Things
Singkatan Internet of Things adalah …|IoT|ICT|API|CPU|IoT.
Perangkat IoT dilengkapi … dan terhubung internet.|sensor|kertas|kabel listrik saja|tinta|Sensor.
=|Lampu yang dapat dinyalakan dari HP disebut lampu …|pintar|Pintar.
=|Jam yang mencatat langkah disebut jam tangan …|pintar|Pintar.
B|Perangkat IoT perlu dijaga keamanannya.|Aman.
S|IoT hanya berupa robot berbentuk manusia.|Benda sehari-hari.
Sensor tanah IoT mengukur …|kelembapan|harga|suara musik|warna langit|Kelembapan.
CCTV daring berfungsi …|memantau rumah|memasak|menyiram tanaman|mencuci baju|Pantau.
## INF|Sistem informasi
Sistem informasi mengubah data menjadi …|informasi|sampah|suara|listrik|Informasi.
Komponen sistem informasi yang berupa langkah kerja disebut …|prosedur|data|perangkat keras|jaringan|Prosedur.
=|Struk belanja termasuk … sistem kasir.|keluaran;output|Keluaran.
=|Pemindai kode batang termasuk perangkat …|keras|Perangkat keras.
B|Manusia termasuk komponen sistem informasi.|Manusia.
S|Sistem informasi hanya terdiri atas komputer.|Banyak komponen.
Alur sistem informasi terdiri atas masukan, proses, keluaran, dan …|penyimpanan|pembakaran|penghapusan|pemotongan|Penyimpanan.
Contoh sistem informasi adalah …|sistem informasi akademik|pensil|meja|papan tulis|SIA.
## INF|Big data
Ciri big data yang berarti jumlah sangat besar adalah …|volume|variety|velocity|value|Volume.
Ciri big data yang berarti jenis data beragam adalah …|variety|volume|velocity|veracity|Variety.
=|Ciri big data yang berarti bertambah sangat cepat adalah …|velocity|Velocity.
=|Ciri big data tentang kebenaran data adalah …|veracity|Veracity.
B|Aplikasi peta mengolah big data lalu lintas.|Big data.
S|Big data hanya berarti satu berkas yang ukurannya besar.|Besar, beragam, cepat.
Big data dipakai untuk …|prakiraan cuaca|menghapus semua data|membuat kertas|menulis tangan|Cuaca.
Ciri big data tentang manfaat data adalah …|value|volume|velocity|variety|Value.
## INF|Karier di bidang informatika
Orang yang membuat aplikasi disebut pengembang …|perangkat lunak|perangkat keras saja|bangunan|jalan|Software developer.
Ahli yang melindungi sistem dari serangan disebut ahli keamanan …|siber|pangan|jalan|laut|Siber.
=|Orang yang mengolah data disebut … data.|analis|Analis.
=|Orang yang merancang tampilan aplikasi disebut desainer UI/ …|UX|UX.
B|Karier informatika memerlukan kemampuan berpikir logis.|Logis.
S|Semua pekerjaan informatika hanya pemrogram.|Beragam.
Orang yang mengelola jaringan komputer disebut …|administrator jaringan|desainer grafis|analis data|penulis|Admin.
Orang yang membuat permainan digital disebut pengembang …|gim|jaringan|data|perangkat keras|Gim.
## INF|Inklusi digital
Upaya agar semua orang dapat memakai teknologi disebut …|inklusi digital|kesenjangan digital|jejak digital|enkripsi|Inklusi.
Pembaca layar membantu pengguna …|tunanetra|tunarungu|lansia saja|anak kecil saja|Tunanetra.
=|Perbedaan akses teknologi antarkelompok disebut kesenjangan …|digital|Digital.
=|Teks otomatis pada video membantu pengguna …|tunarungu|Tunarungu.
B|Mode sederhana membantu lansia memakai HP.|Lansia.
S|Semua teknologi digital otomatis dapat dipakai semua orang.|Perlu inklusi.
Penyebab kesenjangan digital adalah perbedaan …|akses internet|warna kulit|hobi|golongan darah|Akses.
Kontras tinggi pada layar membantu pengguna …|buta warna|tunarungu|tunawicara|tunadaksa saja|Kontras.
## INF|Tabel pivot
Fitur untuk meringkas data besar dengan cepat adalah tabel …|pivot|biasa|kosong|acak|Pivot.
Bagian pivot yang berisi angka yang dihitung adalah …|nilai|baris|kolom|filter|Nilai.
=|Bagian pivot untuk menyaring data adalah …|filter|Filter.
=|Tabel pivot dapat menghitung jumlah, banyak data, dan rata- …|rata|Rata-rata.
B|Tabel pivot tidak mengubah data asli.|Asli tetap.
S|Tabel pivot menghapus data asli.|Tetap.
Total penjualan per bulan dapat dibuat dengan …|tabel pivot|menggambar manual|surel|presentasi|Pivot.
Bagian pivot berisi kategori yang dikelompokkan adalah …|baris|nilai|rata-rata|jumlah|Baris.
## INF|Simulasi dan pemodelan
Gambaran sederhana dari sistem nyata disebut …|model|data|algoritma|server|Model.
Menjalankan model untuk melihat hasil dalam berbagai kondisi disebut …|simulasi|enkripsi|kompresi|navigasi|Simulasi.
=|Alat untuk melatih pilot secara aman disebut … penerbangan.|simulator|Simulator.
=|Hasil simulasi bergantung pada … model.|asumsi|Asumsi.
B|Simulasi membantu mencoba tanpa risiko nyata.|Aman.
S|Hasil simulasi pasti sama dengan kenyataan.|Asumsi.
Simulasi gempa membantu merancang …|bangunan aman|lagu|resep|pakaian|Gempa.
Simulasi lalu lintas membantu mengatur …|lampu jalan|harga beras|jadwal sekolah|menu kantin|Lalu lintas.
## INF|CSS untuk tampilan web
CSS adalah bahasa untuk mengatur … halaman web.|tampilan|isi teks|basis data|server|Tampilan.
Properti CSS untuk warna teks adalah …|color|font-size|margin|padding|color.
=|Properti CSS untuk ukuran huruf adalah …|font-size|font-size.
=|Properti CSS untuk warna latar adalah …|background-color|background-color.
B|CSS memisahkan isi dan tampilan.|Pisah.
S|CSS adalah bahasa untuk menyimpan data siswa.|Tampilan.
Properti CSS untuk jarak dalam adalah …|padding|margin|color|border|Padding.
Properti CSS untuk perataan teks adalah …|text-align|font-size|color|margin|text-align.
## INF|Basis data relasional
Kunci yang mengenali setiap baris secara unik disebut …|primary key|foreign key|index|query|Primary.
Kunci yang menghubungkan ke tabel lain disebut …|foreign key|primary key|password|label|Foreign.
=|Bahasa kueri basis data disebut …|SQL|SQL.
=|Perintah SQL untuk mengambil data adalah …|SELECT|SELECT.
B|Basis data relasional mengurangi data ganda.|Relasi.
S|Data siswa sebaiknya ditulis ulang di setiap baris peminjaman.|Relasi.
Hubungan antartabel disebut …|relasi|kolom|baris|kueri|Relasi.
Pada tabel peminjaman, NIS siswa berperan sebagai …|foreign key|primary key tabel buku|judul|tanggal|Foreign.
## INF|Kolaborasi kode dengan Git
Git adalah sistem kendali …|versi|suhu|lalu lintas|listrik|Versi.
Simpanan perubahan dalam Git disebut …|commit|branch|merge|pull|Commit.
=|Cabang pengembangan dalam Git disebut …|branch|Branch.
=|Menggabungkan cabang disebut …|merge|Merge.
B|GitHub memudahkan kolaborasi tim.|GitHub.
S|Menyimpan berkas final, final2, final3 lebih rapi daripada Git.|Git.
Mengirim perubahan ke server disebut …|push|pull|clone|commit|Push.
Tempat menyimpan proyek beserta riwayatnya disebut …|repositori|folder sampah|kalkulator|basis data|Repositori.
## INF|Pengujian perangkat lunak
Pengujian bagian kecil program disebut pengujian …|unit|sistem|penerimaan|integrasi|Unit.
Pengujian keseluruhan aplikasi disebut pengujian …|sistem|unit|nilai batas|regresi|Sistem.
=|Masukan, langkah, dan hasil yang diharapkan disebut kasus …|uji|Kasus uji.
=|Pengujian dengan masukan ekstrem disebut uji nilai …|batas|Batas.
B|Pengujian dilakukan sebelum aplikasi dirilis.|Sebelum.
S|Cukup menguji program dengan masukan yang biasa.|Batas dan tidak valid.
Pengujian untuk memastikan fitur lama tetap berjalan disebut uji …|regresi|unit|batas|integrasi|Regresi.
Pengujian sesuai kebutuhan pengguna disebut pengujian …|penerimaan|unit|regresi|integrasi|Penerimaan.
## INF|Antarmuka pemrograman aplikasi
Singkatan antarmuka pemrograman aplikasi adalah …|API|IoT|CSS|SQL|API.
Permintaan data ke API disebut …|request|response|endpoint|JSON|Request.
=|Tanggapan data dari API disebut …|response|Response.
=|Format data teks yang sering dipakai API adalah …|JSON|JSON.
B|Aplikasi ojek memakai API peta.|API.
S|Setiap aplikasi selalu membuat semua datanya sendiri.|API.
Alamat layanan pada API disebut …|endpoint|request|kunci|server lokal|Endpoint.
Tanda izin untuk memakai API disebut …|kunci API|JSON|response|request|Kunci.
## INF|Pengembangan aplikasi seluler
Sistem operasi untuk aplikasi seluler adalah Android dan …|iOS|Windows Server|Linux Desktop|DOS|iOS.
Aplikasi Android dirilis di …|Google Play|Microsoft Word|Excel|Paint|Play Store.
=|Tahap menulis kode disebut …|pemrograman|Pemrograman.
=|Tahap mengunggah aplikasi ke toko aplikasi disebut …|rilis|Rilis.
B|Tombol aplikasi HP perlu cukup besar untuk jari.|Besar.
S|Aplikasi HP tidak perlu memperhatikan pemakaian baterai.|Hemat.
Tahap menentukan fitur aplikasi disebut analisis …|kebutuhan|risiko|pasar saham|warna|Kebutuhan.
Tahap mencari kesalahan aplikasi disebut …|pengujian|rilis|desain|analisis|Pengujian.
## KKA|Membaca berkas CSV
Pada berkas CSV, kolom dipisahkan dengan …|koma|titik dua|garis bawah|spasi ganda|Koma.
Modul Python untuk membaca CSV adalah …|csv|math|random|os|csv.
=|Ekstensi berkas CSV adalah …|.csv;csv|.csv.
=|Fungsi untuk membaca CSV adalah csv.…|reader|reader.
B|Baris pertama CSV sering berisi judul kolom.|Header.
S|CSV hanya bisa dibuka dengan aplikasi lembar kerja.|Teks.
Kepanjangan CSV adalah Comma Separated …|Values|Versions|Videos|Variables|Values.
CSV memudahkan … data antaraplikasi.|bertukar|menghapus|menyembunyikan|mengenkripsi|Bertukar.
## KKA|Pencarian biner
Pencarian biner hanya dapat dipakai pada data yang …|terurut|acak|kosong|berwarna|Terurut.
Pencarian biner membandingkan nilai yang dicari dengan nilai …|tengah|pertama|terakhir|acak|Tengah.
=|Jika nilai yang dicari lebih kecil dari nilai tengah, cari di setengah …|kiri|Kiri.
=|Untuk 1.000 data, pencarian biner memerlukan sekitar … langkah.|10|10.
B|Pencarian biner lebih cepat dari pencarian linear untuk data besar.|Cepat.
S|Pencarian biner dapat dipakai pada data acak.|Terurut.
Untuk 16 data, pencarian biner memerlukan maksimal … langkah.|4|16|8|2|Log2.
Mencari kata di kamus dengan membuka bagian tengah mirip …|pencarian biner|pencarian linear|pengurutan|enkripsi|Biner.
## KKA|Rekursi
Fungsi yang memanggil dirinya sendiri disebut fungsi …|rekursif|linear|statis|kosong|Rekursif.
Fungsi rekursif harus memiliki kasus …|dasar|acak|ganda|tanpa akhir|Dasar.
=|Nilai 5! adalah …|120|120.
=|Nilai 0! adalah …|1|Satu.
B|Rekursi cocok untuk struktur bertingkat seperti folder.|Folder.
S|Fungsi rekursif tanpa kasus dasar pasti berhenti.|Tidak berhenti.
Nilai 4! adalah …|24|16|12|10|4 × 3 × 2 × 1.
Rumus rekursif faktorial adalah n! = n × …|(n - 1)!|(n + 1)!|n²|2n|Rekursi.
## KKA|Kelas dan objek
Cetak biru dalam pemrograman berorientasi objek disebut …|kelas|objek|metode|atribut|Kelas.
Wujud nyata dari kelas disebut …|objek|atribut|modul|list|Objek.
=|Fungsi di dalam kelas disebut …|metode|Metode.
=|Kata kunci untuk membuat kelas di Python adalah …|class|class.
B|Atribut menyimpan data objek.|Atribut.
S|Kelas dan objek adalah hal yang sama persis.|Berbeda.
Metode inisialisasi kelas di Python bernama …|__init__|start|main|begin|Konstruktor.
Kata self dalam kelas merujuk pada …|objek itu sendiri|kelas lain|modul|berkas|Self.
## KKA|Validasi masukan
Memeriksa data pengguna sebelum dipakai disebut …|validasi|enkripsi|kompresi|rekursi|Validasi.
Pasangan perintah Python untuk menangani error adalah try dan …|except|else saja|for|while|except.
=|Kesalahan saat mengubah teks bukan angka menjadi int disebut …|ValueError|ValueError.
=|Nilai ujian sebaiknya berada pada rentang 0 sampai …|100|100.
B|Alamat surel yang valid berisi tanda @.|Format.
S|Masukan pengguna selalu aman dipakai tanpa diperiksa.|Validasi.
Kata sandi minimal 8 karakter termasuk validasi …|panjang|jenis data|pilihan|rentang angka|Panjang.
Nama yang tidak boleh kosong termasuk validasi …|wajib diisi|format|rentang|jenis|Wajib.
## KKA|Pohon keputusan
Bagian pohon keputusan yang berisi keputusan akhir disebut …|daun|akar|cabang|batang|Daun.
Pertanyaan pertama pada pohon keputusan berada di …|akar|daun|cabang terakhir|tengah|Akar.
=|Bagian yang berisi jawaban pertanyaan disebut …|cabang|Cabang.
=|Pohon keputusan dipakai untuk menentukan kelompok atau …|klasifikasi|Klasifikasi.
B|Pohon keputusan mudah dipahami manusia.|Mudah.
S|Cabang pohon keputusan tidak perlu berakhir pada keputusan.|Daun.
Banyaknya tingkat pertanyaan pohon keputusan disebut …|kedalaman|lebar|daun|akar|Kedalaman.
Pertanyaan "Apakah hujan?" dengan jawaban "bawa payung" berakhir pada …|daun|akar|kedalaman|data uji|Daun.
## KKA|Visualisasi data dengan Python
Pustaka Python untuk membuat grafik adalah …|matplotlib|csv|random|math|matplotlib.
Fungsi untuk grafik batang adalah plt.…|bar|plot|pie|show|bar.
=|Fungsi untuk grafik garis adalah plt.…|plot|plot.
=|Fungsi untuk menampilkan grafik adalah plt.…|show|show.
B|Grafik perlu judul dan label sumbu.|Label.
S|Jenis grafik tidak perlu disesuaikan dengan data.|Sesuai.
Fungsi untuk grafik lingkaran adalah plt.…|pie|bar|plot|title|pie.
Fungsi untuk memberi judul grafik adalah plt.…|title|xlabel|show|bar|title.
## KKA|Proyek kalkulator nilai
Rata-rata nilai dalam list dihitung dengan sum dibagi …|len|max|min|int|len.
Predikat ditentukan dengan perintah …|if-elif|for saja|import|def saja|if-elif.
=|Rata-rata 85 mendapat predikat …|B|B.
=|Rata-rata 92 mendapat predikat …|A|A.
B|Program perlu diuji dengan berbagai masukan.|Uji.
S|Rata-rata dihitung dengan mengalikan total dan banyak data.|Dibagi.
Rata-rata 74 mendapat predikat …|C|B|D|A|C.
Masukan yang bukan angka sebaiknya …|ditolak|dijumlahkan|dikalikan|diabaikan diam-diam|Validasi.
## KKA|Model bahasa besar
Singkatan model bahasa besar dalam bahasa Inggris adalah …|LLM|IoT|API|CPU|LLM.
LLM dilatih dengan sangat banyak …|teks|kayu|logam|air|Teks.
=|LLM bekerja dengan memprediksi kata …|berikutnya|Berikutnya.
=|Jawaban LLM perlu di … kebenarannya.|periksa;cek|Periksa.
B|LLM dapat meringkas artikel panjang.|Ringkas.
S|LLM memahami dunia persis seperti manusia.|Pola.
LLM dapat membantu menerjemahkan …|bahasa|cuaca|batu|makanan|Bahasa.
Pemakaian LLM yang tepat adalah sebagai …|alat bantu belajar|sumber kebenaran mutlak|pengganti guru sepenuhnya|alat mencontek|Alat bantu.
## KKA|Halusinasi KA
Informasi salah yang terdengar meyakinkan dari KA disebut …|halusinasi|enkripsi|validasi|kompresi|Halusinasi.
Halusinasi terjadi karena KA memprediksi …|pola|fakta pasti|cuaca|suara|Pola.
=|Fakta dari KA sebaiknya dicek ke sumber …|terpercaya|Terpercaya.
=|Judul buku yang ternyata tidak ada termasuk sumber …|palsu|Palsu.
B|Meminta rujukan membantu memeriksa jawaban KA.|Rujukan.
S|Semua fakta dari KA pasti benar.|Periksa.
Tanggal peristiwa dari KA sebaiknya dicek di …|buku sejarah|gosip teman|tebakan|mimpi|Buku.
Membandingkan beberapa sumber membantu mendeteksi …|tokoh tertukar|baterai habis|sinyal lemah|layar retak|Bandingkan.
## KKA|KA pembuat gambar
KA pembuat gambar menghasilkan gambar dari perintah …|teks|suara mesin|bau|sentuhan|Teks.
Pemakaian etis KA pembuat gambar adalah …|memberi label buatan KA|membuat hoaks|meniru wajah tanpa izin|mengaku buatan tangan|Etis.
=|Gambar tokoh palsu untuk menyesatkan dapat menyebarkan …|hoaks|Hoaks.
=|Karya seniman harus di …|hormati;hargai|Dihormati.
B|Poster acara kelas berlabel KA termasuk pemakaian etis.|Etis.
S|Semua gambar realistis di internet pasti foto asli.|Bisa KA.
Meniru wajah teman dengan KA tanpa izin melanggar …|privasi|aturan lalu lintas|tata bahasa|rumus|Privasi.
KA pembuat gambar dapat membantu membuat konsep …|desain awal|hoaks|penipuan|plagiat|Desain.
## KKA|Regulasi KA
Aturan pengembangan dan pemakaian KA disebut … KA.|regulasi|halusinasi|algoritma|enkripsi|Regulasi.
Undang-undang Indonesia yang berkaitan dengan data pribadi adalah UU Pelindungan …|Data Pribadi|Konsumen|Lingkungan|Pajak|PDP.
=|Prinsip agar pengguna tahu cara kerja KA disebut …|transparansi|Transparansi.
=|Prinsip agar ada pihak yang bertanggung jawab disebut …|akuntabilitas|Akuntabilitas.
B|Regulasi melindungi masyarakat dari risiko KA.|Lindungi.
S|KA boleh dipakai tanpa aturan apa pun.|Ada aturan.
Prinsip agar KA tidak diskriminatif disebut …|keadilan|keamanan|privasi|transparansi|Adil.
Manusia tetap mengendalikan KA termasuk prinsip …|pengawasan manusia|otomatis penuh|tanpa batas|rahasia|Pengawasan.
## KKA|Keadilan algoritma
Ketidakadilan algoritma sering berasal dari data latih yang …|bias|lengkap|beragam|terbaru|Bias.
Cara mengurangi bias algoritma adalah memakai data yang …|beragam|sedikit|lama|seragam|Beragam.
=|Keputusan otomatis sebaiknya tetap diawasi …|manusia|Manusia.
=|Hasil algoritma perlu diuji untuk setiap …|kelompok|Kelompok.
B|Pengenal wajah dapat kurang akurat jika datanya kurang beragam.|Data.
S|Keputusan mesin selalu netral dan adil.|Bisa bias.
Label data yang keliru sebaiknya …|diperiksa ulang|dibiarkan|ditambah|disembunyikan|Periksa.
Data lama yang tidak sesuai kondisi sekarang sebaiknya …|diperbarui|dipakai terus|dihapus semua|dikunci|Perbarui.
## KKA|KA dalam keamanan siber
KA membantu menyaring surel …|spam|penting saja|keluarga|resmi|Spam.
Bank memakai KA untuk mendeteksi transaksi …|mencurigakan|normal|kecil|harian|Aneh.
=|Program jahat yang dideteksi KA disebut …|malware|Malware.
=|Penjahat dapat memakai KA untuk membuat … yang lebih meyakinkan.|phishing;penipuan|Phishing.
B|Pengguna tetap harus waspada walaupun ada KA.|Waspada.
S|KA hanya dipakai untuk menyerang sistem.|Melindungi juga.
Verifikasi wajah dipakai untuk memastikan … akun.|pemilik|harga|warna|nama aplikasi|Pemilik.
Pemantauan jaringan dengan KA mencari aktivitas …|mencurigakan|hiburan|olahraga|belanja|Mencurigakan.
## KKA|KA dalam kesehatan
KA dapat membantu membaca hasil …|rontgen|ujian|rapor|resep masakan|Rontgen.
Keputusan medis tetap ditentukan oleh …|dokter|aplikasi|teman|iklan|Dokter.
=|Data kesehatan termasuk data …|sensitif|Sensitif.
=|Konsultasi kesehatan jarak jauh disebut …|telemedisin|Telemedisin.
B|KA dapat mempercepat penemuan obat.|Riset.
S|Aplikasi KA dapat sepenuhnya menggantikan dokter.|Membantu.
Prediksi wabah dengan KA membantu …|persiapan layanan kesehatan|menyebarkan penyakit|menutup rumah sakit|menaikkan harga|Persiapan.
Aplikasi pengingat obat membantu pasien …|teratur minum obat|lupa obat|berhenti berobat|membeli obat palsu|Teratur.
## KKA|Belajar cerdas dengan KA
Pemakaian KA yang baik untuk belajar adalah …|meminta penjelasan ulang konsep|menyalin jawaban tugas|memakai saat ujian tanpa izin|mengaku tulisan KA|Baik.
Saat memakai KA untuk belajar, kita tetap harus …|berpikir sendiri|berhenti berpikir|menyalin semua|mempercayai semua|Aktif.
=|Meminta saran perbaikan esai disebut meminta umpan …|balik|Umpan balik.
=|Pemakaian KA di sekolah harus mengikuti … sekolah.|aturan|Aturan.
B|Membuat soal latihan dengan KA membantu berlatih.|Latihan.
S|Menyalin jawaban KA tanpa memahami menguntungkan diri sendiri.|Merugikan.
Memakai KA saat ujian tanpa izin termasuk perbuatan …|curang|jujur|kreatif|terpuji|Curang.
Memeriksa ulang fakta dari KA termasuk sikap …|bertanggung jawab|malas|curang|ceroboh|Tanggung jawab.
"""

SAS += """
## INF 1
0|Dengan sandi Caesar geseran 3, huruf Z menjadi ....|C|A|B|D|Z → C.
1|Pesan "akun diblokir dalam 1 jam" termasuk ciri phishing yang ....|mendesak|resmi|aman|rapi|Mendesak.
2|Campuran acak 16 karakter termasuk kata sandi ....|sangat kuat|sangat lemah|lemah|umum|Kuat.
3|Meteran listrik pintar berfungsi ....|memantau pemakaian listrik|menyalakan kompor|mencuci baju|memasak nasi|IoT.
4|Aplikasi kasir termasuk komponen sistem informasi berupa ....|perangkat lunak|perangkat keras|manusia|prosedur|Software.
5|Penyajian big data agar mudah dipahami disebut ....|visualisasi|volume|velocity|variety|Visualisasi.
6|Orang yang merancang tampilan aplikasi disebut ....|desainer UI/UX|administrator jaringan|analis data|ahli keamanan|UI/UX.
7|Perintah suara membantu pengguna yang ....|kesulitan menyentuh layar|buta warna|lansia saja|tunarungu|Suara.
## INF 2
0|Bagian pivot berupa kategori tambahan disebut ....|kolom|nilai|filter|jumlah|Kolom.
1|Simulasi antrean membantu mengatur ....|kasir|cuaca|gempa|pesawat|Antrean.
2|Properti CSS untuk jarak luar adalah ....|margin|padding|color|font-size|Margin.
3|Kumpulan data sejenis dalam basis data relasional disebut ....|tabel|kueri|relasi|kunci|Tabel.
4|Mengambil perubahan dari server ke komputer disebut ....|pull|push|commit|merge|Pull.
5|Pengujian gabungan beberapa bagian program disebut pengujian ....|integrasi|unit|sistem|penerimaan|Integrasi.
6|Jumlah akses maksimum ke API disebut ....|batas permintaan|endpoint|JSON|response|Batas.
7|Memperbaiki dan menambah fitur setelah rilis disebut ....|pembaruan|analisis|desain|pemrograman|Update.
## KKA 1
0|Baris kedua berkas CSV biasanya berisi ....|data pertama|judul kolom|nama berkas|kode program|Data.
1|Untuk 1.000.000 data, pencarian biner memerlukan sekitar ... langkah.|20|1.000|100|10|Log2.
2|Nilai 3! adalah ....|6|3|9|27|3 × 2 × 1.
3|Pada objek kitty = Kucing("Kitty"), kitty disebut ....|objek|kelas|metode|modul|Objek.
4|Jawaban yang hanya boleh ya atau tidak termasuk validasi ....|pilihan|panjang|format|rentang|Pilihan.
5|Pertanyaan lanjutan dalam pohon keputusan berada pada ....|simpul|daun|akar|kedalaman|Simpul.
6|Fungsi plt.xlabel dipakai untuk ....|label sumbu X|grafik batang|grafik lingkaran|menampilkan grafik|xlabel.
7|Rata-rata 65 mendapat predikat ....|D|C|E|B|D.
## KKA 2
0|Membuat kerangka esai dengan bantuan LLM termasuk kemampuan ....|menulis draf|menerjemahkan|meringkas|membaca rontgen|Draf.
1|Istilah yang dibuat-buat oleh KA sebaiknya dicek di ....|kamus|gosip|iklan|mimpi|Kamus.
2|Mengaku karya KA sebagai buatan tangan termasuk perbuatan ....|tidak jujur|etis|kreatif|terbuka|Tidak jujur.
3|Prinsip agar KA tidak membahayakan pengguna disebut ....|keamanan|transparansi|akuntabilitas|privasi|Keamanan.
4|Tujuan yang terlalu sempit dalam pembuatan algoritma dapat diperbaiki dengan ....|merumuskan tujuan yang adil|menghapus data|menambah bias|menutup pengujian|Tujuan.
5|Phishing buatan KA merupakan contoh KA yang ....|disalahgunakan penjahat|melindungi pengguna|menyaring spam|mendeteksi malware|Disalahgunakan.
6|Asisten rekam medis berbasis KA membantu dokter ....|hemat waktu|mengganti diagnosis|menutup klinik|menaikkan biaya|Hemat.
7|Meminta KA membuat soal latihan lalu mengerjakannya sendiri termasuk cara belajar yang ....|baik|curang|malas|terlarang|Baik.
"""

TOPICS += """
## PAI
# 1|Al-Qur'an, Akidah, dan Fikih
@ Surah Al-Qari'ah
min: 15
act: Baca Surah Al-Qari'ah bersama keluarga, lalu diskusikan arti timbangan amal.
mis: mengira amal baik dan buruk tidak akan ditimbang
exp: Surah Al-Qari'ah adalah surah ke-101 dan terdiri atas 11 ayat. Al-Qari'ah artinya hari kiamat yang menggetarkan. Surah ini menggambarkan manusia seperti laron yang beterbangan dan gunung seperti bulu yang dihambur. Orang yang berat timbangan kebaikannya hidup senang, sedangkan yang ringan timbangannya tempatnya di neraka Hawiyah.
ex: Beramal baik agar timbangan kebaikan berat. // Gunung dihamburkan seperti bulu.
pt: Surah ke-101, terdiri atas 11 ayat ; Al-Qari'ah artinya hari kiamat ; Timbangan amal menentukan balasan
sum: Al-Qari'ah mengingatkan kita memperbanyak amal saleh.
fig: table Hal | Isi ;; nomor surah | 101 ;; jumlah ayat | 11 ;; arti nama surah | hari kiamat yang menggetarkan ;; ayat 4 | manusia seperti laron ;; ayat 5 | gunung seperti bulu ;; ayat 9 | neraka Hawiyah ~ Isi Surah Al-Qari'ah.
read: quran 101:1-11
@ Iman kepada hari akhir
min: 15
act: Tulis lima perbuatan baik yang ingin kamu tingkatkan sebagai bekal hari akhir.
mis: mengira hari akhir hanya cerita tanpa pengaruh pada perilaku
exp: Iman kepada hari akhir adalah rukun iman kelima. Hari akhir adalah hari berakhirnya kehidupan dunia. Tahapannya antara lain kiamat, alam barzakh, yaumul ba'as atau kebangkitan, yaumul mahsyar atau pengumpulan, yaumul hisab atau perhitungan amal, mizan atau timbangan, dan surga atau neraka. Iman ini mendorong manusia berbuat baik.
ex: Setiap amal akan dihisab. // Alam barzakh adalah alam kubur.
pt: Rukun iman kelima ; Barzakh, ba'as, mahsyar, hisab, mizan ; Mendorong berbuat baik
sum: Iman kepada hari akhir membuat kita berhati-hati dalam berbuat.
fig: table Tahapan | Arti ;; alam barzakh | alam kubur ;; yaumul ba'as | hari kebangkitan ;; yaumul mahsyar | hari pengumpulan ;; yaumul hisab | hari perhitungan amal ;; mizan | timbangan amal ;; sirat | jembatan menuju surga ~ Tahapan hari akhir.
@ Iman kepada qada dan qadar
min: 15
act: Ingat satu kejadian yang tidak sesuai harapan, lalu tulis hikmah yang kamu dapat.
mis: mengira takdir membuat manusia tidak perlu berusaha
exp: Iman kepada qada dan qadar adalah rukun iman keenam. Qada adalah ketetapan Allah sejak zaman azali, sedangkan qadar adalah perwujudan ketetapan itu. Takdir mubram tidak dapat diubah, misalnya kematian. Takdir muallaq dapat berubah dengan usaha dan doa, misalnya kepandaian. Sikap yang benar adalah ikhtiar, doa, lalu tawakal.
ex: Belajar giat untuk meraih nilai baik (ikhtiar). // Menerima hasil dengan sabar (tawakal).
pt: Rukun iman keenam ; Takdir mubram dan muallaq ; Ikhtiar, doa, tawakal
sum: Iman kepada takdir membuat kita tetap berusaha dan tenang.
fig: table Istilah | Arti ;; qada | ketetapan Allah sejak azali ;; qadar | perwujudan ketetapan ;; takdir mubram | tidak dapat diubah ;; takdir muallaq | dapat berubah dengan usaha ;; ikhtiar | berusaha sungguh-sungguh ;; tawakal | berserah diri setelah berusaha ~ Istilah qada dan qadar.
@ Merawat jenazah
min: 15
act: Tanyakan kepada pengurus masjid urutan merawat jenazah di lingkunganmu.
mis: mengira merawat jenazah adalah fardu ain bagi setiap orang
exp: Merawat jenazah muslim hukumnya fardu kifayah, yaitu kewajiban bersama yang gugur jika sudah dilakukan sebagian orang. Kewajiban terhadap jenazah ada empat: memandikan, mengafani, menyalatkan, dan menguburkan. Jenazah dimandikan dengan air bersih, dikafani dengan kain putih, disalatkan, lalu dikuburkan menghadap kiblat.
ex: Jenazah laki-laki dikafani tiga lapis kain. // Jenazah dikuburkan menghadap kiblat.
pt: Fardu kifayah ; Memandikan, mengafani, menyalatkan, menguburkan ; Kain kafan putih
sum: Merawat jenazah adalah wujud penghormatan terakhir.
fig: table Kewajiban | Keterangan ;; memandikan | dengan air bersih ;; mengafani | kain putih ;; menyalatkan | salat jenazah ;; menguburkan | menghadap kiblat ;; kafan laki-laki | tiga lapis ;; kafan perempuan | lima lembar ~ Kewajiban terhadap jenazah.
@ Salat jenazah
min: 15
act: Hafalkan bacaan setelah takbir kedua salat jenazah dengan bimbingan orang tua.
mis: melakukan rukuk dan sujud saat salat jenazah
exp: Salat jenazah dilakukan dengan empat takbir tanpa rukuk dan sujud. Setelah takbir pertama membaca Al-Fatihah, setelah takbir kedua membaca selawat, setelah takbir ketiga mendoakan jenazah, dan setelah takbir keempat mendoakan jenazah dan yang ditinggalkan, lalu salam. Salat jenazah dilakukan dengan berdiri.
ex: Takbir pertama diikuti Al-Fatihah. // Salat jenazah diakhiri salam.
pt: Empat takbir ; Tanpa rukuk dan sujud ; Al-Fatihah, selawat, doa
sum: Salat jenazah adalah doa bagi saudara yang wafat.
fig: table Takbir | Bacaan sesudahnya ;; pertama | Al-Fatihah ;; kedua | selawat Nabi ;; ketiga | doa untuk jenazah ;; keempat | doa untuk jenazah dan keluarga ;; penutup | salam ;; posisi | berdiri ~ Urutan salat jenazah.
@ Semangat menuntut ilmu
min: 15
act: Buat target belajar satu keterampilan baru dalam sebulan dan catat kemajuannya.
mis: mengira menuntut ilmu hanya kewajiban di sekolah
exp: Menuntut ilmu adalah kewajiban setiap muslim. Allah mengangkat derajat orang beriman dan berilmu, sebagaimana dalam Surah Al-Mujadalah ayat 11. Ilmu dicari sepanjang hayat, dari buaian sampai liang lahat. Adab menuntut ilmu antara lain niat ikhlas, menghormati guru, tekun, dan mengamalkan ilmu.
ex: Membaca buku di perpustakaan. // Mengajarkan kembali ilmu kepada adik.
pt: Kewajiban setiap muslim ; Derajat orang berilmu diangkat ; Sepanjang hayat
sum: Ilmu yang bermanfaat membawa kebaikan dunia dan akhirat.
fig: table Adab | Contoh ;; niat ikhlas | belajar karena Allah ;; hormat guru | mendengarkan dengan baik ;; tekun | rajin mengulang pelajaran ;; rendah hati | tidak sombong dengan ilmu ;; mengamalkan | menerapkan ilmu ;; mengajarkan | berbagi ilmu ~ Adab menuntut ilmu.
# 2|Akhlak, Muamalah, dan Sejarah
@ Surah Al-Lahab
min: 15
act: Baca Surah Al-Lahab, lalu diskusikan pelajaran tentang menentang kebenaran.
mis: mengira harta dapat menyelamatkan dari azab
exp: Surah Al-Lahab adalah surah ke-111 dan terdiri atas 5 ayat. Al-Lahab artinya gejolak api. Surah ini menceritakan Abu Lahab dan istrinya yang memusuhi dakwah Nabi Muhammad saw. Harta dan usaha Abu Lahab tidak berguna untuk menyelamatkannya. Pelajarannya adalah tidak memusuhi kebenaran dan tidak sombong dengan harta.
ex: Abu Lahab adalah paman Nabi yang memusuhi dakwah. // Harta tidak menyelamatkan orang yang ingkar.
pt: Surah ke-111, terdiri atas 5 ayat ; Al-Lahab artinya gejolak api ; Harta tidak menyelamatkan
sum: Al-Lahab mengajarkan untuk menerima kebenaran.
fig: table Hal | Isi ;; nomor surah | 111 ;; jumlah ayat | 5 ;; arti nama surah | gejolak api ;; tokoh | Abu Lahab ;; ayat 2 | harta tidak berguna ;; ayat 4 | istrinya pembawa kayu bakar ~ Isi Surah Al-Lahab.
read: quran 111:1-5
@ Qanaah dan zuhud
min: 15
act: Catat keinginan belanja selama seminggu, lalu pilah mana kebutuhan dan mana keinginan.
mis: mengira zuhud berarti tidak boleh memiliki harta
exp: Qanaah artinya merasa cukup dan menerima rezeki dari Allah dengan rela setelah berusaha. Zuhud artinya tidak terlalu mencintai dunia sehingga hati tidak diperbudak harta, walaupun tetap bekerja dan boleh memiliki harta. Lawan qanaah adalah tamak atau rakus. Qanaah membuat hidup tenang.
ex: Bersyukur dengan uang saku yang ada. // Memakai barang sampai benar-benar rusak.
pt: Qanaah merasa cukup ; Zuhud tidak diperbudak dunia ; Lawannya tamak
sum: Qanaah dan zuhud membuat hati tenteram.
fig: table Sikap | Contoh ;; qanaah | bersyukur dengan uang saku ;; zuhud | tidak sombong dengan harta ;; tamak | ingin semua barang teman ;; boros | membeli barang tak perlu ;; hemat | menabung sisa uang ;; sederhana | tidak pamer ~ Sikap terhadap harta.
@ Jual beli dalam Islam
min: 15
act: Amati transaksi di warung, lalu tentukan rukun jual beli yang terpenuhi.
mis: mengira jual beli sah walaupun barangnya tidak jelas
exp: Jual beli adalah pertukaran barang dengan uang atas dasar suka sama suka. Rukun jual beli meliputi penjual dan pembeli, barang yang diperjualbelikan, alat tukar, dan ijab kabul. Syarat barang antara lain suci, bermanfaat, milik penjual, dan jelas. Jual beli dilarang jika mengandung penipuan, barang haram, atau curang dalam timbangan.
ex: Penjual menimbang dengan jujur. // Menjual barang curian tidak sah.
pt: Suka sama suka ; Penjual, pembeli, barang, ijab kabul ; Dilarang menipu dan curang
sum: Jual beli yang jujur membawa berkah.
fig: table Rukun jual beli | Contoh ;; penjual | pemilik warung ;; pembeli | siswa ;; barang | buku tulis ;; alat tukar | uang ;; ijab | saya jual ;; kabul | saya beli ~ Rukun jual beli.
@ Larangan riba
min: 15
act: Diskusikan dengan orang tua contoh pinjaman yang memberatkan karena bunga berlipat.
mis: mengira tambahan pembayaran pinjaman selalu diperbolehkan
exp: Riba adalah tambahan yang disyaratkan dalam utang piutang atau pertukaran barang sejenis secara tidak adil. Islam mengharamkan riba karena merugikan dan memberatkan pihak yang lemah. Islam menganjurkan pinjaman kebaikan atau qardul hasan, jual beli yang adil, dan kerja sama bagi hasil.
ex: Meminjamkan uang tanpa meminta tambahan. // Pinjaman berbunga tinggi memberatkan peminjam.
pt: Tambahan tidak adil dalam utang ; Diharamkan karena memberatkan ; Qardul hasan dan bagi hasil
sum: Menjauhi riba menjaga keadilan ekonomi.
fig: table Istilah | Arti ;; riba | tambahan tidak adil ;; qardul hasan | pinjaman kebaikan ;; mudarabah | kerja sama bagi hasil ;; utang piutang | pinjam meminjam ;; bagi hasil | keuntungan dibagi sesuai kesepakatan ;; sedekah | pemberian tanpa balasan ~ Istilah muamalah.
@ Sedekah, hibah, dan hadiah
min: 15
act: Sisihkan sebagian uang saku untuk sedekah selama seminggu.
mis: mengira sedekah hanya berupa uang
exp: Sedekah adalah pemberian kepada orang lain dengan ikhlas untuk mengharap rida Allah, dapat berupa harta, tenaga, atau senyuman. Hibah adalah pemberian harta kepada orang lain tanpa imbalan semasa hidup. Hadiah adalah pemberian sebagai tanda kasih sayang atau penghargaan. Ketiganya mempererat persaudaraan.
ex: Tersenyum kepada teman termasuk sedekah. // Memberi hadiah kepada sahabat yang berulang tahun.
pt: Sedekah mengharap rida Allah ; Hibah tanpa imbalan ; Hadiah tanda kasih sayang
sum: Memberi dengan ikhlas mempererat persaudaraan.
fig: table Pemberian | Tujuan ;; sedekah | mengharap rida Allah ;; hibah | pemberian harta tanpa imbalan ;; hadiah | tanda kasih sayang ;; zakat | kewajiban harta ;; infak | membelanjakan harta di jalan Allah ;; wakaf | harta untuk kepentingan umum ~ Jenis pemberian dalam Islam.
@ Peran ulama dalam kemerdekaan
min: 15
act: Cari tokoh ulama dari daerahmu yang berjuang melawan penjajah.
mis: mengira perjuangan kemerdekaan tidak melibatkan ulama dan santri
exp: Ulama dan santri berperan besar dalam perjuangan kemerdekaan Indonesia. K.H. Hasyim Asy'ari mengeluarkan Resolusi Jihad pada 22 Oktober 1945 yang membakar semangat pertempuran 10 November di Surabaya. Tanggal 22 Oktober kemudian diperingati sebagai Hari Santri. Tokoh lain antara lain K.H. Ahmad Dahlan dan K.H. Zainal Mustafa.
ex: Resolusi Jihad mendorong rakyat mempertahankan kemerdekaan. // Hari Santri diperingati setiap 22 Oktober.
pt: Ulama dan santri berjuang ; Resolusi Jihad 22 Oktober 1945 ; Hari Santri
sum: Ulama menanamkan semangat cinta tanah air.
fig: table Tokoh | Peran ;; K.H. Hasyim Asy'ari | Resolusi Jihad ;; K.H. Ahmad Dahlan | pendiri Muhammadiyah ;; K.H. Wahid Hasyim | anggota BPUPKI ;; K.H. Zainal Mustafa | melawan Jepang ;; Ki Bagus Hadikusumo | perumus dasar negara ;; Buya Hamka | ulama dan sastrawan ~ Ulama dalam perjuangan bangsa.

## SUN
# 1|Sastra jeung Seni Sunda
@ Maca sajak
min: 15
act: Baca hiji sajak Sunda di hareupeun kulawarga kalawan lentong anu merenah.
mis: membaca sajak dengan suara datar tanpa ekspresi
exp: Sajak adalah puisi bebas dalam bahasa Sunda yang tidak terikat jumlah suku kata dan rima. Membaca sajak perlu memperhatikan lafal atau ucapan yang jelas, lentong atau intonasi, wirahma atau irama, dan ekspresi wajah. Sajak Sunda modern dipelopori antara lain oleh Kis WS.
ex: Lentong naék dina kalimah pananya. // Ekspresi sedih dina sajak kasedih.
pt: Puisi bébas ; Lafal, lentong, wirahma, ekspresi ; Dipelopori Kis WS
sum: Maca sajak anu hadé nepikeun rasa ka pangdéngé.
fig: table Unsur maca sajak | Harti ;; lafal | cara ngucapkeun kecap ;; lentong | naék turunna sora ;; wirahma | gancang lalaunna maca ;; ekspresi | rasa dina beungeut ;; artikulasi | jelas sora ;; sikep | gerak awak ~ Unsur maca sajak.
@ Biografi tokoh Sunda
min: 15
act: Tulis biografi pondok salah saurang tokoh Sunda anu dipikawanoh.
mis: menulis biografi dengan kata ganti aku
exp: Biografi adalah tulisan tentang riwayat hidup seseorang yang ditulis orang lain. Isinya meliputi identitas, latar belakang keluarga, pendidikan, perjuangan, dan karya. Tokoh Sunda yang dikenal antara lain Ajip Rosidi (sastrawan), R.A.A. Kusumadilaga, Mang Koko (seniman karawitan), dan Ir. H. Djuanda.
ex: Ajip Rosidi lahir di Jatiwangi taun 1938. // Mang Koko nyiptakeun loba kawih.
pt: Riwayat hirup ditulis batur ; Idéntitas, atikan, karya ; Tokoh Sunda kawentar
sum: Biografi tokoh Sunda mere inspirasi.
fig: table Tokoh | Widang ;; Ajip Rosidi | sastra ;; Mang Koko | karawitan ;; Ir. H. Djuanda | pamaréntahan ;; Dewi Sartika | atikan awéwé ;; Gugum Gumbira | tari Jaipong ;; Darso | pop Sunda ~ Tokoh Sunda.
@ Tembang Cianjuran
min: 15
act: Dengekeun rékaman tembang Cianjuran, tuluy catet waditra anu dipaké.
mis: menganggap tembang Cianjuran sama dengan lagu pop Sunda
exp: Tembang Cianjuran atau mamaos adalah seni vokal Sunda yang berasal dari Cianjur. Tembang ini diiringi kacapi indung, kacapi rincik, dan suling atau rebab. Rumpakanya banyak memakai pupuh dan berisi keindahan alam serta nasihat. Tembang Cianjuran dinyanyikan dengan suara halus dan banyak cengkok.
ex: Kacapi indung jadi pirigan utama. // Suling ngeusian mélodi.
pt: Seni sora ti Cianjur ; Dipirig kacapi jeung suling ; Rumpaka pupuh
sum: Tembang Cianjuran mangrupa seni sora anu luhung.
fig: table Waditra | Fungsi ;; kacapi indung | pirigan utama ;; kacapi rincik | ngeusian wirahma ;; suling | mélodi ;; rebab | mélodi ganti suling ;; juru mamaos | nembang ;; rumpaka | lirik tembang ~ Waditra tembang Cianjuran.
@ Nulis surat pribadi
min: 15
act: Tulis surat pribadi dina basa Sunda ka dulur anu aya di kota séjén.
mis: memakai basa yang terlalu kaku untuk surat kepada sahabat
exp: Surat pribadi adalah surat untuk keluarga atau sahabat dengan bahasa yang akrab. Bagian surat pribadi meliputi titimangsa, alamat atau sapaan, salam pembuka, bubuka, eusi, panutup, salam panutup, dan ngaran pangirim. Basa yang dipakai menyesuaikan dengan penerima, misalnya basa hormat untuk orang tua.
ex: Kahatur Ema di lembur. // Sakitu heula, wassalam.
pt: Surat ka kulawarga atawa sobat ; Titimangsa, bubuka, eusi, panutup ; Basa luyu jeung panarima
sum: Surat pribadi ngadeukeutkeun silaturahmi.
fig: table Bagian surat | Conto ;; titimangsa | Bandung, 5 Désémber ;; sapaan | Kahatur Ema ;; bubuka | nanyakeun kawilujengan ;; eusi | carita atawa béja ;; panutup | sakitu heula ;; ngaran | tanda tangan pangirim ~ Bagian surat pribadi.
@ Laporan kagiatan
min: 15
act: Jieun laporan kagiatan kerja bakti di lingkungan dina basa Sunda.
mis: menulis laporan tanpa menyebut waktu dan tempat kegiatan
exp: Laporan kagiatan adalah tulisan yang melaporkan kegiatan yang sudah dilaksanakan. Isinya meliputi nama kegiatan, waktu, tempat, peserta, jalannya kegiatan, hasil, dan kesimpulan. Bahasa laporan jelas, runtut, dan sesuai fakta.
ex: Kagiatan kerja bakti dilaksanakeun poé Minggu. // Hasilna, susukan jadi beresih.
pt: Ngalaporkeun kagiatan ; Waktu, tempat, jalanna kagiatan ; Basa jelas jeung faktual
sum: Laporan anu runtut gampang dipaham.
fig: table Bagian laporan | Eusi ;; judul | ngaran kagiatan ;; waktu | poé jeung tanggal ;; tempat | lokasi kagiatan ;; pamilon | jalma anu milu ;; jalanna kagiatan | runtuyan acara ;; hasil | kahontal kagiatan ~ Bagian laporan kagiatan.
@ Kalimah dina basa Sunda
min: 15
act: Jieun hiji conto kalimah wawaran, pananya, paréntah, jeung panyeluk.
mis: menulis kalimah pananya tanpa tanda tanya
exp: Kalimah dalam bahasa Sunda dibedakan menurut fungsinya. Kalimah wawaran memberi informasi, kalimah pananya menanyakan sesuatu, kalimah paréntah menyuruh, kalimah panyeluk mengungkapkan perasaan, dan kalimah pangajak mengajak. Setiap kalimah diakhiri tanda baca yang sesuai.
ex: Kuring keur diajar. (wawaran) // Hayu urang ulin! (pangajak)
pt: Wawaran, pananya, paréntah ; Panyeluk jeung pangajak ; Tanda baca luyu
sum: Jenis kalimah ditangtukeun ku fungsina.
fig: table Kalimah | Jenis ;; Kuring keur diajar. | wawaran ;; Rék ka mana? | pananya ;; Tutup pantona! | paréntah ;; Duh, éndahna! | panyeluk ;; Hayu urang ulin! | pangajak ;; Mangga calik. | panyaram atawa sopan ~ Jenis kalimah.
# 2|Budaya jeung Kaarifan Lokal
@ Dongéng fabel
min: 15
act: Caritakeun deui dongéng Sakadang Kuya jeung Sakadang Monyét ka adi.
mis: menganggap fabel tidak mengandung pesan untuk manusia
exp: Dongéng fabel adalah dongeng yang tokohnya binatang yang berperilaku seperti manusia. Fabel Sunda terkenal antara lain Sakadang Kuya jeung Sakadang Monyét serta Sakadang Peucang. Fabel mengandung amanat, misalnya tidak serakah, cerdik, dan jujur. Sebutan sakadang dipakai untuk tokoh binatang.
ex: Monyét anu sarakah antukna rugi. // Peucang anu pinter bisa nyalametkeun manéh.
pt: Tokoh sato kawas jalma ; Sakadang Kuya, Sakadang Peucang ; Ngandung amanat
sum: Fabel ngajarkeun ajén moral ngaliwatan sato.
fig: table Fabel | Amanat ;; Sakadang Kuya jeung Monyét | ulah sarakah ;; Sakadang Peucang | kudu pinter ;; Sakadang Kancil Maling Bonténg | ulah maling ;; Gagak jeung Merak | ulah sombong ;; Kuya jeung Kalinci | ulah ngagampangkeun ;; Sireum jeung Japati | silih tulungan ~ Conto fabel jeung amanatna.
@ Situs sajarah Jawa Barat
min: 15
act: Teangan hiji situs sajarah di Jawa Barat, tuluy jieun poster informasina.
mis: mengira Jawa Barat tidak memiliki candi
exp: Jawa Barat memiliki banyak situs sejarah. Candi Cangkuang di Garut adalah candi Hindu. Prasasti Batutulis di Bogor berkaitan dengan Kerajaan Pajajaran. Situs Gunung Padang di Cianjur adalah situs megalitikum. Keraton Kasepuhan di Cirebon adalah peninggalan Kesultanan Cirebon. Situs sejarah harus dijaga dan tidak dicorat-coret.
ex: Candi Cangkuang aya di tengah situ. // Prasasti Batutulis aya di Bogor.
pt: Candi Cangkuang, Batutulis, Gunung Padang ; Keraton Kasepuhan Cirebon ; Kudu dijaga
sum: Situs sajarah mangrupa warisan anu kudu dimumulé.
fig: table Situs | Lokasi ;; Candi Cangkuang | Garut ;; Prasasti Batutulis | Bogor ;; Situs Gunung Padang | Cianjur ;; Keraton Kasepuhan | Cirebon ;; Astana Gede Kawali | Ciamis ;; Candi Jiwa | Karawang ~ Situs sajarah Jawa Barat.
@ Kaarifan lokal tatanén
min: 15
act: Tanyakeun ka kolot ngeunaan leuit jeung kabiasaan ngajaga paré di lembur.
mis: menganggap cara bertani tradisional tidak memiliki nilai
exp: Masyarakat Sunda memiliki kearifan lokal dalam bertani. Leuit adalah lumbung padi untuk menyimpan cadangan pangan. Ngaseuk adalah menanam padi huma dengan tongkat. Upacara seren taun adalah ungkapan syukur setelah panen. Kampung adat seperti Kasepuhan Ciptagelar menjaga tradisi menanam padi setahun sekali.
ex: Leuit nyimpen paré pikeun usum paceklik. // Seren taun dilaksanakeun sanggeus panén.
pt: Leuit lumbung paré ; Ngaseuk jeung seren taun ; Ciptagelar ngajaga tradisi
sum: Kaarifan lokal tatanén ngajaga katahanan pangan.
fig: table Kaarifan | Harti ;; leuit | lumbung paré ;; ngaseuk | melak paré huma ;; seren taun | sukuran panén ;; nyalin | mitembeyan dibuat ;; huma | kebon paré di darat ;; sawah | lahan paré dicaian ~ Kaarifan lokal tatanén.
@ Karawitan degung
min: 15
act: Dengekeun lagu degung klasik, tuluy sebutkeun waditra anu kadéngé.
mis: menganggap gamelan degung sama dengan gamelan Bali
exp: Degung adalah seni karawitan Sunda yang dimainkan dengan gamelan degung. Waditranya antara lain bonang, saron, panerus, jengglong, goong, kendang, dan suling degung. Degung bernada lembut dan sering dipakai untuk mengiringi upacara pernikahan dan acara resmi. Lagu degung klasik antara lain Palwa dan Sang Bango.
ex: Suling degung maénkeun mélodi. // Degung mirig acara nikahan.
pt: Karawitan Sunda ; Bonang, saron, goong, suling ; Mirig acara resmi
sum: Degung ngagambarkeun kalemesan budaya Sunda.
fig: table Waditra degung | Fungsi ;; bonang | pamurba lagu ;; saron | mélodi pokok ;; jengglong | panganteb ;; goong | panutup wiletan ;; kendang | ngatur wirahma ;; suling degung | ngahias mélodi ~ Waditra gamelan degung.
@ Kalimah langsung jeung teu langsung
min: 15
act: Robah lima kalimah langsung tina paguneman jadi kalimah teu langsung.
mis: tetap memakai tanda petik pada kalimah teu langsung
exp: Kalimah langsung adalah kalimah yang menirukan ucapan seseorang secara langsung dan ditulis di antara tanda petik. Kalimah teu langsung melaporkan ucapan tanpa tanda petik, biasanya memakai kata yén atau sangkan, dan kata ganti disesuaikan. Contohnya Ceuk Ibu, "Kuring rék ka pasar." menjadi Ceuk Ibu, manéhna rék ka pasar.
ex: Budi nyarita, "Kuring lapar." // Budi nyarita yén manéhna lapar.
pt: Langsung maké tanda petik ; Teu langsung tanpa tanda petik ; Maké kecap yén
sum: Kalimah teu langsung nyaritakeun deui omongan batur.
fig: table Kalimah langsung | Kalimah teu langsung ;; "Kuring lapar." | manéhna lapar ;; "Hayu urang diajar!" | ngajak diajar ;; "Ulah ribut!" | sangkan ulah ribut ;; "Kuring rék ka pasar." | rék ka pasar ;; "Kamari kuring gering." | poé saméméhna gering ;; "Ieu buku kuring." | éta bukuna ~ Robahan kalimah langsung.
@ Kampung adat Jawa Barat
min: 15
act: Teangan informasi ngeunaan hiji kampung adat, tuluy tulis aturan adat anu aya di dinya.
mis: menganggap kampung adat menolak semua hal dari luar
exp: Jawa Barat memiliki kampung adat yang menjaga tradisi leluhur. Kampung Naga di Tasikmalaya terkenal dengan rumah adat seragam dan larangan listrik. Baduy di Lebak, Banten, terkenal dengan pikukuh atau aturan adat yang ketat. Kampung Pulo di Garut memiliki enam rumah dan satu musala. Kasepuhan Ciptagelar di Sukabumi terkenal dengan tradisi padi.
ex: Kampung Naga ngajaga imah adat. // Kampung Pulo ngan boga genep imah jeung hiji tajug.
pt: Ngajaga tradisi karuhun ; Kampung Naga, Baduy, Kampung Pulo ; Aturan adat
sum: Kampung adat mangrupa conto hirup luyu jeung alam.
fig: table Kampung adat | Lokasi ;; Kampung Naga | Tasikmalaya ;; Baduy | Lebak ;; Kampung Pulo | Garut ;; Kasepuhan Ciptagelar | Sukabumi ;; Kampung Kuta | Ciamis ;; Kampung Dukuh | Garut kidul ~ Kampung adat Jawa Barat.
"""

BANK += """
## PAI|Surah Al-Qari'ah
Surah Al-Qari'ah adalah surah ke …|101|100|102|99|101.
Jumlah ayat Surah Al-Qari'ah adalah …|11|8|5|9|11.
=|Dalam Surah Al-Qari'ah, manusia diibaratkan seperti …|laron|Laron.
=|Neraka yang disebut dalam Surah Al-Qari'ah adalah …|Hawiyah|Hawiyah.
B|Orang yang berat timbangan kebaikannya hidup senang.|Berat.
S|Amal baik dan buruk tidak akan ditimbang.|Ditimbang.
Dalam Surah Al-Qari'ah, gunung diibaratkan seperti …|bulu yang dihambur|batu besar|air mengalir|api menyala|Ayat 5.
Arti Al-Qari'ah adalah …|hari kiamat yang menggetarkan|gejolak api|kegoncangan|pengumpat|Arti.
## PAI|Iman kepada hari akhir
Iman kepada hari akhir adalah rukun iman ke …|lima|empat|enam|tiga|Kelima.
Alam kubur disebut juga alam …|barzakh|mahsyar|hisab|mizan|Barzakh.
=|Hari perhitungan amal disebut yaumul …|hisab|Hisab.
=|Timbangan amal disebut …|mizan|Mizan.
B|Yaumul ba'as adalah hari kebangkitan.|Ba'as.
S|Iman kepada hari akhir tidak berpengaruh pada perilaku.|Mendorong.
Hari pengumpulan seluruh manusia disebut yaumul …|mahsyar|hisab|ba'as|barzakh|Mahsyar.
Jembatan menuju surga disebut …|sirat|mizan|barzakh|mahsyar|Sirat.
## PAI|Iman kepada qada dan qadar
Iman kepada qada dan qadar adalah rukun iman ke …|enam|lima|empat|tiga|Keenam.
Takdir yang tidak dapat diubah disebut takdir …|mubram|muallaq|ikhtiar|tawakal|Mubram.
=|Takdir yang dapat berubah dengan usaha disebut takdir …|muallaq|Muallaq.
=|Berserah diri setelah berusaha disebut …|tawakal|Tawakal.
B|Kepandaian termasuk takdir yang dapat diubah dengan usaha.|Muallaq.
S|Karena ada takdir, manusia tidak perlu berusaha.|Ikhtiar.
Ketetapan Allah sejak zaman azali disebut …|qada|qadar|ikhtiar|tawakal|Qada.
Urutan sikap yang benar adalah …|ikhtiar, doa, tawakal|tawakal, diam, doa|doa saja|diam saja|Urutan.
## PAI|Merawat jenazah
Hukum merawat jenazah muslim adalah …|fardu kifayah|fardu ain|sunah|mubah|Kifayah.
Kewajiban terhadap jenazah berjumlah …|empat|tiga|lima|dua|Empat.
=|Kain pembungkus jenazah disebut kain …|kafan|Kafan.
=|Jenazah dikuburkan menghadap …|kiblat|Kiblat.
B|Jenazah laki-laki dikafani tiga lapis kain.|Tiga.
S|Merawat jenazah adalah fardu ain bagi setiap orang.|Kifayah.
Kafan untuk jenazah perempuan berjumlah …|lima lembar|tiga lembar|satu lembar|tujuh lembar|Lima.
Jenazah dimandikan dengan air …|bersih|kotor|berwarna|panas mendidih|Bersih.
## PAI|Salat jenazah
Salat jenazah dilakukan dengan … takbir.|empat|tiga|dua|lima|Empat.
Setelah takbir pertama salat jenazah dibaca …|Al-Fatihah|selawat|doa jenazah|salam|Al-Fatihah.
=|Setelah takbir kedua salat jenazah dibaca …|selawat|Selawat.
=|Salat jenazah diakhiri dengan …|salam|Salam.
B|Salat jenazah dilakukan dengan berdiri.|Berdiri.
S|Salat jenazah memakai rukuk dan sujud.|Tanpa.
Setelah takbir ketiga dibaca doa untuk …|jenazah|diri sendiri|guru|tetangga|Jenazah.
Setelah takbir keempat dibaca doa untuk jenazah dan …|keluarga yang ditinggalkan|pedagang|penguasa|musafir|Keluarga.
## PAI|Semangat menuntut ilmu
Menuntut ilmu hukumnya … bagi setiap muslim.|wajib|makruh|mubah|haram|Wajib.
Ayat tentang Allah mengangkat derajat orang berilmu terdapat dalam Surah …|Al-Mujadalah ayat 11|Al-Fatihah ayat 1|Al-Ikhlas ayat 1|An-Nas ayat 1|Al-Mujadalah.
=|Ilmu dicari sepanjang …|hayat|Hayat.
=|Adab menuntut ilmu dimulai dengan niat yang …|ikhlas|Ikhlas.
B|Mengajarkan ilmu kepada orang lain termasuk adab berilmu.|Berbagi.
S|Menuntut ilmu hanya kewajiban selama di sekolah.|Sepanjang hayat.
Rajin mengulang pelajaran mencerminkan sikap …|tekun|malas|sombong|lalai|Tekun.
Ilmu yang baik adalah ilmu yang …|diamalkan|disimpan sendiri|dipamerkan|dilupakan|Amal.
## PAI|Surah Al-Lahab
Surah Al-Lahab adalah surah ke …|111|110|112|101|111.
Jumlah ayat Surah Al-Lahab adalah …|5|4|6|11|5.
=|Arti Al-Lahab adalah gejolak …|api|Api.
=|Tokoh yang diceritakan dalam Surah Al-Lahab adalah Abu …|Lahab|Abu Lahab.
B|Harta Abu Lahab tidak menyelamatkannya.|Ayat 2.
S|Abu Lahab adalah pendukung dakwah Nabi.|Memusuhi.
Istri Abu Lahab digambarkan sebagai pembawa …|kayu bakar|air|bunga|makanan|Ayat 4.
Pelajaran Surah Al-Lahab adalah tidak memusuhi …|kebenaran|teman baik|orang tua|guru|Kebenaran.
## PAI|Qanaah dan zuhud
Qanaah artinya …|merasa cukup|rakus|boros|sombong|Qanaah.
Lawan qanaah adalah …|tamak|zuhud|sabar|syukur|Tamak.
=|Tidak diperbudak oleh dunia disebut …|zuhud|Zuhud.
=|Membeli barang yang tidak perlu termasuk sikap …|boros|Boros.
B|Zuhud tetap boleh bekerja dan memiliki harta.|Boleh.
S|Zuhud berarti tidak boleh memiliki harta sama sekali.|Boleh.
Bersyukur dengan uang saku yang ada mencerminkan sikap …|qanaah|tamak|boros|riya|Qanaah.
Qanaah membuat hidup …|tenang|gelisah|serakah|iri|Tenang.
## PAI|Jual beli dalam Islam
Jual beli dilakukan atas dasar …|suka sama suka|paksaan|ancaman|tipuan|Rela.
Ucapan penjual "saya jual" disebut …|ijab|kabul|riba|hibah|Ijab.
=|Ucapan pembeli "saya beli" disebut …|kabul|Kabul.
=|Uang dalam jual beli berfungsi sebagai alat …|tukar|Alat tukar.
B|Penjual harus menimbang dengan jujur.|Jujur.
S|Menjual barang curian tetap sah.|Bukan milik.
Syarat barang yang dijual adalah …|milik penjual|barang curian|barang haram|tidak jelas|Milik.
Jual beli dilarang jika mengandung …|penipuan|kejujuran|kerelaan|ijab kabul|Penipuan.
## PAI|Larangan riba
Tambahan tidak adil dalam utang piutang disebut …|riba|hibah|sedekah|zakat|Riba.
Pinjaman kebaikan tanpa tambahan disebut …|qardul hasan|riba|mudarabah|wakaf|Qardul hasan.
=|Kerja sama bagi hasil disebut …|mudarabah|Mudarabah.
=|Hukum riba dalam Islam adalah …|haram|Haram.
B|Riba memberatkan pihak yang lemah.|Memberatkan.
S|Semua tambahan pembayaran pinjaman diperbolehkan.|Riba.
Meminjamkan uang tanpa meminta tambahan termasuk …|qardul hasan|riba|tamak|curang|Qardul hasan.
Dalam bagi hasil, keuntungan dibagi sesuai …|kesepakatan|kehendak satu pihak|undian|paksaan|Sepakat.
## PAI|Sedekah, hibah, dan hadiah
Pemberian untuk mengharap rida Allah disebut …|sedekah|hadiah|upah|pinjaman|Sedekah.
Pemberian harta tanpa imbalan semasa hidup disebut …|hibah|riba|utang|zakat|Hibah.
=|Pemberian sebagai tanda kasih sayang disebut …|hadiah|Hadiah.
=|Harta untuk kepentingan umum yang tidak boleh dijual disebut …|wakaf|Wakaf.
B|Tersenyum kepada teman termasuk sedekah.|Senyum.
S|Sedekah hanya boleh berupa uang.|Banyak bentuk.
Membelanjakan harta di jalan Allah disebut …|infak|riba|tamak|boros|Infak.
Pemberian yang hukumnya wajib atas harta tertentu adalah …|zakat|hadiah|hibah|sedekah sunah|Zakat.
## PAI|Peran ulama dalam kemerdekaan
Resolusi Jihad dikeluarkan oleh K.H. …|Hasyim Asy'ari|Ahmad Dahlan|Zainal Mustafa|Wahid Hasyim|Hasyim Asy'ari.
Hari Santri diperingati setiap tanggal …|22 Oktober|10 November|17 Agustus|28 Oktober|22 Oktober.
=|Resolusi Jihad membakar semangat pertempuran 10 November di kota …|Surabaya|Surabaya.
=|Pendiri Muhammadiyah adalah K.H. Ahmad …|Dahlan|Dahlan.
B|Ulama dan santri berperan dalam perjuangan kemerdekaan.|Berperan.
S|Perjuangan kemerdekaan tidak melibatkan ulama.|Melibatkan.
K.H. Wahid Hasyim menjadi anggota …|BPUPKI|KPU|DPR|OSIS|BPUPKI.
Ulama yang juga sastrawan terkenal adalah …|Buya Hamka|Ki Bagus Hadikusumo|K.H. Zainal Mustafa|K.H. Ahmad Dahlan|Hamka.
## SUN|Maca sajak
Sajak nyaéta puisi … dina basa Sunda.|bébas|kauger pupuh|dongéng|wawacan|Bébas.
Naék turunna sora waktu maca sajak disebut …|lentong|lafal|wirahma|ekspresi|Lentong.
=|Cara ngucapkeun kecap disebut …|lafal|Lafal.
=|Gancang lalaunna maca sajak disebut …|wirahma|Wirahma.
B|Ekspresi beungeut penting waktu maca sajak.|Ekspresi.
S|Sajak hadé dibaca kalayan sora datar tanpa rasa.|Ekspresi.
Panaratas sajak Sunda modéren nyaéta …|Kis WS|Ajip Rosidi|D.K. Ardiwinata|Mang Koko|Kis WS.
Gerak awak waktu maca sajak disebut …|sikep|lafal|lentong|wirahma|Sikep.
## SUN|Biografi tokoh Sunda
Biografi nyaéta tulisan ngeunaan … hiji jalma.|riwayat hirup|harga barang|cuaca|resép|Riwayat.
Biografi ditulis ku …|batur|tokoh sorangan|mesin|sato|Batur.
=|Mang Koko kawentar dina widang …|karawitan|Karawitan.
=|Ajip Rosidi kawentar dina widang …|sastra|Sastra.
B|Biografi ngawengku atikan jeung karya tokoh.|Eusi.
S|Biografi ditulis maké kecap gaganti kuring.|Batur.
Gugum Gumbira kawentar nyiptakeun tari …|Jaipong|Saman|Kecak|Piring|Jaipong.
Ajip Rosidi lahir di …|Jatiwangi|Bandung|Garut|Bogor|Jatiwangi.
## SUN|Tembang Cianjuran
Tembang Cianjuran disebut ogé …|mamaos|kawih|degung|calung|Mamaos.
Tembang Cianjuran asalna ti …|Cianjur|Cirebon|Garut|Bogor|Cianjur.
=|Pirigan utama tembang Cianjuran nyaéta kacapi …|indung|Kacapi indung.
=|Waditra tiup dina tembang Cianjuran nyaéta …|suling|Suling.
B|Rumpaka tembang Cianjuran loba maké pupuh.|Pupuh.
S|Tembang Cianjuran sarua jeung lagu pop Sunda.|Béda.
Waditra anu bisa ngaganti suling dina tembang Cianjuran nyaéta …|rebab|kendang|goong|angklung|Rebab.
Jalma anu nembang Cianjuran disebut juru …|mamaos|dalang|pantun|sinden wayang|Juru mamaos.
## SUN|Nulis surat pribadi
Surat pribadi ditujukeun ka …|kulawarga atawa sobat|kantor pamaréntah|perusahaan|sakola resmi|Pribadi.
Tempat jeung tanggal surat disebut …|titimangsa|perkawis|lampiran|kop|Titimangsa.
=|Bagian surat anu nanyakeun kawilujengan disebut …|bubuka|Bubuka.
=|Kecap panutup surat anu umum nyaéta sakitu …|heula|Sakitu heula.
B|Basa surat pribadi kudu luyu jeung panarima.|Luyu.
S|Surat ka sobat kudu maké basa anu kaku pisan.|Akrab.
Kahatur Ema kaasup bagian …|sapaan|panutup|eusi|ngaran|Sapaan.
Bagian surat anu eusina carita atawa béja disebut …|eusi|bubuka|titimangsa|panutup|Eusi.
## SUN|Laporan kagiatan
Laporan kagiatan ngalaporkeun kagiatan anu …|geus dilaksanakeun|can kajadian|ngan rencana|lamunan|Geus.
Basa laporan kudu … jeung runtut.|jelas|hésé|kasar|panjang teuing|Jelas.
=|Jalma anu milu kagiatan disebut …|pamilon|Pamilon.
=|Kahontal kagiatan ditulis dina bagian …|hasil|Hasil.
B|Laporan kudu luyu jeung fakta.|Fakta.
S|Laporan kagiatan teu kudu nyebutkeun waktu jeung tempat.|Kudu.
Runtuyan acara ditulis dina bagian …|jalanna kagiatan|judul|pamilon|tempat|Jalanna.
Ngaran kagiatan ditulis dina bagian …|judul|hasil|tempat|waktu|Judul.
## SUN|Kalimah dina basa Sunda
Kalimah anu mere informasi disebut kalimah …|wawaran|pananya|paréntah|panyeluk|Wawaran.
Kalimah anu nanyakeun hiji hal disebut kalimah …|pananya|wawaran|pangajak|paréntah|Pananya.
=|Kalimah anu nyuruh disebut kalimah …|paréntah|Paréntah.
=|Kalimah anu ngajak disebut kalimah …|pangajak|Pangajak.
B|Kalimah pananya ditungtungan ku tanda tanya.|Tanda tanya.
S|Duh, éndahna! kaasup kalimah pananya.|Panyeluk.
Kalimah anu ngébréhkeun rasa disebut kalimah …|panyeluk|wawaran|pananya|paréntah|Panyeluk.
Kuring keur diajar. kaasup kalimah …|wawaran|pananya|pangajak|panyeluk|Wawaran.
## SUN|Dongéng fabel
Dongéng fabel palakuna …|sato|jalma wungkul|tutuwuhan wungkul|batu|Sato.
Sebutan pikeun tokoh sato dina dongéng Sunda nyaéta …|sakadang|aki|nini|juragan|Sakadang.
=|Amanat Sakadang Kuya jeung Monyét nyaéta ulah …|sarakah|Sarakah.
=|Fabel Sunda anu tokohna peucang nyaéta Sakadang …|Peucang|Peucang.
B|Fabel ngandung amanat pikeun manusa.|Amanat.
S|Fabel teu boga pesen naon-naon.|Amanat.
Amanat fabel Sireum jeung Japati nyaéta …|silih tulungan|ulah diajar|sarakah|sombong|Tulung.
Amanat fabel Gagak jeung Merak nyaéta ulah …|sombong|daék digawé|jujur|bageur|Sombong.
## SUN|Situs sajarah Jawa Barat
Candi Cangkuang aya di …|Garut|Bogor|Cirebon|Cianjur|Garut.
Prasasti Batutulis aya di …|Bogor|Garut|Ciamis|Karawang|Bogor.
=|Situs megalitikum Gunung Padang aya di …|Cianjur|Cianjur.
=|Keraton Kasepuhan aya di …|Cirebon|Cirebon.
B|Situs sajarah kudu dijaga.|Jaga.
S|Jawa Barat teu boga candi.|Cangkuang.
Astana Gede Kawali aya di …|Ciamis|Garut|Bogor|Karawang|Ciamis.
Candi Jiwa aya di …|Karawang|Ciamis|Garut|Cianjur|Karawang.
## SUN|Kaarifan lokal tatanén
Lumbung paré urang Sunda disebut …|leuit|saung|imah|tajug|Leuit.
Upacara sukuran sanggeus panén disebut …|seren taun|ngaseuk|nyalin|ruwatan|Seren taun.
=|Melak paré huma ku iteuk disebut …|ngaseuk|Ngaseuk.
=|Kebon paré di darat disebut …|huma|Huma.
B|Leuit nyimpen paré pikeun usum paceklik.|Cadangan.
S|Tatanén tradisional teu boga ajén naon-naon.|Ajén.
Kasepuhan anu ngajaga tradisi paré aya di …|Ciptagelar|Bandung kota|Jakarta|Bekasi|Ciptagelar.
Lahan paré anu dicaian disebut …|sawah|huma|leuit|kebon|Sawah.
## SUN|Karawitan degung
Gamelan degung kaasup seni …|karawitan|tari|rupa|sastra|Karawitan.
Waditra degung anu jadi pamurba lagu nyaéta …|bonang|goong|kendang|jengglong|Bonang.
=|Waditra anu ngatur wirahma nyaéta …|kendang|Kendang.
=|Waditra tiup dina degung nyaéta suling …|degung|Suling degung.
B|Degung sok mirig acara nikahan.|Nikahan.
S|Gamelan degung sarua jeung gamelan Bali.|Béda.
Waditra degung anu panutup wiletan nyaéta …|goong|saron|bonang|suling|Goong.
Conto lagu degung klasik nyaéta …|Palwa|Bubuy Bulan pop|Cingcangkeling|Manuk Dadali|Palwa.
## SUN|Kalimah langsung jeung teu langsung
Kalimah langsung ditulis di antara tanda …|petik|tanya|seru|kurung|Petik.
Kalimah teu langsung sok maké kecap …|yén|jeung|atawa|tapi|Yén.
=|Kalimah anu nyaritakeun deui omongan tanpa tanda petik disebut kalimah teu …|langsung|Teu langsung.
=|Budi nyarita, "Kuring lapar." Jadi teu langsung: Budi nyarita yén manéhna …|lapar|Lapar.
B|Dina kalimah teu langsung, kecap gaganti disaluyukeun.|Gaganti.
S|Kalimah teu langsung tetep maké tanda petik.|Tanpa.
Kecap kuring dina kalimah langsung robah jadi … dina kalimah teu langsung.|manéhna|urang|aranjeun|kami|Manéhna.
Kecap kamari dina kalimah langsung bisa robah jadi …|poé saméméhna|isukan|ayeuna|engké|Waktu.
## SUN|Kampung adat Jawa Barat
Kampung Naga aya di …|Tasikmalaya|Garut|Sukabumi|Lebak|Tasikmalaya.
Kampung Pulo aya di …|Garut|Ciamis|Sukabumi|Bogor|Garut.
=|Aturan adat Baduy disebut …|pikukuh|Pikukuh.
=|Kasepuhan Ciptagelar aya di …|Sukabumi|Sukabumi.
B|Kampung Pulo ngan boga genep imah jeung hiji tajug.|Genep.
S|Kampung adat nolak sagala hal ti luar.|Teu sakabéh.
Kampung adat Baduy aya di …|Lebak|Garut|Ciamis|Tasikmalaya|Lebak.
Kampung Kuta aya di …|Ciamis|Garut|Bogor|Sukabumi|Ciamis.
"""

SAS += """
## PAI 1
0|Pada ayat 9 Surah Al-Qari'ah disebutkan neraka ....|Hawiyah|Hutamah|Jahim|Saqar|Hawiyah.
1|Hari kebangkitan manusia dari kubur disebut ....|yaumul ba'as|yaumul hisab|yaumul mahsyar|mizan|Ba'as.
2|Berusaha sungguh-sungguh untuk meraih cita-cita disebut ....|ikhtiar|tawakal|qada|qadar|Ikhtiar.
3|Menyalatkan jenazah termasuk kewajiban terhadap jenazah yang ke ....|tiga|satu|dua|empat|Urutan.
4|Salat jenazah dilakukan dengan posisi ....|berdiri|duduk|rukuk|sujud|Berdiri.
5|Tidak sombong dengan ilmu termasuk adab ....|rendah hati|tekun|ikhlas|mengajarkan|Rendah hati.
## PAI 2
0|Surah Al-Lahab menceritakan tokoh yang memusuhi dakwah, yaitu ....|Abu Lahab|Abu Bakar|Umar|Ali|Abu Lahab.
1|Menabung sisa uang saku mencerminkan sikap ....|hemat|boros|tamak|riya|Hemat.
2|Pembeli dalam jual beli termasuk ....|rukun jual beli|syarat barang|riba|hibah|Rukun.
3|Sedekah adalah pemberian tanpa ....|balasan|niat|ikhlas|rida Allah|Sedekah.
4|Contoh wakaf adalah memberikan tanah untuk ....|masjid atau sekolah|dijual kembali|disewakan pribadi|disimpan sendiri|Wakaf.
5|Ki Bagus Hadikusumo berperan sebagai ....|perumus dasar negara|pendiri NU|pencetus Resolusi Jihad|sastrawan|Perumus.
## SUN 1
0|Jelas sora waktu maca sajak disebut ....|artikulasi|lentong|wirahma|sikep|Artikulasi.
1|Darso kawentar dina widang ....|pop Sunda|sastra|pamaréntahan|tari|Darso.
2|Waditra anu ngeusian wirahma dina tembang Cianjuran nyaéta kacapi ....|rincik|indung|siter|celempung|Rincik.
3|Tanda tangan pangirim dina surat pribadi aya dina bagian ....|ngaran|sapaan|bubuka|titimangsa|Ngaran.
4|Lokasi kagiatan ditulis dina bagian ....|tempat|waktu|hasil|judul|Tempat.
5|Hayu urang ulin! kaasup kalimah ....|pangajak|wawaran|pananya|panyeluk|Pangajak.
## SUN 2
0|Amanat Sakadang Kancil Maling Bonténg nyaéta ulah ....|maling|diajar|digawé|tutulung|Maling.
1|Situs anu aya di tengah situ di Garut nyaéta ....|Candi Cangkuang|Batutulis|Gunung Padang|Candi Jiwa|Cangkuang.
2|Mitembeyan dibuat disebut ....|nyalin|ngaseuk|seren taun|leuit|Nyalin.
3|Waditra degung anu jadi mélodi pokok nyaéta ....|saron|goong|kendang|jengglong|Saron.
4|"Ulah ribut!" robah jadi kalimah teu langsung maké kecap ....|sangkan|yén manéhna lapar|atawa|jeung|Sangkan.
5|Kampung Dukuh aya di ....|Garut kidul|Lebak|Sukabumi|Ciamis|Dukuh.
"""
