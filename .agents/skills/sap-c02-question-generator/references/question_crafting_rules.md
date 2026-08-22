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

## 6. Engenharia Rigorosa de Distratores (Eliminação de Alternativas Óbvias)

No exame SAP-C02, **nenhuma alternativa pode ser descartada com uma leitura rápida ou superficial**. Para que o simulador tenha o mesmo nível de dificuldade da prova oficial, os distratores **DEVEM** ser elaborados seguindo 4 regras fundamentais:

### 6.1. A Regra da Matriz de Decisão 2x2 (OBRIGATÓRIO)
Estruture as 4 alternativas em **dois pares de abordagens concorrentes**:
- **Abordagem 1 (2 opções: ex. A e B)**: Propõe resolver o cenário usando o Padrão Arquitetural X (ex: *AWS Network Firewall centralizado com Transit Gateway*).
- **Abordagem 2 (2 opções: ex. C e D)**: Propõe resolver o cenário usando o Padrão Arquitetural Y (ex: *Gateway Load Balancer com appliances de terceiros*).

Dentro de cada par:
- Uma opção acerta a implementação técnica completa e atende a todos os critérios do gatilho.
- A outra opção propõe quase os mesmos passos, mas erra em uma **nuance técnica crítica** (ex: esquece de habilitar o *Appliance Mode* no attachment do Transit Gateway, ou usa *Gateway Endpoint* em vez de *Interface Endpoint*).

Dessa forma, o candidato é forçado a:
1. Identificar qual das duas famílias arquiteturais (X ou Y) é a mais adequada para o trade-off do enunciado.
2. Analisar minuciosamente a configuração técnica interna para discernir qual das duas opções do mesmo padrão possui a implementação perfeita.

---

### 6.2. Simetria Estrutural e Sintática Estrita
- **Comprimento Equivalente**: Todas as 4 alternativas devem ter extensão semelhante (3 a 5 linhas de texto bem estruturado). Nunca crie a alternativa correta longa e detalhada e os distratores com apenas 1 linha.
- **Mesma Estrutura de Passos**: Todas as alternativas devem descrever uma sequência acionável e completa de passos técnicos:
  - *Passo 1*: Provisionamento/Criação do recurso base.
  - *Passo 2*: Configuração de rede, roteamento ou IAM.
  - *Passo 3*: Associação, política de segurança ou automação.

---

### 6.3. Os 4 Arquétipos de Distratores Profissionais (Plausible Distractors)

| Arquétipo | Como Funciona | Por Que o Candidato Fica em Dúvida? | Exemplo Real SAP-C02 |
| :--- | :--- | :--- | :--- |
| **1. A Nuance Técnica Oculta** *(Technical Nuance Trap)* | A arquitetura usa exatamente os serviços certos e modernos, mas falha em um detalhe interno de funcionamento da AWS. | Parece 100% correta à primeira vista; exige conhecimento profundo do serviço. | Configura S3 Cross-Region Replication para novos dados, mas omite o **S3 Batch Replication** para replicar os petabytes de dados já existentes no bucket. |
| **2. O Trade-off de Custo / Over-Engineering** *(Cost Mismatch)* | A solução funciona perfeitamente, é altamente resiliente e automatizada, mas é excessivamente complexa e cara para o RTO/RPO solicitado. | É uma solução válida em produção, mas desrespeita a restrição de "MENOR custo". | Propõe *Aurora Global Database Active-Active* e *Route 53 ARC* quando o enunciado solicitava uma solução econômica com RTO aceitável de 4 horas. |
| **3. A Sobrecarga Operacional Oculta** *(Overhead Trap)* | A arquitetura atinge o objetivo técnico, mas requer código customizado, scripts Lambda, agentes ou intervenção manual quando há funcionalidade nativa gerenciada. | É viável e comum em ambientes legados, mas perde para serviços nativos no critério "MENOR sobrecarga operacional". | Cria funções Lambda customizadas para consultar CloudWatch e atualizar rotas de DNS, em vez de usar *Route 53 Application Recovery Controller (ARC)* ou *DNS Failover* nativo. |
| **4. A Falha de Requisito Específico / Scope Gap** *(Compliance/Scope Gap)* | Resolve a infraestrutura principal com maestria, mas deixa de atender a um requisito secundário essencial mencionado no enunciado. | O candidato foca no problema principal e esquece da restrição secundária. | Configura tráfego privado via *VPC Peering*, mas não resolve o requisito de **blocos CIDR sobrepostos** (que exige *AWS PrivateLink*). |

---

### 6.4. Comparativo: Distrator Ruim/Óbvio vs. Distrator Profissional de Alta Fidelidade

#### Cenário de Exemplo:
*Empresa precisa inspecionar e filtrar tráfego de saída para a internet de 200 VPCs sem permitir bypass e com a menor sobrecarga de manutenção.*

- ❌ **Distrator Ruim / Óbvio (NÃO FAZER)**:
  > *"Instale instâncias EC2 com proxy Squid em cada uma das 200 VPCs e configure scripts de inicialização para atualizar as regras de iptables manualmente."*  
  *(Motivo do erro: Óbvio demais. Qualquer pessoa elimina imediatamente por ser anti-padrão absurdo).*

- ✅ **Distrator Profissional de Alta Fidelidade (FAZER)**:
  > *"Crie uma VPC de egresso centralizada contendo endpoints do AWS Network Firewall em sub-redes dedicadas em cada Availability Zone. Crie um AWS Transit Gateway e anexe todas as 200 VPCs de aplicação e a VPC de egresso. Atualize as tabelas de rotas das VPCs de aplicação para direcionar a rota padrão 0.0.0.0/0 para o Transit Gateway. Na VPC de egresso, configure o roteamento para o Network Firewall e depois para os NAT Gateways. Não habilite o Appliance Mode no attachment do Transit Gateway."*  
  *(Motivo da excelência: A arquitetura inteira está correta, usa os serviços enterprise exatos, mas a omissão do Appliance Mode causa assimetria no tráfego de retorno, quebrando conexões TCP com estado).*

---

## 7. Regras de Formato

### Tipo Single Choice (Escolha Única)
- **4 alternativas (A, B, C, D)**.
- **Exatamente 1 alternativa correta** (distribuída pseudo-aleatoriamente entre A, B, C ou D ~25% cada).
- `type: "single"`, `requiredChoices: 1`.

### Tipo Multiple Choice (Múltipla Escolha)
- **5 alternativas (A, B, C, D, E)** com **2 corretas**, OU **6 alternativas (A, B, C, D, E, F)** com **3 corretas**.
- `type: "multiple"`, `requiredChoices: 2` ou `3`.
- No enunciado, inclua em negrito: `**Qual combinação de ações atenderá a esses requisitos? (Escolha duas.)**` ou `(Escolha três.)`.
- Letras corretas distribuídas aleatoriamente (ex: `["B", "D"]`, `["A", "E"]`, `["C", "E"]`).
