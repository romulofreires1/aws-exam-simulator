'use client';

import React from 'react';
import { Flag, CheckCircle, AlertTriangle, ArrowLeft, Send, LogOut } from 'lucide-react';
import { Question, QuestionUserResponse, ExamLanguage } from '@/types/exam';
import { getLocalizedQuestion } from '@/lib/localization';

interface ExamReviewScreenProps {
  questions: Question[];
  responses: Record<string, QuestionUserResponse>;
  language?: ExamLanguage;
  onGoToQuestion: (index: number) => void;
  onBackToExam: () => void;
  onSubmitExam: () => void;
  onAbandonExam?: () => void;
}

export function ExamReviewScreen({
  questions,
  responses,
  language = 'en',
  onGoToQuestion,
  onBackToExam,
  onSubmitExam,
  onAbandonExam,
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
          Exam Review Screen
        </h1>
        <p className="text-slate-400 text-sm leading-relaxed">
          Review your answers before submitting. You can click on any question row in the table to return to that question.
        </p>

        {/* Status Summary */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-6">
          <div className="bg-slate-950/60 border border-slate-800 p-4 rounded-xl flex items-center gap-3">
            <div className="p-2 rounded-lg bg-emerald-500/20 text-emerald-400">
              <CheckCircle className="h-5 w-5" />
            </div>
            <div>
              <p className="text-xs text-slate-400">Answered</p>
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
              <p className="text-xs text-slate-400">Flagged for Review</p>
              <p className="text-xl font-bold text-white">{flagged}</p>
            </div>
          </div>

          <div className="bg-slate-950/60 border border-slate-800 p-4 rounded-xl flex items-center gap-3">
            <div className="p-2 rounded-lg bg-rose-500/20 text-rose-400">
              <AlertTriangle className="h-5 w-5" />
            </div>
            <div>
              <p className="text-xs text-slate-400">Unanswered</p>
              <p className="text-xl font-bold text-white">{unanswered}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Review Table */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl mb-8">
        <div className="max-h-[500px] overflow-y-auto">
          <table className="w-full text-left text-sm text-slate-300">
            <thead className="bg-slate-950/80 text-xs uppercase font-bold text-slate-400 sticky top-0 border-b border-slate-800">
              <tr>
                <th className="px-6 py-3.5">#</th>
                <th className="px-6 py-3.5">Status</th>
                <th className="px-6 py-3.5">Flagged</th>
                <th className="px-6 py-3.5">Domain</th>
                <th className="px-6 py-3.5 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {questions.map((rawQ, idx) => {
                const q = getLocalizedQuestion(rawQ, language);
                const resp = responses[rawQ.id];
                const isRespAnswered = !!(resp?.selectedOptionIds && resp.selectedOptionIds.length > 0);
                const isRespFlagged = !!resp?.isFlagged;

                return (
                  <tr
                    key={rawQ.id}
                    onClick={() => onGoToQuestion(idx)}
                    className="hover:bg-slate-800/50 cursor-pointer transition-colors"
                  >
                    <td className="px-6 py-4 font-mono font-bold text-white">
                      Question {idx + 1}
                    </td>
                    <td className="px-6 py-4">
                      {isRespAnswered ? (
                        <span className="inline-flex items-center gap-1 text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full">
                          Answered ({resp.selectedOptionIds.join(', ')})
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-xs font-semibold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-full">
                          Incomplete
                        </span>
                      )}
                    </td>
                    <td className="px-6 py-4">
                      {isRespFlagged ? (
                        <span className="inline-flex items-center gap-1 text-xs font-bold text-amber-400">
                          <Flag className="h-4 w-4 fill-amber-400" />
                          Yes
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
                        Go to question
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 p-4 rounded-xl bg-slate-900 border border-slate-800">
        <button
          onClick={onBackToExam}
          className="w-full sm:w-auto flex items-center justify-center gap-2 px-5 py-3 rounded-xl border border-slate-700 bg-slate-800 text-slate-200 hover:bg-slate-700 font-semibold text-sm transition-colors cursor-pointer"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Back to Questions</span>
        </button>

        <div className="flex flex-col sm:flex-row items-center gap-3 w-full sm:w-auto">
          {onAbandonExam && (
            <button
              type="button"
              onClick={onAbandonExam}
              className="w-full sm:w-auto flex items-center justify-center gap-2 px-5 py-3 rounded-xl border border-rose-900/60 bg-rose-950/20 hover:bg-rose-950/40 text-rose-300 hover:text-rose-200 font-semibold text-sm transition-colors cursor-pointer"
            >
              <LogOut className="h-4 w-4 text-rose-400" />
              <span>Abandon Exam</span>
            </button>
          )}

          <button
            onClick={onSubmitExam}
            className="w-full sm:w-auto flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-sm shadow-lg shadow-emerald-900/30 transition-all hover:scale-[1.02] cursor-pointer"
          >
            <Send className="h-4 w-4" />
            <span>Submit & Finish Exam</span>
          </button>
        </div>
      </div>
    </div>
  );
}
