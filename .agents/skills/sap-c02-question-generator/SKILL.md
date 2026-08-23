---
name: sap-c02-question-generator
description: >-
  Generates high-quality, realistic AWS Certified Solutions Architect - Professional (SAP-C02)
  exam questions in JSON format (for the aws-exam-simulator) or Markdown format (for Obsidian study notes).
  Explores ANY topic, service, or architectural scenario that can appear on the official SAP-C02 exam across
  all 4 domains, ensuring strictly shuffled answer distributions (never fixed to options A or B).
---

# AWS SAP-C02 Exam Question Generator Skill

This skill guides the creation and validation of exam-grade questions for the **AWS Certified Solutions Architect - Professional (SAP-C02)** certification.

---

## 🎯 Scope & Core Principles

1. **Broad & Unrestricted Exam Coverage**:
   - The generator covers **ANY topic, service, challenge, or scenario** that can be assessed on the official SAP-C02 exam blueprint across all 4 domains.
   - It is **NOT** restricted to any specific folder, past gaps list, or external subset. It explores the entire breadth of AWS enterprise architectures (hybrid networking, IAM/governance multi-account, resilience/DR, analytics/data lakes, cost optimization, migration 7 Rs, container & serverless modernizations, etc.).
2. **100% Inéditas (Original Enterprise Scenarios)**:
   - All questions feature fresh, realistic enterprise scenarios (fintechs, streaming OTT, global retail, healthcare compliance, autonomous vehicles, genomic pipelines, industrial IoT, telecom, SaaS multi-tenant).
3. **Engenharia Rigorosa de Distratores Altamente Plausíveis (ZERO Alternativas Óbvias)**:
   - **PROIBIDO**: Distratores obviamente errados, ingênuos, curtos ou contendo serviços/scripts absurdos.
   - **OBRIGATÓRIO**: Todas as 4 alternativas (ou 5/6 em múltipla escolha) **DEVEM parecer soluções 100% profissionais, válidas, modernas e viáveis tecnicamente**.
   - **Matriz de Decisão 2x2**: Estruture as opções em pares conceituais (ex: 2 opções usam Abordagem A e 2 usam Abordagem B; uma acerta a nuance técnica exata e as outras falham por sutilezas como sobrecarga operacional, custo desnecessário, ou limites não-transitivos da AWS).
   - **Simetria Estrutural e de Extensão**: Todas as alternativas devem ter comprimento similar (3 a 5 linhas cada) e mesmo nível de detalhamento técnico passo a passo.
4. **Regra Obrigatória de Embaralhamento de Gabaritos (Strict Answer Shuffling)**:
   - **NUNCA** posicione a resposta correta sempre na opção `A` ou nas opções `A` e `B`.
   - As respostas corretas **DEVEM** ser distribuídas de forma balanceada e pseudo-aleatória entre todas as opções (`A`, `B`, `C`, `D` para escolha única; combinações variadas como `["B", "D"]`, `["A", "C"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]` para múltipla escolha).
   - Em um lote ou simulado completo, a distribuição de gabaritos individuais deve ser equilibrada (~25% para cada letra).

---

## 🧭 Workflow

Follow these steps to produce high-fidelity SAP-C02 questions:

### Step 1: Determine the Target Domain, Format, and Time Limit
- **Domain Distribution** (Official SAP-C02 Blueprint):
  - **Domain 1**: Design Solutions for Organizational Complexity (26%)
  - **Domain 2**: Design for New Solutions (29%)
  - **Domain 3**: Continuous Improvement for Existing Solutions (25%)
  - **Domain 4**: Accelerate Workload Migration and Modernization (20%)
- **Time Calculation Rule (2m 56s per question)**:
  - Base pace: **176 seconds (2 min 56 sec)** per question (220 min / 75 questions).
  - Formula: $\text{timeLimitMinutes} = \text{round}\left( \frac{N \times 176}{60} \right)$
  - Examples:
    - 25 questions = $\approx$ **73 minutos** (ou 74 min).
    - 50 questions = $\approx$ **147 minutos**.
    - 75 questions = **220 minutos**.
- **Target Output Format**:
  - **JSON**: Integration into `src/data/exams/*.json` (see [templates/simulator_question.json](./templates/simulator_question.json)).
  - **Markdown**: Formatted for Obsidian study vaults (see [templates/obsidian_question.md](./templates/obsidian_question.md)).
  - **Bilingual Support**: Portuguese (PT-BR) with standard AWS English terminology, or English, based on user preference.

