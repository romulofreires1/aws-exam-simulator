'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { Clock, ShieldCheck, HelpCircle, ArrowRight, Play, RotateCcw, Award, CheckCircle } from 'lucide-react';
import { ExamDefinition, ExamAttempt } from '@/types/exam';
import { getActiveSession, getAttemptsByExamId } from '@/lib/storage/examStorage';

interface ExamCardProps {
  exam: ExamDefinition;
}

export function ExamCard({ exam }: ExamCardProps) {
  const [activeSession, setActiveSession] = useState<ExamAttempt | null>(null);
  const [historyAttempts, setHistoryAttempts] = useState<ExamAttempt[]>([]);

  useEffect(() => {
    setActiveSession(getActiveSession(exam.id));
    setHistoryAttempts(getAttemptsByExamId(exam.id));
  }, [exam.id]);

  const bestAttempt = historyAttempts.reduce<ExamAttempt | null>((best, current) => {
    if (!current.score) return best;
    if (!best || (current.score.scaledScore > (best.score?.scaledScore || 0))) {
      return current;
    }
    return best;
  }, null);

  const categoryColor =
    exam.category === 'Professional'
      ? 'bg-purple-500/20 text-purple-300 border-purple-500/30'
      : exam.category === 'Associate'
      ? 'bg-blue-500/20 text-blue-300 border-blue-500/30'
      : exam.category === 'Specialty'
      ? 'bg-amber-500/20 text-amber-300 border-amber-500/30'
      : 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30';

  return (
    <div className="group relative rounded-3xl border border-slate-800 bg-slate-900/90 p-6 sm:p-7 shadow-xl hover:border-slate-700 hover:shadow-2xl transition-all duration-200 flex flex-col justify-between">
      {/* Top Details */}
      <div>
        <div className="flex items-center justify-between gap-3 mb-4">
          <span className="font-mono text-xs font-black px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 shadow-sm">
            {exam.code}
          </span>
          <span className={`text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full border ${categoryColor}`}>
            {exam.category}
          </span>
        </div>

        <h3 className="text-xl font-black text-white group-hover:text-amber-400 transition-colors leading-snug mb-2">
          {exam.title}
        </h3>

        <p className="text-xs text-slate-400 leading-relaxed mb-6 line-clamp-2">
          {exam.description}
        </p>

        {/* Exam Specifications */}
        <div className="grid grid-cols-3 gap-2 py-3 px-3.5 bg-slate-950/60 rounded-xl border border-slate-800/80 text-center mb-6">
          <div>
            <p className="text-[10px] uppercase font-bold text-slate-500">Questões</p>
            <p className="text-sm font-bold text-slate-200">{exam.questions.length}</p>
          </div>
          <div className="border-x border-slate-800">
            <p className="text-[10px] uppercase font-bold text-slate-500">Tempo</p>
            <p className="text-sm font-bold text-slate-200">{exam.timeLimitMinutes} min</p>
          </div>
          <div>
            <p className="text-[10px] uppercase font-bold text-slate-500">Nota Corte</p>
            <p className="text-sm font-bold text-slate-200">{exam.passingScore}/1000</p>
          </div>
        </div>

        {/* History / Active Session Status */}
        {activeSession && !activeSession.isCompleted && (
          <div className="mb-4 p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-between text-xs">
            <div className="flex items-center gap-2 text-amber-300 font-semibold">
              <RotateCcw className="h-4 w-4 animate-spin" />
              <span>Sessão em andamento ({activeSession.mode === 'real' ? 'Real' : 'Treino'})</span>
            </div>
            <Link
              href={`/exams/${exam.id}/runner?mode=${activeSession.mode}`}
              className="text-amber-400 hover:text-amber-300 font-bold underline text-xs"
            >
              Continuar
            </Link>
          </div>
        )}

        {bestAttempt?.score && (
          <div className="mb-4 px-3.5 py-2 rounded-xl bg-slate-950/40 border border-slate-800/80 flex items-center justify-between text-xs">
            <span className="text-slate-400 flex items-center gap-1.5">
              <Award className="h-4 w-4 text-amber-400" />
              Melhor Pontuação:
            </span>
            <span
              className={`font-black ${
                bestAttempt.score.passed ? 'text-emerald-400' : 'text-rose-400'
              }`}
            >
              {bestAttempt.score.scaledScore} / 1000 ({bestAttempt.score.percentage}%)
            </span>
          </div>
        )}
      </div>

      {/* Action Buttons */}
      <div className="grid grid-cols-2 gap-3 mt-2">
        <Link
          href={`/exams/${exam.id}/runner?mode=practice`}
          className="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white font-bold text-xs border border-slate-700 transition-colors"
        >
          <HelpCircle className="h-3.5 w-3.5 text-blue-400" />
          <span>Modo Treino</span>
        </Link>

        <Link
          href={`/exams/${exam.id}/runner?mode=real`}
          className="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-slate-950 font-black text-xs shadow-md shadow-orange-500/20 transition-all hover:scale-[1.02]"
        >
          <Play className="h-3.5 w-3.5 fill-current" />
          <span>Simulado Real</span>
        </Link>
      </div>
    </div>
  );
}
