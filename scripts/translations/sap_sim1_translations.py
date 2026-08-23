"""
High quality, verified Portuguese (PT-BR) and Spanish (ES) translations for SAP-C02 Mock Exam 1.
Questions: sap-sim1-q001 to sap-sim1-q025
"""

TRANSLATIONS = {
    "sap-sim1-q001": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Um conglomerado global opera 300 contas AWS no AWS Organizations com múltiplas Unidades Organizacionais (OUs) aninhadas. A equipe central de segurança exige que todos os usuários e roles do IAM das contas-membro sejam estritamente impedidos de criar buckets do Amazon S3 não criptografados ou desabilitar o AWS CloudTrail em qualquer região da AWS, permitindo ao mesmo tempo que pipelines de implantação automatizados específicos na OU de Infraestrutura gerenciem políticas de chaves KMS personalizadas sem interrupções. Além disso, a solução deve impedir que os administradores das contas-membro (incluindo o usuário root) contornem esses controles. Qual arquitetura impõe esses requisitos com a MENOR sobrecarga operacional?",
            "options": [
                {
                    "id": "A",
                    "text": "Aplicar Service Control Policies (SCPs) com condições de Deny explícitas nos níveis intermediários de OU para criptografia do S3 e proteção do CloudTrail, aplicando uma SCP dedicada à OU de Infraestrutura que mantém as permissões de gerenciamento do KMS intactas.",
                    "explanation": "Correto: As SCPs estabelecem limites de proteção (guardrails) entre as OUs sem impactar as contas em OUs irmãs. A aplicação de SCPs granulares nas OUs intermediárias impõe controles preventivos nas contas-membro (incluindo o usuário root) sem restringir as operações do KMS na OU de Infraestrutura."
                },
                {
                    "id": "B",
                    "text": "Anexar uma Service Control Policy (SCP) à OU Raiz que nega explicitamente s3:CreateBucket sem cabeçalhos de criptografia e cloudtrail:StopLogging/DeleteTrail, excluindo a OU de Infraestrutura ao posicioná-la fora da hierarquia Raiz.",
                    "explanation": "Incorreto: Todas as contas e OUs no AWS Organizations devem residir sob o contêiner Raiz (Root); uma OU não pode ser posicionada fora da Raiz."
                },
                {
                    "id": "C",
                    "text": "Implantar IAM Permission Boundaries em cada role do IAM em todas as 300 contas usando runbooks do AWS Systems Manager Automation e agendar verificações diárias de conformidade com o AWS Config.",
                    "explanation": "Incorreto: As Permission Boundaries não se aplicam ao usuário root nas contas-membro e exigem manutenção contínua massiva em comparação com SCPs declarativas."
                },
                {
                    "id": "D",
                    "text": "Implantar AWS CloudFormation StackSets em todas as contas para provisionar políticas de Deny do IAM e configurar o AWS WAF em todos os endpoints regionais.",
                    "explanation": "Incorreto: Os administradores de contas-membro podem modificar ou excluir políticas do IAM criadas pelo CloudFormation StackSets, falhando no requisito de impedir o contorno dos controles."
                }
            ],
            "generalExplanation": "As Service Control Policies (SCPs) no AWS Organizations impõem limites de proteção (guardrails) que se aplicam a todos os principais (incluindo o usuário root da conta) nas contas-membro, sem a necessidade de modificar políticas individuais do IAM."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un conglomerado global opera 300 cuentas de AWS en AWS Organizations con múltiples Unidades Organizativas (OUs) anidadas. El equipo central de seguridad requiere que todos los usuarios y roles de IAM de las cuentas miembro tengan estrictamente prohibido crear buckets de Amazon S3 sin cifrar o deshabilitar AWS CloudTrail en cualquier región de AWS, permitiendo al mismo tiempo que canales de implementación automatizados específicos en la OU de Infraestructura administren políticas de claves KMS personalizadas sin interrupciones. Además, la solución debe evitar que los administradores de las cuentas miembro (incluido el usuario root) eludan estos controles. ¿Qué arquitectura impone estos requisitos con la MENOR sobrecarga operativa?",
            "options": [
                {
                    "id": "A",
                    "text": "Aplicar Service Control Policies (SCPs) con condiciones de Deny explícitas en los niveles intermedios de OU para el cifrado de S3 y la protección de CloudTrail, aplicando una SCP dedicada a la OU de Infraestructura que mantiene intactos los permisos de administración de KMS.",
                    "explanation": "Correcto: Las SCPs establecen barreras de protección (guardrails) en todas las OUs sin afectar a las cuentas de OUs hermanas. La aplicación de SCPs granulares en OUs intermedias impone controles preventivos en las cuentas miembro (incluido el usuario root) sin restringir las operaciones de KMS en la OU de Infraestructura."
                },
                {
                    "id": "B",
                    "text": "Adjuntar una Service Control Policy (SCP) a la OU Raíz que niega explícitamente s3:CreateBucket sin encabezados de cifrado y cloudtrail:StopLogging/DeleteTrail, excluyendo la OU de Infraestructura al colocarla fuera de la jerarquía Raíz.",
                    "explanation": "Incorrecto: Todas las cuentas y OUs en AWS Organizations deben residir bajo el contenedor Raíz (Root); una OU no puede colocarse fuera de la Raíz."
                },
                {
                    "id": "C",
                    "text": "Implementar IAM Permission Boundaries en cada rol de IAM en todas las 300 cuentas mediante runbooks de AWS Systems Manager Automation y programar análisis diarios de cumplimiento con AWS Config.",
                    "explanation": "Incorrecto: Las Permission Boundaries no se aplican al usuario root en las cuentas miembro y requieren un mantenimiento continuo masivo en comparación con las SCPs declarativas."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS CloudFormation StackSets en todas las cuentas para aprovisionar políticas de Deny de IAM y configurar AWS WAF en todos los endpoints regionales.",
                    "explanation": "Incorrecto: Los administradores de cuentas miembro pueden modificar o eliminar políticas de IAM creadas por CloudFormation StackSets, no cumpliendo con el requisito de evitar la elusión de controles."
                }
            ],
            "generalExplanation": "Las Service Control Policies (SCPs) en AWS Organizations aplican barreras de protección (guardrails) que afectan a todos los principales (incluido el usuario root de la cuenta) en las cuentas miembro sin necesidad de modificar políticas individuales de IAM."
        }
    },
    "sap-sim1-q002": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa com 50 VPCs em múltiplas contas AWS usa um AWS Transit Gateway para conectividade inter-VPC e acesso à internet. A arquitetura de segurança exige que todo o tráfego leste-oeste (inter-VPC) e norte-sul (saída para a internet) passe por uma VPC de inspeção centralizada contendo firewalls stateful do AWS Network Firewall. Durante os testes iniciais, as sessões TCP entre VPCs estão caindo de forma intermitente devido ao roteamento assimétrico entre Zonas de Disponibilidade. Como o arquiteto de redes deve resolver esse problema?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Appliance Mode do Transit Gateway no anexo de VPC (VPC attachment) para a VPC de inspeção em todas as Zonas de Disponibilidade.",
                    "explanation": "Correto: Habilitar o Appliance Mode no anexo de VPC do Transit Gateway garante que o tráfego bidirecional dentro de um fluxo seja roteado pela mesma Zona de Disponibilidade e Elastic Network Interface (ENI), prevenindo o roteamento assimétrico através de firewalls stateful."
                },
                {
                    "id": "B",
                    "text": "Configurar o roteamento Equal-Cost Multi-Path (ECMP) nas tabelas de rotas do Transit Gateway com um limite máximo de caminho de 1.",
                    "explanation": "Incorreto: O ECMP opera na camada BGP/Direct Connect e não garante simetria de Zona de Disponibilidade para anexos de VPC."
                },
                {
                    "id": "C",
                    "text": "Substituir o AWS Network Firewall por um Application Load Balancer em cada VPC spoke.",
                    "explanation": "Incorreto: ALBs não podem inspecionar tráfego não HTTP nem realizar inspeção geral de pacotes de Camada 3/4 leste-oeste."
                },
                {
                    "id": "D",
                    "text": "Implantar uma malha de conexões VPC Peering entre todas as 50 VPCs e rotear o tráfego diretamente.",
                    "explanation": "Incorreto: O VPC Peering cria uma complexidade exponencial (N*(N-1)/2) e contorna a VPC de inspeção centralizada."
                }
            ],
            "generalExplanation": "O Appliance Mode do Transit Gateway garante que os fluxos de tráfego simétricos de uma determinada sessão de rede sejam direcionados para a mesma Zona de Disponibilidade onde reside o firewall stateful."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa con 50 VPCs en múltiples cuentas de AWS utiliza un AWS Transit Gateway para la conectividad inter-VPC e internet. La arquitectura de seguridad exige que todo el tráfico este-oeste (inter-VPC) y norte-sur (salida a internet) pase a través de una VPC de inspección centralizada que contiene firewalls con estado (stateful) de AWS Network Firewall. Durante las pruebas iniciales, las sesiones TCP entre VPCs se caen de forma intermitente debido al enrutamiento asimétrico entre Zonas de Disponibilidad. ¿Cómo debe resolver este problema el arquitecto de redes?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar el Appliance Mode de Transit Gateway en el adjunto de VPC (VPC attachment) para la VPC de inspección en todas las Zonas de Disponibilidad.",
                    "explanation": "Correcto: Habilitar Appliance Mode en el adjunto de VPC de Transit Gateway garantiza que el tráfico bidireccional dentro de un flujo se enrute a través de la misma Zona de Disponibilidad y Elastic Network Interface (ENI), evitando el enrutamiento asimétrico a través de firewalls con estado."
                },
                {
                    "id": "B",
                    "text": "Configurar el enrutamiento Equal-Cost Multi-Path (ECMP) en las tablas de rutas de Transit Gateway con un límite máximo de ruta de 1.",
                    "explanation": "Incorrecto: ECMP opera en la capa BGP/Direct Connect y no garantiza la simetría de Zona de Disponibilidad para los adjuntos de VPC."
                },
                {
                    "id": "C",
                    "text": "Reemplazar AWS Network Firewall con un Application Load Balancer en cada VPC spoke.",
                    "explanation": "Incorrecto: Los ALBs no pueden inspeccionar tráfico no HTTP ni manejar la inspección general de paquetes de Capa 3/4 de tráfico este-oeste."
                },
                {
                    "id": "D",
                    "text": "Implementar una malla de conexiones de VPC Peering entre todas las 50 VPCs y enrutar el tráfico directamente.",
                    "explanation": "Incorrecto: VPC Peering crea una complejidad exponencial (N*(N-1)/2) y elude la VPC de inspección centralizada."
                }
            ],
            "generalExplanation": "El Appliance Mode de Transit Gateway garantiza que los flujos de tráfico simétricos para una sesión de red determinada se dirijan a la misma Zona de Disponibilidad donde reside el firewall con estado."
        }
    },
    "sap-sim1-q003": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa multinacional deseja simplificar o gerenciamento de rede VPC em 80 contas de desenvolvimento. A equipe de rede deseja gerenciar centralmente sub-redes, tabelas de rotas e NAT Gateways em uma conta dedicada de Hub de Rede, permitindo que os desenvolvedores nas contas-membro iniciem instâncias EC2 e tarefas ECS dentro de sub-redes privadas compartilhadas sem ter controle administrativo sobre a configuração de rede subjacente. Qual solução atinge esse objetivo com a MENOR complexidade operacional?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Resource Access Manager (AWS RAM) para compartilhar sub-redes da VPC centralizada na conta Hub de Rede com o AWS Organizations ou OUs específicas.",
                    "explanation": "Correto: O compartilhamento de VPC via AWS RAM permite a propriedade centralizada da rede, enquanto as contas participantes podem executar recursos de computação em sub-redes compartilhadas sem modificar as estruturas de rede."
                },
                {
                    "id": "B",
                    "text": "Criar VPCs em cada conta-membro e estabelecer anexos de VPC do AWS Transit Gateway para a conta central Hub de Rede.",
                    "explanation": "Incorreto: A criação de VPCs individuais em 80 contas multiplica o gerenciamento de VPCs, a alocação de blocos CIDR e os custos de infraestrutura de NAT Gateways."
                },
                {
                    "id": "C",
                    "text": "Configurar um modelo do AWS CloudFormation que implanta VPCs e roles do IAM idênticos em todas as contas, sincronizando rotas via AWS Lambda.",
                    "explanation": "Incorreto: A sincronização personalizada com Lambda adiciona alto risco de falhas e não fornece uma propriedade de rede unificada."
                },
                {
                    "id": "D",
                    "text": "Criar VPC Peering entre a conta Hub de Rede e todas as 80 contas-membro com resolução de DNS habilitada.",
                    "explanation": "Incorreto: O VPC Peering não permite que os participantes compartilhem sub-redes diretamente e exige o gerenciamento de 80 conexões de emparelhamento individuais."
                }
            ],
            "generalExplanation": "O compartilhamento de VPC (via AWS RAM) permite que múltiplas contas AWS criem recursos de aplicação (EC2, ECS, RDS) em sub-redes VPC compartilhadas e gerenciadas centralmente dentro de uma organização."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa multinacional desea simplificar la administración de redes VPC en 80 cuentas de desarrollo. El equipo de redes desea administrar de forma centralizada subredes, tablas de rutas y NAT Gateways en una cuenta dedicada de Hub de Red, permitiendo al mismo tiempo que los desarrolladores de las cuentas miembro inicien instancias EC2 y tareas ECS dentro de subredes privadas compartidas sin tener control administrativo sobre la configuración de red subyacente. ¿Qué solución logra esto con la MENOR complejidad operativa?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar AWS Resource Access Manager (AWS RAM) para compartir subredes de la VPC centralizada en la cuenta Hub de Red con la organización de AWS Organizations o OUs específicas.",
                    "explanation": "Correcto: El uso compartido de VPC a través de AWS RAM permite la propiedad centralizada de la red, mientras que las cuentas participantes pueden lanzar recursos de cómputo en subredes compartidas sin modificar las construcciones de red."
                },
                {
                    "id": "B",
                    "text": "Crear VPCs en cada cuenta miembro y establecer adjuntos de VPC de AWS Transit Gateway a la cuenta central Hub de Red.",
                    "explanation": "Incorrecto: Crear VPCs individuales en 80 cuentas multiplica la gestión de VPCs, la asignación de CIDR y los costos de infraestructura de NAT Gateways."
                },
                {
                    "id": "C",
                    "text": "Configurar una plantilla de AWS CloudFormation que implemente VPCs y roles de IAM idénticos en todas las cuentas, sincronizando rutas a través de AWS Lambda.",
                    "explanation": "Incorrecto: La sincronización personalizada mediante Lambda agrega un alto riesgo de fallos y no proporciona una propiedad de red unificada."
                },
                {
                    "id": "D",
                    "text": "Crear VPC Peering entre la cuenta Hub de Red y las 80 cuentas miembro con resolución de DNS habilitada.",
                    "explanation": "Incorrecto: VPC Peering no permite a los participantes compartir subredes directamente y requiere administrar 80 conexiones de interconexión individuales."
                }
            ],
            "generalExplanation": "El uso compartido de VPC (a través de AWS RAM) permite que múltiples cuentas de AWS creen recursos de aplicaciones (EC2, ECS, RDS) en subredes de VPC compartidas y administradas centralmente dentro de una organización."
        }
    },
    "sap-sim1-q004": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma instituição financeira possui duas conexões dedicadas de 10 Gbps do AWS Direct Connect terminando em dois locais diferentes do Direct Connect para alta resiliência. O data center on-premises precisa se conectar a 120 VPCs em 4 Regiões AWS. A arquitetura exige roteamento BGP ativo/passivo sobre a rede global da AWS com failover automático, criptografia MACsec nas interconexões dedicadas e sobrecarga mínima de gerenciamento de pares BGP. Qual combinação de serviços o arquiteto deve implantar?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar Private Virtual Interfaces (Private VIFs) diretamente das conexões do Direct Connect para cada uma das 120 VPCs em todas as 4 regiões.",
                    "explanation": "Incorreto: As conexões do Direct Connect suportam um máximo de 50 Private VIFs e não escalam para 120 VPCs em múltiplas regiões sem um Direct Connect Gateway."
                },
                {
                    "id": "B",
                    "text": "Implantar túneis VPN IPsec pela internet pública para cada VPC e terminá-los em virtual private gateways.",
                    "explanation": "Incorreto: As VPNs IPsec padrão têm um limite de largura de banda de 1,25 Gbps e não aproveitam a infraestrutura dedicada de 10 Gbps do Direct Connect."
                },
                {
                    "id": "C",
                    "text": "Provisionar um Direct Connect Gateway, associá-lo a AWS Transit Gateways regionais em cada Região AWS via Transit Virtual Interfaces (Transit VIFs), habilitar MACsec nas portas do Direct Connect e usar BGP AS-Path prepending para failover.",
                    "explanation": "Correto: O Direct Connect Gateway com Transit VIFs conectado a Transit Gateways regionais escala para centenas de VPCs entre regiões, suporta MACsec em links dedicados de 10G/100G e usa BGP AS-Path prepending para seleção de caminho ativo/passivo."
                },
                {
                    "id": "D",
                    "text": "Anexar conexões do Direct Connect diretamente a um AWS Network Load Balancer em cada região.",
                    "explanation": "Incorreto: O Direct Connect se conecta na Camada 2/3 por meio de VIFs e Direct Connect Gateways, e não diretamente a NLBs."
                }
            ],
            "generalExplanation": "O uso de um Direct Connect Gateway com Transit VIFs anexado a AWS Transit Gateways regionais permite conectividade híbrida escalável multirregião e multi-VPC com criptografia MACsec em nível de hardware."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una institución financiera tiene dos conexiones dedicadas de 10 Gbps de AWS Direct Connect que terminan en dos ubicaciones diferentes de Direct Connect para alta resiliencia. El centro de datos local (on-premises) necesita conectarse a 120 VPCs en 4 Regiones de AWS. La arquitectura requiere enrutamiento BGP activo/pasivo sobre la red global de AWS con conmutación por error automática, cifrado MACsec en las interconexiones dedicadas y una sobrecarga mínima de gestión de pares BGP. ¿Qué combinación de servicios debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear Private Virtual Interfaces (Private VIFs) directamente desde las conexiones de Direct Connect a cada una de las 120 VPCs en las 4 regiones.",
                    "explanation": "Incorrecto: Las conexiones de Direct Connect admiten un máximo de 50 Private VIFs y no escalan a 120 VPCs en múltiples regiones sin un Direct Connect Gateway."
                },
                {
                    "id": "B",
                    "text": "Implementar túneles VPN IPsec a través de internet pública hacia cada VPC y terminarlos en virtual private gateways.",
                    "explanation": "Incorrecto: Las VPNs IPsec estándar tienen un límite de ancho de banda de 1.25 Gbps y no utilizan la infraestructura dedicada de 10 Gbps de Direct Connect."
                },
                {
                    "id": "C",
                    "text": "Aprovisionar un Direct Connect Gateway, asociarlo con AWS Transit Gateways regionales en cada Región de AWS mediante Transit Virtual Interfaces (Transit VIFs), habilitar MACsec en los puertos de Direct Connect y usar BGP AS-Path prepending para la conmutación por error.",
                    "explanation": "Correcto: Direct Connect Gateway con Transit VIFs conectado a Transit Gateways regionales escala a cientos de VPCs entre regiones, admite MACsec en enlaces dedicados de 10G/100G y utiliza BGP AS-Path prepending para la selección de rutas activa/pasiva."
                },
                {
                    "id": "D",
                    "text": "Adjuntar conexiones de Direct Connect directamente a un AWS Network Load Balancer en cada región.",
                    "explanation": "Incorrecto: Direct Connect se conecta en la Capa 2/3 a través de VIFs y Direct Connect Gateways, no directamente a los NLBs."
                }
            ],
            "generalExplanation": "El uso de un Direct Connect Gateway con Transit VIFs conectado a AWS Transit Gateways regionales permite una conectividad híbrida escalable entre múltiples VPCs y regiones con cifrado MACsec a nivel de hardware."
        }
    },
    "sap-sim1-q005": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa está migrando 5.000 usuários corporativos do Microsoft Active Directory local para a AWS. A solução deve fornecer acesso Single Sign-On (SSO) ao Console de Gerenciamento da AWS em 150 contas AWS, suportar autenticação multifator (MFA) e integrar-se a um provedor de identidade SAML 2.0 externo (Okta) sem sincronizar senhas de usuários na AWS. Qual solução atende a esses requisitos com o MENOR esforço administrativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o AWS IAM Identity Center (AWS Single Sign-On), configurar a federação SAML 2.0 com o Okta como provedor de identidade externo, habilitar o provisionamento automático de usuários SCIM e atribuir conjuntos de permissões (permission sets) a grupos em todas as contas AWS.",
                    "explanation": "Correto: O AWS IAM Identity Center integra-se com IdPs externos (Okta, Azure AD) via SAML 2.0 e SCIM para fornecer SSO e MFA centralizados em múltiplas contas sem a necessidade de sincronizar senhas."
                },
                {
                    "id": "B",
                    "text": "Criar usuários do IAM em cada uma das 150 contas AWS e configurar políticas de senha com dispositivos MFA virtuais.",
                    "explanation": "Incorreto: Criar e gerenciar 5.000 usuários do IAM em 150 contas separadas (750.000 credenciais) gera uma sobrecarga administrativa inviável."
                },
                {
                    "id": "C",
                    "text": "Implantar o AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) em cada conta AWS e configurar relações de confiança de floresta bidirecionais.",
                    "explanation": "Incorreto: A implantação do Managed AD em 150 contas adiciona custos imensos de licenciamento e grande complexidade de manutenção."
                },
                {
                    "id": "D",
                    "text": "Implantar pools de usuários do Amazon Cognito em uma conta de segurança central e escrever triggers Lambda personalizados para cada sessão da AWS CLI.",
                    "explanation": "Incorreto: Os pools de usuários do Cognito são projetados para aplicações web/mobile voltadas para clientes finais, e não para SSO corporativo de força de trabalho em múltiplas contas AWS."
                }
            ],
            "generalExplanation": "O AWS IAM Identity Center (sucessor do AWS SSO) fornece gerenciamento centralizado de acesso da força de trabalho em contas AWS e aplicativos em nuvem com integração nativa com SAML 2.0 e SCIM."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa está migrando 5.000 usuarios corporativos desde Microsoft Active Directory local a AWS. La solución debe proporcionar acceso de inicio de sesión único (Single Sign-On - SSO) a la Consola de administración de AWS en 150 cuentas de AWS, admitir autenticación multifactor (MFA) e integrarse con un proveedor de identidad SAML 2.0 externo (Okta) sin sincronizar las contraseñas de los usuarios en AWS. ¿Qué solución satisface estos requisitos con el MENOR esfuerzo administrativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar AWS IAM Identity Center (AWS Single Sign-On), configurar la federación SAML 2.0 con Okta como proveedor de identidad externo, habilitar el aprovisionamiento automático de usuarios SCIM y asignar conjuntos de permisos (permission sets) a grupos en todas las cuentas de AWS.",
                    "explanation": "Correcto: AWS IAM Identity Center se integra con IdPs externos (Okta, Azure AD) a través de SAML 2.0 y SCIM para proporcionar SSO y MFA centralizados en múltiples cuentas sin sincronizar contraseñas."
                },
                {
                    "id": "B",
                    "text": "Crear usuarios de IAM en cada una de las 150 cuentas de AWS y configurar directivas de contraseñas con dispositivos MFA virtuales.",
                    "explanation": "Incorrecto: Crear y administrar 5.000 usuarios de IAM en 150 cuentas independientes (750.000 credenciales) representa una carga administrativa inasumible."
                },
                {
                    "id": "C",
                    "text": "Implementar AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) en cada cuenta de AWS y configurar relaciones de confianza de bosque bidireccionales.",
                    "explanation": "Incorrecto: Implementar Managed AD en 150 cuentas agrega inmensos costos de licencias y complejidad de mantenimiento."
                },
                {
                    "id": "D",
                    "text": "Implementar grupos de usuarios de Amazon Cognito en una cuenta de seguridad central y escribir triggers de Lambda personalizados para cada sesión de AWS CLI.",
                    "explanation": "Incorrecto: Los grupos de usuarios de Cognito están diseñados para aplicaciones web/móviles orientadas al cliente final, no para SSO corporativo en múltiples cuentas de AWS."
                }
            ],
            "generalExplanation": "AWS IAM Identity Center (sucesor de AWS SSO) proporciona administración centralizada del acceso de la fuerza laboral en cuentas de AWS y aplicaciones en la nube con integración transparente de SAML 2.0 y SCIM."
        }
    },
    "sap-sim1-q006": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Um serviço de análise em execução na Conta A precisa ler conjuntos de dados de clientes criptografados em um bucket do Amazon S3 localizado na Conta B. Os objetos na Conta B são criptografados com uma chave gerenciada pelo cliente (Customer Managed Key - CMK) do AWS KMS localizada na Conta B. Qual configuração é necessária para conceder à role do IAM na Conta A permissão para descriptografar e ler os objetos do S3?",
            "options": [
                {
                    "id": "A",
                    "text": "Exportar a chave privada do KMS da Conta B e importá-la em uma chave do AWS KMS na Conta A.",
                    "explanation": "Incorreto: As chaves gerenciadas pelo cliente do KMS não são exportáveis; o AWS KMS gerencia o material de chave simétrica dentro de HSMs."
                },
                {
                    "id": "B",
                    "text": "Alterar a criptografia no bucket S3 na Conta B para AWS Managed Key (aws/s3), que permite automaticamente todas as roles do IAM entre contas.",
                    "explanation": "Incorreto: A chave gerenciada pela AWS padrão (aws/s3) não pode ser compartilhada entre contas AWS diferentes; o KMS entre contas exige Customer Managed Keys."
                },
                {
                    "id": "C",
                    "text": "Configurar uma ACL do S3 no bucket da Conta B concedendo permissões de leitura pública.",
                    "explanation": "Incorreto: As ACLs não concedem permissões de descriptografia do KMS, e tornar o bucket público cria uma grave exposição de segurança."
                },
                {
                    "id": "D",
                    "text": "Anexar uma política do IAM à role na Conta A concedendo kms:Decrypt e s3:GetObject, configurar a política de bucket do S3 na Conta B para permitir o ARN da role da Conta A e atualizar a política de chave do KMS na Conta B para permitir que o ARN da role da Conta A (ou o root da Conta A) execute kms:Decrypt.",
                    "explanation": "Correto: O acesso entre contas ao KMS e ao S3 requer delegação explícita: a política de identidade do IAM na Conta A, a política de recursos do bucket S3 na Conta B e a política de chaves do KMS na Conta B devem permitir a ação."
                }
            ],
            "generalExplanation": "O acesso entre contas a objetos do S3 criptografados com KMS requer permissões em três locais: a política do IAM do consumidor, a política do bucket do S3 de destino e a política de chaves do KMS de destino."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un servicio de análisis que se ejecuta en la Cuenta A necesita leer conjuntos de datos de clientes cifrados de un bucket de Amazon S3 ubicado en la Cuenta B. Los objetos en la Cuenta B están cifrados con una clave administrada por el cliente (Customer Managed Key - CMK) de AWS KMS ubicada en la Cuenta B. ¿Qué configuración se requiere para otorgar al rol de IAM en la Cuenta A permiso para descifrar y leer los objetos de S3?",
            "options": [
                {
                    "id": "A",
                    "text": "Exportar la clave privada de KMS de la Cuenta B e importarla en una clave de AWS KMS en la Cuenta A.",
                    "explanation": "Incorrecto: Las Customer Managed Keys de KMS no son exportables; AWS KMS administra el material de claves simétricas dentro de módulos HSM."
                },
                {
                    "id": "B",
                    "text": "Cambiar el cifrado en el bucket de S3 de la Cuenta B a AWS Managed Key (aws/s3), lo que permite automáticamente todos los roles de IAM entre cuentas.",
                    "explanation": "Incorrecto: La clave administrada por AWS predeterminada (aws/s3) no se puede compartir entre diferentes cuentas de AWS; el acceso entre cuentas a KMS requiere Customer Managed Keys."
                },
                {
                    "id": "C",
                    "text": "Configurar una ACL de S3 en el bucket de la Cuenta B otorgando permisos de lectura pública.",
                    "explanation": "Incorrecto: Las ACLs no otorgan permisos de descifrado de KMS y hacer que el bucket sea público crea una grave vulnerabilidad de seguridad."
                },
                {
                    "id": "D",
                    "text": "Adjuntar una política de IAM al rol en la Cuenta A otorgando kms:Decrypt y s3:GetObject, configurar la política de bucket de S3 en la Cuenta B para permitir el ARN del rol de la Cuenta A, y actualizar la política de clave de KMS en la Cuenta B para permitir que el ARN del rol de la Cuenta A (o el root de la Cuenta A) ejecute kms:Decrypt.",
                    "explanation": "Correcto: El acceso entre cuentas a KMS y S3 requiere delegación explícita: la directiva de identidad de IAM en la Cuenta A, la directiva de recursos del bucket de S3 en la Cuenta B y la directiva de clave de KMS en la Cuenta B deben permitir la acción."
                }
            ],
            "generalExplanation": "El acceso entre cuentas a objetos de S3 cifrados con KMS requiere permisos en tres lugares: la directiva de IAM del consumidor, la directiva del bucket de S3 de destino y la directiva de clave de KMS de destino."
        }
    },
    "sap-sim1-q007": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa usa o AWS Control Tower para governar seu ambiente de múltiplas contas. A equipe de governança de segurança exige um controle de detecção (detective guardrail) personalizado para garantir que nenhum volume do Amazon EBS seja criado sem uma tag 'Owner' e que os volumes não conformes sejam sinalizados automaticamente em todas as contas existentes e recém-provisionadas. Como isso deve ser implementado?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma regra agendada do Amazon CloudWatch em uma instância EC2 na conta de gerenciamento para consultar o Relatório de Custos e Uso da AWS (Cost and Usage Report).",
                    "explanation": "Incorreto: Os Relatórios de Custos e Uso têm horas de latência de faturamento e não podem avaliar a conformidade de tags de recursos em tempo real."
                },
                {
                    "id": "B",
                    "text": "Criar manualmente uma regra do AWS Config em cada conta via Console de Gerenciamento da AWS sempre que uma nova conta for inscrita.",
                    "explanation": "Incorreto: A criação manual é propensa a erros, não é escalável e não é aplicada automaticamente a contas futuras."
                },
                {
                    "id": "C",
                    "text": "Implantar uma regra personalizada do AWS Config em toda a organização usando as Customizations for AWS Control Tower (CfCT) ou os Controles Personalizados do AWS Control Tower (governance guardrails).",
                    "explanation": "Correto: O Customizations for AWS Control Tower (CfCT) ou os guardrails personalizados nativos do Control Tower permitem a implantação de regras customizadas do AWS Config e templates do CloudFormation em todas as contas automaticamente."
                },
                {
                    "id": "D",
                    "text": "Anexar uma Service Control Policy (SCP) à OU raiz que nega explicitamente ec2:CreateVolume sem uma tag Owner.",
                    "explanation": "Incorreto: As SCPs são controles preventivos (bloqueiam a criação), enquanto o requisito pede especificamente um guardrail de detecção que sinalize recursos existentes que não estejam em conformidade."
                }
            ],
            "generalExplanation": "O Customizations for AWS Control Tower (CfCT) permite que os clientes implantem guardrails preventivos e de detecção personalizados (regras do AWS Config) em todas as contas gerenciadas pelo Control Tower."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa utiliza AWS Control Tower para controlar su entorno de múltiples cuentas. El equipo de gobierno de seguridad requiere un control de detección (detective guardrail) personalizado para garantizar que ningún volumen de Amazon EBS se cree sin una etiqueta 'Owner' y que los volúmenes no conformes se marquen automáticamente en todas las cuentas existentes y recién aprovisionadas. ¿Cómo se debe implementar esto?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una regla programada de Amazon CloudWatch en una instancia EC2 en la cuenta de administración para consultar el Informe de costos y uso de AWS (Cost and Usage Report).",
                    "explanation": "Incorrecto: Los informes de costos y uso tienen horas de latencia de facturación y no pueden evaluar el cumplimiento del etiquetado de recursos en tiempo real."
                },
                {
                    "id": "B",
                    "text": "Crear manualmente una regla de AWS Config en cada cuenta a través de la Consola de administración de AWS cada vez que se inscriba una nueva cuenta.",
                    "explanation": "Incorrecto: La creación manual es propensa a errores, no es escalable y no se aplica automáticamente a cuentas futuras."
                },
                {
                    "id": "C",
                    "text": "Implementar una regla personalizada de AWS Config en toda la organización mediante Customizations for AWS Control Tower (CfCT) o Controles Personalizados de AWS Control Tower (guardrails de gobernanza).",
                    "explanation": "Correcto: Customizations for AWS Control Tower (CfCT) o los guardrails personalizados nativos de Control Tower permiten la implementación automática de reglas personalizadas de AWS Config y plantillas de CloudFormation en todas las cuentas."
                },
                {
                    "id": "D",
                    "text": "Adjuntar una Service Control Policy (SCP) a la OU raíz que niega explícitamente ec2:CreateVolume sin una etiqueta Owner.",
                    "explanation": "Incorrecto: Las SCPs son controles preventivos (bloquean la creación), mientras que el requisito solicita específicamente un guardrail de detección que identifique recursos existentes no conformes."
                }
            ],
            "generalExplanation": "Customizations for AWS Control Tower (CfCT) permite a los clientes implementar barreras de protección preventivas y de detección personalizadas (reglas de AWS Config) en todas las cuentas administradas por Control Tower."
        }
    },
    "sap-sim1-q008": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma empresa de tecnologia financeira (fintech) está projetando uma plataforma de processamento de pagamentos distribuída globalmente, implantada em us-east-1 (Primária) e eu-west-1 (Secundária). A camada de banco de dados requer conformidade relacional ACID, latência de replicação entre regiões inferior a um segundo e capacidade de realizar failover de recuperação de desastres não planejado em menos de 1 minuto com perda zero de dados (RPO = 0 ou próximo de 0). Qual arquitetura de banco de dados atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB Global Tables com replicação ativo-ativo em múltiplas regiões.",
                    "explanation": "Incorreto: O DynamoDB é um banco de dados NoSQL de chave-valor, não um banco de dados relacional SQL com conformidade ACID conforme exigido."
                },
                {
                    "id": "B",
                    "text": "Amazon Aurora Global Database com o cluster primário em us-east-1 e um cluster secundário em eu-west-1, utilizando replicação dedicada em nível de armazenamento e failover rápido entre regiões.",
                    "explanation": "Correto: O Amazon Aurora Global Database replica blocos de armazenamento entre regiões tipicamente em menos de 1 segundo sem impactar o desempenho de computação e oferece suporte a failover planejado/não planejado gerenciado em menos de 1 minuto."
                },
                {
                    "id": "C",
                    "text": "Cluster multirregional do Amazon Redshift com ingestão de dados em streaming.",
                    "explanation": "Incorreto: O Amazon Redshift é um data warehouse analítico, não um mecanismo transacional OLTP para processamento de pagamentos."
                },
                {
                    "id": "D",
                    "text": "Amazon RDS PostgreSQL Multi-AZ com uma réplica de leitura assíncrona entre regiões em eu-west-1.",
                    "explanation": "Incorreto: As réplicas de leitura padrão do RDS entre regiões usam replicação assíncrona com maior latência (segundos a minutos) e exigem promoção e reconfiguração manuais."
                }
            ],
            "generalExplanation": "O Amazon Aurora Global Database usa infraestrutura de armazenamento dedicada para replicar dados entre Regiões AWS com latência típica inferior a 1 segundo, fornecendo rápida recuperação de desastres entre regiões para cargas de trabalho relacionais."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una empresa fintech está diseñando una plataforma de procesamiento de pagos distribuida globalmente, implementada en us-east-1 (Primaria) y eu-west-1 (Secundaria). La capa de base de datos requiere conformidad relacional ACID, retraso de replicación entre regiones inferior a un segundo y la capacidad de realizar una conmutación por error no planificada de recuperación ante desastres en menos de 1 minuto sin pérdida de datos (RPO = 0 o cercano a 0). ¿Qué arquitectura de base de datos cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB Global Tables con replicación multirregional activo-activo.",
                    "explanation": "Incorrecto: DynamoDB es un almacén de clave-valor NoSQL, no una base de datos relacional SQL con conformidad ACID como se requiere."
                },
                {
                    "id": "B",
                    "text": "Amazon Aurora Global Database con el clúster principal en us-east-1 y un clúster secundario en eu-west-1, utilizando replicación dedicada a nivel de almacenamiento y conmutación por error rápida entre regiones.",
                    "explanation": "Correcto: Amazon Aurora Global Database replica bloques de almacenamiento entre regiones generalmente en menos de 1 segundo sin afectar el rendimiento de cómputo, y admite conmutación por error administrada planificada/no planificada en menos de 1 minuto."
                },
                {
                    "id": "C",
                    "text": "Clúster multirregional de Amazon Redshift con ingesta de datos en streaming.",
                    "explanation": "Incorrecto: Amazon Redshift es un almacén de datos analítico (data warehouse), no un motor transaccional OLTP de pagos."
                },
                {
                    "id": "D",
                    "text": "Amazon RDS PostgreSQL Multi-AZ con una réplica de lectura asíncrona entre regiones en eu-west-1.",
                    "explanation": "Incorrecto: Las réplicas de lectura entre regiones estándar de RDS utilizan replicación asíncrona con mayor retraso (de segundos a minutos) y requieren promoción y reconfiguración manuales."
                }
            ],
            "generalExplanation": "Amazon Aurora Global Database utiliza hardware de almacenamiento dedicado para replicar datos entre Regiones de AWS con una latencia típica inferior a 1 segundo, lo que proporciona una rápida recuperación ante desastres multirregional para cargas de trabajo relacionales."
        }
    },
    "sap-sim1-q009": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Um pipeline de ingestão de pedidos de comércio eletrônico (e-commerce) recebe 20.000 pedidos por segundo durante liquidações relâmpago. O sistema deve garantir que os pedidos para a mesma conta de cliente sejam processados estritamente em sequência cronológica, pedidos duplicados sejam filtrados e pedidos com falha sejam isolados sem bloquear os pedidos de outros clientes. Qual arquitetura serverless satisfaz esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Fila Amazon SQS Standard com tempo limite de visibilidade máximo, consultada por um grupo de Auto Scaling do EC2 executando scripts Python de thread única.",
                    "explanation": "Incorreto: As filas SQS Standard fornecem entrega de pelo menos uma vez (at-least-once) e não garantem ordenação estrita de mensagens."
                },
                {
                    "id": "B",
                    "text": "Fila Amazon SQS FIFO configurada com o ID do cliente como Message Group ID, desduplicação baseada em conteúdo habilitada, consumida pelo AWS Lambda com uma Dead Letter Queue (DLQ) configurada.",
                    "explanation": "Correto: O SQS FIFO com Message Group ID garante ordenação estrita por cliente enquanto permite alto processamento paralelo simultâneo entre clientes diferentes. A desduplicação baseada em conteúdo evita duplicatas e uma DLQ isola mensagens com falha."
                },
                {
                    "id": "C",
                    "text": "Tópico Amazon SNS Standard transmitindo para 10 funções AWS Lambda em paralelo.",
                    "explanation": "Incorreto: O SNS Standard não garante ordenação nem desduplicação automática de mensagens."
                },
                {
                    "id": "D",
                    "text": "Amazon Kinesis Data Firehose gravando diretamente no Amazon S3 com uma tabela do Athena particionada pelo ID do cliente.",
                    "explanation": "Incorreto: O Kinesis Firehose agrupa dados em lotes com buffer e foi projetado para entrega analítica, não para processamento transacional de pedidos de baixa latência."
                }
            ],
            "generalExplanation": "As filas Amazon SQS FIFO com Message Group IDs fornecem ordenação estrita por grupo, desduplicação e isolamento com filas de mensagens mortas (DLQ) para pipelines transacionais de missão crítica."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Un flujo de trabajo (pipeline) de ingesta de pedidos de comercio electrónico recibe 20.000 pedidos por segundo durante ofertas flash. El sistema debe garantizar que los pedidos de la misma cuenta de cliente se procesen estrictamente en secuencia cronológica, se filtren los pedidos duplicados y se aíslen los pedidos fallidos sin bloquear los pedidos de otros clientes. ¿Qué arquitectura serverless cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Cola Amazon SQS Standard con tiempo de espera de visibilidad máximo, sondeada por un grupo de Auto Scaling de EC2 que ejecuta scripts de Python de un solo hilo.",
                    "explanation": "Incorrecto: Las colas SQS Standard proporcionan entrega al menos una vez y no garantizan un orden estricto de los mensajes."
                },
                {
                    "id": "B",
                    "text": "Cola Amazon SQS FIFO configurada con el ID del cliente como Message Group ID, deduplicación basada en contenido habilitada, respaldada por un consumidor de AWS Lambda con una Dead Letter Queue (DLQ) configurada.",
                    "explanation": "Correcto: SQS FIFO con Message Group ID garantiza un orden estricto por cliente al tiempo que permite un alto procesamiento concurrente en paralelo entre diferentes clientes. La deduplicación basada en contenido evita duplicados y una DLQ aísla los mensajes fallidos."
                },
                {
                    "id": "C",
                    "text": "Tema Amazon SNS Standard con difusión (broadcast) a 10 funciones de AWS Lambda en paralelo.",
                    "explanation": "Incorrecto: SNS Standard no garantiza el orden ni la deduplicación automática de mensajes."
                },
                {
                    "id": "D",
                    "text": "Amazon Kinesis Data Firehose escribiendo directamente en Amazon S3 con una tabla de Athena particionada por ID de cliente.",
                    "explanation": "Incorrecto: Kinesis Firehose almacena en búfer por lotes y está diseñado para la entrega de análisis, no para el procesamiento de pedidos transaccionales de baja latencia."
                }
            ],
            "generalExplanation": "Las colas Amazon SQS FIFO con Message Group IDs proporcionan orden estricto por grupo, deduplicación y aislamiento de colas de mensajes fallidos (DLQ) para canalizaciones transaccionales de misión crítica."
        }
    },
    "sap-sim1-q010": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Um provedor de SaaS publica uma API REST multilocatário (multi-tenant) usando o Amazon API Gateway. Diferentes níveis de locatários exigem limites de taxa diferentes: os usuários do nível Gratuito (Free) estão limitados a 100 requisições/minuto, enquanto os usuários do nível Enterprise têm permissão para 10.000 requisições/minuto. Além disso, os clientes devem autenticar-se por meio de tokens JWT emitidos por um provedor OAuth 2.0 externo. Qual arquitetura deve ser implantada com o MENOR desenvolvimento personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar um Lambda Authorizer no API Gateway para validar o token JWT e retornar o contexto, associar Planos de Uso (Usage Plans) a Chaves de API (API Keys) para cada nível e configurar limites de controle de fluxo (throttling) no Plano de Uso.",
                    "explanation": "Correto: Os Planos de Uso e as Chaves de API do API Gateway lidam nativamente com limitação de taxa e controle de fluxo por nível de cliente, enquanto um Lambda Authorizer valida tokens JWT do OAuth externo."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster de proxy NGINX no Amazon EC2 na frente do API Gateway para gerenciar limites de taxa por IP de cliente no Redis.",
                    "explanation": "Incorreto: Clusters auto-gerenciados de NGINX e Redis introduzem alta sobrecarga de manutenção e failover em comparação com os Planos de Uso nativos do API Gateway."
                },
                {
                    "id": "C",
                    "text": "Implantar o AWS WAF com regras baseadas em taxa de IP para cada endereço IP de cliente.",
                    "explanation": "Incorreto: As regras baseadas em taxa do AWS WAF se aplicam a endereços IP, não a níveis de identidade autenticados por JWT, e não conseguem diferenciar usuários Free de Enterprise atrás de IPs NAT corporativos compartilhados."
                },
                {
                    "id": "D",
                    "text": "Implementar a lógica de limitação de taxa dentro de cada microsserviço de backend gravando tokens em uma tabela do Amazon DynamoDB.",
                    "explanation": "Incorreto: Criar lógica manual de rate limiting no código do backend adiciona latência, custos de I/O de banco de dados e complexidade no código."
                }
            ],
            "generalExplanation": "Os Planos de Uso (Usage Plans) do Amazon API Gateway permitem definir limites de requisições (throttle) e cotas para níveis de clientes individuais, integrando-se perfeitamente com chaves de API e autorizadores personalizados."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Un proveedor de SaaS publica una API REST multi-tenant utilizando Amazon API Gateway. Los diferentes niveles de clientes requieren diferentes límites de tasa: los usuarios del nivel Gratuito (Free) están limitados a 100 solicitudes/minuto, mientras que los usuarios del nivel Enterprise tienen permitido 10.000 solicitudes/minuto. Además, los clientes deben autenticarse mediante tokens JWT emitidos por un proveedor de OAuth 2.0 externo. ¿Qué arquitectura debe implementarse con el MENOR desarrollo personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar un Lambda Authorizer en API Gateway para validar el token JWT y devolver el contexto, asociar Planes de Uso (Usage Plans) con Claves de API (API Keys) para cada nivel y configurar límites de control de flujo (throttling) en el Plan de Uso.",
                    "explanation": "Correcto: Los Planes de Uso y las Claves de API de API Gateway manejan de forma nativa la limitación de tasa y el control de flujo en niveles por cliente, mientras que un Lambda Authorizer valida los tokens JWT de OAuth externo."
                },
                {
                    "id": "B",
                    "text": "Implementar un clúster proxy NGINX en Amazon EC2 frente a API Gateway para administrar los límites de tasa de IP de cliente en Redis.",
                    "explanation": "Incorrecto: Los clústeres autogestionados de NGINX y Redis introducen una gran sobrecarga de mantenimiento y conmutación por error en comparación con los Planes de Uso nativos de API Gateway."
                },
                {
                    "id": "C",
                    "text": "Implementar AWS WAF con reglas basadas en tasas de IP para cada dirección IP de cliente.",
                    "explanation": "Incorrecto: Las reglas basadas en tasas de AWS WAF se aplican a direcciones IP, no a identidades de inquilinos autenticadas por JWT, y no pueden diferenciar usuarios de nivel Free frente a Enterprise detrás de IPs NAT corporativas compartidas."
                },
                {
                    "id": "D",
                    "text": "Implementar lógica de limitación de tasa dentro de cada microservicio backend escribiendo tokens en una tabla de Amazon DynamoDB.",
                    "explanation": "Incorrecto: Crear lógica manual de limitación de tasa en el código backend agrega latencia, costos de E/S de base de datos y complejidad en el código."
                }
            ],
            "generalExplanation": "Los Planes de Uso de Amazon API Gateway le permiten definir límites de control de flujo (throttle) y cuotas para niveles de clientes individuales, integrándose perfectamente con claves de API y autorizadores personalizados."
        }
    },
    "sap-sim1-q011": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma plataforma automatizada de aprovação de empréstimos requer a orquestração de um fluxo de trabalho com várias etapas, envolvendo verificações em órgãos de proteção ao crédito, modelos de ML de detecção de fraudes, aprovação humana por um subscritor para empréstimos acima de US$ 50.000 e notificação ao cliente. Algumas tarefas podem ser executadas em paralelo, enquanto a análise humana pode levar até 3 dias úteis. Qual solução orquestra esse fluxo de trabalho com gerenciamento de estado nativo e o mínimo de código personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Step Functions Express Workflows com tempo limite máximo de 5 minutos.",
                    "explanation": "Incorreto: Os fluxos Express Workflows têm uma duração máxima de execução de 5 minutos e não suportam aprovações humanas de longa duração de até 3 dias."
                },
                {
                    "id": "B",
                    "text": "AWS Step Functions Standard Workflows usando estados de Tarefa (Task), estados Paralelos (Parallel) e o padrão de retorno de chamada (Task Token) para a etapa de aprovação humana.",
                    "explanation": "Correto: Os fluxos Standard Workflows do AWS Step Functions suportam durações de execução de até 1 ano, ramificações de execução paralela, tratamento de erros/novas tentativas e tokens de tarefa para aprovação humana (waitForTaskToken)."
                },
                {
                    "id": "C",
                    "text": "Uma fila do Amazon Simple Queue Service (SQS) com tempo limite de visibilidade definido para 72 horas.",
                    "explanation": "Incorreto: O tempo limite máximo de visibilidade do SQS é de 12 horas, tornando impossíveis pausas de 3 dias sem polling personalizado complexo."
                },
                {
                    "id": "D",
                    "text": "Encadeamento síncrono de funções AWS Lambda onde cada função chama a próxima função via AWS SDK.",
                    "explanation": "Incorreto: As funções Lambda têm um tempo limite máximo de 15 minutos e o encadeamento síncrono não pode aguardar 3 dias pela análise humana."
                }
            ],
            "generalExplanation": "Os fluxos de trabalho Standard Workflows do AWS Step Functions foram projetados para execuções de longa duração (até 1 ano) e fornecem tokens de retorno de chamada nativos (Task Tokens) para aprovações humanas assíncronas."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una plataforma automatizada de aprobación de préstamos requiere orquestar un flujo de trabajo de varios pasos que involucra verificaciones en agencias de crédito, modelos de ML para detección de fraudes, aprobación humana de un suscriptor para préstamos superiores a $50.000 y notificación al cliente. Algunas tareas pueden ejecutarse en paralelo, mientras que la revisión humana puede demorar hasta 3 días hábiles. ¿Qué solución orquesta este flujo de trabajo con administración de estado nativa y mínimo código personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Step Functions Express Workflows con tiempo de espera máximo de 5 minutos.",
                    "explanation": "Incorrecto: Los Express Workflows tienen una duración máxima de ejecución de 5 minutos y no admiten aprobaciones humanas de larga duración de 3 días."
                },
                {
                    "id": "B",
                    "text": "AWS Step Functions Standard Workflows utilizando estados de Tarea (Task), estados Paralelos (Parallel) y el patrón de devolución de llamada (Task Token) para el paso de aprobación humana.",
                    "explanation": "Correcto: Los Standard Workflows de AWS Step Functions admiten duraciones de ejecución de hasta 1 año, ramas de ejecución paralelas, control de errores/reintentos y tokens de tareas con intervención humana (waitForTaskToken)."
                },
                {
                    "id": "C",
                    "text": "Una cola de Amazon Simple Queue Service (SQS) con tiempo de espera de visibilidad establecido en 72 horas.",
                    "explanation": "Incorrecto: El tiempo de espera de visibilidad máximo de SQS es de 12 horas, lo que hace imposibles las pausas de 3 días sin sondeos personalizados complejos."
                },
                {
                    "id": "D",
                    "text": "Encadenamiento sincrónico de funciones AWS Lambda donde cada función llama a la siguiente función a través del SDK de AWS.",
                    "explanation": "Incorrecto: Las funciones Lambda tienen un tiempo de espera máximo de 15 minutos y el encadenamiento sincrónico no puede esperar 3 días para la revisión humana."
                }
            ],
            "generalExplanation": "Los flujos de trabajo Standard Workflows de AWS Step Functions están diseñados para ejecuciones prolongadas (hasta 1 año) y proporcionan tokens de devolución de llamada nativos (Task Tokens) para aprobaciones humanas asíncronas."
        }
    },
    "sap-sim1-q012": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma empresa de cibersegurança precisa ingerir 5 TB de logs de acesso a servidores diariamente, executar detecção de padrões de ameaças em tempo real dentro de 5 segundos após a geração dos logs e armazenar dados indexados para consultas de pesquisa interativas e painéis de conformidade por 90 dias. Qual arquitetura oferece a solução gerenciada mais escalável?",
            "options": [
                {
                    "id": "A",
                    "text": "Salvar logs diretamente no Amazon S3 Standard e executar crawlers diários do AWS Glue ETL para consultar logs com o Amazon Athena.",
                    "explanation": "Incorreto: Crawlers diários do Glue e consultas no Athena introduzem uma latência de 24 horas, violando o requisito de detecção em tempo real de 5 segundos."
                },
                {
                    "id": "B",
                    "text": "Armazenar logs em tabelas do Amazon RDS PostgreSQL com índices B-tree em endereços IP.",
                    "explanation": "Incorreto: Um banco de dados relacional não consegue suportar a ingestão e indexação contínua de 5 TB de logs diários sem contenção severa de bloqueios."
                },
                {
                    "id": "C",
                    "text": "Ingerir logs com o Amazon Kinesis Data Streams, processar streams com o Amazon Managed Service for Apache Flink para detecção de anomalias em tempo real e entregar logs transformados ao Amazon OpenSearch Service com gerenciamento automatizado do ciclo de vida dos índices.",
                    "explanation": "Correto: O Kinesis Data Streams + Managed Service for Apache Flink fornece análise de streaming com latência abaixo de um segundo, e o Amazon OpenSearch Service oferece indexação e visualização rápida de texto completo (OpenSearch Dashboards) com políticas de gerenciamento de ciclo de vida (ISM)."
                },
                {
                    "id": "D",
                    "text": "Transmitir logs para uma fila Amazon SQS Standard e invocar o AWS Lambda para gravar documentos no Amazon DynamoDB.",
                    "explanation": "Incorreto: O DynamoDB é um banco de dados de chave-valor, não um mecanismo de pesquisa de texto completo otimizado para consultas ad-hoc e visualização de logs como o OpenSearch."
                }
            ],
            "generalExplanation": "O Amazon Kinesis com Managed Apache Flink oferece processamento de streaming em tempo real, enquanto o Amazon OpenSearch Service fornece pesquisa distribuída, indexação e visualização para análise de logs."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una empresa de ciberseguridad necesita ingerir 5 TB de registros (logs) de acceso a servidores diariamente, realizar la detección de patrones de amenazas en tiempo real dentro de los 5 segundos posteriores a la generación del registro y almacenar datos indexados para consultas de búsqueda interactivas y paneles de cumplimiento durante 90 días. ¿Qué arquitectura proporciona la solución administrada más escalable?",
            "options": [
                {
                    "id": "A",
                    "text": "Guardar registros directamente en Amazon S3 Standard y ejecutar rastreadores (crawlers) diarios de AWS Glue ETL para consultar registros con Amazon Athena.",
                    "explanation": "Incorrecto: Los crawlers diarios de Glue y las consultas de Athena introducen una latencia de 24 horas, no cumpliendo con el requisito de detección en tiempo real de 5 segundos."
                },
                {
                    "id": "B",
                    "text": "Almacenar registros en tablas de Amazon RDS PostgreSQL con índices de árbol B en direcciones IP.",
                    "explanation": "Incorrecto: Una base de datos relacional no puede manejar 5 TB de ingesta continua diaria de registros e indexación sin una grave contención de bloqueos."
                },
                {
                    "id": "C",
                    "text": "Ingerir registros con Amazon Kinesis Data Streams, procesar flujos con Amazon Managed Service for Apache Flink para la detección de anomalías en tiempo real y entregar registros transformados a Amazon OpenSearch Service con administración automatizada del ciclo de vida de índices.",
                    "explanation": "Correcto: Kinesis Data Streams + Managed Service for Apache Flink proporciona análisis de streaming en subsegundos, y Amazon OpenSearch Service proporciona indexación de texto completo rápida y visualización (OpenSearch Dashboards) con políticas ISM."
                },
                {
                    "id": "D",
                    "text": "Transmitir registros a una cola Amazon SQS Standard e invocar AWS Lambda para escribir documentos en Amazon DynamoDB.",
                    "explanation": "Incorrecto: DynamoDB es un almacén de clave-valor, no un motor de búsqueda de texto completo optimizado para consultas de registros ad-hoc y visualización como OpenSearch."
                }
            ],
            "generalExplanation": "Amazon Kinesis con Managed Apache Flink ofrece procesamiento de secuencias en tiempo real, mientras que Amazon OpenSearch Service proporciona búsqueda distribuida, indexación y visualización para el análisis de registros."
        }
    },
    "sap-sim1-q013": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma rede global de notícias transmite vídeos e artigos de notícias de última hora ao vivo. Durante grandes eventos mundiais, o tráfego de espectadores aumenta em 1.000 vezes dentro de 30 segundos. A solução deve armazenar em cache respostas de API dinâmicas e ativos estáticos em locais de borda (edge locations), executar lógica computacional de borda em submilissegundos para personalizar cabeçalhos HTTP com base no país do espectador e proteger os servidores de origem contra colapso de requisições. Qual combinação de serviços o arquiteto deve recomendar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um Application Load Balancer em cada Região AWS e usar o roteamento por geolocalização do Amazon Route 53 sem cache de borda.",
                    "explanation": "Incorreto: Sem o cache de borda, picos repentinos de 1.000x no tráfego atingirão diretamente as origens de backend, levando à exaustão de recursos."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS Global Accelerator com instâncias EC2 executando proxies reversos de cache NGINX.",
                    "explanation": "Incorreto: O Global Accelerator otimiza o roteamento de rede, mas não fornece cache HTTP de borda, Origin Shield ou computação serverless na borda."
                },
                {
                    "id": "C",
                    "text": "Implantar o Amazon CloudFront com CloudFront Functions para manipulação de cabeçalhos na borda, configurar o Origin Shield e políticas de cache, e anexar o AWS WAF à distribuição.",
                    "explanation": "Correto: O CloudFront Functions fornece modificação de cabeçalhos na borda com latência ultrabaixa (<1ms), o CloudFront Origin Shield elimina requisições redundantes para proteger os servidores de origem durante picos de tráfego e o AWS WAF fornece segurança na borda."
                },
                {
                    "id": "D",
                    "text": "Configurar o Amazon API Gateway com Lambda Authorizers e desabilitar a distribuição do CloudFront.",
                    "explanation": "Incorreto: Desabilitar o CloudFront remove o cache global de borda e expõe as funções Lambda de backend a picos massivos de simultaneidade."
                }
            ],
            "generalExplanation": "O Amazon CloudFront com CloudFront Functions e Origin Shield minimiza a carga na origem durante picos extremos de tráfego, enquanto personaliza as solicitações na borda em frações de milissegundos."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una red global de noticias ofrece videos y artículos de noticias de última hora en vivo. Durante eventos mundiales importantes, el tráfico de espectadores aumenta 1.000 veces en 30 segundos. La solución debe almacenar en caché respuestas de API dinámicas y recursos estáticos en ubicaciones perimetrales (edge), ejecutar lógica de cómputo en el borde en submilisegundos para personalizar los encabezados HTTP según el país del espectador y proteger los servidores de origen contra el colapso de solicitudes. ¿Qué combinación de servicios debería recomendar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un Application Load Balancer en cada Región de AWS y usar el enrutamiento de geolocalización de Amazon Route 53 sin almacenamiento en caché perimetral.",
                    "explanation": "Incorrecto: Sin el almacenamiento en caché perimetral, los aumentos repentinos de tráfico de 1.000x llegarán directamente a los orígenes del backend, provocando el agotamiento de los recursos."
                },
                {
                    "id": "B",
                    "text": "Usar AWS Global Accelerator con instancias EC2 ejecutando proxies inversos de almacenamiento en caché NGINX.",
                    "explanation": "Incorrecto: Global Accelerator optimiza el enrutamiento de red, pero no proporciona almacenamiento en caché perimetral HTTP, Origin Shield ni cómputo sin servidor en el borde."
                },
                {
                    "id": "C",
                    "text": "Implementar Amazon CloudFront con CloudFront Functions para la manipulación de encabezados en el borde, configurar Origin Shield y directivas de caché, y adjuntar AWS WAF a la distribución.",
                    "explanation": "Correcto: CloudFront Functions proporciona modificación de encabezados en el borde con latencia ultrabaja (<1ms), CloudFront Origin Shield elimina solicitudes redundantes para proteger los servidores de origen durante sobrecargas de tráfico y AWS WAF proporciona seguridad en el borde."
                },
                {
                    "id": "D",
                    "text": "Configurar Amazon API Gateway con Lambda Authorizers y deshabilitar la distribución de CloudFront.",
                    "explanation": "Incorrecto: Deshabilitar CloudFront elimina el almacenamiento en caché global en el borde y expone las funciones Lambda de backend a picos masivos de concurrencia."
                }
            ],
            "generalExplanation": "Amazon CloudFront con CloudFront Functions y Origin Shield minimiza la carga de origen durante picos extremos de tráfico, mientras personaliza las solicitudes en el borde en fracciones de milisegundo."
        }
    },
    "sap-sim1-q014": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma equipe de engenharia de implantação contínua precisa de um mecanismo para gerenciar sinalizadores de recursos (feature flags) de aplicações em milhares de instâncias EC2 e tarefas ECS. A solução deve permitir a liberação gradual e controlada de alterações de configuração (por exemplo, 10% do tráfego a cada 5 minutos), reverter automaticamente a configuração se os alarmes do Amazon CloudWatch ultrapassarem os limites de erro e validar os esquemas de configuração antes da implantação. Qual serviço da AWS foi projetado especificamente para essa finalidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Armazenar as feature flags de configuração de aplicações no AWS Secrets Manager e agendar a rotação automática de segredos.",
                    "explanation": "Incorreto: O Secrets Manager foi projetado para rotação de credenciais e senhas, não para rollouts dinâmicos de feature flags."
                },
                {
                    "id": "B",
                    "text": "Configurar o AWS CodeDeploy com o modo de implantação in-place e scripts de hook de ciclo de vida de implantação personalizados em toda a frota.",
                    "explanation": "Incorreto: O CodeDeploy implanta pacotes binários de aplicações, não feature flags de configuração dinâmica de aplicações em tempo de execução."
                },
                {
                    "id": "C",
                    "text": "Armazenar arquivos JSON de configuração em um bucket do Amazon S3 com versionamento e S3 Event Notifications configuradas.",
                    "explanation": "Incorreto: O S3 não fornece estratégias integradas de implantação linear/canary, validadores de esquema ou rollbacks automatizados com alarmes do CloudWatch."
                },
                {
                    "id": "D",
                    "text": "AWS AppConfig (um recurso do AWS Systems Manager)",
                    "explanation": "Correto: O AWS AppConfig permite que as equipes criem, validem, implantem e monitorem configurações de aplicações com estratégias de implantação personalizadas (linear/canary) e rollback automatizado acionado por alarmes do CloudWatch."
                }
            ],
            "generalExplanation": "O AWS AppConfig permite implantar com rapidez e segurança alterações de configuração de tempo de execução e feature flags em aplicações no EC2, ECS, Lambda ou on-premises com guardrails e rollbacks automatizados."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Un equipo de ingeniería de implementación continua necesita un mecanismo para administrar indicadores de funciones (feature flags) de aplicaciones en miles de instancias EC2 y tareas ECS. La solución debe permitir el despliegue gradual y controlado de cambios de configuración (por ejemplo, 10% de tráfico cada 5 minutos), revertir automáticamente la configuración si las alarmas de Amazon CloudWatch superan los umbrales de error y validar esquemas de configuración antes de la implementación. ¿Qué servicio de AWS está diseñado específicamente para este requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Almacenar las feature flags de configuración de aplicaciones en AWS Secrets Manager y programar la rotación automática de secretos.",
                    "explanation": "Incorrecto: Secrets Manager está diseñado para la rotación de credenciales/contraseñas, no para implementaciones dinámicas de indicadores de funciones."
                },
                {
                    "id": "B",
                    "text": "Configurar AWS CodeDeploy con modo de implementación in-place y scripts personalizados de enlaces del ciclo de vida de implementación en toda la flota.",
                    "explanation": "Incorrecto: CodeDeploy implementa paquetes binarios de aplicaciones, no feature flags dinámicas de configuración en tiempo de ejecución."
                },
                {
                    "id": "C",
                    "text": "Almacenar archivos JSON de configuración en un bucket de Amazon S3 con control de versiones y notificaciones de eventos de S3 configuradas.",
                    "explanation": "Incorrecto: S3 no proporciona estrategias de implementación lineal/canary integradas, validadores de esquemas ni reversiones automáticas por alarmas de CloudWatch."
                },
                {
                    "id": "D",
                    "text": "AWS AppConfig (una funcionalidad de AWS Systems Manager)",
                    "explanation": "Correcto: AWS AppConfig permite a los equipos crear, validar, implementar y monitorear configuraciones de aplicaciones con estrategias de implementación personalizadas (lineal/canary) y reversión automatizada por alarmas de CloudWatch."
                }
            ],
            "generalExplanation": "AWS AppConfig le permite implementar de forma rápida y segura cambios de configuración en tiempo de ejecución y feature flags en aplicaciones en EC2, ECS, Lambda o entornos locales con barreras de seguridad y reversiones automáticas."
        }
    },
    "sap-sim1-q015": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa armazena 20 petabytes de dados em 2.000 buckets do Amazon S3 em 50 contas AWS no AWS Organizations. O Diretor de Segurança da Informação (CISO) e o CFO exigem visibilidade em toda a organização sobre o uso do armazenamento, identificação de buckets sem criptografia padrão e insights práticos para descobrir uploads fracionados incompletos (incomplete multipart uploads) e marcadores de exclusão de versão órfãos. Qual solução fornece essas métricas em toda a organização com o MENOR esforço?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Amazon S3 Storage Lens com um painel no nível da organização na conta de gerenciamento do AWS Organizations e exportar métricas diariamente para um bucket S3.",
                    "explanation": "Correto: O Amazon S3 Storage Lens fornece visibilidade em toda a organização sobre o armazenamento de objetos, métricas de atividade e recomendações de otimização de custos em todas as contas no AWS Organizations."
                },
                {
                    "id": "B",
                    "text": "Escrever um script em Python em uma instância EC2 que chama a API s3:ListObjectsV2 em todos os 2.000 buckets diariamente e grava os resultados no Amazon DynamoDB.",
                    "explanation": "Incorreto: Chamar ListObjectsV2 em 20 PB de dados gera custos massivos de API, alta latência e grande esforço de manutenção operacional."
                },
                {
                    "id": "C",
                    "text": "Implantar regras do AWS Config em todas as contas e consultar o AWS Config Aggregator.",
                    "explanation": "Incorreto: O AWS Config rastreia metadados de configuração de buckets, mas não fornece análises detalhadas de armazenamento, métricas de atividade em nível de prefixo ou análises de multipart uploads incompletos como o S3 Storage Lens."
                },
                {
                    "id": "D",
                    "text": "Habilitar o S3 Server Access Logging em cada bucket e usar o Amazon Athena para analisar os logs de texto bruto diariamente.",
                    "explanation": "Incorreto: Analisar bilhões de linhas brutas de logs de acesso no Athena gera custos operacionais e de consulta substanciais em comparação com o S3 Storage Lens nativo."
                }
            ],
            "generalExplanation": "O Amazon S3 Storage Lens é um recurso de análise de armazenamento em nuvem que oferece visibilidade em toda a organização sobre o uso do armazenamento de objetos, tendências de atividade e recomendações de otimização de custos."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa almacena 20 petabytes de datos en 2.000 buckets de Amazon S3 en 50 cuentas de AWS en AWS Organizations. El Director de Seguridad de la Información (CISO) y el CFO requieren visibilidad en toda la organización sobre el uso del almacenamiento, identificación de buckets sin cifrado predeterminado y recomendaciones prácticas para descubrir cargas multiparte incompletas y marcadores de eliminación de versiones huérfanos. ¿Qué solución proporciona estas métricas para toda la organización con el MENOR esfuerzo?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar Amazon S3 Storage Lens con un panel a nivel de organización en la cuenta de administración de AWS Organizations y exportar métricas diariamente a un bucket de S3.",
                    "explanation": "Correcto: Amazon S3 Storage Lens proporciona visibilidad en toda la organización del almacenamiento de objetos, métricas de actividad y recomendaciones de optimización de costos en todas las cuentas de AWS Organizations."
                },
                {
                    "id": "B",
                    "text": "Escribir un script de Python en una instancia EC2 que llame a la API s3:ListObjectsV2 en los 2.000 buckets diariamente y escriba los resultados en Amazon DynamoDB.",
                    "explanation": "Incorrecto: Llamar a ListObjectsV2 en 20 PB de datos genera costos masivos de API, latencia y mantenimiento operativo."
                },
                {
                    "id": "C",
                    "text": "Implementar reglas de AWS Config en cada cuenta y consultar el AWS Config Aggregator.",
                    "explanation": "Incorrecto: AWS Config realiza un seguimiento de las configuraciones de metadatos de buckets, pero no puede proporcionar análisis de almacenamiento detallados, métricas de actividad a nivel de prefijo o análisis de cargas multiparte incompletas como S3 Storage Lens."
                },
                {
                    "id": "D",
                    "text": "Habilitar el registro de acceso al servidor de S3 (S3 Server Access Logging) en cada bucket y usar Amazon Athena para analizar los registros de texto sin procesar diariamente.",
                    "explanation": "Incorrecto: Analizar miles de millones de líneas de registros de acceso sin procesar en Athena genera costos sustanciales de consulta y operativos en comparación con S3 Storage Lens nativo."
                }
            ],
            "generalExplanation": "Amazon S3 Storage Lens es una funcionalidad de análisis de almacenamiento en la nube que ofrece visibilidad en toda la organización sobre el uso del almacenamiento de objetos, tendencias de actividad y recomendaciones para optimizar costos."
        }
    },
    "sap-sim1-q016": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa com centenas de instâncias Amazon EC2, volumes EBS e funções Lambda em 40 contas deseja otimizar a utilização de recursos e eliminar gastos com infraestrutura superdimensionada. A solução deve usar análise de machine learning de métricas históricas do CloudWatch (incluindo utilização de memória por meio do agente CloudWatch) para gerar recomendações de dimensionamento ideal (right-sizing) em todas as contas. Qual serviço deve ser configurado?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Budgets para configurar notificações mensais de gastos por conta.",
                    "explanation": "Incorreto: O AWS Budgets rastreia limites de gastos, mas não analisa métricas de CPU/memória para recomendar alterações específicas no tipo e tamanho de instâncias."
                },
                {
                    "id": "B",
                    "text": "Implantar canários do Amazon CloudWatch Synthetics para monitorar a latência de endpoints da web.",
                    "explanation": "Incorreto: O CloudWatch Synthetics monitora a disponibilidade de endpoints, não o dimensionamento de recursos de computação."
                },
                {
                    "id": "C",
                    "text": "Ativar o AWS Compute Optimizer na conta de gerenciamento do AWS Organizations com acesso de administrador delegado e habilitar métricas de infraestrutura aprimoradas.",
                    "explanation": "Correto: O AWS Compute Optimizer usa machine learning para analisar a utilização histórica de recursos (incluindo memória quando o agente do CloudWatch está instalado) em todas as contas da organização e recomenda configurações ideais de computação e armazenamento."
                },
                {
                    "id": "D",
                    "text": "Configurar verificações básicas do AWS Trusted Advisor em cada conta-membro.",
                    "explanation": "Incorreto: O Trusted Advisor Básico fornece apenas verificações essenciais limitadas e não possui recomendações de right-sizing com ML para múltiplas contas."
                }
            ],
            "generalExplanation": "O AWS Compute Optimizer recomenda recursos ideais da AWS para suas cargas de trabalho a fim de reduzir custos e melhorar o desempenho, usando machine learning para analisar métricas históricas de utilização."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa con cientos de instancias de Amazon EC2, volúmenes EBS y funciones Lambda en 40 cuentas desea optimizar la utilización de recursos y eliminar el gasto en infraestructura sobreaprovisionada. La solución debe utilizar el análisis de aprendizaje automático (machine learning) de métricas históricas de CloudWatch (incluida la utilización de memoria a través del agente de CloudWatch) para generar recomendaciones de dimensionamiento adecuado (right-sizing) en todas las cuentas. ¿Qué servicio se debe configurar?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar AWS Budgets para configurar notificaciones de gastos mensuales por cuenta.",
                    "explanation": "Incorrecto: AWS Budgets realiza un seguimiento de los umbrales de gasto, pero no analiza las métricas de CPU/memoria para recomendar cambios específicos en el tamaño de instancias."
                },
                {
                    "id": "B",
                    "text": "Implementar canarios de Amazon CloudWatch Synthetics para monitorear la latencia de endpoints web.",
                    "explanation": "Incorrecto: CloudWatch Synthetics monitorea la disponibilidad de endpoints, no el dimensionamiento adecuado del cómputo."
                },
                {
                    "id": "C",
                    "text": "Activar AWS Compute Optimizer en la cuenta de administración de AWS Organizations con acceso de administrador delegado y habilitar métricas de infraestructura mejoradas.",
                    "explanation": "Correcto: AWS Compute Optimizer utiliza machine learning para analizar la utilización histórica de recursos (incluida la memoria cuando el agente de CloudWatch está instalado) en todas las cuentas de la organización y recomienda configuraciones óptimas de cómputo y almacenamiento."
                },
                {
                    "id": "D",
                    "text": "Configurar verificaciones de AWS Trusted Advisor Básico en cada cuenta miembro.",
                    "explanation": "Incorrecto: Trusted Advisor Básico solo proporciona verificaciones esenciales limitadas y carece de recomendaciones de dimensionamiento con ML para múltiples cuentas."
                }
            ],
            "generalExplanation": "AWS Compute Optimizer recomienda recursos de AWS óptimos para sus cargas de trabajo para reducir costos y mejorar el rendimiento mediante el uso de machine learning para analizar métricas de utilización históricas."
        }
    },
    "sap-sim1-q017": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma aplicação distribuída de microsserviços em execução no Amazon EKS e no AWS Lambda apresenta picos intermitentes de latência que afetam as transações de checkout. A equipe de engenharia precisa de rastreamento distribuído de ponta a ponta para mapear todo o grafo de requisições entre microsserviços, isolar consultas lentas de banco de dados e identificar gargalos de APIs downstream em tempo real. Qual serviço o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o VPC Flow Logs em todas as sub-redes do EKS e analisar o descarte de pacotes no Amazon Athena.",
                    "explanation": "Incorreto: Os VPC Flow Logs capturam metadados de rede de Camada 4, não árvores de chamadas em nível de aplicação, cabeçalhos HTTP ou spans de rastreamento de microsserviços."
                },
                {
                    "id": "B",
                    "text": "Configurar filtros de métricas do Amazon CloudWatch para contar ocorrências de erros HTTP 500 em arquivos de log.",
                    "explanation": "Incorreto: Os filtros de métricas contam ocorrências em logs, mas não fornecem rastreamento distribuído ou mapeamento de grafos de serviços entre microsserviços assíncronos."
                },
                {
                    "id": "C",
                    "text": "Configurar e implantar o Amazon GuardDuty no cluster EKS seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O GuardDuty é um serviço de detecção de ameaças de segurança, não uma ferramenta de rastreamento de desempenho de aplicações."
                },
                {
                    "id": "D",
                    "text": "Instrumentar os microsserviços da aplicação com o AWS X-Ray (ou AWS Distro for OpenTelemetry) para gerar mapas de rastreamento e analisar latências de segmentos no CloudWatch ServiceLens.",
                    "explanation": "Correto: O AWS X-Ray e o AWS Distro for OpenTelemetry (ADOT) fornecem rastreamento distribuído, gerando mapas de serviço e detalhamento minucioso da latência de subsegmentos entre microsserviços e bancos de dados."
                }
            ],
            "generalExplanation": "O AWS X-Ray ajuda desenvolvedores a analisar e depurar aplicações distribuídas, como aquelas construídas usando uma arquitetura de microsserviços, fornecendo mapas visuais de serviços e rastreamento de requisições."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una aplicación distribuida de microservicios que se ejecuta en Amazon EKS y AWS Lambda experimenta picos de latencia intermitentes que afectan las transacciones de pago (checkout). El equipo de ingeniería necesita un seguimiento distribuido de extremo a extremo para mapear todo el gráfico de solicitudes entre microservicios, aislar consultas lentas a bases de datos e identificar cuellos de botella en APIs downstream en tiempo real. ¿Qué servicio debería implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar VPC Flow Logs en todas las subredes de EKS y analizar la pérdida de paquetes en Amazon Athena.",
                    "explanation": "Incorrecto: Los registros de VPC Flow Logs capturan metadatos de red de Capa 4, no árboles de llamadas a nivel de aplicación, encabezados HTTP o tramos de seguimiento de microservicios."
                },
                {
                    "id": "B",
                    "text": "Configurar filtros de métricas de Amazon CloudWatch para contar cadenas de errores HTTP 500 en archivos de registro.",
                    "explanation": "Incorrecto: Los filtros de métricas cuentan apariciones en registros, pero no proporcionan seguimiento distribuido ni mapeo de gráficos de servicios a través de microservicios asíncronos."
                },
                {
                    "id": "C",
                    "text": "Configurar e implementar Amazon GuardDuty en el clúster de EKS siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: GuardDuty es un servicio de detección de amenazas de seguridad, no una herramienta de seguimiento del rendimiento de aplicaciones."
                },
                {
                    "id": "D",
                    "text": "Instrumentar los microservicios de aplicaciones con AWS X-Ray (o AWS Distro for OpenTelemetry) para generar mapas de seguimiento y analizar latencias de segmentos en CloudWatch ServiceLens.",
                    "explanation": "Correcto: AWS X-Ray y AWS Distro for OpenTelemetry (ADOT) proporcionan seguimiento distribuido, generando mapas de servicios y desgloses detallados de latencia de subsegmentos en microservicios y bases de datos."
                }
            ],
            "generalExplanation": "AWS X-Ray ayuda a los desarrolladores a analizar y depurar aplicaciones distribuidas, como las creadas mediante una arquitectura de microservicios, proporcionando mapas de servicios visuales y seguimiento de solicitudes."
        }
    },
    "sap-sim1-q018": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Um arquiteto de soluções está auditando uma aplicação financeira de missão crítica para garantir que ela possa resistir a falhas de Zonas de Disponibilidade e failovers de banco de dados sem intervenção manual. O arquiteto deseja executar experimentos controlados de engenharia do caos em ambientes de produção e homologação para injetar falhas do mundo real (como encerrar instâncias EC2, drenar AZs e induzir failovers de banco de dados) de maneira segura e controlada, com condições de parada automatizadas. Qual serviço da AWS deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "Assinar o AWS Shield Advanced para fornecer mitigação dedicada contra ataques DDoS e acesso 24/7 à equipe de resposta a DDoS (DDoS Response Team).",
                    "explanation": "Incorreto: O Shield Advanced é um serviço de mitigação de DDoS, não uma ferramenta de injeção de falhas para engenharia do caos."
                },
                {
                    "id": "B",
                    "text": "Configurar o AWS Systems Manager Patch Manager para automatizar linhas de base de patches de sistema operacional em todas as instâncias EC2.",
                    "explanation": "Incorreto: O Patch Manager automatiza a aplicação de patches no sistema operacional, e não a injeção de falhas de engenharia do caos."
                },
                {
                    "id": "C",
                    "text": "Implantar o AWS Fault Injection Service (AWS FIS) para executar experimentos controlados de engenharia do caos com condições de parada automatizadas em todos os recursos.",
                    "explanation": "Correto: O AWS Fault Injection Service (AWS FIS) é um serviço totalmente gerenciado para executar experimentos de injeção de falhas em cargas de trabalho da AWS para testar a resiliência e validar mecanismos de failover com condições de parada integradas."
                },
                {
                    "id": "D",
                    "text": "Implantar AWS Config Conformance Packs em todas as contas para avaliar a conformidade de recursos em relação às regras de governança corporativa.",
                    "explanation": "Incorreto: Os pacotes de conformidade avaliam a conformidade com regras de governança, não realizam injeção ativa de falhas."
                }
            ],
            "generalExplanation": "O AWS Fault Injection Service (AWS FIS) permite realizar experimentos controlados de engenharia do caos na infraestrutura da AWS para aprimorar a resiliência da aplicação e validar procedimentos de recuperação."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Un arquitecto de soluciones está auditando una aplicación financiera de misión crítica para garantizar que pueda sobrevivir a fallas en Zonas de Disponibilidad y conmutaciones por error de bases de datos sin intervención manual. El arquitecto desea ejecutar experimentos controlados de ingeniería del caos en entornos de producción y pruebas (staging) para inyectar fallos reales (como terminar instancias EC2, drenar AZs e inducir conmutaciones por error de bases de datos) de manera segura y controlada con condiciones de parada automatizadas. ¿Qué servicio de AWS se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Suscribirse a AWS Shield Advanced para proporcionar mitigación dedicada de ataques DDoS y acceso 24/7 al equipo de respuesta a DDoS (DDoS Response Team).",
                    "explanation": "Incorrecto: Shield Advanced es un servicio de mitigación de DDoS, no una herramienta de inyección para ingeniería del caos."
                },
                {
                    "id": "B",
                    "text": "Configurar AWS Systems Manager Patch Manager para automatizar líneas base de parches del sistema operativo en todas las instancias EC2.",
                    "explanation": "Incorrecto: Patch Manager automatiza la aplicación de parches del sistema operativo, no la inyección de fallos de ingeniería del caos."
                },
                {
                    "id": "C",
                    "text": "Implementar AWS Fault Injection Service (AWS FIS) para ejecutar experimentos controlados de ingeniería del caos con condiciones de parada automatizadas en todos los recursos.",
                    "explanation": "Correcto: AWS Fault Injection Service (AWS FIS) es un servicio totalmente administrado para ejecutar experimentos de inyección de fallas en cargas de trabajo de AWS para probar la resiliencia y validar los mecanismos de conmutación por error con condiciones de parada integradas."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS Config Conformance Packs en todas las cuentas para evaluar el cumplimiento de los recursos con respecto a las reglas de gobernanza corporativa.",
                    "explanation": "Incorrecto: Los paquetes de conformidad evalúan el cumplimiento de las reglas de gobernanza, no la inyección activa de fallos."
                }
            ],
            "generalExplanation": "AWS Fault Injection Service (AWS FIS) permite realizar experimentos controlados de ingeniería del caos en la infraestructura de AWS para mejorar la resiliencia de las aplicaciones y validar los procedimientos de recuperación."
        }
    },
    "sap-sim1-q019": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma equipe de DevOps gerencia a infraestrutura em 50 contas AWS usando o AWS CloudFormation. Com o tempo, membros da equipe fizeram modificações manuais de emergência diretamente no Console de Gerenciamento da AWS em grupos de segurança e tabelas de rotas. A equipe precisa detectar todas as alterações manuais fora de banda nas pilhas (stacks) existentes sem modificar os recursos ativos. Qual recurso do CloudFormation eles devem usar?",
            "options": [
                {
                    "id": "A",
                    "text": "Revisar o Histórico de Eventos do AWS CloudTrail no console para identificar eventos históricos de modificação de API.",
                    "explanation": "Incorreto: O CloudTrail registra chamadas de API, mas não fornece uma comparação de estado declarativa com relação aos modelos do CloudFormation."
                },
                {
                    "id": "B",
                    "text": "Criar AWS CloudFormation Change Sets para visualizar as modificações propostas na infraestrutura antes da implantação da pilha.",
                    "explanation": "Incorreto: Os Change Sets mostram quais alterações ocorrerão ao enviar um novo modelo, mas não verificam as pilhas ativas em busca de edições manuais feitas no console no passado."
                },
                {
                    "id": "C",
                    "text": "Configurar gatilhos de reversão (Rollback Triggers) do AWS CloudFormation para monitorar alarmes do CloudWatch e cancelar implantações de pilha com falha.",
                    "explanation": "Incorreto: Os Rollback Triggers monitoram alarmes do CloudWatch durante atualizações de pilha para reverter falhas."
                },
                {
                    "id": "D",
                    "text": "Executar a Detecção de Desvio (Drift Detection) do AWS CloudFormation nas pilhas existentes para identificar modificações manuais de recursos fora de banda.",
                    "explanation": "Correto: O CloudFormation Drift Detection identifica alterações feitas nos recursos da pilha fora do gerenciamento do CloudFormation, exibindo as diferenças entre a configuração esperada no modelo e o estado real do recurso em execução."
                }
            ],
            "generalExplanation": "O CloudFormation Drift Detection permite detectar se a configuração real de uma pilha desviou da configuração esperada no seu modelo devido a atualizações manuais fora de banda."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Un equipo de DevOps administra infraestructura en 50 cuentas de AWS mediante AWS CloudFormation. Con el tiempo, los miembros del equipo han realizado modificaciones manuales de emergencia directamente en la Consola de administración de AWS en grupos de seguridad y tablas de rutas. El equipo necesita detectar todos los cambios manuales fuera de banda en las pilas (stacks) existentes sin modificar los recursos activos. ¿Qué característica de CloudFormation deberían usar?",
            "options": [
                {
                    "id": "A",
                    "text": "Revisar el Historial de eventos de AWS CloudTrail en la consola para identificar eventos históricos de modificación de API.",
                    "explanation": "Incorrecto: CloudTrail registra llamadas a la API, pero no proporciona una comparación declarativa del estado con respecto a las plantillas de CloudFormation."
                },
                {
                    "id": "B",
                    "text": "Crear AWS CloudFormation Change Sets para previsualizar las modificaciones propuestas a la infraestructura antes de la implementación de la pila.",
                    "explanation": "Incorrecto: Los Change Sets muestran qué cambios ocurrirán al enviar una nueva plantilla, pero no analizan las pilas activas en busca de ediciones manuales anteriores en la consola."
                },
                {
                    "id": "C",
                    "text": "Configurar desencadenadores de reversión (Rollback Triggers) de AWS CloudFormation para monitorear alarmas de CloudWatch y cancelar implementaciones de pilas fallidas.",
                    "explanation": "Incorrecto: Los desencadenadores de reversión monitorean alarmas de CloudWatch durante las actualizaciones de la pila para revertir fallos."
                },
                {
                    "id": "D",
                    "text": "Ejecutar la Detección de Desviación (Drift Detection) de AWS CloudFormation en las pilas existentes para identificar modificaciones manuales de recursos fuera de banda.",
                    "explanation": "Correcto: CloudFormation Drift Detection identifica los cambios realizados en los recursos de la pila fuera de la administración de CloudFormation, mostrando las diferencias entre la configuración esperada de la plantilla y el estado real del recurso en ejecución."
                }
            ],
            "generalExplanation": "CloudFormation Drift Detection le permite detectar si la configuración real de una pila se ha desviado de la configuración esperada de su plantilla debido a actualizaciones manuales fuera de banda."
        }
    },
    "sap-sim1-q020": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Um banco de dados em uma instância Amazon EC2 está ficando sem espaço em disco em um volume Amazon EBS gp3 anexado. A capacidade de armazenamento deve ser aumentada de 500 GB para 2 TB e o IOPS deve ser aumentado de 3.000 para 10.000. O banco de dados de produção não pode tolerar nenhum tempo de inatividade nem desanexação de volume durante essa alteração. Como o arquiteto deve executar essa modificação?",
            "options": [
                {
                    "id": "A",
                    "text": "Exportar tabelas do banco de dados para o Amazon S3 e restaurá-las em um cluster do Amazon Aurora.",
                    "explanation": "Incorreto: A migração para o Aurora é um projeto complexo de replataformização de banco de dados que requer tempo de inatividade planejado."
                },
                {
                    "id": "B",
                    "text": "Parar a instância EC2, criar um snapshot do EBS, restaurar o snapshot em um novo volume de 2 TB, anexar o novo volume e reiniciar a instância.",
                    "explanation": "Incorreto: Parar a instância EC2 introduz tempo de inatividade no banco de dados de produção."
                },
                {
                    "id": "C",
                    "text": "Anexar um segundo volume de 1,5 TB e criar um array RAID 0 de software em ambos os volumes enquanto o banco de dados estiver em execução.",
                    "explanation": "Incorreto: A criação de uma nova matriz RAID requer a formatação de discos e a reinicialização dos processos de banco de dados, causando tempo de inatividade e riscos de migração de dados."
                },
                {
                    "id": "D",
                    "text": "Usar o Amazon EBS Elastic Volumes para modificar o tamanho do volume e o IOPS provisionado dinamicamente no local, sem desanexar o volume ou parar a instância EC2, e em seguida estender o sistema de arquivos no nível do sistema operacional.",
                    "explanation": "Correto: O Amazon EBS Elastic Volumes permite a modificação dinâmica de tamanho, IOPS e tipo de volume em instâncias em execução com zero tempo de inatividade, exigindo apenas um comando de extensão do sistema de arquivos no nível do SO posteriormente."
                }
            ],
            "generalExplanation": "O recurso Amazon EBS Elastic Volumes permite a modificação em tempo de execução do tamanho do volume, IOPS e taxa de transferência sem desanexar o volume ou reiniciar a instância."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una base de datos en una instancia de Amazon EC2 se está quedando sin espacio en disco en un volumen Amazon EBS gp3 adjunto. La capacidad de almacenamiento debe aumentarse de 500 GB a 2 TB, y las IOPS deben aumentarse de 3.000 a 10.000. La base de datos de producción no puede tolerar ningún tiempo de inactividad ni la desconexión del volumen durante este cambio. ¿Cómo debería ejecutar esta modificación el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Exportar tablas de base de datos a Amazon S3 y restaurarlas en un clúster de Amazon Aurora.",
                    "explanation": "Incorrecto: Migrar a Aurora es un proyecto complejo de replataformado de bases de datos que requiere tiempo de inactividad planificado."
                },
                {
                    "id": "B",
                    "text": "Detener la instancia EC2, tomar una instantánea (snapshot) de EBS, restaurar el snapshot en un nuevo volumen de 2 TB, adjuntar el nuevo volumen y reiniciar la instancia.",
                    "explanation": "Incorrecto: Detener la instancia EC2 introduce tiempo de inactividad en la base de datos de producción."
                },
                {
                    "id": "C",
                    "text": "Adjuntar un segundo volumen de 1,5 TB y crear una matriz RAID 0 por software en ambos volúmenes mientras la base de datos está en ejecución.",
                    "explanation": "Incorrecto: Crear una nueva matriz RAID requiere formatear discos y reiniciar procesos de base de datos, lo que provoca tiempo de inactividad y riesgos de migración de datos."
                },
                {
                    "id": "D",
                    "text": "Usar Amazon EBS Elastic Volumes para modificar el tamaño del volumen y las IOPS aprovisionadas dinámicamente en el lugar sin desconectar el volumen ni detener la instancia EC2, y luego extender el sistema de archivos a nivel del sistema operativo.",
                    "explanation": "Correcto: Amazon EBS Elastic Volumes permite la modificación dinámica del tamaño, las IOPS y el tipo de volumen en instancias en ejecución con cero tiempo de inactividad, lo que solo requiere un comando de extensión del sistema de archivos a nivel de SO posteriormente."
                }
            ],
            "generalExplanation": "Amazon EBS Elastic Volumes permite la modificación en vivo del tamaño del volumen, IOPS y rendimiento (throughput) sin desconectar el volumen ni reiniciar la instancia."
        }
    },
    "sap-sim1-q021": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa precisa migrar 400 máquinas virtuais VMware locais (executando Linux e Windows) para o Amazon EC2 com tempo de inatividade mínimo de transição (cutover de menos de 15 minutos por servidor) e replicação contínua de dados em nível de bloco através de uma conexão existente do AWS Direct Connect. Qual serviço da AWS é a ferramenta principal recomendada para essa migração lift-and-shift?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar o conector herdado do AWS Server Migration Service (AWS SMS) para criar backups periódicos de snapshots do hipervisor.",
                    "explanation": "Incorreto: O AWS SMS é um serviço herdado baseado em snapshots descontinuado em favor do AWS MGN."
                },
                {
                    "id": "B",
                    "text": "Implantar o AWS Application Migration Service (AWS MGN) para realizar replicação contínua de servidores em nível de bloco sem interrupções para a AWS.",
                    "explanation": "Correto: O AWS Application Migration Service (AWS MGN) é o principal serviço da AWS para migrações lift-and-shift, realizando replicação contínua em nível de bloco sem interrupções para uma área de preparação (staging) de baixo custo na AWS para uma transição rápida."
                },
                {
                    "id": "C",
                    "text": "Solicitar um appliance físico AWS Snowball Edge Storage Optimized para transportar imagens de disco de servidores offline.",
                    "explanation": "Incorreto: O Snowball Edge é para transferência de dados offline em lote, não para replicação contínua em nível de bloco para transições ao vivo."
                },
                {
                    "id": "D",
                    "text": "Implantar agentes do AWS DataSync nas máquinas virtuais locais para transferir sistemas de arquivos para o Amazon S3.",
                    "explanation": "Incorreto: O AWS DataSync migra dados de arquivos e objetos, e não volumes de inicialização de sistemas operacionais em execução com orquestração automatizada de cutover."
                }
            ],
            "generalExplanation": "O AWS Application Migration Service (AWS MGN) minimiza processos manuais demorados ao converter automaticamente seus servidores de origem de infraestruturas físicas, virtuais ou em nuvem para execução nativa na AWS."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa necesita migrar 400 máquinas virtuales VMware locales (que ejecutan Linux y Windows) a Amazon EC2 con un tiempo de inactividad de corte (cutover) mínimo (menos de 15 minutos por servidor) y replicación continua de datos a nivel de bloque a través de una conexión existente de AWS Direct Connect. ¿Qué servicio de AWS es la herramienta principal recomendada para esta migración tipo lift-and-shift?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar el conector heredado de AWS Server Migration Service (AWS SMS) para crear copias de seguridad periódicas de snapshots del hipervisor.",
                    "explanation": "Incorrecto: AWS SMS es un servicio heredado basado en snapshots que ha sido sustituido por AWS MGN."
                },
                {
                    "id": "B",
                    "text": "Implementar AWS Application Migration Service (AWS MGN) para realizar una replicación continua de servidores a nivel de bloque sin interrupciones en AWS.",
                    "explanation": "Correcto: AWS Application Migration Service (AWS MGN) es el principal servicio de AWS para migraciones lift-and-shift, realizando replicación continua a nivel de bloque sin interrupciones en un área de preparación de bajo costo en AWS para una conmutación rápida."
                },
                {
                    "id": "C",
                    "text": "Solicitar un dispositivo físico AWS Snowball Edge Storage Optimized para transportar imágenes de disco de servidores sin conexión (offline).",
                    "explanation": "Incorrecto: Snowball Edge es para transferencia masiva de datos fuera de línea, no para replicación continua a nivel de bloque para transiciones en vivo."
                },
                {
                    "id": "D",
                    "text": "Implementar agentes de AWS DataSync en máquinas virtuales locales para transferir sistemas de archivos a Amazon S3.",
                    "explanation": "Incorrecto: AWS DataSync migra datos de archivos y objetos, no volúmenes de arranque del sistema operativo en ejecución con orquestación automatizada de corte."
                }
            ],
            "generalExplanation": "AWS Application Migration Service (AWS MGN) minimiza los procesos manuales que consumen mucho tiempo al convertir automáticamente sus servidores de origen desde infraestructura física, virtual o en la nube para ejecutarse de forma nativa en AWS."
        }
    },
    "sap-sim1-q022": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa está migrando um banco de dados Oracle local de 15 TB com stored procedures e triggers personalizados para um cluster Amazon Aurora PostgreSQL. A migração deve ocorrer com tempo de inatividade quase zero, enquanto as transações comerciais continuam no ambiente local até a transição (cutover) final. Qual combinação de ferramentas de migração da AWS deve ser usada?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o Oracle Data Pump para exportar arquivos de dump para o S3 e escrever scripts Python personalizados para converter PL/SQL em PL/pgSQL.",
                    "explanation": "Incorreto: A conversão manual de procedimentos de banco de dados por scripts personalizados é propensa a erros, e a exportação do Data Pump cria um longo tempo de inatividade durante o cutover."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS DataSync para copiar arquivos de dados brutos do banco de dados Oracle diretamente para um volume EBS do Aurora PostgreSQL.",
                    "explanation": "Incorreto: O DataSync não pode converter formatos de dados de bancos de dados heterogêneos (os blocos binários proprietários do Oracle não podem ser lidos diretamente pelo mecanismo PostgreSQL)."
                },
                {
                    "id": "C",
                    "text": "Implantar o AWS Application Migration Service (AWS MGN) para replicar o servidor Oracle diretamente para uma instância Amazon EC2 executando PostgreSQL.",
                    "explanation": "Incorreto: O AWS MGN é uma ferramenta de migração de servidor em nível de bloco e não converte esquemas de banco de dados entre mecanismos de banco de dados heterogêneos."
                },
                {
                    "id": "D",
                    "text": "Usar o AWS Schema Conversion Tool (AWS SCT) para converter o esquema do banco de dados Oracle, stored procedures e triggers para PostgreSQL e, em seguida, usar o AWS Database Migration Service (AWS DMS) com Full Load e Change Data Capture (CDC) para sincronizar dados continuamente até o cutover.",
                    "explanation": "Correto: O AWS SCT converte esquemas e código de bancos de dados heterogêneos (Oracle para PostgreSQL), enquanto o AWS DMS executa o carregamento inicial completo e a replicação contínua com CDC para manter os dados sincronizados até a virada."
                }
            ],
            "generalExplanation": "As migrações de bancos de dados heterogêneos requerem o AWS SCT (para converter esquemas, views e stored procedures) combinado com o AWS DMS (para replicar dados históricos e transmitir alterações contínuas via CDC)."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa está migrando una base de datos Oracle local de 15 TB con procedimientos almacenados (stored procedures) y desencadenadores (triggers) personalizados a un clúster de Amazon Aurora PostgreSQL. La migración debe ocurrir con un tiempo de inactividad casi nulo mientras las transacciones comerciales continúan en el entorno local hasta el corte final (cutover). ¿Qué combinación de herramientas de migración de AWS se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar Oracle Data Pump para exportar archivos de volcado (dump) a S3 y escribir scripts de Python personalizados para convertir PL/SQL a PL/pgSQL.",
                    "explanation": "Incorrecto: La conversión mediante scripts personalizados de procedimientos de base de datos es propensa a errores, y la exportación de Data Pump genera un tiempo de inactividad prolongado durante el corte."
                },
                {
                    "id": "B",
                    "text": "Usar AWS DataSync para copiar archivos de datos sin procesar de la base de datos Oracle directamente en un volumen EBS de Aurora PostgreSQL.",
                    "explanation": "Incorrecto: DataSync no puede convertir formatos de datos de bases de datos heterogéneas (los bloques binarios propietarios de Oracle no pueden ser leídos directamente por el motor de PostgreSQL)."
                },
                {
                    "id": "C",
                    "text": "Implementar AWS Application Migration Service (AWS MGN) para replicar el servidor Oracle directamente en una instancia de Amazon EC2 que ejecuta PostgreSQL.",
                    "explanation": "Incorrecto: AWS MGN es una herramienta de migración de servidores a nivel de bloque y no convierte esquemas de bases de datos entre motores de bases de datos heterogéneos."
                },
                {
                    "id": "D",
                    "text": "Usar AWS Schema Conversion Tool (AWS SCT) para convertir el esquema de la base de datos Oracle, procedimientos almacenados y triggers a PostgreSQL, y luego usar AWS Database Migration Service (AWS DMS) con Full Load y Change Data Capture (CDC) para sincronizar datos continuamente hasta el corte.",
                    "explanation": "Correcto: AWS SCT convierte esquemas y código de bases de datos heterogéneas (Oracle a PostgreSQL), mientras que AWS DMS realiza la carga inicial completa y la replicación continua con CDC para mantener los datos sincronizados hasta la conmutación final."
                }
            ],
            "generalExplanation": "Las migraciones de bases de datos heterogéneas requieren AWS SCT (para convertir esquemas, vistas y procedimientos almacenados) combinado con AWS DMS (para replicar datos históricos y transmitir cambios continuos de CDC)."
        }
    },
    "sap-sim1-q023": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Um centro de pesquisa de imagens médicas precisa migrar 500 TB de imagens DICOM armazenadas em um storage NAS (Network Attached Storage) local para o Amazon S3. A instalação possui uma conexão dedicada de 1 Gbps do AWS Direct Connect. A migração deve automatizar a otimização de rede, criptografia de dados em trânsito, preservação de metadados de arquivos (permissões POSIX, carimbos de data/hora) e verificação de integridade de dados usando somas de verificação (checksums) sem scripts personalizados. Qual serviço o arquiteto deve implantar?",
            "options": [
                {
                    "id": "A",
                    "text": "Montar o NAS local em uma instância EC2 e executar o comando CLI `aws s3 sync` por meio de um cron job.",
                    "explanation": "Incorreto: O `aws s3 sync` executado em uma instância EC2 opera em thread única, não possui otimização acelerada de rede para multipart uploads e não preserva metadados POSIX nativamente."
                },
                {
                    "id": "B",
                    "text": "Solicitar um appliance AWS Snowball Edge Storage Optimized e copiar os arquivos manualmente via SCP.",
                    "explanation": "Incorreto: O Snowball exige atrasos de remessa física, enquanto 500 TB podem ser transferidos perfeitamente pela conexão existente de 1 Gbps do Direct Connect usando o DataSync automatizado."
                },
                {
                    "id": "C",
                    "text": "Usar o AWS Storage Gateway File Gateway para espelhar todos os arquivos continuamente.",
                    "explanation": "Incorreto: O File Gateway foi projetado para acesso híbrido com cache, não para migração massiva em lote de 500 TB com verificação automatizada de tarefas."
                },
                {
                    "id": "D",
                    "text": "Implantar um agente do AWS DataSync no ambiente local e configurar uma tarefa do DataSync com controle de largura de banda e verificação habilitadas para transferir dados diretamente do NAS para o Amazon S3.",
                    "explanation": "Correto: O AWS DataSync foi desenvolvido especificamente para transferências automatizadas e de alta velocidade de arquivos de sistemas NAS/NFS locais para o S3, preservando metadados POSIX e realizando validação automatizada de integridade de dados de ponta a ponta."
                }
            ],
            "generalExplanation": "O AWS DataSync acelera e automatiza a transferência de grandes volumes de dados entre o armazenamento local e os serviços de armazenamento da AWS, com criptografia integrada, verificação e preservação de metadados."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Un centro de investigación de imágenes médicas necesita migrar 500 TB de imágenes DICOM almacenadas en una matriz de almacenamiento conectado a la red (NAS) local a Amazon S3. La instalación cuenta con una conexión dedicada de 1 Gbps de AWS Direct Connect. La migración debe automatizar la optimización de la red, el cifrado de datos en tránsito, la preservación de metadados de archivos (permisos POSIX, marcas de tiempo) y la verificación de la integridad de los datos mediante sumas de comprobación (checksums) sin scripts personalizados. ¿Qué servicio debería implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Montar el NAS local en una instancia EC2 y ejecutar el comando de CLI `aws s3 sync` a través de una tarea cron.",
                    "explanation": "Incorrecto: `aws s3 sync` a través de una instancia EC2 es de un solo hilo, carece de optimización de red acelerada de varias partes y no conserva los metadatos POSIX de forma nativa."
                },
                {
                    "id": "B",
                    "text": "Solicitar un dispositivo AWS Snowball Edge Storage Optimized y copiar archivos manualmente a través de SCP.",
                    "explanation": "Incorrecto: Snowball implica retrasos de envío físico, mientras que 500 TB se pueden transferir sin problemas a través de la conexión Direct Connect de 1 Gbps existente utilizando DataSync automatizado."
                },
                {
                    "id": "C",
                    "text": "Usar AWS Storage Gateway File Gateway para reflejar todos los archivos continuamente.",
                    "explanation": "Incorrecto: File Gateway está diseñado para acceso de almacenamiento en caché híbrido, no para la migración masiva de 500 TB con verificación de tareas automatizada."
                },
                {
                    "id": "D",
                    "text": "Implementar un agente de AWS DataSync en las instalaciones locales y configurar una tarea de DataSync con limitación de ancho de banda y verificación habilitada para transferir datos directamente desde el NAS a Amazon S3.",
                    "explanation": "Correcto: AWS DataSync está diseñado específicamente para transferencias automatizadas de archivos de alta velocidad desde sistemas NAS/NFS locales a S3, preservando metadatos POSIX y realizando una validación de integridad de datos de extremo a extremo automatizada."
                }
            ],
            "generalExplanation": "AWS DataSync acelera y automatiza la transferencia de grandes cantidades de datos entre el almacenamiento local y los servicios de almacenamiento de AWS, con cifrado integrado, verificación y preservación de metadados."
        }
    },
    "sap-sim1-q024": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa está planejando uma migração de data center em larga escala envolvendo 1.200 servidores. Antes da migração, a equipe de arquitetura corporativa precisa mapear as dependências de rede dos servidores, medir a utilização de desempenho (CPU, memória, E/S de disco), agrupar servidores inter-relacionados em ondas de migração (migration waves) e acompanhar o progresso da migração em várias ferramentas em um único painel. Qual combinação de serviços deve ser usada?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar agentes do Amazon CloudWatch em todos os servidores locais e consultar os logs do CloudWatch com o Amazon Athena.",
                    "explanation": "Incorreto: Os agentes do CloudWatch coletam logs e métricas, mas não fornecem mapeamento automatizado de dependências de rede de várias camadas nem agrupamento de ondas de migração."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS Config Aggregator para descobrir máquinas virtuais VMware locais.",
                    "explanation": "Incorreto: O AWS Config foi projetado para recursos na nuvem AWS, não para mapeamento de dependências de rede baseado em agentes em servidores locais."
                },
                {
                    "id": "C",
                    "text": "Implantar agentes do AWS Application Discovery Service em servidores locais para coletar dados detalhados de desempenho e dependência de rede, e visualizar e organizar ondas de migração no AWS Migration Hub.",
                    "explanation": "Correto: O AWS Application Discovery Service descobre configurações de servidor e dependências de rede, enquanto o AWS Migration Hub fornece um painel central para rastrear e organizar ondas de migração."
                },
                {
                    "id": "D",
                    "text": "Implantar o agente do AWS Systems Manager em todos os servidores locais e executar o AWS Systems Manager Inventory.",
                    "explanation": "Incorreto: O Systems Manager Inventory rastreia pacotes de software instalados, mas não fornece mapeamento visual de dependências de rede nem rastreamento de ondas de migração."
                }
            ],
            "generalExplanation": "O AWS Application Discovery Service coleta inventário de servidores e dados de dependência, que se integram perfeitamente ao AWS Migration Hub para planejar e rastrear ondas de migração."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa está planificando una migración de centro de datos a gran escala que involucra a 1.200 servidores. Antes de migrar, el equipo de arquitectura empresarial necesita mapear las dependencias de red del servidor, medir la utilización del rendimiento (CPU, memoria, E/S de disco), agrupar servidores interrelacionados en olas de migración (migration waves) y realizar un seguimiento del progreso de la migración en múltiples herramientas en un solo panel. ¿Qué combinación de servicios se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar agentes de Amazon CloudWatch en todos los servidores locales y consultar registros de CloudWatch con Amazon Athena.",
                    "explanation": "Incorrecto: Los agentes de CloudWatch recopilan registros de métricas, pero no proporcionan mapeo automatizado de dependencias de red de múltiples niveles ni agrupación de olas de migración."
                },
                {
                    "id": "B",
                    "text": "Usar AWS Config Aggregator para descubrir máquinas virtuales VMware locales.",
                    "explanation": "Incorrecto: AWS Config está diseñado para recursos en la nube de AWS, no para el mapeo de dependencias de red basado en agentes en servidores locales."
                },
                {
                    "id": "C",
                    "text": "Implementar agentes de AWS Application Discovery Service en servidores locales para recopilar datos detallados de rendimiento y dependencias de red, y ver y organizar olas de migración en AWS Migration Hub.",
                    "explanation": "Correcto: AWS Application Discovery Service descubre configuraciones de servidores y dependencias de red, mientras que AWS Migration Hub proporciona un panel central para rastrear y organizar olas de migración."
                },
                {
                    "id": "D",
                    "text": "Implementar el agente de AWS Systems Manager en todos los servidores locales y ejecutar AWS Systems Manager Inventory.",
                    "explanation": "Incorrecto: Systems Manager Inventory realiza un seguimiento de los paquetes de software instalados, pero no proporciona un mapeo visual de dependencias de red ni seguimiento de olas de migración."
                }
            ],
            "generalExplanation": "AWS Application Discovery Service recopila datos de inventario y dependencias de servidores, que se integran perfectamente en AWS Migration Hub para planificar y realizar el seguimiento de las olas de migración."
        }
    },
    "sap-sim1-q025": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Um banco deseja modernizar um sistema bancário central herdado em COBOL executado em mainframe IBM local para a AWS. O banco deseja fazer a transição para uma arquitetura nativa da nuvem refatorando a base de código COBOL em microsserviços Java implantados em plataformas gerenciadas de contêineres da AWS, com testes automatizados e pipelines de integração contínua. Qual serviço da AWS fornece o ambiente desenvolvido especificamente e ferramentas automatizadas para essa transformação?",
            "options": [
                {
                    "id": "A",
                    "text": "Serviço AWS Mainframe Modernization usando o padrão Automated Refactor (tecnologia AWS Blu Age)",
                    "explanation": "Correto: O serviço AWS Mainframe Modernization com o padrão Automated Refactor (AWS Blu Age) analisa, transforma e testa automaticamente aplicações legadas em COBOL de mainframes em microsserviços modernos baseados em Java."
                },
                {
                    "id": "B",
                    "text": "Implantar o AWS Application Migration Service (AWS MGN) para realizar replicação contínua de servidores em nível de bloco sem interrupções para a AWS.",
                    "explanation": "Incorreto: O AWS MGN realiza migração lift-and-shift em nível de bloco de máquinas virtuais/físicas x86 e não pode refatorar código COBOL de mainframe IBM z/OS para Java."
                },
                {
                    "id": "C",
                    "text": "Implantar tarefas do AWS Database Migration Service (AWS DMS) para replicar tabelas de banco de dados continuamente no Amazon Aurora.",
                    "explanation": "Incorreto: O AWS DMS migra bancos de dados, mas não refatora a lógica de aplicação de mainframe nem bases de código COBOL."
                },
                {
                    "id": "D",
                    "text": "Implantar aplicações pré-empacotadas do AWS Serverless Application Repository para substituir módulos bancários herdados.",
                    "explanation": "Incorreto: O Serverless Application Repository é um repositório para aplicações serverless pré-construídas, não uma plataforma de refatoração de mainframes."
                }
            ],
            "generalExplanation": "O AWS Mainframe Modernization fornece ferramentas gerenciadas e ambientes de execução para modernizar cargas de trabalho de mainframe, oferecendo refatoração automatizada via AWS Blu Age em microsserviços baseados em Java."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabalho",
            "statement": "Un banco desea modernizar un sistema bancario central heredado en COBOL que se ejecuta en un mainframe IBM local hacia AWS. El banco desea realizar la transición a una arquitectura nativa de la nube refactorizando la base de código COBOL en microservicios Java implementados en plataformas de contenedores administradas de AWS con pruebas automatizadas y canales de integración continua. ¿Qué servicio de AWS proporciona el entorno creado específicamente y las herramientas automatizadas para esta transformación?",
            "options": [
                {
                    "id": "A",
                    "text": "Servicio AWS Mainframe Modernization utilizando el patrón Automated Refactor (impulsado por AWS Blu Age)",
                    "explanation": "Correcto: El servicio AWS Mainframe Modernization con el patrón Automated Refactor (AWS Blu Age) analiza, transforma y prueba automáticamente aplicaciones heredadas de mainframe en COBOL en microservicios modernos basados en Java."
                },
                {
                    "id": "B",
                    "text": "Implementar AWS Application Migration Service (AWS MGN) para realizar una replicación continua de servidores a nivel de bloque sin interrupciones en AWS.",
                    "explanation": "Incorrecto: AWS MGN realiza lift-and-shift a nivel de bloque de máquinas virtuales/físicas x86, y no puede refactorizar código COBOL de mainframe IBM z/OS a Java."
                },
                {
                    "id": "C",
                    "text": "Implementar tareas de AWS Database Migration Service (AWS DMS) para replicar tablas de bases de datos continuamente en Amazon Aurora.",
                    "explanation": "Incorrecto: AWS DMS migra bases de datos, pero no refactoriza la lógica de aplicaciones de mainframe ni bases de código COBOL."
                },
                {
                    "id": "D",
                    "text": "Implementar aplicaciones preempaquetadas del AWS Serverless Application Repository para reemplazar módulos bancarios heredados.",
                    "explanation": "Incorrecto: Serverless Application Repository es un almacén para aplicaciones serverless prediseñadas, no una plataforma de refactorización de mainframes."
                }
            ],
            "generalExplanation": "AWS Mainframe Modernization proporciona herramientas administradas y entornos de tiempo de ejecución para modernizar las cargas de trabajo de mainframe, ofreciendo refactorización automatizada a través de AWS Blu Age en microservicios basados en Java."
        }
    }
}
