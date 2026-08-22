# Domínio 3: Design High-Performing Architectures (24%)

Este guia de referência aborda computação, armazenamento, bancos de dados, aceleração de rede e ingestão de dados de alto desempenho para o **Domínio 3** do exame SAA-C03.

---

## 💾 1. Armazenamento de Alto Desempenho
- **Amazon Elastic Block Store (EBS):**
  - **gp3 (General Purpose SSD):** Volume padrão de uso geral com baseline de 3.000 IOPS e 125 MB/s independentes do tamanho do volume, expansível até 16.000 IOPS e 1.000 MB/s.
  - **io2 / io2 Block Express (Provisioned IOPS SSD):** Projetado para bancos de dados corporativos críticos I/O-intensive (até 256.000 IOPS e 4.000 MB/s com 99,999% de durabilidade). Suporta **Multi-Attach** em instâncias Nitro na mesma AZ.
  - **st1 (Throughput Optimized HDD) / sc1 (Cold HDD):** Projetados para grandes volumes sequenciais (Big Data, Data Warehouses, logs) - NÃO suportam boot volumes.
- **Amazon Elastic File System (EFS):**
  - Armazenamento em nível de arquivo gerenciado, elástico e compatível com NFSv4 para Linux.
  - Suporta acesso simultâneo de centenas/milhares de instâncias EC2, containers ECS/EKS e funções Lambda.
  - Modos de desempenho: *General Purpose* (baixa latência por operação) e *Max I/O* (alta concorrência e throughput massivo agregados).
- **Amazon FSx Family:**
  - **FSx for Windows File Server:** SMB nativo, integração com Microsoft Active Directory e suporte a DFS Namespaces.
  - **FSx for Lustre:** Sistema de arquivos POSIX de ultra-alto desempenho (centenas de GB/s e milhões de IOPS) para cargas de trabalho de HPC, Machine Learning e processamento financeiro, integrado diretamente a buckets S3.
- **Amazon S3 High Performance:**
  - **S3 Express One Zone:** Armazenamento em zona única de baixíssima latência de milissegundos de um dígito (single-digit millisecond latency) para centenas de milhares de requisições por segundo.
  - Particionamento por prefixos para escalabilidade horizontal de requisições (3.500 PUT/POST/DELETE e 5.500 GET/HEAD por segundo por prefixo).

---

## 💻 2. Computação Elástica e Serverless
- **Famílias de Instâncias EC2:**
  - **General Purpose (M, T):** Equilíbrio entre computação, memória e rede.
  - **Compute Optimized (C):** Alta proporção CPU/Memória para computação intensiva (processamento de vídeo, servidores de jogos, inferência ML).
  - **Memory Optimized (R, X, z):** Grandes conjuntos de dados em memória (bancos de dados in-memory Redis, cache de alto desempenho, SAP HANA).
  - **Storage Optimized (I, D, H):** Alto throughput sequencial e IOPS local NVMe (bancos NoSQL, Cassandra, data lakes locais).
  - **Processadores AWS Graviton:** CPUs baseadas em ARM de alta eficiência energética com até 40% de melhora no custo-benefício em comparação com arquiteturas x86 comparáveis.
- **Computação Serverless e Containers:**
  - **AWS Lambda:** Execução orientada a eventos sem provisionamento de servidores. Concorrência provisionada (Provisioned Concurrency) para eliminar atrasos de inicialização a frio (cold starts).
  - **AWS Fargate:** Mecanismo de execução serverless para Amazon ECS e EKS, eliminando a gestão do cluster subjacente de instâncias EC2.

---

## 🚀 3. Bancos de Dados e Caching de Baixa Latência
- **Amazon DynamoDB & DAX:**
  - Banco de dados NoSQL de chave-valor e documentos totalmente gerenciado, com latência consistente de milissegundos de um dígito em qualquer escala.
  - **DynamoDB Accelerator (DAX):** Cache em memória totalmente gerenciado para DynamoDB que reduz a latência de leitura de milissegundos para **microssegundos** sem alterar a lógica de dados.
- **Amazon ElastiCache:**
  - **ElastiCache for Redis (ou Valkey):** Suporta estruturas de dados complexas, persistência, Multi-AZ com failover automático, réplicas de leitura e Pub/Sub.
  - **ElastiCache for Memcached:** Cache de objetos chave-valor simples, multi-thread, puro em memória sem persistência.
  - **Padrões de Caching:** *Lazy Loading / Cache-Aside* (carrega sob demanda) vs *Write-Through* (atualiza cache junto com gravação no banco).

---

## ⚡ 4. Aceleração de Rede e Ingestão de Dados
- **Amazon CloudFront:**
  - Rede global de entrega de conteúdo (CDN) com mais de 400+ Pontos de Presença (Edge Locations). Faz cache de conteúdo estático e dinâmico, suporta compressão Brotli/Gzip e terminação SSL/TLS na borda.
- **AWS Global Accelerator:**
  - Acelera o tráfego TCP/UDP de usuários globais roteando requisições através de IPs estáticos Anycast diretamente para a rede backbone global da AWS, evitando a internet pública instável.
- **Amazon Kinesis:**
  - **Kinesis Data Streams:** Ingestão de dados em tempo real com retenção de 24 horas até 365 dias, permitindo múltiplos consumidores simultâneos e processamento personalizado via Lambda/KCL.
  - **Kinesis Data Firehose:** Entrega automatizada e transformação de streaming sem servidor para S3, Redshift, OpenSearch e Splunk com buffer configurável por tempo/tamanho.
