'use client';

import React from 'react';
import { Flag, CheckCircle, AlertTriangle, ArrowLeft, Send } from 'lucide-react';
import { Question, QuestionUserResponse } from '@/types/exam';

interface ExamReviewScreenProps {
  questions: Question[];
  responses: Record<string, QuestionUserResponse>;
  onGoToQuestion: (index: number) => void;
  onBackToExam: () => void;
  onSubmitExam: () => void;
}

export function ExamReviewScreen({
  questions,
  responses,
  onGoToQuestion,
  onBackToExam,
  onSubmitExam,
}: ExamReviewScreenProps) {
  const total = questions.length;
  let answered = 0;
  let flagged = 0;

  questions.forEach((q) => {
    const resp = responses[q.id];
    if (resp?.selectedOptionIds && resp.selectedOptionIds.length > 0) {
      answered++;
    }
    if (resp?.isFlagged) {
      flagged++;
    }
  });

  const unanswered = total - answered;

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 mb-8">
        <h1 className="text-2xl font-black text-white mb-2">
          Tela de Revisão do Simulado
        </h1>
        <p className="text-slate-400 text-sm leading-relaxed">
          Revise suas respostas antes de realizar o envio final. Você pode clicar em qualquer linha da tabela para retornar à questão correspondente.
        </p>

        {/* Resumo de Status */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-6">
          <div className="bg-slate-950/60 border border-slate-800 p-4 rounded-xl flex items-center gap-3">
            <div className="p-2 rounded-lg bg-emerald-500/20 text-emerald-400">
              <CheckCircle className="h-5 w-5" />
            </div>
            <div>
              <p className="text-xs text-slate-400">Respondidas</p>
              <p className="text-xl font-bold text-white">
                {answered} / {total}
              </p>
            </div>
          </div>

          <div className="bg-slate-950/60 border border-slate-800 p-4 rounded-xl flex items-center gap-3">
            <div className="p-2 rounded-lg bg-amber-500/20 text-amber-400">
              <Flag className="h-5 w-5" />
            </div>
            <div>
              <p className="text-xs text-slate-400">Marcadas para Revisão</p>
              <p className="text-xl font-bold text-white">{flagged}</p>
            </div>
          </div>

          <div className="bg-slate-950/60 border border-slate-800 p-4 rounded-xl flex items-center gap-3">
            <div className="p-2 rounded-lg bg-rose-500/20 text-rose-400">
              <AlertTriangle className="h-5 w-5" />
            </div>
            <div>
              <p className="text-xs text-slate-400">Não Respondidas</p>
              <p className="text-xl font-bold text-white">{unanswered}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Tabela de Revisão */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl mb-8">
        <div className="max-h-[500px] overflow-y-auto">
          <table className="w-full text-left text-sm text-slate-300">
            <thead className="bg-slate-950/80 text-xs uppercase font-bold text-slate-400 sticky top-0 border-b border-slate-800">
              <tr>
                <th className="px-6 py-3.5">#</th>
                <th className="px-6 py-3.5">Status</th>
                <th className="px-6 py-3.5">Marcada</th>
                <th className="px-6 py-3.5">Domínio</th>
                <th className="px-6 py-3.5 text-right">Ação</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {questions.map((q, idx) => {
                const resp = responses[q.id];
                const isRespAnswered = !!(resp?.selectedOptionIds && resp.selectedOptionIds.length > 0);
                const isRespFlagged = !!resp?.isFlagged;

                return (
                  <tr
                    key={q.id}
                    onClick={() => onGoToQuestion(idx)}
                    className="hover:bg-slate-800/50 cursor-pointer transition-colors"
                  >
                    <td className="px-6 py-4 font-mono font-bold text-white">
                      Questão {idx + 1}
                    </td>
                    <td className="px-6 py-4">
                      {isRespAnswered ? (
                        <span className="inline-flex items-center gap-1 text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full">
                          Respondida ({resp.selectedOptionIds.join(', ')})
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-xs font-semibold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-full">
                          Incompleta
                        </span>
                      )}
                    </td>
                    <td className="px-6 py-4">
                      {isRespFlagged ? (
                        <span className="inline-flex items-center gap-1 text-xs font-bold text-amber-400">
                          <Flag className="h-4 w-4 fill-amber-400" />
                          Sim
                        </span>
                      ) : (
                        <span className="text-xs text-slate-500">—</span>
                      )}
                    </td>
                    <td className="px-6 py-4 text-xs text-slate-400 truncate max-w-xs">
                      {q.domainName}
                    </td>
                    <td className="px-6 py-4 text-right">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          onGoToQuestion(idx);
                        }}
                        className="text-xs font-semibold text-amber-400 hover:text-amber-300 underline"
                      >
                        Ir para questão
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Botões de Ação Final */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 p-4 rounded-xl bg-slate-900 border border-slate-800">
        <button
          onClick={onBackToExam}
          className="w-full sm:w-auto flex items-center justify-center gap-2 px-5 py-3 rounded-xl border border-slate-700 bg-slate-800 text-slate-200 hover:bg-slate-700 font-semibold text-sm transition-colors"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Voltar para as Questões</span>
        </button>

        <button
          onClick={onSubmitExam}
          className="w-full sm:w-auto flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-sm shadow-lg shadow-emerald-900/30 transition-all hover:scale-[1.02]"
        >
          <Send className="h-4 w-4" />
          <span>Submeter e Finalizar Simulado</span>
        </button>
      </div>
    </div>
  );
}
