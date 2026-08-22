import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const EXAMS_DIR = path.resolve(__dirname, '../src/data/exams');

interface QuestionOption {
  id: string;
  text: string;
  explanation?: string;
}

interface Question {
  id: string;
  examId?: string;
  domainId: string;
  domainName?: string;
  services?: string[];
  type: 'single' | 'multiple';
  requiredChoices: number;
  statement: string;
  options: QuestionOption[];
  correctAnswers: string[];
  generalExplanation: string;
  translations?: Record<string, any>;
  referenceUrl?: string;
  difficulty?: 'easy' | 'medium' | 'hard';
}

interface DomainDefinition {
  id: string;
  name: string;
  weightPercentage?: number;
}

interface ExamDefinition {
  id: string;
  title: string;
  code: string;
  category: 'Foundational' | 'Associate' | 'Professional' | 'Specialty';
  description: string;
  totalQuestions?: number;
  timeLimitMinutes: number;
  passingScore: number;
  availableLanguages?: string[];
  defaultLanguage?: string;
  domains: DomainDefinition[];
  questions: Question[];
}

function validateExamFile(filePath: string): { isValid: boolean; errors: string[]; stats: { totalQuestions: number; domainsCount: number } } {
  const fileName = path.basename(filePath);
  const errors: string[] = [];

  let content: string;
  try {
    content = fs.readFileSync(filePath, 'utf-8');
  } catch (err) {
    return { isValid: false, errors: [`Could not read file: ${(err as Error).message}`], stats: { totalQuestions: 0, domainsCount: 0 } };
  }

  let exam: ExamDefinition;
  try {
    exam = JSON.parse(content);
  } catch (err) {
    return { isValid: false, errors: [`Invalid JSON: ${(err as Error).message}`], stats: { totalQuestions: 0, domainsCount: 0 } };
  }

  // Validate required fields at exam level
  if (!exam.id) errors.push(`[${fileName}] Field 'id' is required.`);
  if (!exam.title) errors.push(`[${fileName}] Field 'title' is required.`);
  if (!exam.code) errors.push(`[${fileName}] Field 'code' is required.`);
  if (!['Foundational', 'Associate', 'Professional', 'Specialty'].includes(exam.category)) {
    errors.push(`[${fileName}] Invalid 'category': '${exam.category}'. Allowed values: Foundational, Associate, Professional, Specialty.`);
  }
  if (!exam.description) errors.push(`[${fileName}] Field 'description' is required.`);
  if (typeof exam.timeLimitMinutes !== 'number' || exam.timeLimitMinutes <= 0) {
    errors.push(`[${fileName}] Field 'timeLimitMinutes' must be a positive number.`);
  }
  if (typeof exam.passingScore !== 'number' || exam.passingScore < 100 || exam.passingScore > 1000) {
    errors.push(`[${fileName}] Field 'passingScore' must be a number between 100 and 1000.`);
  }

  // Domain validation
  if (!Array.isArray(exam.domains) || exam.domains.length === 0) {
    errors.push(`[${fileName}] 'domains' must be an array with at least 1 domain.`);
  }

  const validDomainIds = new Set<string>();
  if (Array.isArray(exam.domains)) {
    for (let i = 0; i < exam.domains.length; i++) {
      const d = exam.domains[i];
      if (!d.id) errors.push(`[${fileName}] Domain at position ${i} is missing 'id'.`);
      if (!d.name) errors.push(`[${fileName}] Domain '${d.id || i}' is missing 'name'.`);
      if (d.id) validDomainIds.add(d.id);
    }
  }

  // Question validation
  if (!Array.isArray(exam.questions) || exam.questions.length === 0) {
    errors.push(`[${fileName}] 'questions' must be an array with at least 1 question.`);
  }

  const questionIds = new Set<string>();

  if (Array.isArray(exam.questions)) {
    exam.questions.forEach((q, idx) => {
      const qPrefix = `[${fileName} > Question #${idx + 1} (${q.id || 'no id'})]`;

      if (!q.id) {
        errors.push(`${qPrefix} 'id' is required.`);
      } else {
        if (questionIds.has(q.id)) {
          errors.push(`${qPrefix} Duplicate ID '${q.id}' found in exam.`);
        }
        questionIds.add(q.id);
      }

      if (!['single', 'multiple'].includes(q.type)) {
        errors.push(`${qPrefix} 'type' must be 'single' or 'multiple' (current value: '${q.type}').`);
      }

      if (typeof q.requiredChoices !== 'number' || q.requiredChoices < 1) {
        errors.push(`${qPrefix} 'requiredChoices' must be a number >= 1.`);
      }

      if (q.type === 'single' && q.requiredChoices !== 1) {
        errors.push(`${qPrefix} 'single' type question must have requiredChoices = 1.`);
      }

      if (q.type === 'multiple' && q.requiredChoices < 2) {
        errors.push(`${qPrefix} 'multiple' type question must have requiredChoices >= 2.`);
      }

      if (!q.domainId || !validDomainIds.has(q.domainId)) {
        errors.push(`${qPrefix} 'domainId' ('${q.domainId}') not found in declared domains list.`);
      }

      if (!q.statement || q.statement.trim().length === 0) {
        errors.push(`${qPrefix} 'statement' cannot be empty.`);
      }

      if (!Array.isArray(q.options) || q.options.length < 2) {
        errors.push(`${qPrefix} 'options' must have at least 2 choices.`);
      } else {
        const optionIds = new Set<string>();
        q.options.forEach((opt, optIdx) => {
          if (!opt.id) errors.push(`${qPrefix} Option #${optIdx + 1} is missing 'id'.`);
          if (optionIds.has(opt.id)) errors.push(`${qPrefix} Duplicate option id '${opt.id}'.`);
          optionIds.add(opt.id);

          if (!opt.text || opt.text.trim().length === 0) {
            errors.push(`${qPrefix} Option '${opt.id}' has empty 'text'.`);
          }
        });

        if (!Array.isArray(q.correctAnswers) || q.correctAnswers.length === 0) {
          errors.push(`${qPrefix} 'correctAnswers' must be an array with at least 1 correct answer.`);
        } else {
          if (q.correctAnswers.length !== q.requiredChoices) {
            errors.push(`${qPrefix} Count of 'correctAnswers' (${q.correctAnswers.length}) does not match 'requiredChoices' (${q.requiredChoices}).`);
          }

          q.correctAnswers.forEach((ans) => {
            if (!optionIds.has(ans)) {
              errors.push(`${qPrefix} Correct answer '${ans}' does not exist among available options (${Array.from(optionIds).join(', ')}).`);
            }
          });
        }
      }

      if (!q.generalExplanation || q.generalExplanation.trim().length === 0) {
        errors.push(`${qPrefix} 'generalExplanation' cannot be empty.`);
      }

      // Multi-language translation validation
      if (q.translations && typeof q.translations === 'object') {
        const allowedLanguages = ['en', 'pt', 'es'];
        const baseOptionIds = (q.options || []).map((o) => o.id);

        for (const [lang, trans] of Object.entries(q.translations)) {
          if (!allowedLanguages.includes(lang)) {
            errors.push(`${qPrefix} Unsupported translation language '${lang}'. Allowed: ${allowedLanguages.join(', ')}.`);
          }
          if (trans && typeof trans === 'object') {
            const t = trans as { statement?: string; options?: { id: string; text: string }[]; generalExplanation?: string };
            if (!t.statement || t.statement.trim().length === 0) {
              errors.push(`${qPrefix} Translation [${lang}] has empty 'statement'.`);
            }
            if (!Array.isArray(t.options) || t.options.length !== baseOptionIds.length) {
              errors.push(`${qPrefix} Translation [${lang}] 'options' count (${t.options?.length || 0}) does not match base options count (${baseOptionIds.length}).`);
            } else {
              t.options.forEach((tOpt) => {
                if (!baseOptionIds.includes(tOpt.id)) {
                  errors.push(`${qPrefix} Translation [${lang}] option '${tOpt.id}' does not match base option IDs (${baseOptionIds.join(', ')}).`);
                }
                if (!tOpt.text || tOpt.text.trim().length === 0) {
                  errors.push(`${qPrefix} Translation [${lang}] option '${tOpt.id}' has empty text.`);
                }
              });
            }
            if (!t.generalExplanation || t.generalExplanation.trim().length === 0) {
              errors.push(`${qPrefix} Translation [${lang}] has empty 'generalExplanation'.`);
            }
          }
        }
      }
    });
  }

  return {
    isValid: errors.length === 0,
    errors,
    stats: {
      totalQuestions: exam.questions?.length || 0,
      domainsCount: exam.domains?.length || 0,
    },
  };
}

