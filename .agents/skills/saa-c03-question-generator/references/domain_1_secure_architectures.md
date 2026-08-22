# Domínio 1: Design Secure Architectures (30%)

Este guia de referência cobre os tópicos de segurança, gerenciamento de acessos e proteção de dados essenciais para o **Domínio 1** do exame SAA-C03.

---

## 🔐 1. Gerenciamento de Identidade e Acesso (AWS IAM)
- **IAM Users, Groups e Roles:**
  - Usuários para identidades individuais com credenciais permanentes (consoles/chaves).
  - IAM Roles para concessão de permissões temporárias para instâncias EC2 (Instance Profiles), funções Lambda e serviços AWS, eliminando credenciais estáticas.
  - Federação de identidades com SAML 2.0 / OIDC para autenticação com provedores corporativos (ex: Google, Okta, Active Directory) via AWS IAM Identity Center ou AWS STS (`AssumeRoleWithWebIdentity`).
- **Políticas IAM (IAM Policies):**
  - **Identity-based Policies:** Anexadas a usuários, grupos ou roles (Managed Policies vs Inline Policies).
  - **Resource-based Policies:** Anexadas a recursos (S3 Bucket Policies, KMS Key Policies, SQS Queue Policies, Secrets Manager Policies). Permitem conceder acesso cross-account direto sem assumir role.
  - **Permission Boundaries:** Definem o limite máximo de permissões que uma role ou usuário pode receber.
- **Segurança de Credenciais:**
  - **AWS Secrets Manager:** Armazenamento seguro e rotação automática de senhas de banco de dados (RDS, Redshift, DocumentDB) e credenciais de APIs com funções Lambda nativas.
  - **AWS Systems Manager Parameter Store:** Armazenamento de parâmetros em texto simples ou criptografados (`SecureString` com KMS) sem custo de rotação automática.

---

## 🛡️ 2. Segurança de Rede e Isolamento
- **VPC Topology & Segregação:**
  - Subnets públicas (com rota para Internet Gateway) vs subnets privadas (com rota para NAT Gateway para saída ou sem acesso à Internet para bancos).
  - **Security Groups (Stateful):** Atuam no nível da instância/interface ENI. Se o tráfego de entrada for permitido, a resposta de saída é permitida automaticamente. Suportam referência a outros Security Groups por ID (encadeamento seguro).
  - **Network ACLs (Stateless):** Atuam no nível da subnet. Avaliação sequencial por número de regra (1-32766). Exigem regras explícitas para tráfego de entrada e de retorno (portas efêmeras 1024-65535).
- **Conectividade Privada (VPC Endpoints):**
  - **Gateway Endpoints:** Gratuitos, configurados nas route tables. Disponíveis apenas para **Amazon S3** e **Amazon DynamoDB**. Não funcionam عبر Direct Connect / VPN ou VPC Peering.
  - **Interface Endpoints (AWS PrivateLink):** Criam Elastic Network Interfaces (ENIs) privadas com IP dentro da subnet para serviços AWS e APIs customizadas. Suportam acesso via Direct Connect / VPN e Peering.
- **Proteção de Borda e Aplicação:**
  - **AWS WAF (Web Application Firewall):** Protege contra ataques web comuns da camada de aplicação (Camada 7 - SQL Injection, Cross-Site Scripting, IP rate limiting) integrado ao CloudFront, ALB, API Gateway e AppSync.
  - **AWS Shield:** Standard (gratuito, protege contra ataques DDoS comuns de camada 3 e 4) e Shield Advanced (proteção especializada, resposta 24/7 de DDoS Response Team e mitigação de picos de custo).

---

## 🔒 3. Proteção de Dados e Criptografia
- **Criptografia com AWS KMS:**
  - **AWS Managed Keys:** Criadas e gerenciadas pela AWS para cada serviço (`aws/s3`, `aws/ebs`).
  - **Customer Managed Keys (CMK):** Criadas pelo cliente com controle total sobre rotação anual automática, políticas de chave e concessões (grants).
  - Modos de criptografia S3: **SSE-S3** (chaves gerenciadas pelo S3), **SSE-KMS** (chaves KMS com auditoria via CloudTrail), **SSE-C** (chaves fornecidas pelo cliente).
- **Amazon S3 Security:**
  - **Origin Access Control (OAC):** Mecanismo moderno e recomendado para restringir o acesso a buckets S3 exclusivamente através de distribuições Amazon CloudFront (substitui o OAI legado).
  - **S3 Block Public Access:** Guardrail de nível de conta e de bucket para evitar exposição pública acidental.
  - **S3 Object Lock:** WORM (Write Once, Read Many) para impedir exclusão ou substituição de objetos (Compliance Mode não pode ser desativado nem por root; Governance Mode permite bypass por usuários autorizados).
- **Auditoria e Detecção de Ameaças:**
  - **Amazon GuardDuty:** Detecção inteligente contínua de anomalias e ameaças usando Machine Learning em CloudTrail, VPC Flow Logs e DNS Logs.
  - **Amazon Inspector:** Análise automatizada de vulnerabilidades em instâncias EC2, imagens ECR e código Lambda.
  - **Amazon Macie:** Descoberta e classificação automatizada de dados sensíveis (PII, números de cartão) armazenados no Amazon S3.
