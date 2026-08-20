# Regras e Anatomia para Criação de Questões SAP-C02

O exame **AWS Certified Solutions Architect - Professional (SAP-C02)** é notório pelo seu alto nível de complexidade técnica, enunciados longos e alternativas sofisticadas. Esta referência define as regras rigorosas para elaborar questões de nível profissional idênticas às da prova real.

---

## 1. Diferenças Críticas: Associate (SAA-C03) vs. Professional (SAP-C02)

| Dimensão | SAA-C03 (Associate) | SAP-C02 (Professional) |
| :--- | :--- | :--- |
| **Escopo** | Cenário isolado ou de 1 a 2 serviços (ex: EC2 + S3) | **Arquitetura Enterprise End-to-End** (5 a 8 serviços interconectados em múltiplas contas/regiões) |
| **Extensão do Enunciado** | 1 a 2 frases diretas | **2 a 4 frases detalhadas** com contexto de negócio, restrições e conformidade |
| **Extensão das Opções** | 1 frase curta por opção | **3 a 6 linhas por opção**, descrevendo sequências completas de configuração e passos de implementação |
| **Eliminação de Distratores** | 2 opções obviamente erradas/absurdas | **Todas as 4 ou 5 opções parecem plausíveis e viáveis tecnicamente**; a correta é diferenciada por nuances de eficiência, custo ou restrições específicas |
| **Foco de Decisão** | "Qual serviço faz X?" | "Qual combinação de serviços resolve o problema com a **MENOR sobrecarga operacional**, **MENOR custo** ou **SEM downtime**?" |
| **Tempo por Questão** | ~2 min por questão (130 min / 65 q) | **2 min 56 s por questão (176 segundos)** (220 min / 75 q) |

---

## 2. Anatomia de uma Questão SAP-C02

Toda questão deve conter 4 componentes obrigatórios no enunciado:

```
[1. CONTEXTO ENTERPRISE & ARQUITETURA ATUAL]
+ [2. PROBLEMA TÉCNICO OU NOVO REQUISITO DE NEGÓCIO]
+ [3. RESTRIÇÕES ESPECÍFICAS / CONSTRAINTS]
+ [4. DIRETIVA DE DECISÃO FINAL (GATILHO)]
```

### Exemplo de Estrutura de Enunciado:
1. **Contexto**: Uma empresa global de serviços financeiros possui mais de 300 contas AWS sob uma única organização no AWS Organizations, distribuídas em várias Unidades Organizacionais (OUs).
2. **Problema/Requisito**: A empresa precisa implementar uma solução de conectividade de rede hub-and-spoke para permitir que mais de 50 VPCs comuniquem-se de forma privada entre si e com a rede on-premises via AWS Direct Connect, inspecionando todo o tráfego Leste-Oeste e Norte-Sul com IDS/IPS centralizado.
3. **Restrições**: A solução deve manter o IP de origem dos clientes (sem SNAT), garantir roteamento simétrico através de appliances de firewall de alta disponibilidade em múltiplas AZs e suportar sobreposição de CIDR em ambientes de parceiros terceiros.
4. **Gatilho de Decisão**: *Qual arquitetura atenderá a esses requisitos com a MAIOR escalabilidade e MENOR complexidade de gerenciamento de rotas?*

---

## 3. Matriz de Palavras-Chave e Gatilhos de Decisão (Decision Triggers)

O final do enunciado determina qual trade-off da arquitetura deve vencer:

