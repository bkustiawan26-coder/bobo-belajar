import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("BOBO_JWT_SECRET", "x" * 40)

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from xml.sax.saxutils import escape

from app.seed.full import arrange, load_grade, topic_semesters

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DVB", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB")

NAMES = {
    "MAT": "Matematika", "BIN": "Bahasa Indonesia", "IPAS": "IPAS", "IPA": "Ilmu Pengetahuan Alam", "IPS": "Ilmu Pengetahuan Sosial",
    "PPK": "Pendidikan Pancasila", "BIG": "Bahasa Inggris", "SBD": "Seni dan Budaya", "PJOK": "PJOK",
    "INF": "Informatika", "KKA": "Koding dan Kecerdasan Artifisial",
}
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
WORD = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
INK = colors.HexColor("#1F2937")
ACCENT = colors.HexColor("#0F766E")
SOFT = colors.HexColor("#E6F4F1")
LINE = colors.HexColor("#CBD5E1")

S = {
    "title": ParagraphStyle("title", fontName="DVB", fontSize=20, leading=26, alignment=TA_CENTER, textColor=ACCENT),
    "sub": ParagraphStyle("sub", fontName="DVB", fontSize=13, leading=18, alignment=TA_CENTER, textColor=INK),
    "center": ParagraphStyle("center", fontName="DV", fontSize=10, leading=14, alignment=TA_CENTER, textColor=INK),
    "h1": ParagraphStyle("h1", fontName="DVB", fontSize=13, leading=17, textColor=ACCENT, spaceBefore=6, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName="DVB", fontSize=11, leading=15, textColor=INK, spaceBefore=8, spaceAfter=4),
    "body": ParagraphStyle("body", fontName="DV", fontSize=10, leading=14, textColor=INK),
    "small": ParagraphStyle("small", fontName="DV", fontSize=8.5, leading=11, textColor=INK),
    "smallb": ParagraphStyle("smallb", fontName="DVB", fontSize=8.5, leading=11, textColor=colors.white),
    "q": ParagraphStyle("q", fontName="DV", fontSize=10, leading=14, textColor=INK, leftIndent=16, firstLineIndent=-16),
    "opt": ParagraphStyle("opt", fontName="DV", fontSize=9.5, leading=13, textColor=INK, leftIndent=14, firstLineIndent=-14),
}


def p(text, style="body"):
    return Paragraph(text, S[style])


def esc(text):
    return escape(text).replace("\n", "<br/>")


def ranges(nums):
    if not nums:
        return "–"
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:] + [None]:
        if n is not None and n == prev + 1:
            prev = n
            continue
        out.append(str(start) if start == prev else f"{start}–{prev}")
        if n is not None:
            start = prev = n
    return ", ".join(out)


def unit(s, sem):
    flat = [t for c in s.chapters for t in c.topics]
    sems = topic_semesters(s)
    qs = [q for q in s.exam if sems[q.topic] == sem]
    pg = [q for q in qs if q.type == "mc"]
    isian = [q for q in qs if q.type == "fill"]
    return flat, pg, isian


def kisi(s, sem):
    flat, pg, isian = unit(s, sem)
    order = []
    for q in pg + isian:
        if q.topic not in order:
            order.append(q.topic)
    rows = [[p("No", "smallb"), p("Materi", "smallb"), p("Indikator Soal", "smallb"), p("No. PG", "smallb"), p("No. Isian", "smallb")]]
    for i, t in enumerate(order, 1):
        topic = flat[t]
        rows.append([
            p(str(i), "small"), p(esc(topic.title), "small"), p(esc(topic.lesson.summary), "small"),
            p(ranges([k + 1 for k, q in enumerate(pg) if q.topic == t]), "small"),
            p(ranges([k + 1 for k, q in enumerate(isian) if q.topic == t]), "small"),
        ])
    tbl = Table(rows, colWidths=[9 * mm, 42 * mm, 83 * mm, 22 * mm, 20 * mm], repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT), ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, SOFT]),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return [p(NAMES[s.code].upper(), "h2"), tbl]


def header(n, name):
    rows = [
        [p("Nama", "body"), p(": " + "." * 48, "body"), p("Kelas", "body"), p(f": {ROMAN[n]} ({WORD[n]})", "body")],
        [p("Mata Pelajaran", "body"), p(": " + esc(name), "body"), p("Nilai", "body"), p(": " + "." * 12, "body")],
    ]
    tbl = Table(rows, colWidths=[34 * mm, 76 * mm, 18 * mm, 46 * mm])
    tbl.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.6, LINE), ("BACKGROUND", (0, 0), (-1, -1), SOFT), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    return tbl


