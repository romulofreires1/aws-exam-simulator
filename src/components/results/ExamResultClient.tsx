'use client';

import React, { useState, useEffect, Suspense } from 'react';
import Link from 'next/link';
import { useSearchParams } from 'next/navigation';
import { getExamById } from '@/data/exams';
import { getAttemptById, getAllAttempts } from '@/lib/storage/examStorage';
import { ExamAttempt } from '@/types/exam';
import { ScoreCard } from '@/components/results/ScoreCard';
import { DomainBreakdownList } from '@/components/results/DomainBreakdownList';
import { QuestionReviewList } from '@/components/results/QuestionReviewList';
import { RotateCcw, History, AlertCircle, ArrowLeft } from 'lucide-react';

function ExamResultContent({ examId }: { examId: string }) {
  const searchParams = useSearchParams();
  const attemptId = searchParams.get('attemptId');

  const [attempt, setAttempt] = useState<ExamAttempt | null>(null);
  const [isLoaded, setIsLoaded] = useState<boolean>(false);

  const exam = getExamById(examId);

  useEffect(() => {
    if (attemptId) {
      const savedAttempt = getAttemptById(attemptId);
      setAttempt(savedAttempt);
    } else {
      // Se não tiver attemptId na URL, busca a tentativa mais recente deste exame
      const attempts = getAllAttempts().filter(
        (a) => a.examId.toUpperCase() === examId.toUpperCase() && a.isCompleted
      );
      if (attempts.length > 0) {
        setAttempt(attempts[0]);
      }
    }
    setIsLoaded(true);
  }, [attemptId, examId]);

  if (!isLoaded) {
    return (
      <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-amber-400 mx-auto mb-4" />
          <p className="text-slate-400 text-sm">Loading exam report...</p>
        </div>
      </div>
    );
  }

  if (!attempt || !exam) {
    return (
      <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center p-4">
        <div className="text-center max-w-md p-8 rounded-3xl bg-slate-900 border border-slate-800">
          <AlertCircle className="h-12 w-12 text-amber-400 mx-auto mb-4" />
          <h1 className="text-2xl font-bold text-white mb-2">Attempt Not Found</h1>
          <p className="text-slate-400 text-sm mb-6">
            Could not load the report for this exam attempt.
          </p>
          <Link
            href="/"
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-sm"
          >
            <ArrowLeft className="h-4 w-4" />
            <span>Back to Home</span>
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 pb-24 pt-8">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        {/* Navigation Breadcrumb & Quick Actions */}
        <div className="flex flex-wrap items-center justify-between gap-4">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-xs font-semibold text-slate-400 hover:text-white transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
            <span>Back to Exam Catalog</span>
          </Link>

          <div className="flex items-center gap-3">
            <Link
              href={`/exams/${exam.id}/runner?mode=${attempt.mode}`}
              className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 hover:text-white font-bold text-xs transition-colors"
            >
              <RotateCcw className="h-3.5 w-3.5" />
              <span>Retake Exam</span>
            </Link>

            <Link
              href="/history"
              className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 hover:text-white font-bold text-xs transition-colors"
            >
              <History className="h-3.5 w-3.5" />
              <span>View History</span>
            </Link>
          </div>
        </div>

        {/* 1. Main Score Card */}
        <ScoreCard attempt={attempt} passingScore={exam.passingScore} />

        {/* 2. Official Domain Breakdown */}
        {attempt.score?.domainBreakdown && (
          <DomainBreakdownList domains={attempt.score.domainBreakdown} />
        )}

        {/* 3. Detailed Question Review */}
        <QuestionReviewList questions={exam.questions} responses={attempt.responses} />
      </div>
    </div>
  );
}

export function ExamResultClient({ examId }: { examId: string }) {
  return (
    <Suspense
      fallback={
        <div className="min-h-screen bg-slate-950 flex items-center justify-center text-slate-400 text-sm">
          Loading report...
        </div>
      }
    >
      <ExamResultContent examId={examId} />
    </Suspense>
  );
}
