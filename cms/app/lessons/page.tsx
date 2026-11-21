"use client";

import Link from "next/link";
import { useState } from "react";
import Shell, { StatusChip, useAsync } from "@/components/Shell";
import { api } from "@/lib/api";

type Lesson = { id: number; title: string; topic: string; minutes: number; status: string; version: number; is_sample: boolean; blocks: unknown[]; updated_at: string | null };

export default function LessonsPage() {
  const [status, setStatus] = useState("");
  const { data, error } = useAsync<Lesson[]>(() => api(`/admin/lessons${status ? `?status_filter=${status}` : ""}`), [status]);
  return (
    <Shell title="Materi" subtitle="Materi pelajaran per topik. Hanya materi terbit yang tampil di aplikasi.">
      <div className="row" style={{ marginBottom: 14 }}>
        <label htmlFor="st" style={{ margin: 0 }}>Status</label>
        <select id="st" style={{ width: 200 }} value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="">Semua</option><option value="draft">Draft</option><option value="in_review">Menunggu review</option><option value="approved">Disetujui</option><option value="rejected">Ditolak</option><option value="published">Terbit</option>
        </select>
        <span className="spacer" />
        <Link className="btn" href="/lessons/new" style={{ background: "var(--brand)", color: "#fff", textDecoration: "none" }}>+ Materi baru</Link>
      </div>
      {error ? <div className="alert err">{error}</div> : null}
      <div className="table-wrap">
        <table>
          <thead><tr><th>Judul</th><th>Topik</th><th>Bagian</th><th>Status</th><th>Versi</th></tr></thead>
          <tbody>
            {data?.map((l) => (
              <tr key={l.id}>
                <td><Link href={`/lessons/${l.id}`}>{l.title}</Link></td>
                <td>{l.topic}</td>
                <td>{l.blocks.length} · {l.minutes} mnt</td>
                <td><StatusChip status={l.status} sample={l.is_sample} /></td>
                <td>{l.version}</td>
              </tr>
            ))}
            {data && data.length === 0 ? <tr><td colSpan={5} className="muted">Belum ada materi.</td></tr> : null}
          </tbody>
        </table>
      </div>
    </Shell>
  );
}
