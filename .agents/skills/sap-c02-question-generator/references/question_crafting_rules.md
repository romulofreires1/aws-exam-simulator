# Regras e Anatomia para Criação de Questões SAP-C02

O exame **AWS Certified Solutions Architect - Professional (SAP-C02)** avalia a capacidade de projetar arquiteturas avançadas, seguras, resilientes e econômicas na AWS em escala enterprise. Esta referência define as regras rigorosas para elaborar questões de nível profissional idênticas às da prova oficial.

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

## 2. Regra de Embaralhamento e Distribuição de Gabaritos (OBRIGATÓRIO)

Para garantir que o simulador seja um reflexo fiel da prova real e não induza vícios de resposta:

1. **PROIBIDO Gabarito Fixo em A ou A/B**:
   - **NUNCA** gere questões onde a resposta correta é invariavelmente a opção `A` (ou `A` e `B` em múltipla escolha).
2. **Distribuição Equilibrada e Aleatória**:
   - Em qualquer lote ou simulado de questões, a posição da resposta correta deve ser distribuída de forma uniforme e pseudo-aleatória entre todas as alternativas disponíveis:
     - **Escolha Única (Single Choice)**: ~25% das questões com gabarito `A`, ~25% `B`, ~25% `C`, ~25% `D`.
     - **Múltipla Escolha (Multiple Choice)**: As duplas/trios corretos devem variar amplamente (ex: `["B", "D"]`, `["A", "C"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`, `["A", "E"]`, `["C", "D"]`, etc.).
3. **Isolamento e Coerência de Explicação**:
   - A explicação (`explanation`) de cada alternativa deve permanecer estritamente atrelada ao conteúdo de sua própria opção ao embaralhar. A opção correta deve iniciar com `Correto: ` (ou `Correct: `) e os distratores com `Incorreto: ` (ou `Incorrect: `).

---

## 3. Cobertura Abrangente e Ineditismo de Cenários

Ao gerar novas questões:
1. **Cobertura Total do Blueprint**: O simulador pode e deve explorar qualquer serviço, recurso, padrão ou desafio técnico do exame SAP-C02 (conectividade híbrida, governança multi-contas, segurança e IAM, recuperação de desastres, modernização serverless, data lakes, finops, migração, etc.).
2. **Cenários Enterprise Originais**: Sintetize contextos de negócios diversificados e inovadores (ex: plataformas de telemetria IoT, processamento de pagamentos instantâneos, genômica e biotecnologia, streaming de mídia OTT, redes de distribuição global, SaaS multi-tenant B2B, manufatura automatizada).

---

## 4. Anatomia de uma Questão SAP-C02

Toda questão deve conter 4 componentes estruturais obrigatórios:

```
[1. CONTEXTO ENTERPRISE & ARQUITETURA ATUAL]
+ [2. PROBLEMA TÉCNICO OU NOVO REQUISITO DE NEGÓCIO]
+ [3. RESTRIÇÕES ESPECÍFICAS / CONSTRAINTS]
+ [4. DIRETIVA DE DECISÃO FINAL (GATILHO EM NEGRITO)]
```

### Exemplo de Estrutura:
1. **Contexto**: Uma instituição global de pagamentos executa uma arquitetura de microsserviços distribuída em mais de 150 contas AWS integradas via AWS Organizations e AWS Transit Gateway.
2. **Problema/Requisito**: A empresa precisa implementar uma solução de auditoria de conformidade para inspecionar e registrar todo o tráfego de saída (Egress) para a Internet, bloqueando conexões para domínios não autorizados e prevenindo exfiltração de dados confidenciais de cartões (PCI-DSS).
3. **Restrições**: A solução deve ser altamente disponível em múltiplas AZs, operar sem necessidade de NAT Gateway individual em cada VPC de aplicação, manter a simetria de fluxo sem utilizar SNAT e ter o menor custo de manutenção operacional.
4. **Gatilho de Decisão**: *Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de gerenciamento?*

---

## 5. Matriz de Palavras-Chave e Gatilhos de Decisão (Decision Triggers)

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

## 6. Engenharia de Distratores (Opções Incorretas)

Crie distratores autênticos seguindo estas 4 categorias clássicas de armadilhas da AWS:

1. **O Anti-Padrão Tecnológico**: Usa um serviço que não suporta a escala ou viola limites da AWS (ex: VPC Peering transitivo entre dezenas de VPCs; DynamoDB para arquivos binários grandes).
2. **A Solução Operacionalmente Invencionista**: Funciona, mas reinventa a roda com EC2 e scripts manuais quando há serviço nativo gerenciado (ex: cluster BIND em EC2 em vez de Route 53 Resolver).
3. **A Falha de Escopo / Requisito Oculto**: Atende ao objetivo geral, mas ignora uma restrição crucial (ex: não suporta IPs sobrepostos; não impede que o usuário root da conta membro apague logs).
4. **O Trade-off Invertido**: Solução excessivamente cara ou complexa para um requisito simples (ex: Multi-Region Active-Active com Aurora Global Database quando o requisito pedia menor custo e RTO de 24 horas).

---

## 7. Regras de Formato

### Tipo Single Choice (Escolha Única)
- **4 alternativas (A, B, C, D)**.
- **Exatamente 1 alternativa correta** (distribuída aleatoriamente entre A, B, C ou D).
- `type: "single"`, `requiredChoices: 1`.

### Tipo Multiple Choice (Múltipla Escolha)
- **5 alternativas (A, B, C, D, E)** com **2 corretas**, OU **6 alternativas (A, B, C, D, E, F)** com **3 corretas**.
- `type: "multiple"`, `requiredChoices: 2` ou `3`.
- No enunciado, inclua em negrito: `**Qual combinação de ações atenderá a esses requisitos? (Escolha duas.)**` ou `(Escolha três.)`.
- Letras corretas distribuídas aleatoriamente (ex: `["B", "D"]`, `["A", "E"]`).
