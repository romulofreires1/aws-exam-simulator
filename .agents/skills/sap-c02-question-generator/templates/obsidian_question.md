# Template de Questão SAP-C02 para Obsidian

Use este formato Markdown quando gerar questões para o cofre do Obsidian ou materiais de estudo:

```markdown
---
tipo: "questao-sap"
dominio: [1 | 2 | 3 | 4]
servicos_principais:
  - "Nome do Serviço 1"
  - "Nome do Serviço 2"
dificuldade: "hard"
---

# Simulado AWS SAP-C02 — Questão [Número]

## 📋 Enunciado

[Descrever o cenário enterprise de 2 a 4 frases, incluindo o contexto da organização, a infraestrutura atual, o problema/novo requisito de negócio, restrições específicas e o critério de decisão em negrito.]

**[Pergunta de Decisão: ex: Qual combinação de ações atenderá a esses requisitos de forma MAIS eficiente operacionalmente? (Escolha duas.)]**

---

## 🔘 Alternativas

**A.** [Texto completo da alternativa detalhando as etapas de implementação]

**B.** [Texto completo da alternativa detalhando as etapas de implementação]

**C.** [Texto completo da alternativa detalhando as etapas de implementação]

**D.** [Texto completo da alternativa detalhando as etapas de implementação]

**E.** [Texto completo da alternativa detalhando as etapas de implementação (se for múltipla escolha)]

---

## 🎯 Gabarito e Justificativa

### Resposta Correta: **[Letra(s)]**

### Análise Detalhada das Alternativas:
- **A. [Correto / Incorreto]:** [Explicação técnica detalhada justificando por que a opção está certa ou errada segundo o AWS Well-Architected Framework]
- **B. [Correto / Incorreto]:** [Explicação técnica detalhada]
- **C. [Correto / Incorreto]:** [Explicação técnica detalhada]
- **D. [Correto / Incorreto]:** [Explicação técnica detalhada]
- **E. [Correto / Incorreto]:** [Explicação técnica detalhada (se aplicável)]

---

## 🧠 AWS Well-Architected Rationale
[Resumo arquitetural destacando o pilar relevante (Segurança, Confiabilidade, Eficiência de Performance, Otimização de Custos ou Excelência Operacional) e links para a documentação oficial.]

- **Documentação Oficial:** [Link para docs.aws.amazon.com]
- **Palavra-chave do Exame:** `[Ex: "RTO < 2 min", "Sem alterar código", "ABAC com PrincipalTag"]`
```
