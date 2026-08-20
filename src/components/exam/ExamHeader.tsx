'use client';

import React from 'react';
import {
  Clock,
  Flag,
  Grid,
  FileText,
  Pause,
  Play,
  CheckCircle2,
  SlidersHorizontal,
  Eye,
} from 'lucide-react';
import { ExamMode } from '@/types/exam';
import { ExamTheme } from '@/lib/storage/examStorage';

interface ExamHeaderProps {
  examCode: string;
  examTitle: string;
  mode: ExamMode;
  currentIndex: number;
  totalQuestions: number;
  formattedTime: string;
  isTimerWarning: boolean;
  isTimerCritical: boolean;
  isTimerRunning: boolean;
  isFlagged: boolean;
  theme: ExamTheme;
  onToggleTimer?: () => void;
  onToggleFlag: () => void;
  onOpenQuestionMap: () => void;
  onOpenScratchpad: () => void;
  onOpenReviewScreen: () => void;
  onToggleTheme: () => void;
}

export function ExamHeader({
  examCode,
  examTitle,
  mode,
  currentIndex,
  totalQuestions,
  formattedTime,
  isTimerWarning,
  isTimerCritical,
  isTimerRunning,
  isFlagged,
  theme,
  onToggleTimer,
  onToggleFlag,
  onOpenQuestionMap,
  onOpenScratchpad,
  onOpenReviewScreen,
  onToggleTheme,
}: ExamHeaderProps) {
  const isPearson = theme === 'pearson-vue';

  return (
    <header
      className={`w-full transition-colors duration-200 select-none border-b ${
        isPearson
          ? 'bg-[#002d62] text-white border-[#001f44]'
          : 'bg-slate-900/95 backdrop-blur border-slate-800 text-slate-100'
      }`}
    >
      {/* Top Banner */}
      <div className="max-w-7xl mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
        {/* Left: Exam Info & Mode */}
        <div className="flex items-center gap-3 min-w-0">
          <span
            className={`font-mono text-xs font-bold px-2 py-0.5 rounded ${
              isPearson
                ? 'bg-amber-400 text-slate-950'
                : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
            }`}
          >
            {examCode}
          </span>
          <h1 className="font-semibold text-sm sm:text-base truncate max-w-xs sm:max-w-md">
            {examTitle}
          </h1>
          <span
            className={`hidden md:inline-flex text-[11px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full ${
              mode === 'real'
                ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                : mode === 'practice'
                ? 'bg-blue-500/20 text-blue-300 border border-blue-500/30'
                : 'bg-purple-500/20 text-purple-300 border border-purple-500/30'
            }`}
          >
            {mode === 'real' ? 'Simulado Real' : mode === 'practice' ? 'Modo Treino' : 'Revisão'}
          </span>
        </div>

        {/* Right: Timer & Tools */}
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          {/* Timer Display (Apenas no Modo Real) */}
          {mode === 'real' ? (
            <div
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-sm font-bold transition-all ${
                isTimerCritical
                  ? 'bg-red-500/20 text-red-400 border border-red-500/50 animate-pulse'
                  : isTimerWarning
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                  : isPearson
                  ? 'bg-blue-900/80 text-white border border-blue-800'
                  : 'bg-slate-800 text-slate-200 border border-slate-700'
              }`}
            >
              <Clock className="h-4 w-4 shrink-0" />
              <span>{formattedTime}</span>
            </div>
          ) : (
            <div
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold ${
                isPearson
                  ? 'bg-blue-900/40 text-blue-200 border border-blue-800'
                  : 'bg-slate-800/80 text-slate-400 border border-slate-700/60'
              }`}
            >
              <span>Sem limite de tempo</span>
            </div>
          )}

          {/* Theme Switch */}
          <button
            onClick={onToggleTheme}
            title={isPearson ? 'Alternar para Tema Moderno' : 'Alternar para Tema Pearson VUE'}
            className={`hidden sm:flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-colors border ${
              isPearson
                ? 'bg-blue-900/60 border-blue-700 text-blue-100 hover:bg-blue-800'
                : 'bg-slate-800 border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white'
            }`}
          >
            <SlidersHorizontal className="h-3.5 w-3.5" />
            <span>{isPearson ? 'VUE View' : 'Modern View'}</span>
          </button>
        </div>
      </div>

      {/* Sub Header: Navigation Tools */}
      <div
        className={`px-4 py-2 border-t flex flex-wrap items-center justify-between gap-3 text-xs ${
          isPearson
            ? 'bg-[#00244e] border-blue-950 text-blue-100'
            : 'bg-slate-950/60 border-slate-800/80 text-slate-300'
        }`}
      >
        <div className="flex items-center gap-2 font-medium">
          <span className="font-bold text-sm text-white">
            Questão {currentIndex + 1} de {totalQuestions}
          </span>
        </div>

        <div className="flex items-center gap-2 sm:gap-3">
          {/* Flag Button */}
          <button
            onClick={onToggleFlag}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md font-semibold transition-all border ${
              isFlagged
                ? 'bg-amber-500 text-slate-950 border-amber-400 font-bold shadow-sm shadow-amber-500/20'
                : isPearson
                ? 'bg-blue-900/80 border-blue-700 text-white hover:bg-blue-800'
                : 'bg-slate-800 border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white'
            }`}
          >
            <Flag className={`h-3.5 w-3.5 ${isFlagged ? 'fill-current' : ''}`} />
            <span>{isFlagged ? 'Marcada (F)' : 'Marcar p/ Revisar (F)'}</span>
          </button>

          {/* Scratchpad Button */}
          <button
            onClick={onOpenScratchpad}
            className={`hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-md font-medium transition-colors border ${
              isPearson
                ? 'bg-blue-900/80 border-blue-700 text-white hover:bg-blue-800'
                : 'bg-slate-800 border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white'
            }`}
          >
            <FileText className="h-3.5 w-3.5" />
            <span>Anotações</span>
          </button>

          {/* Question Map */}
          <button
            onClick={onOpenQuestionMap}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md font-medium transition-colors border ${
              isPearson
                ? 'bg-blue-900/80 border-blue-700 text-white hover:bg-blue-800'
                : 'bg-slate-800 border-slate-700 text-slate-300 hover:bg-slate-700 hover:text-white'
            }`}
          >
            <Grid className="h-3.5 w-3.5" />
            <span>Mapa de Questões</span>
          </button>

          {/* End / Review */}
          <button
            onClick={onOpenReviewScreen}
            className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-md font-semibold text-white transition-all shadow-sm ${
              isPearson
                ? 'bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold'
                : 'bg-emerald-600 hover:bg-emerald-500 shadow-emerald-900/30'
            }`}
          >
            <CheckCircle2 className="h-3.5 w-3.5" />
            <span>Revisar & Finalizar</span>
          </button>
        </div>
      </div>
    </header>
  );
}
