'use client';

import React, { useState, useMemo } from 'react';
import {
  CheckCircle2,
  XCircle,
  Flag,
  Filter,
  ExternalLink,
  Lightbulb,
  Tag,
  Layers,
  Globe,
} from 'lucide-react';
import { Question, QuestionUserResponse, ExamLanguage } from '@/types/exam';
import { isAnswerCorrect } from '@/lib/scoreCalculator';
import { getLocalizedQuestion, SUPPORTED_LANGUAGES } from '@/lib/localization';

interface QuestionReviewListProps {
  questions: Question[];
  responses: Record<string, QuestionUserResponse>;
  language?: ExamLanguage;
  availableLanguages?: ExamLanguage[];
}

type FilterType = 'all' | 'incorrect' | 'correct' | 'flagged';

export function QuestionReviewList({
  questions,
  responses,
  language: initialLanguage = 'en',
  availableLanguages = ['en'],
}: QuestionReviewListProps) {
  const [filter, setFilter] = useState<FilterType>('all');
  const [currentLang, setCurrentLang] = useState<ExamLanguage>(initialLanguage);

  const questionStats = useMemo(() => {
    let correctCount = 0;
    let incorrectCount = 0;
    let flaggedCount = 0;

    questions.forEach((q) => {
      const resp = responses[q.id];
      const correct = isAnswerCorrect(resp?.selectedOptionIds || [], q.correctAnswers);
      if (correct) correctCount++;
      else incorrectCount++;

      if (resp?.isFlagged) flaggedCount++;
    });

    return {
      total: questions.length,
      correctCount,
      incorrectCount,
      flaggedCount,
    };
  }, [questions, responses]);

  const filteredQuestions = useMemo(() => {
    return questions.filter((q, idx) => {
      const resp = responses[q.id];
      const correct = isAnswerCorrect(resp?.selectedOptionIds || [], q.correctAnswers);

      if (filter === 'correct') return correct;
      if (filter === 'incorrect') return !correct;
      if (filter === 'flagged') return !!resp?.isFlagged;
      return true;
    });
  }, [questions, responses, filter]);

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
      {/* Header & Filter Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8 pb-6 border-b border-slate-800">
        <div>
          <h2 className="text-xl font-bold text-white">Detailed Question Review</h2>
          <p className="text-xs text-slate-400">
            Analyze each question, technical rationales, and official AWS documentation references
          </p>
        </div>

        {/* Filter & Language Controls */}
        <div className="flex flex-wrap items-center gap-3">
          {/* Language Selector */}
          <div className="flex items-center gap-1 bg-slate-950/80 border border-slate-800 rounded-xl p-1">
            <span className="text-[11px] text-slate-500 font-bold px-1.5 flex items-center gap-1">
              <Globe className="h-3 w-3 text-amber-400" />
              <span className="hidden sm:inline">Language:</span>
            </span>
            {(['en', 'pt', 'es'] as ExamLanguage[]).map((lang) => {
              const meta = SUPPORTED_LANGUAGES[lang];
              const isAvailable = availableLanguages?.includes(lang);
              const isSelected = isAvailable && currentLang === lang;

              return (
                <button
                  key={lang}
                  disabled={!isAvailable}
                  onClick={() => isAvailable && setCurrentLang(lang)}
                  title={isAvailable ? `View explanations in ${meta?.label || lang}` : `${meta?.label || lang} (Not available for this exam)`}
                  className={`px-2 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
                    !isAvailable
                      ? 'opacity-35 cursor-not-allowed text-slate-600 hover:bg-transparent'
                      : isSelected
                      ? 'bg-amber-500 text-slate-950 font-bold shadow-sm'
                      : 'text-slate-400 hover:text-white hover:bg-slate-800'
                  }`}
                >
                  <span>{meta?.flag}</span>
                  <span className="uppercase text-[11px]">{lang}</span>
                </button>
              );
            })}
          </div>

          {/* Filter Pills */}
          <div className="flex flex-wrap items-center gap-2">
            <button
              onClick={() => setFilter('all')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                filter === 'all'
                  ? 'bg-amber-500 text-slate-950 shadow-sm shadow-amber-500/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              All ({questionStats.total})
            </button>

            <button
              onClick={() => setFilter('incorrect')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                filter === 'incorrect'
                  ? 'bg-rose-500 text-white shadow-sm shadow-rose-500/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              Incorrect ({questionStats.incorrectCount})
            </button>

            <button
              onClick={() => setFilter('correct')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                filter === 'correct'
                  ? 'bg-emerald-600 text-white shadow-sm shadow-emerald-600/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              Correct ({questionStats.correctCount})
            </button>

            <button
              onClick={() => setFilter('flagged')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                filter === 'flagged'
                  ? 'bg-amber-600 text-white shadow-sm shadow-amber-600/20'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              Flagged ({questionStats.flaggedCount})
            </button>
          </div>
        </div>
      </div>

      {/* Questions List */}
      <div className="space-y-8">
        {filteredQuestions.length === 0 ? (
          <div className="text-center py-12 text-slate-500">
            No questions found with the selected filter.
          </div>
        ) : (
          filteredQuestions.map((rawQ) => {
            const q = getLocalizedQuestion(rawQ, currentLang);
            const originalIndex = questions.findIndex((orig) => orig.id === rawQ.id);
            const resp = responses[rawQ.id];
            const selectedOptions = resp?.selectedOptionIds || [];
            const isCorrect = isAnswerCorrect(selectedOptions, rawQ.correctAnswers);
            const isFlagged = !!resp?.isFlagged;

            return (
              <div
                key={q.id}
                className={`rounded-2xl border p-6 transition-all ${
                  isCorrect
                    ? 'bg-slate-950/40 border-slate-800 hover:border-emerald-500/30'
                    : 'bg-rose-950/10 border-rose-500/30 hover:border-rose-500/50'
                }`}
              >
                {/* Question Header */}
                <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
                  <div className="flex items-center gap-2.5">
                    <span className="font-mono font-black text-sm text-white bg-slate-800 px-2.5 py-1 rounded-lg border border-slate-700">
                      Question {originalIndex + 1}
                    </span>

                    <span
                      className={`inline-flex items-center gap-1 text-xs font-bold px-2.5 py-1 rounded-full ${
                        isCorrect
                          ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                          : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                      }`}
                    >
                      {isCorrect ? (
                        <>
                          <CheckCircle2 className="h-3.5 w-3.5" />
                          <span>Correct</span>
                        </>
                      ) : (
                        <>
                          <XCircle className="h-3.5 w-3.5" />
                          <span>Incorrect</span>
                        </>
                      )}
                    </span>

                    {isFlagged && (
                      <span className="inline-flex items-center gap-1 text-xs font-semibold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-md border border-amber-500/20">
                        <Flag className="h-3 w-3 fill-amber-400" />
                        <span>Flagged</span>
                      </span>
                    )}
                  </div>

                  {/* Domain & Service */}
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="text-xs text-slate-400 bg-slate-900 px-2.5 py-1 rounded-md border border-slate-800 flex items-center gap-1">
                      <Layers className="h-3 w-3 text-amber-400" />
                      {q.domainName}
                    </span>
                    {q.services &&
                      q.services.map((s) => (
                        <span
                          key={s}
                          className="text-[11px] font-mono text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800"
                        >
                          {s}
                        </span>
                      ))}
                  </div>
                </div>

                {/* Statement */}
                <div className="text-base text-slate-200 leading-relaxed mb-6 font-normal">
                  {q.statement}
                </div>

                {/* Options Breakdown */}
                <div className="space-y-2.5 mb-6">
                  {q.options.map((opt) => {
                    const isThisCorrect = q.correctAnswers.includes(opt.id);
                    const wasSelected = selectedOptions.includes(opt.id);

                    return (
                      <div
                        key={opt.id}
                        className={`p-3.5 rounded-xl border text-sm leading-relaxed transition-colors ${
                          isThisCorrect
                            ? 'bg-emerald-950/30 border-emerald-500/50 text-slate-100'
                            : wasSelected
                            ? 'bg-rose-950/30 border-rose-500/50 text-slate-100'
                            : 'bg-slate-950/30 border-slate-800 text-slate-400'
                        }`}
                      >
                        <div className="flex items-start justify-between gap-3 font-medium mb-1">
                          <div className="flex items-start gap-2.5 flex-1 min-w-0">
                            <span
                              className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-lg text-xs font-mono font-black mt-0.5 ${
                                isThisCorrect
                                  ? 'bg-emerald-500 text-slate-950'
                                  : wasSelected
                                  ? 'bg-rose-500 text-white'
                                  : 'bg-slate-800 text-slate-400'
                              }`}
                            >
                              {opt.id}
                            </span>
                            <span className="text-slate-200 text-sm leading-relaxed">{opt.text}</span>
                          </div>
                          {isThisCorrect && (
                            <span className="shrink-0 text-xs text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded-md border border-emerald-500/20">
                              ✓ Correct
                            </span>
                          )}
                          {!isThisCorrect && wasSelected && (
                            <span className="shrink-0 text-xs text-rose-400 font-bold bg-rose-500/10 px-2 py-0.5 rounded-md border border-rose-500/20">
                              ✗ Your answer
                            </span>
                          )}
                        </div>

                        {opt.explanation && (
                          <p className="mt-2 text-xs text-slate-300 pl-8.5 border-t border-slate-800/60 pt-2">
                            {opt.explanation}
                          </p>
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* General Explanation & Reference Link */}
                <div className="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
                  <div className="flex items-center gap-2 font-semibold text-xs text-amber-400 mb-1.5">
                    <Lightbulb className="h-4 w-4" />
                    <span>Explanation & AWS Best Practices:</span>
                  </div>
                  <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                    {q.generalExplanation}
                  </p>

                  {q.referenceUrl && (
                    <div className="mt-3 pt-2 border-t border-slate-800/80 flex justify-end">
                      <a
                        href={q.referenceUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1 text-xs text-amber-400 hover:text-amber-300 font-semibold underline"
                      >
                        <span>Official AWS Documentation</span>
                        <ExternalLink className="h-3 w-3" />
                      </a>
                    </div>
                  )}
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
