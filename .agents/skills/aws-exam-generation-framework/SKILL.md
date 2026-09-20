---
name: aws-exam-generation-framework
description: >-
  Master framework establishing the standard operating procedures, quality assurance,
  and generation rules for ANY AWS certification exam simulator (CLF, SAA, SAP, etc.).
---

# AWS Exam Generation Framework (Master Standard)

Este documento é a **diretriz de hierarquia superior (Master Framework)** para a criação de questões e simulados no projeto `aws-exam-simulator`. Ele padroniza o workflow, o formato e as regras de qualidade globais, garantindo que todo simulado gerado — seja Foundational, Associate ou Professional — mantenha o "Padrão Ouro" estabelecido, respeitando as particularidades de cada certificação.

> [!IMPORTANT]
> Qualquer sub-skill específica de exame (como `sap-c02-question-generator` ou `clf-c02-question-generator`) **herda e deve obedecer** às regras globais deste documento. Em caso de conflito, este Master Framework prevalece.

---

## 1. Estrutura de Diretórios e Arquivos Obrigatória (The Scaffold)

Para garantir que o fluxo de geração, qualidade e conhecimento seja replicável e consistente, **qualquer** gerador de simulado no projeto DEVE respeitar e implementar a seguinte estrutura exata de diretórios sob a pasta `.agents/skills/<exame>-question-generator/`:

```text
.agents/skills/<exame>-question-generator/
├── SKILL.md                                 # [OBRIGATÓRIO] Documento principal com regras de geração locais, cotas e fluxo de execução.
├── scripts/
│   └── validate_questions.py                # [OBRIGATÓRIO] Script de QA em Python com verificações de schema, tamanho, traduções e vício de gabarito.
├── templates/
│   ├── obsidian_question.md                 # [OBRIGATÓRIO] Template de exportação em Markdown para cofres Obsidian.
│   └── simulator_question.json              # [OBRIGATÓRIO] Template JSON com exemplos de single e multiple choice.
└── references/
    ├── exam_blueprint.md                    # [OBRIGATÓRIO] Mapeamento dos domínios, Task Statements e o peso (%) de cada domínio na prova oficial.
    ├── question_crafting_rules.md           # [OBRIGATÓRIO] Guia de estilo de escrita, profundidade e regras de distratores para o nível do exame.
    ├── gap_analysis_and_traps.md            # [OBRIGATÓRIO] Compilado de "pegadinhas" comuns e padrões arquiteturais core do exame.
    ├── domain_1_*.md                        # [OBRIGATÓRIO] Conteúdo técnico isolado do Domínio 1.
    ├── domain_2_*.md                        # [OBRIGATÓRIO] Conteúdo técnico isolado do Domínio 2.
    └── domain_N_*.md                        # [OBRIGATÓRIO] Um arquivo para cada domínio restante do exame.
```

### Regras Estruturais:

1. **Script de Validação é Obrigatório:** O arquivo `scripts/validate_questions.py` não é opcional. Todo gerador DEVE ter seu próprio validador que audite os arquivos JSON antes que qualquer questão seja salva no simulador.
2. **Separação de Preocupações:** O conhecimento técnico (conceitos de nuvem, limites de serviço e armadilhas) **nunca** deve ser colocado diretamente no `SKILL.md`. Todo conhecimento de domínio deve ficar segmentado na pasta `references/` para manter o `SKILL.md` focado exclusivamente no processo e nas regras de geração.
3. **Pré-Requisito para Novos Exames:** A adição de qualquer novo exame ao simulador (ex: *DVA-C02* ou *ANS-C01*) é condicionada à criação prévia de toda esta estrutura. O agente encarregado não pode gerar questões sem antes criar o scaffolding completo e preencher todos os arquivos obrigatórios de referência e templates.

### Conformidade Atual dos Geradores Existentes:

| Gerador | SKILL.md | scripts/ | templates/ | references/ (blueprint + crafting + traps + domínios) | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `clf-c02-question-generator` | ✅ | ✅ | ✅ | ✅ (blueprint + crafting + traps + 4 domínios) | ✅ Conforme |
| `saa-c03-question-generator` | ✅ | ✅ | ✅ | ✅ (blueprint + crafting + traps + 4 domínios) | ✅ Conforme |
| `sap-c02-question-generator` | ✅ | ✅ | ✅ | ✅ (blueprint + crafting + traps + 4 domínios) | ✅ Conforme |

---

## 2. Princípios Universais de Qualidade (Quality Assurance Global)

Independentemente do nível da certificação AWS, os seguintes princípios são **inegociáveis** e se aplicam a todos os geradores:

