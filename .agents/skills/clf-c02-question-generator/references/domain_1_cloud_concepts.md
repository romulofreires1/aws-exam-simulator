# Domínio 1: Cloud Concepts (24%)

Este guia de referência aborda os conceitos fundamentais de computação em nuvem, vantagens da AWS, os 6 pilares do Well-Architected Framework e estratégias de adoção de nuvem para o **Domínio 1** do exame CLF-C02.

---

## ☁️ 1. Vantagens e Benefícios da Nuvem AWS

1. **Trocar despesas de capital (CapEx) por despesas operacionais variáveis (OpEx):**
   - Em vez de investir pesado em data centers e servidores antes de saber como serão usados, o cliente paga apenas pelos recursos de computação consumidos e pelo tempo em que forem usados.
2. **Beneficiar-se de economias de escala massivas:**
   - Como centenas de milhares de clientes agregam seu uso na nuvem, a AWS alcança economias de escala mais altas, traduzindo-se em preços pré-pagos menores e reduções contínuas de preço.
3. **Parar de adivinhar a capacidade (Stop guessing capacity):**
   - Elimina o risco de subdimensionamento (queda de servidores em picos) ou superdimensionamento (recursos ociosos pagos). Recursos são provisionados ou encerrados automaticamente sob demanda.
4. **Aumentar a velocidade e a agilidade (Speed and Agility):**
   - Novos recursos de TI ficam disponíveis em minutos com poucos cliques, reduzindo o tempo de disponibilização para desenvolvedores de semanas para minutos.
5. **Parar de gastar dinheiro com a manutenção de data centers:**
   - Permite que a empresa foque em projetos que diferenciam o negócio (aplicações, clientes), enquanto a AWS cuida do "heavy lifting" indiferenciado (infraestrutura física, refrigeração, cabeamento, energia).
6. **Tornar-se global em minutos (Go global in minutes):**
   - Implantação rápida de aplicações em múltiplas regiões da AWS ao redor do mundo com latência mínima e baixo custo.

---

## 🏛️ 2. Os 6 Pilares do AWS Well-Architected Framework

| Pilar | Foco Principal | Exemplos Práticos / Serviços |
| :--- | :--- | :--- |
| **1. Excelência Operacional (Operational Excellence)** | Executar e monitorar sistemas, melhorar continuamente processos e procedimentos operacionais, automatizar alterações. | AWS CloudFormation (IaC), Amazon CloudWatch, AWS Systems Manager, evolução por pequenas falhas reversíveis. |
| **2. Segurança (Security)** | Proteger dados, sistemas e ativos, aplicar o princípio do menor privilégio, rastreabilidade e proteção em camadas. | AWS IAM, AWS KMS, AWS WAF, AWS Shield, Amazon GuardDuty, AWS CloudTrail. |
| **3. Confiabilidade (Reliability)** | Recuperar-se de interrupções de infraestrutura ou serviços, adquirir recursos computacionais dinamicamente para atender à demanda. | Multi-AZ deployments, Auto Scaling, Amazon S3 (99.999999999% durabilidade), Route 53 DNS Failover, testes de recuperação. |
| **4. Eficiência de Performance (Performance Efficiency)** | Usar recursos computacionais de forma eficiente para atender aos requisitos do sistema e manter a eficiência conforme a tecnologia evolui. | Escolha adequada de instâncias EC2, AWS Lambda, Amazon CloudFront, caching com ElastiCache, bancos especializados. |
| **5. Otimização de Custos (Cost Optimization)** | Evitar gastos desnecessários, entender onde os custos são incorridos e usar o modelo de preços ideal. | S3 Intelligent-Tiering, Compute Savings Plans, Instâncias Spot, AWS Cost Explorer, AWS Budgets. |
| **6. Sustentabilidade (Sustainability)** | Minimizar os impactos ambientais da execução de cargas de trabalho em nuvem, otimizando a utilização de recursos. | Utilização de processadores AWS Graviton, redução de recursos ociosos, políticas de retenção de dados eficientes. |

---

## 🚀 3. Estratégias de Adoção de Nuvem (AWS CAF e Migração)

- **AWS Cloud Adoption Framework (AWS CAF):**
  - **Perspectivas de Negócios:** *Negócios (Business)*, *Pessoas (People)* e *Governança (Governance)*.
  - **Perspectivas Técnicas:** *Plataforma (Platform)*, *Segurança (Security)* e *Operações (Operations)*.
- **As Estratégias de Migração (6/7 Rs):**
  - **Rehost ("Lift and Shift"):** Mover a aplicação para a nuvem sem qualquer alteração de código ou arquitetura (ex: usando AWS Application Migration Service - MGN).
  - **Replatform ("Lift, Tinker, and Shift"):** Fazer otimizações básicas na nuvem sem alterar a arquitetura central (ex: migrar de banco auto-hospedado para Amazon RDS).
  - **Refactor / Re-architect:** Redesenhar a aplicação do zero utilizando recursos nativos da nuvem (ex: migrar monólito para microsserviços serverless no Lambda e DynamoDB).
  - **Repurchase ("Drop and Shop"):** Substituir a aplicação existente por um produto SaaS de terceiros (ex: migrar CRM próprio para Salesforce ou AWS Marketplace).
  - **Retain:** Manter a aplicação no ambiente on-premises atual por enquanto.
  - **Retire:** Desativar aplicações ou servidores legados que não são mais necessários.
  - **Relocate:** Mover servidores virtuais VMware para o VMware Cloud on AWS sem alterar hardware ou configurações.
