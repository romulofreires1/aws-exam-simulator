# AWS Certified Solutions Architect - Professional (SAP-C02) Blueprint

O exame SAP-C02 avalia a capacidade de projetar soluções avançadas em nuvem abrangendo requisitos complexos de resiliência, segurança, desempenho e governança enterprise.

---

## 📊 Estrutura e Pesos Oficiais dos Domínios

| Domínio | Descrição Oficial | Peso (%) | Total de Questões (~75 Qs) |
| :--- | :--- | :---: | :---: |
| **Domínio 1** | **Design Solutions for Organizational Complexity** | **26%** | ~19 - 20 questões |
| **Domínio 2** | **Design for New Solutions** | **29%** | ~21 - 22 questões |
| **Domínio 3** | **Continuous Improvement for Existing Solutions** | **25%** | ~18 - 19 questões |
| **Domínio 4** | **Accelerate Workload Migration and Modernization** | **20%** | ~15 - 16 questões |
| **Total** | | **100%** | **75 questões (65 pontuadas + 10 não pontuadas)** |

---

## 🎯 Detalhamento dos Task Statements por Domínio

### Domínio 1: Design Solutions for Organizational Complexity (26%)
- **Task Statement 1.1: Conectividade de Rede**
  - Transit Gateway (peering inter-regional, route tables isoladas, Appliance Mode).
  - Direct Connect (Dedicated vs Hosted Connections, Private/Public/Transit VIFs, redundância com VPN BGP failover, MACsec).
  - VPC Endpoints (Gateway vs Interface Endpoints com AWS PrivateLink, políticas de endpoint).
  - Resolução DNS corporativa com Route 53 Resolver (Inbound/Outbound Endpoints, regras de repasse e RAM).
- **Task Statement 1.2: Controles de Segurança Multi-Contas**
  - AWS Organizations e Service Control Policies (SCPs) com `Deny` explícito para impor conformidade de segurança e restrições geográficas.
  - IAM Identity Center (AWS Single Sign-On), federação SAML 2.0 com IdPs externos (Entra ID, Okta) e provisionamento SCIM.
  - Controle de Acesso Baseado em Atributos (ABAC) com tags de sessão (`aws:PrincipalTag`).
  - Compartilhamento seguro de recursos com AWS RAM (Transit Gateway, Subnets, Route 53 Resolver Rules).
- **Task Statement 1.3: Arquiteturas Confiáveis e Resilientes Multi-Contas**
  - Gerenciamento de cotas de serviço centralizado (Service Quotas + AWS Organizations).
  - Isolamento de falhas por conta e por região.
- **Task Statement 1.4: Governança e Ambientes Multi-Conta**
  - AWS Control Tower (Landing Zones, guardrails preventivos via SCPs, guardrails detectivos via AWS Config).
  - Centralização de logs com AWS CloudTrail (Organization Trail) e agregação no bucket S3 da conta de Log Archive.
- **Task Statement 1.5: Otimização e Visibilidade de Custos Organizacionais**
  - AWS Cost Categories, AWS Cost Anomaly Detection, faturamento consolidado e compartilhamento de Savings Plans.

---

### Domínio 2: Design for New Solutions (29%)
- **Task Statement 2.1: Estratégias de Implantação e Automação**
  - Infraestrutura como Código com AWS CloudFormation (StackSets multi-contas/multi-regiões, nested stacks, DeletionPolicy).
  - AWS CDK (Cloud Development Kit).
  - CI/CD com AWS CodePipeline, CodeBuild e CodeDeploy (blue/green, canary e linear deployments).
- **Task Statement 2.2: Continuidade de Negócios e Disaster Recovery**
  - Estratégias de DR: Backup & Restore, Pilot Light, Warm Standby, Multi-Site Active-Active.
  - RTO e RPO específicos para bancos e aplicações (Aurora Global Database, DRS, Redshift Cross-Region Snapshots).
  - AWS Route 53 Application Recovery Controller (ARC) e failover de DNS com Health Checks.
