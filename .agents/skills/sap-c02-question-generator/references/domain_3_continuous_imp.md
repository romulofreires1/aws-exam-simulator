# Domínio 3: Continuous Improvement for Existing Solutions (25%)

Este guia de referência detalha os cenários, arquiteturas e padrões de questões para o **Domínio 3** do exame SAP-C02.

---

## 🏗️ Padrões Arquiteturais Centrais

### 1. Centralização de Segurança, Detecção e Remediação Automatizada
- **AWS GuardDuty:**
  - Detecção contínua de comportamento anômalo e ameaças utilizando aprendizado de máquina.
  - Fontes de dados: AWS CloudTrail Management Events, CloudTrail S3 Data Events, VPC Flow Logs, DNS Logs, EKS Audit Logs, RDS Login Activity, e EBS Volume Malware Protection.
  - Delegated Administrator no AWS Organizations para gerenciar todas as contas de forma centralizada.
- **AWS Security Hub:**
  - Centraliza e normaliza achados no formato ASF (AWS Security Finding Format) vindos do GuardDuty, Inspector, Macie, IAM Access Analyzer e AWS Firewall Manager.
  - Realiza verificações de conformidade automáticas (CIS AWS Foundations Benchmark, PCI-DSS, AWS Foundational Security Best Practices).
  - **Fluxo de Remediação Automatizada:**
    `Security Hub Finding -> Amazon EventBridge Rule -> AWS Systems Manager Automation Document / AWS Lambda`.
- **Amazon Macie:**
  - Varredura e descoberta automatizada de dados sensíveis (PII, números de cartão de crédito, chaves de API) em buckets Amazon S3.
- **Amazon Inspector v2:**
  - Gerenciamento de vulnerabilidades contínuo e automatizado para instâncias Amazon EC2, imagens em repositórios Amazon ECR e funções AWS Lambda (inclusive dependências de código).

---

### 2. Criptografia Enterprise e Gestão Avançada de Chaves (AWS KMS)
- **KMS Multi-Region Keys:**
  - Chaves de criptografia primárias e réplicas que compartilham o mesmo Key ID e material criptográfico entre diferentes regiões da AWS.
  - Permite que dados replicados (ex: S3 Cross-Region Replication, DynamoDB Global Tables, Aurora Global Database) sejam lidos em outra região sem exigir re-criptografia completa.
- **KMS Key Policies vs. IAM Policies:**
  - Uma IAM Policy por si só **não** pode conceder acesso a uma chave KMS se a Key Policy da chave não permitir explicitamente ou delegar o controle à conta raiz (`Principal: { "AWS": "arn:aws:iam::123456789012:root" }`).
- **KMS Grants:**
  - Concede permissões temporárias e de escopo restrito a serviços AWS (como Auto Scaling para lançar instâncias a partir de AMIs criptografadas) sem alterar a política estática da chave.
- **AWS CloudHSM:**
  - Módulo de segurança em hardware dedicado e exclusivo para clientes que exigem controle total do appliance sob padrões FIPS 140-2 Level 3.

---

### 3. FinOps Enterprise e Modelos de Economia de Custos
- **Compute Savings Plans:**
  - Oferece até 66% de desconto em troca de um compromisso de gasto em $/hora por 1 ou 3 anos.
  - Aplica-se automaticamente a **Amazon EC2** (qualquer família, SO, região, tenancy), **AWS Fargate** e **AWS Lambda**.
- **EC2 Instance Savings Plans:**
  - Oferece até 72% de desconto para uma família específica de instâncias dentro de uma região definida (ex: família c6g em us-east-1).
- **Amazon RDS / Aurora Reserved Instances:**
  - RIs específicas para instâncias de bancos de dados relacionais e clusters.
- **Análise Avançada com Cost and Usage Report (CUR):**
  - O CUR entrega relatórios detalhados no Amazon S3 que podem ser particionados e consultados usando **Amazon Athena** e visualizados no **Amazon QuickSight**.
- **AWS Cost Anomaly Detection:**
  - Usa machine learning para identificar aumentos inesperados de custos e envia notificações automáticas via Amazon SNS / Slack.

---

### 4. Excelência Operacional com AWS Systems Manager (SSM)
- **SSM Session Manager:**
  - Acesso interativo a instâncias EC2 e servidores on-premises sem a necessidade de chaves SSH/RDP, bastiões na sub-rede pública ou portas 22/3389 abertas em Security Groups.
  - Todas as sessões são auditadas com logs gravados em buckets S3 criptografados com KMS ou no CloudWatch Logs.
- **SSM Patch Manager:**
  - Automação de correções de segurança em sistemas operacionais (Linux/Windows) com Patch Baselines customizadas, regras de aprovação e janelas de manutenção (*Maintenance Windows*).

---

## 🎯 Modelos de Cenários de Questões para o Domínio 3

1. **Cenário de Resposta a Incidentes Automatizada:**
   - *Problema:* Uma organização precisa detectar imediatamente se credenciais de acesso IAM estão vazando ou se instâncias EC2 estão se comunicando com endereços IP maliciosos de comando e controle conhecidos, e isolar automaticamente as instâncias comprometidas sem intervenção manual.
   - *Solução Correta:* Habilitar o **Amazon GuardDuty** com administração delegada no AWS Organizations. Criar uma regra no **Amazon EventBridge** que capture achados críticos do GuardDuty e acione um documento de automação do **AWS Systems Manager (SSM Automation)** para desanexar as interfaces de rede ou aplicar um Security Group de isolamento estrito.

2. **Cenário de Governança de Custos Enterprise (FinOps):**
   - *Problema:* Uma empresa possui centenas de contas AWS com arquiteturas dinâmicas compostas por instâncias EC2, contêineres no AWS Fargate e microsserviços em AWS Lambda em várias regiões. A liderança técnica precisa de uma estratégia de desconto que ofereça a máxima flexibilidade para cobrir todas essas tecnologias com o menor risco de subutilização.
   - *Solução Correta:* Adquirir **Compute Savings Plans** na conta de gerenciamento do AWS Organizations e habilitar o compartilhamento de desconto de Savings Plans entre todas as contas-membro.
