'use client';

import React from 'react';
import { Check, Strikethrough, RotateCcw } from 'lucide-react';
import { QuestionOption, QuestionType } from '@/types/exam';
import { ExamTheme } from '@/lib/storage/examStorage';

interface OptionCardProps {
  option: QuestionOption;
  type: QuestionType;
  isSelected: boolean;
  isStruckOut: boolean;
  theme: ExamTheme;
  onToggleSelect: (optionId: string) => void;
  onToggleStrikeThrough: (optionId: string) => void;
}

export function OptionCard({
  option,
  type,
  isSelected,
  isStruckOut,
  theme,
  onToggleSelect,
  onToggleStrikeThrough,
}: OptionCardProps) {
  const isPearson = theme === 'pearson-vue';

  const handleContextMenu = (e: React.MouseEvent) => {
    e.preventDefault();
    onToggleStrikeThrough(option.id);
  };

  const handleClickCard = () => {
    onToggleSelect(option.id);
  };

  const handleStrikeClick = (e: React.MouseEvent) => {
    e.stopPropagation();
    onToggleStrikeThrough(option.id);
  };

  return (
    <div
      onClick={handleClickCard}
      onContextMenu={handleContextMenu}
      className={`group relative flex items-start gap-4 p-4 sm:p-5 rounded-2xl border transition-all duration-150 cursor-pointer select-none ${
        isStruckOut
          ? 'opacity-40 bg-slate-950/40 border-slate-800 text-slate-500'
          : isSelected
          ? isPearson
            ? 'bg-blue-900/40 border-blue-400 text-white ring-2 ring-blue-500 shadow-md'
            : 'bg-amber-500/15 border-amber-400 text-slate-100 ring-2 ring-amber-500/50 shadow-lg shadow-amber-500/10'
          : isPearson
          ? 'bg-[#00244e]/40 hover:bg-[#00244e]/80 border-slate-700 hover:border-blue-500 text-slate-200'
          : 'bg-slate-900/80 hover:bg-slate-850 border-slate-800 hover:border-slate-600 text-slate-200'
      }`}
    >
      {/* Caixa da Letra / Indicador */}
      <div
        className={`flex items-center justify-center h-8 w-8 shrink-0 rounded-xl font-mono text-sm font-black transition-all ${
          isSelected
            ? isPearson
              ? 'bg-blue-500 text-white shadow'
              : 'bg-amber-500 text-slate-950 shadow-md shadow-amber-500/30'
            : 'bg-slate-800 border border-slate-700 text-slate-300 group-hover:border-slate-500 group-hover:text-white'
        }`}
      >
        {isSelected ? (
          type === 'single' ? (
            option.id
          ) : (
            <Check className="h-4 w-4 stroke-[3]" />
          )
        ) : (
          option.id
        )}
      </div>

      {/* Option Text */}
      <div className="flex-1 pt-0.5 min-w-0">
        <p
          className={`text-sm sm:text-base leading-relaxed ${
            isStruckOut
              ? 'line-through text-slate-500'
              : isSelected
              ? 'text-white font-medium'
              : 'text-slate-200'
          }`}
        >
          {option.text}
        </p>

        {isStruckOut && (
          <span className="inline-block mt-1 text-[11px] font-bold text-amber-400/80 uppercase tracking-wider">
            (Option eliminated / struck out)
          </span>
        )}
      </div>

      {/* Strike-Through Button */}
      <button
        type="button"
        title={isStruckOut ? 'Restore eliminated option' : 'Strike through option (Eliminate)'}
        onClick={handleStrikeClick}
        className={`flex items-center gap-1 px-2 py-1.5 rounded-lg text-xs font-semibold transition-all shrink-0 ${
          isStruckOut
            ? 'bg-slate-800 text-amber-300 hover:bg-slate-700 border border-slate-700'
            : 'text-slate-500 hover:text-slate-200 hover:bg-slate-800 border border-transparent hover:border-slate-700'
        }`}
      >
        {isStruckOut ? (
          <>
            <RotateCcw className="h-3.5 w-3.5" />
            <span className="hidden sm:inline">Restore</span>
          </>
        ) : (
          <>
            <Strikethrough className="h-3.5 w-3.5" />
            <span className="hidden sm:inline">Strike</span>
          </>
        )}
      </button>
    </div>
  );
}
