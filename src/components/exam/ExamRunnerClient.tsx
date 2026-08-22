'use client';

import React, { useState, useEffect, Suspense, useCallback } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { getExamById } from '@/data/exams';
import { ExamMode } from '@/types/exam';
import { useExamEngine } from '@/hooks/useExamEngine';
import { ExamHeader } from '@/components/exam/ExamHeader';
import { QuestionView } from '@/components/exam/QuestionView';
import { ExamReviewScreen } from '@/components/exam/ExamReviewScreen';
import { QuestionGridModal } from '@/components/exam/QuestionGridModal';
import { ScratchpadModal } from '@/components/exam/ScratchpadModal';
import { ExamPauseModal } from '@/components/exam/ExamPauseModal';
import {
  getThemePreference,
  setThemePreference,
  ExamTheme,
} from '@/lib/storage/examStorage';
import { AlertCircle, ArrowLeft } from 'lucide-react';
import Link from 'next/link';

function ExamRunnerContent({ examId }: { examId: string }) {
  const searchParams = useSearchParams();
  const rawMode = searchParams.get('mode');
  const mode: ExamMode = rawMode === 'practice' ? 'practice' : 'real';

  const router = useRouter();
  const exam = getExamById(examId);

  const [theme, setTheme] = useState<ExamTheme>('aws-modern');

  useEffect(() => {
    setTheme(getThemePreference());
  }, []);

  const handleToggleTheme = () => {
    const nextTheme: ExamTheme = theme === 'aws-modern' ? 'pearson-vue' : 'aws-modern';
    setTheme(nextTheme);
    setThemePreference(nextTheme);
  };

  const handleFinishExam = (attemptId: string) => {
    router.push(`/exams/${examId}/result?attemptId=${attemptId}`);
  };

  const engine = useExamEngine({
    exam: exam || {
      id: '',
      title: '',
      code: '',
      category: 'Associate',
      description: '',
      totalQuestions: 0,
      timeLimitMinutes: 0,
      passingScore: 0,
      domains: [],
      questions: [],
    },
    mode,
    onFinishExam: handleFinishExam,
  });

  const handleExitToHome = useCallback(() => {
    engine.saveCurrentSession();
    router.push('/');
  }, [engine, router]);

  if (!exam) {
    return (
      <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center p-4">
        <div className="text-center max-w-md p-8 rounded-3xl bg-slate-900 border border-slate-800">
          <AlertCircle className="h-12 w-12 text-amber-400 mx-auto mb-4" />
          <h1 className="text-2xl font-bold text-white mb-2">Exam Not Found</h1>
          <p className="text-slate-400 text-sm mb-6">
            The exam with identifier &quot;{examId}&quot; was not found in our catalog.
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

  const isPearson = theme === 'pearson-vue';

  return (
    <div
      className={`min-h-screen flex flex-col transition-colors duration-200 ${
        isPearson ? 'bg-[#001733] text-slate-100' : 'bg-slate-950 text-slate-100'
      }`}
    >
      {/* Exam Header */}
      <ExamHeader
        examCode={exam.code}
        examTitle={exam.title}
        mode={mode}
        currentIndex={engine.currentIndex}
        totalQuestions={exam.questions.length}
        formattedTime={engine.formattedTime}
        isTimerWarning={engine.isTimerWarning}
        isTimerCritical={engine.isTimerCritical}
        isTimerRunning={engine.isTimerRunning}
        isFlagged={engine.currentResponse?.isFlagged || false}
        theme={theme}
        isPaused={engine.isPaused}
        onTogglePause={engine.togglePause}
        onToggleTimer={engine.togglePause}
        onToggleFlag={engine.toggleFlag}
        onOpenQuestionMap={() => engine.setIsQuestionMapOpen(true)}
        onOpenScratchpad={() => engine.setIsScratchpadOpen(true)}
        onOpenReviewScreen={() => engine.setIsReviewScreenOpen(true)}
        onToggleTheme={handleToggleTheme}
      />

      {/* Main Content */}
      <main className="flex-1">
        {engine.isReviewScreenOpen ? (
          <ExamReviewScreen
            questions={exam.questions}
            responses={engine.responses}
            onGoToQuestion={(idx) => {
              engine.goToQuestion(idx);
              engine.setIsReviewScreenOpen(false);
            }}
            onBackToExam={() => engine.setIsReviewScreenOpen(false)}
            onSubmitExam={engine.submitExam}
          />
        ) : (
          <QuestionView
            question={engine.currentQuestion}
            questionIndex={engine.currentIndex}
            totalQuestions={exam.questions.length}
            response={
              engine.currentResponse || {
                questionId: engine.currentQuestion?.id || '',
                selectedOptionIds: [],
                struckOutOptionIds: [],
                isFlagged: false,
                timeSpentSeconds: 0,
              }
            }
            mode={mode}
            theme={theme}
            onToggleOption={engine.toggleOption}
            onToggleStrikeThrough={engine.toggleStrikeThrough}
            onToggleHighlight={engine.toggleHighlight}
            onClearHighlights={engine.clearHighlights}
            onToggleCheckAnswer={engine.toggleCheckAnswer}
            onPrev={engine.prevQuestion}
            onNext={engine.nextQuestion}
          />
        )}
      </main>

      {/* Support Modals */}
      <ExamPauseModal
        isOpen={engine.isPaused}
        examCode={exam.code}
        examTitle={exam.title}
        mode={mode}
        currentIndex={engine.currentIndex}
        totalQuestions={exam.questions.length}
        formattedTime={engine.formattedTime}
        stats={engine.stats}
        theme={theme}
        onResume={engine.resumeExam}
        onExit={handleExitToHome}
        onReview={() => {
          engine.resumeExam();
          engine.setIsReviewScreenOpen(true);
        }}
      />

      <QuestionGridModal
        isOpen={engine.isQuestionMapOpen}
        onClose={() => engine.setIsQuestionMapOpen(false)}
        questions={exam.questions}
        responses={engine.responses}
        currentIndex={engine.currentIndex}
        onSelectQuestion={(idx) => engine.goToQuestion(idx)}
      />

      <ScratchpadModal
        isOpen={engine.isScratchpadOpen}
        onClose={() => engine.setIsScratchpadOpen(false)}
        questionNumber={engine.currentIndex + 1}
        initialNotes={engine.currentResponse?.notes || ''}
        onSaveNotes={(notes) => engine.setNotes(notes)}
      />
    </div>
  );
}

export function ExamRunnerClient({ examId }: { examId: string }) {
  return (
    <Suspense
      fallback={
        <div className="min-h-screen bg-slate-950 flex items-center justify-center text-slate-400 text-sm">
          Loading exam...
        </div>
      }
    >
      <ExamRunnerContent examId={examId} />
    </Suspense>
  );
}
