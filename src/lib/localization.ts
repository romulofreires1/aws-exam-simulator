import { Question, ExamLanguage, ExamDefinition } from '@/types/exam';

export interface LanguageMeta {
  code: ExamLanguage;
  label: string;
  nativeName: string;
  flag: string;
}

export const SUPPORTED_LANGUAGES: Record<ExamLanguage, LanguageMeta> = {
  en: {
    code: 'en',
    label: 'English',
    nativeName: 'English',
    flag: '🇺🇸',
  },
  pt: {
    code: 'pt',
    label: 'Portuguese',
    nativeName: 'Português',
    flag: '🇧🇷',
  },
  es: {
    code: 'es',
    label: 'Spanish',
    nativeName: 'Español',
    flag: '🇪🇸',
  },
};

/**
 * Returns a localized copy of a Question for the given language.
 * Falls back to base fields if no translation exists for the requested language.
 */
export function getLocalizedQuestion(question: Question, language: ExamLanguage): Question {
  if (!question) return question;

  if (question.translations && question.translations[language]) {
    const t = question.translations[language]!;
    return {
      ...question,
      domainName: t.domainName || question.domainName,
      statement: t.statement || question.statement,
      options: question.options.map((opt) => {
        const transOpt = t.options?.find((o) => o.id === opt.id);
        return {
          id: opt.id,
          text: transOpt?.text || opt.text,
          explanation: transOpt?.explanation || opt.explanation,
        };
      }),
      generalExplanation: t.generalExplanation || question.generalExplanation,
    };
  }

  return question;
}

/**
 * Detects all available languages for a given exam.
 */
export function getExamAvailableLanguages(exam: ExamDefinition): ExamLanguage[] {
  if (!exam) return ['en'];

  if (exam.availableLanguages && exam.availableLanguages.length > 0) {
    return exam.availableLanguages;
  }

  const detected = new Set<ExamLanguage>();
  const defaultLang: ExamLanguage = exam.defaultLanguage || 'pt';
  detected.add(defaultLang);

  if (Array.isArray(exam.questions)) {
    exam.questions.forEach((q) => {
      if (q.translations) {
        Object.keys(q.translations).forEach((langKey) => {
          if (langKey === 'en' || langKey === 'pt' || langKey === 'es') {
            detected.add(langKey as ExamLanguage);
          }
        });
      }
    });
  }

  return Array.from(detected);
}
