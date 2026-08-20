---
name: sap-c02-question-generator
description: >-
  Generates high-quality, realistic AWS Certified Solutions Architect - Professional (SAP-C02)
  exam questions in JSON format (for the aws-exam-simulator) or Markdown format (for Obsidian study notes).
  Use this skill whenever the user asks to create, generate, review, refine, or add SAP-C02 questions,
  mock tests, or architectural scenario problems based on AWS best practices, gap analysis, and the 4 SAP-C02 exam domains.
---

# AWS SAP-C02 Exam Question Generator Skill

This skill guides the creation and validation of exam-grade questions for the **AWS Certified Solutions Architect - Professional (SAP-C02)** certification.

---

## 🎯 When to Use This Skill

Activate this skill when:
1. The user asks to generate new SAP-C02 exam questions or question batches.
2. The user wants questions focusing on specific AWS domains, services, or gap analysis topics (e.g., IAM Identity Center ABAC, Transit Gateway Inspection VPC, Aurora Global Database, Lake Formation, AWS MGN/DMS, FinOps).
3. The user wants questions formatted for the **aws-exam-simulator** (`.json`) or **Obsidian study notes** (`.md`).
4. The user wants to review, refine, or translate existing AWS SAP-C02 questions.

---

## 🧭 Workflow

Follow these steps to produce high-fidelity SAP-C02 questions:

### Step 1: Determine the Target Scope, Format, and Time Limit
- **Domain Focus**: Identify the target SAP-C02 domain(s) or cross-domain topics:
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
  - **JSON**: Direct integration into `src/data/exams/sap-c02.json` (see [templates/simulator_question.json](./templates/simulator_question.json)).
  - **Markdown**: Formatted for Obsidian study vaults (see [templates/obsidian_question.md](./templates/obsidian_question.md)).
  - **Bilingual Support**: Questions can be generated in Portuguese (PT-BR) with standard AWS English terminology, or in English, according to user preference.

### Step 2: Consult Technical References & Gap Analysis
Before drafting the scenario, review the domain references and gap analysis to incorporate realistic enterprise patterns:
- [Question Crafting Rules & Anatomy](./references/question_crafting_rules.md)
- [Gap Analysis & High-Yield Topics](./references/gap_analysis_and_traps.md)
- [Domain 1 Reference: Organizational Complexity](./references/domain_1_org_complexity.md)
- [Domain 2 Reference: New Solutions](./references/domain_2_new_solutions.md)
- [Domain 3 Reference: Continuous Improvement](./references/domain_3_continuous_imp.md)
- [Domain 4 Reference: Migration & Modernization](./references/domain_4_migration_mod.md)

### Step 3: Craft the Question Anatomy
Every SAP-C02 question **MUST** exhibit professional-grade depth:
1. **Scenario (2-4 sentences)**: Realistic enterprise context (e.g., 200+ AWS accounts, hybrid data center, global user base, regulatory compliance, microservices architecture).
2. **Conflicting Constraints**: Establish 2 or more competing needs (e.g., strict RTO/RPO + minimal operational overhead; maximum security + no code modification; lowest egress cost + multi-VPC connectivity).
3. **Decision Criteria Trigger (The Final Prompt)**:
   - *"Qual solução atenderá a esses requisitos de forma MAIS eficiente operacionalmente?"*
   - *"Qual combinação de etapas atenderá a esses requisitos com o MENOR custo?"*
   - *"Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de manutenção e SEM alterar o código?"*
4. **Distractor Engineering**:
   - Create 4 options for single-choice (A, B, C, D) or 5-6 options for multiple-choice (A-E or A-F).
   - Distractors must NOT be obviously fake or contain fictional AWS services.
   - Each distractor must represent a real AWS pattern that is sub-optimal (e.g., violates least privilege, incurs higher operational burden, exceeds RTO, requires manual intervention, or costs more).

### Step 4: Write Detailed Explanations
For each option (both correct and incorrect):
- **Correct Option(s)**: Explain *why* this architecture satisfies all constraints and the specific optimization criteria (Well-Architected Framework justification).
- **Incorrect Options**: Explicitly point out *why* each distractor is wrong, insufficient, or sub-optimal (e.g., "Incorreto: Peering de VPC não suporta roteamento transitivo", "Incorreto: Exige sobrecarga operacional manual", "Incorreto: RPO de 1 hora viola o requisito de RPO < 1 minuto").

### Step 5: Validate Output
- If generating JSON for the simulator, validate against the JSON schema and ensure:
  - `id`: Unique string (e.g., `sap-q076`).
  - `examId`: `"SAP-C02"`.
  - `domainId`: One of `domain-1-org-complexity`, `domain-2-new-solutions`, `domain-3-continuous-improvement`, `domain-4-migration-modernization`.
  - `services`: Array of 2-5 AWS services involved.
  - `type`: `"single"` (1 choice) or `"multiple"` (2-3 choices).
  - `requiredChoices`: Must match length of `correctAnswers`.
  - `correctAnswers`: Array of option IDs (e.g. `["A"]` or `["A", "C"]`).
  - All options have `id`, `text`, and non-empty `explanation`.
  - `generalExplanation`: Comprehensive summary explanation.
  - `referenceUrl`: Valid AWS documentation link.
  - `difficulty`: `"hard"` or `"medium"`.

---

## 🛠️ Helper Scripts & Validation

You can run the Python validation script to verify questions before saving:
```bash
python3 .agents/skills/sap-c02-question-generator/scripts/validate_questions.py <path_to_json_file>
```
Or test the exam simulator bank:
```bash
npm run validate:exams
```
