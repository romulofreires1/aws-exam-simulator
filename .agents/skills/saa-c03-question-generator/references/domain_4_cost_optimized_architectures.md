# Domínio 4: Design Cost-Optimized Architectures (20%)

Este guia de referência aborda a otimização de custos em armazenamento, computação, bancos de dados e redes para o **Domínio 4** do exame SAA-C03.

---

## 💰 1. Otimização de Armazenamento
- **Amazon S3 Storage Classes e Lifecycle:**
  | Classe S3 | Indicada Para | Recuperação / Custo |
  | :--- | :--- | :--- |
  | **S3 Standard** | Dados acessados com frequência (> 1 vez ao mês) | Acesso instantâneo, custo padrão de armazenamento, sem taxa de recuperação |
  | **S3 Intelligent-Tiering** | **Padrões de acesso variáveis, desconhecidos ou imprevisíveis** | Move dados automaticamente entre tiers de acesso frequente, infrequente e arquivo sem taxa de recuperação |
  | **S3 Standard-IA** | Dados acessados com pouca frequência, mas que exigem milissegundos quando solicitados | Menor custo de GB/mês, taxa por GB recuperado, permanência mínima de 30 dias |
  | **S3 One Zone-IA** | Dados infrequentes reproduzíveis/secundários em uma única AZ | ~20% mais barato que Standard-IA, sem resiliência a perda de AZ |
  | **S3 Glacier Flexible Archive** | Arquivamento de longo prazo (backups anuais) | Opções de recuperação: Expedited (1-5 min), Standard (3-5 h), Bulk (5-12 h) |
  | **S3 Glacier Deep Archive** | Arquivamento de conformidade regulatória (retenção de 7-10 anos) | Menor custo absoluto de armazenamento na AWS, recuperação Standard (12 h) ou Bulk (48 h) |

- **Políticas de Ciclo de Vida do S3 (S3 Lifecycle Rules):**
  - Ações de transição baseadas em idade (ex: Standard -> Standard-IA após 30 dias -> Glacier Flexible após 90 dias -> Expiração/Exclusão após 365 dias).
  - Exclusão de versões não atuais de objetos e limpeza de uploads multipartes incompletos (`AbortIncompleteMultipartUpload`).
- **Otimização de Custos de EBS e EFS:**
  - Migração de volumes legados **gp2** para **gp3** (até 20% de economia por GB e baseline de 3.000 IOPS gratuito).
  - **EFS Lifecycle Management:** Transição automática de arquivos frios para a classe *EFS Infrequent Access (EFS IA)* ou *EFS Archive* gerando economia de até 90%.

---

## 🖥️ 2. Otimização de Custos em Computação
- **Modelos de Compra do Amazon EC2:**
  - **Instâncias Sob Demanda (On-Demand):** Cargas de trabalho de curto prazo, imprevisíveis ou em fase de desenvolvimento que não podem ser interrompidas.
  - **Instâncias Spot:** Descontos de até 90% em comparação com On-Demand. Ideais para processamento em lote (batch), renderização de vídeo, pipelines de dados, CI/CD e cargas de trabalho sem estado (stateless) altamente tolerantes a interrupções com aviso prévio de 2 minutos.
  - **Savings Plans:**
    - *Compute Savings Plans:* Até 66% de desconto com compromisso de 1 ou 3 anos ($/hora constante). Maior flexibilidade (aplica-se a EC2 de qualquer família/região/SO, AWS Fargate e AWS Lambda).
    - *EC2 Instance Savings Plans:* Até 72% de desconto para famílias de instâncias específicas em uma determinada região.
  - **Instâncias Reservadas (Reserved Instances - RIs):** Descontos similares aplicáveis a EC2, RDS, ElastiCache, OpenSearch e Redshift.
- **Auto Scaling Orientado a Custo:**
  - Uso de grupos de Auto Scaling mistos combinando instâncias Spot e On-Demand via *Allocation Strategies* (ex: `capacity-optimized` ou `price-capacity-optimized`).
  - Desligamento agendado de instâncias de desenvolvimento/testes fora do horário de expediente usando AWS Systems Manager Quick Setup ou AWS Instance Scheduler.

---

## 🗄️ 3. Otimização de Custos em Bancos de Dados
- **Amazon DynamoDB Pricing Modes:**
  - **On-Demand Capacity:** Cargas de trabalho com tráfego desconhecido, intermitente ou de picos imprevisíveis. Cobra estritamente por leitura e gravação realizadas.
  - **Provisioned Capacity:** Cargas de trabalho com padrões de tráfego estáveis e previsíveis, com suporte a Auto Scaling de RCU/WCU e Reservas de Capacidade para maior desconto.
- **Amazon RDS / Aurora Cost Optimization:**
  - Uso de **Aurora Serverless v2** para cargas com picos ocasionais de tráfego, escalando instantaneamente em frações de ACUs.
  - Parada temporária de instâncias de teste do Amazon RDS por até 7 dias consecutivos.

---

## 🌐 4. Otimização de Custos de Rede e Transferência de Dados
- **Redução de Transferência de Dados Externa (Data Transfer Out - DTO):**
  - Tráfego de saída da AWS para a internet tem custo por GB. Distribuir assets via **Amazon CloudFront** reduz significativamente a cobrança de tráfego de saída e melhora o cache.
- **Economia com VPC Endpoints:**
  - Instâncias EC2 em subnets privadas baixando gigabytes/terabytes de dados do S3 via NAT Gateway pagam taxa por GB processado pelo NAT Gateway.
  - Criar um **VPC Gateway Endpoint para S3** direciona o tráfego pela rede interna da AWS sem passar pelo NAT Gateway, **com custo ZERO de processamento e ZERO custo de endpoint**.
- **Comunicação Inter-VPC:**
  - **VPC Peering:** Não tem custo de infraestrutura fixa por hora de anexo; cobra apenas o tráfego entre AZs/regiões. Mais econômico para conexão ponto a ponto entre poucas VPCs do que manter anexos de Transit Gateway.
