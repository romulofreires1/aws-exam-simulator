'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { getAllAttempts, deleteAttempt } from '@/lib/storage/examStorage';
import { ExamAttempt } from '@/types/exam';
import {
  History,
  CheckCircle2,
  XCircle,
  Clock,
  Trash2,
  Award,
  ArrowRight,
  TrendingUp,
  RotateCcw,
} from 'lucide-react';

export default function HistoryPage() {
  const [attempts, setAttempts] = useState<ExamAttempt[]>([]);
  const [filterExam, setFilterExam] = useState<string>('all');

  useEffect(() => {
    setAttempts(getAllAttempts());
  }, []);

  const handleDelete = (id: string) => {
    if (confirm('Tem certeza que deseja excluir o registro deste simulado?')) {
      deleteAttempt(id);
      setAttempts(getAllAttempts());
    }
  };

  const completedAttempts = attempts.filter((a) => a.isCompleted);

  const filtered = completedAttempts.filter((a) => {
    if (filterExam === 'all') return true;
    return a.examCode.toUpperCase() === filterExam.toUpperCase();
  });

  const totalCompleted = completedAttempts.length;
  const passedCount = completedAttempts.filter((a) => a.score?.passed).length;
  const averageScore =
    totalCompleted > 0
      ? Math.round(
          completedAttempts.reduce((acc, a) => acc + (a.score?.scaledScore || 0), 0) /
            totalCompleted
        )
      : 0;

  const totalTimeSeconds = completedAttempts.reduce(
    (acc, a) => acc + (a.totalTimeSpentSeconds || 0),
    0
  );
  const totalHours = (totalTimeSeconds / 3600).toFixed(1);

  const uniqueExams = Array.from(new Set(completedAttempts.map((a) => a.examCode)));

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 pb-24 pt-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto space-y-8">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <History className="h-6 w-6 text-amber-400" />
              <h1 className="text-3xl font-black text-white">Histórico & Desempenho</h1>
            </div>
            <p className="text-xs sm:text-sm text-slate-400">
              Acompanhe sua evolução e revise simulados anteriores salvos no navegador
            </p>
          </div>
        </div>

        {/* Global Stats Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <p className="text-xs font-bold uppercase text-slate-400">Total de Simulados</p>
            <p className="text-3xl font-black text-white mt-1">{totalCompleted}</p>
          </div>

          <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <p className="text-xs font-bold uppercase text-slate-400">Aprovações</p>
            <p className="text-3xl font-black text-emerald-400 mt-1">
              {passedCount} <span className="text-xs text-slate-500">/ {totalCompleted}</span>
            </p>
          </div>

          <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <p className="text-xs font-bold uppercase text-slate-400">Média Geral</p>
            <p className="text-3xl font-black text-amber-400 mt-1">
              {averageScore > 0 ? `${averageScore}` : '—'}
            </p>
          </div>

          <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <p className="text-xs font-bold uppercase text-slate-400">Tempo de Estudo</p>
            <p className="text-3xl font-black text-blue-400 mt-1">{totalHours}h</p>
          </div>
        </div>

        {/* Filter Bar */}
        {uniqueExams.length > 0 && (
          <div className="flex items-center gap-2 overflow-x-auto pb-1">
            <button
              onClick={() => setFilterExam('all')}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                filterExam === 'all'
                  ? 'bg-amber-500 text-slate-950 font-black'
                  : 'bg-slate-900 text-slate-300 border border-slate-800 hover:bg-slate-800'
              }`}
            >
              Todos os Exames
            </button>
            {uniqueExams.map((code) => (
              <button
                key={code}
                onClick={() => setFilterExam(code)}
                className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                  filterExam === code
                    ? 'bg-amber-500 text-slate-950 font-black'
                    : 'bg-slate-900 text-slate-300 border border-slate-800 hover:bg-slate-800'
                }`}
              >
                {code}
              </button>
            ))}
          </div>
        )}

        {/* Table of Attempts */}
        {filtered.length === 0 ? (
          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-12 text-center max-w-lg mx-auto">
            <History className="h-12 w-12 text-slate-600 mx-auto mb-4" />
            <h3 className="text-lg font-bold text-white mb-1">Nenhum Simulado Encontrado</h3>
            <p className="text-xs text-slate-400 mb-6">
              Complete um simulado para ver suas métricas e histórico detalhado aqui.
            </p>
            <Link
              href="/"
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs"
            >
              <span>Ir para o Catálogo</span>
              <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
        ) : (
          <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm text-slate-300">
                <thead className="bg-slate-950/80 text-xs uppercase font-bold text-slate-400 border-b border-slate-800">
                  <tr>
                    <th className="px-6 py-4">Exame</th>
                    <th className="px-6 py-4">Modo</th>
                    <th className="px-6 py-4">Pontuação</th>
                    <th className="px-6 py-4">Resultado</th>
                    <th className="px-6 py-4">Tempo Gasto</th>
                    <th className="px-6 py-4">Data</th>
                    <th className="px-6 py-4 text-right">Ações</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {filtered.map((att) => {
                    const mins = Math.floor(att.totalTimeSpentSeconds / 60);
                    const secs = att.totalTimeSpentSeconds % 60;
                    const dateStr = att.completedAt
                      ? new Date(att.completedAt).toLocaleDateString('pt-BR', {
                          day: '2-digit',
                          month: '2-digit',
                          year: 'numeric',
                          hour: '2-digit',
                          minute: '2-digit',
                        })
                      : '—';

                    return (
                      <tr
                        key={att.id}
                        className="hover:bg-slate-800/40 transition-colors"
                      >
                        <td className="px-6 py-4">
                          <div>
                            <span className="font-mono font-black text-white text-base">
                              {att.examCode}
                            </span>
                            <p className="text-xs text-slate-400 truncate max-w-xs">
                              {att.examTitle}
                            </p>
                          </div>
                        </td>

                        <td className="px-6 py-4">
                          <span
                            className={`text-[11px] font-bold uppercase px-2.5 py-1 rounded-full ${
                              att.mode === 'real'
                                ? 'bg-emerald-500/10 text-emerald-300 border border-emerald-500/20'
                                : 'bg-blue-500/10 text-blue-300 border border-blue-500/20'
                            }`}
                          >
                            {att.mode === 'real' ? 'Simulado Real' : 'Modo Treino'}
                          </span>
                        </td>

                        <td className="px-6 py-4 font-mono font-black text-white text-base">
                          {att.score?.scaledScore} / 1000{' '}
                          <span className="text-xs font-normal text-slate-400">
                            ({att.score?.percentage}%)
                          </span>
                        </td>

                        <td className="px-6 py-4">
                          {att.score?.passed ? (
                            <span className="inline-flex items-center gap-1.5 text-xs font-bold text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full">
                              <CheckCircle2 className="h-3.5 w-3.5" />
                              Aprovado
                            </span>
                          ) : (
                            <span className="inline-flex items-center gap-1.5 text-xs font-bold text-rose-400 bg-rose-500/10 px-3 py-1 rounded-full">
                              <XCircle className="h-3.5 w-3.5" />
                              Reprovado
                            </span>
                          )}
                        </td>

                        <td className="px-6 py-4 text-xs text-slate-300">
                          {mins}m {secs}s
                        </td>

                        <td className="px-6 py-4 text-xs text-slate-400">
                          {dateStr}
                        </td>

                        <td className="px-6 py-4 text-right space-x-3">
                          <Link
                            href={`/exams/${att.examId}/result?attemptId=${att.id}`}
                            className="text-xs font-bold text-amber-400 hover:text-amber-300 underline"
                          >
                            Revisar
                          </Link>

                          <button
                            onClick={() => handleDelete(att.id)}
                            title="Excluir tentativa"
                            className="text-slate-500 hover:text-rose-400 transition-colors p-1"
                          >
                            <Trash2 className="h-4 w-4" />
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
