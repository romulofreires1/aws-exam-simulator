'use client';

import React from 'react';
import { X, Flag, Check, HelpCircle } from 'lucide-react';
import { Question, QuestionUserResponse } from '@/types/exam';

interface QuestionGridModalProps {
  isOpen: boolean;
  onClose: () => void;
  questions: Question[];
  responses: Record<string, QuestionUserResponse>;
  currentIndex: number;
  onSelectQuestion: (index: number) => void;
}

export function QuestionGridModal({
  isOpen,
  onClose,
  questions,
  responses,
  currentIndex,
  onSelectQuestion,
}: QuestionGridModalProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-150">
      <div className="relative w-full max-w-2xl rounded-2xl border border-slate-800 bg-slate-900 shadow-2xl overflow-hidden flex flex-col max-h-[85vh]">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
          <div>
            <h2 className="text-lg font-bold text-white">Mapa de Questões</h2>
            <p className="text-xs text-slate-400">
              Clique em qualquer número para navegar diretamente até a questão.
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Legend */}
        <div className="px-6 py-3 bg-slate-950/50 border-b border-slate-800 flex flex-wrap gap-4 text-xs font-medium">
          <div className="flex items-center gap-1.5 text-slate-300">
            <span className="h-3.5 w-3.5 rounded bg-emerald-600 inline-block" />
            <span>Respondida</span>
          </div>
          <div className="flex items-center gap-1.5 text-slate-300">
            <span className="h-3.5 w-3.5 rounded bg-amber-500 inline-block" />
            <span>Marcada (Flag)</span>
          </div>
          <div className="flex items-center gap-1.5 text-slate-300">
            <span className="h-3.5 w-3.5 rounded border border-slate-600 bg-slate-800 inline-block" />
            <span>Não Respondida</span>
          </div>
          <div className="flex items-center gap-1.5 text-slate-300">
            <span className="h-3.5 w-3.5 rounded border-2 border-amber-400 bg-slate-800 inline-block" />
            <span>Questão Atual</span>
          </div>
        </div>

        {/* Questions Grid */}
        <div className="p-6 overflow-y-auto grid grid-cols-5 sm:grid-cols-8 md:grid-cols-10 gap-2.5">
          {questions.map((q, idx) => {
            const resp = responses[q.id];
            const isAnswered = !!(resp?.selectedOptionIds && resp.selectedOptionIds.length > 0);
            const isFlagged = !!resp?.isFlagged;
            const isCurrent = idx === currentIndex;

            return (
              <button
                key={q.id}
                onClick={() => {
                  onSelectQuestion(idx);
                }}
                className={`relative h-11 rounded-xl font-bold text-sm flex items-center justify-center transition-all ${
                  isCurrent
                    ? 'ring-2 ring-amber-400 scale-105 z-10'
                    : 'hover:scale-105'
                } ${
                  isFlagged
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/60'
                    : isAnswered
                    ? 'bg-emerald-600 text-white shadow-sm'
                    : 'bg-slate-800/80 text-slate-400 border border-slate-700 hover:text-white'
                }`}
              >
                <span>{idx + 1}</span>
                {isFlagged && (
                  <Flag className="absolute -top-1.5 -right-1.5 h-3.5 w-3.5 fill-amber-400 text-amber-400 drop-shadow" />
                )}
              </button>
            );
          })}
        </div>

        {/* Footer */}
        <div className="px-6 py-3 border-t border-slate-800 bg-slate-950/40 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-white transition-colors"
          >
            Fechar
          </button>
        </div>
      </div>
    </div>
  );
}
