---
name: saa-c03-question-generator
description: >-
  Generates high-quality, realistic AWS Certified Solutions Architect - Associate (SAA-C03)
  exam questions in JSON format (for the aws-exam-simulator) or Markdown format (for Obsidian study notes).
  Explores ANY topic, service, or architectural scenario that can appear on the official SAA-C03 exam across
  all 4 domains, ensuring strictly shuffled answer distributions (never fixed to options A or B).
---

# AWS SAA-C03 Exam Question Generator Skill

This skill guides the creation and validation of exam-grade questions for the **AWS Certified Solutions Architect - Associate (SAA-C03)** certification.

---

##  Recommended LLM Model
* **Model**: **`Model: "pro"` (Gemini 3.1 Pro / Gemini 3.7 Thinking)**
* **Rationale**: SAA-C03 requires evaluating multi-service trade-offs (operational overhead vs cost vs latency) and constructing realistic 2x2 distractor matrices where options must differ by subtle configuration parameters without introducing hallucinations.

---

##  Scope & Core Principles

1. **Broad & Unrestricted Exam Coverage**:
   - The generator covers **ANY topic, service, challenge, or scenario** that can be assessed on the official SAA-C03 exam blueprint across all 4 domains.
   - It explores core multi-tier web applications, serverless architectures, storage selection, database scaling, network isolation, security guardrails, and cost optimization according to the AWS Well-Architected Framework.
2. **100% Inditas (Original Architectural Scenarios)**:
   - All questions feature fresh, realistic scenario contexts (e-commerce platforms, media streaming, SaaS web apps, data pipelines, healthcare compliance, IoT telemetry, microservices).
3. **Engenharia Rigorosa de Distratores Plausveis (ZERO Alternativas Absurdas)**:
   - **PROIBIDO**: Distratores obviamente errados, ingnuos, curtos ou contendo servios/conceitos inventados.
   - **OBRIGATRIO**: Todas as 4 alternativas (ouem mltipla escolha) **DEVEM parecer solues viveis tecnicamente**.
   - **Matriz de Deciso 2x2**: Estruture opes em pares conceituais (ex: 2 opes usam Abordagem A e 2 usam Abordagem B; a correta atende exatamente  restrio de menor sobrecarga operacional ou menor custo, enquanto os distratores falham por sutilezas como complexidade desnecessria ou escolha incorreta de servio).
   - **Simetria Estrutural e de Extenso**: Todas as alternativas devem ter comprimento similar (15 a 35 palavras cada) e mesmo nvel de clareza tcnica.
4. **Regras Estritas de Quantidade de Alternativas e Mltipla Escolha**:
   - **Single Choice (`type: "single"`)**: Exatamente **4 opes** (`A`, `B`, `C`, `D`) e `requiredChoices: 1`.
   - **Select TWO (`type: "multiple"`)**: Exatamente **5 opes** (`A`, `B`, `C`, `D`, `E`) e `requiredChoices: 2`.
   - **Select THREE (`type: "multiple"`)**: Exatamente **6 opes** (`A`, `B`, `C`, `D`, `E`, `F`) e `requiredChoices: 3`.
   - Em simulados completos, mantenha uma quota de **15% a 20%** de questes de mltipla escolha.
5. **Regra Obrigatria de Embaralhamento de Gabaritos (Strict Answer Shuffling)**:
   - **NUNCA** posicione a resposta correta sempre na opo `A` ou nas opes `A` e `B`.
   - As respostas corretas **DEVEM** ser distribudas de forma balanceada e pseudo-aleatria entre todas as opes (`A`, `B`, `C`, `D` para escolha nica; combinaes variadas como `["B", "D"]`, `["A", "C"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]` para mltipla escolha).
   - Em um lote ou simulado completo, a distribuio de gabaritos individuais deve ser equilibrada (~25% para cada letra).

---

##  Workflow

Follow these steps to produce high-fidelity SAA-C03 questions:

### Step 1: Determine the Target Domain, Format, and Time Limit
- **Domain Distribution** (Official SAA-C03 Blueprint):
  - **Domain 1**: Design Secure Architectures (30%)
  - **Domain 2**: Design Resilient Architectures (26%)
  - **Domain 3**: Design High-Performing Architectures (24%)
  - **Domain 4**: Design Cost-Optimized Architectures (20%)
- **Time Calculation Rule (2 min per question)**:
  - Base pace: **120 seconds (2 minutes)** per question (130 min / 65 questions).
  - Formula: $\text{timeLimitMinutes} = \text{round}\left( \frac{N \times 120}{60} \right) = 2 \times N$
  - Examples:
    - 25 questions = **50 minutos**.
    - 50 questions = **100 minutos**.
    - 65 questions = **130 minutos**.
