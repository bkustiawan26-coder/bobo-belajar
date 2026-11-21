"use client";

import Link from "next/link";
import Shell, { useAsync } from "@/components/Shell";
import { api } from "@/lib/api";

type Stats = { lessons: Record<string, number>; questions: Record<string, number>; assessments_published: number; students: number; unverified_sources: number; sample_content_published: number };

export default function Dashboard() {
  const { data, error } = useAsync<Stats>(() => api("/admin/stats"));
  return (
    <Shell title="Ringkasan" subtitle="Status konten dan hal yang perlu ditindaklanjuti.">
      {error ? <div className="alert err">{error}</div> : null}
      {data ? (
        <>
          {data.unverified_sources > 0 ? (
            <div className="alert warn">{data.unverified_sources} sumber kurikulum belum terverifikasi. Lengkapi referensi resmi di <Link href="/curriculum">Kurikulum</Link> sebelum rilis.</div>
          ) : null}
          {data.sample_content_published > 0 ? (
            <div className="alert warn">{data.sample_content_published} konten contoh sedang terbit. Konten contoh wajib ditinjau ulang tim kurikulum sebelum dipakai di produksi.</div>
          ) : null}
          <div className="grid" style={{ marginBottom: 16 }}>
            <Kpi label="Materi terbit" value={data.lessons.published} ctx={`${data.lessons.in_review} menunggu review · ${data.lessons.draft} draft`} />
            <Kpi label="Soal terbit" value={data.questions.published} ctx={`${data.questions.in_review} menunggu review · ${data.questions.draft} draft`} />
            <Kpi label="Asesmen terbit" value={data.assessments_published} ctx="semua soal sudah ditinjau" />
            <Kpi label="Profil siswa aktif" value={data.students} ctx="tidak termasuk profil dihapus" />
          </div>
          <div className="card">
            <h2>Alur publikasi</h2>
            <p className="muted" style={{ margin: 0 }}>Draft → Kirim untuk review → Disetujui peninjau (bukan penulisnya) → Terbit. Konten yang diubah setelah terbit kembali ke draft dan harus ditinjau ulang. Hanya konten terbit yang tampil di aplikasi dan dipakai Tutor AI.</p>
          </div>
        </>
      ) : null}
    </Shell>
  );
}

function Kpi({ label, value, ctx }: { label: string; value: number; ctx: string }) {
  return (
    <div className="card kpi" style={{ margin: 0 }}>
      <div className="label">{label}</div>
      <div className="value">{value}</div>
      <div className="ctx">{ctx}</div>
    </div>
  );
}
