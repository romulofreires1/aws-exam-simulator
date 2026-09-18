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
2. **Mandatory Type Mix (20-25% Multiple Choice)**:
   - A realistic exam must contain **20% to 25% multiple choice questions** ("Select TWO" or "Select THREE").
   - A 25-question mock exam must contain **at least 5 multiple choice questions**.
3. **Engenharia Rigorosa de Distratores Altamente Plausíveis (ZERO Alternativas Óbvias)**:
   - **PROIBIDO**: Distratores obviamente errados, ingênuos, curtos (menos de 20 palavras) ou contendo serviços/scripts absurdos (como "criar 5000 usuários manuais" ou "fazer proxy com iptables").
   - **OBRIGATÓRIO**: Todas as alternativas **DEVEM parecer soluções 100% profissionais, válidas, modernas e viáveis tecnicamente**. Devem ter entre 25 a 45 palavras no mínimo.
   - **Matriz de Decisão 2x2 (Micro-Diff)**: Estruture as opções em pares conceituais simétricos. Duas opções devem diferir APENAS em um detalhe técnico, como nome de uma API, flag de configuração, porta ou mecanismo de permissão.
4. **Regra Obrigatória de Embaralhamento de Gabaritos (Strict Answer Shuffling)**:
   - **NUNCA** posicione a resposta correta sempre na opção `A` ou nas opções `A` e `B`.
   - As respostas corretas **DEVEM** ser distribuídas de forma balanceada e pseudo-aleatória entre todas as opções (`A`, `B`, `C`, `D` para escolha única; combinações variadas como `["B", "D"]`, `["A", "C"]`, `["C", "E"]` para múltipla escolha).

---

## 🧭 Workflow

Follow these steps to produce high-fidelity SAP-C02 questions:

### Step 1: Determine the Target Domain, Format, and Question Mix
- **Domain Distribution** (Official SAP-C02 Blueprint):
  - **Domain 1**: Design Solutions for Organizational Complexity (26%)
  - **Domain 2**: Design for New Solutions (29%)
  - **Domain 3**: Continuous Improvement for Existing Solutions (25%)
  - **Domain 4**: Accelerate Workload Migration and Modernization (20%)
- **Target Output Format**:
  - **JSON**: Integration into `src/data/exams/*.json` (see `templates/simulator_question.json`).
  - **Markdown**: Formatted for Obsidian study vaults (see `templates/obsidian_question.md`).
  - **Bilingual Support**: Portuguese (PT-BR) with standard AWS English terminology, or English, based on user preference.
- **Enforce Multiple Choice Quotas**: If generating a batch of questions, ensure at least 20-25% are `multiple` choice (with 5 options for "Select TWO" and 6 options for "Select THREE").

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
   - *"Qual combinação de etapas atenderá a esses requisitos com o MENOR custo? (Escolha duas.)"*
   - *"Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de manutenção e SEM alterar o código?"*
4. **High-Fidelity Distractor Engineering (Engenharia de Distratores Plausíveis)**:
   - **Apply the 2x2 Decision Matrix (Micro-Diff)**: Provide competing architectural approaches. The correct option and its closest distractor should differ by only a few words (a parameter, an IAM capability, an API name).
   - In each approach, design real, multi-step technical steps (at least 25 words per option).
   - Distractors must fail purely on subtle constraints: Nuance Trap, Overhead Trap, Cost Trap, or Compliance Trap.
   - **Shuffle the final options**: Randomly assign the correct answer(s) across different positions.

### Step 4: Write Detailed Explanations
For each option (both correct and incorrect):
- **Correct Option(s)**: Explain *why* this architecture satisfies all constraints and the specific optimization criteria (Well-Architected Framework justification).
- **Incorrect Options**: Explicitly point out *why* each distractor is wrong or sub-optimal with deep technical rigor (e.g., "Incorreto: Embora o AWS Network Firewall seja a escolha correta, a falta do Appliance Mode no TGW attachment causa roteamento assimétrico e descarte de pacotes com estado"). Explanations must be detailed (15+ words).

### Step 5: Validate Output

> [!CAUTION]
> **NUNCA salve ou integre um arquivo JSON sem antes executar o checklist abaixo. Qualquer item com ❌ é um bloqueador.**

