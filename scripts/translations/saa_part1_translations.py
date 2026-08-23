"""
Translations for AWS Certified Solutions Architect - Associate (SAA-C03) Exam Questions 1 to 33.
Part 1 of the translation dataset.
"""

TRANSLATIONS = {
    "saa-q001": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma grande empresa armazena seus ativos web em um bucket privado do Amazon S3 e os distribui globalmente usando o Amazon CloudFront. O diretor de segurança exige que todos os ativos web sejam acessíveis estritamente por meio do domínio da distribuição do CloudFront e nunca por meio de URLs diretas do S3. Além disso, a arquitetura deve oferecer suporte à criptografia no lado do servidor com chaves gerenciadas pelo cliente do AWS KMS (SSE-KMS) e seguir as melhores práticas de segurança mais recentes da AWS. Qual solução atende a esses requisitos com a MENOR sobrecarga operacional?",
            "options": [
                {
                    "id": "A",
                    "text": "Colocar o bucket do S3 dentro de uma sub-rede privada de VPC e criar um Gateway VPC Endpoint para rotear o tráfego do CloudFront diretamente para a VPC.",
                    "explanation": "Incorreto: Os buckets do Amazon S3 são endpoints públicos regionais que não podem ser colocados dentro de uma sub-rede de VPC, e o CloudFront é um serviço de borda global que não pode ser roteado para Gateway Endpoints."
                },
                {
                    "id": "B",
                    "text": "Configurar uma política de bucket do S3 permitindo acesso de leitura público, mas aplicar uma condição baseada em IP restringindo as solicitações aos blocos CIDR corporativos.",
                    "explanation": "Incorreto: Usuários globais acessam o CloudFront a partir de endereços IP dinâmicos arbitrários em todo o mundo, tornando a restrição por IP estático inviável e insegura."
                },
                {
                    "id": "C",
                    "text": "Implantar uma Origin Access Identity (OAI) legada e configurar a política de bucket do S3 para conceder permissões de leitura ao principal da OAI.",
                    "explanation": "Incorreto: A OAI é um mecanismo legado que não oferece suporte a SSE-KMS com chaves gerenciadas pelo cliente nem a regiões da AWS lançadas após 2022 sem soluções alternativas complexas."
                },
                {
                    "id": "D",
                    "text": "Criar um Origin Access Control (OAC) para a distribuição do CloudFront, associá-lo à origem do S3 e atualizar a política do bucket do S3 para permitir acesso de leitura exclusivamente ao service principal do CloudFront com uma condição que corresponda ao ARN da distribuição.",
                    "explanation": "Correto: O Origin Access Control (OAC) é a solução moderna e recomendada pela AWS que oferece suporte nativo a SSE-KMS, métodos HTTP dinâmicos e permissões granulares de service principal do IAM em buckets do S3."
                }
            ],
            "generalExplanation": "O Amazon CloudFront Origin Access Control (OAC) fornece segurança aprimorada para origens do S3 com suporte total a SSE-KMS, a todas as regiões da AWS e a políticas baseadas em recursos refinadas usando o AWS Signature Version 4 (SigV4)."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una empresa aloja sus recursos web en un bucket privado de Amazon S3 y los distribuye globalmente mediante Amazon CloudFront. El responsable de seguridad exige que todos los recursos web sean accesibles estrictamente a través del dominio de distribución de CloudFront y nunca mediante URLs directas de S3. Además, la arquitectura debe admitir el cifrado del lado del servidor con claves administradas por el cliente de AWS KMS (SSE-KMS) y seguir las mejores prácticas de seguridad más recientes de AWS. ¿Qué solución cumple con estos requisitos con la MENOR sobrecarga operativa?",
            "options": [
                {
                    "id": "A",
                    "text": "Ubicar el bucket de S3 dentro de una subred de VPC privada y crear un Gateway VPC Endpoint para enrutar el tráfico de CloudFront directamente hacia la VPC.",
                    "explanation": "Incorrecto: Los buckets de Amazon S3 son puntos de enlace públicos regionales que no se pueden colocar dentro de una subred de VPC, y CloudFront es un servicio global perimetral que no se puede enrutar hacia Gateway Endpoints."
                },
                {
                    "id": "B",
                    "text": "Configurar una política de bucket de S3 que permita el acceso de lectura público, pero aplicar una condición basada en IP que restrinja las solicitudes a los bloques CIDR corporativos.",
                    "explanation": "Incorrecto: Los usuarios globales acceden a CloudFront desde direcciones IP dinámicas arbitrarias en todo el mundo, lo que hace que la restricción por IP estática sea inviable e insegura."
                },
                {
                    "id": "C",
                    "text": "Implementar una Origin Access Identity (OAI) heredada y configurar la política del bucket de S3 para otorgar permisos de lectura al principal de la OAI.",
                    "explanation": "Incorrecto: OAI es un mecanismo heredado que no admite SSE-KMS con claves administradas por el cliente ni regiones de AWS lanzadas después de 2022 sin soluciones complejas."
                },
                {
                    "id": "D",
                    "text": "Crear un Origin Access Control (OAC) para la distribución de CloudFront, asociarlo al origen de S3 y actualizar la política del bucket de S3 para permitir el acceso de lectura exclusivamente al service principal de CloudFront con una condición que coincida con el ARN de la distribución.",
                    "explanation": "Correcto: Origin Access Control (OAC) es la solución moderna y recomendada por AWS que admite de forma nativa SSE-KMS, métodos HTTP dinámicos y permisos granulares de service principal de IAM en buckets de S3."
                }
            ],
            "generalExplanation": "Amazon CloudFront Origin Access Control (OAC) proporciona seguridad mejorada para orígenes de S3 con soporte completo para SSE-KMS, todas las regiones de AWS y políticas detalladas basadas en recursos mediante AWS Signature Version 4 (SigV4)."
        }
    },
    "saa-q002": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma empresa executa uma aplicação de processamento de transações financeiras em instâncias do Amazon EC2 que consultam um banco de dados Amazon RDS PostgreSQL. A conformidade regulatória exige que as credenciais do banco de dados sejam rotacionadas automaticamente a cada 30 dias, sem intervenção manual ou tempo de inatividade da aplicação. Qual solução atende a esses requisitos de conformidade com a MENOR sobrecarga de desenvolvimento e manutenção?",
            "options": [
                {
                    "id": "A",
                    "text": "Armazenar as credenciais do banco de dados no AWS Systems Manager Parameter Store como um parâmetro SecureString e agendar uma regra do Amazon EventBridge para invocar um script Python personalizado em um bastion host do EC2 a cada 30 dias.",
                    "explanation": "Incorreto: O SSM Parameter Store não oferece suporte nativo à rotação automatizada integrada, exigindo manutenção de servidores e scripts personalizados."
                },
                {
                    "id": "B",
                    "text": "Armazenar as credenciais do banco de dados no AWS Secrets Manager e habilitar a rotação automática usando o modelo integrado de função de rotação do AWS Lambda configurado para o Amazon RDS PostgreSQL.",
                    "explanation": "Correto: O AWS Secrets Manager integra-se nativamente com o Amazon RDS para fornecer rotação de credenciais automatizada e pronta para uso em uma programação configurável (como 30 dias), utilizando modelos predefinidos do Lambda."
                },
                {
                    "id": "C",
                    "text": "Codificar rigidamente (hardcode) as credenciais do banco de dados nos arquivos de configuração da aplicação e usar o AWS CodeDeploy para realizar implantações blue/green automatizadas a cada 30 dias com novas credenciais.",
                    "explanation": "Incorreto: Codificar segredos no código viola as melhores práticas de segurança, e reimplementações blue/green não rotacionam a senha real do usuário dentro do RDS."
                },
                {
                    "id": "D",
                    "text": "Criar uma role do IAM anexada às instâncias do EC2 com uma política inline do IAM contendo a senha mestra do RDS em texto simples e definir uma política de expiração de credenciais do IAM.",
                    "explanation": "Incorreto: Segredos em texto simples em políticas do IAM ficam expostos no CloudTrail/console, e a expiração de credenciais do IAM não altera a senha do banco de dados."
                }
            ],
            "generalExplanation": "O AWS Secrets Manager foi projetado especificamente para gerenciar, recuperar e rotacionar automaticamente segredos de banco de dados e chaves de API usando modelos nativos de rotação do AWS Lambda."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una empresa ejecuta una aplicación de procesamiento de transacciones financieras en instancias de Amazon EC2 que consultan una base de datos Amazon RDS PostgreSQL. El cumplimiento normativo exige que las credenciales de la base de datos se roten automáticamente cada 30 días sin intervención manual ni tiempo de inactividad de la aplicación. ¿Qué solución cumple con estos requisitos con la MENOR sobrecarga de desarrollo y mantenimiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Almacenar las credenciales de la base de datos en AWS Systems Manager Parameter Store como un parámetro SecureString y programar una regla de Amazon EventBridge para invocar un script Python personalizado en un bastion host de EC2 cada 30 días.",
                    "explanation": "Incorrecto: SSM Parameter Store no admite rotación automática integrada de forma nativa, lo que requiere secuencias de comandos y mantenimiento de servidores personalizados."
                },
                {
                    "id": "B",
                    "text": "Almacenar las credenciales de la base de datos en AWS Secrets Manager y habilitar la rotación automática mediante la plantilla integrada de función de rotación de AWS Lambda configurada para Amazon RDS PostgreSQL.",
                    "explanation": "Correcto: AWS Secrets Manager se integra de forma nativa con Amazon RDS para ofrecer rotación de credenciales automatizada y lista para usar según una programación configurable (como 30 días) mediante plantillas de Lambda prediseñadas."
                },
                {
                    "id": "C",
                    "text": "Codificar directamente (hardcode) las credenciales de la base de datos en los archivos de configuración de la aplicación y usar AWS CodeDeploy para realizar implementaciones blue/green automatizadas cada 30 días con nuevas credenciales.",
                    "explanation": "Incorrecto: Incluir secretos en el código fuente infringe las mejores prácticas de seguridad, y las reimplementaciones blue/green no rotan la contraseña real del usuario dentro de RDS."
                },
                {
                    "id": "D",
                    "text": "Crear un rol de IAM asociado a las instancias de EC2 con una política en línea de IAM que contenga la contraseña maestra de RDS en texto plano y establecer una política de expiración de credenciales de IAM.",
                    "explanation": "Incorrecto: Los secretos en texto plano en políticas de IAM quedan expuestos en CloudTrail/consola, y la caducidad de credenciales de IAM no modifica la contraseña de la base de datos."
                }
            ],
            "generalExplanation": "AWS Secrets Manager está diseñado específicamente para administrar, recuperar y rotar automáticamente secretos de bases de datos y claves de API mediante plantillas nativas de rotación de AWS Lambda."
        }
    },
    "saa-q003": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Um arquiteto de soluções está projetando uma aplicação web em camadas em uma Amazon VPC distribuída em duas Zonas de Disponibilidade. A sub-rede pública contém um Application Load Balancer (ALB), enquanto os servidores da aplicação web são executados em instâncias do Amazon EC2 em sub-redes privadas. A política de segurança determina que as instâncias do EC2 devem aceitar apenas tráfego HTTP/HTTPS originado do ALB e rejeitar rigorosamente conexões diretas de qualquer outra fonte. Como os security groups devem ser configurados?",
            "options": [
                {
                    "id": "A",
                    "text": "Atribuir endereços IP elásticos às instâncias privadas do EC2 e incluir na lista de permissões apenas os endereços IP públicos do ALB no security group do EC2.",
                    "explanation": "Incorreto: Instâncias privadas do EC2 não devem ter IPs elásticos, e os endereços IP do ALB são dinâmicos em vez de fixos."
                },
                {
                    "id": "B",
                    "text": "Atribuir um security group às instâncias do EC2 com uma regra de entrada que permita o tráfego nas portas da aplicação referenciando o ID do security group do ALB como origem.",
                    "explanation": "Correto: Security groups podem referenciar outros security groups por ID. Isso garante que apenas o tráfego que passa pelo security group do ALB seja aceito pelas instâncias do EC2, independentemente de mudanças de IP."
                },
                {
                    "id": "C",
                    "text": "Configurar a Network ACL na sub-rede privada para permitir tráfego de entrada dos blocos CIDR das sub-redes públicas nas portas 80 e 443.",
                    "explanation": "Incorreto: A filtragem por CIDR de sub-rede em Network ACLs não restringe o tráfego exclusivamente ao ALB, pois qualquer recurso na sub-rede pública poderia acessar as instâncias privadas."
                },
                {
                    "id": "D",
                    "text": "Configurar o security group do EC2 com uma regra de entrada permitindo 0.0.0.0/0 nas portas 80 e 443 e configurar uma regra iptables em cada instância do EC2.",
                    "explanation": "Incorreto: Abrir para 0.0.0.0/0 viola o princípio do menor privilégio e gerenciar regras de iptables em instâncias individuais aumenta a complexidade operacional."
                }
            ],
            "generalExplanation": "Referenciar o security group do ALB diretamente dentro da regra de entrada do security group das instâncias privadas impõe um isolamento de rede rígido de menor privilégio e se adapta automaticamente a alterações de IP do ALB."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un arquitecto de soluciones está diseñando una aplicación web multicapa en una Amazon VPC distribuida en dos Zonas de Disponibilidad. La subred pública contiene un Application Load Balancer (ALB), mientras que los servidores de aplicaciones web se ejecutan en instancias de Amazon EC2 en subredes privadas. La política de seguridad exige que las instancias de EC2 solo acepten tráfico HTTP/HTTPS originado desde el ALB y rechacen estrictamente conexiones directas desde cualquier otra fuente. ¿Cómo se deben configurar los security groups?",
            "options": [
                {
                    "id": "A",
                    "text": "Asignar direcciones IP elásticas a las instancias privadas de EC2 y autorizar únicamente las direcciones IP públicas del ALB en el security group de EC2.",
                    "explanation": "Incorrecto: Las instancias privadas de EC2 no deben tener IPs elásticas, y las direcciones IP del ALB son dinámicas en lugar de fijas."
                },
                {
                    "id": "B",
                    "text": "Asignar un security group a las instancias de EC2 con una regla de entrada que permita el tráfico en los puertos de la aplicación haciendo referencia al ID del security group del ALB como origen.",
                    "explanation": "Correcto: Los security groups pueden hacer referencia a otros security groups por ID. Esto garantiza que únicamente el tráfico que pasa por el security group del ALB sea aceptado por las instancias de EC2, independientemente de los cambios de IP."
                },
                {
                    "id": "C",
                    "text": "Configurar la Network ACL en la subred privada para permitir tráfico entrante desde los bloques CIDR de las subredes públicas en los puertos 80 y 443.",
                    "explanation": "Incorrecto: El filtrado por CIDR de subred en Network ACLs no restringe el tráfico exclusivamente al ALB, ya que cualquier recurso en la subred pública podría acceder a las instancias privadas."
                },
                {
                    "id": "D",
                    "text": "Configurar el security group de EC2 con una regla de entrada que permita 0.0.0.0/0 en los puertos 80 y 443 y configurar una regla de iptables en cada instancia de EC2.",
                    "explanation": "Incorrecto: Abrir hacia 0.0.0.0/0 infringe el principio de mínimo privilegio y gestionar iptables en instancias individuales incrementa la complejidad operativa."
                }
            ],
            "generalExplanation": "Hacer referencia al security group del ALB directamente en la regla de entrada del security group de las instancias privadas aplica un aislamiento de red estricto de mínimo privilegio y se adapta automáticamente a los cambios de IP del ALB."
        }
    },
    "saa-q004": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Um provedor de serviços de saúde precisa armazenar prontuários médicos de pacientes no Amazon S3 por um período de retenção obrigatório de 7 anos. Para cumprir as regulamentações federais, os objetos armazenados devem ser imutáveis e não podem ser sobrescritos, modificados ou excluídos por nenhum usuário, incluindo o usuário root da conta da AWS, durante a janela de retenção de 7 anos. Qual configuração garantirá a conformidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Aplicar uma política de bucket do S3 com uma declaração de negação explícita (Deny) para s3:DeleteObject e s3:DeleteObjectVersion abrangendo todos os principais do IAM.",
                    "explanation": "Incorreto: O usuário root da conta da AWS ou um administrador com privilégios do IAM pode modificar ou excluir a política do bucket para contornar a restrição."
                },
                {
                    "id": "B",
                    "text": "Habilitar o S3 Versioning no bucket e configurar o S3 Object Lock no Modo de Conformidade (Compliance Mode) com um período de retenção de 7 anos.",
                    "explanation": "Correto: O S3 Object Lock no Modo de Conformidade impõe um modelo WORM (Write Once, Read Many) rigoroso, no qual nenhum usuário, incluindo a conta root, pode excluir ou modificar objetos nem reduzir a retenção."
                },
                {
                    "id": "C",
                    "text": "Habilitar o S3 Versioning no bucket e configurar uma regra de ciclo de vida do S3 para fazer a transição dos objetos para o S3 Glacier Deep Archive após 1 dia.",
                    "explanation": "Incorreto: Transições de ciclo de vida para o Glacier não impedem que usuários com permissões apropriadas excluam versões de objetos."
                },
                {
                    "id": "D",
                    "text": "Habilitar o S3 Versioning e configurar o S3 Object Lock no Modo de Governança (Governance Mode) com um período de retenção padrão de 7 anos.",
                    "explanation": "Incorreto: O Modo de Governança permite que usuários com permissões específicas do IAM (s3:BypassGovernanceRetention) ou o usuário root alterem ou excluam objetos protegidos."
                }
            ],
            "generalExplanation": "O Amazon S3 Object Lock no Modo de Conformidade impede que uma versão de objeto seja excluída ou sobrescrita por qualquer usuário, incluindo o usuário root da sua conta da AWS, durante a vigência do período de retenção."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un proveedor de atención médica debe almacenar registros médicos de pacientes en Amazon S3 durante un período de retención obligatorio de 7 años. Para cumplir con las regulaciones federales, los objetos almacenados deben ser inmutables y ningún usuario, incluido el usuario root de la cuenta de AWS, puede sobrescribirlos, modificarlos ni eliminarlos durante el período de retención de 7 años. ¿Qué configuración garantizará el cumplimiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Aplicar una política de bucket de S3 con una declaración de denegación explícita (Deny) para s3:DeleteObject y s3:DeleteObjectVersion que cubra a todos los principales de IAM.",
                    "explanation": "Incorrecto: El usuario root de la cuenta de AWS o un administrador con privilegios de IAM puede modificar o eliminar la política del bucket para eludir la restricción."
                },
                {
                    "id": "B",
                    "text": "Habilitar S3 Versioning en el bucket y configurar S3 Object Lock en Modo de Cumplimiento (Compliance Mode) con un período de retención de 7 años.",
                    "explanation": "Correcto: S3 Object Lock en Modo de Cumplimiento aplica un modelo estricto WORM (Write Once, Read Many) en el que ningún usuario, incluida la cuenta root, puede eliminar o modificar objetos ni reducir la retención."
                },
                {
                    "id": "C",
                    "text": "Habilitar S3 Versioning en el bucket y configurar una regla de ciclo de vida de S3 para realizar la transición de los objetos a S3 Glacier Deep Archive después de 1 día.",
                    "explanation": "Incorrecto: Las transiciones de ciclo de vida a Glacier no impiden que los usuarios con permisos adecuados eliminen versiones de objetos."
                },
                {
                    "id": "D",
                    "text": "Habilitar S3 Versioning y configurar S3 Object Lock en Modo de Gobernanza (Governance Mode) con un período de retención predeterminado de 7 años.",
                    "explanation": "Incorrecto: El Modo de Gobernanza permite que los usuarios con permisos específicos de IAM (s3:BypassGovernanceRetention) o el usuario root alteren o eliminen objetos protegidos."
                }
            ],
            "generalExplanation": "Amazon S3 Object Lock en Modo de Cumplimiento impide que cualquier usuario, incluido el usuario root de su cuenta de AWS, elimine o sobrescriba una versión de objeto durante la vigencia del período de retención."
        }
    },
    "saa-q005": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Um site de comércio eletrônico global protegido pelo Amazon CloudFront está sofrendo ataques recorrentes de HTTP flood na camada de aplicação (Camada 7) e tentativas maliciosas de injeção de SQL a partir de intervalos de IP automatizados suspeitos. A equipe de segurança precisa de uma solução para inspecionar automaticamente as solicitações web recebidas, bloquear padrões conhecidos de injeção de SQL e aplicar rate limiting a clientes que enviarem mais de 2.000 solicitações por janela de 5 minutos. Qual solução o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar regras personalizadas de Network ACL nas sub-redes da VPC com regras explícitas de DENY para tráfego de HTTP flood.",
                    "explanation": "Incorreto: As Network ACLs operam na Camada 4 (IP/porta) e não podem inspecionar corpos de requisições HTTP para injeção de SQL nem rastrear taxas de requisição ao longo de janelas de tempo."
                },
                {
                    "id": "B",
                    "text": "Habilitar o AWS Shield Standard no bucket de origem do Amazon S3 e configurar políticas de bucket do S3 para rejeitar payloads HTTP malformados.",
                    "explanation": "Incorreto: O Shield Standard opera nas camadas 3/4 do modelo OSI e as políticas de bucket do S3 não conseguem analisar o conteúdo do payload HTTP nem aplicar limites de taxa."
                },
                {
                    "id": "C",
                    "text": "Configurar o Amazon GuardDuty com correção automatizada usando o AWS Lambda para banir endereços IP nos Security Groups.",
                    "explanation": "Incorreto: O GuardDuty é um serviço de detecção de anomalias investigativo, não um firewall de aplicação de Camada 7 inline com inspeção de solicitações em tempo real."
                },
                {
                    "id": "D",
                    "text": "Implantar o AWS WAF na distribuição do CloudFront com AWS Managed Rules para proteção de banco de dados SQL e uma regra personalizada baseada em taxa (rate-based rule).",
                    "explanation": "Correto: O AWS WAF integra-se diretamente ao CloudFront, fornecendo conjuntos de regras gerenciadas para injeção de SQL e regras baseadas em taxa que bloqueiam dinamicamente IPs que excedem limites de solicitações."
                }
            ],
            "generalExplanation": "O AWS WAF fornece inspeção de Camada 7 na borda quando conectado ao Amazon CloudFront, permitindo regras gerenciadas para prevenção de SQLi/XSS e regras baseadas em taxa para mitigar HTTP floods."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un sitio web minorista global respaldado por Amazon CloudFront está experimentando ataques recurrentes de inundación HTTP en la capa de aplicación (Capa 7) e intentos maliciosos de inyección SQL desde rangos de IP automatizados no autorizados. El equipo de seguridad necesita una solución para inspeccionar automáticamente las solicitudes web entrantes, bloquear patrones conocidos de inyección SQL y aplicar limitación de tasa (rate limiting) a los clientes que envíen más de 2.000 solicitudes por ventana de 5 minutos. ¿Qué solución debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear reglas personalizadas de Network ACL en las subredes de la VPC con reglas explícitas de DENY para el tráfico de inundación HTTP.",
                    "explanation": "Incorrecto: Las Network ACLs operan en la Capa 4 (IP/puerto) y no pueden inspeccionar cuerpos HTTP en busca de inyección SQL ni realizar seguimiento de tasas de solicitudes en ventanas de tiempo."
                },
                {
                    "id": "B",
                    "text": "Habilitar AWS Shield Standard en el bucket de origen de Amazon S3 y configurar políticas de bucket de S3 para rechazar cargas útiles HTTP malformadas.",
                    "explanation": "Incorrecto: Shield Standard opera en las capas OSI 3/4 y las políticas de bucket de S3 no pueden analizar el contenido de las cargas útiles HTTP ni aplicar límites de tasa."
                },
                {
                    "id": "C",
                    "text": "Configurar Amazon GuardDuty con corrección automatizada mediante AWS Lambda para bloquear direcciones IP en Security Groups.",
                    "explanation": "Incorrecto: GuardDuty es un servicio de detección de anomalías detectivesco, no un firewall de aplicaciones en línea de Capa 7 con inspección de solicitudes en tiempo real."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS WAF en la distribución de CloudFront con AWS Managed Rules para protección de bases de datos SQL y una regla personalizada basada en tasa (rate-based rule).",
                    "explanation": "Correcto: AWS WAF se integra directamente con CloudFront, ofreciendo conjuntos de reglas administradas para inyección SQL y reglas basadas en tasa que bloquean dinámicamente las IPs que superan los umbrales de solicitudes."
                }
            ],
            "generalExplanation": "AWS WAF proporciona inspección de Capa 7 en el borde cuando se asocia a Amazon CloudFront, habilitando reglas administradas para la prevención de SQLi/XSS y reglas basadas en tasa para mitigar inundaciones HTTP."
        }
    },
    "saa-q006": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma equipe de operações de segurança precisa de detecção contínua e inteligente de ameaças em toda a sua infraestrutura da AWS para identificar comportamentos não autorizados, como instâncias do EC2 comprometidas comunicando-se com servidores de comando e controle (C&C) conhecidos e atividades de mineração de criptomoedas. A solução deve analisar VPC Flow Logs, logs de consultas de DNS e eventos do CloudTrail sem exigir a instalação de agentes nas instâncias do EC2. Qual serviço satisfaz esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Amazon Macie para descobrir, classificar e proteger dados confidenciais (PII) armazenados em buckets do Amazon S3.",
                    "explanation": "Incorreto: O Amazon Macie descobre e classifica dados confidenciais (PII) armazenados no Amazon S3, em vez de monitorar o comportamento de rede do EC2."
                },
                {
                    "id": "B",
                    "text": "Habilitar o AWS CloudTrail Insights para identificar picos anômalos no volume de chamadas de API entre contas.",
                    "explanation": "Incorreto: O CloudTrail Insights detecta picos incomuns em chamadas de API de gravação, mas não analisa logs de consultas DNS ou VPC Flow Logs para comunicação de malware de criptomoedas."
                },
                {
                    "id": "C",
                    "text": "Habilitar o Amazon GuardDuty para analisar eventos do CloudTrail, VPC Flow Logs e logs de consultas de DNS com machine learning.",
                    "explanation": "Correto: O Amazon GuardDuty é um serviço de detecção de ameaças totalmente gerenciado que usa machine learning e inteligência integrada contra ameaças para analisar CloudTrail, VPC Flow Logs, logs de DNS e logs de auditoria do EKS sem a necessidade de agentes."
                },
                {
                    "id": "D",
                    "text": "Habilitar o Amazon Inspector para realizar varredura contínua e automatizada de vulnerabilidades e correspondência de CVEs de software em recursos do EC2 e ECR.",
                    "explanation": "Incorreto: O Amazon Inspector verifica vulnerabilidades de software e exposição indesejada de rede em recursos de computação, em vez de realizar detecção comportamental contínua de ameaças de C&C."
                }
            ],
            "generalExplanation": "O Amazon GuardDuty monitora continuamente contas e cargas de trabalho da AWS usando machine learning, detecção de anomalias e inteligência integrada contra ameaças sem a necessidade de implantar agentes."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un equipo de operaciones de seguridad requiere detección continua e inteligente de amenazas en toda su infraestructura de AWS para identificar comportamientos no autorizados, como instancias de EC2 comprometidas que se comunican con servidores conocidos de comando y control (C&C) y actividades de minería de criptomonedas. La solución debe analizar VPC Flow Logs, registros de consultas DNS y eventos de CloudTrail sin requerir la instalación de agentes en las instancias de EC2. ¿Qué servicio satisface estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar Amazon Macie para descubrir, clasificar y proteger datos confidenciales (PII) almacenados en buckets de Amazon S3.",
                    "explanation": "Incorrecto: Amazon Macie descubre y clasifica datos confidenciales (PII) almacenados en Amazon S3, en lugar de monitorear el comportamiento de red de EC2."
                },
                {
                    "id": "B",
                    "text": "Habilitar AWS CloudTrail Insights para identificar picos anómalos en el volumen de llamadas a la API entre cuentas.",
                    "explanation": "Incorrecto: CloudTrail Insights detecta picos inusuales en llamadas de escritura a la API, pero no analiza registros de consultas DNS ni registros de flujo de VPC para detectar malware de criptomonedas."
                },
                {
                    "id": "C",
                    "text": "Habilitar Amazon GuardDuty para analizar eventos de CloudTrail, VPC Flow Logs y registros de consultas DNS con machine learning.",
                    "explanation": "Correcto: Amazon GuardDuty es un servicio administrado de detección de amenazas que utiliza machine learning e inteligencia integrada sobre amenazas para analizar CloudTrail, VPC Flow Logs, registros DNS y registros de auditoría de EKS sin agentes."
                },
                {
                    "id": "D",
                    "text": "Habilitar Amazon Inspector para realizar análisis de vulnerabilidades continuos y automatizados y cotejo de CVEs de software en recursos de EC2 y ECR.",
                    "explanation": "Incorrecto: Amazon Inspector analiza vulnerabilidades de software y exposición de red no deseada en recursos de cómputo, en lugar de detección continua del comportamiento de amenazas de C&C."
                }
            ],
            "generalExplanation": "Amazon GuardDuty monitorea continuamente cuentas y cargas de trabajo de AWS mediante machine learning, detección de anomalías e inteligencia de amenazas integrada sin necesidad de implementar agentes."
        }
    },
    "saa-q007": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma aplicação executada em uma instância do Amazon EC2 precisa ler e gravar objetos em um bucket do Amazon S3. As diretrizes de segurança corporativa proíbem estritamente o armazenamento de access keys ou secret access keys de longo prazo da AWS em discos de instâncias ou em repositórios de código-fonte. Qual arquitetura oferece o mecanismo de autenticação mais seguro?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar uma IAM Role com uma política anexada que conceda as permissões necessárias no S3, anexar a role a um Perfil de Instância (Instance Profile) do EC2 e atribuí-lo à instância do EC2.",
                    "explanation": "Correto: As roles do IAM para o EC2 utilizam perfis de instância para fornecer credenciais de segurança temporárias e rotacionadas automaticamente por meio do serviço de metadados da instância (IMDS)."
                },
                {
                    "id": "B",
                    "text": "Criar um IAM User com permissões no S3, gerar um par de access keys e armazenar as chaves em um arquivo criptografado no volume EBS raiz do EC2.",
                    "explanation": "Incorreto: Armazenar chaves de acesso estáticas no volume da instância viola políticas de segurança e cria riscos de vazamento de credenciais."
                },
                {
                    "id": "C",
                    "text": "Configurar uma política de bucket do S3 com acesso público de leitura e gravação, mas restringir as ações ao endereço IP privado da instância do EC2.",
                    "explanation": "Incorreto: Os endpoints públicos do S3 não conseguem avaliar IPs privados RFC 1918 em políticas de bucket, e tornar o bucket público cria uma vulnerabilidade grave."
                },
                {
                    "id": "D",
                    "text": "Passar as credenciais da conta root da AWS para o script de user data do EC2 como variáveis de ambiente codificadas em base64 durante a inicialização.",
                    "explanation": "Incorreto: Utilizar credenciais root e expô-las em scripts de user data é um antipadrão de segurança grave."
                }
            ],
            "generalExplanation": "O uso de IAM Roles e perfis de instância permite que aplicações no Amazon EC2 obtenham de forma segura credenciais temporárias de curto prazo gerenciadas e rotacionadas automaticamente pela AWS."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una aplicación que se ejecuta en una instancia de Amazon EC2 necesita leer y escribir objetos en un bucket de Amazon S3. Las pautas de seguridad corporativa prohíben estrictamente almacenar access keys o secret access keys de AWS a largo plazo en discos de instancias o en repositorios de código fuente. ¿Qué arquitectura proporciona el mecanismo de autenticación más seguro?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear un rol de IAM con una política asociada que otorgue los permisos requeridos en S3, adjuntar el rol a un perfil de instancia (Instance Profile) de EC2 y asignarlo a la instancia de EC2.",
                    "explanation": "Correcto: Los roles de IAM para EC2 aprovechan los perfiles de instancia para entregar credenciales de seguridad temporales y rotadas automáticamente a través del servicio de metadatos de la instancia (IMDS)."
                },
                {
                    "id": "B",
                    "text": "Crear un usuario de IAM con permisos en S3, generar un par de claves de acceso y almacenar las claves en un archivo cifrado en el volumen EBS raíz de EC2.",
                    "explanation": "Incorrecto: Almacenar claves de acceso estáticas en el volumen de la instancia infringe las políticas de seguridad y crea riesgos de fuga de credenciales."
                },
                {
                    "id": "C",
                    "text": "Configurar una política de bucket de S3 con acceso público de lectura y escritura, pero restringir las acciones a la dirección IP privada de la instancia de EC2.",
                    "explanation": "Incorrecto: Los puntos de enlace públicos de S3 no pueden evaluar IPs privadas RFC 1918 en políticas de bucket, y hacer que el bucket sea público crea una vulnerabilidad crítica."
                },
                {
                    "id": "D",
                    "text": "Pasar las credenciales de la cuenta root de AWS en el script de user data de EC2 como variables de entorno codificadas en base64 durante el lanzamiento inicial.",
                    "explanation": "Incorrecto: Usar credenciales root y exponerlas en scripts de user data es un antipatrón de seguridad extremadamente riesgoso."
                }
            ],
            "generalExplanation": "El uso de roles de IAM y perfiles de instancia permite que las aplicaciones en Amazon EC2 obtengan de forma segura credenciales temporales de corto plazo administradas y rotadas automáticamente por AWS."
        }
    },
    "saa-q008": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma empresa de auditoria financeira deve armazenar documentos fiscais confidenciais de clientes no Amazon S3. A empresa exige gerenciamento de chaves de criptografia controlado pelo cliente, rotação automática anual obrigatória de chaves e auditabilidade total de cada solicitação de API de criptografia e descriptografia nos logs do AWS CloudTrail. Qual método de criptografia do S3 atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Criptografia no lado do servidor com chaves gerenciadas pelo cliente do AWS KMS (SSE-KMS)",
                    "explanation": "Correto: As Customer Managed Keys (CMKs) no AWS KMS oferecem suporte à rotação automática anual de chaves, políticas de chaves personalizadas e registram todas as chamadas de API Decrypt/GenerateDataKey no CloudTrail."
                },
                {
                    "id": "B",
                    "text": "Criptografia no lado do servidor com chaves fornecidas pelo cliente (SSE-C)",
                    "explanation": "Incorreto: O SSE-C exige que o cliente armazene, rotacione e envie a chave a cada solicitação, sem rotação nativa de chaves do KMS nem trilhas de auditoria do KMS no CloudTrail."
                },
                {
                    "id": "C",
                    "text": "Criptografia no lado do servidor com chaves gerenciadas pelo Amazon S3 (SSE-S3)",
                    "explanation": "Incorreto: O SSE-S3 usa chaves gerenciadas inteiramente pelo S3 e não registra chamadas individuais de descriptografia no CloudTrail sob controle do cliente."
                },
                {
                    "id": "D",
                    "text": "Criptografia no lado do cliente usando uma única chave simétrica AES-256 embutida no código da aplicação",
                    "explanation": "Incorreto: Embutir chaves estáticas no código da aplicação não possui recursos de rotação de chave nem auditoria no KMS via CloudTrail."
                }
            ],
            "generalExplanation": "As Customer Managed Keys do AWS KMS (SSE-KMS) fornecem controle de acesso granular, rotação automática anual opcional e auditoria detalhada no CloudTrail de todos os eventos de uso de chaves."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una firma de auditoría financiera debe almacenar documentos tributarios confidenciales de clientes en Amazon S3. La empresa requiere administración de claves de cifrado controlada por el cliente, rotación automática anual obligatoria de claves y auditabilidad completa de cada solicitud de API de cifrado y descifrado en los registros de AWS CloudTrail. ¿Qué método de cifrado de S3 cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Cifrado del lado del servidor con claves administradas por el cliente de AWS KMS (SSE-KMS)",
                    "explanation": "Correcto: Las Customer Managed Keys (CMKs) en AWS KMS admiten rotación automática anual de claves, políticas de claves personalizadas y registran todas las llamadas a la API Decrypt/GenerateDataKey en CloudTrail."
                },
                {
                    "id": "B",
                    "text": "Cifrado del lado del servidor con claves proporcionadas por el cliente (SSE-C)",
                    "explanation": "Incorrecto: SSE-C requiere que el cliente almacene, rote y envíe la clave con cada solicitud, sin rotación nativa de claves de KMS ni registros de auditoría de KMS en CloudTrail."
                },
                {
                    "id": "C",
                    "text": "Cifrado del lado del servidor con claves administradas por Amazon S3 (SSE-S3)",
                    "explanation": "Incorrecto: SSE-S3 utiliza claves administradas completamente por S3 y no registra llamadas individuales de descifrado en CloudTrail bajo control del cliente."
                },
                {
                    "id": "D",
                    "text": "Cifrado del lado del cliente mediante una única clave simétrica AES-256 integrada en el código de la aplicación",
                    "explanation": "Incorrecto: Integrar claves estáticas en el código de la aplicación carece de rotación de claves y de capacidades de auditoría en KMS con CloudTrail."
                }
            ],
            "generalExplanation": "Las Customer Managed Keys de AWS KMS (SSE-KMS) brindan control de acceso granular, rotación automática anual opcional y auditoría detallada en CloudTrail de todos los eventos de uso de claves."
        }
    },
    "saa-q009": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Um provedor de SaaS hospeda uma API em instâncias do Amazon EC2 atrás de um Network Load Balancer (NLB) na VPC A. Vários clientes corporativos em contas distintas da AWS precisam acessar essa API de forma privada a partir de suas próprias VPCs sem trafegar pela internet pública, sem estabelecer conexões complexas de VPC peering e sem risco de sobreposição de blocos CIDR de endereços IP. Qual solução o arquiteto de SaaS deve configurar?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar um VPC Endpoint Service (AWS PrivateLink) sustentado pelo Network Load Balancer na VPC A e fazer com que os clientes criem Interface Endpoints em suas respectivas VPCs.",
                    "explanation": "Correto: O AWS PrivateLink permite comunicação privada e segura entre VPCs em diferentes contas, mesmo com CIDRs sobrepostos, sem expor os endpoints à internet."
                },
                {
                    "id": "B",
                    "text": "Criar um AWS Transit Gateway, anexar todas as VPCs dos clientes e a VPC A ao Transit Gateway e configurar tabelas de rotas estáticas.",
                    "explanation": "Incorreto: O Transit Gateway exige blocos CIDR não sobrepostos e coordenação total de roteamento entre todas as contas."
                },
                {
                    "id": "C",
                    "text": "Estabelecer conexões de VPC Peering entre contas entre a VPC A e a VPC de cada cliente e atualizar as tabelas de rotas adequadamente.",
                    "explanation": "Incorreto: O VPC Peering falha se as VPCs dos clientes tiverem intervalos CIDR que se sobreponham à VPC A."
                },
                {
                    "id": "D",
                    "text": "Configurar um Internet Gateway na VPC A e usar conexões AWS Site-to-Site VPN sobre endereços IP públicos para cada cliente.",
                    "explanation": "Incorreto: A VPN Site-to-Site introduz sobrecarga de criptografia, requer túneis IPsec e não oferece integração nativa com endpoints sem servidor como o PrivateLink."
                }
            ],
            "generalExplanation": "O AWS PrivateLink (VPC Endpoint Services) permite que provedores de serviços publiquem com segurança serviços privados para VPCs consumidoras por meio de Elastic Network Interfaces (ENIs), superando nativamente a sobreposição de CIDRs."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un proveedor de SaaS aloja una API en instancias de Amazon EC2 detrás de un Network Load Balancer (NLB) en la VPC A. Varios clientes empresariales en cuentas separadas de AWS necesitan acceder a esta API de forma privada desde sus propias VPCs sin pasar por la internet pública, sin establecer conexiones complejas de VPC peering y sin riesgo de superposición de rangos CIDR de direcciones IP. ¿Qué solución debe configurar el arquitecto de SaaS?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear un VPC Endpoint Service (AWS PrivateLink) respaldado por el Network Load Balancer en la VPC A y hacer que los clientes creen Interface Endpoints en sus respectivas VPCs.",
                    "explanation": "Correcto: AWS PrivateLink permite la comunicación privada y segura entre VPCs a través de diferentes cuentas incluso con CIDRs superpuestos, sin exponer puntos de enlace a internet."
                },
                {
                    "id": "B",
                    "text": "Crear un AWS Transit Gateway, conectar todas las VPCs de clientes y la VPC A al Transit Gateway y configurar tablas de rutas estáticas.",
                    "explanation": "Incorrecto: Transit Gateway requiere bloques CIDR que no se superpongan y una coordinación completa de enrutamiento entre todas las cuentas."
                },
                {
                    "id": "C",
                    "text": "Establecer conexiones de VPC Peering entre cuentas entre la VPC A y la VPC de cada cliente y actualizar las tablas de rutas en consecuencia.",
                    "explanation": "Incorrecto: VPC Peering no funciona si las VPCs de los clientes tienen rangos CIDR superpuestos con la VPC A."
                },
                {
                    "id": "D",
                    "text": "Configurar un Internet Gateway en la VPC A y utilizar conexiones AWS Site-to-Site VPN sobre direcciones IP públicas para cada cliente.",
                    "explanation": "Incorrecto: Site-to-Site VPN introduce sobrecarga de cifrado, requiere túneles IPsec y no proporciona una integración nativa de puntos de enlace sin servidor como PrivateLink."
                }
            ],
            "generalExplanation": "AWS PrivateLink (VPC Endpoint Services) permite a los proveedores de servicios publicar de forma segura servicios privados en las VPCs consumidoras a través de Elastic Network Interfaces (ENIs), superando de forma nativa la superposición de CIDRs."
        }
    },
    "saa-q010": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma corporação jurídica armazena centenas de milhares de contratos em PDF e documentos de texto em buckets do Amazon S3 em vários departamentos. O responsável por conformidade deve descobrir, classificar e gerar alertas sempre que Informações de Identificação Pessoal (PII), como CPFs, números de cartão de crédito ou números de passaporte, forem armazenadas sem criptografia no S3. Qual serviço da AWS foi desenvolvido especificamente para essa tarefa?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Amazon Inspector para realizar varredura automatizada e contínua de vulnerabilidades e correspondência de CVEs de software em recursos do EC2 e ECR.",
                    "explanation": "Incorreto: O Amazon Inspector verifica recursos de computação e imagens de contêiner em busca de CVEs de software, não o conteúdo dos dados dentro do S3."
                },
                {
                    "id": "B",
                    "text": "Configurar e implantar o AWS CloudTrail de acordo com as melhores práticas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O CloudTrail registra chamadas de API, não o texto do payload ou o conteúdo interno dos arquivos enviados."
                },
                {
                    "id": "C",
                    "text": "Habilitar o Amazon Macie para descobrir, classificar e proteger dados confidenciais (PII) armazenados em buckets do Amazon S3.",
                    "explanation": "Correto: O Amazon Macie utiliza machine learning e correspondência de padrões para descobrir, classificar e alertar automaticamente sobre dados confidenciais e PII armazenados no Amazon S3."
                },
                {
                    "id": "D",
                    "text": "Habilitar o Amazon GuardDuty para analisar eventos do CloudTrail, VPC Flow Logs e logs de consultas de DNS com machine learning.",
                    "explanation": "Incorreto: O GuardDuty monitora anomalias de comportamento de rede e conta, mas não inspeciona texto de documentos dentro de objetos do S3 em busca de padrões de PII."
                }
            ],
            "generalExplanation": "O Amazon Macie é um serviço totalmente gerenciado de segurança e privacidade de dados que analisa buckets do S3 para identificar e proteger dados confidenciais, como PII e registros financeiros."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una corporación jurídica almacena cientos de miles de contratos en PDF y documentos de texto en buckets de Amazon S3 en varios departamentos. El oficial de cumplimiento debe descubrir, clasificar y generar alertas cada vez que se almacene Información de Identificación Personal (PII), como números de Seguro Social, números de tarjetas de crédito o pasaportes, sin cifrar en S3. ¿Qué servicio de AWS está diseñado específicamente para esta tarea?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar Amazon Inspector para realizar análisis continuos y automatizados de vulnerabilidades y cotejo de CVEs de software en recursos de EC2 y ECR.",
                    "explanation": "Incorrecto: Amazon Inspector analiza recursos de cómputo e imágenes de contenedores en busca de CVEs de software, no el contenido de los datos dentro de S3."
                },
                {
                    "id": "B",
                    "text": "Configurar e implementar AWS CloudTrail de acuerdo con las mejores prácticas de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: CloudTrail registra llamadas a la API, no el texto de la carga útil ni el contenido interno de los archivos cargados."
                },
                {
                    "id": "C",
                    "text": "Habilitar Amazon Macie para descubrir, clasificar y proteger datos confidenciales (PII) almacenados en buckets de Amazon S3.",
                    "explanation": "Correcto: Amazon Macie utiliza machine learning y coincidencia de patrones para descubrir, clasificar y alertar automáticamente sobre datos confidenciales y PII almacenados en Amazon S3."
                },
                {
                    "id": "D",
                    "text": "Habilitar Amazon GuardDuty para analizar eventos de CloudTrail, VPC Flow Logs y registros de consultas DNS con machine learning.",
                    "explanation": "Incorrecto: GuardDuty supervisa anomalías en el comportamiento de redes y cuentas, pero no inspecciona el texto de los documentos dentro de los objetos de S3 en busca de patrones de PII."
                }
            ],
            "generalExplanation": "Amazon Macie es un servicio totalmente administrado de seguridad y privacidad de datos que escanea buckets de S3 para identificar y proteger datos confidenciales, como PII y registros financieros."
        }
    },
    "saa-q011": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Um aplicativo móvel permite que usuários registrados enviem fotos de perfil para um bucket do Amazon S3. A política de segurança determina que os uploads devem ocorrer diretamente dos dispositivos móveis dos clientes para o S3 via HTTPS, sem rotear cargas massivas de arquivos binários por meio dos servidores de API de backend, garantindo que cada usuário só possa fazer upload de arquivos para sua pasta designada por uma janela máxima de 15 minutos. Qual solução o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um Application Load Balancer com uma frota de instâncias EC2 para receber as imagens, salvá-las em volumes EBS locais e executar um script cron para copiá-las para o S3.",
                    "explanation": "Incorreto: Isso encaminha cargas pesadas através de servidores, aumentando os custos de infraestrutura e violando o requisito de uploads diretos do cliente para o S3."
                },
                {
                    "id": "B",
                    "text": "Gerar URLs pré-assinadas (pre-signed URLs) do Amazon S3 com expiração de 15 minutos por meio de uma função Lambda de backend autenticada para cada solicitação de upload.",
                    "explanation": "Correto: As URLs pré-assinadas do S3 concedem acesso de upload direto com limite de tempo a chaves de objeto específicas sem compartilhar credenciais da AWS ou rotear arquivos por meio de servidores de aplicação."
                },
                {
                    "id": "C",
                    "text": "Configurar o bucket do S3 como um endpoint público de upload e usar notificações de eventos do S3 para excluir arquivos enviados após 15 minutos.",
                    "explanation": "Incorreto: Tornar o bucket público permite que qualquer pessoa faça upload de dados arbitrários e não protege os limites de isolamento dos usuários."
                },
                {
                    "id": "D",
                    "text": "Criar um usuário do IAM para cada usuário do aplicativo móvel e embutir credenciais temporárias com expiração de 15 minutos dentro do pacote do aplicativo móvel.",
                    "explanation": "Incorreto: Criar usuários individuais do IAM para usuários externos de dispositivos móveis é um antipadrão que viola escalabilidade e segurança de credenciais."
                }
            ],
            "generalExplanation": "As URLs pré-assinadas do S3 fornecem acesso temporário e seguro para que clientes façam upload ou download de objetos diretamente de/para o S3 sem a necessidade de credenciais permanentes da AWS."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una aplicación móvil permite a los usuarios registrados subir fotos de perfil personales a un bucket de Amazon S3. La política de seguridad exige que las cargas se realicen directamente desde los dispositivos móviles de los clientes hacia S3 a través de HTTPS, sin enrutar cargas masivas de archivos binarios a través de servidores API de backend, garantizando que cada usuario solo pueda subir archivos a su carpeta designada durante una ventana máxima de 15 minutos. ¿Qué solución debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un Application Load Balancer con una flota de EC2 para recibir las imágenes, guardarlas en volúmenes EBS locales y ejecutar un script cron para copiarlas en S3.",
                    "explanation": "Incorrecto: Esto enruta cargas pesadas a través de servidores, aumentando el costo de infraestructura y violando el requisito de subidas directas del cliente a S3."
                },
                {
                    "id": "B",
                    "text": "Generar URLs prefirmadas (pre-signed URLs) de Amazon S3 con una expiración de 15 minutos a través de una función Lambda de backend autenticada para cada solicitud de carga.",
                    "explanation": "Correcto: Las URLs prefirmadas de S3 otorgan acceso de carga directo y limitado en el tiempo a claves de objetos específicas sin compartir credenciales de AWS ni enrutar archivos a través de servidores de aplicaciones."
                },
                {
                    "id": "C",
                    "text": "Configurar el bucket de S3 como un punto de enlace de carga público y usar notificaciones de eventos de S3 para eliminar archivos subidos después de 15 minutos.",
                    "explanation": "Incorrecto: Hacer que el bucket sea público permite que cualquiera cargue datos arbitrarios y no protege los límites entre usuarios."
                },
                {
                    "id": "D",
                    "text": "Crear un usuario de IAM para cada usuario de la aplicación móvil e incrustar credenciales temporales con expiración de 15 minutos dentro del paquete de la aplicación móvil.",
                    "explanation": "Incorrecto: Crear usuarios de IAM individuales para usuarios móviles externos es un antipatrón que infringe la escala y la seguridad de las credenciales."
                }
            ],
            "generalExplanation": "Las URLs prefirmadas de S3 proporcionan acceso temporal y seguro para que los clientes suban o descarguen objetos directamente hacia/desde S3 sin credenciales directas de AWS."
        }
    },
    "saa-q012": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma empresa está lançando um site público HTTPS usando o Amazon CloudFront e um Application Load Balancer (ALB). O arquiteto de soluções precisa provisionar e associar certificados SSL/TLS para o nome de domínio personalizado 'example.com' com renovação automática e custo zero de licenciamento de certificado. Onde os certificados SSL/TLS devem ser provisionados no AWS Certificate Manager (ACM)?",
            "options": [
                {
                    "id": "A",
                    "text": "Solicitar um único certificado na região do ALB e importar sua chave privada manualmente para o CloudFront.",
                    "explanation": "Incorreto: Chaves privadas de certificados públicos gerenciados pelo ACM não podem ser exportadas nem importadas manualmente, e o CloudFront exige estritamente certificados em us-east-1."
                },
                {
                    "id": "B",
                    "text": "Solicitar um certificado público na região us-east-1 (Norte da Virgínia) para o CloudFront e solicitar outro certificado na região de destino do ALB para o ALB.",
                    "explanation": "Correto: As distribuições do CloudFront exigem certificados solicitados especificamente em us-east-1, enquanto recursos regionais como ALBs exigem certificados na mesma região da AWS em que residem."
                },
                {
                    "id": "C",
                    "text": "Comprar um certificado de uma autoridade certificadora (CA) de terceiros e armazená-lo em um bucket do Amazon S3 acessível por ambos os serviços.",
                    "explanation": "Incorreto: Armazenar certificados no S3 não se integra com o encerramento de SSL no ALB/CloudFront e envolve custos desnecessários de licenciamento de terceiros."
                },
                {
                    "id": "D",
                    "text": "Solicitar um único certificado em qualquer região da AWS e habilitar o compartilhamento global multirregional de certificados no ACM.",
                    "explanation": "Incorreto: Os certificados do ACM são regionais e não podem ser compartilhados automaticamente entre regiões sem solicitá-los na região de destino."
                }
            ],
            "generalExplanation": "O AWS Certificate Manager fornece certificados SSL/TLS públicos gratuitos com renovação automática. O CloudFront requer certificados em us-east-1, enquanto os ALBs requerem certificados em sua região local correspondente."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una empresa va a lanzar un sitio web HTTPS público utilizando Amazon CloudFront y un Application Load Balancer (ALB). El arquitecto de soluciones necesita aprovisionar y asociar certificados SSL/TLS para el nombre de dominio personalizado 'example.com' con renovación automática y cero costos de licencia de certificados. ¿Dónde se deben aprovisionar los certificados SSL/TLS en AWS Certificate Manager (ACM)?",
            "options": [
                {
                    "id": "A",
                    "text": "Solicitar un único certificado en la región del ALB e importar su clave privada manualmente en CloudFront.",
                    "explanation": "Incorrecto: Las claves privadas de los certificados públicos administrados por ACM no se pueden exportar ni importar manualmente, y CloudFront requiere estrictamente certificados en us-east-1."
                },
                {
                    "id": "B",
                    "text": "Solicitar un certificado público en la región us-east-1 (Norte de Virginia) para CloudFront y solicitar otro certificado en la región de destino del ALB para el ALB.",
                    "explanation": "Correcto: Las distribuciones de CloudFront requieren certificados solicitados específicamente en us-east-1, mientras que los recursos regionales como los ALBs requieren certificados en su misma región de AWS."
                },
                {
                    "id": "C",
                    "text": "Comprar un certificado de una autoridad de certificación (CA) externa y almacenarlo en un bucket de Amazon S3 accesible por ambos servicios.",
                    "explanation": "Incorrecto: Almacenar certificados en S3 no se integra con la terminación SSL de ALB/CloudFront e incurre en costos de licencia innecesarios de terceros."
                },
                {
                    "id": "D",
                    "text": "Solicitar un único certificado en cualquier región de AWS y habilitar el uso compartido global multirregión de certificados en ACM.",
                    "explanation": "Incorrecto: Los certificados de ACM son regionales y no se pueden compartir automáticamente entre regiones sin solicitarlos en la región de destino."
                }
            ],
            "generalExplanation": "AWS Certificate Manager proporciona certificados SSL/TLS públicos gratuitos con renovación automática. CloudFront requiere certificados en us-east-1, mientras que los ALBs requieren certificados en su región local."
        }
    },
    "saa-q013": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma corporação gerencia 50 contas da AWS dentro do AWS Organizations. A equipe central de segurança exige que nenhum administrador de conta-membro, incluindo o usuário root da conta-membro, possa excluir trilhas do Amazon CloudTrail ou interromper o registro de logs em qualquer região. Qual solução impõe esse controle preventivo em toda a organização?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar regras do AWS Config em cada conta para detectar quando o CloudTrail for desativado e acionar um runbook do AWS Systems Manager Automation.",
                    "explanation": "Incorreto: O AWS Config é um controle investigativo e reativo após a exclusão ocorrer, não uma barreira preventiva."
                },
                {
                    "id": "B",
                    "text": "Criar uma política do IAM no bucket do CloudTrail concedendo acesso somente leitura a todos os usuários.",
                    "explanation": "Incorreto: Políticas de bucket protegem objetos do S3, mas não impedem a interrupção ou exclusão da trilha no próprio serviço CloudTrail."
                },
                {
                    "id": "C",
                    "text": "Criar uma Service Control Policy (SCP) na conta de gerenciamento do Organizations com uma negação explícita (Deny) para cloudtrail:DeleteTrail e cloudtrail:StopLogging e anexá-la à Unidade Organizacional Raiz (Root OU).",
                    "explanation": "Correto: As SCPs estabelecem limites preventivos no nível do AWS Organizations que se aplicam a todos os principais nas contas-membro, incluindo o usuário root da conta-membro."
                },
                {
                    "id": "D",
                    "text": "Criar um IAM Permission Boundary em cada conta-membro que restrinja as ações cloudtrail:DeleteTrail e cloudtrail:StopLogging.",
                    "explanation": "Incorreto: Os limites de permissão (Permission Boundaries) não se aplicam ao usuário root das contas-membro e exigem manutenção descentralizada por role."
                }
            ],
            "generalExplanation": "As Service Control Policies (SCPs) no AWS Organizations impõem limites e controles preventivos em toda a organização que se sobrepõem a todas as políticas do IAM das contas-membro, incluindo o usuário root."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una corporación administra 50 cuentas de AWS dentro de AWS Organizations. El equipo central de seguridad exige que ningún administrador de cuenta miembro, incluido el usuario root de la cuenta miembro, pueda eliminar rutas de Amazon CloudTrail ni detener el registro de logs en ninguna región. ¿Qué solución aplica este control preventivo en toda la organización?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar reglas de AWS Config en cada cuenta para detectar cuándo se deshabilita CloudTrail y activar un runbook de AWS Systems Manager Automation.",
                    "explanation": "Incorrecto: AWS Config es un control detectivesco y reactivo posterior a que ocurra la eliminación, no una barrera preventiva."
                },
                {
                    "id": "B",
                    "text": "Crear una política de IAM en el bucket de CloudTrail que otorgue acceso de solo lectura a todos los usuarios.",
                    "explanation": "Incorrecto: Las políticas de bucket protegen los objetos de S3, pero no impiden detener o eliminar la ruta de CloudTrail en el propio servicio CloudTrail."
                },
                {
                    "id": "C",
                    "text": "Crear una Service Control Policy (SCP) en la cuenta de administración de Organizations con una denegación explícita (Deny) para cloudtrail:DeleteTrail y cloudtrail:StopLogging, y adjuntarla a la Unidad Organizativa Raíz (Root OU).",
                    "explanation": "Correcto: Las SCP establecen barreras preventivas a nivel de AWS Organizations que se aplican a todos los principales en las cuentas miembro, incluido el usuario root de la cuenta miembro."
                },
                {
                    "id": "D",
                    "text": "Crear un límite de permisos de IAM (Permission Boundary) en cada cuenta miembro que restrinja las acciones cloudtrail:DeleteTrail y cloudtrail:StopLogging.",
                    "explanation": "Incorrecto: Los límites de permisos no se aplican al usuario root de las cuentas miembro y requieren mantenimiento descentralizado por rol."
                }
            ],
            "generalExplanation": "Las Service Control Policies (SCPs) en AWS Organizations aplican límites y controles preventivos en toda la organización que invalidan todas las políticas de IAM de las cuentas miembro, incluido el usuario root."
        }
    },
    "saa-q014": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma startup está desenvolvendo uma aplicação web voltada para clientes finais. Os usuários precisam se cadastrar, fazer login com e-mail/senha ou provedores de identidade social (Google, Apple) e receber credenciais temporárias da AWS com escopo limitado para fazer upload de recursos de perfil diretamente para o Amazon S3. Qual combinação de serviços o arquiteto deve recomendar?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Cognito User Pools para autenticação e Amazon Cognito Identity Pools (Federated Identities) para autorização e credenciais temporárias da AWS.",
                    "explanation": "Correto: Os Cognito User Pools gerenciam o diretório de usuários, autenticação e login social de IdP. Os Cognito Identity Pools trocam tokens por credenciais temporárias do AWS IAM para acessar recursos da AWS como o S3."
                },
                {
                    "id": "B",
                    "text": "AWS IAM Identity Center com federação SAML e criação direta de usuários do IAM para cada cliente.",
                    "explanation": "Incorreto: O IAM Identity Center foi projetado para identidade de força de trabalho corporativa, não para milhões de clientes externos B2C."
                },
                {
                    "id": "C",
                    "text": "AWS Directory Service para Microsoft Active Directory conectado diretamente às políticas de bucket do Amazon S3.",
                    "explanation": "Incorreto: O Active Directory é um diretório corporativo inadequado para autenticação social de consumidores em plataformas web e móveis."
                },
                {
                    "id": "D",
                    "text": "AWS Secrets Manager para armazenar todas as senhas dos usuários e uma frota de proxy EC2 para validar senhas a cada solicitação ao S3.",
                    "explanation": "Incorreto: O Secrets Manager foi projetado para credenciais de banco de dados e APIs, não para pools de usuários de consumidores em grande escala."
                }
            ],
            "generalExplanation": "Os Amazon Cognito User Pools fornecem recursos de cadastro e login, enquanto os Cognito Identity Pools concedem aos usuários autorizados credenciais temporárias de menor privilégio da AWS para acessar serviços como o S3."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una startup está creando una aplicación web orientada al cliente. Los usuarios deben registrarse, iniciar sesión con correo electrónico/contraseña o proveedores de identidades sociales (Google, Apple) y recibir credenciales temporales de AWS con alcance limitado para subir recursos de perfil directamente a Amazon S3. ¿Qué combinación de servicios debería recomendar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Cognito User Pools para autenticación y Amazon Cognito Identity Pools (Federated Identities) para autorización y credenciales temporales de AWS.",
                    "explanation": "Correcto: Cognito User Pools administra el directorio de usuarios, la autenticación y el inicio de sesión con IdP social. Cognito Identity Pools intercambia tokens por credenciales temporales de AWS IAM para acceder a recursos de AWS como S3."
                },
                {
                    "id": "B",
                    "text": "AWS IAM Identity Center con federación SAML y creación directa de usuarios de IAM para cada cliente.",
                    "explanation": "Incorrecto: IAM Identity Center está diseñado para la identidad del personal corporativo, no para millones de clientes B2C externos."
                },
                {
                    "id": "C",
                    "text": "AWS Directory Service para Microsoft Active Directory conectado directamente a las políticas de bucket de Amazon S3.",
                    "explanation": "Incorrecto: Active Directory es un directorio empresarial no apto para la autenticación social en aplicaciones móviles y web de consumidores."
                },
                {
                    "id": "D",
                    "text": "AWS Secrets Manager para almacenar todas las contraseñas de los usuarios y una flota proxy de EC2 para validar contraseñas en cada solicitud a S3.",
                    "explanation": "Incorrecto: Secrets Manager está diseñado para credenciales de bases de datos/APIs, no para directorios escalables de usuarios consumidores."
                }
            ],
            "generalExplanation": "Amazon Cognito User Pools proporciona funciones de registro e inicio de sesión, mientras que Cognito Identity Pools otorga a los usuarios autorizados credenciales de AWS temporales y de mínimo privilegio para acceder a servicios como S3."
        }
    },
    "saa-q015": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma equipe de DevOps desenvolve e implanta microsserviços em contêineres no Amazon ECR e executa cargas de trabalho em instâncias do Amazon EC2. A equipe de conformidade de segurança exige a verificação automatizada de imagens de contêiner enviadas para o Amazon ECR e de pacotes do sistema operacional em instâncias do EC2 para detectar vulnerabilidades e exposições comuns (CVEs) de forma contínua. Qual serviço da AWS oferece essa funcionalidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Amazon Macie para descobrir, classificar e proteger dados confidenciais (PII) armazenados em buckets do Amazon S3.",
                    "explanation": "Incorreto: O Amazon Macie analisa buckets do S3 em busca de dados confidenciais (PII), não vulnerabilidades de sistema operacional ou contêineres."
                },
                {
                    "id": "B",
                    "text": "Configurar e implantar o AWS Systems Manager Run Command de acordo com as melhores práticas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O Run Command permite a execução remota de comandos, mas não fornece inteligência automatizada de vulnerabilidades e correspondência de CVEs de forma nativa."
                },
                {
                    "id": "C",
                    "text": "Habilitar o Amazon Inspector para realizar varredura contínua e automatizada de vulnerabilidades e correspondência de CVEs de software em recursos do EC2 e ECR.",
                    "explanation": "Correto: O Amazon Inspector fornece gerenciamento de vulnerabilidades contínuo e automatizado e verificação de CVEs para instâncias do Amazon EC2, imagens de contêiner no Amazon ECR e funções do AWS Lambda."
                },
                {
                    "id": "D",
                    "text": "Assinar o AWS Shield Advanced para mitigação dedicada de DDoS e suporte 24 horas por dia, 7 dias por semana da Equipe de Resposta a DDoS.",
                    "explanation": "Incorreto: O AWS Shield Advanced é um serviço de mitigação de DDoS e não analisa pacotes de software em busca de CVEs."
                }
            ],
            "generalExplanation": "O Amazon Inspector descobre cargas de trabalho automaticamente e analisa instâncias do EC2, imagens de contêiner do ECR e funções do Lambda em busca de vulnerabilidades de software e exposição indesejada de rede."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un equipo de DevOps crea e implementa microservicios en contenedores en Amazon ECR y ejecuta cargas de trabajo en instancias de Amazon EC2. El equipo de cumplimiento de seguridad requiere el análisis automatizado de imágenes de contenedores enviadas a Amazon ECR y paquetes del sistema operativo en instancias de EC2 para detectar vulnerabilidades y exposiciones comunes (CVEs) de forma continua. ¿Qué servicio de AWS proporciona esta funcionalidad?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar Amazon Macie para descubrir, clasificar y proteger datos confidenciales (PII) almacenados en buckets de Amazon S3.",
                    "explanation": "Incorrecto: Amazon Macie escanea buckets de S3 en busca de datos confidenciales (PII), no vulnerabilidades del SO ni de contenedores."
                },
                {
                    "id": "B",
                    "text": "Configurar e implementar AWS Systems Manager Run Command de acuerdo con las mejores prácticas de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Run Command permite la ejecución remota de comandos, pero no proporciona inteligencia automatizada de vulnerabilidades ni cotejo de CVEs de fábrica."
                },
                {
                    "id": "C",
                    "text": "Habilitar Amazon Inspector para realizar análisis de vulnerabilidades continuos y automatizados y cotejo de CVEs de software en recursos de EC2 y ECR.",
                    "explanation": "Correcto: Amazon Inspector proporciona administración automatizada y continua de vulnerabilidades y análisis de CVEs para instancias de Amazon EC2, imágenes de contenedores en Amazon ECR y funciones de AWS Lambda."
                },
                {
                    "id": "D",
                    "text": "Suscribirse a AWS Shield Advanced para mitigación dedicada de DDoS y soporte 24/7 del Equipo de Respuesta ante DDoS.",
                    "explanation": "Incorrecto: AWS Shield Advanced es un servicio de mitigación de DDoS y no analiza paquetes de software en busca de CVEs."
                }
            ],
            "generalExplanation": "Amazon Inspector descubre automáticamente cargas de trabajo y analiza instancias de EC2, imágenes de contenedores de ECR y funciones de Lambda en busca de vulnerabilidades de software y exposición de red no intencionada."
        }
    },
    "saa-q016": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma frota de instâncias do Amazon EC2 em sub-redes privadas sem acesso à internet precisa baixar patches de software e conjuntos de dados de um bucket do Amazon S3 na mesma região da AWS. O arquiteto de rede deve garantir que o tráfego entre as instâncias do EC2 e o bucket do S3 trafegue inteiramente pela rede privada da AWS, sem exigir um NAT Gateway, Internet Gateway ou cobranças recorrentes por hora de endpoint. Qual solução deve ser implementada?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um NAT Gateway em uma sub-rede pública e adicionar uma rota padrão (0.0.0.0/0) na tabela de rotas privadas apontando para o NAT Gateway.",
                    "explanation": "Incorreto: Os NAT Gateways incorrem em custos de execução por hora e taxas de processamento de dados por GB, além de passarem pelo Internet Gateway para alcançar os IPs públicos do S3."
                },
                {
                    "id": "B",
                    "text": "Anexar um Internet Gateway à VPC e atribuir endereços IPv4 públicos às instâncias privadas do EC2.",
                    "explanation": "Incorreto: Atribuir IPs públicos e abrir rotas de internet viola a postura de segurança da sub-rede privada."
                },
                {
                    "id": "C",
                    "text": "Criar um Gateway VPC Endpoint para o Amazon S3 e associá-lo às tabelas de rotas das sub-redes privadas.",
                    "explanation": "Correto: Os Gateway VPC Endpoints para S3 e DynamoDB são totalmente gratuitos, não exigem dispositivos NAT e roteiam o tráfego de forma privada por meio de listas de prefixos de tabelas de rotas da AWS."
                },
                {
                    "id": "D",
                    "text": "Criar um Interface VPC Endpoint (AWS PrivateLink) para o S3 nas sub-redes privadas.",
                    "explanation": "Incorreto: Os Interface Endpoints incorrem em cobranças horárias por endpoint e taxas de processamento de dados por GB, ao contrário dos Gateway Endpoints gratuitos para S3."
                }
            ],
            "generalExplanation": "Os VPC Gateway Endpoints para Amazon S3 fornecem conectividade direta e segura a partir de sub-redes privadas de VPC para o S3 por meio do backbone da AWS sem custos adicionais."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una flota de instancias de Amazon EC2 en subredes privadas sin acceso a internet necesita descargar parches de software y conjuntos de datos desde un bucket de Amazon S3 en la misma región de AWS. El arquitecto de red debe garantizar que el tráfico entre las instancias de EC2 y el bucket de S3 viaje completamente a través de la red privada de AWS, sin requerir un NAT Gateway, Internet Gateway ni tarifas recurrentes por hora de endpoint. ¿Qué solución se debe implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un NAT Gateway en una subred pública y agregar una ruta predeterminada (0.0.0.0/0) en la tabla de rutas privadas que apunte al NAT Gateway.",
                    "explanation": "Incorrecto: Los NAT Gateways generan costos de ejecución por hora y tarifas de procesamiento de datos por GB, y atraviesan la ruta del Internet Gateway para llegar a las IPs públicas de S3."
                },
                {
                    "id": "B",
                    "text": "Adjuntar un Internet Gateway a la VPC y asignar direcciones IPv4 públicas a las instancias privadas de EC2.",
                    "explanation": "Incorrecto: Asignar IPs públicas y abrir rutas a internet compromete la postura de seguridad de la subred privada."
                },
                {
                    "id": "C",
                    "text": "Crear un Gateway VPC Endpoint para Amazon S3 y asociarlo a las tablas de rutas de las subredes privadas.",
                    "explanation": "Correcto: Los Gateway VPC Endpoints para S3 y DynamoDB son completamente gratuitos, no requieren dispositivos NAT y enrutan el tráfico de forma privada mediante listas de prefijos en las tablas de rutas de AWS."
                },
                {
                    "id": "D",
                    "text": "Crear un Interface VPC Endpoint (AWS PrivateLink) para S3 en las subredes privadas.",
                    "explanation": "Incorrecto: Los Interface Endpoints incurren en cargos por hora y tarifas de procesamiento de datos por GB, a diferencia de los Gateway Endpoints gratuitos para S3."
                }
            ],
            "generalExplanation": "Los VPC Gateway Endpoints para Amazon S3 proporcionan conectividad segura y directa desde subredes privadas de VPC hacia S3 a través de la red troncal de AWS sin costo adicional."
        }
    },
    "saa-q017": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma instituição financeira exige uma solução de registro centralizado para capturar todas as atividades de API de gerenciamento em todas as contas e regiões da AWS. Os logs devem ser agregados em um bucket do Amazon S3 localizado em uma conta dedicada de Auditoria de Segurança. A política de conformidade de segurança determina que os arquivos de log de auditoria devem ter validação criptográfica para verificar se os arquivos não foram modificados, excluídos ou violados após a entrega. Qual combinação de ações o arquiteto deve configurar?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o VPC Flow Logs em todas as contas e definir políticas de ciclo de vida do S3 para expirar objetos após 30 dias.",
                    "explanation": "Incorreto: O VPC Flow Logs captura fluxos de pacotes IP de rede, não eventos de gerenciamento de API e usuários do IAM."
                },
                {
                    "id": "B",
                    "text": "Implantar agentes do Amazon CloudWatch Logs em todas as instâncias do EC2 e transmitir logs para o Amazon OpenSearch Service.",
                    "explanation": "Incorreto: Os agentes do CloudWatch no EC2 capturam logs do sistema operacional, não chamadas de API de gerenciamento da conta da AWS."
                },
                {
                    "id": "C",
                    "text": "Configurar trilhas individuais em cada conta e escrever uma função Lambda diária para comparar hashes de arquivos manualmente.",
                    "explanation": "Incorreto: O cálculo manual de hashes com Lambda introduz complexidade operacional e é inferior à validação nativa de digests do CloudTrail."
                },
                {
                    "id": "D",
                    "text": "Habilitar o AWS CloudTrail Organization Trail com a Validação de Integridade de Arquivo de Log (Log File Integrity Validation) ativada, entregando logs a um bucket criptografado do S3 na conta de Auditoria de Segurança.",
                    "explanation": "Correto: As trilhas de organização do CloudTrail capturam eventos em todas as contas, e a habilitação da validação de integridade de arquivos de log gera arquivos digest SHA-256 para detectar qualquer adulteração."
                }
            ],
            "generalExplanation": "A Validação de Integridade de Arquivo de Log do AWS CloudTrail utiliza hashing SHA-256 e assinaturas digitais para fornecer registros de auditoria à prova de adulteração em todo o AWS Organizations."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una empresa financiera requiere una solución de registro centralizada para capturar todas las actividades de la API de administración en todas las cuentas y regiones de AWS. Los registros deben agregarse en un bucket de Amazon S3 ubicado en una cuenta dedicada de Auditoría de Seguridad. La política de cumplimiento de seguridad exige que los archivos de registro de auditoría tengan validación criptográfica para verificar que los archivos no hayan sido modificados, eliminados ni manipulados después de su entrega. ¿Qué combinación de acciones debe configurar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar VPC Flow Logs en todas las cuentas y establecer políticas de ciclo de vida de S3 para caducar objetos después de 30 días.",
                    "explanation": "Incorrecto: VPC Flow Logs captura flujos de paquetes IP de red, no eventos de administración de API y usuarios de IAM."
                },
                {
                    "id": "B",
                    "text": "Implementar agentes de Amazon CloudWatch Logs en todas las instancias de EC2 y transmitir registros a Amazon OpenSearch Service.",
                    "explanation": "Incorrecto: Los agentes de CloudWatch en EC2 capturan registros del sistema operativo, no llamadas a la API de administración de cuentas de AWS."
                },
                {
                    "id": "C",
                    "text": "Configurar rutas individuales en cada cuenta y escribir una función Lambda diaria para comparar hashes de archivos manualmente.",
                    "explanation": "Incorrecto: El hash manual con Lambda introduce complejidad operativa y es inferior a la validación nativa de resúmenes de CloudTrail."
                },
                {
                    "id": "D",
                    "text": "Habilitar una ruta de organización de AWS CloudTrail con la Validación de Integridad de Archivos de Registro (Log File Integrity Validation) habilitada, entregando registros a un bucket de S3 cifrado en la cuenta de Auditoría de Seguridad.",
                    "explanation": "Correcto: Las rutas de organización de CloudTrail capturan eventos en todas las cuentas, y habilitar la validación de integridad genera archivos de resumen SHA-256 para detectar manipulaciones."
                }
            ],
            "generalExplanation": "La validación de integridad de archivos de registro de AWS CloudTrail utiliza hash SHA-256 y firmas digitales para proporcionar registros de auditoría a prueba de manipulaciones en todo AWS Organizations."
        }
    },
    "saa-q018": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma organização gerencia um bucket compartilhado do Amazon S3 na Conta A que contém conjuntos de dados analíticos. Usuários do IAM entre contas (cross-account) na Conta B precisam de acesso de leitura a esses conjuntos de dados. A política de governança de dados exige que os dados enviados pela Conta B sejam de propriedade da Conta A e que o acesso público ao bucket seja completamente impedido em todos os momentos. Qual combinação de ações atende a esses requisitos? (Escolha duas.)",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma instância proxy do Amazon EC2 em uma sub-rede pública para intermediar transferências de arquivos entre contas.",
                    "explanation": "Incorreto: Um proxy no EC2 adiciona sobrecarga desnecessária de computação e manutenção em comparação com permissões nativas do IAM entre contas do S3."
                },
                {
                    "id": "B",
                    "text": "Configurar o S3 Object Ownership como Bucket Owner Enforced no bucket da Conta A.",
                    "explanation": "Correto: A opção Bucket Owner Enforced desativa ACLs e transfere automaticamente a propriedade de todos os objetos enviados entre contas para o proprietário do bucket (Conta A)."
                },
                {
                    "id": "C",
                    "text": "Configurar a ACL do bucket para conceder permissões públicas de gravação para uploads anônimos.",
                    "explanation": "Incorreto: Conceder permissões públicas cria graves riscos de segurança e contradiz a exigência de não ter acesso público."
                },
                {
                    "id": "D",
                    "text": "Criar uma role do IAM na Conta A com uma chave de acesso e distribuir a chave secreta estática para todos os usuários na Conta B.",
                    "explanation": "Incorreto: A distribuição de credenciais estáticas viola princípios de segurança; os usuários devem assumir roles entre contas ou usar políticas de bucket."
                },
                {
                    "id": "E",
                    "text": "Habilitar as configurações do S3 Block Public Access no nível do bucket e da conta na Conta A.",
                    "explanation": "Correto: O S3 Block Public Access impede a exposição pública acidental por meio de políticas de bucket ou ACLs."
                }
            ],
            "generalExplanation": "Configurar o S3 Object Ownership como 'Bucket Owner Enforced' desativa ACLs e garante que o proprietário do bucket possua todos os objetos enviados de principais entre contas. O S3 Block Public Access garante que o bucket permaneça estritamente privado."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Una organización administra un bucket compartido de Amazon S3 en la Cuenta A que contiene conjuntos de datos analíticos. Usuarios de IAM entre cuentas en la Cuenta B necesitan acceso de lectura a estos conjuntos de datos. La política de gobernanza de datos requiere que los datos cargados por la Cuenta B sean propiedad de la Cuenta A, y que el acceso público al bucket esté completamente bloqueado en todo momento. ¿Qué combinación de acciones cumple con estos requisitos? (Seleccione dos.)",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una instancia proxy de Amazon EC2 en una subred pública para mediar transferencias de archivos entre cuentas.",
                    "explanation": "Incorrecto: Un proxy en EC2 agrega sobrecarga de cómputo y mantenimiento innecesarios en comparación con los permisos nativos de IAM entre cuentas de S3."
                },
                {
                    "id": "B",
                    "text": "Configurar S3 Object Ownership en Bucket Owner Enforced en el bucket de la Cuenta A.",
                    "explanation": "Correcto: Bucket Owner Enforced deshabilita las ACLs y transfiere automáticamente la propiedad de todos los objetos cargados entre cuentas al propietario del bucket (Cuenta A)."
                },
                {
                    "id": "C",
                    "text": "Configurar la ACL del bucket para otorgar permisos de escritura públicos para cargas anónimas.",
                    "explanation": "Incorrecto: Otorgar permisos públicos crea riesgos de seguridad severos y contradice el requisito de privacidad."
                },
                {
                    "id": "D",
                    "text": "Crear un rol de IAM en la Cuenta A con una clave de acceso y distribuir la clave secreta estática a todos los usuarios de la Cuenta B.",
                    "explanation": "Incorrecto: Distribuir credenciales estáticas infringe los principios de seguridad; los usuarios deben asumir roles entre cuentas o usar políticas de bucket."
                },
                {
                    "id": "E",
                    "text": "Habilitar la configuración de S3 Block Public Access a nivel de bucket y de cuenta en la Cuenta A.",
                    "explanation": "Correcto: S3 Block Public Access previene la exposición pública accidental a través de políticas de bucket o ACLs."
                }
            ],
            "generalExplanation": "Configurar S3 Object Ownership en 'Bucket Owner Enforced' desactiva las ACLs y garantiza que el propietario del bucket posea todos los objetos cargados por principales de otras cuentas. S3 Block Public Access garantiza que el bucket permanezca privado."
        }
    },
    "saa-q019": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Um arquiteto de soluções está auditando as permissões do IAM de uma equipe de analytics. Várias políticas do IAM contêm instruções com caracteres curinga (`Action: *`, `Resource: *`). O arquiteto deve refatorar essas políticas para aderir ao princípio do menor privilégio e proteger os dados confidenciais da empresa no S3. Quais ações o arquiteto deve tomar? (Escolha duas.)",
            "options": [
                {
                    "id": "A",
                    "text": "Anexar a política gerenciada AdministratorAccess a todas as roles de usuário e confiar nas tags de bucket do S3 para segurança.",
                    "explanation": "Incorreto: AdministratorAccess concede controle irrestrito total sobre todos os serviços da AWS, violando o princípio do menor privilégio."
                },
                {
                    "id": "B",
                    "text": "Criar políticas inline em cada usuário do IAM em vez de usar políticas gerenciadas pelo cliente anexadas a grupos do IAM.",
                    "explanation": "Incorreto: Políticas inline em usuários individuais criam desorganização administrativa e são difíceis de gerenciar e auditar em comparação com políticas gerenciadas anexadas a grupos."
                },
                {
                    "id": "C",
                    "text": "Usar o AWS IAM Access Analyzer para revisar o acesso aos recursos e gerar políticas refinadas com base na atividade real registrada no CloudTrail.",
                    "explanation": "Correto: A geração de políticas do IAM Access Analyzer analisa os logs do CloudTrail para criar automaticamente políticas de menor privilégio correspondentes às ações observadas."
                },
                {
                    "id": "D",
                    "text": "Substituir as permissões com curinga por ações específicas do S3 (como s3:GetObject e s3:PutObject) restritas aos ARNs de buckets específicos no bloco Resource.",
                    "explanation": "Correto: Ações explícitas e ARNs de recursos limitam os usuários estritamente às operações mínimas necessárias nos buckets autorizados."
                },
                {
                    "id": "E",
                    "text": "Gerar access keys do IAM de longo prazo para cada desenvolvedor e embuti-las nas aplicações clientes.",
                    "explanation": "Incorreto: Codificar credenciais estáticas cria vulnerabilidades graves de segurança."
                }
            ],
            "generalExplanation": "Aderir ao menor privilégio requer restringir as ações do IAM e os ARNs de recursos, além de usar ferramentas como o AWS IAM Access Analyzer para gerar políticas a partir de logs de acesso verificados."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un arquitecto de soluciones está auditando los permisos de IAM para un equipo de analítica. Varias políticas de IAM contienen declaraciones con comodines (`Action: *`, `Resource: *`). El arquitecto debe refactorizar estas políticas para adherirse al principio de mínimo privilegio y proteger los datos confidenciales de S3 de la empresa. ¿Qué acciones debe tomar el arquitecto? (Seleccione dos.)",
            "options": [
                {
                    "id": "A",
                    "text": "Asociar la política administrada AdministratorAccess a todos los roles de usuario y confiar en las etiquetas de bucket de S3 para la seguridad.",
                    "explanation": "Incorrecto: AdministratorAccess proporciona control irrestricto sobre todos los servicios de AWS, violando el mínimo privilegio."
                },
                {
                    "id": "B",
                    "text": "Crear políticas en línea en cada usuario de IAM en lugar de utilizar políticas administradas por el cliente asociadas a grupos de IAM.",
                    "explanation": "Incorrecto: Las políticas en línea en usuarios individuales provocan dispersión administrativa y son difíciles de auditar en comparación con políticas administradas asociadas a grupos."
                },
                {
                    "id": "C",
                    "text": "Utilizar AWS IAM Access Analyzer para revisar el acceso a los recursos y generar políticas detalladas basadas en la actividad real de CloudTrail.",
                    "explanation": "Correcto: La generación de políticas de IAM Access Analyzer analiza los registros de CloudTrail para crear automáticamente políticas de mínimo privilegio según las acciones observadas."
                },
                {
                    "id": "D",
                    "text": "Reemplazar los permisos de comodín con acciones específicas de S3 (como s3:GetObject y s3:PutObject) restringidas a ARNs de buckets específicos en el bloque Resource.",
                    "explanation": "Correcto: Las acciones explícitas y los ARNs de recursos limitan estrictamente a los usuarios a las operaciones mínimas requeridas en los buckets autorizados."
                },
                {
                    "id": "E",
                    "text": "Generar claves de acceso de IAM a largo plazo para cada desarrollador e incrustarlas en aplicaciones cliente.",
                    "explanation": "Incorrecto: Incluir credenciales estáticas crea vulnerabilidades de seguridad críticas."
                }
            ],
            "generalExplanation": "Adherirse al mínimo privilegio requiere limitar las acciones de IAM y los ARNs de recursos, y usar herramientas como AWS IAM Access Analyzer para generar políticas a partir de registros de acceso reales."
        }
    },
    "saa-q020": {
        "pt": {
            "domainName": "Domínio 1: Projetar Arquiteturas Seguras",
            "statement": "Uma equipe de operações precisa de acesso administrativo via SSH e RDP para gerenciar instâncias do Amazon EC2 executadas em sub-redes privadas. A equipe de segurança proíbe a abertura de portas de entrada 22 ou 3389 em security groups, veta a atribuição de endereços IPv4 públicos às instâncias e proíbe a manutenção de bastion hosts (jump boxes). Qual solução atende a essas restrições de segurança?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar uma conexão AWS Site-to-Site VPN e abrir a porta 22 nos security groups privados para 0.0.0.0/0.",
                    "explanation": "Incorreto: Abrir a porta 22 para 0.0.0.0/0 viola o menor privilégio e a Site-to-Site VPN envolve sobrecarga de configuração de hardware/gateway."
                },
                {
                    "id": "B",
                    "text": "Instalar um servidor OpenVPN em uma instância do EC2 em uma sub-rede pública e conectar-se por meio de certificados VPN de cliente.",
                    "explanation": "Incorreto: Executar uma instância VPN autogerenciada requer manutenção de infraestrutura pública, aplicação de patches e portas de entrada abertas."
                },
                {
                    "id": "C",
                    "text": "Configurar um Application Load Balancer com listeners TCP para atuar como proxy de conexões SSH para as instâncias privadas.",
                    "explanation": "Incorreto: ALBs operam na Camada 7 (HTTP/HTTPS/gRPC) e não oferecem suporte a listeners genéricos de proxy TCP/SSH (o que exigiria NLB), além de ainda requerer portas de entrada abertas."
                },
                {
                    "id": "D",
                    "text": "Anexar uma role do IAM com a política AmazonSSMManagedInstanceCore às instâncias do EC2 e usar o AWS Systems Manager Session Manager para acesso ao shell e à CLI.",
                    "explanation": "Correto: O AWS Systems Manager Session Manager permite gerenciamento seguro e auditado de instâncias por meio do agente SSM em HTTPS de saída, sem abrir portas de entrada nem executar bastion hosts."
                }
            ],
            "generalExplanation": "O AWS Systems Manager Session Manager fornece acesso seguro e com um clique ao terminal e ao PowerShell em instâncias do EC2 sem portas de entrada abertas, bastion hosts ou gerenciamento de chaves SSH."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Arquitecturas Seguras",
            "statement": "Un equipo de operaciones necesita acceso administrativo SSH y RDP para administrar instancias de Amazon EC2 que se ejecutan en subredes privadas. El equipo de seguridad prohíbe abrir los puertos de entrada 22 o 3389 en los security groups, prohíbe asignar direcciones IPv4 públicas a las instancias y prohíbe mantener servidores bastion (jump boxes). ¿Qué solución satisface estas restricciones de seguridad?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear una conexión AWS Site-to-Site VPN y abrir el puerto 22 en los security groups privados hacia 0.0.0.0/0.",
                    "explanation": "Incorrecto: Abrir el puerto 22 a 0.0.0.0/0 viola el mínimo privilegio y Site-to-Site VPN requiere sobrecarga de configuración de hardware y puertas de enlace."
                },
                {
                    "id": "B",
                    "text": "Instalar un servidor OpenVPN en una instancia de EC2 en una subred pública y conectarse a través de certificados VPN de cliente.",
                    "explanation": "Incorrecto: Ejecutar una instancia VPN autoadministrada requiere gestionar infraestructura pública, aplicar parches y mantener puertos de entrada abiertos."
                },
                {
                    "id": "C",
                    "text": "Configurar un Application Load Balancer con listeners TCP para actuar como proxy de conexiones SSH hacia las instancias privadas.",
                    "explanation": "Incorrecto: Los ALBs operan en la Capa 7 (HTTP/HTTPS/gRPC) y no admiten listeners proxy TCP/SSH genéricos (que requieren NLB), y esto aún requeriría puertos de entrada abiertos."
                },
                {
                    "id": "D",
                    "text": "Adjuntar un rol de IAM con la política AmazonSSMManagedInstanceCore a las instancias de EC2 y utilizar AWS Systems Manager Session Manager para el acceso a terminal y CLI.",
                    "explanation": "Correcto: AWS Systems Manager Session Manager permite una administración de instancias segura y auditada a través del agente SSM mediante HTTPS saliente sin abrir puertos de entrada ni ejecutar bastion hosts."
                }
            ],
            "generalExplanation": "AWS Systems Manager Session Manager proporciona acceso seguro a terminal y PowerShell en instancias de EC2 con un solo clic sin puertos de entrada abiertos, bastion hosts ni administración de claves SSH."
        }
    },
    "saa-q021": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa de comércio eletrônico executa uma instância de banco de dados Amazon RDS MySQL compatível com sua aplicação de carrinho de compras. O banco de dados está atualmente implantado em uma única Zona de Disponibilidade. A empresa exige alta disponibilidade com failover automático em caso de interrupção da AZ ou degradação de hardware, sem perda de dados e com o mínimo de reconfiguração da aplicação. Qual modificação arquitetural o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma segunda instância single-AZ do RDS em uma AZ diferente e configurar o código da aplicação para executar gravações duplas (dual-writes) em ambos os bancos de dados.",
                    "explanation": "Incorreto: Gravações duplas no código da aplicação criam anomalias de consistência de dados e enorme sobrecarga de desenvolvimento."
                },
                {
                    "id": "B",
                    "text": "Modificar a instância do Amazon RDS para habilitar a implantação Multi-AZ para provisionar e replicar dados de forma síncrona automaticamente para uma instância em espera (standby) em uma AZ diferente.",
                    "explanation": "Correto: As implantações Multi-AZ do RDS mantêm uma cópia síncrona em espera em uma AZ separada com failover automático por DNS normalmente em menos de 60 a 120 segundos e zero perda de dados."
                },
                {
                    "id": "C",
                    "text": "Tirar snapshots automáticos do banco de dados a cada hora e configurar o AWS Backup para restaurar o snapshot em uma AZ secundária quando ocorrer uma falha.",
                    "explanation": "Incorreto: Restaurar a partir de snapshots pode levar horas e resulta em perda de até 1 hora de transações (altos RPO e RTO)."
                },
                {
                    "id": "D",
                    "text": "Criar uma Read Replica assíncrona entre regiões (Cross-Region) e escrever uma função do AWS Lambda para promover a réplica durante uma interrupção.",
                    "explanation": "Incorreto: As réplicas de leitura entre regiões usam replicação assíncrona (possível perda de dados) e exigem promoção manual e redirecionamento de DNS."
                }
            ],
            "generalExplanation": "As implantações Multi-AZ do Amazon RDS oferecem maior disponibilidade e durabilidade para instâncias de banco de dados, replicando dados de forma síncrona para uma instância em espera em uma Zona de Disponibilidade diferente com failover automatizado."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa de comercio electrónico ejecuta una instancia de base de datos Amazon RDS MySQL que respalda su aplicación de carrito de compras. La base de datos está implementada actualmente en una sola Zona de Disponibilidad. La empresa requiere alta disponibilidad con conmutación por error automática en caso de una interrupción de la AZ o degradación de hardware, sin pérdida de datos y con una reconfiguración mínima de la aplicación. ¿Qué modificación arquitectónica debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una segunda instancia de una sola AZ de RDS en una AZ diferente y configurar el código de la aplicación para realizar escrituras dobles en ambas bases de datos.",
                    "explanation": "Incorrecto: La escritura dual en el código de la aplicación genera inconsistencias en los datos y una sobrecarga masiva de desarrollo."
                },
                {
                    "id": "B",
                    "text": "Modificar la instancia de Amazon RDS para habilitar la implementación Multi-AZ y aprovisionar y replicar datos de forma síncrona y automática en una instancia en espera (standby) en una AZ diferente.",
                    "explanation": "Correcto: Las implementaciones Multi-AZ de RDS mantienen una copia síncrona en espera en una AZ separada con conmutación por error automática por DNS normalmente en menos de 60 a 120 segundos y sin pérdida de datos."
                },
                {
                    "id": "C",
                    "text": "Tomar snapshots automatizados de la base de datos cada hora y configurar AWS Backup para restaurar el snapshot en una AZ secundaria cuando ocurra una falla.",
                    "explanation": "Incorrecto: Restaurar desde snapshots puede tardar horas y ocasionar la pérdida de hasta 1 hora de transacciones (RPO y RTO altos)."
                },
                {
                    "id": "D",
                    "text": "Crear una réplica de lectura asíncrona entre regiones (Cross-Region) y escribir una función de AWS Lambda para promover la réplica durante una interrupción.",
                    "explanation": "Incorrecto: Las réplicas de lectura entre regiones utilizan replicación asíncrona (posible pérdida de datos) y requieren promoción manual y redireccionamiento de DNS."
                }
            ],
            "generalExplanation": "Las implementaciones Multi-AZ de Amazon RDS proporcionan alta disponibilidad y durabilidad para instancias de bases de datos al replicar datos sincrónicamente en una instancia en espera en una Zona de Disponibilidad diferente con conmutación por error automatizada."
        }
    },
    "saa-q022": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma aplicação de digitalização de documentos processa faturas de clientes enviadas para um bucket do S3. Uma camada de trabalhadores (workers) no EC2 analisa as faturas e extrai dados. Durante o horário comercial, milhares de faturas chegam simultaneamente, fazendo com que a camada de trabalhadores trave devido ao esgotamento de threads. O sistema deve ser desacoplado para que nenhuma fatura seja perdida e as instâncias de trabalhadores escalem dinamicamente com base no acúmulo da fila. Qual solução o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar um Application Load Balancer para distribuir notificações de eventos do S3 diretamente para instâncias de trabalhadores do EC2 usando roteamento round-robin.",
                    "explanation": "Incorreto: O S3 não pode enviar notificações de webhook diretamente por meio de um ALB para o EC2 sem proteção de buffer contra falhas dos trabalhadores."
                },
                {
                    "id": "B",
                    "text": "Armazenar faturas no Amazon ElastiCache for Redis e definir a métrica do Auto Scaling group do EC2 para utilização de CPU em 90%.",
                    "explanation": "Incorreto: O Redis é um cache em memória inadequado para armazenamento de documentos pesados, e a utilização de CPU não reflete com precisão o acúmulo de trabalho pendente."
                },
                {
                    "id": "C",
                    "text": "Enviar notificações de eventos de upload do S3 para uma fila do Amazon SQS e configurar o Auto Scaling Group de trabalhadores do EC2 para escalar com base em uma métrica personalizada que rastreie o acúmulo por instância (ApproximateNumberOfMessagesVisible).",
                    "explanation": "Correto: O SQS atua como um buffer resiliente evitando a perda de tarefas, e escalar o Auto Scaling Group com base na profundidade da fila do SQS garante um dimensionamento responsivo."
                },
                {
                    "id": "D",
                    "text": "Aumentar o tamanho das instâncias de trabalhadores do EC2 para um tipo de instância maior (escalar verticalmente) e armazenar as faturas em um volume EBS anexado.",
                    "explanation": "Incorreto: O dimensionamento vertical possui limites físicos, introduz um ponto único de falha e não desacopla a camada de ingestão do processamento."
                }
            ],
            "generalExplanation": "O uso de uma fila do Amazon SQS para armazenar tarefas recebidas em buffer, combinado com um Auto Scaling group que rastreia o backlog da fila por instância (ApproximateNumberOfMessagesVisible), fornece um desacoplamento escalável e resiliente."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una aplicación de escaneo de documentos procesa facturas de clientes cargadas en un bucket de S3. Una capa de procesamiento de EC2 analiza las facturas y extrae datos. Durante el horario comercial, llegan miles de facturas simultáneamente, lo que provoca la caída de la capa de procesamiento debido al agotamiento de subprocesos. El sistema debe desacoplarse para que no se pierda ninguna factura y las instancias de procesamiento escalen dinámicamente según la acumulación en la cola. ¿Qué solución debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar un Application Load Balancer para distribuir notificaciones de eventos de S3 directamente a las instancias de EC2 mediante enrutamiento round-robin.",
                    "explanation": "Incorrecto: S3 no puede enviar notificaciones webhook directamente a través de un ALB hacia EC2 sin protección de búfer contra caídas de servidores."
                },
                {
                    "id": "B",
                    "text": "Almacenar facturas en Amazon ElastiCache for Redis y configurar la métrica del grupo de Auto Scaling de EC2 en 90% de utilización de CPU.",
                    "explanation": "Incorrecto: Redis es una memoria caché no adecuada para almacenamiento en búfer de documentos grandes, y la utilización de CPU no refleja con precisión el trabajo pendiente."
                },
                {
                    "id": "C",
                    "text": "Enviar notificaciones de eventos de carga de S3 a una cola de Amazon SQS y configurar el Auto Scaling Group de trabajadores de EC2 para escalar en función de una métrica personalizada que rastree el trabajo acumulado por instancia (ApproximateNumberOfMessagesVisible).",
                    "explanation": "Correcto: SQS actúa como un búfer resiliente que evita la pérdida de trabajos, y escalar el Auto Scaling Group según la profundidad de la cola de SQS garantiza una respuesta rápida."
                },
                {
                    "id": "D",
                    "text": "Aumentar el tamaño de las instancias de procesamiento de EC2 a un tipo de instancia más grande (escalar verticalmente) y almacenar facturas en un volumen EBS conectado.",
                    "explanation": "Incorrecto: El escalado vertical tiene límites físicos, introduce un punto único de falla y no desacopla la capa de ingesta del procesamiento."
                }
            ],
            "generalExplanation": "El uso de una cola de Amazon SQS para almacenar trabajos entrantes junto con un grupo de Auto Scaling que realiza un seguimiento del trabajo pendiente por instancia (ApproximateNumberOfMessagesVisible) proporciona un desacoplamiento resiliente y escalable."
        }
    },
    "saa-q023": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma plataforma bancária processa solicitações de autorização de cartão de crédito em tempo real. A ordem das transações dentro de cada conta de cliente deve ser preservada exatamente (Primeiro a Entrar, Primeiro a Sair - FIFO) e mensagens de transações duplicadas devem ser evitadas. Qual configuração de serviço de enfileiramento de mensagens atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Tópico Standard do Amazon SNS com vários endpoints HTTP inscritos.",
                    "explanation": "Incorreto: Tópicos Standard do SNS não garantem ordenação estrita de mensagens nem desduplicação de mensagens."
                },
                {
                    "id": "B",
                    "text": "Barramento de eventos personalizado do Amazon EventBridge com políticas de repetição e Dead-Letter Queue (DLQ).",
                    "explanation": "Incorreto: O EventBridge não garante ordenação FIFO sequencial para registros transacionais de alto throughput como uma fila SQS FIFO."
                },
                {
                    "id": "C",
                    "text": "Fila Standard do Amazon SQS configurada com Long Polling ativado e um Visibility Timeout de 60 segundos.",
                    "explanation": "Incorreto: Filas Standard do SQS fornecem ordenação de melhor esforço e entrega pelo menos uma vez (at-least-once), o que pode resultar em mensagens fora de ordem e duplicadas."
                },
                {
                    "id": "D",
                    "text": "Fila FIFO do Amazon SQS configurada com um Message Group ID correspondente ao número da conta do cliente e ID de desduplicação.",
                    "explanation": "Correto: As filas FIFO do Amazon SQS garantem a ordenação First-In-First-Out exata por Message Group ID e garantem processamento exatamente uma vez (exactly-once) por meio de desduplicação de mensagens."
                }
            ],
            "generalExplanation": "As filas FIFO (First-In-First-Out) do Amazon SQS preservam a ordem exata em que as mensagens são enviadas e recebidas, com desduplicação garantindo que não haja mensagens duplicadas."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una plataforma bancaria procesa solicitudes de autorización de tarjetas de crédito en tiempo real. El orden de las transacciones dentro de cada cuenta de cliente debe mantenerse con total exactitud (First-In, First-Out) y se deben evitar mensajes de transacciones duplicados. ¿Qué configuración de servicio de colas de mensajes cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Tema Standard de Amazon SNS con múltiples puntos de enlace HTTP suscritos.",
                    "explanation": "Incorrecto: Los temas Standard de SNS no garantizan un orden estricto de mensajes ni deduplicación de mensajes."
                },
                {
                    "id": "B",
                    "text": "Bus de eventos personalizado de Amazon EventBridge con políticas de reintento de DLQ.",
                    "explanation": "Incorrecto: EventBridge no garantiza el orden FIFO secuencial para registros transaccionales de alto rendimiento como una cola SQS FIFO."
                },
                {
                    "id": "C",
                    "text": "Cola Standard de Amazon SQS configurada con Long Polling habilitado y un Visibility Timeout de 60 segundos.",
                    "explanation": "Incorrecto: Las colas Standard de SQS proporcionan orden de mejor esfuerzo y entrega al menos una vez (at-least-once), lo que puede generar mensajes desordenados y duplicados."
                },
                {
                    "id": "D",
                    "text": "Cola FIFO de Amazon SQS configurada con un Message Group ID correspondiente al número de cuenta del cliente e ID de deduplicación.",
                    "explanation": "Correcto: Las colas FIFO de Amazon SQS garantizan el orden First-In-First-Out exacto por Message Group ID y aseguran el procesamiento exactamente una vez mediante la deduplicación de mensajes."
                }
            ],
            "generalExplanation": "Las colas FIFO (First-In-First-Out) de Amazon SQS preservan el orden exacto en el que se envían y reciben los mensajes, con deduplicación que garantiza la ausencia de duplicados."
        }
    },
    "saa-q024": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa opera um serviço web crítico implantado em duas regiões da AWS: us-east-1 (Primária) e us-west-2 (Secundária). A empresa exige uma estratégia de recuperação de desastres ativo-passiva em que o Amazon Route 53 roteie 100% do tráfego de usuários para a região primária em operações normais e desvie automaticamente o tráfego para a região secundária caso as verificações de integridade em us-east-1 falhem. Qual política de roteamento do Route 53 deve ser configurada?",
            "options": [
                {
                    "id": "A",
                    "text": "Política de roteamento ponderada (Weighted) com pesos definidos em 50/50",
                    "explanation": "Incorreto: Um peso de 50/50 divide o tráfego igualmente entre as regiões, criando uma configuração ativo-ativo."
                },
                {
                    "id": "B",
                    "text": "Configurar uma política de roteamento baseada em latência do Amazon Route 53 para direcionar os usuários para o endpoint regional de menor latência.",
                    "explanation": "Incorreto: O roteamento por latência direciona o tráfego para a região de menor latência, resultando em distribuição ativo-ativo em vez de ativo-passivo."
                },
                {
                    "id": "C",
                    "text": "Política de roteamento de failover (Failover) configurada com verificações de integridade do Route 53 associadas ao registro primário",
                    "explanation": "Correto: O roteamento de Failover do Route 53 cria uma configuração ativo-passiva, roteando o tráfego para o endpoint primário até que sua verificação de integridade associada falhe, momento em que ele muda para o secundário."
                },
                {
                    "id": "D",
                    "text": "Política de roteamento de geolocalização (Geolocation) com base no continente",
                    "explanation": "Incorreto: A geolocalização roteia o tráfego com base na localização do cliente, não no status de saúde ou failover ativo-passivo."
                }
            ],
            "generalExplanation": "O roteamento de Failover do Route 53 foi desenvolvido especificamente para configurações de recuperação de desastres ativo-passivas, redirecionando o tráfego automaticamente quando as verificações de integridade primárias falham."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa opera un servicio web crítico implementado en dos regiones de AWS: us-east-1 (Primaria) y us-west-2 (Secundaria). La empresa requiere una estrategia de recuperación ante desastres activo-pasiva en la que Amazon Route 53 enrute el 100% del tráfico de usuarios hacia la región primaria en operaciones normales y desvíe automáticamente el tráfico hacia la región secundaria si fallan las comprobaciones de estado en us-east-1. ¿Qué política de enrutamiento de Route 53 se debe configurar?",
            "options": [
                {
                    "id": "A",
                    "text": "Política de enrutamiento ponderado (Weighted) con pesos establecidos en 50/50",
                    "explanation": "Incorrecto: Un peso 50/50 divide el tráfico equitativamente entre regiones, creando una configuración activo-activo."
                },
                {
                    "id": "B",
                    "text": "Configurar una política de enrutamiento basada en latencia de Amazon Route 53 para dirigir a los usuarios al punto de enlace regional con menor latencia.",
                    "explanation": "Incorrecto: El enrutamiento por latencia dirige el tráfico a la región con menor latencia, resultando en una distribución activo-activo en lugar de activo-pasivo."
                },
                {
                    "id": "C",
                    "text": "Política de enrutamiento por conmutación por error (Failover) configurada con comprobaciones de estado de Route 53 asociadas al registro primario",
                    "explanation": "Correcto: El enrutamiento por conmutación por error de Route 53 crea una configuración activo-pasiva, enviando tráfico al punto de enlace principal hasta que falle su comprobación de estado, momento en el cual cambia al secundario."
                },
                {
                    "id": "D",
                    "text": "Política de enrutamiento por geolocalización (Geolocation) basada en continente",
                    "explanation": "Incorrecto: La geolocalización enruta el tráfico en función de la ubicación del cliente, no del estado de salud ni de la conmutación por error activo-pasiva."
                }
            ],
            "generalExplanation": "El enrutamiento por conmutación por error (Failover) de Route 53 está diseñado específicamente para configuraciones de recuperación ante desastres activo-pasivas, desviando el tráfico automáticamente cuando fallan los health checks primarios."
        }
    },
    "saa-q025": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa global de jogos online precisa de um banco de dados relacional de backend capaz de sobreviver a um desastre regional completo na AWS com um Objetivo de Ponto de Recuperação (RPO) inferior a 1 segundo e um Objetivo de Tempo de Recuperação (RTO) inferior a 1 minuto. O cluster de banco de dados primário está implantado em us-east-1. Qual arquitetura de banco de dados satisfaz esses objetivos estritos de recuperação?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantação Multi-AZ do Amazon RDS PostgreSQL em três Zonas de Disponibilidade em us-east-1.",
                    "explanation": "Incorreto: O Multi-AZ padrão opera dentro de uma única região e não pode sobreviver a uma interrupção catastrófica regional multizona."
                },
                {
                    "id": "B",
                    "text": "AWS Backup agendado para tirar snapshots a cada hora de uma instância do Amazon RDS e copiá-los para us-west-2.",
                    "explanation": "Incorreto: Snapshots horários geram um RPO de até 1 hora, falhando no requisito de RPO < 1s."
                },
                {
                    "id": "C",
                    "text": "Amazon DynamoDB com tabelas em uma única região e exportações periódicas de dados para o S3.",
                    "explanation": "Incorreto: O DynamoDB é um serviço NoSQL (não relacional) e exportações periódicas para o S3 não atendem a RPO < 1s."
                },
                {
                    "id": "D",
                    "text": "Amazon Aurora Global Database com o cluster primário em us-east-1 e um cluster secundário em us-west-2.",
                    "explanation": "Correto: O Amazon Aurora Global Database usa replicação dedicada no nível de armazenamento entre regiões com latência típica de replicação inferior a 1 segundo (RPO < 1s) e oferece suporte a failover rápido em menos de 1 minuto (RTO < 1m)."
                }
            ],
            "generalExplanation": "O Amazon Aurora Global Database fornece replicação entre regiões no nível de armazenamento com atraso de replicação inferior a 1 segundo e promoção de recuperação de desastres entre regiões em menos de um minuto."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa global de videojuegos requiere un backend de base de datos relacional que pueda sobrevivir a un desastre regional completo en AWS con un Objetivo de Punto de Recuperación (RPO) inferior a 1 segundo y un Objetivo de Tiempo de Recuperación (RTO) inferior a 1 minuto. El clúster de base de datos principal está implementado en us-east-1. ¿Qué arquitectura de base de datos satisface estos estrictos objetivos de recuperación?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementación Multi-AZ de Amazon RDS PostgreSQL en tres Zonas de Disponibilidad en us-east-1.",
                    "explanation": "Incorrecto: Multi-AZ estándar opera dentro de una sola región y no puede sobrevivir a una interrupción catastrófica multizona a nivel regional."
                },
                {
                    "id": "B",
                    "text": "AWS Backup programado para tomar snapshots cada hora de una instancia de Amazon RDS y copiarlos a us-west-2.",
                    "explanation": "Incorrecto: Los snapshots por hora ofrecen un RPO de hasta 1 hora, incumpliendo el requisito de RPO < 1s."
                },
                {
                    "id": "C",
                    "text": "Amazon DynamoDB con tablas en una sola región y exportaciones periódicas de datos a S3.",
                    "explanation": "Incorrecto: DynamoDB es un servicio NoSQL (no relacional) y las exportaciones periódicas a S3 no cumplen con RPO < 1s."
                },
                {
                    "id": "D",
                    "text": "Amazon Aurora Global Database con el clúster primario en us-east-1 y un clúster secundario en us-west-2.",
                    "explanation": "Correcto: Amazon Aurora Global Database utiliza replicación dedicada a nivel de almacenamiento entre regiones con una latencia de replicación típica inferior a 1 segundo (RPO < 1s) y admite conmutación rápida en menos de 1 minuto (RTO < 1m)."
                }
            ],
            "generalExplanation": "Amazon Aurora Global Database proporciona replicación entre regiones a nivel de almacenamiento con un retraso inferior a 1 segundo y promoción de recuperación ante desastres entre regiones en menos de un minuto."
        }
    },
    "saa-q026": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma agência de mídia digital armazena gravações de vídeo master em um bucket do Amazon S3 em us-east-1. Devido a requisitos de conformidade, todos os vídeos enviados devem ser replicados automaticamente para um bucket secundário em eu-west-1. Os objetos no bucket de origem são criptografados com uma chave gerenciada pelo cliente do AWS KMS (SSE-KMS). O que deve ser configurado para garantir que a replicação entre regiões funcione corretamente?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o S3 Cross-Region Replication (CRR), fornecer uma role do IAM com permissão kms:Decrypt na chave de origem e kms:Encrypt em uma chave KMS de destino, e especificar o ID da chave de destino na regra de replicação.",
                    "explanation": "Correto: A replicação de objetos criptografados com SSE-KMS requer a habilitação de CRR com o S3 Versioning, especificação da chave KMS de destino e concessão de permissões à role do IAM de replicação para descriptografar na origem e criptografar no destino."
                },
                {
                    "id": "B",
                    "text": "Alterar a criptografia no bucket de origem para texto simples, replicar os objetos e criptografá-los novamente de forma manual no bucket de destino.",
                    "explanation": "Incorreto: Remover a criptografia viola regras de conformidade e introduz sobrecarga manual desnecessária."
                },
                {
                    "id": "C",
                    "text": "Criar uma regra de ciclo de vida do S3 para fazer a transição de objetos para o S3 Glacier em eu-west-1 após 0 dias.",
                    "explanation": "Incorreto: Regras de ciclo de vida do S3 fazem a transição de classes de armazenamento dentro do mesmo bucket/região, não entre regiões da AWS."
                },
                {
                    "id": "D",
                    "text": "Usar o AWS DataSync para executar uma tarefa contínua de sincronização entre os dois endpoints regionais do S3.",
                    "explanation": "Incorreto: O S3 Cross-Region Replication é o mecanismo nativo, automático e sem servidor para replicação de objetos no S3."
                }
            ],
            "generalExplanation": "O Amazon S3 Cross-Region Replication (CRR) requer o S3 Versioning em ambos os buckets e permissões explícitas de IAM e KMS quando os objetos são criptografados com chaves SSE-KMS."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una agencia de medios digitales almacena grabaciones de video maestras en un bucket de Amazon S3 en us-east-1. Debido a requisitos de cumplimiento, todos los videos cargados deben replicarse automáticamente en un bucket secundario en eu-west-1. Los objetos en el bucket de origen están cifrados con una clave administrada por el cliente de AWS KMS (SSE-KMS). ¿Qué se debe configurar para garantizar que la replicación entre regiones funcione correctamente?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar S3 Cross-Region Replication (CRR), proporcionar un rol de IAM con permisos kms:Decrypt en la clave de origen y kms:Encrypt en una clave KMS de destino, y especificar el ID de la clave de destino en la regla de replicación.",
                    "explanation": "Correcto: Replicar objetos cifrados con SSE-KMS requiere habilitar CRR con S3 Versioning, especificar la clave KMS de destino y otorgar permisos al rol de IAM de replicación para descifrar en el origen y cifrar en el destino."
                },
                {
                    "id": "B",
                    "text": "Cambiar el cifrado en el bucket de origen a texto sin formato, replicar los objetos y volver a cifrarlos manualmente en el bucket de destino.",
                    "explanation": "Incorrecto: Eliminar el cifrado infringe las normas de cumplimiento e introduce una sobrecarga manual innecesaria."
                },
                {
                    "id": "C",
                    "text": "Crear una regla de ciclo de vida de S3 para realizar la transición de objetos a S3 Glacier en eu-west-1 después de 0 días.",
                    "explanation": "Incorrecto: Las reglas de ciclo de vida de S3 transfieren clases de almacenamiento dentro del mismo bucket/región, no entre regiones de AWS."
                },
                {
                    "id": "D",
                    "text": "Utilizar AWS DataSync para ejecutar una tarea de sincronización continua entre los dos puntos de enlace regionales de S3.",
                    "explanation": "Incorrecto: S3 Cross-Region Replication es el mecanismo nativo, automático y sin servidor para la replicación de objetos en S3."
                }
            ],
            "generalExplanation": "Amazon S3 Cross-Region Replication (CRR) requiere S3 Versioning en ambos buckets y permisos explícitos de IAM y KMS cuando los objetos están cifrados con claves SSE-KMS."
        }
    },
    "saa-q027": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Um arquiteto de soluções está projetando uma aplicação de microsserviços de alto tráfego. O tráfego para `/orders` deve ser roteado para uma frota de contêineres de processamento de pedidos, enquanto o tráfego para `/users` deve ser roteado para contêineres de gerenciamento de usuários. Ambas as frotas são executadas em instâncias do Amazon EC2 atrás de um único ponto de entrada público. Qual balanceador de carga deve ser selecionado para rotear o tráfego com base no caminho da URL?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um Network Load Balancer (NLB) com listeners TCP/UDP para distribuir tráfego bruto da Camada 4.",
                    "explanation": "Incorreto: Os Network Load Balancers operam na Camada 4 (camada de transporte) e não podem inspecionar URLs de requisições HTTP ou cabeçalhos de caminho."
                },
                {
                    "id": "B",
                    "text": "Implantar um Gateway Load Balancer (GWLB) para rotear tráfego de firewalls virtuais de terceiros.",
                    "explanation": "Incorreto: Os Gateway Load Balancers são usados para rotear tráfego de rede transparente para firewalls e dispositivos virtuais de terceiros na Camada 3."
                },
                {
                    "id": "C",
                    "text": "Implantar um Classic Load Balancer (CLB) legado com roteamento de listener round-robin básico.",
                    "explanation": "Incorreto: O Classic Load Balancer é legado e não oferece suporte a roteamento baseado em caminho entre múltiplos target groups."
                },
                {
                    "id": "D",
                    "text": "Implantar um Application Load Balancer (ALB) com regras de listener de Camada 7 baseadas em caminho e host.",
                    "explanation": "Correto: Os Application Load Balancers operam na Camada 7 (camada de aplicação) e oferecem suporte nativo a regras de roteamento baseadas em caminho, host, parâmetros de consulta e cabeçalhos HTTP."
                }
            ],
            "generalExplanation": "Os Application Load Balancers (ALB) operam na Camada 7 do modelo OSI e fornecem recursos avançados de roteamento, incluindo roteamento baseado em caminho (`/orders` vs `/users`)."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Un arquitecto de soluciones está diseñando una aplicación de microservicios de alto tráfico. El tráfico hacia `/orders` debe enrutarse a una flota de contenedores de procesamiento de pedidos, mientras que el tráfico hacia `/users` debe enrutarse a contenedores de gestión de usuarios. Ambas flotas se ejecutan en instancias de Amazon EC2 detrás de un único punto de entrada público. ¿Qué balanceador de carga se debe seleccionar para enrutar el tráfico según la ruta URL?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un Network Load Balancer (NLB) con listeners TCP/UDP para distribuir tráfico sin procesar de Capa 4.",
                    "explanation": "Incorrecto: Los Network Load Balancers operan en la Capa 4 (capa de transporte) y no pueden inspeccionar URLs de solicitudes HTTP ni encabezados de ruta."
                },
                {
                    "id": "B",
                    "text": "Implementar un Gateway Load Balancer (GWLB) para enrutar el tráfico de dispositivos de firewall virtuales de terceros.",
                    "explanation": "Incorrecto: Los Gateway Load Balancers se utilizan para enrutar tráfico de red transparente a dispositivos virtuales de terceros en la Capa 3."
                },
                {
                    "id": "C",
                    "text": "Implementar un Classic Load Balancer (CLB) heredado con enrutamiento de listener round-robin básico.",
                    "explanation": "Incorrecto: Classic Load Balancer es una solución heredada y no admite enrutamiento basado en rutas hacia múltiples target groups."
                },
                {
                    "id": "D",
                    "text": "Implementar un Application Load Balancer (ALB) con reglas de listener de Capa 7 basadas en ruta y host.",
                    "explanation": "Correcto: Los Application Load Balancers operan en la Capa 7 (capa de aplicación) y admiten de forma nativa reglas de enrutamiento basadas en ruta, host, parámetros de consulta y encabezados HTTP."
                }
            ],
            "generalExplanation": "Los Application Load Balancers (ALB) operan en la Capa 7 del modelo OSI y proporcionan características avanzadas de enrutamiento, incluido el enrutamiento basado en rutas (`/orders` frente a `/users`)."
        }
    },
    "saa-q028": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma plataforma de pagamento de comércio eletrônico precisa transmitir eventos de confirmação de pedidos simultaneamente para quatro subsistemas de backend independentes: Estoque, Analytics, Envio e Detecção de Fraude. Cada subsistema tem velocidades de processamento diferentes e deve ser capaz de processar mensagens de forma assíncrona, sem impactar os outros subsistemas nem perder eventos se um serviço de trabalhador falhar. Qual padrão arquitetural o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Publicar eventos de pedidos em um tópico do Amazon SNS e inscrever quatro filas separadas do Amazon SQS (uma para cada subsistema) no tópico (padrão SNS Fanout).",
                    "explanation": "Correto: O padrão SNS-to-SQS Fanout permite que uma única mensagem publicada em um tópico SNS seja replicada em várias filas SQS dedicadas para consumo paralelo e desacoplado."
                },
                {
                    "id": "B",
                    "text": "Publicar eventos de pedidos diretamente em uma única fila Standard do Amazon SQS e fazer com que todos os quatro subsistemas façam polling na mesma fila.",
                    "explanation": "Incorreto: Em uma única fila SQS, cada mensagem é consumida por apenas um trabalhador, o que significa que os subsistemas competiriam pelas mensagens em vez de cada um receber uma cópia."
                },
                {
                    "id": "C",
                    "text": "Gravar eventos de pedidos em uma tabela do Amazon RDS MySQL e fazer com que cada subsistema execute consultas periódicas via cron a cada 5 segundos.",
                    "explanation": "Incorreto: Fazer consultas constantes a um banco de dados relacional cria acoplamento forte, severa contenção no banco de dados e gargalos de escalabilidade."
                },
                {
                    "id": "D",
                    "text": "Configurar um Application Load Balancer para duplicar cada solicitação POST para quatro target groups diferentes simultaneamente.",
                    "explanation": "Incorreto: ALBs roteiam solicitações para um único target group por regra, não duplicando payloads para múltiplos target groups simultaneamente."
                }
            ],
            "generalExplanation": "O padrão SNS Fanout cria alta resiliência e desacoplamento: publicar um evento em um tópico do SNS entrega automaticamente uma cópia distinta da mensagem para múltiplas filas inscritas do SQS."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una plataforma de pagos de comercio electrónico necesita transmitir eventos de confirmación de pedidos simultáneamente a cuatro subsistemas de backend independientes: Inventario, Analítica, Envíos y Detección de Fraudes. Cada subsistema tiene velocidades de procesamiento diferentes y debe poder procesar mensajes de forma asíncrona sin afectar a los demás subsistemas ni perder eventos si falla un servicio de trabajo. ¿Qué patrón arquitectónico debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Publicar eventos de pedidos en un tema de Amazon SNS y suscribir cuatro colas separadas de Amazon SQS (una para cada subsistema) al tema (patrón SNS Fanout).",
                    "explanation": "Correcto: El patrón SNS-to-SQS Fanout permite que un único mensaje publicado en un tema de SNS se replique en múltiples colas SQS dedicadas para su consumo paralelo y desacoplado."
                },
                {
                    "id": "B",
                    "text": "Publicar eventos de pedidos directamente en una única cola Standard de Amazon SQS y hacer que los cuatro subsistemas sondeen la misma cola.",
                    "explanation": "Incorrecto: En una sola cola SQS, cada mensaje es consumido por un único trabajador, lo que significa que los subsistemas competirían por los mensajes en lugar de que cada uno reciba una copia."
                },
                {
                    "id": "C",
                    "text": "Escribir eventos de pedidos en una tabla de Amazon RDS MySQL y hacer que cada subsistema ejecute consultas mediante tareas cron cada 5 segundos.",
                    "explanation": "Incorrecto: Sondear una base de datos relacional genera un acoplamiento estrecho, sobrecarga en la base de datos y cuellos de botella de escalado."
                },
                {
                    "id": "D",
                    "text": "Configurar un Application Load Balancer para duplicar cada solicitud POST hacia cuatro target groups diferentes simultáneamente.",
                    "explanation": "Incorrecto: Los ALBs enrutan solicitudes a un único target group por regla, no duplican cargas útiles entre múltiples target groups simultáneamente."
                }
            ],
            "generalExplanation": "El patrón SNS Fanout proporciona alta resiliencia y desacoplamiento: publicar un evento en un tema de SNS entrega automáticamente una copia independiente del mensaje a múltiples colas suscritas de SQS."
        }
    },
    "saa-q029": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa de manufatura opera máquinas virtuais VMware locais executando sistemas ERP de missão crítica. A empresa deseja implementar uma solução econômica de recuperação de desastres (DR) em nuvem para a AWS com um RPO de segundos e um RTO de minutos. A solução deve manter o armazenamento de preparação (staging) de baixo custo continuamente sincronizado e iniciar instâncias completas de computação EC2 apenas durante um desastre ou simulação de teste. Qual serviço da AWS é mais adequado para esse requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Solicitar um dispositivo físico AWS Snowball Edge Storage Optimized para transferência de dados offline em lote.",
                    "explanation": "Incorreto: O Snowball Edge é um dispositivo físico de transporte de dados usado para migrações em lote pontuais, não para replicação de DR contínua em tempo real."
                },
                {
                    "id": "B",
                    "text": "Implantar agentes do AWS Application Discovery Service para coletar dados de inventário de servidores locais.",
                    "explanation": "Incorreto: O Application Discovery Service coleta inventário de servidores e dados de dependência para planejamento de migração, não para execução de DR."
                },
                {
                    "id": "C",
                    "text": "AWS Elastic Disaster Recovery (AWS DRS)",
                    "explanation": "Correto: O AWS DRS replica continuamente o armazenamento em nível de bloco local para uma área de preparação de baixo custo na AWS, permitindo recuperação rápida (RPO em segundos, RTO em minutos) ao inicializar computação completa apenas durante o failover."
                },
                {
                    "id": "D",
                    "text": "AWS DataSync configurado para sincronizar discos locais a cada 24 horas para o S3 Glacier Deep Archive",
                    "explanation": "Incorreto: A sincronização a cada 24 horas para o Glacier gera um RPO de 24 horas e um RTO de horas/dias, falhando no requisito de segundos/minutos."
                }
            ],
            "generalExplanation": "O AWS Elastic Disaster Recovery (DRS) minimiza o tempo de inatividade e a perda de dados fornecendo recuperação rápida e confiável de servidores físicos, virtuais e baseados em nuvem para a AWS usando replicação contínua no nível de bloco."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa de manufactura opera máquinas virtuales VMware locales que ejecutan sistemas ERP de misión crítica. La empresa desea implementar una solución rentable de recuperación ante desastres (DR) en la nube hacia AWS con un RPO de segundos y un RTO de minutos. La solución debe mantener un almacenamiento de preparación (staging) de bajo costo sincronizado continuamente y solo iniciar instancias de cómputo EC2 completas durante un desastre o simulacro de prueba. ¿Qué servicio de AWS se adapta mejor a este requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Solicitar un dispositivo físico AWS Snowball Edge Storage Optimized para transferencia de datos sin conexión masiva.",
                    "explanation": "Incorrecto: Snowball Edge es un dispositivo de transporte físico de datos utilizado para migraciones masivas únicas, no para replicación continua de DR en tiempo real."
                },
                {
                    "id": "B",
                    "text": "Implementar agentes de AWS Application Discovery Service para recopilar datos de inventario de servidores locales.",
                    "explanation": "Incorrecto: Application Discovery Service recopila inventario de servidores y datos de dependencias para la planificación de migraciones, no para la ejecución de DR."
                },
                {
                    "id": "C",
                    "text": "AWS Elastic Disaster Recovery (AWS DRS)",
                    "explanation": "Correcto: AWS DRS replica continuamente el almacenamiento a nivel de bloque local en un área de almacenamiento de bajo costo en AWS, permitiendo una recuperación rápida (RPO en segundos, RTO en minutos) iniciando cómputo completo solo durante el cutover."
                },
                {
                    "id": "D",
                    "text": "AWS DataSync configurado para sincronizar discos locales cada 24 horas con S3 Glacier Deep Archive",
                    "explanation": "Incorrecto: La sincronización cada 24 horas a Glacier produce un RPO de 24 horas y un RTO de horas/días, incumpliendo el requisito de segundos/minutos."
                }
            ],
            "generalExplanation": "AWS Elastic Disaster Recovery (DRS) minimiza el tiempo de inactividad y la pérdida de datos al proporcionar una recuperación rápida y confiable de servidores físicos, virtuales y en la nube hacia AWS mediante replicación continua a nivel de bloque."
        }
    },
    "saa-q030": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma aplicação web hospedada em um EC2 Auto Scaling group atrás de um Application Load Balancer está enfrentando degradação aleatória de desempenho. Uma investigação revela que várias instâncias passam nas verificações básicas de status do EC2, mas apresentam processos de servidor web travados retornando erros HTTP 500 internal server error. Quais ações o arquiteto deve implementar para garantir que instâncias degradadas sejam substituídas automaticamente? (Escolha duas.)",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar o health check do target group do ALB para sondar um endpoint válido de integridade da aplicação (como `/healthz`) e esperar uma resposta HTTP 200.",
                    "explanation": "Correto: Sondar um endpoint de health check dedicado verifica se o processo da aplicação está funcionando corretamente e retornando respostas de sucesso."
                },
                {
                    "id": "B",
                    "text": "Alterar as instâncias do EC2 para instâncias Spot para que sejam encerradas automaticamente em caso de falha.",
                    "explanation": "Incorreto: Instâncias Spot são encerradas quando a AWS recupera capacidade sobressalente, não quando um processo interno da aplicação trava."
                },
                {
                    "id": "C",
                    "text": "Configurar o tipo de verificação de integridade do Auto Scaling group para usar health checks do ELB além das verificações de status do EC2.",
                    "explanation": "Correto: Definir o tipo de health check como 'ELB' faz com que o Auto Scaling substitua instâncias que falham nas verificações de integridade HTTP da aplicação do ALB."
                },
                {
                    "id": "D",
                    "text": "Desativar o Auto Scaling group e gerenciar substituições de instâncias manualmente via AWS Systems Manager.",
                    "explanation": "Incorreto: Intervenção manual degrada a disponibilidade e elimina a resiliência de autocura automatizada."
                },
                {
                    "id": "E",
                    "text": "Aumentar o período de carência (grace period) do health check para 24 horas no Auto Scaling group.",
                    "explanation": "Incorreto: Um período de carência de 24 horas atrasa a detecção de falhas e impede que o Auto Scaling substitua instâncias não íntegras prontamente."
                }
            ],
            "generalExplanation": "Ao definir o tipo de health check do Auto Scaling como 'ELB' e configurar verificações de integridade HTTP do target group em um endpoint da aplicação (por exemplo, `/healthz`), o Auto Scaling substitui automaticamente as instâncias cuja camada de aplicação falhar."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una aplicación web alojada en un grupo de Auto Scaling de EC2 detrás de un Application Load Balancer experimenta una degradación aleatoria del rendimiento. Una investigación revela que varias instancias superan las comprobaciones de estado básicas de EC2 pero tienen procesos de servidor web caídos que devuelven errores HTTP 500 internal server error. ¿Qué acciones debe implementar el arquitecto para garantizar que las instancias degradadas se reemplacen automáticamente? (Seleccione dos.)",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar la comprobación de estado del target group del ALB para consultar un punto de enlace de salud válido de la aplicación (como `/healthz`) y esperar una respuesta HTTP 200.",
                    "explanation": "Correcto: Consultar un endpoint de verificación de salud dedicado confirma que el proceso de la aplicación funciona correctamente y devuelve respuestas satisfactorias."
                },
                {
                    "id": "B",
                    "text": "Cambiar las instancias de EC2 a instancias Spot para que se terminen automáticamente al fallar.",
                    "explanation": "Incorrecto: Las instancias Spot se terminan cuando AWS reclama capacidad excedente, no cuando falla un proceso interno de la aplicación."
                },
                {
                    "id": "C",
                    "text": "Configurar el tipo de comprobación de estado del grupo de Auto Scaling para utilizar comprobaciones de estado de ELB además de las comprobaciones de estado de EC2.",
                    "explanation": "Correcto: Establecer el tipo de comprobación en 'ELB' hace que Auto Scaling reemplace las instancias que no superan las comprobaciones de estado HTTP de la aplicación del ALB."
                },
                {
                    "id": "D",
                    "text": "Deshabilitar el grupo de Auto Scaling y administrar los reemplazos de instancias manualmente mediante AWS Systems Manager.",
                    "explanation": "Incorrecto: La intervención manual degrada la disponibilidad y elimina la resiliencia automatizada de autorrecuperación."
                },
                {
                    "id": "E",
                    "text": "Aumentar el período de gracia de la comprobación de estado a 24 horas en el grupo de Auto Scaling.",
                    "explanation": "Incorrecto: Un período de gracia de 24 horas retrasa la detección de fallas e impide que Auto Scaling reemplace instancias no saludables a tiempo."
                }
            ],
            "generalExplanation": "Al configurar el tipo de comprobación de salud de Auto Scaling en 'ELB' y configurar health checks HTTP en el target group hacia un endpoint de la aplicación (ej. `/healthz`), Auto Scaling reemplaza automáticamente las instancias cuya capa de aplicación falle."
        }
    },
    "saa-q031": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma aplicação online de processamento de empréstimos envolve um fluxo de trabalho em várias etapas: verificação de crédito, validação de documentos, cálculo de risco de fraude e notificação do cliente. Várias etapas exigem tratamento de erros, dependências sequenciais, ramificações condicionais e repetições automáticas com recuo exponencial (exponential backoff). Como o arquiteto deve orquestrar esse fluxo de trabalho distribuído com o mínimo de código personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Escrever um script Python monolítico executado dentro de uma instância do EC2 que usa tarefas cron para invocar funções individuais.",
                    "explanation": "Incorreto: Scripts monolíticos no EC2 introduzem pontos únicos de falha e código complexo de gerenciamento de estado."
                },
                {
                    "id": "B",
                    "text": "Encadear funções do Lambda fazendo com que cada função invoque a próxima função de forma síncrona por meio do AWS SDK.",
                    "explanation": "Incorreto: Encadear invocações síncronas do Lambda aumenta a latência, gera risco de propagação de tempo limite (timeout) e cria um tratamento de erros frágil."
                },
                {
                    "id": "C",
                    "text": "Usar máquinas de estado do AWS Step Functions (State Machines) para coordenar visualmente as etapas do fluxo de trabalho, gerenciar o estado e lidar com repetições automáticas e blocos de captura de erros (catch blocks).",
                    "explanation": "Correto: O AWS Step Functions é um orquestrador visual de fluxo de trabalho de baixo código desenvolvido especificamente para coordenar microsserviços distribuídos e gerenciar lógica complexa de ramificação e repetição."
                },
                {
                    "id": "D",
                    "text": "Armazenar o estado em um arquivo de texto no Amazon S3 e fazer com que funções Lambda consultem o bucket do S3 a cada minuto.",
                    "explanation": "Incorreto: Fazer polling no S3 para orquestração de estado introduz latência severa, condições de corrida (race conditions) e custos desnecessários."
                }
            ],
            "generalExplanation": "O AWS Step Functions fornece fluxos de trabalho de máquina de estado sem servidor para coordenar funções do Lambda e serviços da AWS com lógica integrada de repetição, tratamento de erros e execução paralela."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una aplicación de procesamiento de préstamos en línea implica un flujo de trabajo de varios pasos: verificación de crédito, validación de documentos, cálculo de riesgo de fraude y notificación al cliente. Varios pasos requieren manejo de errores, dependencias secuenciales, ramificaciones condicionales y reintentos automáticos con retroceso exponencial (exponential backoff). ¿Cómo debe orquestar el arquitecto este flujo de trabajo distribuido con el mínimo código personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Escribir un script de Python monolítico que se ejecute dentro de una instancia de EC2 y use tareas cron para invocar funciones individuales.",
                    "explanation": "Incorrecto: Los scripts monolíticos en EC2 introducen puntos únicos de falla y un código de gestión de estado complejo."
                },
                {
                    "id": "B",
                    "text": "Encadenar funciones Lambda haciendo que cada función invoque la siguiente función de forma síncrona a través del SDK de AWS.",
                    "explanation": "Incorrecto: Encadenar invocaciones síncronas de Lambda incrementa la latencia, arriesga la propagación de tiempos de espera y crea un manejo de errores frágil."
                },
                {
                    "id": "C",
                    "text": "Utilizar máquinas de estado de AWS Step Functions (State Machines) para coordinar visualmente los pasos del flujo de trabajo, administrar el estado y manejar reintentos automáticos y bloques de captura de errores (catch blocks).",
                    "explanation": "Correcto: AWS Step Functions es un orquestador visual de flujos de trabajo de poco código creado específicamente para coordinar microservicios distribuidos y manejar lógica compleja de bifurcación y reintentos."
                },
                {
                    "id": "D",
                    "text": "Almacenar el estado en un archivo de texto en Amazon S3 y hacer que las funciones Lambda sondeen el bucket de S3 cada minuto.",
                    "explanation": "Incorrecto: Sondear S3 para la orquestación de estados introduce latencia severa, condiciones de carrera y costos innecesarios."
                }
            ],
            "generalExplanation": "AWS Step Functions proporciona flujos de trabajo de máquinas de estado sin servidor para coordinar funciones Lambda y servicios de AWS con reintentos integrados, manejo de errores y ejecución paralela."
        }
    },
    "saa-q032": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa de software deseja construir uma arquitetura orientada a eventos na qual os microsserviços se comuniquem por meio de eventos JSON fracamente acoplados. A solução deve suportar filtragem de eventos com base nos valores de atributos JSON, roteamento de eventos de parceiros SaaS (como Zendesk e Datadog) e entrega de eventos para múltiplos destinos, incluindo AWS Lambda e Amazon SQS. Qual serviço deve ser usado como o barramento central de eventos?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar o Amazon EventBridge como o barramento de eventos central com filtragem de regras JSON baseada em conteúdo.",
                    "explanation": "Correto: O Amazon EventBridge é um barramento de eventos sem servidor que suporta filtragem baseada em conteúdo JSON, integrações nativas com parceiros SaaS e roteamento para mais de 20 destinos da AWS."
                },
                {
                    "id": "B",
                    "text": "Amazon Simple Queue Service (Amazon SQS)",
                    "explanation": "Incorreto: O SQS é uma fila de mensagens ponto a ponto, não um barramento de roteamento de eventos com integrações de parceiros SaaS e filtragem de conteúdo."
                },
                {
                    "id": "C",
                    "text": "Implantar um cluster do Amazon Kinesis Data Streams para capturar registros de dados ordenados em tempo real.",
                    "explanation": "Incorreto: O Kinesis foi projetado para streaming massivo de dados ordenados em tempo real e ingestão de logs, e não para correspondência de padrões em barramento de eventos."
                },
                {
                    "id": "D",
                    "text": "Implantar um serviço gerenciado GraphQL do AWS AppSync com assinaturas WebSocket em tempo real.",
                    "explanation": "Incorreto: O AWS AppSync é um serviço gerenciado de API GraphQL, não um barramento central de eventos."
                }
            ],
            "generalExplanation": "O Amazon EventBridge facilita a criação de arquiteturas orientadas a eventos conectando aplicações com dados de uma variedade de fontes e roteando-os para destinos da AWS com filtragem de conteúdo."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa de software desea crear una arquitectura basada en eventos en la que los microservicios se comuniquen a través de eventos JSON débilmente acoplados. La solución debe admitir el filtrado de eventos según los valores de atributos JSON, el enrutamiento de eventos desde socios de SaaS (como Zendesk y Datadog) y la entrega de eventos a múltiples destinos, incluidos AWS Lambda y Amazon SQS. ¿Qué servicio se debe utilizar como bus central de eventos?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar Amazon EventBridge como el bus central de eventos con filtrado de reglas JSON basado en contenido.",
                    "explanation": "Correcto: Amazon EventBridge es un bus de eventos sin servidor que admite filtrado basado en contenido JSON, integraciones nativas con socios SaaS y enrutamiento a más de 20 destinos de AWS."
                },
                {
                    "id": "B",
                    "text": "Amazon Simple Queue Service (Amazon SQS)",
                    "explanation": "Incorrecto: SQS es una cola de mensajes punto a punto, no un bus de enrutamiento de eventos con integraciones de socios SaaS y filtrado de contenido."
                },
                {
                    "id": "C",
                    "text": "Implementar un clúster de Amazon Kinesis Data Streams para capturar registros de datos ordenados en tiempo real.",
                    "explanation": "Incorrecto: Kinesis está diseñado para la ingesta y transmisión masiva de datos ordenados en tiempo real, no para coincidencia de patrones en un bus de eventos."
                },
                {
                    "id": "D",
                    "text": "Implementar un servicio GraphQL administrado de AWS AppSync con suscripciones WebSocket en tiempo real.",
                    "explanation": "Incorrecto: AWS AppSync es un servicio administrado de APIs GraphQL, no un bus de eventos central."
                }
            ],
            "generalExplanation": "Amazon EventBridge facilita la creación de arquitecturas basadas en eventos al conectar aplicaciones con datos de diversas fuentes y enrutarlos a destinos de AWS con filtrado de contenido."
        }
    },
    "saa-q033": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa de jogos multijogador em tempo real hospeda servidores de jogos em regiões da AWS em us-east-1 e ap-southeast-1. Jogadores de todo o mundo relatam conectividade instável e alta latência ao se conectarem pelo roteamento padrão da internet pública. O arquiteto precisa fornecer endereços IP Anycast estáticos para clientes de jogos e rotear o tráfego UDP dos jogadores pela rede global de alta velocidade da AWS até o servidor regional saudável mais próximo. Qual serviço da AWS deve ser implantado?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar o AWS Global Accelerator com endereços IP Anycast estáticos roteando sobre a rede global da AWS.",
                    "explanation": "Correto: O AWS Global Accelerator fornece endereços IP Anycast estáticos e roteia o tráfego TCP/UDP diretamente na rede global da AWS para o endpoint regional ideal com failover por verificação de integridade."
                },
                {
                    "id": "B",
                    "text": "Criar um hub do AWS Transit Gateway para rotear o tráfego de rede inter-VPC entre contas.",
                    "explanation": "Incorreto: O Transit Gateway conecta VPCs e redes corporativas locais, não dispositivos de clientes públicos executando jogos multijogador."
                },
                {
                    "id": "C",
                    "text": "Roteamento por geoproximidade do Amazon Route 53 sem endpoints",
                    "explanation": "Incorreto: O roteamento DNS do Route 53 apenas resolve nomes de domínio para IPs e não fornece IPs Anycast nem otimiza os saltos de internet do tráfego UDP ativo."
                },
                {
                    "id": "D",
                    "text": "Implantar uma distribuição do Amazon CloudFront para armazenar em cache conteúdo web estático e dinâmico em locais de borda.",
                    "explanation": "Incorreto: O CloudFront é uma CDN projetada para tráfego HTTP/HTTPS/WebSockets, não para tráfego UDP arbitrário de jogos."
                }
            ],
            "generalExplanation": "O AWS Global Accelerator usa endereços IP estáticos Anycast para receber o tráfego em edge locations e rotear pacotes TCP/UDP pela rede global de alta velocidade da AWS para endpoints em qualquer região."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa de videojuegos multijugador en tiempo real aloja servidores de juegos en las regiones de AWS us-east-1 y ap-southeast-1. Jugadores de todo el mundo informan conectividad inconsistente y alta latencia al conectarse a través del enrutamiento público de internet. El arquitecto necesita proporcionar direcciones IP Anycast estáticas para los clientes de juegos y enrutar el tráfico UDP de los jugadores a través de la red troncal global de AWS hacia el servidor regional saludable más cercano. ¿Qué servicio de AWS se debe implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar AWS Global Accelerator con direcciones IP Anycast estáticas que enrutan a través de la red global de AWS.",
                    "explanation": "Correcto: AWS Global Accelerator proporciona direcciones IP Anycast estáticas y enruta el tráfico TCP/UDP directamente sobre la red global de AWS hacia el punto de enlace regional óptimo con conmutación por error basada en comprobaciones de salud."
                },
                {
                    "id": "B",
                    "text": "Crear un concentrador AWS Transit Gateway para enrutar el tráfico de red inter-VPC entre cuentas.",
                    "explanation": "Incorrecto: Transit Gateway conecta VPCs y redes corporativas locales, no dispositivos de clientes públicos que ejecutan juegos multijugador."
                },
                {
                    "id": "C",
                    "text": "Enrutamiento por geoproximidad de Amazon Route 53 sin puntos de enlace",
                    "explanation": "Incorrecto: El enrutamiento DNS de Route 53 solo resuelve nombres de dominio en direcciones IP y no proporciona IPs Anycast ni enmascara saltos de internet para el tráfico UDP activo."
                },
                {
                    "id": "D",
                    "text": "Implementar una distribución de Amazon CloudFront para almacenar en caché contenido web estático y dinámico en ubicaciones perimetrales.",
                    "explanation": "Incorrecto: CloudFront es una CDN diseñada para contenido HTTP/HTTPS/WebSockets, no para tráfico UDP arbitrario de juegos."
                }
            ],
            "generalExplanation": "AWS Global Accelerator utiliza direcciones IP estáticas Anycast para recibir tráfico en ubicaciones perimetrales y enrutar paquetes TCP/UDP a través de la red global de alta velocidad de AWS hacia endpoints en cualquier región."
        }
    }
}
