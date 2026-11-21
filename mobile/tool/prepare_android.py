import pathlib
import re
import shutil
import sys

root = pathlib.Path(__file__).resolve().parent.parent
app_dir = root / "android" / "app"
manifest = app_dir / "src" / "main" / "AndroidManifest.xml"
if not manifest.exists():
    sys.exit("android/ belum ada. Jalankan: flutter create --platforms=android --org id.bobo --project-name bobo_belajar .")

text = manifest.read_text(encoding="utf-8")
text = re.sub(r'\s*<uses-permission android:name="android.permission.INTERNET"\s*/>', "", text)
text = text.replace(' android:usesCleartextTraffic="true"', "")
text = re.sub(r'android:label="[^"]*"', 'android:label="BOBO Belajar"', text, count=1)
extra_queries = '        <intent>\n            <action android:name="android.intent.action.TTS_SERVICE"/>\n        </intent>\n'
if "TTS_SERVICE" not in text:
    if "<queries>" in text:
        text = text.replace("<queries>\n", "<queries>\n" + extra_queries, 1)
    else:
        text = text.replace("</manifest>", "    <queries>\n" + extra_queries + "    </queries>\n</manifest>", 1)
manifest.write_text(text, encoding="utf-8")

res_src = root / "tool" / "android-res"
for d in res_src.glob("mipmap-*"):
    target = app_dir / "src" / "main" / "res" / d.name
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(d / "ic_launcher.png", target / "ic_launcher.png")

signing_head = (
    "import java.io.FileInputStream\nimport java.util.Properties\n\n"
)
signing_props = (
    'val keystoreProperties = Properties()\n'
    'val keystorePropertiesFile = rootProject.file("key.properties")\n'
    'if (keystorePropertiesFile.exists()) {\n'
    '    keystoreProperties.load(FileInputStream(keystorePropertiesFile))\n'
    '}\n\n'
)
signing_config = (
    '    signingConfigs {\n'
    '        create("release") {\n'
    '            if (keystorePropertiesFile.exists()) {\n'
    '                keyAlias = keystoreProperties["keyAlias"] as String\n'
    '                keyPassword = keystoreProperties["keyPassword"] as String\n'
    '                storeFile = file(keystoreProperties["storeFile"] as String)\n'
    '                storePassword = keystoreProperties["storePassword"] as String\n'
    '            }\n'
    '        }\n'
    '    }\n\n'
    '    buildTypes {'
)

kts = app_dir / "build.gradle.kts"
groovy = app_dir / "build.gradle"
if kts.exists():
    g = kts.read_text(encoding="utf-8")
    g = re.sub(r"minSdk\s*=\s*flutter\.minSdkVersion", "minSdk = 24", g)
    if "keystoreProperties" not in g:
        g = signing_head + g
        g = g.replace("android {", signing_props + "android {", 1)
        g = g.replace("    buildTypes {", signing_config, 1)
        g = re.sub(
            r'signingConfig\s*=\s*signingConfigs\.getByName\("debug"\)',
            'signingConfig = if (keystorePropertiesFile.exists()) signingConfigs.getByName("release") else signingConfigs.getByName("debug")',
            g,
            count=1,
        )
    kts.write_text(g, encoding="utf-8")
elif groovy.exists():
    g = groovy.read_text(encoding="utf-8")
    g = re.sub(r"minSdkVersion\s+flutter\.minSdkVersion", "minSdkVersion 24", g)
    groovy.write_text(g, encoding="utf-8")

signed = (root / "android" / "key.properties").exists()
print(f"Android disiapkan (mode lokal, tanpa izin internet), signing {'rilis' if signed else 'debug'}.")
