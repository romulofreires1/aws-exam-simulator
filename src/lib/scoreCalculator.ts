import { ExamDefinition, ExamScore, QuestionUserResponse, DomainScoreResult } from '@/types/exam';

export function isAnswerCorrect(selectedOptions: string[] = [], correctAnswers: string[] = []): boolean {
  if (selectedOptions.length !== correctAnswers.length) return false;
  const sortedSelected = [...selectedOptions].sort();
  const sortedCorrect = [...correctAnswers].sort();
  return sortedSelected.every((val, idx) => val === sortedCorrect[idx]);
}

export function calculateExamScore(
  exam: ExamDefinition,
  responses: Record<string, QuestionUserResponse>
): ExamScore {
  let totalCorrect = 0;
  const totalQuestions = exam.questions.length;

  const domainMap: Record<string, { domainName: string; total: number; correct: number }> = {};

  // Inicializa domínios
  exam.domains.forEach((d) => {
    domainMap[d.id] = {
      domainName: d.name,
      total: 0,
      correct: 0,
    };
  });

  exam.questions.forEach((q) => {
    const userResp = responses[q.id];
    const correct = isAnswerCorrect(userResp?.selectedOptionIds || [], q.correctAnswers);

    if (correct) {
      totalCorrect++;
    }

    if (!domainMap[q.domainId]) {
      domainMap[q.domainId] = {
        domainName: q.domainName || q.domainId,
        total: 0,
        correct: 0,
      };
    }

    domainMap[q.domainId].total++;
    if (correct) {
      domainMap[q.domainId].correct++;
    }
  });

  const percentage = totalQuestions > 0 ? (totalCorrect / totalQuestions) * 100 : 0;
  // Escala oficial AWS: 100 a 1000 pontos
  const scaledScore = totalQuestions > 0 ? Math.round(100 + (percentage / 100) * 900) : 100;
  const passed = scaledScore >= exam.passingScore;

  const domainBreakdown: Record<string, DomainScoreResult> = {};
  Object.entries(domainMap).forEach(([domainId, data]) => {
    domainBreakdown[domainId] = {
      domainId,
      domainName: data.domainName,
      totalQuestions: data.total,
      correctQuestions: data.correct,
      percentage: data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0,
    };
  });

  return {
    scaledScore,
    percentage: Math.round(percentage),
    passed,
    totalCorrect,
    totalQuestions,
    domainBreakdown,
  };
}
