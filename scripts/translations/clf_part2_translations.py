"""
Translations for AWS Certified Cloud Practitioner (CLF-C02) exam.
Questions: clf-q034 through clf-q065 (Part 2)
Languages: Portuguese (PT-BR) and Spanish (ES)
"""

TRANSLATIONS = {
    "clf-q034": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço da AWS permite armazenar, recuperar e rotacionar automaticamente senhas de banco de dados, chaves de API e outros segredos de forma segura ao longo de todo o ciclo de vida deles?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Secrets Manager",
                    "explanation": "Correto: O AWS Secrets Manager ajuda a proteger os segredos necessários para acessar seus aplicativos e serviços, contando com rotação automática para bancos de dados RDS."
                },
                {
                    "id": "B",
                    "text": "AWS IAM Access Analyzer",
                    "explanation": "Incorreto: O IAM Access Analyzer analisa políticas de acesso a recursos para identificar acessos públicos ou entre contas."
                },
                {
                    "id": "C",
                    "text": "AWS Shield Standard",
                    "explanation": "Incorreto: O Shield Standard oferece proteção contra ataques DDoS."
                },
                {
                    "id": "D",
                    "text": "Amazon CloudWatch Logs",
                    "explanation": "Incorreto: O CloudWatch Logs armazena fluxos de logs de sistemas e aplicativos."
                }
            ],
            "generalExplanation": "O AWS Secrets Manager permite substituir credenciais codificadas diretamente na aplicação (hardcoded) por uma chamada de API e rotacionar automaticamente as credenciais de banco de dados."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de AWS le permite almacenar, recuperar y rotar automáticamente de forma segura contraseñas de bases de datos, claves de API y otros secretos a lo largo de su ciclo de vida?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Secrets Manager",
                    "explanation": "Correcto: AWS Secrets Manager le ayuda a proteger los secretos necesarios para acceder a sus aplicaciones y servicios, ofreciendo rotación automática para bases de datos RDS."
                },
                {
                    "id": "B",
                    "text": "AWS IAM Access Analyzer",
                    "explanation": "Incorrecto: IAM Access Analyzer revisa las políticas de acceso a recursos para identificar el acceso público o entre cuentas."
                },
                {
                    "id": "C",
                    "text": "AWS Shield Standard",
                    "explanation": "Incorrecto: Shield Standard proporciona protección contra ataques DDoS."
                },
                {
                    "id": "D",
                    "text": "Amazon CloudWatch Logs",
                    "explanation": "Incorrecto: CloudWatch Logs almacena flujos de registros (logs) de aplicaciones y del sistema."
                }
            ],
            "generalExplanation": "AWS Secrets Manager le permite reemplazar credenciales codificadas en el código fuente (hardcoded) por una llamada a la API y rotar automáticamente las credenciales de bases de datos."
        }
    },
    "clf-q035": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço da AWS ajuda as organizações a auditar continuamente o uso da AWS para simplificar a avaliação de riscos e coletar evidências automaticamente para conformidade com regulamentações como GDPR, HIPAA e PCI-DSS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorreto: O Direct Connect é uma linha de rede física dedicada."
                },
                {
                    "id": "B",
                    "text": "AWS Audit Manager",
                    "explanation": "Correto: O AWS Audit Manager ajuda a auditar continuamente o uso da AWS para simplificar a avaliação de riscos e conformidade por meio da coleta automatizada de evidências."
                },
                {
                    "id": "C",
                    "text": "Amazon Athena",
                    "explanation": "Incorreto: O Athena é um serviço de consultas SQL interativas para dados no S3."
                },
                {
                    "id": "D",
                    "text": "AWS Billing Conductor",
                    "explanation": "Incorreto: O Billing Conductor personaliza taxas de faturamento e faturas pro forma para parceiros e empresas."
                }
            ],
            "generalExplanation": "O AWS Audit Manager mapeia continuamente o uso da AWS em relação a controles de conformidade e coleta automaticamente evidências para auditorias regulatórias."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de AWS ayuda a las organizaciones a auditar continuamente su uso de AWS para simplificar la evaluación de riesgos y recopilar automáticamente evidencias de cumplimiento de normativas como GDPR, HIPAA y PCI-DSS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorrecto: Direct Connect es una línea de conexión de red física y dedicada."
                },
                {
                    "id": "B",
                    "text": "AWS Audit Manager",
                    "explanation": "Correcto: AWS Audit Manager le ayuda a auditar continuamente su uso de AWS para simplificar la evaluación de riesgos y cumplimiento mediante la recopilación automatizada de evidencias."
                },
                {
                    "id": "C",
                    "text": "Amazon Athena",
                    "explanation": "Incorrecto: Athena es un servicio de consultas interactivas mediante SQL para datos almacenados en S3."
                },
                {
                    "id": "D",
                    "text": "AWS Billing Conductor",
                    "explanation": "Incorrecto: Billing Conductor personaliza tarifas de facturación y facturas proforma para socios y empresas."
                }
            ],
            "generalExplanation": "AWS Audit Manager mapea continuamente su uso de AWS con los controles de cumplimiento y recopila evidencia de manera automática para auditorías regulatorias."
        }
    },
    "clf-q036": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "O que é uma Região AWS (AWS Region)?",
            "options": [
                {
                    "id": "A",
                    "text": "Um agrupamento lógico de usuários do IAM dentro de um único departamento corporativo.",
                    "explanation": "Incorreto: Isso descreve um Grupo de Usuários do IAM (IAM User Group)."
                },
                {
                    "id": "B",
                    "text": "Uma área geográfica separada no mundo que contém múltiplas Zonas de Disponibilidade isoladas e fisicamente separadas.",
                    "explanation": "Correto: Uma Região AWS é uma localização geográfica física no mundo contendo múltiplas (no mínimo 3) Zonas de Disponibilidade isoladas e fisicamente separadas."
                },
                {
                    "id": "C",
                    "text": "Um edifício físico de data center contendo racks de computação.",
                    "explanation": "Incorreto: Um único edifício de data center faz parte de uma Zona de Disponibilidade, e não de uma Região inteira."
                },
                {
                    "id": "D",
                    "text": "Um local de borda global usado exclusivamente para armazenar em cache imagens de sites estáticos.",
                    "explanation": "Incorreto: Isso descreve um Local de Borda / Ponto de Presença (Edge Location / PoP)."
                }
            ],
            "generalExplanation": "Uma Região AWS é uma área geográfica separada composta por múltiplas Zonas de Disponibilidade fisicamente isoladas, interconectadas por meio de links de fibra redundantes de baixa latência."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué es una Región de AWS (AWS Region)?",
            "options": [
                {
                    "id": "A",
                    "text": "Una agrupación lógica de usuarios de IAM dentro de un solo departamento corporativo.",
                    "explanation": "Incorrecto: Eso describe un Grupo de Usuarios de IAM (IAM User Group)."
                },
                {
                    "id": "B",
                    "text": "Un área geográfica independiente en el mundo que contiene múltiples Zonas de Disponibilidad aisladas y físicamente separadas.",
                    "explanation": "Correcto: Una Región de AWS es una ubicación geográfica física en el mundo que contiene múltiples (al menos 3) Zonas de Disponibilidad aisladas y físicamente separadas."
                },
                {
                    "id": "C",
                    "text": "Un edificio físico de centro de datos que contiene racks de servidores.",
                    "explanation": "Incorrecto: Un edificio individual de centro de datos forma parte de una Zona de Disponibilidad, no de una Región completa."
                },
                {
                    "id": "D",
                    "text": "Una ubicación de borde global utilizada exclusivamente para almacenar en caché imágenes de sitios web estáticos.",
                    "explanation": "Incorrecto: Eso describe una Ubicación de Borde / Punto de Presencia (Edge Location / PoP)."
                }
            ],
            "generalExplanation": "Una Región de AWS es un área geográfica independiente que consta de múltiples Zonas de Disponibilidad físicamente aisladas y conectadas mediante fibra redundante de baja latencia."
        }
    },
    "clf-q037": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "O que é uma Zona de Disponibilidade (Availability Zone - AZ) na Infraestrutura Global da AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Um ponto de entrega de conteúdo global hospedado em uma área metropolitana.",
                    "explanation": "Incorreto: Isso descreve um Local de Borda (Edge Location)."
                },
                {
                    "id": "B",
                    "text": "Uma coleção de contas da AWS vinculadas sob faturamento consolidado.",
                    "explanation": "Incorreto: Isso descreve o AWS Organizations."
                },
                {
                    "id": "C",
                    "text": "Um ou mais data centers distintos com alimentação de energia, rede e conectividade redundantes localizados em uma Região AWS.",
                    "explanation": "Correto: Uma Zona de Disponibilidade consiste em um ou mais data centers distintos com energia, refrigeração e segurança física independentes."
                },
                {
                    "id": "D",
                    "text": "Uma conexão de rede virtual privada entre data centers on-premises e a AWS.",
                    "explanation": "Incorreto: Isso descreve a AWS Site-to-Site VPN."
                }
            ],
            "generalExplanation": "Uma Zona de Disponibilidade (AZ) é composta por um ou mais data centers distintos com fornecimento redundante de energia, rede e conectividade em uma Região AWS."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué es una Zona de Disponibilidad (Availability Zone - AZ) en la Infraestructura Global de AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Un punto de enlace global de entrega de contenido alojado en una ciudad metropolitana.",
                    "explanation": "Incorrecto: Eso describe una Ubicación de Borde (Edge Location)."
                },
                {
                    "id": "B",
                    "text": "Una colección de cuentas de AWS vinculadas bajo una facturación consolidada.",
                    "explanation": "Incorrecto: Eso describe AWS Organizations."
                },
                {
                    "id": "C",
                    "text": "Uno o más centros de datos independientes con energía, redes y conectividad redundantes ubicados dentro de una Región de AWS.",
                    "explanation": "Correcto: Una Zona de Disponibilidad consta de uno o más centros de datos independientes con energía, refrigeración y seguridad física autónomas."
                },
                {
                    "id": "D",
                    "text": "Una conexión de red privada virtual entre centros de datos locales (on-premises) y AWS.",
                    "explanation": "Incorrecto: Eso describe AWS Site-to-Site VPN."
                }
            ],
            "generalExplanation": "Una Zona de Disponibilidad (AZ) es uno o más centros de datos independientes con redundancia de energía, conectividad y redes dentro de una Región de AWS."
        }
    },
    "clf-q038": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual componente da infraestrutura da AWS é utilizado pelo Amazon CloudFront para entregar conteúdo a usuários finais em todo o mundo com menor latência, armazenando dados em cache mais próximos dos visualizadores?",
            "options": [
                {
                    "id": "A",
                    "text": "Locais de Borda / Pontos de Presença (Edge Locations)",
                    "explanation": "Correto: Os Locais de Borda são pontos de presença distribuídos globalmente usados por serviços como Amazon CloudFront e Route 53 para armazenar conteúdo em cache e reduzir a latência para os usuários finais."
                },
                {
                    "id": "B",
                    "text": "AWS Outposts",
                    "explanation": "Incorreto: O Outposts leva hardware da AWS para os data centers locais (on-premises) dos clientes."
                },
                {
                    "id": "C",
                    "text": "Virtual Private Gateways",
                    "explanation": "Incorreto: Os Virtual Private Gateways encerram conexões VPN na extremidade da VPC."
                },
                {
                    "id": "D",
                    "text": "Volumes do Elastic Block Store",
                    "explanation": "Incorreto: Volumes do EBS são opções de armazenamento em bloco virtual para instâncias EC2."
                }
            ],
            "generalExplanation": "Os Locais de Borda (Edge Locations) são pontos distribuídos nas principais cidades do mundo que armazenam cópias de conteúdo em cache para entregá-lo aos espectadores com a menor latência possível."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué componente de la infraestructura de AWS utiliza Amazon CloudFront para entregar contenido a usuarios finales de todo el mundo con menor latencia al almacenar datos en caché más cerca de los espectadores?",
            "options": [
                {
                    "id": "A",
                    "text": "Ubicaciones de Borde / Puntos de Presencia (Edge Locations)",
                    "explanation": "Correcto: Las Ubicaciones de Borde son puntos de presencia distribuidos globalmente que utilizan servicios como Amazon CloudFront y Route 53 para almacenar contenido en caché y reducir la latencia de los usuarios finales."
                },
                {
                    "id": "B",
                    "text": "AWS Outposts",
                    "explanation": "Incorrecto: Outposts lleva hardware de AWS a los centros de datos locales (on-premises) del cliente."
                },
                {
                    "id": "C",
                    "text": "Virtual Private Gateways",
                    "explanation": "Incorrecto: Los Virtual Private Gateways terminan conexiones VPN en el borde de la VPC."
                },
                {
                    "id": "D",
                    "text": "Volúmenes de Elastic Block Store",
                    "explanation": "Incorrecto: Los volúmenes EBS son almacenamiento de bloques virtual para instancias EC2."
                }
            ],
            "generalExplanation": "Las Ubicaciones de Borde (Edge Locations) son puntos de enlace ubicados en las principales ciudades del mundo que almacenan en caché copias de contenido para entregarlas a los usuarios con la menor latencia posible."
        }
    },
    "clf-q039": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Uma empresa precisa executar a infraestrutura da AWS e serviços nativos da AWS dentro do seu próprio data center corporativo local (on-premises) para atender a requisitos rigorosos de residência de dados. Qual serviço da AWS entrega racks de hardware totalmente gerenciados pela AWS nas instalações locais do cliente?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorreto: O Direct Connect é uma conexão de rede dedicada, não um hardware físico de rack de computação/armazenamento."
                },
                {
                    "id": "B",
                    "text": "AWS Outposts",
                    "explanation": "Correto: O AWS Outposts leva serviços nativos, infraestrutura e modelos operacionais da AWS para praticamente qualquer data center, espaço de colocation ou instalação on-premises de clientes."
                },
                {
                    "id": "C",
                    "text": "Amazon Lightsail",
                    "explanation": "Incorreto: O Lightsail é um servidor virtual privado (VPS) fácil de usar na nuvem."
                },
                {
                    "id": "D",
                    "text": "AWS Snowmobile",
                    "explanation": "Incorreto: O Snowmobile é um contêiner de transporte em escala de exabytes para migração de dados em lote única."
                }
            ],
            "generalExplanation": "O AWS Outposts estende a infraestrutura, os serviços, as APIs e as ferramentas da AWS para as instalações do cliente, proporcionando uma experiência híbrida verdadeiramente consistente."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "Una empresa requiere ejecutar infraestructura de AWS y servicios nativos de AWS dentro de su propio centro de datos corporativo local (on-premises) para cumplir con estrictos requisitos de residencia de datos. ¿Qué servicio de AWS entrega racks de hardware de AWS totalmente administrados en las instalaciones del cliente?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorrecto: Direct Connect es una línea de red dedicada, no hardware físico de racks de cómputo/almacenamiento."
                },
                {
                    "id": "B",
                    "text": "AWS Outposts",
                    "explanation": "Correcto: AWS Outposts lleva los servicios nativos, la infraestructura y los modelos operativos de AWS a prácticamente cualquier centro de datos, espacio de colocación o instalación local del cliente."
                },
                {
                    "id": "C",
                    "text": "Amazon Lightsail",
                    "explanation": "Incorrecto: Lightsail es un servidor privado virtual (VPS) fácil de usar en la nube."
                },
                {
                    "id": "D",
                    "text": "AWS Snowmobile",
                    "explanation": "Incorrecto: Snowmobile es un contenedor de transporte a escala de exabytes para migración masiva de datos puntual."
                }
            ],
            "generalExplanation": "AWS Outposts extiende la infraestructura, los servicios, las API y las herramientas de AWS a las instalaciones del cliente para brindar una experiencia híbrida verdaderamente coherente."
        }
    },
    "clf-q040": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço de computação da AWS permite executar código em resposta a eventos sem provisionar, gerenciar ou aplicar patches em servidores virtuais, cobrando apenas pelo tempo de computação consumido na escala de milissegundos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Lightsail",
                    "explanation": "Incorreto: O Lightsail provisiona máquinas virtuais pré-configuradas cobradas com base em uma taxa mensal."
                },
                {
                    "id": "B",
                    "text": "Amazon EC2",
                    "explanation": "Incorreto: O EC2 requer o provisionamento e o gerenciamento de servidores virtuais."
                },
                {
                    "id": "C",
                    "text": "AWS Lambda",
                    "explanation": "Correto: O AWS Lambda é um serviço de computação sem servidor (serverless) e orientado a eventos que executa código automaticamente em resposta a gatilhos e cobra apenas pela duração da execução em milissegundos."
                },
                {
                    "id": "D",
                    "text": "AWS Elastic Beanstalk",
                    "explanation": "Incorreto: O Elastic Beanstalk implanta e gerencia instâncias EC2 e balanceadores de carga subjacentes."
                }
            ],
            "generalExplanation": "O AWS Lambda é um serviço de computação sem servidor que permite executar código sem provisionar ou gerenciar servidores, escalando automaticamente de acordo com o uso."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de cómputo de AWS le permite ejecutar código en respuesta a eventos sin aprovisionar, administrar o aplicar parches a servidores virtuales, cobrando únicamente por el tiempo de cómputo consumido al milisegundo?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Lightsail",
                    "explanation": "Incorrecto: Lightsail aprovisiona máquinas virtuales preconfiguradas que se facturan mediante una tarifa mensual."
                },
                {
                    "id": "B",
                    "text": "Amazon EC2",
                    "explanation": "Incorrecto: EC2 requiere aprovisionar y administrar servidores virtuales."
                },
                {
                    "id": "C",
                    "text": "AWS Lambda",
                    "explanation": "Correcto: AWS Lambda es un servicio de cómputo sin servidor (serverless) basado en eventos que ejecuta código automáticamente en respuesta a desencadenadores y cobra únicamente por la duración de la ejecución en milisegundos."
                },
                {
                    "id": "D",
                    "text": "AWS Elastic Beanstalk",
                    "explanation": "Incorrecto: Elastic Beanstalk despliega y administra instancias EC2 y balanceadores de carga subyacentes."
                }
            ],
            "generalExplanation": "AWS Lambda es un servicio de cómputo sin servidor que le permite ejecutar código sin necesidad de aprovisionar ni administrar servidores, escalando automáticamente según la demanda."
        }
    },
    "clf-q041": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Uma empresa deseja executar contêineres Docker na nuvem usando o Amazon ECS ou o Amazon EKS sem precisar gerenciar, configurar ou dimensionar as instâncias de host EC2 subjacentes. Qual mecanismo de computação sem servidor (serverless) ela deve escolher?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon EC2 Spot Fleet",
                    "explanation": "Incorreto: As frotas EC2 Spot exigem o gerenciamento da escalabilidade das instâncias EC2 e a aplicação de patches no sistema operacional."
                },
                {
                    "id": "B",
                    "text": "AWS Batch",
                    "explanation": "Incorreto: O AWS Batch gerencia trabalhos de computação em lote, mas utiliza EC2 ou Fargate nos bastidores."
                },
                {
                    "id": "C",
                    "text": "AWS Storage Gateway",
                    "explanation": "Incorreto: O Storage Gateway é um serviço de armazenamento híbrido, não um mecanismo de computação de contêineres."
                },
                {
                    "id": "D",
                    "text": "AWS Fargate",
                    "explanation": "Correto: O AWS Fargate é um mecanismo de computação sem servidor e pré-pago para contêineres compatível com Amazon ECS e Amazon EKS, eliminando a necessidade de gerenciar instâncias EC2."
                }
            ],
            "generalExplanation": "O AWS Fargate é um mecanismo de computação sem servidor para contêineres que permite executar contêineres ECS ou EKS sem precisar gerenciar a infraestrutura subjacente do EC2."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "Una empresa desea ejecutar contenedores Docker en la nube mediante Amazon ECS o Amazon EKS sin tener que administrar, configurar o escalar las instancias host de EC2 subyacentes. ¿Qué motor de cómputo sin servidor (serverless) deberían elegir?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon EC2 Spot Fleet",
                    "explanation": "Incorrecto: Las flotas Spot de EC2 requieren administrar el escalado de instancias EC2 y los parches del sistema operativo."
                },
                {
                    "id": "B",
                    "text": "AWS Batch",
                    "explanation": "Incorrecto: AWS Batch gestiona trabajos de cómputo por lotes, pero utiliza EC2 o Fargate internamente."
                },
                {
                    "id": "C",
                    "text": "AWS Storage Gateway",
                    "explanation": "Incorrecto: Storage Gateway es un servicio de almacenamiento híbrido, no un motor de cómputo de contenedores."
                },
                {
                    "id": "D",
                    "text": "AWS Fargate",
                    "explanation": "Correcto: AWS Fargate es un motor de cómputo sin servidor y de pago por uso para contenedores que funciona con Amazon ECS y Amazon EKS, eliminando la necesidad de administrar instancias EC2."
                }
            ],
            "generalExplanation": "AWS Fargate es un motor de cómputo sin servidor para contenedores que le permite ejecutar contenedores ECS o EKS sin administrar la infraestructura subyacente de EC2."
        }
    },
    "clf-q042": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual classe de armazenamento do Amazon S3 foi projetada para arquivamento de longo prazo de dados de conformidade raramente acessados, aceita tempos de recuperação de 12 a 48 horas e oferece o MENOR custo absoluto de armazenamento na AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Glacier Deep Archive",
                    "explanation": "Correto: O Amazon S3 Glacier Deep Archive é a classe de armazenamento de menor custo do S3, projetada para retenção a longo prazo de dados acessados uma ou duas vezes por ano, com tempos de recuperação de 12 a 48 horas."
                },
                {
                    "id": "B",
                    "text": "Amazon S3 Standard-Infrequent Access (S3 Standard-IA)",
                    "explanation": "Incorreto: O Standard-IA destina-se a dados acessados com pouca frequência, mas que exigem recuperação em milissegundos."
                },
                {
                    "id": "C",
                    "text": "Amazon S3 Standard",
                    "explanation": "Incorreto: O S3 Standard foi projetado para dados acessados com frequência."
                },
                {
                    "id": "D",
                    "text": "Amazon S3 Express One Zone",
                    "explanation": "Incorreto: O Express One Zone é um armazenamento de alto desempenho com latência de milissegundos de um dígito."
                }
            ],
            "generalExplanation": "O Amazon S3 Glacier Deep Archive oferece o armazenamento de menor custo na nuvem para retenção de conformidade a longo prazo, com tempos de recuperação entre 12 e 48 horas."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué clase de almacenamiento de Amazon S3 está diseñada para el archivado a largo plazo de datos de cumplimiento a los que rara vez se accede, admite tiempos de recuperación de 12 a 48 horas y ofrece el costo de almacenamiento absolutamente más BAJO en AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Glacier Deep Archive",
                    "explanation": "Correcto: Amazon S3 Glacier Deep Archive es la clase de almacenamiento de menor costo de S3, diseñada para la retención a largo plazo de datos a los que se accede una o dos veces al año con tiempos de recuperación de 12 a 48 horas."
                },
                {
                    "id": "B",
                    "text": "Amazon S3 Standard-Infrequent Access (S3 Standard-IA)",
                    "explanation": "Incorrecto: Standard-IA es para datos a los que se accede con poca frecuencia pero que requieren recuperación en milisegundos."
                },
                {
                    "id": "C",
                    "text": "Amazon S3 Standard",
                    "explanation": "Incorrecto: S3 Standard está diseñado para datos a los que se accede con frecuencia."
                },
                {
                    "id": "D",
                    "text": "Amazon S3 Express One Zone",
                    "explanation": "Incorrecto: Express One Zone es almacenamiento de alto rendimiento con latencias de un solo dígito de milisegundo."
                }
            ],
            "generalExplanation": "Amazon S3 Glacier Deep Archive proporciona el almacenamiento de menor costo en la nube para la retención de datos por cumplimiento normativo a largo plazo con tiempos de recuperación de entre 12 y 48 horas."
        }
    },
    "clf-q043": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço de armazenamento da AWS fornece volumes de armazenamento persistente em nível de bloco de alto desempenho projetados para serem conectados a uma instância do Amazon EC2 em execução como um disco rígido virtual?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB",
                    "explanation": "Incorreto: O DynamoDB é um banco de dados NoSQL, não um armazenamento em bloco."
                },
                {
                    "id": "B",
                    "text": "AWS Snowball",
                    "explanation": "Incorreto: O Snowball é um dispositivo físico de transporte de dados de hardware."
                },
                {
                    "id": "C",
                    "text": "Amazon Elastic Block Store (Amazon EBS)",
                    "explanation": "Correto: O Amazon EBS fornece volumes de armazenamento em bloco persistente para uso com instâncias do Amazon EC2."
                },
                {
                    "id": "D",
                    "text": "Amazon S3 Glacier",
                    "explanation": "Incorreto: O S3 Glacier é um armazenamento de objetos para arquivamento."
                }
            ],
            "generalExplanation": "O Amazon Elastic Block Store (EBS) fornece volumes de armazenamento em nível de bloco para uso com instâncias EC2, oferecendo desempenho persistente para sistemas operacionais e arquivos de bancos de dados."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de almacenamiento de AWS proporciona volúmenes de almacenamiento en bloques persistentes y de alto rendimiento diseñados para conectarse a una instancia en ejecución de Amazon EC2 como un disco duro virtual?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB",
                    "explanation": "Incorrecto: DynamoDB es una base de datos NoSQL, no almacenamiento en bloques."
                },
                {
                    "id": "B",
                    "text": "AWS Snowball",
                    "explanation": "Incorrecto: Snowball es un dispositivo de hardware físico para el transporte de datos."
                },
                {
                    "id": "C",
                    "text": "Amazon Elastic Block Store (Amazon EBS)",
                    "explanation": "Correcto: Amazon EBS proporciona volúmenes de almacenamiento en bloques persistentes para su uso con instancias de Amazon EC2."
                },
                {
                    "id": "D",
                    "text": "Amazon S3 Glacier",
                    "explanation": "Incorrecto: S3 Glacier es almacenamiento de objetos para archivado."
                }
            ],
            "generalExplanation": "Amazon Elastic Block Store (EBS) ofrece volúmenes de almacenamiento a nivel de bloque para usar con instancias EC2, brindando rendimiento persistente para el sistema operativo y archivos de base de datos."
        }
    },
    "clf-q044": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço de armazenamento da AWS oferece um sistema de arquivos elástico, compartilhado, totalmente gerenciado e sem servidor (serverless), que pode ser montado simultaneamente por centenas de instâncias Linux do Amazon EC2 em várias Zonas de Disponibilidade usando o protocolo NFS?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Elastic File System (Amazon EFS)",
                    "explanation": "Correto: O Amazon EFS é um sistema de arquivos totalmente elástico e sem servidor que permite compartilhar dados de arquivos entre várias instâncias EC2, contêineres e funções Lambda."
                },
                {
                    "id": "B",
                    "text": "Amazon S3 One Zone-IA",
                    "explanation": "Incorreto: O S3 é armazenamento de objetos, não um sistema de arquivos NFS montável."
                },
                {
                    "id": "C",
                    "text": "Instance Store",
                    "explanation": "Incorreto: O armazenamento de instâncias (Instance Store) é um armazenamento temporário e efêmero fisicamente conectado à máquina host."
                },
                {
                    "id": "D",
                    "text": "Amazon EBS gp3",
                    "explanation": "Incorreto: Volumes EBS gp3 se conectam a uma única instância em uma única AZ."
                }
            ],
            "generalExplanation": "O Amazon EFS fornece armazenamento de arquivos escalável para uso com serviços da Nuvem AWS e recursos locais (on-premises) por meio do protocolo padrão NFSv4."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de almacenamiento de AWS proporciona un sistema de archivos elástico, compartido, sin servidor y totalmente administrado que puede ser montado simultáneamente por cientos de instancias Linux de Amazon EC2 en múltiples Zonas de Disponibilidad mediante el protocolo NFS?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Elastic File System (Amazon EFS)",
                    "explanation": "Correcto: Amazon EFS es un sistema de archivos completamente elástico y sin servidor que le permite compartir datos de archivos entre múltiples instancias EC2, contenedores y funciones Lambda."
                },
                {
                    "id": "B",
                    "text": "Amazon S3 One Zone-IA",
                    "explanation": "Incorrecto: S3 es almacenamiento de objetos, no un sistema de archivos NFS montable."
                },
                {
                    "id": "C",
                    "text": "Instance Store",
                    "explanation": "Incorrecto: Instance Store es almacenamiento temporal y efímero conectado físicamente a la máquina host."
                },
                {
                    "id": "D",
                    "text": "Amazon EBS gp3",
                    "explanation": "Incorrecto: Los volúmenes EBS gp3 se conectan a una sola instancia dentro de una única AZ."
                }
            ],
            "generalExplanation": "Amazon EFS proporciona almacenamiento de archivos escalable para usar con servicios de AWS Cloud y recursos locales mediante el protocolo estándar NFSv4."
        }
    },
    "clf-q045": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço da AWS é um serviço de banco de dados relacional totalmente gerenciado que oferece suporte a mecanismos de banco de dados populares, incluindo PostgreSQL, MySQL, MariaDB, Oracle e Microsoft SQL Server?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB",
                    "explanation": "Incorreto: O DynamoDB é um banco de dados NoSQL gerenciado de chave-valor e documentos."
                },
                {
                    "id": "B",
                    "text": "Amazon Relational Database Service (Amazon RDS)",
                    "explanation": "Correto: O Amazon RDS facilita a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem em vários mecanismos populares."
                },
                {
                    "id": "C",
                    "text": "Amazon Redshift",
                    "explanation": "Incorreto: O Redshift é um data warehouse para análise de dados, não um banco de dados relacional operacional OLTP."
                },
                {
                    "id": "D",
                    "text": "Amazon Neptune",
                    "explanation": "Incorreto: O Neptune é um serviço de banco de dados de grafo especializado."
                }
            ],
            "generalExplanation": "O Amazon RDS é um serviço gerenciado que simplifica a configuração, a operação e a escalabilidade de bancos de dados relacionais na nuvem."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de AWS es un servicio de base de datos relacional totalmente administrado que admite motores de bases de datos populares como PostgreSQL, MySQL, MariaDB, Oracle y Microsoft SQL Server?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB",
                    "explanation": "Incorrecto: DynamoDB es una base de datos NoSQL administrada de clave-valor y documentos."
                },
                {
                    "id": "B",
                    "text": "Amazon Relational Database Service (Amazon RDS)",
                    "explanation": "Correcto: Amazon RDS facilita la configuración, operación y escalabilidad de bases de datos relacionales en la nube compatibles con diversos motores populares."
                },
                {
                    "id": "C",
                    "text": "Amazon Redshift",
                    "explanation": "Incorrecto: Redshift es un almacén de datos (data warehouse) para análisis, no una base de datos relacional operativa OLTP."
                },
                {
                    "id": "D",
                    "text": "Amazon Neptune",
                    "explanation": "Incorrecto: Neptune es un servicio especializado de base de datos de grafos."
                }
            ],
            "generalExplanation": "Amazon RDS es un servicio administrado que simplifica la configuración, el funcionamiento y el escalado de bases de datos relacionales en la nube."
        }
    },
    "clf-q046": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Um aplicativo móvel requer um banco de dados NoSQL de chave-valor e documentos, totalmente gerenciado e sem servidor (serverless), capaz de fornecer tempos de resposta consistentes de milissegundos de um dígito em qualquer escala. Qual serviço da AWS deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB",
                    "explanation": "Correto: O Amazon DynamoDB é um serviço de banco de dados NoSQL totalmente gerenciado que oferece desempenho rápido e previsível com escalabilidade contínua."
                },
                {
                    "id": "B",
                    "text": "Amazon ElastiCache for Memcached",
                    "explanation": "Incorreto: O ElastiCache Memcached é um cache em memória, não um banco de dados primário durável."
                },
                {
                    "id": "C",
                    "text": "Amazon RDS for MySQL",
                    "explanation": "Incorreto: O RDS for MySQL é um banco de dados SQL relacional."
                },
                {
                    "id": "D",
                    "text": "Amazon Aurora PostgreSQL",
                    "explanation": "Incorreto: O Aurora PostgreSQL é um banco de dados relacional."
                }
            ],
            "generalExplanation": "O Amazon DynamoDB é um banco de dados sem servidor de chave-valor e documentos que oferece desempenho de milissegundos de um dígito em qualquer escala."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "Una aplicación móvil requiere una base de datos NoSQL de clave-valor y documentos, completamente administrada y sin servidor, capaz de ofrecer tiempos de respuesta constantes de un solo dígito de milisegundo a cualquier escala. ¿Qué servicio de AWS se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon DynamoDB",
                    "explanation": "Correcto: Amazon DynamoDB es un servicio de base de datos NoSQL completamente administrado que ofrece un rendimiento rápido y predecible con escalabilidad sin interrupciones."
                },
                {
                    "id": "B",
                    "text": "Amazon ElastiCache for Memcached",
                    "explanation": "Incorrecto: ElastiCache Memcached es una memoria caché en memoria, no una base de datos principal duradera."
                },
                {
                    "id": "C",
                    "text": "Amazon RDS for MySQL",
                    "explanation": "Incorrecto: RDS for MySQL es una base de datos relacional SQL."
                },
                {
                    "id": "D",
                    "text": "Amazon Aurora PostgreSQL",
                    "explanation": "Incorrecto: Aurora PostgreSQL es una base de datos relacional."
                }
            ],
            "generalExplanation": "Amazon DynamoDB es una base de datos sin servidor de clave-valor y documentos que ofrece un rendimiento de milisegundos de un solo dígito a cualquier escala."
        }
    },
    "clf-q047": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Uma empresa deseja executar consultas SQL analíticas complexas e relatórios de business intelligence (BI) em petabytes de dados históricos de vendas estruturados. Qual serviço especializado da AWS é otimizado para data warehousing?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Lambda",
                    "explanation": "Incorreto: O Lambda é um serviço de computação sem servidor."
                },
                {
                    "id": "B",
                    "text": "Amazon Redshift",
                    "explanation": "Correto: O Amazon Redshift é um data warehouse rápido e escalável que simplifica a análise de dados em data warehouses e data lakes usando SQL padrão."
                },
                {
                    "id": "C",
                    "text": "Amazon SQS",
                    "explanation": "Incorreto: O SQS é um serviço de fila de mensagens."
                },
                {
                    "id": "D",
                    "text": "Amazon DynamoDB",
                    "explanation": "Incorreto: O DynamoDB é um repositório NoSQL de chave-valor, não um data warehouse analítico."
                }
            ],
            "generalExplanation": "O Amazon Redshift é o serviço de data warehouse em nuvem totalmente gerenciado da AWS em escala de petabytes, projetado para análises SQL de alto desempenho."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "Una empresa desea ejecutar consultas SQL analíticas complejas e informes de inteligencia empresarial (BI) sobre petabytes de datos históricos de ventas estructurados. ¿Qué servicio especializado de AWS está optimizado para el almacenamiento de datos (data warehousing)?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Lambda",
                    "explanation": "Incorrecto: Lambda es un servicio de cómputo sin servidor."
                },
                {
                    "id": "B",
                    "text": "Amazon Redshift",
                    "explanation": "Correcto: Amazon Redshift es un almacén de datos (data warehouse) rápido y escalable que simplifica el análisis de todos sus datos a través de almacenes de datos y lagos de datos mediante SQL estándar."
                },
                {
                    "id": "C",
                    "text": "Amazon SQS",
                    "explanation": "Incorrecto: SQS es un servicio de colas de mensajes."
                },
                {
                    "id": "D",
                    "text": "Amazon DynamoDB",
                    "explanation": "Incorrecto: DynamoDB es un almacén NoSQL de clave-valor, no un almacén de datos analítico."
                }
            ],
            "generalExplanation": "Amazon Redshift es el servicio de almacén de datos en la nube a escala de petabytes totalmente administrado de AWS, diseñado para análisis de SQL de alto rendimiento."
        }
    },
    "clf-q048": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço de rede da AWS permite provisionar uma seção logicamente isolada da Nuvem AWS onde você pode iniciar recursos da AWS em uma rede virtual definida por você?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Global Accelerator",
                    "explanation": "Incorreto: O Global Accelerator otimiza caminhos de rede para tráfego TCP/UDP."
                },
                {
                    "id": "B",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorreto: O Direct Connect é uma linha de rede física dedicada do ambiente local para a AWS."
                },
                {
                    "id": "C",
                    "text": "Amazon Route 53",
                    "explanation": "Incorreto: O Route 53 é um serviço web de DNS."
                },
                {
                    "id": "D",
                    "text": "Amazon Virtual Private Cloud (Amazon VPC)",
                    "explanation": "Correto: O Amazon VPC permite provisionar uma seção logicamente isolada da Nuvem AWS para iniciar recursos em uma rede virtual com controle total sobre intervalos de IP, sub-redes e gateways."
                }
            ],
            "generalExplanation": "O Amazon Virtual Private Cloud (Amazon VPC) oferece controle total sobre seu ambiente de rede virtual, incluindo alocação de recursos, conectividade e segurança."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de redes de AWS le permite aprovisionar una sección lógicamente aislada de AWS Cloud donde puede lanzar recursos de AWS en una red virtual definida por usted?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Global Accelerator",
                    "explanation": "Incorrecto: Global Accelerator optimiza las rutas de red para el tráfico TCP/UDP."
                },
                {
                    "id": "B",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorrecto: Direct Connect es una línea de red dedicada física desde el entorno local hacia AWS."
                },
                {
                    "id": "C",
                    "text": "Amazon Route 53",
                    "explanation": "Incorrecto: Route 53 es un servicio web de DNS."
                },
                {
                    "id": "D",
                    "text": "Amazon Virtual Private Cloud (Amazon VPC)",
                    "explanation": "Correcto: Amazon VPC le permite aprovisionar una sección lógicamente aislada de AWS Cloud donde puede iniciar recursos en una red virtual con control total sobre rangos de IP, subredes y puertas de enlace (gateways)."
                }
            ],
            "generalExplanation": "Amazon Virtual Private Cloud (Amazon VPC) le brinda control total sobre su entorno de red virtual, incluida la ubicación de recursos, la conectividad y la seguridad."
        }
    },
    "clf-q049": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Um administrador de sistemas deseja coletar e monitorar métricas de utilização de CPU para instâncias do Amazon EC2, definir alarmes que notifiquem a equipe quando a utilização ultrapassar 85% e visualizar painéis de desempenho. Qual serviço deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Config",
                    "explanation": "Incorreto: O AWS Config rastreia alterações de configuração e conformidade de recursos."
                },
                {
                    "id": "B",
                    "text": "AWS Trusted Advisor",
                    "explanation": "Incorreto: O Trusted Advisor fornece recomendações de práticas recomendadas, não métricas personalizadas de instâncias em tempo real e alarmes de limites."
                },
                {
                    "id": "C",
                    "text": "Amazon CloudWatch",
                    "explanation": "Correto: O Amazon CloudWatch coleta e visualiza métricas em tempo real, logs e rastreamentos, permitindo criar alarmes automatizados e painéis operacionais."
                },
                {
                    "id": "D",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorreto: O CloudTrail registra chamadas de API e atividades de usuários para auditorias de segurança, não métricas de desempenho de recursos em tempo real como porcentagem de CPU."
                }
            ],
            "generalExplanation": "O Amazon CloudWatch é um serviço de observabilidade que fornece dados e insights práticos para monitorar aplicações, responder a alterações de desempenho em todo o sistema e otimizar a utilização de recursos."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "Un administrador de sistemas desea recopilar y monitorear métricas de utilización de CPU para instancias de Amazon EC2, configurar alarmas que notifiquen al equipo cuando la utilización supere el 85% y ver paneles de rendimiento. ¿Qué servicio se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Config",
                    "explanation": "Incorrecto: AWS Config realiza un seguimiento de los cambios de configuración y el cumplimiento de los recursos."
                },
                {
                    "id": "B",
                    "text": "AWS Trusted Advisor",
                    "explanation": "Incorrecto: Trusted Advisor ofrece recomendaciones sobre las mejores prácticas, no métricas de instancias personalizadas en tiempo real ni alarmas de umbral."
                },
                {
                    "id": "C",
                    "text": "Amazon CloudWatch",
                    "explanation": "Correcto: Amazon CloudWatch recopila y visualiza métricas en tiempo real, registros (logs) y trazas, lo que le permite crear alarmas automatizadas y paneles operativos."
                },
                {
                    "id": "D",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorrecto: CloudTrail registra llamadas a la API y actividad de usuarios para auditorías de seguridad, no métricas de rendimiento en tiempo real como el porcentaje de CPU."
                }
            ],
            "generalExplanation": "Amazon CloudWatch es un servicio de observabilidad que proporciona datos e información práctica para monitorear aplicaciones, responder a cambios de rendimiento en todo el sistema y optimizar la utilización de recursos."
        }
    },
    "clf-q050": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Um auditor de segurança precisa determinar qual usuário do IAM encerrou uma instância do Amazon EC2 na última terça-feira, a partir de qual endereço IP a solicitação foi feita e o registro de data e hora exato da ação. Qual serviço da AWS fornece esse histórico de atividades de API?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS CloudTrail",
                    "explanation": "Correto: O AWS CloudTrail registra atividades da conta AWS e chamadas de API, fornecendo um histórico auditável de quem fez quais solicitações de API, quando e a partir de qual endereço IP."
                },
                {
                    "id": "B",
                    "text": "Amazon GuardDuty",
                    "explanation": "Incorreto: O GuardDuty gera descobertas de anomalias de segurança, mas o CloudTrail é o log principal que registra chamadas de API brutas."
                },
                {
                    "id": "C",
                    "text": "Amazon CloudWatch",
                    "explanation": "Incorreto: O CloudWatch monitora métricas e logs de desempenho, mas não registra o histórico de chamadas de API no nível da conta."
                },
                {
                    "id": "D",
                    "text": "AWS Artifact",
                    "explanation": "Incorreto: O Artifact fornece relatórios de conformidade para a infraestrutura da AWS."
                }
            ],
            "generalExplanation": "O AWS CloudTrail permite auditoria, monitoramento de segurança e solução de problemas operacionais ao rastrear atividades de usuários e o uso de APIs em toda a infraestrutura da AWS."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "Un auditor de seguridad necesita determinar qué usuario de IAM terminó una instancia de Amazon EC2 el martes pasado, desde qué dirección IP se realizó la solicitud y la marca de tiempo exacta de la acción. ¿Qué servicio de AWS proporciona este registro histórico de actividad de la API?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS CloudTrail",
                    "explanation": "Correcto: AWS CloudTrail registra la actividad de la cuenta de AWS y las llamadas a la API, proporcionando un historial auditable de quién realizó qué solicitudes de API, cuándo y desde qué dirección IP."
                },
                {
                    "id": "B",
                    "text": "Amazon GuardDuty",
                    "explanation": "Incorrecto: GuardDuty genera hallazgos de anomalías de seguridad, pero CloudTrail es el registro principal de llamadas de API sin procesar."
                },
                {
                    "id": "C",
                    "text": "Amazon CloudWatch",
                    "explanation": "Incorrecto: CloudWatch monitorea métricas de rendimiento y logs, pero no registra el historial de llamadas a la API a nivel de cuenta."
                },
                {
                    "id": "D",
                    "text": "AWS Artifact",
                    "explanation": "Incorrecto: Artifact proporciona informes de cumplimiento para la infraestructura de AWS."
                }
            ],
            "generalExplanation": "AWS CloudTrail permite la auditoría, la monitorización de seguridad y la resolución de problemas operativos al realizar un seguimiento de la actividad de los usuarios y el uso de la API en toda la infraestructura de AWS."
        }
    },
    "clf-q051": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço totalmente gerenciado da AWS fornece acesso a uma variedade de modelos fundamentais (Foundation Models - FMs) de alto desempenho das principais empresas de IA (como Anthropic, AI21 Labs, Cohere, Meta e Amazon) por meio de uma API única e unificada para criar aplicativos de IA generativa?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Comprehend",
                    "explanation": "Incorreto: O Comprehend é um serviço de processamento de linguagem natural (NLP) para análise de texto."
                },
                {
                    "id": "B",
                    "text": "Amazon Polly",
                    "explanation": "Incorreto: O Polly converte texto em fala realista."
                },
                {
                    "id": "C",
                    "text": "Amazon Rekognition",
                    "explanation": "Incorreto: O Rekognition é um serviço de visão computacional para análise de imagens e vídeos."
                },
                {
                    "id": "D",
                    "text": "Amazon Bedrock",
                    "explanation": "Correto: O Amazon Bedrock é um serviço totalmente gerenciado que oferece uma seleção de modelos fundamentais (FMs) de alto desempenho com um amplo conjunto de recursos para criar e escalar aplicações de IA generativa."
                }
            ],
            "generalExplanation": "O Amazon Bedrock é a maneira mais fácil de criar e escalar aplicações de IA generativa usando modelos fundamentais das principais startups de IA e da Amazon."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio totalmente administrado de AWS brinda acceso a una selección de modelos fundacionales (Foundation Models - FMs) de alto rendimiento de empresas líderes de IA (como Anthropic, AI21 Labs, Cohere, Meta y Amazon) a través de una API única y unificada para crear aplicaciones de IA generativa?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Comprehend",
                    "explanation": "Incorrecto: Comprehend es un servicio de procesamiento de lenguaje natural (NLP) para análisis de texto."
                },
                {
                    "id": "B",
                    "text": "Amazon Polly",
                    "explanation": "Incorrecto: Polly convierte texto en voz realista."
                },
                {
                    "id": "C",
                    "text": "Amazon Rekognition",
                    "explanation": "Incorrecto: Rekognition es un servicio de visión artificial para análisis de imágenes y vídeos."
                },
                {
                    "id": "D",
                    "text": "Amazon Bedrock",
                    "explanation": "Correcto: Amazon Bedrock es un servicio totalmente administrado que ofrece una selección de modelos fundacionales (FMs) de alto rendimiento junto con un amplio conjunto de capacidades para crear y escalar aplicaciones de IA generativa."
                }
            ],
            "generalExplanation": "Amazon Bedrock es la forma más sencilla de crear y escalar aplicaciones de IA generativa con modelos fundacionales de las principales empresas emergentes de IA y de Amazon."
        }
    },
    "clf-q052": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço abrangente e totalmente gerenciado da AWS fornece a cientistas de dados e desenvolvedores todas as ferramentas necessárias para criar, treinar, ajustar e implantar modelos de machine learning (ML) em escala?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS CloudFormation",
                    "explanation": "Incorreto: O CloudFormation é um serviço de provisionamento de infraestrutura como código (IaC)."
                },
                {
                    "id": "B",
                    "text": "Amazon SageMaker",
                    "explanation": "Correto: O Amazon SageMaker é uma plataforma de machine learning totalmente gerenciada que ajuda cientistas de dados e desenvolvedores a preparar, construir, treinar e implantar rapidamente modelos de ML de alta qualidade."
                },
                {
                    "id": "C",
                    "text": "AWS Glue",
                    "explanation": "Incorreto: O Glue é um serviço de integração de dados (ETL) sem servidor."
                },
                {
                    "id": "D",
                    "text": "Amazon Transcribe",
                    "explanation": "Incorreto: O Transcribe é um serviço especializado de conversão de fala em texto."
                }
            ],
            "generalExplanation": "O Amazon SageMaker oferece ferramentas completas de ponta a ponta para criar, treinar e implantar modelos de machine learning com fluxos de trabalho e infraestrutura totalmente gerenciados."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio integral y totalmente administrado de AWS proporciona a científicos de datos y desarrolladores todas las herramientas necesarias para crear, entrenar, ajustar e implementar modelos de machine learning (ML) a escala?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS CloudFormation",
                    "explanation": "Incorrecto: CloudFormation es un servicio de aprovisionamiento de infraestructura como código (IaC)."
                },
                {
                    "id": "B",
                    "text": "Amazon SageMaker",
                    "explanation": "Correcto: Amazon SageMaker es una plataforma de aprendizaje automático (ML) totalmente administrada que ayuda a científicos de datos y desarrolladores a preparar, crear, entrenar e implementar rápidamente modelos de ML de alta calidad."
                },
                {
                    "id": "C",
                    "text": "AWS Glue",
                    "explanation": "Incorrecto: Glue es un servicio de integración de datos (ETL) sin servidor."
                },
                {
                    "id": "D",
                    "text": "Amazon Transcribe",
                    "explanation": "Incorrecto: Transcribe es un servicio especializado de voz a texto."
                }
            ],
            "generalExplanation": "Amazon SageMaker proporciona herramientas integrales de extremo a extremo para crear, entrenar e implementar modelos de aprendizaje automático con infraestructura y flujos de trabajo totalmente administrados."
        }
    },
    "clf-q053": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço de inteligência artificial da AWS utiliza visão computacional para detectar automaticamente objetos, pessoas, texto, cenas e conteúdo inadequado em arquivos de imagem e vídeo?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Lex",
                    "explanation": "Incorreto: O Lex cria interfaces de chatbots conversacionais usando voz e texto."
                },
                {
                    "id": "B",
                    "text": "Amazon Translate",
                    "explanation": "Incorreto: O Translate realiza tradução automática neural de idiomas."
                },
                {
                    "id": "C",
                    "text": "Amazon Polly",
                    "explanation": "Incorreto: O Polly converte texto em áudio falado."
                },
                {
                    "id": "D",
                    "text": "Amazon Rekognition",
                    "explanation": "Correto: O Amazon Rekognition facilita a adição de análise de imagem e vídeo aos seus aplicativos usando tecnologia comprovada e altamente escalável de deep learning."
                }
            ],
            "generalExplanation": "O Amazon Rekognition oferece recursos de visão computacional pré-treinados e personalizáveis para extrair insights de imagens e vídeos sem a necessidade de conhecimento avançado em machine learning."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de inteligencia artificial de AWS utiliza visión artificial para detectar automáticamente objetos, personas, texto, escenas y contenido inapropiado en archivos de imagen y vídeo?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Lex",
                    "explanation": "Incorrecto: Lex crea interfaces conversacionales de chatbot mediante voz y texto."
                },
                {
                    "id": "B",
                    "text": "Amazon Translate",
                    "explanation": "Incorrecto: Translate realiza traducción automática neuronal de idiomas."
                },
                {
                    "id": "C",
                    "text": "Amazon Polly",
                    "explanation": "Incorrecto: Polly convierte texto en audio hablado."
                },
                {
                    "id": "D",
                    "text": "Amazon Rekognition",
                    "explanation": "Correcto: Amazon Rekognition facilita la incorporación de análisis de imágenes y vídeos a sus aplicaciones mediante tecnología de aprendizaje profundo (deep learning) probada y altamente escalable."
                }
            ],
            "generalExplanation": "Amazon Rekognition ofrece funciones de visión artificial previamente entrenadas y personalizables para extraer información de imágenes y vídeos sin necesidad de experiencia en aprendizaje automático."
        }
    },
    "clf-q054": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço da AWS permite modelar, provisionar e controlar a versão de toda a sua infraestrutura em nuvem como código (IaC) usando arquivos de modelo declarativos em JSON ou YAML?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Elastic Beanstalk",
                    "explanation": "Incorreto: O Elastic Beanstalk é uma plataforma como serviço (PaaS) para implantar aplicativos web."
                },
                {
                    "id": "B",
                    "text": "AWS CloudFormation",
                    "explanation": "Correto: O AWS CloudFormation permite tratar a infraestrutura como código (IaC), possibilitando criar, versionar e implantar recursos da AWS usando modelos JSON ou YAML."
                },
                {
                    "id": "C",
                    "text": "AWS CodeCommit",
                    "explanation": "Incorreto: O CodeCommit é um serviço de repositório de controle de código-fonte Git gerenciado."
                },
                {
                    "id": "D",
                    "text": "AWS Config",
                    "explanation": "Incorreto: O Config avalia a conformidade de configurações, mas não provisiona pilhas de recursos a partir de modelos."
                }
            ],
            "generalExplanation": "O AWS CloudFormation permite modelar uma coleção de recursos relacionados da AWS e de terceiros, provisioná-los de maneira rápida e consistente e gerenciá-los ao longo de todo o ciclo de vida."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio de AWS le permite modelar, aprovisionar y versionar toda su infraestructura en la nube como código (IaC) mediante archivos de plantilla declarativos en JSON o YAML?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Elastic Beanstalk",
                    "explanation": "Incorrecto: Elastic Beanstalk es una plataforma como servicio (PaaS) para implementar aplicaciones web."
                },
                {
                    "id": "B",
                    "text": "AWS CloudFormation",
                    "explanation": "Correcto: AWS CloudFormation le permite tratar la infraestructura como código (IaC), lo que le permite crear, versionar e implementar recursos de AWS mediante plantillas JSON o YAML."
                },
                {
                    "id": "C",
                    "text": "AWS CodeCommit",
                    "explanation": "Incorrecto: CodeCommit es un servicio de repositorio de control de código fuente Git administrado."
                },
                {
                    "id": "D",
                    "text": "AWS Config",
                    "explanation": "Incorrecto: Config evalúa el cumplimiento de la configuración, pero no aprovisiona pilas a partir de plantillas."
                }
            ],
            "generalExplanation": "AWS CloudFormation le permite modelar una colección de recursos relacionados de AWS y de terceros, aprovisionarlos de manera rápida y coherente y administrarlos a lo largo de su ciclo de vida."
        }
    },
    "clf-q055": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual serviço web de Sistema de Nomes de Domínio (DNS) em nuvem, altamente disponível e escalável, converte nomes de domínio amigáveis (como `example.com`) em endereços IP numéricos e oferece recursos de registro de domínio?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon CloudFront",
                    "explanation": "Incorreto: O CloudFront é uma Rede de Entrega de Conteúdo (CDN), não um serviço de registro de DNS."
                },
                {
                    "id": "B",
                    "text": "Amazon VPC",
                    "explanation": "Incorreto: A VPC fornece isolamento de rede virtual privada."
                },
                {
                    "id": "C",
                    "text": "Amazon Route 53",
                    "explanation": "Correto: O Amazon Route 53 é um serviço web de DNS em nuvem altamente disponível e escalável, projetado para rotear usuários finais para aplicações na internet."
                },
                {
                    "id": "D",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorreto: O Direct Connect é uma conexão de rede física."
                }
            ],
            "generalExplanation": "O Amazon Route 53 conecta com eficiência as solicitações dos usuários à infraestrutura em execução na AWS e oferece registro de nomes de domínio."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué servicio web de Sistema de Nombres de Dominio (DNS) en la nube, altamente disponible y escalable, traduce nombres de dominio descriptivos (como `example.com`) en direcciones IP numéricas y proporciona funciones de registro de dominios?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon CloudFront",
                    "explanation": "Incorrecto: CloudFront es una Red de Entrega de Contenido (CDN), no un servicio de registro de DNS."
                },
                {
                    "id": "B",
                    "text": "Amazon VPC",
                    "explanation": "Incorrecto: VPC proporciona aislamiento de red privada virtual."
                },
                {
                    "id": "C",
                    "text": "Amazon Route 53",
                    "explanation": "Correcto: Amazon Route 53 es un servicio web de DNS en la nube altamente disponible y escalable diseñado para enrutar usuarios finales hacia aplicaciones de Internet."
                },
                {
                    "id": "D",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorrecto: Direct Connect es una línea de red física."
                }
            ],
            "generalExplanation": "Amazon Route 53 conecta de manera efectiva las solicitudes de los usuarios con la infraestructura que se ejecuta en AWS y proporciona registro de nombres de dominio."
        }
    },
    "clf-q056": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Qual ferramenta da AWS fornece alertas personalizados e notificações proativas sobre interrupções de serviço, eventos de manutenção programada e status geral que afetam especificamente os recursos da sua conta da AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Artifact",
                    "explanation": "Incorreto: O Artifact fornece relatórios de conformidade."
                },
                {
                    "id": "B",
                    "text": "AWS KMS",
                    "explanation": "Incorreto: O KMS gerencia chaves de criptografia."
                },
                {
                    "id": "C",
                    "text": "Amazon Inspector",
                    "explanation": "Incorreto: O Inspector verifica vulnerabilidades de software em cargas de trabalho."
                },
                {
                    "id": "D",
                    "text": "AWS Health Dashboard",
                    "explanation": "Correto: O AWS Health Dashboard fornece alertas e orientações de correção quando a AWS passa por eventos que podem impactar os recursos específicos da sua conta."
                }
            ],
            "generalExplanation": "O AWS Health Dashboard fornece visibilidade personalizada sobre o desempenho e a disponibilidade dos serviços da AWS subjacentes aos seus recursos específicos."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Qué herramienta de AWS proporciona alertas personalizadas y notificaciones proactivas sobre interrupciones de servicio, eventos de mantenimiento planificado y el estado general que afecta específicamente a los recursos de su cuenta de AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Artifact",
                    "explanation": "Incorrecto: Artifact proporciona informes de cumplimiento."
                },
                {
                    "id": "B",
                    "text": "AWS KMS",
                    "explanation": "Incorrecto: KMS administra claves de cifrado."
                },
                {
                    "id": "C",
                    "text": "Amazon Inspector",
                    "explanation": "Incorrecto: Inspector analiza vulnerabilidades de software en las cargas de trabajo."
                },
                {
                    "id": "D",
                    "text": "AWS Health Dashboard",
                    "explanation": "Correcto: AWS Health Dashboard proporciona alertas y orientación de solución cuando AWS experimenta eventos que pueden afectar los recursos específicos de su cuenta."
                }
            ],
            "generalExplanation": "AWS Health Dashboard proporciona visibilidad personalizada sobre el rendimiento y la disponibilidad de los servicios de AWS que respaldan sus recursos específicos de AWS."
        }
    },
    "clf-q057": {
        "pt": {
            "domainName": "Domínio 3: Tecnologia e Serviços em Nuvem",
            "statement": "Quais dos seguintes serviços são serviços essenciais de mensagens e notificações da AWS usados para desacoplar arquiteturas distribuídas de microsserviços? (Escolha dois.)",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Simple Queue Service (Amazon SQS)",
                    "explanation": "Correto: O Amazon SQS é um serviço de filas de mensagens totalmente gerenciado que permite desacoplar e escalar microsserviços, sistemas distribuídos e aplicações sem servidor."
                },
                {
                    "id": "B",
                    "text": "Amazon QuickSight",
                    "explanation": "Incorreto: O QuickSight é uma ferramenta de visualização de Business Intelligence (BI)."
                },
                {
                    "id": "C",
                    "text": "Amazon Simple Notification Service (Amazon SNS)",
                    "explanation": "Correto: O Amazon SNS é um serviço de mensagens pub/sub totalmente gerenciado para comunicação aplicativo a aplicativo (A2A) e aplicativo para pessoa (A2P)."
                },
                {
                    "id": "D",
                    "text": "Amazon Aurora",
                    "explanation": "Incorreto: O Aurora é um mecanismo de banco de dados relacional."
                },
                {
                    "id": "E",
                    "text": "AWS Snowball Edge",
                    "explanation": "Incorreto: O Snowball Edge é um dispositivo físico de transferência de dados."
                }
            ],
            "generalExplanation": "O Amazon SQS (filas de mensagens) e o Amazon SNS (tópicos de notificação de publicação/assinatura) são serviços fundamentais de mensagens da AWS usados para desacoplar microsserviços."
        },
        "es": {
            "domainName": "Dominio 3: Tecnología y Servicios en la Nube",
            "statement": "¿Cuáles de los siguientes servicios son servicios principales de mensajería y notificación de AWS que se utilizan para desacoplar arquitecturas de microservicios distribuidas? (Elija dos).",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Simple Queue Service (Amazon SQS)",
                    "explanation": "Correcto: Amazon SQS es un servicio de colas de mensajes totalmente administrado que le permite desacoplar y escalar microservicios, sistemas distribuidos y aplicaciones sin servidor."
                },
                {
                    "id": "B",
                    "text": "Amazon QuickSight",
                    "explanation": "Incorrecto: QuickSight es una herramienta de visualización de inteligencia empresarial (BI)."
                },
                {
                    "id": "C",
                    "text": "Amazon Simple Notification Service (Amazon SNS)",
                    "explanation": "Correcto: Amazon SNS es un servicio de mensajería de publicación/suscripción (pub/sub) totalmente administrado para comunicación de aplicación a aplicación (A2A) y de aplicación a persona (A2P)."
                },
                {
                    "id": "D",
                    "text": "Amazon Aurora",
                    "explanation": "Incorrecto: Aurora es un motor de base de datos relacional."
                },
                {
                    "id": "E",
                    "text": "AWS Snowball Edge",
                    "explanation": "Incorrecto: Snowball Edge es un dispositivo físico de transferencia de datos."
                }
            ],
            "generalExplanation": "Amazon SQS (colas de mensajes) y Amazon SNS (temas de notificación de publicación/suscripción) son servicios fundamentales de mensajería de AWS utilizados para desacoplar microservicios."
        }
    },
    "clf-q058": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Uma equipe de pesquisa executa trabalhos de processamento de dados em lote, sem estado (stateless) e tolerantes a falhas, que podem aceitar interrupções inesperadas. Qual modelo de definição de preço do Amazon EC2 oferece o maior desconto (até 90% de desconto sobre as taxas On-Demand) aproveitando a capacidade ociosa de computação?",
            "options": [
                {
                    "id": "A",
                    "text": "Instâncias sob demanda (On-Demand Instances)",
                    "explanation": "Incorreto: As instâncias sob demanda são cobradas com taxas horárias padrão integrais."
                },
                {
                    "id": "B",
                    "text": "Instâncias Spot (Spot Instances)",
                    "explanation": "Correto: As instâncias Spot do Amazon EC2 permitem solicitar capacidade ociosa do EC2 com grandes descontos de até 90% em comparação com os preços sob demanda, sendo ideais para cargas de trabalho tolerantes a falhas."
                },
                {
                    "id": "C",
                    "text": "Instâncias reservadas padrão (Standard Reserved Instances)",
                    "explanation": "Incorreto: As instâncias reservadas exigem compromisso de 1 ou 3 anos e oferecem descontos de até 72%, ao contrário do modelo Spot de capacidade ociosa."
                },
                {
                    "id": "D",
                    "text": "Hosts dedicados (Dedicated Hosts)",
                    "explanation": "Incorreto: Os hosts dedicados alocam servidores físicos exclusivamente para seu uso com custos mais elevados."
                }
            ],
            "generalExplanation": "As instâncias Spot do Amazon EC2 oferecem até 90% de desconto sobre a capacidade ociosa do EC2 para cargas de trabalho tolerantes a falhas e capazes de suportar interrupções."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "Un equipo de investigación ejecuta tareas de procesamiento de datos por lotes sin estado y tolerantes a fallos que pueden admitir interrupciones inesperadas. ¿Qué modelo de precios de Amazon EC2 ofrece el mayor descuento (hasta un 90% de descuento sobre las tarifas bajo demanda) al aprovechar la capacidad de cómputo no utilizada?",
            "options": [
                {
                    "id": "A",
                    "text": "Instancias bajo demanda (On-Demand Instances)",
                    "explanation": "Incorrecto: Las instancias bajo demanda se facturan según tarifas horarias estándar completas."
                },
                {
                    "id": "B",
                    "text": "Instancias Spot (Spot Instances)",
                    "explanation": "Correcto: Las instancias Spot de Amazon EC2 le permiten solicitar capacidad no utilizada de EC2 con grandes descuentos de hasta un 90% en comparación con los precios bajo demanda, lo que resulta ideal para cargas de trabajo tolerantes a fallos."
                },
                {
                    "id": "C",
                    "text": "Instancias reservadas estándar (Standard Reserved Instances)",
                    "explanation": "Incorrecto: Las instancias reservadas requieren compromisos de 1 o 3 años y ofrecen hasta un 72% de descuento, a diferencia de la capacidad no utilizada de Spot."
                },
                {
                    "id": "D",
                    "text": "Hosts dedicados (Dedicated Hosts)",
                    "explanation": "Incorrecto: Los hosts dedicados asignan servidores físicos exclusivamente para su uso con costos más elevados."
                }
            ],
            "generalExplanation": "Las instancias Spot de Amazon EC2 ofrecen hasta un 90% de descuento sobre la capacidad de EC2 no utilizada para cargas de trabajo tolerantes a fallos que pueden admitir interrupciones."
        }
    },
    "clf-q059": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Qual ferramenta da AWS permite visualizar, entender e gerenciar seus custos históricos da AWS e padrões de uso ao longo do tempo, além de gerar previsões de custos para períodos de faturamento futuros?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Artifact",
                    "explanation": "Incorreto: O Artifact fornece relatórios de conformidade."
                },
                {
                    "id": "B",
                    "text": "AWS Cost Explorer",
                    "explanation": "Correto: O AWS Cost Explorer possui uma interface fácil de usar que permite visualizar, compreender e gerenciar seus custos e uso da AWS ao longo do tempo, incluindo previsões de gastos futuros."
                },
                {
                    "id": "C",
                    "text": "Amazon CloudWatch Logs",
                    "explanation": "Incorreto: O CloudWatch Logs armazena linhas de logs de aplicativos, não gráficos de análise de custos."
                },
                {
                    "id": "D",
                    "text": "AWS Pricing Calculator",
                    "explanation": "Incorreto: A Calculadora de Preços da AWS estima custos para arquiteturas propostas antes da implantação, mas não rastreia gastos históricos da conta."
                }
            ],
            "generalExplanation": "O AWS Cost Explorer fornece análises visuais interativas, filtragem e previsões para compreender e otimizar os gastos históricos da AWS."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "¿Qué herramienta de AWS le permite visualizar, comprender y administrar sus costos históricos de AWS y patrones de uso a lo largo del tiempo, así como generar previsiones de costos para períodos de facturación futuros?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Artifact",
                    "explanation": "Incorrecto: Artifact proporciona informes de cumplimiento."
                },
                {
                    "id": "B",
                    "text": "AWS Cost Explorer",
                    "explanation": "Correcto: AWS Cost Explorer cuenta con una interfaz fácil de usar que le permite visualizar, comprender y administrar sus costos y uso de AWS a lo largo del tiempo, incluido el pronóstico de gastos futuros."
                },
                {
                    "id": "C",
                    "text": "Amazon CloudWatch Logs",
                    "explanation": "Incorrecto: CloudWatch Logs almacena líneas de registro de aplicaciones, no gráficos de análisis de costos."
                },
                {
                    "id": "D",
                    "text": "AWS Pricing Calculator",
                    "explanation": "Incorrecto: La calculadora de precios de AWS calcula los costos de arquitecturas propuestas antes de la implementación, pero no realiza un seguimiento del gasto histórico de la cuenta."
                }
            ],
            "generalExplanation": "AWS Cost Explorer proporciona análisis visuales interactivos, filtrado y pronósticos para comprender y optimizar el gasto histórico de AWS."
        }
    },
    "clf-q060": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Um gerente financeiro deseja definir um limite mensal de gastos personalizado de US$ 5.000 para uma conta da AWS e receber notificações automáticas por e-mail sempre que os custos reais ou custos previstos ultrapassarem 80% do limite. Qual serviço deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Shield Standard",
                    "explanation": "Incorreto: O Shield Standard é um serviço de proteção contra ataques DDoS."
                },
                {
                    "id": "B",
                    "text": "AWS Trusted Advisor Basic",
                    "explanation": "Incorreto: O plano Basic do Trusted Advisor não envia notificações proativas de limites orçamentários personalizados."
                },
                {
                    "id": "C",
                    "text": "AWS Budgets",
                    "explanation": "Correto: O AWS Budgets permite definir limites personalizados de custo e uso e receber alertas por e-mail ou SNS quando seus custos excederem (ou estiverem previstos para exceder) o valor orçado."
                },
                {
                    "id": "D",
                    "text": "AWS Pricing Calculator",
                    "explanation": "Incorreto: A Calculadora de Preços estima os custos antes da construção, mas não envia alertas de limites em contas ativas."
                }
            ],
            "generalExplanation": "O AWS Budgets oferece a capacidade de definir orçamentos personalizados que emitem alertas quando o custo ou o uso ultrapassa o limite orçado."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "Un gerente de finanzas desea establecer un límite de gasto mensual personalizado de 5.000 USD para una cuenta de AWS y recibir notificaciones automáticas por correo electrónico siempre que los costos reales o previstos superen el 80% del límite. ¿Qué servicio se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Shield Standard",
                    "explanation": "Incorrecto: Shield Standard es un servicio de protección contra ataques DDoS."
                },
                {
                    "id": "B",
                    "text": "AWS Trusted Advisor Basic",
                    "explanation": "Incorrecto: El nivel básico de Trusted Advisor no envía notificaciones proactivas sobre umbrales de presupuesto personalizados."
                },
                {
                    "id": "C",
                    "text": "AWS Budgets",
                    "explanation": "Correcto: AWS Budgets le permite establecer límites de costos y uso personalizados y recibir alertas por correo electrónico o SNS cuando sus costos excedan (o se prevea que excedan) la cantidad presupuestada."
                },
                {
                    "id": "D",
                    "text": "AWS Pricing Calculator",
                    "explanation": "Incorrecto: La calculadora de precios calcula estimaciones de costos antes de la creación, pero no envía alertas de umbral en cuentas activas."
                }
            ],
            "generalExplanation": "AWS Budgets le permite establecer presupuestos personalizados que le alertan cuando su costo o uso supera el umbral presupuestado."
        }
    },
    "clf-q061": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Um arquiteto de soluções está planejando uma nova arquitetura em nuvem para um cliente e precisa estimar os custos mensais projetados de instâncias EC2, armazenamento S3 e bancos de dados RDS ANTES de provisionar qualquer recurso. Qual ferramenta da AWS deve ser usada?",
            "options": [
                {
                    "id": "A",
                    "text": "Painel de Faturamento da AWS (AWS Billing Dashboard)",
                    "explanation": "Incorreto: O painel de faturamento exibe as faturas mensais ativas."
                },
                {
                    "id": "B",
                    "text": "AWS Pricing Calculator",
                    "explanation": "Correto: A Calculadora de Preços da AWS (AWS Pricing Calculator) é uma ferramenta de planejamento baseada na web que permite criar estimativas de custos para suas propostas de arquitetura na AWS antes de iniciar os recursos."
                },
                {
                    "id": "C",
                    "text": "AWS Cost and Usage Report (CUR)",
                    "explanation": "Incorreto: O CUR é um relatório abrangente gerado após a execução dos recursos."
                },
                {
                    "id": "D",
                    "text": "AWS Cost Explorer",
                    "explanation": "Incorreto: O Cost Explorer analisa os gastos históricos anteriores em recursos existentes."
                }
            ],
            "generalExplanation": "A Calculadora de Preços da AWS permite modelar soluções e gerar estimativas de custos antes do lançamento de recursos em sua conta da AWS."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "Un arquitecto de soluciones está planificando una nueva arquitectura en la nube para un cliente y necesita estimar los costos mensuales proyectados de instancias EC2, almacenamiento S3 y bases de datos RDS ANTES de aprovisionar cualquier recurso. ¿Qué herramienta de AWS se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Panel de facturación de AWS (AWS Billing Dashboard)",
                    "explanation": "Incorrecto: El panel de facturación muestra las facturas mensuales activas."
                },
                {
                    "id": "B",
                    "text": "AWS Pricing Calculator",
                    "explanation": "Correcto: La calculadora de precios de AWS (AWS Pricing Calculator) es una herramienta de planificación basada en la web que le permite crear estimaciones de costos para sus arquitecturas de AWS propuestas antes de lanzar recursos."
                },
                {
                    "id": "C",
                    "text": "AWS Cost and Usage Report (CUR)",
                    "explanation": "Incorrecto: El CUR es un informe detallado que se genera después de que los recursos entran en ejecución."
                },
                {
                    "id": "D",
                    "text": "AWS Cost Explorer",
                    "explanation": "Incorrecto: Cost Explorer analiza el gasto histórico anterior en recursos existentes."
                }
            ],
            "generalExplanation": "AWS Pricing Calculator le permite modelar soluciones y generar estimaciones de costos antes de iniciar recursos en su cuenta de AWS."
        }
    },
    "clf-q062": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Uma empresa necessita de acesso a suporte técnico 24 horas por dia, 7 dias por semana por telefone, chat e e-mail, tempo de resposta inferior a 15 minutos para interrupções críticas de sistemas de negócios, acesso a um Technical Account Manager (TAM) dedicado e a uma equipe do Concierge Support. Qual plano do AWS Support é obrigatório?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Developer Support",
                    "explanation": "Incorreto: O plano Developer oferece suporte por e-mail apenas em horário comercial, sem suporte por telefone ou TAM."
                },
                {
                    "id": "B",
                    "text": "AWS Enterprise Support",
                    "explanation": "Correto: O AWS Enterprise Support inclui um Technical Account Manager (TAM) designado, equipe de suporte do Concierge e tempos de resposta inferiores a 15 minutos para eventos de paralisação de sistemas críticos para os negócios."
                },
                {
                    "id": "C",
                    "text": "AWS Basic Support",
                    "explanation": "Incorreto: O suporte básico cobre apenas dúvidas de faturamento e conta, sem suporte técnico a chamados."
                },
                {
                    "id": "D",
                    "text": "AWS Business Support",
                    "explanation": "Incorreto: O plano Business oferece suporte técnico 24 horas por dia, 7 dias por semana, mas NÃO inclui um Technical Account Manager (TAM) dedicado."
                }
            ],
            "generalExplanation": "O AWS Enterprise Support oferece suporte técnico de nível superior com atendimento personalizado, incluindo um Technical Account Manager (TAM) dedicado, equipe de Concierge e tempo de resposta de 15 minutos para incidentes críticos."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "Una empresa requiere acceso a soporte técnico las 24 horas, los 7 días de la semana por teléfono, chat y correo electrónico, un tiempo de respuesta de menos de 15 minutos para caídas críticas de sistemas empresariales, acceso a un Technical Account Manager (TAM) exclusivo y un equipo de Concierge Support. ¿Qué plan de AWS Support se requiere?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Developer Support",
                    "explanation": "Incorrecto: El soporte Developer ofrece asistencia por correo electrónico únicamente en horario comercial, sin atención telefónica ni TAM."
                },
                {
                    "id": "B",
                    "text": "AWS Enterprise Support",
                    "explanation": "Correcto: AWS Enterprise Support incluye un Technical Account Manager (TAM) designado, un equipo de soporte de Concierge y tiempos de respuesta de menos de 15 minutos para caídas de sistemas de misión crítica."
                },
                {
                    "id": "C",
                    "text": "AWS Basic Support",
                    "explanation": "Incorrecto: El soporte Basic solo cubre consultas de facturación y de cuenta sin soporte para casos técnicos."
                },
                {
                    "id": "D",
                    "text": "AWS Business Support",
                    "explanation": "Incorrecto: El soporte Business proporciona soporte técnico las 24 horas, los 7 días de la semana, pero NO incluye un Technical Account Manager (TAM) dedicado."
                }
            ],
            "generalExplanation": "AWS Enterprise Support brinda soporte técnico altamente personalizado que incluye un Technical Account Manager (TAM) exclusivo, un equipo de Concierge y tiempos de respuesta de 15 minutos para incidentes críticos."
        }
    },
    "clf-q063": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Qual é o plano MÍNIMO do AWS Support que oferece acesso técnico 24 horas por dia, 7 dias por semana por telefone, e-mail e chat a engenheiros de suporte em nuvem (Cloud Support Engineers), tempos de resposta inferiores a 1 hora para paralisações de sistemas em produção e acesso completo a todas as verificações de práticas recomendadas do AWS Trusted Advisor?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Basic Support",
                    "explanation": "Incorreto: O Basic Support não tem acesso a abertura de casos técnicos."
                },
                {
                    "id": "B",
                    "text": "AWS Developer Support",
                    "explanation": "Incorreto: O Developer Support oferece apenas suporte por e-mail durante o horário comercial e 7 verificações básicas limitadas do Trusted Advisor."
                },
                {
                    "id": "C",
                    "text": "AWS Free Tier",
                    "explanation": "Incorreto: O Nível Gratuito (Free Tier) é um benefício de definição de preço, não um plano de suporte técnico."
                },
                {
                    "id": "D",
                    "text": "AWS Business Support",
                    "explanation": "Correto: O AWS Business Support é o plano de suporte mínimo que fornece acesso 24 horas por dia, 7 dias por semana a engenheiros de suporte via telefone/chat, tempo de resposta < 1 hora para produção inoperante e verificações completas do Trusted Advisor."
                }
            ],
            "generalExplanation": "O AWS Business Support foi desenvolvido para cargas de trabalho em execução em produção, oferecendo suporte técnico 24 horas por dia, 7 dias por semana, verificações completas do Trusted Advisor e resposta em 1 hora para problemas de produção."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "¿Cuál es el plan MÍNIMO de AWS Support que ofrece acceso técnico por teléfono, correo electrónico y chat las 24 horas, los 7 días de la semana con ingenieros de soporte en la nube (Cloud Support Engineers), tiempos de respuesta de menos de 1 hora para caídas de sistemas en producción y acceso completo a todas las comprobaciones de mejores prácticas de AWS Trusted Advisor?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Basic Support",
                    "explanation": "Incorrecto: Basic Support no tiene acceso para abrir casos técnicos."
                },
                {
                    "id": "B",
                    "text": "AWS Developer Support",
                    "explanation": "Incorrecto: Developer Support solo ofrece soporte por correo electrónico en horario comercial y 7 comprobaciones básicas limitadas de Trusted Advisor."
                },
                {
                    "id": "C",
                    "text": "Capa gratuita de AWS (AWS Free Tier)",
                    "explanation": "Incorrecto: La capa gratuita es un beneficio de precios, no un nivel de soporte técnico."
                },
                {
                    "id": "D",
                    "text": "AWS Business Support",
                    "explanation": "Correcto: AWS Business Support es el nivel de plan de soporte mínimo que brinda acceso 24/7 a ingenieros de soporte en la nube por teléfono/chat, respuesta en < 1 hora para sistemas de producción fuera de servicio y todas las comprobaciones de Trusted Advisor."
                }
            ],
            "generalExplanation": "AWS Business Support está diseñado para cargas de trabajo en producción, brindando soporte técnico 24/7, comprobaciones completas de Trusted Advisor y respuesta en 1 hora ante problemas en producción."
        }
    },
    "clf-q064": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Uma empresa deseja organizar e rastrear seus custos da AWS entre diferentes departamentos, projetos e centros de custo em sua fatura mensal consolidada. Qual recurso permite que os administradores atribuam metadados no formato chave-valor aos recursos para categorização de custos?",
            "options": [
                {
                    "id": "A",
                    "text": "Security Groups da AWS",
                    "explanation": "Incorreto: Grupos de segurança são firewalls de rede."
                },
                {
                    "id": "B",
                    "text": "Histórico de eventos do AWS CloudTrail",
                    "explanation": "Incorreto: O CloudTrail registra atividades de API, não alocação financeira de custos."
                },
                {
                    "id": "C",
                    "text": "Tags de Alocação de Custos da AWS (AWS Cost Allocation Tags)",
                    "explanation": "Correto: As tags de alocação de custos são pares chave-valor aplicados aos recursos que aparecem nos seus relatórios de faturamento para organizar e rastrear custos por departamento, ambiente ou projeto."
                },
                {
                    "id": "D",
                    "text": "Alarmes do Amazon CloudWatch",
                    "explanation": "Incorreto: Os alarmes do CloudWatch notificam sobre violações de limites, mas não categorizam itens de linha de fatura."
                }
            ],
            "generalExplanation": "As tags de alocação de custos da AWS permitem rotular seus recursos da AWS com metadados chave-valor para acompanhar e categorizar custos em relatórios de faturamento detalhados."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "Una empresa desea organizar y realizar un seguimiento de sus costos de AWS en diferentes departamentos, proyectos y centros de costos en su factura mensual consolidada. ¿Qué característica permite a los administradores asignar metadatos de clave-valor a los recursos para la categorización de costos?",
            "options": [
                {
                    "id": "A",
                    "text": "Grupos de seguridad de AWS (AWS Security Groups)",
                    "explanation": "Incorrecto: Los grupos de seguridad son firewalls de red."
                },
                {
                    "id": "B",
                    "text": "Historial de eventos de AWS CloudTrail",
                    "explanation": "Incorrecto: CloudTrail registra la actividad de la API, no la asignación financiera de costos."
                },
                {
                    "id": "C",
                    "text": "Etiquetas de asignación de costos de AWS (AWS Cost Allocation Tags)",
                    "explanation": "Correcto: Las etiquetas de asignación de costos son pares clave-valor que se aplican a los recursos y que aparecen en sus informes de facturación para organizar y monitorear los costos por departamento, entorno o proyecto."
                },
                {
                    "id": "D",
                    "text": "Alarmas de Amazon CloudWatch",
                    "explanation": "Incorrecto: Las alarmas de CloudWatch notifican incumplimientos de umbrales, pero no clasifican partidas de facturación."
                }
            ],
            "generalExplanation": "Las etiquetas de asignación de costos de AWS le permiten etiquetar sus recursos de AWS con metadatos de clave-valor para realizar un seguimiento y categorizar los costos en informes de facturación detallados."
        }
    },
    "clf-q065": {
        "pt": {
            "domainName": "Domínio 4: Faturamento, Preços e Suporte",
            "statement": "Qual catálogo digital na AWS permite aos clientes encontrar, testar, comprar e implantar instantaneamente milhares de produtos de software de terceiros (como soluções de segurança, bancos de dados e ferramentas de DevOps) com faturamento simplificado e consolidado diretamente em sua fatura da AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Artifact",
                    "explanation": "Incorreto: O Artifact fornece relatórios e certificações de conformidade."
                },
                {
                    "id": "B",
                    "text": "AWS Service Catalog",
                    "explanation": "Incorreto: O AWS Service Catalog permite que equipes internas de TI gerenciem catálogos de recursos internos aprovados da AWS, e não compras públicas de software de terceiros (ISVs)."
                },
                {
                    "id": "C",
                    "text": "Amazon QuickSight",
                    "explanation": "Incorreto: O QuickSight é um serviço de visualização de dados de Business Intelligence."
                },
                {
                    "id": "D",
                    "text": "AWS Marketplace",
                    "explanation": "Correto: O AWS Marketplace é um catálogo digital selecionado que facilita para os clientes encontrar, comprar, implantar e gerenciar softwares de terceiros executados na AWS com faturamento unificado."
                }
            ],
            "generalExplanation": "O AWS Marketplace é um catálogo digital com milhares de ofertas de softwares de fornecedores independentes de software (ISVs) que simplifica a aquisição de software e a consolidação de faturas na AWS."
        },
        "es": {
            "domainName": "Dominio 4: Facturación, Precios y Soporte",
            "statement": "¿Qué catálogo digital de AWS permite a los clientes buscar, probar, comprar e implementar instantáneamente miles de productos de software de terceros (como dispositivos de seguridad, bases de datos y herramientas de DevOps) con facturación simplificada y consolidada directamente en su factura de AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Artifact",
                    "explanation": "Incorrecto: Artifact proporciona informes de cumplimiento y certificaciones."
                },
                {
                    "id": "B",
                    "text": "AWS Service Catalog",
                    "explanation": "Incorrecto: AWS Service Catalog permite a los equipos internos de TI administrar catálogos de recursos de AWS internos aprobados, no la compra pública de software de terceros de proveedores independientes (ISVs)."
                },
                {
                    "id": "C",
                    "text": "Amazon QuickSight",
                    "explanation": "Incorrecto: QuickSight es un servicio de visualización de datos de inteligencia empresarial."
                },
                {
                    "id": "D",
                    "text": "AWS Marketplace",
                    "explanation": "Correcto: AWS Marketplace es un catálogo digital seleccionado que facilita a los clientes encontrar, comprar, implementar y administrar software de terceros que se ejecuta en AWS con facturación unificada."
                }
            ],
            "generalExplanation": "AWS Marketplace es un catálogo digital con miles de productos de software de proveedores de software independientes (ISVs) que simplifica la adquisición de software y la facturación en AWS."
        }
    }
}
