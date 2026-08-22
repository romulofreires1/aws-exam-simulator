# 🧠 Contexto do Projeto para Agentes de IA: AWS Exam Simulator

Este documento foi elaborado para que qualquer agente de IA ou desenvolvedor compreenda instantaneamente a arquitetura, regras de negócio e padrões deste repositório.

---

## 📌 1. Visão Geral

O **AWS Exam Simulator** é uma aplicação web estática (Next.js 15 App Router + React 19 + Tailwind CSS) que simula com alta fidelidade a experiência de exames oficiais da AWS (plataforma Pearson VUE).

- **100% Client-Side**: Não possui backend, banco de dados centralizado nem autenticação de terceiros.
- **Deploy Estático**: Configurado com `output: 'export'` em `next.config.ts`, gerando a pasta `out/` sincronizada com Amazon S3 e distribuída via Amazon CloudFront.
- **Armazenamento**: Todos os dados do usuário (sessão ativa em andamento, respostas, alternativas riscadas, textos realçados, histórico de tentativas e pontuações) são persistidos no `localStorage` do navegador.

---

## 🏗️ 2. Estrutura de Diretórios e Responsabilidades

```
src/
├── app/
│   ├── layout.tsx                    # Layout raiz com metadata, tema escuro e Header global
│   ├── page.tsx                      # Dashboard inicial (métricas gerais, catálogo de simulados e histórico rápido)
│   ├── history/
│   │   └── page.tsx                  # Histórico completo de tentativas, estatísticas e exclusão
│   ├── exams/[examId]/
│   │   ├── runner/
│   │   │   └── page.tsx              # Server component com generateStaticParams que renderiza ExamRunnerClient
│   │   └── result/
│   │       └── page.tsx              # Server component com generateStaticParams que renderiza ExamResultClient (?attemptId=...)
│   └── globals.css                   # Tailwind directives e estilo de scrollbar customizado
├── components/
│   ├── common/
│   │   └── Header.tsx                # Barra de navegação superior (oculta durante a execução da prova)
│   ├── dashboard/
│   │   └── ExamCard.tsx              # Card interativo de cada certificação com melhor nota e ação direta
│   ├── exam/
│   │   ├── ExamHeader.tsx            # Header da prova com Timer (Modo Real), flag, atalhos, anotações e troca de tema
│   │   ├── OptionCard.tsx            # Alternativa interativa (clique total, riscador dedicado e botão direito)
│   │   ├── QuestionView.tsx          # Enunciado com realce amarelo interativo, opções e botão de verificar resposta
│   │   ├── InstantFeedback.tsx       # Explicação técnica aprofundada por alternativa no Modo Treino
│   │   ├── ExamRunnerClient.tsx      # Client component orquestrador do simulador
│   │   ├── QuestionGridModal.tsx     # Mapa de questões com status (respondida, marcada, pendente)
│   │   ├── ScratchpadModal.tsx       # Bloco de rascunho individual por questão
│   │   └── ExamReviewScreen.tsx      # Tela de revisão prévia da prova antes do envio no Modo Real
│   └── results/
│       ├── ExamResultClient.tsx      # Client component do relatório de resultado
│       ├── ScoreCard.tsx             # Nota oficial escalada (100–1000), selo Pass/Fail e confete
│       ├── DomainBreakdownList.tsx   # Gráficos e porcentagens por domínio oficial da AWS
│       └── QuestionReviewList.tsx    # Revisor de questões com filtros (todas, erros, acertos, marcadas)
├── data/
│   └── exams/
│       ├── _template.json            # Template base para novos simulados
│       ├── sap-c02.json              # Banco AWS Solutions Architect - Professional (SAP-C02)
│       ├── saa-c03.json              # Banco AWS Solutions Architect - Associate (SAA-C03)
│       ├── clf-c02.json              # Banco AWS Cloud Practitioner (CLF-C02)
│       └── index.ts                  # Registro central e funções getAllExams() e getExamById()
├── hooks/
│   ├── useExamEngine.ts              # Motor de estado da prova (respostas, flags, destaques, atalhos e auto-save)
│   └── useTimer.ts                   # Hook de temporizador com alertas aos 15m e 5m finais
├── lib/
│   ├── scoreCalculator.ts            # Cálculo de score escalado (100–1000) e competências por domínio
│   └── storage/
│       └── examStorage.ts            # Wrapper tipado e SSR-safe de acesso ao localStorage
├── scripts/
│   └── validate-exams.ts             # Script CLI que valida integridade de todos os JSONs de simulados
└── types/
    └── exam.ts                       # Tipos TypeScript centralizados (Question, ExamDefinition, ExamAttempt, etc.)
```

---

## 🎯 3. Regras de Negócio e Comportamento

### 3.1. Modos de Exame
1. **Modo Simulado Real (`mode = 'real'`)**:
   - Temporizador regressivo oficial com alertas visuais.
   - Sem gabarito durante o teste.
   - Ao avançar na última questão, abre a `ExamReviewScreen`.
   - Submissão final calcula a pontuação oficial AWS (100–1000) e salva a tentativa.
2. **Modo Treino (`mode = 'practice'`)**:
   - Sem cronômetro (estudo sem pressão).
   - O usuário seleciona suas alternativas e clica em **`[ Verificar Resposta & Explicação ]`**.
   - As justificativas detalhadas para cada opção e link oficial da AWS são exibidos sob demanda.

### 3.2. Ferramentas da Interface Oficial
- **Strikethrough (Riscar Alternativa)**: Clique no botão "Riscar" ou clique com o botão direito do mouse na opção. O estado de risco fica persistido na sessão.
- **Highlighting (Realce de Texto)**: O usuário seleciona qualquer trecho no enunciado e clica em "Realçar Texto". O trecho é pintado de amarelo e permanece salvo ao mudar de questão e voltar.
- **Limite Estrito de Opções**: Em questões de múltipla seleção (ex: `requiredChoices: 2`), o simulador impede que mais de 2 alternativas fiquem marcadas simultaneamente.
- **Atalhos de Teclado**: Teclas <kbd>A</kbd>–<kbd>E</kbd> para marcar, <kbd>F</kbd> para Flag, <kbd>→</kbd> / <kbd>Enter</kbd> para avançar e <kbd>←</kbd> para voltar.

---

## 🚀 4. Como Adicionar um Novo Simulado

1. Crie o arquivo JSON em `src/data/exams/[codigo-do-exame].json` seguindo o modelo em [`.agents/AI_PROMPT_TEMPLATE.md`](.agents/AI_PROMPT_TEMPLATE.md).
2. Registre o exame no array `AVAILABLE_EXAMS` em `src/data/exams/index.ts`.
3. Valide o esquema com:
   ```bash
   npm run validate:exams
   ```
4. Teste o build:
   ```bash
   npm run build
   ```

---

## 💻 5. Comandos de Terminal

| Comando | Descrição |
| :--- | :--- |
| `npm run dev` | Inicia o servidor de desenvolvimento em `http://localhost:3000` |
| `npm run build` | Valida tipos e compila a aplicação estática para a pasta `out/` |
| `npm run start` | Serve localmente a pasta estática `out/` em `http://localhost:3000` |
| `npm run validate:exams` | Valida todos os bancos de questões JSON antes do commit |
| `npm run lint` | Executa o linter ESLint |
