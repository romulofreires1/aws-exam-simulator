# 🧠 Contexto do Projeto para Agentes de IA: AWS Exam Simulator

Este documento foi elaborado para que qualquer agente de IA ou desenvolvedor compreenda instantaneamente a arquitetura, regras de negócio e padrões deste repositório.

---

## 📌 1. Visão Geral

O **AWS Exam Simulator** é uma aplicação web estática (Next.js 15 App Router + React 19 + Tailwind CSS) que simula com alta fidelidade a experiência de exames oficiais da AWS (plataforma Pearson VUE).

- **100% Client-Side**: Não possui backend, banco de dados centralizado nem autenticação de terceiros.
- **Deploy Estático**: Configurado com `output: 'export'` e `trailingSlash: true` em `next.config.ts`, gerando a pasta estática `out/` sincronizada com Amazon S3 e distribuída globalmente via Amazon CloudFront.
- **Armazenamento**: Todos os dados do usuário (sessão ativa em andamento, respostas, alternativas riscadas, textos realçados, notas de scratchpad, histórico de tentativas e pontuações) são persistidos no `localStorage` do navegador.
- **Internacionalização (i18n)**: Suporte nativo a múltiplos idiomas (**English [EN]**, **Português [PT]**, **Español [ES]**) com troca em tempo real durante a prova.

---

## 🏗️ 2. Estrutura de Diretórios e Responsabilidades

```
aws-exam-simulator/
├── .agents/
│   ├── AI_PROMPT_TEMPLATE.md         # Template base para geração de novos simulados com IA
│   ├── PROJECT.md                    # Este documento de contexto técnico
│   └── skills/                       # Skills de IA especializadas em geração de questões
│       ├── clf-c02-question-generator/   # Gerador para AWS Cloud Practitioner (CLF-C02)
│       ├── saa-c03-question-generator/   # Gerador para AWS Solutions Architect Associate (SAA-C03)
│       └── sap-c02-question-generator/   # Gerador para AWS Solutions Architect Professional (SAP-C02)
├── src/
│   ├── app/
│   │   ├── layout.tsx                # Layout raiz com metadata, tema escuro e Header global
│   │   ├── page.tsx                  # Dashboard inicial (métricas gerais, busca, filtros de categoria, paginação e catálogo)
│   │   ├── history/
│   │   │   └── page.tsx              # Histórico completo de tentativas, estatísticas agregadas e exclusão
│   │   ├── exams/[examId]/
│   │   │   ├── runner/
│   │   │   │   └── page.tsx          # Server component SSG com generateStaticParams que renderiza ExamRunnerClient
│   │   │   └── result/
│   │   │       └── page.tsx          # Server component SSG com generateStaticParams que renderiza ExamResultClient (?attemptId=...)
│   │   └── globals.css               # Tailwind directives e estilo de scrollbar customizado
│   ├── components/
│   │   ├── common/
│   │   │   └── Header.tsx            # Barra de navegação superior (oculta durante a execução da prova)
│   │   ├── dashboard/
│   │   │   └── ExamCard.tsx          # Card interativo de cada certificação com melhor nota e ação direta
│   │   ├── exam/
│   │   │   ├── ExamHeader.tsx        # Header da prova com Timer, idioma, flag, rascunho, mapa e botão de pausa
│   │   │   ├── OptionCard.tsx        # Alternativa interativa (seleção, riscador dedicado e botão direito)
│   │   │   ├── QuestionView.tsx      # Enunciado com realce amarelo, opções, overlay de pausa e botão de verificação
│   │   │   ├── InstantFeedback.tsx   # Explicação técnica aprofundada por alternativa no Modo Treino
│   │   │   ├── ExamRunnerClient.tsx  # Client component orquestrador do simulador
│   │   │   ├── QuestionGridModal.tsx # Mapa de questões com status (respondida, marcada, pendente)
│   │   │   ├── ScratchpadModal.tsx   # Bloco de rascunho individual persistido por questão
│   │   │   └── ExamReviewScreen.tsx  # Tela de revisão prévia da prova antes do envio no Modo Real
│   │   └── results/
│   │       ├── ExamResultClient.tsx  # Client component do relatório de resultado
│   │       ├── ScoreCard.tsx         # Nota oficial escalada (100–1000), selo Pass/Fail e confete
│   │       ├── DomainBreakdownList.tsx # Gráficos e porcentagens por domínio oficial da AWS
│   │       └── QuestionReviewList.tsx  # Revisor de questões com filtros (todas, erros, acertos, marcadas)
│   ├── data/
│   │   └── exams/
│   │       ├── _template.json        # Template base para novos simulados
│   │       ├── sap-c02-sim-1.json    # Simulado SAP-C02 Mock 1 (25 questões, Professional)
│   │       ├── sap-c02-sim-2.json    # Simulado SAP-C02 Mock 2 (25 questões, Professional)
│   │       ├── sap-c02-sim-3.json    # Simulado SAP-C02 Mock 3 (25 questões, Professional)
│   │       ├── saa-c03.json          # Simulado SAA-C03 (65 questões, Associate)
│   │       ├── clf-c02.json          # Simulado CLF-C02 (65 questões, Foundational)
│   │       └── index.ts              # Registro central e funções getAllExams() e getExamById()
│   ├── hooks/
│   │   ├── useExamEngine.ts          # Motor de estado da prova (respostas, flags, destaques, atalhos, pausa e auto-save)
│   │   └── useTimer.ts               # Hook de temporizador com alertas aos 15m e 5m finais
│   ├── lib/
│   │   ├── localization.ts           # Utilitários de tradução e detecção de idiomas (EN, PT, ES)
│   │   ├── scoreCalculator.ts        # Cálculo de score escalado (100–1000) e competências por domínio
│   │   └── storage/
│   │       └── examStorage.ts        # Wrapper tipado e SSR-safe de acesso ao localStorage
│   ├── scripts/
│   │   ├── validate-exams.ts         # Script CLI que valida integridade de todos os JSONs de simulados
│   │   └── infra-aws.sh              # Automação de infraestrutura S3 + CloudFront + Route 53
│   └── types/
│       └── exam.ts                   # Tipos TypeScript centralizados (Question, ExamDefinition, ExamAttempt, etc.)
```

