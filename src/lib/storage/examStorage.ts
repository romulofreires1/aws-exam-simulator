import { ExamAttempt, ExamLanguage } from '@/types/exam';

const ACTIVE_SESSION_PREFIX = 'aws_exam_active_session_';
const ATTEMPTS_KEY = 'aws_exam_history_attempts';
const THEME_KEY = 'aws_exam_theme_preference';
const LANGUAGE_KEY = 'aws_exam_language_preference';

export type ExamTheme = 'aws-modern' | 'pearson-vue';

// Verifica disponibilidade de window/localStorage (SSR Safe)
function isClient(): boolean {
  return typeof window !== 'undefined' && !!window.localStorage;
}

export function getLanguagePreference(): ExamLanguage {
  if (!isClient()) return 'en';
  try {
    const saved = localStorage.getItem(LANGUAGE_KEY) as ExamLanguage;
    return saved === 'pt' || saved === 'es' || saved === 'en' ? saved : 'en';
  } catch {
    return 'en';
  }
}

export function setLanguagePreference(lang: ExamLanguage): void {
  if (!isClient()) return;
  try {
    localStorage.setItem(LANGUAGE_KEY, lang);
  } catch (e) {
    console.error('Erro ao salvar preferência de idioma:', e);
  }
}

export function saveActiveSession(attempt: ExamAttempt): void {
  if (!isClient()) return;
  try {
    const key = `${ACTIVE_SESSION_PREFIX}${attempt.examId}`;
    localStorage.setItem(key, JSON.stringify(attempt));
  } catch (e) {
    console.error('Erro ao salvar sessão ativa no localStorage:', e);
  }
}

export function getActiveSession(examId: string): ExamAttempt | null {
  if (!isClient() || !examId) return null;
  try {
    const key = `${ACTIVE_SESSION_PREFIX}${examId}`;
    const data = localStorage.getItem(key);
    if (!data) return null;
    return JSON.parse(data) as ExamAttempt;
  } catch (e) {
    console.error('Erro ao carregar sessão ativa do localStorage:', e);
    return null;
  }
}

export function clearActiveSession(examId: string): void {
  if (!isClient() || !examId) return;
  try {
    const key = `${ACTIVE_SESSION_PREFIX}${examId}`;
    localStorage.removeItem(key);
  } catch (e) {
    console.error('Erro ao remover sessão ativa do localStorage:', e);
  }
}

export function saveCompletedAttempt(attempt: ExamAttempt): void {
  if (!isClient()) return;
  try {
    const attempts = getAllAttempts();
    // Adiciona no início da lista
    const updated = [attempt, ...attempts.filter((a) => a.id !== attempt.id)];
    localStorage.setItem(ATTEMPTS_KEY, JSON.stringify(updated));
    // Limpa a sessão ativa pendente desse exame
    clearActiveSession(attempt.examId);
  } catch (e) {
    console.error('Erro ao salvar histórico de tentativa:', e);
  }
}

export function getAllAttempts(): ExamAttempt[] {
  if (!isClient()) return [];
  try {
    const data = localStorage.getItem(ATTEMPTS_KEY);
    if (!data) return [];
    return JSON.parse(data) as ExamAttempt[];
  } catch (e) {
    console.error('Erro ao buscar tentativas:', e);
    return [];
  }
}

export function getAttemptById(attemptId: string): ExamAttempt | null {
  if (!isClient() || !attemptId) return null;
  const attempts = getAllAttempts();
  return attempts.find((a) => a.id === attemptId) || null;
}

export function getAttemptsByExamId(examId: string): ExamAttempt[] {
  if (!isClient() || !examId) return [];
  const attempts = getAllAttempts();
  return attempts.filter((a) => a.examId.toUpperCase() === examId.toUpperCase());
}

export function deleteAttempt(attemptId: string): void {
  if (!isClient() || !attemptId) return;
  try {
    const attempts = getAllAttempts().filter((a) => a.id !== attemptId);
    localStorage.setItem(ATTEMPTS_KEY, JSON.stringify(attempts));
  } catch (e) {
    console.error('Erro ao deletar tentativa:', e);
  }
}

export function getThemePreference(): ExamTheme {
  if (!isClient()) return 'aws-modern';
  try {
    const saved = localStorage.getItem(THEME_KEY) as ExamTheme;
    return saved === 'pearson-vue' ? 'pearson-vue' : 'aws-modern';
  } catch {
    return 'aws-modern';
  }
}

export function setThemePreference(theme: ExamTheme): void {
  if (!isClient()) return;
  try {
    localStorage.setItem(THEME_KEY, theme);
  } catch (e) {
    console.error('Erro ao salvar preferência de tema:', e);
  }
}
