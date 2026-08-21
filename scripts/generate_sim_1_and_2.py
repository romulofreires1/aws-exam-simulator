#!/usr/bin/env python3
"""
Script gerador para Simulado 1 e Simulado 2 do AWS SAP-C02.
Gera 25 questões inéditas de nível profissional para cada simulado com distribuição balanceada de gabarito.
"""

import json
import os

SIM1_DATA = {
  "id": "SAP-C02-SIM-1",
  "title": "AWS Solutions Architect Professional — Simulado 1 (25Q Inéditas)",
  "code": "SAP-C02-SIM-1",
  "category": "Professional",
  "description": "Simulado prático com 25 questões inéditas de alta complexidade cobrindo os 4 domínios da prova SAP-C02: redes enterprise, governança multi-contas, resiliência/DR, analytics e modernização. Tempo calibrado a 2m 56s por questão (73 minutos).",
  "totalQuestions": 25,
  "timeLimitMinutes": 73,
  "passingScore": 750,
  "icon": "shield-check",
  "domains": [
    {
      "id": "domain-1-org-complexity",
      "name": "Domain 1: Design Solutions for Organizational Complexity",
      "weightPercentage": 26
    },
    {
      "id": "domain-2-new-solutions",
      "name": "Domain 2: Design for New Solutions",
      "weightPercentage": 29
    },
    {
      "id": "domain-3-continuous-improvement",
      "name": "Domain 3: Continuous Improvement for Existing Solutions",
      "weightPercentage": 25
    },
    {
      "id": "domain-4-migration-modernization",
      "name": "Domain 4: Accelerate Workload Migration and Modernization",
      "weightPercentage": 20
    }
  ],
  "questions": [
    {
      "id": "sim1-q001",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Transit Gateway", "AWS Network Firewall", "AWS Organizations"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação global de comércio eletrônico gerencia 350 contas no AWS Organizations estruturadas em uma topologia hub-and-spoke com o AWS Transit Gateway (TGW). A diretoria de segurança cibernética exige que todo o tráfego inter-VPC (Leste-Oeste) e o tráfego de saída para a Internet (Norte-Sul) passem obrigatoriamente por uma frota centralizada de firewalls com estado de inspeção profunda de pacotes (AWS Network Firewall). A solução deve manter os endereços IP de origem reais dos clientes sem utilizar Source NAT (SNAT), garantir simetria de fluxo bidirecional em múltiplas Availability Zones e evitar assimetria de roteamento. Qual arquitetura atenderá a esses requisitos com a MENOR sobrecarga de gerenciamento de rotas?",
      "options": [
        {
          "id": "A",
          "text": "Implantar um cluster de instâncias EC2 com firewall NGFW de terceiros em cada VPC de aplicação individual com interfaces de rede elásticas (ENIs) secundárias e rotas estáticas locais.",
          "explanation": "Incorreto: Implementar firewalls individuais em cada uma das 350 VPCs descentraliza a gestão de regras e gera altíssima sobrecarga operacional e custos excessivos."
        },
        {
          "id": "B",
          "text": "Estabelecer conexões de VPC Peering completas entre todas as 350 VPCs e usar um Network Load Balancer (NLB) com SNAT habilitado em uma VPC de segurança compartilhada.",
          "explanation": "Incorreto: VPC Peering não escala para centenas de VPCs (limite de conexões e sem suporte a roteamento transitivo) e o uso de SNAT viola o requisito de preservar os IPs de origem reais."
        },
        {
          "id": "C",
          "text": "Criar uma VPC de Inspeção centralizada com endpoints do AWS Network Firewall em subnets dedicadas por AZ. Anexar a VPC de Inspeção ao AWS Transit Gateway com a opção 'Appliance Mode' habilitada e configurar tabelas de rotas do TGW separadas para direcionar o tráfego das VPCs spokes para a VPC de inspeção antes de atingir o destino.",
          "explanation": "Correto: A habilitação do Appliance Mode no anexo do Transit Gateway com a VPC de Inspeção garante que o tráfego de ida e volta seja processado simetricamente pela mesma AZ do firewall, eliminando a necessidade de SNAT e preservando o IP de origem dos clientes com gerenciamento centralizado."
        },
        {
          "id": "D",
          "text": "Configurar regras de Security Groups e Network ACLs restritivas em todas as VPCs spokes e utilizar o AWS WAF diretamente nos Application Load Balancers de cada conta membro.",
          "explanation": "Incorreto: O AWS WAF atua na camada 7 para tráfego web de entrada e não inspeciona tráfego de rede genérico Leste-Oeste (L3/L4) entre VPCs ou saída TCP/UDP arbitrária."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "Em arquiteturas hub-and-spoke com o AWS Transit Gateway, a centralização da inspeção de tráfego com o AWS Network Firewall requer a ativação do recurso 'Appliance Mode' no Transit Gateway VPC Attachment. Esse recurso força o TGW a usar a mesma interface de rede e AZ para os fluxos de envio e resposta, garantindo roteamento simétrico sem necessidade de SNAT.",
      "referenceUrl": "https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q002",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["Amazon Route 53", "AWS Resource Access Manager", "AWS Direct Connect"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma montadora de veículos elétricos opera uma plataforma de telemetria conectada a mais de 80 contas AWS e a dois datacenters on-premises por meio de conexões redundantes do AWS Direct Connect. A empresa precisa implementar uma solução de resolução de DNS híbrida para que servidores on-premises resolvam zonas hospedadas privadas do Route 53 (.corp.aws) e instâncias na AWS resolvam nomes internos do datacenter (.corp.local). A solução deve ser compartilhada com todas as contas da organização de forma centralizada e sem gerenciar servidores BIND ou Unbound em instâncias EC2. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Criar Route 53 Resolver Inbound Endpoints e Outbound Endpoints em uma VPC de Serviços Compartilhados. Criar regras de encaminhamento (Forwarding Rules) no Route 53 Resolver apontando para os servidores DNS on-premises e compartilhá-las com toda a organização no AWS Organizations via AWS Resource Access Manager (RAM).",
          "explanation": "Correto: O Route 53 Resolver com Inbound Endpoints permite que o datacenter resolva PHZs da AWS, enquanto Outbound Endpoints + Forwarding Rules permitem que a AWS resolva nomes locais. O compartilhamento via AWS RAM elimina a duplicação de infraestrutura em cada conta."
        },
        {
          "id": "B",
          "text": "Instalar servidores DNS BIND em instâncias EC2 em Auto Scaling groups em cada conta membro e configurar tabelas de encaminhamento estáticas sincronizadas por scripts do AWS Systems Manager.",
          "explanation": "Incorreto: Gerenciar clusters de DNS em EC2 em 80 contas acarreta alta sobrecarga de manutenção e viola as melhores práticas de uso de serviços gerenciados nativos."
        },
        {
          "id": "C",
          "text": "Configurar zonas hospedadas públicas no Amazon Route 53 para todos os domínios internos e restringir o acesso usando políticas de roteamento baseadas em geolocalização e Security Groups.",
          "explanation": "Incorreto: Zonas públicas expõem registros internos para a internet pública e não resolvem a resolução privada segura necessária para ambientes corporativos híbridos."
        },
        {
          "id": "D",
          "text": "Associar manualmente cada uma das zonas hospedadas privadas do Route 53 a todas as centenas de VPCs em todas as contas utilizando a CLI da AWS com autorizações de cross-account VPC association individuais.",
          "explanation": "Incorreto: Associar manualmente PHZs a centenas de VPCs em 80 contas é complexo, tem limites de escala e não resolve o encaminhamento de nomes on-premises (.corp.local) a partir da AWS."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "A arquitetura padrão recomendada pela AWS para DNS híbrido em escala enterprise consiste em implantar Route 53 Resolver Inbound e Outbound Endpoints em uma VPC central de Shared Services e compartilhar as Forwarding Rules com todas as contas da organização via AWS RAM.",
      "referenceUrl": "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q003",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS PrivateLink", "Elastic Load Balancing", "Amazon VPC"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma empresa de software SaaS desenvolveu uma API de análise financeira hospedada em sua própria VPC na AWS. Centenas de clientes corporativos que também possuem contas na AWS precisam consumir essa API de forma privada e segura. Vários clientes possuem blocos CIDR em suas VPCs que se sobrepõem (overlap) ao bloco CIDR da VPC do provedor SaaS. A empresa precisa fornecer conectividade unidirecional para que os clientes acessem o serviço sem expor a API à Internet e sem exigir que os clientes alterem seus blocos CIDR. Qual arquitetura atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Criar conexões de VPC Peering entre a VPC SaaS e a VPC de cada cliente, configurando NAT Gateway em cada VPC de cliente para tradução de endereços.",
          "explanation": "Incorreto: VPC Peering não permite o estabelecimento de conexões entre VPCs com blocos CIDR sobrepostos (overlapping CIDR blocks)."
        },
        {
          "id": "B",
          "text": "Configurar túneis de VPN IPsec com BGP dinâmico entre a VPC SaaS e a VPC de cada cliente, utilizando roteamento estático com Policy-Based Routing.",
          "explanation": "Incorreto: Gerenciar centenas de conexões VPN IPsec adiciona sobrecarga de gerenciamento desnecessária, limites de throughput (1.25 Gbps por túnel) e complexidade de chaves criptográficas."
        },
        {
          "id": "C",
          "text": "Configurar um Transit Gateway compartilhado com os clientes via AWS RAM e utilizar tabelas de rotas com NAT de entrada em instâncias EC2.",
          "explanation": "Incorreto: Transit Gateway não permite anexos de VPCs com blocos CIDR sobrepostos na mesma tabela de rotas sem NAT complexo e instâncias gerenciadas manualmente."
        },
        {
          "id": "D",
          "text": "Implantar um Network Load Balancer (NLB) interno na frente dos serviços de API na VPC SaaS e criar um VPC Endpoint Service (AWS PrivateLink). Permitir os IDs das contas AWS dos clientes e orientá-los a criar um Interface VPC Endpoint em suas respectivas VPCs.",
          "explanation": "Correto: O AWS PrivateLink com VPC Endpoint Service desacopla os espaços de endereçamento IP através de interfaces ENI locais na VPC do cliente conectadas ao NLB do provedor, funcionando perfeitamente mesmo com blocos CIDR sobrepostos e sem expor tráfego à Internet."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS PrivateLink (VPC Endpoint Service com NLB) é a solução oficial e recomendada pela AWS para publicar microsserviços entre diferentes contas e organizações. Como a comunicação ocorre por meio de mapeamento de endpoints privados locais, ele suporta de forma nativa e transparente sobreposição de blocos CIDR entre clientes e provedores.",
      "referenceUrl": "https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service-overview.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q004",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Organizations", "AWS IAM Identity Center", "AWS IAM"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma corporação com 500 contas no AWS Organizations precisa implementar controles estritos de segurança e governança de acesso. Os requisitos exigem: 1) Impedir preventivamente que administradores de contas membro criem volumes EBS não criptografados ou desativem o AWS CloudTrail, inclusive o usuário root das contas membro; 2) Fornecer acesso federado aos engenheiros de dados integrados com o Microsoft Entra ID corporativo, garantindo que o acesso a recursos específicos seja concedido dinamicamente com base no departamento do usuário, sem necessidade de manter dezenas de Permission Sets separados para cada equipe. Quais DUAS ações atenderão a esses requisitos? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Criar regras gerenciadas do AWS Config com remediação automática via AWS Systems Manager Automation em cada conta membro para criptografar volumes e reativar o CloudTrail.",
          "explanation": "Incorreto: O AWS Config é uma ferramenta detectiva que atua após o recurso ser criado, não impedindo a ação preventivamente."
        },
        {
          "id": "B",
          "text": "Criar e anexar Service Control Policies (SCPs) com cláusulas 'Deny' explícitas na raiz do AWS Organizations ou nas OUs aplicáveis, bloqueando as ações ec2:CreateVolume sem criptografia e cloudtrail:StopLogging / cloudtrail:DeleteTrail.",
          "explanation": "Correto: SCPs atuam como guardrails preventivos na camada de controle do AWS Organizations e aplicam-se a todos os usuários e roles das contas membro, incluindo o usuário root."
        },
        {
          "id": "C",
          "text": "Criar 50 Permission Sets individuais no IAM Identity Center, um para cada departamento, com políticas IAM que listam explicitamente os ARNs de recursos autorizados de cada equipe.",
          "explanation": "Incorreto: Criar Permission Sets estáticos para cada departamento gera alta complexidade de manutenção e viola o requisito de gerenciamento dinâmico."
        },
        {
          "id": "D",
          "text": "Configurar o IAM Identity Center com sincronização SCIM e habilitar atributos de sessão (Session Tags) repassando o atributo 'Department'. Criar um único Permission Set com política baseada em ABAC utilizando a condição StringEquals {'aws:ResourceTag/Department': '${aws:PrincipalTag/Department}'}.",
          "explanation": "Correto: O Attribute-Based Access Control (ABAC) com tags de sessão permite que uma única política conceda acesso dinâmico a recursos marcados com a mesma tag do departamento do usuário autenticado."
        },
        {
          "id": "E",
          "text": "Definir IAM Permissions Boundaries em cada conta membro para restringir as permissões máximas delegadas aos administradores locais.",
          "explanation": "Incorreto: Permissions Boundaries não afetam o usuário root das contas membro e exigem configuração descentralizada em cada conta."
        }
      ],
      "correctAnswers": ["B", "D"],
      "generalExplanation": "Para governança preventiva global multi-contas que afete inclusive o usuário root das contas membro, as Service Control Policies (SCPs) são a solução recomendada. Para gerenciamento dinâmico e escalável de acesso com IdP corporativo, o IAM Identity Center combinado com ABAC (Session Tags com aws:PrincipalTag) permite uma única política que escala para qualquer número de departamentos.",
      "referenceUrl": "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q005",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Resource Access Manager", "Amazon VPC", "AWS Organizations"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira internacional está implementando uma arquitetura de rede multi-contas na AWS. Para otimizar custos e simplificar o gerenciamento de endereçamento IP, a equipe de infraestrutura central deseja compartilhar subnets privadas e o AWS Transit Gateway criados na conta de rede central com mais de 60 contas de desenvolvimento e produção pertencentes à mesma organização no AWS Organizations. Os desenvolvedores nas contas membro devem ser capazes de lançar instâncias EC2 e clusters EKS diretamente nessas subnets compartilhadas, mas não podem ter permissão para modificar tabelas de rotas, gateways ou configurações da VPC. Qual solução atende a esses requisitos com a MENOR sobrecarga?",
      "options": [
        {
          "id": "A",
          "text": "Criar VPCs individuais em cada uma das 60 contas e estabelecer VPC Peering entre cada conta e a conta central com scripts CloudFormation.",
          "explanation": "Incorreto: VPC Peering requer criar e gerenciar 60 VPCs e 60 blocos CIDR separados, não atingindo o objetivo de subnets e VPC compartilhadas."
        },
        {
          "id": "B",
          "text": "Habilitar o compartilhamento de recursos com o AWS Organizations no AWS Resource Access Manager (RAM) na conta central de rede e compartilhar as subnets privadas com as OUs ou contas aplicáveis.",
          "explanation": "Correto: O VPC Sharing via AWS RAM permite que a conta proprietária da VPC compartilhe subnets com outras contas da organização. Os participantes podem criar recursos nessas subnets, mas não podem alterar a infraestrutura da VPC (rotas, ACLs, gateways)."
        },
        {
          "id": "C",
          "text": "Criar IAM Roles com permissões cross-account na conta central e orientar os desenvolvedores a assumir essas roles para lançar instâncias na VPC central.",
          "explanation": "Incorreto: Assumir roles cross-account faz com que os recursos pertençam à conta central, dificultando o isolamento de faturamento e governança das contas membro."
        },
        {
          "id": "D",
          "text": "Configurar conexões VPN privadas entre cada conta membro e a VPC central utilizando software appliance em EC2.",
          "explanation": "Incorreto: VPNs adicionam custos de tráfego, limites de throughput e complexidade de manutenção desnecessária dentro da mesma região."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "O VPC Sharing via AWS RAM permite desacoplar a governança da rede (gerenciada centralmente pela equipe de infraestrutura) da propriedade das aplicações (executadas nas contas membro). As contas participantes podem visualizar e instanciar recursos nas subnets compartilhadas sem capacidade de alterar a arquitetura da rede.",
      "referenceUrl": "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q006",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS CloudTrail", "Amazon S3", "AWS Organizations", "AWS KMS"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação de serviços bancários exige que todos os eventos de gerenciamento e dados da API da AWS em mais de 200 contas sejam registrados e retidos por 7 anos para fins de conformidade regulatória. A arquitetura deve garantir que: 1) O registro de logs seja ativado automaticamente para qualquer nova conta adicionada à organização; 2) Os arquivos de log sejam centralizados em um bucket S3 dedicado na conta Log Archive; 3) Os logs sejam imutáveis e protegidos contra exclusão ou modificação, inclusive por administradores com privilégios totais ou pelo usuário root; 4) A integridade dos logs seja validada criptograficamente. Qual arquitetura atende a TODOS esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Criar trilhas do CloudTrail individuais em cada conta membro usando CloudFormation StackSets e enviar os logs para um bucket S3 local em cada conta com versionamento habilitado.",
          "explanation": "Incorreto: Trilhas locais descentralizadas permitem que administradores da conta membro modifiquem configurações ou excluam logs locais."
        },
        {
          "id": "B",
          "text": "Habilitar o AWS CloudWatch Logs em todas as contas e configurar assinaturas do Kinesis Data Firehose para transmitir os logs para um cluster Amazon OpenSearch Service com retenção de 7 anos.",
          "explanation": "Incorreto: O OpenSearch não é otimizado para retenção fria de longo prazo de 7 anos com imutabilidade estrita e tem custo significativamente superior ao S3 com Object Lock."
        },
        {
          "id": "C",
          "text": "Criar uma trilha organizacional (Organization Trail) no AWS CloudTrail a partir da conta de gerenciamento com validação de integridade de arquivos ativada. Armazenar os logs em um bucket S3 na conta Log Archive protegido por S3 Object Lock no modo Compliance (retenção de 7 anos), criptografado com uma chave KMS gerenciada pelo cliente (CMK) com política restrita.",
          "explanation": "Correto: A Organization Trail aplica-se automaticamente a todas as contas membro atuais e futuras. A validação de integridade do CloudTrail detecta alterações, e o S3 Object Lock no modo Compliance impede que qualquer usuário (inclusive root da conta) exclua ou sobrescreva os logs durante o período de retenção."
        },
        {
          "id": "D",
          "text": "Configurar o AWS Security Hub para coletar logs de auditoria e exportá-los diariamente para o Amazon DynamoDB com políticas de exclusão por TTL.",
          "explanation": "Incorreto: O Security Hub coleta achados de segurança, não o histórico completo de chamadas de API do CloudTrail, e o DynamoDB com TTL apaga dados em vez de retê-los imutavelmente."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "A arquitetura recomendada para auditoria enterprise na AWS combina o AWS CloudTrail Organization Trail (ativado para todas as contas da organização) com armazenamento em bucket S3 centralizado na conta de Log Archive, protegido por S3 Object Lock em modo Compliance (WORM - Write Once, Read Many) e criptografia KMS CMK.",
      "referenceUrl": "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q007",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon Aurora", "Amazon Route 53", "AWS Route 53 Application Recovery Controller"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma empresa de serviços financeiros opera uma plataforma transacional crítica em us-east-1 usando Amazon EC2 e um banco de dados relacional Amazon Aurora MySQL. A empresa possui o requisito de implementar uma solução de recuperação de desastres (DR) para a região us-west-2 com RTO inferior a 1 minuto e RPO inferior a 1 segundo para a camada de banco de dados. A solução deve incluir verificação contínua e automatizada da prontidão da infraestrutura standby antes de acionar a alternância de DNS, evitando failovers para ambientes com capacidade insuficiente. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Implantar o Amazon Aurora Global Database com a região primária em us-east-1 e uma região secundária em us-west-2. Configurar o AWS Route 53 Application Recovery Controller (ARC) com Routing Controls e Readiness Checks contínuos para validar a prontidão dos recursos em us-west-2 e alternar o tráfego global de DNS de forma controlada em caso de desastre.",
          "explanation": "Correto: O Aurora Global Database oferece replicação física no storage com latência < 1s (RPO < 1s) e failover planejado/não planejado em menos de 1 minuto (RTO < 1 min). O Route 53 ARC realiza Readiness Checks para garantir que a região secundária possui capacidade e réplicas prontas antes de alternar os Routing Controls."
        },
        {
          "id": "B",
          "text": "Configurar réplicas de leitura assíncronas do Amazon RDS MySQL entre regiões e utilizar AWS Lambda disparado por alarmes do CloudWatch para promover a réplica a mestre primário.",
          "explanation": "Incorreto: Réplicas de leitura RDS tradicionais utilizam replicação lógica mais lenta e a promoção manual/scriptada do RDS exige reinicialização e reconfiguração de endpoints, ultrapassando o RTO de 1 minuto."
        },
        {
          "id": "C",
          "text": "Utilizar o AWS Backup para criar snapshots a cada 5 minutos do cluster Aurora e copiá-los para us-west-2, restaurando o cluster sob demanda com scripts do Terraform.",
          "explanation": "Incorreto: Snapshots a cada 5 minutos violam o requisito estrito de RPO < 1 segundo e a restauração de um snapshot leva de 15 a 30 minutos, violando o RTO < 1 minuto."
        },
        {
          "id": "D",
          "text": "Implantar uma política de roteamento de failover padrão no Route 53 associada a Health Checks HTTP convencionais apontando diretamente para as instâncias de aplicação.",
          "explanation": "Incorreto: Health checks HTTP padrão do Route 53 não avaliam a prontidão de recursos e réplicas de infraestrutura profunda (capacidade de instâncias, cotas de serviço e limites) como o Route 53 ARC."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "Para cumprir RPO < 1s e RTO < 1 min em banco de dados relacional multi-região, a arquitetura padrão ouro na AWS é o Amazon Aurora Global Database (replicação a nível de storage). O Route 53 Application Recovery Controller (ARC) complementa a solução com Readiness Checks contínuos (evitando failovers para regiões despreparadas) e Routing Controls acionáveis em milissegundos.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q008",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon DynamoDB", "AWS Global Accelerator"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma plataforma global de apostas esportivas e e-sports precisa registrar centenas de milhares de palpites simultâneos durante eventos esportivos ao vivo. Os usuários estão distribuídos na América do Norte, Europa e Ásia-Pacífico. A arquitetura exige latência de leitura e escrita local inferior a 10 milissegundos em todas as três regiões, com replicação totalmente ativa-ativa em múltiplas regiões (Multi-Region Active-Active) e reconciliação automática de conflitos. Qual tecnologia de banco de dados deve ser utilizada?",
      "options": [
        {
          "id": "A",
          "text": "Amazon RDS PostgreSQL com réplicas de leitura cross-region configuradas em us-east-1, eu-west-1 e ap-southeast-1.",
          "explanation": "Incorreto: Réplicas de leitura do RDS são somente leitura; todas as gravações precisam viajar até a região primária única, introduzindo alta latência de rede inter-regional e impedindo gravações locais ativas em todas as regiões."
        },
        {
          "id": "B",
          "text": "Amazon Aurora MySQL com Aurora Global Database e gravador primário em us-east-1.",
          "explanation": "Incorreto: O Aurora Global Database possui apenas uma região de gravação primária (Single-Writer). Requisições de gravação em regiões secundárias exigem write-forwarding para a região primária, aumentando a latência."
        },
        {
          "id": "C",
          "text": "Amazon DocumentDB com replicação de snapshots contínua entre regiões via AWS Backup.",
          "explanation": "Incorreto: Snapshots periódicos não oferecem escrita ativa-ativa multi-região e possuem latência de replicação de minutos ou horas."
        },
        {
          "id": "D",
          "text": "Amazon DynamoDB Global Tables com modo de capacidade On-Demand ativado em todas as três regiões.",
          "explanation": "Incorreto/Correto: O Amazon DynamoDB Global Tables é um banco de dados NoSQL totalmente gerenciado, ativo-ativo multi-região, que permite leituras e gravações locais em sub-milissegundos com replicação bidirecional automática e resolução de conflitos nativa ('last writer wins')."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O Amazon DynamoDB Global Tables é a solução gerenciada nativa da AWS para cargas de trabalho que exigem gravação e leitura ativa-ativa multi-região (Multi-Region Active-Active) de baixa latência (single-digit millisecond) com sincronização e resolução de conflitos totalmente gerenciadas.",
      "referenceUrl": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q009",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon CloudFront", "AWS Lambda", "Amazon S3"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma rede de televisão global transmite eventos esportivos ao vivo para mais de 10 milhões de espectadores simultâneos em todo o mundo. O conteúdo de vídeo é gerado em tempo real e distribuído via Amazon CloudFront a partir de um cluster de origem de transcodificação. A empresa precisa: 1) Validar tokens JWT assinados em cada requisição de segmento de vídeo com latência inferior a 1 milissegundo; 2) Proteger o cluster de origem contra picos de tráfego (thundering herd problem); 3) Bloquear requisições de países com restrições de direitos de transmissão. Qual arquitetura atende a esses requisitos com a MENOR latência e MENOR carga na origem?",
      "options": [
        {
          "id": "A",
          "text": "Executar a validação de JWT nos servidores de aplicação de origem na VPC e configurar regras de restrição geográfica no Application Load Balancer.",
          "explanation": "Incorreto: Validar tokens na origem obriga cada requisição a trafegar até os servidores de backend, sobrecarregando a infraestrutura e aumentando a latência para usuários distantes."
        },
        {
          "id": "B",
          "text": "Utilizar o Amazon CloudFront com CloudFront Functions no evento 'viewer-request' para validação ultrarrápida de tokens JWT, habilitar o CloudFront Origin Shield para consolidar requisições de cache e reduzir carga na origem, e configurar a Restrição Geográfica nativa do CloudFront (Geo Restriction).",
          "explanation": "Correto: CloudFront Functions executam em locais de borda em sub-milissegundos (ideal para validação leve de tokens e cabeçalhos). O Origin Shield atua como uma camada centralizada de cache que minimiza a carga na origem, e o Geo Restriction bloqueia acessos não autorizados diretamente na borda."
        },
        {
          "id": "C",
          "text": "Implantar funções Lambda@Edge no evento 'origin-response' e configurar um cluster Redis em EC2 para cache de sessões de vídeo.",
          "explanation": "Incorreto: O evento 'origin-response' executa após a requisição já ter atingido a origem, não impedindo a carga na origem. Lambda@Edge tem latência e custo superiores a CloudFront Functions para validação simples de cabeçalhos/tokens."
        },
        {
          "id": "D",
          "text": "Usar AWS WAF anexado ao CloudFront com regras customizadas de inspeção de corpo de requisição e configurar múltiplos buckets S3 replicados em 10 regiões.",
          "explanation": "Incorreto: AWS WAF não faz validação criptográfica nativa de assinaturas JWT em sub-milissegundos com a mesma eficiência de CloudFront Functions, e replicar vídeo ao vivo em 10 buckets S3 é ineficiente."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "Para distribuição de mídia em hiperescala, a combinação de CloudFront Functions (execução de código em sub-milissegundos na borda para validação de JWT/tokens e manipulação de cabeçalhos) + CloudFront Origin Shield (camada intermediária de cache para colapsar requisições e proteger a origem) + Geo Restriction é a arquitetura de referência da AWS.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q010",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon S3", "AWS KMS", "AWS Global Accelerator"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma corporação de biotecnologia executa pipelines de sequenciamento genômico distribuídos entre laboratórios nos Estados Unidos (us-east-1) e Europa (eu-west-1). Os sequenciadores geram arquivos binários pesados (50 GB a 200 GB por amostra) que devem ser carregados para o Amazon S3 com a menor latência possível através de um endpoint global único e resiliente. Além disso, todos os dados devem ser replicados bidirecionalmente entre as duas regiões com criptografia obrigatória usando chaves KMS gerenciadas pelo cliente (CMK), garantindo SLA de replicação de 15 minutos (S3 RTC). Quais DUAS soluções devem ser combinadas para atender a esses requisitos? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Criar um Amazon S3 Multi-Region Access Point (MRAP) para fornecer um endpoint DNS global único que roteia uploads automaticamente pela rede global privada da AWS para o bucket mais próximo e com menor latência.",
          "explanation": "Correto: O S3 Multi-Region Access Point (MRAP) fornece um hostname global único sustentado pelo AWS Global Accelerator que roteia o tráfego de clientes automaticamente para o bucket S3 de menor latência com failover automático."
        },
        {
          "id": "B",
          "text": "Configurar servidores SFTP em instâncias EC2 com AWS Transfer Family em cada laboratório para gerenciar o upload de arquivos via Internet pública.",
          "explanation": "Incorreto: AWS Transfer Family sobre internet pública não oferece o mesmo desempenho e automação de roteamento global otimizado que o S3 MRAP."
        },
        {
          "id": "C",
          "text": "Utilizar chaves KMS Single-Region distintas em cada região e configurar funções do AWS Lambda para descriptografar e re-criptografar cada objeto durante o processo de cópia.",
          "explanation": "Incorreto: Re-criptografar objetos com Lambda gera alto custo computacional, latência e complexidade de código desnecessária."
        },
        {
          "id": "D",
          "text": "Configurar o S3 Cross-Region Replication (CRR) usando criptografia padrão S3 SSE-S3 (chaves gerenciadas pela AWS) com S3 Lifecycle policies de 1 hora.",
          "explanation": "Incorreto: A especificação exige chaves gerenciadas pelo cliente (KMS CMK) e conformidade com SLA de replicação de 15 minutos."
        },
        {
          "id": "E",
          "text": "Configurar o S3 Cross-Region Replication (CRR) bidirecional entre os buckets de us-east-1 e eu-west-1 com S3 Replication Time Control (S3 RTC) ativado, utilizando chaves KMS Multi-Region (Multi-Region Keys) para criptografia.",
          "explanation": "Correto: O S3 Replication Time Control (S3 RTC) garante contratualmente a replicação de 99,99% dos objetos em até 15 minutos. O uso de KMS Multi-Region Keys permite que os dados replicados compartilhem o mesmo material de chave criptográfica sem necessidade de re-criptografia complexa."
        }
      ],
      "correctAnswers": ["A", "E"],
      "generalExplanation": "Para uploads globais acelerados de grandes volumes de dados em S3 com failover automático e endpoint unificado, o S3 Multi-Region Access Points (MRAP) é a tecnologia nativa da AWS. Combinado com S3 Cross-Region Replication (CRR) com S3 Replication Time Control (S3 RTC) e chaves KMS Multi-Region, garante-se criptografia em repouso e replicação em até 15 minutos.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q011",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["AWS App Mesh", "AWS Certificate Manager", "Amazon ECS", "Amazon EKS"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira está migrando seus serviços de pagamentos para uma arquitetura de microsserviços em contêineres distribuída em dezenas de clusters Amazon EKS e Amazon ECS na AWS. A equipe de conformidade de segurança impõe um requisito estrito de Zero-Trust: todo o tráfego de comunicação serviço a serviço (Leste-Oeste) entre contêineres deve ser autenticado e criptografado com mutual TLS (mTLS). A renovação e rotação de certificados X.509 devem ser totalmente automatizadas, sem exigir alterações no código das aplicações ou gerenciamento manual de chaves privadas pelos desenvolvedores. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Instalar agentes customizados em cada contêiner que executam scripts periódicos do OpenSSL para gerar certificados autoassinados em volumes locais.",
          "explanation": "Incorreto: Scripts manuais e certificados autoassinados geram alto risco de segurança, não fornecem cadeia de confiança centralizada e exigem manutenção complexa."
        },
        {
          "id": "B",
          "text": "Configurar Application Load Balancers individuais na frente de cada microsserviço com certificados públicos do AWS Certificate Manager (ACM).",
          "explanation": "Incorreto: Implantar centenas de ALBs individuais para cada microsserviço interno acarreta custos astronômicos, latência de múltiplos saltos e não resolve mTLS serviço a serviço de forma nativa e transparente."
        },
        {
          "id": "C",
          "text": "Implantar uma Service Mesh utilizando o AWS App Mesh integrado ao AWS Certificate Manager Private Certificate Authority (ACM Private CA) e proxies Envoy sidecar. Configurar as políticas de TLS do App Mesh para impor mTLS estrito entre os Virtual Nodes.",
          "explanation": "Correto: O AWS App Mesh com proxies sidecar Envoy gerencia automaticamente a emissão, distribuição e rotação contínua de certificados TLS emitidos pelo ACM Private CA, aplicando mTLS transparente e de alto desempenho sem alteração de código na aplicação."
        },
        {
          "id": "D",
          "text": "Configurar regras de Network ACLs e Security Groups com criptografia IPsec em nível de interface de rede elástica em cada nó do cluster.",
          "explanation": "Incorreto: Security Groups e NACLs não realizam autenticação criptográfica de camada de aplicação mTLS nem gerenciam certificados digitais X.509."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "Para impor segurança Zero-Trust e criptografia mTLS entre microsserviços sem alterar código de aplicação, a solução enterprise de referência da AWS é a Service Mesh (AWS App Mesh com proxies Envoy) integrada ao AWS Private CA, automatizando a rotação de certificados criptográficos.",
      "referenceUrl": "https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual-node-tls.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q012",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon FSx", "Amazon S3", "Amazon EC2"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma empresa de energia executa modelos complexos de simulação sísmica e de reservatórios de petróleo em um cluster de High Performance Computing (HPC) composto por centenas de instâncias EC2 otimizadas para computação. A carga de trabalho exige um sistema de arquivos compartilhado compatível com POSIX que ofereça centenas de gigabytes por segundo de throughput, milhões de IOPS e latência consistente inferior a 1 milissegundo. Os dados brutos de entrada e os resultados finais residem permanentemente em buckets Amazon S3. A solução deve permitir sincronização transparente com o S3 e minimizar custos operacionais quando as simulações não estiverem em execução. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Implantar um sistema de arquivos Amazon EFS no modo General Purpose com Elastic Throughput anexado a todas as instâncias EC2.",
          "explanation": "Incorreto: O Amazon EFS é projetado para compartilhamento geral de arquivos e não atinge centenas de GB/s de throughput com latência sub-milissegundo para HPC sísmico extremo."
        },
        {
          "id": "B",
          "text": "Criar um sistema de arquivos Amazon FSx for Lustre conectado diretamente ao bucket Amazon S3 como repositório de dados. Configurar a importação e exportação automática de dados de/para o S3 e utilizar armazenamento scratch ou persistente baseado em SSD com compactação de dados ativada.",
          "explanation": "Correto: O Amazon FSx for Lustre é desenvolvido especificamente para cargas de trabalho de HPC, processamento de mídia e ML. Ele oferece centenas de GB/s de throughput, milhões de IOPS e latência sub-milissegundo, integrando-se nativamente com buckets S3 como Data Repositories."
        },
        {
          "id": "C",
          "text": "Montar volumes Amazon EBS io2 Block Express em cada instância EC2 e configurar scripts rsync contínuos para manter os dados sincronizados com o S3.",
          "explanation": "Incorreto: Volumes EBS io2 não são sistemas de arquivos compartilhados em rede para centenas de instâncias concorrentes com sincronização nativa S3."
        },
        {
          "id": "D",
          "text": "Utilizar o AWS Storage Gateway File Gateway implantado em instâncias EC2 para cache local de arquivos S3.",
          "explanation": "Incorreto: O File Gateway é projetado para ambientes híbridos de escritório e não fornece o throughput massivo e latência ultra-baixa exigidos por clusters de HPC."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "O Amazon FSx for Lustre é o serviço de sistema de arquivos de alto desempenho da AWS ideal para HPC e processamento intensivo de dados. Sua capacidade de conexão nativa e bidirecional com buckets S3 permite carregar dados sob demanda e persistir resultados com facilidade e máxima eficiência de custo.",
      "referenceUrl": "https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q013",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["AWS Global Accelerator", "Elastic Load Balancing", "Amazon EC2"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira global oferece uma API de liquidação de transações em tempo real para bancos parceiros. A aplicação está implantada em Application Load Balancers nas regiões us-east-1 e eu-west-1. Devido a firewalls corporativos restritivos nos datacenters dos parceiros, o tráfego deve ser enviado obrigatoriamente para um conjunto fixo de endereços IP públicos estáticos e roteado pela rede global privada da AWS para garantir menor jitter e menor perda de pacotes. Em caso de falha total de uma região, o tráfego deve ser redirecionado para a região saudável em menos de 30 segundos, sem depender de expiração de cache DNS (TTL) dos clientes. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o Amazon Route 53 com políticas de roteamento baseadas em latência associadas a Health Checks e diminuir o TTL dos registros para 5 segundos.",
          "explanation": "Incorreto: O Route 53 não fornece IPs estáticos fixos e depende do comportamento de cache DNS dos clientes e ISPs intermediários (que frequentemente ignoram TTLs baixos)."
        },
        {
          "id": "B",
          "text": "Implantar o Amazon CloudFront na frente dos ALBs e associar uma distribuição com IPs elásticos estáticos dedicados.",
          "explanation": "Incorreto: O CloudFront não fornece endereços IP anycast estáticos dedicados fixos para configuração de firewall de clientes (ele usa grandes faixas dinâmicas de IPs)."
        },
        {
          "id": "C",
          "text": "Configurar túneis de VPN IPsec dedicados com Elastic IPs em instâncias EC2 em cada região e usar BGP para alternância de rotas.",
          "explanation": "Incorreto: VPNs IPsec exigem gerenciamento complexo de chaves e túneis com centenas de bancos parceiros e não oferecem a simplicidade de uma API pública protegida."
        },
        {
          "id": "D",
          "text": "Criar um acelerador no AWS Global Accelerator fornecendo dois endereços IP anycast estáticos globais fixos. Adicionar os Application Load Balancers de us-east-1 e eu-west-1 como grupos de endpoints (Endpoint Groups) com verificações de integridade contínuas.",
          "explanation": "Correto: O AWS Global Accelerator fornece 2 IPs anycast estáticos globais fixos que servem como ponto de entrada para clientes com firewalls rígidos. Ele ingere o tráfego na borda mais próxima e utiliza a rede de fibra privada da AWS, realizando failover instantâneo entre regiões em segundos sem depender de propagação de DNS."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS Global Accelerator é a solução ideal quando se exige IPs públicos estáticos fixos (Anycast), redução de latência/jitter via backbone privado da AWS e failover quase instantâneo entre regiões independentemente de caches DNS de clientes.",
      "referenceUrl": "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q014",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon SQS", "AWS Lambda"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Um sistema de processamento de ordens de compra em um marketplace de alta escala precisa processar eventos de compra assíncronos. A arquitetura exige: 1) Garantir a ordem estrita de processamento das mensagens para cada cliente individual (CustomerID); 2) Processar requisições de diferentes clientes em paralelo com alta taxa de transferência (throughput); 3) Evitar que mensagens corrompidas ou que gerem falhas repetidas travem a fila de processamento indefinidamente. Qual arquitetura atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar uma fila Amazon SQS FIFO com MessageGroupId configurado como CustomerID e MessageDeduplicationId único. Configurar uma Dead-Letter Queue (DLQ) do tipo FIFO com maxReceiveCount = 3 associada à fila principal.",
          "explanation": "Correto: Filas SQS FIFO garantem ordenação estrita dentro do mesmo MessageGroupId (CustomerID), permitindo paralelismo massivo entre diferentes grupos de mensagens. A DLQ FIFO com maxReceiveCount isola mensagens venenosas após 3 tentativas de falha sem bloquear as mensagens subsequentes."
        },
        {
          "id": "B",
          "text": "Utilizar uma fila Amazon SQS Standard com ordenação gerenciada por carimbo de data/hora (timestamp) na aplicação consumidora.",
          "explanation": "Incorreto: Filas SQS Standard não garantem entrega First-In, First-Out (FIFO) nem entrega única (podem entregar mensagens fora de ordem e duplicadas)."
        },
        {
          "id": "C",
          "text": "Configurar um tópico Amazon SNS Standard com filtro de mensagens (Message Filtering) para cada CustomerID direcionado a instâncias EC2.",
          "explanation": "Incorreto: Tópicos SNS Standard não oferecem retenção durável em fila com desacoplamento nem garantem processamento sequencial ordenado como filas SQS FIFO."
        },
        {
          "id": "D",
          "text": "Utilizar uma tabela Amazon DynamoDB como fila de mensagens com Streams habilitados e uma função AWS Lambda como consumidora.",
          "explanation": "Incorreto: Usar banco de dados como fila gera anti-padrão de concorrência, polling ineficiente e custo superior a uma solução nativa de mensageria gerenciada como o SQS FIFO."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "O Amazon SQS FIFO garante ordem exata de entrega e processamento 'exactly-once' agrupado por 'MessageGroupId'. A associação com uma Dead Letter Queue (DLQ) FIFO evita que mensagens malformatadas travem o fluxo do grupo, movendo-as automaticamente para análise após o número máximo de tentativas.",
      "referenceUrl": "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q015",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Systems Manager", "Amazon EC2"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma organização de saúde possui uma frota de 1.500 instâncias EC2 heterogêneas (Amazon Linux 2, Ubuntu e Windows Server) distribuídas em 40 contas AWS. A auditoria de segurança determinou que todos os servidores devem receber atualizações de segurança críticas automaticamente a cada 7 dias dentro de janelas de manutenção aprovadas. Além disso, por exigência de conformidade HIPAA, os administradores não podem utilizar chaves SSH, servidores bastiões ou manter as portas 22/3389 abertas nas Security Groups para tarefas de suporte. Qual solução atende a esses requisitos com a MAIOR segurança e MENOR sobrecarga?",
      "options": [
        {
          "id": "A",
          "text": "Configurar servidores bastião redundantes em cada VPC e usar scripts Ansible via cron para aplicar atualizações e gerenciar o acesso de administradores via SSH.",
          "explanation": "Incorreto: Bastiões mantêm portas de entrada abertas (22/3389), exigem gerenciamento de chaves SSH e vulnerabilidades em cada VPC."
        },
        {
          "id": "B",
          "text": "Desenvolver funções do AWS Lambda acionadas pelo Amazon EventBridge que conectam nas instâncias via SSH utilizando chaves armazenadas no AWS Secrets Manager.",
          "explanation": "Incorreto: Conexões SSH diretas exigem portas abertas e conectividade de rede direta, não eliminando a sobrecarga de gerenciamento."
        },
        {
          "id": "C",
          "text": "Instalar e configurar o AWS Systems Manager Agent (SSM Agent) em todas as instâncias com a IAM Role apropriada. Utilizar o SSM Patch Manager com Patch Baselines customizadas e Maintenance Windows para aplicar patches automaticamente. Utilizar o SSM Session Manager para acesso administrativo seguro sem necessidade de portas de entrada abertas ou chaves SSH.",
          "explanation": "Correto: O SSM Patch Manager automatiza a aplicação de patches com regras de aprovação e janelas de manutenção em frotas heterogêneas. O SSM Session Manager fornece acesso seguro via console/CLI através de HTTPS de saída (porta 443), sem portas de entrada abertas ou bastiões."
        },
        {
          "id": "D",
          "text": "Substituir todas as instâncias EC2 semanalmente gerando novas AMIs com o EC2 Image Builder e implantando novos Auto Scaling groups com Blue/Green deployment.",
          "explanation": "Incorreto: Recriar instâncias de bancos de dados ou servidores com estado semanalmente pode gerar indisponibilidade e não resolve o requisito de acesso administrativo sem portas abertas."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "O AWS Systems Manager (SSM) é a ferramenta recomendada pela AWS para operações em escala. O Patch Manager automatiza o ciclo de vida de correções de segurança em frotas multi-OS, enquanto o Session Manager elimina totalmente a necessidade de bastiões, chaves SSH e portas abertas em Security Groups.",
      "referenceUrl": "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q016",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Security Hub", "Amazon GuardDuty", "AWS Systems Manager", "Amazon EventBridge"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira precisa implementar uma solução centralizada de monitoramento de ameaças e resposta automatizada a incidentes para todas as suas 120 contas no AWS Organizations. A solução deve: 1) Detectar comportamentos anômalos em CloudTrail, VPC Flow Logs e DNS Logs em tempo real; 2) Centralizar todos os alertas de segurança em uma conta de segurança designada; 3) Quando uma instância EC2 for detectada como comprometida (comunicação com C2/botnet conhecida), isolar a instância imediatamente alterando sua Security Group para uma regra de quarentena sem intervenção humana. Qual arquitetura atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Configurar o Amazon Inspector em todas as contas e enviar relatórios semanais por e-mail via Amazon SNS para a equipe de segurança.",
          "explanation": "Incorreto: O Amazon Inspector faz análise de vulnerabilidades em pacotes de software, não detecção de ameaças de tráfego de rede C2 em tempo real, e relatórios semanais por e-mail não atendem à remediação automatizada instantânea."
        },
        {
          "id": "B",
          "text": "Habilitar o Amazon GuardDuty e o AWS Security Hub em toda a organização através da conta Security Delegated Administrator. Criar uma regra no Amazon EventBridge na conta de segurança que capture achados críticos do GuardDuty ('UnauthorizedAccess:EC2/MaliciousIPCaller.Custom') e acione um Runbook do AWS Systems Manager Automation para substituir a Security Group da instância por uma Security Group de quarentena sem tráfego de entrada ou saída.",
          "explanation": "Correto: O GuardDuty utiliza ML para detectar ameaças de rede e anomalias de API em tempo real. O Security Hub centraliza os achados em nível organizacional e o EventBridge aciona automações nativas do Systems Manager para isolar instâncias comprometidas em segundos."
        },
        {
          "id": "C",
          "text": "Escrever scripts em Python em cada conta membro que consultam o AWS CloudTrail a cada 10 minutos e executam comandos locais para desligar instâncias.",
          "explanation": "Incorreto: Scripts locais baseados em polling do CloudTrail são lentos, propensos a falhas e não utilizam inteligência de ameaças avançada como o GuardDuty."
        },
        {
          "id": "D",
          "text": "Utilizar o AWS WAF em todas as contas e configurar o AWS Firewall Manager para bloquear IPs maliciosos nas VPCs.",
          "explanation": "Incorreto: O AWS WAF atua na camada 7 de ALBs/CloudFront e não analisa tráfego de rede geral de instâncias EC2 ou chamadas de API do CloudTrail."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "A arquitetura padrão da AWS para SOC automatizado consiste em delegar a administração do Amazon GuardDuty e AWS Security Hub para a conta de segurança corporativa. Eventos de achados de alta severidade são capturados em tempo real pelo Amazon EventBridge, acionando runbooks do AWS Systems Manager Automation para isolar recursos comprometidos de forma instantânea.",
      "referenceUrl": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q017",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Lake Formation", "Amazon S3", "Amazon Athena", "AWS Glue"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação de telecomunicações mantém um Data Lake de 500 TB no Amazon S3 centralizado na conta de Analytics. O Data Lake contém tabelas particionadas com registros detalhados de chamadas (CDR) e dados pessoais de clientes (PII). Analistas de 20 contas AWS diferentes precisam consultar esses dados utilizando o Amazon Athena e o Amazon Redshift Spectrum. A equipe de governança exige: 1) Conceder acesso restrito a nível de colunas e linhas (ex: mascarar CPF e ocultar colunas financeiras para determinados departamentos); 2) Evitar a criação e manutenção de dezenas de políticas de bucket S3 e IAM complexas; 3) Permitir compartilhamento federado de dados sem duplicar os arquivos no S3. Qual solução atende a esses requisitos com a MENOR complexidade?",
      "options": [
        {
          "id": "A",
          "text": "Criar cópias dos dados filtrados em 20 buckets S3 diferentes, um para cada conta de departamento, sincronizados via S3 Replication diário.",
          "explanation": "Incorreto: Duplicar 500 TB em 20 buckets gera custos astronômicos de armazenamento, redundância desnecessária e sérios riscos de inconsistência de dados."
        },
        {
          "id": "B",
          "text": "Utilizar exibições (Views) customizadas no Amazon Athena em cada conta com funções de criptografia gerenciadas por IAM Roles locais.",
          "explanation": "Incorreto: Views locais no Athena não impedem o acesso direto aos arquivos subjacentes no S3 e exigem permissões amplas nos buckets de dados brutos."
        },
        {
          "id": "C",
          "text": "Configurar S3 Access Points com políticas de controle de acesso anexadas a cada grupo de usuários em cada conta membro.",
          "explanation": "Incorreto: S3 Access Points controlam acesso no nível do bucket/prefixo, não fornecendo controle granular nativo de colunas, linhas e células de tabelas estruturadas."
        },
        {
          "id": "D",
          "text": "Registrar o bucket S3 e o catálogo de dados do AWS Glue no AWS Lake Formation na conta central. Configurar permissões granulares de acesso no Lake Formation definindo filtros de dados por coluna, linha e célula. Conceder permissões cross-account (Lake Formation Permissions) para as contas dos departamentos através do AWS Resource Access Manager (RAM).",
          "explanation": "Correto: O AWS Lake Formation simplifica a governança de Data Lakes, oferecendo controle de acesso fino (banco, tabela, coluna, linha e célula) de forma centralizada e sem replicação de dados, com suporte a compartilhamento cross-account nativo via AWS RAM."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS Lake Formation é o serviço dedicado da AWS para governança e segurança de Data Lakes. Ele permite definir permissões granulares de acesso no nível de coluna e linha diretamente nas tabelas do Glue Data Catalog, delegando acesso cross-account sem necessidade de duplicar dados ou manter políticas de S3 excessivamente complexas.",
      "referenceUrl": "https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q018",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Organizations", "AWS Cost Explorer", "Amazon EC2", "AWS Fargate", "AWS Lambda"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma empresa de tecnologia com faturamento consolidado no AWS Organizations gasta cerca de US$ 600.000 mensais em recursos de computação. A infraestrutura é altamente dinâmica: consiste em instâncias EC2 de diversas famílias (C6i, M6g com Graviton, R6i) em 4 regiões diferentes, além de centenas de microsserviços em execução no AWS Fargate e milhares de funções AWS Lambda. A equipe de FinOps precisa adquirir um compromisso de desconto para reduzir custos em até 60% com as seguintes restrições: 1) O desconto deve ser aplicado automaticamente a EC2, Fargate e Lambda; 2) O compromisso deve permitir migrar livremente entre famílias de instâncias, sistemas operacionais, regiões e arquiteturas (x86 para ARM Graviton) sem perder o benefício; 3) O benefício deve ser compartilhado entre todas as contas da organização. Qual opção de compra atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Adquirir Compute Savings Plans com compromisso de 3 anos na conta de gerenciamento (Management Account) com compartilhamento de descontos habilitado nas preferências de faturamento do AWS Organizations.",
          "explanation": "Correto: O Compute Savings Plans oferece a máxima flexibilidade, aplicando descontos automaticamente ao uso de Amazon EC2 (independente de família, SO, região ou tenancy), AWS Fargate e AWS Lambda, sendo compartilhado automaticamente com todas as contas sob o mesmo faturamento consolidado."
        },
        {
          "id": "B",
          "text": "Adquirir EC2 Instance Savings Plans específicos para cada família de instâncias em cada uma das 4 regiões.",
          "explanation": "Incorreto: O EC2 Instance Savings Plans é restrito a uma família específica em uma região fixa e não cobre AWS Fargate ou AWS Lambda."
        },
        {
          "id": "C",
          "text": "Comprar Instâncias Reservadas Padrão (Standard Reserved Instances) de 3 anos em cada conta membro individual.",
          "explanation": "Incorreto: Standard RIs são rígidas (não permitem troca de família de instância, SO ou região) e não cobrem Fargate ou Lambda."
        },
        {
          "id": "D",
          "text": "Migrar todas as cargas de trabalho para instâncias Spot do Amazon EC2 com políticas de rescisão de 2 minutos.",
          "explanation": "Incorreto: Instâncias Spot podem ser interrompidas com aviso prévio de 2 minutos e não são adequadas para cargas de trabalho críticas ou com compromisso previsível de uso base."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "Para ambientes corporativos heterogêneos e em constante evolução que combinam EC2 (múltiplas famílias/regiões), Fargate e Lambda, o Compute Savings Plans é o modelo de precificação ideal, fornecendo a maior flexibilidade de adaptação arquitetural com descontos substanciais compartilhados em toda a organização.",
      "referenceUrl": "https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q019",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["Amazon RDS", "AWS Lambda", "Amazon RDS Proxy"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma plataforma de comércio eletrônico executa sua camada de microsserviços em funções AWS Lambda acionadas por eventos do Amazon API Gateway. O banco de dados relacional backend é um cluster Amazon RDS PostgreSQL Multi-AZ. Durante eventos promocionais sazonais (Flash Sales), o tráfego aumenta repentinamente para dezenas de milhares de invocações simultâneas de Lambda, resultando em erros frequentes de 'Too Many Connections' e degradação severa do banco de dados, devido ao esgotamento de memória por conexões simultâneas abertas pelas funções efêmeras. Qual solução resolve esse problema de forma MAIS eficiente e com menor sobrecarga operacional?",
      "options": [
        {
          "id": "A",
          "text": "Aumentar o tamanho da instância do RDS PostgreSQL para a maior família disponível (ex: db.m6i.32xlarge) para suportar mais conexões abertas.",
          "explanation": "Incorreto: Superdimensionar a instância do RDS gera custos exorbitantes contínuos e não resolve a raiz do problema de conexões efêmeras massivas abertas por funções serverless."
        },
        {
          "id": "B",
          "text": "Configurar filas Amazon SQS com concorrência máxima de 10 funções Lambda para limitar o número de conexões simultâneas ao banco de dados.",
          "explanation": "Incorreto: Limitar a concorrência do Lambda introduz latência severa no processamento de requisições de checkout dos clientes em tempo real durante a venda promocional."
        },
        {
          "id": "C",
          "text": "Implantar o Amazon RDS Proxy entre as funções AWS Lambda e o cluster Amazon RDS PostgreSQL, configurando o pool de conexões gerenciado e integrando a autenticação de segredos com o AWS Secrets Manager.",
          "explanation": "Correto: O Amazon RDS Proxy é um proxy de banco de dados totalmente gerenciado que mantém pools de conexões estabelecidas com o RDS, permitindo que milhares de instâncias do Lambda compartilhem e reutilizem conexões eficientemente, evitando o esgotamento de memória e conexões do banco."
        },
        {
          "id": "D",
          "text": "Implantar um cluster de instâncias EC2 executando PgBouncer em Auto Scaling com Network Load Balancer.",
          "explanation": "Incorreto: Manter e escalar clusters de PgBouncer em EC2 adiciona alta sobrecarga de gerenciamento de infraestrutura, patches e alta disponibilidade em comparação com o serviço gerenciado RDS Proxy."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "O Amazon RDS Proxy foi projetado especificamente para gerenciar pools de conexões entre aplicações com alta concorrência e arquiteturas serverless (AWS Lambda) e bancos de dados relacionais (RDS PostgreSQL/MySQL), reduzindo o uso de CPU e memória do banco e prevenindo falhas de esgotamento de conexões.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q020",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["Amazon Macie", "AWS IAM Access Analyzer", "Amazon S3"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma corporação de saúde e seguros precisa aprimorar sua postura de conformidade em mais de 100 contas AWS. A auditoria identificou duas necessidades urgentes: 1) Identificar, classificar e auditar continuamente dados confidenciais e dados de saúde de pacientes (PII / PHI) armazenados em milhares de buckets Amazon S3 distribuídos por toda a organização; 2) Identificar e remediar permissões excessivas e políticas IAM em desuso concedidas a roles e usuários em todas as contas, aplicando o princípio do menor privilégio com base no histórico real de chamadas de API. Quais DUAS ferramentas gerenciadas da AWS devem ser implementadas? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Habilitar o Amazon Macie em nível de organização a partir de uma conta Security Delegated Administrator para descoberta e classificação automatizada de PII e dados confidenciais em buckets S3.",
          "explanation": "Correto: O Amazon Macie utiliza machine learning e correspondência de padrões para descobrir, classificar e proteger dados confidenciais (PII, dados de saúde, credenciais) em grande escala no Amazon S3 em toda a organização."
        },
        {
          "id": "B",
          "text": "Executar o Amazon Inspector para auditar os arquivos de texto e objetos armazenados no Amazon S3.",
          "explanation": "Incorreto: O Amazon Inspector faz varredura de vulnerabilidades em pacotes de SO de instâncias EC2, imagens ECR e funções Lambda, não varredura de dados sensíveis em S3."
        },
        {
          "id": "C",
          "text": "Utilizar o IAM Access Analyzer para identificar recursos compartilhados externamente e gerar políticas IAM de menor privilégio baseadas nas atividades registradas no AWS CloudTrail.",
          "explanation": "Correto: O IAM Access Analyzer analisa permissões e acessos a recursos e possui o recurso de geração de políticas de menor privilégio baseado no histórico de chamadas de API registradas pelo CloudTrail."
        },
        {
          "id": "D",
          "text": "Configurar o AWS Trusted Advisor em cada conta membro para emitir relatórios semanais de IAM.",
          "explanation": "Incorreto: O Trusted Advisor oferece verificações de alto nível, mas não gera políticas refinadas de menor privilégio com base no histórico de chamadas de API."
        },
        {
          "id": "E",
          "text": "Implantar o AWS Glue DataBrew para ler todos os buckets S3 e mascarar os dados em novos arquivos CSV.",
          "explanation": "Incorreto: O DataBrew é uma ferramenta visual de preparação de dados para analytics, não um serviço contínuo de auditoria e segurança de conformidade em nível de organização."
        }
      ],
      "correctAnswers": ["A", "C"],
      "generalExplanation": "O Amazon Macie é o serviço nativo especializado em descobrir e classificar dados confidenciais (PII/PHI) no Amazon S3 em escala organizacional. O IAM Access Analyzer complementa a postura de segurança identificando acessos externos indevidos e gerando políticas estritas de menor privilégio a partir das atividades reais no CloudTrail.",
      "referenceUrl": "https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q021",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Application Migration Service", "Amazon EC2", "AWS Direct Connect"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma grande rede de varejo precisa migrar 450 servidores virtuais VMware vSphere e servidores físicos (Windows Server e Linux) de um datacenter legado para a AWS. A empresa possui conectividade via AWS Direct Connect de 10 Gbps. Os requisitos do projeto são: 1) A migração deve ocorrer com tempo de inatividade (cutover) inferior a 10 minutos por aplicação; 2) A replicação de dados deve ser contínua em nível de bloco, operando em segundo plano sem impactar a produção local; 3) O custo dos recursos de replicação durante o período de sincronização deve ser minimizado; 4) A solução deve permitir testes de inicialização não disruptivos na AWS antes da virada definitiva. Qual serviço atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o AWS Backup para criar backups locais e restaurá-los como AMIs na AWS.",
          "explanation": "Incorreto: Restaurar backups periódicos gera alto tempo de inatividade no momento do cutover (horas) e não suporta replicação contínua em nível de bloco."
        },
        {
          "id": "B",
          "text": "Exportar os discos virtuais em formato VMDK/OVA e utilizar o VM Import/Export via AWS CLI.",
          "explanation": "Incorreto: O VM Import/Export é manual, lento, não suporta sincronização contínua de deltas de dados e exige longo período de parada dos servidores."
        },
        {
          "id": "C",
          "text": "Instalar o AWS DataSync em cada servidor para copiar arquivos do sistema operacional para o Amazon S3 e lançar instâncias via CloudFormation.",
          "explanation": "Incorreto: O AWS DataSync migra dados de arquivos e objetos, não sistemas operacionais completos em execução com replicação de blocos de boot para instâncias EC2."
        },
        {
          "id": "D",
          "text": "Instalar o AWS Application Migration Service (AWS MGN) Replication Agent em todos os servidores de origem. Replicar os dados continuamente em nível de bloco para uma Staging Area de baixo custo na AWS, executar testes de inicialização em modo de teste e realizar o cutover definitivo em poucos minutos.",
          "explanation": "Correto: O AWS MGN é a ferramenta primária e recomendada pela AWS para migrações lift-and-shift (Rehost). Ele realiza replicação contínua em nível de bloco com impacto mínimo no servidor de origem, utiliza instâncias de baixo custo na staging area e permite cutovers com downtime mínimo (minutos)."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS Application Migration Service (AWS MGN) é o serviço padrão para migrações do tipo Rehost (Lift-and-Shift) para a AWS. Ele simplifica e automatiza a migração de servidores físicos, virtuais ou de outras nuvens através de replicação contínua em nível de bloco para uma staging area econômica, viabilizando cutovers rápidos com downtime mínimo.",
      "referenceUrl": "https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q022",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Database Migration Service", "AWS Schema Conversion Tool", "Amazon Aurora"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação de logística opera um banco de dados relacional Oracle Enterprise Edition de 12 TB on-premises que suporta seu sistema de rastreamento de entregas 24/7. A empresa decidiu modernizar o banco de dados migrando-o para o Amazon Aurora PostgreSQL (migração heterogênea) para eliminar custos recorrentes de licenciamento de software. A migração deve cumprir os seguintes critérios: 1) Converter automaticamente schemas, tabelas, índices e stored procedures; 2) Manter o banco de dados de origem totalmente operacional durante a migração com sincronização contínua de alterações (CDC); 3) Realizar o cutover final com tempo de inatividade inferior a 5 minutos. Qual estratégia atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o Oracle Data Pump para exportar os dados e importá-los diretamente no Aurora PostgreSQL utilizando o utilitário pg_restore.",
          "explanation": "Incorreto: O Oracle Data Pump gera dumps proprietários da Oracle que não são compatíveis diretamente com o motor PostgreSQL."
        },
        {
          "id": "B",
          "text": "Utilizar o AWS Schema Conversion Tool (AWS SCT) para analisar e converter o schema, tabelas e código PL/SQL do Oracle para PostgreSQL. Em seguida, utilizar o AWS Database Migration Service (AWS DMS) com uma tarefa de carga inicial (Full Load) combinada com replicação contínua (Change Data Capture - CDC) para sincronizar as alterações até o momento do cutover final.",
          "explanation": "Correto: A combinação de AWS SCT (para conversão de schemas heterogêneos Oracle -> PostgreSQL) com o AWS DMS (carga full + CDC contínuo) é a metodologia oficial da AWS para migrações heterogêneas de bancos de dados com downtime mínimo de cutover."
        },
        {
          "id": "C",
          "text": "Configurar o Oracle GoldenGate on-premises para replicar dados diretamente para um bucket Amazon S3 e carregar os dados no Aurora via extensões aws_s3.",
          "explanation": "Incorreto: GoldenGate para S3 não converte schemas e código PL/SQL heterogêneos para PostgreSQL e exige licenciamento de software adicional de terceiros."
        },
        {
          "id": "D",
          "text": "Implantar o AWS DataSync para replicar os arquivos de dados (.dbf) do Oracle para instâncias Amazon EC2 rodando PostgreSQL.",
          "explanation": "Incorreto: Arquivos binários .dbf do Oracle não podem ser lidos diretamente por instâncias do PostgreSQL."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "Para migrações heterogêneas de banco de dados (ex: Oracle para PostgreSQL), o AWS Schema Conversion Tool (SCT) é utilizado para traduzir a estrutura de schemas e código de banco. O AWS Database Migration Service (DMS) complementa o processo executando a carga inicial de dados e capturando transações em tempo real (CDC) para permitir a virada da aplicação em poucos minutos.",
      "referenceUrl": "https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html",
      "difficulty": "hard"
    },
    {
      "id": "sim1-q023",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS DataSync", "Amazon S3", "AWS Direct Connect"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma rede hospitalar mantém 800 TB de imagens médicas (arquivos DICOM não estruturados) em um storage NAS on-premises com protocolo NFS. A empresa possui uma conexão AWS Direct Connect de 1 Gbps. A equipe de arquitetura precisa transferir todo esse repositório de dados para o Amazon S3 Glacier Flexible Recovery. A solução deve: 1) Acelerar a cópia de dados pela rede com validação automática de integridade; 2) Limitar o consumo de largura de banda durante o horário comercial para não prejudicar as operações clínicas; 3) Preservar metadados de arquivos e permissões POSIX. Qual solução atende a esses requisitos com a MENOR sobrecarga?",
      "options": [
        {
          "id": "A",
          "text": "Instalar o AWS DataSync Agent no datacenter on-premises conectado ao storage NFS. Configurar tarefas do DataSync para transferir os dados diretamente para o Amazon S3 com a classe de armazenamento apropriada, ativando a validação de integridade dos dados e definindo limites de largura de banda (bandwidth throttling) nos horários comerciais.",
          "explanation": "Correto: O AWS DataSync é um serviço acelerado de transferência de dados que opera até 10x mais rápido que ferramentas tradicionais (rsync), com validação automática de integridade ponta a ponta, preservação de metadados POSIX e suporte a agendamento com controle de largura de banda."
        },
        {
          "id": "B",
          "text": "Configurar scripts em Python utilizando a AWS CLI com comandos 'aws s3 sync' executados em cron jobs no storage local.",
          "explanation": "Incorreto: A AWS CLI sobre 800 TB com milhões de arquivos pequenos é lenta, não possui aceleração de protocolo de rede nem controle nativo robusto de throttling e validação de integridade em escala."
        },
        {
          "id": "C",
          "text": "Implantar o AWS Storage Gateway File Gateway e copiar os arquivos manualmente utilizando ferramentas do sistema operacional.",
          "explanation": "Incorreto: O File Gateway é voltado para armazenamento em nuvem híbrida contínuo com cache local, não para migrações em massa aceleradas de 800 TB com validação automatizada."
        },
        {
          "id": "D",
          "text": "Contratar o AWS Snowball Edge para transferir todos os dados fisicamente via correios.",
          "explanation": "Incorreto: Embora o Snowball seja viável, o enunciado especifica o uso da conexão Direct Connect existente com controle de largura de banda na rede."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "O AWS DataSync é o serviço otimizado da AWS para migração acelerada de dados de arquivos (NFS/SMB) e objetos através da rede (Direct Connect ou VPN). Ele inclui protocolo de rede proprietário com compactação, paralelismo massivo, verificação de integridade e controle de consumo de largura de banda configurável.",
      "referenceUrl": "https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q024",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Snow Family", "Amazon S3"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma mineradora multinacional opera em uma localidade remota e acumulou 1,5 PB de dados geológicos e de telemetria sísmica armazenados localmente. A instalação possui apenas uma conexão de internet via satélite com largura de banda de 10 Mbps e alta latência. A empresa precisa transferir todos os 1,5 PB para o Amazon S3 em menos de 3 semanas para permitir que algoritmos de aprendizado de máquina processem os dados em larga escala na nuvem. Qual estratégia atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o AWS DataSync com aceleração de transferência e compressão pela conexão via satélite de 10 Mbps.",
          "explanation": "Incorreto: Uma conexão de 10 Mbps levaria mais de 40 anos para transferir 1,5 PB de dados, violando o prazo estrito de 3 semanas."
        },
        {
          "id": "B",
          "text": "Solicitar um circuito dedicado do AWS Direct Connect de 100 Gbps para a instalação remota da mina.",
          "explanation": "Incorreto: Provisionar circuitos de fibra óptica em regiões remotas de mineração leva meses e tem custos inviáveis para uma transferência pontual."
        },
        {
          "id": "C",
          "text": "Solicitar múltiplos dispositivos AWS Snowball Edge Storage Optimized através do console da AWS. Copiar os dados localmente para os dispositivos usando a rede local de alta velocidade e enviá-los de volta à AWS para carregamento direto no Amazon S3.",
          "explanation": "Correto: A família AWS Snowball Edge é a solução recomendada para transferências de dados em escala de petabytes em locais com conectividade de rede restrita ou inexistente, permitindo migrar 1,5 PB em poucos dias/semanas através de transporte físico seguro."
        },
        {
          "id": "D",
          "text": "Configurar o S3 Transfer Acceleration na conexão via satélite existente.",
          "explanation": "Incorreto: O S3 Transfer Acceleration otimiza a rota após atingir a borda da AWS, mas o gargalo físico da conexão de 10 Mbps via satélite impede a transferência em 3 semanas."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "Quando a largura de banda de rede disponível é insuficiente para transferir grandes volumes de dados (Petabytes) dentro do prazo do projeto, a família AWS Snowball Edge (dispositivos físicos criptografados e resistentes) é a solução ideal e com o menor custo e tempo de migração.",
      "referenceUrl": "https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html",
      "difficulty": "medium"
    },
    {
      "id": "sim1-q025",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["Amazon ECS", "AWS Fargate", "AWS CodeDeploy", "Elastic Load Balancing"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma empresa está modernizando uma aplicação monolítica legada desenvolvida em Java Spring Boot hospedada em servidores físicos on-premises para uma arquitetura de contêineres na AWS. A equipe de arquitetura exige: 1) Operar os contêineres sem necessidade de provisionar, configurar ou gerenciar instâncias de servidores (computação serverless para contêineres); 2) Implementar implantações automáticas com zero tempo de inatividade (Blue/Green Deployment) integradas ao balanceador de carga; 3) Reverter automaticamente para a versão estável caso alarmes do Amazon CloudWatch detectem um aumento na taxa de erros HTTP 5xx durante a virada de tráfego. Quais DUAS soluções atendem a esses requisitos? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Implantar o cluster Amazon EKS utilizando instâncias EC2 gerenciadas com Karpenter para auto-scaling de nós.",
          "explanation": "Incorreto: Instâncias EC2 gerenciadas com Karpenter exigem gestão de nós de infraestrutura e AMI, não sendo modelo serverless puro."
        },
        {
          "id": "B",
          "text": "Executar a aplicação em contêineres no Amazon Elastic Container Service (Amazon ECS) utilizando o tipo de inicialização AWS Fargate (Fargate Launch Type).",
          "explanation": "Correto: O AWS Fargate é o motor de computação serverless para contêineres que elimina totalmente a necessidade de provisionar, gerenciar, aplicar patches ou escalar instâncias EC2 subjacentes."
        },
        {
          "id": "C",
          "text": "Utilizar o AWS Elastic Beanstalk no ambiente Single-Instance com políticas de implantação All-at-Once.",
          "explanation": "Incorreto: Single-Instance com All-at-Once gera tempo de inatividade durante a implantação e não fornece alta disponibilidade."
        },
        {
          "id": "D",
          "text": "Configurar deploys manuais com scripts bash no Jenkins executando comandos 'docker run' diretamente nos servidores.",
          "explanation": "Incorreto: Scripts manuais no Jenkins não oferecem automação de Blue/Green gerenciada nem rollback automatizado baseado em alarmes do CloudWatch."
        },
        {
          "id": "E",
          "text": "Configurar o AWS CodeDeploy com o tipo de implantação Blue/Green para Amazon ECS, associado a dois Target Groups de um Application Load Balancer e configurado com alarmes do Amazon CloudWatch para disparar rollback automático em caso de erros.",
          "explanation": "Correto: O AWS CodeDeploy suporta nativamente implantações Blue/Green para Amazon ECS, roteando o tráfego gradualmente entre target groups do ALB e revertendo automaticamente se os alarmes do CloudWatch forem acionados."
        }
      ],
      "correctAnswers": ["B", "E"],
      "generalExplanation": "A combinação de Amazon ECS com AWS Fargate fornece computação serverless para contêineres sem gestão de servidores. Integrado ao AWS CodeDeploy, viabiliza-se implantações Blue/Green gerenciadas com alternância de tráfego via Application Load Balancer e rollbacks automáticos baseados em alarmes do CloudWatch.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html",
      "difficulty": "hard"
    }
  ]
}

SIM2_DATA = {
  "id": "SAP-C02-SIM-2",
  "title": "AWS Solutions Architect Professional — Simulado 2 (25Q Inéditas)",
  "code": "SAP-C02-SIM-2",
  "category": "Professional",
  "description": "Simulado prático avançado com 25 questões inéditas de alta complexidade, abordando segurança profunda, Disaster Recovery ativo-ativo, HPC, governança multi-contas e estratégias de modernização dos 7 Rs. Tempo calibrado a 2m 56s por questão (73 minutos).",
  "totalQuestions": 25,
  "timeLimitMinutes": 73,
  "passingScore": 750,
  "icon": "shield-check",
  "domains": [
    {
      "id": "domain-1-org-complexity",
      "name": "Domain 1: Design Solutions for Organizational Complexity",
      "weightPercentage": 26
    },
    {
      "id": "domain-2-new-solutions",
      "name": "Domain 2: Design for New Solutions",
      "weightPercentage": 29
    },
    {
      "id": "domain-3-continuous-improvement",
      "name": "Domain 3: Continuous Improvement for Existing Solutions",
      "weightPercentage": 25
    },
    {
      "id": "domain-4-migration-modernization",
      "name": "Domain 4: Accelerate Workload Migration and Modernization",
      "weightPercentage": 20
    }
  ],
  "questions": [
    {
      "id": "sim2-q001",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Network Firewall", "AWS Transit Gateway", "AWS Organizations"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma companhia aérea internacional opera mais de 200 contas no AWS Organizations conectadas via AWS Transit Gateway. A equipe de segurança exige a implementação de uma solução centralizada de filtragem de saída (Egress Filtering) para todo o tráfego HTTP/HTTPS com destino à Internet. A solução deve: 1) Permitir conexões apenas para domínios totalmente qualificados (FQDN) explicitamente autorizados usando filtragem baseada em SNI (Server Name Indication); 2) Registrar e enviar todos os logs de fluxo e alertas para um bucket S3 centralizado na conta de Log Archive; 3) Escalar automaticamente sem exigir proxies manuais em instâncias EC2 em cada VPC. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Configurar NAT Gateways em cada VPC de aplicação e aplicar regras de Network ACLs baseadas em nomes de domínio FQDN.",
          "explanation": "Incorreto: Network ACLs operam na camada 3/4 com base em blocos de endereços IP e portas, não sendo capazes de interpretar cabeçalhos TLS/HTTP ou nomes de domínio FQDN."
        },
        {
          "id": "B",
          "text": "Criar uma VPC de Saída (Egress VPC) centralizada com endpoints do AWS Network Firewall em múltiplas AZs conectada ao AWS Transit Gateway. Configurar Stateful Rule Groups com regras de lista de domínios (Domain Lists) com ação de 'Allow' para os FQDNs aprovados e habilitar o log de alertas e fluxos diretamente para o bucket S3 central na conta Log Archive.",
          "explanation": "Correto: O AWS Network Firewall fornece inspeção de tráfego com estado (Stateful) nas camadas 3 a 7, permitindo filtragem precisa de domínios FQDN via SNI em tráfego TLS/HTTP, com suporte a alta disponibilidade multi-AZ e integração com o Transit Gateway."
        },
        {
          "id": "C",
          "text": "Instalar clusters de servidores Squid Proxy em instâncias EC2 em cada conta membro com scripts de sincronização de listas de domínios via cron.",
          "explanation": "Incorreto: Proxies Squid em EC2 em 200 contas geram alta sobrecarga de manutenção, gargalos de desempenho e custos desnecessários em comparação ao serviço gerenciado."
        },
        {
          "id": "D",
          "text": "Utilizar o AWS WAF diretamente associado aos NAT Gateways de cada VPC para filtrar tráfego de saída.",
          "explanation": "Incorreto: O AWS WAF não pode ser associado a NAT Gateways; ele se integra a Application Load Balancers, API Gateways, CloudFront e AppSync para tráfego de entrada."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "Para controle centralizado de tráfego de saída (Egress) em escala enterprise, o AWS Network Firewall implantado em uma Egress VPC conectada ao Transit Gateway é a solução de referência. Seus grupos de regras com estado permitem filtragem avançada por SNI/FQDN com registro completo de logs.",
      "referenceUrl": "https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q002",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS IAM", "AWS Organizations"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira deseja delegar a criação de IAM Roles para os líderes de desenvolvimento em 100 contas membros da organização. No entanto, o Diretor de Segurança da Informação (CISO) exige que os administradores delegados não possam criar roles que concedam privilégios mais amplos do que um conjunto de permissões estritas predefinidas (por exemplo, não podem desativar o GuardDuty, apagar trilhas do CloudTrail ou modificar chaves KMS corporativas). A solução também deve impedir que esses administradores excluam ou modifiquem o limite de permissão das roles que criarem. Qual mecanismo atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Configurar Service Control Policies (SCPs) que neguem a ação iam:CreateRole em todas as contas membro.",
          "explanation": "Incorreto: Negar iam:CreateRole impede totalmente que os desenvolvedores criem qualquer role, violando o requisito de delegar a criação."
        },
        {
          "id": "B",
          "text": "Criar regras gerenciadas do AWS Config que detectem roles com permissões de administrador e notifiquem o time de segurança por e-mail via Amazon SNS.",
          "explanation": "Incorreto: O AWS Config é uma ferramenta detectiva a posteriori e não impede preventivamente a escalada de privilégios no momento da criação da role."
        },
        {
          "id": "C",
          "text": "Anexar uma política gerenciada do IAM aos grupos de desenvolvedores com a condição 'aws:PrincipalTag/RoleType'.",
          "explanation": "Incorreto: Políticas de grupo não impedem que um usuário com privilégio de criar roles crie uma nova role com permissões 'AdministratorAccess' sem limites."
        },
        {
          "id": "D",
          "text": "Impor o uso de IAM Permissions Boundaries. Criar uma política IAM anexada aos desenvolvedores exigindo que qualquer chamada a iam:CreateRole ou iam:PutRolePolicy inclua a Permissions Boundary obrigatória, e utilizar SCPs ou políticas IAM para negar as ações iam:DeleteRolePermissionsBoundary e iam:PutRolePermissionsBoundary.",
          "explanation": "Correto: As IAM Permissions Boundaries estabelecem o limite máximo de privilégios que uma role criada por um desenvolvedor delegado pode ter. Bloquear a remoção da boundary impede que o desenvolvedor crie roles superprivilegiadas."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "As IAM Permissions Boundaries são o padrão oficial da AWS para delegação segura de administração do IAM. Elas garantem que administradores delegados possam criar e gerenciar roles para suas aplicações sem jamais conceder mais permissões do que o teto estabelecido pela boundary.",
      "referenceUrl": "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q003",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["Amazon EFS", "AWS Resource Access Manager", "Amazon VPC"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Um consórcio de pesquisa médica possui 40 contas AWS integradas no AWS Organizations. Os pesquisadores executam cargas de trabalho distribuídas em instâncias EC2 em várias contas que precisam acessar simultaneamente um sistema de arquivos compartilhado NFS de alta performance e baixa latência (Amazon EFS). A infraestrutura de rede deve garantir comunicação totalmente privada através de subnets compartilhadas, sem tráfego passando pela Internet ou por gateways públicos. Qual solução atende a esses requisitos de forma centralizada?",
      "options": [
        {
          "id": "A",
          "text": "Criar um sistema de arquivos Amazon EFS na conta central de infraestrutura utilizando subnets compartilhadas com todas as contas membros via AWS Resource Access Manager (RAM). Criar Mount Targets do EFS nessas subnets compartilhadas e permitir o tráfego NFS (porta 2049) nas Security Groups associadas.",
          "explanation": "Correto: O Amazon EFS em conjunto com VPC Sharing (via AWS RAM) permite que instâncias EC2 em contas participantes montem o sistema de arquivos diretamente nas subnets compartilhadas através dos Mount Targets locais com alta performance e tráfego 100% privado."
        },
        {
          "id": "B",
          "text": "Criar sistemas de arquivos EFS separados em cada uma das 40 contas e sincronizar os dados diariamente utilizando funções do AWS Lambda com S3 como ponte.",
          "explanation": "Incorreto: Criar 40 EFS separados quebra o requisito de sistema de arquivos compartilhado e sincronizado em tempo real para análises concorrentes."
        },
        {
          "id": "C",
          "text": "Expor o sistema de arquivos EFS utilizando um Internet Gateway e atribuir Elastic IPs públicos a cada nó de montagem.",
          "explanation": "Incorreto: Expor tráfego NFS para a internet pública viola regras básicas de segurança e o requisito de comunicação privada."
        },
        {
          "id": "D",
          "text": "Utilizar o AWS Storage Gateway Volume Gateway conectado via túneis VPN IPsec em cada conta membro.",
          "explanation": "Incorreto: O Volume Gateway fornece volumes de bloco (iSCSI), não compartilhamento de arquivos NFS multi-nó concorrente de alta performance na mesma região."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "O Amazon EFS suporta nativamente montagem multi-conta através de subnets compartilhadas via AWS RAM (VPC Sharing), permitindo que instâncias em diferentes contas acessem os Mount Targets locais de forma transparente com segurança e alto throughput.",
      "referenceUrl": "https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-vpc-peering.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q004",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Control Tower", "AWS Organizations", "AWS Service Catalog"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma corporação global precisa modernizar sua governança na nuvem para gerenciar mais de 100 contas AWS. A equipe executiva exige: 1) Implementar uma Landing Zone automatizada baseada nas melhores práticas da AWS com provisionamento padronizado de novas contas em minutos; 2) Impor guardrails preventivos que impeçam violações de conformidade de segurança e guardrails detectivos que monitorem recursos continuamente; 3) Automatizar a criação de contas por meio de um portal de autoatendimento para os times de engenharia. Quais DUAS soluções atendem a esses requisitos? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Desenvolver scripts em Python utilizando o Boto3 para criar contas via API do Organizations e configurar instâncias EC2 com Puppet para aplicar configurações.",
          "explanation": "Incorreto: Desenvolver scripts manuais sob medida exige alta manutenção e não oferece a governança padronizada e guardrails nativos de uma Landing Zone."
        },
        {
          "id": "B",
          "text": "Configurar o AWS OpsWorks em cada conta membro com receitas Chef para aplicar políticas de segurança.",
          "explanation": "Incorreto: O AWS OpsWorks é voltado para gerenciamento de configurações de servidores e não para provisionamento e governança de contas em nível de organização."
        },
        {
          "id": "C",
          "text": "Implantar o AWS Control Tower para estabelecer uma Landing Zone estruturada com OUs (Core, Custom, Sandbox), aplicando guardrails preventivos via Service Control Policies (SCPs) e guardrails detectivos via regras do AWS Config.",
          "explanation": "Correto: O AWS Control Tower é o serviço gerenciado oficial para configurar e governar ambientes multi-contas seguros e escaláveis (Landing Zones), aplicando guardrails preventivos (SCPs) e detectivos (AWS Config)."
        },
        {
          "id": "D",
          "text": "Utilizar o Amazon CloudWatch Synthetics para verificar a conformidade de segurança de cada conta a cada 5 minutos.",
          "explanation": "Incorreto: O CloudWatch Synthetics serve para monitorar endpoints e APIs de aplicações através de canaries, não para governança de conformidade de contas AWS."
        },
        {
          "id": "E",
          "text": "Utilizar a Account Factory do AWS Control Tower, integrada opcionalmente com o AWS Service Catalog, para permitir que equipes autorizadas solicitem e provisionem novas contas em autoatendimento com guardrails pré-configurados.",
          "explanation": "Correto: A Account Factory do Control Tower (sustentada pelo Service Catalog) automatiza o provisionamento padronizado de novas contas em conformidade com as políticas corporativas."
        }
      ],
      "correctAnswers": ["C", "E"],
      "generalExplanation": "O AWS Control Tower fornece a implementação de Landing Zone automatizada mais rápida e recomendada pela AWS. Ele combina o provisionamento de contas via Account Factory (integrado ao Service Catalog) com guardrails preventivos (SCPs) e detectivos (AWS Config) em toda a organização.",
      "referenceUrl": "https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q005",
      "examId": "SAP-C02-SIM-1",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Direct Connect", "AWS Transit Gateway"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação de telecomunicações possui dois datacenters on-premises conectados à AWS através de conexões redundantes do AWS Direct Connect de 10 Gbps em locais de conexão distintos. A empresa possui 50 VPCs distribuídas em duas regiões da AWS (us-east-1 e us-west-2) que precisam se comunicar com a rede local. A equipe de rede precisa consolidar a conectividade de rede híbrida evitando a criação de dezenas de Virtual Interfaces (VIFs) privadas e minimizando a sobrecarga de sessões BGP nos roteadores locais. Qual arquitetura atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Criar Virtual Interfaces (VIFs) privadas para cada uma das 50 VPCs diretamente conectadas aos Virtual Private Gateways (VGWs) de cada VPC.",
          "explanation": "Incorreto: Criar VIFs privadas para 50 VPCs gera 50 sessões BGP nos roteadores locais por conexão Direct Connect, excedendo limites e criando altíssima complexidade de gerenciamento."
        },
        {
          "id": "B",
          "text": "Configurar conexões VPN IPsec através da Internet pública para cada VPC a partir dos roteadores locais.",
          "explanation": "Incorreto: Utilizar VPN pela internet pública desperdiça os links dedicados de 10 Gbps do Direct Connect e introduz instabilidade de latência."
        },
        {
          "id": "C",
          "text": "Implantar um AWS Transit Gateway em cada região (us-east-1 e us-west-2) anexado às respectivas VPCs. Criar um Direct Connect Gateway (DXGW) global, associá-lo a uma Transit Virtual Interface (Transit VIF) em cada link do Direct Connect, e associar o Direct Connect Gateway aos Transit Gateways de ambas as regiões.",
          "explanation": "Correto: A Transit VIF combinada com o Direct Connect Gateway permite conectar links físicos de Direct Connect a múltiplos Transit Gateways em diferentes regiões, exigindo apenas uma sessão BGP por link e suportando centenas de VPCs de forma consolidada."
        },
        {
          "id": "D",
          "text": "Estabelecer conexões de VPC Peering entre a VPC de us-east-1 e us-west-2 e conectar o Direct Connect a apenas uma VPC.",
          "explanation": "Incorreto: O VPC Peering não suporta tráfego transitivo (Edge-to-Edge routing) vindo de um Direct Connect para saltar para outra VPC."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "Para conectar conexões dedicadas do AWS Direct Connect a múltiplas VPCs em múltiplas regiões sem sobrecarga de sessões BGP, a arquitetura recomendada consiste em usar uma Transit VIF conectada a um Direct Connect Gateway, associado aos AWS Transit Gateways regionais.",
      "referenceUrl": "https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q006",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-1-org-complexity",
      "domainName": "Domain 1: Design Solutions for Organizational Complexity",
      "services": ["AWS Service Quotas", "Amazon EventBridge", "Amazon SNS"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma equipe de operações em nuvem gerencia mais de 120 contas no AWS Organizations. Recentemente, lançamentos de novos produtos falharam porque algumas contas atingiram inesperadamente os limites de cotas de serviço da AWS (ex: limite de instâncias EC2, limites de VPCs por região e limite de Elastic IPs). A liderança de engenharia exige uma solução centralizada que monitore continuamente a utilização de cotas em todas as contas e notifique a equipe no canal do Slack/PagerDuty sempre que qualquer cota atingir 80% do seu limite, permitindo solicitar aumentos de cota proativamente. Qual solução atende a esses requisitos com a MENOR sobrecarga?",
      "options": [
        {
          "id": "A",
          "text": "Desenvolver um script em Python que roda a cada 15 minutos em uma instância EC2, executa comandos da CLI em cada conta assumindo roles cross-account e calcula os limites manualmente.",
          "explanation": "Incorreto: Scripts manuais em EC2 sofrem com rate limits de chamadas de API, têm manutenção complexa e não utilizam as capacidades nativas do Service Quotas."
        },
        {
          "id": "B",
          "text": "Utilizar o AWS Service Quotas integrado ao AWS Organizations e configurar modelos de solicitação de cota (Quota Request Templates). Criar alarmes do Amazon CloudWatch associados às métricas do Service Quotas nas contas e rotear alertas via Amazon EventBridge e Amazon SNS para as ferramentas de notificação da equipe.",
          "explanation": "Correto: O AWS Service Quotas integra-se nativamente com o CloudWatch e Organizations, emitindo métricas de utilização de cotas e eventos para o EventBridge quando limites pré-configurados (como 80%) são atingidos, permitindo automação de alertas e solicitações."
        },
        {
          "id": "C",
          "text": "Configurar o AWS Trusted Advisor em cada conta e contratar suporte Enterprise para que o Technical Account Manager (TAM) monitore manualmente as cotas diariamente.",
          "explanation": "Incorreto: O monitoramento manual pelo TAM não fornece alertas em tempo real automatizados e tem custo desnecessário para automação de cotas."
        },
        {
          "id": "D",
          "text": "Implantar o AWS Config com regras customizadas em cada conta para inspecionar o número de recursos provisionados em relação a tabelas DynamoDB estáticas.",
          "explanation": "Incorreto: O AWS Config não é projetado para monitoramento de métricas dinâmicas de cotas de serviço da AWS."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "O AWS Service Quotas permite visualizar e gerenciar limites de serviços da AWS de forma centralizada. A integração com o Amazon CloudWatch e Amazon EventBridge possibilita monitorar o consumo de cotas e disparar notificações automáticas quando os limites se aproximam de valores críticos.",
      "referenceUrl": "https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q007",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon DynamoDB"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma empresa de jogos online multiplayer está lançando um jogo competitivo global. O estado das sessões dos jogadores, inventário de itens e placares em tempo real devem ser lidos e atualizados simultaneamente por servidores de jogos hospedados em us-east-1, eu-central-1 e ap-northeast-1. O sistema exige: 1) Latência de leitura e gravação inferior a 10 milissegundos localmente em cada região; 2) Gravação ativa-ativa (Multi-Region Active-Active) com replicação totalmente gerenciada; 3) Escalonamento automático para acomodar picos súbitos de milhões de jogadores durante torneios. Qual solução de banco de dados atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Amazon RDS for MySQL com réplicas de leitura cross-region assíncronas.",
          "explanation": "Incorreto: O RDS for MySQL possui apenas uma única região de gravação (Single-Writer); gravações vindas de outras regiões sofrem com latência de rede transcontinental."
        },
        {
          "id": "B",
          "text": "Amazon ElastiCache for Redis com cluster multi-região configurado com sincronização por scripts de aplicação.",
          "explanation": "Incorreto: ElastiCache for Redis Global Datastore é projetado para leituras locais em réplicas secundárias, com todas as gravações direcionadas para a região primária."
        },
        {
          "id": "C",
          "text": "Amazon Aurora PostgreSQL com replicação lógica bidirecional configurada manualmente em instâncias EC2.",
          "explanation": "Incorreto: Configurar replicação lógica bidirecional manualmente em PostgreSQL é altamente complexo, propenso a conflitos de chave primária e não oferece escalabilidade serverless automática."
        },
        {
          "id": "D",
          "text": "Amazon DynamoDB Global Tables com modo de capacidade On-Demand ativado nas três regiões.",
          "explanation": "Correto: O DynamoDB Global Tables fornece arquitetura ativa-ativa multi-região nativa com leituras e gravações em milissegundos de um dígito em qualquer uma das regiões participantes, replicação assíncrona automática com resolução de conflitos ('last writer wins') e modo On-Demand para acomodar picos repentinos sem provisionamento manual."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O Amazon DynamoDB Global Tables é o serviço de banco de dados NoSQL totalmente gerenciado da AWS que suporta gravação e leitura multi-região ativa-ativa com latência ultra-baixa e resolução nativa de conflitos, sendo o padrão para jogos globais e aplicações de alta escala.",
      "referenceUrl": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q008",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon API Gateway", "AWS WAF", "AWS Lambda"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma fintech está lançando um aplicativo de carteira digital que expõe endpoints de API REST para autenticação e consulta de saldo de milhões de clientes móveis. A arquitetura exige: 1) Execução serverless de alta disponibilidade sem servidores dedicados; 2) Proteção contra ataques de força bruta e DDoS na camada de aplicação, aplicando limitação de taxa (Rate Limiting) automática de no máximo 100 requisições por minuto por endereço IP; 3) Garantir que a inicialização de funções (Cold Starts) não cause picos de latência superiores a 100 ms para os usuários finais. Qual combinação de serviços atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Implantar o Amazon API Gateway (Edge-Optimized) integrado a funções AWS Lambda com Provisioned Concurrency configurada. Associar o AWS WAF ao API Gateway com uma Rate-Based Rule configurada para limitar o tráfego a 100 requisições por minuto por IP.",
          "explanation": "Correto: O API Gateway fornece gerenciamento serverless de API; o Provisioned Concurrency do Lambda mantém ambientes de execução pré-inicializados, eliminando cold starts; e o AWS WAF com Rate-Based Rules bloqueia automaticamente IPs que excedem o limite de requisições por minuto."
        },
        {
          "id": "B",
          "text": "Implantar instâncias EC2 com NGINX em Auto Scaling e configurar o módulo 'limit_req_zone' para controlar a taxa de requisições.",
          "explanation": "Incorreto: Utilizar servidores EC2 com NGINX adiciona gerenciamento de servidores, balanceamento de carga e manutenção de patches, violando o requisito serverless."
        },
        {
          "id": "C",
          "text": "Utilizar o Network Load Balancer (NLB) com Target Groups apontando diretamente para funções AWS Lambda sem WAF.",
          "explanation": "Incorreto: O NLB opera na camada 4 e não oferece suporte nativo à inspeção de camada 7 e Rate-Based Rules do AWS WAF contra ataques de força bruta em URLs de autenticação."
        },
        {
          "id": "D",
          "text": "Configurar o Amazon CloudFront na frente de instâncias EC2 e escrever código no backend para rastrear IPs em tabelas DynamoDB.",
          "explanation": "Incorreto: Implementar controle de taxa manualmente no código consumindo DynamoDB introduz latência, custos extras de banco de dados e desperdício de esforço em relação ao AWS WAF."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "A arquitetura recomendada para APIs serverless protegidas e de baixa latência combina Amazon API Gateway + AWS Lambda com Provisioned Concurrency (para eliminar cold starts) e AWS WAF com Rate-Based Rules para mitigação automática de abusos e ataques de força bruta.",
      "referenceUrl": "https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q009",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon FSx", "AWS Directory Service", "Amazon EC2"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação de engenharia utiliza uma aplicação legada em Windows que requer acesso concorrente a um compartilhamento de arquivos SMB com mais de 20 TB de arquivos CAD. A aplicação exige: 1) Integração nativa com o Microsoft Active Directory corporativo on-premises para autenticação baseada em Kerberos e listas de controle de acesso (ACLs) NTFS; 2) Alta disponibilidade em múltiplas Availability Zones com failover automático e transparente para a aplicação; 3) Throughput de pelo menos 1 GB/s com armazenamento em estado sólido (SSD); 4) Capacidade de restaurar versões de arquivos anteriores via Shadow Copies (VSS). Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Implantar um sistema de arquivos Amazon EFS com o EFS Mount Helper configurado em instâncias Windows.",
          "explanation": "Incorreto: O Amazon EFS é um sistema de arquivos NFS nativo para Linux e não fornece suporte nativo a ACLs NTFS, Kerberos via Active Directory e protocolo SMB para Windows."
        },
        {
          "id": "B",
          "text": "Montar volumes Amazon EBS Multi-Attach em instâncias EC2 rodando Windows Server em cluster de failover.",
          "explanation": "Incorreto: Volumes EBS Multi-Attach (io1/io2) não oferecem sistema de arquivos SMB gerenciado com suporte nativo a Active Directory e Shadow Copies para instâncias em múltiplas AZs."
        },
        {
          "id": "C",
          "text": "Criar um sistema de arquivos Amazon FSx for Windows File Server com implantação Multi-AZ e armazenamento SSD. Integrar o sistema de arquivos ao Microsoft Active Directory corporativo através de uma relação de confiança (Forest Trust) com o AWS Directory Service for Microsoft AD (AWS Managed Microsoft AD) e habilitar cópias de sombra periódicas (Shadow Copies / VSS).",
          "explanation": "Correto: O Amazon FSx for Windows File Server é totalmente gerenciado em Windows Server nativo, suporta SMB, NTFS ACLs, integração com Active Directory, failover síncrono automático Multi-AZ e Shadow Copies (VSS) para recuperação de arquivos por usuários."
        },
        {
          "id": "D",
          "text": "Utilizar o Amazon S3 File Gateway montado como disco de rede em cada estação Windows.",
          "explanation": "Incorreto: O S3 File Gateway não suporta bloqueio de arquivos SMB avançado exigido por aplicações CAD e não implementa o conjunto completo de ACLs NTFS e Shadow Copies."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "O Amazon FSx for Windows File Server é o serviço de armazenamento compartilhado de arquivos padrão da AWS para cargas de trabalho Windows. Ele oferece compatibilidade nativa completa com o protocolo SMB, integração profunda com Microsoft Active Directory, suporte a NTFS e implantação Multi-AZ resiliente.",
      "referenceUrl": "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q010",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["AWS CloudHSM", "AWS KMS", "Amazon S3"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma empresa prestadora de serviços para o governo federal precisa armazenar e criptografar documentos confidenciais no Amazon S3. Devido a exigências regulatórias rigorosas (FIPS 140-2 Nível 3), a empresa tem os seguintes requisitos obrigatórios: 1) As chaves criptográficas devem ser geradas e armazenadas exclusivamente em módulos de segurança de hardware (HSM) dedicados e validados em FIPS 140-2 Nível 3, sob controle físico e lógico exclusivo da empresa; 2) Nem mesmo funcionários da AWS podem ter acesso ao material criptográfico; 3) A solução deve suportar alta disponibilidade através de múltiplas Availability Zones na região. Quais DUAS soluções atendem a esses requisitos? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o AWS KMS com chaves gerenciadas pela AWS (AWS Managed Keys) padrão para criptografia SSE-KMS nos buckets S3.",
          "explanation": "Incorreto: Chaves gerenciadas pela AWS utilizam HSMs com certificação FIPS 140-2 Nível 2 (multi-tenant) e não fornecem controle de hardware dedicado exclusivo FIPS 140-2 Nível 3."
        },
        {
          "id": "B",
          "text": "Provisionar um cluster do AWS CloudHSM com múltiplos appliances HSM distribuídos em diferentes Availability Zones para garantir alta disponibilidade.",
          "explanation": "Correto: O AWS CloudHSM fornece appliances HSM dedicados e com certificação FIPS 140-2 Nível 3, onde o cliente possui controle criptográfico exclusivo sobre os usuários e chaves, inacessíveis para o pessoal da AWS."
        },
        {
          "id": "C",
          "text": "Utilizar criptografia SSE-S3 padrão com rotação de chaves a cada 90 dias.",
          "explanation": "Incorreto: SSE-S3 utiliza chaves gerenciadas pelo S3 sem controle de hardware dedicado FIPS Nível 3."
        },
        {
          "id": "D",
          "text": "Configurar um AWS KMS Custom Key Store backed by AWS CloudHSM (ou utilizar bibliotecas PKCS#11 / JCE diretamente na aplicação) para realizar a criptografia dos objetos com as chaves hospedadas no cluster CloudHSM.",
          "explanation": "Correto: Integrar o AWS KMS com um Custom Key Store respaldado por um cluster CloudHSM permite combinar a facilidade de integração do KMS com os serviços da AWS (como S3) mantendo as chaves armazenadas no hardware FIPS 140-2 Nível 3 dedicado."
        },
        {
          "id": "E",
          "text": "Criar um cluster de instâncias EC2 com discos EBS criptografados para executar software de criptografia GPG customizado.",
          "explanation": "Incorreto: Instâncias EC2 comuns com software GPG não atendem aos requisitos de conformidade com módulos de hardware FIPS 140-2 Nível 3 dedicados."
        }
      ],
      "correctAnswers": ["B", "D"],
      "generalExplanation": "Quando os requisitos de conformidade exigem módulos de segurança em hardware dedicados com certificação FIPS 140-2 Nível 3 e controle exclusivo do cliente sobre o material das chaves, o AWS CloudHSM é o serviço obrigatório. Ele pode ser integrado ao AWS KMS por meio de um Custom Key Store para fornecer criptografia transparente a serviços como o Amazon S3.",
      "referenceUrl": "https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q011",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon Kinesis", "Amazon S3", "AWS Lambda"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira precisa construir um pipeline de ingestão e análise de transações financeiras em tempo real capaz de receber mais de 100.000 eventos por segundo de terminais de pagamento. A arquitetura deve atender a dois requisitos simultâneos: 1) Avaliar cada transação em tempo real com latência inferior a 15 milissegundos utilizando um modelo de machine learning de detecção de fraudes; 2) Persistir todos os eventos brutos no Amazon S3 em lotes compactados no formato Apache Parquet particionados por ano/mês/dia/hora para consultas analíticas posteriores no Amazon Athena. Qual arquitetura atende a esses requisitos com a MENOR sobrecarga operacional?",
      "options": [
        {
          "id": "A",
          "text": "Enviar as transações diretamente para o Amazon SQS Standard, consumir as mensagens com instâncias EC2 em Auto Scaling que gravam no S3 e executam a inferência localmente.",
          "explanation": "Incorreto: Filas SQS Standard com instâncias EC2 gerenciadas manualmente não oferecem conversão nativa de formato Parquet nem a latência de streaming em tempo real otimizada do Kinesis."
        },
        {
          "id": "B",
          "text": "Ingerir as transações em um Amazon Kinesis Data Streams. Configurar funções AWS Lambda (ou Amazon Managed Service for Apache Flink) conectadas ao stream para processamento e avaliação de fraude em tempo real. Paralelamente, conectar um Amazon Kinesis Data Firehose ao stream para realizar o buffer, conversão automática de formato para Parquet e entrega particionada no Amazon S3.",
          "explanation": "Correto: O Kinesis Data Streams permite múltiplos consumidores simultâneos em tempo real (Lambda/Flink para detecção de fraude imediata em sub-segundos). O Kinesis Data Firehose conectado ao mesmo stream realiza agregação de lote, conversão nativa para Parquet com o Glue Schema Registry e entrega particionada no S3 sem servidores."
        },
        {
          "id": "C",
          "text": "Gravar cada transação individualmente como um arquivo JSON no Amazon S3 via API REST e acionar eventos S3 Event Notifications para executar o Lambda.",
          "explanation": "Incorreto: Gravar 100.000 pequenos arquivos individuais por segundo no S3 gera custos excessivos de chamadas PUT, problemas de 'small files' para o Athena e latência inadequada para antifraude em tempo real."
        },
        {
          "id": "D",
          "text": "Utilizar o Amazon Managed Streaming for Apache Kafka (Amazon MSK) e criar conectores Kafka Connect customizados rodando em clusters EC2.",
          "explanation": "Incorreto: O Amazon MSK com conectores customizados em EC2 adiciona sobrecarga de gerenciamento e infraestrutura muito superior ao Kinesis Data Streams + Firehose serverless totalmente gerenciados."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "Para fluxos de dados em tempo real com múltiplos padrões de consumo (análise imediata de sub-segundos + arquivamento em data lake colunar no S3), o padrão arquitetural de referência é o Amazon Kinesis Data Streams (camada de ingestão multi-consumidor) associado ao Amazon Kinesis Data Firehose (conversão nativa para Parquet e persistência no S3).",
      "referenceUrl": "https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q012",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["AWS Global Accelerator", "Elastic Load Balancing", "AWS Shield Advanced"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação global de SaaS hospeda seu portal de clientes em Application Load Balancers nas regiões us-east-1 e eu-west-1. Devido a rígidas exigências de governança de segurança dos clientes, as conexões de saída das redes dos clientes devem ser autorizadas para um conjunto fixo e imutável de 2 endereços IP estáticos globais em seus firewalls. A arquitetura também precisa garantir: 1) Roteamento de clientes para a região mais próxima com menor latência; 2) Failover de tráfego automático e imediato em caso de pane regional em menos de 20 segundos; 3) Proteção contra ataques DDoS de camadas 3, 4 e 7. Qual arquitetura atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o Amazon Route 53 com registros A baseados em roteamento por latência associados a Health Checks e diminuir o TTL para 5 segundos.",
          "explanation": "Incorreto: O Route 53 não fornece endereços IP fixos estáticos únicos (os IPs dos ALBs são dinâmicos) e depende de caches DNS que frequentemente ignoram o TTL."
        },
        {
          "id": "B",
          "text": "Implantar distribuições do Amazon CloudFront com Elastic IPs associados em cada região.",
          "explanation": "Incorreto: O CloudFront utiliza conjuntos dinâmicos e amplos de endereços IP em suas centenas de Edge Locations, não fornecendo dois IPs estáticos fixos dedicados para regras de firewall corporativo."
        },
        {
          "id": "C",
          "text": "Configurar gateways NAT com Elastic IPs em cada VPC e usar BGP para anunciar os mesmos IPs em ambas as regiões.",
          "explanation": "Incorreto: NAT Gateways são exclusivamente para tráfego de saída (outbound) originado na VPC, não para receber conexões de entrada (inbound) da Internet."
        },
        {
          "id": "D",
          "text": "Configurar o AWS Global Accelerator fornecendo 2 endereços IP Anycast estáticos globais e associar os Application Load Balancers de us-east-1 e eu-west-1 como Endpoint Groups. Habilitar o AWS Shield Advanced e o AWS WAF nos ALBs.",
          "explanation": "Correto: O AWS Global Accelerator fornece 2 endereços IP Anycast estáticos que servem como ponto de entrada fixo global. Ele monitora a saúde dos endpoints nas duas regiões e realiza failover automático em segundos pela rede backbone privada da AWS, com integração nativa com o AWS Shield Advanced."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS Global Accelerator é a solução indicada para fornecer endereços IP estáticos globais fixos (Anycast) com failover determinístico e instantâneo entre regiões, contornando limitações de cache DNS de clientes corporativos restritivos.",
      "referenceUrl": "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q013",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["Amazon EKS", "AWS Secrets Manager", "AWS IAM"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma fintech está implantando uma plataforma de pagamentos em clusters Amazon EKS (Kubernetes) em conformidade com o padrão PCI-DSS. A arquitetura de segurança exige que: 1) As credenciais e chaves de API sejam armazenadas e rotacionadas automaticamente a cada 30 dias pelo AWS Secrets Manager; 2) Os pods nos nós do EKS consumam os segredos diretamente como variáveis de ambiente ou arquivos montados em memória, sem persistir dados no disco rígido; 3) O acesso ao Secrets Manager seja concedido de forma estrita no nível de cada Pod individual (IAM Roles for Service Accounts - IRSA), e não no nível da instância do nó de trabalho (Node IAM Role). Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Utilizar o Secrets Store CSI Driver do Kubernetes com o AWS Secrets and Configuration Provider (ASCP) no cluster EKS. Configurar Service Accounts do Kubernetes associadas a IAM Roles (IRSA) específicas para cada pod com políticas mínimas que autorizam a leitura das chaves correspondentes no AWS Secrets Manager.",
          "explanation": "Correto: O Secrets Store CSI Driver com o provedor da AWS (ASCP) monta segredos do Secrets Manager diretamente na memória dos pods (tmpfs) como volumes ou variáveis. Combinado com IRSA (IAM Roles for Service Accounts), o controle de acesso é isolado por Pod usando OpenID Connect (OIDC), sem expor credenciais na IAM Role do nó EC2."
        },
        {
          "id": "B",
          "text": "Anexar uma política com permissão de leitura no Secrets Manager à IAM Role das instâncias EC2 (Node Instance Role) do cluster EKS e orientar os pods a consultar a API do Secrets Manager na inicialização.",
          "explanation": "Incorreto: Conceder permissões na Node Instance Role viola o princípio do menor privilégio, permitindo que qualquer pod em execução no mesmo nó acesse os segredos de outros microsserviços."
        },
        {
          "id": "C",
          "text": "Armazenar as credenciais como Kubernetes Secrets padrão em base64 diretamente nos manifestos do Git (GitOps).",
          "explanation": "Incorreto: Kubernetes Secrets são apenas codificados em base64 (não criptografados com rotação automática) e armazená-los no Git viola normas de segurança PCI-DSS."
        },
        {
          "id": "D",
          "text": "Escrever scripts initContainers em cada Pod que usam credenciais estáticas de usuário IAM (Access Key e Secret Key) para baixar os segredos do Secrets Manager.",
          "explanation": "Incorreto: Utilizar credenciais estáticas de usuário IAM dentro de contêineres cria grave risco de vazamento e quebra a rotação automatizada."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "A arquitetura recomendada para consumo seguro de segredos no Amazon EKS utiliza o Secrets Store CSI Driver associado ao AWS Provider (ASCP) e autenticação via IAM Roles for Service Accounts (IRSA), montando segredos em memória efêmera com isolamento granular por Pod.",
      "referenceUrl": "https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_csi_driver.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q014",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-2-new-solutions",
      "domainName": "Domain 2: Design for New Solutions",
      "services": ["AWS Step Functions", "Amazon Textract", "Amazon Comprehend", "Amazon Augmented AI"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma companhia de seguros recebe diariamente milhares de reivindicações de sinistros em formato PDF. A empresa precisa implementar um fluxo de trabalho automatizado que: 1) Extraia texto e dados estruturados de tabelas usando o Amazon Textract; 2) Analise a linguagem e sentimento com o Amazon Comprehend; 3) Caso o índice de confiança da extração seja inferior a 90%, direcione automaticamente o documento para uma fila de revisão humana por especialistas da empresa; 4) Gerencie o estado, novas tentativas com backoff exponencial e tratamento de exceções de forma serverless. Qual solução orquestra esse processo com a MENOR complexidade?",
      "options": [
        {
          "id": "A",
          "text": "Desenvolver uma aplicação monolítica em Java executando em instâncias EC2 com filas SQS gerenciadas por código customizado.",
          "explanation": "Incorreto: Gerenciar estado, retentativas e orquestração de serviços em código monolítico em EC2 é complexo, propenso a falhas e tem alta sobrecarga operacional."
        },
        {
          "id": "B",
          "text": "Utilizar o Amazon EventBridge acionando uma única função AWS Lambda que executa todas as etapas sincronicamente e bloqueia a execução aguardando a revisão humana.",
          "explanation": "Incorreto: O AWS Lambda tem limite máximo de execução de 15 minutos e não suporta aguardar revisões humanas que podem levar horas ou dias."
        },
        {
          "id": "C",
          "text": "Criar uma máquina de estados no AWS Step Functions (Standard Workflow) orquestrando o Amazon Textract e o Amazon Comprehend com blocos de tratamento de erro (Catch/Retry). Integrar o Amazon Augmented AI (Amazon A2I) na etapa de decisão condicional para direcionar documentos com confiança inferior a 90% para fluxos de revisão humana.",
          "explanation": "Correto: O AWS Step Functions Standard Workflow é o serviço nativo para orquestração de fluxos de longa duração e serverless, com suporte a retentativas, ramificações condicionais e integração direta com o Amazon Augmented AI (A2I) para tarefas de Human-in-the-Loop."
        },
        {
          "id": "D",
          "text": "Configurar o Amazon Simple Workflow Service (Amazon SWF) com deciders e workers desenvolvidos em instâncias EC2 em Auto Scaling.",
          "explanation": "Incorreto: O Amazon SWF é um serviço de geração anterior que exige desenvolvimento e manutenção manual de deciders e workers em servidores, sendo o Step Functions a recomendação moderna oficial da AWS."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "O AWS Step Functions é o orquestrador serverless de referência da AWS para pipelines de processamento de documentos com IA. Ele integra-se nativamente com Textract, Comprehend e Amazon Augmented AI (Amazon A2I) para incorporar revisões humanas (Human-in-the-Loop) em fluxos de trabalho com controle visual de estado.",
      "referenceUrl": "https://docs.aws.amazon.com/step-functions/latest/dg/connect-a2i.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q015",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["Amazon S3", "AWS Cost Explorer"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma plataforma de streaming de áudio armazena mais de 10 PB de arquivos de áudio e logs no Amazon S3, gerando um custo de armazenamento de US$ 230.000 mensais em S3 Standard. A análise dos padrões de acesso revelou que: 1) Os arquivos de áudio novos são acessados intensamente nos primeiros 30 dias; 2) Entre 30 e 90 dias, o acesso cai em 90%; 3) Após 90 dias, o acesso é muito raro (menos de 0,5% dos arquivos por ano), mas os arquivos devem ser retidos por 7 anos para fins contratuais e podem ser recuperados em até 12 horas. Qual política de ciclo de vida do Amazon S3 (S3 Lifecycle Policy) reduzirá os custos ao MÁXIMO?",
      "options": [
        {
          "id": "A",
          "text": "Transicionar os objetos imediatamente para o S3 One Zone-IA no dia 1 e excluí-los após 7 anos.",
          "explanation": "Incorreto: S3 One Zone-IA não oferece resiliência Multi-AZ (risco de perda de dados em desastres) e tem custos significativamente mais altos que as classes Glacier para retenção de 7 anos."
        },
        {
          "id": "B",
          "text": "Configurar uma S3 Lifecycle Policy para transicionar os objetos para S3 Standard-IA aos 30 dias, transicionar para S3 Glacier Flexible Recovery aos 90 dias, e transicionar para S3 Glacier Deep Archive após 180 dias com expiração aos 7 anos (2.555 dias).",
          "explanation": "Correto: O S3 Standard-IA reduz o custo aos 30 dias mantendo acesso rápido; o Glacier Flexible Recovery reduz ainda mais aos 90 dias; e o S3 Glacier Deep Archive (classe de menor custo da AWS, ~$0.00099 por GB/mês) otimiza o armazenamento de longo prazo até 7 anos com tempo de recuperação em até 12 horas."
        },
        {
          "id": "C",
          "text": "Habilitar o S3 Versioning com exclusão automática de versões anteriores a cada 7 dias.",
          "explanation": "Incorreto: O S3 Versioning duplica objetos e aumenta custos caso versões antigas não sejam gerenciadas, e não aplica classes frias de armazenamento."
        },
        {
          "id": "D",
          "text": "Manter todos os arquivos no S3 Standard e contratar instâncias reservadas de computação para processar os dados.",
          "explanation": "Incorreto: Instâncias reservadas não fornecem descontos em custos de armazenamento do Amazon S3."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "O uso de políticas de S3 Lifecycle em cascata permite transicionar objetos de forma transparente do S3 Standard para S3 Standard-IA, Glacier Flexible Recovery e finalmente S3 Glacier Deep Archive (a classe de armazenamento em nuvem mais econômica do mercado), maximizando a economia de custos em dados com retenção obrigatória de longo prazo.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q016",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS X-Ray", "Amazon CloudWatch", "Amazon ECS"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma equipe de engenharia gerencia uma arquitetura complexa de microsserviços distribuída em mais de 50 serviços no Amazon ECS, AWS Lambda e Amazon DynamoDB. Os usuários relatam lentidão intermitente nas transações de checkout, mas as métricas individuais de utilização de CPU e memória de cada serviço aparecem saudáveis no CloudWatch. A equipe precisa de uma solução de observabilidade que: 1) Forneça rastreamento distribuído ponta a ponta (Distributed Tracing) de cada requisição através de todos os microsserviços; 2) Gere um mapa visual de dependências dos serviços (Service Map) identificando gargalos e falhas de latência; 3) Isole exatamente qual chamada de banco de dados ou serviço downstream está causando atrasos. Qual serviço atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Configurar o Amazon CloudWatch Logs Insights com consultas SQL para analisar logs de texto estruturados em cada microsserviço.",
          "explanation": "Incorreto: O CloudWatch Logs Insights pesquisa logs de texto, mas não correlaciona automaticamente spans de requisições distribuídas nem gera mapas dinâmicos de serviços."
        },
        {
          "id": "B",
          "text": "Implantar o AWS CloudTrail Insights para monitorar anomalias de chamadas de API de gerenciamento da AWS.",
          "explanation": "Incorreto: O CloudTrail Insights rastreia chamadas na camada de controle da API da AWS (management events), não o fluxo de requisições de aplicação interna de microsserviços."
        },
        {
          "id": "C",
          "text": "Configurar o Amazon VPC Flow Logs em todas as subnets com agregação no Amazon Athena.",
          "explanation": "Incorreto: VPC Flow Logs registram apenas metadados de pacotes IP de rede (L3/L4) e não identificam chamadas de aplicação, queries de banco ou traces distribuídos."
        },
        {
          "id": "D",
          "text": "Implementar o AWS X-Ray (ou AWS Distro for OpenTelemetry) integrando SDKs nas aplicações e executando o daemon/coletor do X-Ray. Utilizar o mapa de serviços do X-Ray (Service Map) e o CloudWatch ServiceLens para analisar traces, segmentos e subsegmentos das requisições.",
          "explanation": "Correto: O AWS X-Ray é o serviço nativo de distributed tracing da AWS. Ele coleta dados sobre as requisições atendidas pela aplicação, gera o mapa visual de serviços interconectados e permite inspecionar tempos de resposta individuais de componentes e chamadas downstream."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS X-Ray combinado com o Amazon CloudWatch ServiceLens é a solução nativa para rastreamento distribuído (Distributed Tracing) e observabilidade de microsserviços na AWS, permitindo mapear gargalos de latência e dependências entre componentes distribuídos.",
      "referenceUrl": "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q017",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Security Hub", "AWS Systems Manager", "Amazon S3", "Amazon EventBridge"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "O CISO de uma organização exige uma solução de remediação automatizada em tempo real para impedir vazamento de dados no Amazon S3 em mais de 80 contas membros no AWS Organizations. Caso qualquer usuário ou script configure um bucket S3 como público (removendo o S3 Block Public Access ou adicionando ACL pública), a solução deve detectar a não-conformidade em segundos e reativar imediatamente o S3 Block Public Access no bucket afetado, sem intervenção humana. Qual arquitetura atende a esses requisitos com a MENOR sobrecarga?",
      "options": [
        {
          "id": "A",
          "text": "Habilitar o AWS Security Hub e o AWS Config em nível organizacional. Configurar uma regra no Amazon EventBridge que capture achados de conformidade de buckets públicos ('[S3.2] S3 buckets should prohibit public read access') e acione um documento do AWS Systems Manager Automation para aplicar o S3 Block Public Access no bucket.",
          "explanation": "Correto: O AWS Security Hub / AWS Config detecta a alteração de conformidade do bucket em tempo real e emite um evento no EventBridge, que aciona o Systems Manager Automation para remediar o bucket instantaneamente."
        },
        {
          "id": "B",
          "text": "Executar um cron job diário em uma instância EC2 que varre todos os buckets S3 e aplica permissões privadas.",
          "explanation": "Incorreto: Varreduras diárias em cron jobs deixam uma janela de vulnerabilidade de até 24 horas onde dados sensíveis podem ser expostos e exfiltrados."
        },
        {
          "id": "C",
          "text": "Criar uma Service Control Policy (SCP) que negue a ação s3:CreateBucket em todas as contas membro.",
          "explanation": "Incorreto: Bloquear s3:CreateBucket impede que os desenvolvedores criem qualquer bucket legítimo na organização."
        },
        {
          "id": "D",
          "text": "Configurar o Amazon GuardDuty para enviar notificações no Amazon SNS para que a equipe de segurança corrija o bucket manualmente.",
          "explanation": "Incorreto: Notificações manuais por e-mail violam o requisito estrito de remediação automatizada instantânea sem intervenção humana."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "A arquitetura recomendada para remediação automatizada de eventos de segurança na AWS utiliza a integração orientada a eventos: AWS Config/Security Hub -> Amazon EventBridge -> AWS Systems Manager Automation (ou AWS Lambda) para reverter configurações inseguras em segundos.",
      "referenceUrl": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q018",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["Amazon Aurora", "Amazon RDS"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma plataforma de e-commerce utiliza o Amazon Aurora PostgreSQL como banco de dados principal. Durante os períodos de pico, consultas analíticas pesadas e relatórios de BI executados pela equipe financeira competem por recursos de CPU e memória com as transações de checkout de clientes na instância primária de gravação (Writer Instance), causando lentidão e bloqueios de tabelas. Como a arquitetura deve ser aprimorada para isolar as consultas analíticas sem alterar a estrutura de dados e com a MENOR sobrecarga?",
      "options": [
        {
          "id": "A",
          "text": "Exportar os dados do banco diariamente para arquivos CSV e importá-los em um cluster Amazon Redshift.",
          "explanation": "Incorreto: Exportações diárias fornecem apenas dados atrasados (D-1) e não atendem a relatórios que necessitam de leitura em tempo real."
        },
        {
          "id": "B",
          "text": "Substituir o Aurora PostgreSQL pelo Amazon DynamoDB com DAX habilitado.",
          "explanation": "Incorreto: Reescrever uma aplicação relacional inteira para NoSQL DynamoDB exige meses de refatoração de código e quebra consultas analíticas complexas com joins."
        },
        {
          "id": "C",
          "text": "Criar réplicas de leitura do Amazon Aurora (Aurora Read Replicas) dedicadas para relatórios e configurar um Aurora Custom Endpoint que agrupa essas réplicas específicas, direcionando a conexão das ferramentas de BI para esse endpoint customizado.",
          "explanation": "Correto: O Amazon Aurora suporta réplicas de leitura com lag típico de milissegundos compartilhando o mesmo volume de storage. O uso de Custom Endpoints permite direcionar consultas pesadas de BI exclusivamente para réplicas dedicadas, isolando 100% dos recursos do nó gravador (Writer)."
        },
        {
          "id": "D",
          "text": "Aumentar o tempo de timeout de conexões na instância primária do Aurora e habilitar multi-threading no sistema operacional.",
          "explanation": "Incorreto: Aumentar timeouts não reduz a concorrência de recursos de hardware e agrava os bloqueios de tabelas."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "No Amazon Aurora, réplicas de leitura compartilham a mesma camada de storage distribuído com latência mínima. A criação de Aurora Custom Endpoints permite criar grupos lógicos de instâncias de leitura (ex: instâncias de alta capacidade para BI) e direcionar o tráfego analítico de forma totalmente isolada da instância de gravação primária.",
      "referenceUrl": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q019",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Savings Plans", "Amazon EC2", "AWS Organizations"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma empresa de software gasta US$ 500.000 mensais em infraestrutura de computação na AWS. A equipe de FinOps e arquitetura precisa otimizar os custos combinando estratégias para dois perfis de cargas de trabalho distintos: 1) Cargas de trabalho corporativas estáveis de missão crítica (APIs e bancos de dados) que rodam 24/7 com consumo previsível de CPU/memória; 2) Cargas de trabalho de processamento em lote (Batch processing e renderização 3D) assíncronas, tolerantes a falhas e que podem ser reiniciadas a qualquer momento. Quais DUAS estratégias de precificação devem ser combinadas para obter o MENOR custo possível mantendo a disponibilidade necessária? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Adquirir Compute Savings Plans com compromisso de 3 anos e pagamento Total Upfront para cobrir a linha de base estável das cargas de trabalho 24/7 em EC2, Fargate e Lambda.",
          "explanation": "Correto: O Compute Savings Plans de 3 anos com pagamento adiantado oferece a maior porcentagem de desconto para a carga de trabalho de base previsível 24/7."
        },
        {
          "id": "B",
          "text": "Utilizar instâncias On-Demand exclusivamente para todas as cargas de trabalho para garantir flexibilidade total.",
          "explanation": "Incorreto: Instâncias sob demanda cobram o preço de tabela cheio sem descontos."
        },
        {
          "id": "C",
          "text": "Comprar Instâncias Reservadas Padrão com prazo de 1 ano para as tarefas de processamento em lote.",
          "explanation": "Incorreto: Adquirir RIs para processamento em lote esporádico resulta em pagamento por capacidade ociosa quando os jobs não estão executando."
        },
        {
          "id": "D",
          "text": "Utilizar instâncias Spot para os bancos de dados de produção para maximizar a economia.",
          "explanation": "Incorreto: Instâncias Spot podem ser interrompidas com aviso prévio de 2 minutos e NUNCA devem ser usadas para bancos de dados de missão crítica."
        },
        {
          "id": "E",
          "text": "Utilizar instâncias Amazon EC2 Spot integradas a Auto Scaling groups com política de alocação Capacity-Optimized e seleção flexível de tipos de instâncias para as cargas de trabalho em lote tolerantes a falhas.",
          "explanation": "Correto: As instâncias EC2 Spot oferecem até 90% de desconto em relação ao preço sob demanda e são ideais para processamento em lote assíncrono e tolerante a interrupções com estratégia Capacity-Optimized."
        }
      ],
      "correctAnswers": ["A", "E"],
      "generalExplanation": "A estratégia ótima de FinOps na AWS combina Compute Savings Plans (descontos de até 66-72% para a capacidade básica previsível 24/7) com instâncias EC2 Spot (descontos de até 90% para processamento em lote descartável e tolerante a interrupções).",
      "referenceUrl": "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-optimized.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q020",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-3-continuous-improvement",
      "domainName": "Domain 3: Continuous Improvement for Existing Solutions",
      "services": ["AWS Fault Injection Simulator", "Amazon CloudWatch", "Amazon Route 53"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma instituição financeira internacional está validando a resiliência de sua arquitetura bancária de missão crítica antes de obter certificação regulatória. A equipe de engenharia do caos precisa executar testes automatizados e controlados em ambiente de pré-produção para simular: 1) Queda súbita de uma Availability Zone inteira; 2) Aumento de latência de rede no banco de dados; 3) Esgotamento de CPU em instâncias EC2 e nós EKS. Os testes devem parar automaticamente caso alarmes do CloudWatch indiquem que a taxa de erros da aplicação ultrapassou os limites aceitáveis de segurança. Qual serviço gerenciado da AWS deve ser utilizado?",
      "options": [
        {
          "id": "A",
          "text": "AWS Trusted Advisor com verificações de tolerância a falhas ativadas.",
          "explanation": "Incorreto: O Trusted Advisor apenas analisa configurações estáticas, não executando injeção ativa e controlada de falhas em tempo real."
        },
        {
          "id": "B",
          "text": "AWS Fault Injection Simulator (AWS FIS) com modelos de experimentos configurados com Stop Conditions vinculadas a alarmes do Amazon CloudWatch.",
          "explanation": "Correto: O AWS Fault Injection Simulator (FIS) é o serviço de engenharia do caos totalmente gerenciado da AWS para criar e executar experimentos controlados de falhas (interrupção de AZ, CPU stress, latência de rede) com condições de parada automática (Stop Conditions) para proteção de integridade."
        },
        {
          "id": "C",
          "text": "AWS Config com regras customizadas para desligar instâncias aleatoriamente.",
          "explanation": "Incorreto: O AWS Config é uma ferramenta de auditoria de conformidade de recursos e não possui controles de segurança de experimentos de caos."
        },
        {
          "id": "D",
          "text": "Amazon CloudWatch Synthetics com canaries que enviam cargas de tráfego excessivas.",
          "explanation": "Incorreto: CloudWatch Synthetics testa endpoints de aplicação simulando usuários, não injetando falhas na infraestrutura da AWS (queda de AZ, latência de disco, interrupção de nós)."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "O AWS Fault Injection Simulator (FIS) é o serviço nativo da AWS projetado para práticas de Engenharia do Caos (Chaos Engineering). Ele permite injetar falhas realistas e complexas (falha de AZ, degradação de banco, throttling de API) com mecanismos de segurança como Stop Conditions atreladas a alarmes do CloudWatch.",
      "referenceUrl": "https://docs.aws.amazon.com/fis/latest/userguide/what-is.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q021",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Database Migration Service", "Amazon RDS", "AWS Direct Connect"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação de saúde gerencia um banco de dados Microsoft SQL Server on-premises de 15 TB que sustenta o prontuário eletrônico de pacientes. A empresa precisa migrar esse banco de dados para o Amazon RDS for SQL Server (migração homogênea). O sistema opera 24 horas por dia e o comitê clínico estabeleceu que a janela máxima de indisponibilidade durante o cutover final não pode exceder 5 minutos. A empresa possui uma conexão Direct Connect de 10 Gbps. Qual abordagem atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Realizar backup completo nativo do SQL Server (.bak) no storage local, transferir o arquivo via AWS Snowball e restaurar no RDS.",
          "explanation": "Incorreto: O envio físico do Snowball e a restauração de 15 TB levam dias, acumulando uma defasagem de dados que violaria o tempo de indisponibilidade de 5 minutos."
        },
        {
          "id": "B",
          "text": "Desligar a aplicação on-premises, realizar exportação de dados via BCP e importar os dados via scripts no Amazon RDS.",
          "explanation": "Incorreto: Parar a aplicação on-premises para exportação e importação de 15 TB levaria de 12 a 24 horas de downtime, violando o limite de 5 minutos."
        },
        {
          "id": "C",
          "text": "Utilizar o AWS Database Migration Service (AWS DMS) com uma tarefa de Carga Completa (Full Load) e Replicação Contínua (Ongoing Replication / CDC) através da conexão AWS Direct Connect. Manter a sincronização em tempo real e redirecionar a conexão da aplicação para o endpoint do Amazon RDS durante a janela de cutover de 5 minutos.",
          "explanation": "Correto: O AWS DMS permite migração contínua com CDC (Change Data Capture) para o SQL Server, mantendo a base de destino no Amazon RDS sincronizada em tempo quase real enquanto a produção local continua ativa, viabilizando o cutover em menos de 5 minutos."
        },
        {
          "id": "D",
          "text": "Configurar replicação de instâncias com o AWS Application Migration Service (AWS MGN) para clonar o sistema operacional do servidor de banco.",
          "explanation": "Incorreto: O AWS MGN migra servidores no nível de bloco para instâncias EC2, não sendo o método recomendado para migrar bases de dados para o serviço gerenciado Amazon RDS."
        }
      ],
      "correctAnswers": ["C"],
      "generalExplanation": "Para migrar bancos de dados relacionais para o Amazon RDS com downtime mínimo (minutos), a metodologia recomendada é o AWS Database Migration Service (DMS) utilizando carga completa + Change Data Capture (CDC) contínuo.",
      "referenceUrl": "https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q022",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["VMware Cloud on AWS", "AWS Direct Connect"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma corporação global precisa desativar um datacenter de colocation terceirizado em menos de 60 dias devido ao término do contrato de locação física. O datacenter executa 800 máquinas virtuais complexas em clusters VMware vSphere com dependências legadas profundas e endereços IP estáticos codificados em código legado. A empresa não possui tempo hábil para converter os formatos de disco ou alterar as subnets e endereços IP das máquinas. Qual solução permite migrar essas 800 VMs para a nuvem da AWS no prazo exigido e sem alteração de endereçamento IP?",
      "options": [
        {
          "id": "A",
          "text": "Implantar o VMware Cloud on AWS (VMC) conectado ao datacenter via AWS Direct Connect com VMware HCX. Estender a rede de Camada 2 (Layer 2 Network Extension) e executar migrações em massa (HCX Bulk Migration / Live vMotion) preservando os mesmos endereços IP das VMs.",
          "explanation": "Correto: O VMware Cloud on AWS em conjunto com o VMware HCX permite estender a rede de Camada 2 entre o ambiente on-premises e a AWS, viabilizando migração a quente via vMotion e Bulk Migration de centenas de VMs sem reconfiguração de IP e sem conversão de formatos em prazos extremamente curtos."
        },
        {
          "id": "B",
          "text": "Utilizar o AWS Application Migration Service (MGN) para converter todas as VMs para instâncias nativas do Amazon EC2 e reconfigurar os IPs estáticos.",
          "explanation": "Incorreto: O MGN converte VMs para instâncias EC2 nativas, mas o enunciado especifica que não há tempo para alterar endereços IP codificados e que a infraestrutura deve permanecer em ambiente VMware."
        },
        {
          "id": "C",
          "text": "Exportar as 800 VMs para arquivos OVF e carregá-las no Amazon S3 utilizando o AWS DataSync.",
          "explanation": "Incorreto: Exportar e converter 800 OVFs manualmente é um processo lento e arriscado que não atende ao prazo de 60 dias."
        },
        {
          "id": "D",
          "text": "Contratar o AWS Snowmobile para transportar as máquinas virtuais em contêineres físicos.",
          "explanation": "Incorreto: O Snowmobile é para migração de dados de centenas de petabytes e não soluciona a extensão de rede L2 e compatibilidade VMware exigidas."
        }
      ],
      "correctAnswers": ["A"],
      "generalExplanation": "O VMware Cloud on AWS (VMC) com VMware HCX é a estratégia 'Relocate' ideal para migrações urgentes em massa de ambientes VMware vSphere, permitindo estender redes L2 e migrar centenas de VMs sem alterações de IP, SO ou formatos de disco.",
      "referenceUrl": "https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-vmware-cloud-on-aws/welcome.html",
      "difficulty": "hard"
    },
    {
      "id": "sim2-q023",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Storage Gateway", "Amazon S3"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Um escritório de advocacia internacional possui mais de 2 PB de backups de processos jurídicos e evidências digitais gravados em fitas magnéticas físicas (LTO-6) em um sistema de robô de fitas (Tape Library) on-premises. A manutenção do hardware de fitas e o armazenamento físico externo geram custos anuais de US$ 80.000. A empresa deseja eliminar o hardware físico de fitas, mas precisa continuar utilizando seu software de backup corporativo existente (compatível com iSCSI VTL) sem alterar seus procedimentos operacionais de gravação. Os dados devem ser armazenados na classe de menor custo da nuvem. Qual solução atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Implantar o AWS Storage Gateway File Gateway e reescrever todos os scripts de backup para gravar em compartilhamentos NFS.",
          "explanation": "Incorreto: O File Gateway emite compartilhamentos NFS/SMB, exigindo reconfigurar e alterar o software de backup existente que opera com fitas iSCSI VTL."
        },
        {
          "id": "B",
          "text": "Substituir o software de backup pelo AWS Backup e instalar agentes em todos os servidores on-premises.",
          "explanation": "Incorreto: A empresa exigiu manter o software de backup existente e não substituir toda a infraestrutura de agentes."
        },
        {
          "id": "C",
          "text": "Criar volumes Amazon EBS io2 e anexá-los via iSCSI às estações de backup on-premises.",
          "explanation": "Incorreto: Volumes EBS não são acessíveis diretamente pela rede on-premises via iSCSI nativo e têm custo muito superior ao arquivamento em S3 Glacier."
        },
        {
          "id": "D",
          "text": "Implantar o AWS Storage Gateway Tape Gateway (VTL) como máquina virtual on-premises. Conectar o software de backup existente à Virtual Tape Library via iSCSI e configurar o arquivamento automático das fitas virtuais no Amazon S3 Glacier Flexible Recovery e Amazon S3 Glacier Deep Archive.",
          "explanation": "Correto: O AWS Tape Gateway expõe uma biblioteca de fitas virtuais (VTL) baseada em iSCSI compatível com os principais softwares de backup do mercado (Veeam, Commvault, Veritas). Ele elimina as fitas físicas e arquiva fitas virtuais diretamente no S3 Glacier e S3 Glacier Deep Archive com o menor custo do mercado."
        }
      ],
      "correctAnswers": ["D"],
      "generalExplanation": "O AWS Storage Gateway Tape Gateway substitui bibliotecas de fitas físicas on-premises por fitas virtuais na nuvem sem exigir qualquer alteração no software de backup corporativo existente, arquivando dados com extrema economia no Amazon S3 Glacier e S3 Glacier Deep Archive.",
      "referenceUrl": "https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q024",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Lambda", "AWS Step Functions", "Amazon EventBridge"],
      "type": "single",
      "requiredChoices": 1,
      "statement": "Uma rede de varejo está modernizando uma aplicação monolítica legada de processamento de pedidos on-premises. A liderança técnica adotou a estratégia 'Refactor' (Rearchitect) para transformar o monólito em microsserviços desacoplados e orientados a eventos na AWS. A arquitetura deve atender a: 1) Eliminar o gerenciamento de servidores, sistemas operacionais e clusters de orquestração; 2) Permitir que múltiplos sistemas assinem eventos de novos pedidos de forma assíncrona com filtragem baseada em atributos (ex: valor do pedido, região); 3) Orquestrar fluxos de trabalho com múltiplas etapas e tratamento de exceções. Qual arquitetura atende a esses requisitos?",
      "options": [
        {
          "id": "A",
          "text": "Implantar as aplicações em instâncias EC2 em Auto Scaling com balanceadores de carga ALB e mensageria via Apache Kafka autogerenciado em EC2.",
          "explanation": "Incorreto: Utilizar EC2 e Kafka autogerenciado exige alto esforço de administração de servidores e patches, violando a exigência serverless."
        },
        {
          "id": "B",
          "text": "Utilizar o Amazon EventBridge como barramento central de eventos para publicação e filtragem de eventos de pedidos, acionando funções AWS Lambda para execução de microsserviços individuais e o AWS Step Functions para orquestração de fluxos complexos de processamento.",
          "explanation": "Correto: A combinação de Amazon EventBridge (barramento de eventos serverless com roteamento/filtragem declarativa) + AWS Lambda (computação serverless) + AWS Step Functions (orquestração de fluxos com estado) é a arquitetura moderna serverless de referência para decomposição de monólitos na AWS."
        },
        {
          "id": "C",
          "text": "Utilizar o Amazon EKS com nós EC2 e RabbitMQ instalado em contêineres.",
          "explanation": "Incorreto: Manter clusters Kubernetes e RabbitMQ requer gerenciamento de servidores e não é um modelo serverless puro."
        },
        {
          "id": "D",
          "text": "Configurar o Amazon Simple Workflow Service (SWF) conectado a servidores on-premises via VPN.",
          "explanation": "Incorreto: O Amazon SWF é um serviço legado que exige workers em servidores gerenciados manualmente."
        }
      ],
      "correctAnswers": ["B"],
      "generalExplanation": "Para modernizações do tipo Refactor voltadas a arquiteturas orientadas a eventos (Event-Driven Architecture) totalmente serverless, a combinação de Amazon EventBridge (barramento de eventos com regras de roteamento) com AWS Lambda (processamento de lógica de negócio) e AWS Step Functions (orquestração de fluxos complexos) é o padrão de referência da AWS.",
      "referenceUrl": "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html",
      "difficulty": "medium"
    },
    {
      "id": "sim2-q025",
      "examId": "SAP-C02-SIM-2",
      "domainId": "domain-4-migration-modernization",
      "domainName": "Domain 4: Accelerate Workload Migration and Modernization",
      "services": ["AWS Application Discovery Service", "AWS Migration Hub", "Migration Evaluator"],
      "type": "multiple",
      "requiredChoices": 2,
      "statement": "Uma corporação financeira planeja migrar mais de 200 servidores e 50 aplicações interdependentes hospedadas em seu datacenter on-premises para a AWS. Antes de iniciar a migração técnica, a diretoria exige: 1) Descobrir e mapear automaticamente todas as conexões de rede ativas e dependências entre servidores; 2) Coletar dados históricos reais de utilização de CPU, memória e disco para dimensionamento correto (Right-Sizing) e projeção de custos do Total Cost of Ownership (TCO) na AWS; 3) Agrupar os servidores em ondas de migração (Migration Waves) e acompanhar o progresso em um painel centralizado. Quais DUAS ferramentas da AWS devem ser utilizadas nessa fase de descoberta e planejamento? (Escolha duas.)",
      "options": [
        {
          "id": "A",
          "text": "Instalar o AWS Application Migration Service (MGN) em modo de produção imediato para clonar os discos.",
          "explanation": "Incorreto: O AWS MGN é uma ferramenta de execução de migração (Rehost), não uma ferramenta de inventário, mapeamento de dependências e estimativa de TCO da fase de planejamento."
        },
        {
          "id": "B",
          "text": "Utilizar o AWS DataSync para medir o throughput de disco dos servidores locais.",
          "explanation": "Incorreto: O DataSync é um serviço de transferência de dados, não de inventário e planejamento de ondas de migração."
        },
        {
          "id": "C",
          "text": "Instalar o AWS Application Discovery Agent (AWS Application Discovery Service) nos servidores locais para coletar dados detalhados de inventário de sistema, métricas de desempenho de recursos e mapeamento de dependências de comunicação de rede entre servidores.",
          "explanation": "Correto: O AWS Application Discovery Agent é executado nos servidores locais para capturar dependências de rede (endereços IP e portas de comunicação entre aplicações) e dados granulares de utilização de CPU/RAM/disco para planejar as ondas de migração."
        },
        {
          "id": "D",
          "text": "Utilizar o AWS Migration Hub e o AWS Migration Evaluator (antigo TSO Logic) para analisar os dados coletados, gerar estimativas de custos de TCO comparativas na AWS e organizar os servidores em ondas de migração (Migration Waves) com rastreamento centralizado.",
          "explanation": "Correto: O AWS Migration Evaluator produz business cases e projeções financeiras detalhadas de TCO com right-sizing, enquanto o AWS Migration Hub permite agrupar servidores em ondas e monitorar o progresso das ferramentas de migração em um painel único."
        },
        {
          "id": "E",
          "text": "Utilizar o AWS Schema Conversion Tool (SCT) para mapear os servidores de aplicação web.",
          "explanation": "Incorreto: O AWS SCT é exclusivo para conversão de schemas de bancos de dados e data warehouses, não para mapeamento de dependências de infraestrutura de servidores."
        }
      ],
      "correctAnswers": ["C", "D"],
      "generalExplanation": "Na fase de avaliação e planejamento de migração (Assess & Plan), o AWS Application Discovery Service (com Discovery Agent) mapeia o inventário e dependências de rede entre servidores. O AWS Migration Evaluator e o AWS Migration Hub utilizam esses dados para construir o business case de TCO e organizar a migração em ondas estruturadas.",
      "referenceUrl": "https://docs.aws.amazon.com/migrationhub/latest/ug/whatis.html",
      "difficulty": "hard"
    }
  ]
}

def main():
    sim1_path = "src/data/exams/sap-c02-sim-1.json"
    sim2_path = "src/data/exams/sap-c02-sim-2.json"
    
    with open(sim1_path, "w", encoding="utf-8") as f:
        json.dump(SIM1_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ Gerado {sim1_path} com {len(SIM1_DATA['questions'])} questões.")

    with open(sim2_path, "w", encoding="utf-8") as f:
        json.dump(SIM2_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ Gerado {sim2_path} com {len(SIM2_DATA['questions'])} questões.")

if __name__ == "__main__":
    main()