def soal(n, s, sem):
    _, pg, isian = unit(s, sem)
    out = [p(NAMES[s.code].upper(), "h1"), header(n, NAMES[s.code]), Spacer(1, 6), p("<b>A. Pilihan Ganda</b>", "h2"),
           p("Berilah tanda silang (X) pada huruf A, B, C, atau D di depan jawaban yang paling tepat!", "small"), Spacer(1, 4)]
    keys = []
    for k, q in enumerate(pg, 1):
        options, answer = arrange(q)
        keys.append("ABCD"[answer["index"]])
        cells = [p(f"{'ABCD'[i]}. {esc(o)}", "opt") for i, o in enumerate(options)]
        grid = Table([[cells[0], cells[1]], [cells[2], cells[3]]], colWidths=[86 * mm, 86 * mm])
        grid.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 16), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        out.append(KeepTogether([p(f"{k}.&nbsp;&nbsp;{esc(q.body)}", "q"), grid, Spacer(1, 5)]))
    out += [p("<b>B. Isian</b>", "h2"), p("Isilah titik-titik dengan jawaban yang benar!", "small"), Spacer(1, 4)]
    answers = []
    for k, q in enumerate(isian, 1):
        answers.append(q.answer["accepted"][0])
        out.append(KeepTogether([p(f"{k}.&nbsp;&nbsp;{esc(q.body)}", "q"), p("&nbsp;" * 6 + "Jawab: " + "." * 90, "body"), Spacer(1, 6)]))
    out.append(PageBreak())
    return out, keys, answers, pg, isian


def kunci(s, keys, answers, pg, isian):
    cells = [p(f"{i}. <b>{k}</b>", "body") for i, k in enumerate(keys, 1)]
    while len(cells) % 5:
        cells.append(p("", "body"))
    grid = Table([cells[i:i + 5] for i in range(0, len(cells), 5)], colWidths=[34 * mm] * 5)
    grid.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    rows = [p(f"{i}. {esc(a)} <font size=8 color='#475569'>({esc(q.explanation)})</font>", "small") for i, (a, q) in enumerate(zip(answers, isian), 1)]
    return [KeepTogether([p(NAMES[s.code].upper(), "h2"), p("<b>A. Pilihan Ganda</b>", "small"), grid, Spacer(1, 4), p("<b>B. Isian</b>", "small"), *rows, Spacer(1, 6)])]


def build(n, sem, path):
    term = "Ganjil" if sem == 1 else "Genap"
    level = "SD/MI" if n <= 6 else "SMP/MTs"
    subjects = load_grade(n).SUBJECTS
    footer = f"Soal Latihan SAS {term} Kelas {n} {level.split('/')[0]} – Kurikulum Merdeka · BOBO Belajar"

    def deco(canvas, doc):
        canvas.saveState()
        canvas.setFont("DV", 8)
        canvas.setFillColor(colors.HexColor("#64748B"))
        canvas.drawString(18 * mm, 10 * mm, footer)
        canvas.drawRightString(192 * mm, 10 * mm, f"Hal. {doc.page}")
        canvas.setStrokeColor(LINE)
        canvas.line(18 * mm, 13 * mm, 192 * mm, 13 * mm)
        canvas.restoreState()

    story = [
        Spacer(1, 8), p("SOAL LATIHAN", "title"), p(f"SUMATIF AKHIR SEMESTER (SAS) {term.upper()}", "title"), Spacer(1, 4),
        p(f"KELAS {n} {level} – KURIKULUM MERDEKA", "sub"), p("Semua Mata Pelajaran + Kisi-Kisi + Kunci Jawaban", "center"),
        p(" • ".join(NAMES[s.code] for s in subjects), "center"), Spacer(1, 10),
    ]
    note = Table([[p(
        "<b>Petunjuk umum:</b> 1) Berdoalah sebelum mengerjakan. 2) Tulis nama di tempat yang disediakan. "
        "3) Bagian A: berilah tanda silang (X) pada huruf A, B, C, atau D di depan jawaban yang paling tepat. "
        "4) Bagian B: isilah titik-titik dengan jawaban yang benar. 5) Periksa kembali jawabanmu. "
        "Kisi-kisi ada di bagian awal, kunci jawaban di bagian akhir. Soal yang sama tersedia di aplikasi BOBO Belajar "
        f"(tab Ujian, SAS {term}).<br/><br/><font size=8 color='#475569'>Draf materi BOBO Belajar disusun dengan bantuan AI mengacu pada Capaian Pembelajaran "
        "Kurikulum Merdeka 2025 untuk tahun ajaran 2026/2027; belum ditinjau guru. Pendidikan Agama belum disertakan.</font>", "body")]],
        colWidths=[174 * mm])
    note.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8, ACCENT), ("BACKGROUND", (0, 0), (-1, -1), SOFT), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    story += [note, PageBreak(), p("KISI-KISI SOAL", "h1"),
              p(f"Kelas/Semester: {ROMAN[n]} / {sem} ({term}) • Kurikulum Merdeka • Bentuk soal: 15 Pilihan Ganda (PG) + 5 Isian per mata pelajaran", "small")]
    for s in subjects:
        story += kisi(s, sem)
    story.append(PageBreak())
    keysets = []
    for s in subjects:
        part, keys, answers, pg, isian = soal(n, s, sem)
        story += part
        keysets.append((s, keys, answers, pg, isian))
    story.append(p("KUNCI JAWABAN", "h1"))
    for item in keysets:
        story += kunci(*item)
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=18 * mm,
                            title=f"Soal Latihan SAS {term} Kelas {n}", author="BOBO Belajar")
    doc.build(story, onFirstPage=deco, onLaterPages=deco)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--grades", type=int, nargs="*", default=list(range(1, 10)))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    for n in args.grades:
        for sem in (1, 2):
            term = "Ganjil" if sem == 1 else "Genap"
            path = os.path.join(args.out, f"Soal_Latihan_SAS_{term}_Kelas{n}.pdf")
            build(n, sem, path)
            print(path)


if __name__ == "__main__":
    main()
