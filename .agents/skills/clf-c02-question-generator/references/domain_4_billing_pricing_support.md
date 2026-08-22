# Domínio 4: Billing, Pricing, and Support (12%)

Este guia de referência aborda os modelos de precificação da AWS, ferramentas de gerenciamento e controle de custos, planos de suporte e ecossistema de parceiros para o **Domínio 4** do exame CLF-C02.

---

## 💵 1. Modelos de Precificação do Amazon EC2

| Modelo | Funcionamento | Casos de Uso Recomendados |
| :--- | :--- | :--- |
| **On-Demand (Sob Demanda)** | Pagamento por segundo/hora sem compromisso a longo prazo. Taxa fixa horária. | Cargas de trabalho imprevisíveis, aplicações de curto prazo, testes ou desenvolvimento inicial. |
| **Savings Plans** | Descontos de até 72% mediante compromisso de uso monetário consistente ($/hora) por 1 ou 3 anos. Flexível entre tipos de instâncias, regiões e serviços (Compute Savings Plans incluem Fargate e Lambda). | Cargas de trabalho contínuas com uso previsível a médio/longo prazo. |
| **Reserved Instances (RIs)** | Descontos significativos (até 72%) mediante compromisso de 1 ou 3 anos com opções de pagamento (All Upfront, Partial Upfront, No Upfront). | Cargas de estado estacionário com capacidade previsível para EC2, RDS, Redshift. |
| **Spot Instances** | Descontos de até 90% utilizando capacidade ociosa do EC2. A AWS pode recuperar a instância com aviso prévio de 2 minutos. | Cargas tolerantes a interrupções, processamento em lote (batch), pipelines de dados, renderização e workers sem estado. |
| **Dedicated Hosts / Instances** | Servidores físicos dedicados de uso exclusivo de um único cliente. | Requisitos rigorosos de conformidade regulatória ou licenças de software por socket/core (BYOL). |

---

## 📊 2. Ferramentas de Gerenciamento de Custos e Faturamento

- **AWS Free Tier (Nível Gratuito):**
  - **Always Free:** Recursos gratuitos que não expiram (ex: 1.000.000 requisições do Lambda/mês, 25 GB do DynamoDB).
  - **12 Months Free:** Gratuito durante os primeiros 12 meses após a criação da conta (ex: 750 horas de EC2 `t2.micro`/`t3.micro`/mês, 5 GB no S3 Standard).
  - **Short-Term Trials:** Testes gratuitos por tempo limitado a partir do momento de ativação do serviço (ex: 30 dias do Amazon Inspector ou GuardDuty).
- **AWS Cost Explorer:**
  - Ferramenta visual interativa para visualizar, entender, analisar e **projetar gastos futuros (forecasting)** com base no histórico de até 12 meses.
- **AWS Budgets:**
  - Permite criar orçamentos personalizados com **limites monetários ou de uso**, enviando notificações automáticas por email ou Amazon SNS quando os custos reais ou previstos excederem o limite.
- **AWS Pricing Calculator:**
  - Calculadora online para modelar soluções e **estimar previamente os custos** de serviços da AWS antes de implantá-los em produção.
- **AWS Cost and Usage Report (CUR):**
  - O relatório de custos mais detalhado e abrangente da AWS, gravando metadados de cobrança por hora em arquivos CSV dentro de um bucket S3 para análise via Amazon Athena ou Amazon QuickSight.
- **Cost Allocation Tags:**
  - Tags chave-valor aplicadas aos recursos para categorizar e rastrear custos por centro de custo, equipe, aplicação ou ambiente de negócio no faturamento consolidado.

---

## 🤝 3. Planos de Suporte da AWS

| Recurso / Benefício | Basic Support | Developer Support | Business Support | Enterprise On-Ramp | Enterprise Support |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Preço** | Gratuito | A partir de $29/mês | A partir de $100/mês | A partir de $5.500/mês | A partir de $15.000/mês |
| **Canais de Contato** | Apenas suporte de faturamento/conta | Email (horário comercial) | Chat 24/7, telefone e email | Chat 24/7, telefone e email | Chat 24/7, telefone e email |
| **Quem pode abrir chamados técnicos?** | Ninguém (apenas fóruns) | 1 contato primário | Contatos ilimitados | Contatos ilimitados | Contatos ilimitados |
| **Tempo de Resposta (Casos Críticos)** | N/A | Orientação geral: < 24h; Sistema degradado: < 12h | Sistema de produção degradado: < 4h; **Sistema de produção fora do ar: < 1h** | Sistema de produção fora do ar: < 1h; **Sistema crítico de negócio fora: < 30m** | Sistema de produção fora: < 1h; **Sistema de missão crítica fora: < 15m** |
| **AWS Trusted Advisor** | 7 verificações básicas | 7 verificações básicas | **Todas as verificações completas** | **Todas as verificações completas** | **Todas as verificações completas** |
| **Gerenciamento Técnico de Conta (TAM)** | Não | Não | Não | Pool compartilhado de TAMs | **Technical Account Manager (TAM) DEDICADO** |
| **Outros Recursos Exclusivos** | AWS Health Dashboard | Recomendações de arquitetura geral | Orientação para arquitetura de produção | Revisões arquiteturais consultivas | **Concierge Support Team**, Consultoria proativa e Infrastructure Event Management (IEM) |

---

## 🌐 4. Programas e Recursos Adicionais
- **AWS Marketplace:** Catálogo digital com milhares de listagens de software de ISVs terceiros que podem ser implantados com cobrança unificada na fatura da AWS.
- **AWS Partner Network (APN):** Rede global de parceiros de serviços (consultoria) e software (tecnologia) credenciados pela AWS.
