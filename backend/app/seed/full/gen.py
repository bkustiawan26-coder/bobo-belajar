import math
import random
from fractions import Fraction

from app.seed.full.dsl import Q, fill, mc, tf


def fmt(v) -> str:
    if isinstance(v, Fraction):
        return f"{v.numerator}/{v.denominator}" if v.denominator != 1 else fmt(v.numerator)
    if isinstance(v, float) and not v.is_integer():
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        whole, _, dec = s.partition(".")
        return fmt(int(whole)) + ("," + dec if dec else "") if not whole.startswith("-") else "-" + fmt(-v)
    v = int(v)
    if v < 0:
        return "−" + fmt(-v)
    s = str(v)
    out = ""
    while len(s) > 3:
        out = "." + s[-3:] + out
        s = s[:-3]
    return s + out


class G:
    def __init__(self, seed: str):
        self.r = random.Random(seed)
        self.qs: list[Q] = []
        self.bodies: set[str] = set()

    def _add(self, q: Q) -> None:
        if q.body not in self.bodies:
            self.bodies.add(q.body)
            self.qs.append(q)

    def pick(self, body, ans, wrong, expl, n=4):
        a = ans if isinstance(ans, str) else fmt(ans)
        opts = [a]
        for w in list(wrong) + [ans + d for d in (1, -1, 2, 10, -2, 3) if not isinstance(ans, str)]:
            w = w if isinstance(w, str) else fmt(w)
            if w not in opts and not w.startswith("−−"):
                opts.append(w)
            if len(opts) == n:
                break
        if len(opts) >= 3:
            self._add(mc(body, opts, 0, expl))

    def isi(self, body, ans, expl, extra=()):
        a = ans if isinstance(ans, str) else fmt(ans)
        acc = [a] + [x for x in extra if x != a]
        if a.startswith("−"):
            acc.append("-" + a[1:])
        self._add(fill(body, acc, expl))

    def bs(self, body, true, expl):
        self._add(tf(body, true, expl))


def _bilang(g):
    icons = "🍎⭐⚽🐟🌸🚗🍌🎈"
    for _ in range(12):
        n = g.r.randint(3, 20)
        ic = g.r.choice(icons)
        if n <= 10:
            g.pick(f"Ada berapa {ic}? {ic * n}", n, [n - 1, n + 1, n + 2], f"Hitung satu per satu, ada {n}.")
        a = g.r.randint(1, 18)
        g.pick(f"Bilangan setelah {a} adalah …", a + 1, [a - 1, a + 2, a], f"Setelah {a} adalah {a + 1}.")
        g.pick(f"Bilangan sebelum {a + 2} adalah …", a + 1, [a + 3, a, a + 2], f"Sebelum {a + 2} adalah {a + 1}.")
        g.isi(f"Lanjutkan: {a}, {a + 1}, …", a + 2, f"Urutannya naik satu: {a}, {a + 1}, {a + 2}.")


def _banding(g):
    for _ in range(12):
        a, b = g.r.sample(range(1, 21), 2)
        g.pick(f"Mana yang lebih besar, {a} atau {b}?", max(a, b), [min(a, b), a + b, abs(a - b) or 21], f"{max(a, b)} lebih besar dari {min(a, b)}.")
        g.bs(f"{a} lebih kecil dari {b}.", a < b, f"{a} {'lebih kecil' if a < b else 'lebih besar'} dari {b}.")
        c = sorted(g.r.sample(range(1, 21), 3))
        g.pick(f"Bilangan terkecil dari {c[2]}, {c[0]}, {c[1]} adalah …", c[0], [c[1], c[2], c[0] + 1], f"Yang paling sedikit adalah {c[0]}.")


