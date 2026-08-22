'use client';

import React, { useState, useEffect, useMemo } from 'react';
import Link from 'next/link';
import { Clock, ShieldCheck, HelpCircle, ArrowRight, Play, RotateCcw, Award, CheckCircle, Globe, Trash2 } from 'lucide-react';
import { ExamDefinition, ExamAttempt, ExamLanguage } from '@/types/exam';
import { getActiveSession, clearActiveSession, getAttemptsByExamId, getLanguagePreference, setLanguagePreference } from '@/lib/storage/examStorage';
import { getExamAvailableLanguages, SUPPORTED_LANGUAGES } from '@/lib/localization';

interface ExamCardProps {
  exam: ExamDefinition;
  onSelectCategory?: (category: string) => void;
}

export function ExamCard({ exam, onSelectCategory }: ExamCardProps) {
  const [activeSession, setActiveSession] = useState<ExamAttempt | null>(null);
  const [historyAttempts, setHistoryAttempts] = useState<ExamAttempt[]>([]);
  const availableLanguages = useMemo(() => getExamAvailableLanguages(exam), [exam]);
  const [selectedLanguage, setSelectedLanguage] = useState<ExamLanguage>('en');

  useEffect(() => {
    setActiveSession(getActiveSession(exam.id));
    setHistoryAttempts(getAttemptsByExamId(exam.id));
    const savedLang = getLanguagePreference();
    if (availableLanguages.includes(savedLang)) {
      setSelectedLanguage(savedLang);
    } else {
      setSelectedLanguage(availableLanguages[0] || 'en');
    }
  }, [exam.id, availableLanguages]);

  const handleSelectLanguage = (lang: ExamLanguage) => {
    setSelectedLanguage(lang);
    setLanguagePreference(lang);
  };

  const handleDiscardSession = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    clearActiveSession(exam.id);
    setActiveSession(null);
  };

  const bestAttempt = historyAttempts.reduce<ExamAttempt | null>((best, current) => {
    if (!current.score) return best;
    if (!best || (current.score.scaledScore > (best.score?.scaledScore || 0))) {
      return current;
    }
    return best;
  }, null);

  const categoryColor =
    exam.category === 'Professional'
      ? 'bg-purple-500/20 text-purple-300 border-purple-500/30 hover:bg-purple-500/30'
      : exam.category === 'Associate'
      ? 'bg-blue-500/20 text-blue-300 border-blue-500/30 hover:bg-blue-500/30'
      : exam.category === 'Specialty'
      ? 'bg-amber-500/20 text-amber-300 border-amber-500/30 hover:bg-amber-500/30'
      : 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30 hover:bg-emerald-500/30';

  return (
    <div className="group relative rounded-3xl border border-slate-800 bg-slate-900/90 p-6 sm:p-7 shadow-xl hover:border-slate-700 hover:shadow-2xl transition-all duration-200 flex flex-col h-full">
      {/* Top Details */}
      <div className="flex items-center justify-between gap-3 mb-4">
        <span className="font-mono text-xs font-black px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 shadow-sm">
          {exam.code}
        </span>
        {onSelectCategory ? (
          <button
            type="button"
            onClick={() => onSelectCategory(exam.category)}
            title={`Filtrar simulados de nível ${exam.category}`}
            className={`text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full border transition-all hover:scale-105 active:scale-95 cursor-pointer ${categoryColor}`}
          >
            {exam.category}
          </button>
        ) : (
          <span className={`text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full border ${categoryColor}`}>
            {exam.category}
          </span>
        )}
      </div>

      <h3
        title={exam.title}
        className="text-lg sm:text-xl font-black text-white group-hover:text-amber-400 transition-colors leading-snug line-clamp-2 h-14 mb-2 flex items-start"
      >
        {exam.title}
      </h3>

      <p
        title={exam.description}
        className="text-xs text-slate-400 leading-relaxed line-clamp-2 h-10 mb-5"
      >
        {exam.description}
      </p>

      {/* Language Selector */}
      <div className="flex items-center justify-between gap-2 py-2 px-3 bg-slate-950/40 rounded-xl border border-slate-800/80 mb-5 text-xs">
        <div className="flex items-center gap-1.5 text-slate-400 font-medium">
          <Globe className="h-3.5 w-3.5 text-amber-400" />
          <span>Language:</span>
        </div>
        <div className="flex items-center gap-1.5">
          {(['en', 'pt', 'es'] as ExamLanguage[]).map((lang) => {
            const meta = SUPPORTED_LANGUAGES[lang];
            const isAvailable = availableLanguages.includes(lang);
            const isSelected = isAvailable && selectedLanguage === lang;

            return (
              <button
                key={lang}
                type="button"
                disabled={!isAvailable}
                onClick={() => isAvailable && handleSelectLanguage(lang)}
                className={`px-2 py-0.5 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
                  !isAvailable
                    ? 'opacity-35 cursor-not-allowed bg-slate-950/60 text-slate-600 border border-slate-850 hover:bg-slate-950/60'
                    : isSelected
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/50 shadow-sm'
                    : 'bg-slate-800/80 text-slate-400 border border-slate-700 hover:text-slate-200 hover:bg-slate-700'
                }`}
                title={isAvailable ? `Take exam in ${meta?.label || lang}` : `${meta?.label || lang} (Not available for this exam)`}
              >
                <span>{meta?.flag}</span>
                <span className="uppercase">{lang}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Exam Specifications */}
      <div className="grid grid-cols-3 gap-2 py-3 px-3.5 bg-slate-950/60 rounded-xl border border-slate-800/80 text-center mb-6">
        <div>
          <p className="text-[10px] uppercase font-bold text-slate-500">Questions</p>
          <p className="text-sm font-bold text-slate-200">{exam.questions.length}</p>
        </div>
        <div className="border-x border-slate-800">
          <p className="text-[10px] uppercase font-bold text-slate-500">Time</p>
          <p className="text-sm font-bold text-slate-200">{exam.timeLimitMinutes} min</p>
        </div>
        <div>
          <p className="text-[10px] uppercase font-bold text-slate-500">Passing Score</p>
          <p className="text-sm font-bold text-slate-200">{exam.passingScore}/1000</p>
        </div>
      </div>

      {/* History / Active Session Status Area */}
      <div className="flex-1 flex flex-col justify-end space-y-2 mb-6 min-h-[3rem]">
        {activeSession && !activeSession.isCompleted && (
          <div className="p-2.5 sm:p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-between gap-2 text-xs">
            <div className="flex items-center gap-2 text-amber-300 font-semibold truncate min-w-0">
              <RotateCcw className="h-4 w-4 text-amber-400 shrink-0" />
              <span className="truncate">In-progress ({activeSession.mode === 'real' ? 'Real' : 'Practice'})</span>
            </div>
            <div className="flex items-center gap-2.5 shrink-0">
              <Link
                href={`/exams/${exam.id}/runner?mode=${activeSession.mode}&lang=${activeSession.language || selectedLanguage}`}
                className="text-amber-400 hover:text-amber-300 font-bold underline text-xs"
              >
                Resume
              </Link>
              <button
                type="button"
                onClick={handleDiscardSession}
                title="Discard in-progress session"
                className="p-1 rounded-lg text-slate-400 hover:text-rose-400 hover:bg-rose-500/15 transition-colors cursor-pointer"
              >
                <Trash2 className="h-3.5 w-3.5" />
              </button>
            </div>
          </div>
        )}

        {bestAttempt?.score && (
          <div className="px-3.5 py-2.5 rounded-xl bg-slate-950/40 border border-slate-800/80 flex items-center justify-between text-xs">
            <span className="text-slate-400 flex items-center gap-1.5">
              <Award className="h-4 w-4 text-amber-400 shrink-0" />
              Best Score:
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

        {!activeSession?.isCompleted && !activeSession && !bestAttempt?.score && (
          <div className="px-3.5 py-2.5 rounded-xl bg-slate-950/20 border border-dashed border-slate-800/60 flex items-center justify-between text-xs text-slate-500">
            <span className="flex items-center gap-1.5">
              <ShieldCheck className="h-4 w-4 text-slate-600 shrink-0" />
              Status:
            </span>
            <span className="font-medium text-slate-500">Not attempted yet</span>
          </div>
        )}
      </div>

      {/* Action Buttons */}
      <div className="grid grid-cols-2 gap-3 mt-auto pt-2 border-t border-slate-800/40">
        <Link
          href={`/exams/${exam.id}/runner?mode=practice&lang=${selectedLanguage}`}
          className="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white font-bold text-xs border border-slate-700 transition-colors"
        >
          <HelpCircle className="h-3.5 w-3.5 text-blue-400" />
          <span>Practice Mode</span>
        </Link>

        <Link
          href={`/exams/${exam.id}/runner?mode=real&lang=${selectedLanguage}`}
          className="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-slate-950 font-black text-xs shadow-md shadow-orange-500/20 transition-all hover:scale-[1.02]"
        >
          <Play className="h-3.5 w-3.5 fill-current" />
          <span>Real Exam</span>
        </Link>
      </div>
    </div>
  );
}