---

## 🎯 3. Regras de Negócio e Comportamento

### 3.1. Modos de Exame
1. **Modo Simulado Real (`mode = 'real'`)**:
   - Temporizador regressivo oficial com alertas visuais (15m e 5m).
   - Sem gabarito durante o teste.
   - Suporte a pausa com congelamento do cronômetro e persistência do tempo restante.
   - Ao avançar na última questão, abre a `ExamReviewScreen`.
   - Submissão final calcula a pontuação oficial AWS (100–1000) e salva a tentativa.
2. **Modo Treino (`mode = 'practice'`)**:
   - Sem cronômetro (estudo focado sem pressão).
   - O usuário seleciona suas alternativas e clica em **`[ Verificar Resposta & Explicação ]`**.
   - As justificativas detalhadas para cada opção e link oficial da AWS são exibidos sob demanda.

### 3.2. Catálogo e Navegação no Dashboard
- **Busca em Tempo Real**: Filtra simulados por código, título, descrição e categoria.
- **Filtros por Categoria**: Pílulas de filtro dinâmicas (*All, Foundational, Associate, Professional, Specialty*) com badges de contagem.
- **Paginação**: Divisão limpa em páginas (6 itens por página) com navegação rápida.
- **Estatísticas Gerais**: Cards de resumo no topo com Total de Questões no Banco, Simulados Concluídos, Taxa de Aprovação e Média de Pontuação.

### 3.3. Ferramentas da Interface Oficial
- **Pausa de Exame Direta**: O usuário pode pausar o exame a qualquer instante. O timer é congelado, o tempo restante é persistido no `localStorage`, e o conteúdo é ocultado por um overlay de retomada.
- **Modal de Abandono**: Confirmação segura para abandonar a prova e retornar ao dashboard.
- **Troca de Idioma (i18n)**: Alternância em tempo real entre Inglês, Português e Espanhol no header da prova, com indicação de disponibilidade.
- **Strikethrough (Riscar Alternativa)**: Clique no botão "Riscar" ou com o botão direito do mouse na opção. O estado de risco fica persistido na sessão.
- **Highlighting (Realce de Texto)**: O usuário seleciona qualquer trecho no enunciado e clica em "Realçar Texto". O trecho é pintado de amarelo e permanece salvo na sessão da questão.
- **Scratchpad Individual**: Bloco de anotações individual por questão persistido na sessão.
- **Limite Estrito de Opções**: Em questões de múltipla seleção (ex: `requiredChoices: 2`), o simulador impede que mais de 2 alternativas fiquem marcadas simultaneamente.
- **Atalhos de Teclado**: Teclas <kbd>A</kbd>–<kbd>E</kbd> para marcar, <kbd>F</kbd> para Flag, <kbd>→</kbd> / <kbd>Enter</kbd> para avançar e <kbd>←</kbd> para voltar.
- **Alternância de Layout**: Toggle entre o tema **AWS Console Dark** moderno e o layout clássico **Pearson VUE**.

---

## 🤖 4. Ecossistema de Skills de IA (`.agents/skills/`)

O repositório inclui três habilidades especializadas para criação de questões com máxima fidelidade:

1. **`clf-c02-question-generator`**: Focado nos 4 domínios da certificação Foundational.
2. **`saa-c03-question-generator`**: Focado em arquiteturas resilientes, seguras, de alta performance e otimizadas para custo.
3. **`sap-c02-question-generator`**: Focado em cenários empresariais complexos, multi-conta, migrações 7 Rs e modernização.

### Diretrizes de Engenharia de Questões:
- **Matriz de Decisão 2x2**: 2 pares conceituais de abordagem (ex: 2 opções com Abordagem A, 2 com Abordagem B).
- **Distratores de Alta Plausibilidade**: Todos os distratores devem ser soluções tecnicamente válidas que falham apenas em restrições sutis do cenário (custo, sobrecarga operacional, limite de serviço).
- **Gabarito Estritamente Embaralhado**: Distribuição uniforme das respostas corretas entre as alternativas A, B, C, D e E.

---

## 🚀 5. Como Adicionar um Novo Simulado

1. Use uma das Skills em [`.agents/skills/`](skills/) ou copie o prompt em [`.agents/AI_PROMPT_TEMPLATE.md`](AI_PROMPT_TEMPLATE.md).
2. Salve o arquivo JSON em `src/data/exams/[codigo-do-exame].json`.
3. Registre o exame no array `AVAILABLE_EXAMS` em `src/data/exams/index.ts`.
4. Valide a integridade com:
   ```bash
   npm run validate:exams
   ```
5. Teste a compilação:
   ```bash
   npm run build
   ```

---

## 💻 6. Comandos de Terminal

| Comando | Descrição |
| :--- | :--- |
| `npm run dev` | Inicia o servidor de desenvolvimento com hot-reload em `http://localhost:3000` |
| `npm run build` | Valida tipos e compila a aplicação estática (`next build` com SSG para `out/`) |
| `npm run start` | Serve localmente a pasta estática exportada `out/` em `http://localhost:3000` |
| `npm run validate:exams` | Valida integridade e esquema de todos os bancos de questões JSON antes do commit |
| `npm run lint` | Executa o linter ESLint |

