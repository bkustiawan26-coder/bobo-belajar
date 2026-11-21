"use client";

import Link from "next/link";
import { useState } from "react";
import Shell, { useAsync } from "@/components/Shell";
import { api, getSession, TYPE_LABEL } from "@/lib/api";

type Item = { id: number; title?: string; body?: string; topic: string; type?: string; status: string; blocks?: { kind: string; text: string | null; points: string[] | null }[]; options?: { label: string }[]; answer?: Record<string, unknown> | null; explanation?: string; source?: string };
type Essay = { answer_id: number; question: string; rubric: string | null; response: string | null };

export default function ReviewPage() {
  const roles = getSession()?.roles ?? [];
  const canReview = roles.includes("admin") || roles.includes("reviewer");
  const lessons = useAsync<Item[]>(() => api("/admin/lessons?status_filter=in_review"));
  const questions = useAsync<Item[]>(() => api("/admin/questions?status_filter=in_review"));
  const approvedL = useAsync<Item[]>(() => api("/admin/lessons?status_filter=approved"));
  const approvedQ = useAsync<Item[]>(() => api("/admin/questions?status_filter=approved"));
  const essays = useAsync<Essay[]>(() => (canReview ? api("/admin/essay-reviews") : Promise.resolve([])));
  const [notes, setNotes] = useState<Record<string, string>>({});
  const [msg, setMsg] = useState<{ kind: "ok" | "err"; text: string } | null>(null);

  async function act(path: string, body: unknown, ok: string) {
    setMsg(null);
    try {
      await api(path, { method: "POST", body });
      setMsg({ kind: "ok", text: ok });
      lessons.reload(); questions.reload(); approvedL.reload(); approvedQ.reload(); essays.reload();
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  function decide(kind: "lessons" | "questions", id: number, decision: "approve" | "reject") {
    const key = `${kind}-${id}`;
    if (decision === "reject" && !notes[key]) {
      setMsg({ kind: "err", text: "Tulis alasan penolakan agar penulis tahu apa yang harus diperbaiki." });
      return;
    }
    act(`/admin/${kind}/${id}/review`, { decision, notes: notes[key] || null }, decision === "approve" ? "Disetujui. Terbitkan di bagian bawah." : "Ditolak dan dikembalikan ke penulis.");
  }

  return (
    <Shell title="Antrean review" subtitle="Periksa ketepatan isi, kunci jawaban, bahasa sesuai jenjang, dan sumbernya. Peninjau tidak boleh menyetujui konten buatannya sendiri.">
      {msg ? <div className={`alert ${msg.kind}`} role="status">{msg.text}</div> : null}
      {!canReview ? <div className="alert warn">Akun Anda berperan editor. Persetujuan dan penerbitan hanya bisa dilakukan peninjau atau admin.</div> : null}

      <h2>Materi menunggu review ({lessons.data?.length ?? 0})</h2>
      {lessons.data?.map((l) => (
        <div className="card" key={l.id}>
          <div className="row"><strong>{l.title}</strong><span className="muted small">· {l.topic}</span><span className="spacer" /><Link href={`/lessons/${l.id}`}>Buka editor</Link></div>
          {l.blocks?.map((b, i) => (
            <div key={i} style={{ marginTop: 10 }}>
              <div className="small" style={{ fontWeight: 800 }}>{b.kind}</div>
              {b.text ? <div style={{ whiteSpace: "pre-line" }}>{b.text}</div> : null}
              {b.points ? <ul style={{ margin: "4px 0" }}>{b.points.map((p, j) => <li key={j}>{p}</li>)}</ul> : null}
            </div>
          ))}
          {canReview ? <ReviewActions id={`lessons-${l.id}`} notes={notes} setNotes={setNotes} onApprove={() => decide("lessons", l.id, "approve")} onReject={() => decide("lessons", l.id, "reject")} /> : null}
        </div>
      ))}

      <h2 style={{ marginTop: 24 }}>Soal menunggu review ({questions.data?.length ?? 0})</h2>
      {questions.data?.map((q) => (
        <div className="card" key={q.id}>
          <div className="row"><strong>{TYPE_LABEL[q.type ?? ""] ?? q.type}</strong><span className="muted small">· {q.topic}</span><span className="spacer" /><Link href={`/questions/${q.id}`}>Buka editor</Link></div>
          <p style={{ whiteSpace: "pre-line" }}>{q.body}</p>
          {q.options?.length ? <ol type="A" style={{ marginTop: 0 }}>{q.options.map((o, i) => <li key={i}>{o.label}</li>)}</ol> : null}
          <div className="small"><strong>Kunci:</strong> <code>{JSON.stringify(q.answer)}</code></div>
          <div className="small" style={{ marginTop: 4 }}><strong>Pembahasan:</strong> {q.explanation}</div>
          <div className="small muted" style={{ marginTop: 4 }}>Sumber: {q.source}</div>
          {canReview ? <ReviewActions id={`questions-${q.id}`} notes={notes} setNotes={setNotes} onApprove={() => decide("questions", q.id, "approve")} onReject={() => decide("questions", q.id, "reject")} /> : null}
        </div>
      ))}

      {canReview ? (
        <>
          <h2 style={{ marginTop: 24 }}>Siap terbit</h2>
          <div className="table-wrap" style={{ marginBottom: 16 }}>
            <table>
              <thead><tr><th>Jenis</th><th>Judul / soal</th><th>Topik</th><th></th></tr></thead>
              <tbody>
                {approvedL.data?.map((l) => <tr key={`l${l.id}`}><td>Materi</td><td>{l.title}</td><td>{l.topic}</td><td><button className="ok" onClick={() => act(`/admin/lessons/${l.id}/publish`, undefined, "Materi terbit")}>Terbitkan</button></td></tr>)}
                {approvedQ.data?.map((q) => <tr key={`q${q.id}`}><td>Soal</td><td>{(q.body ?? "").slice(0, 80)}</td><td>{q.topic}</td><td><button className="ok" onClick={() => act(`/admin/questions/${q.id}/publish`, undefined, "Soal terbit")}>Terbitkan</button></td></tr>)}
                {!approvedL.data?.length && !approvedQ.data?.length ? <tr><td colSpan={4} className="muted">Tidak ada.</td></tr> : null}
              </tbody>
            </table>
          </div>

          <h2>Penilaian esai ({essays.data?.length ?? 0})</h2>
          {essays.data?.map((e) => (
            <div className="card" key={e.answer_id}>
              <p style={{ marginTop: 0 }}><strong>Soal:</strong> {e.question}</p>
              <p><strong>Rubrik:</strong> {e.rubric}</p>
              <p><strong>Jawaban siswa:</strong> {e.response ?? <span className="muted">kosong</span>}</p>
              <div className="row">
                <button className="ok" onClick={() => act(`/admin/assessment-answers/${e.answer_id}/score`, { correct: true }, "Dinilai benar")}>Sesuai rubrik</button>
                <button className="danger" onClick={() => act(`/admin/assessment-answers/${e.answer_id}/score`, { correct: false }, "Dinilai belum sesuai")}>Belum sesuai</button>
              </div>
            </div>
          ))}
        </>
      ) : null}
    </Shell>
  );
}

function ReviewActions({ id, notes, setNotes, onApprove, onReject }: { id: string; notes: Record<string, string>; setNotes: (f: (n: Record<string, string>) => Record<string, string>) => void; onApprove: () => void; onReject: () => void }) {
  return (
    <div style={{ marginTop: 12 }}>
      <label htmlFor={`n-${id}`}>Catatan review</label>
      <textarea id={`n-${id}`} value={notes[id] ?? ""} onChange={(e) => setNotes((n) => ({ ...n, [id]: e.target.value }))} />
      <div className="row" style={{ marginTop: 8 }}>
        <button className="ok" onClick={onApprove}>Setujui</button>
        <button className="danger" onClick={onReject}>Tolak</button>
      </div>
    </div>
  );
}
