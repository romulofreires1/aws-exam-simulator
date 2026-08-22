# Regras e Anatomia para Criação de Questões SAA-C03

O exame **AWS Certified Solutions Architect - Associate (SAA-C03)** avalia o conhecimento prático e arquitetural para projetar sistemas distribuídos robustos, eficientes, seguros e econômicos na AWS. Esta referência define as diretrizes para produzir questões no exato padrão da prova oficial.

---

## 1. Diferenciação de Níveis: CLF-C02 vs. SAA-C03 vs. SAP-C02

| Dimensão | CLF-C02 (Foundational) | SAA-C03 (Associate) | SAP-C02 (Professional) |
| :--- | :--- | :--- | :--- |
| **Escopo** | Conceitos fundamentais, definição de serviços, modelo de responsabilidade compartilhada e faturamento | **Arquitetura de Aplicações e Soluções (1 a 4 serviços principais integrados em 1 ou 2 contas/VPCs)** | Arquitetura Enterprise End-to-End complexa (5 a 8+ serviços em centenas de contas/regiões) |
| **Enunciado** | 1 a 2 frases diretas | **2 a 3 frases estruturadas** com cenário de workload real, requisitos técnicos e restrições claras | 3 a 5 frases longas com histórico de legado, compliance e restrições cruzadas |
| **Opções** | 1 frase curta com nomes de serviços ou conceitos | **2 a 4 linhas por opção**, detalhando os passos técnicos de configuração na AWS | 3 a 6 linhas por opção com passos profundos e parametrizações complexas |
| **Distratores** | Serviços com propósitos diferentes (ex: CloudWatch vs CloudTrail) | **Opções tecnicamente plausíveis**, mas que violam uma restrição (ex: custo excessivo, sobrecarga de scripts manuais, failover imperfeito) | Arquiteturas completas válidas onde apenas nuances sutis ou limites não-transitivos desqualificam a opção |
| **Tempo / Questão** | ~1 min 23 s (90 min / 65 q) | **2 min (120 s)** (130 min / 65 q) | **2 min 56 s (176 s)** (220 min / 75 q) |

---

## 2. Regra de Embaralhamento e Distribuição de Gabaritos (OBRIGATÓRIO)

Para evitar qualquer viés de resposta:
1. **PROIBIDO Gabarito Fixo em A ou A/B**:
   - Nunca coloque sempre a opção `A` como correta.