#### ❌ BLOQUEADORES — Cheklist Obrigatório Antes de Salvar

Para cada questão gerada, verifique:

| # | Verificação | Campo |
|---|-------------|-------|
| 1 | `type` ESTRITAMENTE `"single"` ou `"multiple"` (NUNCA "single-choice" etc) | `type` |
| 1.5 | Proibido usar `scenario` e `question` separados, use APENAS `statement` com tudo junto | `statement` |
| 2 | `statement` (a pergunta) está presente no root E em todas as translations | `statement` |
| 3 | `correctAnswers` contém os IDs corretos (maiúscula para `single`, array para `multiple`) | `correctAnswers` |
| 4 | `requiredChoices` == `len(correctAnswers)` | `requiredChoices` |
| 5 | **Cada opção no root tem `text` (≥ 25 palavras) E `explanation` (≥ 15 palavras)** | `options[].text`, `options[].explanation` |
| 6 | **Cada opção em TODAS as translations tem `text` E `explanation` preenchidos** | `translations.*.options[].text`, `translations.*.options[].explanation` |
| 7 | `generalExplanation` presente no root E em todas as translations | `generalExplanation` |
| 8 | **Respostas corretas NÃO concentradas em `A` ou `B` para múltiplas questões seguidas** | `correctAnswers` distribution |
| 9 | Textos de opções NÃO são apenas nomes de serviços (ex.: `"File Gateway"`) — devem descrever a solução completa | `options[].text` |

#### 🔍 Self-Audit Script

Após gerar as questões e **antes de integrar ao simulador**, execute:

```bash
python3 .agents/skills/sap-c02-question-generator/scripts/validate_questions.py <path_to_json_file> --strict
```

Ou use este snippet rápido para um audit imediato:

```python
import json
with open("path/to/exam.json") as f:
    data = json.load(f)
for i, q in enumerate(data["questions"]):
    issues = []
    if not q.get("type"): issues.append("NO_TYPE")
    if not q.get("statement"): issues.append("NO_STATEMENT")
    if not q.get("generalExplanation"): issues.append("NO_GENERAL_EXPLANATION")
    for opt in q.get("options", []):
        if not opt.get("text") or len(opt["text"].split()) < 15: issues.append(f"OPT_{opt['id']}_SHORT_TEXT")
        if not opt.get("explanation"): issues.append(f"OPT_{opt['id']}_NO_EXPLANATION")
    for lang in ["en", "pt", "es"]:
        t = q.get("translations", {}).get(lang, {})
        if not t.get("statement"): issues.append(f"{lang.upper()}_NO_STATEMENT")
        for opt in t.get("options", []):
            if not opt.get("explanation"): issues.append(f"{lang.upper()}_OPT_{opt['id']}_NO_EXPLANATION")
    if issues:
        print(f"Q{i+1} [{q.get('id')}]: BLOQUEADO — {', '.join(issues)}")
    else:
        print(f"Q{i+1} [{q.get('id')}]: OK")
```

**Se qualquer questão retornar `BLOQUEADO`, corrija antes de salvar.**

---

#### Schema Completo de Referência

Se generating JSON for the simulator, ensure:
- `id`: Unique string (e.g., `sap-q076`).
- `examId`: `"SAP-C02"` (or specific mock code).
- `type`: `"single"` (4 choices) or `"multiple"` (5 or 6 choices).
- `requiredChoices`: Must match length of `correctAnswers`.
- `statement`, `options`, `domainName`, `generalExplanation`: **MUST be present at the root level** (e.g., in English or Portuguese) as the base fallback.
- `options`: Ensure options are long and detailed. No short obvious statements.
- `translations`: Complete and independent localized content for `"en"`, `"pt"` (PT-BR), and `"es"` (ES) with zero mixed/hybrid text. Provide translated `statement`, `options`, `domainName`, and `generalExplanation` inside each language key.

---

## 🛠️ Helper Scripts & Validation

Run the Python validation script to verify questions, type quotas, lengths, and answer distribution:
```bash
python3 .agents/skills/sap-c02-question-generator/scripts/validate_questions.py <path_to_json_file> --strict
```
