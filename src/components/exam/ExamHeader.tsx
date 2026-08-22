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
  Globe,
} from 'lucide-react';
import { ExamMode, ExamLanguage } from '@/types/exam';
import { ExamTheme } from '@/lib/storage/examStorage';
import { SUPPORTED_LANGUAGES } from '@/lib/localization';

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
  language?: ExamLanguage;
  availableLanguages?: ExamLanguage[];
  isPaused?: boolean;
  onSelectLanguage?: (lang: ExamLanguage) => void;
  onTogglePause?: () => void;
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
  language = 'en',
  availableLanguages = ['en'],
  isPaused,
  onSelectLanguage,
  onTogglePause,
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
            {mode === 'real' ? 'Real Exam' : mode === 'practice' ? 'Practice Mode' : 'Review'}
          </span>
        </div>

        {/* Right: Timer, Pause & Tools */}
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          {/* Timer Display (Real Mode Only) */}
          {mode === 'real' ? (
            <button
              onClick={onTogglePause}
              title="Pause Exam (P)"
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-sm font-bold transition-all cursor-pointer ${
                isTimerCritical
                  ? 'bg-red-500/20 text-red-400 border border-red-500/50 animate-pulse'
                  : isTimerWarning
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                  : isPearson
                  ? 'bg-blue-900/80 text-white border border-blue-800 hover:bg-blue-800'
                  : 'bg-slate-800 text-slate-200 border border-slate-700 hover:border-slate-600'
              }`}
            >
              <Clock className="h-4 w-4 shrink-0" />
              <span>{formattedTime}</span>
            </button>
          ) : (
            <div
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold ${
                isPearson
                  ? 'bg-blue-900/40 text-blue-200 border border-blue-800'
                  : 'bg-slate-800/80 text-slate-400 border border-slate-700/60'
              }`}
            >
              <span>No time limit</span>
            </div>
          )}

          {/* Pause Button */}
          {onTogglePause && (
            <button
              onClick={onTogglePause}
              title="Pause Simulator (P)"
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all border ${
                isPearson
                  ? 'bg-blue-900/80 border-blue-700 text-blue-100 hover:bg-blue-800 hover:text-white'
                  : 'bg-slate-800 border-slate-700 text-slate-200 hover:bg-slate-700 hover:text-amber-300'
              }`}
            >
              <Pause className="h-3.5 w-3.5" />
              <span className="hidden xs:inline sm:inline">Pause</span>
            </button>
          )}

          {/* Language Switcher */}
          {onSelectLanguage && (
            <div className={`flex items-center gap-1 p-0.5 rounded-lg border ${
              isPearson ? 'bg-blue-950/80 border-blue-800' : 'bg-slate-800/90 border-slate-700'
            }`}>
              {(['en', 'pt', 'es'] as ExamLanguage[]).map((lang) => {
                const meta = SUPPORTED_LANGUAGES[lang];
                const isAvailable = availableLanguages?.includes(lang);
                const isSelected = isAvailable && language === lang;

                return (
                  <button
                    key={lang}
                    disabled={!isAvailable}
                    onClick={() => isAvailable && onSelectLanguage(lang)}
                    title={isAvailable ? `Switch questions to ${meta?.label || lang}` : `${meta?.label || lang} (Not available for this exam)`}
                    className={`px-2 py-1 rounded text-xs font-bold flex items-center gap-1 transition-all ${
                      !isAvailable
                        ? 'opacity-35 cursor-not-allowed text-slate-500 hover:bg-transparent'
                        : isSelected
                        ? isPearson
                          ? 'bg-amber-400 text-slate-950 shadow-sm'
                          : 'bg-amber-500 text-slate-950 shadow-sm'
                        : 'text-slate-300 hover:text-white hover:bg-slate-700/60'
                    }`}
                  >
                    <span>{meta?.flag}</span>
                    <span className="uppercase text-[11px]">{lang}</span>
                  </button>
                );
              })}
            </div>
          )}

          {/* Theme Switch */}
          <button
            onClick={onToggleTheme}
            title={isPearson ? 'Switch to Modern Theme' : 'Switch to Pearson VUE Theme'}
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
            Question {currentIndex + 1} of {totalQuestions}
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
            <span>{isFlagged ? 'Flagged (F)' : 'Flag for Review (F)'}</span>
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
            <span>Notes</span>
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
            <span>Question Map</span>
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
            <span>Review & Finish</span>
          </button>
        </div>
      </div>
    </header>
  );
}
