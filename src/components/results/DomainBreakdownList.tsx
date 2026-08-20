'use client';

import React from 'react';
import { Layers, CheckCircle2, AlertCircle } from 'lucide-react';
import { DomainScoreResult } from '@/types/exam';

interface DomainBreakdownListProps {
  domains: Record<string, DomainScoreResult>;
}

export function DomainBreakdownList({ domains }: DomainBreakdownListProps) {
  const domainList = Object.values(domains);

  if (domainList.length === 0) return null;

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
      <div className="flex items-center gap-2.5 mb-6">
        <div className="p-2 rounded-lg bg-amber-500/20 text-amber-400">
          <Layers className="h-5 w-5" />
        </div>
        <div>
          <h2 className="text-xl font-bold text-white">Desempenho por Domínio Oficial</h2>
          <p className="text-xs text-slate-400">
            Avaliação por seção de competência do guia oficial da certificação AWS
          </p>
        </div>
      </div>

      <div className="space-y-4">
        {domainList.map((d) => {
          const isProficient = d.percentage >= 70;

          return (
            <div
              key={d.domainId}
              className="bg-slate-950/60 border border-slate-800/80 rounded-xl p-4.5 transition-all hover:border-slate-700"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
                <div>
                  <h3 className="font-semibold text-sm sm:text-base text-slate-200">
                    {d.domainName}
                  </h3>
                  <span className="text-xs text-slate-400">
                    {d.correctQuestions} de {d.totalQuestions} questões corretas
                  </span>
                </div>

                <div className="flex items-center gap-3 self-end sm:self-center">
                  <span
                    className={`inline-flex items-center gap-1 text-xs font-bold px-2.5 py-1 rounded-full ${
                      isProficient
                        ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                        : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                    }`}
                  >
                    {isProficient ? (
                      <>
                        <CheckCircle2 className="h-3 w-3" />
                        <span>Atende à Competência</span>
                      </>
                    ) : (
                      <>
                        <AlertCircle className="h-3 w-3" />
                        <span>Necessita Reforço</span>
                      </>
                    )}
                  </span>

                  <span className="font-black text-lg text-white min-w-[3rem] text-right">
                    {d.percentage}%
                  </span>
                </div>
              </div>

              {/* Barra de Progresso */}
              <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div
                  className={`h-full rounded-full transition-all duration-700 ${
                    d.percentage >= 75
                      ? 'bg-emerald-500'
                      : d.percentage >= 60
                      ? 'bg-amber-500'
                      : 'bg-rose-500'
                  }`}
                  style={{ width: `${d.percentage}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
