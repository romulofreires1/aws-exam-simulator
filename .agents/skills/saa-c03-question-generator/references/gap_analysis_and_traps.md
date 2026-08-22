# Padrões Arquiteturais e Armadilhas Clássicas do Exame SAA-C03

Esta referência compila os principais pares conceituais e armadilhas frequentes encontradas no exame **AWS Certified Solutions Architect - Associate (SAA-C03)**.

---

## ⚠️ 1. As 10 Armadilhas Mais Frequentes no SAA-C03

### 1. S3 Gateway Endpoint vs. Interface Endpoint (AWS PrivateLink)
- **Armadilha:** Propor Gateway Endpoint para conectar-se ao S3 a partir de um data center on-premises via Direct Connect ou de outra região via VPC Peering.
- **Regra:** **Gateway Endpoints** funcionam apenas dentro da própria VPC local (via rotas na route table) e são gratuitos. Se o tráfego vier de on-premises (Direct Connect/VPN) ou de outra VPC, é obrigatório utilizar um **Interface Endpoint** (PrivateLink).

### 2. RDS Multi-AZ vs. Read Replicas
- **Armadilha:** Sugerir Read Replicas para solucionar uma exigência de recuperação de desastres ou alta disponibilidade com failover automático síncrono.
- **Regra:** **Multi-AZ** é para Alta Disponibilidade / Resiliência (replicação síncrona, failover automático transparente em 1-2 min). **Read Replicas** são para Escalabilidade de Leitura e Performance (replicação assíncrona; failover exige intervenção/promoção manual).

### 3. Origin Access Control (OAC) vs. Origin Access Identity (OAI)
- **Armadilha:** Escolher OAI como melhor prática em novas arquiteturas.
- **Regra:** **OAC** é o padrão moderno da AWS que suporta todos os buckets S3 em todas as regiões, criptografia SSE-KMS e métodos HTTP avançados (PUT/DELETE/POST). OAI é um recurso legado.

### 4. S3 Intelligent-Tiering vs. Políticas de Ciclo de Vida (S3 Lifecycle)
- **Armadilha:** Configurar regras de ciclo de vida com dias fixos (ex: transição aos 30 dias) quando o enunciado menciona que os "padrões de acesso aos dados são desconhecidos, imprevisíveis ou mudam constantemente".
- **Regra:** Padrão desconhecido ou variável = **S3 Intelligent-Tiering**. Padrão conhecido (ex: acessado no 1º mês e arquivado após 90 dias) = **S3 Lifecycle Rules**.

### 5. SQS Standard vs. SQS FIFO
- **Armadilha:** Usar fila Standard quando a ordem exata das transações financeiras e a garantia de não duplicidade forem mandatórias.
- **Regra:** Se a ordem estrita e entrega única ("exactly-once") importam, use **SQS FIFO** (com Message Group ID e Deduplication ID).

### 6. Instâncias Spot vs. On-Demand / Savings Plans
- **Armadilha:** Propor Instâncias Spot para aplicações com estado (stateful), bancos de dados críticos ou serviços que não toleram interrupções com aviso de 2 minutos.
- **Regra:** **Spot** é exclusivo para cargas de trabalho sem estado (stateless), processamento em lote (batch), workers de filas SQS e pipelines distribuídos.

### 7. ALB vs. NLB vs. Gateway Load Balancer
- **Armadilha:** Utilizar ALB para tráfego TCP/UDP não-HTTP, para requisitos de IP estático por AZ ou para milhões de requisições por segundo com latência de microssegundos.
- **Regra:** HTTP/HTTPS, path routing, host routing = **ALB (L7)**. TCP/UDP, IPs estáticos/Anycast, ultra-alta taxa de transferência = **NLB (L4)**. Terceiros firewalls de rede = **GWLB (L3)**.

### 8. VPC Peering vs. AWS Transit Gateway
- **Armadilha:** Configurar VPC Peering quando é exigido tráfego transitivo (A conecta em B, B conecta em C, e A precisa falar com C sem conexão direta).
- **Regra:** VPC Peering **NÃO** suporta roteamento transitivo. Se for necessária topologia hub-and-spoke transitiva entre dezenas de VPCs, utilize o **AWS Transit Gateway**.

### 9. Armazenamento Compartilhado: EBS Multi-Attach vs. EFS vs. FSx
- **Armadilha:** Tentar anexar um volume EBS gp3 a várias instâncias em AZs diferentes.
- **Regra:** EBS Multi-Attach funciona apenas com volumes **io2** e **dentro da mesma Availability Zone**. Para compartilhamento Multi-AZ compatível com POSIX/Linux, use o **Amazon EFS**. Para Windows/SMB/AD, use o **Amazon FSx for Windows**.

### 10. Secrets Manager vs. SSM Parameter Store
- **Armadilha:** Usar Parameter Store quando a principal exigência é **rotação automática gerenciada** de credenciais com AWS Lambda nativo.
- **Regra:** Se precisar de rotação automática de senhas de bancos RDS sem código manual = **AWS Secrets Manager**. Se for configuração de texto simples ou chave criptografada com baixo custo = **SSM Parameter Store**.
