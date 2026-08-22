# Domínio 2: Security and Compliance (30%)

Este guia de referência aborda o Modelo de Responsabilidade Compartilhada, fundamentos de segurança e identidade (IAM), serviços de segurança e governança de conformidade para o **Domínio 2** do exame CLF-C02.

---

## 🤝 1. O Modelo de Responsabilidade Compartilhada da AWS

O modelo divide as responsabilidades de segurança entre a AWS e o cliente:

| Categoria | Responsabilidade da AWS ("Segurança DA Nuvem") | Responsabilidade do Cliente ("Segurança NA Nuvem") |
| :--- | :--- | :--- |
| **Infraestrutura Física** | Proteção física dos data centers, energia ininterrupta, climatização, biometria e descarte seguro de hardware | Nenhuma (cliente não tem acesso físico) |
| **Hardware e Rede Global** | Servidores físicos de computação, switches, roteadores, cabos de fibra ótica submarinos, hypervisors de virtualização | Configuração de subnets na VPC, regras de Security Groups e Network ACLs |
| **Sistemas Operacionais** | Patches e atualizações do hypervisor e de serviços totalmente gerenciados (DynamoDB, S3, SQS, RDS engine) | **Instalação de patches, atualizações e segurança do sistema operacional convidado (SO) em instâncias Amazon EC2** |
| **Gerenciamento de Dados** | Criptografia na camada física de armazenamento da AWS | **Classificação dos dados, políticas de criptografia (SSE), backups e permissões de acesso ao Amazon S3** |
| **Identidade e Acesso** | Disponibilidade e integridade da infraestrutura do AWS IAM | **Criação de usuários/senhas, ativação de MFA, configuração de políticas de Menor Privilégio e rotação de credenciais** |

---

## 🔑 2. Fundamentos do AWS IAM e Melhores Práticas
- **IAM Users:** Identidades persistentes com credenciais próprias para pessoas ou aplicações individuais.
- **IAM Groups:** Coleções de usuários IAM para facilitar a aplicação coletiva de políticas de permissão.
- **IAM Roles:** Identidades temporárias sem credenciais estáticas que podem ser assumidas por pessoas, instâncias EC2 (Instance Profiles) ou outros serviços AWS.
- **IAM Policies:** Documentos em formato JSON que definem permissões de forma explícita (`Effect: Allow/Deny`, `Action`, `Resource`).
- **Autenticação Multifator (MFA):** Camada adicional obrigatória de segurança que exige um código temporário além da senha.
- **Proteção da Conta Root da AWS:**
  - A conta root tem acesso irrestrito a todos os recursos e dados de faturamento.
  - **Melhores Práticas Root:** Nunca usar no dia a dia; bloquear com MFA físico/virtual forte; não gerar Access Keys para o usuário root; criar um usuário administrador IAM para tarefas diárias.

---

## 🛡️ 3. Principais Serviços de Segurança, Conformidade e Governança

- **AWS Artifact:**
  - Portal gratuito de autoatendimento para download de acordos de conformidade da AWS (ex: BAA para HIPAA) e relatórios de auditoria de segurança terceirizados (SOC 1/2/3, PCI-DSS, ISO 27001).
- **AWS KMS (Key Management Service):**
  - Serviço gerenciado para criação, controle e armazenamento seguro de chaves de criptografia para proteger dados em repouso nos serviços AWS.
- **AWS Secrets Manager:**
  - Armazena, gerencia e rotaciona credenciais de bancos de dados, tokens de API e chaves secretas de forma automática.
- **AWS Shield:**
  - **Shield Standard:** Proteção contra ataques DDoS de camadas de rede/transporte (L3/L4) ativada automaticamente sem custo adicional.
  - **Shield Advanced:** Proteção DDoS especializada e expandida, acesso 24/7 ao AWS DDoS Response Team (DRT) e proteção contra picos de cobrança decorrentes de ataques.
- **AWS WAF (Web Application Firewall):**
  - Firewall de camada de aplicação (Camada 7) para filtrar tráfego HTTP/HTTPS, bloqueando SQL Injection, Cross-Site Scripting (XSS) e bots maliciosos no CloudFront, ALB e API Gateway.
- **Amazon GuardDuty:**
  - Serviço de detecção inteligente de ameaças que monitora continuamente anomalias na conta analisando logs do CloudTrail, VPC Flow Logs, DNS Logs e eventos de auditoria EKS.
- **Amazon Inspector:**
  - Serviço automatizado de gerenciamento de vulnerabilidades que varre instâncias EC2, imagens de contêineres no Amazon ECR e funções AWS Lambda em busca de falhas de software e exposição acidental.
- **Amazon Macie:**
  - Serviço de segurança de dados e privacidade que utiliza Machine Learning para descobrir, classificar e proteger dados confidenciais (PII, números de cartão) armazenados no Amazon S3.
- **AWS Security Hub:**
  - Painel unificado de gerenciamento de postura de segurança que agrega e prioriza alertas e achados de segurança de múltiplos serviços AWS (GuardDuty, Inspector, Macie, IAM Access Analyzer).
- **AWS Trusted Advisor:**
  - Ferramenta online que fornece recomendações em 5 pilares: Otimização de Custos, Desempenho, Segurança, Tolerância a Falhas e Limites de Serviço (Cotas). O plano Basic inclui 7 verificações de segurança essenciais.
