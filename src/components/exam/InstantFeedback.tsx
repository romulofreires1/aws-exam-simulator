'use client';

import React from 'react';
import { CheckCircle2, XCircle, ExternalLink, HelpCircle, Lightbulb } from 'lucide-react';
import { Question } from '@/types/exam';

interface InstantFeedbackProps {
  question: Question;
  selectedOptionIds: string[];
  isCorrect: boolean;
}

export function InstantFeedback({
  question,
  selectedOptionIds,
  isCorrect,
}: InstantFeedbackProps) {
  if (selectedOptionIds.length === 0) {
    return (
      <div className="mt-6 p-4 rounded-xl border border-dashed border-slate-800 bg-slate-900/30 text-slate-400 text-sm flex items-center gap-2">
        <HelpCircle className="h-4 w-4 text-slate-500 shrink-0" />
        <span>Selecione uma resposta acima para ver o feedback e a explicação detalhada.</span>
      </div>
    );
  }

  return (
    <div
      className={`mt-6 rounded-xl border p-5 transition-all ${
        isCorrect
          ? 'bg-emerald-950/20 border-emerald-500/40 text-emerald-100'
          : 'bg-rose-950/20 border-rose-500/40 text-rose-100'
      }`}
    >
      {/* Feedback Banner */}
      <div className="flex items-center gap-2.5 mb-4">
        {isCorrect ? (
          <CheckCircle2 className="h-6 w-6 text-emerald-400 shrink-0" />
        ) : (
          <XCircle className="h-6 w-6 text-rose-400 shrink-0" />
        )}
        <div>
          <h3 className="font-bold text-base">
            {isCorrect ? 'Resposta Correta!' : 'Resposta Incorreta'}
          </h3>
          <p className="text-xs opacity-80">
            {isCorrect
              ? 'Excelente raciocínio arquitetural.'
              : `A resposta correta é: ${question.correctAnswers.join(', ')}.`}
          </p>
        </div>
      </div>

      {/* Explicação Geral */}
      <div className="mb-4 bg-slate-900/80 rounded-lg p-4 border border-slate-800 text-slate-200 text-sm leading-relaxed">
        <div className="flex items-center gap-2 font-semibold text-amber-400 mb-2">
          <Lightbulb className="h-4 w-4" />
          <span>Explicação Oficial AWS:</span>
        </div>
        <p>{question.generalExplanation}</p>
      </div>

      {/* Detalhamento por Opção */}
      <div className="space-y-2 mt-4">
        <p className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
          Análise de cada alternativa:
        </p>
        {question.options.map((opt) => {
          const isThisCorrect = question.correctAnswers.includes(opt.id);
          const wasSelected = selectedOptionIds.includes(opt.id);

          return (
            <div
              key={opt.id}
              className={`p-3 rounded-lg border text-xs leading-relaxed ${
                isThisCorrect
                  ? 'bg-emerald-950/40 border-emerald-500/40 text-slate-200'
                  : wasSelected
                  ? 'bg-rose-950/40 border-rose-500/40 text-slate-200'
                  : 'bg-slate-900/40 border-slate-800/80 text-slate-400'
              }`}
            >
              <div className="flex items-center gap-2 font-semibold mb-1">
                <span
                  className={`px-1.5 py-0.5 rounded font-mono ${
                    isThisCorrect
                      ? 'bg-emerald-500/20 text-emerald-300 font-bold'
                      : 'bg-slate-800 text-slate-400'
                  }`}
                >
                  Opção {opt.id}
                </span>
                {isThisCorrect && (
                  <span className="text-emerald-400 text-[11px] font-bold">✓ Correta</span>
                )}
                {!isThisCorrect && wasSelected && (
                  <span className="text-rose-400 text-[11px] font-bold">✗ Sua escolha</span>
                )}
              </div>
              <p className="text-slate-300">{opt.explanation || opt.text}</p>
            </div>
          );
        })}
      </div>

      {/* Link de Referência */}
      {question.referenceUrl && (
        <div className="mt-4 pt-3 border-t border-slate-800/60 flex items-center justify-end">
          <a
            href={question.referenceUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 text-xs text-amber-400 hover:text-amber-300 font-semibold underline"
          >
            <span>Documentação Oficial AWS</span>
            <ExternalLink className="h-3 w-3" />
          </a>
        </div>
      )}
    </div>
  );
}