- **Target Output Format**:
  - **JSON**: Integration into `src/data/exams/*.json` (see [templates/simulator_question.json](./templates/simulator_question.json)).
  - **Markdown**: Formatted for Obsidian study vaults (see [templates/obsidian_question.md](./templates/obsidian_question.md)).
  - **Bilingual Support**: Portuguese (PT-BR) with standard AWS English terminology, or English, based on user preference.

### Step 2: Consult Technical References
Review domain references and architectural patterns:
- [Question Crafting Rules & Anatomy](./references/question_crafting_rules.md)
- [Architectural Patterns, Trade-offs & Traps](./references/gap_analysis_and_traps.md)
- [Exam Blueprint & Task Statements](./references/exam_blueprint.md)
- [Domain 1 Reference: Secure Architectures](./references/domain_1_secure_architectures.md)
- [Domain 2 Reference: Resilient Architectures](./references/domain_2_resilient_architectures.md)
- [Domain 3 Reference: High-Performing Architectures](./references/domain_3_high_perf_architectures.md)
- [Domain 4 Reference: Cost-Optimized Architectures](./references/domain_4_cost_optimized_architectures.md)

### Step 3: Craft the Question Anatomy
Every question **MUST** exhibit associate-grade depth:
1. **Scenario (1-3 sentences)**: Realistic context (e.g., a 3-tier web app on EC2 with RDS MySQL, S3 storage for user uploads, global users experiencing latency, microservices decoupled via queues).
2. **Conflicting Constraints**: Establish clear trade-offs (e.g., minimal operational overhead vs manual scripts; lowest cost vs maximum redundancy; zero application code changes vs full refactoring).
3. **Decision Criteria Trigger (Final Prompt)**:
   - *"Qual soluo atender a esses requisitos com a MENOR sobrecarga operacional?"*
   - *"Qual arquitetura atender a esses requisitos com o MENOR custo?"*
   - *"Qual combinao de etapas atender a esses requisitos de forma MAIS resiliente e SEM alterar o cdigo?"*
4. **High-Fidelity Distractor Engineering**:
   - **Apply the 2x2 Decision Matrix**: Provide 2 competing architectural approaches (e.g., CloudFront + S3 OAC vs ALB + EC2, or SQS Standard vs SQS FIFO + Lambda).
   - In each approach, design clear, realistic technical steps with matching terminology.
   - Distractors must fail purely on subtle constraints (e.g., using S3 Gateway Endpoint across regions where only Interface Endpoint / Direct Access works; using S3 Standard instead of Intelligent-Tiering for unknown access patterns; using manual Cron instead of EventBridge Scheduler).
   - **Shuffle the final options**: Randomly assign the correct answer(s) across different positions (e.g., Q1 -> `B`, Q2 -> `D`, Q3 -> `A`, Q4 -> `C`, Q5 -> `["B", "E"]`).

### Step 4: Write Detailed Explanations
For each option (both correct and incorrect):
- **Correct Option(s)**: Explain *why* this architecture satisfies all constraints and the specific optimization criteria (Well-Architected Framework justification).
- **Incorrect Options**: Explicitly point out *why* each distractor is wrong or sub-optimal with technical clarity (e.g., "Incorreto: Embora o uso de rplicas de leitura aumente a taxa de leitura, elas no fornecem failover automtico sncrono com zero perda de dados para gravaes como uma implantao Multi-AZ do RDS").

### Step 5: Validate Output
- If generating JSON for the simulator, validate against the JSON schema and ensure:
  - `id`: Unique string (e.g., `saa-q066`).
  - `examId`: `"SAA-C03"` (or specific mock code).
  - `domainId`: One of `domain-1-secure-architectures`, `domain-2-resilient-architectures`, `domain-3-high-performing-architectures`, `domain-4-cost-optimized-architectures`.
  - `services`: Array of 2-4 AWS services involved.
  - `type`: `"single"` (1 choice, exactly 4 options) or `"multiple"` (2 choices =options, 3 choices = 6 options).
  - `requiredChoices`: Must match length of `correctAnswers`.
  - `correctAnswers`: Array of option IDs with shuffled letters (e.g. `["C"]` or `["B", "D"]`).
  - All options have `id`, `text`, and non-empty `explanation`.
  - `generalExplanation`: Comprehensive summary explanation.
  - `referenceUrl`: Valid AWS documentation link.
  - `difficulty`: `"medium"` or `"hard"`.
  - `translations`: Complete and independent localized content for `"en"`, `"pt"` (PT-BR), and `"es"` (ES) with zero mixed/hybrid text. Each locale must contain `domainName`, `statement`, `options` (with `id`, `text`, `explanation`), and `generalExplanation`.

---

##  Helper Scripts & Validation

Run the Python validation script in strict mode to verify questions and answer distribution:
```bash
python3 .agents/skills/saa-c03-question-generator/scripts/validate_questions.py <path_to_json_file> --strict
```
Or test the entire exam simulator bank:
```bash
npm run validate:exams
```
