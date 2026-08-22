# Domínio 3: Cloud Technology and Services (34%)

Este guia de referência aborda a infraestrutura global da AWS e os serviços essenciais de computação, armazenamento, bancos de dados, redes e observabilidade para o **Domínio 3** do exame CLF-C02.

---

## 🌍 1. Infraestrutura Global da AWS

- **AWS Regions (Regiões):**
  - Áreas geográficas físicas no mundo que contêm múltiplos data centers isolados (ex: `us-east-1`, `sa-east-1`).
  - Cada região é completamente independente e isolada das outras. Fatores para escolher uma região: Conformidade/Governança legal dos dados, Proximidade aos usuários finais (latência), Disponibilidade de serviços e Custos regionais.
- **Availability Zones (AZs - Zonas de Disponibilidade):**
  - Cada Região possui no mínimo **3 Zonas de Disponibilidade** (AZs).
  - Uma AZ é composta por **um ou mais data centers físicos discretos**, com energia redundante, rede de fibra dedicada e refrigeração independente.
  - As AZs de uma mesma região são interconectadas por redes de fibra ótica de latência ultra-baixa.
- **Edge Locations (Pontos de Presença / PoPs):**
  - Centenas de locais de borda espalhados globalmente em grandes cidades para armazenar conteúdo em cache via **Amazon CloudFront** e acelerar DNS via **Amazon Route 53**.
- **Outros Componentes:**
  - **AWS Outposts:** Hardware de servidores físicos e infraestrutura da AWS instalados diretamente no data center local on-premises do cliente.
  - **AWS Local Zones:** Extensão da infraestrutura da AWS para cidades metropolitanas para cargas com latência inferior a 10 ms.
  - **AWS Wavelength:** Infraestrutura da AWS incorporada às redes 5G de operadoras de telecomunicação para aplicações móveis de latência ultra-baixa.

---

## 💻 2. Serviços Centrais de Computação
- **Amazon EC2 (Elastic Compute Cloud):**
  - Servidores virtuais escaláveis na nuvem. Suporta escolha de SO, processadores (Intel, AMD, AWS Graviton), memória, armazenamento e rede.
- **AWS Lambda:**
  - Serviço de computação Serverless (sem servidor) que executa código em resposta a eventos HTTP, alterações no S3 ou mensagens em filas SQS, cobrando exclusivamente pelo tempo de execução em milissegundos.
- **Amazon ECS e Amazon EKS:**
  - **Amazon Elastic Container Service (ECS):** Orquestrador de contêineres Docker gerenciado nativo da AWS, altamente opinativo e simples de operar.
  - **Amazon Elastic Kubernetes Service (EKS):** Serviço gerenciado de Kubernetes para executar e gerenciar clusters padrão K8s na nuvem AWS.
- **AWS Fargate:**
  - Mecanismo de computação Serverless para containers (compatível com ECS e EKS). O desenvolvedor não precisa gerenciar instâncias EC2 subjacentes.
- **Amazon Lightsail:**
  - Plataforma de nuvem simplificada (VPS) com planos de preço fixo mensal incluindo instância, SSD, transferência e IP estático para sites simples e pequenos sistemas.
- **AWS Batch:**
  - Planejamento e execução automatizada de milhares de trabalhos de processamento em lote (batch computing) em qualquer escala.

---

## 💾 3. Serviços Centrais de Armazenamento
- **Amazon S3 (Simple Storage Service):**
  - Armazenamento de objetos com escalabilidade ilimitada e durabilidade de 99.999999999% (11 9s). Classes: *S3 Standard*, *S3 Intelligent-Tiering*, *S3 Standard-IA*, *S3 Glacier Flexible* e *S3 Glacier Deep Archive*.
- **Amazon EBS (Elastic Block Store):**
  - Armazenamento persistente em nível de bloco projetado para ser anexado a uma única instância EC2 (como um disco rígido virtual).
- **Amazon EFS (Elastic File System):**
  - Sistema de arquivos elástico gerenciado que suporta compartilhamento de arquivos entre centenas de instâncias EC2 Linux simultaneamente via NFS.
- **AWS Storage Gateway:**
  - Serviço de armazenamento híbrido que conecta ambientes locais ao armazenamento em nuvem da AWS (File Gateway, Volume Gateway, Tape Gateway).

---

## 🗄️ 4. Serviços Centrais de Bancos de Dados
- **Amazon RDS (Relational Database Service):**
  - Serviço gerenciado para 6 motores relacionais: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle e Microsoft SQL Server. Cuida de provisionamento, backups automáticos e patches de software.
- **Amazon Aurora:**
  - Banco de dados relacional proprietário da AWS de nível empresarial compatível com MySQL e PostgreSQL, até 5x mais rápido que MySQL padrão e com replicação em 3 AZs.
- **Amazon DynamoDB:**
  - Banco de dados NoSQL de chave-valor e documento totalmente gerenciado e Serverless, com desempenho consistente de milissegundos em qualquer escala.
- **Amazon ElastiCache:**
  - Cache em memória de alta performance baseado em Redis OSS ou Memcached para acelerar leituras de bancos de dados.
- **Amazon Redshift:**
  - Data Warehouse analítico petabyte-scale em nuvem baseado em SQL para Business Intelligence (BI).

---

## 🌐 5. Serviços Centrais de Rede
- **Amazon VPC (Virtual Private Cloud):**
  - Rede virtual logicamente isolada na nuvem AWS onde você provisiona seus recursos.
  - **Subnets:** Segmentos de IP dentro de uma VPC localizados em uma AZ específica (Públicas ou Privadas).
  - **Internet Gateway (IGW):** Permite comunicação bidirecional entre recursos na VPC e a internet.
  - **NAT Gateway:** Permite que instâncias em sub-redes privadas acessem a internet de forma segura sem permitir conexões de entrada iniciadas de fora.
- **Amazon Route 53:**
  - Serviço de Sistema de Nomes de Domínio (DNS) na nuvem altamente disponível e escalável, com suporte a registro de domínios e health checks.
- **Amazon CloudFront:**
  - Rede de entrega de conteúdo (CDN) global e segura para aceleração de sites, vídeos e APIs.

---

## 📊 6. Gerenciamento, Monitoramento e IA
- **Amazon CloudWatch:** Monitoramento operacional de métricas (CPU, disco, rede), coleta de logs e configuração de alarmes com ações automatizadas.
- **AWS CloudTrail:** Registro contínuo e histórico de auditoria de todas as chamadas de API e ações realizadas na conta da AWS (quem fez o quê, de qual IP e quando).
- **AWS Config:** Registro de inventário e histórico de configurações de recursos para auditoria de conformidade.
- **Serviços de IA e Machine Learning:**
  - **Amazon Bedrock:** Serviço totalmente gerenciado para construir aplicações com Modelos de Fundação (FMs) de IA Generativa.
  - **Amazon SageMaker:** Plataforma ponta a ponta para cientistas de dados construírem, treinarem e implantarem modelos de ML.
  - **Serviços de IA pré-treinados:** *Amazon Rekognition* (visão computacional/análise de imagens), *Amazon Polly* (conversão de texto em fala realista), *Amazon Transcribe* (fala em texto), *Amazon Translate* (tradução automática) e *Amazon Comprehend* (Processamento de Linguagem Natural - NLP).
