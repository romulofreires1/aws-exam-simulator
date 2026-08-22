'use client';

import React, { useEffect } from 'react';
import { AlertTriangle, LogOut, ArrowLeft, Layers, CheckCircle2, Clock } from 'lucide-react';
import { ExamMode, ExamLanguage } from '@/types/exam';
import { ExamTheme } from '@/lib/storage/examStorage';

interface ExamAbandonModalProps {
  isOpen: boolean;
  examCode: string;
  examTitle: string;
  mode: ExamMode;
  currentIndex: number;
  totalQuestions: number;
  formattedTime: string;
  stats: {
    total: number;
    answeredCount: number;
    unansweredCount: number;
    flaggedCount: number;
    percentage: number;
  };
  theme: ExamTheme;
  language?: ExamLanguage;
  onClose: () => void;
  onConfirmAbandon: () => void;
}

const TEXTS: Record<
  ExamLanguage,
  {
    badge: string;
    title: string;
    description: string;
    warningNote: string;
    timeLabel: string;
    questionLabel: string;
    answeredLabel: string;
    progressLabel: string;
    cancelBtn: string;
    confirmBtn: string;
  }
> = {
  pt: {
    badge: 'Confirmação',
    title: 'Abandonar o Exame?',
    description:
      'Tem certeza de que deseja abandonar este exame? Todo o seu progresso, respostas e tempo gasto nesta tentativa serão descartados e não poderão ser recuperados.',
    warningNote:
      'Esta ação não salvará o histórico desta tentativa e removerá a sessão ativa salva no navegador.',
    timeLabel: 'Tempo',
    questionLabel: 'Questão',
    answeredLabel: 'Respondidas',
    progressLabel: 'Progresso Geral',
    cancelBtn: 'Continuar no Exame',
    confirmBtn: 'Sim, Abandonar Exame',
  },
  es: {
    badge: 'Confirmación',
    title: '¿Abandonar el Examen?',
    description:
      '¿Estás seguro de que deseas abandonar este examen? Todo tu progreso, respuestas y tiempo transcurrido en este intento se descartarán permanentemente.',
    warningNote:
      'Esta acción no guardará el historial de este intento y eliminará la sesión activa guardada en el navegador.',
    timeLabel: 'Tiempo',
    questionLabel: 'Pregunta',
    answeredLabel: 'Respondidas',
    progressLabel: 'Progreso General',
    cancelBtn: 'Continuar en el Examen',
    confirmBtn: 'Sí, Abandonar Examen',
  },
  en: {
    badge: 'Confirmation',
    title: 'Abandon Exam?',
    description:
      'Are you sure you want to abandon this exam? All your progress, answers, and time spent on this attempt will be discarded and cannot be recovered.',
    warningNote:
      'This action will not save this attempt to your history and will remove any saved in-progress session.',
    timeLabel: 'Time',
    questionLabel: 'Question',
    answeredLabel: 'Answered',
    progressLabel: 'Overall Progress',
    cancelBtn: 'Keep Taking Exam',
    confirmBtn: 'Yes, Abandon Exam',
  },
};

export function ExamAbandonModal({
  isOpen,
  examCode,
  examTitle,
  mode,
  currentIndex,
  totalQuestions,
  formattedTime,
  stats,
  theme,
  language = 'pt',
  onClose,
  onConfirmAbandon,
}: ExamAbandonModalProps) {
  const isPearson = theme === 'pearson-vue';
  const t = TEXTS[language] || TEXTS.pt;

  // Atalho de teclado: Escape fecha / cancela o abandono
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/85 backdrop-blur-md animate-in fade-in duration-200"
    >
      <div
        className={`relative w-full max-w-lg rounded-3xl border shadow-2xl overflow-hidden p-6 sm:p-8 transition-all animate-in zoom-in-95 duration-200 ${
          isPearson
            ? 'bg-[#001f44] border-red-900/80 text-white'
            : 'bg-slate-900/95 border-rose-900/50 text-slate-100'
        }`}
      >
        {/* Top Header Badge */}
        <div className="flex items-center justify-between gap-3 mb-5">
          <div className="flex items-center gap-2">
            <span
              className={`font-mono text-xs font-black px-2.5 py-1 rounded-lg ${
                isPearson
                  ? 'bg-amber-400 text-slate-950'
                  : 'bg-amber-500 text-slate-950 shadow-sm'
              }`}
            >
              {examCode}
            </span>
            <span
              className={`text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full ${
                mode === 'real'
                  ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                  : 'bg-blue-500/20 text-blue-300 border border-blue-500/30'
              }`}
            >
              {mode === 'real' ? 'Real Exam' : 'Practice Mode'}
            </span>
          </div>

          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-rose-500/15 border border-rose-500/40 text-rose-300 text-xs font-bold">
            <AlertTriangle className="h-3.5 w-3.5 text-rose-400" />
            <span>{t.badge}</span>
          </div>
        </div>

        {/* Title and Icon */}
        <div className="text-center mb-6">
          <div className="mx-auto w-16 h-16 rounded-2xl bg-rose-500/15 border border-rose-500/30 flex items-center justify-center text-rose-400 mb-4 shadow-lg shadow-rose-500/10">
            <LogOut className="h-8 w-8" />
          </div>
          <h2 className="text-2xl font-black text-white mb-2 tracking-tight">
            {t.title}
          </h2>
          <p className="text-sm text-slate-300 max-w-md mx-auto leading-relaxed">
            {t.description}
          </p>
        </div>

        {/* Metrics Box */}
        <div className="grid grid-cols-3 gap-2.5 mb-5">
          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <Clock className="h-3 w-3 text-amber-400" />
              <span>{t.timeLabel}</span>
            </div>
            <p className="font-mono font-bold text-xs sm:text-sm text-amber-300">
              {mode === 'real' ? formattedTime : 'No limit'}
            </p>
          </div>

          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <Layers className="h-3 w-3 text-blue-400" />
              <span>{t.questionLabel}</span>
            </div>
            <p className="font-bold text-xs sm:text-sm text-white">
              {currentIndex + 1} / {totalQuestions}
            </p>
          </div>

          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <CheckCircle2 className="h-3 w-3 text-emerald-400" />
              <span>{t.answeredLabel}</span>
            </div>
            <p className="font-bold text-xs sm:text-sm text-emerald-400">
              {stats.answeredCount} ({stats.percentage}%)
            </p>
          </div>
        </div>

        {/* Warning Note */}
        <div className="mb-6 p-3.5 rounded-2xl bg-rose-950/30 border border-rose-900/50 text-xs text-rose-200/90 flex items-start gap-2.5">
          <AlertTriangle className="h-4 w-4 text-rose-400 shrink-0 mt-0.5" />
          <p className="leading-relaxed">{t.warningNote}</p>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col-reverse sm:flex-row items-center gap-3">
          {/* Cancel / Keep taking exam */}
          <button
            type="button"
            onClick={onClose}
            autoFocus
            className="w-full sm:flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white text-xs sm:text-sm font-bold transition-all cursor-pointer"
          >
            <ArrowLeft className="h-4 w-4" />
            <span>{t.cancelBtn}</span>
          </button>

          {/* Confirm Abandon Button */}
          <button
            type="button"
            onClick={onConfirmAbandon}
            className="w-full sm:flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-xl font-black text-xs sm:text-sm transition-all shadow-lg bg-rose-600 hover:bg-rose-500 text-white shadow-rose-900/40 hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
          >
            <LogOut className="h-4 w-4" />
            <span>{t.confirmBtn}</span>
          </button>
        </div>
      </div>
    </div>
  );
}
