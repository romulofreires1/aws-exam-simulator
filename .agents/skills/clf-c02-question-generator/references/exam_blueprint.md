# AWS Certified Cloud Practitioner (CLF-C02) Blueprint

O exame **AWS Certified Cloud Practitioner (CLF-C02)** valida o conhecimento fundamental e abrangente sobre a Nuvem AWS, seus serviços centrais, modelo de segurança e conformidade, modelo de faturamento e precificação, e planos de suporte.

---

## 📊 Estrutura e Pesos Oficiais dos Domínios

| Domínio | Descrição Oficial | Peso (%) | Total de Questões (~65 Qs) |
| :--- | :--- | :---: | :---: |
| **Domínio 1** | **Cloud Concepts** | **24%** | ~15 - 16 questões |
| **Domínio 2** | **Security and Compliance** | **30%** | ~19 - 20 questões |
| **Domínio 3** | **Cloud Technology and Services** | **34%** | ~22 questões |
| **Domínio 4** | **Billing, Pricing, and Support** | **12%** | ~8 questões |
| **Total** | | **100%** | **65 questões (50 pontuadas + 15 não pontuadas)** |

---

## 🎯 Detalhamento dos Task Statements por Domínio

### Domínio 1: Cloud Concepts (24%)
- **Task Statement 1.1: Define the benefits of the AWS Cloud**
  - Proposta de valor da nuvem: Agilidade (velocidade de inovação), Elasticidade (provisionamento/desprovisionamento automático com a demanda), Alta Disponibilidade, Tolerância a Falhas e Escalabilidade.
  - Benefícios econômicos: Trocar despesas de capital (CapEx) por despesas operacionais variáveis (OpEx), economias de escala massivas da AWS e pagamento pelo que usar (Pay-as-you-go).
  - Alcance global em minutos através da infraestrutura mundial da AWS.
- **Task Statement 1.2: Identify design principles of the AWS Cloud**
  - Os 6 Pilares do **AWS Well-Architected Framework**:
    1. *Excelência Operacional (Operational Excellence)*
    2. *Segurança (Security)*
    3. *Confiabilidade (Reliability)*
    4. *Eficiência de Performance (Performance Efficiency)*
    5. *Otimização de Custos (Cost Optimization)*
    6. *Sustentabilidade (Sustainability)*
  - Princípios de design: Arquitetura fracamente acoplada (loose coupling), dimensionamento horizontal vs vertical, automação e eliminação de pontos únicos de falha (SPOF).
- **Task Statement 1.3: Understand the benefits of and strategies for migration to the AWS Cloud**
  - **AWS Cloud Adoption Framework (AWS CAF)**: 6 perspectivas (Negócios, Pessoas, Governança, Plataforma, Segurança, Operações).
  - Estratégias de migração de aplicações (as 6/7 Rs: Rehost, Relocate, Replatform, Repurchase, Refactor, Retain, Retire).

---

### Domínio 2: Security and Compliance (30%)
- **Task Statement 2.1: Understand the AWS Shared Responsibility Model**
  - **Segurança DA Nuvem (AWS):** Hardware físico, data centers, infraestrutura global, servidores host de virtualização e patches de serviços gerenciados (S3, DynamoDB, RDS engine).
  - **Segurança NA Nuvem (Cliente):** Dados do cliente, gerenciamento de IAM, sistema operacional convidado (SO de instâncias EC2), patches de SO/aplicações, firewall (Security Groups e NACLs) e configurações de criptografia.
- **Task Statement 2.2: Understand AWS Cloud security, governance, and compliance concepts**
  - Gerenciamento de acessos com **AWS IAM** (usuários, grupos, roles, políticas, MFA e credenciais de acesso).
  - Princípio do Menor Privilégio (Least Privilege) e melhores práticas para proteção da conta root da AWS.
  - Governança multi-contas com **AWS Organizations** e Service Control Policies (SCPs).
- **Task Statement 2.3: Identify AWS access management capabilities**
  - Autenticação e federação com AWS IAM Identity Center.
- **Task Statement 2.4: Identify security and compliance resources**
  - **AWS Artifact:** Portal de autoatendimento para download de relatórios de auditoria e conformidade (SOC, PCI-DSS, ISO, HIPAA) e acordos de conformidade da AWS.
  - **AWS Audit Manager:** Avaliação contínua do uso de recursos para simplificar relatórios de conformidade com padrões regulatórios.
  - **Serviços de Segurança:** AWS WAF, AWS Shield (Standard e Advanced), AWS KMS, Amazon GuardDuty, Amazon Inspector, Amazon Macie e AWS Security Hub.

---

