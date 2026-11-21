import re
from dataclasses import dataclass

PATTERNS: list[tuple[str, re.Pattern]] = [
    ("self_harm", re.compile(r"\b(bunuh diri|ingin mati|pengen mati|mau mati aja|menyakiti diri|melukai diri|nyakitin diri)\b")),
    ("personal_info_request", re.compile(r"(alamat(mu| kamu| rumah)|rumahmu|nomor (hp|telepon|wa)|no\.? ?hp|whatsapp|password|kata sandi|\bpin\b|kirim foto|foto kamu|ketemuan|bertemu langsung|kopdar)")),
    ("adult", re.compile(r"\b(seks|sex|porno|bokep|telanjang|bugil|ngewe|mesum)\b")),
    ("violence", re.compile(r"\b(cara membunuh|bikin bom|membuat bom|senjata api|merakit senjata|menusuk orang)\b")),
    ("drugs", re.compile(r"\b(narkoba|sabu|ganja|cara mabuk|beli obat terlarang)\b")),
    ("homework_dump", re.compile(r"((jawaban|kunci)\s.*(pr|tugas|ujian))|kerjain pr|kerjakan pr(ku)?|contekan|nyontek|langsung jawabannya")),
]

PII_SHARE = re.compile(r"(\b0?8\d{8,11}\b|\+62\s?\d{8,12}|\b\d{16}\b|alamat(ku| saya| rumahku)?\s+(di|jl|jalan)|@\w+\.(com|id|co))")

DIAGNOSIS = re.compile(r"(disleksia|diskalkulia|adhd|autis|autisme|gangguan (belajar|konsentrasi|mental)|diagnos|bodoh|malas|lambat belajar|\biq\b|keterbelakangan)")

URL = re.compile(r"https?://\S+")


@dataclass
class SafetyVerdict:
    category: str | None
    action: str
    reply: str | None


CHILD_REPLIES = {
    "self_harm": "Terima kasih sudah cerita. Perasaanmu penting. Tolong segera bicara dengan orang dewasa yang kamu percaya, seperti ayah, ibu, guru, atau keluargamu, sekarang juga. Kalau kamu merasa tidak aman, minta orang dewasa di dekatmu untuk menghubungi layanan darurat 112.",
    "personal_info_request": "Itu informasi pribadi. Jangan bagikan alamat, nomor HP, kata sandi, atau foto ke siapa pun di aplikasi, termasuk ke BOBO. Kalau ada yang memintanya, ceritakan ke orang tuamu.\n\nYuk, kembali ke pelajaran!",
    "pii_share": "Sepertinya kamu menulis informasi pribadi. Jangan tulis nomor HP, alamat, atau data pribadi lain di sini, ya. BOBO tidak membutuhkannya.\n\nAda yang mau kamu tanyakan tentang pelajaran?",
    "adult": "BOBO hanya membahas pelajaran sekolah. Pertanyaan seperti itu sebaiknya kamu tanyakan ke orang tua atau guru yang kamu percaya.\n\nYuk, kembali ke materi!",
    "violence": "BOBO tidak bisa membantu hal yang bisa membahayakan orang lain. Kalau ada yang membuatmu takut atau tidak aman, ceritakan ke orang dewasa yang kamu percaya.",
    "drugs": "BOBO tidak membahas hal itu. Kalau kamu punya pertanyaan atau kekhawatiran, bicarakan dengan orang tua atau guru yang kamu percaya.",
    "homework_dump": "Aku tidak memberi jawaban PR atau ujian secara langsung, tapi aku bisa memandu langkah demi langkah. Ketik soalnya, lalu kita kerjakan bersama.",
}


def check_child_input(text: str) -> SafetyVerdict:
    t = text.lower()
    for cat, pat in PATTERNS:
        if pat.search(t):
            action = "guide" if cat == "homework_dump" else "refuse"
            return SafetyVerdict(cat, action, CHILD_REPLIES[cat])
    if PII_SHARE.search(t):
        return SafetyVerdict("pii_share", "refuse", CHILD_REPLIES["pii_share"])
    return SafetyVerdict(None, "allow", None)


def check_parent_input(text: str, child_name: str) -> SafetyVerdict:
    t = text.lower()
    if DIAGNOSIS.search(t):
        return SafetyVerdict("diagnosis", "redirect", (
            f"BOBO tidak memberi diagnosis atau label tentang {child_name}. Data di aplikasi hanya berisi hasil latihan dan asesmen, "
            "yang tidak cukup untuk menyimpulkan kondisi belajar, psikologis, atau medis.\n\n"
            "Jika Anda khawatir, bicarakan dengan guru kelas, psikolog, atau dokter anak. Untuk pelajaran sehari-hari, saya bisa membantu menyusun latihan yang sesuai."
        ))
    if PATTERNS[0][1].search(t):
        return SafetyVerdict("self_harm", "redirect", "Jika Anda atau anak Anda dalam bahaya atau berpikir untuk menyakiti diri, segera hubungi layanan darurat 112 atau tenaga kesehatan terdekat. BOBO hanya membantu urusan belajar dan tidak dapat menggantikan bantuan profesional.")
    return SafetyVerdict(None, "allow", None)


def clean_output(text: str, max_chars: int) -> tuple[str, bool]:
    flagged = False
    out = URL.sub("", text).strip()
    if PII_SHARE.search(out.lower()):
        flagged = True
        out = PII_SHARE.sub("[disembunyikan]", out)
    for cat, pat in PATTERNS[:5]:
        if pat.search(out.lower()):
            return "Maaf, BOBO tidak bisa menjawab itu. Yuk, kembali ke materi pelajaran.", True
    if len(out) > max_chars:
        cut = out[:max_chars]
        dot = max(cut.rfind(". "), cut.rfind("\n"))
        out = (cut[: dot + 1] if dot > max_chars // 2 else cut).strip()
    return out, flagged
