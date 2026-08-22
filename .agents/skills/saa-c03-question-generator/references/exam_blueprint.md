# AWS Certified Solutions Architect - Associate (SAA-C03) Blueprint

O exame **AWS Certified Solutions Architect - Associate (SAA-C03)** avalia a capacidade de projetar soluções seguras, resilientes, de alto desempenho e otimizadas em termos de custo, com base nos pilares do AWS Well-Architected Framework.

---

## 📊 Estrutura e Pesos Oficiais dos Domínios

| Domínio | Descrição Oficial | Peso (%) | Questões (~65 Qs) |
| :--- | :--- | :---: | :---: |
| **Domínio 1** | **Design Secure Architectures** | **30%** | ~19 - 20 questões |
| **Domínio 2** | **Design Resilient Architectures** | **26%** | ~17 questões |
| **Domínio 3** | **Design High-Performing Architectures** | **24%** | ~15 - 16 questões |
| **Domínio 4** | **Design Cost-Optimized Architectures** | **20%** | ~13 questões |
| **Total** | | **100%** | **65 questões (50 pontuadas + 15 não pontuadas)** |

---

## 🎯 Detalhamento dos Task Statements por Domínio

### Domínio 1: Design Secure Architectures (30%)
- **Task Statement 1.1: Design secure access to AWS resources**
  - Gerenciamento de identidades e permissões com AWS IAM (usuários, grupos de usuários, funções/roles, políticas gerenciadas vs inline).
  - Princípio do Menor Privilégio (Least Privilege) e políticas baseadas em recursos (Resource-based policies).
  - Autenticação multifator (MFA) e proteção de credenciais temporárias via AWS STS (AssumeRole).
  - Gerenciamento centralizado de segredos com AWS Secrets Manager e armazenamento de parâmetros com AWS Systems Manager Parameter Store.
  - Guardrails organizacionais básicos com AWS Organizations e Service Control Policies (SCPs).
- **Task Statement 1.2: Design secure workloads and applications**
  - Isolamento de rede em VPCs: subnets públicas vs privadas, route tables, Internet Gateways (IGW), NAT Gateways.
  - Segurança de rede: Security Groups (stateful) vs Network Access Control Lists - NACLs (stateless).
  - Proteção de aplicações web e mitigação de DDoS com AWS WAF e AWS Shield (Standard e Advanced).
  - Detecção contínua de ameaças com Amazon GuardDuty, avaliação de vulnerabilidades com Amazon Inspector e detecção de dados confidenciais com Amazon Macie.
  - Conectividade privada a serviços AWS via VPC Endpoints (Gateway Endpoints para S3/DynamoDB e Interface Endpoints com AWS PrivateLink).
- **Task Statement 1.3: Determine appropriate data security controls**
  - Criptografia em repouso (KMS CMK, SSE-S3, SSE-KMS, SSE-C) e em trânsito (TLS/HTTPS, AWS Certificate Manager - ACM).
  - Controle de acesso a dados no Amazon S3: Bucket Policies, Access Points, Origin Access Control (OAC) para CloudFront, S3 Block Public Access.
  - Imutabilidade e conformidade de dados com Amazon S3 Object Lock (modo Compliance vs Governance) e Vault Lock do AWS Backup.

---

### Domínio 2: Design Resilient Architectures (26%)
- **Task Statement 2.1: Design scalable and loosely coupled architectures**
  - Desacoplamento assíncrono com Amazon SQS (filas Standard vs FIFO, Dead-Letter Queues - DLQ, delay queues).
  - Publicação/inscrição (Pub/Sub) e fanout de notificações com Amazon SNS.
  - Arquiteturas orientadas a eventos com Amazon EventBridge (regras, barramentos de eventos personalizados e de terceiros).
  - Orquestração serverless com AWS Step Functions e APIs escaláveis com Amazon API Gateway.
  - Balanceamento de carga com Elastic Load Balancing (Application Load Balancer - ALB, Network Load Balancer - NLB, Gateway Load Balancer - GWLB).
  - Auto escalabilidade com Amazon EC2 Auto Scaling (políticas Target Tracking, Step Scaling, Simple Scaling e agendadas).
- **Task Statement 2.2: Design highly available and/or fault-tolerant architectures**
  - Implantações Multi-AZ no Amazon RDS e Amazon Aurora para alta disponibilidade com failover automático síncrono.
  - Réplicas de leitura (Read Replicas) locais e cross-region para escalabilidade de leitura e recuperação.
  - Estratégias de replicação no Amazon S3: Cross-Region Replication (CRR) e Same-Region Replication (SRR).
  - Políticas de roteamento no Amazon Route 53: Simple, Weighted, Latency, Failover (ativo-passivo com Health Checks), Geolocation, Geoproximity e Multi-Value Answer.
  - Estratégias de Disaster Recovery (DR): Backup & Restore, Pilot Light, Warm Standby e Multi-Site Active-Active.

