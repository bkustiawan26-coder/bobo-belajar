"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { getSession, setSession, type Session } from "@/lib/api";

const NAV = [
  { href: "/dashboard", label: "Ringkasan" },
  { href: "/curriculum", label: "Kurikulum" },
  { href: "/lessons", label: "Materi" },
  { href: "/questions", label: "Bank soal" },
  { href: "/review", label: "Antrean review" },
  { href: "/assessments", label: "Asesmen" },
  { href: "/tools", label: "Impor, AI & audit" },
];

export default function Shell({ title, subtitle, children }: { title: string; subtitle?: string; children: React.ReactNode }) {
  const router = useRouter();
  const path = usePathname();
  const [session, setS] = useState<Session | null>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const s = getSession();
    if (!s) router.replace("/");
    else setS(s);
    setReady(true);
  }, [router]);

  if (!ready || !session) return null;

  return (
    <div className="shell">
      <nav className="side" aria-label="Menu CMS">
        <div className="brand"><span className="logo" aria-hidden="true">BB</span>BOBO CMS</div>
        {NAV.map((n) => (
          <Link key={n.href} href={n.href} className={path?.startsWith(n.href) ? "on" : ""} aria-current={path?.startsWith(n.href) ? "page" : undefined}>
            {n.label}
          </Link>
        ))}
        <div className="who">
          <div><strong>{session.name}</strong></div>
          <div>{session.roles.join(", ")}</div>
          <button style={{ marginTop: 8 }} onClick={() => { setSession(null); router.replace("/"); }}>Keluar</button>
        </div>
      </nav>
      <main className="main">
        <h1>{title}</h1>
        {subtitle ? <p className="muted" style={{ marginTop: 0 }}>{subtitle}</p> : null}
        {children}
      </main>
    </div>
  );
}

export function StatusChip({ status, sample }: { status: string; sample?: boolean }) {
  const labels: Record<string, string> = { draft: "Draft", in_review: "Menunggu review", approved: "Disetujui", rejected: "Ditolak", published: "Terbit" };
  return (
    <span className="row" style={{ gap: 6, display: "inline-flex" }}>
      <span className={`chip ${status}`}>{labels[status] ?? status}</span>
      {sample ? <span className="chip sample">Konten contoh</span> : null}
    </span>
  );
}

export function useAsync<T>(fn: () => Promise<T>, deps: unknown[] = []) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [tick, setTick] = useState(0);
  useEffect(() => {
    let alive = true;
    setError(null);
    fn().then((d) => alive && setData(d)).catch((e: Error) => alive && setError(e.message));
    return () => { alive = false; };
  }, [tick, ...deps]);
  return { data, error, reload: () => setTick((t) => t + 1), setData };
}
