# Template de Questão SAA-C03 para Obsidian

Use este formato Markdown quando gerar questões para o cofre do Obsidian ou resumos de estudo:

```markdown
---
tipo: "questao-saa"
dominio: [1 | 2 | 3 | 4]
servicos_principais:
  - "Nome do Serviço 1"
  - "Nome do Serviço 2"
dificuldade: "medium" # ou "hard"
---

# Simulado AWS SAA-C03 — Questão [Número]

## 📋 Enunciado

[Descrever o cenário de arquitetura em 2 a 3 frases, incluindo a carga de trabalho atual, o novo requisito de negócio, restrições específicas (ex: menor custo, menor sobrecarga de manutenção, sem alteração de código) e a pergunta com o gatilho em negrito.]

**[Pergunta de Decisão: ex: Qual solução atenderá a esses requisitos com a MENOR sobrecarga operacional?]**

---

## 🔘 Alternativas

**A.** [Texto descritivo do distrator ou alternativa correta]

**B.** [Texto descritivo do distrator ou alternativa correta]

**C.** [Texto descritivo do distrator ou alternativa correta]

**D.** [Texto descritivo do distrator ou alternativa correta]

*(Nota: Assegure-se de que a resposta correta varie aleatoriamente entre A, B, C, D ou pares como B, D)*

---

## 🎯 Gabarito e Justificativa

### Resposta Correta: **[Letra Correta: ex: B]**

### Análise Detalhada das Alternativas:
- **A. Incorreto:** [Explicação técnica detalhada justificando por que esta opção é incorreta ou viola as restrições]
- **B. Correto:** [Explicação técnica detalhada justificando por que esta é a solução recomendada pelo AWS Well-Architected Framework]
- **C. Incorreto:** [Explicação técnica detalhada]
- **D. Incorreto:** [Explicação técnica detalhada]

---

## 🧠 AWS Well-Architected Rationale
[Resumo arquitetural destacando o pilar relevante (Segurança, Resiliência/Confiabilidade, Eficiência de Performance ou Otimização de Custos) e links para a documentação oficial.]

- **Documentação Oficial:** [Link para docs.aws.amazon.com]
- **Palavra-chave do Exame:** `[Ex: "S3 Origin Access Control (OAC)", "RDS Multi-AZ Failover", "SQS Decoupling"]`
```
