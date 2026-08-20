import { getAllExams } from '@/data/exams';
import { ExamRunnerClient } from '@/components/exam/ExamRunnerClient';

interface ExamRunnerPageProps {
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

export default async function ExamRunnerPage({ params }: ExamRunnerPageProps) {
  const { examId } = await params;
  return <ExamRunnerClient examId={examId} />;
}