### Domínio 3: Cloud Technology and Services (34%)
- **Task Statement 3.1: Understand methods of deploying and operating in the AWS Cloud**
  - Métodos de interação: AWS Management Console, AWS Command Line Interface (CLI), AWS SDKs e Infraestrutura como Código com **AWS CloudFormation**.
- **Task Statement 3.2: Understand the AWS Global Infrastructure**
  - **AWS Regions:** Localizações geográficas isoladas contendo múltiplas Zonas de Disponibilidade.
  - **Availability Zones (AZs):** Um ou mais data centers discretos com energia, rede e conectividade redundantes dentro de uma Região AWS.
  - **Edge Locations (Pontos de Presença):** Locais de borda usados pelo Amazon CloudFront, AWS Global Accelerator e Route 53 para entregar conteúdo com menor latência.
  - **AWS Outposts, Local Zones e Wavelength:** Extensões da infraestrutura da AWS para data centers locais, cidades metropolitanas e bordas de rede 5G.
- **Task Statement 3.3: Identify core AWS compute services**
  - Amazon EC2 (servidores virtuais), AWS Lambda (execução de código sem servidor), Amazon ECS e EKS (orquestração de containers Docker e Kubernetes), AWS Fargate (computação serverless para containers) e Amazon Lightsail (VPS simplificado).
- **Task Statement 3.4: Identify core AWS storage services**
  - Amazon S3 (armazenamento de objetos escalável), Amazon EBS (armazenamento em bloco para EC2), Amazon EFS (sistema de arquivos elástico NFS), AWS Backup (gestão centralizada de backups) e AWS Storage Gateway (integração de armazenamento híbrido).
- **Task Statement 3.5: Identify core AWS database services**
  - Amazon RDS (bancos relacionais gerenciados: PostgreSQL, MySQL, MariaDB, Oracle, SQL Server), Amazon Aurora (banco de dados relacional de alta performance e compatibilidade), Amazon DynamoDB (banco NoSQL de chave-valor e documento), Amazon ElastiCache (cache in-memory) e Amazon Redshift (data warehouse analítico).
- **Task Statement 3.6: Identify core AWS networking services**
  - Amazon VPC (rede virtual isolada), Subnets, Internet Gateway, NAT Gateway, Security Groups, Route 53 (DNS gerenciado) e Amazon CloudFront (CDN global).
- **Task Statement 3.7: Identify core AWS management and monitoring services**
  - Amazon CloudWatch (métricas operacionais, logs e alarmes), AWS CloudTrail (auditoria e rastreamento de chamadas de API), AWS Trusted Advisor (orientações e recomendações de melhores práticas) e AWS Health Dashboard (status da infraestrutura AWS e eventos da conta).

---

### Domínio 4: Billing, Pricing, and Support (12%)
- **Task Statement 4.1: Compare AWS pricing models**
  - Modelos de precificação EC2: On-Demand, Savings Plans, Reserved Instances (RIs) e Spot Instances.
  - Níveis do AWS Free Tier: Always Free, 12 Months Free e Short-Term Trials.
- **Task Statement 4.2: Understand billing, cost management, and cost allocation tools**
  - **AWS Billing Dashboard:** Visão geral e faturas mensais da conta.
  - **AWS Cost Explorer:** Visualização, análise e projeção de custos e padrões de uso históricos.
  - **AWS Budgets:** Definição de limites orçamentários personalizados com alertas automáticos por email/SNS.
  - **AWS Pricing Calculator:** Estimativa prévia do custo de arquiteturas e serviços na AWS.
  - **Cost Allocation Tags:** Tags chave-valor para rastrear e categorizar custos por departamento, projeto ou ambiente.
- **Task Statement 4.3: Understand AWS Support plans and resources**
  - Planos de Suporte:
    - **Basic:** Gratuito; acesso a documentação, fóruns, faturamento e 7 verificações básicas do Trusted Advisor.
    - **Developer:** Horário comercial por email; tempo de resposta de 12 a 24h para orientações gerais.
    - **Business:** Suporte 24/7 por chat, telefone e email; tempo de resposta < 1h para sistemas em produção degradados; acesso a todas as verificações do Trusted Advisor.
    - **Enterprise On-Ramp:** Suporte 24/7 com tempo de resposta < 30 min para incidentes críticos de negócios; pool de Technical Account Managers (TAM).
    - **Enterprise:** Suporte 24/7 com tempo de resposta < 15 min para sistemas de missão crítica indisponíveis; **Technical Account Manager (TAM) dedicado** e Concierge Support Team.
  - Recursos de parceiros: **AWS Partner Network (APN)** e **AWS Marketplace** (catálogo digital para descoberta e compra de softwares de terceiros).
