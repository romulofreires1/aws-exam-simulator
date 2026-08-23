# Regras e Anatomia para Criação de Questões SAP-C02

O exame **AWS Certified Solutions Architect - Professional (SAP-C02)** avalia a capacidade de projetar arquiteturas avançadas, seguras, resilientes e econômicas na AWS em escala enterprise. Esta referência define as regras rigorosas para elaborar questões de nível profissional idênticas às da prova oficial.

---

## 1. Regra de Cota e Tamanho (OBRIGATÓRIO)

No exame SAP-C02:
1. **Quotas de Múltipla Escolha**: Pelo menos **20% a 25%** das questões de um lote ou simulado DEVEM ser do tipo `multiple` (ex: 5 a 6 questões em um simulado de 25).
   - "Escolha duas": Deve possuir exatamente **5 alternativas (A, B, C, D, E)**.
   - "Escolha três": Deve possuir exatamente **6 alternativas (A, B, C, D, E, F)**.
2. **Tamanho Mínimo de Alternativa**: Cada alternativa deve ter, no mínimo, **25 a 45 palavras** detalhando a implementação passo a passo. Alternativas com menos de 20 palavras não descrevem a arquitetura enterprise de forma adequada e serão rejeitadas.

## 2. Diferenças Críticas: Associate (SAA-C03) vs. Professional (SAP-C02)

| Dimensão | SAA-C03 (Associate) | SAP-C02 (Professional) |
| :--- | :--- | :--- |
| **Escopo** | Cenário isolado ou de 1 a 2 serviços (ex: EC2 + S3) | **Arquitetura Enterprise End-to-End** (5 a 8 serviços interconectados em múltiplas contas/regiões) |
| **Extensão do Enunciado** | 1 a 2 frases diretas | **2 a 4 frases detalhadas** com contexto de negócio, restrições e conformidade |
| **Extensão das Opções** | 1 frase curta por opção | **3 a 6 linhas por opção** (25+ palavras), descrevendo sequências completas de configuração e passos de implementação |
| **Eliminação de Distratores** | 2 opções obviamente erradas/absurdas | **Todas as opções parecem plausíveis e viáveis tecnicamente**; a correta é diferenciada por nuances de eficiência, custo ou restrições específicas |
| **Foco de Decisão** | "Qual serviço faz X?" | "Qual combinação de serviços resolve o problema com a **MENOR sobrecarga operacional**, **MENOR custo** ou **SEM downtime**?" |
| **Tempo por Questão** | ~2 min por questão (130 min / 65 q) | **2 min 56 s por questão (176 segundos)** (220 min / 75 q) |

---

## 3. Regra de Embaralhamento e Distribuição de Gabaritos

Para garantir que o simulador seja um reflexo fiel da prova real e não induza vícios de resposta:
1. **PROIBIDO Gabarito Fixo em A ou A/B**: **NUNCA** gere questões onde a resposta correta é invariavelmente a opção `A` (ou `A` e `B` em múltipla escolha).
2. **Distribuição Equilibrada e Aleatória**:
   - **Escolha Única (Single Choice)**: ~25% `A`, ~25% `B`, ~25% `C`, ~25% `D`.
   - **Múltipla Escolha (Multiple Choice)**: As duplas/trios corretos devem variar amplamente (ex: `["B", "D"]`, `["A", "C"]`, `["C", "E"]`, `["A", "D"]`, `["B", "E"]`).
3. A explicação de cada alternativa deve iniciar com `Correto: ` na opção que é a resposta e `Incorreto: ` nos distratores.

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
2. **Problema/Requisito**: A empresa precisa implementar uma solução de auditoria de conformidade para inspecionar e registrar todo o tráfego de saída (Egress) para a Internet...
3. **Restrições**: A solução deve ser altamente disponível em múltiplas AZs, operar sem necessidade de NAT Gateway individual em cada VPC de aplicação, manter a simetria de fluxo sem utilizar SNAT e ter o menor custo de manutenção operacional.
4. **Gatilho de Decisão**: *Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de gerenciamento?*

---

## 5. Engenharia Rigorosa de Distratores ("Micro-Diff" e Simetria)

