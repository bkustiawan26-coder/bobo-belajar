"use client";

import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import Shell, { StatusChip } from "@/components/Shell";
import TopicPicker from "@/components/TopicPicker";
import { api } from "@/lib/api";

type Block = { kind: string; text: string | null; points: string[] | null; visual: string | null };
type Lesson = { id: number; topic_id: number; topic: string; title: string; minutes: number; status: string; version: number; is_sample: boolean; blocks: Block[]; reviews: { decision: string; notes: string | null; at: string }[] };

const KINDS = ["Penjelasan", "Contoh", "Poin penting", "Ringkasan", "Latihan singkat"];

export default function LessonEditor() {
  const params = useParams<{ id: string }>();
  const router = useRouter();
  const isNew = params.id === "new";
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [topicId, setTopicId] = useState<number | null>(null);
  const [title, setTitle] = useState("");
  const [minutes, setMinutes] = useState(5);
  const [blocks, setBlocks] = useState<Block[]>([{ kind: "Penjelasan", text: "", points: null, visual: null }]);
  const [msg, setMsg] = useState<{ kind: "ok" | "err"; text: string } | null>(null);

  function hydrate(l: Lesson) {
    setLesson(l);
    setTopicId(l.topic_id);
    setTitle(l.title);
    setMinutes(l.minutes);
    setBlocks(l.blocks.map((b) => ({ ...b })));
  }

  useEffect(() => {
    if (!isNew) api<Lesson>(`/admin/lessons/${params.id}`).then(hydrate).catch((e) => setMsg({ kind: "err", text: e.message }));
  }, [params.id, isNew]);

  async function save() {
    setMsg(null);
    const body = { topic_id: topicId, title, minutes, blocks: blocks.map((b) => ({ kind: b.kind, text: b.text || null, points: b.points && b.points.length ? b.points.filter(Boolean) : null, visual: b.visual || null })) };
    try {
      const l = isNew ? await api<Lesson>("/admin/lessons", { method: "POST", body }) : await api<Lesson>(`/admin/lessons/${params.id}`, { method: "PUT", body });
      hydrate(l);
      setMsg({ kind: "ok", text: lesson?.status === "published" ? "Tersimpan. Materi kembali ke draft dan perlu ditinjau ulang." : "Tersimpan sebagai draft." });
      if (isNew) router.replace(`/lessons/${l.id}`);
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  async function act(path: string, body?: unknown, ok = "Berhasil") {
    setMsg(null);
    try {
      hydrate(await api<Lesson>(`/admin/lessons/${params.id}/${path}`, { method: "POST", body }));
      setMsg({ kind: "ok", text: ok });
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  function upd(i: number, patch: Partial<Block>) {
    setBlocks((bs) => bs.map((b, j) => (j === i ? { ...b, ...patch } : b)));
  }

  return (
    <Shell title={isNew ? "Materi baru" : title || "Materi"} subtitle="Gunakan bahasa sesuai jenjang: kalimat pendek dan contoh konkret untuk kelas kecil, penalaran runtut untuk SMP.">
      {msg ? <div className={`alert ${msg.kind}`} role="status">{msg.text}</div> : null}
      {lesson ? <div className="row" style={{ marginBottom: 12 }}><StatusChip status={lesson.status} sample={lesson.is_sample} /><span className="muted small">Versi terbit: {lesson.version} · Topik: {lesson.topic}</span></div> : null}
      <div className="card">
        <TopicPicker value={topicId} onChange={setTopicId} />
        <div className="grid">
          <div className="field"><label htmlFor="l-title">Judul</label><input id="l-title" value={title} onChange={(e) => setTitle(e.target.value)} /></div>
          <div className="field"><label htmlFor="l-min">Durasi (menit)</label><input id="l-min" type="number" min={1} max={120} value={minutes} onChange={(e) => setMinutes(Number(e.target.value))} /></div>
        </div>
      </div>
      {blocks.map((b, i) => (
        <div className="card" key={i}>
          <div className="row" style={{ marginBottom: 10 }}>
            <strong>Bagian {i + 1}</strong>
            <span className="spacer" />
            <button disabled={i === 0} onClick={() => setBlocks((bs) => { const c = [...bs]; [c[i - 1], c[i]] = [c[i], c[i - 1]]; return c; })} aria-label={`Naikkan bagian ${i + 1}`}>↑</button>
            <button disabled={i === blocks.length - 1} onClick={() => setBlocks((bs) => { const c = [...bs]; [c[i + 1], c[i]] = [c[i], c[i + 1]]; return c; })} aria-label={`Turunkan bagian ${i + 1}`}>↓</button>
            <button className="danger" disabled={blocks.length === 1} onClick={() => setBlocks((bs) => bs.filter((_, j) => j !== i))}>Hapus</button>
          </div>
          <div className="grid">
            <div className="field"><label htmlFor={`k${i}`}>Jenis</label>
              <select id={`k${i}`} value={b.kind} onChange={(e) => upd(i, { kind: e.target.value })}>{KINDS.map((k) => <option key={k}>{k}</option>)}</select>
            </div>
            <div className="field"><label htmlFor={`v${i}`}>Visual bawaan</label>
              <select id={`v${i}`} value={b.visual ?? ""} onChange={(e) => upd(i, { visual: e.target.value || null })}>
                <option value="">Tidak ada</option><option value="frac">Batang pecahan</option><option value="tens">Puluhan & satuan</option><option value="tri">Segitiga siku-siku</option>
              </select>
            </div>
          </div>
          <div className="field"><label htmlFor={`t${i}`}>Teks</label><textarea id={`t${i}`} value={b.text ?? ""} onChange={(e) => upd(i, { text: e.target.value })} /></div>
          <div className="field"><label htmlFor={`p${i}`}>Poin (satu per baris, opsional)</label><textarea id={`p${i}`} value={(b.points ?? []).join("\n")} onChange={(e) => upd(i, { points: e.target.value ? e.target.value.split("\n") : null })} /></div>
        </div>
      ))}
      <div className="row" style={{ marginBottom: 16 }}>
        <button onClick={() => setBlocks((bs) => [...bs, { kind: "Penjelasan", text: "", points: null, visual: null }])}>+ Bagian</button>
      </div>
      <div className="card">
        <div className="row">
          <button className="primary" disabled={!topicId || title.length < 2} onClick={save}>Simpan draft</button>
          {lesson && ["draft", "rejected"].includes(lesson.status) ? <button onClick={() => act("submit", undefined, "Dikirim ke antrean review")}>Kirim untuk review</button> : null}
          {lesson?.status === "approved" ? <button className="ok" onClick={() => act("publish", undefined, "Materi terbit dan siap dipakai Tutor")}>Terbitkan</button> : null}
          {lesson?.status === "published" ? <button className="danger" onClick={() => act("unpublish", undefined, "Materi ditarik dari aplikasi")}>Tarik dari aplikasi</button> : null}
        </div>
      </div>
      {lesson?.reviews?.length ? (
        <div className="card">
          <h2>Riwayat review</h2>
          {lesson.reviews.map((r, i) => <div key={i} className="small" style={{ marginBottom: 6 }}><strong>{r.decision === "approve" ? "Disetujui" : "Ditolak"}</strong> · {new Date(r.at).toLocaleString("id-ID")} {r.notes ? `· ${r.notes}` : ""}</div>)}
        </div>
      ) : null}
    </Shell>
  );
}
