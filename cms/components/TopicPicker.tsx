"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";

type Subject = { id: number; name: string; grade_number: number };
type Tree = { chapters: { id: number; number: number; title: string; topics: { id: number; title: string }[] }[] };

export default function TopicPicker({ value, onChange }: { value: number | null; onChange: (topicId: number) => void }) {
  const [grade, setGrade] = useState(1);
  const [subjects, setSubjects] = useState<Subject[]>([]);
  const [subjectId, setSubjectId] = useState<number | null>(null);
  const [tree, setTree] = useState<Tree | null>(null);

  const [resolved, setResolved] = useState(false);

  useEffect(() => {
    if (value == null || resolved) return;
    api<{ subject_id: number; grade_number: number }>(`/admin/topics/${value}`).then((t) => {
      setResolved(true);
      setGrade(t.grade_number);
      api<Subject[]>(`/admin/subjects?grade=${t.grade_number}`).then((s) => { setSubjects(s); setSubjectId(t.subject_id); });
    }).catch(() => setResolved(true));
  }, [value, resolved]);

  useEffect(() => {
    if (value != null && !resolved) return;
    api<Subject[]>(`/admin/subjects?grade=${grade}`).then((s) => {
      setSubjects(s);
      setSubjectId((cur) => (cur && s.some((x) => x.id === cur) ? cur : s[0]?.id ?? null));
    }).catch(() => setSubjects([]));
  }, [grade, resolved]);

  useEffect(() => {
    if (!subjectId) { setTree(null); return; }
    api<Tree>(`/admin/subjects/${subjectId}/tree`).then(setTree).catch(() => setTree(null));
  }, [subjectId]);

  return (
    <div className="grid">
      <div className="field">
        <label htmlFor="tp-grade">Kelas</label>
        <select id="tp-grade" value={grade} onChange={(e) => setGrade(Number(e.target.value))}>
          {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((g) => <option key={g} value={g}>Kelas {g}</option>)}
        </select>
      </div>
      <div className="field">
        <label htmlFor="tp-subject">Mata pelajaran</label>
        <select id="tp-subject" value={subjectId ?? ""} onChange={(e) => setSubjectId(Number(e.target.value))}>
          {subjects.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}
        </select>
      </div>
      <div className="field">
        <label htmlFor="tp-topic">Topik</label>
        <select id="tp-topic" value={value ?? ""} onChange={(e) => onChange(Number(e.target.value))}>
          <option value="" disabled>Pilih topik</option>
          {tree?.chapters.map((c) => (
            <optgroup key={c.id} label={`Bab ${c.number} · ${c.title}`}>
              {c.topics.map((t) => <option key={t.id} value={t.id}>{t.title}</option>)}
            </optgroup>
          ))}
        </select>
      </div>
    </div>
  );
}
