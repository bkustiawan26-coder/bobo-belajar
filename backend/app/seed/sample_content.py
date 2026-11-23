SAMPLE = {
    2: {
        "chapter": (2, "Penjumlahan dan Pengurangan"),
        "topics": [
            ("Penjumlahan sampai 100", "Gunakan sedotan atau stik es krim, ikat per 10 sebagai puluhan. Minta anak menjumlah dua kelompok, misalnya 23 + 15, sambil menyebut puluhan dan satuannya.", "lupa memisahkan puluhan dan satuan"),
            ("Pengurangan sampai 100", "Berikan uang mainan Rp50, lalu \"belanja\" Rp20. Tanyakan sisa uangnya dan minta anak menunjukkan cara menghitungnya.", "mengurangkan tanpa memperhatikan posisi puluhan dan satuan"),
            ("Soal Cerita", "Ceritakan kejadian di rumah (berbagi permen, membeli telur) dan minta anak menebak: harus ditambah atau dikurangi?", "salah memilih operasi hitung dari kata kunci cerita"),
        ],
        "lesson": ("Penjumlahan sampai 100", 6, [
            ("Penjelasan", "Menjumlah artinya menggabungkan. Kalau kamu punya 23 kelereng, lalu diberi 15 kelereng lagi, kelerengmu jadi lebih banyak.", None, None),
            ("Contoh", "Hitung 23 + 15.\nSatuan dulu: 3 + 5 = 8.\nLalu puluhan: 20 + 10 = 30.\nGabungkan: 30 + 8 = 38.", None, "tens"),
            ("Poin penting", None, ["Satuan dijumlah dengan satuan.", "Puluhan dijumlah dengan puluhan.", "Terakhir, gabungkan hasilnya."], None),
            ("Ringkasan", "Pisahkan puluhan dan satuan, jumlahkan masing-masing, lalu gabungkan. Mudah, kan?", None, None),
        ]),
        "practice": [
            ("mc", "34 + 25 = …", ["59", "69", "49", "58"], {"index": 0}, "Satuan: 4 + 5 = 9. Puluhan: 30 + 20 = 50. Jadi 50 + 9 = 59.", "Coba jumlahkan satuan dulu, baru puluhan.", 0, "mudah"),
            ("tf", "47 − 12 = 35", ["Benar", "Salah"], {"index": 0}, "Satuan: 7 − 2 = 5. Puluhan: 40 − 10 = 30. Jadi 35. Pernyataan ini benar.", "Kurangi satuan dengan satuan, puluhan dengan puluhan.", 1, "mudah"),
            ("mc", "Rani punya 18 permen. Ia memberi 6 permen ke adiknya. Sisa permen Rani …", ["12", "24", "14", "11"], {"index": 0}, "Memberi artinya permen Rani berkurang: 18 − 6 = 12.", "Kata \"memberi\" berarti dikurangi, bukan ditambah.", 2, "sedang"),
            ("fill", "52 + 36 = …", [], {"accepted": ["88"]}, "Satuan: 2 + 6 = 8. Puluhan: 50 + 30 = 80. Jadi 88.", "Periksa lagi penjumlahan satuan dan puluhannya.", 0, "mudah"),
        ],
        "exam": ("Asesmen Sumatif Lingkup Materi: Penjumlahan dan Pengurangan", "Penjumlahan & Pengurangan", 10, [
            ("mc", "21 + 13 = …", ["24", "34", "33", "43"], {"index": 1}, "1 + 3 = 4 dan 20 + 10 = 30, jadi 34.", 0),
            ("mc", "65 − 23 = …", ["42", "32", "48", "88"], {"index": 0}, "5 − 3 = 2 dan 60 − 20 = 40, jadi 42.", 1),
            ("tf", "40 + 50 = 90", ["Benar", "Salah"], {"index": 0}, "4 puluhan + 5 puluhan = 9 puluhan = 90. Benar.", 0),
            ("mc", "Ayah membeli 25 telur, lalu membeli 10 telur lagi. Jumlah telur Ayah …", ["15", "35", "30", "45"], {"index": 1}, "Membeli lagi berarti bertambah: 25 + 10 = 35.", 2),
            ("mc", "58 − … = 30", ["28", "38", "18", "22"], {"index": 0}, "58 − 28 = 30, karena 8 − 8 = 0 dan 50 − 20 = 30.", 1),
        ]),
    },
    5: {
        "chapter": (3, "Pecahan"),
        "topics": [
            ("Pecahan Senilai", "Potong roti atau martabak menjadi 2, lalu 4 bagian. Tanyakan: \"1 dari 2 potong sama banyak dengan berapa dari 4 potong?\"", "mengubah pembilang tanpa mengubah penyebut"),
            ("Penjumlahan Pecahan", "Gunakan kue yang dipotong 4 bagian. Ambil 1 lalu 2 bagian, minta anak menghitung totalnya, lalu tuliskan 1/4 + 2/4 = 3/4. Tekankan bahwa penyebut tetap 4 karena ukuran potongannya tidak berubah.", "ikut menjumlahkan penyebut, misalnya 1/4 + 2/4 dijawab 3/8"),
            ("Soal Cerita Pecahan", "Saat berbelanja atau membagi makanan, buat satu soal cerita pecahan secara lisan dan minta anak menjelaskan langkahnya.", "kesulitan mengubah cerita menjadi bentuk pecahan"),
            ("Pecahan Desimal", "Gunakan contoh uang: Rp500 adalah setengah dari Rp1.000, ditulis 0,5. Ajak anak mencari contoh lain di rumah.", None),
        ],
        "lesson": ("Pecahan Senilai", 8, [
            ("Penjelasan", "Pecahan senilai adalah pecahan yang nilainya sama walaupun angkanya berbeda. 1/2, 2/4, dan 4/8 sama-sama menunjukkan setengah bagian.", None, "frac"),
            ("Contoh", "Kalikan pembilang dan penyebut dengan bilangan yang sama.\n1/3 = (1 × 2)/(3 × 2) = 2/6\n2/5 = (2 × 3)/(5 × 3) = 6/15\n\nKamu juga bisa membagi: 6/8 = (6 ÷ 2)/(8 ÷ 2) = 3/4.", None, None),
            ("Poin penting", None, ["Kalikan atau bagi pembilang dan penyebut dengan bilangan yang sama.", "Jangan hanya mengubah salah satunya.", "Pecahan senilai menunjukkan bagian yang sama besar."], None),
            ("Ringkasan", "Untuk mencari pecahan senilai, kalikan atau bagi pembilang dan penyebut dengan bilangan yang sama. Bentuknya berubah, nilainya tetap.", None, None),
        ]),
        "practice": [
            ("mc", "Pecahan yang senilai dengan 2/3 adalah …", ["4/6", "4/5", "3/4", "2/6"], {"index": 0}, "2/3 = (2 × 2)/(3 × 2) = 4/6.", "Pembilang dan penyebut harus dikali bilangan yang sama.", 0, "mudah"),
            ("multi", "Pilih semua pecahan yang senilai dengan 1/2.", ["2/4", "3/6", "2/3", "5/10"], {"indices": [0, 1, 3]}, "2/4, 3/6, dan 5/10 semuanya bernilai setengah. 2/3 lebih dari setengah.", "Periksa setiap pilihan: apakah pembilangnya tepat setengah dari penyebut?", 0, "sedang"),
            ("mc", "1/4 + 2/4 = …", ["3/4", "3/8", "2/4", "1/2"], {"index": 0}, "Penyebutnya sama, jadi jumlahkan pembilangnya saja: 1 + 2 = 3. Penyebut tetap 4.", "Penyebut tidak ikut dijumlahkan.", 1, "sedang"),
            ("mc", "Ibu memotong kue menjadi 8 bagian sama besar. Dina makan 3 bagian. Pecahan kue yang dimakan Dina adalah …", ["3/8", "5/8", "3/5", "8/3"], {"index": 0}, "Bagian yang dimakan (3) dibagi seluruh bagian (8) = 3/8.", "Pembilang adalah bagian yang diambil, penyebut adalah seluruh bagian.", 2, "mudah"),
            ("fill", "1/2 = …/8 (isi pembilangnya)", [], {"accepted": ["4"]}, "Penyebut 2 dikali 4 menjadi 8, jadi pembilang 1 juga dikali 4 = 4.", "Cari dulu angka pengali penyebutnya.", 0, "sedang"),
        ],
        "exam": ("Asesmen Sumatif Lingkup Materi: Pecahan", "Pecahan", 10, [
            ("mc", "Pecahan senilai dengan 3/5 adalah …", ["6/10", "3/10", "5/3", "6/5"], {"index": 0}, "3/5 = (3 × 2)/(5 × 2) = 6/10.", 0),
            ("mc", "2/7 + 3/7 = …", ["5/14", "5/7", "6/7", "1/7"], {"index": 1}, "Penyebut sama, jumlahkan pembilangnya: 2 + 3 = 5. Hasilnya 5/7.", 1),
            ("tf", "4/8 senilai dengan 1/2.", ["Benar", "Salah"], {"index": 0}, "4/8 = (4 ÷ 4)/(8 ÷ 4) = 1/2. Benar.", 0),
            ("mc", "Sebuah tali dipotong menjadi 5 bagian sama panjang. 2 bagian dipakai. Pecahan tali yang tersisa adalah …", ["2/5", "3/5", "5/3", "3/2"], {"index": 1}, "Tersisa 5 − 2 = 3 bagian dari 5, yaitu 3/5.", 2),
            ("mc", "1/6 + 4/6 = …", ["5/12", "5/6", "4/6", "3/6"], {"index": 1}, "1 + 4 = 5, penyebut tetap 6. Hasilnya 5/6.", 1),
        ]),
    },
    8: {
        "chapter": (5, "Teorema Pythagoras"),
        "topics": [
            ("Teorema Pythagoras", "Cari benda bersudut siku-siku seperti ubin atau buku. Minta anak mengukur dua sisi tegak, memprediksi panjang diagonalnya dengan rumus, lalu membuktikannya dengan penggaris.", "menjumlahkan panjang sisi tanpa mengkuadratkannya"),
            ("Tripel Pythagoras", "Bergantian menyebut tiga bilangan; anak memeriksa apakah a² + b² = c². Mulai dari 3-4-5 dan kelipatannya, lalu coba 5-12-13.", "kurang teliti saat menghitung kuadrat"),
            ("Soal Kontekstual Pythagoras", "Diskusikan tangga yang disandarkan ke dinding atau ukuran layar TV (diagonal). Minta anak menggambar segitiganya dulu sebelum menghitung.", "salah menentukan mana sisi miringnya"),
            ("Jarak Dua Titik", "Gambar denah rumah di kertas berpetak, tandai dua titik, lalu hitung jaraknya dengan Pythagoras.", None),
        ],
        "lesson": ("Teorema Pythagoras", 10, [
            ("Penjelasan", "Pada segitiga siku-siku, kuadrat sisi miring (hipotenusa) sama dengan jumlah kuadrat dua sisi lainnya:\nc² = a² + b²", None, "tri"),
            ("Contoh", "Sisi tegak a = 6 cm dan b = 8 cm.\nc² = 6² + 8² = 36 + 64 = 100\nc = √100 = 10 cm\n\nUntuk mencari sisi tegak: a² = c² − b².", None, None),
            ("Poin penting", None, ["Hanya berlaku untuk segitiga siku-siku.", "c selalu sisi terpanjang, di depan sudut siku-siku.", "Kuadratkan dulu, baru jumlahkan atau kurangkan."], None),
            ("Ringkasan", "Teorema Pythagoras menghubungkan ketiga sisi segitiga siku-siku. Kenali sisi miringnya, tulis c² = a² + b², lalu selesaikan untuk sisi yang dicari.", None, None),
        ]),
        "practice": [
            ("mc", "Segitiga siku-siku memiliki sisi tegak 5 cm dan 12 cm. Panjang hipotenusanya adalah …", ["13 cm", "17 cm", "15 cm", "11 cm"], {"index": 0}, "c² = 5² + 12² = 25 + 144 = 169, sehingga c = 13 cm.", "5 + 12 = 17 terjadi jika sisi dijumlahkan langsung. Kuadratkan dulu.", 0, "mudah"),
            ("multi", "Pilih semua yang merupakan tripel Pythagoras.", ["3, 4, 5", "6, 8, 10", "5, 7, 9", "8, 15, 17"], {"indices": [0, 1, 3]}, "9 + 16 = 25, 36 + 64 = 100, dan 64 + 225 = 289 memenuhi a² + b² = c². Untuk 5, 7, 9: 25 + 49 = 74, bukan 81.", "Periksa a² + b² = c² untuk setiap pilihan.", 1, "sedang"),
            ("mc", "Tangga sepanjang 10 m disandarkan ke dinding. Jarak kaki tangga ke dinding 6 m. Tinggi dinding yang dicapai ujung tangga adalah …", ["8 m", "4 m", "16 m", "12 m"], {"index": 0}, "Tangga adalah sisi miring. t² = 10² − 6² = 100 − 36 = 64, sehingga t = 8 m.", "Tangga adalah sisi miring, jadi gunakan pengurangan: t² = c² − a².", 2, "menantang"),
            ("tf", "Teorema Pythagoras berlaku untuk semua jenis segitiga.", ["Benar", "Salah"], {"index": 1}, "Teorema Pythagoras hanya berlaku untuk segitiga siku-siku.", "Perhatikan syarat jenis segitiganya.", 0, "mudah"),
            ("fill", "Jika c = 25 dan a = 7, maka b = …", [], {"accepted": ["24"]}, "b² = 25² − 7² = 625 − 49 = 576, sehingga b = 24.", "Untuk sisi tegak, kurangkan: b² = c² − a².", 0, "sedang"),
        ],
        "exam": ("Asesmen Sumatif Lingkup Materi: Teorema Pythagoras", "Teorema Pythagoras", 15, [
            ("mc", "Hipotenusa segitiga dengan sisi tegak 9 cm dan 12 cm adalah …", ["15 cm", "21 cm", "18 cm", "13 cm"], {"index": 0}, "81 + 144 = 225, √225 = 15 cm.", 0),
            ("tf", "7, 24, 25 merupakan tripel Pythagoras.", ["Benar", "Salah"], {"index": 0}, "49 + 576 = 625 = 25². Benar.", 1),
            ("mc", "Panjang benang layang-layang 17 m. Jarak horizontal anak ke titik tepat di bawah layang-layang 8 m. Tinggi layang-layang adalah …", ["15 m", "9 m", "25 m", "12 m"], {"index": 0}, "t² = 17² − 8² = 289 − 64 = 225, t = 15 m.", 2),
            ("mc", "Jika a² + b² < c², segitiga tersebut adalah segitiga …", ["Siku-siku", "Lancip", "Tumpul", "Sama sisi"], {"index": 2}, "Jika kuadrat sisi terpanjang lebih besar dari jumlah kuadrat dua sisi lain, segitiganya tumpul.", 0),
            ("mc", "Jarak titik A(1, 2) dan B(4, 6) adalah …", ["5", "7", "25", "4"], {"index": 0}, "Selisih x = 3 dan selisih y = 4. Jarak = √(9 + 16) = √25 = 5.", 3),
        ]),
    },
}

