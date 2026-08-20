# Domínio 4: Accelerate Workload Migration and Modernization (20%)

Este guia de referência detalha os cenários, arquiteturas e padrões de questões para o **Domínio 4** do exame SAP-C02.

---

## 🏗️ Padrões Arquiteturais Centrais

### 1. As 7 Estratégias de Migração (7 Rs)
| Estratégia | Definição | Caso de Uso Típico | Ferramental AWS Recomendado |
| :--- | :--- | :--- | :--- |
| **Rehost** (Lift-and-Shift) | Mover servidores para a AWS sem alterar a arquitetura, SO ou código. | Prazos curtos, fechamento urgente de data center. | **AWS Application Migration Service (MGN)** |
| **Relocate** (Hipervisor / Container) | Mover infraestrutura mantendo o mesmo hypervisor ou runtime de container sem reescrever imagens. | Cargas VMware legadas ou clusters Kubernetes. | **VMware Cloud on AWS (com VMware HCX)**, Amazon EKS / ECS |
| **Replatform** (Lift-tinker-and-shift) | Pequenas otimizações na infraestrutura sem alterar a lógica de negócios da aplicação. | Mover bancos auto-gerenciados para serviços gerenciados. | **Amazon RDS**, **AWS Elastic Beanstalk** |
| **Repurchase** (Drop-and-shop) | Substituição de software customizado ou proprietário por soluções SaaS/comerciais. | Troca de sistemas legados de CRM/ERP/RH por produtos parceiros. | **AWS Marketplace** |
| **Refactor / Re-architect** | Redesenho completo da aplicação para padrões nativos de nuvem e microsserviços. | Aplicações core que necessitam de escala massiva, agilidade e desacoplamento. | **AWS Lambda**, **Amazon ECS/EKS**, **Amazon DynamoDB**, **Step Functions** |
| **Retain** | Manter a carga de trabalho no data center on-premises por conformidade estrita ou dependência física. | Aplicações legadas com latência ultra-baixa com hardware fabril. | **AWS Outposts**, conectividade Direct Connect |
| **Retire** | Desativação de aplicações obsoletas ou redundantes. | Servidores de teste abandonados, softwares legados em desuso. | Inventário com **AWS Application Discovery Service** |

---

### 2. Ferramentas Essenciais de Migração de Dados e Servidores
- **AWS Application Migration Service (MGN):**
  - Serviço primário para Rehost automatizado de servidores físicos, máquinas virtuais (VMware, Hyper-V) ou instâncias em outras nuvens.
  - Instala o AWS Replication Agent nos servidores de origem.
  - Realiza replicação contínua e assíncrona em nível de bloco para volumes EBS em uma **Staging Area** de baixo custo.
  - Executa testes não disruptivos antes do cutover final com downtime mínimo (minutos).
- **AWS Database Migration Service (DMS) + Schema Conversion Tool (SCT):**
  - **AWS SCT:** Converte esquemas e código de banco de dados para migrações heterogêneas (ex: Oracle/SQL Server -> Amazon Aurora PostgreSQL/MySQL).
  - **AWS DMS:** Executa a migração inicial de dados (Full Load) e mantém a sincronização contínua com **Change Data Capture (CDC)** para corte com downtime próximo de zero.
- **AWS DataSync:**
  - Transferência automatizada de dados em alta velocidade pela rede (VPN ou Direct Connect) para Amazon S3, Amazon EFS ou Amazon FSx.
  - Otimiza a largura de banda, inclui criptografia em trânsito e valida a integridade dos dados transferidos.
- **AWS Snow Family (Migração Física de Dados):**
  - **AWS Snowcone:** 8 TB de armazenamento utilizável, portátil e leve (Edge computing / transferência moderada).
  - **AWS Snowball Edge Storage Optimized:** 80 TB a 210 TB de capacidade, ideal para migração offline de petabytes onde o link de internet é insuficiente.
  - **AWS Snowmobile:** Caminhão de dados com até 100 PB por unidade para migrações de escala de exabytes.

---

### 3. Integração e Armazenamento Híbrido Durante a Migração
- **AWS Storage Gateway:**
  - **Volume Gateway (Cached Mode):** Armazena dados primários no S3 e mantém cópias em cache localmente no data center para acesso de baixa latência.
  - **Volume Gateway (Stored Mode):** Armazena dados primários localmente e realiza backups assíncronos de snapshots para o S3 (EBS Snapshots).
  - **Tape Gateway:** Substitui fitas físicas locais por fitas virtuais no S3 e S3 Glacier Flexible / Deep Archive.
  - **Amazon FSx File Gateway:** Fornece cache local de baixa latência para compartilhamentos Amazon FSx for Windows File Server.

---

## 🎯 Modelos de Cenários de Questões para o Domínio 4

1. **Cenário de Migração de Data Center com Prazo Crítico:**
   - *Problema:* Uma organização precisa migrar 500 servidores físicos e virtuais de um data center que será desativado em 60 dias. O downtime durante o cutover deve ser de apenas alguns minutos por aplicação, e nenhuma modificação no código ou arquitetura é permitida no primeiro momento.
   - *Solução Correta:* Utilizar o **AWS Application Migration Service (MGN)** para instalar agentes de replicação nos servidores, realizar replicação contínua em nível de bloco para a staging area na AWS, validar os testes de lançamento e executar o cutover programado.

2. **Cenário de Migração Heterogênea de Banco de Dados com Zero Downtime:**
   - *Problema:* Uma empresa precisa migrar um banco de dados transacional Oracle crítico de 15 TB on-premises para o Amazon Aurora PostgreSQL. A aplicação transacional não pode sofrer mais de 10 minutos de inatividade durante a transição final.
   - *Solução Correta:* Utilizar o **AWS Schema Conversion Tool (SCT)** para converter o esquema e procedimentos armazenados para PostgreSQL. Configurar uma instância de replicação do **AWS Database Migration Service (DMS)** com migração de dados existente mais **Change Data Capture (CDC)** contínuo. Apontar a aplicação para o Aurora após sincronização completa.
