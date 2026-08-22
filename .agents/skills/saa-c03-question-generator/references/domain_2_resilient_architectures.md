# Domínio 2: Design Resilient Architectures (26%)

Este guia de referência aborda estratégias de alta disponibilidade, tolerância a falhas, desacoplamento assíncrono e recuperação de desastres para o **Domínio 2** do exame SAA-C03.

---

## ⚡ 1. Desacoplamento e Mensageria Assíncrona
- **Amazon SQS (Simple Queue Service):**
  - **Standard Queues:** Throughput ilimitado, entrega "at-least-once" (pelo menos uma vez), ordenação de melhor esforço (best-effort ordering).
  - **FIFO Queues (First-In-First-Out):** Garantia estrita de ordenação e entrega única ("exactly-once"), throughput de até 300 mensagens/s (ou 3.000 com batching / high throughput mode). Exige Message Group ID para ordenação por grupo e Deduplication ID.
  - **Visibility Timeout:** Janela de tempo (padrão 30s) em que uma mensagem fica invisível para outros consumidores enquanto está sendo processada.
  - **Dead-Letter Queue (DLQ):** Destino para mensagens que falharam no processamento após determinado número de tentativas (`maxReceiveCount`).
- **Amazon SNS (Simple Notification Service):**
  - Modelo Pub/Sub com fanout: uma única publicação é distribuída para múltiplos assinantes (filas SQS, endpoints HTTP/S, funções Lambda, emails, SMS).
  - Suporta tópicos Standard e tópicos FIFO.
- **Amazon EventBridge:**
  - Barramento de eventos serverless que roteia eventos em tempo real de serviços AWS, aplicações SaaS e aplicações próprias para múltiplos destinos usando regras com filtros JSON.
- **AWS Step Functions:**
  - Orquestração de fluxos de trabalho visuais com máquinas de estados (State Machines) para coordenar microsserviços, tratamento de erros e retentativas automáticas.

---

## ⚖️ 2. Balanceamento de Carga e Auto Escalabilidade
- **Elastic Load Balancing (ELB):**
  - **Application Load Balancer (ALB):** Camada 7 (HTTP/HTTPS/gRPC). Roteamento avançado baseado em path (`/api`), host header, query strings, headers HTTP. Suporta autenticação OIDC/Cognito e redirecionamento HTTP para HTTPS.
  - **Network Load Balancer (NLB):** Camada 4 (TCP/UDP/TLS). Ultra-alta performance (milhões de requisições/s), latência ultra-baixa, IPs elásticos estáticos por AZ e suporte a AWS PrivateLink.
  - **Gateway Load Balancer (GWLB):** Camada 3. Roteamento transparente de tráfego para frotas de firewalls e appliances de segurança de terceiros via protocolo GENEVE.
- **Amazon EC2 Auto Scaling:**
  - **Políticas de Dimensionamento:**
    - *Target Tracking:* Mantém métricas específicas em um valor alvo (ex: utilização média de CPU em 60%).
    - *Step Scaling / Simple Scaling:* Aumenta ou diminui instâncias em degraus com base em alarmes do CloudWatch.
    - *Scheduled Scaling:* Escala preventivamente em horários programados.
    - *Predictive Scaling:* Utiliza aprendizado de máquina para prever padrões de tráfego diários/semanais.
  - **Health Checks do Auto Scaling:** Podem ser baseados em verificações de status do EC2 ou nas verificações de saúde do Application Load Balancer (ALB Health Checks) para substituir instâncias degradadas no nível da aplicação.

---

## 🗄️ 3. Resiliência e Alta Disponibilidade de Dados
- **Amazon RDS Multi-AZ vs. Read Replicas:**
  | Recurso | Multi-AZ Deployment | Read Replicas |
  | :--- | :--- | :--- |
  | **Objetivo** | **Alta Disponibilidade e Resiliência (DR)** | **Escalabilidade de Leitura e Performance** |
  | **Replicação** | **Síncrona** (zero perda de dados) | **Assíncrona** (eventual consistency) |
  | **Acesso aos Dados** | Standby passivo (não aceita leituras) | Ativo para consultas de leitura (SELECT) |
  | **Failover** | **Automático** em ~1 a 2 min (DNS atualizado nativamente) | **Manual** (exige promoção manual da réplica a primário) |
  | **Localização** | Múltiplas AZs na mesma região | Mesma região ou Cross-Region |

- **Amazon Aurora:**
  - Storage compartilhado com 6 cópias dos dados distribuídas em 3 Availability Zones. Tolerante à perda de 2 cópias para gravações e 3 cópias para leituras.
  - Aurora Replicas atuam simultaneamente como réplicas de leitura e alvos de failover automático prioritário com RTO < 30 segundos.

---

## 🌐 4. DNS e Estratégias de Disaster Recovery (DR)
- **Amazon Route 53 Routing Policies:**
  - **Failover Routing:** Ativo-Passivo baseado em Health Checks para desviar tráfego em falhas.
  - **Latency-based Routing:** Encaminha requisições para a região AWS com a menor latência para o usuário.
  - **Geolocation vs Geoproximity:** Geolocation roteia pelo país/continente do usuário; Geoproximity roteia pela proximidade geográfica real e permite ajuste via bias (requer Route 53 Traffic Flow).
  - **Multi-Value Answer:** Retorna múltiplos registros IP saudáveis com health checks simples.
- **Os 4 Padrões de Disaster Recovery (DR):**
  1. **Backup & Restore:** RTO alto (horas), RPO alto (horas), MENOR custo.
  2. **Pilot Light:** Recursos essenciais (banco de dados replicado) sempre ligados; compute provisionado apenas em desastre. RTO médio (dezenas de minutos).
  3. **Warm Standby:** Versão em escala reduzida do ambiente em execução contínua na região secundária. RTO baixo (minutos).
  4. **Multi-Site Active-Active:** Ambientes completos em execução contínua em múltiplas regiões. RTO ~0, RPO ~0, MAIOR custo.
