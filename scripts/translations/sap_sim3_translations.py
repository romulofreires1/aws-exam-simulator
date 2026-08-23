"""
Translations for SAP-C02 Mock Exam 3 (sap-sim3-q001 to sap-sim3-q025).
100% natural, fluent Portuguese (PT-BR) and Spanish (ES) translations.
"""

TRANSLATIONS = {
    "sap-sim3-q001": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Um fundo soberano possui um requisito regulatório rigoroso que exige que as chaves de criptografia sejam geradas, armazenadas e gerenciadas dentro de Módulos de Segurança de Hardware (HSMs) dedicados, de locatário único (single-tenant), validados pelo FIPS 140-2 Nível 3 e diretamente sob o controle físico e lógico exclusivo dos responsáveis de segurança da empresa. A equipe da AWS deve ter zero acesso administrativo ao material das chaves no HSM. Qual serviço da AWS atende a esses requisitos de conformidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Certificate Manager (ACM) para provisionar e renovar automaticamente certificados SSL/TLS públicos.",
                    "explanation": "Incorreto: O ACM gerencia certificados públicos SSL/TLS, e não chaves corporativas simétricas de criptografia em HSMs dedicados."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster do AWS CloudHSM dentro de uma VPC privada para gerenciar hardware criptográfico de locatário único validado pelo FIPS 140-2 Nível 3.",
                    "explanation": "Correto: O AWS CloudHSM fornece módulos de segurança de hardware dedicados, single-tenant e validados pelo FIPS 140-2 Nível 3 executados na sua VPC, onde o cliente possui propriedade e controle exclusivos sobre as chaves criptográficas e a administração de usuários do HSM."
                },
                {
                    "id": "C",
                    "text": "AWS Key Management Service (AWS KMS) com repositórios de chaves padrão multi-tenant.",
                    "explanation": "Incorreto: O AWS KMS padrão utiliza HSMs multi-tenant gerenciados pela AWS, e não dispositivos single-tenant dedicados administrados exclusivamente pelo cliente."
                },
                {
                    "id": "D",
                    "text": "Armazenar flags de configuração da aplicação no AWS Secrets Manager e agendar a rotação automática de segredos.",
                    "explanation": "Incorreto: O Secrets Manager armazena credenciais de banco de dados e chaves de API, dependendo do KMS ou CloudHSM para a criptografia das chaves."
                }
            ],
            "generalExplanation": "O AWS CloudHSM fornece módulos de segurança de hardware (HSMs) dedicados e de locatário único sob controle exclusivo do cliente para atender a requisitos regulatórios rigorosos e de conformidade com o FIPS 140-2 Nível 3."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un fondo soberano tiene un estricto requisito normativo que exige que las claves de cifrado criptográficas se generen, almacenen y administren dentro de Módulos de Seguridad de Hardware (HSM) dedicados, de inquilino único (single-tenant), validados según FIPS 140-2 Nivel 3 y directamente bajo el control físico y lógico exclusivo de los oficiales de seguridad de la empresa. El personal de AWS no debe tener ningún acceso administrativo al material de las claves del HSM. ¿Qué servicio de AWS cumple con estos requisitos de conformidad?",
            "options": [
                {
                    "id": "A",
                    "text": "Utilizar AWS Certificate Manager (ACM) para aprovisionar y renovar automáticamente certificados SSL/TLS públicos.",
                    "explanation": "Incorrecto: ACM administra certificados públicos SSL/TLS, no claves corporativas de cifrado simétrico en HSM."
                },
                {
                    "id": "B",
                    "text": "Implementar un clúster de AWS CloudHSM dentro de una VPC privada para administrar hardware criptográfico de inquilino único validado según FIPS 140-2 Nivel 3.",
                    "explanation": "Correcto: AWS CloudHSM proporciona módulos de seguridad de hardware dedicados, de inquilino único y validados según FIPS 140-2 Nivel 3 que se ejecutan en su VPC, donde el cliente tiene la propiedad y el control exclusivos de las claves criptográficas y la administración de usuarios del HSM."
                },
                {
                    "id": "C",
                    "text": "AWS Key Management Service (AWS KMS) con almacenes de claves predeterminados multi-tenant.",
                    "explanation": "Incorrecto: AWS KMS estándar utiliza HSMs multi-tenant administrados por AWS, en lugar de dispositivos dedicados de inquilino único administrados por el cliente."
                },
                {
                    "id": "D",
                    "text": "Almacenar flags de configuración de la aplicación en AWS Secrets Manager y programar la rotación automática de secretos.",
                    "explanation": "Incorrecto: Secrets Manager almacena credenciales de bases de datos y claves de API, dependiendo de KMS o CloudHSM para el cifrado."
                }
            ],
            "generalExplanation": "AWS CloudHSM proporciona módulos de seguridad de hardware (HSM) dedicados de inquilino único bajo el control total del cliente para cumplir con estrictas normativas y la conformidad con FIPS 140-2 Nivel 3."
        }
    },
    "sap-sim3-q002": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Um provedor de serviços gerenciados (MSP) global administra 500 contas da AWS sob uma organização com faturamento consolidado no AWS Organizations. O MSP precisa gerar faturas pró-forma personalizadas para diferentes clientes corporativos, aplicar margens de lucro (markup) personalizadas e descontos progressivos, além de permitir que os clientes visualizem suas taxas de cobrança personalizadas em seus próprios consoles sem expor os descontos reais por volume no atacado obtidos pelo MSP junto à AWS. Qual serviço da AWS foi projetado para esse requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Cost Explorer para visualizar gastos históricos consolidados da AWS e prever o uso futuro.",
                    "explanation": "Incorreto: O Cost Explorer exibe custos e descontos históricos reais da AWS no faturamento consolidado, sem recursos de mecanismo de markup personalizado para clientes."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS Pricing Calculator para modelar custos de arquitetura antes de provisionar recursos de infraestrutura da AWS.",
                    "explanation": "Incorreto: O Pricing Calculator é uma ferramenta de estimativa de arquitetura, não um mecanismo automatizado de personalização de faturamento multi-contas em produção."
                },
                {
                    "id": "C",
                    "text": "Configurar o AWS Billing Conductor para definir grupos de faturamento personalizados, aplicar markups de preços e gerar faturas pró-forma.",
                    "explanation": "Correto: O AWS Billing Conductor é um serviço de faturamento personalizável que permite aos MSPs e empresas personalizar taxas de cobrança, agrupar contas em grupos de faturamento e gerar visualizações de faturamento pró-forma para clientes finais."
                },
                {
                    "id": "D",
                    "text": "Configurar o AWS Budgets para enviar notificações automáticas quando os limites de gastos mensais excederem limites predefinidos.",
                    "explanation": "Incorreto: O AWS Budgets envia alertas de gastos, mas não calcula markups de tarifas personalizados nem gera faturas pró-forma."
                }
            ],
            "generalExplanation": "O AWS Billing Conductor permite que clientes e MSPs personalizem parâmetros de cobrança, criem grupos de faturamento, apliquem regras de preços customizadas e apresentem faturas pró-forma aos usuários finais."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un proveedor de servicios gestionados (MSP) global administra 500 cuentas de AWS en una organización con facturación consolidada en AWS Organizations. El MSP necesita generar facturas proforma personalizadas para diferentes clientes empresariales, aplicar márgenes de recargo (markup) personalizados y descuentos por volumen, y permitir que los clientes vean sus tarifas de facturación personalizadas en sus propias consolas sin exponer los descuentos reales por volumen mayorista de AWS que recibe el MSP. ¿Qué servicio de AWS está diseñado para este requisito?",
            "options": [
                {
                    "id": "A",
                    "text": "Utilizar AWS Cost Explorer para visualizar los gastos históricos consolidados de AWS y pronosticar el uso futuro.",
                    "explanation": "Incorrecto: Cost Explorer muestra los costos y descuentos históricos reales de AWS en la facturación consolidada, sin motores de recargo personalizados para clientes."
                },
                {
                    "id": "B",
                    "text": "Utilizar AWS Pricing Calculator para modelar los costos de arquitectura antes de aprovisionar recursos de infraestructura de AWS.",
                    "explanation": "Incorrecto: Pricing Calculator es una herramienta de estimación de arquitectura, no un motor automatizado de personalización de facturación multicueenta en vivo."
                },
                {
                    "id": "C",
                    "text": "Configurar AWS Billing Conductor para definir grupos de facturación personalizados, aplicar recargos de precios y generar facturas proforma.",
                    "explanation": "Correcto: AWS Billing Conductor es un servicio de facturación personalizable que permite a los MSPs y empresas personalizar las tarifas de facturación, agrupar cuentas en grupos de facturación y generar vistas de facturación proforma para los clientes finales."
                },
                {
                    "id": "D",
                    "text": "Configurar AWS Budgets para enviar notificaciones automáticas cuando los límites de gasto mensual superen los umbrales predefinidos.",
                    "explanation": "Incorrecto: AWS Budgets envía alertas de gasto, pero no calcula recargos de tarifas personalizados ni genera facturas de facturación proforma."
                }
            ],
            "generalExplanation": "AWS Billing Conductor permite a los clientes y MSPs personalizar los parámetros de facturación, crear grupos de facturación, aplicar reglas de precios personalizadas y presentar facturas proforma a los usuarios finales."
        }
    },
    "sap-sim3-q003": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa precisa implementar a inspeção centralizada de saída de tráfego de internet (egress) para 80 VPCs em 2 regiões da AWS. Todas as solicitações web de saída devem ser inspecionadas em relação a listas de permissão de domínios TLS Server Name Indication (SNI) e conjuntos de regras Suricata de sistema de prevenção contra intrusões (IPS). A solução deve ter capacidade de escalar até 45 Gbps de tráfego de saída por região com alta disponibilidade em 3 Zonas de Disponibilidade e nenhum ponto único de falha. Qual arquitetura deve ser implantada?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma VPC de inspeção de saída centralizada em cada região contendo um anexo do AWS Transit Gateway com o Appliance Mode ativado e implantar endpoints do AWS Network Firewall em uma sub-rede de firewall dedicada em cada Zona de Disponibilidade, com suporte de um grupo de regras com estado (stateful) para filtragem SNI de domínios e regras Suricata de IPS.",
                    "explanation": "Correto: A inspeção centralizada de saída via AWS Transit Gateway com Appliance Mode e endpoints do AWS Network Firewall em 3 AZs escala até 100 Gbps, fornece filtragem stateful de domínios SNI e elimina pontos únicos de falha."
                },
                {
                    "id": "B",
                    "text": "Implantar instâncias EC2 com proxy squid em uma única instância t3.medium em cada VPC spoke.",
                    "explanation": "Incorreto: Instâncias de proxy autogerenciadas em t3.medium não suportam 45 Gbps, criam pontos únicos de falha e introduzem enorme sobrecarga operacional de manutenção."
                },
                {
                    "id": "C",
                    "text": "Configurar zonas hospedadas privadas do Amazon Route 53 em cada VPC com registros curinga apontando para 127.0.0.1.",
                    "explanation": "Incorreto: O sinkholing de DNS via Route 53 não fornece inspeção stateful de pacotes na Camada 7 (IPS) nem filtragem SNI para fluxos TCP ativos."
                },
                {
                    "id": "D",
                    "text": "Criar conexões de VPC Peering entre todas as 80 VPCs e implantar NAT Gateways em cada sub-rede spoke.",
                    "explanation": "Incorreto: Implantar NAT Gateways em centenas de sub-redes spoke é extremamente caro e não oferece inspeção centralizada de IPS/SNI com estado."
                }
            ],
            "generalExplanation": "A arquitetura de VPC de saída centralizada com AWS Transit Gateway e AWS Network Firewall oferece filtragem de domínios na Camada 7 escalável e altamente disponível, além de inspeção IPS compatível com Suricata."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa necesita implementar la inspección centralizada del tráfico de salida hacia Internet (egress) para 80 VPCs en 2 regiones de AWS. Todas las solicitudes web salientes deben inspeccionarse contra listas de permitidos de dominios TLS Server Name Indication (SNI) y conjuntos de reglas Suricata de sistema de prevención de intrusiones (IPS). La solución debe escalar hasta 45 Gbps de tráfico de salida por región con alta disponibilidad en 3 Zonas de Disponibilidad y sin puntos únicos de fallo. ¿Qué arquitectura se debe implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una VPC de inspección de salida centralizada en cada región con un adjunto de AWS Transit Gateway con Appliance Mode habilitado, e implementar endpoints de AWS Network Firewall en una subred de firewall dedicada en cada Zona de Disponibilidad respaldados por un grupo de reglas con estado para filtrado de dominios por SNI y reglas Suricata de IPS.",
                    "explanation": "Correcto: La inspección centralizada de salida a través de AWS Transit Gateway con Appliance Mode y endpoints de AWS Network Firewall en 3 AZ escala hasta 100 Gbps, proporciona filtrado de dominios SNI con estado y elimina puntos únicos de fallo."
                },
                {
                    "id": "B",
                    "text": "Implementar instancias EC2 de proxy squid en una única instancia t3.medium en cada VPC spoke.",
                    "explanation": "Incorrecto: Las instancias proxy autogestionadas en t3.medium no pueden manejar 45 Gbps, crean puntos únicos de fallo e introducen un mantenimiento operativo masivo."
                },
                {
                    "id": "C",
                    "text": "Configurar zonas alojadas privadas de Amazon Route 53 en cada VPC con registros comodín que apunten a 127.0.0.1.",
                    "explanation": "Incorrecto: El sinkholing de DNS con Route 53 no proporciona inspección de paquetes IPS de Capa 7 con estado ni filtrado SNI para flujos TCP activos."
                },
                {
                    "id": "D",
                    "text": "Crear conexiones de VPC Peering entre las 80 VPCs e implementar NAT Gateways en cada subred spoke.",
                    "explanation": "Incorrecto: Implementar NAT Gateways en cientos de subredes spoke resulta extremadamente costoso y carece de inspección centralizada con estado de IPS/SNI."
                }
            ],
            "generalExplanation": "La arquitectura centralizada de VPC de salida con AWS Transit Gateway y AWS Network Firewall proporciona filtrado de dominios en Capa 7 escalable y altamente disponible, además de inspección IPS compatible con Suricata."
        }
    },
    "sap-sim3-q004": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Um pipeline automatizado de processamento de dados executado em uma instância EC2 na Conta A precisa acessar um bucket do Amazon S3 na Conta B. Para maior segurança, a Conta B exige que a role do IAM na Conta A forneça um External ID ao assumir a role entre contas para evitar o problema do 'Confused Deputy' (representante confuso). Como a política de confiança (trust policy) do IAM na Conta B deve ser configurada?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar um usuário do IAM na Conta B com uma chave de acesso e enviar a chave secreta em texto sem formatação para a Conta A por e-mail.",
                    "explanation": "Incorreto: A distribuição de credenciais estáticas de longo prazo do IAM viola as práticas recomendadas de segurança e não resolve a vulnerabilidade do representante confuso."
                },
                {
                    "id": "B",
                    "text": "Adicionar uma política de bucket pública de leitura/gravação no bucket S3 na Conta B.",
                    "explanation": "Incorreto: Tornar o bucket público expõe todos os dados à internet."
                },
                {
                    "id": "C",
                    "text": "Configurar a política de confiança da role do IAM na Conta B com a ação `sts:AssumeRole`, especificando a role da Conta A como Principal, e adicionar um bloco `Condition` exigindo que `sts:ExternalId` corresponda à cadeia de identificador exclusivo compartilhado.",
                    "explanation": "Correto: O problema do Confused Deputy é mitigado exigindo que a assunção de role entre contas forneça um `sts:ExternalId` no bloco `Condition` da política de confiança da role do IAM."
                },
                {
                    "id": "D",
                    "text": "Configurar o VPC Peering e desativar totalmente a autorização do IAM.",
                    "explanation": "Incorreto: O VPC Peering opera na camada de rede e não ignora nem configura a autorização de confiança de roles do IAM."
                }
            ],
            "generalExplanation": "O uso de um External ID no bloco `Condition` da política de confiança de uma role do IAM é o mecanismo padrão da AWS para evitar o problema do Confused Deputy durante a assunção de roles entre contas."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Un canal automatizado de procesamiento de datos que se ejecuta en una instancia EC2 en la Cuenta A necesita acceder a un bucket de Amazon S3 en la Cuenta B. Para mayor seguridad, la Cuenta B requiere que el rol de IAM en la Cuenta A proporcione un External ID al asumir el rol entre cuentas para evitar el problema del 'Confused Deputy' (diputado confundido). ¿Cómo se debe configurar la política de confianza de IAM en la Cuenta B?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear un usuario de IAM en la Cuenta B con una clave de acceso y enviar la clave secreta en texto plano a la Cuenta A por correo electrónico.",
                    "explanation": "Incorrecto: Distribuir credenciales estáticas de IAM a largo plazo viola las mejores prácticas de seguridad y no soluciona la vulnerabilidad del diputado confundido."
                },
                {
                    "id": "B",
                    "text": "Agregar una política de bucket pública de lectura/escritura en el bucket S3 de la Cuenta B.",
                    "explanation": "Incorrecto: Hacer que el bucket sea público expone todos los datos a Internet."
                },
                {
                    "id": "C",
                    "text": "Configurar la política de confianza del rol de IAM en la Cuenta B con la acción `sts:AssumeRole`, especificando el rol de la Cuenta A como Principal, y agregar un bloque `Condition` que requiera `sts:ExternalId` coincidente con la cadena de identificador único compartido.",
                    "explanation": "Correcto: El problema del Confused Deputy se mitiga requiriendo que la asunción del rol entre cuentas proporcione un `sts:ExternalId` en el bloque `Condition` de la política de confianza del rol de IAM."
                },
                {
                    "id": "D",
                    "text": "Configurar VPC Peering y deshabilitar completamente la autorización de IAM.",
                    "explanation": "Incorrecto: VPC Peering opera en la capa de red y no elude ni configura la autorización de confianza de roles de IAM."
                }
            ],
            "generalExplanation": "El uso de un External ID en el bloque `Condition` de la política de confianza de un rol de IAM es el mecanismo estándar de AWS para evitar el problema del Confused Deputy durante la asunción de roles entre cuentas."
        }
    },
    "sap-sim3-q005": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma empresa executa 1.000 instâncias do Amazon EC2 Windows Server em várias contas da AWS em uma organização do AWS Organizations. As instâncias devem ingressar perfeitamente em um domínio do Active Directory para gerenciamento centralizado de Objetos de Política de Grupo (GPOs) e autenticação Kerberos. A empresa deseja minimizar o tráfego para os controladores de domínio locais via Direct Connect e eliminar a criação manual de scripts de ingresso no domínio. Qual solução é a mais adequada?",
            "options": [
                {
                    "id": "A",
                    "text": "Apontar todas as 1.000 instâncias EC2 em todas as contas diretamente para os endereços IP dos controladores de domínio locais pela internet pública.",
                    "explanation": "Incorreto: Expor portas do Active Directory na internet pública representa uma grande vulnerabilidade de segurança e cria alta latência de rede."
                },
                {
                    "id": "B",
                    "text": "Criar usuários administradores locais do Windows em cada instância EC2 usando o EC2 User Data.",
                    "explanation": "Incorreto: O gerenciamento de usuários locais em 1.000 instâncias carece de governança de domínio centralizada, GPOs e SSO com Kerberos."
                },
                {
                    "id": "C",
                    "text": "Implantar pools de usuários do Amazon Cognito e configurar o login do Windows via OAuth 2.0.",
                    "explanation": "Incorreto: O ingresso no domínio do Windows Server Active Directory e as GPOs exigem o Microsoft Active Directory nativo / Kerberos / LDAP, e não o Cognito."
                },
                {
                    "id": "D",
                    "text": "Implantar o AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) em uma conta de Serviços compartilhados, estabelecer uma relação de confiança de floresta bidirecional com o Active Directory local, compartilhar o diretório com as contas-membro via AWS RAM e usar o AWS Systems Manager Seamless Domain Join.",
                    "explanation": "Correto: O AWS Managed Microsoft AD implantado na AWS com uma relação de confiança de floresta para o AD local permite autenticação de domínio local de baixa latência na AWS, e o SSM Seamless Domain Join automatiza o ingresso no domínio entre contas sem scripts personalizados."
                }
            ],
            "generalExplanation": "O AWS Managed Microsoft AD compartilhado entre contas combinado com uma relação de confiança de floresta e o AWS Systems Manager Seamless Domain Join oferece uma arquitetura de diretório corporativo escalável e altamente disponível."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una empresa ejecuta 1.000 instancias de Amazon EC2 Windows Server en múltiples cuentas de AWS en una organización de AWS Organizations. Las instancias deben unirse de forma fluida a un dominio de Active Directory para el uso centralizado de Objetos de Directiva de Grupo (GPO) y autenticación Kerberos. La empresa desea minimizar el tráfico hacia los controladores de dominio locales a través de Direct Connect y eliminar la creación manual de scripts de unión al dominio. ¿Qué solución es la más adecuada?",
            "options": [
                {
                    "id": "A",
                    "text": "Apuntar las 1.000 instancias EC2 en todas las cuentas directamente a las direcciones IP de los controladores de dominio locales a través de la Internet pública.",
                    "explanation": "Incorrecto: Exponer los puertos de Active Directory en la Internet pública supone una vulnerabilidad de seguridad grave y genera una alta latencia de red."
                },
                {
                    "id": "B",
                    "text": "Crear usuarios Administradores locales de Windows en cada instancia EC2 utilizando EC2 User Data.",
                    "explanation": "Incorrecto: La administración de usuarios locales en 1.000 instancias carece de gobernanza de dominio centralizada, GPOs y SSO con Kerberos."
                },
                {
                    "id": "C",
                    "text": "Implementar grupos de usuarios de Amazon Cognito y configurar el inicio de sesión de Windows mediante OAuth 2.0.",
                    "explanation": "Incorrecto: La unión al dominio de Windows Server Active Directory y las GPOs requieren Microsoft Active Directory nativo / Kerberos / LDAP, no Cognito."
                },
                {
                    "id": "D",
                    "text": "Implementar AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) en una cuenta de Servicios compartidos, establecer una relación de confianza de bosque bidireccional con el Active Directory local, compartir el directorio con las cuentas miembro mediante AWS RAM y utilizar AWS Systems Manager Seamless Domain Join.",
                    "explanation": "Correcto: AWS Managed Microsoft AD implementado en AWS con una relación de confianza de bosque hacia el AD local permite autenticación de dominio local de baja latencia en AWS, y SSM Seamless Domain Join automatiza la unión al dominio entre cuentas sin scripts personalizados."
                }
            ],
            "generalExplanation": "AWS Managed Microsoft AD compartido entre cuentas combinado con una relación de confianza de bosque y AWS Systems Manager Seamless Domain Join proporciona una arquitectura de directorio empresarial escalable y altamente disponible."
        }
    },
    "sap-sim3-q006": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma organização exige auditoria contínua de conformidade em 100 contas da AWS em relação aos padrões CIS AWS Foundations Benchmark e PCI-DSS. Os achados de recursos não compatíveis devem ser consolidados automaticamente em uma conta central de segurança, e os relatórios executivos de conformidade devem ser visíveis em um único painel. Qual serviço deve ser designado como o gerenciador central de postura de conformidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar uma instância EC2 em cada conta-membro executando scripts personalizados de código aberto para verificação de conformidade e salvar os arquivos de saída no S3.",
                    "explanation": "Incorreto: Scripts de varredura personalizados em 100 instâncias EC2 geram alta manutenção, não oferecem avaliação contínua e exigem código de agregação customizado."
                },
                {
                    "id": "B",
                    "text": "Configurar o AWS Budgets para enviar notificações automáticas quando os limites de gastos mensais excederem limites predefinidos.",
                    "explanation": "Incorreto: O AWS Budgets rastreia limites de custos financeiros, e não padrões de configuração de segurança."
                },
                {
                    "id": "C",
                    "text": "Designar uma conta de Auditoria de Segurança como administrador delegado do AWS Security Hub, habilitar o Security Hub em todas as contas-membro com os padrões CIS AWS Foundations e PCI-DSS ativados e visualizar as pontuações de conformidade agregadas no painel central.",
                    "explanation": "Correto: O AWS Security Hub fornece verificações de conformidade automatizadas e contínuas em relação a padrões de segurança da indústria (CIS, PCI-DSS, NIST), com pontuação consolidada e agregação de achados multi-contas."
                },
                {
                    "id": "D",
                    "text": "Configurar o Amazon CloudWatch Logs Insights para verificar diariamente os VPC Flow Logs brutos.",
                    "explanation": "Incorreto: Os VPC Flow Logs contêm registros de fluxo de rede, e não dados de conformidade de configuração básica do IAM, S3 e CIS."
                }
            ],
            "generalExplanation": "O AWS Security Hub agrega, organiza e prioriza achados de segurança de serviços suportados da AWS e avalia ambientes de várias contas em relação a padrões regulatórios como CIS e PCI-DSS."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una organización requiere auditoría continua de cumplimiento en 100 cuentas de AWS frente a los estándares CIS AWS Foundations Benchmark y PCI-DSS. Los hallazgos de recursos no conformes deben consolidarse automáticamente en una cuenta de seguridad central, y los paneles de puntuación de cumplimiento ejecutivo deben ser visibles en un único panel. ¿Qué servicio debe designarse como administrador central de la postura de cumplimiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar una instancia EC2 en cada cuenta miembro que ejecute scripts personalizados de escaneo de cumplimiento de código abierto y guardar los archivos de salida en S3.",
                    "explanation": "Incorrecto: Los scripts de escaneo personalizados en 100 instancias EC2 introducen un alto mantenimiento, carecen de evaluación continua y requieren código de agregación personalizado."
                },
                {
                    "id": "B",
                    "text": "Configurar AWS Budgets para enviar notificaciones automáticas cuando los límites de gasto mensual superen los umbrales predefinidos.",
                    "explanation": "Incorrecto: AWS Budgets realiza un seguimiento de los umbrales de costos financieros, no de los estándares de configuración de seguridad."
                },
                {
                    "id": "C",
                    "text": "Designar una cuenta de Auditoría de Seguridad como administrador delegado de AWS Security Hub, habilitar Security Hub en todas las cuentas miembro con los estándares CIS AWS Foundations y PCI-DSS activados, y ver las puntuaciones de cumplimiento agregadas en el panel central.",
                    "explanation": "Correcto: AWS Security Hub proporciona comprobaciones de cumplimiento continuas y automatizadas frente a los estándares de la industria de la seguridad (CIS, PCI-DSS, NIST) con puntuación consolidada de múltiples cuentas y agregación de hallazgos."
                },
                {
                    "id": "D",
                    "text": "Configurar Amazon CloudWatch Logs Insights para escanear diariamente los VPC Flow Logs sin procesar.",
                    "explanation": "Incorrecto: Los VPC Flow Logs contienen registros de flujo de red, no datos de cumplimiento de configuración fundamental de IAM, S3 y CIS."
                }
            ],
            "generalExplanation": "AWS Security Hub agrega, organiza y prioriza los hallazgos de seguridad de los servicios compatibles de AWS y evalúa los entornos de múltiples cuentas frente a estándares regulatorios como CIS y PCI-DSS."
        }
    },
    "sap-sim3-q007": {
        "pt": {
            "domainName": "Domínio 1: Projetar Soluções para Complexidade Organizacional",
            "statement": "Uma landing zone corporativa gerenciada pelo AWS Control Tower precisa automatizar o provisionamento de contas para novas equipes de engenharia. O processo de criação de contas deve provisionar uma conta da AWS dedicada, associá-la à Unidade Organizacional (OU) apropriada, aplicar Service Control Policies (SCPs) de linha de base, configurar conjuntos de permissões do IAM Identity Center e inicializar a conectividade de rede via Transit Gateway automaticamente por meio da aprovação de um chamado no ServiceNow. Qual solução viabiliza esse fluxo de trabalho automatizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Control Tower Account Factory integrado ao conector do AWS Service Catalog para ServiceNow (ou Account Factory for Terraform - AFT) para automatizar o provisionamento de contas de ponta a ponta mediante aprovação do chamado.",
                    "explanation": "Correto: O AWS Control Tower Account Factory e o Account Factory for Terraform (AFT) automatizam a criação padronizada de contas, guardrails de governança e provisionamento de rede por meio de integração via API/ITSM."
                },
                {
                    "id": "B",
                    "text": "Instruir um administrador a fazer login manualmente no Console de Gerenciamento da AWS para criar as contas uma a uma.",
                    "explanation": "Incorreto: A criação manual de contas no console é lenta, propensa a erros e não se integra automaticamente às aprovações de chamados do ServiceNow."
                },
                {
                    "id": "C",
                    "text": "Implantar uma função AWS Lambda que executa a chamada `create-user` em todas as contas.",
                    "explanation": "Incorreto: A chamada `create-user` cria usuários individuais do IAM, e não novas contas completas da AWS no AWS Organizations."
                },
                {
                    "id": "D",
                    "text": "Anexar uma Service Control Policy (SCP) ao endereço IP do ServiceNow.",
                    "explanation": "Incorreto: As SCPs são aplicadas a OUs e contas do AWS Organizations, e não a endereços IP de terceiros."
                }
            ],
            "generalExplanation": "O AWS Control Tower Account Factory e o Account Factory for Terraform (AFT) automatizam o provisionamento padronizado e governado de várias contas integrado a ferramentas corporativas de ITSM, como o ServiceNow."
        },
        "es": {
            "domainName": "Dominio 1: Diseñar Soluciones para la Complejidad Organizacional",
            "statement": "Una landing zone empresarial administrada por AWS Control Tower necesita automatizar el aprovisionamiento de cuentas para nuevos equipos de ingeniería. El proceso de creación de cuentas debe aprovisionar una cuenta de AWS dedicada, adjuntarla a la Unidad Organizativa (OU) correspondiente, aplicar Service Control Policies (SCPs) de referencia, configurar conjuntos de permisos de IAM Identity Center e inicializar la conectividad de red mediante Transit Gateway automáticamente a través de la aprobación de un ticket en ServiceNow. ¿Qué solución habilita este flujo de trabajo automatizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Utilizar AWS Control Tower Account Factory integrado con el conector de AWS Service Catalog para ServiceNow (o Account Factory for Terraform - AFT) para automatizar el aprovisionamiento integral de cuentas tras la aprobación del ticket.",
                    "explanation": "Correcto: AWS Control Tower Account Factory y Account Factory for Terraform (AFT) automatizan la creación estandarizada de cuentas, las barreras de protección de gobernanza y el aprovisionamiento de red mediante la integración de API/ITSM."
                },
                {
                    "id": "B",
                    "text": "Indicar a un administrador que inicie sesión manualmente en la Consola de Administración de AWS para crear las cuentas una por una.",
                    "explanation": "Incorrecto: La creación manual de cuentas en la consola es lenta, propensa a errores y no puede integrarse automáticamente con las aprobaciones de tickets de ServiceNow."
                },
                {
                    "id": "C",
                    "text": "Implementar una función AWS Lambda que llame a `create-user` en todas las cuentas.",
                    "explanation": "Incorrecto: `create-user` crea usuarios individuales de IAM, no cuentas completas nuevas de AWS dentro de AWS Organizations."
                },
                {
                    "id": "D",
                    "text": "Adjuntar una Service Control Policy (SCP) a la dirección IP de ServiceNow.",
                    "explanation": "Incorrecto: Las SCP se aplican a las OUs y cuentas de AWS Organizations, no a direcciones IP externas de terceros."
                }
            ],
            "generalExplanation": "AWS Control Tower Account Factory y Account Factory for Terraform (AFT) automatizan el aprovisionamiento estandarizado y gobernado de múltiples cuentas integrado con herramientas de ITSM empresariales como ServiceNow."
        }
    },
    "sap-sim3-q008": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Uma empresa financeira multinacional armazena 10 petabytes de arquivos históricos de transações em um bucket do Amazon S3 na região us-east-1. Para atender aos novos requisitos de recuperação de desastres e conformidade de residência de dados, todos os objetos recém-enviados E todos os 10 petabytes existentes de objetos históricos devem ser replicados para um bucket secundário na região eu-west-1. Os objetos são criptografados com uma chave gerenciada pelo cliente do AWS KMS (SSE-KMS). Qual combinação de ações deve ser realizada para replicar tanto os dados novos quanto os existentes?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o S3 Versioning em ambos os buckets, configurar a Replicação Entre Regiões (CRR) do S3 com opções de criptografia KMS e uma chave KMS de destino especificada, e iniciar um trabalho de Amazon S3 Batch Replication para replicar os objetos pré-existentes.",
                    "explanation": "Correto: O S3 CRR padrão replica apenas objetos recém-carregados após a criação da regra. Replicar objetos existentes exige a criação de um job do Amazon S3 Batch Replication, além da configuração do CRR com permissões SSE-KMS."
                },
                {
                    "id": "B",
                    "text": "Habilitar a Replicação Entre Regiões (CRR) do S3 e aguardar 24 horas para que a AWS sincronize automaticamente todos os objetos históricos.",
                    "explanation": "Incorreto: As regras padrão do S3 CRR NÃO replicam automaticamente objetos que existiam antes da criação da regra sem um job do S3 Batch Replication."
                },
                {
                    "id": "C",
                    "text": "Usar o comando da CLI da AWS `aws s3 cp` em uma instância EC2 t3.nano pela internet pública.",
                    "explanation": "Incorreto: Uma instância EC2 t3.nano ficará sem memória, levará meses para transferir 10 PB pela internet e custará significativamente mais do que a replicação nativa em lote do S3."
                },
                {
                    "id": "D",
                    "text": "Alterar a classe de armazenamento do bucket de origem para S3 Glacier Flexible Archive para acionar o espelhamento automático entre regiões.",
                    "explanation": "Incorreto: As transições de classe de armazenamento não replicam dados entre regiões da AWS."
                }
            ],
            "generalExplanation": "O Amazon S3 Batch Replication permite replicar objetos existentes que estavam armazenados em um bucket antes da configuração da Replicação Entre Regiões (CRR) do S3."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Una empresa financiera multinacional almacena 10 petabytes de archivos de transacciones históricas en un bucket de Amazon S3 en us-east-1. Para cumplir con los nuevos requisitos de recuperación ante desastres y cumplimiento de residencia de datos, todos los objetos recién cargados Y todos los 10 petabytes existentes de objetos históricos deben replicarse en un bucket secundario en eu-west-1. Los objetos están cifrados con una clave administrada por el cliente de AWS KMS (SSE-KMS). ¿Qué combinación de acciones se debe tomar para replicar tanto los datos nuevos como los existentes?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar el control de versiones de S3 (S3 Versioning) en ambos buckets, configurar la replicación entre regiones (CRR) de S3 con opciones de cifrado KMS y una clave KMS de destino especificada, e iniciar un trabajo de Amazon S3 Batch Replication para replicar los objetos preexistentes.",
                    "explanation": "Correcto: El S3 CRR estándar solo replica los objetos recién cargados después de crear la regla. La replicación de objetos existentes requiere la creación de un trabajo de Amazon S3 Batch Replication además de configurar CRR con permisos SSE-KMS."
                },
                {
                    "id": "B",
                    "text": "Habilitar la replicación entre regiones (CRR) de S3 y esperar 24 horas a que AWS sincronice automáticamente todos los objetos históricos.",
                    "explanation": "Incorrecto: Las reglas estándar de CRR de S3 NO replican automáticamente los objetos que existían antes de la creación de la regla sin un trabajo de S3 Batch Replication."
                },
                {
                    "id": "C",
                    "text": "Utilizar el comando de AWS CLI `aws s3 cp` en una instancia EC2 t3.nano a través de la Internet pública.",
                    "explanation": "Incorrecto: Una instancia EC2 t3.nano se quedará sin memoria, tardará meses en transferir 10 PB por Internet y costará sustancialmente más que la replicación nativa de S3 Batch Replication."
                },
                {
                    "id": "D",
                    "text": "Cambiar la clase de almacenamiento del bucket de origen a S3 Glacier Flexible Archive para activar la duplicación automática entre regiones.",
                    "explanation": "Incorrecto: Las transiciones de clase de almacenamiento no replican datos entre regiones de AWS."
                }
            ],
            "generalExplanation": "Amazon S3 Batch Replication le permite replicar objetos existentes que se almacenaron en un bucket antes de configurar la replicación entre regiones (CRR) de S3."
        }
    },
    "sap-sim3-q009": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Uma empresa global de jogos está desenvolvendo uma plataforma de jogos multijogador ativo-ativo implantada em três regiões da AWS: us-east-1, eu-central-1 e ap-northeast-1. Os jogadores devem ser capazes de ler e gravar dados de inventário localmente na região mais próxima com latência de dígito único em milissegundos, e os dados devem ser replicados bidirecionalmente em todas as três regiões com resolução automática de conflitos baseada em carimbos de data/hora (timestamps). Qual solução de banco de dados atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon RDS PostgreSQL Multi-AZ com réplicas de leitura entre regiões em todas as três regiões.",
                    "explanation": "Incorreto: As réplicas de leitura do RDS são somente leitura; elas não permitem gravações transacionais ativas locais nas regiões secundárias."
                },
                {
                    "id": "B",
                    "text": "Amazon DocumentDB com trabalhos periódicos de exportação e importação no S3.",
                    "explanation": "Incorreto: A exportação/importação periódica pelo S3 introduz horas de latência e não oferece suporte à replicação multi-região ativo-ativo em tempo real."
                },
                {
                    "id": "C",
                    "text": "Amazon DynamoDB Global Tables (versão 2019.11.21) implantado nas três regiões com escalabilidade automática (auto-scaling) configurada.",
                    "explanation": "Correto: O Amazon DynamoDB Global Tables fornece replicação multi-região ativo-ativo totalmente gerenciada com latência de leitura/gravação local de dígito único em milissegundos e resolução automática de conflitos baseada em 'a última gravação vence' (last-writer-wins)."
                },
                {
                    "id": "D",
                    "text": "Configurar e implantar a cópia de snapshots entre regiões do Amazon Redshift seguindo as melhores práticas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O Redshift é um data warehouse analítico, e não um banco de dados transacional em tempo real para jogos."
                }
            ],
            "generalExplanation": "O Amazon DynamoDB Global Tables permite a replicação de dados multi-região ativo-ativo totalmente gerenciada, oferecendo latência de leitura/gravação local inferior a 10 ms para bases de usuários globais."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Una empresa global de videojuegos está desarrollando una plataforma de juegos multijugador activo-activo implementada en tres regiones de AWS: us-east-1, eu-central-1 y ap-northeast-1. Los jugadores deben poder leer y escribir datos del inventario localmente en su región más cercana con latencia de un solo dígito de milisegundos, y los datos deben replicarse bidireccionalmente en las tres regiones con resolución automática de conflictos basada en marcas de tiempo. ¿Qué solución de base de datos cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon RDS PostgreSQL Multi-AZ con réplicas de lectura entre regiones en las tres regiones.",
                    "explanation": "Incorrecto: Las réplicas de lectura de RDS son de solo lectura; no permiten escrituras transaccionales activo-activo locales en regiones secundarias."
                },
                {
                    "id": "B",
                    "text": "Amazon DocumentDB con trabajos periódicos de exportación e importación en S3.",
                    "explanation": "Incorrecto: La exportación/importación periódica en S3 introduce horas de latencia y no admite la replicación multirregión activo-activo en tiempo real."
                },
                {
                    "id": "C",
                    "text": "Amazon DynamoDB Global Tables (versión 2019.11.21) implementadas en las tres regiones con escalado automático configurado.",
                    "explanation": "Correcto: Amazon DynamoDB Global Tables proporciona replicación multirregión activo-activo totalmente administrada con latencia de lectura/escritura local de un solo dígito de milisegundos y resolución automática de conflictos de 'el último que escribe gana' (last-writer-wins)."
                },
                {
                    "id": "D",
                    "text": "Configurar e implementar la copia de instantáneas entre regiones de Amazon Redshift siguiendo las mejores prácticas de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Redshift es un almacén de datos analítico (data warehouse), no una base de datos transaccional en tiempo real para videojuegos."
                }
            ],
            "generalExplanation": "Amazon DynamoDB Global Tables permite la replicación de datos activo-activo multirregión totalmente administrada, ofreciendo una latencia de lectura/escritura local inferior a 10 ms para bases de usuarios globales."
        }
    },
    "sap-sim3-q010": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Uma empresa corporativa executa aplicações críticas do Windows em instâncias do Amazon EC2 e servidores Windows locais. As aplicações exigem um sistema de arquivos compartilhado do Microsoft Windows totalmente gerenciado que suporte o protocolo SMB, permissões de arquivos NTFS do Windows, integração com o Microsoft Active Directory, DFS Namespaces e alta disponibilidade Multi-AZ com latência submilisegundo. Qual serviço de armazenamento o arquiteto deve escolher?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Elastic File System (Amazon EFS) com modo Max I/O.",
                    "explanation": "Incorreto: O Amazon EFS é um sistema de arquivos NFSv4 projetado para ambientes Linux e não suporta SMB do Windows ou ACLs NTFS nativas."
                },
                {
                    "id": "B",
                    "text": "Amazon FSx for Windows File Server implantado em uma configuração Multi-AZ integrado com o Microsoft Active Directory.",
                    "explanation": "Correto: O Amazon FSx for Windows File Server é construído sobre o Windows Server, fornecendo suporte nativo a SMB, permissões NTFS, integração com Active Directory, DFS Namespaces e failover automático Multi-AZ."
                },
                {
                    "id": "C",
                    "text": "Configurar e implantar o Amazon S3 Standard com o S3 File Gateway seguindo as melhores práticas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O S3 File Gateway destina-se ao armazenamento em cache de backup híbrido, não a um sistema de arquivos transacional nativo do Windows de alto desempenho Multi-AZ com DFS."
                },
                {
                    "id": "D",
                    "text": "Volumes Amazon EBS gp3 configurados com EBS Multi-Attach entre Zonas de Disponibilidade.",
                    "explanation": "Incorreto: O EBS Multi-Attach é suportado apenas em volumes io2 dentro de uma única AZ, não entre múltiplas Zonas de Disponibilidade, e requer um sistema de arquivos com reconhecimento de cluster (cluster-aware)."
                }
            ],
            "generalExplanation": "O Amazon FSx for Windows File Server fornece armazenamento de arquivos nativo do Microsoft Windows totalmente gerenciado com suporte a SMB, ACLs NTFS completas, integração com o AD e alta disponibilidade Multi-AZ."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Una empresa corporativa ejecuta aplicaciones críticas de Windows en instancias de Amazon EC2 y servidores Windows locales. Las aplicaciones requieren un sistema de archivos compartido de Microsoft Windows totalmente administrado que admita el protocolo SMB, permisos de archivos NTFS de Windows, integración con Microsoft Active Directory, DFS Namespaces y alta disponibilidad Multi-AZ con latencia inferior al milisegundo. ¿Qué servicio de almacenamiento debe elegir el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Elastic File System (Amazon EFS) con modo Max I/O.",
                    "explanation": "Incorrecto: Amazon EFS es un sistema de archivos NFSv4 diseñado para entornos Linux y no admite SMB de Windows ni ACLs NTFS nativas."
                },
                {
                    "id": "B",
                    "text": "Amazon FSx for Windows File Server implementado en una configuración Multi-AZ integrado con Microsoft Active Directory.",
                    "explanation": "Correcto: Amazon FSx for Windows File Server está basado en Windows Server, lo que proporciona compatibilidad nativa con SMB, permisos NTFS, integración con Active Directory, DFS Namespaces y conmutación por error automática Multi-AZ."
                },
                {
                    "id": "C",
                    "text": "Configurar e implementar Amazon S3 Standard con S3 File Gateway siguiendo las mejores prácticas del marco AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: S3 File Gateway está diseñado para almacenamiento en caché de copias de seguridad híbridas, no como un sistema de archivos transaccional nativo de Windows Multi-AZ de alto rendimiento con DFS."
                },
                {
                    "id": "D",
                    "text": "Volúmenes Amazon EBS gp3 configurados con EBS Multi-Attach entre Zonas de Disponibilidad.",
                    "explanation": "Incorrecto: EBS Multi-Attach solo se admite en volúmenes io2 dentro de una sola AZ, no entre múltiples Zonas de Disponibilidad, y requiere un sistema de archivos compatible con clústeres."
                }
            ],
            "generalExplanation": "Amazon FSx for Windows File Server proporciona almacenamiento de archivos nativo de Microsoft Windows totalmente administrado con compatibilidad con SMB, ACLs NTFS completas, integración con AD y alta disponibilidad Multi-AZ."
        }
    },
    "sap-sim3-q011": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Um marketplace de comércio eletrônico com milhões de anúncios de produtos precisa implementar uma funcionalidade de pesquisa inteligente com preenchimento automático (autocomplete) e busca de texto completo compatível com correspondência aproximada (fuzzy), tolerância a erros de digitação, sinônimos e filtros por facetas (por marca, preço, classificação). O banco de dados principal é o Amazon DynamoDB. Como o pipeline de indexação de busca deve ser arquitetado?",
            "options": [
                {
                    "id": "A",
                    "text": "Transmitir modificações de itens do DynamoDB via DynamoDB Streams para uma função AWS Lambda que indexa documentos no Amazon OpenSearch Service e direcionar as consultas de busca das aplicações clientes para o OpenSearch Service.",
                    "explanation": "Correto: O DynamoDB Streams com Lambda fornece sincronização quase em tempo real de registros do banco de dados no Amazon OpenSearch Service, que é desenvolvido para correspondência fuzzy, filtragem por facetas e pesquisa de texto completo tolerante a erros de digitação."
                },
                {
                    "id": "B",
                    "text": "Armazenar todas as descrições de produtos no Amazon S3 e executar consultas SQL no Amazon Athena a cada tecla pressionada pelo usuário.",
                    "explanation": "Incorreto: As consultas do Athena levam segundos para serem executadas e não são adequadas para barras de pesquisa em tempo real com preenchimento automático em menos de 100 ms."
                },
                {
                    "id": "C",
                    "text": "Executar operações `Scan` no DynamoDB com expressões de filtro complexas a cada tecla digitada pelos usuários na barra de pesquisa.",
                    "explanation": "Incorreto: A execução de varreduras (`Scan`) em milhões de itens a cada tecla consome imensas RCUs, introduz alta latência e não suporta correspondência fuzzy de erros de digitação."
                },
                {
                    "id": "D",
                    "text": "Implantar um cluster do Amazon ElastiCache for Memcached para executar consultas SQL de texto completo.",
                    "explanation": "Incorreto: O Memcached é um cache de chave-valor em memória simples, e não um mecanismo de pesquisa com tokenizadores de texto completo e filtros de sinônimos."
                }
            ],
            "generalExplanation": "A combinação do Amazon DynamoDB como armazenamento de dados transacional com o Amazon OpenSearch Service para pesquisa e indexação de texto completo (via DynamoDB Streams) fornece a arquitetura ideal para busca em e-commerce."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Un marketplace de comercio electrónico con millones de listados de productos necesita implementar una función de búsqueda inteligente con autocompletado y búsqueda de texto completo que admita coincidencias aproximadas (fuzzy), tolerancia a errores tipográficos, sinónimos y filtrado por facetas (por marca, precio, calificación). La base de datos principal es Amazon DynamoDB. ¿Cómo se debe diseñar la arquitectura del canal de indexación de búsqueda?",
            "options": [
                {
                    "id": "A",
                    "text": "Transmitir las modificaciones de elementos de DynamoDB a través de DynamoDB Streams a una función AWS Lambda que indexe los documentos en Amazon OpenSearch Service, y dirigir las consultas de búsqueda de las aplicaciones cliente a OpenSearch Service.",
                    "explanation": "Correcto: DynamoDB Streams junto con Lambda proporciona una sincronización casi en tiempo real de los registros de la base de datos en Amazon OpenSearch Service, que está especialmente diseñado para coincidencias aproximadas, facetas y búsqueda de texto completo con tolerancia a errores tipográficos."
                },
                {
                    "id": "B",
                    "text": "Almacenar todas las descripciones de productos en Amazon S3 y ejecutar consultas SQL de Amazon Athena en cada pulsación de tecla del usuario.",
                    "explanation": "Incorrecto: Las consultas de Athena tardan segundos en ejecutarse y no son adecuadas para barras de autocompletado de búsqueda en tiempo real de menos de 100 ms."
                },
                {
                    "id": "C",
                    "text": "Ejecutar operaciones `Scan` de DynamoDB con expresiones de filtro complejas en cada pulsación de tecla escrita por los usuarios en la barra de búsqueda.",
                    "explanation": "Incorrecto: Ejecutar consultas `Scan` en millones de elementos en cada pulsación de tecla consume enormes RCUs, introduce una latencia severa y no admite coincidencias difusas de errores tipográficos."
                },
                {
                    "id": "D",
                    "text": "Implementar un clúster de Amazon ElastiCache for Memcached para ejecutar consultas SQL de texto completo.",
                    "explanation": "Incorrecto: Memcached es una caché simple en memoria de clave-valor, no un motor de búsqueda con tokenizadores de texto completo y filtros de sinónimos."
                }
            ],
            "generalExplanation": "Combinar Amazon DynamoDB como almacén de datos transaccional con Amazon OpenSearch Service para indexación y búsqueda de texto completo (a través de DynamoDB Streams) proporciona la arquitectura óptima para la búsqueda en comercio electrónico."
        }
    },
    "sap-sim3-q012": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Uma empresa de manufatura industrial está implantando 200.000 sensores de temperatura IoT em instalações de produção em todo o mundo. Os sensores publicam mensagens de telemetria a cada 5 segundos via MQTT com autenticação mútua TLS (mTLS). O sistema deve ingerir a telemetria dos sensores, rotear os dados para um banco de dados de séries temporais dedicado e otimizado para análises de séries temporais e consultas SQL, e acionar alarmes de emergência automatizados se a temperatura exceder 95°C. Qual arquitetura da AWS atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Fazer com que todos os 200.000 sensores enviem solicitações HTTP POST diretamente para um banco de dados Amazon RDS PostgreSQL.",
                    "explanation": "Incorreto: 200.000 sensores enviando solicitações HTTP POST síncronas sobrecarregarão as conexões do banco de dados, e dispositivos sensores frequentemente exigem o protocolo leve MQTT."
                },
                {
                    "id": "B",
                    "text": "Armazenar os dados dos sensores no Amazon S3 Glacier Deep Archive e executar jobs diários de ETL do AWS Glue.",
                    "explanation": "Incorreto: O Deep Archive possui horas de atraso na recuperação e não pode fornecer alertas imediatos de emergência para temperaturas superiores a 95°C."
                },
                {
                    "id": "C",
                    "text": "Implantar uma frota de instâncias Amazon EC2 executando corretores Mosquitto MQTT em um grupo do Auto Scaling com certificados SSL autoassinados.",
                    "explanation": "Incorreto: Clusters de corretores MQTT autogerenciados exigem ampla manutenção, aplicação de patches e gerenciamento de ciclo de vida de certificados em comparação com o AWS IoT Core sem servidor."
                },
                {
                    "id": "D",
                    "text": "Conectar os sensores ao AWS IoT Core usando certificados de cliente X.509, usar o Mecanismo de Regras do AWS IoT para avaliar limites de temperatura e publicar no Amazon SNS para alarmes, e rotear os dados de séries temporais diretamente para o Amazon Timestream.",
                    "explanation": "Correto: O AWS IoT Core suporta MQTT com autenticação mTLS X.509. O Mecanismo de Regras do IoT filtra eventos e encaminha a telemetria de séries temporais nativamente para o Amazon Timestream, com o SNS para alertas em tempo real."
                }
            ],
            "generalExplanation": "O AWS IoT Core fornece comunicação MQTT segura em escala, enquanto o Mecanismo de Regras do IoT e o Amazon Timestream permitem a ingestão de séries temporais sem servidor e o acionamento de alarmes em tempo real."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Una empresa de fabricación industrial está implementando 200.000 sensores de temperatura IoT en instalaciones de producción de todo el mundo. Los sensores publican mensajes de telemetría cada 5 segundos a través de MQTT con autenticación mutua TLS. El sistema debe ingerir la telemetría de los sensores, enrutar los datos a una base de datos de series temporales dedicada optimizada para análisis de series temporales y consultas SQL, y activar alarmas de emergencia automáticas si la temperatura supera los 95 °C. ¿Qué arquitectura de AWS cumple con estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Hacer que los 200.000 sensores envíen solicitudes HTTP POST directamente a una base de datos Amazon RDS PostgreSQL.",
                    "explanation": "Incorrecto: 200.000 sensores enviando solicitudes HTTP POST sincrónicas saturarán las conexiones de la base de datos y los dispositivos sensores a menudo requieren el protocolo ligero MQTT."
                },
                {
                    "id": "B",
                    "text": "Almacenar los datos de los sensores en Amazon S3 Glacier Deep Archive y ejecutar trabajos diarios de ETL de Glue.",
                    "explanation": "Incorrecto: Deep Archive tiene horas de retraso en la recuperación y no puede proporcionar alertas de emergencia inmediatas para infracciones de temperatura de 95 °C."
                },
                {
                    "id": "C",
                    "text": "Implementar una flota de instancias de Amazon EC2 que ejecuten brokers Mosquitto MQTT en un grupo de Auto Scaling con certificados SSL autofirmados.",
                    "explanation": "Incorrecto: Los clústeres de intermediarios MQTT autogestionados requieren un amplio mantenimiento, parches y gestión del ciclo de vida de certificados personalizados en comparación con el servicio sin servidor AWS IoT Core."
                },
                {
                    "id": "D",
                    "text": "Conectar los sensores a AWS IoT Core mediante certificados de cliente X.509, utilizar el motor de reglas de AWS IoT para evaluar los umbrales de temperatura y publicar en Amazon SNS para alarmas, y enrutar los datos de series temporales directamente a Amazon Timestream.",
                    "explanation": "Correcto: AWS IoT Core admite MQTT con autenticación mTLS X.509. El motor de reglas de IoT filtra eventos y enruta la telemetría de series temporales de forma nativa hacia Amazon Timestream, utilizando SNS para alertas en tiempo real."
                }
            ],
            "generalExplanation": "AWS IoT Core proporciona comunicación MQTT segura a escala, mientras que el motor de reglas de IoT y Amazon Timestream permiten la ingesta de series temporales sin servidor y la generación de alarmas en tiempo real."
        }
    },
    "sap-sim3-q013": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Um site de negociações financeiras de alta relevância protegido pelo Amazon CloudFront sofre ataques recorrentes e sofisticados de DDoS na Camada 7, bots automatizados de raspagem (scraping) visando preços de mercado e ataques de preenchimento de credenciais (credential stuffing) no endpoint `/login`. A empresa exige proteção gerenciada avançada com acesso 24/7 à equipe de resposta a DDoS da AWS (AWS Shield Response Team - SRT), proteção financeira contra picos de custos de escalabilidade durante ataques e mitigação automatizada de bots. Qual combinação de serviços fornece essa defesa abrangente?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o AWS Shield Standard em um Application Load Balancer e escrever scripts de firewall iptables personalizados nas instâncias EC2.",
                    "explanation": "Incorreto: O Shield Standard não inclui suporte 24/7 do SRT, proteção contra custos de DDoS nem regras gerenciadas de Bot Control."
                },
                {
                    "id": "B",
                    "text": "Assinar o AWS Shield Advanced, conceder engajamento proativo e acesso do IAM à equipe de resposta do AWS Shield (SRT) e implantar o AWS WAF na distribuição do CloudFront com Regras Gerenciadas da AWS para Bot Control e Account Takeover Prevention (ATP).",
                    "explanation": "Correto: O AWS Shield Advanced oferece suporte 24/7 do SRT, proteção contra picos de custos de DDoS e engajamento proativo. O AWS WAF Bot Control e o ATP mitigam o credential stuffing e bots de raspagem na borda."
                },
                {
                    "id": "C",
                    "text": "Implantar Network ACLs com regras explícitas de Deny em todas as sub-redes da VPC.",
                    "explanation": "Incorreto: As Network ACLs operam na Camada 4 (IP/porta) e não podem analisar payloads HTTP para credential stuffing nem fornecer proteção financeira contra picos de DDoS."
                },
                {
                    "id": "D",
                    "text": "Alterar todos os registros de DNS no Amazon Route 53 para zonas hospedadas privadas.",
                    "explanation": "Incorreto: Zonas hospedadas privadas tornam o site inacessível para clientes na internet pública."
                }
            ],
            "generalExplanation": "O AWS Shield Advanced oferece proteção contra DDoS de nível empresarial com engajamento 24/7 do SRT e proteção de custos, integrando-se ao AWS WAF Bot Control e ao Account Takeover Prevention (ATP)."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Un sitio web de operaciones financieras de alto perfil respaldado por Amazon CloudFront experimenta ataques DDoS sofisticados y recurrentes de Capa 7, bots de raspado automatizado dirigidos a precios de mercado y ataques de relleno de credenciales (credential stuffing) en el endpoint `/login`. La empresa requiere protección administrada avanzada con acceso 24/7 al equipo de respuesta ante DDoS de AWS (SRT), protección financiera contra picos en los costos de escalado durante los ataques y mitigación automatizada de bots. ¿Qué combinación de servicios proporciona esta defensa integral?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar AWS Shield Standard en un Application Load Balancer y escribir scripts de firewall iptables personalizados en instancias EC2.",
                    "explanation": "Incorrecto: Shield Standard no incluye soporte 24/7 del equipo SRT, protección de costos de DDoS ni reglas administradas de Bot Control."
                },
                {
                    "id": "B",
                    "text": "Suscribirse a AWS Shield Advanced, otorgar compromiso proactivo y acceso de IAM al AWS Shield Response Team (SRT), e implementar AWS WAF en la distribución de CloudFront con Reglas Administradas de AWS para Bot Control y Account Takeover Prevention (ATP).",
                    "explanation": "Correcto: AWS Shield Advanced proporciona soporte 24/7 de SRT, protección contra picos de costos por DDoS y compromiso proactivo. AWS WAF Bot Control y ATP mitigan el credential stuffing y los bots de raspado en el borde."
                },
                {
                    "id": "C",
                    "text": "Implementar Network ACLs con reglas explícitas de Deny en todas las subredes de la VPC.",
                    "explanation": "Incorrecto: Las Network ACLs operan en la Capa 4 (IP/puerto) y no pueden inspeccionar cargas útiles HTTP para credential stuffing ni ofrecer protección financiera ante picos de DDoS."
                },
                {
                    "id": "D",
                    "text": "Cambiar todos los registros DNS en Amazon Route 53 a zonas alojadas privadas.",
                    "explanation": "Incorrecto: Las zonas alojadas privadas hacen que el sitio web sea inaccesible para los clientes de la Internet pública."
                }
            ],
            "generalExplanation": "AWS Shield Advanced proporciona protección contra DDoS de nivel empresarial con soporte 24/7 de SRT y protección de costos, integrándose con AWS WAF Bot Control y Account Takeover Prevention (ATP)."
        }
    },
    "sap-sim3-q014": {
        "pt": {
            "domainName": "Domínio 2: Projetar Novas Soluções",
            "statement": "Um aplicativo móvel de fintech precisa oferecer suporte a cadastro de usuários, login com e-mail ou provedores sociais (Apple, Google), autenticação multifator (MFA via SMS/TOTP) e integração direta com o Amazon API Gateway. Quando um usuário se autentica, o API Gateway deve validar automaticamente o token JWT OAuth 2.0 / OpenID Connect (OIDC) antes de repassar as solicitações aos microsserviços de back-end. Qual solução implementa isso com a MENOR quantidade de código personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Armazenar as senhas dos usuários em um banco de dados Amazon RDS MySQL e escrever scripts de autenticação PHP personalizados em uma instância EC2.",
                    "explanation": "Incorreto: Armazenar senhas manualmente no MySQL exige a implementação de código personalizado de hash, salt, MFA e emissão de tokens do zero."
                },
                {
                    "id": "B",
                    "text": "Implantar um pool de usuários do Amazon Cognito (User Pool) com federação de provedores de identidade social e MFA ativado, e configurar um Autorizador Cognito do Amazon API Gateway nos endpoints da API REST.",
                    "explanation": "Correto: Os pools de usuários do Amazon Cognito gerenciam usuários, federação social e MFA de forma nativa. Os autorizadores Cognito do API Gateway validam tokens nativamente sem a necessidade de escrever código de autenticação customizado."
                },
                {
                    "id": "C",
                    "text": "Criar um usuário do IAM para cada cliente do aplicativo móvel.",
                    "explanation": "Incorreto: Usuários do IAM destinam-se a identidades de força de trabalho na nuvem e não escalam para aplicativos móveis voltados a consumidores finais."
                },
                {
                    "id": "D",
                    "text": "Configurar uma regra baseada em taxa do AWS WAF no API Gateway.",
                    "explanation": "Incorreto: Regras baseadas em taxa do AWS WAF filtram a frequência de requisições, mas não fornecem autenticação de usuário, emissão de tokens ou login social."
                }
            ],
            "generalExplanation": "O Amazon Cognito User Pools combinado com os Autorizadores Cognito do API Gateway fornece uma solução totalmente gerenciada e sem servidor de autenticação e autorização para aplicações web e móveis."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Nuevas Soluciones",
            "statement": "Una aplicación móvil fintech necesita admitir el registro de usuarios, el inicio de sesión con correo electrónico o proveedores sociales (Apple, Google), autenticación multifactor (MFA mediante SMS/TOTP) y una integración fluida con Amazon API Gateway. Cuando un usuario se autentica, API Gateway debe validar automáticamente el token JWT de OAuth 2.0 / OpenID Connect (OIDC) antes de pasar las solicitudes a los microservicios de backend. ¿Qué solución implementa esto con la MENOR cantidad de código personalizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Almacenar contraseñas de usuarios en una base de datos Amazon RDS MySQL y escribir scripts de autenticación PHP personalizados en una instancia EC2.",
                    "explanation": "Incorrecto: Almacenar contraseñas manualmente en MySQL requiere implementar código de hashing, salt, MFA y emisión de tokens desde cero."
                },
                {
                    "id": "B",
                    "text": "Implementar un grupo de usuarios de Amazon Cognito (User Pool) con federación de proveedores de identidad social y MFA habilitado, y configurar un autorizador Cognito de Amazon API Gateway en los endpoints de la API REST.",
                    "explanation": "Correcto: Amazon Cognito User Pools gestiona la administración de usuarios, la federación social y el MFA de forma nativa. Los autorizadores de Cognito en API Gateway validan tokens de forma nativa sin escribir código de autenticación personalizado."
                },
                {
                    "id": "C",
                    "text": "Crear un usuario de IAM para cada cliente de la aplicación móvil.",
                    "explanation": "Incorrecto: Los usuarios de IAM son para identidades de empleados de nube y no pueden escalar para aplicaciones móviles de consumo masivo."
                },
                {
                    "id": "D",
                    "text": "Configurar una regla basada en tasa de AWS WAF en API Gateway.",
                    "explanation": "Incorrecto: Las reglas basadas en tasa de AWS WAF filtran la frecuencia de solicitudes, pero no proporcionan autenticación de usuarios, emisión de tokens o inicio de sesión social."
                }
            ],
            "generalExplanation": "Amazon Cognito User Pools combinado con los autorizadores de Cognito de API Gateway proporciona una solución de autenticación y autorización totalmente administrada y sin servidor para aplicaciones web y móviles."
        }
    },
    "sap-sim3-q015": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa gasta US$ 500.000 mensais em computação do Amazon EC2 em várias regiões da AWS e famílias de instâncias (c5, m6g, r5, g4dn), juntamente com o uso crescente do AWS Fargate para microsserviços em contêineres e AWS Lambda. As equipes financeira e de engenharia concordam em assumir um compromisso monetário de 3 anos (US$/hora) para maximizar a economia de custos, mantendo total flexibilidade arquitetônica para alterar famílias de instâncias, sistemas operacionais, plataformas de computação e regiões da AWS no futuro. Qual modelo de preços o arquiteto deve recomendar?",
            "options": [
                {
                    "id": "A",
                    "text": "Comprar Instâncias Reservadas Padrão (Standard Reserved Instances) de 3 anos para instâncias c5.xlarge específicas em us-east-1.",
                    "explanation": "Incorreto: As Instâncias Reservadas Padrão ficam restritas a famílias de instâncias, regiões e plataformas específicas e não se aplicam ao Fargate ou ao Lambda."
                },
                {
                    "id": "B",
                    "text": "Comprar planos Compute Savings Plans de 3 anos com pagamento Total Adiantado (All Upfront) ou Parcialmente Adiantado (Partial Upfront).",
                    "explanation": "Correto: O Compute Savings Plans oferece a maior flexibilidade, aplicando automaticamente até 66% de desconto em famílias de instâncias EC2, tamanhos, sistemas operacionais, tenancy, regiões da AWS, AWS Fargate e AWS Lambda."
                },
                {
                    "id": "C",
                    "text": "Comprar planos EC2 Instance Savings Plans bloqueados para a família c5 em us-east-1.",
                    "explanation": "Incorreto: O EC2 Instance Savings Plans não se aplica entre regiões, a outras famílias de instâncias (m6g, r5) ou ao Fargate/Lambda."
                },
                {
                    "id": "D",
                    "text": "Depender exclusivamente do faturamento sob demanda (On-Demand) com descontos por volume.",
                    "explanation": "Incorreto: O faturamento sob demanda não oferece os descontos por compromisso de até 66% disponíveis por meio do Savings Plans."
                }
            ],
            "generalExplanation": "O Compute Savings Plans oferece economia substancial de custos (até 66%) com o máximo de flexibilidade, aplicando-se automaticamente independentemente da família de instâncias, tamanho, sistema operacional, região, Fargate ou Lambda."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa gasta 500.000 USD mensuales en computación de Amazon EC2 en múltiples regiones de AWS y familias de instancias (c5, m6g, r5, g4dn), junto con un uso creciente de AWS Fargate para microservicios en contenedores y AWS Lambda. Los equipos de finanzas e ingeniería acuerdan asumir un compromiso monetario de 3 años ($/hora) para maximizar el ahorro de costos, manteniendo al mismo tiempo una flexibilidad arquitectónica total para cambiar familias de instancias, sistemas operativos, plataformas de cómputo y regiones de AWS en el futuro. ¿Qué modelo de precios debería recomendar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Comprar Instancias Reservadas Estándar de 3 años para instancias c5.xlarge específicas en us-east-1.",
                    "explanation": "Incorrecto: Las RIs estándar están bloqueadas a familias de instancias, regiones y plataformas específicas, y no se aplican a Fargate o Lambda."
                },
                {
                    "id": "B",
                    "text": "Comprar Compute Savings Plans de 3 años con pago Total por Adelantado (All Upfront) o Parcial por Adelantado (Partial Upfront).",
                    "explanation": "Correcto: Compute Savings Plans proporciona la mayor flexibilidad, aplicando automáticamente hasta un 66% de descuento en familias de instancias EC2, tamaños, SO, tenencia, regiones de AWS, AWS Fargate y AWS Lambda."
                },
                {
                    "id": "C",
                    "text": "Comprar EC2 Instance Savings Plans vinculados a la familia c5 en us-east-1.",
                    "explanation": "Incorrecto: Los EC2 Instance Savings Plans no se aplican entre regiones, a otras familias de instancias (m6g, r5), ni a Fargate/Lambda."
                },
                {
                    "id": "D",
                    "text": "Confiar únicamente en la facturación Bajo Demanda (On-Demand) con descuentos por volumen.",
                    "explanation": "Incorrecto: La facturación Bajo Demanda no ofrece descuentos por compromiso de hasta el 66% disponibles a través de Savings Plans."
                }
            ],
            "generalExplanation": "Compute Savings Plans ofrece importantes ahorros de costos (hasta un 66%) con la máxima flexibilidad, aplicándose automáticamente sin importar la familia de instancias, el tamaño, el SO, la región, Fargate o Lambda."
        }
    },
    "sap-sim3-q016": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Um varejista de comércio eletrônico deseja monitorar 24/7 a integridade e a experiência do cliente em seu fluxo de checkout em várias etapas (Login -> Adicionar ao Carrinho -> Informar Pagamento -> Confirmar Pedido). A solução de monitoramento deve simular ações realistas de usuários em um navegador headless a partir de várias regiões geográficas, capturar capturas de tela (screenshots) das etapas com falha, medir o tempo de carregamento da interface do usuário e alertar o engenheiro de DevOps de plantão antes que clientes reais sejam afetados. Qual serviço atende a esses critérios?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar o Amazon GuardDuty nas instâncias EC2 de checkout para monitorar anomalias no sistema operacional e na rede.",
                    "explanation": "Incorreto: O GuardDuty monitora ameaças de segurança, e não a experiência sintética de checkout do usuário final ou o desempenho da interface do usuário."
                },
                {
                    "id": "B",
                    "text": "Implantar canários do Amazon CloudWatch Synthetics (usando scripts Puppeteer/Node.js ou Selenium/Python) em execução em intervalos de 1 minuto a partir de várias regiões da AWS com alarmes do CloudWatch.",
                    "explanation": "Correto: Os canários do CloudWatch Synthetics executam scripts automatizados que simulam ações do usuário em navegadores headless, capturando a latência da interface, respostas de APIs e capturas de tela em caso de falhas."
                },
                {
                    "id": "C",
                    "text": "Habilitar o Amazon VPC Flow Logs em todas as sub-redes públicas para capturar metadados brutos de pacotes entre instâncias.",
                    "explanation": "Incorreto: O VPC Flow Logs captura o tráfego IP de rede na Camada 4, e não fluxos de interface da aplicação, renderização de navegador ou simulação de usuário."
                },
                {
                    "id": "D",
                    "text": "Configurar verificações de integridade de DNS do Amazon Route 53 na URL pública da página inicial sem simulação de navegador em várias etapas.",
                    "explanation": "Incorreto: Uma verificação básica de integridade TCP/HTTP na página inicial não simula fluxos de login/carrinho/checkout em várias etapas nem captura telas."
                }
            ],
            "generalExplanation": "O Amazon CloudWatch Synthetics permite monitorar endpoints de aplicações e fluxos de trabalho de usuários em várias etapas usando canários sintéticos que são executados 24/7 para detectar problemas proativamente."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Un minorista de comercio electrónico desea monitorear la salud y la experiencia del cliente de su flujo de compra de múltiples pasos (Iniciar sesión -> Agregar al carrito -> Ingresar pago -> Confirmar pedido) las 24 horas del día, los 7 días de la semana. La solución de monitoreo debe simular acciones realistas del usuario en un navegador headless desde múltiples regiones geográficas, tomar capturas de pantalla de los pasos fallidos, medir los tiempos de carga de la interfaz de usuario y alertar al ingeniero de DevOps de guardia antes de que los clientes reales se vean afectados. ¿Qué servicio cumple con estos criterios?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar Amazon GuardDuty en las instancias EC2 de compra para monitorear anomalías del sistema operativo y de la red.",
                    "explanation": "Incorrecto: GuardDuty monitorea amenazas de seguridad, no la experiencia sintética del usuario final en el proceso de compra ni el rendimiento de la interfaz de usuario."
                },
                {
                    "id": "B",
                    "text": "Implementar canarios de Amazon CloudWatch Synthetics (utilizando scripts de Puppeteer/Node.js o Selenium/Python) que se ejecuten en un intervalo de 1 minuto desde múltiples regiones de AWS con Alarmas de CloudWatch.",
                    "explanation": "Correcto: Los canarios de CloudWatch Synthetics ejecutan scripts automatizados que simulan acciones del usuario en navegadores headless, capturando la latencia de la interfaz de usuario, las respuestas de la API y capturas de pantalla en caso de fallo."
                },
                {
                    "id": "C",
                    "text": "Habilitar Amazon VPC Flow Logs en todas las subredes públicas para capturar metadados de paquetes sin procesar en todas las instancias.",
                    "explanation": "Incorrecto: VPC Flow Logs captura el tráfico de red IP de Capa 4, no los flujos de interfaz de usuario de aplicaciones, el renderizado de navegadores o la simulación de usuarios."
                },
                {
                    "id": "D",
                    "text": "Configurar comprobaciones de estado de DNS de Amazon Route 53 en la URL de la página de inicio pública sin simulación de navegador de múltiples pasos.",
                    "explanation": "Incorrecto: Una comprobación de estado TCP/HTTP básica de la página de inicio no simula flujos de trabajo de múltiples pasos de inicio de sesión/carrito/pago ni captura pantallas."
                }
            ],
            "generalExplanation": "Amazon CloudWatch Synthetics le permite monitorear endpoints de aplicaciones y flujos de trabajo de usuarios de múltiples pasos utilizando canarios sintéticos que se ejecutan 24/7 para detectar problemas de manera proactiva."
        }
    },
    "sap-sim3-q017": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa está se preparando para uma auditoria regulatória anual de resiliência. O arquiteto de soluções precisa de um serviço central que possa definir Objetivos de Tempo de Recuperação (RTO) e Objetivos de Ponto de Recuperação (RPO) para aplicações de negócios críticas, avaliar toda a arquitetura em relação a essas metas, recomendar estratégias de remediação e gerar conjuntos de testes automatizados para validar a prontidão de recuperação de desastres. Qual serviço da AWS foi projetado especificamente para essa finalidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar o AWS Resilience Hub para avaliar arquiteturas de aplicações em relação às metas de RTO e RPO do negócio e gerar conjuntos de testes.",
                    "explanation": "Correto: O AWS Resilience Hub fornece um local centralizado para definir, medir e gerenciar a postura de resiliência de suas aplicações, rastreando metas de RTO/RPO e gerando modelos de testes automatizados para o AWS FIS."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS Cost Explorer para visualizar gastos históricos consolidados da AWS e prever o uso futuro.",
                    "explanation": "Incorreto: O Cost Explorer é uma ferramenta de relatórios financeiros, e não um mecanismo de avaliação de RTO/RPO para recuperação de desastres."
                },
                {
                    "id": "C",
                    "text": "Usar o AWS Certificate Manager (ACM) para provisionar e renovar automaticamente certificados SSL/TLS públicos.",
                    "explanation": "Incorreto: O AWS Certificate Manager (ACM) gerencia certificados SSL/TLS públicos e privados e não avalia a resiliência arquitetônica de RTO/RPO."
                },
                {
                    "id": "D",
                    "text": "Baixar relatórios de conformidade e certificações regulatórias a partir do portal de autoatendimento AWS Artifact.",
                    "explanation": "Incorreto: O AWS Artifact fornece relatórios de auditoria de conformidade para a infraestrutura de nuvem da AWS, mas não avalia arquiteturas de aplicações personalizadas em relação a metas de RTO/RPO."
                }
            ],
            "generalExplanation": "O AWS Resilience Hub fornece um painel único para definir, medir e aprimorar a resiliência de suas aplicações na AWS com base nas metas de RTO e RPO do negócio."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa se está preparando para una auditoría anual de resiliencia regulatoria. El arquitecto de soluciones necesita un servicio central que pueda definir Objetivos de Tiempo de Recuperación (RTO) y Objetivos de Punto de Recuperación (RPO) para aplicaciones comerciales críticas, evaluar toda la arquitectura frente a estos objetivos, recomendar estrategias de corrección y generar conjuntos de pruebas automatizadas para validar la preparación ante desastres. ¿Qué servicio de AWS está diseñado específicamente para este propósito?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar AWS Resilience Hub para evaluar las arquitecturas de las aplicaciones frente a los objetivos de RTO y RPO del negocio y generar conjuntos de pruebas.",
                    "explanation": "Correcto: AWS Resilience Hub proporciona un lugar central para definir, medir y administrar la postura de resiliencia de sus aplicaciones, realizando un seguimiento de los objetivos de RTO/RPO y generando plantillas de pruebas automatizadas para AWS FIS."
                },
                {
                    "id": "B",
                    "text": "Utilizar AWS Cost Explorer para visualizar los gastos históricos consolidados de AWS y pronosticar el uso futuro.",
                    "explanation": "Incorrecto: Cost Explorer es una herramienta de informes financieros, no un motor de evaluación de RTO/RPO de recuperación ante desastres."
                },
                {
                    "id": "C",
                    "text": "Utilizar AWS Certificate Manager (ACM) para aprovisionar y renovar automáticamente certificados SSL/TLS públicos.",
                    "explanation": "Incorrecto: AWS Certificate Manager (ACM) administra certificados SSL/TLS públicos y privados y no evalúa la resiliencia arquitectónica de RTO/RPO."
                },
                {
                    "id": "D",
                    "text": "Descargar informes de cumplimiento y certificaciones regulatorias desde el portal de autoservicio de AWS Artifact.",
                    "explanation": "Incorrecto: AWS Artifact proporciona informes de cumplimiento para la infraestructura en la nube de AWS, pero no evalúa las arquitecturas de aplicaciones personalizadas de clientes frente a los objetivos de RTO/RPO."
                }
            ],
            "generalExplanation": "AWS Resilience Hub proporciona un único panel para definir, medir y mejorar la resiliencia de sus aplicaciones de AWS en función de los objetivos de RTO y RPO comerciales."
        }
    },
    "sap-sim3-q018": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa gerencia 5.000 volumes do Amazon EBS em 200 instâncias EC2 em uma região da AWS. A política de conformidade exige a criação de snapshots diários automatizados de todos os volumes EBS de produção (identificados pela tag `Environment=Production`), mantendo snapshots diários por 14 dias, snapshots semanais por 90 dias, snapshots mensais por 1 ano e replicando todos os snapshots para uma região secundária de recuperação de desastres. Qual solução atinge esse objetivo com a MENOR sobrecarga operacional?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar e implantar a ativação do S3 Versioning nos volumes EBS, seguindo as melhores práticas corporativas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: Volumes EBS são dispositivos de bloco e não suportam o S3 Versioning."
                },
                {
                    "id": "B",
                    "text": "Escrever um script Python em uma instância EC2 que chama `ec2:CreateSnapshot` e `ec2:CopySnapshot` por meio de uma tarefa cron.",
                    "explanation": "Incorreto: Scripts personalizados exigem manutenção contínua, tratamento de erros e gerenciamento de servidores em comparação com o Amazon DLM nativo."
                },
                {
                    "id": "C",
                    "text": "Anexar todos os 5.000 volumes EBS a uma única instância EC2 central e executar comandos `dd` para fita.",
                    "explanation": "Incorreto: Anexar 5.000 volumes a uma única instância excede os limites de anexo do EC2 e usar `dd` é um antipadrão."
                },
                {
                    "id": "D",
                    "text": "Configurar uma política de ciclo de vida do Amazon Data Lifecycle Manager (Amazon DLM) direcionada aos volumes EBS com a tag `Environment=Production`, definindo programações diárias, semanais e mensais com períodos de retenção e regras automatizadas de cópia entre regiões.",
                    "explanation": "Correto: O Amazon Data Lifecycle Manager (Amazon DLM) automatiza a criação, retenção e replicação entre regiões de snapshots do EBS com base em tags declarativas de recursos com zero scripts personalizados."
                }
            ],
            "generalExplanation": "O Amazon Data Lifecycle Manager (DLM) oferece gerenciamento automatizado do ciclo de vida de snapshots para volumes EBS, suportando camadas de retenção personalizadas e replicação entre regiões com base em tags."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa administra 5.000 volúmenes de Amazon EBS en 200 instancias EC2 en una región de AWS. La política de cumplimiento exige realizar instantáneas (snapshots) diarias automatizadas de todos los volúmenes de EBS de producción (identificados con la etiqueta `Environment=Production`), conservando las instantáneas diarias durante 14 días, las semanales durante 90 días, las mensuales durante 1 año y replicando todas las instantáneas a una región secundaria de recuperación ante desastres. ¿Qué solución logra esto con la MENOR sobrecarga operativa?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar e implementar la activación de S3 Versioning en los volúmenes de EBS, siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Los volúmenes EBS son dispositivos de bloque y no admiten el control de versiones de S3 (S3 Versioning)."
                },
                {
                    "id": "B",
                    "text": "Escribir un script de Python en una instancia EC2 que llame a `ec2:CreateSnapshot` y `ec2:CopySnapshot` a través de un cron job.",
                    "explanation": "Incorrecto: Los scripts personalizados requieren mantenimiento continuo, gestión de errores y administración de servidores en comparación con el servicio nativo DLM."
                },
                {
                    "id": "C",
                    "text": "Adjuntar los 5.000 volúmenes de EBS a una sola instancia EC2 central y ejecutar comandos `dd` en cinta.",
                    "explanation": "Incorrecto: Adjuntar 5.000 volúmenes a una instancia supera los límites de adjuntos de EC2 y `dd` es un antipatrón."
                },
                {
                    "id": "D",
                    "text": "Configurar una política de ciclo de vida de Amazon Data Lifecycle Manager (Amazon DLM) dirigida a los volúmenes de EBS etiquetados como `Environment=Production`, definiendo programaciones diarias, semanales y mensuales con períodos de retención y reglas automatizadas de copia entre regiones.",
                    "explanation": "Correcto: Amazon Data Lifecycle Manager (Amazon DLM) automatiza la creación, retención y replicación entre regiones de instantáneas de EBS en función de etiquetas de recursos declarativas sin scripts personalizados."
                }
            ],
            "generalExplanation": "Amazon Data Lifecycle Manager (DLM) proporciona administración automatizada del ciclo de vida de instantáneas para volúmenes de EBS, admitiendo niveles de retención personalizados y replicación entre regiones basada en etiquetas."
        }
    },
    "sap-sim3-q019": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma instituição bancária e financeira deve armazenar registros regulatórios de transações sob a Regra 17a-4 da SEC no Amazon S3 por um período de retenção obrigatório de 5 anos. Os registros devem ser estritamente imutáveis: nenhum usuário do IAM, administrador ou usuário root da conta da AWS pode excluir ou sobrescrever qualquer objeto nem reduzir o período de retenção durante a janela de 5 anos. Qual configuração impõe essa garantia de conformidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Aplicar uma política de bucket do S3 com um Deny explícito para `s3:DeleteObject` cobrindo todos os usuários do IAM.",
                    "explanation": "Incorreto: O usuário root da conta da AWS ou um administrador com privilégios do IAM pode modificar ou excluir a política de bucket para burlar a restrição."
                },
                {
                    "id": "B",
                    "text": "Configurar uma regra de ciclo de vida do S3 para transicionar objetos para o S3 Glacier Deep Archive.",
                    "explanation": "Incorreto: As transições do S3 Lifecycle alteram a classe de armazenamento, mas não impedem a exclusão por usuários autorizados, a menos que o Object Lock esteja ativado."
                },
                {
                    "id": "C",
                    "text": "Habilitar o Amazon S3 Object Lock no Modo de Governança (Governance Mode) com um período de retenção de 5 anos.",
                    "explanation": "Incorreto: O Modo de Governança permite que usuários com permissões específicas do IAM (s3:BypassGovernanceRetention) ou o usuário root alterem ou excluam objetos protegidos."
                },
                {
                    "id": "D",
                    "text": "Habilitar o S3 Versioning no bucket e configurar o Amazon S3 Object Lock no Modo de Conformidade (Compliance Mode) com um período de retenção padrão de 5 anos.",
                    "explanation": "Correto: O S3 Object Lock no Modo de Conformidade impõe um modelo estrito de WORM (Gravar Uma Vez, Ler Várias), no qual nenhum usuário, incluindo o usuário root da conta da AWS, pode excluir objetos ou reduzir a retenção durante o período de conformidade."
                }
            ],
            "generalExplanation": "O Amazon S3 Object Lock no Modo de Conformidade impede que uma versão de objeto seja excluída ou sobrescrita por qualquer usuário, incluindo o usuário root, atendendo aos requisitos de conformidade da Regra 17a-4 da SEC."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una institución bancaria y financiera debe almacenar registros de transacciones regulatorias según la Regla 17a-4 de la SEC en Amazon S3 durante un período de retención obligatorio de 5 años. Los registros deben ser estrictamente inmutables: ningún usuario de IAM, administrador o usuario root de la cuenta de AWS puede eliminar o sobrescribir ningún objeto ni reducir el período de retención durante la ventana de 5 años. ¿Qué configuración exige esta garantía de cumplimiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Aplicar una política de bucket de S3 con un Deny explícito para `s3:DeleteObject` que cubra a todos los usuarios de IAM.",
                    "explanation": "Incorrecto: El usuario root de la cuenta de AWS o un administrador con privilegios de IAM pueden modificar o eliminar la política de bucket para eludir la restricción."
                },
                {
                    "id": "B",
                    "text": "Configurar una regla de ciclo de vida de S3 para realizar la transición de objetos a S3 Glacier Deep Archive.",
                    "explanation": "Incorrecto: Las transiciones de S3 Lifecycle cambian la clase de almacenamiento, pero no evitan la eliminación por parte de usuarios autorizados a menos que Object Lock esté habilitado."
                },
                {
                    "id": "C",
                    "text": "Habilitar Amazon S3 Object Lock en Modo de Gobernanza (Governance Mode) con un período de retención de 5 años.",
                    "explanation": "Incorrecto: El Modo de Gobernanza permite a los usuarios con permisos de IAM específicos (s3:BypassGovernanceRetention) o a root alterar o eliminar objetos protegidos."
                },
                {
                    "id": "D",
                    "text": "Habilitar el control de versiones de S3 (S3 Versioning) en el bucket y configurar Amazon S3 Object Lock en Modo de Cumplimiento (Compliance Mode) con un período de retención predeterminado de 5 años.",
                    "explanation": "Correcto: S3 Object Lock en Modo de Cumplimiento aplica un modelo estricto de WORM (Escribir una vez, leer muchas), en el que ningún usuario, incluido el usuario root de la cuenta de AWS, puede eliminar objetos ni reducir la retención durante el período de cumplimiento."
                }
            ],
            "generalExplanation": "Amazon S3 Object Lock en Modo de Cumplimiento evita que cualquier usuario, incluido el usuario root, elimine o sobrescriba una versión de objeto, cumpliendo con la Regla 17a-4 de la SEC."
        }
    },
    "sap-sim3-q020": {
        "pt": {
            "domainName": "Domínio 3: Melhoria Contínua para Soluções Existentes",
            "statement": "Uma empresa de mídia global distribui arquivos de vídeo e notícias dinâmicas via Amazon CloudFront. Devido a acordos de licenciamento regional, determinados conteúdos de vídeo devem ser acessíveis apenas a espectadores localizados em países específicos (como Estados Unidos e Canadá), enquanto espectadores de outros países devem receber uma resposta HTTP 403 Forbidden. Qual solução impõe essa restrição na borda com a MENOR latência?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um Application Load Balancer em cada país e escrever scripts PHP personalizados para verificar os endereços IP dos clientes em um banco de dados GeoIP de terceiros.",
                    "explanation": "Incorreto: Gerenciar consultas GeoIP personalizadas em ALBs adiciona sobrecarga operacional desnecessária e não bloqueia requisições na borda da CDN global."
                },
                {
                    "id": "B",
                    "text": "Configurar as Restrições Geográficas (Geo-blocking) do Amazon CloudFront para permitir o acesso apenas a partir de países autorizados (Estados Unidos e Canadá) nos pontos de presença (edge locations) do CloudFront.",
                    "explanation": "Correto: As restrições geográficas do CloudFront bloqueiam ou permitem a distribuição de conteúdo com base na localização geográfica do espectador diretamente nos locais de borda, impedindo que espectadores não autorizados baixem o conteúdo."
                },
                {
                    "id": "C",
                    "text": "Configurar uma política de bucket do Amazon S3 com lista de permissões de endereços IP.",
                    "explanation": "Incorreto: Usuários globais possuem IPs públicos dinâmicos, tornando a lista estática de IPs no S3 inviável e a identificação geográfica por país impossível."
                },
                {
                    "id": "D",
                    "text": "Desativar o CloudFront e exigir que os usuários se conectem por meio de uma VPN Site-to-Site da AWS.",
                    "explanation": "Incorreto: A VPN Site-to-Site destina-se a escritórios corporativos, e não à transmissão pública de mídia para consumidores."
                }
            ],
            "generalExplanation": "As Restrições Geográficas do Amazon CloudFront (Geo-blocking) permitem restringir o acesso a todos ou a arquivos selecionados na borda com base no país do espectador."
        },
        "es": {
            "domainName": "Dominio 3: Mejora Continua para Soluciones Existentes",
            "statement": "Una empresa global de medios distribuye archivos de video y noticias dinámicas a través de Amazon CloudFront. Debido a acuerdos de licencia regional, cierto contenido de video solo debe ser accesible para los espectadores ubicados en países específicos (como Estados Unidos y Canadá), mientras que los espectadores de otros países deben recibir una respuesta HTTP 403 Forbidden. ¿Qué solución aplica esta restricción en el borde con la MENOR latencia?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un Application Load Balancer en cada país y escribir scripts PHP personalizados para comprobar las direcciones IP de los clientes con una base de datos GeoIP de terceros.",
                    "explanation": "Incorrecto: Administrar búsquedas GeoIP personalizadas en ALBs agrega sobrecarga operativa innecesaria y no bloquea solicitudes en el borde de la CDN global."
                },
                {
                    "id": "B",
                    "text": "Configurar restricciones geográficas de Amazon CloudFront (Geo-blocking) para permitir el acceso únicamente desde países autorizados (Estados Unidos y Canadá) en las ubicaciones de borde de CloudFront.",
                    "explanation": "Correcto: Las restricciones geográficas de CloudFront bloquean o permiten la distribución de contenido según la ubicación geográfica del espectador directamente en las ubicaciones del borde, evitando que los espectadores no autorizados descarguen contenido."
                },
                {
                    "id": "C",
                    "text": "Configurar una política de bucket de Amazon S3 con una lista de IP permitidas.",
                    "explanation": "Incorrecto: Los usuarios globales tienen IPs públicas dinámicas, lo que hace inviable la lista estática de IPs en S3 e imposible la geolocalización por país."
                },
                {
                    "id": "D",
                    "text": "Deshabilitar CloudFront y requerir que los usuarios se conecten a través de una VPN Site-to-Site de AWS.",
                    "explanation": "Incorrecto: La VPN Site-to-Site es para oficinas corporativas, no para la transmisión pública de medios de consumo masivo."
                }
            ],
            "generalExplanation": "Las restricciones geográficas de Amazon CloudFront (Geo-blocking) le permiten restringir el acceso a todos o a determinados archivos en el borde en función del país del espectador."
        }
    },
    "sap-sim3-q021": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa está planejando migrar 250 servidores locais Windows e Linux para a AWS dentro de um prazo apertado de 60 dias. O plano de migração exige replicação contínua de dados sem interrupções, testes automatizados pré-migração (pre-cutover) em uma VPC de preparação (staging) isolada sem impactar os sistemas de produção de origem e ações automatizadas pós-inicialização (como instalar o AWS Systems Manager Agent e atualizar drivers). Qual serviço da AWS deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar agentes do AWS DataSync em máquinas virtuais locais para transferir sistemas de arquivos para o Amazon S3.",
                    "explanation": "Incorreto: O DataSync migra dados de sistemas de arquivos e objetos, e não volumes de inicialização de sistemas operacionais e fluxos de migração de servidores."
                },
                {
                    "id": "B",
                    "text": "AWS Application Migration Service (AWS MGN) configurado com Launch Templates e Post-Launch Settings.",
                    "explanation": "Correto: O AWS Application Migration Service (AWS MGN) fornece replicação contínua em nível de bloco sem interrupções, permite testes automatizados antes do cutover em VPCs isoladas e oferece suporte a ações de configuração automatizadas pós-inicialização (instalação do agente SSM, atualizações de driver, scripts personalizados)."
                },
                {
                    "id": "C",
                    "text": "Implantar o conector legado do AWS Server Migration Service (AWS SMS) para criar backups periódicos de snapshots de hipervisor.",
                    "explanation": "Incorreto: O AWS SMS foi descontinuado, é baseado em snapshots (e não em replicação contínua) e não possui os recursos modernos de automação pós-inicialização."
                },
                {
                    "id": "D",
                    "text": "Solicitar um dispositivo físico AWS Snowball Edge Storage Optimized para transportar imagens de disco de servidores offline.",
                    "explanation": "Incorreto: O Snowball Edge é para migração de dados em massa offline, e não para replicação automatizada de servidores em tempo real com inicialização de drivers pós-lançamento."
                }
            ],
            "generalExplanation": "O AWS Application Migration Service (AWS MGN) automatiza migrações no modelo lift-and-shift de servidores com replicação contínua, testes sem interrupções e automação pós-inicialização."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa planea migrar 250 servidores locales Windows y Linux a AWS en un plazo ajustado de 60 días. El plan de migración requiere replicación continua de datos sin interrupciones, pruebas automatizadas antes del traspaso definitivo (pre-cutover) en una VPC de ensayo aislada sin afectar los sistemas de producción de origen y acciones automatizadas posteriores al lanzamiento (como la instalación del agente de AWS Systems Manager y la actualización de controladores). ¿Qué servicio de AWS se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar agentes de AWS DataSync en máquinas virtuales locales para transferir sistemas de archivos a Amazon S3.",
                    "explanation": "Incorrecto: DataSync migra datos de sistemas de archivos/objetos, no volúmenes de arranque del sistema operativo ni flujos de migración de servidores."
                },
                {
                    "id": "B",
                    "text": "AWS Application Migration Service (AWS MGN) configurado con Plantillas de Lanzamiento (Launch Templates) y Ajustes Posteriores al Lanzamiento (Post-Launch Settings).",
                    "explanation": "Correcto: AWS Application Migration Service (AWS MGN) proporciona replicación continua a nivel de bloque sin interrupciones, permite pruebas automatizadas previas al cutover en VPCs aisladas y admite acciones de configuración posteriores al lanzamiento automatizadas (instalación del agente SSM, actualizaciones de controladores, scripts personalizados)."
                },
                {
                    "id": "C",
                    "text": "Implementar el conector heredado de AWS Server Migration Service (AWS SMS) para crear copias de seguridad periódicas de instantáneas de hipervisor.",
                    "explanation": "Incorrecto: AWS SMS está en desuso, se basa en instantáneas (no en replicación continua) y carece de capacidades modernas de automatización posteriores al lanzamiento."
                },
                {
                    "id": "D",
                    "text": "Solicitar un dispositivo físico AWS Snowball Edge Storage Optimized para transportar imágenes de disco de servidores fuera de línea.",
                    "explanation": "Incorrecto: Snowball Edge es para migración masiva de datos fuera de línea, no para replicación automatizada de servidores en vivo con inicialización de controladores posterior al lanzamiento."
                }
            ],
            "generalExplanation": "AWS Application Migration Service (AWS MGN) automatiza las migraciones lift-and-shift de servidores con replicación continua, pruebas sin interrupciones y automatización posterior al lanzamiento."
        }
    },
    "sap-sim3-q022": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa financeira está migrando um banco de dados local Microsoft SQL Server de 20 TB para o Amazon Aurora PostgreSQL. Durante a fase inicial de carregamento completo (full load), tabelas de banco de dados contendo Grandes Objetos Binários (LOBs) estão fazendo com que as tarefas de migração do AWS DMS sejam executadas de forma extremamente lenta. A aplicação exige a replicação precisa de todos os dados de LOB sem truncar informações. Qual configuração do AWS DMS otimiza o desempenho da migração de LOBs?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar o AWS DMS com o modo Limited LOB para validação inicial e o modo Full LOB (ou modo Inline LOB com um Max LOB Size otimizado) para tabelas com colunas LOB grandes, dividindo tabelas grandes em várias tarefas de replicação dedicadas.",
                    "explanation": "Correto: A otimização de LOBs no AWS DMS envolve o ajuste dos modos de LOB: o modo Full LOB preserva dados completos sem truncamento, enquanto a configuração do modo Inline LOB com dimensionamento de buffer apropriado e a divisão de tabelas grandes em tarefas paralelas otimizam o throughput."
                },
                {
                    "id": "B",
                    "text": "Excluir todas as colunas LOB do banco de dados SQL Server de origem antes da migração.",
                    "explanation": "Incorreto: A exclusão de dados LOB de produção causa perda permanente de dados e viola a integridade da aplicação."
                },
                {
                    "id": "C",
                    "text": "Mudar o mecanismo de replicação do AWS DMS para o modo sequencial single-threaded em uma instância t3.nano.",
                    "explanation": "Incorreto: O modo single-threaded em uma instância diminuta degrada severamente o desempenho da replicação."
                },
                {
                    "id": "D",
                    "text": "Usar o AWS Storage Gateway Volume Gateway para espelhar o banco de dados.",
                    "explanation": "Incorreto: O Storage Gateway não converte esquemas entre mecanismos de bancos de dados heterogêneos (SQL Server para PostgreSQL)."
                }
            ],
            "generalExplanation": "A otimização do AWS DMS para Grandes Objetos Binários (LOBs) requer a configuração dos modos Full LOB ou Inline LOB com tamanhos de bloco de LOB personalizados e distribuição paralela de tarefas."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa financiera está migrando una base de datos Microsoft SQL Server local de 20 TB a Amazon Aurora PostgreSQL. Durante la fase inicial de carga completa (full load), las tablas de la base de datos que contienen Objetos Binarios Grandes (LOBs) hacen que las tareas de migración de AWS DMS se ejecuten con extrema lentitud. La aplicación requiere replicar todos los datos LOB con precisión sin truncar la información. ¿Qué configuración de AWS DMS optimiza el rendimiento de la migración de LOBs?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar AWS DMS con el modo Limited LOB para la validación inicial y el modo Full LOB (o modo Inline LOB con un Max LOB Size optimizado) para tablas con columnas LOB grandes, dividiendo las tablas grandes en múltiples tareas de replicación dedicadas.",
                    "explanation": "Correcto: La optimización de LOB en AWS DMS implica ajustar los modos de LOB: el modo Full LOB preserva los datos completos sin truncamiento, mientras que la configuración del modo Inline LOB con el tamaño de búfer adecuado y la división de tablas grandes en tareas paralelas optimizan el rendimiento de transferencia."
                },
                {
                    "id": "B",
                    "text": "Eliminar todas las columnas LOB de la base de datos SQL Server de origen antes de la migración.",
                    "explanation": "Incorrecto: Eliminar los datos LOB de producción provoca una pérdida permanente de datos y viola la integridad de la aplicación."
                },
                {
                    "id": "C",
                    "text": "Cambiar el motor de replicación de AWS DMS al modo secuencial de un solo hilo (single-threaded) en una instancia t3.nano.",
                    "explanation": "Incorrecto: El modo de un solo hilo en una instancia minúscula degrada gravemente el rendimiento de la replicación."
                },
                {
                    "id": "D",
                    "text": "Utilizar AWS Storage Gateway Volume Gateway para duplicar la base de datos.",
                    "explanation": "Incorrecto: Storage Gateway no convierte esquemas entre motores de bases de datos heterogéneos (SQL Server a PostgreSQL)."
                }
            ],
            "generalExplanation": "Optimizar AWS DMS para Objetos Binarios Grandes (LOBs) requiere configurar los modos Full LOB o Inline LOB con tamaños de fragmento de LOB personalizados y distribución de tareas paralelas."
        }
    },
    "sap-sim3-q023": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma empresa deseja migrar um data warehouse Oracle local com scripts ETL complexos em PL/SQL para o Amazon Redshift. Antes de iniciar a migração, a equipe de arquitetura precisa de um relatório de avaliação automatizado detalhando a porcentagem de objetos de banco de dados que podem ser convertidos automaticamente versus aqueles que exigem refatoração manual, juntamente com orientações passo a passo para remediação. Qual ferramenta gera essa avaliação?",
            "options": [
                {
                    "id": "A",
                    "text": "Relatório de Avaliação de Migração de Banco de Dados do AWS Schema Conversion Tool (AWS SCT)",
                    "explanation": "Correto: O AWS SCT gera um Relatório de Avaliação de Migração de Banco de Dados abrangente que analisa esquemas, procedimentos armazenados (stored procedures) e código ETL, informando a porcentagem de conversão e destacando os itens de ação manual."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS Cost Explorer para visualizar gastos históricos consolidados da AWS e prever o uso futuro.",
                    "explanation": "Incorreto: O Cost Explorer analisa gastos na nuvem, e não a compatibilidade de código de esquemas de bancos de dados."
                },
                {
                    "id": "C",
                    "text": "Configurar e implantar o Amazon Inspector seguindo as melhores práticas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O Inspector verifica vulnerabilidades de segurança (CVEs) em softwares, e não a compatibilidade de PL/SQL com o SQL do Redshift."
                },
                {
                    "id": "D",
                    "text": "Configurar e implantar o AWS Application Discovery Service seguindo as melhores práticas do AWS Well-Architected Framework.",
                    "explanation": "Incorreto: O Application Discovery Service descobre máquinas virtuais de servidores e dependências de rede, e não a lógica de procedimentos armazenados em SQL/PL-SQL de bancos de dados."
                }
            ],
            "generalExplanation": "O Relatório de Avaliação de Migração de Banco de Dados do AWS Schema Conversion Tool (AWS SCT) avalia a complexidade da migração de esquemas heterogêneos de bancos de dados e destaca as tarefas de conversão manual."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Una empresa desea migrar un almacén de datos (data warehouse) Oracle local con scripts ETL complejos en PL/SQL a Amazon Redshift. Antes de iniciar la migración, el equipo de arquitectura necesita un informe de evaluación automatizado que detalle el porcentaje de objetos de la base de datos que se pueden convertir automáticamente frente a los que requieren refactorización manual, junto con una guía de corrección paso a paso. ¿Qué herramienta genera esta evaluación?",
            "options": [
                {
                    "id": "A",
                    "text": "Informe de Evaluación de Migración de Bases de Datos de AWS Schema Conversion Tool (AWS SCT)",
                    "explanation": "Correcto: AWS SCT genera un informe exhaustivo de evaluación de migración de base de datos que analiza esquemas, procedimientos almacenados y código ETL, informando el porcentaje de conversión y describiendo los elementos que requieren acción manual."
                },
                {
                    "id": "B",
                    "text": "Utilizar AWS Cost Explorer para visualizar los gastos históricos consolidados de AWS y pronosticar el uso futuro.",
                    "explanation": "Incorrecto: Cost Explorer analiza el gasto en la nube, no la compatibilidad del código de esquemas de bases de datos."
                },
                {
                    "id": "C",
                    "text": "Configurar e implementar Amazon Inspector siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Inspector analiza vulnerabilidades de seguridad CVE de software, no la compatibilidad de bases de datos PL/SQL con Redshift SQL."
                },
                {
                    "id": "D",
                    "text": "Configurar e implementar AWS Application Discovery Service siguiendo las mejores prácticas empresariales de AWS Well-Architected Framework.",
                    "explanation": "Incorrecto: Application Discovery Service descubre máquinas virtuales de servidores y dependencias de red, no la lógica de procedimientos almacenados SQL/PL-SQL dentro de la base de datos."
                }
            ],
            "generalExplanation": "El Informe de Evaluación de Migración de Bases de Datos de AWS Schema Conversion Tool (AWS SCT) evalúa la complejidad de migrar esquemas de bases de datos heterogéneas y destaca las tareas de conversión manual."
        }
    },
    "sap-sim3-q024": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "Uma equipe de engenharia de plataforma corporativa deseja fornecer modelos padronizados de infraestrutura e pipelines de implantação automatizados para centenas de equipes de desenvolvimento de microsserviços que implantam serviços em contêineres no Amazon ECS e Amazon EKS. A equipe de plataforma deve gerenciar as arquiteturas de ambiente centralmente, enquanto os desenvolvedores simplesmente enviam o código da aplicação e declaram parâmetros de serviço sem gerenciar modelos subjacentes do CloudFormation ou Terraform. Qual serviço da AWS foi desenvolvido especificamente para essa governança de engenharia de plataforma?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar o AWS OpsWorks Stacks para gerenciar a automação de configuração usando receitas Chef em instâncias Amazon EC2.",
                    "explanation": "Incorreto: O OpsWorks é um serviço gerenciado de configuração Chef/Puppet, não um orquestrador moderno de engenharia de plataforma de contêineres."
                },
                {
                    "id": "B",
                    "text": "Provisionar ambientes de desenvolvimento integrados na nuvem AWS Cloud9 para que os desenvolvedores editem o código da aplicação.",
                    "explanation": "Incorreto: O Cloud9 é um ambiente de desenvolvimento integrado (IDE) baseado em nuvem."
                },
                {
                    "id": "C",
                    "text": "Implantar o AWS Proton para gerenciar centralmente modelos padronizados de infraestrutura de ambiente e serviço para equipes de desenvolvimento.",
                    "explanation": "Correto: O AWS Proton é um serviço totalmente gerenciado para equipes de engenharia de plataforma fornecerem modelos padronizados de infraestrutura, pipelines automatizados de CI/CD e gerenciamento de ambientes para microsserviços executados em contêineres e serverless."
                },
                {
                    "id": "D",
                    "text": "Configurar o AWS CodeDeploy com modo de implantação in-place e scripts personalizados de hook de ciclo de vida de implantação em toda a frota.",
                    "explanation": "Incorreto: O CodeDeploy é um serviço individual de implantação, carecendo de governança centralizada de modelos de ambiente e abstrações de engenharia de plataforma."
                }
            ],
            "generalExplanation": "O AWS Proton é um serviço totalmente gerenciado de implantação de aplicações para contêineres e tecnologias sem servidor, permitindo que equipes de plataforma definam e gerenciem modelos de infraestrutura consistentes."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "Un equipo de ingeniería de plataformas empresariales desea proporcionar plantillas de infraestructura estandarizadas y canales de implementación automatizados para cientos de equipos de desarrollo de microservicios que implementan servicios en contenedores en Amazon ECS y Amazon EKS. El equipo de plataforma debe administrar las arquitecturas de entorno de forma centralizada, mientras que los desarrolladores simplemente envían el código de la aplicación y declaran los parámetros del servicio sin administrar plantillas subyacentes de CloudFormation o Terraform. ¿Qué servicio de AWS está diseñado específicamente para esta gobernanza de ingeniería de plataforma?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar AWS OpsWorks Stacks para administrar la automatización de la configuración mediante recetas de Chef en instancias de Amazon EC2.",
                    "explanation": "Incorrecto: OpsWorks es un servicio administrado de configuración de Chef/Puppet, no un orquestrador moderno de ingeniería de plataformas de contenedores."
                },
                {
                    "id": "B",
                    "text": "Aprovisionar entornos de desarrollo integrados en la nube AWS Cloud9 para que los desarrolladores editen el código de la aplicación.",
                    "explanation": "Incorrecto: Cloud9 es un entorno de desarrollo integrado (IDE) basado en la nube."
                },
                {
                    "id": "C",
                    "text": "Implementar AWS Proton para administrar de forma centralizada plantillas estándar de infraestructura de entornos y servicios para los equipos de desarrollo.",
                    "explanation": "Correcto: AWS Proton es un servicio totalmente administrado para que los equipos de ingeniería de plataformas proporcionen plantillas de infraestructura estándar, canales de CI/CD automatizados y administración de entornos para microservicios que se ejecutan en contenedores y tecnologías sin servidor."
                },
                {
                    "id": "D",
                    "text": "Configurar AWS CodeDeploy con el modo de implementación in-place y scripts personalizados de enlace (hook) de ciclo de vida de implementación en toda la flota.",
                    "explanation": "Incorrecto: CodeDeploy es un servicio de implementación individual que carece de gobernanza centralizada de plantillas de entorno y abstracciones de ingeniería de plataformas."
                }
            ],
            "generalExplanation": "AWS Proton es el primer servicio de implementación de aplicaciones totalmente administrado para aplicaciones sin servidor y en contenedores, lo que permite a los equipos de plataforma definir y administrar plantillas de infraestructura consistentes."
        }
    },
    "sap-sim3-q025": {
        "pt": {
            "domainName": "Domínio 4: Acelerar a Migração e Modernização de Cargas de Trabalho",
            "statement": "O CFO de uma empresa corporativa exige uma comparação abrangente de business case de Custo Total de Propriedade (TCO) antes de se comprometer com a migração de 2.000 servidores locais para a AWS. A análise deve modelar vários cenários de migração (incluindo Bring-Your-Own-License vs. licenciamento fornecido pela AWS, dimensionamento correto de computação com base na utilização histórica real de CPU/RAM e opções ideais de compra da AWS, como o Compute Savings Plans). Qual serviço da AWS fornece essa análise de business case?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Migration Evaluator (anteriormente TSO Logic) para analisar o inventário local e modelar business cases de custo total de propriedade.",
                    "explanation": "Correto: O AWS Migration Evaluator fornece modelagem gratuita de business case e análise de custo total de propriedade (TCO), analisando a utilização real de computação local e o licenciamento de software (Microsoft SQL/Windows) para projetar gastos otimizados na AWS."
                },
                {
                    "id": "B",
                    "text": "Baixar relatórios de conformidade e certificações regulatórias a partir do portal de autoatendimento AWS Artifact.",
                    "explanation": "Incorreto: O AWS Artifact fornece relatórios de auditoria de conformidade."
                },
                {
                    "id": "C",
                    "text": "Usar o AWS Pricing Calculator para modelar custos de arquitetura antes de provisionar recursos de infraestrutura da AWS.",
                    "explanation": "Incorreto: O Pricing Calculator exige a inserção manual de cada recurso e não analisa automaticamente o inventário real de servidores locais ou a otimização de licenciamento de software."
                },
                {
                    "id": "D",
                    "text": "Configurar o AWS Budgets para enviar notificações automáticas quando os limites de gastos mensais excederem limites predefinidos.",
                    "explanation": "Incorreto: O AWS Budgets destina-se a definir limites de gastos em contas existentes da AWS."
                }
            ],
            "generalExplanation": "O AWS Migration Evaluator (anteriormente TSO Logic) cria business cases orientados a dados para migração para a nuvem, analisando o inventário local e otimizando o dimensionamento correto de computação e o licenciamento de software."
        },
        "es": {
            "domainName": "Dominio 4: Acelerar la Migración y Modernización de Cargas de Trabajo",
            "statement": "El CFO de una empresa requiere una comparación exhaustiva de casos de negocio de Costo Total de Propiedad (TCO) antes de comprometerse a migrar 2.000 servidores locales a AWS. El análisis debe modelar múltiples escenarios de migración (incluyendo Bring-Your-Own-License vs licenciamiento proporcionado por AWS, dimensionamiento adecuado de cómputo basado en la utilización histórica real de CPU/RAM y opciones de compra óptimas de AWS como Compute Savings Plans). ¿Qué servicio de AWS proporciona este análisis de caso de negocio?",
            "options": [
                {
                    "id": "A",
                    "text": "Utilizar AWS Migration Evaluator (anteriormente TSO Logic) para analizar el inventario local y modelar casos de negocio de costo total de propiedad.",
                    "explanation": "Correcto: AWS Migration Evaluator proporciona modelado gratuito de casos de negocio y análisis de costo total de propiedad (TCO), analizando la utilización real de cómputo local y las licencias de software (Microsoft SQL/Windows) para proyectar un gasto optimizado en AWS."
                },
                {
                    "id": "B",
                    "text": "Descargar informes de cumplimiento y certificaciones regulatorias desde el portal de autoservicio de AWS Artifact.",
                    "explanation": "Incorrecto: AWS Artifact proporciona informes de auditoría de cumplimiento."
                },
                {
                    "id": "C",
                    "text": "Utilizar AWS Pricing Calculator para modelar los costos de arquitectura antes de aprovisionar recursos de infraestructura de AWS.",
                    "explanation": "Incorrecto: Pricing Calculator requiere la entrada manual de cada recurso y no analiza automáticamente el inventario real de servidores locales ni la optimización de licencias de software."
                },
                {
                    "id": "D",
                    "text": "Configurar AWS Budgets para enviar notificaciones automáticas cuando los límites de gasto mensual superen los umbrales predefinidos.",
                    "explanation": "Incorrecto: AWS Budgets es para establecer límites de gasto en cuentas de AWS existentes."
                }
            ],
            "generalExplanation": "AWS Migration Evaluator (anteriormente TSO Logic) crea casos de negocio basados en datos para la migración a la nube analizando el inventario local y optimizando el dimensionamiento adecuado del cómputo y las licencias de software."
        }
    }
}