2. **Distribuição Equilibrada**:
   - Em qualquer lote gerado, distribua os gabaritos de forma balanceada:
     - **Escolha Única (Single Choice)**: ~25% `A`, ~25% `B`, ~25% `C`, ~25% `D`.
     - **Múltipla Escolha (Multiple Choice)**: Pares balanceados (ex: `["B", "D"]`, `["A", "C"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
3. **Explicações Coerentes**:
   - Cada opção deve conter sua própria explicação (`explanation`), iniciando com `Correto: ` / `Correct: ` ou `Incorreto: ` / `Incorrect: `.

---

## 3. Anatomia de uma Questão SAA-C03

Toda questão deve ser composta por 4 elementos:

```
[1. CONTEXTO DA APLICAÇÃO & INFRAESTRUTURA ATUAL]
+ [2. NOVO REQUISITO OU PROBLEMA A RESOLVER]
+ [3. RESTRIÇÃO ESPECÍFICA (EX: CUSTO, RESILIÊNCIA, SEM ALTERAR CÓDIGO)]
+ [4. DIRETIVA DE DECISÃO FINAL (GATILHO EM NEGRITO)]
```

### Exemplo de Estrutura:
1. **Contexto:** Uma empresa hospeda uma aplicação web de 3 camadas no Amazon EC2 atrás de um Application Load Balancer, persistindo transações em uma instância de banco de dados Amazon RDS PostgreSQL Single-AZ.
2. **Problema/Requisito:** A equipe de produtos necessita que a base de dados suporte failover de alta disponibilidade automático sem intervenção manual e com perda zero de dados em caso de falha de hardware ou indisponibilidade de zona.
3. **Restrição:** A solução deve minimizar a sobrecarga de manutenção e não exigir alterações no código de conexão da aplicação.
4. **Gatilho de Decisão:** *Qual solução atenderá a esses requisitos de forma MAIS eficiente?*

---

## 4. Matriz de Palavras-Chave e Gatilhos de Decisão (Decision Triggers)

| Gatilho no Enunciado | Favorece Soluções Com... | Desqualifica Soluções Com... |
| :--- | :--- | :--- |
| **"MENOR sobrecarga operacional"** / **"MAIS eficiente operacionalmente"** | Serviços totalmente gerenciados / Serverless (ex: S3 Intelligent-Tiering, Secrets Manager, Aurora Serverless, EventBridge, Lambda, SSM Parameter Store) | Scripts customizados em instâncias EC2, cron jobs manuais, servidores de banco auto-hospedados em EC2. |
| **"MENOR custo"** / **"MAIS econômica"** | S3 Standard-IA / Glacier, VPC Gateway Endpoints para S3/DynamoDB (sem custo de NAT), Spot Instances (batch/tolerante a falha), Compute Savings Plans, Auto Scaling scale-in | NAT Gateways intermediando petabytes para S3, instâncias superdimensionadas, volumes Provisioned IOPS (io2) desnecessários. |
| **"SEM alterar o código da aplicação"** | Configurações no nível de infraestrutura (ex: RDS Multi-AZ, CloudFront com S3 OAC, AWS Systems Manager, Application Load Balancer Path-based routing) | Refatoração para DynamoDB, reescrita para arquitetura de microsserviços orientada a eventos. |
| **"MAIOR disponibilidade / Resiliência"** | Implantações Multi-AZ, Route 53 Failover com Health Checks, S3 Cross-Region Replication, filas SQS para desacoplar picos | Arquiteturas Single-AZ, instâncias EC2 individuais sem Auto Scaling, gravações síncronas sem fila de buffer. |
| **"Princípio do Menor Privilégio"** | Políticas IAM com recursos específicos (`Resource: arn:aws:s3:::bucket/*`), IAM Roles temporárias para instâncias, S3 Bucket Policies granulares | Políticas com `"Resource": "*"` e `"Action": "*"`, credenciais estáticas (Access Keys) embutidas no código. |

---

## 5. Engenharia de Distratores Plausíveis (Matriz 2x2)

Em questões SAA-C03, não crie opções absurdas. Utilize o modelo de pares:
- **Abordagem A (2 opções: ex. A e B)**: Usa o serviço correto ou padrão recomendado (ex: *Amazon S3 + CloudFront + Origin Access Control*).
  - Uma acerta a configuração precisa (habilita OAC e restringe a política do bucket S3).
  - A outra comete um erro técnico comum (configura uma política pública no S3 ou usa o legado Origin Access Identity - OAI incorretamente).
- **Abordagem B (2 opções: ex. C e D)**: Usa uma abordagem arquitetural alternativa que não é a mais indicada para o caso de uso.
  - Ex: Tenta colocar o S3 dentro de uma VPC privada com NAT Gateway, ou cria instâncias EC2 para fazer proxy de arquivos estáticos.

---

## 6. Regras de Formato

### Single Choice (Escolha Única)
- **4 opções (A, B, C, D)**.
- **1 alternativa correta** (`requiredChoices: 1`).
- Letra correta embaralhada de forma balanceada.

### Multiple Choice (Múltipla Escolha)
- **5 opções (A, B, C, D, E)** com **2 respostas corretas** (`requiredChoices: 2`).
- No enunciado: `**Qual combinação de ações atenderá a esses requisitos? (Escolha duas.)**`
- Gabaritos variados (`["A", "C"]`, `["B", "D"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
