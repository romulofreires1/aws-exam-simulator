# 🤖 Template de Prompt para IA Gerar Novos Simulados AWS

Copie e cole o prompt abaixo em qualquer IA (ChatGPT, Claude, Gemini, etc.) para gerar um novo simulado pronto para inclusão no projeto.

> 💡 **Dica**: Para gerar questões com os prompts e regras mais avançados do repositório, consulte também as **Agent Skills** especializadas em [`.agents/skills/`](skills/):
> - [CLF-C02 Question Generator](skills/clf-c02-question-generator/SKILL.md)
> - [SAA-C03 Question Generator](skills/saa-c03-question-generator/SKILL.md)
> - [SAP-C02 Question Generator](skills/sap-c02-question-generator/SKILL.md)

---

```markdown
Por favor, gere um banco de questões para a certificação AWS **[SUBSTITUA PELO CÓDIGO DA CERTIFICAÇÃO, ex: DVA-C02 ou ANS-C01]** seguindo rigorosamente as diretrizes e o esquema JSON abaixo.

### Diretrizes Obrigatórias de Engenharia de Questões:
1. **Domínios Oficiais**: Respeite os Domínios oficiais do blueprint da AWS e seus respectivos pesos percentuais.
2. **Matriz de Decisão 2x2 & Distratores Altamente Plausíveis**:
   - NÃO crie alternativas ingênuas, absurdas ou obviamente incorretas.
   - Todas as opções DEVEM descrever soluções técnicas válidas e profissionais no ecossistema AWS.
   - Os distratores devem falhar apenas em restrições sutis do cenário (ex: custo excessivo, sobrecarga operacional, falta de tolerância a falhas multi-AZ, ou limites específicos de serviços).
3. **Embaralhamento Rigoroso de Gabaritos**:
   - NUNCA concentre respostas certas na letra A ou nas letras A/B.
   - Distribua as respostas uniformemente entre as opções (A, B, C, D para single; combinações variadas como B/D, A/C, C/E para multiple).
4. **Campos da Questão**:
   - `id`: único (ex: "dva-q001")
   - `type`: "single" (1 correta) ou "multiple" (2 ou mais corretas)
   - `requiredChoices`: 1 para single, ou o número exato de opções exigidas (ex: 2 para "(Choose TWO.)")
   - `statement`: Enunciado com cenário empresarial realista. Se for de múltipla resposta, inclua "(Choose TWO.)" ou "(Choose THREE.)" no final.
   - `options`: Array de opções com `id` ("A", "B", "C", "D", "E"), `text` detalhado e `explanation` justificando tecnicamente o porquê de estar certa ou errada.
   - `correctAnswers`: Array com as letras corretas, ex: `["C"]` ou `["B", "D"]`.
   - `generalExplanation`: Síntese da arquitetura recomendada baseada no AWS Well-Architected Framework.
   - `referenceUrl`: Link oficial da documentação da AWS.
   - `services`: Lista dos serviços AWS abordados (ex: `["DynamoDB", "Lambda", "API Gateway"]`).
   - `difficulty`: "easy", "medium" ou "hard".
   - `translations` *(opcional)*: Objeto com traduções localizadas para `"pt"`, `"en"` e/ou `"es"`.

### Formato JSON Esperado:
```json
{
  "id": "CODIGO-DO-EXAME",
  "title": "Nome Completo da Certificação",
  "code": "CODIGO-DO-EXAME",
  "category": "Associate", // "Foundational" | "Associate" | "Professional" | "Specialty"
  "description": "Descrição sucinta da prova e objetivos.",
  "totalQuestions": 65,
  "timeLimitMinutes": 130,
  "passingScore": 720,
  "availableLanguages": ["en", "pt", "es"],
  "defaultLanguage": "en",
  "domains": [
    {
      "id": "domain-1-development-with-aws-services",
      "name": "Domain 1: Development with AWS Services",
      "weightPercentage": 32
    },
    {
      "id": "domain-2-security",
      "name": "Domain 2: Security",
      "weightPercentage": 26
    },
    {
      "id": "domain-3-deployment",
      "name": "Domain 3: Deployment",
      "weightPercentage": 24
    },
    {
      "id": "domain-4-troubleshooting-and-optimization",
      "name": "Domain 4: Troubleshooting and Optimization",
      "weightPercentage": 18
    }
  ],
  "questions": [
    {
      "id": "dva-q001",
      "examId": "DVA-C02",
      "domainId": "domain-1-development-with-aws-services",
      "domainName": "Domain 1: Development with AWS Services",
      "services": ["DynamoDB", "Lambda"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "A company is designing a high-throughput microservice backend to ingest telemetry data from millions of connected smart devices...",
      "options": [
        {
          "id": "A",
          "text": "Buffer raw telemetry payloads into Amazon SQS Standard and write batch records to Amazon RDS MySQL Single-AZ...",
          "explanation": "Incorrect: RDS Single-AZ introduces a database write bottleneck and single point of failure under peak ingestion."
        },
        {
          "id": "B",
          "text": "Mount Amazon EFS Elastic Throughput onto an EC2 fleet behind an Application Load Balancer to log incoming payloads...",
          "explanation": "Incorrect: EFS file storage creates unnecessary compute fleet management overhead compared to managed serverless NoSQL."
        },
        {
          "id": "C",
          "text": "Stream incoming payloads via Amazon Kinesis Data Streams and process records using AWS Lambda into Amazon DynamoDB with on-demand capacity...",
          "explanation": "Correct: Kinesis provides elastic stream buffering, Lambda auto-scales compute, and DynamoDB on-demand seamlessly absorbs massive write bursts."
        },
        {
          "id": "D",
          "text": "Write records directly to Amazon Redshift using multi-statement transactions over an API Gateway HTTP API...",
          "explanation": "Incorrect: Amazon Redshift is optimized for analytical batch OLAP queries, not continuous single-row transaction ingestion."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "Combining Amazon Kinesis Data Streams with AWS Lambda and Amazon DynamoDB delivers a serverless, highly scalable ingestion pipeline without database bottlenecks.",
      "referenceUrl": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html",
      "difficulty": "medium"
    }
  ]
}
```
---

### Como Adicionar ao Projeto após Gerado:
1. Salve o JSON gerado em `src/data/exams/[codigo-do-exame].json` (ex: `src/data/exams/dva-c02.json`).
2. Registre o exame no array `AVAILABLE_EXAMS` em `src/data/exams/index.ts`.
3. Valide a integridade:
   ```bash
   npm run validate:exams
   ```
4. Teste o build:
   ```bash
   npm run build
   ```
5. Faça o commit e push:
   ```bash
   git add src/data/exams/
   git commit -m "feat(exams): add DVA-C02 exam simulator"
   git push origin main
   ```
Pronto! O novo simulado aparecerá automaticamente no catálogo da aplicação com contagem e filtros dinâmicos.

