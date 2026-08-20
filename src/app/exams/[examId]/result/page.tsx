import { getAllExams } from '@/data/exams';
import { ExamResultClient } from '@/components/results/ExamResultClient';

interface ExamResultPageProps {
  params: Promise<{ examId: string }>;
}

export function generateStaticParams() {
  const exams = getAllExams();
  return exams.map((exam) => ({
    examId: exam.id,
  }));
}

export default async function ExamResultPage({ params }: ExamResultPageProps) {
  const { examId } = await params;
  return <ExamResultClient examId={examId} />;
}
