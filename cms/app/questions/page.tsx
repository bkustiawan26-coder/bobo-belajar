"use client";

import Link from "next/link";
import { useState } from "react";
import Shell, { StatusChip, useAsync } from "@/components/Shell";
import { api, TYPE_LABEL } from "@/lib/api";

type Q = { id: number; body: string; topic: string; type: string; difficulty: string; usage: string; status: string; is_sample: boolean };

export default function QuestionsPage() {
  const [status, setStatus] = useState("");
  const { data, error } = useAsync<Q[]>(() => api(`/admin/questions${status ? `?status_filter=${status}` : ""}`), [status]);
  return (
    <Shell title="Bank soal" subtitle="Setiap soal wajib punya kunci, pembahasan, sumber, dan lolos review sebelum terbit.">
      <div className="row" style={{ marginBottom: 14 }}>
        <label htmlFor="st" style={{ margin: 0 }}>Status</label>
        <select id="st" style={{ width: 200 }} value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="">Semua</option><option value="draft">Draft</option><option value="in_review">Menunggu review</option><option value="approved">Disetujui</option><option value="rejected">Ditolak</option><option value="published">Terbit</option>
        </select>
        <span className="spacer" />
        <Link className="btn" href="/questions/new" style={{ background: "var(--brand)", color: "#fff", textDecoration: "none" }}>+ Soal baru</Link>
      </div>
      {error ? <div className="alert err">{error}</div> : null}
      <div className="table-wrap">
        <table>
          <thead><tr><th>Soal</th><th>Topik</th><th>Tipe</th><th>Penggunaan</th><th>Status</th></tr></thead>
          <tbody>
            {data?.map((q) => (
              <tr key={q.id}>
                <td style={{ maxWidth: 420 }}><Link href={`/questions/${q.id}`}>{q.body.length > 90 ? `${q.body.slice(0, 90)}…` : q.body}</Link></td>
                <td>{q.topic}</td>
                <td>{TYPE_LABEL[q.type] ?? q.type}<div className="muted small">{q.difficulty}</div></td>
                <td>{q.usage === "both" ? "Latihan & asesmen" : q.usage === "practice" ? "Latihan" : "Asesmen"}</td>
                <td><StatusChip status={q.status} sample={q.is_sample} /></td>
              </tr>
            ))}
            {data && data.length === 0 ? <tr><td colSpan={5} className="muted">Belum ada soal.</td></tr> : null}
          </tbody>
        </table>
      </div>
    </Shell>
  );
}
