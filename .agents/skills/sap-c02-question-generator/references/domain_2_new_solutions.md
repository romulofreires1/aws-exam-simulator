# Domínio 2: Design for New Solutions (29%)

Este guia de referência detalha os cenários, arquiteturas e padrões de questões para o **Domínio 2** do exame SAP-C02.

---

## 🏗️ Padrões Arquiteturais Centrais

### 1. Estratégias de Disaster Recovery (DR) e Matriz RTO/RPO
| Estratégia de DR | RPO Típico | RTO Típico | Complexidade / Custo | Serviços AWS Chave |
| :--- | :--- | :--- | :--- | :--- |
| **Backup & Restore** | Horas a Dias | Horas a Dias | Custo Mínimo | AWS Backup, S3 Cross-Region Replication, Redshift Cross-Region Snapshots |
| **Pilot Light** | Minutos | 10 - 30 Minutos | Custo Baixo | AWS Elastic Disaster Recovery (DRS), RDS Cross-Region Read Replicas, AMIs/StackSets prontos |
| **Warm Standby** | Segundos | Poucos Minutos | Custo Moderado | Infraestrutura mínima ativa na região de DR, Aurora Read Replicas / Global Database, Auto Scaling pronto para expandir |
| **Multi-Site Active-Active** | Próximo de Zero | Próximo de Zero (Imediato) | Custo Altíssimo | Aurora Global Database, DynamoDB Global Tables, Route 53 ARC (Routing Controls / Readiness Checks), CloudFront |

- **AWS Elastic Disaster Recovery (DRS):** Replicação contínua em nível de bloco de servidores on-premises ou EC2 para uma região AWS de recuperação, usando instâncias EC2 pequenas na staging area para manter custos baixos até que o failover seja disparado.
- **AWS Route 53 Application Recovery Controller (ARC):** Gerencia controles de roteamento para failover regional automatizado e seguro, validando se a região de destino possui capacidade e integridade adequadas (*Readiness Checks*) antes de mudar o tráfego.

---

### 2. Bancos de Dados Multi-Região e Alta Disponibilidade
- **Amazon Aurora Global Database:**
  - Replicação de dados no nível de armazenamento físico entre regiões com latência < 1s.
  - Não afeta a performance de gravação na região primária.
  - Failover planejado ou recuperação de desastre não planejada com promoção de região secundária em menos de 1 minuto sem perda de dados.
- **Amazon DynamoDB Global Tables:**
  - Replicação totalmente gerenciada ativo-ativo multi-região.
  - Resolução de conflitos baseada em carimbo de data/hora ("last-writer-wins").
  - Ideal para aplicações globais distribuídas com leituras e gravações locais de baixa latência em milissegundos.
- **RDS Multi-AZ vs. Multi-AZ DB Cluster vs. Read Replicas:**
  - *Multi-AZ Instance:* Standby síncrono para failover automático em outra AZ (não aceita tráfego de leitura).
  - *Multi-AZ DB Cluster:* 1 primário + 2 réplicas de leitura síncronas/semissíncronas em diferentes AZs com menor latência de commit e failover em < 35s.
  - *Read Replicas:* Replicação assíncrona para escalar leitura; podem ser promovidas em caso de desastre (exige reinicialização e RTO maior).

---

### 3. Governança e Analytics de Data Lakes (AWS Lake Formation)
- **AWS Lake Formation:**
  - Centraliza o controle de acesso fino (a nível de banco, tabela, coluna, linha e célula) sobre dados no Amazon S3.
  - Substitui regras IAM e políticas de bucket excessivamente complexas.
  - Integra nativamente com **Amazon Athena**, **Amazon Redshift Spectrum**, **AWS Glue** e **Amazon EMR**.
  - Permite compartilhamento federado de dados (*cross-account data sharing*) sem duplicação de datasets.

---

### 4. Sistemas de Arquivos Compartilhados de Alta Performance (FSx Suite)
- **Amazon FSx for NetApp ONTAP:**
  - Suporta protocolos NFS, SMB e iSCSI.
  - Tiering automático de dados frios para armazenamento em nuvem S3.
  - SnapMirror entre regiões para replicação de dados e DR.
- **Amazon FSx for Windows File Server:**
  - Suporte total a SMB, integração nativa Multi-AZ com Microsoft Active Directory e DFS Namespaces.
- **Amazon FSx for OpenZFS & Lustre:**
  - OpenZFS: Armazenamento NFS POSIX de altíssimo IOPS e baixa latência.
  - Lustre: Projetado para cargas HPC, machine learning e renderização de vídeo integrado a buckets S3.

---

## 🎯 Modelos de Cenários de Questões para o Domínio 2

1. **Cenário de DR de Baixa Latência e Alta Resiliência:**
   - *Problema:* Aplicação bancária crítica com base de dados relacional precisa de RPO < 1 segundo e RTO < 2 minutos em caso de falha regional total, com capacidade de validação automática de prontidão da infraestrutura na região secundária.
   - *Solução Correta:* Implementar **Amazon Aurora Global Database** na região primária e secundária, combinado com o **AWS Route 53 Application Recovery Controller (ARC)** com Readiness Checks e Routing Controls.

2. **Cenário de Governança de Data Lake em Larga Escala:**
   - *Problema:* Uma empresa armazena centenas de Terabytes de dados analíticos no Amazon S3. Diversos times (Finanças, RH, Marketing) em contas AWS distintas precisam consultar dados usando o Amazon Athena, mas a equipe de segurança exige que dados confidenciais (PII) em certas colunas e linhas sejam mascarados ou inacessíveis para o time de Marketing.
   - *Solução Correta:* Utilizar o **AWS Lake Formation** para registrar o bucket S3, definir controle de acesso granular a nível de linha e coluna baseado em tags LF-tags, e conceder permissões cross-account para as contas dos times.
