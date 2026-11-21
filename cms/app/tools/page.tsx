"use client";

import { useState } from "react";
import Shell, { useAsync } from "@/components/Shell";
import { api, getSession } from "@/lib/api";

type Usage = { days: number; rows: { day: string; purpose: string; requests: number; cost_usd: number; input_tokens: number; output_tokens: number }[]; active_students: number; total_cost_usd: number; cost_per_active_student_usd: number; outcomes: Record<string, number> };
type Prompt = { id: number; purpose: string; version: number; template: string; is_active: boolean };
type Audit = { at: string; action: string; actor: string | null; entity: string | null };
type Version = { id: number; is_active: boolean; name: string };

export default function ToolsPage() {
  const isAdmin = getSession()?.roles.includes("admin") ?? false;
  const [days, setDays] = useState(7);
  const usage = useAsync<Usage | null>(() => (isAdmin ? api(`/admin/ai/usage?days=${days}`) : Promise.resolve(null)), [days]);
  const prompts = useAsync<Prompt[]>(() => (isAdmin ? api("/admin/ai/prompts") : Promise.resolve([])));
  const audit = useAsync<Audit[]>(() => (isAdmin ? api("/admin/audit") : Promise.resolve([])));
  const versions = useAsync<Version[]>(() => api("/admin/curriculum/versions"));
  const [importText, setImportText] = useState("");
  const [exportGrade, setExportGrade] = useState(5);
  const [exported, setExported] = useState("");
  const [newPrompt, setNewPrompt] = useState({ purpose: "tutor", template: "" });
  const [msg, setMsg] = useState<{ kind: "ok" | "err"; text: string } | null>(null);
  const active = versions.data?.find((v) => v.is_active);

  async function run(fn: () => Promise<unknown>, ok: (r: any) => string) {
    setMsg(null);
    try {
      const r = await fn();
      setMsg({ kind: "ok", text: ok(r) });
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  return (
    <Shell title="Impor, AI & audit" subtitle="Impor/ekspor konten, pemakaian dan biaya AI, versi prompt, dan jejak audit.">
      {msg ? <div className={`alert ${msg.kind}`} role="status">{msg.text}</div> : null}

      <div className="card">
        <h2>Ekspor konten</h2>
        <div className="row">
          <select aria-label="Kelas ekspor" style={{ width: 160 }} value={exportGrade} onChange={(e) => setExportGrade(Number(e.target.value))}>{[1, 2, 3, 4, 5, 6, 7, 8, 9].map((g) => <option key={g} value={g}>Kelas {g}</option>)}</select>
          <button onClick={() => run(async () => { const r = await api(`/admin/export?grade=${exportGrade}`); setExported(JSON.stringify(r, null, 2)); return r; }, () => "Ekspor siap. Salin teks di bawah.")}>Ekspor JSON</button>
        </div>
        {exported ? <pre>{exported}</pre> : null}
      </div>

      <div className="card">
        <h2>Impor konten</h2>
        <p className="muted small" style={{ marginTop: 0 }}>Format <code>bobo-content-v1</code> (sama dengan hasil ekspor; isi <code>subjects</code>). Semua hasil impor menjadi draft dan wajib ditinjau. Versi kurikulum tujuan: {active?.name ?? "–"}.</p>
        <textarea aria-label="JSON impor" style={{ minHeight: 160, fontFamily: "monospace", fontSize: 12 }} value={importText} onChange={(e) => setImportText(e.target.value)} placeholder='{"format":"bobo-content-v1","subjects":[...]}' />
        <button className="primary" style={{ marginTop: 8 }} disabled={!importText || !active} onClick={() => run(async () => {
          let parsed: any;
          try { parsed = JSON.parse(importText); } catch { throw new Error("JSON tidak valid"); }
          return api("/admin/import", { method: "POST", body: { format: "bobo-content-v1", curriculum_version_id: active!.id, subjects: parsed.subjects ?? [] } });
        }, (r) => `Impor berhasil: ${r.subjects} mapel, ${r.chapters} bab, ${r.topics} topik, ${r.lessons} materi, ${r.questions} soal (semua draft).`)}>Impor</button>
      </div>

      {isAdmin ? (
        <>
          <div className="card">
            <div className="row" style={{ marginBottom: 12 }}>
              <h2 style={{ margin: 0 }}>Pemakaian AI</h2><span className="spacer" />
              <select aria-label="Rentang hari" style={{ width: 140 }} value={days} onChange={(e) => setDays(Number(e.target.value))}><option value={7}>7 hari</option><option value={30}>30 hari</option><option value={90}>90 hari</option></select>
            </div>
            {usage.data ? (
              <>
                <div className="grid" style={{ marginBottom: 12 }}>
                  <div className="card kpi" style={{ margin: 0 }}><div className="label">Total biaya</div><div className="value">${usage.data.total_cost_usd.toFixed(2)}</div><div className="ctx">{days} hari terakhir, dari log token</div></div>
                  <div className="card kpi" style={{ margin: 0 }}><div className="label">Siswa aktif memakai Tutor</div><div className="value">{usage.data.active_students}</div><div className="ctx">unik per siswa</div></div>
                  <div className="card kpi" style={{ margin: 0 }}><div className="label">Biaya per siswa aktif</div><div className="value">${usage.data.cost_per_active_student_usd.toFixed(3)}</div><div className="ctx">mode grounded = $0</div></div>
                </div>
                <div className="small muted" style={{ marginBottom: 8 }}>Hasil: {Object.entries(usage.data.outcomes).map(([k, v]) => `${k} ${v}`).join(" · ") || "belum ada"}</div>
                <div className="table-wrap">
                  <table>
                    <thead><tr><th>Tanggal</th><th>Untuk</th><th>Permintaan</th><th>Token masuk/keluar</th><th>Biaya</th></tr></thead>
                    <tbody>
                      {usage.data.rows.map((r, i) => <tr key={i}><td>{r.day}</td><td>{r.purpose === "tutor" ? "Tutor anak" : "Tanya BOBO"}</td><td>{r.requests}</td><td>{r.input_tokens}/{r.output_tokens}</td><td>${r.cost_usd.toFixed(4)}</td></tr>)}
                      {usage.data.rows.length === 0 ? <tr><td colSpan={5} className="muted">Belum ada pemakaian.</td></tr> : null}
                    </tbody>
                  </table>
                </div>
              </>
            ) : null}
          </div>

          <div className="card">
            <h2>Versi prompt AI</h2>
            {prompts.data?.map((p) => (
              <details key={p.id} style={{ marginBottom: 8 }}>
                <summary style={{ cursor: "pointer" }}><strong>{p.purpose === "tutor" ? "Tutor anak" : "Tanya BOBO"}</strong> · versi {p.version} {p.is_active ? <span className="chip published">Aktif</span> : null}</summary>
                <pre>{p.template}</pre>
              </details>
            ))}
            <div className="field"><label htmlFor="p-purpose">Untuk</label><select id="p-purpose" style={{ maxWidth: 240 }} value={newPrompt.purpose} onChange={(e) => setNewPrompt({ ...newPrompt, purpose: e.target.value })}><option value="tutor">Tutor anak</option><option value="parent">Tanya BOBO</option></select></div>
            <div className="field"><label htmlFor="p-tpl">Template baru (wajib memuat {"{grade}"} dan {"{level}"})</label><textarea id="p-tpl" style={{ minHeight: 140 }} value={newPrompt.template} onChange={(e) => setNewPrompt({ ...newPrompt, template: e.target.value })} /></div>
            <button className="primary" disabled={newPrompt.template.length < 20} onClick={() => run(() => api("/admin/ai/prompts", { method: "POST", body: { ...newPrompt, activate: true } }), () => { prompts.reload(); return "Versi prompt baru aktif"; })}>Simpan sebagai versi aktif</button>
          </div>

          <div className="card">
            <h2>Jejak audit (200 terakhir)</h2>
            <div className="table-wrap" style={{ maxHeight: 360, overflowY: "auto" }}>
              <table>
                <thead><tr><th>Waktu</th><th>Aksi</th><th>Objek</th></tr></thead>
                <tbody>{audit.data?.map((a, i) => <tr key={i}><td className="small">{new Date(a.at).toLocaleString("id-ID")}</td><td>{a.action}</td><td className="small">{a.entity ?? "–"}</td></tr>)}</tbody>
              </table>
            </div>
          </div>
        </>
      ) : <div className="alert warn">Pemakaian AI, prompt, dan audit hanya untuk admin.</div>}
    </Shell>
  );
}
