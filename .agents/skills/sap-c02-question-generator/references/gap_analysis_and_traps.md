# Padrões Arquiteturais Enterprise e Armadilhas do Exame SAP-C02

Esta referência compila os principais tópicos e arquiteturas enterprise avaliadas no exame **AWS Certified Solutions Architect - Professional (SAP-C02)**, além das armadilhas clássicas de formulação de questões.

---

## 🚀 Principais Padrões Arquiteturais Avaliados no Exame

### 1. IAM Identity Center (AWS SSO) + SCIM + ABAC
- **Padrão:** Federação SAML 2.0 com IdPs corporativos (Microsoft Entra ID / Okta) na conta de gerenciamento.
- **Diferencial SAP:** Provisionamento automático de usuários e grupos via **SCIM**. Uso de **Attribute-Based Access Control (ABAC)** repassando atributos de sessão (`aws:PrincipalTag/Department`, `aws:PrincipalTag/CostCenter`) para evitar a criação de centenas de IAM Roles individuais para cada departamento.

### 2. AWS Organizations + SCPs Avançadas + Control Tower
- **Padrão:** Estrutura de OUs (Core, Security, Workloads, Sandbox), SCPs com `Explicit Deny` aplicadas na raiz ou OUs.
- **Diferencial SAP:**
  - SCPs aplicam-se a todos os usuários e roles das contas-membro, **inclusive ao usuário root da conta-membro**. SCPs **não** afetam a conta de gerenciamento (Management Account).
  - Herança de SCPs: Se qualquer SCP pai negar uma ação, ela estará negada para todas as OUs e contas filhas.
  - Customizações do Control Tower: Customizations for Control Tower (CfCT) e Account Factory for Terraform (AFT).
  - Service Control Policies para impor criptografia (`rds:StorageEncrypted == false`), restrição de regiões (`aws:RequestedRegion`) e proteção de logs do CloudTrail.

### 3. Transit Gateway + VPC de Inspeção Central (Appliance Mode & Network Firewall)
- **Padrão:** Hub-and-spoke com centenas de VPCs e Direct Connect.
- **Diferencial SAP:**
  - Inspeção centralizada de tráfego Leste-Oeste (VPC para VPC) e Norte-Sul (Internet/On-prem).
  - Habilitação do **Appliance Mode** no Transit Gateway VPC Attachment para garantir roteamento simétrico através de firewalls com estado (AWS Network Firewall ou NGFW de terceiros com Gateway Load Balancer - GWLB).
  - Não requer SNAT, preservando o IP original do cliente.

### 4. Resolução DNS Híbrida Corporativa com Route 53 Resolver
- **Padrão:** Comunicação entre on-premises (`.corp.local`) e AWS (`.aws.internal`).
- **Diferencial SAP:**
  - **Inbound Endpoints:** Permitem que servidores DNS on-premises resolvam Route 53 Private Hosted Zones na AWS.
  - **Outbound Endpoints + Forwarding Rules:** Permitem que instâncias na AWS resolvam domínios on-premises.
  - Compartilhamento de Forwarding Rules entre contas via **AWS RAM** (Resource Access Manager).
  - **Route 53 Resolver DNS Firewall** para bloqueio de domínios maliciosos e data exfiltration via DNS.

### 5. AWS PrivateLink & VPC Endpoint Services em Escala
- **Padrão:** Compartilhar microsserviços entre provedores e dezenas/centenas de clientes sem abrir para a internet.
- **Diferencial SAP:**
  - Exposição de serviços via **Internal Network Load Balancer (NLB)** + **VPC Endpoint Service**.
  - Permite comunicação privada mesmo com **blocos CIDR sobrepostos** (overlap) entre VPCs de clientes e a VPC do provedor.
  - Controle de acesso fino através de **Endpoint Policies** e IAM Principals autorizados.

### 6. Banco de Dados Multi-Região: Aurora Global vs. DynamoDB Global Tables
- **Padrão:** Cargas de trabalho globais de baixa latência e alta disponibilidade.
- **Diferencial SAP:**
  - **Aurora Global Database:** Replicação física a nível de storage com latência típica < 1 segundo. Suporta failover gerenciado com RTO < 1 minuto e sem perda de dados (RPO = 0 ou near-zero). Permite até 5 regiões secundárias de leitura com até 16 réplicas cada.
  - **DynamoDB Global Tables:** Replicação ativo-ativo multi-região totalmente gerenciada com resolução de conflitos ("last writer wins"). RPO/RTO em milissegundos.
  - **RDS Cross-Region Read Replicas:** Replicação lógica assíncrona. Promoção a primário exige reinicialização e atualização de DNS manual/scriptada (RTO maior).