- **Task Statement 2.3: Controles de Segurança para Novas Soluções**
  - Proteção de borda com AWS WAF, AWS Shield Advanced e CloudFront.
  - Criptografia de dados em repouso e trânsito (KMS CMK, KMS Multi-Region, CloudHSM, ACM).
  - Gerenciamento e rotação de segredos com AWS Secrets Manager.
- **Task Statement 2.4: Requisitos de Confiabilidade**
  - Desacoplamento assíncrono com Amazon SQS, SNS e EventBridge.
  - Estratégias de Auto Scaling (Target Tracking, Step Scaling, Predictive Scaling) e políticas de saúde.
  - Sistemas de arquivos compartilhados Multi-AZ (Amazon EFS, FSx for ONTAP, FSx for Windows).
- **Task Statement 2.5: Objetivos de Desempenho**
  - Caching distribuído com Amazon ElastiCache (Redis/Memcached) e DynamoDB DAX.
  - Bancos de dados especializados (DynamoDB, Aurora Serverless v2, Neptune, Timestream).
  - Otimização de rede: AWS Global Accelerator, Enhanced Networking (SR-IOV) e Elastic Fabric Adapter (EFA).

---

### Domínio 3: Continuous Improvement for Existing Solutions (25%)
- **Task Statement 3.1: Excelência Operacional**
  - Automação de correções com AWS Systems Manager (Automation Documents, Run Command, Patch Manager).
  - Acesso seguro sem bastiões via SSM Session Manager.
  - Observabilidade com CloudWatch Logs Insights, Métricas customizadas, Alarmes e AWS X-Ray.
- **Task Statement 3.2: Melhoria de Segurança Contínua**
  - Centralização de segurança com AWS Security Hub e AWS GuardDuty.
  - Varredura de vulnerabilidades com Amazon Inspector v2 em EC2, ECR e Lambda.
  - Descoberta de PII com Amazon Macie em data lakes S3.
  - Análise de privilégios com IAM Access Analyzer.
- **Task Statement 3.3: Melhoria de Performance**
  - Análise de gargalos com AWS Compute Optimizer e RDS Performance Insights.
  - Tuning de conexões de banco de dados com Amazon RDS Proxy.
- **Task Statement 3.4: Melhoria de Confiabilidade**
  - Testes de resiliência e injeção controlada de falhas com AWS Fault Injection Simulator (FIS).
- **Task Statement 3.5: Otimização de Custos Contínua**
  - Compute Savings Plans vs EC2 Instance Savings Plans vs RIs.
  - S3 Lifecycle Policies (S3 Standard -> Intelligent-Tiering -> Glacier Flexible -> Glacier Deep Archive).
  - Relatórios de custos avançados com Cost and Usage Report (CUR) consultado via Amazon Athena.

---

### Domínio 4: Accelerate Workload Migration and Modernization (20%)
- **Task Statement 4.1: Planejamento e Avaliação de Migração**
  - As 7 estratégias de migração (7 Rs): Rehost, Relocate, Replatform, Repurchase, Refactor, Retain, Retire.
  - Descoberta e inventário de aplicações com AWS Application Discovery Service e Migration Evaluator.
  - Priorização de ondas de migração (Wave Planning).
- **Task Statement 4.2: Abordagem de Migração Ideal**
  - AWS Application Migration Service (MGN) para lift-and-shift automatizado de servidores com staging area e cutover rápido.
  - AWS Database Migration Service (DMS) + Schema Conversion Tool (SCT) para migrações heterogêneas com replicação contínua CDC.
  - Migração de dados acelerada via rede com AWS DataSync.
  - Migração física em larga escala com AWS Snow Family (Snowball Edge Storage/Compute Optimized, Snowmobile).
- **Task Statement 4.3: Arquitetura para Cargas Migradas**
  - Hibridismo e transição com VMware Cloud on AWS (VMC) usando VMware HCX.
  - Armazenamento híbrido com AWS Storage Gateway (Volume Gateway, Tape Gateway, File Gateway / FSx File Gateway).
- **Task Statement 4.4: Oportunidades de Modernização**
  - Decomposição de monólitos em microsserviços via Amazon ECS, Amazon EKS e AWS Fargate.
  - Modernização para arquiteturas Serverless com AWS Lambda, Step Functions e Amazon EventBridge.
