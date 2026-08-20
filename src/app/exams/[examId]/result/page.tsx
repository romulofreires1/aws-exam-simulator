import { getAllExams } from '@/data/exams';
import { ExamResultClient } from '@/components/results/ExamResultClient';

interface ExamResultPageProps {
  params: Promise<{ examId: string }>;
}

export function generateStaticParams() {
  const exams = getAllExams();
  const params: { examId: string }[] = [];
  exams.forEach((exam) => {
    params.push({ examId: exam.id });
    if (exam.id.toLowerCase() !== exam.id) {
      params.push({ examId: exam.id.toLowerCase() });
    }
  });
  return params;
}

export default async function ExamResultPage({ params }: ExamResultPageProps) {
  const { examId } = await params;
  return <ExamResultClient examId={examId} />;
}
