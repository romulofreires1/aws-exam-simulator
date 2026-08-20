import { ExamDefinition } from '@/types/exam';
import sapC02 from './sap-c02.json';
import saaC03 from './saa-c03.json';
import clfC02 from './clf-c02.json';

// Registro central dos simulados disponíveis
export const AVAILABLE_EXAMS: ExamDefinition[] = [
  sapC02 as unknown as ExamDefinition,
  saaC03 as unknown as ExamDefinition,
  clfC02 as unknown as ExamDefinition,
];

export function getAllExams(): ExamDefinition[] {
  return AVAILABLE_EXAMS;
}

export function getExamById(id: string): ExamDefinition | undefined {
  if (!id) return undefined;
  const normalizedId = id.toUpperCase();
  return AVAILABLE_EXAMS.find(
    (exam) => exam.id.toUpperCase() === normalizedId || exam.code.toUpperCase() === normalizedId
  );
}
