# Regras e Anatomia para Criação de Questões SAA-C03

O exame **AWS Certified Solutions Architect - Associate (SAA-C03)** avalia o conhecimento prático e arquitetural para projetar sistemas distribuídos robustos, eficientes, seguros e econômicos na AWS. Esta referência define as diretrizes para produzir questões no exato padrão da prova oficial.

---

## 1. Diferenciação de Níveis: CLF-C02 vs. SAA-C03 vs. SAP-C02

| Dimensão | CLF-C02 (Foundational) | SAA-C03 (Associate) | SAP-C02 (Professional) |
| :--- | :--- | :--- | :--- |
| **Escopo** | Conceitos fundamentais, definição de serviços, modelo de responsabilidade compartilhada e faturamento | **Arquitetura de Soluções Aplicada (1 a 4 serviços principais integrados em 1 ou 2 VPCs/contas)** | Arquitetura Enterprise End-to-End complexa (5 a 8+ serviços em centenas de contas/regiões) |
| **Enunciado** | 1 a 2 frases diretas | **2 a 4 frases estruturadas** com cenário de workload real, requisitos técnicos e restrições claras | 3 a 5 frases longas com histórico de legado, compliance e restrições cruzadas |
| **Opções** | 1 frase curta com nomes de serviços ou conceitos | **15 a 35 palavras por opção**, detalhando os passos técnicos de configuração na AWS | 25 a 50+ palavras por opção com passos profundos e parametrizações complexas |
| **Distratores** | Serviços com propósitos diferentes (ex: CloudWatch vs CloudTrail) | **Opções tecnicamente plausíveis (Matriz 2x2)**, onde distratores falham por restrições finas de custo, overhead ou protocolo | Arquiteturas completas válidas onde apenas nuances sutis ou limites não-transitivos desqualificam a opção |
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

### Exemplo "Padrão Ouro" (Single Choice - Matriz 2x2 Micro-Diff):
* **Enunciado**: Uma empresa de comércio eletrônico hospeda uma aplicação web de 3 camadas no Amazon EC2 em uma VPC privada atrás de um Application Load Balancer. As instâncias EC2 processam uploads de imagens de clientes e gravam os arquivos em um bucket Amazon S3. Durante campanhas promocionais, o tráfego de saída das instâncias para o Amazon S3 através dos NAT Gateways gera custos elevados de processamento de dados por gigabyte. Um arquiteto de soluções deve eliminar os custos de processamento do NAT Gateway para o tráfego do S3 sem modificar o código da aplicação e sem expor as instâncias à internet pública. Qual solução atenderá a esses requisitos com o MENOR custo?
* **Opções (A–D com Micro-Diff)**:
  * `A`: Configurar um Gateway VPC Endpoint para o Amazon S3 e associá-lo a todas as tabelas de rotas das sub-redes privadas da VPC. *(Correta)*
  * `B`: Configurar um Interface VPC Endpoint (AWS PrivateLink) para o Amazon S3 em cada sub-rede privada da VPC. *(Incorreta: Interface Endpoints cobram taxa horária e tarifa por GB transferido).*
  * `C`: Mover as instâncias EC2 para sub-redes públicas e associar endereços IP Elásticos a cada instância. *(Incorreta: expõe servidores à internet pública).*
  * `D`: Criar uma conexão AWS Direct Connect dedicada entre a VPC privada e o bucket Amazon S3. *(Incorreta: Direct Connect conecta data centers on-premises à AWS, não VPC ao S3).*

---

## 4. Matriz de Palavras-Chave e Gatilhos de Decisão (Decision Triggers)

| Gatilho no Enunciado | Favorece Soluções Com... | Desqualifica Soluções Com... |
| :--- | :--- | :--- |
| **"MENOR sobrecarga operacional"** | Serviços totalmente gerenciados / Serverless (ex: S3 Intelligent-Tiering, Secrets Manager, Aurora Serverless, EventBridge, Lambda, SSM Parameter Store) | Scripts customizados em instâncias EC2, cron jobs manuais, servidores de banco auto-hospedados em EC2. |
| **"MENOR custo"** / **"MAIS econômica"** | S3 Standard-IA / Glacier, VPC Gateway Endpoints para S3/DynamoDB (sem custo de NAT), Spot Instances (batch/tolerante a falha), Compute Savings Plans, Auto Scaling scale-in | NAT Gateways intermediando petabytes para S3, instâncias superdimensionadas, volumes Provisioned IOPS (io2) desnecessários. |
| **"SEM alterar o código da aplicação"** | Configurações no nível de infraestrutura (ex: RDS Multi-AZ, CloudFront com S3 OAC, AWS Systems Manager, Application Load Balancer Path-based routing) | Refatoração para DynamoDB, reescrita para arquitetura de microsserviços orientada a eventos. |
| **"MAIOR disponibilidade / Resiliência"** | Implantações Multi-AZ, Route 53 Failover com Health Checks, S3 Cross-Region Replication, filas SQS para desacoplar picos | Arquiteturas Single-AZ, instâncias EC2 individuais sem Auto Scaling, gravações síncronas sem fila de buffer. |
| **"Princípio do Menor Privilégio"** | Políticas IAM com recursos específicos (`Resource: arn:aws:s3:::bucket/*`), IAM Roles temporárias para instâncias, S3 Bucket Policies granulares | Políticas com `"Resource": "*"` e `"Action": "*"`, credenciais estáticas (Access Keys) embutidas no código. |

---

## 5. Regras Estritas de Formato de Opções

### Single Choice (Escolha Única)
- **Exatamente 4 opções (A, B, C, D)**.
- **1 alternativa correta** (`requiredChoices: 1`).
- Letra correta balanceada entre A, B, C e D.

### Multiple Choice (Múltipla Escolha)
- **Select TWO (`requiredChoices: 2`)**: **Exatamente 5 opções (A, B, C, D, E)** com **2 respostas corretas**.
- **Select THREE (`requiredChoices: 3`)**: **Exatamente 6 opções (A, B, C, D, E, F)** com **3 respostas corretas**.
- No enunciado: `Qual combinação de ações atenderá a esses requisitos? (Escolha duas.)` ou `(Escolha três.)`.
- Gabaritos variados (`["A", "C"]`, `["B", "D"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