def _tambah(lim, minus=False, thou=False):
    def f(g):
        names = ["Ani", "Budi", "Sari", "Dodi", "Rina", "Tono"]
        things = ["kelereng", "permen", "buku", "pensil", "kue", "balon"]
        for _ in range(14):
            a = g.r.randint(lim // 10 or 1, lim // 2)
            b = g.r.randint(1, lim - a)
            if minus:
                a, b = a + b, b
                ans = a - b
                g.pick(f"{a} − {b} = …", ans, [ans + 1, ans - 1, a + b], f"{a} dikurangi {b} sama dengan {ans}.")
                nm, th = g.r.choice(names), g.r.choice(things)
                g.isi(f"{nm} punya {fmt(a)} {th}, diberikan {fmt(b)}. Sisa {th} {nm} …", ans, f"{fmt(a)} − {fmt(b)} = {fmt(ans)}.")
            else:
                ans = a + b
                g.pick(f"{fmt(a)} + {fmt(b)} = …", ans, [ans + 1, ans - 1, ans + 10], f"{fmt(a)} ditambah {fmt(b)} sama dengan {fmt(ans)}.")
                nm, th = g.r.choice(names), g.r.choice(things)
                g.isi(f"{nm} punya {fmt(a)} {th}, lalu mendapat {fmt(b)} lagi. Sekarang ada …", ans, f"{fmt(a)} + {fmt(b)} = {fmt(ans)}.")
            if thou:
                x, y = g.r.randint(100, 900), g.r.randint(10, 99)
                g.pick(f"{fmt(x)} − {fmt(y)} = …", x - y, [x - y + 10, x - y - 10, x + y], f"{fmt(x)} − {fmt(y)} = {fmt(x - y)}.")
    return f


def _place(lo, hi):
    names = ["satuan", "puluhan", "ratusan", "ribuan", "puluh ribuan", "ratus ribuan"]

    def f(g):
        for _ in range(14):
            n = g.r.randint(lo, hi)
            s = str(n)
            k = g.r.randrange(len(s))
            place = len(s) - 1 - k
            d = int(s[k])
            if d == 0:
                continue
            val = d * 10 ** place
            g.pick(f"Pada bilangan {fmt(n)}, angka {d} menempati tempat …", names[place], [x for x in names[:len(s)] if x != names[place]], f"Angka {d} pada {fmt(n)} berada di tempat {names[place]}.")
            g.pick(f"Nilai angka {d} pada bilangan {fmt(n)} adalah …", val, [d, val * 10 if place < 5 else val // 10, val // 10 if place else d + 10], f"Angka {d} di tempat {names[place]} bernilai {fmt(val)}.")
            parts = [int(c) * 10 ** (len(s) - 1 - i) for i, c in enumerate(s) if c != "0"]
            g.isi(f"{' + '.join(fmt(p) for p in parts)} = …", n, f"Jumlahkan nilai tiap tempat: {fmt(n)}.")
    return f


def _ukur(g):
    pairs = [("pensil", 15), ("penghapus", 5), ("buku", 25), ("sedotan", 20), ("krayon", 9), ("lidi", 30)]
    for _ in range(10):
        (a, x), (b, y) = g.r.sample(pairs, 2)
        g.pick(f"Panjang {a} {x} cm dan {b} {y} cm. Mana yang lebih panjang?", a if x > y else b, [b if x > y else a, "sama panjang"], f"{max(x, y)} cm lebih panjang dari {min(x, y)} cm.", n=3)
        g.isi(f"Selisih panjang {a} ({x} cm) dan {b} ({y} cm) adalah … cm", abs(x - y), f"{max(x, y)} − {min(x, y)} = {abs(x - y)}.")
        m = g.r.randint(1, 9)
        g.pick(f"{m} m = … cm", m * 100, [m * 10, m * 1000, m], f"1 m = 100 cm, jadi {m} m = {m * 100} cm.")
        kg = g.r.randint(1, 9)
        g.pick(f"{kg} kg = … g", kg * 1000, [kg * 100, kg * 10, kg], f"1 kg = 1.000 g, jadi {kg} kg = {fmt(kg * 1000)} g.")


def _diagram(g):
    sets = [("🍎 Apel", "🍊 Jeruk", "🍌 Pisang", "🥭 Mangga"), ("🚗 Mobil", "🚲 Sepeda", "🛵 Motor", "🚌 Bus"), ("⚽ Bola", "🏸 Bulu tangkis", "🏊 Renang", "🎨 Menggambar")]
    for _ in range(8):
        labels = g.r.choice(sets)
        vals = g.r.sample(range(2, 12), 4)
        data = ", ".join(f"{l} {v}" for l, v in zip(labels, vals))
        top = labels[vals.index(max(vals))].split(" ", 1)[1]
        low = labels[vals.index(min(vals))].split(" ", 1)[1]
        names = [l.split(" ", 1)[1] for l in labels]
        g.pick(f"Data: {data}. Mana yang paling banyak?", top, [x for x in names if x != top], f"Nilai terbesar {max(vals)}, yaitu {top}.")
        g.pick(f"Data: {data}. Mana yang paling sedikit?", low, [x for x in names if x != low], f"Nilai terkecil {min(vals)}, yaitu {low}.")
        g.isi(f"Data: {data}. Jumlah semuanya …", sum(vals), f"{' + '.join(str(v) for v in vals)} = {sum(vals)}.")
        i, j = 0, 1
        g.isi(f"Data: {data}. Selisih {names[i]} dan {names[j]} …", abs(vals[i] - vals[j]), f"{max(vals[i], vals[j])} − {min(vals[i], vals[j])} = {abs(vals[i] - vals[j])}.")


def _bentuk(g):
    facts = [("segitiga", 3), ("persegi", 4), ("persegi panjang", 4), ("segi lima", 5), ("segi enam", 6)]
    objs = [("pintu", "persegi panjang"), ("jam dinding", "lingkaran"), ("potongan semangka", "segitiga"), ("ubin lantai", "persegi"), ("koin", "lingkaran"), ("bendera segitiga", "segitiga"), ("buku tulis", "persegi panjang"), ("piring", "lingkaran")]
    for name, n in facts:
        g.pick(f"Banyak sisi {name} adalah …", n, [n + 1, n - 1, n + 2], f"{name.capitalize()} punya {n} sisi.")
        g.pick(f"Banyak sudut {name} adalah …", n, [n + 1, n - 1, 0], f"{name.capitalize()} punya {n} sudut.")
    for o, b in objs:
        g.pick(f"{o.capitalize()} biasanya berbentuk …", b, [x for x in ["lingkaran", "segitiga", "persegi panjang", "persegi"] if x != b], f"{o.capitalize()} berbentuk {b}.")
    g.bs("Lingkaran punya sudut.", False, "Lingkaran tidak punya sudut.")
    g.bs("Persegi punya 4 sisi sama panjang.", True, "Keempat sisi persegi sama panjang.")


def _ruang(g):
    objs = [("dadu", "kubus"), ("kardus sepatu", "balok"), ("kaleng susu", "tabung"), ("bola sepak", "bola"), ("topi ulang tahun", "kerucut"), ("lemari", "balok"), ("drum", "tabung"), ("kelereng", "bola")]
    names = ["kubus", "balok", "tabung", "bola", "kerucut"]
    for o, b in objs:
        g.pick(f"{o.capitalize()} berbentuk bangun ruang …", b, [x for x in names if x != b], f"{o.capitalize()} berbentuk {b}.")
    for b, sisi in [("kubus", 6), ("balok", 6), ("tabung", 3)]:
        g.pick(f"Banyak sisi {b} adalah …", sisi, [sisi + 2, sisi - 1, 8], f"{b.capitalize()} punya {sisi} sisi.")
    g.bs("Bola tidak punya titik sudut.", True, "Bola hanya punya satu sisi lengkung.")
    g.bs("Tabung punya 2 sisi lingkaran.", True, "Alas dan tutup tabung berbentuk lingkaran.")
    g.bs("Kerucut punya 2 titik sudut.", False, "Kerucut punya 1 titik puncak.")
    g.pick("Bangun ruang yang semua sisinya persegi adalah …", "kubus", ["balok", "tabung", "kerucut"], "Kubus punya 6 sisi persegi.")
    g.pick("Banyak rusuk kubus adalah …", 12, [6, 8, 4], "Kubus punya 12 rusuk.")
    g.bs("Kubus punya 8 titik sudut.", True, "Kubus punya 8 titik sudut.")


def _pola(g):
    for _ in range(12):
        a, d = g.r.randint(1, 20), g.r.randint(2, 6)
        seq = [a + d * i for i in range(5)]
        g.pick(f"Lanjutkan pola: {', '.join(map(str, seq[:4]))}, …", seq[4], [seq[4] + 1, seq[3] + 1, seq[4] + d], f"Pola bertambah {d}: {seq[3]} + {d} = {seq[4]}.")
        g.isi(f"Pola: {seq[0]}, {seq[1]}, …, {seq[3]}. Bilangan yang hilang …", seq[2], f"Setiap langkah bertambah {d}.")
        b = g.r.randint(40, 90)
        down = [b - d * i for i in range(4)]
        g.pick(f"Lanjutkan pola turun: {', '.join(map(str, down[:3]))}, …", down[3], [down[3] - 1, down[2] + d, down[3] + d], f"Pola berkurang {d}.")


def _pecahan_dasar(g):
    for d in (2, 3, 4, 5, 6, 8, 10):
        for n in range(1, d):
            if g.r.random() < 0.5:
                g.pick(f"Sebuah kue dipotong {d} sama besar. Diambil {n} potong. Pecahannya …", f"{n}/{d}", [f"{d}/{n}", f"{n}/{d + 1}", f"{d - n}/{d}" if d - n != n else f"{n + 1}/{d}"], f"{n} dari {d} bagian ditulis {n}/{d}.")
    g.pick("Pada pecahan 3/5, angka 5 disebut …", "penyebut", ["pembilang", "pecahan", "pembagi"], "Angka di bawah disebut penyebut.")
    g.pick("Pada pecahan 2/7, angka 2 disebut …", "pembilang", ["penyebut", "pecahan", "pembagi"], "Angka di atas disebut pembilang.")
    g.pick("Setengah ditulis …", "1/2", ["1/4", "2/1", "1/3"], "Setengah = satu dari dua bagian = 1/2.")
    g.pick("Seperempat ditulis …", "1/4", ["1/2", "4/1", "1/3"], "Seperempat = satu dari empat bagian = 1/4.")
    g.pick("Mana yang lebih besar, 1/2 atau 1/4?", "1/2", ["1/4", "sama besar"], "Dibagi 2 bagiannya lebih besar daripada dibagi 4.", n=3)


def _kali(g):
    for _ in range(12):
        a, b = g.r.randint(2, 10), g.r.randint(2, 10)
        g.pick(f"{a} × {b} = …", a * b, [a * b + a, a + b, a * b - b], f"{a} × {b} = {a * b}.")
        g.pick(f"{' + '.join([str(b)] * a)} sama dengan …", f"{a} × {b}", [f"{b} + {a}", f"{a} + {b}", f"{b} × {b}"], f"{b} dijumlahkan {a} kali = {a} × {b}.")
        g.isi(f"Ada {a} kotak, setiap kotak berisi {b} kue. Jumlah kue …", a * b, f"{a} × {b} = {a * b}.")


def _bagi(g):
    for _ in range(12):
        b, c = g.r.randint(2, 10), g.r.randint(2, 10)
        a = b * c
        g.pick(f"{a} : {b} = …", c, [c + 1, c - 1, b], f"{a} : {b} = {c}, karena {b} × {c} = {a}.")
        g.isi(f"{a} permen dibagi sama banyak kepada {b} anak. Setiap anak mendapat …", c, f"{a} : {b} = {c}.")


def _kalimat(g):
    for _ in range(10):
        a, b = g.r.randint(10, 60), g.r.randint(2, 9)
        g.pick(f"Ibu membeli {a} telur, lalu membeli {b} lagi. Kalimat matematikanya …", f"{a} + {b} = {a + b}", [f"{a} − {b} = {a - b}", f"{a} × {b} = {a * b}", f"{a} : {b}"], "Membeli lagi berarti ditambah.")
        g.pick(f"Ada {a} telur, {b} pecah. Kalimat matematikanya …", f"{a} − {b} = {a - b}", [f"{a} + {b} = {a + b}", f"{b} − {a}", f"{a} × {b} = {a * b}"], "Pecah berarti dikurangi.")
        c = g.r.randint(2, 6)
        g.isi(f"Ada {c} piring, tiap piring {b} kue. Banyak kue seluruhnya …", c * b, f"{c} × {b} = {c * b}.")


def _segiempat(g):
    facts = [("persegi", "4 sisi sama panjang dan 4 sudut siku-siku"), ("persegi panjang", "sisi berhadapan sama panjang dan 4 sudut siku-siku"), ("jajar genjang", "sisi berhadapan sejajar, sudut tidak siku-siku"), ("belah ketupat", "4 sisi sama panjang, diagonal saling tegak lurus"), ("trapesium", "sepasang sisi sejajar"), ("layang-layang", "dua pasang sisi berdekatan sama panjang")]
    names = [f for f, _ in facts]
    for name, ciri in facts:
        g.pick(f"Bangun dengan ciri {ciri} adalah …", name, [x for x in names if x != name], f"Itu ciri {name}.")
    for name, _ in facts:
        g.pick(f"Banyak sisi {name} adalah …", 4, [3, 5, 6], "Semua segi empat punya 4 sisi.")
    g.bs("Persegi juga termasuk persegi panjang.", True, "Persegi memenuhi semua ciri persegi panjang.")
    g.bs("Trapesium punya dua pasang sisi sejajar.", False, "Trapesium hanya punya sepasang sisi sejajar.")
    g.bs("Diagonal belah ketupat saling tegak lurus.", True, "Diagonalnya berpotongan tegak lurus.")
    g.pick("Segi empat yang semua sudutnya siku-siku dan sisinya sama panjang adalah …", "persegi", ["belah ketupat", "trapesium", "jajar genjang"], "Itu persegi.")
    g.pick("Jumlah sudut dalam segi empat adalah …", "360°", ["180°", "90°", "270°"], "Jumlah sudut segi empat 360°.")


def _kelfak(g):
    for _ in range(10):
        n = g.r.choice([12, 16, 18, 20, 24, 28, 30, 36])
        fs = [d for d in range(1, n + 1) if n % d == 0]
        non = [d for d in range(2, n) if n % d][:3]
        g.pick(f"Manakah yang merupakan faktor {n}?", g.r.choice(fs[1:-1]), non, f"Faktor {n}: {', '.join(map(str, fs))}.")
        k = g.r.randint(3, 9)
        g.pick(f"Kelipatan {k} yang ketiga adalah …", 3 * k, [2 * k, 4 * k, 3 + k], f"{k}, {2 * k}, {3 * k}.")
        g.isi(f"Banyak faktor dari {n} adalah …", len(fs), f"Faktor {n}: {', '.join(map(str, fs))} ({len(fs)} faktor).")


def _klpk(g):
    for _ in range(10):
        a, b = g.r.sample([4, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24], 2)
        lcm = a * b // math.gcd(a, b)
        g.pick(f"KPK dari {a} dan {b} adalah …", lcm, [a * b if a * b != lcm else lcm * 2, math.gcd(a, b), max(a, b)], f"Kelipatan persekutuan terkecil {a} dan {b} = {lcm}.")
        g.pick(f"FPB dari {a} dan {b} adalah …", math.gcd(a, b), [lcm, 1 if math.gcd(a, b) != 1 else 2, min(a, b) if min(a, b) != math.gcd(a, b) else min(a, b) * 2], f"Faktor persekutuan terbesar {a} dan {b} = {math.gcd(a, b)}.")
    g.pick("Lampu A menyala tiap 4 menit, lampu B tiap 6 menit. Keduanya menyala bersama lagi setelah … menit", 12, [24, 10, 2], "KPK 4 dan 6 = 12.")
    g.pick("18 apel dan 24 jeruk dibagi ke keranjang sama banyak. Paling banyak ada … keranjang", 6, [12, 3, 42], "FPB 18 dan 24 = 6.")


def _luas_pp(g):
    for _ in range(10):
        p, l = g.r.randint(4, 20), g.r.randint(2, 12)
        if p == l:
            p += 1
        g.pick(f"Persegi panjang p = {p} cm, l = {l} cm. Kelilingnya …", f"{2 * (p + l)} cm", [f"{p * l} cm", f"{p + l} cm", f"{2 * p + l} cm"], f"K = 2 × ({p} + {l}) = {2 * (p + l)} cm.")
        g.pick(f"Persegi panjang p = {p} cm, l = {l} cm. Luasnya …", f"{p * l} cm²", [f"{2 * (p + l)} cm²", f"{p + l} cm²", f"{p * l * 2} cm²"], f"L = {p} × {l} = {p * l} cm².")
        s = g.r.randint(3, 15)
        g.isi(f"Luas persegi dengan sisi {s} cm adalah … cm²", s * s, f"L = {s} × {s} = {s * s} cm².")


def _desimal(g):
    pairs = [(Fraction(1, 2), "0,5", "50%"), (Fraction(1, 4), "0,25", "25%"), (Fraction(3, 4), "0,75", "75%"), (Fraction(1, 5), "0,2", "20%"), (Fraction(2, 5), "0,4", "40%"), (Fraction(1, 10), "0,1", "10%"), (Fraction(3, 10), "0,3", "30%"), (Fraction(7, 10), "0,7", "70%"), (Fraction(9, 100), "0,09", "9%"), (Fraction(45, 100), "0,45", "45%")]
    for f, d, p in pairs:
        g.pick(f"Bentuk desimal dari {fmt(f)} adalah …", d, [x for _, x, _ in pairs if x != d][:3], f"{fmt(f)} = {d}.")
        g.pick(f"{d} dalam persen adalah …", p, [x for _, _, x in pairs if x != p][:3], f"{d} = {p}.")
    g.bs("0,5 sama dengan 50%.", True, "0,5 = 50/100 = 50%.")


def _senilai(g):
    for _ in range(12):
        n, d = g.r.choice([(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (1, 4), (3, 5)])
        k = g.r.randint(2, 5)
        g.pick(f"Pecahan yang senilai dengan {n}/{d} adalah …", f"{n * k}/{d * k}", [f"{n + k}/{d + k}", f"{n * k}/{d}", f"{n}/{d * k}"], f"Kalikan pembilang dan penyebut dengan {k}.")
        g.isi(f"{n}/{d} = …/{d * k}", n * k, f"{d} × {k} = {d * k}, jadi pembilang {n} × {k} = {n * k}.")


def _jumlah_pecahan(g):
    for _ in range(12):
        d = g.r.choice([5, 6, 7, 8, 9, 10, 12])
        a, b = g.r.randint(1, d - 2), 1
        b = g.r.randint(1, d - a - 1)
        g.pick(f"{a}/{d} + {b}/{d} = …", f"{a + b}/{d}", [f"{a + b}/{2 * d}", f"{a * b}/{d}", f"{a + b + 1}/{d}"], f"Penyebut sama, jumlahkan pembilang: {a} + {b} = {a + b}.")
        g.pick(f"{a + b}/{d} − {b}/{d} = …", f"{a}/{d}", [f"{a}/{0 or d * 2}", f"{a + 2 * b}/{d}", f"{b}/{d}" if b != a else f"{a + 1}/{d}"], f"{a + b} − {b} = {a}.")
    g.pick("1/2 + 1/4 = …", "3/4", ["2/6", "1/6", "2/4"], "1/2 = 2/4, lalu 2/4 + 1/4 = 3/4.")
    g.pick("1/3 + 1/6 = …", "1/2", ["2/9", "2/6", "1/9"], "1/3 = 2/6, jadi 2/6 + 1/6 = 3/6 = 1/2.")


def _volume_balok(g):
    for _ in range(10):
        p, l, t = g.r.randint(2, 12), g.r.randint(2, 10), g.r.randint(2, 10)
        g.pick(f"Volume balok p = {p} cm, l = {l} cm, t = {t} cm adalah …", f"{p * l * t} cm³", [f"{p + l + t} cm³", f"{p * l} cm³", f"{2 * (p * l + p * t + l * t)} cm³"], f"V = {p} × {l} × {t} = {p * l * t} cm³.")
        s = g.r.randint(2, 10)
        g.isi(f"Volume kubus dengan rusuk {s} cm adalah … cm³", s ** 3, f"V = {s} × {s} × {s} = {s ** 3} cm³.")


def _bulat(g):
    for _ in range(12):
        n = g.r.randint(1001, 99999)
        if n % 100 == 50 or n % 1000 == 500:
            n += 7
        r100 = int(round(n / 100.0)) * 100 if n % 100 != 50 else n + 50
        r1000 = int(math.floor(n / 1000 + 0.5)) * 1000
        g.pick(f"{fmt(n)} dibulatkan ke ratusan terdekat menjadi …", r100, [r100 + 100, r100 - 100, n // 100 * 100 if n // 100 * 100 != r100 else r100 + 200], f"Lihat angka puluhan, {fmt(n)} ≈ {fmt(r100)}.")
        g.pick(f"{fmt(n)} dibulatkan ke ribuan terdekat menjadi …", r1000, [r1000 + 1000, r1000 - 1000 if r1000 > 1000 else r1000 + 2000, r100], f"Lihat angka ratusan, {fmt(n)} ≈ {fmt(r1000)}.")


def _luas_seg(g):
    for _ in range(10):
        a, t = g.r.randint(2, 20) * 2, g.r.randint(3, 15)
        g.pick(f"Luas segitiga dengan alas {a} cm dan tinggi {t} cm adalah …", f"{a * t // 2} cm²", [f"{a * t} cm²", f"{a + t} cm²", f"{a * t // 4} cm²"], f"L = {a} × {t} : 2 = {a * t // 2} cm².")
        x, y, z = g.r.randint(3, 12), g.r.randint(3, 12), g.r.randint(3, 12)
        g.isi(f"Keliling segitiga dengan sisi {x} cm, {y} cm, dan {z} cm adalah … cm", x + y + z, f"{x} + {y} + {z} = {x + y + z}.")


def _sudut(g):
    kinds = [(30, "lancip"), (45, "lancip"), (60, "lancip"), (90, "siku-siku"), (100, "tumpul"), (120, "tumpul"), (150, "tumpul"), (180, "lurus")]
    for deg, k in kinds:
        g.pick(f"Sudut {deg}° termasuk sudut …", k, [x for x in ["lancip", "siku-siku", "tumpul", "lurus"] if x != k], f"{deg}° adalah sudut {k}.")
    for deg in (30, 40, 55, 70):
        g.pick(f"Pelurus sudut {deg}° adalah …", f"{180 - deg}°", [f"{90 - deg}°", f"{deg}°", f"{360 - deg}°"], f"180° − {deg}° = {180 - deg}°.")
        g.pick(f"Penyiku sudut {deg}° adalah …", f"{90 - deg}°", [f"{180 - deg}°", f"{deg}°", f"{90 + deg}°"], f"90° − {deg}° = {90 - deg}°.")
    g.pick("Alat untuk mengukur besar sudut adalah …", "busur derajat", ["penggaris", "jangka", "meteran"], "Sudut diukur dengan busur derajat.")


def _bulat_int(g):
    for _ in range(12):
        a, b = g.r.sample(range(-10, 11), 2)
        g.pick(f"Mana yang lebih besar, {fmt(a)} atau {fmt(b)}?", max(a, b), [min(a, b), abs(min(a, b)) if abs(min(a, b)) != max(a, b) else max(a, b) + 1], f"Di garis bilangan, {fmt(max(a, b))} lebih ke kanan.", n=3)
        t = g.r.randint(-8, 12)
        d = g.r.randint(2, 9)
        g.pick(f"Suhu {fmt(t)}°C turun {d}°C menjadi …", f"{fmt(t - d)}°C", [f"{fmt(t + d)}°C", f"{fmt(d - t)}°C", f"{fmt(t - d + 1)}°C"], f"{fmt(t)} − {d} = {fmt(t - d)}.")


def _operasi_int(g):
    for _ in range(24):
        a, b = g.r.randint(-15, 15), g.r.randint(-15, 15)
        if b == 0:
            continue
        op = g.r.choice("+−×")
        val = a + b if op == "+" else a - b if op == "−" else a * b
        bb = f"({fmt(b)})" if b < 0 else fmt(b)
        g.pick(f"{fmt(a)} {op} {bb} = …", val, [-val if val else 1, val + 2, val - 2], f"{fmt(a)} {op} {bb} = {fmt(val)}.")


def _lingkaran(g):
    for r in (7, 14, 21, 3.5, 10, 20, 35, 28):
        if r in (10, 20):
            g.pick(f"Keliling lingkaran r = {fmt(float(r))} cm (π = 3,14) adalah …", f"{fmt(2 * 3.14 * r)} cm", [f"{fmt(3.14 * r * r)} cm", f"{fmt(3.14 * r)} cm", f"{fmt(4 * r)} cm"], f"K = 2 × 3,14 × {fmt(float(r))} = {fmt(2 * 3.14 * r)} cm.")
            g.pick(f"Luas lingkaran r = {fmt(float(r))} cm (π = 3,14) adalah …", f"{fmt(3.14 * r * r)} cm²", [f"{fmt(2 * 3.14 * r)} cm²", f"{fmt(3.14 * r)} cm²", f"{fmt(3.14 * r * r * 2)} cm²"], f"L = 3,14 × {fmt(float(r))} × {fmt(float(r))} = {fmt(3.14 * r * r)} cm².")
        else:
            k = Fraction(44, 7) * Fraction(r).limit_denominator()
            area = Fraction(22, 7) * Fraction(r).limit_denominator() ** 2
            g.pick(f"Keliling lingkaran r = {fmt(float(r))} cm (π = 22/7) adalah …", f"{fmt(float(k))} cm", [f"{fmt(float(area))} cm", f"{fmt(float(k / 2))} cm", f"{fmt(float(k + 7))} cm"], f"K = 2 × 22/7 × {fmt(float(r))} = {fmt(float(k))} cm.")
            g.pick(f"Luas lingkaran r = {fmt(float(r))} cm (π = 22/7) adalah …", f"{fmt(float(area))} cm²", [f"{fmt(float(k))} cm²", f"{fmt(float(area * 2))} cm²", f"{fmt(float(area / 2))} cm²"], f"L = 22/7 × {fmt(float(r))} × {fmt(float(r))} = {fmt(float(area))} cm².")
    g.pick("Diameter lingkaran yang jari-jarinya 9 cm adalah …", "18 cm", ["9 cm", "4,5 cm", "27 cm"], "d = 2 × r.")


def _mean(g):
    for _ in range(10):
        data = sorted(g.r.choices(range(5, 11), k=5))
        if len(set(data)) == 5:
            data[1] = data[2]
        mode = max(set(data), key=data.count)
        mean = Fraction(sum(data), 5)
        g.pick(f"Data: {', '.join(map(str, data))}. Mediannya …", data[2], [data[1] if data[1] != data[2] else data[2] + 1, data[3] if data[3] != data[2] else data[2] - 1, data[0]], "Data sudah urut, median = data ke-3.")
        g.pick(f"Data: {', '.join(map(str, data))}. Rata-ratanya …", fmt(float(mean)), [fmt(float(mean) + 1), fmt(float(mean) - 1), fmt(sum(data))], f"{sum(data)} : 5 = {fmt(float(mean))}.")
        if data.count(mode) > 1 and sum(1 for v in set(data) if data.count(v) == data.count(mode)) == 1:
            g.pick(f"Data: {', '.join(map(str, data))}. Modusnya …", mode, [v for v in sorted(set(data)) if v != mode] + [mode + 1], "Modus = data yang paling sering muncul.")


def _kali_pecahan(g):
    for _ in range(30):
        a, b = Fraction(g.r.randint(1, 4), g.r.randint(2, 6)), Fraction(g.r.randint(1, 4), g.r.randint(2, 6))
        if a.numerator >= a.denominator or b.numerator >= b.denominator:
            continue
        g.pick(f"{fmt(a)} × {fmt(b)} = …", fmt(a * b), [fmt(a + b), fmt(a / b), fmt(a * b + Fraction(1, 2))], f"Kalikan pembilang dan penyebut: {fmt(a * b)}.")
        g.pick(f"{fmt(a)} : {fmt(b)} = …", fmt(a / b), [fmt(a * b), fmt(b / a), fmt(a - b) if a != b else "1"], f"Dibagi = dikali kebalikan: {fmt(a)} × {fmt(1 / b)} = {fmt(a / b)}.")


def _rasio(g):
    for _ in range(10):
        a, b = g.r.randint(2, 9), g.r.randint(2, 9)
        if a == b:
            continue
        k = g.r.randint(2, 6)
        gcd = math.gcd(a, b)
        g.pick(f"Ada {a * k} kelereng merah dan {b * k} biru. Rasio merah : biru …", f"{a // gcd} : {b // gcd}", [f"{b // gcd} : {a // gcd}", f"{a * k} : {b}", f"{a + b} : {b}"], f"{a * k} : {b * k} disederhanakan menjadi {a // gcd} : {b // gcd}.")
        s = g.r.choice([100000, 200000, 500000, 1000000])
        cm = g.r.randint(2, 9)
        g.pick(f"Skala peta 1 : {fmt(s)}. Jarak di peta {cm} cm. Jarak sebenarnya …", f"{fmt(cm * s // 100000)} km", [f"{fmt(cm * s // 10000)} km", f"{fmt(cm * s // 1000000) if cm * s >= 1000000 else cm} m", f"{fmt(cm * s)} km"], f"{cm} × {fmt(s)} cm = {fmt(cm * s)} cm = {fmt(cm * s // 100000)} km.")


def _permukaan(g):
    for _ in range(10):
        s = g.r.randint(2, 12)
        g.pick(f"Luas permukaan kubus dengan rusuk {s} cm adalah …", f"{6 * s * s} cm²", [f"{s ** 3} cm²", f"{4 * s * s} cm²", f"{6 * s} cm²"], f"L = 6 × {s} × {s} = {6 * s * s} cm².")
        p, l, t = g.r.randint(3, 10), g.r.randint(2, 8), g.r.randint(2, 8)
        g.isi(f"Luas permukaan balok p = {p} cm, l = {l} cm, t = {t} cm adalah … cm²", 2 * (p * l + p * t + l * t), f"L = 2 × ({p}×{l} + {p}×{t} + {l}×{t}) = {2 * (p * l + p * t + l * t)}.")
    g.pick("Banyak persegi pada jaring-jaring kubus adalah …", 6, [4, 8, 12], "Kubus punya 6 sisi persegi.")


def _peluang(g):
    events = [("dadu muncul angka 3", Fraction(1, 6)), ("dadu muncul angka genap", Fraction(1, 2)), ("dadu muncul angka lebih dari 4", Fraction(1, 3)), ("koin muncul gambar", Fraction(1, 2)), ("dadu muncul angka prima", Fraction(1, 2)), ("dadu muncul angka 7", Fraction(0)), ("dadu muncul angka 1 sampai 6", Fraction(1))]
    for e, p in events:
        g.pick(f"Peluang {e} adalah …", fmt(p), [fmt(x) for x in (Fraction(1, 6), Fraction(1, 2), Fraction(1, 3), Fraction(0), Fraction(1), Fraction(2, 3)) if x != p][:3], f"Peluang {e} = {fmt(p)}.")
    for _ in range(8):
        r, b = g.r.randint(1, 6), g.r.randint(1, 6)
        p = Fraction(r, r + b)
        g.pick(f"Kantong berisi {r} kelereng merah dan {b} biru. Peluang terambil merah …", fmt(p), [fmt(Fraction(b, r + b)) if b != r else fmt(Fraction(1, r + b)), fmt(Fraction(r, b)) if r != b else "1", f"{r}/{r + b + 1}"], f"{r} dari {r + b} kelereng: {fmt(p)}.")
    for n in (60, 120, 300):
        g.pick(f"Dadu dilempar {n} kali. Frekuensi harapan muncul angka 6 adalah …", n // 6, [n // 2, n // 3, n // 12], f"1/6 × {n} = {n // 6}.")


def _aljabar(g):
    for _ in range(12):
        a, b, c = g.r.randint(2, 9), g.r.randint(2, 9), g.r.randint(1, 9)
        g.pick(f"{a}x + {b}x = …", f"{a + b}x", [f"{a * b}x", f"{a + b}x²", f"{a + b}"], "Jumlahkan koefisien suku sejenis.")
        g.pick(f"Koefisien x pada {a}x + {c} adalah …", a, [c, a + c, 1], "Koefisien = angka di depan variabel.")
        x = g.r.randint(1, 6)
        g.isi(f"Nilai {a}x + {c} untuk x = {x} adalah …", a * x + c, f"{a} × {x} + {c} = {a * x + c}.")


def _plsv(g):
    for _ in range(14):
        x, a, b = g.r.randint(-5, 12), g.r.randint(2, 7), g.r.randint(1, 15)
        c = a * x + b
        g.pick(f"Penyelesaian {a}x + {b} = {fmt(c)} adalah …", f"x = {fmt(x)}", [f"x = {fmt(x + 1)}", f"x = {fmt(-x) if x else 2}", f"x = {fmt(c - b)}"], f"{a}x = {fmt(c)} − {b} = {fmt(c - b)}, x = {fmt(x)}.")
        g.isi(f"Jika x + {b} = {fmt(x + b)}, maka x = …", x, f"x = {fmt(x + b)} − {b} = {fmt(x)}.")


def _senilai_berbalik(g):
    for _ in range(10):
        n, p = g.r.randint(2, 6), g.r.choice([2000, 2500, 3000, 4000, 5000])
        m = g.r.randint(7, 12)
        g.pick(f"Harga {n} buku Rp{fmt(n * p)}. Harga {m} buku …", f"Rp{fmt(m * p)}", [f"Rp{fmt(n * p + m)}", f"Rp{fmt(m * p + p)}", f"Rp{fmt((m - 1) * p)}"], f"Senilai: 1 buku Rp{fmt(p)}, jadi {m} buku Rp{fmt(m * p)}.")
        w, d = g.r.choice([(4, 12), (6, 10), (3, 20), (5, 12), (8, 9)])
        w2 = g.r.choice([x for x in (2, 3, 4, 6, 8, 10, 12) if (w * d) % x == 0 and x != w])
        g.pick(f"{w} pekerja menyelesaikan rumah dalam {d} hari. Jika {w2} pekerja, waktunya …", f"{w * d // w2} hari", [f"{d * w2 // w} hari" if d * w2 // w != w * d // w2 else f"{d + 1} hari", f"{d} hari", f"{w * d} hari"], f"Berbalik nilai: {w} × {d} = {w * d}, {w * d} : {w2} = {w * d // w2} hari.")


def _faktor_prima(g):
    for n in (12, 18, 20, 24, 28, 30, 36, 40, 45, 48, 50, 60, 72, 84, 90, 100):
        fs, m, p = [], n, 2
        while m > 1:
            while m % p == 0:
                fs.append(p)
                m //= p
            p += 1
        txt = " × ".join(f"{q}{'²' if fs.count(q) == 2 else '³' if fs.count(q) == 3 else ''}" for q in sorted(set(fs)))
        wrong = [" × ".join(map(str, fs[:-1])) + f" × {fs[-1] + 1}", f"{n // 2} × 2", " × ".join(str(q) for q in sorted(set(fs)))]
        g.pick(f"Faktorisasi prima dari {n} adalah …", txt, [w for w in wrong if w != txt], f"{n} = {' × '.join(map(str, fs))} = {txt}.")
    g.pick("Bilangan prima terkecil adalah …", "2", ["1", "3", "0"], "2 adalah bilangan prima terkecil.")
    g.pick("Bilangan prima di antara berikut adalah …", "17", ["21", "27", "15"], "17 hanya habis dibagi 1 dan 17.")


def _rasional(g):
    for _ in range(10):
        a, b = sorted(g.r.sample([-2.5, -1.5, -0.75, -0.5, 0.25, 0.5, 1.25, 1.5, 2.75], 2))
        g.pick(f"Mana yang lebih kecil, {fmt(a)} atau {fmt(b)}?", fmt(a), [fmt(b), "sama besar"], f"{fmt(a)} lebih ke kiri di garis bilangan.", n=3)
    for f, d in [(Fraction(3, 4), "0,75"), (Fraction(2, 5), "0,4"), (Fraction(7, 4), "1,75"), (Fraction(1, 8), "0,125"), (Fraction(5, 2), "2,5"), (Fraction(3, 5), "0,6"), (Fraction(9, 4), "2,25"), (Fraction(1, 20), "0,05")]:
        g.pick(f"Bentuk desimal {fmt(f)} adalah …", d, ["0,34", "1,5", "0,8", "2,25"], f"{fmt(f)} = {d}.")


def _sebangun(g):
    for _ in range(10):
        t, s = g.r.randint(1, 3), g.r.randint(2, 4)
        k = g.r.randint(3, 8)
        g.pick(f"Tongkat {t} m membentuk bayangan {t * s} m. Pada saat sama, bayangan tiang {t * s * k} m. Tinggi tiang …", f"{t * k} m", [f"{t * s * k} m", f"{t * k + s} m", f"{k} m" if k != t * k else f"{k + 1} m"], f"Perbandingan tinggi : bayangan = 1 : {s}, jadi tiang = {t * s * k} : {s} = {t * k} m.")
        a, k2 = g.r.randint(3, 8), g.r.randint(2, 4)
        g.isi(f"Dua segitiga sebangun dengan faktor skala {k2}. Sisi segitiga kecil {a} cm, sisi yang bersesuaian pada segitiga besar … cm", a * k2, f"{a} × {k2} = {a * k2}.")


def _diag_lingkaran(g):
    for _ in range(10):
        total = g.r.choice([20, 30, 36, 40, 60, 120])
        part = g.r.choice([d for d in range(1, total) if (360 * d) % total == 0])
        deg = 360 * part // total
        g.pick(f"Dari {total} siswa, {part} suka basket. Sudut juring basket pada diagram lingkaran …", f"{deg}°", [f"{deg + 10}°", f"{part}°", f"{180 - deg if 180 - deg > 0 else deg + 20}°"], f"{part}/{total} × 360° = {deg}°.")
        pct = 100 * part / total
        if pct.is_integer():
            g.isi(f"Dari {total} siswa, {part} suka basket. Persentasenya … %", int(pct), f"{part}/{total} × 100% = {int(pct)}%.")


def _pythagoras(g):
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25), (12, 16, 20), (20, 21, 29), (15, 20, 25)]
    for a, b, c in triples:
        g.pick(f"Sisi tegak segitiga siku-siku {a} cm dan {b} cm. Sisi miringnya …", f"{c} cm", [f"{a + b} cm", f"{c + 1} cm", f"{b + 1} cm"], f"c² = {a}² + {b}² = {a * a + b * b}, c = {c}.")
        g.pick(f"Sisi miring {c} cm dan salah satu sisi tegak {a} cm. Sisi tegak lainnya …", f"{b} cm", [f"{c - a} cm", f"{b + 2} cm", f"{a} cm"], f"b² = {c}² − {a}² = {b * b}, b = {b}.")


def _tripel(g):
    for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]:
        g.bs(f"{a}, {b}, {c} merupakan tripel Pythagoras.", True, f"{a}² + {b}² = {c}².")
        g.bs(f"{a}, {b}, {c + 1} merupakan tripel Pythagoras.", False, f"{a}² + {b}² = {c * c}, bukan {(c + 1) ** 2}.")
    for a, b, c in [(6, 8, 10), (9, 12, 15), (12, 16, 20), (5, 12, 13), (8, 15, 17)]:
        g.pick(f"Tangga {c} m bersandar di tembok. Jarak kaki tangga ke tembok {a} m. Tinggi ujung tangga …", f"{b} m", [f"{c - a} m", f"{a + b} m", f"{b + 2} m"], f"√({c}² − {a}²) = {b} m.")


def _pola_bil(g):
    for n in range(4, 9):
        g.pick(f"Pola persegi: 1, 4, 9, 16, … Suku ke-{n} adalah …", n * n, [n * n + 1, 2 * n, (n - 1) ** 2], f"Suku ke-n = n², jadi {n}² = {n * n}.")
        g.pick(f"Pola segitiga: 1, 3, 6, 10, … Suku ke-{n} adalah …", n * (n + 1) // 2, [n * n, n * (n - 1) // 2, n * (n + 1)], f"Suku ke-n = n(n + 1)/2 = {n * (n + 1) // 2}.")
    for _ in range(6):
        a, d = g.r.randint(1, 10), g.r.randint(2, 7)
        n = g.r.randint(6, 15)
        g.pick(f"Barisan {a}, {a + d}, {a + 2 * d}, … Suku ke-{n} adalah …", a + (n - 1) * d, [a + n * d, a * n, a + (n - 2) * d], f"U{n} = {a} + ({n} − 1) × {d} = {a + (n - 1) * d}.")


def _gradien(g):
    for _ in range(12):
        x1, y1 = g.r.randint(-4, 4), g.r.randint(-4, 4)
        m = g.r.choice([-3, -2, -1, 1, 2, 3])
        dx = g.r.randint(1, 3)
        x2, y2 = x1 + dx, y1 + m * dx
        g.pick(f"Gradien garis melalui ({fmt(x1)}, {fmt(y1)}) dan ({fmt(x2)}, {fmt(y2)}) adalah …", m, [-m, m * 2, Fraction(1, m) if abs(m) > 1 else m + 2], f"m = ({fmt(y2)} − {fmt(y1)}) : ({fmt(x2)} − {fmt(x1)}) = {fmt(m)}.")
        c = g.r.randint(-5, 5)
        g.pick(f"Gradien garis y = {fmt(m)}x {'+' if c >= 0 else '−'} {abs(c)} adalah …", m, [c if c != m else m + 1, -m, 1 if m != 1 else 2], "Pada y = mx + c, gradien = m.")


def _fungsi(g):
    for _ in range(18):
        a, b = g.r.randint(2, 6), g.r.randint(-5, 8)
        x = g.r.randint(-3, 6)
        g.pick(f"f(x) = {a}x {'+' if b >= 0 else '−'} {abs(b)}. Nilai f({fmt(x)}) = …", a * x + b, [a * x - b, a + x + b, a * (x + 1) + b], f"f({fmt(x)}) = {a} × {fmt(x)} {'+' if b >= 0 else '−'} {abs(b)} = {fmt(a * x + b)}.")
    g.bs("Pada fungsi, setiap anggota domain punya tepat satu pasangan.", True, "Itu syarat fungsi.")
    g.bs("Relasi {(1, 2), (1, 3)} merupakan fungsi.", False, "1 punya dua pasangan.")


def _ptlsv(g):
    for _ in range(12):
        a, x, b = g.r.randint(2, 6), g.r.randint(-3, 8), g.r.randint(1, 10)
        g.pick(f"Penyelesaian {a}x + {b} > {fmt(a * x + b)} adalah …", f"x > {fmt(x)}", [f"x < {fmt(x)}", f"x > {fmt(x + 1)}", f"x ≥ {fmt(x)}"], f"{a}x > {fmt(a * x)}, x > {fmt(x)}.")
        g.pick(f"Penyelesaian −{a}x ≤ {fmt(-a * x)} adalah …", f"x ≥ {fmt(x)}", [f"x ≤ {fmt(x)}", f"x ≥ {fmt(-x) if x else 1}", f"x < {fmt(x)}"], "Dibagi bilangan negatif, tanda dibalik.")


def _pemusatan(g):
    _mean(g)


def _penyebaran(g):
    for _ in range(12):
        data = sorted(g.r.sample(range(50, 100), 7))
        g.pick(f"Data: {', '.join(map(str, data))}. Jangkauannya …", data[-1] - data[0], [data[-1], data[3], data[-1] - data[1]], f"{data[-1]} − {data[0]} = {data[-1] - data[0]}.")
        g.pick(f"Data: {', '.join(map(str, data))}. Kuartil tengah (Q2) adalah …", data[3], [data[2], data[4], data[0]], "7 data urut, Q2 = data ke-4.")


def _pangkat(g):
    for _ in range(10):
        a, m, n = g.r.randint(2, 5), g.r.randint(2, 5), g.r.randint(1, 4)
        g.pick(f"{a}{_sup(m)} × {a}{_sup(n)} = …", f"{a}{_sup(m + n)}", [f"{a}{_sup(m * n)}", f"{a * a}{_sup(m + n)}", f"{a}{_sup(abs(m - n) or 1)}"], "Basis sama dikali, pangkat dijumlahkan.")
        g.pick(f"({a}{_sup(m)}){_sup(n)} = …", f"{a}{_sup(m * n)}", [f"{a}{_sup(m + n)}", f"{a * n}{_sup(m)}", f"{a}{_sup(m)}"], "Pangkat dipangkatkan, pangkatnya dikalikan.")
        g.isi(f"Nilai {a}{_sup(m)} = …", a ** m, f"{' × '.join([str(a)] * m)} = {a ** m}.")


_SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def _sup(n):
    return str(n).translate(_SUP)


def _akar(g):
    for n in (4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144):
        g.pick(f"√{n} = …", int(math.isqrt(n)), [int(math.isqrt(n)) + 1, n // 2, int(math.isqrt(n)) - 1], f"{int(math.isqrt(n))} × {int(math.isqrt(n))} = {n}.")
    for k, m in [(2, 3), (3, 2), (5, 2), (2, 5), (4, 3), (6, 2)]:
        g.pick(f"Bentuk sederhana √{k * k * m} adalah …", f"{k}√{m}", [f"{m}√{k}", f"{k * k}√{m}", f"√{k + m}"], f"√{k * k * m} = √({k * k} × {m}) = {k}√{m}.")


def _kuadrat(g):
    for _ in range(24):
        p, q = g.r.sample(range(-6, 7), 2)
        b, c = -(p + q), p * q
        eq = f"x² {'+' if b >= 0 else '−'} {abs(b)}x {'+' if c >= 0 else '−'} {abs(c)} = 0".replace(" + 0x", "").replace(" − 0x", "")
        g.pick(f"Akar-akar {eq} adalah …", f"{fmt(min(p, q))} dan {fmt(max(p, q))}", [f"{fmt(-max(p, q))} dan {fmt(-min(p, q))}", f"{fmt(min(p, q) + 1)} dan {fmt(max(p, q) + 1)}", f"{fmt(c)} dan {fmt(b)}"], f"Faktorkan: (x − ({fmt(p)}))(x − ({fmt(q)})) = 0.")


def _spldv(g):
    for _ in range(12):
        x, y = g.r.randint(1, 9), g.r.randint(1, 9)
        g.pick(f"Penyelesaian x + y = {x + y} dan x − y = {fmt(x - y)} adalah …", f"x = {x}, y = {y}", [f"x = {y}, y = {x}" if x != y else f"x = {x + 1}, y = {y - 1}", f"x = {x + 1}, y = {y}", f"x = {x}, y = {y + 1}"], f"Jumlahkan: 2x = {2 * x}, x = {x}, y = {y}.")
        a, b = g.r.randint(1000, 5000) // 500 * 500, g.r.randint(1000, 5000) // 500 * 500
        g.pick(f"2 pensil dan 1 buku Rp{fmt(2 * a + b)}. 1 pensil dan 1 buku Rp{fmt(a + b)}. Harga 1 pensil …", f"Rp{fmt(a)}", [f"Rp{fmt(b)}" if a != b else f"Rp{fmt(a + 500)}", f"Rp{fmt(a + b)}", f"Rp{fmt(a * 2)}"], f"Selisih kedua persamaan = 1 pensil = Rp{fmt(a)}.")


def _transformasi(g):
    for _ in range(12):
        x, y = g.r.randint(-6, 6), g.r.randint(-6, 6)
        a, b = g.r.randint(-4, 4), g.r.randint(-4, 4)
        g.pick(f"Titik ({fmt(x)}, {fmt(y)}) ditranslasi ({fmt(a)}, {fmt(b)}) menjadi …", f"({fmt(x + a)}, {fmt(y + b)})", [f"({fmt(x - a)}, {fmt(y - b)})", f"({fmt(x + b)}, {fmt(y + a)})", f"({fmt(x * a)}, {fmt(y * b)})" if (x * a, y * b) != (x + a, y + b) else f"({fmt(x)}, {fmt(y)})"], f"({fmt(x)} + {fmt(a)}, {fmt(y)} + {fmt(b)}).")
        g.pick(f"Titik ({fmt(x)}, {fmt(y)}) dicerminkan terhadap sumbu x menjadi …", f"({fmt(x)}, {fmt(-y)})", [f"({fmt(-x)}, {fmt(y)})", f"({fmt(-x)}, {fmt(-y)})", f"({fmt(y)}, {fmt(x)})"], "Cermin sumbu x: (x, y) → (x, −y).")


def _tabung(g):
    for r, t in [(7, 10), (14, 5), (7, 20), (21, 10), (3.5, 8), (14, 12), (7, 4), (28, 10), (21, 5)]:
        rf = Fraction(r).limit_denominator()
        v = Fraction(22, 7) * rf * rf * t
        lp = 2 * Fraction(22, 7) * rf * (rf + t)
        g.pick(f"Volume tabung r = {fmt(float(r))} cm, t = {t} cm (π = 22/7) adalah …", f"{fmt(float(v))} cm³", [f"{fmt(float(v / 2))} cm³", f"{fmt(float(lp))} cm³", f"{fmt(float(v * 2))} cm³"], f"V = 22/7 × {fmt(float(r))}² × {t} = {fmt(float(v))} cm³.")
        g.pick(f"Luas permukaan tabung r = {fmt(float(r))} cm, t = {t} cm (π = 22/7) adalah …", f"{fmt(float(lp))} cm²", [f"{fmt(float(v))} cm²", f"{fmt(float(lp / 2))} cm²", f"{fmt(float(lp + 44))} cm²"], f"L = 2πr(r + t) = {fmt(float(lp))} cm².")


def _kerucut(g):
    for r, t in [(7, 24), (3, 4), (6, 8), (14, 48), (5, 12), (9, 12), (12, 16), (15, 20)]:
        s = math.isqrt(r * r + t * t)
        vk = Fraction(1, 3) * Fraction(22, 7) * r * r * t
        g.pick(f"Garis pelukis kerucut r = {r} cm, t = {t} cm adalah …", f"{s} cm", [f"{r + t} cm", f"{s + 1} cm", f"{t} cm"], f"s = √({r}² + {t}²) = {s} cm.")
        g.pick(f"Volume kerucut r = {r} cm, t = {t} cm (π = 22/7) adalah …", f"{fmt(float(vk))} cm³", [f"{fmt(float(vk * 3))} cm³", f"{fmt(float(vk / 2))} cm³", f"{fmt(float(vk + 22))} cm³"], f"V = 1/3 × 22/7 × {r}² × {t} = {fmt(float(vk))} cm³.")
    for r in (7, 14, 21):
        vb = Fraction(4, 3) * Fraction(22, 7) * r ** 3
        g.pick(f"Volume bola r = {r} cm (π = 22/7) adalah …", f"{fmt(float(vb))} cm³", [f"{fmt(float(vb / 2))} cm³", f"{fmt(float(4 * Fraction(22, 7) * r * r))} cm³", f"{fmt(float(vb * 2))} cm³"], f"V = 4/3 × 22/7 × {r}³ = {fmt(float(vb))} cm³.")


def _tabel(g):
    _diagram(g)


GENS = {
    (1, "Membilang sampai 20"): _bilang, (1, "Membandingkan bilangan"): _banding, (1, "Penjumlahan sampai 20"): _tambah(20),
    (1, "Pengurangan sampai 20"): _tambah(20, minus=True), (1, "Bangun datar di sekitarku"): _bentuk, (1, "Mengelompokkan benda menurut bentuk"): _bentuk,
    (1, "Membandingkan panjang benda"): _ukur, (1, "Diagram gambar"): _diagram,
    (2, "Nilai tempat puluhan dan satuan"): _place(10, 99), (2, "Membandingkan dan mengurutkan bilangan"): _banding, (2, "Penjumlahan sampai 100"): _tambah(100),
    (2, "Pengurangan sampai 100"): _tambah(100, minus=True), (2, "Mengukur panjang"): _ukur, (2, "Bangun ruang di sekitar kita"): _ruang,
    (2, "Pola gambar dan bilangan"): _pola, (2, "Pecahan setengah dan seperempat"): _pecahan_dasar, (2, "Membaca diagram batang sederhana"): _diagram,
    (3, "Nilai tempat ratusan"): _place(100, 999), (3, "Penjumlahan dan pengurangan sampai 1.000"): _tambah(1000, thou=True),
    (3, "Perkalian sebagai penjumlahan berulang"): _kali, (3, "Pembagian sebagai berbagi sama banyak"): _bagi, (3, "Kalimat matematika"): _kalimat,
    (3, "Mengukur panjang dan berat"): _ukur, (3, "Sisi dan sudut bangun datar"): _bentuk, (3, "Penyajian data dalam tabel"): _tabel,
    (4, "Bilangan sampai 10.000"): _place(1000, 9999), (4, "Kelipatan dan faktor"): _kelfak, (4, "Mengenal pecahan"): _pecahan_dasar,
    (4, "Keliling dan luas persegi panjang"): _luas_pp, (4, "Pecahan desimal dan persen"): _desimal, (4, "Pola gambar dan pola bilangan"): _pola,
    (4, "Ciri-ciri segi empat"): _segiempat, (4, "Piktogram dan diagram batang"): _diagram,
    (5, "Pecahan senilai"): _senilai, (5, "Penjumlahan dan pengurangan pecahan"): _jumlah_pecahan, (5, "KPK dan FPB"): _klpk,
    (5, "Volume kubus dan balok"): _volume_balok, (5, "Bilangan cacah sampai 100.000"): _place(10000, 99999), (5, "Pembulatan dan taksiran"): _bulat,
    (5, "Keliling dan luas segitiga"): _luas_seg, (5, "Mengukur dan menggambar sudut"): _sudut,
    (6, "Mengenal bilangan bulat"): _bulat_int, (6, "Operasi hitung bilangan bulat"): _operasi_int, (6, "Keliling dan luas lingkaran"): _lingkaran,
    (6, "Mean, median, dan modus"): _mean, (6, "Perkalian dan pembagian pecahan"): _kali_pecahan, (6, "Rasio dan skala"): _rasio,
    (6, "Jaring-jaring dan luas permukaan"): _permukaan, (6, "Peluang sederhana"): _peluang,
    (7, "Bentuk aljabar"): _aljabar, (7, "Persamaan linear satu variabel"): _plsv, (7, "Perbandingan senilai dan berbalik nilai"): _senilai_berbalik,
    (7, "Sudut dan garis"): _sudut, (7, "Faktor prima dan faktorisasi"): _faktor_prima, (7, "Bilangan rasional"): _rasional,
    (7, "Kesebangunan segitiga"): _sebangun, (7, "Diagram batang dan diagram lingkaran"): _diag_lingkaran,
    (8, "Teorema Pythagoras"): _pythagoras, (8, "Tripel dan penerapan Pythagoras"): _tripel, (8, "Pola bilangan"): _pola_bil,
    (8, "Gradien dan persamaan garis lurus"): _gradien, (8, "Relasi dan fungsi"): _fungsi, (8, "Pertidaksamaan linear satu variabel"): _ptlsv,
    (8, "Ukuran pemusatan data"): _pemusatan, (8, "Ukuran penyebaran data"): _penyebaran,
    (9, "Bilangan berpangkat"): _pangkat, (9, "Bentuk akar"): _akar, (9, "Persamaan kuadrat"): _kuadrat, (9, "Peluang"): _peluang,
    (9, "Sistem persamaan linear dua variabel"): _spldv, (9, "Transformasi geometri"): _transformasi,
    (9, "Luas permukaan dan volume tabung"): _tabung, (9, "Volume kerucut dan bola"): _kerucut,
}


def generate(grade: int, title: str) -> list[Q]:
    fn = GENS.get((grade, title))
    if fn is None:
        return []
    g = G(f"{grade}|{title}")
    fn(g)
    return g.qs


def _bilang10(g):
    icons = "🍎⭐⚽🐟🌸🚗🍌🎈🐤🧸"
    words = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"]
    for n in range(1, 11):
        ic = icons[n - 1]
        g.pick(f"Ada berapa {ic}? {ic * n}", n, [n - 1 or 2, n + 1, n + 2], f"Hitung satu per satu, ada {n}.")
        g.pick(f"Lambang bilangan {words[n - 1]} adalah …", n, [n % 10 + 1, (n + 2) % 10 + 1, (n + 5) % 10 + 1], f"{words[n - 1].capitalize()} ditulis {n}.")
        g.isi(f"Angka {n} dibaca …", words[n - 1], f"{n} dibaca {words[n - 1]}.")


def _pola1(g):
    pats = [("🔴", "🔵"), ("⭐", "🌙"), ("🍎", "🍌"), ("🐱", "🐶"), ("🟥", "🟨"), ("🌸", "🍀")]
    for a, b in pats:
        g.pick(f"Lanjutkan pola: {a} {b} {a} {b} {a} …", b, [a, "🟢", "⚪"], f"Polanya bergantian {a} {b}, jadi berikutnya {b}.", n=3)
        g.pick(f"Lanjutkan pola: {a} {a} {b} {a} {a} …", b, [a, "🟢"], f"Polanya dua {a} lalu satu {b}.", n=3)
    for _ in range(8):
        a, d = g.r.randint(1, 6), g.r.choice([1, 2])
        seq = [a + d * i for i in range(5)]
        g.pick(f"Lanjutkan pola: {', '.join(map(str, seq[:4]))}, …", seq[4], [seq[4] + 1, seq[3], seq[4] + 2], f"Setiap langkah bertambah {d}.")
        g.isi(f"Pola: {seq[0]}, {seq[1]}, …, {seq[3]}. Bilangan yang hilang …", seq[2], f"Setiap langkah bertambah {d}.")


def _bil100(g):
    tens = ["sepuluh", "dua puluh", "tiga puluh", "empat puluh", "lima puluh", "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]
    ones = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
    for _ in range(14):
        n = g.r.randint(21, 99)
        t, o = divmod(n, 10)
        word = tens[t - 1] + (" " + ones[o] if o else "")
        g.pick(f"Bilangan {word} ditulis …", n, [o * 10 + t if o else n + 10, n + 1, n - 10], f"{word.capitalize()} ditulis {n}.")
        g.pick(f"Bilangan setelah {n} adalah …", n + 1, [n - 1, n + 10, n + 2], f"Setelah {n} adalah {n + 1}.")
        g.isi(f"Lanjutkan hitungan puluhan: {(t - 1) * 10 or 10}, {t * 10}, …", t * 10 + 10 if t > 1 else 20, "Hitung loncat sepuluh-sepuluh.")
    g.isi("Sepuluh puluhan sama dengan …", 100, "10 puluhan = 100.")


def _jengkal(g):
    objs = [("meja", 6), ("papan tulis", 12), ("buku", 2), ("pintu", 5), ("karpet", 9), ("lemari", 7)]
    for _ in range(8):
        (a, x), (b, y) = g.r.sample(objs, 2)
        g.pick(f"Panjang {a} {x} jengkal, panjang {b} {y} jengkal. Mana yang lebih panjang?", a if x > y else b, [b if x > y else a, "sama panjang"], f"{max(x, y)} jengkal lebih panjang dari {min(x, y)} jengkal.", n=3)
        g.isi(f"Panjang {a} {x} jengkal dan {b} {y} jengkal. Selisihnya … jengkal", abs(x - y), f"{max(x, y)} − {min(x, y)} = {abs(x - y)}.")
    for a in ["jengkal", "langkah kaki", "depa", "hasta"]:
        g.bs(f"{a.capitalize()} termasuk satuan tidak baku.", True, f"{a.capitalize()} berbeda-beda untuk tiap orang, jadi tidak baku.")
    g.pick("Hasil mengukur dengan jengkal bisa berbeda karena …", "panjang jengkal tiap orang berbeda", ["bendanya berubah", "jengkal selalu sama", "salah menghitung saja"], "Tangan setiap orang tidak sama besar.")


def _berat(g):
    pairs = [("gajah", "kucing"), ("batu bata", "bulu ayam"), ("semangka", "anggur"), ("tas penuh buku", "tas kosong"), ("sapi", "ayam"), ("galon air", "gelas plastik"), ("kelapa", "kelereng"), ("meja kayu", "pensil")]
    for a, b in pairs:
        g.pick(f"Mana yang lebih berat, {a} atau {b}?", a, [b, "sama berat"], f"{a.capitalize()} lebih berat dari {b}.", n=3)
        g.bs(f"{b.capitalize()} lebih ringan dari {a}.", True, f"{b.capitalize()} lebih ringan.")
    g.pick("Alat untuk mengetahui berat benda adalah …", "timbangan", ["penggaris", "jam", "termometer"], "Berat benda diukur dengan timbangan.")
    g.pick("Pada timbangan dua lengan, sisi yang turun berarti bendanya …", "lebih berat", ["lebih ringan", "sama berat", "lebih panjang"], "Sisi yang lebih berat akan turun.")


def _jam(g):
    for h in range(1, 13):
        g.pick(f"Jarum pendek menunjuk angka {h} dan jarum panjang menunjuk angka 12. Pukul berapa?", f"pukul {h}", [f"pukul {h % 12 + 1}", f"pukul 12", f"pukul {(h + 5) % 12 + 1}"], f"Jarum panjang di 12 berarti tepat. Jarum pendek di {h}, jadi pukul {h}.")
    g.pick("Jarum yang menunjukkan jam adalah jarum …", "pendek", ["panjang", "detik", "tengah"], "Jarum pendek menunjukkan jam.")
    g.pick("Saat jam tepat, jarum panjang menunjuk angka …", "12", ["6", "3", "1"], "Jam tepat: jarum panjang di angka 12.")
    g.isi("Banyak angka pada jam dinding ada …", 12, "Jam dinding berisi angka 1 sampai 12.")


def _hari(g):
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    for i, d in enumerate(days):
        nxt, prv = days[(i + 1) % 7], days[i - 1]
        g.pick(f"Hari sesudah {d} adalah …", nxt, [prv, days[(i + 2) % 7], days[(i + 3) % 7]], f"Sesudah {d} adalah {nxt}.")
        g.pick(f"Hari sebelum {d} adalah …", prv, [nxt, days[(i + 2) % 7], days[i - 2]], f"Sebelum {d} adalah {prv}.")
    g.isi("Banyak hari dalam satu minggu ada …", 7, "Satu minggu ada 7 hari.")
    g.pick("Hari libur sekolah biasanya hari …", "Minggu", ["Senin", "Rabu", "Kamis"], "Hari Minggu biasanya libur.")


GENS.update({
    (1, "Bilangan 1 sampai 10"): _bilang10, (1, "Bilangan sebelum dan sesudah"): _bilang, (1, "Penjumlahan sampai 10"): _tambah(10),
    (1, "Pengurangan sampai 10"): _tambah(10, minus=True), (1, "Bangun ruang di sekitarku"): _ruang, (1, "Pola gambar dan bilangan kecil"): _pola1,
    (1, "Puluhan dan satuan"): _place(10, 99), (1, "Bilangan sampai 100"): _bil100, (1, "Mengukur panjang dengan jengkal"): _jengkal,
    (1, "Berat dan ringan benda"): _berat, (1, "Membaca jam tepat"): _jam, (1, "Nama hari dalam seminggu"): _hari,
})
