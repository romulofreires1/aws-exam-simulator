import { ExamDefinition } from '@/types/exam';
import sapC02Sim1 from './sap-c02-sim-1.json';
import sapC02Sim2 from './sap-c02-sim-2.json';
import sapC02Sim3 from './sap-c02-sim-3.json';
import saaC03 from './saa-c03.json';
import clfC02 from './clf-c02.json';

// Central registry of available exams
export const AVAILABLE_EXAMS: ExamDefinition[] = [
  sapC02Sim1 as unknown as ExamDefinition,
  sapC02Sim2 as unknown as ExamDefinition,
  sapC02Sim3 as unknown as ExamDefinition,
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
