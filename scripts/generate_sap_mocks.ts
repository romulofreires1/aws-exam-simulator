import fs from 'fs';
import path from 'path';

// Configurações
const OBSIDIAN_DIR = '/home/romulofreires/MEGA/obsidian/Geral/Arquitetura de Soluções/SAP/certified-aws-solutions-architect-professional';
const EXAMS_DIR = path.join(__dirname, '../src/data/exams');
const API_KEY = process.env.GEMINI_API_KEY;
const MODEL = 'gemini-2.5-pro';
const QUESTIONS_PER_SIM = 25;
const SIM_COUNT = 3;

if (!API_KEY) {
  console.error('ERRO: Defina a variável de ambiente GEMINI_API_KEY antes de rodar o script.');
  process.exit(1);
}

// 1. Ler os arquivos do Obsidian recursivamente para buscar inspiração
function getObsidianNotes(dirPath: string): string[] {
  let notes: string[] = [];
  if (!fs.existsSync(dirPath)) return notes;
  
  const files = fs.readdirSync(dirPath);
  for (const file of files) {
    const fullPath = path.join(dirPath, file);
    if (fs.statSync(fullPath).isDirectory()) {
      notes = notes.concat(getObsidianNotes(fullPath));
    } else if (file.endsWith('.md')) {
      notes.push(fullPath);
    }
  }
  return notes;
}

const allNotes = getObsidianNotes(OBSIDIAN_DIR);

function getRandomNotesContent(count = 3): string {
  if (allNotes.length === 0) return "Nenhuma anotação encontrada.";
  const selected = [];
  for (let i = 0; i < count; i++) {
    const randomFile = allNotes[Math.floor(Math.random() * allNotes.length)];
    const content = fs.readFileSync(randomFile, 'utf8').substring(0, 1500); // pegar apenas o início para contexto
    selected.push(`--- Nota: ${path.basename(randomFile)} ---\n${content}`);
  }
  return selected.join('\n\n');
}

// 2. Função para chamar a API do Gemini
async function generateQuestionsBatch(simId: number, batchIndex: number, batchSize: number): Promise<any[]> {
  const notesContent = getRandomNotesContent(3);
  
  const systemPrompt = `Você é um criador de questões para o exame AWS Certified Solutions Architect - Professional (SAP-C02).
Sua tarefa é gerar EXATAMENTE ${batchSize} questões em JSON.

REGRAS:
1. Dificuldade altíssima, cenários com múltiplas restrições.
2. Distratores plausíveis. Misture questões "single" (1 resp) e "multiple" (2 ou 3 resp).
3. Texto nos 3 idiomas: "en", "pt", "es".

INSPIRAÇÃO (Tópicos do aluno):
${notesContent}

O JSON deve ser estritamente um ARRAY DE OBJETOS com este schema (sem bloco de markdown em volta):
[{
  "id": "sap-sim${simId}-q${Date.now()}-${batchIndex}",
  "examId": "SAP-C02",
  "domainId": "domain-1-org-complexity",
  "services": ["Service1"],
  "type": "single",
  "requiredChoices": 1,
  "correctAnswers": ["A"],
  "difficulty": "hard",
  "translations": {
    "en": {
      "domainName": "Domain 1",
      "statement": "Question...",
      "options": [
        { "id": "A", "text": "...", "explanation": "..." },
        { "id": "B", "text": "...", "explanation": "..." },
        { "id": "C", "text": "...", "explanation": "..." },
        { "id": "D", "text": "...", "explanation": "..." }
      ],
      "generalExplanation": "..."
    },
    "pt": { ... },
    "es": { ... }
  }
}]`;

  const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${API_KEY}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ role: "user", parts: [{ text: systemPrompt }] }],
      generationConfig: { temperature: 0.7, response_mime_type: "application/json" }
    })
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`Erro na API: ${response.status} ${errText}`);
  }

  const data = await response.json();
  const rawText = data.candidates[0].content.parts[0].text;
  
  try {
    return JSON.parse(rawText);
  } catch (e) {
    console.error("Falha ao parsear JSON. Retorno da API: ", rawText.substring(0, 500));
    return [];
  }
}

async function main() {
  console.log('Iniciando geração de simulados SAP-C02 usando Gemini...');
  console.log(`Anotações em: ${OBSIDIAN_DIR}`);
  console.log(`Encontradas ${allNotes.length} anotações em markdown.`);

  for (let sim = 4; sim <= 3 + SIM_COUNT; sim++) {
    console.log(`\n=== Gerando Simulado ${sim} ===`);
    let questions: any[] = [];
    
    const batches = Math.ceil(QUESTIONS_PER_SIM / 5);
    for (let b = 0; b < batches; b++) {
      const qToGenerate = Math.min(5, QUESTIONS_PER_SIM - questions.length);
      console.log(`Gerando lote ${b + 1}/${batches} (${qToGenerate} questões)...`);
      
      try {
        const batchQs = await generateQuestionsBatch(sim, b, qToGenerate);
        questions.push(...batchQs);
        console.log(`✅ Lote ${b + 1} gerado com sucesso.`);
      } catch (error) {
        console.error(`❌ Erro no lote ${b + 1}:`, error);
        console.log("Aguardando 5s para retentar...");
        await new Promise(r => setTimeout(r, 5000));
        b--; // retry
      }
      
      await new Promise(r => setTimeout(r, 2000));
    }

    const examData = {
      id: `sap-c02-sim-${sim}`,
      name: `AWS Certified Solutions Architect - Professional (Simulado ${sim})`,
      description: "Simulado gerado por IA baseado nas anotações do Obsidian.",
      passingScore: 75,
      timeLimitMinutes: 180,
      questions: questions
    };

    const filePath = path.join(EXAMS_DIR, `sap-c02-sim-${sim}.json`);
    fs.writeFileSync(filePath, JSON.stringify(examData, null, 2), 'utf8');
    console.log(`🎉 Simulado ${sim} salvo em: ${filePath}`);
  }
}

main().catch(console.error);
