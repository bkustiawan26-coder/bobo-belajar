# Arsitektur AI

Alur: Aplikasi → `/student/tutor/messages` atau `/parent/assistant/messages` → kuota → safety input → retrieval → prompt berversi → provider → validasi output → log pemakaian.

## Provider (tidak terikat satu vendor)
| `BOBO_AI_PROVIDER` | Keterangan | Biaya |
|---|---|---|
| `grounded` (default) | menyusun jawaban langsung dari potongan materi terbit; mode petunjuk untuk soal; jawaban orang tua dari data penguasaan | $0 |
| `anthropic` | Messages API, model dari `BOBO_AI_MODEL` | sesuai tarif yang diisi |
| `openai_compat` | endpoint `/chat/completions` (OpenAI, Gemini kompatibel, Ollama, vLLM) | sesuai tarif yang diisi |

Jika provider eksternal gagal atau timeout, otomatis jatuh ke `grounded` (`outcome=fallback`). Jika batas biaya harian global (`BOBO_AI_GLOBAL_DAILY_COST_LIMIT_USD`) tercapai, provider eksternal tidak dipanggil.

## Retrieval (RAG)
PostgreSQL full-text search konfigurasi `indonesian` atas `knowledge_chunks` (materi terbit prioritas 3, pembahasan bank soal prioritas 2). Disaring per kelas. Konten draft tidak pernah diindeks. pgvector bisa ditambahkan nanti tanpa mengubah API.

## Kontrol biaya & pemakaian
- Kuota harian per anak (gratis 10, premium 40) dan per orang tua (10/40) dari `subscription_entitlements`; orang tua bisa menurunkan batas per anak.
- Token dan biaya dicatat per permintaan (`ai_usage_logs`) dengan harga dari `BOBO_AI_PRICE_*_PER_MTOK`.
- Cache jawaban tutor 1 jam untuk pertanyaan identik per kelas.
- Batas laju login/refresh/registrasi.

## Menjelaskan ulang
Tombol "Belum paham?" di Tutor mengirim ulang pertanyaan dengan `style`: `story` (cerita sehari-hari), `visual` (aplikasi menampilkan gambar + alat peraga pecahan, nilai tempat, atau Pythagoras sesuai topik), `steps` (langkah bernomor). Tetap memakai materi yang sama dan memotong kuota seperti pertanyaan biasa.

## Prompt berversi
`ai_prompt_versions` (tutor, parent). Admin membuat versi baru di CMS; versi yang dipakai dicatat di log.

## Batasan
- Jawaban AI bukan otoritas kurikulum atau penilaian. Esai tidak dinilai final oleh AI.
- Asisten orang tua tidak mendiagnosis; pertanyaan diagnosis dialihkan ke guru/psikolog/dokter.
- Percakapan anak tidak dipakai untuk melatih model (persetujuan `ai_training` default tidak aktif).
