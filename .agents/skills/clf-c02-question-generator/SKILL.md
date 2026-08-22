---
name: clf-c02-question-generator
description: >-
  Generates high-quality, realistic AWS Certified Cloud Practitioner (CLF-C02)
  exam questions in JSON format (for the aws-exam-simulator) or Markdown format (for Obsidian study notes).
  Explores ANY foundational topic, service, or concept that can appear on the official CLF-C02 exam across
  all 4 domains, ensuring strictly shuffled answer distributions (never fixed to options A or B).
---

# AWS CLF-C02 Exam Question Generator Skill

This skill guides the creation and validation of exam-grade questions for the **AWS Certified Cloud Practitioner (CLF-C02)** certification.

---

## 🎯 Scope & Core Principles

1. **Broad & Unrestricted Exam Coverage**:
   - The generator covers **ANY topic, service, definition, or concept** on the official CLF-C02 blueprint across all 4 domains.
   - It explores core cloud computing advantages, the AWS Shared Responsibility Model, IAM fundamentals, basic security tools (Artifact, Shield, WAF, KMS), global infrastructure (Regions, AZs, Edge Locations), core AWS services (EC2, S3, RDS, DynamoDB, VPC, CloudWatch, CloudTrail), the 6 pillars of the Well-Architected Framework, pricing models, and AWS Support plans.
2. **100% Inéditas (Original Foundational Questions)**:
   - Fresh, realistic foundational scenarios and direct conceptual inquiries mirroring the official AWS CLF-C02 exam.
3. **Engenharia de Distratores Plausíveis (ZERO Alternativas Absurdas)**:
   - **PROIBIDO**: Distratores inventados, termos inexistentes no ecossistema AWS ou respostas ambíguas.
   - **OBRIGATÓRIO**: Todas as 4 alternativas (ou 5 em múltipla escolha) **DEVEM representar termos, serviços ou conceitos reais da AWS**, mas apenas a correta responde perfeitamente à definição ou requisito da questão.
   - **Simetria Estrutural e de Extensão**: Todas as opções devem ter extensão e formato semelhantes (1 a 3 frases claras).
4. **Regra Obrigatória de Embaralhamento de Gabaritos (Strict Answer Shuffling)**:
   - **NUNCA** posicione a resposta correta sempre na opção `A` ou nas opções `A` e `B`.
   - As respostas corretas **DEVEM** ser distribuídas de forma balanceada e pseudo-aleatória entre todas as opções (`A`, `B`, `C`, `D` para escolha única; pares variados como `["B", "D"]`, `["A", "C"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]` para múltipla escolha).
   - Em um lote ou simulado completo, a distribuição de gabaritos individuais deve ser equilibrada (~25% para cada letra).

---

## 🧭 Workflow

Follow these steps to produce high-fidelity CLF-C02 questions:

### Step 1: Determine the Target Domain, Format, and Time Limit
- **Domain Distribution** (Official CLF-C02 Blueprint):
  - **Domain 1**: Cloud Concepts (24%)
  - **Domain 2**: Security and Compliance (30%)
  - **Domain 3**: Cloud Technology and Services (34%)
  - **Domain 4**: Billing, Pricing, and Support (12%)
- **Time Calculation Rule (83 seconds / ~1.38 min per question)**:
  - Base pace: **83 seconds (~1 min 23 sec)** per question (90 min / 65 questions).
  - Formula: $\text{timeLimitMinutes} = \text{round}\left( \frac{N \times 83}{60} \right)$
  - Examples:
    - 25 questions = **35 minutos**.
    - 50 questions = **69 minutos**.
    - 65 questions = **90 minutos**.
- **Target Output Format**:
  - **JSON**: Integration into `src/data/exams/*.json` (see [templates/simulator_question.json](./templates/simulator_question.json)).
  - **Markdown**: Formatted for Obsidian study vaults (see [templates/obsidian_question.md](./templates/obsidian_question.md)).
  - **Bilingual Support**: Portuguese (PT-BR) with standard AWS English terminology, or English, based on user preference.

### Step 2: Consult Technical References
Review domain references and foundational concepts:
- [Question Crafting Rules & Anatomy](./references/question_crafting_rules.md)
- [Foundational Traps, Distinctions & Confusions](./references/gap_analysis_and_traps.md)
- [Exam Blueprint & Task Statements](./references/exam_blueprint.md)
- [Domain 1 Reference: Cloud Concepts](./references/domain_1_cloud_concepts.md)
- [Domain 2 Reference: Security and Compliance](./references/domain_2_security_compliance.md)
- [Domain 3 Reference: Cloud Technology & Services](./references/domain_3_cloud_technology_services.md)
- [Domain 4 Reference: Billing, Pricing, and Support](./references/domain_4_billing_pricing_support.md)

### Step 3: Craft the Question Anatomy
Every question **MUST** reflect practitioner-grade precision:
1. **Clear Statement (1-2 sentences)**: Focused on service identification, definition, Shared Responsibility Model boundary, Well-Architected pillar, billing feature, or support plan tier.
2. **Decision Trigger**:
   - *"Qual serviço da AWS deve ser usado para..."*
   - *"De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual é uma responsabilidade do cliente?"*
   - *"Qual pilar do AWS Well-Architected Framework se concentra em..."*
   - *"Qual plano de suporte da AWS oferece acesso 24/7 a Engenheiros de Suporte em Nuvem e um Technical Account Manager (TAM) dedicado?"*
3. **Plausible Distractor Engineering**:
   - Utilize serviços e termos reais da AWS que candidatos frequentemente confundem (ex: CloudWatch vs CloudTrail; Artifact vs Shield; S3 Standard vs S3 Glacier; Cost Explorer vs Budgets).
   - **Shuffle the final options**: Randomly assign the correct answer(s) across different positions (e.g., Q1 -> `C`, Q2 -> `A`, Q3 -> `D`, Q4 -> `B`).

### Step 4: Write Detailed Explanations
For each option (both correct and incorrect):
- **Correct Option(s)**: Explain *why* this service, pillar, or concept directly matches the definition and official AWS best practice.
- **Incorrect Options**: Explicitly point out *what* the distractor service/concept actually does and why it does not fit the question's requirement (e.g., "Incorreto: O AWS CloudTrail registra o histórico de chamadas de API e atividades de conta para auditoria, enquanto o monitoramento de métricas e alarmes operacionais de CPU é função do Amazon CloudWatch").

### Step 5: Validate Output
- If generating JSON for the simulator, validate against the JSON schema and ensure:
  - `id`: Unique string (e.g., `clf-q066`).
  - `examId`: `"CLF-C02"` (or specific mock code).
  - `domainId`: One of `domain-1-cloud-concepts`, `domain-2-security-compliance`, `domain-3-cloud-technology-services`, `domain-4-billing-pricing-support`.
  - `services`: Array of 1-3 AWS services involved.
  - `type`: `"single"` (1 choice) or `"multiple"` (2 choices).
  - `requiredChoices`: Must match length of `correctAnswers`.
  - `correctAnswers`: Array of option IDs with shuffled letters (e.g. `["C"]` or `["A", "D"]`).
  - All options have `id`, `text`, and non-empty `explanation`.
  - `generalExplanation`: Comprehensive summary explanation.
  - `referenceUrl`: Valid AWS documentation link.
  - `difficulty`: `"easy"` or `"medium"`.

---

## 🛠️ Helper Scripts & Validation

Run the Python validation script to verify questions and answer distribution:
```bash
python3 .agents/skills/clf-c02-question-generator/scripts/validate_questions.py <path_to_json_file>
```
Or test the entire exam simulator bank:
```bash
npm run validate:exams
```