### 7. Disaster Recovery Avançado: AWS DRS vs. Route 53 ARC
- **Padrão:** Recuperação rápida de falhas zonais ou regionais.
- **Diferencial SAP:**
  - **AWS Elastic Disaster Recovery (DRS):** Replicação contínua em nível de bloco de servidores físicos, virtuais ou instâncias EC2 para uma região de DR em staging area de baixo custo. RPO em segundos e RTO em minutos.
  - **AWS Route 53 Application Recovery Controller (ARC):**
    - **Readiness Checks:** Monitora continuamente se os recursos na região de standby estão prontos para receber tráfego antes de autorizar o failover.
    - **Routing Controls & Safety Rules:** Permite alternância rápida de tráfego de DNS evitando failover em cascata ou envio de tráfego para regiões não saudáveis.

### 8. Governança de Data Lakes Enterprise: AWS Lake Formation & Glue
- **Padrão:** Data Lake centralizado em Amazon S3 consumido por múltiplas contas e ferramentas analíticas (Athena, Redshift Spectrum, EMR).
- **Diferencial SAP:**
  - **AWS Lake Formation:** Controle de acesso granular a nível de banco de dados, tabela, coluna, linha e célula.
  - Compartilhamento de dados federado entre contas sem duplicação de dados (Lake Formation cross-account grants).
  - Substitui políticas IAM e S3 Bucket Policies excessivamente complexas.

### 9. Armazenamento Avançado: Suíte Amazon FSx (ONTAP, OpenZFS, Windows)
- **Padrão:** Compartilhamento de arquivos corporativos de alta performance.
- **Diferencial SAP:**
  - **FSx for NetApp ONTAP:** Suporte a protocolos NFS, SMB e iSCSI. Tiering automático de dados frios para S3 (capacidade infinita). SnapMirror entre regiões para DR. Deduplicação e compactação integradas.
  - **FSx for Windows File Server:** Integração nativa Multi-AZ com Microsoft Active Directory corporativo, DFS Namespaces e SMB.
  - **FSx for Lustre:** Alta performance para HPC, processamento de vídeo e machine learning conectado diretamente a buckets S3.

### 10. Centralização de Segurança & Remediação Automatizada
- **Padrão:** Detecção e resposta contínua a ameaças.
- **Diferencial SAP:**
  - **AWS GuardDuty:** Detecção inteligente com ML em CloudTrail, VPC Flow Logs, DNS Logs, S3 Data Events, EKS Audit Logs e RDS Login Events.
  - **AWS Security Hub:** Centralização de achados de múltiplos serviços (GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager).
  - **Remediação Automatizada:** Security Hub -> EventBridge Custom Rule -> AWS Systems Manager Automation Runbook ou AWS Lambda.
  - **AWS Macie:** Descoberta e classificação automática de PII (dados sensíveis) em S3.

### 11. Criptografia Enterprise & Gestão de Chaves (AWS KMS)
- **Padrão:** Criptografia em repouso e em trânsito com conformidade estrita.
- **Diferencial SAP:**
  - **KMS Multi-Region Keys:** Chaves primárias e réplicas que compartilham o mesmo Key ID e material criptográfico em diferentes regiões, permitindo descriptografar dados replicados sem re-criptografia.
  - **KMS Grants:** Permissões temporárias e refinadas para permitir que serviços (ex: Auto Scaling, EBS) usem CMKs gerenciadas pelo cliente.
  - **KMS Key Policies:** A política da chave é o principal mecanismo de controle; sem concessão explícita na Key Policy, nem o administrador IAM da conta consegue usar a chave.
  - **CloudHSM:** Exigido quando normas de conformidade (FIPS 140-2 Nível 3) exigem controle exclusivo do hardware criptográfico dedicado.

### 12. FinOps & Otimização de Custos Enterprise
- **Padrão:** Redução contínua de custos em larga escala.
- **Diferencial SAP:**
  - **Compute Savings Plans:** Máxima flexibilidade (aplica-se a EC2, AWS Fargate e AWS Lambda independente de família de instância, SO, região ou tenancy).
  - **EC2 Instance Savings Plans:** Maior desconto para famílias específicas em uma região fixa.
  - Compartilhamento de Savings Plans em AWS Organizations gerenciado pela conta de gerenciamento.
  - **Cost & Usage Report (CUR) + Athena + QuickSight** para análise granular de faturamento.
  - **AWS Cost Anomaly Detection** com alertas via SNS para desvios de gastos inesperados.

### 13. AWS Systems Manager (SSM) em Escala
- **Padrão:** Gerenciamento operacional sem abrir portas de entrada (bastiões/SSH).
- **Diferencial SAP:**
  - **SSM Session Manager:** Acesso seguro a instâncias via console/CLI sem necessidade de bastiões, chaves SSH ou portas 22/3389 abertas nas Security Groups. Logs de sessão enviados diretamente para S3 ou CloudWatch Logs com criptografia KMS.
  - **SSM Patch Manager:** Criação de Patch Baselines e Maintenance Windows automatizadas para aplicar patches de segurança em frotas heterogêneas de EC2 e servidores on-premises (via SSM Agent).

