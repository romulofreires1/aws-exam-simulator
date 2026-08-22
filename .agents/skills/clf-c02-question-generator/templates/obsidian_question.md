# Template de Questão CLF-C02 para Obsidian

Use este formato Markdown quando gerar questões para o cofre do Obsidian ou notas de estudo fundamentais:

```markdown
---
tipo: "questao-clf"
dominio: [1 | 2 | 3 | 4]
servicos_principais:
  - "Nome do Serviço 1"
  - "Nome do Serviço 2"
dificuldade: "easy" # ou "medium"
---

# Simulado AWS CLF-C02 — Questão [Número]

## 📋 Enunciado

[Descrever a questão fundamental ou cenário de 1 a 2 frases claras e objetivas, com a pergunta principal em negrito.]

**[Pergunta de Decisão: ex: Qual serviço da AWS deve ser usado para...? / De acordo com o Modelo de Responsabilidade Compartilhada...?]**

---

## 🔘 Alternativas

**A.** [Texto claro do distrator ou alternativa correta]

**B.** [Texto claro do distrator ou alternativa correta]

**C.** [Texto claro da alternativa correta ou distrator]

**D.** [Texto claro do distrator ou alternativa correta]

*(Nota: Assegure-se de que a resposta correta varie aleatoriamente entre A, B, C, D ou pares como A, C)*

---

## 🎯 Gabarito e Justificativa

### Resposta Correta: **[Letra Correta: ex: C]**

### Análise Detalhada das Alternativas:
- **A. Incorreto:** [Explicação direta justificando o que este serviço/conceito faz e por que não atende ao enunciado]
- **B. Incorreto:** [Explicação direta]
- **C. Correto:** [Explicação detalhada justificando por que esta é a resposta correta de acordo com as definições oficiais da AWS]
- **D. Incorreto:** [Explicação direta]

---

## 🧠 Conceito Fundamental da AWS
[Resumo do conceito ou serviço abordado, destacando sua definição essencial, benefícios e links para a documentação oficial.]

- **Documentação Oficial:** [Link para docs.aws.amazon.com / aws.amazon.com]
- **Palavra-chave do Exame:** `[Ex: "Responsabilidade Compartilhada", "Well-Architected Confiabilidade", "CloudTrail vs CloudWatch"]`
```
