# 🤖 Template de Prompt para IA Gerar Novos Simulados AWS

Copie e cole o prompt abaixo em qualquer IA (ChatGPT, Claude, Gemini, etc.) para gerar um novo simulado pronto para inclusão no projeto:

---

```markdown
Por favor, gere um banco de questões para a certificação AWS **[SUBSTITUA PELO CÓDIGO DA CERTIFICAÇÃO, ex: DVA-C02 ou ANS-C01]** seguindo rigorosamente o esquema JSON abaixo.

### Regras Obrigatórias:
1. Respeite os Domínios oficiais da prova AWS e seus pesos aproximados.
2. Cada questão deve ter:
   - `id`: único (ex: "dva-q001")
   - `type`: "single" (1 resposta correta) ou "multiple" (2 ou mais corretas)
   - `requiredChoices`: 1 para single, ou o número exato de opções que o candidato deve selecionar (ex: 2 para "Choose TWO")
   - `statement`: Enunciado detalhado em formato de cenário realista de arquitetura/desenvolvimento AWS. Se for de múltipla resposta, termine o enunciado com "(Choose TWO.)" ou "(Choose THREE.)".
   - `options`: Lista com id ("A", "B", "C", "D", "E"), text da alternativa e explanation explicando detalhadamente o porquê de estar certa ou errada.
   - `correctAnswers`: Array com as letras corretas, ex: ["A"] ou ["B", "D"].
   - `generalExplanation`: Resumo da solução ideal e boas práticas do Well-Architected Framework.
   - `referenceUrl`: Link oficial da documentação da AWS sobre o serviço abordado.
   - `services`: Lista dos serviços AWS envolvidos (ex: ["DynamoDB", "Lambda"]).
   - `difficulty`: "easy", "medium" ou "hard".

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
  "icon": "aws-service-ou-shield",
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
      "statement": "A developer is designing an application that receives high-frequency IoT sensor telemetry...",
      "options": [
        {
          "id": "A",
          "text": "Use Amazon DynamoDB with auto-scaling enabled and partition key on device_id...",
          "explanation": "Correto: DynamoDB escala horizontalmente e distribui a carga de escrita com boa chave de partição."
        },
        {
          "id": "B",
          "text": "Write data directly to Amazon RDS MySQL Single-AZ...",
          "explanation": "Incorreto: RDS MySQL Single-AZ não possui a escalabilidade elástica necessária para picos de telemetria IoT."
        },
        {
          "id": "C",
          "text": "Store messages in AWS SQS FIFO queue with default throughput...",
          "explanation": "Incorreto: SQS FIFO possui limites estritos de TPS que podem causar gargalo sem batching/high-throughput."
        },
        {
          "id": "D",
          "text": "Save data in Amazon EFS mount target...",
          "explanation": "Incorreto: EFS não é o banco de dados orientado para telemetria de sensores."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "Amazon DynamoDB é a solução serverless recomendada para ingestão e consulta de dados de telemetria em alta escala.",
      "referenceUrl": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html",
      "difficulty": "medium"
    }
  ]
}
```
---

### Como Adicionar ao Projeto após Gerado:
1. Salve o JSON retornado em `src/data/exams/[codigo-do-exame].json` (ex: `src/data/exams/dva-c02.json`).
2. Execute o validador para garantir integridade:
   ```bash
   npm run validate:exams
   ```
3. Faça o commit e push:
   ```bash
   git add src/data/exams/dva-c02.json
   git commit -m "feat(exams): add DVA-C02 exam simulator"
   git push origin main
   ```
Pronto! O novo simulado aparecerá automaticamente no catálogo da aplicação.
