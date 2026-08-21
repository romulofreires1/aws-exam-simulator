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

**[Pergunta de Decisão: ex: Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de gerenciamento?]**

---

## 🔘 Alternativas

**A.** [Texto completo do distrator com sequência detalhada de configuração]

**B.** [Texto completo do distrator com sequência detalhada de configuração]

**C.** [Texto completo da alternativa correta detalhando as etapas de implementação]

**D.** [Texto completo do distrator com sequência detalhada de configuração]

*(Nota: Assegure-se de que a resposta correta varie aleatoriamente entre A, B, C, D ou combinações de múltipla escolha como B, D)*

---

## 🎯 Gabarito e Justificativa

### Resposta Correta: **C** *(exemplo embaralhado)*

### Análise Detalhada das Alternativas:
- **A. Incorreto:** [Explicação técnica detalhada justificando por que esta opção é incorreta ou sub-ótima]
- **B. Incorreto:** [Explicação técnica detalhada]
- **C. Correto:** [Explicação técnica detalhada justificando por que esta é a solução ideal segundo o AWS Well-Architected Framework]
- **D. Incorreto:** [Explicação técnica detalhada]

---

## 🧠 AWS Well-Architected Rationale
[Resumo arquitetural destacando o pilar relevante (Segurança, Confiabilidade, Eficiência de Performance, Otimização de Custos ou Excelência Operacional) e links para a documentação oficial.]

- **Documentação Oficial:** [Link para docs.aws.amazon.com]
- **Palavra-chave do Exame:** `[Ex: "RTO < 2 min", "Sem alterar código", "ABAC com PrincipalTag"]`
```
