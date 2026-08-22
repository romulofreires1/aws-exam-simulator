export type QuestionType = 'single' | 'multiple';

export type ExamCategory = 'Foundational' | 'Associate' | 'Professional' | 'Specialty';

export type ExamMode = 'real' | 'practice' | 'review';

export type ExamLanguage = 'en' | 'pt' | 'es';

export interface QuestionOption {
  id: string; // e.g. "A", "B", "C", "D", "E"
  text: string;
  explanation?: string;
}

export interface LocalizedOption {
  id: string;
  text: string;
  explanation?: string;
}

export interface LocalizedQuestionContent {
  statement: string;
  options: LocalizedOption[];
  generalExplanation: string;
  domainName?: string;
}

export interface Question {
  id: string;
  examId: string;
  domainId: string;
  domainName: string;
  services?: string[];
  type: QuestionType;
  requiredChoices: number;
  statement: string;
  options: QuestionOption[];
  correctAnswers: string[];
  generalExplanation: string;
  translations?: Partial<Record<ExamLanguage, LocalizedQuestionContent>>;
  referenceUrl?: string;
  difficulty?: 'easy' | 'medium' | 'hard';
}

export interface DomainDefinition {
  id: string;
  name: string;
  weightPercentage: number;
}

export interface ExamDefinition {
  id: string;
  title: string;
  code: string;
  category: ExamCategory;
  description: string;
  totalQuestions: number;
  timeLimitMinutes: number;
  passingScore: number; // e.g. 700 or 750 (scale 100-1000)
  icon?: string;
  availableLanguages?: ExamLanguage[];
  defaultLanguage?: ExamLanguage;
  domains: DomainDefinition[];
  questions: Question[];
}

export interface QuestionUserResponse {
  questionId: string;
  selectedOptionIds: string[];
  struckOutOptionIds: string[];
  highlights?: string[];
  isFlagged: boolean;
  isAnswerChecked?: boolean;
  notes?: string;
  isCorrect?: boolean;
  timeSpentSeconds: number;
}

export interface DomainScoreResult {
  domainId: string;
  domainName: string;
  totalQuestions: number;
  correctQuestions: number;
  percentage: number;
}

export interface ExamScore {
  scaledScore: number; // 100 - 1000
  percentage: number; // 0 - 100
  passed: boolean;
  totalCorrect: number;
  totalQuestions: number;
  domainBreakdown: Record<string, DomainScoreResult>;
}

export interface ExamAttempt {
  id: string;
  examId: string;
  examCode: string;
  examTitle: string;
  mode: ExamMode;
  language?: ExamLanguage;
  startedAt: string;
  completedAt?: string;
  timeRemainingSeconds: number;
  totalTimeSpentSeconds: number;
  isCompleted: boolean;
  currentQuestionIndex: number;
  responses: Record<string, QuestionUserResponse>;
  score?: ExamScore;
}
