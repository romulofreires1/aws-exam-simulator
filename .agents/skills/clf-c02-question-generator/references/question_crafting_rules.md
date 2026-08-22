# Regras e Anatomia para Criação de Questões CLF-C02

O exame **AWS Certified Cloud Practitioner (CLF-C02)** avalia o conhecimento fundamental dos conceitos de computação em nuvem, serviços centrais da AWS, modelo de segurança compartilhada, precificação e suporte técnico. Esta referência define as diretrizes para produzir questões no exato padrão da prova oficial.

---

## 1. Características do Nível Foundational (CLF-C02)

| Dimensão | CLF-C02 (Foundational) | SAA-C03 (Associate) |
| :--- | :--- | :--- |
| **Público-Alvo** | Profissionais em início de jornada em nuvem, gerentes de produto, vendas técnicas, finanças e TI | Arquitetos de soluções, desenvolvedores e engenheiros de infraestrutura |
| **Tipo de Pergunta** | Identificação direta de serviços, papéis de responsabilidade, pilares do Well-Architected e planos de suporte | Cenários de arquitetura aplicada com múltiplos requisitos conflitantes (RTO/RPO, custos, rede) |
| **Extensão do Enunciado** | **1 a 2 frases claras e objetivas** | 2 a 3 frases com contexto de arquitetura e restrições |
| **Extensão das Opções** | **1 frase curta (1 a 2 linhas)** com termos técnicos precisos | 2 a 4 linhas detalhando passos de configuração |
| **Distratores** | Serviços ou conceitos reais da AWS com propósitos distintos da pergunta | Soluções técnicas válidas que falham em trade-offs de custo/overhead |
| **Tempo / Questão** | **~1 min 23 s (83 segundos)** (90 min / 65 q) | **2 min (120 s)** (130 min / 65 q) |

---

## 2. Regra Obrigatória de Embaralhamento de Gabaritos

Para garantir integridade dos simulados:
1. **PROIBIDO Gabarito Fixo em A ou A/B**:
   - Nunca fixe a resposta correta na opção `A` ou nas opções `A` e `B`.
2. **Distribuição Equilibrada**:
   - As respostas corretas **DEVEM** ser distribuídas de forma homogênea (~25% para cada letra `A`, `B`, `C`, `D` em questões de escolha única).
   - Em múltipla escolha, varie os pares (`["A", "C"]`, `["B", "D"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
3. **Explicações Coerentes**:
   - Cada opção deve ter uma explicação individual (`explanation`), iniciando com `Correto: ` ou `Incorreto: `, detalhando claramente o porquê.

---

## 3. Padrões de Formulação de Perguntas CLF-C02

As questões do exame Cloud Practitioner seguem principalmente 5 arquétipos:

### Padrão 1: Identificação de Serviço por Propósito
- *Exemplo:* "Uma empresa precisa executar código em resposta a eventos sem provisionar ou gerenciar servidores físicos ou virtuais. Qual serviço da AWS atende a essa necessidade?"
- *Gabarito Correto:* **AWS Lambda** (Serverless Compute).

### Padrão 2: Modelo de Responsabilidade Compartilhada
- *Exemplo:* "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes tarefas é de responsabilidade exclusiva do cliente ao executar uma instância Amazon EC2?"
- *Gabarito Correto:* **Instalação de patches no sistema operacional convidado e configuração de regras de firewall (Security Groups).**

### Padrão 3: Pilares do AWS Well-Architected Framework
- *Exemplo:* "Qual pilar do AWS Well-Architected Framework se concentra na capacidade de executar e monitorar sistemas para entregar valor ao negócio e melhorar continuamente os processos e procedimentos operacionais?"
- *Gabarito Correto:* **Excelência Operacional (Operational Excellence).**

### Padrão 4: Planos de Suporte e Governança Financeira
- *Exemplo:* "Qual plano de suporte da AWS inclui acesso a um Technical Account Manager (TAM) dedicado para fornecer orientações proativas e revisões arquiteturais regulares?"
- *Gabarito Correto:* **AWS Enterprise Support.**

### Padrão 5: Infraestrutura Global da AWS
- *Exemplo:* "Qual componente da infraestrutura global da AWS consiste em um ou mais data centers discretos com energia, rede e conectividade redundantes localizados em uma mesma área geográfica?"
- *Gabarito Correto:* **Availability Zone (Zona de Disponibilidade).**

---

## 4. Engenharia de Distratores Plausíveis

- **Nunca invente serviços inexistentes** (ex: *AWS CloudSecure*, *Amazon AutoServer*).
- **Utilize serviços reais que pertençam à mesma categoria conceitual**, mas que tenham finalidades distintas:
  - Confundir **Amazon CloudWatch** (métricas e alarmes operacionais) com **AWS CloudTrail** (auditoria de chamadas de API).
  - Confundir **AWS Artifact** (relatórios de conformidade) com **AWS Shield** (mitigação de ataques DDoS).
  - Confundir **AWS Cost Explorer** (análise e previsão histórica) com **AWS Budgets** (alertas de limites de gastos).
  - Confundir **Amazon EBS** (armazenamento em bloco para EC2) com **Amazon EFS** (sistema de arquivos compartilhado) e **Amazon S3** (armazenamento de objetos).

---

## 5. Regras de Formato

### Single Choice (Escolha Única)
- **4 opções (A, B, C, D)**.
- **1 alternativa correta** (`requiredChoices: 1`).
- Letras equilibradas entre A, B, C e D.

### Multiple Choice (Múltipla Escolha)
- **5 opções (A, B, C, D, E)** com **2 respostas corretas** (`requiredChoices: 2`).
- No enunciado: `**Qual das seguintes opções atenderá a essa necessidade? (Escolha duas.)**` ou `(Escolha duas.)`.