---

### Domínio 3: Design High-Performing Architectures (24%)
- **Task Statement 3.1: Determine high-performing and/or scalable storage solutions**
  - Classes de armazenamento do Amazon S3 (S3 Standard, S3 Express One Zone, S3 Standard-IA, S3 One Zone-IA).
  - Armazenamento em bloco de alto desempenho com Amazon EBS (gp3, io2 Block Express) e otimização de IOPS/throughput.
  - Sistemas de arquivos compartilhados escaláveis: Amazon EFS (para Linux) e Amazon FSx (FSx for Windows File Server, FSx for Lustre para HPC/ML).
- **Task Statement 3.2: Design high-performing and elastic compute solutions**
  - Seleção de famílias e tipos de instâncias EC2 (General Purpose, Compute Optimized, Memory Optimized, Storage Optimized, processadores AWS Graviton).
  - Computação Serverless com AWS Lambda (concorrência provisionada, limites de memória/tempo de execução).
  - Containers elásticos com Amazon ECS e Amazon EKS (ecossistema AWS Fargate para gerenciamento serverless).
- **Task Statement 3.3: Determine high-performing database solutions**
  - Dimensionamento e escalabilidade do Amazon Aurora (Aurora Serverless v2, Global Database, auto scaling de réplicas).
  - Bancos NoSQL de baixa latência em milissegundos com Amazon DynamoDB e aceleração em memória com DynamoDB Accelerator (DAX).
  - Caching distribuído na camada de dados e aplicação com Amazon ElastiCache (Redis OSS / Valkey e Memcached).
  - Data warehousing analítico de alto desempenho com Amazon Redshift.
- **Task Statement 3.4: Design high-performing and/or scalable network architectures**
  - Distribuição global de conteúdo e aceleração estática/dinâmica com Amazon CloudFront.
  - Aceleração de tráfego TCP/UDP via rede global Anycast da AWS com AWS Global Accelerator.
  - Conectividade de rede: VPC Peering, AWS Transit Gateway, AWS Site-to-Site VPN e AWS Direct Connect.
- **Task Statement 3.5: Determine high-performing data ingestion and transformation solutions**
  - Ingestão de streaming em tempo real com Amazon Kinesis Data Streams e entrega gerenciada com Amazon Kinesis Data Firehose.
  - ETL serverless e catálogo de dados com AWS Glue e consultas interativas com Amazon Athena.

---

### Domínio 4: Design Cost-Optimized Architectures (20%)
- **Task Statement 4.1: Design cost-optimized storage solutions**
  - Gerenciamento automático de ciclo de vida no S3 com S3 Lifecycle Policies e S3 Intelligent-Tiering para padrões de acesso variáveis/desconhecidos.
  - Arquivamento de longo prazo de baixo custo com S3 Glacier Flexible Archive e S3 Glacier Deep Archive.
  - Otimização de custo em EBS (migração de gp2 para gp3, dimensionamento correto de volumes) e EFS Infrequent Access (EFS IA).
- **Task Statement 4.2: Design cost-optimized compute solutions**
  - Modelos de precificação computacional: Instâncias Sob Demanda (On-Demand), Instâncias Spot (cargas tolerantes a falhas/batch) e Savings Plans (Compute vs EC2 Instance Savings Plans).
  - Migração de workloads para AWS Graviton (melhor relação custo/performance).
  - Dimensionamento automático orientado a custos (EC2 Auto Scaling scale-in e suspensão de ambientes fora do horário comercial).
- **Task Statement 4.3: Design cost-optimized database solutions**
  - Modos de capacidade do Amazon DynamoDB: Provisioned (cargas previsíveis) vs On-Demand (cargas intermitentes/picos imprevisíveis).
  - Dimensionamento econômico de banco relacional: Aurora Serverless v2 vs RDS Reserved Instances.
- **Task Statement 4.4: Design cost-optimized network architectures**
  - Redução de custos de transferência de dados (Data Transfer Out - DTO): uso de Amazon CloudFront para transferências de borda com desconto.
  - Eliminação de custos de processamento de NAT Gateway para tráfego interno ao S3 e DynamoDB através de **VPC Gateway Endpoints** (gratuitos).
  - Escolha entre VPC Peering (sem custo por hora de anexo) e AWS Transit Gateway com base na complexidade e volume de dados.
