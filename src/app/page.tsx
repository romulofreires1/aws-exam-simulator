'use client';

import React, { useState, useEffect, useMemo } from 'react';
import Link from 'next/link';
import { getAllExams } from '@/data/exams';
import { ExamCard } from '@/components/dashboard/ExamCard';
import { getAllAttempts } from '@/lib/storage/examStorage';
import { ExamAttempt } from '@/types/exam';
import {
  Award,
  CheckCircle2,
  History,
  Layers,
  Zap,
  Clock,
  ArrowRight,
  ShieldAlert,
  Search,
  X,
  ChevronLeft,
  ChevronRight,
  Filter,
  SearchX,
} from 'lucide-react';

const CATEGORIES = ['All', 'Foundational', 'Associate', 'Professional', 'Specialty'] as const;
type CategoryFilter = (typeof CATEGORIES)[number];

const ITEMS_PER_PAGE = 6;

export default function HomePage() {
  const exams = useMemo(() => getAllExams(), []);
  const [attempts, setAttempts] = useState<ExamAttempt[]>([]);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [currentPage, setCurrentPage] = useState<number>(1);

  useEffect(() => {
    setAttempts(getAllAttempts());
  }, []);

  const totalQuestionsInBank = exams.reduce((acc, e) => acc + e.questions.length, 0);
  const completedAttempts = attempts.filter((a) => a.isCompleted);
  const passedAttempts = completedAttempts.filter((a) => a.score?.passed);
  const averageScore =
    completedAttempts.length > 0
      ? Math.round(
          completedAttempts.reduce((acc, a) => acc + (a.score?.scaledScore || 0), 0) /
            completedAttempts.length
        )
      : 0;

  // Categorias disponíveis dinamicamente com base nos exames cadastrados
  const categoryCounts = useMemo(() => {
    const counts: Record<string, number> = { All: exams.length };
    exams.forEach((exam) => {
      const cat = exam.category || 'Other';
      counts[cat] = (counts[cat] || 0) + 1;
    });
    return counts;
  }, [exams]);

  // Lista apenas categorias que realmente têm simulados para não gerar filtros vazios
  const activeCategoriesList = useMemo(() => {
    const list = ['All'];
    ['Foundational', 'Associate', 'Professional', 'Specialty'].forEach((cat) => {
      if ((categoryCounts[cat] || 0) > 0) {
        list.push(cat);
      }
    });
    return list;
  }, [categoryCounts]);

  // Filtragem combinada por busca e categoria
  const filteredExams = useMemo(() => {
    const query = searchQuery.trim().toLowerCase();
    const selectedCat = selectedCategory.trim().toLowerCase();

    return exams.filter((exam) => {
      const examCat = (exam.category || '').trim().toLowerCase();

      // Filtro de categoria
      const matchesCategory =
        selectedCat === 'all' || examCat === selectedCat;

      if (!matchesCategory) return false;

      // Filtro de busca textual
      if (!query) return true;

      const code = (exam.code || '').toLowerCase();
      const title = (exam.title || '').toLowerCase();
      const description = (exam.description || '').toLowerCase();
      const id = (exam.id || '').toLowerCase();
      const category = (exam.category || '').toLowerCase();

      return (
        code.includes(query) ||
        title.includes(query) ||
        description.includes(query) ||
        id.includes(query) ||
        category.includes(query)
      );
    });
  }, [exams, searchQuery, selectedCategory]);

  // Paginação
  const totalPages = Math.max(1, Math.ceil(filteredExams.length / ITEMS_PER_PAGE));

  const paginatedExams = useMemo(() => {
    const start = (currentPage - 1) * ITEMS_PER_PAGE;
    return filteredExams.slice(start, start + ITEMS_PER_PAGE);
  }, [filteredExams, currentPage]);

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
    const catalogElement = document.getElementById('catalog-section');
    if (catalogElement) {
      catalogElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const handleCategorySelect = (cat: string) => {
    setSelectedCategory((prev) => (prev.toLowerCase() === cat.toLowerCase() ? 'All' : cat));
    setCurrentPage(1);
  };

  const handleSearchChange = (val: string) => {
    setSearchQuery(val);
    setCurrentPage(1);
  };

  const handleClearFilters = () => {
    setSearchQuery('');
    setSelectedCategory('All');
    setCurrentPage(1);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 pb-20">
      {/* Hero Section */}
      <section className="relative overflow-hidden border-b border-slate-800/80 bg-gradient-to-b from-slate-900/60 via-slate-950 to-slate-950 pt-12 pb-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold mb-4">
              <Zap className="h-3.5 w-3.5" />
              <span>Official Client-Side Simulator • 100% Offline & Private</span>
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-tight">
              Prepare for your <span className="bg-gradient-to-r from-amber-400 to-orange-500 bg-clip-text text-transparent">AWS</span> certification
            </h1>

            <p className="mt-4 text-base sm:text-lg text-slate-400 leading-relaxed">
              Realistic exam simulations with complex scenario-based questions, official timers, elimination strike-through, detailed explanations, and domain breakdowns.
            </p>
          </div>

          {/* Quick Metrics Bar */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-10">
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Certifications</p>
              <p className="text-2xl font-black text-white mt-1">{exams.length}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Question Bank</p>
              <p className="text-2xl font-black text-amber-400 mt-1">{totalQuestionsInBank}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Exams Completed</p>
              <p className="text-2xl font-black text-emerald-400 mt-1">{completedAttempts.length}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
              <p className="text-xs font-bold uppercase text-slate-500">Average Score</p>
              <p className="text-2xl font-black text-white mt-1">
                {averageScore > 0 ? `${averageScore}/1000` : '—'}
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Main Catalog */}
      <section id="catalog-section" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 scroll-mt-6">
        {/* Header & Controls */}
        <div className="flex flex-col gap-5 mb-8">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 className="text-2xl font-black text-white">Certification Catalog</h2>
              <p className="text-xs sm:text-sm text-slate-400">
                Select an exam to start in Real Exam or Practice Mode
              </p>
            </div>

            {/* Results Count Badge */}
            <div className="inline-flex items-center gap-2 text-xs font-semibold text-slate-400 bg-slate-900 px-3.5 py-2 rounded-xl border border-slate-800 self-start sm:self-auto">
              <span>
                Showing{' '}
                <strong className="text-white">
                  {filteredExams.length > 0
                    ? `${(currentPage - 1) * ITEMS_PER_PAGE + 1}–${Math.min(
                        currentPage * ITEMS_PER_PAGE,
                        filteredExams.length
                      )}`
                    : '0'}
                </strong>{' '}
                of <strong className="text-amber-400">{filteredExams.length}</strong> exams
              </span>
            </div>
          </div>

          {/* Search Bar & Category Filters (No nested scrollbars) */}
          <div className="p-4 sm:p-5 bg-slate-900/80 border border-slate-800 rounded-2xl flex flex-col gap-4 shadow-lg">
            {/* Search Input Box */}
            <div className="relative w-full">
              <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400 pointer-events-none" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => handleSearchChange(e.target.value)}
                placeholder="Search certifications by code (CLF, SAA, SAP...), title, or keywords..."
                className="w-full pl-10 pr-10 py-3 bg-slate-950/90 border border-slate-750 focus:border-amber-500/80 rounded-xl text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-amber-500/20 transition-all"
              />
              {searchQuery && (
                <button
                  type="button"
                  onClick={() => handleSearchChange('')}
                  title="Clear search"
                  className="absolute right-3 top-1/2 -translate-y-1/2 p-1 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition-colors cursor-pointer"
                >
                  <X className="h-4 w-4" />
                </button>
              )}
            </div>

            {/* Category Filter Pills (Wrap Naturally - No horizontal scroll) */}
            <div className="flex flex-wrap items-center gap-2 pt-1 border-t border-slate-800/60">
              <span className="text-xs text-slate-400 font-semibold mr-1 flex items-center gap-1.5">
                <Filter className="h-3.5 w-3.5 text-amber-400" />
                <span>Level:</span>
              </span>

              {activeCategoriesList.map((cat) => {
                const isSelected = selectedCategory.toLowerCase() === cat.toLowerCase();
                const count = categoryCounts[cat] || 0;

                const getCategoryStyle = () => {
                  if (isSelected) {
                    if (cat === 'Foundational') return 'bg-emerald-500 text-slate-950 shadow-sm shadow-emerald-500/20 ring-2 ring-emerald-400/50';
                    if (cat === 'Associate') return 'bg-blue-500 text-slate-950 shadow-sm shadow-blue-500/20 ring-2 ring-blue-400/50';
                    if (cat === 'Professional') return 'bg-purple-600 text-white shadow-sm shadow-purple-600/20 ring-2 ring-purple-400/50';
                    if (cat === 'Specialty') return 'bg-amber-500 text-slate-950 shadow-sm shadow-amber-500/20 ring-2 ring-amber-400/50';
                    return 'bg-amber-500 text-slate-950 shadow-sm shadow-amber-500/20 ring-2 ring-amber-400/50';
                  }

                  if (cat === 'Foundational') return 'bg-slate-950/60 hover:bg-emerald-500/10 text-emerald-300 border border-emerald-500/30';
                  if (cat === 'Associate') return 'bg-slate-950/60 hover:bg-blue-500/10 text-blue-300 border border-blue-500/30';
                  if (cat === 'Professional') return 'bg-slate-950/60 hover:bg-purple-500/10 text-purple-300 border border-purple-500/30';
                  if (cat === 'Specialty') return 'bg-slate-950/60 hover:bg-amber-500/10 text-amber-300 border border-amber-500/30';
                  return 'bg-slate-950/60 hover:bg-slate-800 text-slate-300 border border-slate-800';
                };

                return (
                  <button
                    key={cat}
                    type="button"
                    onClick={() => handleCategorySelect(cat)}
                    title={isSelected ? `Remove filter ${cat}` : `Filter by ${cat}`}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer hover:scale-105 active:scale-95 ${getCategoryStyle()}`}
                  >
                    <span>{cat === 'All' ? 'All Levels' : cat}</span>
                    <span
                      className={`text-[10px] px-1.5 py-0.2 rounded-full font-mono font-bold ${
                        isSelected
                          ? cat === 'Professional'
                            ? 'bg-purple-950/80 text-purple-100'
                            : 'bg-slate-950/30 text-slate-950'
                          : 'bg-slate-900 border border-slate-800 text-slate-400'
                      }`}
                    >
                      {count}
                    </span>
                  </button>
                );
              })}

              {(selectedCategory !== 'All' || searchQuery) && (
                <button
                  type="button"
                  onClick={handleClearFilters}
                  className="sm:ml-auto text-xs text-amber-400 hover:text-amber-200 underline font-semibold flex items-center gap-1 cursor-pointer py-1"
                >
                  <X className="h-3.5 w-3.5" />
                  <span>Clear all filters</span>
                </button>
              )}
            </div>
          </div>

          {/* Active Filter Indicator Banner */}
          {(selectedCategory !== 'All' || searchQuery) && (
            <div className="flex flex-wrap items-center justify-between gap-2 px-4 py-2.5 bg-amber-500/10 border border-amber-500/30 rounded-xl text-xs">
              <div className="flex items-center gap-2 text-amber-300">
                <Filter className="h-3.5 w-3.5 text-amber-400 shrink-0" />
                <span>
                  Filtering by:{' '}
                  {selectedCategory !== 'All' && (
                    <strong className="underline mr-2">Level: {selectedCategory}</strong>
                  )}
                  {searchQuery && (
                    <span>
                      Search: <strong>&quot;{searchQuery}&quot;</strong>
                    </span>
                  )}
                  {' '}({filteredExams.length} {filteredExams.length === 1 ? 'exam' : 'exams'} found)
                </span>
              </div>

              <button
                type="button"
                onClick={handleClearFilters}
                className="text-xs font-bold text-amber-400 hover:text-amber-200 underline cursor-pointer"
              >
                Reset
              </button>
            </div>
          )}
        </div>

        {/* Card Grid / Empty State */}
        {paginatedExams.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 transition-all">
            {paginatedExams.map((exam) => (
              <ExamCard
                key={exam.id}
                exam={exam}
                onSelectCategory={(cat) => handleCategorySelect(cat)}
              />
            ))}
          </div>
        ) : (
          <div className="text-center py-16 px-4 bg-slate-900/50 border border-dashed border-slate-800 rounded-3xl animate-in fade-in duration-150">
            <div className="mx-auto w-16 h-16 rounded-2xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 mb-4">
              <SearchX className="h-8 w-8" />
            </div>
            <h3 className="text-lg font-bold text-white mb-2">No exams found</h3>
            <p className="text-sm text-slate-400 max-w-md mx-auto mb-6 leading-relaxed">
              No certifications matched your filter{' '}
              {selectedCategory !== 'All' && <span>(Category: <strong className="text-white">{selectedCategory}</strong>)</span>}
              {searchQuery && <span> with search query &quot;<strong className="text-white">{searchQuery}</strong>&quot;</span>}.
            </p>
            <button
              type="button"
              onClick={handleClearFilters}
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition-colors cursor-pointer"
            >
              <X className="h-3.5 w-3.5" />
              <span>Clear filters & show all</span>
            </button>
          </div>
        )}

        {/* Pagination Controls */}
        {totalPages > 1 && (
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 mt-10 pt-6 border-t border-slate-800/80">
            <p className="text-xs text-slate-400 order-2 sm:order-1 font-medium">
              Page <strong className="text-white">{currentPage}</strong> of{' '}
              <strong className="text-white">{totalPages}</strong> ({filteredExams.length} total exams)
            </p>

            <div className="flex items-center gap-2 order-1 sm:order-2">
              {/* Previous Button */}
              <button
                type="button"
                onClick={() => handlePageChange(currentPage - 1)}
                disabled={currentPage === 1}
                className={`flex items-center gap-1 px-3.5 py-2 rounded-xl text-xs font-bold transition-all border ${
                  currentPage === 1
                    ? 'opacity-40 cursor-not-allowed bg-slate-950 border-slate-850 text-slate-600'
                    : 'bg-slate-900 hover:bg-slate-800 border-slate-700 text-slate-200 hover:text-white cursor-pointer shadow-sm'
                }`}
              >
                <ChevronLeft className="h-4 w-4" />
                <span className="hidden xs:inline">Previous</span>
              </button>

              {/* Numbered Page Buttons */}
              <div className="flex items-center gap-1">
                {Array.from({ length: totalPages }, (_, i) => i + 1).map((pageNum) => {
                  const isCurrent = pageNum === currentPage;
                  return (
                    <button
                      key={pageNum}
                      type="button"
                      onClick={() => handlePageChange(pageNum)}
                      className={`h-8 w-8 rounded-xl text-xs font-mono font-bold transition-all cursor-pointer ${
                        isCurrent
                          ? 'bg-amber-500 text-slate-950 shadow-sm shadow-amber-500/20'
                          : 'bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-white border border-slate-800'
                      }`}
                    >
                      {pageNum}
                    </button>
                  );
                })}
              </div>

              {/* Next Button */}
              <button
                type="button"
                onClick={() => handlePageChange(currentPage + 1)}
                disabled={currentPage === totalPages}
                className={`flex items-center gap-1 px-3.5 py-2 rounded-xl text-xs font-bold transition-all border ${
                  currentPage === totalPages
                    ? 'opacity-40 cursor-not-allowed bg-slate-950 border-slate-850 text-slate-600'
                    : 'bg-slate-900 hover:bg-slate-800 border-slate-700 text-slate-200 hover:text-white cursor-pointer shadow-sm'
                }`}
              >
                <span className="hidden xs:inline">Next</span>
                <ChevronRight className="h-4 w-4" />
              </button>
            </div>
          </div>
        )}
      </section>

      {/* Recent Activity */}
      {completedAttempts.length > 0 && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16">
          <div className="flex items-center justify-between gap-4 mb-6">
            <div className="flex items-center gap-2">
              <History className="h-5 w-5 text-amber-400" />
              <h2 className="text-xl font-bold text-white">Recent Attempts</h2>
            </div>
            <Link
              href="/history"
              className="text-xs font-semibold text-amber-400 hover:text-amber-300 flex items-center gap-1"
            >
              <span>View full history</span>
              <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </div>

          <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm text-slate-300">
                <thead className="bg-slate-950/80 text-xs uppercase font-bold text-slate-400 border-b border-slate-800">
                  <tr>
                    <th className="px-6 py-3.5">Exam</th>
                    <th className="px-6 py-3.5">Mode</th>
                    <th className="px-6 py-3.5">Score</th>
                    <th className="px-6 py-3.5">Result</th>
                    <th className="px-6 py-3.5">Date</th>
                    <th className="px-6 py-3.5 text-right">Report</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {completedAttempts.slice(0, 5).map((att) => (
                    <tr key={att.id} className="hover:bg-slate-800/40 transition-colors">
                      <td className="px-6 py-4 font-bold text-white">
                        {att.examCode}
                      </td>
                      <td className="px-6 py-4 text-xs capitalize text-slate-400">
                        {att.mode === 'real' ? 'Real Exam' : 'Practice Mode'}
                      </td>
                      <td className="px-6 py-4 font-mono font-bold text-white">
                        {att.score?.scaledScore} / 1000 ({att.score?.percentage}%)
                      </td>
                      <td className="px-6 py-4">
                        {att.score?.passed ? (
                          <span className="inline-flex items-center gap-1 text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full">
                            <CheckCircle2 className="h-3.5 w-3.5" />
                            Passed
                          </span>
                        ) : (
                          <span className="inline-flex items-center gap-1 text-xs font-bold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-full">
                            Failed
                          </span>
                        )}
                      </td>
                      <td className="px-6 py-4 text-xs text-slate-400">
                        {att.completedAt
                          ? new Date(att.completedAt).toLocaleDateString('en-US', {
                              month: 'short',
                              day: 'numeric',
                              year: 'numeric',
                            })
                          : '—'}
                      </td>
                      <td className="px-6 py-4 text-right">
                        <Link
                          href={`/exams/${att.examId}/result?attemptId=${att.id}`}
                          className="text-xs font-bold text-amber-400 hover:text-amber-300 underline"
                        >
                          View Review
                        </Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