SUBJECTS = {
    1: [("MAT", "Matematika", "Mt"), ("BIN", "Bahasa Indonesia", "BI"), ("PPK", "Pendidikan Pancasila", "PP"), ("SBD", "Seni dan Budaya", "SB"), ("PJOK", "PJOK", "PJ")],
    2: [("MAT", "Matematika", "Mt"), ("BIN", "Bahasa Indonesia", "BI"), ("IPAS", "IPAS", "IP"), ("PPK", "Pendidikan Pancasila", "PP"), ("SBD", "Seni dan Budaya", "SB"), ("PJOK", "PJOK", "PJ")],
    3: [("MAT", "Matematika", "Mt"), ("BIN", "Bahasa Indonesia", "BI"), ("IPAS", "IPAS", "IP"), ("PPK", "Pendidikan Pancasila", "PP"), ("BIG", "Bahasa Inggris", "En"), ("SBD", "Seni dan Budaya", "SB"), ("PJOK", "PJOK", "PJ"), ("KKA", "Koding dan KA", "KA")],
    4: [("MAT", "Matematika", "Mt"), ("BIN", "Bahasa Indonesia", "BI"), ("IPA", "IPA", "IA"), ("IPS", "IPS", "IS"), ("BIG", "Bahasa Inggris", "En"), ("PPK", "Pendidikan Pancasila", "PP"), ("SBD", "Seni dan Budaya", "SB"), ("PJOK", "PJOK", "PJ"), ("INF", "Informatika", "If"), ("KKA", "Koding dan KA", "KA")],
}

