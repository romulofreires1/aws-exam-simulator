import { ExamDefinition } from '@/types/exam';
import sapC02Sim1 from './sap-c02-sim-1.json';
import sapC02Sim2 from './sap-c02-sim-2.json';
import sapC02Sim3 from './sap-c02-sim-3.json';
import sapC02Sim4 from './sap-c02-sim-4.json';
import sapC02Sim5 from './sap-c02-sim-5.json';
import sapC02Sim6 from './sap-c02-sim-6.json';
import sapC02Sim7 from './sap-c02-sim-7-gaps.json';
import sapC02Sim8 from './sap-c02-sim-8.json';
import saaC03 from './saa-c03.json';
import clfC02 from './clf-c02.json';

// Central registry of available exams
export const AVAILABLE_EXAMS: ExamDefinition[] = [
  sapC02Sim1 as unknown as ExamDefinition,
  sapC02Sim2 as unknown as ExamDefinition,
  sapC02Sim3 as unknown as ExamDefinition,
  sapC02Sim4 as unknown as ExamDefinition,
  sapC02Sim5 as unknown as ExamDefinition,
  sapC02Sim6 as unknown as ExamDefinition,
  sapC02Sim7 as unknown as ExamDefinition,
  sapC02Sim8 as unknown as ExamDefinition,
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
