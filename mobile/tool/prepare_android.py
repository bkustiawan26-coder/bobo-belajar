import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
manifest = root / "android" / "app" / "src" / "main" / "AndroidManifest.xml"
if not manifest.exists():
    sys.exit("android/ belum ada. Jalankan: flutter create --platforms=android --org id.bobo --project-name bobo_belajar .")

text = manifest.read_text(encoding="utf-8")
if "android.permission.INTERNET" not in text:
    text = text.replace("<application", '<uses-permission android:name="android.permission.INTERNET"/>\n    <application', 1)
text = re.sub(r'android:label="[^"]*"', 'android:label="BOBO Belajar"', text, count=1)
allow_http = "--allow-http" in sys.argv
if allow_http and "usesCleartextTraffic" not in text:
    text = text.replace("<application", '<application android:usesCleartextTraffic="true"', 1)
if not allow_http:
    text = text.replace(' android:usesCleartextTraffic="true"', "")
manifest.write_text(text, encoding="utf-8")

for name in ("build.gradle.kts", "build.gradle"):
    gradle = root / "android" / "app" / name
    if gradle.exists():
        g = gradle.read_text(encoding="utf-8")
        g = re.sub(r"minSdk\s*=\s*flutter\.minSdkVersion", "minSdk = 23", g)
        g = re.sub(r"minSdkVersion\s+flutter\.minSdkVersion", "minSdkVersion 23", g)
        gradle.write_text(g, encoding="utf-8")

print(f"AndroidManifest disiapkan (HTTP lokal {'diizinkan' if allow_http else 'tidak diizinkan'}).")
