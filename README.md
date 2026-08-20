# 🛡️ AWS Exam Simulator

> **Simulador de Certificações AWS moderno, offline e 100% client-side com fidelidade ao exame oficial (Pearson VUE).**

---

## ✨ Funcionalidades Principais

- ⏱️ **Modo Simulado Real**: Temporizador oficial regressivo da AWS (com alertas visuais aos 15m e 5m finais), navegação livre, tela de revisão prévia e cálculo de nota na escala oficial AWS (100 a 1000 pontos).
- 💡 **Modo Treino (Estudo)**: Sem limite de tempo, com botão de verificação de resposta sob demanda e explicações técnicas aprofundadas por alternativa + links para a documentação oficial da AWS.
- 🚫 **Strikethrough (Riscador de Alternativas)**: Elimine alternativas descartadas com botão dedicado ou clicando com o botão direito do mouse.
- ✨ **Highlighting (Realce de Texto)**: Selecione qualquer trecho no enunciado para pintar de amarelo com persistência entre questões.
- 🚩 **Flag & Scratchpad**: Marque questões para revisar mais tarde e faça anotações de rascunho individuais por questão.
- 📊 **Desempenho por Domínio**: Relatório final com radar de competências de acordo com o guia oficial de cada exame AWS.
- 💾 **100% Armazenamento Local**: Auto-save automático contínuo no `localStorage`. Recarregue ou feche a aba sem perder o progresso.
- ⌨️ **Atalhos de Teclado**: Teclas <kbd>A</kbd>–<kbd>E</kbd> para selecionar, <kbd>F</kbd> para Flag, <kbd>→</kbd> / <kbd>Enter</kbd> para próxima e <kbd>←</kbd> para anterior.
- 🌗 **Alternância de Layout**: Troque em tempo real entre o tema **AWS Console Dark Moderno** e a interface clássica **Pearson VUE**.

---

## 📚 Certificações Incluídas

| Código | Certificação | Nível | Tempo Oficial | Nota de Corte |
| :--- | :--- | :--- | :--- | :--- |
| **SAP-C02** | AWS Certified Solutions Architect - Professional | Professional | 180 min | 750 / 1000 |
| **SAA-C03** | AWS Certified Solutions Architect - Associate | Associate | 130 min | 720 / 1000 |
| **CLF-C02** | AWS Certified Cloud Practitioner | Foundational | 90 min | 700 / 1000 |

---

## 💻 Desenvolvimento e Execução Local

### 1. Instalação de Dependências
```bash
npm install
```

### 2. Rodar em Ambiente de Desenvolvimento (Hot-Reload)
```bash
npm run dev
```
Acesse [http://localhost:3000](http://localhost:3000) no seu navegador.

### 3. Build de Produção e Visualização Estática
```bash
npm run build
npm run start
```

---

## 🤖 Como Adicionar Novos Simulados com IA

O projeto possui um template padronizado e um validador automático para inclusão de novos exames sem necessidade de alterar a lógica da aplicação:

1. Abra o arquivo [`.agent/AI_PROMPT_TEMPLATE.md`](.agent/AI_PROMPT_TEMPLATE.md) e copie o prompt para o seu assistente de IA favorito (ChatGPT, Claude, Gemini).
2. Salve o JSON gerado em `src/data/exams/[codigo-do-exame].json`.
3. Registre o exame no array `AVAILABLE_EXAMS` em `src/data/exams/index.ts`.
4. Valide a integridade do JSON executando:
   ```bash
   npm run validate:exams
   ```
5. Faça o commit e push:
   ```bash
   git add src/data/exams/
   git commit -m "feat: add DVA-C02 exam"
   git push origin main
   ```

---

## 🚀 Deploy e Infraestrutura AWS

Este projeto utiliza uma arquitetura multi-conta AWS com deploy automatizado via GitHub Actions:

- **Infraestrutura**: Amazon S3 (hospedagem estática), Amazon CloudFront (CDN global com SSL ACM) e Amazon Route 53 (DNS).
- **CI/CD**: Ao fazer `git push origin main`, o workflow do GitHub Actions valida os exames, gera o build estático (`out/`), sincroniza com o bucket S3 e invalida o cache do CloudFront.

---

## 🛠️ Tecnologias

- **Framework**: Next.js 15 (App Router, Static Export)
- **UI & Estilização**: React 19, Tailwind CSS, Lucide React, Canvas Confetti
- **Linguagem**: TypeScript
- **Validação & Scripts**: TSX, Node.js
