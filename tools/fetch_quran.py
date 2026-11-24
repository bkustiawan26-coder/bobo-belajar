import io
import json
import re
import sys
import time
import urllib.request
import zipfile

RANGES = {
    1: (1, 7), 2: [(168, 168)], 3: [(190, 191)], 16: [(114, 114)], 17: [(23, 24)], 39: [(53, 53)],
    49: [(10, 13)], 53: [(39, 42)], 55: [(33, 33)], 58: [(11, 11)],
    87: (1, 19), 93: (1, 11), 94: (1, 8), 95: (1, 8), 96: [(1, 5)], 97: (1, 5), 99: (1, 8), 100: (1, 11), 101: (1, 11),
    102: (1, 8), 103: (1, 3), 104: (1, 9), 105: (1, 5), 106: (1, 4), 107: (1, 7), 108: (1, 3), 109: (1, 6), 110: (1, 3),
    111: (1, 5), 112: (1, 4), 113: (1, 5), 114: (1, 6),
}
RECITER = "Alafasy_64kbps"
BASMALAH = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"


def get(url, tries=5):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "bobo-belajar-build"}), timeout=60) as r:
                return r.read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 + i * 3)


def wanted(surah):
    r = RANGES[surah]
    spans = [r] if isinstance(r, tuple) else r
    return [a for lo, hi in spans for a in range(lo, hi + 1)]


def main(out_zip):
    meta = {"reciter": "Mishary Rashid Alafasy", "audio_source": f"https://everyayah.com/data/{RECITER}/", "text_source": "https://api.alquran.cloud/v1 (quran-uthmani, Tanzil)", "surahs": {}}
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        for surah in RANGES:
            data = json.loads(get(f"https://api.alquran.cloud/v1/surah/{surah}/quran-uthmani"))["data"]
            ayahs = {a["numberInSurah"]: a["text"] for a in data["ayahs"]}
            keep = wanted(surah)
            texts = {}
            for n in keep:
                t = ayahs[n].strip()
                if surah != 1 and n == 1 and t.startswith(BASMALAH[:10]):
                    t = re.sub(r"^\S+\s+\S+\s+\S+\s+\S+\s*", "", t, count=1)
                texts[str(n)] = t
                z.writestr(f"audio/{surah:03d}{n:03d}.mp3", get(f"https://everyayah.com/data/{RECITER}/{surah:03d}{n:03d}.mp3"))
            meta["surahs"][str(surah)] = {"name": data["englishName"], "arabic": data["name"], "count": data["numberOfAyahs"], "ayahs": texts}
        z.writestr("audio/001001.mp3", get(f"https://everyayah.com/data/{RECITER}/001001.mp3"))
        z.writestr("quran.json", json.dumps(meta, ensure_ascii=False, indent=1))
    open(out_zip, "wb").write(buf.getvalue())
    print("ok", len(buf.getvalue()))


if __name__ == "__main__":
    main(sys.argv[1])
