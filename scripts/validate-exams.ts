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
    return { isValid: false, errors: [`Não foi possível ler o arquivo: ${(err as Error).message}`], stats: { totalQuestions: 0, domainsCount: 0 } };
  }

  let exam: ExamDefinition;
  try {
    exam = JSON.parse(content);
  } catch (err) {
    return { isValid: false, errors: [`JSON Inválido: ${(err as Error).message}`], stats: { totalQuestions: 0, domainsCount: 0 } };
  }

  // Valida campos obrigatórios no nível do exame
  if (!exam.id) errors.push(`[${fileName}] Campo 'id' é obrigatório.`);
  if (!exam.title) errors.push(`[${fileName}] Campo 'title' é obrigatório.`);
  if (!exam.code) errors.push(`[${fileName}] Campo 'code' é obrigatório.`);
  if (!['Foundational', 'Associate', 'Professional', 'Specialty'].includes(exam.category)) {
    errors.push(`[${fileName}] Campo 'category' inválido: '${exam.category}'. Valores permitidos: Foundational, Associate, Professional, Specialty.`);
  }
  if (!exam.description) errors.push(`[${fileName}] Campo 'description' é obrigatório.`);
  if (typeof exam.timeLimitMinutes !== 'number' || exam.timeLimitMinutes <= 0) {
    errors.push(`[${fileName}] Campo 'timeLimitMinutes' deve ser um número positivo.`);
  }
  if (typeof exam.passingScore !== 'number' || exam.passingScore < 100 || exam.passingScore > 1000) {
    errors.push(`[${fileName}] Campo 'passingScore' deve ser um número entre 100 e 1000.`);
  }

  // Validação de domínios
  if (!Array.isArray(exam.domains) || exam.domains.length === 0) {
    errors.push(`[${fileName}] 'domains' deve ser um array com pelo menos 1 domínio.`);
  }

  const validDomainIds = new Set<string>();
  if (Array.isArray(exam.domains)) {
    for (let i = 0; i < exam.domains.length; i++) {
      const d = exam.domains[i];
      if (!d.id) errors.push(`[${fileName}] Domínio na posição ${i} não possui 'id'.`);
      if (!d.name) errors.push(`[${fileName}] Domínio '${d.id || i}' não possui 'name'.`);
      if (d.id) validDomainIds.add(d.id);
    }
  }

  // Validação de questões
  if (!Array.isArray(exam.questions) || exam.questions.length === 0) {
    errors.push(`[${fileName}] 'questions' deve ser um array com pelo menos 1 questão.`);
  }

  const questionIds = new Set<string>();

  if (Array.isArray(exam.questions)) {
    exam.questions.forEach((q, idx) => {
      const qPrefix = `[${fileName} > Questão #${idx + 1} (${q.id || 'sem id'})]`;

      if (!q.id) {
        errors.push(`${qPrefix} 'id' é obrigatório.`);
      } else {
        if (questionIds.has(q.id)) {
          errors.push(`${qPrefix} ID '${q.id}' está duplicado no simulado.`);
        }
        questionIds.add(q.id);
      }

      if (!['single', 'multiple'].includes(q.type)) {
        errors.push(`${qPrefix} 'type' deve ser 'single' ou 'multiple' (valor atual: '${q.type}').`);
      }

      if (typeof q.requiredChoices !== 'number' || q.requiredChoices < 1) {
        errors.push(`${qPrefix} 'requiredChoices' deve ser um número >= 1.`);
      }

      if (q.type === 'single' && q.requiredChoices !== 1) {
        errors.push(`${qPrefix} Questão do tipo 'single' deve ter requiredChoices = 1.`);
      }

      if (q.type === 'multiple' && q.requiredChoices < 2) {
        errors.push(`${qPrefix} Questão do tipo 'multiple' deve ter requiredChoices >= 2.`);
      }

      if (!q.domainId || !validDomainIds.has(q.domainId)) {
        errors.push(`${qPrefix} 'domainId' ('${q.domainId}') não encontrado na lista de domínios declarada.`);
      }

      if (!q.statement || q.statement.trim().length === 0) {
        errors.push(`${qPrefix} 'statement' (enunciado) não pode ser vazio.`);
      }

      if (!Array.isArray(q.options) || q.options.length < 2) {
        errors.push(`${qPrefix} 'options' deve ter pelo menos 2 alternativas.`);
      } else {
        const optionIds = new Set<string>();
        q.options.forEach((opt, optIdx) => {
          if (!opt.id) errors.push(`${qPrefix} Alternativa #${optIdx + 1} não possui 'id'.`);
          if (optionIds.has(opt.id)) errors.push(`${qPrefix} Alternativa com id '${opt.id}' duplicada.`);
          optionIds.add(opt.id);

          if (!opt.text || opt.text.trim().length === 0) {
            errors.push(`${qPrefix} Alternativa '${opt.id}' está com 'text' vazio.`);
          }
        });

        if (!Array.isArray(q.correctAnswers) || q.correctAnswers.length === 0) {
          errors.push(`${qPrefix} 'correctAnswers' deve ser um array com pelo menos 1 resposta correta.`);
        } else {
          if (q.correctAnswers.length !== q.requiredChoices) {
            errors.push(`${qPrefix} Quantidade de 'correctAnswers' (${q.correctAnswers.length}) não bate com 'requiredChoices' (${q.requiredChoices}).`);
          }

          q.correctAnswers.forEach((ans) => {
            if (!optionIds.has(ans)) {
              errors.push(`${qPrefix} Resposta correta '${ans}' não existe entre as alternativas disponíveis (${Array.from(optionIds).join(', ')}).`);
            }
          });
        }
      }

      if (!q.generalExplanation || q.generalExplanation.trim().length === 0) {
        errors.push(`${qPrefix} 'generalExplanation' não pode ser vazio.`);
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
  console.log('🔍 Validando bancos de questões em:', EXAMS_DIR);
  console.log('--------------------------------------------------');

  if (!fs.existsSync(EXAMS_DIR)) {
    console.error(`❌ Diretório ${EXAMS_DIR} não encontrado.`);
    process.exit(1);
  }

  const files = fs.readdirSync(EXAMS_DIR).filter((f) => f.endsWith('.json') && !f.startsWith('_'));

  if (files.length === 0) {
    console.warn('⚠️  Nenhum arquivo de simulado (.json) encontrado para validar.');
    process.exit(0);
  }

  let hasErrors = false;

  for (const file of files) {
    const fullPath = path.join(EXAMS_DIR, file);
    const result = validateExamFile(fullPath);

    if (result.isValid) {
      console.log(`✅ [OK] ${file} - ${result.stats.totalQuestions} questões | ${result.stats.domainsCount} domínios`);
    } else {
      hasErrors = true;
      console.error(`❌ [ERRO] ${file} possui os seguintes problemas:`);
      result.errors.forEach((err) => console.error(`   - ${err}`));
      console.log('');
    }
  }

  console.log('--------------------------------------------------');
  if (hasErrors) {
    console.error('❌ Falha na validação de simulados. Corrija os erros acima.');
    process.exit(1);
  } else {
    console.log('🎉 Todos os simulados estão válidos e prontos para uso!');
  }
}

runValidation();
