# Domínio 1: Design Solutions for Organizational Complexity (26%)

Este guia de referência detalha os cenários, arquiteturas e padrões de questões para o **Domínio 1** do exame SAP-C02.

---

## 🏗️ Padrões Arquiteturais Centrais

### 1. Conectividade de Rede Híbrida e Centralizada
- **Hub-and-Spoke com Transit Gateway (TGW):**
  - Conecta centenas de VPCs e redes on-premises (Direct Connect e VPNs).
  - Suporta *Transit Gateway Route Tables* separadas para isolar ambientes (ex: Prod, Dev, Shared Services, Inspection).
  - Suporta *Transit Gateway Peering* inter-regional para topologias multi-região.
- **VPC de Inspeção Centralizada (Centralized Inspection VPC):**
  - Todo o tráfego Norte-Sul (Internet) e Leste-Oeste (VPC para VPC ou On-prem para VPC) passa por firewalls de inspeção (AWS Network Firewall ou NGFW de terceiros).
  - Exige a ativação de **Appliance Mode** no Transit Gateway VPC Attachment da VPC de Inspeção para garantir tráfego bidirecional simétrico através da mesma AZ/firewall.
- **Resolução DNS Híbrida com Route 53 Resolver:**
  - **Inbound Endpoints:** Fornecem IPs privados na VPC para que servidores DNS on-premises encaminhem consultas de domínios privados da AWS (`.aws.internal` ou PHZs).
  - **Outbound Endpoints + Forwarding Rules:** Permitem que instâncias na AWS resolvam domínios on-premises (`.corp.local`), encaminhando as consultas para os IPs dos servidores DNS do datacenter.
  - As regras de encaminhamento (*Resolver Rules*) são compartilhadas com toda a organização via **AWS Resource Access Manager (RAM)**.
- **AWS PrivateLink e VPC Endpoint Services:**
  - Permite expor serviços com segurança para clientes em outras contas/VPCs sem expor à internet e sem exigir roteamento transitivo ou peering completo.
  - Funciona perfeitamente mesmo quando as VPCs possuem **blocos CIDR sobrepostos (overlapping CIDRs)**.
  - Utiliza um **Internal Network Load Balancer (NLB)** como frontend do Endpoint Service.

---

### 2. Governança Multi-Contas e Identidade
- **AWS Organizations e Service Control Policies (SCPs):**
  - Guardrails preventivos aplicados na raiz da organização, em OUs ou contas individuais.
  - Imposição de restrições globais: proibir desligamento do CloudTrail, proibir criação de recursos não criptografados (`rds:StorageEncrypted == false`, `ec2:Encrypted == false`), e restringir regiões permitidas (`aws:RequestedRegion`).
  - **Atenção:** SCPs afetam todas as contas membro (incluindo o usuário root), mas **não afetam a conta de gerenciamento (Management Account)**.
- **AWS IAM Identity Center (AWS SSO) com ABAC:**
  - Federação centralizada via SAML 2.0 com IdPs externos (Microsoft Entra ID, Okta, Ping Identity) e sincronização automática de usuários/grupos via **SCIM**.
  - **Attribute-Based Access Control (ABAC):** Mapeamento de atributos de sessão SAML para tags de sessão (`aws:PrincipalTag/Department`, `aws:PrincipalTag/CostCenter`).
  - Permite criar uma única política/Permission Set genérico que concede acesso dinâmico a recursos marcados com a mesma tag (`ResourceTag/Department == aws:PrincipalTag/Department`), eliminando a necessidade de dezenas de roles separadas.
- **AWS Control Tower & Landing Zones:**
  - Provisionamento automatizado de novas contas via **Account Factory** com guardrails preventivos (SCPs) e detectivos (AWS Config Rules).
  - Agregação centralizada de logs no **Log Archive Account** e notificações no **Audit Account**.
  - Customizações automatizadas com **Customizations for Control Tower (CfCT)** ou **Account Factory for Terraform (AFT)**.

---

## 🎯 Modelos de Cenários de Questões para o Domínio 1

1. **Cenário de Inspeção Centralizada:**
   - *Problema:* Uma empresa com 80 contas e 100 VPCs conectadas via Transit Gateway precisa inspecionar todo o tráfego inter-VPC e de saída para a internet com um firewall centralizado de alta disponibilidade, mantendo os IPs reais dos clientes e evitando assimetria de roteamento.
   - *Solução Correta:* Criar uma VPC de Inspeção centralizada com o AWS Network Firewall, anexá-la ao Transit Gateway com **Appliance Mode habilitado**, e configurar tabelas de rotas do TGW separadas para enviar o tráfego spokes -> inspection -> destino.

2. **Cenário de Governança de Acesso ABAC Multi-Contas:**
   - *Problema:* Uma organização possui 400 contas AWS e precisa conceder acesso baseado nas equipes e centros de custo dos usuários gerenciados no Microsoft Entra ID corporativo, sem criar ou gerenciar roles específicas para cada time em cada conta.
   - *Solução Correta:* Habilitar o AWS IAM Identity Center com sincronização SCIM e federação SAML 2.0. Configurar atributos de sessão no Permission Set e aplicar políticas IAM baseadas em ABAC usando a chave de condição `aws:PrincipalTag`.

3. **Cenário de Resolução DNS Híbrida Multi-Conta:**
   - *Problema:* 50 contas AWS conectadas via Direct Connect precisam resolver nomes de host corporativos do data center on-premises (`.corp`), e servidores locais precisam resolver zonas hospedadas privadas do Route 53.
   - *Solução Correta:* Criar Route 53 Inbound e Outbound Resolver Endpoints na VPC de Shared Services. Criar Forwarding Rules para o domínio on-premises e compartilhá-las com todas as contas da organização via AWS RAM.