No exame SAP-C02, **nenhuma alternativa pode ser descartada com uma leitura rápida ou superficial**. Para que o simulador tenha o mesmo nível de dificuldade da prova oficial, os distratores **DEVEM** ser elaborados seguindo 3 regras fundamentais:

### 5.1. A Regra da Matriz de Decisão 2x2 (Micro-Diff)
Estruture as 4 alternativas em **dois pares de abordagens concorrentes** que são quase idênticos (90% do texto igual). A diferença entre um distrator plausível e a resposta correta deve ser sutil:
- **Flag/Atributo de configuração**: ex: *Appliance Mode* ativado vs desativado no TGW attachment.
- **Chamada de API**: ex: usar `MoveAccount` vs `RemoveAccountFromOrganization` e `InviteAccountToOrganization` (sendo que Move não pode mover entre organizações distintas).
- **Tipo de componente**: ex: *Interface Endpoint* (resolve) vs *Gateway Endpoint* (não suportado on-premise).
- **Hooks de eventos**: ex: Função Lambda de exceção vs etapa nominal do workflow.

### 5.2. Simetria Estrutural Estrita
Todas as opções DEVEM ter comprimento equivalente e descrever os passos técnicos completos na mesma ordem (1. Provisionamento, 2. Rede/IAM, 3. Associação/Regras).

### 5.3. Exemplo Prático (Transfer Family PGP - O "Padrão Ouro")
Note como as alternativas são longas e simétricas, diferindo APENAS no tipo de chave (`chave pública` vs `chave privada`), tipo de etapa (`nominal` vs `exceção`) e target de associação (`servidor` vs `usuário`):

*   **A (Incorreto):** Armazenar a **chave pública PGP** no Secrets Manager. Adicionar uma **etapa nominal** no fluxo de trabalho gerenciado do Transfer Family para descriptografar arquivos. Configurar os parâmetros de criptografia PGP na etapa nominal. Associar o fluxo de trabalho ao **servidor do Transfer Family**.
*   **B (Incorreto):** Armazenar a **chave privada PGP** no Secrets Manager. Adicionar uma **etapa de tratamento de exceções** no fluxo de trabalho gerenciado do Transfer Family para descriptografar arquivos. Configurar os parâmetros de criptografia PGP no tratador de exceções. Associar o fluxo de trabalho ao **usuário do SFTP**.
*   **C (Correto):** Armazenar a **chave privada PGP** no Secrets Manager. Adicionar uma **etapa nominal** no fluxo de trabalho gerenciado do Transfer Family para descriptografar arquivos. Configurar os parâmetros de descriptografia PGP na etapa nominal. Associar o fluxo de trabalho ao **servidor do Transfer Family**.
*   **D (Incorreto):** Armazenar a **chave pública PGP** no Secrets Manager. Adicionar uma **etapa de tratamento de exceções** no fluxo de trabalho...

### 5.4. Os 4 Arquétipos de Distratores Profissionais (Plausible Distractors)

| Arquétipo | Como Funciona | Por Que o Candidato Fica em Dúvida? |
| :--- | :--- | :--- |
| **1. A Nuance Técnica Oculta** *(Technical Nuance Trap)* | A arquitetura usa exatamente os serviços certos, mas falha em um detalhe interno. | Parece correta; exige conhecimento profundo do serviço (ex: Omitir o S3 Batch Replication para replicar objetos existentes num bucket de origem). |
| **2. O Trade-off de Custo** *(Cost Mismatch)* | A solução funciona perfeitamente, mas é excessivamente complexa e cara. | É viável em produção, mas desrespeita a restrição de "MENOR custo" (ex: Usar Aurora Global Database quando o RTO solicitado era de 4 horas). |
| **3. A Sobrecarga Operacional Oculta** *(Overhead Trap)* | Requer código customizado, scripts Lambda/cron ou EC2 quando há funcionalidade nativa. | Perde para serviços gerenciados no critério "MENOR sobrecarga operacional". |
| **4. A Falha de Escopo** *(Compliance/Scope Gap)* | Resolve o problema principal, mas esquece de um requisito secundário essencial. | O candidato foca na parte técnica principal e esquece a restrição do final do parágrafo. |