### Step 2: Consult Technical References
Review domain references and enterprise architecture patterns:
- [Question Crafting Rules & Anatomy](./references/question_crafting_rules.md)
- [Enterprise Architectures, Trade-offs & Traps](./references/gap_analysis_and_traps.md)
- [Exam Blueprint & Task Statements](./references/exam_blueprint.md)
- [Domain 1 Reference: Organizational Complexity](./references/domain_1_org_complexity.md)
- [Domain 2 Reference: New Solutions](./references/domain_2_new_solutions.md)
- [Domain 3 Reference: Continuous Improvement](./references/domain_3_continuous_imp.md)
- [Domain 4 Reference: Migration & Modernization](./references/domain_4_migration_mod.md)

### Step 3: Craft the Question Anatomy
Every question **MUST** exhibit professional-grade depth:
1. **Scenario (2-4 sentences)**: Realistic enterprise context (e.g., 200+ AWS accounts, hybrid data center, global user base, regulatory compliance, microservices architecture).
2. **Conflicting Constraints**: Establish 2 or more competing needs (e.g., strict RTO/RPO + minimal operational overhead; maximum security + no code modification; lowest egress cost + multi-VPC connectivity).
3. **Decision Criteria Trigger (Final Prompt)**:
   - *"Qual solução atenderá a esses requisitos de forma MAIS eficiente operacionalmente?"*
   - *"Qual combinação de etapas atenderá a esses requisitos com o MENOR custo?"*
   - *"Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de manutenção e SEM alterar o código?"*
4. **High-Fidelity Distractor Engineering (Engenharia de Distratores Plausíveis)**:
   - **Apply the 2x2 Decision Matrix**: Provide 2 competing architectural approaches (2 options for Approach 1, 2 options for Approach 2).
   - In each approach, design real, multi-step technical steps (3-5 lines per option) with matching terminology.
   - Distractors must fail purely on subtle constraints:
     - *Nuance Trap*: Misses a non-obvious technical limit (e.g., Appliance Mode missing on Transit Gateway VPC attachment; S3 Batch Replication omitted for existing objects; SCP applied to Management Account).
     - *Overhead Trap*: Works, but introduces custom scripts, Lambda orchestrators, or manual tasks where a managed AWS capability exists.
     - *Cost/Over-Engineering Trap*: Highly resilient and functional, but unnecessarily expensive for the specified RTO/RPO.
     - *Compliance/Scope Trap*: Satisfies the main technical flow, but leaves a specific security requirement unaddressed.
   - **Shuffle the final options**: Randomly assign the correct answer(s) across different positions (e.g., Q1 -> `C`, Q2 -> `A`, Q3 -> `D`, Q4 -> `B`, Q5 -> `["B", "D"]`, Q6 -> `["A", "E"]`).

### Step 4: Write Detailed Explanations
For each option (both correct and incorrect):
- **Correct Option(s)**: Explain *why* this architecture satisfies all constraints and the specific optimization criteria (Well-Architected Framework justification).
- **Incorrect Options**: Explicitly point out *why* each distractor is wrong or sub-optimal with deep technical rigor (e.g., "Incorreto: Embora o AWS Network Firewall seja a escolha correta, a falta do Appliance Mode no TGW attachment causa roteamento assimétrico e descarte de pacotes com estado").

### Step 5: Validate Output
- If generating JSON for the simulator, validate against the JSON schema and ensure:
  - `id`: Unique string (e.g., `sap-q076`).
  - `examId`: `"SAP-C02"` (or specific mock code).
  - `domainId`: One of `domain-1-org-complexity`, `domain-2-new-solutions`, `domain-3-continuous-improvement`, `domain-4-migration-modernization`.
  - `services`: Array of 2-5 AWS services involved.
  - `type`: `"single"` (1 choice) or `"multiple"` (2-3 choices).
  - `requiredChoices`: Must match length of `correctAnswers`.
  - `correctAnswers`: Array of option IDs with shuffled letters (e.g. `["C"]` or `["B", "D"]`).
  - All options have `id`, `text`, and non-empty `explanation`.
  - `generalExplanation`: Comprehensive summary explanation.
  - `referenceUrl`: Valid AWS documentation link.
  - `difficulty`: `"hard"` or `"medium"`.
  - `translations`: Complete and independent localized content for `"en"`, `"pt"` (PT-BR), and `"es"` (ES) with zero mixed/hybrid text. Each locale must contain `domainName`, `statement`, `options` (with `id`, `text`, `explanation`), and `generalExplanation`.

---

## 🛠️ Helper Scripts & Validation

Run the Python validation script to verify questions and answer distribution:
```bash
python3 .agents/skills/sap-c02-question-generator/scripts/validate_questions.py <path_to_json_file>
```
Or test the entire exam simulator bank:
```bash
npm run validate:exams
```
