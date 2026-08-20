'use client';

import React, { useState, useEffect, useRef } from 'react';
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle,
  CheckCircle2,
  Tag,
  Layers,
  HelpCircle,
  Highlighter,
  Trash2,
  Sparkles,
} from 'lucide-react';
import { Question, QuestionUserResponse, ExamMode } from '@/types/exam';
import { OptionCard } from './OptionCard';
import { InstantFeedback } from './InstantFeedback';
import { ExamTheme } from '@/lib/storage/examStorage';

interface QuestionViewProps {
  question: Question;
  questionIndex: number;
  totalQuestions: number;
  response: QuestionUserResponse;
  mode: ExamMode;
  theme: ExamTheme;
  onToggleOption: (optionId: string) => void;
  onToggleStrikeThrough: (optionId: string) => void;
  onToggleHighlight?: (text: string) => void;
  onClearHighlights?: () => void;
  onToggleCheckAnswer?: () => void;
  onPrev: () => void;
  onNext: () => void;
}

export function QuestionView({
  question,
  questionIndex,
  totalQuestions,
  response,
  mode,
  theme,
  onToggleOption,
  onToggleStrikeThrough,
  onToggleHighlight,
  onClearHighlights,
  onToggleCheckAnswer,
  onPrev,
  onNext,
}: QuestionViewProps) {
  const isPearson = theme === 'pearson-vue';
  const isLastQuestion = questionIndex === totalQuestions - 1;

  const isMultiple = question.type === 'multiple';
  const requiredCount = question.requiredChoices || 1;

  const [selectedText, setSelectedText] = useState<string>('');
  const statementRef = useRef<HTMLDivElement>(null);

  const handleMouseUp = () => {
    const selection = window.getSelection();
    if (selection) {
      const text = selection.toString().trim();
      if (text.length > 1 && text.length < 200) {
        setSelectedText(text);
        return;
      }
    }
    setSelectedText('');
  };

  const handleApplyHighlight = () => {
    if (selectedText && onToggleHighlight) {
      onToggleHighlight(selectedText);
      setSelectedText('');
      window.getSelection()?.removeAllRanges();
    }
  };

  // Renderizador de texto com realce amarelo persistido
  const renderHighlightedText = (text: string, highlights: string[] = []) => {
    if (!highlights || highlights.length === 0) {
      return text;
    }

    // Escapa caracteres regex e ordena por tamanho decrescente
    const validHighlights = highlights
      .filter((h) => h && h.trim().length > 0)
      .sort((a, b) => b.length - a.length);

    if (validHighlights.length === 0) return text;

    const regexPattern = `(${validHighlights
      .map((h) => h.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
      .join('|')})`;

    const regex = new RegExp(regexPattern, 'gi');
    const parts = text.split(regex);

    return parts.map((part, idx) => {
      const isMatch = validHighlights.some(
        (h) => h.toLowerCase() === part.toLowerCase()
      );

      if (isMatch) {
        return (
          <mark
            key={idx}
            className="bg-amber-300 text-slate-950 font-bold px-1 py-0.5 rounded shadow-sm"
          >
            {part}
          </mark>
        );
      }
      return part;
    });
  };

  const highlightsCount = response.highlights?.length || 0;

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-6 pb-28">
      {/* Top Metadata Box */}
      <div className="flex flex-wrap items-center justify-between gap-2 mb-4">
        {/* Domain Badge */}
        <div className="flex items-center gap-2 flex-wrap">
          <span
            className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-semibold ${
              isPearson
                ? 'bg-blue-900/60 text-blue-200 border border-blue-800'
                : 'bg-slate-800 text-slate-300 border border-slate-700'
            }`}
          >
            <Layers className="h-3.5 w-3.5 text-amber-400" />
            <span>{question.domainName}</span>
          </span>

          {question.difficulty && (
            <span
              className={`text-[11px] font-bold uppercase px-2 py-0.5 rounded ${
                question.difficulty === 'hard'
                  ? 'bg-rose-500/20 text-rose-300'
                  : question.difficulty === 'medium'
                  ? 'bg-amber-500/20 text-amber-300'
                  : 'bg-emerald-500/20 text-emerald-300'
              }`}
            >
              {question.difficulty}
            </span>
          )}
        </div>

        {/* Highlighting Tools */}
        <div className="flex items-center gap-2">
          {highlightsCount > 0 && onClearHighlights && (
            <button
              onClick={onClearHighlights}
              title="Clear all highlights for this question"
              className="inline-flex items-center gap-1 text-xs text-slate-400 hover:text-rose-400 px-2.5 py-1 rounded-lg border border-slate-800 hover:border-rose-500/40 bg-slate-900/60 transition-colors"
            >
              <Trash2 className="h-3 w-3" />
              <span>Clear Highlights ({highlightsCount})</span>
            </button>
          )}

          {/* Services Tags */}
          {question.services && question.services.length > 0 && (
            <div className="hidden sm:flex items-center gap-1.5 flex-wrap">
              {question.services.map((svc) => (
                <span
                  key={svc}
                  className="inline-flex items-center gap-1 text-[11px] font-mono text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800"
                >
                  <Tag className="h-2.5 w-2.5" />
                  {svc}
                </span>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Question Box */}
      <div
        className={`p-6 sm:p-8 rounded-2xl border shadow-xl transition-colors relative ${
          isPearson
            ? 'bg-[#001c3d] border-blue-900 text-slate-100'
            : 'bg-slate-900/90 border-slate-800 text-slate-100 backdrop-blur'
        }`}
      >
        {/* Instruction pill & Highlight hint */}
        <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
          <div
            className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-bold ${
              isMultiple
                ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                : 'bg-slate-800 text-slate-300 border border-slate-700'
            }`}
          >
            <HelpCircle className="h-3.5 w-3.5" />
            <span>
              {isMultiple
                ? `Choose ${requiredCount} correct options (Choose ${
                    requiredCount === 2 ? 'TWO' : requiredCount === 3 ? 'THREE' : requiredCount
                  })`
                : 'Choose ONE single option'}
            </span>
          </div>

          <div className="flex items-center gap-2 text-xs text-slate-400">
            <span className="hidden md:inline">
              Select text to highlight • Right-click to strike through
            </span>
          </div>
        </div>

        {/* Floating Highlight Action Button when text is selected */}
        {selectedText && (
          <div className="mb-4 p-3 rounded-xl bg-amber-500/15 border border-amber-400/50 flex items-center justify-between animate-in fade-in slide-in-from-top-2 duration-150">
            <div className="flex items-center gap-2 text-xs text-amber-200 truncate mr-3">
              <Highlighter className="h-4 w-4 text-amber-400 shrink-0" />
              <span className="truncate">&quot;{selectedText}&quot;</span>
            </div>
            <button
              onClick={handleApplyHighlight}
              className="shrink-0 flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs shadow-md transition-all"
            >
              <Sparkles className="h-3.5 w-3.5" />
              <span>Highlight Text</span>
            </button>
          </div>
        )}

        {/* Statement with highlight rendering */}
        <div
          ref={statementRef}
          onMouseUp={handleMouseUp}
          onTouchEnd={handleMouseUp}
          className="text-base sm:text-lg leading-relaxed font-normal text-slate-100 mb-8 whitespace-pre-line select-text"
        >
          {renderHighlightedText(question.statement, response.highlights || [])}
        </div>

        {/* Options List */}
        <div className="space-y-3">
          {question.options.map((option) => (
            <OptionCard
              key={option.id}
              option={option}
              type={question.type}
              isSelected={response.selectedOptionIds.includes(option.id)}
              isStruckOut={response.struckOutOptionIds?.includes(option.id) || false}
              theme={theme}
              onToggleSelect={onToggleOption}
              onToggleStrikeThrough={onToggleStrikeThrough}
            />
          ))}
        </div>

        {/* Practice Mode Action: Check Answer Button */}
        {mode === 'practice' && (
          <div className="mt-6 pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div className="text-xs text-slate-400">
              {isMultiple ? (
                <span>
                  {response.selectedOptionIds.length} of {requiredCount} options selected
                  {response.selectedOptionIds.length < requiredCount && (
                    <span className="text-amber-400 ml-1.5 font-semibold">
                      (Select {requiredCount - response.selectedOptionIds.length} more)
                    </span>
                  )}
                </span>
              ) : (
                <span>
                  {response.selectedOptionIds.length > 0
                    ? '1 option selected'
                    : 'Select an option above'}
                </span>
              )}
            </div>

            <button
              type="button"
              onClick={onToggleCheckAnswer}
              disabled={response.selectedOptionIds.length === 0}
              className={`flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all shadow-md ${
                response.selectedOptionIds.length === 0
                  ? 'opacity-40 cursor-not-allowed bg-slate-800 text-slate-500 border border-slate-750'
                  : response.isAnswerChecked
                  ? 'bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600'
                  : 'bg-emerald-600 hover:bg-emerald-500 text-white shadow-emerald-950/40 hover:scale-[1.02]'
              }`}
            >
              <CheckCircle2 className="h-4 w-4" />
              <span>
                {response.isAnswerChecked
                  ? 'Hide Answer & Explanation'
                  : 'Check Answer & Explanation'}
              </span>
            </button>
          </div>
        )}

        {/* Practice Mode Feedback */}
        {mode === 'practice' && response.isAnswerChecked && (
          <InstantFeedback
            question={question}
            selectedOptionIds={response.selectedOptionIds}
            isCorrect={response.isCorrect || false}
          />
        )}
      </div>

      {/* Bottom Sticky Action Bar */}
      <div className="fixed bottom-0 left-0 right-0 z-30 border-t border-slate-800 bg-slate-950/90 backdrop-blur-md px-4 py-3">
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-4">
          {/* Previous Button */}
          <button
            type="button"
            onClick={onPrev}
            disabled={questionIndex === 0}
            className={`flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-xl font-semibold text-sm transition-all border ${
              questionIndex === 0
                ? 'opacity-40 cursor-not-allowed bg-slate-900 border-slate-800 text-slate-500'
                : 'bg-slate-900 hover:bg-slate-800 border-slate-700 text-slate-200 hover:text-white shadow-sm'
            }`}
          >
            <ArrowLeft className="h-4 w-4" />
            <span className="hidden sm:inline">Previous Question</span>
            <span className="sm:hidden">Previous</span>
            <kbd className="hidden md:inline-block text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-400">
              ←
            </kbd>
          </button>

          {/* Quick Counter */}
          <div className="text-xs font-semibold text-slate-400">
            {questionIndex + 1} / {totalQuestions}
          </div>

          {/* Next Button */}
          <button
            type="button"
            onClick={onNext}
            className={`flex items-center gap-2 px-5 sm:px-6 py-2.5 rounded-xl font-bold text-sm transition-all shadow-md ${
              isLastQuestion
                ? 'bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-slate-950 shadow-orange-500/20'
                : isPearson
                ? 'bg-blue-600 hover:bg-blue-500 text-white'
                : 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-amber-500/20'
            }`}
          >
            <span>{isLastQuestion ? 'Review Exam' : 'Next Question'}</span>
            <ArrowRight className="h-4 w-4" />
            <kbd className="hidden md:inline-block text-[10px] font-mono px-1.5 py-0.5 rounded bg-black/20 text-current">
              →
            </kbd>
          </button>
        </div>
      </div>
    </div>
  );
}
