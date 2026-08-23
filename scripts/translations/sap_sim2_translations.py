# -*- coding: utf-8 -*-
"""
Translations for AWS Certified Solutions Architect - Professional (SAP-C02) Mock Exam 2.
Contains 100% natural, professional translations in Brazilian Portuguese (PT-BR) and Spanish (ES).
"""

TRANSLATIONS = {
    "sap-sim2-q001": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa com 200 contas AWS gerenciadas pelo AWS Organizations precisa de uma estratégia centralizada de registro de auditoria. Todos os eventos de API de gerenciamento e de dados em todas as regiões e contas devem ser entregues a um bucket do Amazon S3 centralizado e imutável, localizado em uma conta dedicada de Auditoria de Segurança. Os administradores das contas membros não devem conseguir modificar, adulterar ou excluir esses logs, e os logs devem ser criptografados com uma chave gerenciada pelo cliente rotacionada anualmente. Qual solução atende a esses requisitos de conformidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Amazon GuardDuty em todas as contas e configurar a exportação para o Amazon S3 na conta de gerenciamento.",
                    "explanation": "Incorreto: O GuardDuty gera descobertas de segurança, mas não fornece trilhas brutas e imutáveis de auditoria de API do CloudTrail para fins de conformidade."
                },
                {
                    "id": "B",
                    "text": "Implantar trilhas individuais do CloudTrail em cada conta membro usando um script de automação do AWS Systems Manager que grava em buckets locais do Amazon S3 em cada conta membro.",
                    "explanation": "Incorreto: Buckets locais nas contas membros podem ser excluídos ou modificados por administradores dessas contas, violando a imutabilidade da auditoria centralizada."
                },
                {
                    "id": "C",
                    "text": "Configurar filtros de assinatura do Amazon CloudWatch Logs em cada conta membro para transmitir logs para um cluster do Amazon OpenSearch Service na conta de gerenciamento.",
                    "explanation": "Incorreto: Os filtros de assinatura do CloudWatch transmitem logs de aplicativos e do sistema operacional, e não eventos abrangentes de gerenciamento e dados do CloudTrail em toda a organização AWS."
                },
                {
                    "id": "D",
                    "text": "Criar uma trilha da organização no AWS CloudTrail (Organization Trail) na conta de gerenciamento do Organizations com a validação de integridade de arquivos de log habilitada, entregando os logs em um bucket do Amazon S3 na conta de Auditoria de Segurança criptografado com uma chave KMS gerenciada pelo cliente (CMK), cuja política de chave conceda permissões ao CloudTrail e restrinja a descriptografia apenas à equipe de segurança.",
                    "explanation": "Correto: Uma trilha da organização registra automaticamente os eventos de todas as contas membros em um único bucket designado. A ativação da validação de integridade de log e o uso de uma CMK na conta de auditoria garantem trilhas de auditoria à prova de adulteração que as contas membros não podem desativar nem modificar."
                }
            ],
            "generalExplanation": "As trilhas de organização do AWS CloudTrail centralizam o registro de eventos de API em todas as contas de uma organização AWS, fornecendo trilhas de auditoria imutáveis e criptografadas com validação de resumo SHA-256."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa con 200 cuentas de AWS gobernadas por AWS Organizations necesita una estrategia centralizada de registro de auditoría. Todos los eventos de API de administración y de datos en todas las regiones y cuentas deben entregarse en un bucket de Amazon S3 centralizado e inmutable ubicado en una cuenta dedicada de Auditoría de Seguridad. Los administradores de las cuentas miembro no deben poder modificar, manipular ni eliminar estos registros, y los registros deben cifrarse con una clave administrada por el cliente rotada anualmente. ¿Qué solución cumple con estos requisitos de cumplimiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar Amazon GuardDuty en todas las cuentas y configurar la exportación a Amazon S3 en la cuenta de administración.",
                    "explanation": "Incorrecto: GuardDuty genera hallazgos de seguridad, pero no proporciona registros de auditoría de API sin procesar e inmutables de CloudTrail para el cumplimiento normativo."
                },
                {
                    "id": "B",
                    "text": "Implementar registros individuales de CloudTrail en cada cuenta miembro mediante un script de automatización de AWS Systems Manager que escriba en buckets locales de Amazon S3 en cada cuenta miembro.",
                    "explanation": "Incorrecto: Los buckets locales en las cuentas miembro pueden ser eliminados o modificados por administradores de esas cuentas, lo que viola la inmutabilidad de la auditoría centralizada."
                },
                {
                    "id": "C",
                    "text": "Configurar filtros de suscripción de Amazon CloudWatch Logs en cada cuenta miembro para transmitir registros a un clúster de Amazon OpenSearch Service en la cuenta de administración.",
                    "explanation": "Incorrecto: Los filtros de suscripción de CloudWatch transmiten registros de aplicaciones y del sistema operativo, no eventos completos de administración y datos de CloudTrail en toda la organización de AWS."
                },
                {
                    "id": "D",
                    "text": "Crear un registro de organización en AWS CloudTrail (Organization Trail) en la cuenta de administración de Organizations con la validación de integridad de archivos de registro habilitada, entregando en un bucket de Amazon S3 en la cuenta de Auditoría de Seguridad cifrado con una clave KMS administrada por el cliente (CMK), cuya directiva de clave otorgue permisos a CloudTrail y restrinja el descifrado al equipo de seguridad.",
                    "explanation": "Correcto: Un registro de organización registra automáticamente eventos en todas las cuentas miembro en un único bucket designado. Habilitar la validación de integridad del registro y usar una CMK en la cuenta de auditoría garantiza registros de auditoría a prueba de manipulaciones que las cuentas miembro no pueden desactivar ni alterar."
                }
            ],
            "generalExplanation": "Las rutas de organización de AWS CloudTrail centralizan el registro de eventos de API en todas las cuentas de una organización de AWS, proporcionando pistas de auditoría inmutables y cifradas con validación de resumen SHA-256."
        }
    },
    "sap-sim2-q002": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma corporação farmacêutica exige segurança rigorosa de DNS e filtragem de domínios de saída em 40 VPCs distribuídas em 3 regiões da AWS. A arquitetura de segurança exige que todas as consultas DNS de saída das instâncias EC2 para a internet sejam inspecionadas e filtradas contra listas de domínios maliciosos (feeds de inteligência contra ameaças), enquanto a resolução de DNS privado para domínios corporativos (`internal.pharma.com`) deve ser roteada para servidores DNS locais (on-premises) por meio do AWS Direct Connect. Qual solução atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar o Amazon Route 53 Resolver DNS Firewall com listas de domínios gerenciadas associadas a todas as VPCs e configurar endpoints de saída do Route 53 Resolver (Outbound Endpoints) com regras de encaminhamento para `internal.pharma.com` apontando para os endereços IP do DNS local.",
                    "explanation": "Correto: O Route 53 Resolver DNS Firewall fornece filtragem de domínio na Camada 7 para consultas DNS de saída entre VPCs, enquanto os Outbound Endpoints do Route 53 Resolver encaminham consultas de domínios específicos para o DNS local através do Direct Connect."
                },
                {
                    "id": "B",
                    "text": "Instalar encaminhadores DNS BIND personalizados em instâncias do Amazon EC2 em cada sub-rede privada e editar o arquivo `/etc/resolv.conf` em todos os servidores.",
                    "explanation": "Incorreto: Encaminhadores BIND autogerenciados em cada sub-rede geram sobrecarga operacional extrema e não possuem integração nativa com a associação de VPC do Route 53."
                },
                {
                    "id": "C",
                    "text": "Implantar um Application Load Balancer em cada VPC e criar regras de roteamento baseadas em host para consultas DNS.",
                    "explanation": "Incorreto: Os ALBs operam nos protocolos HTTP/HTTPS/gRPC, e não no tráfego de protocolo DNS UDP/TCP na porta 53."
                },
                {
                    "id": "D",
                    "text": "Configurar Listas de Controle de Acesso à Rede (NACLs) para bloquear o tráfego de saída na porta 53 para todos os endereços IP públicos.",
                    "explanation": "Incorreto: As NACLs bloqueiam IPs/portas na Camada 4 e não podem inspecionar nem avaliar nomes de domínio ou hostnames de DNS."
                }
            ],
            "generalExplanation": "O Amazon Route 53 Resolver DNS Firewall permite bloquear consultas DNS feitas para domínios maliciosos conhecidos, enquanto os Outbound Endpoints encaminham perfeitamente consultas de namespaces privados para o DNS on-premises."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa farmacéutica requiere una estricta seguridad de DNS y filtrado de dominios salientes en 40 VPCs en 3 regiones de AWS. La arquitectura de seguridad exige que todas las consultas DNS salientes desde instancias EC2 hacia Internet sean inspeccionadas y filtradas contra listas de dominios maliciosos (fuentes de inteligencia sobre amenazas), mientras que la resolución DNS privada para dominios corporativos (`internal.pharma.com`) debe enrutarse a servidores DNS locales (on-premises) a través de Direct Connect. ¿Qué solución cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar Amazon Route 53 Resolver DNS Firewall con listas de dominios administradas asociadas a todas las VPCs y configurar endpoints de salida de Route 53 Resolver (Outbound Endpoints) con reglas de reenvío para `internal.pharma.com` que apunten a las direcciones IP del DNS local.",
                    "explanation": "Correcto: Route 53 Resolver DNS Firewall proporciona filtrado de dominios de Capa 7 para consultas DNS salientes en las VPCs, mientras que los Outbound Endpoints de Route 53 Resolver reenvían consultas de dominios específicos al DNS local a través de Direct Connect."
                },
                {
                    "id": "B",
                    "text": "Instalar reenviadores DNS BIND personalizados en instancias de Amazon EC2 en cada subred privada y editar `/etc/resolv.conf` en todos los servidores.",
                    "explanation": "Incorrecto: Los reenviadores BIND autogestionados en cada subred crean un mantenimiento operativo extremo y carecen de integración nativa con la asociación de VPC de Route 53."
                },
                {
                    "id": "C",
                    "text": "Implementar un Application Load Balancer en cada VPC y crear reglas de enrutamiento basadas en host para consultas DNS.",
                    "explanation": "Incorrecto: Los ALB operan en HTTP/HTTPS/gRPC, no en tráfico de protocolo DNS UDP/TCP en el puerto 53."
                },
                {
                    "id": "D",
                    "text": "Configurar Listas de Control de Acceso a la Red (NACL) para bloquear el tráfico saliente del puerto 53 hacia todas las direcciones IP públicas.",
                    "explanation": "Incorrecto: Las NACL bloquean IP/puertos en la Capa 4 y no pueden inspeccionar ni evaluar nombres de dominio o hostnames de DNS."
                }
            ],
            "generalExplanation": "Amazon Route 53 Resolver DNS Firewall le permite bloquear consultas DNS realizadas a dominios maliciosos conocidos, mientras que los Outbound Endpoints reenvían sin problemas las consultas de espacios de nombres privados al DNS local."
        }
    },
    "sap-sim2-q003": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa com implantação de várias contas no AWS Organizations necessita de correção automatizada e em tempo quase real de vulnerabilidades críticas de segurança. Especificamente, sempre que o Amazon GuardDuty detectar uma instância EC2 comunicando-se com um servidor de comando e controle (C&C), ou quando o AWS Security Hub relatar um bucket do Amazon S3 com acesso de leitura público, o sistema deverá isolar automaticamente a instância EC2 (anexando um grupo de segurança de isolamento) e ativar o Bloqueio de Acesso Público do S3 (S3 Block Public Access) sem intervenção humana. Qual arquitetura atende a esse requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar uma conta de administrador delegado para o AWS Security Hub e o Amazon GuardDuty, criar regras no Amazon EventBridge correspondentes aos padrões de descobertas específicos e acionar runbooks de automação do AWS Systems Manager (ou funções AWS Lambda) para executar ações de correção direcionadas nas contas membros.",
                    "explanation": "Correto: O EventBridge captura as descobertas do Security Hub e do GuardDuty em tempo quase real e aciona runbooks automatizados do SSM Automation ou funções Lambda para executar a correção nas contas membros."
                },
                {
                    "id": "B",
                    "text": "Agendar um trabalho diário do AWS Glue que leia os logs do CloudTrail no S3, analise os eventos JSON e modifique as políticas do AWS IAM.",
                    "explanation": "Incorreto: Trabalhos diários do Glue são executados em lotes de 24 horas e não fornecem a correção de incidentes em tempo quase real necessária para um comprometimento ativo."
                },
                {
                    "id": "C",
                    "text": "Configurar alarmes do Amazon CloudWatch na utilização da CPU para encerrar instâncias EC2 sempre que ocorrerem picos de rede.",
                    "explanation": "Incorreto: Alarmes de CPU não avaliam descobertas de inteligência contra ameaças do GuardDuty, e encerrar instâncias destrói evidências forenses essenciais."
                },
                {
                    "id": "D",
                    "text": "Anexar uma Política de Controle de Serviços (SCP) para negar todo o tráfego de rede para instâncias EC2 em toda a organização.",
                    "explanation": "Incorreto: As SCPs são limites de permissão organizacionais genéricos e não podem avaliar dinamicamente anomalias de comportamento de instâncias individuais nem isolar instâncias específicas."
                }
            ],
            "generalExplanation": "A combinação da administração delegada do AWS Security Hub e GuardDuty com o Amazon EventBridge e o AWS Systems Manager Automation oferece resposta automatizada e escalável a incidentes em ambientes com várias contas."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa con una implementación de múltiples cuentas en AWS Organizations requiere una corrección automatizada y casi en tiempo real de vulnerabilidades críticas de seguridad. Específicamente, siempre que Amazon GuardDuty detecte una instancia EC2 comunicándose con un servidor de comando y control, o cuando AWS Security Hub informe de un bucket de S3 con acceso de lectura público, el sistema debe aislar automáticamente la instancia EC2 (adjuntando un grupo de seguridad de aislamiento) y habilitar el Bloqueo de Acceso Público de S3 (S3 Block Public Access) sin intervención humana. ¿Qué arquitectura cumple con este requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar una cuenta de administrador delegado para AWS Security Hub y Amazon GuardDuty, crear reglas en Amazon EventBridge que coincidan con patrones de hallazgos específicos y activar runbooks de AWS Systems Manager Automation (o funciones AWS Lambda) para ejecutar acciones de corrección específicas en las cuentas miembro.",
                    "explanation": "Correcto: EventBridge captura los hallazgos de Security Hub y GuardDuty casi en tiempo real y activa runbooks automatizados de SSM Automation o funciones Lambda para ejecutar la remediación en las cuentas miembro."
                },
                {
                    "id": "B",
                    "text": "Programar un trabajo diario de AWS Glue que lea los registros de CloudTrail desde S3, analice los eventos JSON y modifique las directivas de AWS IAM.",
                    "explanation": "Incorrecto: Los trabajos diarios de Glue se ejecutan en lotes de 24 horas y no pueden proporcionar la corrección de incidentes casi en tiempo real requerida ante un compromiso activo."
                },
                {
                    "id": "C",
                    "text": "Configurar alarmas de Amazon CloudWatch sobre la utilización de CPU para terminar instancias EC2 cada vez que ocurran picos de red.",
                    "explanation": "Incorrecto: Las alarmas de CPU no evalúan hallazgos de inteligencia sobre amenazas de GuardDuty, y terminar instancias destruye pruebas forenses."
                },
                {
                    "id": "D",
                    "text": "Adjuntar una Política de Control de Servicios (SCP) para denegar todo el tráfico de red hacia las instancias EC2 en toda la organización.",
                    "explanation": "Incorrecto: Las SCP son límites de permisos organizacionales generales y no pueden evaluar dinámicamente anomalías de comportamiento de instancias individuales ni aislar instancias específicas."
                }
            ],
            "generalExplanation": "La combinación de la administración delegada de AWS Security Hub y GuardDuty con Amazon EventBridge y AWS Systems Manager Automation ofrece una respuesta a incidentes automatizada y escalable en entornos de múltiples cuentas."
        }
    },
    "sap-sim2-q004": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma equipe central de análise de dados na Conta A hospeda uma API de catálogo de dados em contêineres do Amazon ECS atrás de um Network Load Balancer (NLB). Mais de 60 VPCs consumidoras em 20 contas AWS diferentes em várias unidades de negócios precisam consultar esse catálogo de forma privada. Várias VPCs consumidoras possuem blocos CIDR IPv4 sobrepostos (`10.0.0.0/16`) entre si e com a Conta A. Como o arquiteto de rede deve expor esse serviço sem precisar rearquitetar as alocações de CIDR das VPCs consumidoras?",
            "options": [
                {
                    "id": "A",
                    "text": "Estabelecer conexões de VPC Peering entre a Conta A e todas as 60 VPCs consumidoras.",
                    "explanation": "Incorreto: O VPC Peering proíbe estritamente intervalos CIDR sobrepostos."
                },
                {
                    "id": "B",
                    "text": "Criar um serviço de endpoint VPC do AWS PrivateLink (VPC Endpoint Service) apoiado pelo Network Load Balancer na Conta A, permitir os IDs das contas consumidoras e fazer com que as VPCs consumidoras provisionem Interface VPC Endpoints em suas sub-redes.",
                    "explanation": "Correto: O AWS PrivateLink (VPC Endpoint Services) estabelece conectividade privada e segura por meio de ENIs entre contas, independentemente da sobreposição de faixas CIDR IPv4, sem complicações de roteamento ou emparelhamento."
                },
                {
                    "id": "C",
                    "text": "Criar conexões AWS Site-to-Site VPN entre cada VPC consumidora e a Conta A.",
                    "explanation": "Incorreto: A VPN IPsec ainda enfrenta conflitos de roteamento IP ao conectar sub-redes privadas sobrepostas."
                },
                {
                    "id": "D",
                    "text": "Implantar um AWS Transit Gateway e criar anexos de VPC (attachments) para todas as 60 VPCs.",
                    "explanation": "Incorreto: O AWS Transit Gateway requer blocos CIDR não sobrepostos para rotear pacotes IP entre VPCs e falha quando os CIDRs se sobrepõem."
                }
            ],
            "generalExplanation": "O AWS PrivateLink permite acesso privado a serviços hospedados em outra VPC entre contas e supera as limitações de blocos CIDR sobrepostos por meio do uso de interfaces de rede elásticas (ENIs) locais."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un equipo central de análisis en la Cuenta A aloja una API de catálogo de datos en contenedores de Amazon ECS detrás de un Network Load Balancer (NLB). Más de 60 VPCs consumidoras en 20 cuentas de AWS diferentes en distintas unidades de negocio necesitan consultar este catálogo de forma privada. Varias VPCs consumidoras tienen bloques CIDR IPv4 superpuestos (`10.0.0.0/16`) entre sí y con la Cuenta A. ¿Cómo debería el arquitecto de redes exponer este servicio sin rediseñar las asignaciones de CIDR de las VPCs consumidoras?",
            "options": [
                {
                    "id": "A",
                    "text": "Establecer conexiones de VPC Peering entre la Cuenta A y las 60 VPCs consumidoras.",
                    "explanation": "Incorrecto: VPC Peering prohíbe estrictamente rangos CIDR superpuestos."
                },
                {
                    "id": "B",
                    "text": "Crear un servicio de punto de enlace de VPC de AWS PrivateLink (VPC Endpoint Service) respaldado por el Network Load Balancer en la Cuenta A, permitir los IDs de las cuentas consumidoras y hacer que las VPCs consumidoras aprovisionen Interface VPC Endpoints en sus subredes.",
                    "explanation": "Correcto: AWS PrivateLink (VPC Endpoint Services) establece conectividad privada y segura a través de ENIs entre cuentas independientemente de la superposición de rangos CIDR IPv4, sin complicaciones de enrutamiento o interconexión."
                },
                {
                    "id": "C",
                    "text": "Crear conexiones AWS Site-to-Site VPN entre cada VPC consumidora y la Cuenta A.",
                    "explanation": "Incorrecto: La VPN IPsec sigue encontrando conflictos de enrutamiento IP al conectar subredes privadas superpuestas."
                },
                {
                    "id": "D",
                    "text": "Implementar un AWS Transit Gateway y crear conexiones de VPC (attachments) para las 60 VPCs.",
                    "explanation": "Incorrecto: AWS Transit Gateway requiere bloques CIDR no superpuestos para enrutar paquetes IP entre VPCs y falla cuando los CIDR se superponen."
                }
            ],
            "generalExplanation": "AWS PrivateLink permite el acceso privado a servicios alojados en otra VPC entre cuentas y supera las limitaciones de bloques CIDR superpuestos mediante el uso de interfaces de red elásticas (ENI) locales."
        }
    },
    "sap-sim2-q005": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa deseja estabelecer um portal de provisionamento de nuvem em autoatendimento onde desenvolvedores em 50 contas AWS possam iniciar padrões de infraestrutura aprovados (como VPCs padrão, clusters EKS seguros e bancos de dados RDS criptografados). A equipe central de plataforma em nuvem deve gerenciar e versionar centralmente os modelos do CloudFormation, aplicar a governança do IAM e compartilhar portfólios em toda a organização sem permitir que os desenvolvedores alterem os parâmetros dos modelos subjacentes. Qual serviço atende a esses critérios?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS OpsWorks Stacks configurado com receitas do Chef em todas as contas.",
                    "explanation": "Incorreto: O OpsWorks é um serviço de gerenciamento de configuração (Chef/Puppet), e não um portal de catálogo de serviços em nuvem para toda a organização."
                },
                {
                    "id": "B",
                    "text": "AWS CodePipeline publicando modelos brutos do CloudFormation em um bucket aberto do Amazon S3 para download pelos desenvolvedores.",
                    "explanation": "Incorreto: Downloads via S3 permitem que os desenvolvedores modifiquem modelos localmente e ignorem os controles de governança organizacional."
                },
                {
                    "id": "C",
                    "text": "AWS Service Catalog com portfólios compartilhados com o AWS Organizations, utilizando Restrições de Inicialização (Launch Constraints com IAM Service Roles) para provisionar recursos em nome dos desenvolvedores.",
                    "explanation": "Correto: O AWS Service Catalog permite que a TI central organize, controle e provisione recursos em nuvem aprovados usando modelos do CloudFormation. Os portfólios podem ser compartilhados no AWS Organizations com Launch Constraints para garantir o princípio do privilégio mínimo."
                },
                {
                    "id": "D",
                    "text": "AWS Systems Manager Parameter Store armazenando strings YAML brutas do CloudFormation em cada conta membro.",
                    "explanation": "Incorreto: O Parameter Store não fornece um portal de autoatendimento gerenciado, compartilhamento de portfólio ou aplicação de IAM com Launch Constraints."
                }
            ],
            "generalExplanation": "O AWS Service Catalog permite que as organizações criem e gerenciem catálogos de serviços de TI aprovados para uso na AWS, garantindo governança e conformidade consistentes por meio de Launch Constraints."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa desea establecer un portal de aprovisionamiento en la nube de autoservicio donde los desarrolladores en 50 cuentas de AWS puedan lanzar patrones de infraestructura aprobados (como VPCs estándar, clústeres EKS seguros y bases de datos RDS cifradas). El equipo central de plataforma en la nube debe administrar y versionar centralmente las plantillas de CloudFormation, aplicar la gobernanza de IAM y compartir portafolios en toda la organización sin permitir que los desarrolladores alteren los parámetros de las plantillas subyacentes. ¿Qué servicio cumple con estos criterios?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS OpsWorks Stacks configurado con recetas de Chef en todas las cuentas.",
                    "explanation": "Incorrecto: OpsWorks es un servicio de administración de configuración (Chef/Puppet), no un portal de catálogo de servicios en la nube para toda la organización."
                },
                {
                    "id": "B",
                    "text": "AWS CodePipeline publicando plantillas sin procesar de CloudFormation en un bucket de Amazon S3 abierto para que los desarrolladores las descarguen.",
                    "explanation": "Incorrecto: Las descargas desde S3 permiten a los desarrolladores modificar plantillas localmente y eludir los controles de gobernanza organizacional."
                },
                {
                    "id": "C",
                    "text": "AWS Service Catalog con portafolios compartidos con AWS Organizations, utilizando Restricciones de Lanzamiento (Launch Constraints con roles de servicio de IAM) para aprovisionar recursos en nombre de los desarrolladores.",
                    "explanation": "Correcto: AWS Service Catalog permite a la TI central organizar, gobernar y aprovisionar recursos aprobados en la nube utilizando plantillas de CloudFormation. Los portafolios se pueden compartir en AWS Organizations con Launch Constraints para garantizar el privilegio mínimo."
                },
                {
                    "id": "D",
                    "text": "AWS Systems Manager Parameter Store almacenando cadenas YAML de CloudFormation sin procesar en cada cuenta miembro.",
                    "explanation": "Incorrecto: Parameter Store no proporciona un portal de autoservicio administrado, uso compartido de portafolios ni aplicación de IAM mediante Launch Constraints."
                }
            ],
            "generalExplanation": "AWS Service Catalog permite a las organizaciones crear y administrar catálogos de servicios de TI aprobados para su uso en AWS, garantizando una gobernanza y cumplimiento coherentes a través de Launch Constraints."
        }
    },
    "sap-sim2-q006": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Um aplicativo móvel com 10 milhões de usuários ativos precisa armazenar dados de perfil de usuário no Amazon DynamoDB. A arquitetura exige que cada cliente móvel consulte diretamente o DynamoDB via HTTPS sem rotear o tráfego por um cluster de servidores de backend. Cada usuário deve ser estritamente restrito a ler e modificar apenas seus próprios itens de chave de partição (`UserID`) na tabela do DynamoDB. Qual combinação de serviços fornece esse controle de acesso granular?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar uma política de bucket do S3 com acesso público de leitura/gravação e sincronizar as tabelas do DynamoDB com o S3.",
                    "explanation": "Incorreto: As políticas de bucket do S3 não podem aplicar autorização de itens em nível de linha dentro de tabelas do DynamoDB."
                },
                {
                    "id": "B",
                    "text": "Criar usuários individuais do IAM para todos os 10 milhões de usuários móveis com políticas inline do IAM.",
                    "explanation": "Incorreto: As contas da AWS suportam um máximo de 5.000 usuários IAM por conta; criar usuários IAM para milhões de clientes móveis é um antipadrão de arquitetura."
                },
                {
                    "id": "C",
                    "text": "Implantar um Application Load Balancer com uma frota de proxies reversos no EC2 que filtra consultas SQL na memória.",
                    "explanation": "Incorreto: O DynamoDB é NoSQL (não SQL), e rotear todo o tráfego de clientes por servidores proxy EC2 anula o requisito de acesso direto do cliente ao DynamoDB."
                },
                {
                    "id": "D",
                    "text": "Pools de Identidades do Amazon Cognito (identidades federadas) combinados com uma IAM Role que utiliza a variável de política `${cognito-identity.amazonaws.com:sub}` na condição `dynamodb:LeadingKeys` da política do DynamoDB.",
                    "explanation": "Correto: Os Identity Pools do Cognito autenticam usuários móveis e trocam tokens por credenciais temporárias da AWS. As políticas do IAM com a condição `dynamodb:LeadingKeys` referenciando `${cognito-identity.amazonaws.com:sub}` impõem segurança em nível de linha diretamente no DynamoDB."
                }
            ],
            "generalExplanation": "O uso de Pools de Identidade do Amazon Cognito com Controle de Acesso Granular (FGAC) do IAM e `dynamodb:LeadingKeys` permite acesso direto e seguro do cliente ao DynamoDB, restrito estritamente à chave de partição de cada usuário."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una aplicación móvil con 10 millones de usuarios activos necesita almacenar datos de perfil de usuario en Amazon DynamoDB. La arquitectura requiere que cada cliente móvil consulte directamente DynamoDB a través de HTTPS sin enrutar el tráfico mediante un clúster de servidores backend. Cada usuario debe estar estrictamente restringido a leer y modificar solo sus propios elementos de clave de partición (`UserID`) en la tabla de DynamoDB. ¿Qué combinación de servicios proporciona este control de acceso granular?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar una directiva de bucket de S3 con acceso de lectura/escritura público y sincronizar las tablas de DynamoDB con S3.",
                    "explanation": "Incorrecto: Las directivas de bucket de S3 no pueden aplicar autorización de elementos a nivel de fila dentro de las tablas de DynamoDB."
                },
                {
                    "id": "B",
                    "text": "Crear usuarios individuales de IAM para los 10 millones de usuarios móviles con políticas integradas de IAM.",
                    "explanation": "Incorrecto: Las cuentas de AWS admiten un máximo de 5000 usuarios de IAM por cuenta; crear usuarios de IAM para millones de clientes móviles es un antipatrón."
                },
                {
                    "id": "C",
                    "text": "Implementar un Application Load Balancer con una flota de proxies inversos en EC2 que filtre consultas SQL en memoria.",
                    "explanation": "Incorrecto: DynamoDB es NoSQL (no SQL), y enrutar todo el tráfico de clientes a través de servidores proxy EC2 anula el requisito de acceso directo del cliente a DynamoDB."
                },
                {
                    "id": "D",
                    "text": "Grupos de Identidad de Amazon Cognito (identidades federadas) combinados con un rol de IAM que utiliza la variable de directiva `${cognito-identity.amazonaws.com:sub}` en la condición `dynamodb:LeadingKeys` de la directiva de IAM de DynamoDB.",
                    "explanation": "Correcto: Los grupos de identidades de Cognito autentican usuarios móviles y canjean tokens por credenciales temporales de AWS. Las políticas de IAM con condiciones `dynamodb:LeadingKeys` que hacen referencia a `${cognito-identity.amazonaws.com:sub}` aplican seguridad a nivel de fila directamente en DynamoDB."
                }
            ],
            "generalExplanation": "El uso de Grupos de Identidad de Amazon Cognito con Control de Acceso de Grano Fino (FGAC) de IAM y `dynamodb:LeadingKeys` permite un acceso directo y seguro de clientes a DynamoDB, restringido estrictamente a la clave de partición de cada usuario."
        }
    },
    "sap-sim2-q007": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma equipe central de segurança precisa provisionar recursos de segurança de linha de base (como políticas de senha do IAM, chaves KMS padrão e regras do AWS Config) em 150 contas AWS no AWS Organizations. Quando novas contas membros forem criadas ou adicionadas a Unidades Organizacionais (OUs) específicas, os recursos de linha de base deverão ser implantados automaticamente sem intervenção manual do administrador. Qual solução realiza isso?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma associação do AWS Systems Manager State Manager em cada conta que clone um repositório Git.",
                    "explanation": "Incorreto: As associações do State Manager nas contas membros não se propagam automaticamente para contas recém-criadas sem integração centralizada com o Organizations."
                },
                {
                    "id": "B",
                    "text": "Criar uma Política de Controle de Serviços (SCP) contendo definições de recursos do CloudFormation.",
                    "explanation": "Incorreto: As SCPs são filtros de autorização que negam ações; elas não podem provisionar nem instanciar recursos de nuvem."
                },
                {
                    "id": "C",
                    "text": "Criar AWS CloudFormation StackSets com permissões gerenciadas por serviço direcionadas a Unidades Organizacionais (OUs) específicas e habilitar a implantação automática quando novas contas forem adicionadas.",
                    "explanation": "Correto: O CloudFormation StackSets com permissões gerenciadas por serviço integra-se nativamente ao AWS Organizations, implantando ou removendo automaticamente instâncias de pilha quando contas são criadas ou movidas entre OUs."
                },
                {
                    "id": "D",
                    "text": "Escrever um script em Python em uma instância EC2 que faça polling na API do Organizations a cada hora e execute o comando da CLI `aws cloudformation create-stack`.",
                    "explanation": "Incorreto: Fazer polling com scripts personalizados no EC2 é uma abordagem frágil, exige manutenção de servidor e é inferior à automação nativa do CloudFormation StackSets."
                }
            ],
            "generalExplanation": "O AWS CloudFormation StackSets com permissões gerenciadas por serviço implanta automaticamente a infraestrutura nas contas das OUs direcionadas do AWS Organizations sempre que novas contas são criadas."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un equipo central de seguridad necesita aprovisionar recursos de seguridad de línea base (como directivas de contraseñas de IAM, claves KMS predeterminadas y reglas de AWS Config) en 150 cuentas de AWS en AWS Organizations. Cuando se creen o agreguen nuevas cuentas miembro a Unidades Organizativas (OU) específicas, los recursos de línea base deben implementarse automáticamente sin intervención manual del administrador. ¿Qué solución logra esto?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una asociación de AWS Systems Manager State Manager en cada cuenta que clone un repositorio Git.",
                    "explanation": "Incorrecto: Las asociaciones de State Manager en las cuentas miembro no se propagan automáticamente a las cuentas recién creadas sin una integración centralizada con Organizations."
                },
                {
                    "id": "B",
                    "text": "Crear una Política de Control de Servicios (SCP) que contenga definiciones de recursos de CloudFormation.",
                    "explanation": "Incorrecto: Las SCP son filtros de autorización que deniegan acciones; no pueden aprovisionar ni instanciar recursos en la nube."
                },
                {
                    "id": "C",
                    "text": "Crear AWS CloudFormation StackSets con permisos administrados por el servicio dirigidos a Unidades Organizativas (OU) específicas y habilitar la implementación automática cuando se agreguen nuevas cuentas.",
                    "explanation": "Correcto: CloudFormation StackSets con permisos administrados por el servicio se integra de forma nativa con AWS Organizations, implementando o eliminando automáticamente instancias de pila cuando las cuentas se crean o se mueven entre OU."
                },
                {
                    "id": "D",
                    "text": "Escribir un script de Python en una instancia EC2 que consulte la API de Organizations cada hora y ejecute el comando de CLI `aws cloudformation create-stack`.",
                    "explanation": "Incorrecto: El sondeo con scripts personalizados en EC2 es frágil, requiere mantenimiento del servidor y es inferior a la automatización nativa de CloudFormation StackSets."
                }
            ],
            "generalExplanation": "AWS CloudFormation StackSets con permisos administrados por el servicio implementa automáticamente la infraestructura en todas las cuentas de las OU de AWS Organizations de destino cada vez que se crean nuevas cuentas."
        }
    },
    "sap-sim2-q008": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Um data lake corporativo armazena petabytes de dados brutos de clientes no Amazon S3. Várias unidades de negócios (Marketing, Risco e Suporte ao Cliente) consultam os dados usando o Amazon Athena e o Amazon EMR. As regulamentações de governança de dados exigem controle de acesso refinado: a equipe de Risco pode ver todas as colunas, enquanto a equipe de Marketing deve ser impedida de visualizar colunas com Informações de Identificação Pessoal (PII) confidenciais (como `SSN` e `CreditCard`), com filtragem em nível de linha aplicada com base no país. Qual serviço deve ser implementado para impor essas permissões granulares centralmente?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma frota de servidores Apache Ranger em instâncias do Amazon EC2 com bancos de dados MySQL autogerenciados.",
                    "explanation": "Incorreto: Clusters Apache Ranger autogerenciados introduzem alta sobrecarga operacional em comparação com o AWS Lake Formation nativo e sem servidor."
                },
                {
                    "id": "B",
                    "text": "Implementar o AWS Lake Formation com permissões de acesso a dados em nível de coluna e de linha e LF-tags, gerenciando centralmente as permissões para o AWS Glue Data Catalog.",
                    "explanation": "Correto: O AWS Lake Formation fornece controle de acesso centralizado em nível de coluna, linha e célula em data lakes do S3 e no Glue Data Catalog para serviços analíticos como Athena e EMR."
                },
                {
                    "id": "C",
                    "text": "Criar buckets separados do Amazon S3 para cada departamento e duplicar os dados usando funções agendadas do AWS Lambda que eliminam colunas de PII.",
                    "explanation": "Incorreto: Duplicar petabytes de dados em buckets departamentais multiplica os custos de armazenamento e gera uma sobrecarga complexa de sincronização."
                },
                {
                    "id": "D",
                    "text": "Depender exclusivamente de Políticas de Bucket do Amazon S3 com condições de endereço IP.",
                    "explanation": "Incorreto: As políticas de bucket do S3 avaliam prefixos de objetos e ações, mas não podem impor permissões relacionais de consulta SQL em nível de coluna e linha dentro dos arquivos."
                }
            ],
            "generalExplanation": "O AWS Lake Formation permite controle de acesso granular (segurança em nível de coluna, linha e célula) para dados no Amazon S3 e metadados no AWS Glue Data Catalog."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Un lago de datos empresarial almacena petabytes de datos sin procesar de clientes en Amazon S3. Múltiples unidades de negocio (Marketing, Riesgos y Atención al Cliente) consultan los datos mediante Amazon Athena y Amazon EMR. Las regulaciones de gobernanza de datos exigen un control de acceso detallado: el equipo de Riesgos puede ver todas las columnas, mientras que el equipo de Marketing no debe ver columnas con Información de Identificación Personal (PII) confidencial (como `SSN` y `CreditCard`), con filtrado a nivel de fila aplicado según el país. ¿Qué servicio debe implementarse para aplicar estos permisos granulares de forma centralizada?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una flota de servidores Apache Ranger en instancias de Amazon EC2 con bases de datos MySQL autogestionadas.",
                    "explanation": "Incorrecto: Los clústeres de Apache Ranger autogestionados introducen una alta sobrecarga operativa en comparación con AWS Lake Formation nativo sin servidor."
                },
                {
                    "id": "B",
                    "text": "Implementar AWS Lake Formation con permisos de acceso a datos a nivel de columna y fila y LF-tags, administrando centralmente los permisos para el AWS Glue Data Catalog.",
                    "explanation": "Correcto: AWS Lake Formation proporciona control de acceso centralizado a nivel de columna, fila y celda en lagos de datos de S3 y el Glue Data Catalog para servicios de análisis como Athena y EMR."
                },
                {
                    "id": "C",
                    "text": "Crear buckets de Amazon S3 independientes para cada departamento y duplicar los datos utilizando funciones programadas de AWS Lambda que eliminen las columnas de PII.",
                    "explanation": "Incorrecto: Duplicar petabytes de datos en buckets departamentales multiplica los costos de almacenamiento y crea una compleja sobrecarga de sincronización."
                },
                {
                    "id": "D",
                    "text": "Depender únicamente de las Directivas de Bucket de Amazon S3 con condiciones de dirección IP.",
                    "explanation": "Incorrecto: Las directivas de bucket de S3 evalúan prefijos y acciones de objetos, pero no pueden aplicar permisos de consulta SQL a nivel de fila y columna dentro de los archivos."
                }
            ],
            "generalExplanation": "AWS Lake Formation permite el control de acceso granular (seguridad a nivel de columna, fila y celda) para datos en Amazon S3 y metadatos en AWS Glue Data Catalog."
        }
    },
    "sap-sim2-q009": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma plataforma de veículos conectados recebe 100.000 registros de telemetria de sensores por segundo. Os dados devem ser ingeridos em tempo real, validados e enriquecidos com metadados de veículos do Amazon DynamoDB, e gravados tanto no Amazon S3 (para arquivamento bruto de longo prazo no formato Parquet) quanto no Amazon Redshift (para análises operacionais da frota em menos de um minuto). A arquitetura deve escalar elasticamente com zero provisionamento de servidores. Qual solução deve ser implementada?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um cluster Apache Kafka em instâncias EC2 Spot gravando diretamente em volumes Amazon EBS.",
                    "explanation": "Incorreto: O Kafka autogerenciado em instâncias Spot corre o risco de perda de dados mediante interrupções de instâncias Spot e exige extensa administração de infraestrutura."
                },
                {
                    "id": "B",
                    "text": "Gravar a telemetria do sensor diretamente em um banco de dados Amazon Aurora MySQL e agendar consultas cron.",
                    "explanation": "Incorreto: Ingerir 100.000 gravações por segundo diretamente em um banco de dados relacional cria contenção severa de bloqueio de gravação e sobrecarrega o banco de dados."
                },
                {
                    "id": "C",
                    "text": "Enviar registros de sensores para uma fila padrão do Amazon SQS e executar um trabalho ETL por hora do AWS Glue para carregar dados no Redshift.",
                    "explanation": "Incorreto: Trabalhos por hora do Glue introduzem uma latência de lote de 60 minutos, falhando no requisito de análise operacional em menos de um minuto."
                },
                {
                    "id": "D",
                    "text": "Ingerir a telemetria no Amazon Kinesis Data Streams, enriquecer os registros usando o AWS Lambda lendo do DynamoDB, transmitir os dados enriquecidos para o Amazon Kinesis Data Firehose para converter em Parquet e entregar no S3, e usar o Amazon Redshift Auto-Copy a partir do S3 (ou entrega direta do Firehose no Redshift).",
                    "explanation": "Correto: O Kinesis Data Streams fornece ingestão de streaming elástica em tempo real, o Lambda cuida do enriquecimento sem servidor e o Kinesis Data Firehose transforma automaticamente os dados em Parquet, entrega no S3 e carrega no Redshift com zero gerenciamento de servidor."
                }
            ],
            "generalExplanation": "O Amazon Kinesis Data Streams combinado com enriquecimento via Lambda e o Kinesis Data Firehose fornece um pipeline de ingestão de streaming totalmente sem servidor e altamente escalável para data lakes no S3 e Amazon Redshift."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una plataforma de vehículos conectados recibe 100.000 registros de telemetría de sensores por segundo. Los datos deben ingerirse en tiempo real, validarse y enriquecerse con metadatos de vehículos de Amazon DynamoDB, y escribirse tanto en Amazon S3 (para archivado sin procesar a largo plazo en formato Parquet) como en Amazon Redshift (para análisis operativos de flota en menos de un minuto). La arquitectura debe escalar elásticamente sin aprovisionamiento de servidores. ¿Qué solución debe implementarse?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un clúster de Apache Kafka en instancias Spot de EC2 que escriba directamente en volúmenes de Amazon EBS.",
                    "explanation": "Incorrecto: Kafka autogestionado en instancias Spot corre el riesgo de pérdida de datos tras la interrupción de Spot y requiere una amplia administración de infraestructura."
                },
                {
                    "id": "B",
                    "text": "Escribir la telemetría de los sensores directamente en una base de datos Amazon Aurora MySQL y programar consultas cron.",
                    "explanation": "Incorrecto: Ingerir 100.000 escrituras por segundo directamente en una base de datos relacional genera una grave contención de bloqueos de escritura y colapsa la base de datos."
                },
                {
                    "id": "C",
                    "text": "Enviar registros de sensores a una cola estándar de Amazon SQS y ejecutar un trabajo ETL de AWS Glue por hora para cargar datos en Redshift.",
                    "explanation": "Incorrecto: Los trabajos de Glue por hora introducen una latencia de lote de 60 minutos, lo que incumple el requisito de análisis operativo en menos de un minuto."
                },
                {
                    "id": "D",
                    "text": "Ingerir telemetría en Amazon Kinesis Data Streams, enriquecer los registros mediante AWS Lambda leyendo desde DynamoDB, transmitir datos enriquecidos a Amazon Kinesis Data Firehose para convertirlos a Parquet y entregarlos a S3, y usar Amazon Redshift Auto-Copy desde S3 (o entrega directa de Firehose a Redshift).",
                    "explanation": "Correcto: Kinesis Data Streams proporciona ingestión de streaming elástica en tiempo real, Lambda maneja el enriquecimiento sin servidor y Kinesis Data Firehose transforma automáticamente los datos a Parquet, los entrega a S3 y los carga en Redshift sin administración de servidores."
                }
            ],
            "generalExplanation": "Amazon Kinesis Data Streams combinado con el enriquecimiento mediante Lambda y Kinesis Data Firehose proporciona un flujo de ingestión de transmisión completamente sin servidor y altamente escalable para lagos de datos en S3 y Amazon Redshift."
        }
    },
    "sap-sim2-q010": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Um aplicativo de microsserviços em contêineres implantado no Amazon ECS com AWS Fargate atende a padrões de tráfego variáveis. Durante o horário comercial, o tráfego oscila rapidamente com base em promoções relâmpago. O líder de engenharia exige escalabilidade automática de contêineres que responda em segundos com base na contagem de solicitações em tempo real por destino, garantindo ao mesmo tempo zero aplicação de patches em instâncias de contêiner e custos mínimos de capacidade ociosa fora dos horários de pico. Qual solução deve ser implementada?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar serviços do Amazon ECS usando o tipo de inicialização AWS Fargate atrás de um Application Load Balancer e configurar o ECS Service Auto Scaling com uma política de Rastreamento de Destino (Target Tracking) baseada em `ALBRequestCountPerTarget`.",
                    "explanation": "Correto: O ECS no AWS Fargate elimina o gerenciamento e a aplicação de patches no servidor, enquanto o escalonamento Target Tracking em `ALBRequestCountPerTarget` dimensiona a contagem de tarefas de contêiner proporcionalmente ao volume de solicitações HTTP recebidas em tempo real."
                },
                {
                    "id": "B",
                    "text": "Implantar tarefas do ECS em um cluster de instâncias EC2 com Auto Scaling configurado para escalonamento agendado às 08:00.",
                    "explanation": "Incorreto: O escalonamento agendado no EC2 não se adapta a picos imprevisíveis de vendas relâmpago e exige manutenção manual do sistema operacional do servidor."
                },
                {
                    "id": "C",
                    "text": "Executar cargas de trabalho em contêineres em clusters do Amazon EMR com instâncias Spot.",
                    "explanation": "Incorreto: O EMR é projetado para análise em lote de big data (Hadoop/Spark), e não para microsserviços REST voltados para clientes."
                },
                {
                    "id": "D",
                    "text": "Implantar ambientes do AWS Elastic Beanstalk de instância única em cada Zona de Disponibilidade.",
                    "explanation": "Incorreto: O Elastic Beanstalk de instância única não oferece alta disponibilidade nem escalonamento elástico de contêineres."
                }
            ],
            "generalExplanation": "O Amazon ECS no AWS Fargate com escalonamento por Target Tracking em `ALBRequestCountPerTarget` oferece escalonamento elástico de microsserviços totalmente sem servidor, alinhando dinamicamente a capacidade ao tráfego."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una aplicación de microservicios en contenedores implementada en Amazon ECS con AWS Fargate maneja patrones de tráfico variables. Durante el horario comercial, el tráfico fluctúa rápidamente debido a ventas flash. El líder de ingeniería requiere un escalado automático de contenedores que responda en segundos según el recuento de solicitudes en tiempo real por objetivo, al tiempo que garantiza cero parches de instancias de contenedores y costos mínimos de capacidad inactiva fuera de las horas pico. ¿Qué solución debe implementarse?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar servicios de Amazon ECS utilizando el tipo de inicio AWS Fargate detrás de un Application Load Balancer y configurar el escalado automático de servicios de ECS con una directiva de Seguimiento de Objetivos (Target Tracking) basada en `ALBRequestCountPerTarget`.",
                    "explanation": "Correcto: ECS en AWS Fargate elimina la administración y la aplicación de parches en el servidor, mientras que el escalado de Target Tracking en `ALBRequestCountPerTarget` escala el recuento de tareas de contenedor proporcionalmente al volumen de solicitudes HTTP entrantes en tiempo real."
                },
                {
                    "id": "B",
                    "text": "Implementar tareas de ECS en un clúster de instancias EC2 con Auto Scaling configurado para escalado programado a las 8:00 AM.",
                    "explanation": "Incorrecto: El escalado programado en EC2 no se adapta a picos impredecibles de ventas flash y requiere mantenimiento manual del sistema operativo del servidor."
                },
                {
                    "id": "C",
                    "text": "Ejecutar cargas de trabajo de contenedores en clústeres de Amazon EMR con instancias Spot.",
                    "explanation": "Incorrecto: EMR está diseñado para análisis por lotes de big data (Hadoop/Spark), no para microservicios REST orientados al cliente."
                },
                {
                    "id": "D",
                    "text": "Implementar entornos de AWS Elastic Beanstalk de instancia única en cada Zona de Disponibilidad.",
                    "explanation": "Incorrecto: Elastic Beanstalk de instancia única carece de alta disponibilidad y escalado automático elástico de contenedores."
                }
            ],
            "generalExplanation": "Amazon ECS en AWS Fargate con escalado de Target Tracking en `ALBRequestCountPerTarget` proporciona un escalado de microservicios elástico y completamente sin servidor que alinea dinámicamente la capacidad con el tráfico."
        }
    },
    "sap-sim2-q011": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma plataforma global de negociação financeira em tempo real opera clusters de backend redundantes em us-east-1 e ap-southeast-1. Os aplicativos de desktop clientes comunicam-se por meio de protocolos TCP não HTTP e exigem endereços IP estáticos para inclusão na lista de permissões (whitelist) de firewalls corporativos empresariais. A arquitetura deve redirecionar automaticamente o tráfego para a região íntegra em até 30 segundos se um endpoint regional falhar. Qual serviço atende a esses critérios?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma distribuição do Amazon CloudFront com failover de origem (Origin Failover).",
                    "explanation": "Incorreto: O CloudFront foi desenvolvido para entrega de conteúdo HTTP/HTTPS/WebSockets, e não para protocolos de negociação TCP brutos não HTTP, além de não fornecer IPs Anycast estáticos para listas de permissões em firewalls."
                },
                {
                    "id": "B",
                    "text": "Configurar o roteamento de Resposta com Múltiplos Valores (Multi-Value Answer) do Amazon Route 53 apontando para endereços IP elásticos.",
                    "explanation": "Incorreto: O failover de DNS do Route 53 está sujeito ao cache de DNS no lado do cliente (TTL), o que pode atrasar o failover por vários minutos, violando o requisito rigoroso de 30 segundos."
                },
                {
                    "id": "C",
                    "text": "Implantar o emparelhamento entre regiões do AWS Transit Gateway com roteamento dinâmico BGP.",
                    "explanation": "Incorreto: O Transit Gateway é utilizado para conectar VPCs e redes corporativas locais privadas, e não aplicativos de desktop clientes públicos na internet."
                },
                {
                    "id": "D",
                    "text": "Implantar o AWS Global Accelerator com dois endereços IP Anycast estáticos, criar grupos de endpoints regionais apontando para Network Load Balancers ou Application Load Balancers em cada região e configurar verificações de integridade automatizadas.",
                    "explanation": "Correto: O AWS Global Accelerator fornece 2 endereços IP Anycast estáticos para listas de permissões de firewall, roteia tráfego TCP/UDP não HTTP pela rede privada global da AWS e realiza failover automatizado rápido (<30s) entre endpoints regionais íntegros."
                }
            ],
            "generalExplanation": "O AWS Global Accelerator fornece 2 endereços IP Anycast estáticos, acelera o tráfego TCP/UDP pela rede global da AWS e realiza failover regional rápido (<30 segundos) orientado por verificações de integridade."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una plataforma global de operaciones financieras en tiempo real opera clústeres backend redundantes en us-east-1 y ap-southeast-1. Las aplicaciones de escritorio cliente se comunican a través de protocolos TCP no HTTP y requieren direcciones IP estáticas para incluirlas en la lista blanca de firewalls empresariales corporativos. La arquitectura debe redirigir automáticamente el tráfico a la región en buen estado en un plazo de 30 segundos si falla un punto de enlace regional. ¿Qué servicio cumple con estos criterios?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una distribución de Amazon CloudFront con conmutación por error de origen (Origin Failover).",
                    "explanation": "Incorrecto: CloudFront está diseñado para la entrega de contenido HTTP/HTTPS/WebSockets, no para protocolos comerciales TCP no HTTP sin formato, y no proporciona IP Anycast estáticas para listas blancas de firewall."
                },
                {
                    "id": "B",
                    "text": "Configurar el enrutamiento de Respuesta de Varios Valores (Multi-Value Answer) de Amazon Route 53 apuntando a direcciones IP elásticas.",
                    "explanation": "Incorrecto: La conmutación por error de DNS de Route 53 está sujeta al almacenamiento en caché de DNS del lado del cliente (TTL), lo que puede retrasar la conmutación por error durante minutos, incumpliendo el estricto requisito de 30 segundos."
                },
                {
                    "id": "C",
                    "text": "Implementar interconexión entre regiones de AWS Transit Gateway con enrutamiento dinámico BGP.",
                    "explanation": "Incorrecto: Transit Gateway sirve para conectar VPC y redes corporativas locales privadas, no aplicaciones de escritorio de clientes públicos en Internet."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS Global Accelerator con dos direcciones IP Anycast estáticas, crear grupos de puntos de enlace regionales que apunten a Network Load Balancers o Application Load Balancers en cada región y configurar comprobaciones de estado automatizadas.",
                    "explanation": "Correcto: AWS Global Accelerator proporciona 2 direcciones IP Anycast estáticas para listas blancas de firewall, enruta tráfico TCP/UDP no HTTP a través de la red privada global de AWS y realiza una conmutación por error automatizada rápida (<30 s) entre puntos de enlace regionales en buen estado."
                }
            ],
            "generalExplanation": "AWS Global Accelerator proporciona 2 direcciones IP Anycast estáticas, acelera el tráfico TCP/UDP a través de la red global de AWS y realiza una conmutación por error regional rápida (<30 segundos) impulsada por comprobaciones de estado."
        }
    },
    "sap-sim2-q012": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma empresa deseja construir um assistente de suporte ao cliente com IA Generativa usando Geração Aumentada por Recuperação (RAG - Retrieval-Augmented Generation). A solução deve consultar documentos PDF confidenciais internos armazenados no Amazon S3, converter texto em embeddings vetoriais, realizar busca semântica por similaridade vetorial e gerar respostas em linguagem natural usando modelos fundamentais (foundation models) sem a necessidade de gerenciar infraestrutura de banco de dados vetorial nem expor a propriedade intelectual da empresa a modelos públicos de IA. Qual arquitetura atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Treinar um modelo de aprendizado profundo personalizado do zero em um cluster de GPUs Amazon EC2 P4de usando PyTorch.",
                    "explanation": "Incorreto: Treinar um modelo fundamental do zero requer milhões de dólares, meses de tempo de computação e imenso esforço de engenharia em comparação com o RAG gerenciado no Bedrock."
                },
                {
                    "id": "B",
                    "text": "Utilizar o Knowledge Bases for Amazon Bedrock, conectando o bucket de documentos do Amazon S3 a uma coleção de busca vetorial do Amazon OpenSearch Serverless e consultando modelos fundamentais (como Anthropic Claude) por meio da API RetrieveAndGenerate do Amazon Bedrock.",
                    "explanation": "Correto: O Knowledge Bases for Amazon Bedrock é um recurso de RAG totalmente gerenciado que divide em partes (chunks), gera embeddings e indexa automaticamente documentos do S3 em coleções vetoriais do OpenSearch Serverless, conectando-se a modelos fundamentais de forma privada."
                },
                {
                    "id": "C",
                    "text": "Enviar todos os documentos de texto PDF internos como parâmetros de consulta URL para uma API pública de chatbot SaaS de terceiros.",
                    "explanation": "Incorreto: O envio de documentos confidenciais internos para APIs públicas não verificadas viola as políticas de segurança de dados e privacidade."
                },
                {
                    "id": "D",
                    "text": "Armazenar texto em uma tabela MySQL do Amazon RDS com índices FULLTEXT e executar consultas `SELECT LIKE` em Python.",
                    "explanation": "Incorreto: As consultas relacionais SQL `LIKE` executam correspondência por palavras-chave, e não a pesquisa semântica por similaridade de vetores exigida para RAG."
                }
            ],
            "generalExplanation": "O Knowledge Bases for Amazon Bedrock fornece um fluxo de trabalho de Geração Aumentada por Recuperação (RAG) totalmente gerenciado e sem servidor, integrando fontes de dados do S3, repositórios de vetores e modelos fundamentais."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una empresa desea crear un asistente de atención al cliente con IA generativa mediante Generación Aumentada por Recuperación (RAG). La solución debe consultar documentos PDF internos confidenciales almacenados en Amazon S3, convertir texto en incrustaciones vectoriales (embeddings), realizar búsquedas semánticas de similitud vectorial y generar respuestas en lenguaje natural mediante modelos fundacionales sin administrar infraestructura de base de datos vectorial ni exponer la propiedad intelectual de la empresa a modelos públicos de IA. ¿Qué arquitectura cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Entrenar un modelo de aprendizaje profundo personalizado desde cero en un clúster de GPU Amazon EC2 P4de utilizando PyTorch.",
                    "explanation": "Incorrecto: Entrenar un modelo fundacional desde cero requiere millones de dólares, meses de tiempo de cómputo y un inmenso esfuerzo de ingeniería en comparación con RAG administrado en Bedrock."
                },
                {
                    "id": "B",
                    "text": "Utilizar Knowledge Bases for Amazon Bedrock, conectando el bucket de documentos de Amazon S3 a una colección de búsqueda vectorial de Amazon OpenSearch Serverless y consultando modelos fundacionales (como Anthropic Claude) mediante la API RetrieveAndGenerate de Amazon Bedrock.",
                    "explanation": "Correcto: Knowledge Bases for Amazon Bedrock es una capacidad de RAG completamente administrada que fragmenta, incrusta e indexa automáticamente documentos de S3 en colecciones vectoriales de OpenSearch Serverless y se conecta a modelos fundacionales de forma privada."
                },
                {
                    "id": "C",
                    "text": "Enviar todos los documentos de texto PDF internos como parámetros de consulta URL a una API pública de chatbot SaaS de terceros.",
                    "explanation": "Incorrecto: Enviar documentos confidenciales internos a API públicas no verificadas viola las políticas de privacidad y seguridad de datos."
                },
                {
                    "id": "D",
                    "text": "Almacenar texto en una tabla MySQL de Amazon RDS con índices FULLTEXT y ejecutar consultas `SELECT LIKE` en Python.",
                    "explanation": "Incorrecto: Las consultas relacionales SQL `LIKE` realizan coincidencia de palabras clave, no la búsqueda semántica de similitud vectorial requerida para RAG."
                }
            ],
            "generalExplanation": "Knowledge Bases for Amazon Bedrock proporciona un flujo de trabajo de Generación Aumentada por Recuperación (RAG) completamente administrado y sin servidor que integra orígenes de datos de S3, almacenes vectoriales y modelos fundacionales."
        }
    },
    "sap-sim2-q013": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Um jogo móvel multijogador registra as pontuações das partidas dos jogadores em uma tabela do Amazon DynamoDB. Sempre que um jogador atinge uma pontuação entre as 100 melhores de todos os tempos, o aplicativo deve acionar imediatamente uma notificação push para todos os jogadores na sala do jogo, atualizar um placar global do Redis no Amazon ElastiCache e gravar um evento de auditoria no Amazon S3. Como essa arquitetura orientada a eventos deve ser implementada com latência mínima e alta resiliência?",
            "options": [
                {
                    "id": "A",
                    "text": "Fazer com que o cliente móvel realize três solicitações de gravação separadas pela internet para o DynamoDB, ElastiCache e S3 simultaneamente.",
                    "explanation": "Incorreto: Múltiplas gravações diretas a partir do cliente geram condições de corrida (race conditions), estado inconsistente, alta latência de rede e graves riscos de segurança."
                },
                {
                    "id": "B",
                    "text": "Habilitar o Amazon DynamoDB Streams na tabela e configurar uma função AWS Lambda acionada pelo fluxo com um padrão de critérios de filtro para processar novas modificações de itens, atualizar o ElastiCache e publicar notificações no SNS.",
                    "explanation": "Correto: O DynamoDB Streams captura modificações de itens ordenadas no tempo e aciona funções AWS Lambda em tempo quase real (sub-segundo) para executar atualizações downstream com novas tentativas integradas e DLQs."
                },
                {
                    "id": "C",
                    "text": "Migrar o banco de dados para o Amazon RDS PostgreSQL e escrever gatilhos de banco de dados em PL/pgSQL para fazer chamadas de API HTTP para dispositivos móveis.",
                    "explanation": "Incorreto: Mecanismos de banco de dados relacionais não conseguem escalar para milhões de gravações móveis simultâneas, e gatilhos de banco de dados que fazem chamadas HTTP externas síncronas congelam as transações do banco de dados."
                },
                {
                    "id": "D",
                    "text": "Configurar uma regra agendada do Amazon CloudWatch para executar um script em Python em uma instância EC2 a cada 10 minutos varrendo (scan) a tabela do DynamoDB.",
                    "explanation": "Incorreto: Varreduras periódicas de tabela a cada 10 minutos introduzem uma latência massiva, consomem altas RCUs e não atendem ao requisito de notificação em tempo real."
                }
            ],
            "generalExplanation": "O Amazon DynamoDB Streams captura sequências ordenadas no tempo de modificações no nível de item em tabelas do DynamoDB, permitindo uma integração perfeita orientada a eventos em tempo real com o AWS Lambda."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Un juego móvil multijugador registra las puntuaciones de las partidas de los jugadores en una tabla de Amazon DynamoDB. Cada vez que un jugador logra una de las 100 mejores puntuaciones de todos los tiempos, la aplicación debe activar inmediatamente una notificación push a todos los jugadores de la sala de juego, actualizar una tabla de clasificación global de Redis en Amazon ElastiCache y escribir un evento de auditoría en Amazon S3. ¿Cómo debería implementarse esta arquitectura basada en eventos con una latencia mínima y alta resiliencia?",
            "options": [
                {
                    "id": "A",
                    "text": "Hacer que el cliente móvil realice tres solicitudes de escritura independientes a través de Internet hacia DynamoDB, ElastiCache y S3 simultáneamente.",
                    "explanation": "Incorrecto: Múltiples escrituras directas de clientes introducen condiciones de carrera, estados inconsistentes, alta latencia de red y graves riesgos de seguridad."
                },
                {
                    "id": "B",
                    "text": "Habilitar Amazon DynamoDB Streams en la tabla y configurar una función de AWS Lambda activada por la secuencia con un patrón de criterios de filtro para procesar nuevas modificaciones de elementos, actualizar ElastiCache y publicar notificaciones en SNS.",
                    "explanation": "Correcto: DynamoDB Streams captura modificaciones a nivel de elemento ordenadas en el tiempo y activa funciones de AWS Lambda casi en tiempo real (en menos de un segundo) para ejecutar actualizaciones posteriores con reintentos integrados y DLQ."
                },
                {
                    "id": "C",
                    "text": "Migrar la base de datos a Amazon RDS PostgreSQL y escribir disparadores de base de datos en PL/pgSQL para realizar llamadas a la API HTTP a dispositivos móviles.",
                    "explanation": "Incorrecto: Los motores de bases de datos relacionales no pueden escalar a millones de escrituras móviles simultáneas, y los disparadores de bases de datos que realizan llamadas HTTP externas sincrónicas bloquean las transacciones de bases de datos."
                },
                {
                    "id": "D",
                    "text": "Configurar una regla programada de Amazon CloudWatch para ejecutar un script de Python en una instancia EC2 cada 10 minutos escaneando la tabla de DynamoDB.",
                    "explanation": "Incorrecto: Los escaneos periódicos de tablas cada 10 minutos introducen una latencia masiva, consumen altas RCU y no cumplen con el requisito de notificación en tiempo real."
                }
            ],
            "generalExplanation": "Amazon DynamoDB Streams captura secuencias ordenadas en el tiempo de modificaciones a nivel de elemento en tablas de DynamoDB, lo que permite una integración fluida basada en eventos en tiempo real con AWS Lambda."
        }
    },
    "sap-sim2-q014": {
        "pt": {
            "domainName": "Domínio 2: Projetar para Novas Soluções",
            "statement": "Uma plataforma corporativa de comércio eletrônico utiliza microsserviços que se comunicam por meio de eventos. A plataforma precisa ingerir eventos de parceiros SaaS terceirizados (Shopify, Zendesk e Auth0) e microsserviços internos, filtrar e transformar payloads com base em padrões de conteúdo JSON e distribuir eventos (fan-out) para múltiplos destinos assíncronos (incluindo filas SQS, fluxos de trabalho do Step Functions e Kinesis Firehose) com validação automatizada de esquema. Qual serviço deve formar o barramento de eventos central?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar e implantar o Amazon API Gateway com APIs WebSocket seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: As APIs WebSocket são projetadas para comunicação bidirecional cliente-servidor em tempo real, e não como um barramento corporativo de eventos que roteia entre serviços da AWS."
                },
                {
                    "id": "B",
                    "text": "Configurar e implantar assinaturas GraphQL do AWS AppSync seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O AppSync é um serviço GraphQL gerenciado, não um barramento de roteamento de eventos com integrações de parceiros SaaS."
                },
                {
                    "id": "C",
                    "text": "Filas FIFO do Amazon Simple Queue Service (Amazon SQS).",
                    "explanation": "Incorreto: O SQS é uma fila ponto a ponto sem integrações nativas de parceiros SaaS, registros de esquema ou regras dinâmicas de roteamento baseadas em conteúdo para múltiplos destinos."
                },
                {
                    "id": "D",
                    "text": "Amazon EventBridge (barramentos de eventos personalizados e de parceiros) com o EventBridge Schema Registry e regras de roteamento baseadas em conteúdo.",
                    "explanation": "Correto: O Amazon EventBridge é um barramento de eventos sem servidor com integrações nativas de parceiros SaaS, Schema Registry com vinculações de código, filtragem JSON baseada em conteúdo e roteamento para mais de 20 destinos da AWS."
                }
            ],
            "generalExplanation": "O Amazon EventBridge facilita a conexão de aplicativos usando dados de seus próprios aplicativos, aplicativos SaaS de terceiros e serviços da AWS com filtragem declarativa de conteúdo e registros de esquema."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar para Nuevas Soluciones",
            "statement": "Una plataforma empresarial de comercio electrónico utiliza microservicios que se comunican mediante eventos. La plataforma necesita ingerir eventos de socios SaaS externos (Shopify, Zendesk y Auth0) y microservicios internos, filtrar y transformar cargas útiles según patrones de contenido JSON y distribuir eventos (fan-out) a múltiples destinos asincrónicos (incluidas colas SQS, flujos de trabajo de Step Functions y Kinesis Firehose) con validación de esquemas automatizada. ¿Qué servicio debería formar el bus de eventos principal?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar e implementar Amazon API Gateway con API WebSocket siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Las API WebSocket están diseñadas para la comunicación bidireccional cliente-servidor en tiempo real, no como un bus de eventos empresarial que enruta entre servicios de AWS."
                },
                {
                    "id": "B",
                    "text": "Configurar e implementar suscripciones GraphQL de AWS AppSync siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: AppSync es un servicio GraphQL administrado, no un bus de enrutamiento de eventos con integraciones de socios SaaS."
                },
                {
                    "id": "C",
                    "text": "Colas FIFO de Amazon Simple Queue Service (Amazon SQS).",
                    "explanation": "Incorrecto: SQS es una cola punto a punto sin integraciones nativas de socios SaaS, registros de esquemas o reglas dinámicas de enrutamiento basadas en contenido multidestino."
                },
                {
                    "id": "D",
                    "text": "Amazon EventBridge (buses de eventos personalizados y de socios) con EventBridge Schema Registry y reglas de enrutamiento basadas en contenido.",
                    "explanation": "Correcto: Amazon EventBridge es un bus de eventos sin servidor con integraciones nativas de socios SaaS, Schema Registry con enlaces de código, filtrado JSON basado en contenido y enrutamiento a más de 20 destinos de AWS."
                }
            ],
            "generalExplanation": "Amazon EventBridge facilita la conexión de aplicaciones utilizando datos de sus propias aplicaciones, aplicaciones SaaS de terceros y servicios de AWS con filtrado de contenido declarativo y registros de esquemas."
        }
    },
    "sap-sim2-q015": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Um site de comércio eletrônico enfrenta extrema latência de leitura de banco de dados em uma instância do Amazon RDS MySQL durante promoções relâmpago de marketing. Mais de 80% das consultas ao banco de dados são instruções `SELECT` repetitivas para itens populares do catálogo de produtos que raramente mudam. A equipe de desenvolvimento deseja aliviar o tráfego de leitura e obter tempos de resposta de consulta inferiores a um milissegundo sem modificar as estruturas de esquema relacional. Qual estratégia de cache o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Fazer upgrade do tamanho da instância de banco de dados do RDS MySQL para um tipo de instância maior (escalar verticalmente) e habilitar Multi-AZ.",
                    "explanation": "Incorreto: O escalonamento vertical tem limites físicos, aumenta significativamente os custos de licenciamento de banco de dados e não fornece latência em memória inferior a um milissegundo como o ElastiCache."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster do Amazon CloudSearch na frente do RDS MySQL.",
                    "explanation": "Incorreto: O CloudSearch é um mecanismo de busca, e não uma camada de cache em memória chave-valor de baixa latência para resultados de consultas relacionais."
                },
                {
                    "id": "C",
                    "text": "Habilitar backups automatizados no RDS MySQL durante promoções relâmpago.",
                    "explanation": "Incorreto: A execução de backups durante períodos de alto tráfego adiciona sobrecarga de E/S em vez de reduzir a latência de leitura."
                },
                {
                    "id": "D",
                    "text": "Implantar um cluster do Amazon ElastiCache for Redis (ou Valkey) usando o padrão Cache-Aside (Lazy Loading) com expiração por Time-to-Live (TTL) para armazenar em cache os resultados frequentes de consultas do catálogo de produtos.",
                    "explanation": "Correto: O Amazon ElastiCache for Redis/Valkey oferece desempenho de leitura em memória inferior a um milissegundo. O uso do padrão Cache-Aside alivia com eficiência as leituras repetitivas do catálogo do RDS MySQL."
                }
            ],
            "generalExplanation": "A implantação de um cache em memória, como o Amazon ElastiCache for Redis usando o padrão Cache-Aside, fornece latência inferior a um milissegundo e alivia a pressão de leitura dos bancos de dados relacionais."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Un sitio web de comercio electrónico experimenta una latencia extrema de lectura en una instancia de Amazon RDS MySQL durante ventas flash de marketing. Más del 80% de las consultas a la base de datos son sentencias `SELECT` repetitivas para artículos populares del catálogo de productos que rara vez cambian. El equipo de desarrollo desea descargar el tráfico de lectura y lograr tiempos de respuesta de consulta inferiores al milisegundo sin modificar las estructuras de esquemas relacionales. ¿Qué estrategia de almacenamiento en caché debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Actualizar el tamaño de la instancia de base de datos RDS MySQL a un tipo de instancia más grande (escalar verticalmente) y habilitar Multi-AZ.",
                    "explanation": "Incorrecto: El escalado vertical tiene límites físicos, aumenta significativamente los costos de licencias de bases de datos y no proporciona una latencia en memoria inferior al milisegundo como ElastiCache."
                },
                {
                    "id": "B",
                    "text": "Implementar un clúster de Amazon CloudSearch frente a RDS MySQL.",
                    "explanation": "Incorrecto: CloudSearch es un motor de búsqueda, no una capa de almacenamiento en caché en memoria clave-valor de baja latencia para resultados de consultas relacionales."
                },
                {
                    "id": "C",
                    "text": "Habilitar Copias de Seguridad Automatizadas en RDS MySQL durante las ventas flash.",
                    "explanation": "Incorrecto: Ejecutar copias de seguridad durante períodos de mucho tráfico añade sobrecarga de E/S en lugar de reducir la latencia de lectura."
                },
                {
                    "id": "D",
                    "text": "Implementar un clúster de Amazon ElastiCache para Redis (o Valkey) utilizando el patrón Cache-Aside (Lazy Loading) con expiración Time-to-Live (TTL) para almacenar en caché los resultados de consultas frecuentes del catálogo de productos.",
                    "explanation": "Correcto: Amazon ElastiCache para Redis/Valkey ofrece un rendimiento de lectura en memoria de menos de un milisegundo. El uso del patrón Cache-Aside descarga eficazmente las lecturas repetitivas del catálogo desde RDS MySQL."
                }
            ],
            "generalExplanation": "Implementar una memoria caché en memoria como Amazon ElastiCache para Redis mediante el patrón Cache-Aside proporciona una latencia inferior al milisegundo y descarga la presión de lectura de las bases de datos relacionales."
        }
    },
    "sap-sim2-q016": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa executa 500 instâncias Linux do Amazon EC2 (c5.xlarge e m5.xlarge) hospedando microsserviços em Go e Node.js. O CTO define a meta de reduzir os custos de computação em 20% e melhorar a eficiência energética, mantendo ou aumentando a taxa de transferência (throughput) dos aplicativos. Qual aprimoramento arquitetural atinge isso com o mínimo de refatoração de código?",
            "options": [
                {
                    "id": "A",
                    "text": "Mudar todas as instâncias para instâncias expansíveis T3-micro com modo de crédito padrão.",
                    "explanation": "Incorreto: As instâncias T3-micro não têm CPU/RAM suficientes para microsserviços e sofrerão estrangulamento severo de CPU sob cargas de produção sustentadas."
                },
                {
                    "id": "B",
                    "text": "Migrar as cargas de trabalho para famílias de instâncias baseadas em AWS Graviton3/Graviton4 (como c7g e m7g), reconstruindo imagens de contêiner multiarquitetura para ARM64 (aarch64).",
                    "explanation": "Correto: Os processadores AWS Graviton oferecem até 40% melhor relação custo-benefício e 60% menor consumo de energia em comparação com instâncias x86 equivalentes, exigindo apenas a recompilação das imagens de contêiner para ARM64."
                },
                {
                    "id": "C",
                    "text": "Converter todas as instâncias em Hosts Dedicados (Dedicated Hosts) com compromissos de 3 anos.",
                    "explanation": "Incorreto: Hosts Dedicados são significativamente mais caros e destinam-se à conformidade de licenciamento de soquetes físicos."
                },
                {
                    "id": "D",
                    "text": "Migrar os aplicativos para instâncias EC2 do Windows Server com aceleração de hardware x86.",
                    "explanation": "Incorreto: O Windows Server incorre em taxas adicionais de licenciamento do sistema operacional e aumenta os custos de computação."
                }
            ],
            "generalExplanation": "Os processadores AWS Graviton (chips ARM64 personalizados) oferecem a melhor relação preço-desempenho e eficiência energética para cargas de trabalho em nuvem no Amazon EC2."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa ejecuta 500 instancias Linux de Amazon EC2 (c5.xlarge y m5.xlarge) que alojan microservicios en Go y Node.js. El CTO establece el objetivo de reducir los costos de computación en un 20% y mejorar la eficiencia energética, manteniendo o aumentando el rendimiento de las aplicaciones. ¿Qué mejora arquitectónica logra esto con una refactorización mínima de código?",
            "options": [
                {
                    "id": "A",
                    "text": "Cambiar todas las instancias a instancias ampliables T3-micro con modo de crédito estándar.",
                    "explanation": "Incorrecto: Las instancias T3-micro carecen de suficiente CPU/RAM para microservicios y sufrirán una severa limitación de CPU bajo cargas de producción sostenidas."
                },
                {
                    "id": "B",
                    "text": "Migrar las cargas de trabajo a familias de instancias basadas en AWS Graviton3/Graviton4 (como c7g y m7g) reconstruyendo imágenes de contenedores multiarquitectura para ARM64 (aarch64).",
                    "explanation": "Correcto: Los procesadores AWS Graviton ofrecen hasta un 40% más de relación precio-rendimiento y un 60% menos de consumo de energía en comparación con instancias x86 equivalentes, requiriendo solo la recompilación de imágenes de contenedores para ARM64."
                },
                {
                    "id": "C",
                    "text": "Convertir todas las instancias a Hosts Dedicados (Dedicated Hosts) con compromisos de 3 años.",
                    "explanation": "Incorrecto: Los hosts dedicados son significativamente más caros y están destinados al cumplimiento de licencias por socket físico."
                },
                {
                    "id": "D",
                    "text": "Migrar las aplicaciones a instancias EC2 de Windows Server con aceleración de hardware x86.",
                    "explanation": "Incorrecto: Windows Server incurre en tarifas de licencia de sistema operativo adicionales y aumenta los costos de cómputo."
                }
            ],
            "generalExplanation": "Los procesadores AWS Graviton (silicio ARM64 personalizado) proporcionan la mejor relación precio-rendimiento y eficiencia energética para cargas de trabajo en la nube en Amazon EC2."
        }
    },
    "sap-sim2-q017": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma corporação jurídica armazena 100 milhões de documentos contratuais digitalizados no Amazon S3. Os documentos são acessados com frequência durante os primeiros 30 dias, acessados de 1 a 2 vezes por mês entre o dia 31 e 180, e raramente acessados após 180 dias (a recuperação dentro de minutos a horas é aceitável após o dia 180). Qual configuração de ciclo de vida do S3 (S3 Lifecycle) minimiza os custos totais de armazenamento?",
            "options": [
                {
                    "id": "A",
                    "text": "Manter todos os objetos no S3 Standard por 7 anos e habilitar o S3 Object Lock.",
                    "explanation": "Incorreto: Reter 100 milhões de objetos no S3 Standard por 7 anos é extremamente caro em comparação com o armazenamento em camadas de arquivo."
                },
                {
                    "id": "B",
                    "text": "Fazer a transição de objetos para o S3 Glacier Deep Archive imediatamente no primeiro dia.",
                    "explanation": "Incorreto: Mover objetos para o Glacier Deep Archive no primeiro dia impede o acesso em tempo real durante os primeiros 30 dias de litígio ativo."
                },
                {
                    "id": "C",
                    "text": "Fazer a transição de objetos do S3 Standard para o S3 Standard-Infrequent Access (S3 Standard-IA) após 30 dias, para o S3 Glacier Flexible Archive após 180 dias, e configurar o S3 Intelligent-Tiering para prefixos com padrões de acesso não determinísticos.",
                    "explanation": "Correto: Essa transição de ciclo de vida otimiza o custo de armazenamento em cada limite de tempo: Standard para os dias 1 a 30, Standard-IA para os dias 31 a 180 (acesso pouco frequente em milissegundos) e Glacier Flexible Archive para arquivamento de longo prazo de baixo custo."
                },
                {
                    "id": "D",
                    "text": "Armazenar todos os arquivos em volumes Amazon EBS sc1 anexados a instâncias EC2.",
                    "explanation": "Incorreto: O armazenamento em volumes EBS é muito mais caro por GB do que o S3 Glacier e não pode escalar elasticamente para 100 milhões de arquivos."
                }
            ],
            "generalExplanation": "A aplicação de regras de ciclo de vida do S3 para fazer a transição progressiva de objetos de S3 Standard -> Standard-IA -> Glacier Flexible Archive reduz os gastos com armazenamento em até 80-90%."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una corporación jurídica almacena 100 millones de documentos de contratos escaneados en Amazon S3. Se accede a los documentos con frecuencia durante los primeros 30 días, se accede 1 o 2 veces al mes entre el día 31 y el 180, y rara vez se accede después de 180 días (la recuperación en minutos u horas es aceptable después del día 180). ¿Qué configuración de ciclo de vida de S3 (S3 Lifecycle) minimiza los costos totales de almacenamiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Mantener todos los objetos en S3 Standard durante 7 años y habilitar S3 Object Lock.",
                    "explanation": "Incorrecto: Conservar 100 millones de objetos en S3 Standard durante 7 años es extremadamente costoso en comparación con el almacenamiento en niveles de archivo."
                },
                {
                    "id": "B",
                    "text": "Realizar la transición de objetos a S3 Glacier Deep Archive inmediatamente el día 1.",
                    "explanation": "Incorrecto: Mover objetos a Glacier Deep Archive el día 1 impide el acceso en tiempo real durante los primeros 30 días de litigio activo."
                },
                {
                    "id": "C",
                    "text": "Realizar la transición de objetos de S3 Standard a S3 Standard-Infrequent Access (S3 Standard-IA) después de 30 días, a S3 Glacier Flexible Archive después de 180 días, y configurar S3 Intelligent-Tiering para prefijos no deterministas.",
                    "explanation": "Correcto: Esta transición del ciclo de vida optimiza el precio del almacenamiento en cada límite de tiempo: Standard para los días 1-30, Standard-IA para los días 31-180 (acceso poco frecuente en milisegundos) y Glacier Flexible Archive para archivado a largo plazo y bajo costo."
                },
                {
                    "id": "D",
                    "text": "Almacenar todos los archivos en volúmenes Amazon EBS sc1 adjuntos a instancias EC2.",
                    "explanation": "Incorrecto: El almacenamiento en volúmenes EBS es mucho más caro por GB que S3 Glacier y no puede escalar elásticamente a 100 millones de archivos."
                }
            ],
            "generalExplanation": "Aplicar reglas de ciclo de vida de S3 para realizar una transición progresiva de objetos de S3 Standard -> Standard-IA -> Glacier Flexible Archive reduce el gasto de almacenamiento hasta en un 80-90%."
        }
    },
    "sap-sim2-q018": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa exige uma estratégia centralizada e automatizada de gerenciamento de backup em 60 contas AWS no AWS Organizations. A política de backup determina backups automatizados diários de volumes Amazon EBS, bancos de dados Amazon RDS, tabelas do Amazon DynamoDB e buckets do Amazon S3, com replicação automatizada entre regiões para uma região secundária de recuperação de desastres, criptografados com uma KMS CMK e protegidos contra exclusão acidental ou maliciosa por administradores não autorizados (conformidade WORM). Qual solução atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar o AWS Backup com políticas de backup em toda a organização, habilitar o AWS Backup Vault Lock no modo de conformidade (Compliance mode) nos cofres de backup e configurar regras de cópia entre regiões para um cofre secundário de recuperação de desastres.",
                    "explanation": "Correto: O AWS Backup centraliza a proteção de dados em vários serviços e contas. O AWS Backup Vault Lock no modo Compliance impede que qualquer usuário (incluindo a conta root) exclua backups ou altere períodos de retenção."
                },
                {
                    "id": "B",
                    "text": "Escrever scripts personalizados em Python usando o AWS Lambda que executem APIs de snapshot diariamente e salvem os snapshots em volumes EBS locais.",
                    "explanation": "Incorreto: Scripts personalizados exigem manutenção extensiva, carecem de governança organizacional centralizada e não podem impor a conformidade WORM do Vault Lock."
                },
                {
                    "id": "C",
                    "text": "Implantar agentes do AWS DataSync em todas as instâncias EC2 para copiar dados brutos de volumes EBS em nível de bloco diretamente para bibliotecas de fitas virtuais locais.",
                    "explanation": "Incorreto: O DataSync não pode copiar blocos brutos de volumes EBS diretamente para unidades de fita locais nem fornecer políticas de backup automatizadas para várias contas."
                },
                {
                    "id": "D",
                    "text": "Configurar uma regra de ciclo de vida do Amazon S3 para transferir arquivos de snapshot do EBS para o S3 Glacier Deep Archive com o versionamento do S3 habilitado.",
                    "explanation": "Incorreto: Volumes EBS são dispositivos de armazenamento em bloco e não suportam versionamento do S3."
                }
            ],
            "generalExplanation": "O AWS Backup com políticas em toda a organização e o AWS Backup Vault Lock fornecem proteção de dados centralizada, imutável (WORM), entre contas e entre regiões."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa requiere una estrategia centralizada y automatizada de administración de copias de seguridad en 60 cuentas de AWS en AWS Organizations. La directiva de respaldo exige copias de seguridad automatizadas diarias de volúmenes de Amazon EBS, bases de datos de Amazon RDS, tablas de Amazon DynamoDB y buckets de Amazon S3, con replicación entre regiones automatizada hacia una región secundaria de recuperación ante desastres, cifrada con una CMK de KMS y protegida contra la eliminación accidental o malintencionada por administradores no autorizados (cumplimiento WORM). ¿Qué solución cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar AWS Backup con directivas de respaldo en toda la organización, habilitar AWS Backup Vault Lock en modo de cumplimiento (Compliance mode) en los almacenes de respaldo y configurar reglas de copia entre regiones hacia un almacén secundario de recuperación ante desastres.",
                    "explanation": "Correcto: AWS Backup centraliza la protección de datos en múltiples servicios y cuentas. AWS Backup Vault Lock en modo Compliance evita que cualquier usuario (incluido root) elimine copias de seguridad o altere los períodos de retención."
                },
                {
                    "id": "B",
                    "text": "Escribir scripts personalizados de Python mediante AWS Lambda que ejecuten API de instantáneas a diario y guarden instantáneas en volúmenes EBS locales.",
                    "explanation": "Incorrecto: Los scripts personalizados requieren un mantenimiento extenso, carecen de gobernanza organizacional centralizada y no pueden aplicar el cumplimiento WORM de Vault Lock."
                },
                {
                    "id": "C",
                    "text": "Implementar agentes de AWS DataSync en todas las instancias EC2 para copiar datos de volúmenes EBS a nivel de bloque sin procesar directamente en bibliotecas de cintas virtuales locales.",
                    "explanation": "Incorrecto: DataSync no puede copiar bloques de volúmenes EBS sin formato directamente a unidades de cinta locales ni proporcionar políticas de respaldo automatizadas para múltiples cuentas."
                },
                {
                    "id": "D",
                    "text": "Configurar una regla de ciclo de vida de Amazon S3 para realizar la transición de archivos de instantáneas de EBS a S3 Glacier Deep Archive con el control de versiones de S3 habilitado.",
                    "explanation": "Incorrecto: Los volúmenes EBS son dispositivos de almacenamiento en bloque y no admiten el control de versiones de S3."
                }
            ],
            "generalExplanation": "AWS Backup con directivas en toda la organización y AWS Backup Vault Lock proporciona protección de datos centralizada, inmutable (WORM), entre cuentas y entre regiones."
        }
    },
    "sap-sim2-q019": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma equipe de operações gerencia centenas de instâncias Linux do Amazon EC2. Quando uma instância fica com pouco espaço em disco (uso de disco > 90%), o sistema deve executar automaticamente um runbook do AWS Systems Manager Automation para limpar arquivos de log temporários em `/tmp` e redimensionar o volume EBS sem intervenção manual de engenheiros. Como esse pipeline de autorrecuperação automatizado deve ser arquitetado?",
            "options": [
                {
                    "id": "A",
                    "text": "Anexar uma IAM Role com AdministratorAccess a todas as instâncias EC2 e permitir que os desenvolvedores acessem via SSH manualmente.",
                    "explanation": "Incorreto: A intervenção manual via SSH viola o princípio de autorrecuperação automatizada, e conceder AdministratorAccess viola o princípio do privilégio mínimo."
                },
                {
                    "id": "B",
                    "text": "Configurar um grupo do EC2 Auto Scaling com um tamanho mínimo de 100 instâncias.",
                    "explanation": "Incorreto: Escalar horizontalmente o número de instâncias não resolve o esgotamento de espaço em disco em instâncias individuais com estado (stateful)."
                },
                {
                    "id": "C",
                    "text": "Instalar o agente unificado do Amazon CloudWatch em todas as instâncias EC2 para coletar a métrica `disk_used_percent`, criar um alarme do CloudWatch para uso de disco > 90%, configurar o alarme para notificar uma regra do Amazon EventBridge e acionar um runbook do AWS Systems Manager Automation com parâmetros de execução.",
                    "explanation": "Correto: O agente do CloudWatch coleta métricas de disco no nível do sistema operacional. Quando o alarme dispara, o EventBridge encaminha o evento para um runbook do SSM Automation para limpar arquivos e invocar dinamicamente o EBS Elastic Volumes."
                },
                {
                    "id": "D",
                    "text": "Agendar um cron job a cada hora em cada instância que reinicie o sistema operacional.",
                    "explanation": "Incorreto: Reiniciar servidores interrompe transações ativas e não libera logs persistentes em disco nem redimensiona volumes EBS."
                }
            ],
            "generalExplanation": "O uso do agente unificado do CloudWatch para métricas de SO combinado com alarmes do CloudWatch, EventBridge e runbooks do AWS Systems Manager Automation possibilita operações de autorrecuperação automatizadas e sem servidor."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Un equipo de operaciones administra cientos de instancias Linux de Amazon EC2. Cuando una instancia se queda con poco espacio en disco (uso de disco > 90%), el sistema debe ejecutar automáticamente un runbook de AWS Systems Manager Automation para limpiar los archivos de registro temporales en `/tmp` y redimensionar el volumen EBS sin intervención manual de ingenieros. ¿Cómo debería diseñarse esta canalización de autorreparación automatizada?",
            "options": [
                {
                    "id": "A",
                    "text": "Adjuntar un rol de IAM con AdministratorAccess a todas las instancias EC2 y permitir que los desarrolladores accedan por SSH manualmente.",
                    "explanation": "Incorrecto: La intervención manual por SSH viola la autorreparación automatizada y otorgar AdministratorAccess viola el privilegio mínimo."
                },
                {
                    "id": "B",
                    "text": "Configurar un grupo de EC2 Auto Scaling con un tamaño mínimo de 100 instancias.",
                    "explanation": "Incorrecto: Escalar horizontalmente el recuento de instancias no soluciona el agotamiento de espacio en disco en instancias individuales con estado."
                },
                {
                    "id": "C",
                    "text": "Instalar el agente unificado de Amazon CloudWatch en todas las instancias EC2 para recopilar métricas de `disk_used_percent`, crear una alarma de CloudWatch para uso de disco > 90%, configurar la alarma para notificar a una regla de Amazon EventBridge y activar un runbook de AWS Systems Manager Automation con parámetros de ejecución.",
                    "explanation": "Correcto: El agente de CloudWatch recopila métricas de disco a nivel del sistema operativo. Cuando se activa la alarma, EventBridge enruta el evento a un runbook de SSM Automation para limpiar archivos e invocar dinámicamente EBS Elastic Volumes."
                },
                {
                    "id": "D",
                    "text": "Programar un trabajo cron cada hora en cada instancia que reinicie el sistema operativo.",
                    "explanation": "Incorrecto: Reiniciar los servidores interrumpe las transacciones activas y no libera registros persistentes en disco ni redimensiona los volúmenes de EBS."
                }
            ],
            "generalExplanation": "El uso del agente unificado de CloudWatch para métricas del sistema operativo combinado con alarmas de CloudWatch, EventBridge y runbooks de AWS Systems Manager Automation permite operaciones de autorreparación automatizadas y sin servidor."
        }
    },
    "sap-sim2-q020": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Um backend de microsserviços sem servidor no AWS Lambda consulta um banco de dados Amazon Aurora PostgreSQL. Durante os picos de tráfego matinais, milhares de instâncias do Lambda são escaladas simultaneamente, abrindo milhares de conexões diretas com o banco de dados e esgotando a memória do banco de dados (`max_connections exceeded`), o que gera erros HTTP 500. Como o arquiteto de soluções deve resolver esse gargalo com o MÍNIMO de refatoração de código do aplicativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Aumentar o parâmetro `max_connections` no grupo de parâmetros do banco de dados Aurora para 500.000.",
                    "explanation": "Incorreto: Definir `max_connections` excessivamente alto causará falha na instância do banco de dados por esgotamento de memória RAM (cada conexão aloca memória dedicada)."
                },
                {
                    "id": "B",
                    "text": "Definir a simultaneidade reservada (reserved concurrency) em todas as funções do AWS Lambda para 1.",
                    "explanation": "Incorreto: Definir a simultaneidade reservada do Lambda para 1 estrangula todas as solicitações do aplicativo, degradando severamente o desempenho para os usuários."
                },
                {
                    "id": "C",
                    "text": "Implantar o Amazon RDS Proxy na VPC entre as funções do AWS Lambda e o banco de dados Aurora PostgreSQL, permitindo que as funções do Lambda compartilhem e reutilizem um pool gerenciado de conexões de banco de dados.",
                    "explanation": "Correto: O Amazon RDS Proxy agrupa e multiplexa conexões de banco de dados, protegendo bancos de dados relacionais contra o esgotamento de conexões causado por invocações intermitentes do AWS Lambda sem servidor."
                },
                {
                    "id": "D",
                    "text": "Migrar o banco de dados para um arquivo CSV no Amazon S3 consultado com o S3 Select.",
                    "explanation": "Incorreto: Arquivos CSV no S3 não podem substituir um banco de dados relacional OLTP PostgreSQL interativo."
                }
            ],
            "generalExplanation": "O Amazon RDS Proxy é um proxy de banco de dados totalmente gerenciado que mantém um pool de conexões estabelecidas, permitindo que milhares de funções Lambda sem servidor compartilhem conexões com eficiência sem sobrecarregar o banco de dados."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Un backend de microservicios sin servidor en AWS Lambda consulta una base de datos Amazon Aurora PostgreSQL. Durante los picos de tráfico matutinos, miles de instancias de Lambda escalan simultáneamente, abriendo miles de conexiones directas a la base de datos y agotando la memoria de la base de datos (`max_connections exceeded`), provocando errores HTTP 500. ¿Cómo debería el arquitecto de soluciones resolver este cuello de botella con la MENOR refactorización de código de aplicación?",
            "options": [
                {
                    "id": "A",
                    "text": "Aumentar el parámetro `max_connections` en el grupo de parámetros de la base de datos Aurora a 500.000.",
                    "explanation": "Incorrecto: Establecer `max_connections` excesivamente alto provocará que la instancia de la base de datos colapse debido al agotamiento de la memoria RAM (cada conexión asigna memoria dedicada)."
                },
                {
                    "id": "B",
                    "text": "Establecer la concurrencia reservada en todas las funciones de AWS Lambda en 1.",
                    "explanation": "Incorrecto: Establecer la concurrencia reservada de Lambda en 1 estrangula todas las solicitudes de la aplicación, creando una degradación severa del rendimiento para los usuarios."
                },
                {
                    "id": "C",
                    "text": "Implementar Amazon RDS Proxy en la VPC entre las funciones de AWS Lambda y la base de datos Aurora PostgreSQL, permitiendo que las funciones de Lambda compartan y reutilicen un grupo de conexiones de base de datos agrupadas.",
                    "explanation": "Correcto: Amazon RDS Proxy agrupa y multiplexa conexiones de base de datos, protegiendo las bases de datos relacionales del agotamiento de conexiones causado por invocaciones masivas de Lambda sin servidor."
                },
                {
                    "id": "D",
                    "text": "Migrar la base de datos a un archivo CSV de Amazon S3 consultado con S3 Select.",
                    "explanation": "Incorrecto: Los archivos CSV de S3 no pueden reemplazar una base de datos relacional OLTP interactiva como PostgreSQL."
                }
            ],
            "generalExplanation": "Amazon RDS Proxy es un proxy de base de datos totalmente administrado que mantiene un grupo de conexiones establecidas, lo que permite a miles de funciones Lambda sin servidor compartir conexiones de manera eficiente sin sobrecargar la base de datos."
        }
    },
    "sap-sim2-q021": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Um navio de pesquisa geológica em um local oceânico remoto coleta 300 TB de conjuntos de dados de sonar sísmico de alta resolução durante uma expedição de 3 semanas. O navio possui apenas um link de satélite de alta latência (largura de banda de 1 Mbps). Os conjuntos de dados devem ser transferidos com segurança para um data lake no Amazon S3 em us-west-2 imediatamente após a atracação no porto, e contêineres de análise sísmica devem executar o pré-processamento de computação na borda (edge compute) nos dados enquanto estiverem no mar. Qual solução o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um AWS Storage Gateway Volume Gateway através da conexão via satélite.",
                    "explanation": "Incorreto: O Volume Gateway não consegue fazer upload de 300 TB em uma conexão de 1 Mbps sem acúmulo massivo de fila e latência impraticável."
                },
                {
                    "id": "B",
                    "text": "Comprimir os dados com formato zip e enviar os arquivos por anexos de e-mail para a equipe de operações em nuvem.",
                    "explanation": "Incorreto: Sistemas de e-mail possuem limites de anexo de 25 MB e não conseguem transportar 300 TB de dados científicos."
                },
                {
                    "id": "C",
                    "text": "Implantar vários dispositivos AWS Snowball Edge Storage Optimized com recursos de computação a bordo do navio para executar contêineres de pré-processamento, armazenar dados localmente no mar e enviar os dispositivos via correio expresso para a AWS após a atracação.",
                    "explanation": "Correto: O AWS Snowball Edge Storage Optimized oferece armazenamento local de blocos/objetos (até 80-210 TB por dispositivo) e capacidade de computação EC2/Lambda para processamento de borda em ambientes desconectados, seguido de trânsito físico para os data centers da AWS."
                },
                {
                    "id": "D",
                    "text": "Transmitir os 300 TB de dados brutos continuamente pelo link de satélite de 1 Mbps usando o AWS DataSync.",
                    "explanation": "Incorreto: Transferir 300 TB por um link de satélite de 1 Mbps levaria mais de 75 anos para ser concluído."
                }
            ],
            "generalExplanation": "Os dispositivos AWS Snowball Edge Storage Optimized são ideais para ambientes remotos de computação de borda com conectividade de rede limitada ou inexistente, fornecendo computação local e transferência física de dados em alta capacidade."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Un barco de investigación geológica en una ubicación oceánica remota recopila 300 TB de conjuntos de datos de sonar sísmico de alta resolución durante una expedición de 3 semanas. El barco solo dispone de un enlace satelital de alta latencia (ancho de banda de 1 Mbps). Los conjuntos de datos deben transferirse de forma segura a un lago de datos de Amazon S3 en us-west-2 inmediatamente después de atracar en el puerto, y los contenedores de análisis sísmico deben ejecutar el preprocesamiento de cómputo en el borde (edge compute) en los datos mientras están en el mar. ¿Qué solución debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un AWS Storage Gateway Volume Gateway a través de la conexión satelital.",
                    "explanation": "Incorrecto: Volume Gateway no puede cargar 300 TB a través de una conexión de 1 Mbps sin una acumulación masiva de colas y latencia inviable."
                },
                {
                    "id": "B",
                    "text": "Comprimir los datos con zip y enviar archivos mediante archivos adjuntos de correo electrónico al equipo de operaciones en la nube.",
                    "explanation": "Incorrecto: Los sistemas de correo electrónico tienen límites de archivos adjuntos de 25 MB y no pueden transportar 300 TB de datos científicos."
                },
                {
                    "id": "C",
                    "text": "Implementar múltiples dispositivos AWS Snowball Edge Storage Optimized con capacidades de cómputo a bordo del barco para ejecutar contenedores de preprocesamiento, almacenar datos localmente en el mar y enviar los dispositivos mediante mensajería urgente a AWS tras el atraque.",
                    "explanation": "Correcto: AWS Snowball Edge Storage Optimized proporciona almacenamiento integrado de bloques/objetos (hasta 80-210 TB por dispositivo) y capacidad de cómputo EC2/Lambda para procesamiento en el borde en entornos desconectados, seguido del tránsito físico hacia los centros de datos de AWS."
                },
                {
                    "id": "D",
                    "text": "Transmitir los 300 TB de datos sin procesar de forma continua a través del enlace satelital de 1 Mbps utilizando AWS DataSync.",
                    "explanation": "Incorrecto: Transferir 300 TB a través de un enlace satelital de 1 Mbps tardaría más de 75 años en completarse."
                }
            ],
            "generalExplanation": "Los dispositivos AWS Snowball Edge Storage Optimized son ideales para entornos informáticos remotos y perimetrales con conectividad de red limitada o nula, proporcionando computación local y transferencia física de datos de alta capacidad."
        }
    },
    "sap-sim2-q022": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa varejista está migrando um catálogo de produtos de alto rendimento de um conjunto de réplicas (replica set) do MongoDB local (on-premises) para o Amazon DocumentDB (compatível com MongoDB). A migração deve capturar alterações contínuas em tempo real (CDC) durante a carga inicial de dados com zero perda de dados e realizar a transição final (cutover) durante uma janela de manutenção de 10 minutos. Qual combinação de serviços deve ser usada?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Database Migration Service (AWS DMS) configurado com endpoint de origem MongoDB (usando o oplog do conjunto de réplicas para CDC) e endpoint de destino Amazon DocumentDB, executando Carga Completa mais Replicação Contínua (Full Load plus Ongoing Replication) até o cutover.",
                    "explanation": "Correto: O AWS DMS suporta endpoints de origem MongoDB com CDC lendo o oplog do conjunto de réplicas do MongoDB, replicando alterações em tempo quase real para o Amazon DocumentDB até o cutover final."
                },
                {
                    "id": "B",
                    "text": "Exportar dados do MongoDB para arquivos BSON usando `mongodump` e importar usando `mongorestore` após parar todos os servidores de aplicativos locais por 3 dias.",
                    "explanation": "Incorreto: Interromper os servidores de aplicativos de produção por 3 dias viola os requisitos de disponibilidade de negócios."
                },
                {
                    "id": "C",
                    "text": "Usar o AWS Schema Conversion Tool (AWS SCT) para converter documentos JSON do MongoDB em tabelas SQL do Amazon RDS.",
                    "explanation": "Incorreto: O destino é o Amazon DocumentDB (NoSQL compatível com MongoDB), e não SQL relacional."
                },
                {
                    "id": "D",
                    "text": "Implantar o AWS Application Migration Service (AWS MGN) para converter nós do MongoDB em funções do AWS Lambda.",
                    "explanation": "Incorreto: O AWS MGN converte servidores em instâncias EC2, e não mecanismos de banco de dados em funções Lambda."
                }
            ],
            "generalExplanation": "O AWS DMS suporta nativamente conjuntos de réplicas do MongoDB como endpoints de origem usando o oplog para Captura de Dados de Alteração (CDC), sincronizando dados continuamente com o Amazon DocumentDB."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa minorista está migrando un catálogo de productos de alto rendimiento desde un conjunto de réplicas (replica set) de MongoDB local a Amazon DocumentDB (con compatibilidad con MongoDB). La migración debe capturar cambios continuos en vivo (CDC) durante la carga inicial de datos sin pérdida de datos y realizar la transición final (cutover) durante una ventana de mantenimiento de 10 minutos. ¿Qué combinación de servicios debe utilizarse?",
            "options": [
                {
                    "id": "A",
                    "text": "Utilizar AWS Database Migration Service (AWS DMS) configurado con el punto de enlace de origen de MongoDB (usando el oplog del conjunto de réplicas para CDC) y el punto de enlace de destino de Amazon DocumentDB, ejecutando Carga Completa más Replicación Continua (Full Load plus Ongoing Replication) hasta el cutover.",
                    "explanation": "Correcto: AWS DMS admite puntos de enlace de origen de MongoDB con CDC al rastrear el oplog del conjunto de réplicas de MongoDB, replicando cambios casi en tiempo real en Amazon DocumentDB hasta el corte final."
                },
                {
                    "id": "B",
                    "text": "Exportar datos de MongoDB a archivos BSON usando `mongodump` e importar usando `mongorestore` después de detener todos los servidores de aplicaciones locales durante 3 días.",
                    "explanation": "Incorrecto: Detener los servidores de aplicaciones de producción durante 3 días viola los requisitos de disponibilidad comercial."
                },
                {
                    "id": "C",
                    "text": "Utilizar AWS Schema Conversion Tool (AWS SCT) para convertir documentos JSON de MongoDB en tablas SQL de Amazon RDS.",
                    "explanation": "Incorrecto: El destino es Amazon DocumentDB (NoSQL compatible con MongoDB), no SQL relacional."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS Application Migration Service (AWS MGN) para convertir nodos de MongoDB en funciones de AWS Lambda.",
                    "explanation": "Incorrecto: AWS MGN convierte servidores en instancias EC2, no motores de bases de datos en funciones Lambda."
                }
            ],
            "generalExplanation": "AWS DMS admite de forma nativa conjuntos de réplicas de MongoDB como puntos de enlace de origen mediante el oplog para la Captura de Datos de Cambio (CDC) para sincronizar datos de forma continua con Amazon DocumentDB."
        }
    },
    "sap-sim2-q023": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa possui 80 aplicativos web legados em Java e .NET Framework em execução em máquinas virtuais locais com Windows e Linux. A equipe de desenvolvimento não possui experiência em conteinerização (criação de Dockerfile e pipelines de CI/CD). A equipe de gestão deseja conteinerizar esses aplicativos legados e implantá-los no Amazon ECS e Amazon EKS com pipelines automatizados de CI/CD e esforço manual mínimo. Qual ferramenta da AWS foi desenvolvida especificamente para essa modernização?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar agentes do AWS DataSync em máquinas virtuais locais para transferir sistemas de arquivos para o Amazon S3.",
                    "explanation": "Incorreto: O DataSync é um serviço de transferência de dados de armazenamento de arquivos e objetos."
                },
                {
                    "id": "B",
                    "text": "Configurar e implantar o AWS App2Container (A2C) seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Correto: O AWS App2Container (A2C) é uma ferramenta de linha de comando que analisa aplicativos Java e .NET em execução em máquinas virtuais, gera automaticamente imagens de contêiner, define definições de tarefas do ECS/EKS e provisiona pipelines de implantação CI/CD."
                },
                {
                    "id": "C",
                    "text": "Configurar e implantar o AWS Serverless Application Model (AWS SAM) seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O AWS SAM é uma estrutura de código aberto para criar aplicativos Lambda sem servidor, e não para conteinerizar aplicativos legados de VMs locais."
                },
                {
                    "id": "D",
                    "text": "Implantar o AWS Application Migration Service (AWS MGN) para realizar a replicação contínua de servidores em nível de bloco sem interrupções para a AWS.",
                    "explanation": "Incorreto: O AWS MGN realiza a migração lift-and-shift de imagens completas de SO de máquinas virtuais para o EC2, em vez de modernizar aplicativos em imagens de contêiner."
                }
            ],
            "generalExplanation": "O AWS App2Container (A2C) conteineriza automaticamente aplicativos legados em Java e .NET em execução em servidores locais e os prepara para implantação no Amazon ECS ou Amazon EKS."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa tiene 80 aplicaciones web heredadas de Java y .NET Framework ejecutándose en máquinas virtuales locales de Windows y Linux. El equipo de desarrollo no tiene experiencia en creación de contenedores (creación de Dockerfile y CI/CD). El equipo de administración desea empaquetar en contenedores estas aplicaciones heredadas e implementarlas en Amazon ECS y Amazon EKS con canalizaciones automatizadas de CI/CD y un esfuerzo manual mínimo. ¿Qué herramienta de AWS está diseñada específicamente para esta modernización?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar agentes de AWS DataSync en máquinas virtuales locales para transferir sistemas de archivos a Amazon S3.",
                    "explanation": "Incorrecto: DataSync es un servicio de transferencia de datos de almacenamiento de archivos y objetos."
                },
                {
                    "id": "B",
                    "text": "Configurar e implementar AWS App2Container (A2C) siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Correcto: AWS App2Container (A2C) es una herramienta de línea de comandos que analiza aplicaciones Java y .NET en ejecución en máquinas virtuales, genera automáticamente imágenes de contenedores, define definiciones de tareas de ECS/EKS y aprovisiona canalizaciones de implementación de CI/CD."
                },
                {
                    "id": "C",
                    "text": "Configurar e implementar AWS Serverless Application Model (AWS SAM) siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: AWS SAM es un marco de código abierto para crear aplicaciones Lambda sin servidor, no para empaquetar en contenedores aplicaciones heredadas de máquinas virtuales locales."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS Application Migration Service (AWS MGN) para realizar una replicación continua de servidores a nivel de bloque sin interrupciones en AWS.",
                    "explanation": "Incorrecto: AWS MGN realiza la migración tipo lift-and-shift de imágenes completas del sistema operativo de máquinas virtuales a EC2, en lugar de modernizar aplicaciones en imágenes de contenedores."
                }
            ],
            "generalExplanation": "AWS App2Container (A2C) empaqueta automáticamente en contenedores aplicaciones heredadas de Java y .NET que se ejecutan en servidores locales y las prepara para su implementación en Amazon ECS o Amazon EKS."
        }
    },
    "sap-sim2-q024": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa opera um grande aplicativo monolítico Microsoft .NET no Windows Server. A equipe de arquitetura de software deseja decompor o monólito em microsserviços independentes analisando o código-fonte, identificando contextos delimitados (bounded contexts), extraindo componentes de negócios individuais e implantando-os em contêineres Linux no Amazon ECS com AWS Fargate. Qual ferramenta da AWS acelera esse processo de refatoração?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Microservice Extractor for .NET",
                    "explanation": "Correto: O AWS Microservice Extractor for .NET simplifica a refatoração de aplicativos monolíticos .NET em microsserviços independentes, visualizando dependências de código, agrupando classes e extraindo serviços em projetos prontos para contêineres."
                },
                {
                    "id": "B",
                    "text": "Configurar e implantar o AWS Schema Conversion Tool (AWS SCT) seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O AWS SCT destina-se à conversão de esquemas de banco de dados, e não à refatoração de código-fonte de aplicativos .NET."
                },
                {
                    "id": "C",
                    "text": "Solicitar um dispositivo físico AWS Snowball Edge Storage Optimized para transportar imagens de disco de servidor offline.",
                    "explanation": "Incorreto: O Snowball Edge é um hardware físico de computação de borda, e não uma ferramenta de extração de microsserviços .NET."
                },
                {
                    "id": "D",
                    "text": "Implantar tarefas do AWS Database Migration Service (AWS DMS) para replicar tabelas de banco de dados continuamente no Amazon Aurora.",
                    "explanation": "Incorreto: O AWS DMS migra bancos de dados, e não código de aplicativo C#/.NET."
                }
            ],
            "generalExplanation": "O AWS Microservice Extractor for .NET auxilia os arquitetos na decomposição de grandes aplicativos monolíticos .NET em microsserviços por meio de análise de código e extração automatizada."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa opera una gran aplicación monolítica de Microsoft .NET en Windows Server. El equipo de arquitectura de software desea descomponer el monolito en microservicios independientes analizando el código fuente, identificando contextos delimitados (bounded contexts), extrayendo componentes comerciales individuales e implementándolos en contenedores Linux en Amazon ECS con AWS Fargate. ¿Qué herramienta de AWS acelera este proceso de refatoración?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Microservice Extractor for .NET",
                    "explanation": "Correcto: AWS Microservice Extractor for .NET simplifica la refactorización de aplicaciones monolíticas de .NET en microservicios independientes mediante la visualización de dependencias de código, la agrupación de clases y la extracción de servicios en proyectos listos para contenedores."
                },
                {
                    "id": "B",
                    "text": "Configurar e implementar AWS Schema Conversion Tool (AWS SCT) siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: AWS SCT sirve para la conversión de esquemas de bases de datos, no para la refactorización del código fuente de aplicaciones .NET."
                },
                {
                    "id": "C",
                    "text": "Solicitar un dispositivo físico AWS Snowball Edge Storage Optimized para transportar imágenes de disco de servidores fuera de línea.",
                    "explanation": "Incorrecto: Snowball Edge es hardware físico de computación perimetral, no una herramienta de extracción de microservicios .NET."
                },
                {
                    "id": "D",
                    "text": "Implementar tareas de AWS Database Migration Service (AWS DMS) para replicar tablas de bases de datos continuamente en Amazon Aurora.",
                    "explanation": "Incorrecto: AWS DMS migra bases de datos, no código de aplicación C#/.NET."
                }
            ],
            "generalExplanation": "AWS Microservice Extractor for .NET ayuda a los arquitectos a descomponer aplicaciones monolíticas grandes de .NET en microservicios mediante análisis de código y extracción automatizada."
        }
    },
    "sap-sim2-q025": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa de manufatura executa aplicativos críticos locais de SQL Server e SAP ERP em servidores físicos e virtuais. A empresa deseja implementar uma solução de recuperação de desastres (DR) para a AWS com RPO inferior a um segundo e RTO em minutos, minimizando os custos de licenciamento de computação ao evitar a execução contínua (24/7) de instâncias EC2 em espera (standby) de tamanho total durante operações normais. Qual serviço atende a esses critérios?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um cluster EC2 Multi-AZ em espera ativa (warm standby) executando licenças ativas do SQL Server Enterprise 24 horas por dia, 7 dias por semana na AWS.",
                    "explanation": "Incorreto: A execução de instâncias standby ativas de tamanho total 24/7 gera custos massivos e desnecessários de computação e licenciamento de software."
                },
                {
                    "id": "B",
                    "text": "Configurar e implantar o AWS Elastic Disaster Recovery (AWS DRS) seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Correto: O AWS Elastic Disaster Recovery (AWS DRS) replica continuamente o armazenamento em bloco local para uma área de preparação (staging) de baixo custo na AWS (usando EBS de baixo custo e pequenas instâncias de preparação), iniciando instâncias de computação de produção de tamanho total somente durante simulações ou failover de desastres.",
                },
                {
                    "id": "C",
                    "text": "Fazer backups noturnos em fita e enviá-los mensalmente para um data center da AWS.",
                    "explanation": "Incorreto: Backups em fita resultam em um RPO de 24 horas e RTO de dias/semanas, falhando no requisito de RPO inferior a um segundo."
                },
                {
                    "id": "D",
                    "text": "Configurar e implantar o AWS Storage Gateway Tape Gateway seguindo as melhores práticas empresariais do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O Tape Gateway destina-se à substituição de backups em fita de longo prazo no S3 Glacier, e não ao failover de aplicativos em tempo real e em menos de um minuto."
                }
            ],
            "generalExplanation": "O AWS Elastic Disaster Recovery (AWS DRS) minimiza o tempo de inatividade e a perda de dados fornecendo recuperação rápida e confiável de servidores físicos, virtuais e baseados em nuvem na AWS usando replicação contínua de preparação (staging) de baixo custo."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa de fabricación ejecuta aplicaciones críticas locales de SQL Server y SAP ERP en servidores físicos y virtuales. La empresa desea implementar una solución de recuperación ante desastres (DR) en AWS con un RPO de menos de un segundo y un RTO en minutos, al tiempo que minimiza los costos de licencias de cómputo al evitar ejecutar instancias EC2 en espera (standby) de tamaño completo las 24 horas del día, los 7 días de la semana durante las operaciones normales. ¿Qué servicio cumple con estos criterios?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un clúster EC2 Multi-AZ en espera activa (warm standby) que ejecute licencias activas de SQL Server Enterprise 24/7 en AWS.",
                    "explanation": "Incorrecto: Ejecutar instancias de reserva activas de tamaño completo 24/7 genera enormes costos innecesarios de cómputo y licencias de software."
                },
                {
                    "id": "B",
                    "text": "Configurar e implementar AWS Elastic Disaster Recovery (AWS DRS) siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Correcto: AWS Elastic Disaster Recovery (AWS DRS) replica continuamente el almacenamiento en bloque local en un área de ensayo (staging) de bajo costo en AWS (utilizando EBS de bajo costo y pequeñas instancias de preparación), iniciando instancias de cómputo de producción de tamaño completo solo durante pruebas o conmutación por error ante desastres."
                },
                {
                    "id": "C",
                    "text": "Realizar copias de seguridad nocturnas en cinta y enviarlas mensualmente a un centro de datos de AWS.",
                    "explanation": "Incorrecto: Las copias de seguridad en cinta producen un RPO de 24 horas y un RTO de días/semanas, lo que no cumple con el requisito de RPO inferior a un segundo."
                },
                {
                    "id": "D",
                    "text": "Configurar e implementar AWS Storage Gateway Tape Gateway siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Tape Gateway sirve para reemplazar copias de seguridad en cinta a largo plazo en S3 Glacier, no para conmutación por error de aplicaciones en tiempo real en menos de un minuto."
                }
            ],
            "generalExplanation": "AWS Elastic Disaster Recovery (AWS DRS) minimiza el tiempo de inactividad y la pérdida de datos al proporcionar una recuperación rápida y confiable de servidores físicos, virtuales y basados en la nube en AWS mediante la replicación continua en un entorno de preparación de bajo costo."
        }
    }
}