| Gatilho no Enunciado | Favorece Arquiteturas Com... | Desqualifica Arquiteturas Com... |
| :--- | :--- | :--- |
| **"MAIS eficiente operacionalmente"** / **"MENOR sobrecarga de gerenciamento"** | Serviços Serverless/Gerenciados (ex: IAM Identity Center, AWS Control Tower, AWS Network Firewall, AWS Lake Formation, AWS Systems Manager, EventBridge, Lambda) | Scripts personalizados em EC2, servidores BIND/Proxy manuais, agentes customizados, tarefas cron manuais. |
| **"MAIS econômica"** / **"MENOR custo"** | S3 Intelligent-Tiering / Glacier Deep Archive, Compute Savings Plans, VPC Gateway Endpoints (gratuitos), Spot Instances, DynamoDB On-Demand vs Provisioned. | NAT Gateways desnecessários, VPC Interface Endpoints em excesso, Direct Connect subutilizado, instâncias sob demanda 24/7. |
| **"MENOR tempo de inatividade"** / **"RTO < 5 minutos"** | Multi-Site Active-Active, Aurora Global Database, Route 53 ARC (Application Recovery Controller), DRS (Elastic Disaster Recovery), DynamoDB Global Tables. | Backup & Restore manual de snapshots, replicação assíncrona com failover manual, reconstrução de infraestrutura por CloudFormation no momento do desastre. |
| **"SEM alterar o código da aplicação"** | AWS Application Migration Service (MGN), AWS DMS, NLB/ALB proxy, API Gateway Private Integrations, Aurora MySQL/PostgreSQL compatibility. | Re-architect para DynamoDB, reescrita para Lambda Serverless, migração de banco relacional para chave-valor. |
| **"Maior resiliência / Tolerância a Falhas Regional"** | Multi-Region, S3 Cross-Region Replication + Multi-Region Access Points (MRAP), Aurora Global Database, Route 53 Geolocation / Latency Routing. | Arquiteturas Single-Region com apenas Multi-AZ. |
| **"Princípio do Menor Privilégio / Segurança Estrita"** | ABAC com tags de sessão (`aws:PrincipalTag`), SCPs com explicit deny, IAM Permission Boundaries, KMS Key Policies granulares. | Políticas IAM com wildcard (`"Action": "*"`), compartilhamento de credenciais estáticas, roles amplas. |

---

## 4. Engenharia de Distratores (Opções Incorretas)

Para que a questão seja genuinamente de nível Professional, crie distratores seguindo estas 4 categorias de armadilhas clássicas da AWS:

1. **O Anti-Padrão Tecnológico**:
   - Usa um serviço que tecnicamente funciona mas que viola os limites da AWS (ex: usar VPC Peering para roteamento transitivo entre 100 VPCs; usar DynamoDB para armazenar arquivos binários de 50MB).
2. **A Solução Operacionalmente Invencionista**:
   - Funciona, mas reinventa a roda com scripts manuais, EC2 e cron jobs quando existe um serviço nativo gerenciado (ex: criar um cluster BIND em EC2 para repasse de DNS em vez de usar Route 53 Resolver Inbound/Outbound Endpoints).
3. **A Falha de Escopo / Requisito Oculto**:
   - Atende à parte principal do problema mas ignora uma restrição crucial mencionada no texto (ex: atende a conectividade multi-conta, mas exige reconfigurar IPs e falha no requisito de blocos CIDR sobrepostos; ou atende a auditoria de logs, mas não impede que o usuário root da conta membro apague o CloudTrail).
4. **O Trade-off Invertido (Custo vs. Performance)**:
   - A solução é excessivamente cara para um requisito simples (ex: configurar Multi-Region Active-Active com Aurora Global Database quando o enunciado exigia explicitamente RTO de 24 horas e foco em menor custo).

---

## 5. Regras de Formato e Tipos de Questão

### Tipo Single Choice (Escolha Única)
- **4 alternativas (A, B, C, D)**.
- **Exatamente 1 alternativa correta**.
- `type: "single"`
- `requiredChoices: 1`

### Tipo Multiple Choice (Múltipla Escolha)
- **5 alternativas (A, B, C, D, E)** com **2 corretas** ("(Escolha duas.)" / "(Choose two.)"), OU
- **6 alternativas (A, B, C, D, E, F)** com **3 corretas** ("(Escolha três.)" / "(Choose three.)").
- `type: "multiple"`
- `requiredChoices: 2` ou `3`.
- No enunciado, inclua explicitamente a frase em negrito: `**Qual combinação de etapas atenderá a esses requisitos? (Escolha duas.)**`

---

## 6. Padrão de Explicações e Rationale

Cada questão gerada deve conter:
1. **Explicação de cada opção individual (`explanation`)**:
   - Começar com `Correto: ` ou `Incorreto: ` (ou `Correct: ` / `Incorrect: ` se em inglês).
   - Justificar claramente o motivo técnico e a relação com o Well-Architected Framework.
2. **Explicação Geral (`generalExplanation`)**:
   - Resumo arquitetural de 2 a 4 parágrafos sintetizando por que a solução escolhida é a recomendada pela AWS.
3. **URL de Referência Oficial (`referenceUrl`)**:
   - Link direto para a documentação oficial da AWS (docs.aws.amazon.com) ou AWS Architecture Blog / Whitepaper relevante.
