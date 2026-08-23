# Regras e Anatomia para Criação de Questões CLF-C02

O exame **AWS Certified Cloud Practitioner (CLF-C02)** avalia o conhecimento fundamental dos conceitos de computação em nuvem, serviços centrais da AWS, modelo de segurança compartilhada, precificação e suporte técnico. Esta referência define as diretrizes para produzir questões no exato padrão da prova oficial.

---

## 1. Características do Nível Foundational (CLF-C02)

| Dimensão | CLF-C02 (Foundational) | SAA-C03 (Associate) | SAP-C02 (Professional) |
| :--- | :--- | :--- | :--- |
| **Público-Alvo** | Profissionais em início de jornada em nuvem, gerentes de produto, vendas técnicas, finanças e TI | Arquitetos de soluções, desenvolvedores e engenheiros de infraestrutura | Arquitetos seniores e líderes de engenharia enterprise |
| **Tipo de Pergunta** | Identificação direta de serviços, papéis de responsabilidade, pilares do Well-Architected e planos de suporte | Cenários de arquitetura aplicada com múltiplos requisitos conflitantes (RTO/RPO, custos, rede) | Cenários enterprise multi-conta/multirregião de alta complexidade |
| **Extensão do Enunciado** | **1 a 2 frases claras e objetivas** | 2 a 4 frases com contexto de arquitetura e restrições | 3 a 5 frases longas com histórico de legado e compliance |
| **Extensão das Opções** | **6 a 25 palavras por opção** (1 a 2 frases concisas e simétricas) | 15 a 35 palavras por opção detalhando passos técnicos | 25 a 50+ palavras por opção com parametrizações |
| **Distratores** | Serviços reais da AWS com propósitos distintos da pergunta (ZERO nomes inventados) | Soluções técnicas válidas que falham em trade-offs de custo/overhead | Arquiteturas completas válidas onde apenas nuances sutis desqualificam a opção |
| **Tempo / Questão** | **~1 min 23 s (83 segundos)** (90 min / 65 q) | **2 min (120 s)** (130 min / 65 q) | **2 min 56 s (176 s)** (220 min / 75 q) |

---

## 2. Regra Obrigatória de Embaralhamento de Gabaritos

Para garantir integridade dos simulados:
1. **PROIBIDO Gabarito Fixo em A ou A/B**:
   - Nunca fixe a resposta correta na opção `A` ou nas opções `A` e `B`.
2. **Distribuição Equilibrada**:
   - As respostas corretas **DEVEM** ser distribuídas de forma homogênea (~25% para cada letra `A`, `B`, `C`, `D` em questões de escolha única).
   - Em múltipla escolha, varie os pares (`["A", "C"]`, `["B", "D"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
3. **Explicações Coerentes**:
   - Cada opção deve ter uma explicação individual (`explanation`), iniciando com `Correto: ` / `Correct: ` ou `Incorreto: ` / `Incorrect: `, detalhando claramente o porquê.

---

## 3. Padrões de Formulação de Perguntas CLF-C02 (Padrão Ouro)

As questões do exame Cloud Practitioner seguem principalmente 5 arquétipos:

### Padrão 1: Identificação de Serviço por Propósito
- *Enunciado:* "Uma empresa precisa executar código em resposta a eventos sem provisionar ou gerenciar servidores físicos ou virtuais. Qual serviço da AWS atende a essa necessidade?"
- *Gabarito Correto:* **AWS Lambda** (Computação Serverless).

### Padrão 2: Modelo de Responsabilidade Compartilhada
- *Enunciado:* "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes tarefas é de responsabilidade exclusiva do cliente ao executar uma instância Amazon EC2?"
- *Gabarito Correto:* **Instalação de patches no sistema operacional convidado e configuração de regras de firewall (Security Groups).**

### Padrão 3: Pilares do AWS Well-Architected Framework
- *Enunciado:* "Qual pilar do AWS Well-Architected Framework se concentra na capacidade de executar e monitorar sistemas para entregar valor ao negócio e melhorar continuamente os processos e procedimentos operacionais?"
- *Gabarito Correto:* **Excelência Operacional (Operational Excellence).**

### Padrão 4: Planos de Suporte e Governança Financeira
- *Enunciado:* "Qual plano de suporte da AWS inclui acesso a um Technical Account Manager (TAM) dedicado para fornecer orientações proativas e revisões arquiteturais regulares?"
- *Gabarito Correto:* **AWS Enterprise Support.**

### Padrão 5: Infraestrutura Global da AWS
- *Enunciado:* "Qual componente da infraestrutura global da AWS consiste em um ou mais data centers discretos com energia, rede e conectividade redundantes localizados em uma mesma área geográfica?"
- *Gabarito Correto:* **Availability Zone (Zona de Disponibilidade).**

---

## 4. Engenharia de Distratores Plausíveis

- **PROIBIÇÃO ABSOLUTA**: Nunca invente serviços inexistentes (ex: *AWS CloudSecure*, *Amazon AutoServer*, *AWS DataShield*).
- **Utilize serviços reais que pertençam à mesma categoria conceitual**, mas que tenham finalidades distintas:
  - Confundir **Amazon CloudWatch** (métricas e alarmes operacionais) com **AWS CloudTrail** (auditoria de chamadas de API).
  - Confundir **AWS Artifact** (relatórios de conformidade e auditoria) com **AWS Shield** (mitigação de ataques DDoS).
  - Confundir **AWS Cost Explorer** (análise e previsão histórica) com **AWS Budgets** (alertas de limites de gastos).
  - Confundir **Amazon EBS** (armazenamento em bloco para EC2) com **Amazon EFS** (sistema de arquivos compartilhado) e **Amazon S3** (armazenamento de objetos).
  - Confundir **Amazon Inspector** (avaliação de vulnerabilidades de software) com **Amazon GuardDuty** (detecção inteligente de ameaças em logs).

---

## 5. Regras Estritas de Formato de Opções

### Single Choice (Escolha Única)
- **Exatamente 4 opções (A, B, C, D)**.
- **1 alternativa correta** (`requiredChoices: 1`).
- Letras equilibradas entre A, B, C e D.

### Multiple Choice (Múltipla Escolha)
- **Select TWO (`requiredChoices: 2`)**: **Exatamente 5 opções (A, B, C, D, E)** com **2 respostas corretas**.
- No enunciado: `Qual das seguintes opções atenderá a essa necessidade? (Escolha duas.)` ou `(Escolha duas.)`.
- Gabaritos variados (`["A", "C"]`, `["B", "D"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
