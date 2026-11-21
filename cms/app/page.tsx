"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { api, getSession, setSession } from "@/lib/api";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    if (getSession()) router.replace("/dashboard");
  }, [router]);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError(null);
    try {
      const r = await api<{ access_token: string; roles: string[]; display_name: string }>("/auth/login", { method: "POST", body: { email, password } });
      const staff = r.roles.filter((x) => ["admin", "editor", "reviewer"].includes(x));
      if (!staff.length) {
        setError("Akun ini bukan akun staf konten.");
        return;
      }
      setSession({ token: r.access_token, roles: staff, name: r.display_name });
      router.replace("/dashboard");
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="login">
      <form className="card" onSubmit={submit} aria-labelledby="login-title">
        <div className="row" style={{ marginBottom: 16 }}>
          <span style={{ width: 40, height: 40, borderRadius: 12, background: "#1e3a5f", color: "#fff", display: "grid", placeItems: "center", fontWeight: 800 }} aria-hidden="true">BB</span>
          <div>
            <h1 id="login-title" style={{ fontSize: 20 }}>BOBO BELAJAR CMS</h1>
            <div className="muted small">Khusus admin, editor, dan peninjau konten</div>
          </div>
        </div>
        {error ? <div className="alert err" role="alert">{error}</div> : null}
        <div className="field">
          <label htmlFor="email">Email</label>
          <input id="email" type="email" autoComplete="username" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </div>
        <div className="field">
          <label htmlFor="pw">Kata sandi</label>
          <input id="pw" type="password" autoComplete="current-password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </div>
        <button className="primary" style={{ width: "100%" }} disabled={busy}>{busy ? "Memeriksa…" : "Masuk"}</button>
        <p className="muted small" style={{ marginBottom: 0 }}>Sesi tersimpan di tab ini saja dan berakhir otomatis.</p>
      </form>
    </div>
  );
}
