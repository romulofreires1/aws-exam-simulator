'use client';

import React, { useEffect } from 'react';
import confetti from 'canvas-confetti';
import { Award, CheckCircle2, XCircle, Clock, Calendar, Shield } from 'lucide-react';
import { ExamAttempt } from '@/types/exam';

interface ScoreCardProps {
  attempt: ExamAttempt;
  passingScore: number;
}

export function ScoreCard({ attempt, passingScore }: ScoreCardProps) {
  const score = attempt.score;
  const passed = score?.passed || false;
  const scaledScore = score?.scaledScore || 100;
  const percentage = score?.percentage || 0;

  useEffect(() => {
    if (passed) {
      try {
        confetti({
          particleCount: 100,
          spread: 70,
          origin: { y: 0.6 },
        });
      } catch (e) {
        // Fallback safe
      }
    }
  }, [passed]);

  const formatDuration = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}m ${secs}s`;
  };

  const formattedDate = attempt.completedAt
    ? new Date(attempt.completedAt).toLocaleDateString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      })
    : '';

  return (
    <div
      className={`rounded-3xl border p-6 sm:p-8 relative overflow-hidden shadow-2xl transition-all ${
        passed
          ? 'bg-gradient-to-br from-slate-900 via-emerald-950/30 to-slate-900 border-emerald-500/40 shadow-emerald-950/30'
          : 'bg-gradient-to-br from-slate-900 via-rose-950/30 to-slate-900 border-rose-500/40 shadow-rose-950/30'
      }`}
    >
      <div className="flex flex-col md:flex-row items-center justify-between gap-8">
        {/* Left: Result Badge & Title */}
        <div className="flex items-center gap-5 text-center md:text-left">
          <div
            className={`flex h-20 w-20 shrink-0 items-center justify-center rounded-2xl shadow-xl ${
              passed
                ? 'bg-emerald-500 text-slate-950 shadow-emerald-500/20'
                : 'bg-rose-500 text-white shadow-rose-500/20'
            }`}
          >
            {passed ? <CheckCircle2 className="h-12 w-12" /> : <XCircle className="h-12 w-12" />}
          </div>
          <div>
            <div className="flex items-center justify-center md:justify-start gap-2 mb-1">
              <span
                className={`text-xs font-black uppercase tracking-widest px-2.5 py-0.5 rounded-full ${
                  passed
                    ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                    : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                }`}
              >
                {passed ? 'APROVADO (PASS)' : 'NÃO APROVADO (FAIL)'}
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-black text-white">
              {attempt.examCode} - {attempt.examTitle}
            </h1>
            <div className="flex flex-wrap items-center justify-center md:justify-start gap-4 mt-2 text-xs text-slate-400">
              <span className="flex items-center gap-1">
                <Calendar className="h-3.5 w-3.5" />
                {formattedDate}
              </span>
              <span className="flex items-center gap-1">
                <Clock className="h-3.5 w-3.5" />
                Tempo: {formatDuration(attempt.totalTimeSpentSeconds)}
              </span>
            </div>
          </div>
        </div>

        {/* Right: Scaled Score & Progress Gauge */}
        <div className="bg-slate-950/70 border border-slate-800/80 rounded-2xl p-5 min-w-[240px] text-center">
          <p className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">
            Pontuação Oficial AWS (100–1000)
          </p>
          <div className="flex items-baseline justify-center gap-1.5">
            <span
              className={`text-4xl sm:text-5xl font-black tracking-tight ${
                passed ? 'text-emerald-400' : 'text-rose-400'
              }`}
            >
              {scaledScore}
            </span>
            <span className="text-slate-500 font-semibold text-sm">/ 1000</span>
          </div>

          <div className="mt-3 space-y-1 text-xs">
            <div className="flex justify-between text-slate-400">
              <span>Nota de corte necessária:</span>
              <span className="font-bold text-slate-200">{passingScore}</span>
            </div>
            <div className="flex justify-between text-slate-400">
              <span>Taxa de Acertos:</span>
              <span className="font-bold text-slate-200">
                {score?.totalCorrect} de {score?.totalQuestions} ({percentage}%)
              </span>
            </div>
          </div>

          {/* Progress bar */}
          <div className="w-full bg-slate-800 h-2 rounded-full mt-3 overflow-hidden">
            <div
              className={`h-full rounded-full transition-all duration-1000 ${
                passed ? 'bg-emerald-500' : 'bg-rose-500'
              }`}
              style={{ width: `${Math.min(100, Math.max(10, (scaledScore / 1000) * 100))}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
