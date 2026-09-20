# Prompt para a Geração do Simulado 9 (SAP-C02)

Copie e cole o prompt abaixo quando quiser gerar o Simulado 9.

```text
Preciso que você atue como o gerador de questões do simulador SAP-C02, criando o "Simulado 9" com exatamente 25 questões de nível "hard" totalmente inéditas. O objetivo é cobrir cenários arquitetônicos de nicho e integrações complexas que ainda não foram amplamente explorados nos simulados anteriores.

Siga **obrigatoriamente** as regras globais descritas no arquivo: `.agents/skills/aws-exam-generation-framework/SKILL.md`. As restrições incluem: distratores detalhados com 20-25 palavras, explicações ricas, estrutura JSON unificada com as traduções en, pt e es completas, e validação rigorosa contra a concentração de gabarito (vício de alternativas).

Para evitar limites de contexto, divida a criação em 5 lotes (scripts Python temporários) contendo 5 questões cada. Após gerar e validar cada lote individualmente, faça o merge em `src/data/exams/sap-c02-sim-9.json` e limpe os arquivos temporários.

Foque nos seguintes domínios e tópicos avançados (5 questões para cada):

1. **Multi-Account & Governance (Lote 1):** AWS Control Tower (Customizations), IAM Identity Center (integração SAML/OIDC avançada com IdPs externos), Service Control Policies (SCPs) complexas e AWS Organizations.
2. **Advanced Analytics & Streaming (Lote 2):** Amazon MSK (Managed Streaming for Kafka), EMR Serverless, Redshift Serverless e integrações de segurança e auditoria com o AWS Lake Formation.
3. **Complex Network Security (Lote 3):** Gateway Load Balancer (integração com firewalls de terceiros), AWS Network Firewall, VPC Traffic Mirroring e Transit Gateway Network Manager / Reachability Analyzer.
4. **CI/CD, Automation & Management (Lote 4):** CloudFormation StackSets (com AWS Organizations), AWS Service Catalog (para governança corporativa), Systems Manager Change Manager e EventBridge (Cross-account/Cross-Region event routing).
5. **Cost Optimization & Edge (Lote 5):** Cenários mistos de Savings Plans vs RIs (compra e compartilhamento em Organizations), EC2 Spot Fleet (Capacity Rebalance), AWS Local Zones e AWS Wavelength.

Para cada lote, crie um script gerador `.py` para construir o JSON, execute-o e valide-o estritamente com `validate_questions.py --strict`. Somente avance para o próximo lote se o script de validação retornar 0 erros. No final, garanta que não há vício de gabarito na consolidação final.
```
