"""
Translations for AWS Solutions Architect - Associate (SAA-C03) Exam Questions 34 to 65.
Contains complete, high-quality, professional Portuguese (PT-BR) and Spanish (ES) translations.
"""

TRANSLATIONS = {
    "saa-q034": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa executa bancos de dados com estado (stateful) em instâncias Amazon EC2 com volumes Amazon EBS gp3. O plano de recuperação de desastres exige snapshots diários automatizados do EBS com um cronograma de retenção de 30 dias, além de uma cópia automatizada dos snapshots para uma Região AWS secundária para recuperação entre regiões. Qual solução atende a esses requisitos com o MENOR esforço operacional?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar uma política de ciclo de vida do Amazon Data Lifecycle Manager (Amazon DLM) direcionada às tags dos volumes EBS, com uma regra de cópia entre regiões para a região de destino e um período de retenção de 30 dias.",
                    "explanation": "Correto: O Amazon Data Lifecycle Manager (Amazon DLM) automatiza a criação, retenção e cópia entre regiões de snapshots do EBS por meio de políticas declarativas baseadas em tags, sem necessidade de scripts personalizados."
                },
                {
                    "id": "B",
                    "text": "Usar o AWS Storage Gateway Volume Gateway para espelhar todos os blocos de volume EBS continuamente para o S3.",
                    "explanation": "Incorreto: O Storage Gateway foi projetado para armazenamento híbrido on-premises, não para automação nativa de snapshots EBS do EC2."
                },
                {
                    "id": "C",
                    "text": "Escrever um script em Python em uma instância EC2 que chame a API ec2:CreateSnapshot e configurar um cron job.",
                    "explanation": "Incorreto: Scripts personalizados exigem manutenção, tratamento de erros e gerenciamento de servidores."
                },
                {
                    "id": "D",
                    "text": "Anexar um volume EBS adicional na região secundária diretamente à instância EC2 na região primária.",
                    "explanation": "Incorreto: Volumes EBS são estritamente zonais e não podem ser anexados entre Zonas de Disponibilidade ou Regiões AWS."
                }
            ],
            "generalExplanation": "O Amazon Data Lifecycle Manager (DLM) fornece uma maneira totalmente gerenciada e automatizada de criar, reter e replicar snapshots do EBS entre Regiões AWS com base em tags de recursos."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa ejecuta bases de datos con estado (stateful) en instancias Amazon EC2 con volúmenes Amazon EBS gp3. El plan de recuperación ante desastres requiere instantáneas (snapshots) diarias automatizadas de EBS con un programa de retención de 30 días, más una copia automatizada de las instantáneas a una Región de AWS secundaria para recuperación entre regiones. ¿Qué solución satisface estos requisitos con el MENOR esfuerzo operativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar una política de ciclo de vida de Amazon Data Lifecycle Manager (Amazon DLM) dirigida a las etiquetas de los volúmenes EBS, con una regla de copia entre regiones hacia la región de destino y un período de retención de 30 días.",
                    "explanation": "Correcto: Amazon Data Lifecycle Manager (Amazon DLM) automatiza la creación, retención y copia entre regiones de instantáneas de EBS mediante políticas declarativas basadas en etiquetas sin scripts personalizados."
                },
                {
                    "id": "B",
                    "text": "Utilizar AWS Storage Gateway Volume Gateway para reflejar todos los bloques de volumen EBS continuamente hacia S3.",
                    "explanation": "Incorrecto: Storage Gateway está diseñado para almacenamiento híbrido on-premises, no para la automatización nativa de instantáneas de EBS en EC2."
                },
                {
                    "id": "C",
                    "text": "Escribir un script en Python en una instancia EC2 que llame a la API ec2:CreateSnapshot y configurar un cron job.",
                    "explanation": "Incorrecto: Los scripts personalizados requieren mantenimiento, control de errores y administración de servidores."
                },
                {
                    "id": "D",
                    "text": "Adjuntar un volumen EBS adicional en la región secundaria directamente a la instancia EC2 en la región primaria.",
                    "explanation": "Incorrecto: Los volúmenes EBS son estrictamente zonales y no se pueden adjuntar entre Zonas de Disponibilidad o Regiones de AWS."
                }
            ],
            "generalExplanation": "Amazon Data Lifecycle Manager (DLM) proporciona una forma totalmente administrada y automatizada de crear, retener y replicar instantáneas de EBS entre Regiones de AWS según las etiquetas de recursos."
        }
    },
    "saa-q035": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma aplicação crítica de arquivamento armazena milhões de documentos contratuais de clientes em um bucket do Amazon S3. A empresa exige proteção contra exclusões acidentais ou sobregravações de objetos por funcionários, bem como a capacidade de restaurar qualquer arquivo excluído acidentalmente de forma imediata. Qual solução o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar o Versionamento do Amazon S3 (S3 Versioning) no bucket.",
                    "explanation": "Correto: O versionamento do S3 preserva versões anteriores de objetos mediante sobregravação ou exclusão. Se um objeto for excluído, o S3 cria um marcador de exclusão (delete marker), permitindo que a versão anterior seja recuperada ou restaurada instantaneamente."
                },
                {
                    "id": "B",
                    "text": "Criar uma política do IAM negando a ação s3:GetObject para todos os funcionários.",
                    "explanation": "Incorreto: Negar GetObject impede que os funcionários leiam os documentos, quebrando o funcionamento da aplicação."
                },
                {
                    "id": "C",
                    "text": "Habilitar os Logs de Acesso ao Servidor do S3 (Server Access Logging) e analisar os logs para recriar objetos excluídos.",
                    "explanation": "Incorreto: Os logs de acesso ao servidor do S3 registram apenas metadados de requisições; eles não retêm os dados binários excluídos."
                },
                {
                    "id": "D",
                    "text": "Configurar uma regra de Ciclo de Vida do S3 para transicionar objetos para o S3 Glacier Flexible Archive após 1 hora.",
                    "explanation": "Incorreto: A transição de ciclo de vida para o Glacier altera a camada de armazenamento, mas não impede a exclusão nem preserva versões."
                }
            ],
            "generalExplanation": "O Versionamento do Amazon S3 mantém múltiplas variantes de um objeto no mesmo bucket, permitindo que você recupere facilmente dados contra ações não intencionais de usuários ou falhas de aplicações."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una aplicación de archivado crítico almacena millones de documentos de contratos de clientes en un bucket de Amazon S3. El negocio requiere protección contra eliminaciones o sobrescrituras accidentales de objetos por parte de los empleados, así como la capacidad de restaurar inmediatamente cualquier archivo eliminado por error. ¿Qué solución debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Habilitar el control de versiones de Amazon S3 (S3 Versioning) en el bucket.",
                    "explanation": "Correcto: El control de versiones de S3 conserva las versiones anteriores de los objetos al sobrescribirlos o eliminarlos. Si se elimina un objeto, S3 crea un marcador de eliminación (delete marker), lo que permite recuperar o restaurar la versión anterior al instante."
                },
                {
                    "id": "B",
                    "text": "Crear una política de IAM que deniegue la acción s3:GetObject a todos los empleados.",
                    "explanation": "Incorrecto: Denegar GetObject impide que los empleados lean los documentos, lo que interrumpe la funcionalidad de la aplicación."
                },
                {
                    "id": "C",
                    "text": "Habilitar el registro de acceso al servidor de S3 (Server Access Logging) y revisar los registros para recrear los objetos eliminados.",
                    "explanation": "Incorrecto: Los registros de acceso al servidor de S3 solo registran metadatos de solicitudes; no conservan los datos binarios eliminados."
                },
                {
                    "id": "D",
                    "text": "Configurar una regla de ciclo de vida de S3 para realizar la transición de objetos a S3 Glacier Flexible Archive después de 1 hora.",
                    "explanation": "Incorrecto: La transición del ciclo de vida a Glacier cambia el nivel de almacenamiento, pero no evita la eliminación ni conserva versiones."
                }
            ],
            "generalExplanation": "El control de versiones de Amazon S3 mantiene múltiples variantes de un objeto en el mismo bucket, lo que permite recuperarse fácilmente de acciones no deseadas de usuarios y fallos de aplicaciones."
        }
    },
    "saa-q036": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma empresa de serviços financeiros executa um banco de dados Oracle em uma instância de banco de dados Amazon RDS Multi-AZ. A carga de trabalho de leitura durante os horários de abertura do mercado está fazendo com que a utilização de CPU atinja 98%, desacelerando gravações transacionais críticas. Como o arquiteto pode descarregar as consultas de relatórios de leitura intensa com o MENOR impacto no desempenho de gravação transacional?",
            "options": [
                {
                    "id": "A",
                    "text": "Encaminhar consultas de leitura diretamente para a instância em espera (standby) da implantação RDS Multi-AZ.",
                    "explanation": "Incorreto: Em uma implantação RDS Multi-AZ padrão, a instância em espera é puramente passiva e não aceita conexões de leitura ou gravação."
                },
                {
                    "id": "B",
                    "text": "Criar uma ou mais Réplicas de Leitura do RDS (Read Replicas) para o banco de dados e direcionar o tráfego de relatórios somente leitura para os endpoints das Réplicas de Leitura.",
                    "explanation": "Correto: As Réplicas de Leitura do Amazon RDS descarregam o tráfego de leitura da instância de banco de dados primária, liberando recursos na instância primária para operações de gravação transacional."
                },
                {
                    "id": "C",
                    "text": "Habilitar Backups Automatizados durante o horário de abertura do mercado para armazenar em cache os resultados das consultas.",
                    "explanation": "Incorreto: Executar backups durante horários de pico adiciona sobrecarga de E/S e não fornece cache de consultas."
                },
                {
                    "id": "D",
                    "text": "Converter o banco de dados para uma tabela do Amazon DynamoDB usando o AWS Database Migration Service (DMS) durante o horário de pico.",
                    "explanation": "Incorreto: Migrar um banco de dados relacional para NoSQL exige refatoração significativa de esquema e não pode ser feito como uma correção pontual em horários de pico."
                }
            ],
            "generalExplanation": "As Réplicas de Leitura do RDS permitem que cargas de trabalho com leitura intensa sejam descarregadas da instância primária, melhorando a taxa de transferência de gravação e a capacidade de resposta geral do banco de dados."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una empresa de servicios financieros ejecuta una base de datos Oracle en una instancia de base de datos Amazon RDS Multi-AZ. La carga de trabajo de lectura durante las horas de apertura del mercado provoca que el uso de la CPU alcance el 98%, ralentizando las escrituras transaccionales críticas. ¿Cómo puede el arquitecto descargar las consultas de informes de lectura intensiva con el MENOR impacto en el rendimiento de escritura transaccional?",
            "options": [
                {
                    "id": "A",
                    "text": "Enrutar las consultas de lectura directamente a la instancia en espera (standby) de la implementación RDS Multi-AZ.",
                    "explanation": "Incorrecto: En una implementación estándar de RDS Multi-AZ, la instancia en espera es puramente pasiva y no acepta conexiones de lectura ni de escritura."
                },
                {
                    "id": "B",
                    "text": "Crear una o más Réplicas de Lectura de RDS (Read Replicas) para la base de datos y dirigir el tráfico de informes de solo lectura a los endpoints de las Réplicas de Lectura.",
                    "explanation": "Correcto: Las Réplicas de Lectura de Amazon RDS descargan el tráfico de lectura de la instancia principal de la base de datos, liberando recursos en la instancia principal para operaciones de escritura transaccionales."
                },
                {
                    "id": "C",
                    "text": "Habilitar Copias de Seguridad Automatizadas durante las horas de apertura del mercado para almacenar en caché los resultados de las consultas.",
                    "explanation": "Incorrecto: Ejecutar copias de seguridad en horas pico genera sobrecarga de E/S y no sirve para almacenar en caché las consultas."
                },
                {
                    "id": "D",
                    "text": "Convertir la base de datos a una tabla de Amazon DynamoDB mediante AWS Database Migration Service (DMS) durante las horas pico.",
                    "explanation": "Incorrecto: Migrar una base de datos relacional a NoSQL requiere una refactorización sustancial del esquema y no puede realizarse como una solución improvisada durante las horas pico."
                }
            ],
            "generalExplanation": "Las Réplicas de Lectura de RDS permiten descargar las cargas de trabajo de lectura intensa de la instancia principal, mejorando el rendimiento de escritura y la capacidad de respuesta general de la base de datos."
        }
    },
    "saa-q037": {
        "pt": {
            "domainName": "Domínio 2: Projetar Arquiteturas Resilientes",
            "statement": "Uma organização hospeda uma aplicação web em duas Regiões AWS usando Application Load Balancers. A empresa deseja que usuários na Europa sejam roteados para a região europeia, usuários na Ásia sejam roteados para a região asiática e usuários de qualquer outro local sejam direcionados para um endpoint padrão. Qual política de roteamento do Amazon Route 53 deve ser configurada?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar uma política de roteamento de resposta de vários valores (Multi-Value Answer) do Amazon Route 53 para retornar múltiplos registros de IP íntegros.",
                    "explanation": "Incorreto: O roteamento Multi-Value retorna múltiplos endereços IP para balanceamento de carga no lado do cliente DNS, não para localização geográfica."
                },
                {
                    "id": "B",
                    "text": "Política de roteamento de geolocalização (Geolocation routing) com um local de registro padrão configurado.",
                    "explanation": "Correto: O roteamento de geolocalização do Route 53 direciona consultas DNS com base na localização geográfica do usuário (continente ou país) e permite definir um registro padrão para locais não mapeados."
                },
                {
                    "id": "C",
                    "text": "Configurar uma política de roteamento baseada em latência do Amazon Route 53 para direcionar usuários ao endpoint regional de menor latência.",
                    "explanation": "Incorreto: O roteamento por latência direciona o tráfego para a região com menor latência de rede, o que não garante limites estritos baseados em continentes."
                },
                {
                    "id": "D",
                    "text": "Configurar uma política de roteamento ponderado (Weighted routing) do Amazon Route 53 com uma proporção de 50/50 entre as regiões.",
                    "explanation": "Incorreto: O roteamento ponderado distribui o tráfego de forma probabilística por proporção, não pela localização do usuário."
                }
            ],
            "generalExplanation": "O roteamento de geolocalização do Amazon Route 53 permite escolher os recursos que atendem ao tráfego com base na localização geográfica dos usuários, com suporte a registros padrão de fallback."
        },
        "es": {
            "domainName": "Dominio 2: Diseñar Arquitecturas Resilientes",
            "statement": "Una organización aloja una aplicación web en dos Regiones de AWS mediante Application Load Balancers. La empresa desea que los usuarios en Europa sean dirigidos a la región europea, los usuarios en Asia a la región asiática y los usuarios de cualquier otra ubicación sean dirigidos a un endpoint predeterminado. ¿Qué política de enrutamiento de Amazon Route 53 se debe configurar?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar una política de enrutamiento de respuesta de varios valores (Multi-Value Answer) de Amazon Route 53 para devolver múltiples registros IP en buen estado.",
                    "explanation": "Incorrecto: El enrutamiento Multi-Value devuelve múltiples direcciones IP para el balanceo de carga del lado del cliente DNS, no para la localización geográfica."
                },
                {
                    "id": "B",
                    "text": "Política de enrutamiento por geolocalización (Geolocation routing) con una ubicación de registro predeterminada configurada.",
                    "explanation": "Correcto: El enrutamiento por geolocalización de Route 53 enruta las consultas DNS según la ubicación geográfica del usuario (continente o país) y permite configurar un registro predeterminado para ubicaciones no asignadas."
                },
                {
                    "id": "C",
                    "text": "Configurar una política de enrutamiento basada en latencia de Amazon Route 53 para dirigir a los usuarios al endpoint regional con menor latencia.",
                    "explanation": "Incorrecto: El enrutamiento por latencia dirige el tráfico a la región con menor latencia de red, lo que no garantiza límites estrictos basados en continentes."
                },
                {
                    "id": "D",
                    "text": "Configurar una política de enrutamiento ponderado (Weighted routing) de Amazon Route 53 con una proporción de 50/50 entre regiones.",
                    "explanation": "Incorrecto: El enrutamiento ponderado distribuye el tráfico probabilísticamente por ratio, no según la ubicación del usuario."
                }
            ],
            "generalExplanation": "El enrutamiento por geolocalización de Amazon Route 53 le permite elegir los recursos que atienden el tráfico en función de la ubicación geográfica de los usuarios con registros predeterminados de respaldo."
        }
    },
    "saa-q038": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma aplicação de placar de jogos móveis usa o Amazon DynamoDB para armazenar as pontuações dos jogadores. Durante torneios ao vivo, o tráfego de consultas de leitura atinge picos de centenas de milhares de solicitações por segundo em itens populares do placar. A equipe de desenvolvimento precisa reduzir a latência de leitura de milissegundos de dígito único para níveis de microssegundos SEM reescrever a lógica de acesso a dados da aplicação ou gerenciar pipelines de invalidação de cache separados. Qual solução o arquiteto deve implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Aumentar as Unidades de Capacidade de Leitura Provisionadas (RCUs) na tabela do DynamoDB para 100.000 RCUs.",
                    "explanation": "Incorreto: Aumentar as RCUs lida com o volume, mas não reduz a latência de milissegundos para microssegundos."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster do Amazon ElastiCache for Memcached e modificar o código da aplicação para consultar o Memcached antes do DynamoDB.",
                    "explanation": "Incorreto: O ElastiCache exige alterações de código para implementar a lógica de cache-aside e gerenciar a invalidação de cache."
                },
                {
                    "id": "C",
                    "text": "Implantar um cluster do Amazon DynamoDB Accelerator (DAX) e atualizar o endpoint do SDK da aplicação para apontar para o DAX.",
                    "explanation": "Correto: O DynamoDB Accelerator (DAX) é um cache em memória totalmente gerenciado para o DynamoDB que oferece tempos de resposta em microssegundos e é compatível com a API sem alterar o modelo de dados ou o código."
                },
                {
                    "id": "D",
                    "text": "Migrar a tabela do DynamoDB para o Amazon RDS PostgreSQL e criar réplicas de leitura.",
                    "explanation": "Incorreto: Bancos de dados relacionais exigem refatoração completa da aplicação e não fornecem desempenho de microssegundos em memória como o DAX."
                }
            ],
            "generalExplanation": "O Amazon DynamoDB Accelerator (DAX) oferece cache em memória integrado que acelera leituras em até 10x (de milissegundos para microssegundos) sem nenhuma reescrita na lógica de dados."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una aplicación de tabla de clasificación de juegos móviles utiliza Amazon DynamoDB para almacenar las puntuaciones de los jugadores. Durante los torneos en vivo, el tráfico de consultas de lectura experimenta picos de cientos de miles de solicitudes por segundo en los elementos más consultados. El equipo de desarrollo necesita reducir la latencia de lectura de milisegundos de un solo dígito a microsegundos SIN reescribir la lógica de acceso a datos de la aplicación ni administrar canales de invalidación de caché independientes. ¿Qué solución debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Aumentar las Unidades de Capacidad de Lectura Provisionadas (RCUs) en la tabla DynamoDB a 100.000 RCUs.",
                    "explanation": "Incorrecto: Aumentar las RCUs maneja el volumen pero no reduce la latencia de milisegundos a microsegundos."
                },
                {
                    "id": "B",
                    "text": "Implementar un clúster de Amazon ElastiCache for Memcached y modificar el código de la aplicación para comprobar Memcached antes de consultar DynamoDB.",
                    "explanation": "Incorrecto: ElastiCache requiere cambios en el código para implementar la lógica de cache-aside y administrar la invalidación de la caché."
                },
                {
                    "id": "C",
                    "text": "Implementar un clúster de Amazon DynamoDB Accelerator (DAX) y actualizar el endpoint del SDK de la aplicación para que apunte a DAX.",
                    "explanation": "Correcto: DynamoDB Accelerator (DAX) es una caché en memoria totalmente administrada para DynamoDB que ofrece tiempos de respuesta en microsegundos y es compatible con la API sin cambiar el código del modelo de datos."
                },
                {
                    "id": "D",
                    "text": "Migrar la tabla de DynamoDB a Amazon RDS PostgreSQL y crear réplicas de lectura.",
                    "explanation": "Incorrecto: Las bases de datos relacionales requieren una refactorización completa de la aplicación y no proporcionan el rendimiento de microsegundos en memoria como DAX."
                }
            ],
            "generalExplanation": "Amazon DynamoDB Accelerator (DAX) proporciona almacenamiento en caché en memoria que acelera las lecturas hasta 10 veces (de milisegundos a microsegundos) sin reescribir la lógica de datos."
        }
    },
    "saa-q039": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um banco de dados de processamento de transações online (OLTP) de alto desempenho em uma instância EC2 requer um volume de armazenamento em bloco persistente capaz de sustentar até 80.000 IOPS e 2.000 MB/s de taxa de transferência (throughput) com latência abaixo de um milissegundo e durabilidade de 99,999%. Qual tipo de volume Amazon EBS deve ser selecionado?",
            "options": [
                {
                    "id": "A",
                    "text": "SSD com IOPS Provisionadas (io2 ou io2 Block Express)",
                    "explanation": "Correto: Volumes io2 Block Express oferecem até 256.000 IOPS, 4.000 MB/s de throughput, latência sub-milissegundo e durabilidade de 99,999% para bancos de dados de missão crítica."
                },
                {
                    "id": "B",
                    "text": "Provisionar um volume Amazon EBS SSD de Uso Geral (gp3) com desempenho de linha de base padrão.",
                    "explanation": "Incorreto: O gp3 atinge no máximo 16.000 IOPS e 1.000 MB/s de taxa de transferência, o que é insuficiente para 80.000 IOPS."
                },
                {
                    "id": "C",
                    "text": "Provisionar um volume Amazon EBS HDD com Throughput Otimizado (st1) para cargas de trabalho sequenciais de blocos grandes.",
                    "explanation": "Incorreto: O st1 é armazenamento magnético projetado para throughput sequencial de blocos grandes (máx. 500 IOPS) e não pode inicializar nem suportar IOPS aleatórias intensivas."
                },
                {
                    "id": "D",
                    "text": "Provisionar um volume Amazon EBS Cold HDD (sc1) para armazenamento magnético frio de menor custo.",
                    "explanation": "Incorreto: O sc1 é um armazenamento magnético de menor custo para cargas de trabalho sequenciais acessadas com pouca frequência (máx. 250 IOPS)."
                }
            ],
            "generalExplanation": "Os volumes Amazon EBS SSD de IOPS Provisionadas io2 Block Express são projetados para as cargas de trabalho de banco de dados mais exigentes e com uso intensivo de E/S, suportando até 256.000 IOPS e 4.000 MB/s."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una base de datos de procesamiento de transacciones en línea (OLTP) de alto rendimiento en una instancia EC2 requiere un volumen de almacenamiento en bloque persistente capaz de soportar hasta 80.000 IOPS y 2.000 MB/s de rendimiento con latencia inferior a un milisegundo y durabilidad del 99,999%. ¿Qué tipo de volumen Amazon EBS se debe seleccionar?",
            "options": [
                {
                    "id": "A",
                    "text": "SSD de IOPS provisionadas (io2 o io2 Block Express)",
                    "explanation": "Correcto: Los volúmenes io2 Block Express ofrecen hasta 256.000 IOPS, 4.000 MB/s de rendimiento, latencia sub-milisegundo y durabilidad del 99,999% para bases de datos de misión crítica."
                },
                {
                    "id": "B",
                    "text": "Aprovisionar un volumen Amazon EBS SSD de uso general (gp3) con rendimiento base estándar.",
                    "explanation": "Incorrecto: gp3 alcanza un máximo de 16.000 IOPS y 1.000 MB/s de rendimiento, lo cual es insuficiente para 80.000 IOPS."
                },
                {
                    "id": "C",
                    "text": "Aprovisionar un volumen Amazon EBS HDD optimizado para rendimiento (st1) para cargas de trabajo secuenciales de bloques grandes.",
                    "explanation": "Incorrecto: st1 es almacenamiento magnético diseñado para rendimiento secuencial de bloques grandes (máx. 500 IOPS) y no puede arrancar ni admitir IOPS aleatorias intensivas."
                },
                {
                    "id": "D",
                    "text": "Aprovisionar un volumen Amazon EBS Cold HDD (sc1) para almacenamiento magnético frío de menor coste.",
                    "explanation": "Incorrecto: sc1 es almacenamiento magnético de bajo coste para cargas de trabajo secuenciales a las que se accede con poca frecuencia (máx. 250 IOPS)."
                }
            ],
            "generalExplanation": "Los volúmenes Amazon EBS SSD de IOPS provisionadas io2 Block Express están diseñados para las cargas de trabajo de bases de datos más exigentes con uso intensivo de E/S, soportando hasta 256.000 IOPS y 4.000 MB/s."
        }
    },
    "saa-q040": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um sistema de gerenciamento de conteúdo (CMS) em contêineres é executado em centenas de tarefas do Amazon ECS e instâncias Linux do Amazon EC2 distribuídas em três Zonas de Disponibilidade. Todas as instâncias devem ler e gravar em um sistema de arquivos compartilhado compatível com POSIX simultaneamente, com alta taxa de transferência e forte suporte a bloqueio de arquivos (file locking). Qual serviço de armazenamento atende a esses requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Standard com S3 File Gateway",
                    "explanation": "Incorreto: O S3 é armazenamento de objetos (não um sistema de arquivos POSIX nativo com bloqueio granular de arquivos) e o File Gateway destina-se a configurações híbridas on-premises."
                },
                {
                    "id": "B",
                    "text": "Amazon Elastic File System (Amazon EFS)",
                    "explanation": "Correto: O Amazon EFS fornece armazenamento de arquivos compartilhado sem servidor (serverless), totalmente gerenciado, Multi-AZ e compatível com POSIX para acesso simultâneo por centenas de instâncias Linux e contêineres."
                },
                {
                    "id": "C",
                    "text": "Amazon Elastic Block Store (Amazon EBS) com Multi-Attach",
                    "explanation": "Incorreto: O EBS Multi-Attach funciona apenas com volumes io2 dentro de uma única AZ, não entre múltiplas Zonas de Disponibilidade."
                },
                {
                    "id": "D",
                    "text": "Amazon FSx for Lustre no modo de implantação Scratch",
                    "explanation": "Incorreto: O FSx for Lustre Scratch é um armazenamento temporário não replicado projetado para picos de computação HPC, não para armazenamento persistente de CMS multi-AZ."
                }
            ],
            "generalExplanation": "O Amazon EFS é um sistema de arquivos NFS elástico, escalável e totalmente gerenciado que pode ser montado simultaneamente por milhares de instâncias de computação em múltiplas Zonas de Disponibilidade."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un sistema de gestión de contenidos (CMS) en contenedores se ejecuta en cientos de tareas de Amazon ECS e instancias Linux de Amazon EC2 distribuidas en tres Zonas de Disponibilidad. Todas las instancias deben leer y escribir en un sistema de archivos compartido compatible con POSIX simultáneamente con alto rendimiento y soporte sólido para bloqueo de archivos (file locking). ¿Qué servicio de almacenamiento satisface estos requisitos?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Standard con S3 File Gateway",
                    "explanation": "Incorrecto: S3 es almacenamiento de objetos (no un sistema de archivos POSIX nativo con bloqueo granular de archivos) y File Gateway está diseñado para entornos híbridos on-premises."
                },
                {
                    "id": "B",
                    "text": "Amazon Elastic File System (Amazon EFS)",
                    "explanation": "Correcto: Amazon EFS proporciona almacenamiento de archivos compartido sin servidor, totalmente administrado, Multi-AZ y compatible con POSIX para acceso simultáneo de cientos de instancias Linux y contenedores."
                },
                {
                    "id": "C",
                    "text": "Amazon Elastic Block Store (Amazon EBS) con Multi-Attach",
                    "explanation": "Incorrecto: EBS Multi-Attach solo funciona con volúmenes io2 dentro de una única AZ, no a través de múltiples Zonas de Disponibilidad."
                },
                {
                    "id": "D",
                    "text": "Amazon FSx for Lustre en modo de implementación Scratch",
                    "explanation": "Incorrecto: Scratch FSx for Lustre es almacenamiento temporal no replicado diseñado para picos de computación HPC, no para almacenamiento persistente multi-AZ de CMS."
                }
            ],
            "generalExplanation": "Amazon EFS es un sistema de archivos NFS elástico, escalable y totalmente administrado que puede ser montado simultáneamente por miles de instancias de cómputo en múltiples Zonas de Disponibilidad."
        }
    },
    "saa-q041": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um laboratório de pesquisa genômica executa treinamentos distribuídos de machine learning e cargas de trabalho de sequenciamento genômico usando um cluster de computação Amazon EC2. A aplicação requer um sistema de arquivos paralelo compatível com POSIX capaz de fornecer centenas de gigabytes por segundo de throughput, latências abaixo de um milissegundo e milhões de IOPS, com sincronização de dados nativa vinculada diretamente a um data lake no Amazon S3. Qual serviço de armazenamento o arquiteto deve implantar?",
            "options": [
                {
                    "id": "A",
                    "text": "Volumes Amazon EBS gp3 configurados em RAID 0 em uma única instância",
                    "explanation": "Incorreto: Um RAID 0 de instância única não pode ser compartilhado em um cluster de computação distribuído e não possui integração nativa com o S3."
                },
                {
                    "id": "B",
                    "text": "Amazon FSx for Windows File Server",
                    "explanation": "Incorreto: O FSx for Windows é otimizado para cargas de trabalho SMB/Windows, não para tarefas paralelas de alto rendimento de genômica em Linux HPC."
                },
                {
                    "id": "C",
                    "text": "Implantar um sistema de arquivos paralelo de alto desempenho Amazon FSx for Lustre vinculado ao Amazon S3.",
                    "explanation": "Correto: O Amazon FSx for Lustre é um sistema de arquivos paralelo de alto desempenho projetado especificamente para cargas de trabalho de computação intensiva de HPC, ML e big data, com integração bidirecional contínua com o Amazon S3."
                },
                {
                    "id": "D",
                    "text": "Amazon EFS no modo General Purpose",
                    "explanation": "Incorreto: O Amazon EFS não oferece throughput de cluster paralelo na escala de centenas de GB/s para cargas de trabalho de treinamento HPC/ML como o FSx for Lustre."
                }
            ],
            "generalExplanation": "O Amazon FSx for Lustre oferece armazenamento paralelo ultrarrápido para HPC, machine learning e processamento de vídeo, vinculando-se perfeitamente e diretamente a buckets do Amazon S3."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un laboratorio de investigación genómica ejecuta entrenamientos distribuidos de machine learning y cargas de trabajo de secuenciación genómica mediante un clúster de cómputo de Amazon EC2. La aplicación requiere un sistema de archivos paralelo compatible con POSIX capaz de ofrecer cientos de gigabytes por segundo de rendimiento, latencias de sub-milisegundos y millones de IOPS, con sincronización de datos nativa vinculada directamente a un data lake en Amazon S3. ¿Qué servicio de almacenamiento debe implementar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Volúmenes Amazon EBS gp3 configurados en RAID 0 en una sola instancia",
                    "explanation": "Incorrecto: Un RAID 0 en una sola instancia no se puede compartir en un clúster de cómputo distribuido y carece de integración nativa con S3."
                },
                {
                    "id": "B",
                    "text": "Amazon FSx for Windows File Server",
                    "explanation": "Incorrecto: FSx for Windows está optimizado para cargas de trabajo SMB/Windows, no para trabajos de genómica paralelos en Linux HPC de alto rendimiento."
                },
                {
                    "id": "C",
                    "text": "Implementar un sistema de archivos paralelo de alto rendimiento Amazon FSx for Lustre vinculado a Amazon S3.",
                    "explanation": "Correcto: Amazon FSx for Lustre es un sistema de archivos paralelo de alto rendimiento diseñado específicamente para cargas de trabajo intensivas en cómputo de HPC, ML y big data, con integración bidireccional perfecta con Amazon S3."
                },
                {
                    "id": "D",
                    "text": "Amazon EFS en modo General Purpose",
                    "explanation": "Incorrecto: Amazon EFS no proporciona rendimiento de clúster paralelo en cientos de GB/s para cargas de trabajo de entrenamiento HPC/ML como FSx for Lustre."
                }
            ],
            "generalExplanation": "Amazon FSx for Lustre proporciona almacenamiento paralelo ultrarrápido para HPC, machine learning y procesamiento de video, vinculándose de forma nativa directamente a buckets de Amazon S3."
        }
    },
    "saa-q042": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma empresa global de streaming de mídia entrega miniaturas de vídeo sob demanda e artigos de notícias dinâmicos. Usuários em diferentes continentes relatam tempos lentos de carregamento de página. O arquiteto precisa armazenar em cache imagens estáticas e respostas de API dinâmicas próximas aos usuários finais, aplicar compactação gzip/Brotli e executar lógica leve de reescrita de URL nas bordas com a menor latência de execução. Qual solução deve ser implementada?",
            "options": [
                {
                    "id": "A",
                    "text": "Usar o AWS Global Accelerator com Replicação Entre Regiões do S3 para todas as 30 regiões da AWS.",
                    "explanation": "Incorreto: A replicação do S3 para todas as regiões gera custos maciços de armazenamento e o Global Accelerator não armazena payloads HTTP em cache nem realiza reescritas de URL."
                },
                {
                    "id": "B",
                    "text": "Instalar servidores proxy de cache Squid em instâncias Amazon EC2 em cada sub-rede pública.",
                    "explanation": "Incorreto: Proxies Squid autogerenciados adicionam alta sobrecarga operacional e de manutenção e não alcançam a escala global de CDN de borda."
                },
                {
                    "id": "C",
                    "text": "Implantar um Application Load Balancer em cada região da AWS e configurar o roteamento ponderado do Route 53.",
                    "explanation": "Incorreto: Implantar ALBs em cada região é caro, não oferece cache de borda e não disponibiliza funções de computação de borda integradas."
                },
                {
                    "id": "D",
                    "text": "Implantar o Amazon CloudFront com CloudFront Functions para reescritas de URL na borda e configurar políticas de cache para compactação.",
                    "explanation": "Correto: O CloudFront armazena em cache respostas estáticas e dinâmicas em mais de 400 locais de borda, e o CloudFront Functions executa reescritas leves de URL em JavaScript com latência abaixo de um milissegundo diretamente na borda do visualizador."
                }
            ],
            "generalExplanation": "O Amazon CloudFront fornece cache global de conteúdo e computação na borda via CloudFront Functions para manipulação de cabeçalhos e reescritas de URL com latência ultrabaixa."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una empresa global de transmisión de medios ofrece miniaturas de video bajo demanda y artículos de noticias dinámicos. Los usuarios de diferentes continentes informan tiempos lentos de carga de páginas. El arquitecto debe almacenar en caché tanto imágenes estáticas como respuestas de API dinámicas cerca de los usuarios finales, aplicar compresión gzip/Brotli y ejecutar una lógica ligera de reescritura de URL en ubicaciones perimetrales con la latencia de ejecución más baja. ¿Qué solución se debe implementar?",
            "options": [
                {
                    "id": "A",
                    "text": "Utilizar AWS Global Accelerator con replicación entre regiones de S3 en las 30 regiones de AWS.",
                    "explanation": "Incorrecto: La replicación de S3 a todas las regiones genera costes masivos de almacenamiento y Global Accelerator no almacena en caché payloads HTTP ni realiza reescrituras de URL."
                },
                {
                    "id": "B",
                    "text": "Instalar servidores proxy de caché Squid en instancias Amazon EC2 en cada subred pública.",
                    "explanation": "Incorrecto: Los proxies Squid autoadministrados agregan un alto mantenimiento y sobrecarga operativa, y no pueden igualar la escala de CDN perimetral global."
                },
                {
                    "id": "C",
                    "text": "Implementar un Application Load Balancer en cada región de AWS y configurar el enrutamiento ponderado de Route 53.",
                    "explanation": "Incorrecto: Implementar ALBs en cada región es costoso, carece de almacenamiento en caché perimetral y no proporciona funciones de cómputo en el borde."
                },
                {
                    "id": "D",
                    "text": "Implementar Amazon CloudFront con CloudFront Functions para reescrituras de URL perimetrales y configurar políticas de caché para compresión.",
                    "explanation": "Correcto: CloudFront almacena en caché respuestas estáticas y dinámicas en más de 400 ubicaciones perimetrales, y CloudFront Functions ejecuta reescrituras ligeras de URL en JavaScript en menos de un milisegundo directamente en el borde del espectador."
                }
            ],
            "generalExplanation": "Amazon CloudFront proporciona almacenamiento en caché de contenido global y computación en el borde mediante CloudFront Functions para reescrituras de URL y manipulaciones de encabezados de ultrabaja latencia."
        }
    },
    "saa-q043": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um portal de notícias de alto tráfego enfrenta extrema contenção de leitura em um banco de dados Amazon RDS MySQL durante eventos de notícias de última hora. Os artigos de notícias são lidos frequentemente por milhões de usuários, mas atualizados raramente pelos editores. A arquitetura precisa de uma camada de cache em memória de alto desempenho que suporte estruturas de dados complexas, operações multi-thread, failover automático e persistência de dados. Qual mecanismo de cache o arquiteto deve escolher?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon ElastiCache for Redis (ou Valkey)",
                    "explanation": "Correto: O ElastiCache for Redis/Valkey oferece suporte a estruturas de dados avançadas, persistência, replicação com failover automático Multi-AZ e réplicas de leitura."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster de cache em memória multi-thread Amazon ElastiCache for Memcached.",
                    "explanation": "Incorreto: O Memcached é um armazenamento simples de chave-valor puramente em memória que não suporta persistência de dados, replicação ou failover automático."
                },
                {
                    "id": "C",
                    "text": "Criar uma tabela do Amazon DynamoDB configurada no modo de capacidade sob demanda para tráfego intermitente.",
                    "explanation": "Incorreto: O DynamoDB é um banco de dados NoSQL persistente, não uma camada de cache em memória para um banco de dados relacional RDS existente."
                },
                {
                    "id": "D",
                    "text": "Criar um domínio gerenciado do Amazon CloudSearch para indexação de pesquisa de texto em documentos personalizados.",
                    "explanation": "Incorreto: O CloudSearch é um mecanismo de busca gerenciado, não um cache de banco de dados em memória de baixa latência."
                }
            ],
            "generalExplanation": "O Amazon ElastiCache for Redis fornece cache em memória com suporte a tipos de dados complexos, persistência, clustering e replicação Multi-AZ com failover automatizado."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un portal de noticias de gran tráfico experimenta una extrema contención de lectura en una base de datos Amazon RDS MySQL durante noticias de última hora. Millones de usuarios leen los artículos con frecuencia, pero los editores los actualizan raramente. La arquitectura necesita una capa de almacenamiento en caché en memoria de alto rendimiento que admita estructuras de datos complejas, operaciones multiproceso, conmutación por error automática y persistencia de datos. ¿Qué motor de caché debe elegir el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon ElastiCache for Redis (o Valkey)",
                    "explanation": "Correcto: ElastiCache for Redis/Valkey admite estructuras de datos complejas, persistencia, replicación con conmutación por error automática Multi-AZ y réplicas de lectura."
                },
                {
                    "id": "B",
                    "text": "Implementar un clúster de almacenamiento en caché en memoria multiproceso Amazon ElastiCache for Memcached.",
                    "explanation": "Incorrecto: Memcached es un almacén de clave-valor puramente en memoria simple que no admite persistencia de datos, replicación ni conmutación por error automática."
                },
                {
                    "id": "C",
                    "text": "Crear una tabla de Amazon DynamoDB configurada en modo de capacidad bajo demanda para tráfico en ráfagas.",
                    "explanation": "Incorrecto: DynamoDB es una base de datos NoSQL persistente, no una capa de caché en memoria para una base de datos relacional RDS existente."
                },
                {
                    "id": "D",
                    "text": "Crear un dominio administrado de Amazon CloudSearch para la indexación de búsqueda de texto de documentos.",
                    "explanation": "Incorrecto: CloudSearch es un motor de búsqueda administrado, no una caché de base de datos en memoria de baja latencia."
                }
            ],
            "generalExplanation": "Amazon ElastiCache for Redis proporciona almacenamiento en caché en memoria compatible con tipos de datos complejos, persistencia, clustering y replicación Multi-AZ con conmutación por error automatizada."
        }
    },
    "saa-q044": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um pipeline de telemetria coleta dados de sensores IoT de 50.000 caminhões de entrega inteligentes, produzindo 10 MB/s de telemetria contínua em formato JSON. Os dados devem ser ingeridos em tempo real, armazenados automaticamente em buffer, transformados no formato Apache Parquet e entregues diretamente em um bucket de data lake no Amazon S3 para análise sem a necessidade de gerenciar clusters de servidores de streaming. Qual serviço atende a esses critérios com o MENOR esforço administrativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Máquina de estados do AWS Step Functions invocada para cada leitura individual do sensor IoT",
                    "explanation": "Incorreto: Invocar o Step Functions para dezenas de milhares de eventos contínuos por segundo resulta em custos excessivos de execução e transições de estado."
                },
                {
                    "id": "B",
                    "text": "Instâncias Amazon EC2 executando Apache Kafka em um Auto Scaling group",
                    "explanation": "Incorreto: O Apache Kafka autogerenciado requer sobrecarga administrativa substancial para gerenciamento de cluster, aplicação de patches e escalabilidade."
                },
                {
                    "id": "C",
                    "text": "Amazon Kinesis Data Firehose (Amazon Data Firehose)",
                    "explanation": "Correto: O Kinesis Data Firehose é um serviço de entrega de streaming totalmente gerenciado e serverless que armazena dados em buffer automaticamente, transforma registros para Parquet e grava no Amazon S3."
                },
                {
                    "id": "D",
                    "text": "Fila Standard do Amazon SQS consultada por um trabalho ETL do AWS Glue em execução a cada 24 horas",
                    "explanation": "Incorreto: A consulta em lote a cada 24 horas não é em tempo real e o SQS tem um limite de tamanho de mensagem de 256 KB."
                }
            ],
            "generalExplanation": "O Amazon Kinesis Data Firehose (Amazon Data Firehose) é a maneira mais simples de capturar, transformar (para Parquet/ORC) e carregar dados de streaming de forma confiável em data lakes como o Amazon S3."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un canal de telemetría recopila datos de sensores IoT de 50.000 camiones de reparto inteligentes que producen 10 MB/s de telemetría continua en formato JSON. Los datos deben ingerirse en tiempo real, almacenarse en búfer automáticamente, transformarse al formato Apache Parquet y entregarse directamente a un bucket de data lake en Amazon S3 para su análisis sin administrar clústeres de servidores de streaming. ¿Qué servicio cumple con estos criterios con el MENOR esfuerzo administrativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Máquina de estado de AWS Step Functions invocada para cada lectura individual de sensor IoT",
                    "explanation": "Incorrecto: Invocar Step Functions para decenas de miles de eventos continuos por segundo genera costes de ejecución y transiciones de estado excesivos."
                },
                {
                    "id": "B",
                    "text": "Instancias Amazon EC2 que ejecutan Apache Kafka en un grupo de Auto Scaling",
                    "explanation": "Incorrecto: Apache Kafka autoadministrado requiere una sobrecarga administrativa sustancial para la gestión de clústeres, parches y escalado."
                },
                {
                    "id": "C",
                    "text": "Amazon Kinesis Data Firehose (Amazon Data Firehose)",
                    "explanation": "Correcto: Kinesis Data Firehose es un servicio de entrega de streaming sin servidor y totalmente administrado que almacena datos en búfer automáticamente, transforma registros a Parquet y los escribe en Amazon S3."
                },
                {
                    "id": "D",
                    "text": "Cola estándar de Amazon SQS sondeada por un trabajo ETL de AWS Glue que se ejecuta cada 24 horas",
                    "explanation": "Incorrecto: El sondeo por lotes de 24 horas no es en tiempo real y SQS tiene un límite de tamaño de mensaje de 256 KB."
                }
            ],
            "generalExplanation": "Amazon Kinesis Data Firehose (Amazon Data Firehose) es la forma más sencilla de capturar, transformar (a Parquet/ORC) y cargar datos de streaming de manera confiable en lagos de datos como Amazon S3."
        }
    },
    "saa-q045": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma equipe de business intelligence precisa executar consultas analíticas SQL ad-hoc em 50 TB de logs CSV armazenados em um bucket de data lake no Amazon S3. Atualmente, as consultas levam vários minutos para serem executadas e geram altos custos de verificação de dados. O arquiteto precisa otimizar o desempenho das consultas e reduzir os custos de varredura de dados no S3 sem gerenciar infraestrutura de banco de dados dedicada. Qual combinação de ações o arquiteto deve recomendar?",
            "options": [
                {
                    "id": "A",
                    "text": "Converter os logs CSV para o formato colunar (como Apache Parquet), particionar os dados no S3 por data e consultar o conjunto de dados usando o Amazon Athena com o AWS Glue Data Catalog.",
                    "explanation": "Correto: Formatos colunares (Parquet) e particionamento por data permitem que o Amazon Athena verifique apenas colunas e partições relevantes, aumentando drasticamente a velocidade da consulta e reduzindo os custos."
                },
                {
                    "id": "B",
                    "text": "Compactar os arquivos CSV com o formato zip e usar o S3 Select para ler arquivos inteiros sequencialmente.",
                    "explanation": "Incorreto: A compactação zip não pode ser dividida em paralelo e o S3 Select não possui agregações relacionais avançadas nem integração com o catálogo Glue."
                },
                {
                    "id": "C",
                    "text": "Habilitar a Replicação Entre Regiões do S3 para duplicar os logs CSV em 5 regiões e consultar todas as regiões simultaneamente.",
                    "explanation": "Incorreto: Duplicar arquivos CSV não particionados multiplica os custos de armazenamento sem resolver a ineficiência da varredura colunar."
                },
                {
                    "id": "D",
                    "text": "Carregar todo o conjunto de dados de 50 TB em uma instância db.t3.medium do Amazon RDS MySQL.",
                    "explanation": "Incorreto: O RDS MySQL não foi projetado para consultas analíticas ad-hoc de 50 TB e uma instância pequena sofreria graves gargalos de desempenho."
                }
            ],
            "generalExplanation": "A conversão de dados para formatos colunares (Parquet/ORC) e o particionamento por campos-chave (ex: Ano/Mês/Dia) permite que o Amazon Athena faça a leitura de significativamente menos dados, acelerando as consultas e reduzindo os custos."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un equipo de business intelligence necesita ejecutar consultas analíticas SQL ad-hoc en 50 TB de registros CSV almacenados en un bucket de data lake en Amazon S3. Actualmente, las consultas tardan varios minutos en ejecutarse e incurren en altos costes de escaneo de datos. El arquitecto necesita optimizar el rendimiento de las consultas y reducir los costes de escaneo de datos de S3 sin administrar una infraestructura de base de datos dedicada. ¿Qué combinación de acciones debería recomendar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Convertir los registros CSV a un formato columnar (como Apache Parquet), particionar los datos en S3 por fecha y consultar el conjunto de datos mediante Amazon Athena con el Catálogo de datos de AWS Glue.",
                    "explanation": "Correcto: Los formatos columnares (Parquet) y el particionamiento por fechas permiten a Amazon Athena escanear solo las columnas y particiones relevantes, lo que acelera radicalmente las consultas y reduce los costes."
                },
                {
                    "id": "B",
                    "text": "Comprimir los archivos CSV con formato zip y usar S3 Select para leer archivos completos secuencialmente.",
                    "explanation": "Incorrecto: La compresión zip no se puede dividir en paralelo y S3 Select carece de agregaciones relacionales avanzadas e integración con el catálogo de Glue."
                },
                {
                    "id": "C",
                    "text": "Habilitar la replicación entre regiones de S3 para duplicar los registros CSV en 5 regiones y consultar todas las regiones simultáneamente.",
                    "explanation": "Incorrecto: Duplicar archivos CSV sin particionar multiplica los costes de almacenamiento sin resolver la ineficiencia del escaneo columnar."
                },
                {
                    "id": "D",
                    "text": "Cargar todo el conjunto de datos de 50 TB en una instancia db.t3.medium de Amazon RDS MySQL.",
                    "explanation": "Incorrecto: RDS MySQL no está diseñado para consultas analíticas ad-hoc de 50 TB y una instancia pequeña sufriría graves cuellos de botella de rendimiento."
                }
            ],
            "generalExplanation": "Convertir datos a formatos columnares (Parquet/ORC) y particionar por campos clave (por ejemplo, Año/Mes/Día) permite a Amazon Athena escanear significativamente menos datos, acelerando las consultas y reduciendo los costes."
        }
    },
    "saa-q046": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma aplicação serverless usa milhares de funções AWS Lambda concorrentes acionadas pelo API Gateway para consultar um banco de dados Amazon RDS Aurora PostgreSQL. Sob picos repentinos de tráfego, o banco de dados falha devido ao esgotamento de conexões (erros de 'too many connections') causado pela rápida abertura e fechamento de conexões de banco de dados por ambientes de execução efêmeros do Lambda. Qual solução resolve esse gargalo?",
            "options": [
                {
                    "id": "A",
                    "text": "Mudar o banco de dados para o Amazon S3 e consultar os dados com o S3 Select.",
                    "explanation": "Incorreto: O S3 é um armazenamento de objetos e não pode substituir um banco de dados relacional transacional OLTP."
                },
                {
                    "id": "B",
                    "text": "Implantar o Amazon RDS Proxy entre as funções AWS Lambda e o banco de dados Aurora.",
                    "explanation": "Correto: O Amazon RDS Proxy mantém um pool de conexões de banco de dados estabelecidas e as compartilha com eficiência entre milhares de invocações concorrentes do Lambda serverless, evitando o esgotamento de conexões."
                },
                {
                    "id": "C",
                    "text": "Aumentar a alocação máxima de memória em todas as funções AWS Lambda para 10 GB.",
                    "explanation": "Incorreto: Aumentar a memória do Lambda aumenta o poder de computação/RAM por função, mas não resolve o pooling de conexões do banco de dados."
                },
                {
                    "id": "D",
                    "text": "Configurar as funções Lambda para serem executadas em sub-redes públicas com endereços IP públicos.",
                    "explanation": "Incorreto: O roteamento de IP público não agrupa conexões de banco de dados e introduz vulnerabilidades de segurança."
                }
            ],
            "generalExplanation": "O Amazon RDS Proxy é um proxy de banco de dados totalmente gerenciado e altamente disponível que agrupa e compartilha conexões estabelecidas com bancos de dados relacionais, tornando as aplicações mais escaláveis e resilientes a picos de conexão."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una aplicación sin servidor utiliza miles de funciones concurrentes de AWS Lambda activadas por API Gateway para consultar una base de datos Amazon RDS Aurora PostgreSQL. Ante picos repentinos de tráfico, la base de datos falla debido al agotamiento de conexiones (errores de 'too many connections') causados por la rápida apertura y cierre de conexiones por parte de los entornos de ejecución efímeros de Lambda. ¿Qué solución resuelve este cuello de botella?",
            "options": [
                {
                    "id": "A",
                    "text": "Cambiar la base de datos a Amazon S3 y consultar datos con S3 Select.",
                    "explanation": "Incorrecto: S3 es almacenamiento de objetos y no puede reemplazar una base de datos relacional transaccional OLTP."
                },
                {
                    "id": "B",
                    "text": "Implementar Amazon RDS Proxy entre las funciones de AWS Lambda y la base de datos Aurora.",
                    "explanation": "Correcto: Amazon RDS Proxy mantiene un grupo de conexiones de base de datos establecidas y las comparte eficientemente entre miles de invocaciones simultáneas de Lambda, evitando el agotamiento de conexiones."
                },
                {
                    "id": "C",
                    "text": "Aumentar la asignación de memoria máxima en todas las funciones de AWS Lambda a 10 GB.",
                    "explanation": "Incorrecto: Aumentar la memoria de Lambda incrementa los recursos de computación/RAM por función, pero no soluciona la gestión de conexiones de base de datos."
                },
                {
                    "id": "D",
                    "text": "Configurar las funciones Lambda para que se ejecuten en subredes públicas con direcciones IP públicas.",
                    "explanation": "Incorrecto: El enrutamiento por IP pública no agrupa conexiones de base de datos e introduce vulnerabilidades de seguridad."
                }
            ],
            "generalExplanation": "Amazon RDS Proxy es un proxy de base de datos altamente disponible y totalmente administrado que agrupa y comparte conexiones establecidas con bases de datos relacionales, haciendo que las aplicaciones sean más escalables y resistentes a picos de conexión."
        }
    },
    "saa-q047": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um serviço de processamento de imagens requer a execução de código Python sempre que uma nova foto é carregada em um bucket do S3. A duração da execução é em média de 3 segundos por imagem, e as solicitações de upload chegam aleatoriamente ao longo do dia, com longos períodos de inatividade total. A empresa precisa de uma arquitetura de computação que dimensione de zero a centenas de execuções simultâneas instantaneamente e tenha custo zero quando nenhuma imagem estiver sendo processada. Qual serviço deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Lambda acionado diretamente por Notificações de Eventos do S3 (S3 Event Notifications)",
                    "explanation": "Correto: O AWS Lambda é serverless, dimensiona automaticamente de zero a milhares de execuções simultâneas em milissegundos e cobra estritamente por milissegundo de tempo de computação utilizado."
                },
                {
                    "id": "B",
                    "text": "Amazon Elastic Container Service (Amazon ECS) com tipo de inicialização EC2",
                    "explanation": "Incorreto: O ECS no EC2 requer o pagamento pelas instâncias EC2 subjacentes 24 horas por dia, 7 dias por semana."
                },
                {
                    "id": "C",
                    "text": "AWS Elastic Beanstalk com ambiente de instância única",
                    "explanation": "Incorreto: A instância única do Elastic Beanstalk é executada continuamente e não é dimensionada para custo zero durante períodos de inatividade."
                },
                {
                    "id": "D",
                    "text": "Instâncias Amazon EC2 em execução em um Auto Scaling group Multi-AZ com tamanho mínimo de 2",
                    "explanation": "Incorreto: Instâncias EC2 geram custos de linha de base 24 horas por dia, 7 dias por semana, mesmo quando ociosas (tamanho mínimo 2), e levam minutos para dimensionar."
                }
            ],
            "generalExplanation": "O AWS Lambda é ideal para tarefas de computação orientadas a eventos, de curta duração e intermitentes, acionadas por eventos do S3, escalando automaticamente a partir do 0 sem custos de ociosidade."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un servicio de procesamiento de imágenes requiere ejecutar código Python cada vez que se sube una nueva foto a un bucket de S3. La duración de la ejecución promedia 3 segundos por imagen, y las solicitudes de carga llegan de manera aleatoria a lo largo del día con largos períodos de inactividad. La empresa requiere una arquitectura de cómputo que escale de cero a cientos de ejecuciones simultáneas al instante y que no genere ningún coste cuando no se procesen imágenes. ¿Qué servicio se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Lambda activado directamente por notificaciones de eventos de S3 (S3 Event Notifications)",
                    "explanation": "Correcto: AWS Lambda es sin servidor, escala automáticamente de cero a miles de ejecuciones simultáneas en milisegundos y factura estrictamente por milisegundo de tiempo de cómputo utilizado."
                },
                {
                    "id": "B",
                    "text": "Amazon Elastic Container Service (Amazon ECS) con tipo de inicio EC2",
                    "explanation": "Incorrecto: ECS en EC2 requiere pagar por las instancias EC2 subyacentes las 24 horas del día, los 7 días de la semana."
                },
                {
                    "id": "C",
                    "text": "AWS Elastic Beanstalk con entorno de instancia única",
                    "explanation": "Incorrecto: Una instancia única de Elastic Beanstalk se ejecuta continuamente y no reduce su coste a cero en periodos de inactividad."
                },
                {
                    "id": "D",
                    "text": "Instancias Amazon EC2 ejecutándose en un grupo de Auto Scaling Multi-AZ con un tamaño mínimo de 2",
                    "explanation": "Incorrecto: Las instancias EC2 incurren en costes base continuos 24/7 incluso inactivas (tamaño mínimo 2) y tardan minutos en escalar."
                }
            ],
            "generalExplanation": "AWS Lambda es ideal para tareas informáticas basadas en eventos, de corta duración e intermitentes, activadas por eventos de S3, escalando automáticamente desde 0 sin costes en reposo."
        }
    },
    "saa-q048": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Um modelo quantitativo financeiro de negociação executado em instâncias Amazon EC2 processa milhões de pequenos objetos de cotação de mercado por segundo. A aplicação requer latência de acesso a dados consistente de milissegundos de dígito único e centenas de milhares de transações por segundo para dados temporários gravados com frequência no S3. Qual classe de armazenamento do Amazon S3 oferece a menor latência de solicitação?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Standard-Infrequent Access (S3 Standard-IA)",
                    "explanation": "Incorreto: O Standard-IA foi projetado para acesso pouco frequente e cobra taxas de recuperação de dados."
                },
                {
                    "id": "B",
                    "text": "Armazenar objetos na classe de armazenamento Amazon S3 Express One Zone para obter latência dedicada de milissegundos de dígito único.",
                    "explanation": "Correto: O S3 Express One Zone é uma classe de armazenamento de zona única e alto desempenho projetada para oferecer acesso consistente a dados em milissegundos de dígito único e velocidades até 10x mais rápidas que o S3 Standard."
                },
                {
                    "id": "C",
                    "text": "Armazenar objetos na classe de armazenamento Amazon S3 Standard com alta durabilidade em 3 Zonas de Disponibilidade.",
                    "explanation": "Incorreto: O S3 Standard oferece latência de milissegundos de dois dígitos em 3 AZs, não desempenho dedicado sub-10ms."
                },
                {
                    "id": "D",
                    "text": "Armazenar objetos na classe de armazenamento Amazon S3 Glacier Instant Retrieval para acesso trimestral de arquivamento.",
                    "explanation": "Incorreto: O Glacier Instant Retrieval destina-se a acesso trimestral a arquivos com tarifas de recuperação por GB."
                }
            ],
            "generalExplanation": "O Amazon S3 Express One Zone foi desenvolvido especificamente para fornecer as velocidades de acesso a dados mais rápidas na nuvem, com latência de milissegundos de dígito único para cargas de trabalho de computação intensiva."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un modelo de negociación cuantitativa financiera que se ejecuta en instancias Amazon EC2 procesa millones de pequeños objetos de ticks de mercado por segundo. La aplicación requiere una latencia de acceso a datos constante de milisegundos de un solo dígito y cientos de miles de transacciones por segundo para datos temporales escritos con frecuencia en S3. ¿Qué clase de almacenamiento de Amazon S3 proporciona la menor latencia de solicitud?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Standard-Infrequent Access (S3 Standard-IA)",
                    "explanation": "Incorrecto: Standard-IA está diseñado para accesos poco frecuentes e incurre en cargos por recuperación de datos."
                },
                {
                    "id": "B",
                    "text": "Almacenar objetos en la clase de almacenamiento Amazon S3 Express One Zone para obtener una latencia dedicada de milisegundos de un solo dígito.",
                    "explanation": "Correcto: S3 Express One Zone es una clase de almacenamiento de alto rendimiento en una sola zona diseñada para ofrecer un acceso consistente a datos en milisegundos de un solo dígito y velocidades hasta 10 veces más rápidas que S3 Standard."
                },
                {
                    "id": "C",
                    "text": "Almacenar objetos en la clase de almacenamiento Amazon S3 Standard con alta durabilidad en 3 Zonas de Disponibilidad.",
                    "explanation": "Incorrecto: S3 Standard ofrece una latencia de dos dígitos de milisegundos en 3 AZs, no un rendimiento dedicado inferior a 10 ms."
                },
                {
                    "id": "D",
                    "text": "Almacenar objetos en la clase de almacenamiento Amazon S3 Glacier Instant Retrieval para acceso trimestral de archivos.",
                    "explanation": "Incorrecto: Glacier Instant Retrieval es para acceso trimestral de archivos con tarifas de recuperación por GB."
                }
            ],
            "generalExplanation": "Amazon S3 Express One Zone está diseñado específicamente para ofrecer las velocidades de acceso a datos más rápidas en la nube con latencia de milisegundos de un solo dígito para cargas de trabajo de cómputo intensivo."
        }
    },
    "saa-q049": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma equipe de análise corporativa executa consultas analíticas SQL complexas em escala de petabytes no Business Intelligence (BI) em dados históricos de vendas com agregações complexas, junções multitabelas (joins) e painéis de relatórios. As consultas devem retornar resultados em segundos para analistas de negócios simultâneos. Qual serviço AWS dedicado é otimizado para essa carga de trabalho de data warehouse?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar um cluster do Amazon DocumentDB para cargas de trabalho de armazenamento de documentos compatíveis com MongoDB.",
                    "explanation": "Incorreto: O DocumentDB é um banco de dados de documentos JSON compatível com MongoDB, não um data warehouse colunar."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster do Amazon OpenSearch Service para análise de logs e indexação de pesquisa de texto completo.",
                    "explanation": "Incorreto: O OpenSearch é otimizado para pesquisa de logs e indexação de texto, não para junções relacionais de data warehouse."
                },
                {
                    "id": "C",
                    "text": "Armazenar dados da aplicação em uma tabela do Amazon DynamoDB com chaves de partição e de classificação.",
                    "explanation": "Incorreto: O DynamoDB é um armazenamento NoSQL de chave-valor/documentos e não é adequado para junções complexas de várias tabelas e agregações SQL."
                },
                {
                    "id": "D",
                    "text": "Implantar um cluster do Amazon Redshift usando armazenamento colunar e processamento massivamente paralelo (MPP).",
                    "explanation": "Correto: O Amazon Redshift é um data warehouse em nuvem rápido e em escala de petabytes que usa armazenamento colunar, processamento massivamente paralelo (MPP) e aprendizado de máquina para fornecer alto desempenho de consulta para BI."
                }
            ],
            "generalExplanation": "O Amazon Redshift usa armazenamento colunar e processamento massivamente paralelo (MPP) para executar consultas SQL analíticas complexas em petabytes de dados estruturados e semiestruturados."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Un equipo de análisis empresarial ejecuta consultas analíticas SQL complejas a escala de petabytes para Business Intelligence (BI) sobre datos históricos de ventas con agregaciones complejas, uniones (joins) de varias tablas y paneles de informes. Las consultas deben devolver resultados en segundos para analistas de negocio simultáneos. ¿Qué servicio de AWS especializado está optimizado para esta carga de trabajo de almacenamiento de datos (data warehouse)?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar un clúster de Amazon DocumentDB para cargas de trabajo de almacenamiento de documentos compatibles con MongoDB.",
                    "explanation": "Incorrecto: DocumentDB es una base de datos de documentos JSON compatible con MongoDB, no un data warehouse columnar."
                },
                {
                    "id": "B",
                    "text": "Implementar un clúster de Amazon OpenSearch Service para análisis de registros e indexación de búsquedas de texto completo.",
                    "explanation": "Incorrecto: OpenSearch está optimizado para búsqueda de registros e indexación de texto, no para uniones de data warehousing relacional."
                },
                {
                    "id": "C",
                    "text": "Almacenar los datos de la aplicación en una tabla de Amazon DynamoDB con claves de partición y de ordenación.",
                    "explanation": "Incorrecto: DynamoDB es un almacén NoSQL de clave-valor/documentos y no es adecuado para uniones multitabla complejas ni agregaciones SQL."
                },
                {
                    "id": "D",
                    "text": "Implementar un clúster de Amazon Redshift utilizando almacenamiento columnar y procesamiento masivamente paralelo (MPP).",
                    "explanation": "Correcto: Amazon Redshift es un data warehouse en la nube rápido a escala de petabytes que utiliza almacenamiento columnar, procesamiento masivamente paralelo (MPP) y aprendizaje automático para ofrecer un alto rendimiento en consultas de BI."
                }
            ],
            "generalExplanation": "Amazon Redshift utiliza almacenamiento columnar y procesamiento masivamente paralelo (MPP) para ejecutar consultas analíticas SQL complejas en petabytes de datos estructurados y semiestructurados."
        }
    },
    "saa-q050": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma empresa de comércio eletrônico está se preparando para a promoção anual da Black Friday. Estima-se que o tráfego aumente em 500% nos primeiros 5 minutos após a meia-noite e permaneça alto por 48 horas. Métricas históricas mostram que as políticas dinâmicas padrão do Auto Scaling reagem muito lentamente para evitar quedas iniciais de tráfego durante o pico abrupto da meia-noite. Quais ações o arquiteto deve combinar para garantir um desempenho contínuo e sem falhas? (Escolha duas.)",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar políticas de dimensionamento com rastreamento de metas (Target Tracking) do Auto Scaling para ajustar a capacidade com base na utilização média de CPU ou contagem de solicitações do ALB por destino durante a promoção.",
                    "explanation": "Correto: As políticas de rastreamento de metas mantêm dinamicamente a capacidade adequada de instâncias para absorver flutuações durante o evento de 48 horas."
                },
                {
                    "id": "B",
                    "text": "Definir o período de espera padrão (cooldown) para 24 horas no Auto Scaling group.",
                    "explanation": "Incorreto: Um cooldown de 24 horas impede que o grupo de Auto Scaling responda a novas alterações de carga durante um dia inteiro."
                },
                {
                    "id": "C",
                    "text": "Desativar o Auto Scaling e iniciar instâncias manualmente uma a uma usando o AWS Management Console durante a promoção.",
                    "explanation": "Incorreto: O dimensionamento manual durante um evento crítico é propenso a erros, lento e não escalável."
                },
                {
                    "id": "D",
                    "text": "Mudar todas as instâncias para instâncias expansíveis (burstable) T3-micro com modo de crédito padrão.",
                    "explanation": "Incorreto: Instâncias expansíveis pequenas esgotarão rapidamente os créditos de CPU e limitarão o desempenho sob carga contínua de 500%."
                },
                {
                    "id": "E",
                    "text": "Criar uma política de dimensionamento programado (Scheduled Scaling) no Auto Scaling para aumentar proativamente a capacidade mínima e desejada do grupo 30 minutos antes da meia-noite.",
                    "explanation": "Correto: O dimensionamento programado provisiona preventivamente a capacidade de computação antes que ocorram picos de tráfego esperados, evitando a latência de inicialização."
                }
            ],
            "generalExplanation": "A combinação de Dimensionamento Programado (para pré-aquecer a capacidade para picos conhecidos) com Dimensionamento de Rastreamento de Metas (para ajustes dinâmicos durante o evento) oferece elasticidade e desempenho ideais."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una empresa de comercio electrónico se está preparando para la venta anual del Black Friday. Se proyecta que el tráfico aumentará un 500% dentro de los 5 minutos posteriores a la medianoche y luego se mantendrá alto durante 48 horas. Las métricas históricas muestran que las políticas dinámicas estándar de Auto Scaling reaccionan con demasiada lentitud para evitar pérdidas iniciales de tráfico durante el repentino pico de medianoche. ¿Qué acciones debe combinar el arquitecto para garantizar un rendimiento óptimo? (Elija dos.)",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar políticas de escalado con seguimiento de objetivos (Target Tracking) de Auto Scaling para ajustar la capacidad en función del uso promedio de CPU o recuento de solicitudes de ALB por destino durante la venta.",
                    "explanation": "Correcto: Las políticas de seguimiento de objetivos mantienen dinámicamente la capacidad de instancias adecuada para absorber las fluctuaciones durante el evento de 48 horas."
                },
                {
                    "id": "B",
                    "text": "Establecer el período de enfriamiento (cooldown) predeterminado en 24 horas en el grupo de Auto Scaling.",
                    "explanation": "Incorrecto: Un enfriamiento de 24 horas evita que el grupo de Auto Scaling responda a cambios adicionales de carga durante un día entero."
                },
                {
                    "id": "C",
                    "text": "Deshabilitar Auto Scaling y lanzar instancias manualmente una por una utilizando la Consola de administración de AWS durante la venta.",
                    "explanation": "Incorrecto: El escalado manual durante un evento crítico es propenso a errores, lento y no escalable."
                },
                {
                    "id": "D",
                    "text": "Cambiar todas las instancias a instancias ampliables (burstable) T3-micro con modo de crédito estándar.",
                    "explanation": "Incorrecto: Las instancias ampliables pequeñas agotarán rápidamente los créditos de CPU y limitarán el rendimiento bajo una carga sostenida del 500%."
                },
                {
                    "id": "E",
                    "text": "Crear una política de escalado programado (Scheduled Scaling) de Auto Scaling para aumentar de forma proactiva la capacidad mínima y deseada del grupo de Auto Scaling 30 minutos antes de la medianoche.",
                    "explanation": "Correcto: El escalado programado amplía preventivamente la capacidad de cómputo antes de que ocurran los picos de tráfico esperados, evitando la latencia de inicio."
                }
            ],
            "generalExplanation": "La combinación de Escalado Programado (para precalentar la capacidad ante picos conocidos) con Escalado por Seguimiento de Objetivos (para adaptarse dinámicamente durante el evento) proporciona elasticidad y rendimiento óptimos."
        }
    },
    "saa-q051": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma plataforma de publicidade online captura bilhões de eventos de clickstream por hora em centenas de jogos para dispositivos móveis. Várias aplicações internas requerem o consumo independente e em tempo real do mesmo fluxo de eventos exato com lógica de processamento personalizada e latência abaixo de um segundo. Os dados do fluxo devem ser retidos por pelo menos 7 dias para permitir a reprodução (replay) em caso de interrupções de consumidores. Qual serviço deve formar o núcleo desse pipeline de ingestão de dados?",
            "options": [
                {
                    "id": "A",
                    "text": "Coordenar a execução do fluxo de trabalho usando máquinas de estado do AWS Step Functions.",
                    "explanation": "Incorreto: O Step Functions é um orquestrador de fluxo de trabalho, não um mecanismo de armazenamento de streaming de alto rendimento."
                },
                {
                    "id": "B",
                    "text": "Amazon Simple Notification Service (Amazon SNS)",
                    "explanation": "Incorreto: O SNS é um serviço de notificação pub/sub do tipo push que não retém dados históricos para reprodução."
                },
                {
                    "id": "C",
                    "text": "Implantar um fluxo do Amazon Kinesis Data Streams para capturar registros de dados ordenados em tempo real.",
                    "explanation": "Correto: O Kinesis Data Streams oferece suporte a múltiplos consumidores simultâneos lendo dos mesmos shards de forma independente, com latência sub-segundo e retenção de dados de até 365 dias para reprodução."
                },
                {
                    "id": "D",
                    "text": "Enviar mensagens para uma fila Standard do Amazon SQS para processamento assíncrono.",
                    "explanation": "Incorreto: As filas do SQS excluem mensagens após o consumo por um único consumidor e não oferecem suporte a múltiplos consumidores paralelos lendo a mesma mensagem de forma independente."
                }
            ],
            "generalExplanation": "O Amazon Kinesis Data Streams foi projetado para streaming contínuo de dados, oferecendo suporte a múltiplas aplicações independentes que leem simultaneamente com retenção de dados configurável para reprodução do fluxo."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una plataforma de publicidad online captura miles de millones de eventos de secuencias de clics (clickstream) por hora en cientos de juegos móviles. Múltiples aplicaciones internas requieren el consumo independiente y en tiempo real del mismo flujo de eventos con lógica de procesamiento personalizada y latencia inferior a un segundo. Los datos del flujo deben conservarse durante al menos 7 días para permitir su reproducción (replay) en caso de caídas de los consumidores. ¿Qué servicio debería constituir el núcleo de este canal de ingesta de datos?",
            "options": [
                {
                    "id": "A",
                    "text": "Coordinar la ejecución del flujo de trabajo utilizando máquinas de estado de AWS Step Functions.",
                    "explanation": "Incorrecto: Step Functions es un orquestador de flujos de trabajo, no un motor de almacenamiento de streaming de alto rendimiento."
                },
                {
                    "id": "B",
                    "text": "Amazon Simple Notification Service (Amazon SNS)",
                    "explanation": "Incorrecto: SNS es un servicio de notificación push de tipo publicación/suscripción que no retiene datos históricos para su reproducción."
                },
                {
                    "id": "C",
                    "text": "Implementar un flujo de Amazon Kinesis Data Streams para capturar registros de datos ordenados en tiempo real.",
                    "explanation": "Correcto: Kinesis Data Streams admite múltiples consumidores simultáneos que leen de los mismos fragmentos (shards) de forma independiente, con latencia de subsegundos y retención de datos de hasta 365 días para reproducción."
                },
                {
                    "id": "D",
                    "text": "Enviar mensajes a una cola estándar de Amazon SQS para procesamiento asíncrono.",
                    "explanation": "Incorrecto: Las colas SQS eliminan los mensajes tras su procesamiento por un único consumidor y no admiten múltiples consumidores paralelos que lean el mismo mensaje de forma independiente."
                }
            ],
            "generalExplanation": "Amazon Kinesis Data Streams está diseñado para la transmisión continua de datos, admitiendo múltiples aplicaciones independientes que leen simultáneamente con retención de datos configurable para la reproducción de flujos."
        }
    },
    "saa-q052": {
        "pt": {
            "domainName": "Domínio 3: Projetar Arquiteturas de Alto Desempenho",
            "statement": "Uma startup SaaS executa microsserviços escritos em Go e Node.js em instâncias Amazon EC2 (arquitetura x86_64). O líder de engenharia deseja otimizar o desempenho da CPU e a eficiência computacional migrando para tipos de instância baseados em AWS Graviton3/Graviton4. O que a equipe de desenvolvimento deve fazer para implantar seu código em instâncias Graviton?",
            "options": [
                {
                    "id": "A",
                    "text": "Recompilar ou reconstruir imagens de contêiner para a arquitetura de CPU ARM64 (aarch64) e iniciar famílias de instâncias baseadas em Graviton (como c7g ou m7g).",
                    "explanation": "Correto: Os processadores AWS Graviton são CPUs personalizadas baseadas em ARM de 64 bits, exigindo que os binários da aplicação e as imagens de contêiner sejam compilados para a arquitetura ARM64."
                },
                {
                    "id": "B",
                    "text": "Converter todo o código Go e Node.js em código Python para o AWS Lambda.",
                    "explanation": "Incorreto: Reescrever bases de código inteiras em Python é desnecessário e contraproducente."
                },
                {
                    "id": "C",
                    "text": "Executar um emulador x86 em instâncias EC2 do Windows Server.",
                    "explanation": "Incorreto: A emulação por software prejudica o desempenho e anula os benefícios de eficiência do Graviton."
                },
                {
                    "id": "D",
                    "text": "Nada; os processadores Graviton executam instruções de máquina x86 nativamente sem recompilação.",
                    "explanation": "Incorreto: O Graviton usa o conjunto de instruções ARM, não o conjunto de instruções x86."
                }
            ],
            "generalExplanation": "Os processadores AWS Graviton usam a arquitetura ARM de 64 bits, proporcionando até 40% melhor relação custo-benefício para cargas de trabalho em contêineres quando criadas para ARM64."
        },
        "es": {
            "domainName": "Dominio 3: Diseñar Arquitecturas de Alto Rendimiento",
            "statement": "Una startup de SaaS ejecuta microservicios escritos en Go y Node.js en instancias Amazon EC2 (arquitectura x86_64). El líder de ingeniería desea optimizar el rendimiento de la CPU y la eficiencia informática migrando a tipos de instancia basados en AWS Graviton3/Graviton4. ¿Qué debe hacer el equipo de desarrollo para desplegar su código en instancias Graviton?",
            "options": [
                {
                    "id": "A",
                    "text": "Recompilar o reconstruir imágenes de contenedor para la arquitectura de CPU ARM64 (aarch64) y lanzar familias de instancias basadas en Graviton (como c7g o m7g).",
                    "explanation": "Correcto: Los procesadores AWS Graviton son CPUs personalizadas basadas en ARM de 64 bits, lo que requiere que los binarios de la aplicación y las imágenes de contenedor se compilen para la arquitectura ARM64."
                },
                {
                    "id": "B",
                    "text": "Convertir todo el código de Go y Node.js en código Python para AWS Lambda.",
                    "explanation": "Incorrecto: Reescribir bases de código enteras en Python es innecesario y contraproducente."
                },
                {
                    "id": "C",
                    "text": "Ejecutar un emulador x86 sobre instancias EC2 de Windows Server.",
                    "explanation": "Incorrecto: La emulación de software degrada el rendimiento y anula las ventajas de eficiencia de Graviton."
                },
                {
                    "id": "D",
                    "text": "Nada; los procesadores Graviton ejecutan instrucciones de máquina x86 de forma nativa sin recompilación.",
                    "explanation": "Incorrecto: Graviton utiliza el conjunto de instrucciones ARM, no el conjunto de instrucciones x86."
                }
            ],
            "generalExplanation": "Los procesadores AWS Graviton utilizan la arquitectura ARM de 64 bits, lo que proporciona hasta un 40% más de relación precio-rendimiento para cargas de trabajo en contenedores compiladas para ARM64."
        }
    },
    "saa-q053": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma plataforma de arquivamento de mídia armazena petabytes de uploads de vídeo de usuários no Amazon S3. Alguns vídeos viralizam e são acessados milhares de vezes ao dia, enquanto outros nunca mais são visualizados após 30 dias. Os padrões de acesso para qualquer vídeo individual são completamente imprevisíveis e não podem ser determinados com antecedência. A empresa deseja minimizar os custos de armazenamento automaticamente sem pagar taxas de recuperação de dados nem arriscar degradação de desempenho quando um vídeo frio for solicitado. Qual classe de armazenamento do S3 deve ser usada?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Standard-Infrequent Access (S3 Standard-IA)",
                    "explanation": "Incorreto: O S3 Standard-IA incorre em taxas de recuperação de dados por GB, o que tornaria os picos de vídeos virais caros."
                },
                {
                    "id": "B",
                    "text": "Armazenar objetos no Amazon S3 One Zone-IA para dados reproduzíveis não críticos.",
                    "explanation": "Incorreto: O One Zone-IA incorre em taxas de recuperação e não protege contra a perda de uma Zona de Disponibilidade."
                },
                {
                    "id": "C",
                    "text": "Armazenar objetos no Amazon S3 Glacier Flexible Archive para arquivamento de conformidade de baixo custo.",
                    "explanation": "Incorreto: O Glacier Flexible Archive exige atrasos de recuperação de minutos a horas, degradando a experiência do usuário para vídeos ativos."
                },
                {
                    "id": "D",
                    "text": "Armazenar objetos no Amazon S3 Intelligent-Tiering para automatizar o escalonamento de custos sem tarifas de recuperação.",
                    "explanation": "Correto: O S3 Intelligent-Tiering move dados automaticamente entre camadas de acesso frequente, pouco frequente e de arquivo com base nos padrões reais de acesso, com zero taxas de recuperação de dados."
                }
            ],
            "generalExplanation": "O Amazon S3 Intelligent-Tiering é a classe de armazenamento ideal para dados com padrões de acesso desconhecidos, mutáveis ou imprevisíveis, proporcionando economia de custos automática sem taxas de recuperação."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una plataforma de archivado multimedia almacena petabytes de videos subidos por usuarios en Amazon S3. Algunos videos se vuelven virales y se accede a ellos miles de veces al día, mientras que otros nunca se vuelven a ver después de 30 días. Los patrones de acceso para cualquier video individual son completamente impredecibles y no se pueden determinar de antemano. La empresa desea minimizar los costes de almacenamiento automáticamente sin pagar tarifas de recuperación de datos ni arriesgar el rendimiento cuando se solicita un video frío. ¿Qué clase de almacenamiento de S3 se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon S3 Standard-Infrequent Access (S3 Standard-IA)",
                    "explanation": "Incorrecto: S3 Standard-IA genera cargos por recuperación de datos por GB, lo que haría que los picos de videos virales fueran costosos."
                },
                {
                    "id": "B",
                    "text": "Almacenar objetos en Amazon S3 One Zone-IA para datos reproducibles no críticos.",
                    "explanation": "Incorrecto: One Zone-IA genera tarifas de recuperación y no protege contra la pérdida de una Zona de Disponibilidad."
                },
                {
                    "id": "C",
                    "text": "Almacenar objetos en Amazon S3 Glacier Flexible Archive para archivado regulatorio de bajo coste.",
                    "explanation": "Incorrecto: Glacier Flexible Archive requiere demoras de recuperación de minutos a horas, degradando la experiencia del usuario para videos activos."
                },
                {
                    "id": "D",
                    "text": "Almacenar objetos en Amazon S3 Intelligent-Tiering para automatizar la asignación por niveles de costes sin cargos de recuperación.",
                    "explanation": "Correcto: S3 Intelligent-Tiering mueve automáticamente los datos entre niveles de acceso frecuente, poco frecuente y de archivo según los patrones de acceso reales, sin cargos por recuperación de datos."
                }
            ],
            "generalExplanation": "Amazon S3 Intelligent-Tiering es la clase de almacenamiento ideal para datos con patrones de acceso desconocidos, cambiantes o impredecibles, que ofrece un ahorro de costes automático sin tarifas de recuperación."
        }
    },
    "saa-q054": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma empresa de bioinformática executa trabalhos noturnos de computação em lote que processam milhares de arquivos de sequências genéticas. Os trabalhos são executados como contêineres Docker sem estado (stateless) retirados de uma fila SQS. Os trabalhos em lote podem ser interrompidos e retomados a qualquer momento e devem ser executados com o menor custo de computação possível. Qual opção de compra do EC2 o arquiteto deve recomendar?",
            "options": [
                {
                    "id": "A",
                    "text": "Provisionar Amazon EC2 Dedicated Hosts para alocar servidores físicos dedicados à sua organização.",
                    "explanation": "Incorreto: Hosts Dedicados são a opção mais cara, destinada a conformidade de hardware dedicado e licenciamento por soquete."
                },
                {
                    "id": "B",
                    "text": "Instâncias Spot em um Auto Scaling group usando estratégia de alocação otimizada para capacidade (capacity-optimized)",
                    "explanation": "Correto: As Instâncias Spot oferecem até 90% de desconto em comparação com os preços On-Demand, tornando-as ideais para cargas de trabalho de processamento em lote tolerantes a falhas e sem estado."
                },
                {
                    "id": "C",
                    "text": "Instâncias Reservadas Padrão com compromisso adiantado de 3 anos",
                    "explanation": "Incorreto: Instâncias Reservadas padrão exigem um compromisso financeiro plurianual e são menos econômicas para trabalhos noturnos flexíveis e interrompíveis do que Instâncias Spot."
                },
                {
                    "id": "D",
                    "text": "Iniciar Instâncias On-Demand do Amazon EC2 cobradas a taxas horárias padrão sem compromisso.",
                    "explanation": "Incorreto: Instâncias On-Demand são cobradas de acordo com tarifas horárias padrão integrais, sem descontos."
                }
            ],
            "generalExplanation": "As instâncias Amazon EC2 Spot permitem que você utilize capacidade sobressalente do EC2 com descontos substanciais de até 90%, sendo perfeitas para cargas de trabalho em lote stateless e tolerantes a falhas."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una empresa de bioinformática ejecuta trabajos nocturnos de procesamiento por lotes que procesan miles de archivos de secuencias genéticas. Los trabajos se ejecutan como contenedores Docker sin estado (stateless) extraídos de una cola SQS. Los trabajos por lotes se pueden interrumpir y reanudar en cualquier momento y deben ejecutarse con el menor coste de cómputo posible. ¿Qué opción de compra de EC2 debería recomendar el arquitecto?",
            "options": [
                {
                    "id": "A",
                    "text": "Aprovisionar Amazon EC2 Dedicated Hosts para asignar servidores físicos dedicados a su organización.",
                    "explanation": "Incorrecto: Los hosts dedicados son la opción más cara, pensada para cumplimiento normativo de hardware dedicado y licencias basadas en sockets."
                },
                {
                    "id": "B",
                    "text": "Instancias Spot en un grupo de Auto Scaling utilizando la estrategia de asignación optimizada para capacidad (capacity-optimized)",
                    "explanation": "Correcto: Las instancias Spot ofrecen hasta un 90% de descuento en comparación con los precios bajo demanda, lo que las hace ideales para cargas de trabajo por lotes sin estado y tolerantes a fallos."
                },
                {
                    "id": "C",
                    "text": "Instancias reservadas estándar con un compromiso inicial de 3 años",
                    "explanation": "Incorrecto: Las instancias reservadas estándar requieren un compromiso financiero plurianual y son menos rentables para trabajos por lotes nocturnos flexibles e interrumpibles que las instancias Spot."
                },
                {
                    "id": "D",
                    "text": "Lanzar instancias bajo demanda de Amazon EC2 facturadas a tarifas estándar por hora sin compromiso.",
                    "explanation": "Incorrecto: Las instancias bajo demanda se facturan a tarifas horarias estándar completas sin descuento."
                }
            ],
            "generalExplanation": "Las instancias Spot de Amazon EC2 le permiten aprovechar la capacidad sobrante de EC2 con grandes descuentos de hasta el 90%, perfectamente adecuadas para cargas de trabajo por lotes sin estado y tolerantes a fallos."
        }
    },
    "saa-q055": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Um escritório de advocacia deve reter registros digitalizados de processos judiciais por 10 anos para cumprir exigências regulatórias. Os registros são acessados frequentemente durante os primeiros 90 dias de litígio, raramente acessados entre o dia 91 e o dia 365 e praticamente nunca acessados após o ano 1 (tempos de recuperação de 12 a 48 horas são aceitáveis após o primeiro ano). Qual é a estratégia de Ciclo de Vida do S3 mais econômica?",
            "options": [
                {
                    "id": "A",
                    "text": "Armazenar objetos no S3 Standard durante todos os 10 anos e habilitar o Versionamento do S3.",
                    "explanation": "Incorreto: Manter petabytes de dados no S3 Standard por 10 anos é extremamente caro em comparação com as camadas de arquivamento."
                },
                {
                    "id": "B",
                    "text": "Armazenar objetos no S3 Glacier Deep Archive imediatamente após a criação no dia 1.",
                    "explanation": "Incorreto: O armazenamento no Deep Archive no dia 1 impede o acesso em tempo real durante os primeiros 90 dias de litígio ativo."
                },
                {
                    "id": "C",
                    "text": "Armazenar objetos em volumes EBS gp3 anexados a uma instância EC2 e criar snapshots anualmente.",
                    "explanation": "Incorreto: O armazenamento em volume EBS é muito mais caro por GB do que o S3 Glacier Deep Archive."
                },
                {
                    "id": "D",
                    "text": "Armazenar objetos no S3 Standard por 90 dias, transicionar para o S3 Standard-IA no dia 91, transicionar para o S3 Glacier Deep Archive no dia 365 e expirar objetos após 3.650 dias (10 anos).",
                    "explanation": "Correto: Essa política de ciclo de vida otimiza custos em todas as fases: S3 Standard para uso ativo, Standard-IA para acesso pouco frequente e Glacier Deep Archive (menor tarifa de armazenamento do S3) para retenção de longo prazo."
                }
            ],
            "generalExplanation": "A combinação de transições entre S3 Standard, S3 Standard-IA e S3 Glacier Deep Archive por meio de regras de ciclo de vida do S3 reduz os custos de armazenamento de longo prazo em mais de 90%, mantendo a disponibilidade necessária."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una firma legal debe conservar los registros escaneados de casos judiciales durante 10 años para cumplir con los mandatos regulatorios. Los registros se consultan con frecuencia durante los primeros 90 días de litigio, rara vez entre el día 91 y el día 365, y prácticamente nunca después del año 1 (los tiempos de recuperación de 12 a 48 horas son aceptables después del año 1). ¿Cuál es la estrategia de ciclo de vida de S3 más rentable?",
            "options": [
                {
                    "id": "A",
                    "text": "Almacenar objetos en S3 Standard durante los 10 años y habilitar el control de versiones de S3.",
                    "explanation": "Incorrecto: Mantener petabytes de datos en S3 Standard durante 10 años es extremadamente costoso en comparación con los niveles de archivado."
                },
                {
                    "id": "B",
                    "text": "Almacenar objetos en S3 Glacier Deep Archive inmediatamente tras su creación en el día 1.",
                    "explanation": "Incorrecto: Almacenar en Deep Archive en el día 1 impide el acceso en tiempo real durante los primeros 90 días de litigio activo."
                },
                {
                    "id": "C",
                    "text": "Almacenar objetos en volúmenes EBS gp3 adjuntos a una instancia EC2 y tomar instantáneas anualmente.",
                    "explanation": "Incorrecto: El almacenamiento en volúmenes EBS es mucho más costoso por GB que S3 Glacier Deep Archive."
                },
                {
                    "id": "D",
                    "text": "Almacenar objetos en S3 Standard durante 90 días, realizar la transición a S3 Standard-IA el día 91, realizar la transición a S3 Glacier Deep Archive el día 365 y caducar los objetos después de 3.650 días (10 años).",
                    "explanation": "Correcto: Esta política de ciclo de vida optimiza los costes en cada fase: S3 Standard para uso activo, Standard-IA para acceso poco frecuente y Glacier Deep Archive (tarifa de almacenamiento de S3 más baja) para retención a largo plazo."
                }
            ],
            "generalExplanation": "La combinación de transiciones entre S3 Standard, S3 Standard-IA y S3 Glacier Deep Archive mediante reglas de ciclo de vida reduce los costes de almacenamiento a largo plazo en más del 90% manteniendo la disponibilidad requerida."
        }
    },
    "saa-q056": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Um pipeline de treinamento de machine learning executado em 50 instâncias EC2 em sub-redes privadas de uma VPC baixa centenas de terabytes de dados de treinamento diariamente de um bucket do Amazon S3 na mesma região. A empresa observa uma fatura mensal extremamente alta referente a taxas de processamento de dados do NAT Gateway. Como o arquiteto pode ELIMINAR os custos de transferência de dados do NAT Gateway para esse tráfego do S3?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantar dois NAT Gateways adicionais em diferentes Zonas de Disponibilidade para balancear a carga da largura de banda.",
                    "explanation": "Incorreto: Adicionar NAT Gateways multiplica as tarifas horárias e de processamento de dados em vez de eliminá-las."
                },
                {
                    "id": "B",
                    "text": "Criar um Amazon S3 Gateway VPC Endpoint e associá-lo às tabelas de rotas das sub-redes privadas.",
                    "explanation": "Correto: Os VPC Endpoints do tipo Gateway para o S3 são totalmente gratuitos, sem taxas de processamento de dados por GB, roteando o tráfego diretamente pela rede interna da AWS sem passar por NAT Gateways."
                },
                {
                    "id": "C",
                    "text": "Criar uma conexão AWS Direct Connect entre a VPC e o Amazon S3.",
                    "explanation": "Incorreto: O Direct Connect serve para conectar data centers on-premises à AWS, não para conectividade intra-VPC com o S3."
                },
                {
                    "id": "D",
                    "text": "Atribuir endereços IPv4 públicos a todas as 50 instâncias EC2 e rotear o tráfego por meio de um Internet Gateway.",
                    "explanation": "Incorreto: Expor instâncias de treinamento com IPs públicos viola os controles de segurança de sub-redes privadas."
                }
            ],
            "generalExplanation": "Os Amazon S3 Gateway VPC Endpoints fornecem roteamento direto e gratuito das sub-redes da VPC para o S3, contornando os NAT Gateways e eliminando completamente as taxas de processamento de dados por GB do NAT."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Un canal de entrenamiento de machine learning que se ejecuta en 50 instancias EC2 en subredes privadas de VPC descarga cientos de terabytes de datos de entrenamiento diariamente desde un bucket de Amazon S3 en la misma región. La empresa nota una factura mensual extremadamente alta por cargos de procesamiento de datos de NAT Gateway. ¿Cómo puede el arquitecto ELIMINAR los costes de transferencia de datos de NAT Gateway para este tráfico hacia S3?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementar dos NAT Gateways adicionales en diferentes Zonas de Disponibilidad para equilibrar la carga del ancho de banda.",
                    "explanation": "Incorrecto: Agregar NAT Gateways multiplica los cargos por hora y procesamiento de datos en lugar de eliminarlos."
                },
                {
                    "id": "B",
                    "text": "Crear un Amazon S3 Gateway VPC Endpoint y asociarlo a las tablas de enrutamiento de las subredes privadas.",
                    "explanation": "Correcto: Los Gateway VPC Endpoints de S3 son completamente gratuitos, sin cargos por procesamiento de datos por GB, y enrutan el tráfico directamente a través de la red interna de AWS sin pasar por NAT Gateways."
                },
                {
                    "id": "C",
                    "text": "Crear una conexión de AWS Direct Connect entre la VPC y Amazon S3.",
                    "explanation": "Incorrecto: Direct Connect es para conectar centros de datos locales (on-premises) a AWS, no para conectividad intra-VPC a S3."
                },
                {
                    "id": "D",
                    "text": "Asignar direcciones IPv4 públicas a las 50 instancias EC2 y enrutar el tráfico a través de una puerta de enlace de Internet (Internet Gateway).",
                    "explanation": "Incorrecto: Exponer instancias de entrenamiento con IPs públicas infringe los controles de seguridad de las subredes privadas."
                }
            ],
            "generalExplanation": "Los endpoints VPC de tipo Gateway para Amazon S3 proporcionan enrutamiento directo y gratuito desde las subredes de la VPC hacia S3, omitiendo los NAT Gateways y eliminando por completo los cargos de procesamiento de datos por GB de NAT."
        }
    },
    "saa-q057": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma grande empresa possui um uso estável de computação de 200 instâncias Linux do EC2 em várias famílias de instâncias (m5, c5, r6g) e Regiões AWS, juntamente com cargas de trabalho crescentes em contêineres no AWS Fargate e funções serverless no AWS Lambda. A empresa deseja fazer um compromisso financeiro de 3 anos para obter a maior economia de custos possível, mantendo a flexibilidade de alternar famílias de instâncias, sistemas operacionais e Regiões AWS. Qual modelo de compromisso eles devem escolher?",
            "options": [
                {
                    "id": "A",
                    "text": "Adquirir EC2 Instance Savings Plans de 3 anos para famílias de instâncias específicas em uma única região.",
                    "explanation": "Incorreto: Os EC2 Instance Savings Plans aplicam-se apenas a uma família de instâncias específica em uma região específica, sem flexibilidade entre famílias, entre regiões e para Fargate/Lambda."
                },
                {
                    "id": "B",
                    "text": "Criar Reservas de Capacidade Sob Demanda (On-Demand Capacity Reservations) para garantir capacidade de computação sem desconto financeiro.",
                    "explanation": "Incorreto: As Capacity Reservations retêm capacidade física, mas não oferecem descontos no faturamento."
                },
                {
                    "id": "C",
                    "text": "Adquirir Compute Savings Plans oferecendo até 66% de desconto com máxima flexibilidade entre regiões e serviços.",
                    "explanation": "Correto: Os Compute Savings Plans oferecem a maior flexibilidade, aplicando descontos de até 66% automaticamente, independentemente da família de instâncias, tamanho, SO, tipo de locação, região ou plataforma de computação (EC2, Fargate, Lambda)."
                },
                {
                    "id": "D",
                    "text": "Adquirir Instâncias Reservadas Padrão de 3 anos vinculadas a tipos de instâncias e plataformas específicas.",
                    "explanation": "Incorreto: As Instâncias Reservadas padrão estão vinculadas a tipos de instância, regiões e plataformas específicas e não se aplicam ao Fargate ou Lambda."
                }
            ],
            "generalExplanation": "Os Compute Savings Plans oferecem economia de custos significativa (até 66%) com flexibilidade máxima, aplicando-se automaticamente a famílias de instâncias do EC2, regiões, SO, Fargate e Lambda."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una empresa tiene un uso base constante de 200 instancias EC2 Linux en múltiples familias de instancias (m5, c5, r6g) y Regiones de AWS, junto con cargas de trabajo de contenedores en crecimiento en AWS Fargate y funciones sin servidor en AWS Lambda. La empresa desea asumir un compromiso financiero de 3 años para lograr el mayor ahorro de costes posible y, al mismo tiempo, conservar la flexibilidad de cambiar de familia de instancias, sistemas operativos y Regiones de AWS. ¿Qué modelo de compromiso deberían elegir?",
            "options": [
                {
                    "id": "A",
                    "text": "Comprar EC2 Instance Savings Plans de 3 años para familias de instancias específicas en una sola región.",
                    "explanation": "Incorrecto: Los EC2 Instance Savings Plans se aplican solo a una familia de instancias específica en una región específica, careciendo de flexibilidad entre familias, entre regiones y para Fargate/Lambda."
                },
                {
                    "id": "B",
                    "text": "Crear reservas de capacidad bajo demanda (On-Demand Capacity Reservations) para garantizar la capacidad informática sin descuento financiero.",
                    "explanation": "Incorrecto: Las reservas de capacidad aseguran capacidad física pero no ofrecen descuentos de facturación."
                },
                {
                    "id": "C",
                    "text": "Comprar Compute Savings Plans que ofrecen hasta un 66% de descuento con la máxima flexibilidad de servicio y entre regiones.",
                    "explanation": "Correcto: Los Compute Savings Plans ofrecen la mayor flexibilidad, aplicando automáticamente descuentos de hasta el 66% independientemente de la familia de instancias, el tamaño, el SO, la tenencia, la región o la plataforma de cómputo (EC2, Fargate, Lambda)."
                },
                {
                    "id": "D",
                    "text": "Comprar instancias reservadas estándar de 3 años vinculadas a tipos de instancias y plataformas específicas.",
                    "explanation": "Incorrecto: Las instancias reservadas estándar están vinculadas a tipos de instancias, regiones y plataformas específicas, y no se aplican a Fargate ni a Lambda."
                }
            ],
            "generalExplanation": "Compute Savings Plans proporciona un ahorro de costes significativo (hasta un 66%) con la máxima flexibilidad, aplicándose automáticamente en familias de instancias de EC2, regiones, SO, Fargate y Lambda."
        }
    },
    "saa-q058": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma startup lança uma nova aplicação de votação social. Durante os primeiros meses, o tráfego é imprevisível, com picos virais esporádicos seguidos por horas de inatividade total. Qual modo de capacidade do Amazon DynamoDB é o MAIS econômico para essa carga de trabalho?",
            "options": [
                {
                    "id": "A",
                    "text": "Modo de Capacidade Provisionada com Capacidade Reservada adquirida para 3 anos",
                    "explanation": "Incorreto: A aquisição de reservas de 3 anos para uma aplicação inicial não comprovada e imprevisível cria um compromisso financeiro desnecessário."
                },
                {
                    "id": "B",
                    "text": "Implantar um cluster Cassandra autogerenciado em instâncias Spot do EC2",
                    "explanation": "Incorreto: Gerenciar clusters NoSQL em instâncias Spot gera uma complexidade administrativa massiva e risco de perda do banco de dados."
                },
                {
                    "id": "C",
                    "text": "Modo de Capacidade Provisionada com alocação estática de 10.000 RCUs e 10.000 WCUs",
                    "explanation": "Incorreto: O superprovisionamento de capacidade estática resulta no pagamento por throughput não utilizado 24 horas por dia, 7 dias por semana, durante horas ociosas."
                },
                {
                    "id": "D",
                    "text": "Configurar a tabela do Amazon DynamoDB no modo de Capacidade Sob Demanda (On-Demand) para pagar por solicitação.",
                    "explanation": "Correto: O modo de capacidade sob demanda do DynamoDB cobra estritamente por solicitação para leituras e gravações executadas, escalando instantaneamente para absorver picos com custo zero durante períodos ociosos."
                }
            ],
            "generalExplanation": "O modo de capacidade sob demanda do Amazon DynamoDB é ideal para cargas de trabalho com padrões de tráfego imprevisíveis ou intermitentes, cobrando apenas pelos recursos consumidos."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una startup lanza una nueva aplicación de encuestas sociales. Durante los primeros meses, el tráfico es impredecible, con picos virales esporádicos seguidos de horas de inactividad total. ¿Qué modo de capacidad de Amazon DynamoDB es el MÁS rentable para esta carga de trabajo?",
            "options": [
                {
                    "id": "A",
                    "text": "Modo de capacidad provisionada con capacidad reservada comprada por 3 años",
                    "explanation": "Incorrecto: Comprar reservas de 3 años para una aplicación de startup no probada e impredecible crea un compromiso financiero innecesario."
                },
                {
                    "id": "B",
                    "text": "Desplegar un clúster Cassandra autoadministrado en instancias Spot de EC2",
                    "explanation": "Incorrecto: La autogestión de clústeres NoSQL en instancias Spot crea una complejidad administrativa masiva y riesgo de pérdida de la base de datos."
                },
                {
                    "id": "C",
                    "text": "Modo de capacidad provisionada con asignación estática de 10.000 RCUs y 10.000 WCUs",
                    "explanation": "Incorrecto: El sobreaprovisionamiento de capacidad estática hace que se pague por rendimiento no utilizado 24/7 durante las horas de inactividad."
                },
                {
                    "id": "D",
                    "text": "Configurar la tabla de Amazon DynamoDB en modo de capacidad bajo demanda (On-Demand) para pagar por solicitud.",
                    "explanation": "Correcto: El modo de capacidad bajo demanda de DynamoDB factura estrictamente por solicitud de lectura y escritura realizada, escalando instantáneamente para absorber picos sin costes durante los períodos de inactividad."
                }
            ],
            "generalExplanation": "El modo de capacidad bajo demanda de Amazon DynamoDB es ideal para cargas de trabajo con patrones de tráfico impredecibles o en ráfagas, cobrando únicamente por los recursos consumidos."
        }
    },
    "saa-q059": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma empresa possui centenas de volumes legados Amazon EBS gp2 anexados a instâncias EC2. O administrador de armazenamento deseja reduzir os custos mensais de armazenamento do EBS em até 20%, ganhando controle independente sobre IOPS e taxa de transferência de linha de base sem provisionar capacidade de armazenamento adicional. Qual ação o administrador deve tomar?",
            "options": [
                {
                    "id": "A",
                    "text": "Criar matrizes RAID 0 usando volumes Cold HDD (sc1).",
                    "explanation": "Incorreto: Volumes Cold HDD não podem servir como volumes raiz inicializáveis e oferecem baixo desempenho de E/S aleatória."
                },
                {
                    "id": "B",
                    "text": "Migrar os volumes EBS gp2 para volumes gp3 usando o Amazon EBS Elastic Volumes.",
                    "explanation": "Correto: Os volumes gp3 são até 20% mais baratos por GB do que o gp2, incluem uma linha de base gratuita de 3.000 IOPS e 125 MB/s e permitem o dimensionamento independente de IOPS/throughput sem aumentar o tamanho do volume."
                },
                {
                    "id": "C",
                    "text": "Tirar snapshots diários e excluir os volumes EBS ativos sempre que as instâncias forem interrompidas.",
                    "explanation": "Incorreto: Excluir volumes ativos e recriá-los manualmente a partir de snapshots gera uma sobrecarga administrativa extrema."
                },
                {
                    "id": "D",
                    "text": "Migrar os volumes para volumes SSD com IOPS Provisionadas (io2).",
                    "explanation": "Incorreto: Volumes io2 são significativamente mais caros do que gp2/gp3 e são destinados a desempenho extremo de banco de dados, não à redução de custos."
                }
            ],
            "generalExplanation": "A migração de volumes gp2 para gp3 proporciona até 20% de economia de custo por GB com provisionamento independente de IOPS e taxa de transferência sem tempo de inatividade via Elastic Volumes."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una empresa tiene cientos de volúmenes heredados de Amazon EBS gp2 asociados a instancias EC2. El administrador de almacenamiento desea reducir los costes mensuales de almacenamiento de EBS hasta en un 20% al tiempo que obtiene un control independiente sobre las IOPS base y el rendimiento sin aprovisionar capacidad de almacenamiento adicional. ¿Qué acción debe tomar el administrador?",
            "options": [
                {
                    "id": "A",
                    "text": "Crear matrices RAID 0 utilizando volúmenes Cold HDD (sc1).",
                    "explanation": "Incorrecto: Los volúmenes Cold HDD no pueden funcionar como volúmenes raíz de arranque y ofrecen un rendimiento deficiente de E/S aleatoria."
                },
                {
                    "id": "B",
                    "text": "Migrar los volúmenes EBS gp2 a volúmenes gp3 utilizando Amazon EBS Elastic Volumes.",
                    "explanation": "Correcto: Los volúmenes gp3 son hasta un 20% más baratos por GB que gp2, incluyen una línea base gratuita de 3.000 IOPS y 125 MB/s, y permiten escalar independientemente las IOPS y el rendimiento sin aumentar el tamaño del volumen."
                },
                {
                    "id": "C",
                    "text": "Tomar instantáneas diarias y eliminar los volúmenes EBS activos cada vez que se detengan las instancias.",
                    "explanation": "Incorrecto: Eliminar volúmenes activos y recrearlos manualmente a partir de instantáneas genera una sobrecarga administrativa extrema."
                },
                {
                    "id": "D",
                    "text": "Migrar los volúmenes a volúmenes SSD de IOPS provisionadas (io2).",
                    "explanation": "Incorrecto: Los volúmenes io2 son significativamente más caros que gp2/gp3 y están destinados a un rendimiento de base de datos extremo, no a la reducción de costes."
                }
            ],
            "generalExplanation": "Migrar de volúmenes gp2 a gp3 ofrece hasta un 20% de ahorro de costes por GB con aprovisionamiento independiente de IOPS y rendimiento sin tiempo de inactividad a través de Elastic Volumes."
        }
    },
    "saa-q060": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma equipe de desenvolvimento de software usa um sistema de arquivos Amazon EFS para armazenar artefatos de compilação compartilhados e repositórios de código. Com o tempo, os custos de armazenamento aumentaram à medida que logs e arquivos de compilação mais antigos raramente são acessados. Como o arquiteto pode reduzir os custos de armazenamento do EFS em até 90% para arquivos não acessados nos últimos 30 dias sem modificar os fluxos de trabalho de acesso dos desenvolvedores?",
            "options": [
                {
                    "id": "A",
                    "text": "Montar o sistema de arquivos EFS em uma instância EC2 com compactação gzip habilitada na camada do sistema operacional.",
                    "explanation": "Incorreto: A compactação manual no nível do sistema operacional cria sobrecarga de CPU e conflitos de bloqueio de arquivos em sistemas de arquivos compartilhados."
                },
                {
                    "id": "B",
                    "text": "Habilitar o Gerenciamento de Ciclo de Vida do Amazon EFS (EFS Lifecycle Management) para transicionar automaticamente arquivos não acessados por 30 dias para a camada de armazenamento EFS Infrequent Access (EFS IA) ou Archive.",
                    "explanation": "Correto: O EFS Lifecycle Management move de forma transparente arquivos inativos para a camada de menor custo EFS Infrequent Access (IA), reduzindo os custos de armazenamento em até 92% sem qualquer alteração no fluxo de trabalho."
                },
                {
                    "id": "C",
                    "text": "Escrever um script cron semanal para copiar arquivos antigos para um volume Amazon EBS sc1.",
                    "explanation": "Incorreto: Scripts personalizados adicionam sobrecarga operacional e volumes EBS não podem ser compartilhados simultaneamente entre várias instâncias em diferentes AZs como o EFS."
                },
                {
                    "id": "D",
                    "text": "Recriar o sistema de arquivos EFS no modo One Zone sem backup.",
                    "explanation": "Incorreto: Recriar o sistema de arquivos perde a resiliência Multi-AZ e não implementa a definição de preços por níveis automatizada baseada na idade do arquivo."
                }
            ],
            "generalExplanation": "O Amazon EFS Lifecycle Management move automaticamente arquivos que não foram acessados durante um período configurado (como 30 dias) para a camada de armazenamento econômica EFS Infrequent Access (IA)."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Un equipo de desarrollo de software utiliza un sistema de archivos Amazon EFS para almacenar artefactos de compilación compartidos y repositorios de código. Con el tiempo, los costes de almacenamiento han aumentado debido a que rara vez se accede a los registros y archivos de compilación antiguos. ¿Cómo puede el arquitecto reducir los costes de almacenamiento de EFS hasta en un 90% para los archivos a los que no se ha accedido en los últimos 30 días sin modificar los flujos de trabajo de acceso de los desarrolladores?",
            "options": [
                {
                    "id": "A",
                    "text": "Montar el sistema de archivos EFS en una instancia EC2 con compresión gzip habilitada en la capa del sistema operativo.",
                    "explanation": "Incorrecto: La compresión manual a nivel de SO crea sobrecarga de CPU y conflictos de bloqueo de archivos en sistemas de archivos compartidos."
                },
                {
                    "id": "B",
                    "text": "Habilitar Amazon EFS Lifecycle Management para realizar automáticamente la transición de los archivos a los que no se haya accedido durante 30 días al nivel de almacenamiento EFS Infrequent Access (EFS IA) o Archive.",
                    "explanation": "Correcto: EFS Lifecycle Management traslada de manera transparente los archivos inactivos al nivel de menor coste EFS Infrequent Access (IA), reduciendo los costes de almacenamiento hasta en un 92% sin cambios en el flujo de trabajo."
                },
                {
                    "id": "C",
                    "text": "Escribir un script cron semanal para copiar archivos antiguos a un volumen Amazon EBS sc1.",
                    "explanation": "Incorrecto: Los scripts personalizados agregan sobrecarga operativa y los volúmenes EBS no se pueden compartir simultáneamente entre múltiples instancias en diferentes AZs como EFS."
                },
                {
                    "id": "D",
                    "text": "Recrear el sistema de archivos EFS en modo One Zone sin copia de seguridad.",
                    "explanation": "Incorrecto: Recrear el sistema de archivos pierde la resiliencia Multi-AZ y no implementa precios por niveles automáticos basados en la antigüedad de los archivos."
                }
            ],
            "generalExplanation": "Amazon EFS Lifecycle Management traslada automáticamente los archivos a los que no se ha accedido durante una duración configurada (como 30 días) al nivel de almacenamiento de coste optimizado EFS Infrequent Access (IA)."
        }
    },
    "saa-q061": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Um site global de notícias entrega 50 TB de imagens estáticas diretamente de um bucket do Amazon S3 para usuários da internet em todo o mundo a cada mês. A fatura mensal mostra cobranças elevadas de Transferência de Dados de Saída (Data Transfer Out - DTO) do Amazon S3 para a internet. Qual mudança arquitetônica reduzirá os custos de saída de transferência de dados e melhorará a latência de download para leitores internacionais?",
            "options": [
                {
                    "id": "A",
                    "text": "Converter o bucket do S3 em um bucket do Amazon S3 Glacier Deep Archive.",
                    "explanation": "Incorreto: O Glacier Deep Archive não pode fornecer imagens de sites em tempo real diretamente para navegadores da internet."
                },
                {
                    "id": "B",
                    "text": "Habilitar a Replicação Entre Regiões do S3 para copiar todas as imagens para 10 regiões adicionais da AWS.",
                    "explanation": "Incorreto: A replicação entre regiões incorre em taxas de transferência de dados inter-regionais e multiplica por 10 os custos contínuos de armazenamento."
                },
                {
                    "id": "C",
                    "text": "Implantar uma distribuição do Amazon CloudFront na frente do bucket de origem do Amazon S3.",
                    "explanation": "Correto: O CloudFront armazena em cache ativos estáticos em locais de borda globais, reduzindo significativamente o tráfego de saída do S3 e oferecendo preços com desconto na transferência de dados de saída em comparação com a saída direta do S3 para a internet."
                },
                {
                    "id": "D",
                    "text": "Configurar uma AWS Site-to-Site VPN para todos os visitantes do site.",
                    "explanation": "Incorreto: A VPN Site-to-Site destina-se a redes corporativas, não a visitantes públicos de sites na internet."
                }
            ],
            "generalExplanation": "Distribuir conteúdo por meio do Amazon CloudFront reduz a latência por meio de cache de borda e reduz os custos de transferência de dados para fora em comparação com o fornecimento direto do tráfego a partir do Amazon S3."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Un sitio web global de noticias sirve 50 TB de recursos de imágenes estáticas directamente desde un bucket de Amazon S3 a usuarios de Internet de todo el mundo cada mes. La factura mensual muestra cargos elevados por transferencia de datos salientes (DTO) de Amazon S3 a Internet. ¿Qué cambio arquitectónico reducirá los costes de transferencia de datos salientes al tiempo que mejorará la latencia de descarga para los lectores internacionales?",
            "options": [
                {
                    "id": "A",
                    "text": "Convertir el bucket de S3 en un bucket de Amazon S3 Glacier Deep Archive.",
                    "explanation": "Incorrecto: Glacier Deep Archive no puede servir imágenes de sitios web en tiempo real directamente a los navegadores de Internet."
                },
                {
                    "id": "B",
                    "text": "Habilitar la replicación entre regiones de S3 para copiar todas las imágenes a 10 regiones de AWS adicionales.",
                    "explanation": "Incorrecto: La replicación entre regiones incurre en tarifas de transferencia de datos entre regiones y multiplica por 10 los costes de almacenamiento continuos."
                },
                {
                    "id": "C",
                    "text": "Implementar una distribución de Amazon CloudFront delante del bucket de origen de Amazon S3.",
                    "explanation": "Correcto: CloudFront almacena en caché activos estáticos en ubicaciones perimetrales globales, reduciendo significativamente el tráfico de salida de S3 y ofreciendo precios reducidos de transferencia de datos en comparación con la salida directa de S3 a Internet."
                },
                {
                    "id": "D",
                    "text": "Configurar una VPN de sitio a sitio de AWS (AWS Site-to-Site VPN) para todos los visitantes del sitio web.",
                    "explanation": "Incorrecto: La VPN de sitio a sitio es para redes corporativas, no para visitantes de sitios web públicos en Internet."
                }
            ],
            "generalExplanation": "Distribuir contenido a través de Amazon CloudFront reduce la latencia mediante el almacenamiento en caché perimetral y reduce los costes de transferencia de datos salientes en comparación con el servicio directo desde Amazon S3."
        }
    },
    "saa-q062": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma empresa de desenvolvimento de software executa ambientes de banco de dados de teste e homologação no Amazon Aurora PostgreSQL. Esses bancos de dados de desenvolvimento são muito utilizados durante o horário comercial (das 9h às 18h em dias úteis), mas ficam completamente ociosos nas noites e fins de semana. A empresa deseja otimizar os custos de banco de dados automaticamente sem precisar desligar e recriar bancos de dados todos os dias. Qual solução é a MAIS econômica?",
            "options": [
                {
                    "id": "A",
                    "text": "Converter os bancos de dados Aurora em implantações Amazon RDS Multi-AZ com IOPS provisionadas.",
                    "explanation": "Incorreto: O Multi-AZ com IOPS provisionadas aumenta os custos para ambientes de não produção."
                },
                {
                    "id": "B",
                    "text": "Migrar os bancos de dados de desenvolvimento para o Amazon Aurora Serverless v2 e configurar uma capacidade mínima de 0,5 ACUs.",
                    "explanation": "Correto: O Aurora Serverless v2 dimensiona a capacidade de computação do banco de dados (ACUs) para cima e para baixo dinamicamente em incrementos detalhados com base na carga em tempo real, reduzindo para a capacidade mínima quando ocioso."
                },
                {
                    "id": "C",
                    "text": "Adquirir Instâncias Reservadas com Pagamento Integral Adiantado de 3 anos para os bancos de dados de homologação.",
                    "explanation": "Incorreto: Instâncias Reservadas cobram continuamente pela capacidade 24 horas por dia, 7 dias por semana durante 3 anos, desperdiçando dinheiro durante noites e fins de semana ociosos."
                },
                {
                    "id": "D",
                    "text": "Tirar snapshots manuais e encerrar os clusters de banco de dados todas as sextas-feiras à noite, restaurando-os nas manhãs de segunda-feira.",
                    "explanation": "Incorreto: A criação e restauração manual geram alta sobrecarga operacional e risco de erro humano."
                }
            ],
            "generalExplanation": "O Amazon Aurora Serverless v2 dimensiona instantaneamente a capacidade do banco de dados para cima e para baixo com base na demanda da aplicação, otimizando os custos durante horários de pico e ociosidade."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una empresa de desarrollo de software ejecuta entornos de bases de datos de prueba y preproducción (staging) en Amazon Aurora PostgreSQL. Estas bases de datos de desarrollo se utilizan intensamente durante el horario laboral (de 9:00 a 18:00 de lunes a viernes), pero permanecen completamente inactivas las noches entre semana y los fines de semana. La empresa desea optimizar los costes de base de datos automáticamente sin necesidad de apagar y recrear las bases de datos todos los días. ¿Qué solución es la más rentable?",
            "options": [
                {
                    "id": "A",
                    "text": "Convertir las bases de datos Aurora en implementaciones Amazon RDS Multi-AZ con IOPS provisionadas.",
                    "explanation": "Incorrecto: Multi-AZ con IOPS provisionadas aumenta los costes para entornos que no son de producción."
                },
                {
                    "id": "B",
                    "text": "Migrar las bases de datos de desarrollo a Amazon Aurora Serverless v2 y configurar una capacidad mínima de 0,5 ACUs.",
                    "explanation": "Correcto: Aurora Serverless v2 escala la capacidad de cómputo de la base de datos (ACUs) dinámicamente en incrementos precisos según la carga en tiempo real, reduciendo a la capacidad mínima cuando está inactiva."
                },
                {
                    "id": "C",
                    "text": "Comprar instancias reservadas con pago total por adelantado de 3 años para las bases de datos de preproducción.",
                    "explanation": "Incorrecto: Las instancias reservadas facturan continuamente capacidad 24/7 durante 3 años, desperdiciando dinero en noches y fines de semana inactivos."
                },
                {
                    "id": "D",
                    "text": "Tomar instantáneas manuales y terminar los clústeres de bases de datos todos los viernes por la noche, restaurándolos los lunes por la mañana.",
                    "explanation": "Incorrecto: La creación y restauración manual genera una alta sobrecarga operativa y riesgo de error humano."
                }
            ],
            "generalExplanation": "Amazon Aurora Serverless v2 escala instantáneamente la capacidad de la base de datos hacia arriba o hacia abajo en función de la demanda de la aplicación, optimizando los costes durante las horas de menor actividad e inactividad."
        }
    },
    "saa-q063": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma plataforma de edição de fotos permite que os usuários enviem grandes arquivos RAW de câmeras usando uploads em partes (multipart uploads). Ao longo do tempo, a análise de armazenamento revela que milhões de partes de uploads multipart abandonadas e incompletas estão consumindo centenas de terabytes de capacidade de armazenamento S3 Standard e gerando cobranças indesejadas. Como o arquiteto pode automatizar a limpeza dessas partes de upload órfãs?",
            "options": [
                {
                    "id": "A",
                    "text": "Desativar uploads em partes (multipart uploads) no bucket do S3.",
                    "explanation": "Incorreto: Uploads de fotos RAW grandes exigem multipart uploads para serem enviados de forma confiável por HTTP."
                },
                {
                    "id": "B",
                    "text": "Configurar uma regra de Ciclo de Vida do S3 com a ação de abortar uploads em partes incompletos após um número especificado de dias (por exemplo, 7 dias).",
                    "explanation": "Correto: As regras de Ciclo de Vida do S3 incluem uma ação dedicada (AbortIncompleteMultipartUpload) que limpa automaticamente as partes de upload não finalizadas após um número definido de dias."
                },
                {
                    "id": "C",
                    "text": "Habilitar o S3 Object Lock no Modo Governança no bucket.",
                    "explanation": "Incorreto: O S3 Object Lock impede exclusões para conformidade WORM, o que é o oposto de excluir partes órfãs."
                },
                {
                    "id": "D",
                    "text": "Escrever uma função diária do AWS Lambda para listar todos os objetos e excluir versões sem tags completas.",
                    "explanation": "Incorreto: Scripts Lambda personalizados exigem extensas chamadas de API e custam mais do que o gerenciamento declarativo nativo de Ciclo de Vida do S3."
                }
            ],
            "generalExplanation": "A configuração de uma regra de Ciclo de Vida do S3 para abortar uploads em partes incompletos remove automaticamente partes órfãs que nunca foram finalizadas, evitando cobranças contínuas de armazenamento."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una plataforma de edición de fotos permite a los usuarios cargar archivos RAW grandes de cámaras mediante cargas multipart (multipart uploads). Con el tiempo, el análisis de almacenamiento revela que millones de partes de carga multipart incompletas y abandonadas consumen cientos de terabytes de almacenamiento S3 Standard y generan costes innecesarios. ¿Cómo puede el arquitecto automatizar la limpieza de estas partes de carga huérfanas?",
            "options": [
                {
                    "id": "A",
                    "text": "Deshabilitar las cargas multipart en el bucket de S3.",
                    "explanation": "Incorrecto: Las fotos RAW grandes requieren multipart uploads para cargarse de forma confiable a través de HTTP."
                },
                {
                    "id": "B",
                    "text": "Configurar una regla de ciclo de vida de S3 con la acción de anular cargas multipart incompletas después de un número específico de días (por ejemplo, 7 días).",
                    "explanation": "Correcto: Las reglas de ciclo de vida de S3 incluyen una acción dedicada (AbortIncompleteMultipartUpload) que elimina automáticamente las partes de carga no finalizadas después de una cantidad establecida de días."
                },
                {
                    "id": "C",
                    "text": "Habilitar S3 Object Lock en modo de gobernanza en el bucket.",
                    "explanation": "Incorrecto: S3 Object Lock evita eliminaciones para cumplimiento normativo WORM, lo cual es lo opuesto a eliminar partes huérfanas."
                },
                {
                    "id": "D",
                    "text": "Escribir una función diaria de AWS Lambda para listar todos los objetos y eliminar versiones sin etiquetas completas.",
                    "explanation": "Incorrecto: Los scripts personalizados de Lambda requieren llamadas continuas a la API y cuestan más que la gestión nativa y declarativa del ciclo de vida de S3."
                }
            ],
            "generalExplanation": "Establecer una regla de ciclo de vida de S3 para cancelar cargas multipart incompletas elimina automáticamente las partes huérfanas que nunca se completaron, evitando costes continuos de almacenamiento."
        }
    },
    "saa-q064": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma empresa possui duas VPCs (VPC A e VPC B) na mesma Região AWS que precisam trocar 10 TB de dados de alto rendimento mensalmente para uma tarefa de análise de dados. A equipe de rede deseja conectar essas duas VPCs com o MENOR custo de infraestrutura contínuo possível e sem tarifas horárias recorrentes de anexo. Qual opção de conectividade é a mais econômica?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar um túnel AWS Site-to-Site VPN entre as duas VPCs através da internet.",
                    "explanation": "Incorreto: A VPN Site-to-Site incorre em tarifas horárias de conexão, limites de throughput (1,25 Gbps) e sobrecarga de CPU de criptografia IPsec."
                },
                {
                    "id": "B",
                    "text": "Implantar um AWS Transit Gateway e conectar ambas as VPCs a ele.",
                    "explanation": "Incorreto: O AWS Transit Gateway cobra taxas horárias fixas por anexo de VPC, além de taxas de processamento de dados, tornando-o mais caro para uma conectividade simples entre duas VPCs."
                },
                {
                    "id": "C",
                    "text": "Implantar uma instância EC2 NAT na VPC A e rotear todo o tráfego por meio de interfaces elásticas com IPs públicos.",
                    "explanation": "Incorreto: A execução de instâncias NAT autogerenciadas gera custos de computação e tarifas de transferência de dados de saída para a internet pública."
                },
                {
                    "id": "D",
                    "text": "Estabelecer uma conexão direta de emparelhamento de VPC (VPC Peering) entre a VPC A e a VPC B.",
                    "explanation": "Correto: O VPC Peering NÃO tem tarifas horárias de conexão nem cobranças de endpoint; você paga apenas as tarifas padrão de transferência de dados intra-região entre AZs."
                }
            ],
            "generalExplanation": "O VPC Peering não possui tarifas básicas por hora nem ponto único de falha, tornando-o a solução mais econômica para o tráfego direto entre VPCs na mesma região."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una empresa tiene dos VPCs (VPC A y VPC B) en la misma Región de AWS que necesitan intercambiar 10 TB de datos de alto rendimiento mensualmente para un trabajo de análisis de datos. El equipo de redes desea conectar estas dos VPCs con el MENOR coste de infraestructura continuo posible y sin tarifas de conexión horarias recurrentes. ¿Qué opción de conectividad es la más rentable?",
            "options": [
                {
                    "id": "A",
                    "text": "Configurar un túnel VPN de sitio a sitio de AWS (AWS Site-to-Site VPN) entre las dos VPCs a través de Internet.",
                    "explanation": "Incorrecto: La VPN de sitio a sitio genera cargos por hora de conexión, límites de rendimiento (1,25 Gbps) y sobrecarga de CPU por cifrado IPsec."
                },
                {
                    "id": "B",
                    "text": "Implementar un AWS Transit Gateway y asociar ambas VPCs a él.",
                    "explanation": "Incorrecto: AWS Transit Gateway cobra tarifas horarias fijas por conexión de VPC además de tarifas de procesamiento de datos, lo que lo hace más costoso para una conectividad simple entre dos VPCs."
                },
                {
                    "id": "C",
                    "text": "Implementar una instancia EC2 NAT en la VPC A y enrutar todo el tráfico a través de interfaces elásticas con IP pública.",
                    "explanation": "Incorrecto: Ejecutar instancias NAT autoadministradas genera costes de computación y tarifas de transferencia de datos salientes hacia Internet."
                },
                {
                    "id": "D",
                    "text": "Establecer una conexión directa de interconexión de VPC (VPC Peering) entre la VPC A y la VPC B.",
                    "explanation": "Correcto: VPC Peering NO tiene tarifas horarias de conexión ni cargos por endpoint; solo paga las tarifas estándar de transferencia de datos intra-región entre AZs."
                }
            ],
            "generalExplanation": "VPC Peering no tiene cargos base por hora ni punto único de falla, lo que lo convierte en la solución más rentable para el tráfico directo entre VPCs en la misma región."
        }
    },
    "saa-q065": {
        "pt": {
            "domainName": "Domínio 4: Projetar Arquiteturas Otimizadas para Custos",
            "statement": "Uma agência de desenvolvimento de software executa 100 instâncias EC2 para ambientes de desenvolvimento e homologação que não são de produção. Essas instâncias são usadas pelos engenheiros apenas das 8h às 18h, de segunda a sexta-feira. Executar essas instâncias 24 horas por dia, 7 dias por semana durante noites e fins de semana desperdiça aproximadamente 65% do orçamento mensal do EC2. Como a empresa pode automatizar o cronograma para interromper instâncias às 18h e iniciá-las às 8h em dias úteis com o MENOR esforço administrativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Converter todas as 100 instâncias em Hosts Dedicados de 3 anos com Pagamento Integral Adiantado.",
                    "explanation": "Incorreto: A compra de Hosts Dedicados de 3 anos aumenta o custo total e não resolve o desperdício de recursos ociosos."
                },
                {
                    "id": "B",
                    "text": "Configurar alarmes de faturamento do CloudWatch para enviar e-mails via SNS aos gerentes sempre que o gasto por hora exceder um limite.",
                    "explanation": "Incorreto: Alarmes de faturamento apenas notificam humanos, mas não iniciam nem interrompem instâncias automaticamente."
                },
                {
                    "id": "C",
                    "text": "Implantar a solução AWS Instance Scheduler (ou o AWS Systems Manager Quick Setup Resource Scheduler) com agendamentos automatizados de início e parada configurados para o horário comercial.",
                    "explanation": "Correto: O AWS Instance Scheduler / SSM Quick Setup inicia e para automaticamente instâncias EC2 e RDS em programações personalizadas de horário comercial, economizando mais de 60% nas faturas de computação."
                },
                {
                    "id": "D",
                    "text": "Instruir todos os desenvolvedores a interromper manualmente suas instâncias EC2 ao final de cada dia de trabalho por meio do AWS Management Console.",
                    "explanation": "Incorreto: Processos manuais humanos não são confiáveis e são frequentemente esquecidos."
                }
            ],
            "generalExplanation": "O uso do AWS Instance Scheduler ou do AWS Systems Manager Resource Scheduler interrompe automaticamente as instâncias fora do horário de trabalho, reduzindo os custos de computação em até 65% a 70%."
        },
        "es": {
            "domainName": "Dominio 4: Diseñar Arquitecturas Optimizadas para Costes",
            "statement": "Una agencia de desarrollo de software ejecuta 100 instancias EC2 para entornos de desarrollo y preproducción no destinados a producción. Estas instancias solo son utilizadas por los ingenieros de 8:00 a 18:00 de lunes a viernes. Ejecutar estas instancias las 24 horas del día, los 7 días de la semana, durante las noches y los fines de semana desperdicia aproximadamente el 65% del presupuesto mensual de EC2. ¿Cómo puede la empresa automatizar la programación para detener las instancias a las 18:00 y arrancarlas a las 8:00 en días laborables con el MENOR esfuerzo administrativo?",
            "options": [
                {
                    "id": "A",
                    "text": "Convertir las 100 instancias en Hosts Dedicados de 3 años con pago total por adelantado.",
                    "explanation": "Incorrecto: Comprar Hosts Dedicados de 3 años aumenta el coste total y no soluciona el desperdicio de recursos inactivos."
                },
                {
                    "id": "B",
                    "text": "Configurar alarmas de facturación de CloudWatch para enviar correos electrónicos por SNS a los administradores cada vez que el gasto por hora supere un umbral.",
                    "explanation": "Incorrecto: Las alarmas de facturación notifican a los humanos pero no inician ni detienen instancias automáticamente."
                },
                {
                    "id": "C",
                    "text": "Implementar la solución AWS Instance Scheduler (o AWS Systems Manager Quick Setup Resource Scheduler) con programaciones automatizadas de inicio y parada configuradas para el horario comercial.",
                    "explanation": "Correcto: AWS Instance Scheduler / SSM Quick Setup inicia y detiene automáticamente instancias EC2 y RDS según programaciones personalizadas en horario comercial, ahorrando más del 60% en facturas de cómputo."
                },
                {
                    "id": "D",
                    "text": "Instruir a todos los desarrolladores para que detengan manualmente sus instancias EC2 al final de cada jornada laboral a través de la Consola de administración de AWS.",
                    "explanation": "Incorrecto: Los procesos humanos manuales no son confiables y se olvidan con frecuencia."
                }
            ],
            "generalExplanation": "El uso de AWS Instance Scheduler o AWS Systems Manager Resource Scheduler detiene automáticamente las instancias fuera de las horas laborables, lo que reduce los costes de computación hasta en un 65-70%."
        }
    }
}