### 14. Estratégias e Ferramental de Migração de Cargas de Trabalho (Os 7 Rs)
- **Padrão:** Migração de data centers legados para AWS.
- **Diferencial SAP:**
  - **AWS MGN (Application Migration Service):** Rehost automatizado com replicação contínua em nível de bloco, staging area de baixo custo e cutover com downtime mínimo (minutos).
  - **AWS DMS (Database Migration Service) + SCT:** Migrações homogêneas e heterogêneas com **CDC (Change Data Capture)** contínuo para transição de banco com downtime próximo de zero.
  - **AWS DataSync:** Migração de dados acelerada (até 10x mais rápida que rsync/scp) sobre Direct Connect/VPN com validação de integridade.
  - **Família Snow (Snowcone, Snowball Edge, Snowmobile):** Migração offline de dados em massa (TB a PB) quando a largura de banda de rede é insuficiente.

### 15. Arquiteturas Serverless e Event-Driven Resilientes
- **Padrão:** Desacoplamento assíncrono e tolerância a picos massivos de tráfego.
- **Diferencial SAP:**
  - **Amazon SQS (Standard vs. FIFO):** DLQ (Dead Letter Queue) com redrive policy para falhas de processamento; SQS Extended Client para mensagens > 256 KB via S3.
  - **Amazon SNS:** Fan-out para múltiplos assinantes SQS, Lambda e HTTPS com Message Filtering por atributos.
  - **Amazon EventBridge:** Barramentos de eventos personalizados (Custom Event Buses), barramentos multi-contas e schema registry para arquiteturas orientadas a eventos enterprise.

---

## 🎯 Catálogo de Nuances & Armadilhas para Distratores de Alta Plausibilidade

Ao gerar opções incorretas, utilize estas nuances reais da AWS para criar distratores sofisticados que exigem conhecimento aprofundado:

| Categoria | Nuance Técnica Real (Armadilha de Distrator) | Por Que o Distrator Falha? |
| :--- | :--- | :--- |
| **Networking** | Esquecer de habilitar o `Appliance Mode` no Transit Gateway VPC attachment ao usar AWS Network Firewall ou GWLB Multi-AZ. | O tráfego de retorno usa uma AZ diferente da requisição original, quebrando o stateful firewall (conexão TCP dropada). |
| **Networking** | Tentar usar VPC Peering para roteamento transitivo através de uma VPC intermediária (ex: On-prem -> Direct Connect -> VPC Hub -> VPC Spoke). | VPC Peering não suporta roteamento transitivo ou borda; requer AWS Transit Gateway ou PrivateLink. |
| **Networking** | Usar Gateway Endpoint para serviços além de S3 e DynamoDB. | Gateway Endpoints só existem para S3 e DynamoDB; todos os outros serviços AWS exigem Interface Endpoints (PrivateLink). |
| **Storage / S3** | Configurar S3 Cross-Region Replication (CRR) sem executar S3 Batch Replication para objetos pré-existentes. | S3 CRR por padrão só replica objetos gravados APÓS a habilitação da regra; os dados já existentes não são replicados. |
| **IAM / Org** | Aplicar uma Service Control Policy (SCP) na Management Account da Organization. | SCPs afetam apenas Member Accounts (inclusive usuário root das member accounts), mas nunca têm efeito sobre a Management Account. |
| **IAM / Org** | Compartilhar recursos entre contas usando políticas baseadas em recursos (Resource Policies) quando a Organização exige isolamento estrito via RAM. | Políticas baseadas em recursos exigem manutenção manual em cada recurso; o AWS RAM permite compartilhamento centralizado por OU. |
| **Database** | Propor Aurora Multi-Master para recuperação de desastres multi-região. | Aurora Multi-Master só opera dentro de uma única região e não suporta replicação global ativo-ativo (para isso usa-se Aurora Global Database ou DynamoDB Global Tables). |
| **Database** | Usar RDS Read Replicas convencionais para RTO < 1 minuto em failover regional. | RDS Read Replicas usam replicação lógica assíncrona; promover réplica a primário exige reinicialização do motor e redirecionamento manual de DNS. |
| **Security / KMS** | Tentar conceder permissões a instâncias Auto Scaling usando IAM Policies sem configurar KMS Grants na CMK. | Serviços que criam recursos delegados (como Auto Scaling provisionando volumes EBS criptografados) necessitam de KMS Grants. |
| **Disaster Recovery** | Usar CloudFront Origin Groups para failover dinâmico de banco de dados ou lógica de negócios. | CloudFront Origin Groups só disparam failover em erros de resposta HTTP de origem (ex: 500, 502, 503, 504), e não em latência ou falha de infraestrutura interna. |
| **Analytics** | Tentar compartilhar tabelas do Glue Data Catalog com centenas de contas usando apenas S3 Bucket Policies e IAM. | Causa explosão de complexidade de políticas que excedem o limite de tamanho do IAM/S3; a solução escalável correta é o **AWS Lake Formation cross-account permissions**. |
| **Modernization** | Propor AWS App2Container para aplicações com dependência de kernel customizado ou arquitetura não suportada. | App2Container containeriza aplicações Java e .NET em IIS/Linux; re-architecting complexo requer refatoração direta ou rehost via AWS MGN. |