SCAFFOLDS = {
    2: [
        {"example": "Contoh: 21 + 13. Satuan 1 + 3 = 4. Puluhan 20 + 10 = 30. Hasilnya 34.", "steps": ["Tulis satuannya: 4 dan 5.", "Jumlahkan satuan: 4 + 5 = ?", "Jumlahkan puluhan: 30 + 20 = ?", "Gabungkan puluhan dan satuan."]},
        {"example": "Contoh: 38 − 15. Satuan 8 − 5 = 3. Puluhan 30 − 10 = 20. Hasilnya 23.", "steps": ["Kurangi satuan: 7 − 2 = ?", "Kurangi puluhan: 40 − 10 = ?", "Gabungkan, lalu bandingkan dengan 35."]},
        {"example": "Contoh: Budi punya 10 kue, memberi 3 kue. Memberi berarti berkurang: 10 − 3 = 7.", "steps": ["Cari kata kunci: \"memberi\".", "Memberi artinya permen berkurang, jadi kita mengurangi.", "Hitung 18 − 6."]},
        {"example": "Contoh: 41 + 27. Satuan 1 + 7 = 8. Puluhan 40 + 20 = 60. Hasilnya 68.", "steps": ["Jumlahkan satuan: 2 + 6 = ?", "Jumlahkan puluhan: 50 + 30 = ?", "Gabungkan hasilnya."]},
    ],
    5: [
        {"example": "Contoh: 1/3 = (1 × 2)/(3 × 2) = 2/6.", "steps": ["Pilih angka pengali, misalnya 2.", "Kalikan pembilang: 2 × 2 = ?", "Kalikan penyebut: 3 × 2 = ?", "Cari pilihan yang sama dengan hasilmu."]},
        {"example": "Contoh: 2/4 senilai dengan 1/2 karena 2 adalah setengah dari 4.", "steps": ["Untuk tiap pilihan, bandingkan pembilang dengan penyebut.", "Apakah pembilangnya tepat setengah dari penyebut?", "Pilih semua yang jawabannya ya."]},
        {"example": "Contoh: 1/5 + 3/5 = 4/5. Penyebutnya tetap 5.", "steps": ["Periksa penyebutnya: keduanya 4.", "Jumlahkan pembilangnya saja: 1 + 2 = ?", "Tulis hasilnya dengan penyebut 4."]},
        {"example": "Contoh: pizza dipotong 6 bagian, dimakan 2 bagian, jadi 2/6.", "steps": ["Ada berapa bagian seluruhnya? Itu penyebut.", "Berapa bagian yang dimakan? Itu pembilang.", "Tulis pembilang/penyebut."]},
        {"example": "Contoh: 1/3 = …/6. Penyebut 3 dikali 2 menjadi 6, jadi pembilang 1 dikali 2 = 2.", "steps": ["Penyebut 2 dikali berapa supaya menjadi 8?", "Kalikan pembilang 1 dengan angka yang sama."]},
    ],
    8: [
        {"example": "Contoh: sisi tegak 3 dan 4. c² = 9 + 16 = 25, jadi c = 5.", "steps": ["Kuadratkan sisi pertama: 5² = ?", "Kuadratkan sisi kedua: 12² = ?", "Jumlahkan kedua kuadrat.", "Cari akar dari hasilnya."]},
        {"example": "Contoh: 6, 8, 10 → 36 + 64 = 100 = 10². Termasuk tripel.", "steps": ["Untuk tiap pilihan, kuadratkan dua bilangan terkecil.", "Jumlahkan.", "Bandingkan dengan kuadrat bilangan terbesar."]},
        {"example": "Contoh: tangga 5 m, jarak ke dinding 3 m. t² = 25 − 9 = 16, t = 4 m.", "steps": ["Gambar segitiganya: tangga adalah sisi miring.", "Kuadratkan panjang tangga dan jarak ke dinding.", "Kurangkan: c² − a².", "Cari akarnya."]},
        {"example": "Contoh: segitiga dengan sudut tumpul tidak memenuhi a² + b² = c².", "steps": ["Ingat syarat teorema Pythagoras.", "Apakah semua segitiga punya sudut siku-siku?"]},
        {"example": "Contoh: c = 13, a = 5. b² = 169 − 25 = 144, b = 12.", "steps": ["Kuadratkan c: 25² = ?", "Kuadratkan a: 7² = ?", "Kurangkan, lalu cari akarnya."]},
    ],
}

PREREQUISITES = [
    (5, "Penjumlahan Pecahan", 5, "Pecahan Senilai"),
    (5, "Soal Cerita Pecahan", 5, "Penjumlahan Pecahan"),
    (5, "Penjumlahan Pecahan", 2, "Penjumlahan sampai 100"),
    (8, "Tripel Pythagoras", 8, "Teorema Pythagoras"),
    (8, "Soal Kontekstual Pythagoras", 8, "Teorema Pythagoras"),
    (8, "Jarak Dua Titik", 8, "Teorema Pythagoras"),
]
