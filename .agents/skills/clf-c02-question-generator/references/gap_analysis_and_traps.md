# Distinções Fundamentais e Armadilhas Clássicas do Exame CLF-C02

Esta referência compila as confusões conceituais mais frequentes entre serviços e termos no exame **AWS Certified Cloud Practitioner (CLF-C02)**.

---

## ⚠️ As 10 Confusões Mais Comuns no CLF-C02

### 1. Amazon CloudWatch vs. AWS CloudTrail
- **Amazon CloudWatch:** Monitora **desempenho e métricas operacionais** (uso de CPU, tráfego de rede, alarmes de limite de capacidade, agregação de logs).
- **AWS CloudTrail:** Grava o **histórico de chamadas de API e auditoria de segurança** (quem fez a ação, qual IAM User/Role, de qual IP, em qual data/hora).
- *Regra rápida:* Métricas/Alarmes = CloudWatch | "Quem fez o quê?" / Auditoria = CloudTrail.

### 2. AWS Artifact vs. AWS Shield vs. AWS Audit Manager
- **AWS Artifact:** Portal para **fazer download de documentos de conformidade e relatórios SOC/PCI/ISO** da infraestrutura da própria AWS.
- **AWS Shield:** Proteção contra **ataques DDoS** (Standard e Advanced).
- **AWS Audit Manager:** Ferramenta que avalia e coleta evidências contínuas de conformidade nos recursos do cliente.

### 3. Elasticidade vs. Escalabilidade vs. Agilidade
- **Elasticidade (Elasticity):** Capacidade de **adquirir e liberar recursos automaticamente** conforme a demanda flutua (aumenta em picos e reduz em calmaria).
- **Escalabilidade (Scalability):** Capacidade de acomodar o crescimento contínuo de um sistema adicionando capacidade (horizontal ou verticalmente).
- **Agilidade (Agility):** Capacidade de **inovar e experimentar rapidamente**, reduzindo o tempo para disponibilizar recursos de TI de semanas para minutos.

### 4. Amazon S3 vs. Amazon EBS vs. Amazon EFS
- **Amazon S3:** Armazenamento de **Objetos** acessível via HTTP/HTTPS/Web API em qualquer lugar, durabilidade 11 9s.
- **Amazon EBS:** Armazenamento em **Bloco** (disco rígido virtual) anexado a uma única instância EC2 por vez.
- **Amazon EFS:** Sistema de **Arquivos** gerenciado que suporta compartilhamento simultâneo com centenas de instâncias EC2 Linux via NFS.

### 5. AWS Cost Explorer vs. AWS Budgets vs. AWS Pricing Calculator
- **AWS Pricing Calculator:** Estima custos **antes** de criar os recursos (planejamento prévio).
- **AWS Cost Explorer:** Analisa e projeta custos **com base no histórico** real de uso da conta (até 12 meses).
- **AWS Budgets:** Cria **alertas e limites de gastos/uso** para notificar quando custos ultrapassarem o orçado.

### 6. Modelo de Responsabilidade Compartilhada: EC2 vs. RDS vs. S3
- **Em Amazon EC2 (IaaS):** O cliente é **100% responsável** por instalar patches no Sistema Operacional (Windows/Linux) e configurar o firewall da instância (Security Groups).
- **Em Amazon RDS (PaaS gerenciado):** A AWS é responsável pelos patches do SO e do motor do banco; o cliente é responsável pelo schema, dados, usuários e otimização de consultas.
- **Em Amazon S3 (SaaS/Storage gerenciado):** A AWS cuida da infraestrutura completa; o cliente é responsável por permissões (Bucket Policies), criptografia e acesso público.

### 7. AWS Support Plans: Business vs. Enterprise
- **Business Support:** Suporte 24/7 por chat/telefone/email, resposta < 1h para produção fora do ar, acesso total ao Trusted Advisor. **NÃO inclui TAM dedicado**.
- **Enterprise Support:** Inclui **Technical Account Manager (TAM) DEDICADO**, Concierge Support Team, resposta < 15 min para missão crítica e revisões consultivas regulares.

### 8. Security Groups vs. Network ACLs
- **Security Groups:** Operam no nível da **instância/ENI**, são **com estado (Stateful)**, suportam apenas regras de permissão (Allow).
- **Network ACLs:** Operam no nível da **sub-rede (Subnet)**, são **sem estado (Stateless)**, suportam regras de permissão (Allow) e negação explícita (Deny) ordenadas por números de regra.

### 9. AWS Trusted Advisor vs. AWS Health Dashboard
- **AWS Trusted Advisor:** Analisa a conta do cliente e dá recomendações de melhores práticas (Custos, Segurança, Desempenho, Tolerância a Falhas, Cotas).
- **AWS Health Dashboard:** Mostra a saúde dos serviços globais da AWS e eventos operacionais que impactam diretamente a conta do cliente.

### 10. Amazon Rekognition vs. Comprehend vs. Transcribe vs. Polly
- **Rekognition:** Visão computacional / Análise de imagens e vídeos.
- **Comprehend:** Processamento de Linguagem Natural (NLP) / Análise de sentimentos em texto.
- **Transcribe:** Conversão de Áudio/Voz para Texto (Speech-to-Text).
- **Polly:** Conversão de Texto para Áudio/Voz realista (Text-to-Speech).
