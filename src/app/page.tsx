'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { getAllExams } from '@/data/exams';
import { ExamCard } from '@/components/dashboard/ExamCard';
import { getAllAttempts } from '@/lib/storage/examStorage';
import { ExamAttempt } from '@/types/exam';
import { Award, CheckCircle2, History, Layers, Zap, Clock, ArrowRight, ShieldAlert } from 'lucide-react';

export default function HomePage() {
  const exams = getAllExams();
  const [attempts, setAttempts] = useState<ExamAttempt[]>([]);

  useEffect(() => {
    setAttempts(getAllAttempts());
  }, []);

  const totalQuestionsInBank = exams.reduce((acc, e) => acc + e.questions.length, 0);
  const completedAttempts = attempts.filter((a) => a.isCompleted);
  const passedAttempts = completedAttempts.filter((a) => a.score?.passed);
  const averageScore =
    completedAttempts.length > 0
      ? Math.round(
          completedAttempts.reduce((acc, a) => acc + (a.score?.scaledScore || 0), 0) /
            completedAttempts.length
        )
      : 0;

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 pb-20">
      {/* Hero Section */}
      <section className="relative overflow-hidden border-b border-slate-800/80 bg-gradient-to-b from-slate-900/60 via-slate-950 to-slate-950 pt-12 pb-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold mb-4">
              <Zap className="h-3.5 w-3.5" />
              <span>Official Client-Side Simulator • 100% Offline & Private</span>
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-tight">
              Prepare for your <span className="bg-gradient-to-r from-amber-400 to-orange-500 bg-clip-text text-transparent">AWS</span> certification
            </h1>

            <p className="mt-4 text-base sm:text-lg text-slate-400 leading-relaxed">
              Realistic exam simulations with complex scenario-based questions, official timers, elimination strike-through, detailed explanations, and domain breakdowns.
            </p>
          </div>

          {/* Quick Metrics Bar */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-10">
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Certifications</p>
              <p className="text-2xl font-black text-white mt-1">{exams.length}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Question Bank</p>
              <p className="text-2xl font-black text-amber-400 mt-1">{totalQuestionsInBank}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Exams Completed</p>
              <p className="text-2xl font-black text-emerald-400 mt-1">{completedAttempts.length}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Average Score</p>
              <p className="text-2xl font-black text-white mt-1">
                {averageScore > 0 ? `${averageScore}/1000` : '—'}
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Main Catalog */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
          <div>
            <h2 className="text-2xl font-black text-white">Certification Catalog</h2>
            <p className="text-xs sm:text-sm text-slate-400">
              Select an exam to start in Real Exam or Practice Mode
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {exams.map((exam) => (
            <ExamCard key={exam.id} exam={exam} />
          ))}
        </div>
      </section>

      {/* Recent Activity */}
      {completedAttempts.length > 0 && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16">
          <div className="flex items-center justify-between gap-4 mb-6">
            <div className="flex items-center gap-2">
              <History className="h-5 w-5 text-amber-400" />
              <h2 className="text-xl font-bold text-white">Recent Attempts</h2>
            </div>
            <Link
              href="/history"
              className="text-xs font-semibold text-amber-400 hover:text-amber-300 flex items-center gap-1"
            >
              <span>View full history</span>
              <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </div>

          <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm text-slate-300">
                <thead className="bg-slate-950/80 text-xs uppercase font-bold text-slate-400 border-b border-slate-800">
                  <tr>
                    <th className="px-6 py-3.5">Exam</th>
                    <th className="px-6 py-3.5">Mode</th>
                    <th className="px-6 py-3.5">Score</th>
                    <th className="px-6 py-3.5">Result</th>
                    <th className="px-6 py-3.5">Date</th>
                    <th className="px-6 py-3.5 text-right">Report</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {completedAttempts.slice(0, 5).map((att) => (
                    <tr key={att.id} className="hover:bg-slate-800/40 transition-colors">
                      <td className="px-6 py-4 font-bold text-white">
                        {att.examCode}
                      </td>
                      <td className="px-6 py-4 text-xs capitalize text-slate-400">
                        {att.mode === 'real' ? 'Real Exam' : 'Practice Mode'}
                      </td>
                      <td className="px-6 py-4 font-mono font-bold text-white">
                        {att.score?.scaledScore} / 1000 ({att.score?.percentage}%)
                      </td>
                      <td className="px-6 py-4">
                        {att.score?.passed ? (
                          <span className="inline-flex items-center gap-1 text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full">
                            <CheckCircle2 className="h-3.5 w-3.5" />
                            Passed
                          </span>
                        ) : (
                          <span className="inline-flex items-center gap-1 text-xs font-bold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-full">
                            Failed
                          </span>
                        )}
                      </td>
                      <td className="px-6 py-4 text-xs text-slate-400">
                        {att.completedAt
                          ? new Date(att.completedAt).toLocaleDateString('en-US', {
                              month: 'short',
                              day: 'numeric',
                              year: 'numeric',
                            })
                          : '—'}
                      </td>
                      <td className="px-6 py-4 text-right">
                        <Link
                          href={`/exams/${att.examId}/result?attemptId=${att.id}`}
                          className="text-xs font-bold text-amber-400 hover:text-amber-300 underline"
                        >
                          View Review
                        </Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
