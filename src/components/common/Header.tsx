'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { ShieldCheck, History, BookOpen, Layers, Award } from 'lucide-react';

export function Header() {
  const pathname = usePathname();
  const isRunner = pathname?.includes('/runner');

  // No modo de execução do exame, usamos o ExamHeader dedicado para evitar distrações
  if (isRunner) {
    return null;
  }

  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-800 bg-slate-950/80 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-3 group">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-tr from-amber-500 to-orange-500 shadow-md shadow-orange-500/20 group-hover:scale-105 transition-transform">
            <Award className="h-6 w-6 text-slate-950" />
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-black text-lg tracking-tight text-white">AWS</span>
              <span className="font-semibold text-lg tracking-tight text-amber-400">Simulator</span>
            </div>
            <p className="text-[10px] uppercase font-bold tracking-widest text-slate-400">
              Certifications & Practice
            </p>
          </div>
        </Link>

        <nav className="flex items-center gap-1 sm:gap-2">
          <Link
            href="/"
            className={`flex items-center gap-2 px-3.5 py-2 text-sm font-medium rounded-lg transition-colors ${
              pathname === '/'
                ? 'bg-slate-800 text-amber-400'
                : 'text-slate-300 hover:bg-slate-800/60 hover:text-white'
            }`}
          >
            <Layers className="h-4 w-4" />
            <span className="hidden sm:inline">Simulados</span>
          </Link>

          <Link
            href="/history"
            className={`flex items-center gap-2 px-3.5 py-2 text-sm font-medium rounded-lg transition-colors ${
              pathname === '/history'
                ? 'bg-slate-800 text-amber-400'
                : 'text-slate-300 hover:bg-slate-800/60 hover:text-white'
            }`}
          >
            <History className="h-4 w-4" />
            <span className="hidden sm:inline">Histórico & Desempenho</span>
          </Link>
        </nav>
      </div>
    </header>
  );
}
