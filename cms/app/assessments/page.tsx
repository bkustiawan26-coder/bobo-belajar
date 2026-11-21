"use client";

import { useState } from "react";
import Shell, { StatusChip, useAsync } from "@/components/Shell";
import { api } from "@/lib/api";

type A = { id: number; template_id: number; title: string; short_title: string; subject_id: number; grade_number: number; semester: number | null; duration_minutes: number; shuffle_questions: boolean; shuffle_options: boolean; passing_score: number | null; status: string; is_sample: boolean; question_ids: number[] };
type T = { id: number; code: string; label: string };
type Subject = { id: number; name: string };
type Q = { id: number; body: string; topic: string; status: string; usage: string };

export default function AssessmentsPage() {
  const list = useAsync<A[]>(() => api("/admin/assessments"));
  const templates = useAsync<T[]>(() => api("/admin/assessment-templates"));
  const [grade, setGrade] = useState(5);
  const subjects = useAsync<Subject[]>(() => api(`/admin/subjects?grade=${grade}`), [grade]);
  const questions = useAsync<Q[]>(() => api("/admin/questions?status_filter=published"));
  const [form, setForm] = useState({ template_id: 1, title: "", short_title: "", subject_id: 0, duration_minutes: 30, semester: 1, shuffle_questions: true, shuffle_options: true, passing_score: "" });
  const [picked, setPicked] = useState<number[]>([]);
  const [msg, setMsg] = useState<{ kind: "ok" | "err"; text: string } | null>(null);
  const tmap = Object.fromEntries((templates.data ?? []).map((t) => [t.id, t.label]));

  async function run(fn: () => Promise<unknown>, ok: string) {
    setMsg(null);
    try {
      await fn();
      setMsg({ kind: "ok", text: ok });
      list.reload();
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  const subjectId = form.subject_id || subjects.data?.[0]?.id || 0;
  const usable = (questions.data ?? []).filter((q) => q.usage !== "practice");

  return (
    <Shell title="Asesmen" subtitle="Jenis asesmen dapat dikonfigurasi. Waktu dan penilaian divalidasi server; pengiriman bersifat idempoten.">
      {msg ? <div className={`alert ${msg.kind}`} role="status">{msg.text}</div> : null}
      <div className="table-wrap" style={{ marginBottom: 20 }}>
        <table>
          <thead><tr><th>Judul</th><th>Jenis</th><th>Kelas</th><th>Durasi</th><th>Soal</th><th>Status</th><th></th></tr></thead>
          <tbody>
            {list.data?.map((a) => (
              <tr key={a.id}>
                <td>{a.title}</td><td>{tmap[a.template_id] ?? "–"}</td><td>{a.grade_number}</td><td>{a.duration_minutes} mnt</td><td>{a.question_ids.length}</td>
                <td><StatusChip status={a.status} sample={a.is_sample} /></td>
                <td>{a.status === "draft" ? <button className="ok" onClick={() => run(() => api(`/admin/assessments/${a.id}/publish`, { method: "POST" }), "Asesmen terbit")}>Terbitkan</button> : <button className="danger" onClick={() => run(() => api(`/admin/assessments/${a.id}/unpublish`, { method: "POST" }), "Asesmen ditarik")}>Tarik</button>}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="card">
        <h2>Buat asesmen</h2>
        <div className="grid">
          <div className="field"><label htmlFor="a-tpl">Jenis</label><select id="a-tpl" value={form.template_id} onChange={(e) => setForm({ ...form, template_id: Number(e.target.value) })}>{templates.data?.map((t) => <option key={t.id} value={t.id}>{t.label}</option>)}</select></div>
          <div className="field"><label htmlFor="a-grade">Kelas</label><select id="a-grade" value={grade} onChange={(e) => { setGrade(Number(e.target.value)); setForm({ ...form, subject_id: 0 }); }}>{[1, 2, 3, 4, 5, 6, 7, 8, 9].map((g) => <option key={g} value={g}>Kelas {g}</option>)}</select></div>
          <div className="field"><label htmlFor="a-sub">Mata pelajaran</label><select id="a-sub" value={subjectId} onChange={(e) => setForm({ ...form, subject_id: Number(e.target.value) })}>{subjects.data?.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}</select></div>
          <div className="field"><label htmlFor="a-sem">Semester</label><select id="a-sem" value={form.semester} onChange={(e) => setForm({ ...form, semester: Number(e.target.value) })}><option value={1}>1</option><option value={2}>2</option></select></div>
          <div className="field"><label htmlFor="a-dur">Durasi (menit)</label><input id="a-dur" type="number" min={1} max={240} value={form.duration_minutes} onChange={(e) => setForm({ ...form, duration_minutes: Number(e.target.value) })} /></div>
          <div className="field"><label htmlFor="a-pass">Batas lulus (opsional)</label><input id="a-pass" type="number" min={0} max={100} value={form.passing_score} onChange={(e) => setForm({ ...form, passing_score: e.target.value })} /></div>
        </div>
        <div className="grid">
          <div className="field"><label htmlFor="a-title">Judul</label><input id="a-title" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} /></div>
          <div className="field"><label htmlFor="a-short">Judul singkat</label><input id="a-short" value={form.short_title} onChange={(e) => setForm({ ...form, short_title: e.target.value })} /></div>
        </div>
        <div className="row" style={{ marginBottom: 12 }}>
          <label className="row" style={{ fontWeight: 600 }}><input type="checkbox" checked={form.shuffle_questions} onChange={(e) => setForm({ ...form, shuffle_questions: e.target.checked })} /> Acak urutan soal</label>
          <label className="row" style={{ fontWeight: 600 }}><input type="checkbox" checked={form.shuffle_options} onChange={(e) => setForm({ ...form, shuffle_options: e.target.checked })} /> Acak urutan pilihan</label>
        </div>
        <strong className="small">Pilih soal terbit ({picked.length} dipilih)</strong>
        <div className="table-wrap" style={{ maxHeight: 320, overflowY: "auto", marginTop: 8 }}>
          <table>
            <tbody>
              {usable.map((q) => (
                <tr key={q.id}>
                  <td style={{ width: 40 }}><input type="checkbox" aria-label={`Pilih soal ${q.id}`} checked={picked.includes(q.id)} onChange={(e) => setPicked((p) => (e.target.checked ? [...p, q.id] : p.filter((x) => x !== q.id)))} /></td>
                  <td>{q.body}</td><td className="muted small">{q.topic}</td>
                </tr>
              ))}
              {usable.length === 0 ? <tr><td className="muted">Belum ada soal terbit untuk asesmen.</td></tr> : null}
            </tbody>
          </table>
        </div>
        <div style={{ marginTop: 12 }}>
          <button className="primary" disabled={!form.title || !form.short_title || !subjectId || picked.length === 0} onClick={() => run(() => api("/admin/assessments", { method: "POST", body: { ...form, subject_id: subjectId, grade_number: grade, passing_score: form.passing_score === "" ? null : Number(form.passing_score), question_ids: picked } }), "Asesmen dibuat sebagai draft")}>Simpan draft</button>
        </div>
      </div>
    </Shell>
  );
}