### 2.1. Ausência de Distratores Ingênuos
- Nunca gerar alternativas curtas demais ou que listem serviços falsos ou abordagens absurdas (ex: "Criar um script em bash rodando em cron", "AWS Data Saver").
- Todos os distratores devem usar serviços reais da AWS e descrever arquiteturas tecnicamente plausíveis.

### 2.2. Justificativas Técnicas Obrigatórias
- NENHUMA explicação pode ser vazia ou genérica ("Incorreto porque não atende ao requisito").
- Todas as alternativas devem explicar o *porquê* mecânico/técnico da falha ou do acerto em relação ao enunciado.
- A explicação de cada alternativa deve iniciar com `Correto:` ou `Incorreto:` (ou `Correct:`/`Incorrect:` em inglês).

### 2.3. Embaralhamento Rigoroso de Gabaritos (Strict Shuffling)
- É estritamente proibido concentrar os gabaritos corretos na opção `A` ou nas opções `A, B`.
- A distribuição estatística das respostas corretas deve ser balanceada e pseudo-aleatória.
- O script de validação deve detectar e bloquear qualquer vício de concentração (>45% em uma letra).

### 2.4. Tradução Integral (en, pt, es)
- Todos os simulados exportados para JSON devem conter blocos completos de tradução para os 3 idiomas.
- Cada tradução deve incluir: `statement`, `domainName`, `options` (com `text` e `explanation` para cada alternativa) e `generalExplanation`.
- Traduções incompletas ou com idiomas misturados são bloqueadores.

### 2.5. Campo `statement` Unificado
- É proibido separar o enunciado em campos `scenario` e `question`.
- Use APENAS o campo `statement` que contém o contexto completo e a pergunta de decisão.

---

## 3. Adaptação Escalar de Complexidade (Por Nível de Certificação)

O processo de geração deve respeitar a anatomia específica do nível do exame. A tabela abaixo calibra como o agente deve se comportar:

| Dimensão | Foundational (ex: CLF-C02) | Associate (ex: SAA-C03) | Professional (ex: SAP-C02) |
| :--- | :--- | :--- | :--- |
| **Escopo Arquitetural** | 1 serviço ou conceito de nuvem. | 2 a 3 serviços interagindo (ex: ALB + EC2 + ASG). | 5 a 8 serviços (Enterprise End-to-End, Multi-Account/Multi-Região). |
| **Tipo de Pergunta** | "O que é X?" / "Qual serviço usar para Y?" | "Como implementar X e Y de forma escalável?" | "Qual combinação de serviços resolve X com o menor trade-off Y e Z?" |
| **Extensão do Enunciado** | 1 a 2 frases diretas. | 2 a 3 frases com contexto de negócio. | 3 a 5 frases com gargalos, restrições conflitantes e sistemas legado. |
| **Extensão das Alternativas** | 1 frase (10-20 palavras). | 1 a 2 frases (15-30 palavras). | 3 a 6 linhas (25-45 palavras) descrevendo sequências de configuração. |
| **Engenharia de Distratores** | Outros serviços de propósito parecido (ex: S3 vs EBS). | Serviços plausíveis mas menos eficientes. | **Micro-Diff (Matriz 2x2):** Opções quase idênticas variando apenas flags de API ou detalhes de configuração interna. |
| **Cota de Múltipla Escolha** | ~10% a 15% | ~15% a 20% | **20% a 25% obrigatório** |
| **Tempo por Questão (prova real)** | ~1 min 32s (90 min / 65 q) | ~2 min (130 min / 65 q) | ~2 min 56s (220 min / 75 q) |

---

## 4. Workflow Universal de Geração de Simulados

Todos os agentes encarregados de gerar simulados **devem** seguir estas etapas obrigatórias, na ordem:

### Passo 1: Leitura Obrigatória das Referências do Exame
- O agente **deve** acessar a pasta `.agents/skills/<exame>-question-generator/references/` e ler:
  1. `exam_blueprint.md` — para respeitar as cotas e pesos percentuais de cada Domínio.
  2. `question_crafting_rules.md` — para calibrar a profundidade, anatomia e distratores do nível.
  3. `gap_analysis_and_traps.md` — para injetar nuances e pegadinhas reais nas questões.
  4. Os arquivos `domain_*.md` relevantes — para garantir precisão técnica no conteúdo.

### Passo 2: Geração Seguindo os Templates Locais
- As questões devem ser formatadas seguindo os templates do exame local (`templates/simulator_question.json` e `templates/obsidian_question.md`).
- A questão deve usar o campo unificado `statement` (nunca `scenario`/`question` separados).
- Os campos `correctAnswers`, `type`, `requiredChoices`, `domainId` e `generalExplanation` são obrigatórios.

