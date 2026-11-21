"use client";

import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import Shell, { StatusChip } from "@/components/Shell";
import TopicPicker from "@/components/TopicPicker";
import { api, TYPE_LABEL } from "@/lib/api";

type Opt = { label: string; side: "a" | "b" };
type Q = {
  id: number; topic_id: number; topic: string; type: string; body: string; difficulty: string; options: Opt[]; answer: Record<string, unknown> | null; rubric: string | null;
  usage: string; status: string; version: number; is_sample: boolean; explanation: string; mistake_hint: string | null; source: string; source_reference: string | null;
  reviews: { decision: string; notes: string | null; at: string }[];
};

export default function QuestionEditor() {
  const params = useParams<{ id: string }>();
  const router = useRouter();
  const isNew = params.id === "new";
  const [q, setQ] = useState<Q | null>(null);
  const [topicId, setTopicId] = useState<number | null>(null);
  const [type, setType] = useState("mc");
  const [body, setBody] = useState("");
  const [difficulty, setDifficulty] = useState("mudah");
  const [usage, setUsage] = useState("both");
  const [options, setOptions] = useState<Opt[]>([{ label: "", side: "a" }, { label: "", side: "a" }, { label: "", side: "a" }, { label: "", side: "a" }]);
  const [single, setSingle] = useState(0);
  const [multi, setMulti] = useState<number[]>([]);
  const [accepted, setAccepted] = useState("");
  const [pairs, setPairs] = useState<Record<string, string>>({});
  const [rubric, setRubric] = useState("");
  const [explanation, setExplanation] = useState("");
  const [mistake, setMistake] = useState("");
  const [source, setSource] = useState("Tim konten BOBO");
  const [sourceRef, setSourceRef] = useState("");
  const [msg, setMsg] = useState<{ kind: "ok" | "err"; text: string } | null>(null);

  function hydrate(x: Q) {
    setQ(x); setTopicId(x.topic_id); setType(x.type); setBody(x.body); setDifficulty(x.difficulty); setUsage(x.usage);
    setOptions(x.options.length ? x.options : [{ label: "", side: "a" }, { label: "", side: "a" }]);
    const a = (x.answer ?? {}) as { index?: number; indices?: number[]; accepted?: string[]; pairs?: Record<string, string> };
    setSingle(a.index ?? 0); setMulti(a.indices ?? []); setAccepted((a.accepted ?? []).join("\n")); setPairs(a.pairs ?? {});
    setRubric(x.rubric ?? ""); setExplanation(x.explanation); setMistake(x.mistake_hint ?? ""); setSource(x.source); setSourceRef(x.source_reference ?? "");
  }

  useEffect(() => {
    if (!isNew) api<Q>(`/admin/questions/${params.id}`).then(hydrate).catch((e) => setMsg({ kind: "err", text: e.message }));
  }, [params.id, isNew]);

  const usesOptions = ["mc", "multi", "matching"].includes(type);
  const opts = type === "tf" ? [{ label: "Benar", side: "a" as const }, { label: "Salah", side: "a" as const }] : options;

  function answer(): Record<string, unknown> | null {
    if (type === "mc" || type === "tf") return { index: single };
    if (type === "multi") return { indices: [...multi].sort() };
    if (type === "fill" || type === "short") return { accepted: accepted.split("\n").map((s) => s.trim()).filter(Boolean) };
    if (type === "matching") return { pairs };
    return null;
  }

  async function save() {
    setMsg(null);
    const payload = { topic_id: topicId, type, body, difficulty, usage, options: usesOptions ? options.filter((o) => o.label.trim()) : type === "tf" ? opts : [], answer: answer(), rubric: type === "essay" ? rubric : null, explanation, mistake_hint: mistake || null, source, source_reference: sourceRef || null };
    try {
      const x = isNew ? await api<Q>("/admin/questions", { method: "POST", body: payload }) : await api<Q>(`/admin/questions/${params.id}`, { method: "PUT", body: payload });
      hydrate(x);
      setMsg({ kind: "ok", text: "Tersimpan sebagai draft." });
      if (isNew) router.replace(`/questions/${x.id}`);
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  async function act(path: string, ok: string) {
    setMsg(null);
    try {
      hydrate(await api<Q>(`/admin/questions/${params.id}/${path}`, { method: "POST" }));
      setMsg({ kind: "ok", text: ok });
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  const aSide = options.map((o, i) => ({ ...o, i })).filter((o) => o.side === "a" && o.label.trim());
  const bSide = options.map((o, i) => ({ ...o, i })).filter((o) => o.side === "b" && o.label.trim());

  return (
    <Shell title={isNew ? "Soal baru" : "Ubah soal"} subtitle="Kunci jawaban hanya dikirim ke aplikasi setelah siswa menjawab (latihan) atau setelah asesmen dikumpulkan.">
      {msg ? <div className={`alert ${msg.kind}`} role="status">{msg.text}</div> : null}
      {q ? <div className="row" style={{ marginBottom: 12 }}><StatusChip status={q.status} sample={q.is_sample} /><span className="muted small">Versi terbit: {q.version} · Topik: {q.topic}</span></div> : null}
      <div className="card">
        <TopicPicker value={topicId} onChange={setTopicId} />
        <div className="grid">
          <div className="field"><label htmlFor="q-type">Tipe</label>
            <select id="q-type" value={type} onChange={(e) => setType(e.target.value)}>{Object.entries(TYPE_LABEL).map(([k, v]) => <option key={k} value={k}>{v}</option>)}</select>
          </div>
          <div className="field"><label htmlFor="q-diff">Kesulitan</label>
            <select id="q-diff" value={difficulty} onChange={(e) => setDifficulty(e.target.value)}><option value="mudah">Mudah</option><option value="sedang">Sedang</option><option value="menantang">Menantang</option></select>
          </div>
          <div className="field"><label htmlFor="q-use">Dipakai untuk</label>
            <select id="q-use" value={usage} onChange={(e) => setUsage(e.target.value)}><option value="both">Latihan & asesmen</option><option value="practice">Latihan saja</option><option value="assessment">Asesmen saja</option></select>
          </div>
        </div>
        <div className="field"><label htmlFor="q-body">Pertanyaan</label><textarea id="q-body" value={body} onChange={(e) => setBody(e.target.value)} /></div>
      </div>

      <div className="card">
        <h2>Jawaban</h2>
        {type === "tf" ? (
          <div className="row" role="radiogroup" aria-label="Kunci benar/salah">
            {opts.map((o, i) => <label key={i} className="row" style={{ fontWeight: 600 }}><input type="radio" name="tf" checked={single === i} onChange={() => setSingle(i)} /> {o.label}</label>)}
          </div>
        ) : null}
        {usesOptions ? (
          <div className="stack">
            {options.map((o, i) => (
              <div key={i} className="row">
                {type === "mc" ? <input type="radio" name="mc" aria-label={`Kunci pilihan ${i + 1}`} checked={single === i} onChange={() => setSingle(i)} /> : null}
                {type === "multi" ? <input type="checkbox" aria-label={`Kunci pilihan ${i + 1}`} checked={multi.includes(i)} onChange={(e) => setMulti((m) => (e.target.checked ? [...m, i] : m.filter((x) => x !== i)))} /> : null}
                {type === "matching" ? (
                  <select aria-label={`Sisi pilihan ${i + 1}`} style={{ width: 120 }} value={o.side} onChange={(e) => setOptions((os) => os.map((x, j) => (j === i ? { ...x, side: e.target.value as "a" | "b" } : x)))}>
                    <option value="a">Kiri</option><option value="b">Kanan</option>
                  </select>
                ) : null}
                <input aria-label={`Pilihan ${i + 1}`} placeholder={`Pilihan ${String.fromCharCode(65 + i)}`} value={o.label} onChange={(e) => setOptions((os) => os.map((x, j) => (j === i ? { ...x, label: e.target.value } : x)))} style={{ flex: 1, width: "auto" }} />
                <button className="danger" disabled={options.length <= 2} onClick={() => setOptions((os) => os.filter((_, j) => j !== i))} aria-label={`Hapus pilihan ${i + 1}`}>Hapus</button>
              </div>
            ))}
            <div><button onClick={() => setOptions((os) => [...os, { label: "", side: "a" }])}>+ Pilihan</button></div>
          </div>
        ) : null}
        {type === "matching" ? (
          <div className="stack" style={{ marginTop: 12 }}>
            <strong className="small">Pasangan benar</strong>
            {aSide.map((a) => (
              <div key={a.i} className="row">
                <span style={{ minWidth: 160 }}>{a.label}</span>→
                <select aria-label={`Pasangan untuk ${a.label}`} style={{ maxWidth: 260 }} value={pairs[String(a.i)] ?? ""} onChange={(e) => setPairs((p) => ({ ...p, [String(a.i)]: e.target.value }))}>
                  <option value="">Pilih</option>{bSide.map((b) => <option key={b.i} value={String(b.i)}>{b.label}</option>)}
                </select>
              </div>
            ))}
          </div>
        ) : null}
        {type === "fill" || type === "short" ? <div className="field"><label htmlFor="q-acc">Jawaban yang diterima (satu per baris)</label><textarea id="q-acc" value={accepted} onChange={(e) => setAccepted(e.target.value)} /></div> : null}
        {type === "essay" ? <div className="field"><label htmlFor="q-rub">Rubrik penilaian (wajib)</label><textarea id="q-rub" value={rubric} onChange={(e) => setRubric(e.target.value)} /><p className="muted small">Esai dinilai manual oleh peninjau di menu Antrean review. AI tidak memfinalkan nilai.</p></div> : null}
      </div>

      <div className="card">
        <h2>Pembahasan & sumber</h2>
        <div className="field"><label htmlFor="q-exp">Pembahasan (wajib)</label><textarea id="q-exp" value={explanation} onChange={(e) => setExplanation(e.target.value)} /></div>
        <div className="field"><label htmlFor="q-mis">Letak kesalahan umum (ditampilkan saat jawaban salah)</label><input id="q-mis" value={mistake} onChange={(e) => setMistake(e.target.value)} /></div>
        <div className="grid">
          <div className="field"><label htmlFor="q-src">Sumber</label><input id="q-src" value={source} onChange={(e) => setSource(e.target.value)} /></div>
          <div className="field"><label htmlFor="q-ref">Referensi (opsional)</label><input id="q-ref" value={sourceRef} onChange={(e) => setSourceRef(e.target.value)} /></div>
        </div>
      </div>

      <div className="card">
        <div className="row">
          <button className="primary" disabled={!topicId || body.length < 2 || explanation.length < 3 || source.length < 2} onClick={save}>Simpan draft</button>
          {q && ["draft", "rejected"].includes(q.status) ? <button onClick={() => act("submit", "Dikirim ke antrean review")}>Kirim untuk review</button> : null}
          {q?.status === "approved" ? <button className="ok" onClick={() => act("publish", "Soal terbit")}>Terbitkan</button> : null}
          {q?.status === "published" ? <button className="danger" onClick={() => act("unpublish", "Soal ditarik")}>Tarik dari aplikasi</button> : null}
        </div>
      </div>
      {q?.reviews?.length ? (
        <div className="card">
          <h2>Riwayat review</h2>
          {q.reviews.map((r, i) => <div key={i} className="small" style={{ marginBottom: 6 }}><strong>{r.decision === "approve" ? "Disetujui" : "Ditolak"}</strong> · {new Date(r.at).toLocaleString("id-ID")} {r.notes ? `· ${r.notes}` : ""}</div>)}
        </div>
      ) : null}
    </Shell>
  );
}
