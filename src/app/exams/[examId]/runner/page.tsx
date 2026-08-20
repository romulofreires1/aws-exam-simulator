import { getAllExams } from '@/data/exams';
import { ExamRunnerClient } from '@/components/exam/ExamRunnerClient';

interface ExamRunnerPageProps {
  params: Promise<{ examId: string }>;
}

export function generateStaticParams() {
  const exams = getAllExams();
  return exams.map((exam) => ({
    examId: exam.id,
  }));
}

export default async function ExamRunnerPage({ params }: ExamRunnerPageProps) {
  const { examId } = await params;
  return <ExamRunnerClient examId={examId} />;
}