### Passo 3: Engenharia "Anti-Leak" e Ineditismo
- Proibido usar cópias exatas de exam dumps vazados da internet.
- Cada questão deve ser sintetizada do zero, combinando restrições de negócio originais.
- Cenários devem variar os setores (fintech, saúde, e-commerce, mídia, governo) para evitar repetição temática.

### Passo 4: Execução Obrigatória do Script de Validação (Self-Audit)

> [!CAUTION]
> **NUNCA salve ou integre um arquivo JSON ao simulador sem antes executar o script de validação. Qualquer erro retornado é um bloqueador.**

```bash
python3 .agents/skills/<exame>-question-generator/scripts/validate_questions.py <path_do_json> --strict
```

O script verifica:
- Campos obrigatórios preenchidos (`statement`, `type`, `correctAnswers`, `generalExplanation`).
- Paridade entre `correctAnswers` e `requiredChoices`.
- Comprimento mínimo de alternativas e explicações.
- Traduções completas em `en`, `pt` e `es` (com `statement`, `options` e `generalExplanation`).
- Distribuição equilibrada de gabaritos (sem vício em uma letra específica).
- Cota mínima de questões de múltipla escolha.
- Detecção de explicações genéricas (boilerplate proibido).
- Contradições entre gabarito e prefixo da explicação (ex: opção correta com explicação "Incorreto:").

---

## 5. Padrão Universal do JSON Schema

Independentemente do exame, a estrutura abaixo é obrigatória para cada questão no simulador:

```json
{
  "id": "<examcode>-q<NNN>",
  "examId": "<EXAM-CODE>",
  "domainId": "domain-<N>-<slug>",
  "domainName": "Domain N: <Official Domain Name>",
  "services": ["Service 1", "Service 2"],
  "type": "single|multiple",
  "requiredChoices": 1,
  "statement": "Full question context with scenario, constraints, and decision trigger.",
  "options": [
    {
      "id": "A",
      "text": "Full text of the option describing the complete architectural approach.",
      "explanation": "Correct:|Incorrect: Full technical justification."
    }
  ],
  "correctAnswers": ["C"],
  "generalExplanation": "A complete architectural summary explaining the right choice.",
  "referenceUrl": "https://docs.aws.amazon.com/...",
  "difficulty": "easy|medium|hard",
  "translations": {
    "en": {
      "domainName": "...",
      "statement": "...",
      "options": [{ "id": "A", "text": "...", "explanation": "..." }],
      "generalExplanation": "..."
    },
    "pt": {
      "domainName": "...",
      "statement": "...",
      "options": [{ "id": "A", "text": "...", "explanation": "..." }],
      "generalExplanation": "..."
    },
    "es": {
      "domainName": "...",
      "statement": "...",
      "options": [{ "id": "A", "text": "...", "explanation": "..." }],
      "generalExplanation": "..."
    }
  }
}
```

### Regras do Schema:
- `type`: Estritamente `"single"` ou `"multiple"`. Qualquer variação (ex: `"single-choice"`) é bloqueada.
- `single`: Exatamente 4 opções (A-D), `requiredChoices` = 1.
- `multiple` com 2 respostas: Exatamente 5 opções (A-E), `requiredChoices` = 2.
- `multiple` com 3 respostas: Exatamente 6 opções (A-F), `requiredChoices` = 3.
- `timeLimitMinutes` (no arquivo do exame): Calculado como `(totalQuestions / 75) * 210`.

---

## 6. Hierarquia de Documentos

```text
aws-exam-generation-framework/SKILL.md          ← ESTE DOCUMENTO (Master Standard — regras globais)
    │
    ├── clf-c02-question-generator/SKILL.md      ← Regras locais do CLF-C02 (herda o Master)
    │   ├── references/                          ← Conhecimento técnico Foundational
    │   ├── scripts/validate_questions.py        ← Validador local com domainIds do CLF
    │   └── templates/                           ← Templates JSON/MD do CLF
    │
    ├── saa-c03-question-generator/SKILL.md      ← Regras locais do SAA-C03 (herda o Master)
    │   ├── references/                          ← Conhecimento técnico Associate
    │   ├── scripts/validate_questions.py        ← Validador local com domainIds do SAA
    │   └── templates/                           ← Templates JSON/MD do SAA
    │
    └── sap-c02-question-generator/SKILL.md      ← Regras locais do SAP-C02 (herda o Master)
        ├── references/                          ← Conhecimento técnico Professional
        ├── scripts/validate_questions.py        ← Validador local com domainIds do SAP
        └── templates/                           ← Templates JSON/MD do SAP
```
