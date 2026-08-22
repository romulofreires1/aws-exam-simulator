'use client';

import React, { useEffect } from 'react';
import {
  Play,
  Clock,
  CheckCircle2,
  Flag,
  Home,
  HelpCircle,
  PauseCircle,
  Layers,
  Sparkles,
} from 'lucide-react';
import { ExamMode } from '@/types/exam';
import { ExamTheme } from '@/lib/storage/examStorage';

interface ExamPauseModalProps {
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
  onResume: () => void;
  onExit: () => void;
  onReview?: () => void;
}

export function ExamPauseModal({
  isOpen,
  examCode,
  examTitle,
  mode,
  currentIndex,
  totalQuestions,
  formattedTime,
  stats,
  theme,
  onResume,
  onExit,
  onReview,
}: ExamPauseModalProps) {
  const isPearson = theme === 'pearson-vue';

  // Listener para atalhos de teclado enquanto pausado
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' || e.key === 'p' || e.key === 'P' || e.key === 'Enter') {
        e.preventDefault();
        onResume();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onResume]);

  if (!isOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/85 backdrop-blur-md animate-in fade-in duration-200"
    >
      <div
        className={`relative w-full max-w-xl rounded-3xl border shadow-2xl overflow-hidden p-6 sm:p-8 transition-all animate-in zoom-in-95 duration-200 ${
          isPearson
            ? 'bg-[#001f44] border-blue-800 text-white'
            : 'bg-slate-900/95 border-slate-800 text-slate-100'
        }`}
      >
        {/* Top Badge & Header */}
        <div className="flex items-center justify-between gap-3 mb-6">
          <div className="flex items-center gap-2.5">
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

          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/40 text-amber-300 text-xs font-bold">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-amber-500"></span>
            </span>
            <span>Simulator Paused</span>
          </div>
        </div>

        {/* Title and Icon */}
        <div className="text-center mb-6">
          <div className="mx-auto w-16 h-16 rounded-2xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4 shadow-lg shadow-amber-500/10">
            <PauseCircle className="h-9 w-9" />
          </div>
          <h2 className="text-2xl font-black text-white mb-2 tracking-tight">
            Exam Paused
          </h2>
          <p className="text-sm text-slate-300 max-w-md mx-auto leading-relaxed">
            The timer and question view are paused. Your answers and progress have been saved safely.
          </p>
        </div>

        {/* Status Metrics Cards */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 mb-6">
          {/* Time Remaining */}
          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <Clock className="h-3 w-3 text-amber-400" />
              <span>Time</span>
            </div>
            <p className="font-mono font-bold text-sm text-amber-300">
              {mode === 'real' ? formattedTime : 'No limit'}
            </p>
          </div>

          {/* Current Question */}
          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <Layers className="h-3 w-3 text-blue-400" />
              <span>Question</span>
            </div>
            <p className="font-bold text-sm text-white">
              {currentIndex + 1} / {totalQuestions}
            </p>
          </div>

          {/* Answered */}
          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <CheckCircle2 className="h-3 w-3 text-emerald-400" />
              <span>Answered</span>
            </div>
            <p className="font-bold text-sm text-emerald-400">
              {stats.answeredCount} ({stats.percentage}%)
            </p>
          </div>

          {/* Flagged */}
          <div className="p-3 rounded-2xl bg-slate-950/60 border border-slate-800/90 text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-[11px] font-semibold mb-1">
              <Flag className="h-3 w-3 text-amber-400" />
              <span>Flagged</span>
            </div>
            <p className="font-bold text-sm text-amber-400">
              {stats.flaggedCount}
            </p>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="mb-6">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1.5 font-medium">
            <span>Overall Progress</span>
            <span>{stats.answeredCount} of {totalQuestions} answered</span>
          </div>
          <div className="w-full h-2 rounded-full bg-slate-950 border border-slate-800 overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-amber-500 to-emerald-500 transition-all duration-300"
              style={{ width: `${stats.percentage}%` }}
            />
          </div>
        </div>

        {/* Tip Box */}
        <div className="mb-6 p-3.5 rounded-2xl bg-slate-950/40 border border-slate-800/70 text-xs text-slate-400 flex items-start gap-2.5">
          <Sparkles className="h-4 w-4 text-amber-400 shrink-0 mt-0.5" />
          <p className="leading-relaxed">
            You can resume now or save and exit to the catalog. Your session will continue from where you left off.
          </p>
        </div>

        {/* Action Buttons */}
        <div className="space-y-3">
          {/* Resume Button */}
          <button
            onClick={onResume}
            autoFocus
            className={`w-full flex items-center justify-center gap-2 py-3.5 px-5 rounded-2xl font-black text-sm transition-all shadow-lg hover:scale-[1.01] active:scale-[0.99] ${
              isPearson
                ? 'bg-amber-400 hover:bg-amber-300 text-slate-950 shadow-amber-500/20'
                : 'bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-slate-950 shadow-orange-500/25'
            }`}
          >
            <Play className="h-4 w-4 fill-current" />
            <span>Resume Exam (Press P or Enter)</span>
          </button>

          {/* Secondary Actions Row */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
            {onReview && (
              <button
                onClick={onReview}
                className="flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-200 text-xs font-bold transition-colors"
              >
                <HelpCircle className="h-4 w-4 text-blue-400" />
                <span>Review Answers</span>
              </button>
            )}

            <button
              onClick={onExit}
              className={`flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl border text-xs font-bold transition-colors ${
                !onReview ? 'col-span-2' : ''
              } border-slate-700/80 bg-slate-800/40 hover:bg-slate-800 text-slate-300 hover:text-white`}
            >
              <Home className="h-4 w-4 text-slate-400" />
              <span>Save & Return to Home</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