function runValidation() {
  console.log('🔍 Validating exam question banks in:', EXAMS_DIR);
  console.log('--------------------------------------------------');

  if (!fs.existsSync(EXAMS_DIR)) {
    console.error(`❌ Directory ${EXAMS_DIR} not found.`);
    process.exit(1);
  }

  const files = fs.readdirSync(EXAMS_DIR).filter((f) => f.endsWith('.json') && !f.startsWith('_'));

  if (files.length === 0) {
    console.warn('⚠️  No exam (.json) files found to validate.');
    process.exit(0);
  }

  let hasErrors = false;

  for (const file of files) {
    const fullPath = path.join(EXAMS_DIR, file);
    const result = validateExamFile(fullPath);

    if (result.isValid) {
      console.log(`✅ [OK] ${file} - ${result.stats.totalQuestions} questions | ${result.stats.domainsCount} domains`);
    } else {
      hasErrors = true;
      console.error(`❌ [ERROR] ${file} has the following issues:`);
      result.errors.forEach((err) => console.error(`   - ${err}`));
      console.log('');
    }
  }

  console.log('--------------------------------------------------');
  if (hasErrors) {
    console.error('❌ Exam validation failed. Please fix the errors above.');
    process.exit(1);
  } else {
    console.log('🎉 All exams are valid and ready to use!');
  }
}

runValidation();
