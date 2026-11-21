export const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

const KEY = "bobo_cms_session";

export type Session = { token: string; roles: string[]; name: string };

export function getSession(): Session | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = window.sessionStorage.getItem(KEY);
    return raw ? (JSON.parse(raw) as Session) : null;
  } catch {
    return null;
  }
}

export function setSession(s: Session | null) {
  if (s) window.sessionStorage.setItem(KEY, JSON.stringify(s));
  else window.sessionStorage.removeItem(KEY);
}

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

export async function api<T = any>(path: string, init: { method?: string; body?: unknown } = {}): Promise<T> {
  const s = getSession();
  const res = await fetch(`${API_BASE}/v1${path}`, {
    method: init.method ?? "GET",
    headers: { "Content-Type": "application/json", ...(s ? { Authorization: `Bearer ${s.token}` } : {}) },
    body: init.body === undefined ? undefined : JSON.stringify(init.body),
  });
  const text = await res.text();
  const data = text ? JSON.parse(text) : null;
  if (!res.ok) {
    if (res.status === 401) setSession(null);
    const d = data?.detail;
    const msg = typeof d === "string" ? d : Array.isArray(d) && d[0]?.msg ? `${d[0].loc?.slice(-1)[0] ?? ""}: ${d[0].msg}` : `Gagal (${res.status})`;
    throw new ApiError(res.status, msg);
  }
  return data as T;
}

export const STATUS_LABEL: Record<string, string> = {
  draft: "Draft",
  in_review: "Menunggu review",
  approved: "Disetujui",
  rejected: "Ditolak",
  published: "Terbit",
};

export const TYPE_LABEL: Record<string, string> = {
  mc: "Pilihan ganda",
  multi: "Pilihan ganda kompleks",
  tf: "Benar/Salah",
  matching: "Menjodohkan",
  fill: "Isian singkat",
  short: "Jawaban singkat",
  essay: "Esai",
};
