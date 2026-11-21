"use client";

import { useState } from "react";
import Shell, { useAsync } from "@/components/Shell";
import { api } from "@/lib/api";

type Version = { id: number; name: string; version: string; academic_year: string | null; is_active: boolean };
type Source = { id: number; title: string; issuing_authority: string | null; reference: string | null; published_on: string | null; retrieved_on: string | null; verification_status: string; notes: string | null };
type Subject = { id: number; grade_number: number; code: string; name: string; short_label: string; sort_order: number; is_enabled: boolean; curriculum_version_id: number };
type Tree = Subject & { chapters: { id: number; number: number; title: string; semester: number | null; topics: { id: number; title: string; sort_order: number; home_activity: string | null; common_mistake: string | null; lesson_count: number; question_count: number }[] }[] };

export default function CurriculumPage() {
  const versions = useAsync<Version[]>(() => api("/admin/curriculum/versions"));
  const active = versions.data?.find((v) => v.is_active) ?? versions.data?.[0];
  const [grade, setGrade] = useState(1);
  const [subjectId, setSubjectId] = useState<number | null>(null);
  const [msg, setMsg] = useState<{ kind: "ok" | "err"; text: string } | null>(null);

  const sources = useAsync<Source[]>(() => (active ? api(`/admin/curriculum/versions/${active.id}/sources`) : Promise.resolve([])), [active?.id]);
  const subjects = useAsync<Subject[]>(() => (active ? api(`/admin/subjects?version_id=${active.id}&grade=${grade}`) : Promise.resolve([])), [active?.id, grade]);
  const tree = useAsync<Tree | null>(() => (subjectId ? api(`/admin/subjects/${subjectId}/tree`) : Promise.resolve(null)), [subjectId]);

  async function run(fn: () => Promise<unknown>, ok: string, after: () => void) {
    setMsg(null);
    try {
      await fn();
      setMsg({ kind: "ok", text: ok });
      after();
    } catch (e) {
      setMsg({ kind: "err", text: (e as Error).message });
    }
  }

  return (
    <Shell title="Kurikulum" subtitle="Struktur kurikulum dapat dikonfigurasi dan berversi. Jangan mengisi referensi resmi yang belum diverifikasi.">
      {msg ? <div className={`alert ${msg.kind}`} role="status">{msg.text}</div> : null}
      <div className="card">
        <h2>Versi kurikulum</h2>
        <div className="table-wrap">
          <table>
            <thead><tr><th>Nama</th><th>Versi</th><th>Tahun ajaran</th><th>Status</th><th></th></tr></thead>
            <tbody>
              {versions.data?.map((v) => (
                <tr key={v.id}>
                  <td>{v.name}</td><td>{v.version}</td><td>{v.academic_year ?? "–"}</td>
                  <td>{v.is_active ? <span className="chip published">Aktif</span> : <span className="chip draft">Tidak aktif</span>}</td>
                  <td>{!v.is_active ? <button onClick={() => run(() => api(`/admin/curriculum/versions/${v.id}/activate`, { method: "POST" }), "Versi diaktifkan", versions.reload)}>Aktifkan</button> : null}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {active ? <SourcesCard versionId={active.id} sources={sources.data ?? []} onSaved={sources.reload} run={run} /> : null}

      <div className="card">
        <div className="row" style={{ marginBottom: 12 }}>
          <h2 style={{ margin: 0 }}>Mata pelajaran</h2>
          <span className="spacer" />
          <label htmlFor="grade" style={{ margin: 0 }}>Kelas</label>
          <select id="grade" style={{ width: 120 }} value={grade} onChange={(e) => { setGrade(Number(e.target.value)); setSubjectId(null); }}>
            {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((g) => <option key={g} value={g}>Kelas {g} {g <= 6 ? "SD" : "SMP"}</option>)}
          </select>
        </div>
        <div className="row">
          {subjects.data?.map((s) => (
            <button key={s.id} className={subjectId === s.id ? "primary" : ""} onClick={() => setSubjectId(s.id)} aria-pressed={subjectId === s.id}>{s.name}</button>
          ))}
        </div>
        {active ? <AddSubject versionId={active.id} grade={grade} run={run} onSaved={subjects.reload} /> : null}
      </div>

      {tree.data ? <TreeCard tree={tree.data} run={run} reload={tree.reload} /> : null}
    </Shell>
  );
}

type Run = (fn: () => Promise<unknown>, ok: string, after: () => void) => Promise<void>;

function SourcesCard({ versionId, sources, onSaved, run }: { versionId: number; sources: Source[]; onSaved: () => void; run: Run }) {
  const empty = { title: "", issuing_authority: "", reference: "", published_on: "", retrieved_on: "", verification_status: "unverified", notes: "" };
  const [form, setForm] = useState(empty);
  const [editId, setEditId] = useState<number | null>(null);
  const body = { ...form, issuing_authority: form.issuing_authority || null, reference: form.reference || null, published_on: form.published_on || null, retrieved_on: form.retrieved_on || null, notes: form.notes || null };
  return (
    <div className="card">
      <h2>Sumber resmi</h2>
      <p className="muted small" style={{ marginTop: 0 }}>Setiap sumber wajib punya judul, instansi penerbit, nomor dokumen atau URL, tanggal terbit, tanggal pengambilan, dan status verifikasi. Status "terverifikasi" hanya boleh diberi peninjau setelah dokumen dicek.</p>
      <div className="table-wrap" style={{ marginBottom: 14 }}>
        <table>
          <thead><tr><th>Judul</th><th>Penerbit</th><th>Referensi</th><th>Status</th><th></th></tr></thead>
          <tbody>
            {sources.map((s) => (
              <tr key={s.id}>
                <td>{s.title}<div className="muted small">{s.notes}</div></td>
                <td>{s.issuing_authority ?? "–"}</td>
                <td style={{ wordBreak: "break-all" }}>{s.reference ?? "–"}</td>
                <td><span className={`chip ${s.verification_status === "verified" ? "published" : s.verification_status === "rejected" ? "rejected" : "in_review"}`}>{s.verification_status === "verified" ? "Terverifikasi" : s.verification_status === "rejected" ? "Ditolak" : "Belum diverifikasi"}</span></td>
                <td><button onClick={() => { setEditId(s.id); setForm({ title: s.title, issuing_authority: s.issuing_authority ?? "", reference: s.reference ?? "", published_on: s.published_on ?? "", retrieved_on: s.retrieved_on ?? "", verification_status: s.verification_status, notes: s.notes ?? "" }); }}>Ubah</button></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="grid">
        <div className="field"><label htmlFor="s-title">Judul dokumen</label><input id="s-title" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} /></div>
        <div className="field"><label htmlFor="s-auth">Instansi penerbit</label><input id="s-auth" value={form.issuing_authority} onChange={(e) => setForm({ ...form, issuing_authority: e.target.value })} /></div>
        <div className="field"><label htmlFor="s-ref">Nomor dokumen / URL</label><input id="s-ref" value={form.reference} onChange={(e) => setForm({ ...form, reference: e.target.value })} /></div>
        <div className="field"><label htmlFor="s-pub">Tanggal terbit</label><input id="s-pub" type="date" value={form.published_on} onChange={(e) => setForm({ ...form, published_on: e.target.value })} /></div>
        <div className="field"><label htmlFor="s-ret">Tanggal diambil</label><input id="s-ret" type="date" value={form.retrieved_on} onChange={(e) => setForm({ ...form, retrieved_on: e.target.value })} /></div>
        <div className="field"><label htmlFor="s-st">Status</label>
          <select id="s-st" value={form.verification_status} onChange={(e) => setForm({ ...form, verification_status: e.target.value })}>
            <option value="unverified">Belum diverifikasi</option><option value="verified">Terverifikasi</option><option value="rejected">Ditolak</option>
          </select>
        </div>
      </div>
      <div className="field"><label htmlFor="s-notes">Catatan</label><textarea id="s-notes" value={form.notes} onChange={(e) => setForm({ ...form, notes: e.target.value })} /></div>
      <div className="row">
        <button className="primary" disabled={form.title.length < 3} onClick={() => run(() => editId ? api(`/admin/curriculum/sources/${editId}`, { method: "PUT", body }) : api(`/admin/curriculum/versions/${versionId}/sources`, { method: "POST", body }), editId ? "Sumber diperbarui" : "Sumber ditambahkan", () => { setForm(empty); setEditId(null); onSaved(); })}>{editId ? "Simpan perubahan" : "Tambah sumber"}</button>
        {editId ? <button onClick={() => { setEditId(null); setForm(empty); }}>Batal</button> : null}
      </div>
    </div>
  );
}

function AddSubject({ versionId, grade, run, onSaved }: { versionId: number; grade: number; run: Run; onSaved: () => void }) {
  const [name, setName] = useState("");
  const [code, setCode] = useState("");
  const [short, setShort] = useState("");
  return (
    <details style={{ marginTop: 14 }}>
      <summary className="small" style={{ cursor: "pointer", fontWeight: 700 }}>Tambah mata pelajaran untuk kelas {grade}</summary>
      <div className="grid" style={{ marginTop: 10 }}>
        <div className="field"><label htmlFor="sub-name">Nama</label><input id="sub-name" value={name} onChange={(e) => setName(e.target.value)} /></div>
        <div className="field"><label htmlFor="sub-code">Kode</label><input id="sub-code" value={code} onChange={(e) => setCode(e.target.value.toUpperCase())} /></div>
        <div className="field"><label htmlFor="sub-short">Label singkat (maks 4)</label><input id="sub-short" maxLength={4} value={short} onChange={(e) => setShort(e.target.value)} /></div>
      </div>
      <button className="primary" disabled={!name || !code || !short} onClick={() => run(() => api("/admin/subjects", { method: "POST", body: { curriculum_version_id: versionId, grade_number: grade, code, name, short_label: short, sort_order: 50 } }), "Mata pelajaran ditambahkan", () => { setName(""); setCode(""); setShort(""); onSaved(); })}>Tambah</button>
    </details>
  );
}

function TreeCard({ tree, run, reload }: { tree: Tree; run: Run; reload: () => void }) {
  const [chTitle, setChTitle] = useState("");
  const [chNum, setChNum] = useState(1);
  const [topicFor, setTopicFor] = useState<number | null>(null);
  const [topicTitle, setTopicTitle] = useState("");
  const [edit, setEdit] = useState<{ id: number; chapter_id: number; title: string; sort_order: number; home_activity: string; common_mistake: string } | null>(null);
  return (
    <div className="card">
      <h2>{tree.name} · Kelas {tree.grade_number}</h2>
      {tree.chapters.length === 0 ? <p className="muted">Belum ada bab.</p> : null}
      {tree.chapters.map((ch) => (
        <div key={ch.id} style={{ marginBottom: 16 }}>
          <div className="row"><strong>Bab {ch.number} · {ch.title}</strong><span className="spacer" /><button onClick={() => { setTopicFor(ch.id); setTopicTitle(""); }}>+ Topik</button></div>
          <div className="table-wrap" style={{ marginTop: 8 }}>
            <table>
              <thead><tr><th>Topik</th><th>Materi</th><th>Soal</th><th>Kegiatan di rumah (untuk orang tua)</th><th></th></tr></thead>
              <tbody>
                {ch.topics.map((t) => (
                  <tr key={t.id}>
                    <td>{t.title}</td><td>{t.lesson_count}</td><td>{t.question_count}</td>
                    <td className="small">{t.home_activity ?? <span className="muted">Belum diisi</span>}</td>
                    <td><button onClick={() => setEdit({ id: t.id, chapter_id: ch.id, title: t.title, sort_order: t.sort_order, home_activity: t.home_activity ?? "", common_mistake: t.common_mistake ?? "" })}>Ubah</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {topicFor === ch.id ? (
            <div className="row" style={{ marginTop: 8 }}>
              <input aria-label="Judul topik baru" placeholder="Judul topik" value={topicTitle} onChange={(e) => setTopicTitle(e.target.value)} style={{ maxWidth: 360 }} />
              <button className="primary" disabled={topicTitle.length < 2} onClick={() => run(() => api("/admin/topics", { method: "POST", body: { chapter_id: ch.id, title: topicTitle, sort_order: ch.topics.length } }), "Topik ditambahkan", () => { setTopicFor(null); reload(); })}>Simpan</button>
              <button onClick={() => setTopicFor(null)}>Batal</button>
            </div>
          ) : null}
        </div>
      ))}
      {edit ? (
        <div className="card" style={{ background: "var(--sunken)" }}>
          <h2>Ubah topik</h2>
          <div className="field"><label htmlFor="t-title">Judul</label><input id="t-title" value={edit.title} onChange={(e) => setEdit({ ...edit, title: e.target.value })} /></div>
          <div className="field"><label htmlFor="t-act">Kegiatan di rumah</label><textarea id="t-act" value={edit.home_activity} onChange={(e) => setEdit({ ...edit, home_activity: e.target.value })} /></div>
          <div className="field"><label htmlFor="t-mis">Kesalahan umum di topik ini</label><input id="t-mis" value={edit.common_mistake} onChange={(e) => setEdit({ ...edit, common_mistake: e.target.value })} /></div>
          <div className="row">
            <button className="primary" onClick={() => run(() => api(`/admin/topics/${edit.id}`, { method: "PUT", body: { chapter_id: edit.chapter_id, title: edit.title, sort_order: edit.sort_order, home_activity: edit.home_activity || null, common_mistake: edit.common_mistake || null } }), "Topik diperbarui", () => { setEdit(null); reload(); })}>Simpan</button>
            <button onClick={() => setEdit(null)}>Batal</button>
          </div>
        </div>
      ) : null}
      <div className="row" style={{ marginTop: 8 }}>
        <input aria-label="Nomor bab" type="number" min={1} value={chNum} onChange={(e) => setChNum(Number(e.target.value))} style={{ width: 90 }} />
        <input aria-label="Judul bab baru" placeholder="Judul bab baru" value={chTitle} onChange={(e) => setChTitle(e.target.value)} style={{ maxWidth: 360 }} />
        <button className="primary" disabled={chTitle.length < 2} onClick={() => run(() => api("/admin/chapters", { method: "POST", body: { subject_id: tree.id, number: chNum, title: chTitle } }), "Bab ditambahkan", () => { setChTitle(""); reload(); })}>+ Bab</button>
      </div>
    </div>
  );
}
