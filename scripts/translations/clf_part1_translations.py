"""
Translations for AWS Certified Cloud Practitioner (CLF-C02) - Part 1 (Questions 1 to 33).
100% natural, fluent Brazilian Portuguese (PT-BR) and Spanish (ES) translations.
Preserves all official AWS service names, technical terms, and option identifiers.
"""

TRANSLATIONS = {
    "clf-q001": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual conceito de computação em nuvem da AWS descreve a capacidade de um sistema adquirir automaticamente recursos de computação conforme a demanda aumenta e liberar recursos conforme a demanda diminui?",
            "options": [
                {
                    "id": "A",
                    "text": "Alta Disponibilidade (High Availability)",
                    "explanation": "Incorreto: A alta disponibilidade garante que os sistemas permaneçam operacionais e acessíveis com tempo de inatividade mínimo em múltiplas Zonas de Disponibilidade (AZs)."
                },
                {
                    "id": "B",
                    "text": "Agilidade (Agility)",
                    "explanation": "Incorreto: A agilidade refere-se à velocidade e à capacidade de resposta organizacional para inovar, experimentar e implantar aplicações rapidamente."
                },
                {
                    "id": "C",
                    "text": "Confiabilidade (Reliability)",
                    "explanation": "Incorreto: A confiabilidade é a capacidade de uma carga de trabalho desempenhar sua função pretendida corretamente e se recuperar de falhas."
                },
                {
                    "id": "D",
                    "text": "Elasticidade (Elasticity)",
                    "explanation": "Correto: A elasticidade é a capacidade de provisionar e desprovisionar recursos de computação automaticamente em tempo real para corresponder às demandas flutuantes de carga de trabalho."
                }
            ],
            "generalExplanation": "A elasticidade permite que as cargas de trabalho dimensionem automaticamente os recursos de computação para mais ou para menos em tempo real para atender à demanda oscilante."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué concepto de computación en la nube de AWS describe la capacidad de un sistema para adquirir automáticamente recursos de computación a medida que aumenta la demanda y liberarlos cuando disminuye?",
            "options": [
                {
                    "id": "A",
                    "text": "Alta disponibilidad (High Availability)",
                    "explanation": "Incorrecto: La alta disponibilidad garantiza que los sistemas permanezcan operativos y accesibles con un tiempo de inactividad mínimo en múltiples Zonas de Disponibilidad (AZ)."
                },
                {
                    "id": "B",
                    "text": "Agilidad (Agility)",
                    "explanation": "Incorrecto: La agilidad se refiere a la velocidad y la capacidad de respuesta organizacional para innovar, experimentar e implementar aplicaciones rápidamente."
                },
                {
                    "id": "C",
                    "text": "Confiabilidad (Reliability)",
                    "explanation": "Incorrecto: La confiabilidad es la capacidad de una carga de trabajo para realizar su función prevista de manera correcta y recuperarse de fallas."
                },
                {
                    "id": "D",
                    "text": "Elasticidad (Elasticity)",
                    "explanation": "Correcto: La elasticidad es la capacidad de aprovisionar y desaprovisionar recursos de computación automáticamente en tiempo real para adaptarse a las demandas fluctuantes de la carga de trabajo."
                }
            ],
            "generalExplanation": "La elasticidad permite que las cargas de trabajo escalen automáticamente los recursos de computación hacia arriba o hacia abajo en tiempo real para adaptarse a la demanda fluctuante."
        }
    },
    "clf-q002": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual benefício financeiro da computação em nuvem descreve a substituição de investimentos fixos iniciais em hardware físico de data center por despesas mensais variáveis com base no uso real?",
            "options": [
                {
                    "id": "A",
                    "text": "Trocar Despesas Operacionais (OpEx) por Despesas de Capital Fixas (CapEx)",
                    "explanation": "Incorreto: Isso é o inverso da economia da nuvem; data centers tradicionais on-premises exigem alto CapEx."
                },
                {
                    "id": "B",
                    "text": "Trocar Despesas de Capital (CapEx) por Despesas Operacionais Variáveis (OpEx)",
                    "explanation": "Correto: A migração para a AWS permite que as organizações troquem despesas de capital (compras iniciais de hardware) por despesas operacionais (preço variável de pagamento conforme o uso)."
                },
                {
                    "id": "C",
                    "text": "Eliminar todas as cobranças de transferência de dados pela internet",
                    "explanation": "Incorreto: O tráfego de saída (egress) pela internet ainda gera custos variáveis padrão de transferência de dados."
                },
                {
                    "id": "D",
                    "text": "Modelos de depreciação de hardware multidecadal com taxa fixa",
                    "explanation": "Incorreto: A depreciação de ativos físicos é um conceito contábil on-premises eliminado nos modelos de pagamento conforme o uso na nuvem."
                }
            ],
            "generalExplanation": "A troca de CapEx por OpEx é um benefício econômico fundamental da computação em nuvem, permitindo que as empresas paguem apenas pelos recursos de computação e armazenamento consumidos."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué beneficio financiero de la computación en la nube describe el reemplazo de inversiones iniciales fijas en hardware físico de centros de datos por gastos mensuales variables basados en el uso real?",
            "options": [
                {
                    "id": "A",
                    "text": "Cambiar Gastos Operativos (OpEx) por Gastos de Capital Fijos (CapEx)",
                    "explanation": "Incorrecto: Este es el inverso de la economía de la nube; los centros de datos locales tradicionales requieren un alto CapEx."
                },
                {
                    "id": "B",
                    "text": "Cambiar Gastos de Capital (CapEx) por Gastos Operativos Variables (OpEx)",
                    "explanation": "Correcto: La migración a AWS permite a las organizaciones cambiar gastos de capital (compras iniciales de hardware) por gastos operativos (precios variables de pago por uso)."
                },
                {
                    "id": "C",
                    "text": "Eliminar todos los cargos por transferencia de datos a través de Internet",
                    "explanation": "Incorrecto: El tráfico de salida hacia Internet todavía genera costos variables estándar por transferencia de datos."
                },
                {
                    "id": "D",
                    "text": "Modelos de depreciación de hardware multidecadales a tasa fija",
                    "explanation": "Incorrecto: La depreciación de activos físicos es un concepto contable on-premises eliminado en los modelos de pago por uso en la nube."
                }
            ],
            "generalExplanation": "Cambiar CapEx por OpEx es un beneficio económico fundamental de la computación en la nube, lo que permite a las empresas pagar solo por los recursos de computación y almacenamiento consumidos."
        }
    },
    "clf-q003": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Uma organização deseja reduzir o tempo necessário para provisionar novos recursos de infraestrutura de TI de semanas para apenas alguns minutos, permitindo que as equipes de desenvolvimento experimentem e inovem com mais rapidez. Qual vantagem da computação em nuvem isso representa?",
            "options": [
                {
                    "id": "A",
                    "text": "Conformidade com a soberania de dados",
                    "explanation": "Incorreto: A soberania de dados refere-se a regulamentações legais que regem os locais de armazenamento de dados."
                },
                {
                    "id": "B",
                    "text": "Velocidade e Agilidade",
                    "explanation": "Correto: A agilidade na nuvem permite que os desenvolvedores instanciem recursos de computação, armazenamento e rede em minutos com poucos cliques ou chamadas de API."
                },
                {
                    "id": "C",
                    "text": "Economias de escala massivas",
                    "explanation": "Incorreto: Economias de escala referem-se a preços mais baixos decorrentes da grande base agregada de clientes da AWS."
                },
                {
                    "id": "D",
                    "text": "Tolerância a falhas",
                    "explanation": "Incorreto: A tolerância a falhas refere-se à resiliência de um sistema contra falhas de componentes sem interrupção do serviço."
                }
            ],
            "generalExplanation": "Em um ambiente de computação em nuvem, novos recursos de TI estão a apenas um clique de distância, o que reduz o tempo para disponibilizar esses recursos aos desenvolvedores de semanas para minutos, aumentando drasticamente a agilidade."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "Una organización desea reducir el tiempo necesario para aprovisionar nuevos recursos de infraestructura de TI de semanas a solo unos minutos, lo que permite a los equipos de desarrollo experimentar e innovar más rápido. ¿Qué ventaja de la computación en la nube representa esto?",
            "options": [
                {
                    "id": "A",
                    "text": "Cumplimiento de soberanía de datos",
                    "explanation": "Incorrecto: La soberanía de datos se refiere a las regulaciones legales que rigen las ubicaciones de almacenamiento de datos."
                },
                {
                    "id": "B",
                    "text": "Velocidad y Agilidad",
                    "explanation": "Correcto: La agilidad en la nube permite a los desarrolladores instanciar recursos de cómputo, almacenamiento y redes en minutos con unos pocos clics o llamadas a la API."
                },
                {
                    "id": "C",
                    "text": "Economías de escala masivas",
                    "explanation": "Incorrecto: Las economías de escala se refieren a precios más bajos derivados de la gran base agregada de clientes de AWS."
                },
                {
                    "id": "D",
                    "text": "Tolerancia a fallos",
                    "explanation": "Incorrecto: La tolerancia a fallos se refiere a la capacidad de un sistema para seguir funcionando ante la falla de componentes sin interrupción del servicio."
                }
            ],
            "generalExplanation": "En un entorno de computación en la nube, los nuevos recursos de TI están a solo un clic de distancia, lo que reduce el tiempo para ponerlos a disposición de los desarrolladores de semanas a minutos, incrementando drásticamente la agilidad."
        }
    },
    "clf-q004": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual pilar do AWS Well-Architected Framework concentra-se na capacidade de uma carga de trabalho desempenhar sua função pretendida de maneira correta e consistente, recuperar-se de interrupções de infraestrutura ou de serviço e adquirir dinamicamente recursos de computação para atender à demanda?",
            "options": [
                {
                    "id": "A",
                    "text": "Eficiência de Performance (Performance Efficiency)",
                    "explanation": "Incorreto: A Eficiência de Performance foca no uso eficiente dos recursos de computação para atender aos requisitos."
                },
                {
                    "id": "B",
                    "text": "Confiabilidade (Reliability)",
                    "explanation": "Correto: O pilar de Confiabilidade engloba a capacidade de um sistema se recuperar de falhas de infraestrutura, mitigar interrupções e escalar dinamicamente para satisfazer a demanda."
                },
                {
                    "id": "C",
                    "text": "Excelência Operacional (Operational Excellence)",
                    "explanation": "Incorreto: A Excelência Operacional foca na execução e no monitoramento de sistemas e na melhoria contínua dos processos."
                },
                {
                    "id": "D",
                    "text": "Otimização de Custos (Cost Optimization)",
                    "explanation": "Incorreto: A Otimização de Custos foca em evitar despesas desnecessárias e entender os gastos."
                }
            ],
            "generalExplanation": "O pilar de Confiabilidade do AWS Well-Architected Framework garante que as cargas de trabalho se recuperem automaticamente de falhas e mantenham a disponibilidade durante interrupções."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué pilar del AWS Well-Architected Framework se centra en la capacidad de una carga de trabajo para realizar su función prevista de manera correcta y consistente, recuperarse de interrupciones de infraestructura o de servicios y adquirir dinámicamente recursos de computación para satisfacer la demanda?",
            "options": [
                {
                    "id": "A",
                    "text": "Eficiencia del rendimiento (Performance Efficiency)",
                    "explanation": "Incorrecto: La Eficiencia del rendimiento se centra en el uso eficiente de los recursos informáticos para cumplir con los requisitos."
                },
                {
                    "id": "B",
                    "text": "Confiabilidad (Reliability)",
                    "explanation": "Correcto: El pilar de Confiabilidad abarca la capacidad de un sistema para recuperarse de fallas de infraestructura, mitigar interrupciones y escalar dinámicamente para satisfacer la demanda."
                },
                {
                    "id": "C",
                    "text": "Excelencia Operacional (Operational Excellence)",
                    "explanation": "Incorrecto: La Excelencia Operacional se centra en ejecutar y monitorear sistemas y en mejorar continuamente los procesos."
                },
                {
                    "id": "D",
                    "text": "Optimización de Costos (Cost Optimization)",
                    "explanation": "Incorrecto: La Optimización de Costos se centra en evitar gastos innecesarios y comprender los patrones de gasto."
                }
            ],
            "generalExplanation": "El pilar de Confiabilidad del AWS Well-Architected Framework garantiza que las cargas de trabajo se recuperen automáticamente de las fallas y mantengan la disponibilidad ante interrupciones."
        }
    },
    "clf-q005": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual pilar do AWS Well-Architected Framework inclui os princípios de design de executar operações como código, fazer alterações frequentes, pequenas e reversíveis, e aprender com todas as falhas operacionais?",
            "options": [
                {
                    "id": "A",
                    "text": "Sustentabilidade (Sustainability)",
                    "explanation": "Incorreto: A Sustentabilidade foca em minimizar o impacto ambiental e a pegada de carbono."
                },
                {
                    "id": "B",
                    "text": "Segurança (Security)",
                    "explanation": "Incorreto: A Segurança foca na proteção de informações, sistemas e ativos por meio de controle de acesso e criptografia."
                },
                {
                    "id": "C",
                    "text": "Otimização de Custos (Cost Optimization)",
                    "explanation": "Incorreto: A Otimização de Custos foca em alinhar a oferta com a demanda para evitar gastos excessivos."
                },
                {
                    "id": "D",
                    "text": "Excelência Operacional (Operational Excellence)",
                    "explanation": "Correto: O pilar de Excelência Operacional concentra-se na execução eficaz de sistemas, na obtenção de insights sobre operações e na melhoria contínua de processos por meio de automação (IaC)."
                }
            ],
            "generalExplanation": "Os princípios de Excelência Operacional incluem realizar operações como código (IaC), anotar documentações, realizar mudanças frequentes, pequenas e reversíveis, e refinar procedimentos operacionais."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué pilar del AWS Well-Architected Framework incluye los principios de diseño de ejecutar operaciones como código, realizar cambios frecuentes, pequeños y reversibles, y aprender de todas las fallas operativas?",
            "options": [
                {
                    "id": "A",
                    "text": "Sostenibilidad (Sustainability)",
                    "explanation": "Incorrecto: La Sostenibilidad se centra en minimizar el impacto ambiental y la huella de carbono."
                },
                {
                    "id": "B",
                    "text": "Seguridad (Security)",
                    "explanation": "Incorrecto: La Seguridad se centra en proteger la información, los sistemas y los activos mediante control de acceso y cifrado."
                },
                {
                    "id": "C",
                    "text": "Optimización de Costos (Cost Optimization)",
                    "explanation": "Incorrecto: La Optimización de Costos se centra en ajustar la oferta a la demanda para evitar gastos excesivos."
                },
                {
                    "id": "D",
                    "text": "Excelencia Operacional (Operational Excellence)",
                    "explanation": "Correcto: El pilar de Excelencia Operacional se centra en ejecutar los sistemas de manera eficaz, obtener visibilidad de las operaciones y mejorar continuamente los procesos mediante la automatización (IaC)."
                }
            ],
            "generalExplanation": "Los principios de Excelencia Operacional incluyen realizar operaciones como código (IaC), anotar la documentación, realizar cambios frecuentes, pequeños y reversibles, y perfeccionar los procedimientos de operaciones."
        }
    },
    "clf-q006": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual pilar do AWS Well-Architected Framework concentra-se em minimizar os impactos ambientais da execução de cargas de trabalho na nuvem por meio da utilização de hardware com eficiência energética e da redução da capacidade ociosa de computação?",
            "options": [
                {
                    "id": "A",
                    "text": "Confiabilidade (Reliability)",
                    "explanation": "Incorreto: A Confiabilidade aborda a resiliência do sistema e a recuperação de falhas."
                },
                {
                    "id": "B",
                    "text": "Otimização de Custos (Cost Optimization)",
                    "explanation": "Incorreto: A Otimização de Custos concentra-se nos gastos financeiros, não na pegada de carbono ecológica."
                },
                {
                    "id": "C",
                    "text": "Sustentabilidade (Sustainability)",
                    "explanation": "Correto: O pilar de Sustentabilidade aborda impactos ambientais, concentrando-se na redução de energia, na eficiência de recursos e na minimização dos recursos totais necessários."
                },
                {
                    "id": "D",
                    "text": "Eficiência de Performance (Performance Efficiency)",
                    "explanation": "Incorreto: A Eficiência de Performance concentra-se na otimização de taxa de transferência (throughput) e latência."
                }
            ],
            "generalExplanation": "O pilar de Sustentabilidade foi adicionado ao AWS Well-Architected Framework para ajudar as organizações a reduzir o impacto ambiental e maximizar a eficiência energética."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué pilar del AWS Well-Architected Framework se centra en minimizar los impactos ambientales de la ejecución de cargas de trabajo en la nube mediante la utilización de hardware energéticamente eficiente y la reducción de la capacidad de cómputo inactiva?",
            "options": [
                {
                    "id": "A",
                    "text": "Confiabilidad (Reliability)",
                    "explanation": "Incorrecto: La Confiabilidad aborda la resiliencia del sistema y la recuperación ante fallos."
                },
                {
                    "id": "B",
                    "text": "Optimización de Costos (Cost Optimization)",
                    "explanation": "Incorrecto: La Optimización de Costos se enfoca en el gasto financiero, no en la huella de carbono ecológica."
                },
                {
                    "id": "C",
                    "text": "Sostenibilidad (Sustainability)",
                    "explanation": "Correcto: El pilar de Sostenibilidad aborda los impactos ambientales, centrándose en la reducción del consumo energético, la eficiencia en el uso de recursos y la minimización de los recursos totales requeridos."
                },
                {
                    "id": "D",
                    "text": "Eficiencia del rendimiento (Performance Efficiency)",
                    "explanation": "Incorrecto: La Eficiencia del rendimiento se centra en la optimización del rendimiento y la latencia."
                }
            ],
            "generalExplanation": "El pilar de Sostenibilidad se agregó al AWS Well-Architected Framework para ayudar a las organizaciones a reducir el impacto ambiental y maximizar la eficiencia energética."
        }
    },
    "clf-q007": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "O AWS Cloud Adoption Framework (AWS CAF) organiza suas orientações em seis perspectivas. Quais das seguintes perspectivas pertencem à categoria técnica do AWS CAF?",
            "options": [
                {
                    "id": "A",
                    "text": "Plataforma, Segurança e Operações (Platform, Security, and Operations)",
                    "explanation": "Correto: Plataforma, Segurança e Operações são as três perspectivas técnicas definidas no AWS Cloud Adoption Framework."
                },
                {
                    "id": "B",
                    "text": "Negócios, Pessoas e Governança (Business, People, and Governance)",
                    "explanation": "Incorreto: Negócios, Pessoas e Governança são as três perspectivas de negócios do AWS CAF."
                },
                {
                    "id": "C",
                    "text": "Computação, Armazenamento e Rede (Compute, Storage, and Networking)",
                    "explanation": "Incorreto: Estes são pilares de infraestrutura, não perspectivas organizacionais do CAF."
                },
                {
                    "id": "D",
                    "text": "Finanças, Marketing e Vendas (Finance, Marketing, and Sales)",
                    "explanation": "Incorreto: Estes são departamentos corporativos gerais, não perspectivas do AWS CAF."
                }
            ],
            "generalExplanation": "O AWS Cloud Adoption Framework (AWS CAF) define seis perspectivas: Negócios, Pessoas e Governança (categoria de Negócios); e Plataforma, Segurança e Operações (categoria Técnica)."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "El AWS Cloud Adoption Framework (AWS CAF) organiza la orientación en seis perspectivas. ¿Cuáles de las siguientes perspectivas pertenecen a la categoría técnica del AWS CAF?",
            "options": [
                {
                    "id": "A",
                    "text": "Plataforma, Seguridad y Operaciones (Platform, Security, and Operations)",
                    "explanation": "Correcto: Plataforma, Seguridad y Operaciones son las tres perspectivas técnicas definidas en el AWS Cloud Adoption Framework."
                },
                {
                    "id": "B",
                    "text": "Negocios, Personas y Gobernanza (Business, People, and Governance)",
                    "explanation": "Incorrecto: Negocios, Personas y Gobernanza son las tres perspectivas de negocio del AWS CAF."
                },
                {
                    "id": "C",
                    "text": "Cómputo, Almacenamiento y Redes (Compute, Storage, and Networking)",
                    "explanation": "Incorrecto: Estos son pilares de infraestructura, no perspectivas organizacionales del CAF."
                },
                {
                    "id": "D",
                    "text": "Finanzas, Marketing y Ventas (Finance, Marketing, and Sales)",
                    "explanation": "Incorrecto: Estos son departamentos corporativos generales, no perspectivas del AWS CAF."
                }
            ],
            "generalExplanation": "El AWS Cloud Adoption Framework (AWS CAF) define seis perspectivas: Negocios, Personas y Gobernanza (categoría de Negocios); y Plataforma, Seguridad y Operaciones (categoría Técnica)."
        }
    },
    "clf-q008": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Uma empresa planeja migrar uma aplicação web on-premises para a AWS movendo máquinas virtuais diretamente para o Amazon EC2 sem modificar o código da aplicação ou a arquitetura principal. Qual estratégia de migração (dos 7 Rs de migração) isso descreve?",
            "options": [
                {
                    "id": "A",
                    "text": "Rehost ('Lift and shift')",
                    "explanation": "Correto: O Rehosting (hospedagem nova ou 'lift and shift') move as aplicações para a AWS no estado em que se encontram, sem qualquer alteração de código ou arquitetura."
                },
                {
                    "id": "B",
                    "text": "Refactor / Re-architect (Refatorar / Rearquitetar)",
                    "explanation": "Incorreto: A refatoração envolve reescrever o código em microsserviços nativos da nuvem ou arquiteturas serverless."
                },
                {
                    "id": "C",
                    "text": "Replatform ('Lift, tinker, and shift')",
                    "explanation": "Incorreto: O Replatforming envolve realizar pequenas otimizações na nuvem (como mudar para um banco de dados gerenciado) sem alterar o código principal."
                },
                {
                    "id": "D",
                    "text": "Repurchase ('Drop and shop')",
                    "explanation": "Incorreto: O Repurchasing significa abandonar o software existente em favor de um produto comercial SaaS."
                }
            ],
            "generalExplanation": "O Rehosting (lift-and-shift) é uma abordagem de migração em que as aplicações são migradas para a nuvem sem modificações no código, frequentemente automatizada usando o AWS Application Migration Service (MGN)."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "Una empresa planea migrar una aplicación web local (on-premises) a AWS trasladando máquinas virtuales directamente a Amazon EC2 sin modificar el código de la aplicación ni la arquitectura principal. ¿Qué estrategia de migración (de las 7 R de migración) describe esto?",
            "options": [
                {
                    "id": "A",
                    "text": "Rehost ('Lift and shift')",
                    "explanation": "Correcto: El Rehosting ('lift and shift') traslada las aplicaciones a AWS tal como están, sin ningún cambio de código ni de arquitectura."
                },
                {
                    "id": "B",
                    "text": "Refactor / Re-architect (Refactorizar / Rediseñar)",
                    "explanation": "Incorrecto: La refactorización implica reescribir el código en microservicios nativos de la nube o arquitecturas serverless."
                },
                {
                    "id": "C",
                    "text": "Replatform ('Lift, tinker, and shift')",
                    "explanation": "Incorrecto: El Replatforming implica realizar optimizaciones menores en la nube (como cambiar a una base de datos administrada) sin modificar el código principal."
                },
                {
                    "id": "D",
                    "text": "Repurchase ('Drop and shop')",
                    "explanation": "Incorrecto: El Repurchasing significa reemplazar el software existente por un producto comercial SaaS."
                }
            ],
            "generalExplanation": "El Rehosting (lift-and-shift) es un enfoque de migración en el que las aplicaciones se trasladan a la nube sin modificaciones en el código, a menudo automatizado mediante AWS Application Migration Service (MGN)."
        }
    },
    "clf-q009": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Por que a AWS pode oferecer preços mais baixos de pagamento conforme o uso aos clientes em comparação com o que organizações individuais conseguiriam obter em seus próprios data centers privados?",
            "options": [
                {
                    "id": "A",
                    "text": "Porque a AWS repassa aos clientes as economias geradas pelas massivas economias de escala agregadas.",
                    "explanation": "Correto: Como o uso de centenas de milhares de clientes é agregado na nuvem, a AWS alcança economias de escala maiores, o que se traduz em preços mais baixos."
                },
                {
                    "id": "B",
                    "text": "Porque a AWS depende exclusivamente de hardware comunitário de código aberto não verificado.",
                    "explanation": "Incorreto: A AWS projeta e utiliza silício corporativo personalizado (Graviton, Nitro) e hardware de nível corporativo."
                },
                {
                    "id": "C",
                    "text": "Porque a AWS cobra dos clientes taxas fixas independentemente do volume de uso.",
                    "explanation": "Incorreto: A AWS utiliza um modelo de preços por consumo baseado no pagamento conforme o uso."
                },
                {
                    "id": "D",
                    "text": "Porque a AWS delega a segurança física dos data centers a voluntários terceirizados.",
                    "explanation": "Incorreto: A AWS gerencia rigorosamente a segurança física dos data centers com controles biométricos e equipe de segurança 24/7."
                }
            ],
            "generalExplanation": "Ao agregar o uso de milhões de clientes, a AWS atinge imensas economias de escala, permitindo reduções regulares de preços nos serviços em nuvem."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Por qué AWS puede ofrecer a los clientes precios de pago por uso más bajos en comparación con lo que las organizaciones individuales podrían lograr en sus propios centros de datos privados?",
            "options": [
                {
                    "id": "A",
                    "text": "Porque AWS traslada a los clientes el ahorro derivado de masivas economías de escala agregadas.",
                    "explanation": "Correcto: Debido a que el uso de cientos de miles de clientes se agrega en la nube, AWS logra mayores economías de escala, lo que se traduce en precios más bajos."
                },
                {
                    "id": "B",
                    "text": "Porque AWS depende exclusivamente de hardware comunitario de código abierto no verificado.",
                    "explanation": "Incorrecto: AWS diseña y utiliza silicio empresarial personalizado (Graviton, Nitro) y hardware de nivel empresarial."
                },
                {
                    "id": "C",
                    "text": "Porque AWS cobra a los clientes tarifas fijas independientemente del volumen de uso.",
                    "explanation": "Incorrecto: AWS utiliza un modelo de precios por consumo de pago por uso."
                },
                {
                    "id": "D",
                    "text": "Porque AWS delega la seguridad física de los centros de datos a voluntarios externos.",
                    "explanation": "Incorrecto: AWS gestiona estrictamente la seguridad física de los centros de datos con controles biométricos y personal de seguridad 24/7."
                }
            ],
            "generalExplanation": "Al agregar el uso de millones de clientes, AWS logra inmensas economías de escala, lo que permite reducciones continuas de precios en los servicios en la nube."
        }
    },
    "clf-q010": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual benefício da computação em nuvem permite que uma organização implante aplicações web para usuários em múltiplos continentes com baixa latência em apenas alguns minutos usando a infraestrutura global da AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Parar de adivinhar a capacidade (Stop guessing capacity)",
                    "explanation": "Incorreto: Isso se refere à elasticidade e ao dimensionamento dinâmico de recursos."
                },
                {
                    "id": "B",
                    "text": "Isolamento de locação única (Single tenancy isolation)",
                    "explanation": "Incorreto: O multi-inquilinato (multi-tenancy) com isolamento lógico é o padrão na infraestrutura em nuvem."
                },
                {
                    "id": "C",
                    "text": "Tornar-se global em minutos (Go global in minutes)",
                    "explanation": "Correto: 'Tornar-se global em minutos' refere-se à capacidade de implantar facilmente aplicações em múltiplas Regiões da AWS e locais de borda em todo o mundo."
                },
                {
                    "id": "D",
                    "text": "Parar de gastar dinheiro na execução e manutenção de data centers",
                    "explanation": "Incorreto: Isso se refere à eliminação do trabalho pesado e indiferenciado de manter instalações de data center."
                }
            ],
            "generalExplanation": "A presença global das Regiões da AWS e dos Pontos de Presença (Edge Locations) permite que as empresas implantem aplicações globalmente com latência mínima em questão de minutos."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué beneficio de la computación en la nube permite a una organización implementar aplicaciones web para usuarios en múltiples continentes con baja latencia en solo unos minutos utilizando la infraestructura global de AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Dejar de adivinar la capacidad (Stop guessing capacity)",
                    "explanation": "Incorrecto: Esto se refiere a la elasticidad y al escalado dinámico de recursos."
                },
                {
                    "id": "B",
                    "text": "Aislamiento de inquilino único (Single tenancy isolation)",
                    "explanation": "Incorrecto: El multi-inquilinato (multi-tenancy) con aislamiento lógico es el estándar en la infraestructura de la nube."
                },
                {
                    "id": "C",
                    "text": "Volverse global en minutos (Go global in minutes)",
                    "explanation": "Correcto: 'Volverse global en minutos' se refiere a la capacidad de implementar fácilmente aplicaciones en múltiples Regiones de AWS y ubicaciones de borde en todo el mundo."
                },
                {
                    "id": "D",
                    "text": "Dejar de gastar dinero en el funcionamiento y mantenimiento de centros de datos",
                    "explanation": "Incorrecto: Esto se refiere a eliminar el trabajo pesado indiferenciado que implica mantener instalaciones de centros de datos."
                }
            ],
            "generalExplanation": "La presencia global de las Regiones de AWS y las ubicaciones de borde (Edge Locations) permite a las empresas implementar aplicaciones a nivel mundial con una latencia mínima en cuestión de minutos."
        }
    },
    "clf-q011": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Uma empresa está migrando um banco de dados on-premises para a AWS. Em vez de gerenciar instalações de banco de dados em instâncias EC2, a equipe decide migrar para o Amazon RDS para descarregar o gerenciamento do sistema operacional do banco de dados e os backups automatizados, mantendo o mesmo mecanismo de banco de dados. Qual estratégia de migração isso representa?",
            "options": [
                {
                    "id": "A",
                    "text": "Retain (Reter)",
                    "explanation": "Incorreto: Reter significa manter a aplicação no data center on-premises."
                },
                {
                    "id": "B",
                    "text": "Replatform ('Lift, tinker, and shift')",
                    "explanation": "Correto: O Replatforming envolve fazer pequenas otimizações na nuvem (como migrar de um banco de dados autogerenciado para um serviço gerenciado como o Amazon RDS) sem reescrever o código principal da aplicação."
                },
                {
                    "id": "C",
                    "text": "Retire (Desativar / Aposentar)",
                    "explanation": "Incorreto: Desativar (Retire) significa desligar uma aplicação que não é mais necessária."
                },
                {
                    "id": "D",
                    "text": "Rehost",
                    "explanation": "Incorreto: O Rehost significaria copiar o banco de dados autogerenciado diretamente para uma máquina virtual do EC2."
                }
            ],
            "generalExplanation": "O Replatforming adota plataformas gerenciadas em nuvem (como o Amazon RDS) para obter eficiências operacionais sem a necessidade de reprojetar a aplicação principal."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "Una empresa está migrando una base de datos local (on-premises) a AWS. En lugar de administrar instalaciones de bases de datos en instancias EC2, el equipo decide migrar a Amazon RDS para delegar la administración del sistema operativo de la base de datos y las copias de seguridad automatizadas, manteniendo el mismo motor de base de datos. ¿Qué estrategia de migración representa esto?",
            "options": [
                {
                    "id": "A",
                    "text": "Retain (Retener)",
                    "explanation": "Incorrecto: Retener significa conservar la aplicación en el centro de datos local (on-premises)."
                },
                {
                    "id": "B",
                    "text": "Replatform ('Lift, tinker, and shift')",
                    "explanation": "Correcto: El Replatforming implica realizar optimizaciones menores en la nube (como migrar de una base de datos autogestionada a un servicio administrado como Amazon RDS) sin reescribir el código principal de la aplicación."
                },
                {
                    "id": "C",
                    "text": "Retire (Retirar / Desactivar)",
                    "explanation": "Incorrecto: Retirar significa dar de baja una aplicación que ya no es necesaria."
                },
                {
                    "id": "D",
                    "text": "Rehost",
                    "explanation": "Incorrecto: El Rehost significaría copiar la base de datos autogestionada directamente en una máquina virtual de EC2."
                }
            ],
            "generalExplanation": "El Replatforming adopta plataformas administradas en la nube (como Amazon RDS) para obtener eficiencias operativas sin rediseñar la aplicación principal."
        }
    },
    "clf-q012": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Uma empresa executa aplicações legadas confidenciais dentro de um data center corporativo on-premises e as conecta com segurança a frontends web escaláveis e data lakes de análise executados na Nuvem AWS. Qual modelo de implantação em nuvem está sendo utilizado?",
            "options": [
                {
                    "id": "A",
                    "text": "Implantação em Nuvem Pública",
                    "explanation": "Incorreto: Uma implantação em nuvem pública pura hospeda todos os componentes na infraestrutura do provedor de nuvem."
                },
                {
                    "id": "B",
                    "text": "Implantação em Nuvem Híbrida",
                    "explanation": "Correto: Uma implantação híbrida conecta a infraestrutura on-premises existente a recursos em nuvem para operar de maneira integrada como uma arquitetura estendida."
                },
                {
                    "id": "C",
                    "text": "Implantação de Software como Serviço (SaaS)",
                    "explanation": "Incorreto: SaaS é um modelo de entrega de software, não um modelo de implantação de infraestrutura híbrida."
                },
                {
                    "id": "D",
                    "text": "Implantação em Nuvem Privada",
                    "explanation": "Incorreto: Uma implantação em nuvem privada reside inteiramente em infraestrutura on-premises ou privada dedicada."
                }
            ],
            "generalExplanation": "Uma arquitetura de Nuvem Híbrida conecta a infraestrutura on-premises aos recursos baseados em nuvem, permitindo o processamento híbrido de dados e migrações em fases."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "Una empresa ejecuta aplicaciones heredadas críticas dentro de un centro de datos corporativo local (on-premises) y las conecta de forma segura a interfaces web escalables y lagos de datos (data lakes) de análisis que se ejecutan en la Nube de AWS. ¿Qué modelo de implementación en la nube se está utilizando?",
            "options": [
                {
                    "id": "A",
                    "text": "Implementación en Nube Pública",
                    "explanation": "Incorrecto: Una implementación en nube pública pura aloja todos los componentes en la infraestructura del proveedor de la nube."
                },
                {
                    "id": "B",
                    "text": "Implementación en Nube Híbrida",
                    "explanation": "Correcto: Una implementación híbrida conecta la infraestructura local existente con recursos en la nube para operar de forma transparente como una arquitectura extendida."
                },
                {
                    "id": "C",
                    "text": "Implementación de Software como Servicio (SaaS)",
                    "explanation": "Incorrecto: SaaS es un modelo de entrega de software, no un modelo de implementación de infraestructura híbrida."
                },
                {
                    "id": "D",
                    "text": "Implementación en Nube Privada",
                    "explanation": "Incorrecto: Una implementación en nube privada reside completamente en infraestructura local o privada dedicada."
                }
            ],
            "generalExplanation": "Una arquitectura de Nube Híbrida une la infraestructura local con recursos basados en la nube, lo que permite el procesamiento híbrido de datos y migraciones por fases."
        }
    },
    "clf-q013": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual pilar do AWS Well-Architected Framework concentra-se no gerenciamento estruturado de identidades, na aplicação do princípio do menor privilégio, na viabilização da rastreabilidade por meio de logs de auditoria e na aplicação de controles de segurança em todas as camadas?",
            "options": [
                {
                    "id": "A",
                    "text": "Otimização de Custos (Cost Optimization)",
                    "explanation": "Incorreto: A Otimização de Custos foca na redução de gastos e na maximização do retorno sobre o investimento (ROI)."
                },
                {
                    "id": "B",
                    "text": "Excelência Operacional (Operational Excellence)",
                    "explanation": "Incorreto: A Excelência Operacional concentra-se na automação de procedimentos operacionais e no aprendizado com falhas."
                },
                {
                    "id": "C",
                    "text": "Segurança (Security)",
                    "explanation": "Correto: O pilar de Segurança concentra-se na proteção de dados, sistemas e ativos, na aplicação do menor privilégio e na implementação de rastreabilidade abrangente."
                },
                {
                    "id": "D",
                    "text": "Confiabilidade (Reliability)",
                    "explanation": "Incorreto: A Confiabilidade concentra-se na recuperação de interrupções de infraestrutura e no teste de recuperação de desastres."
                }
            ],
            "generalExplanation": "O pilar de Segurança abrange os fundamentos de segurança, incluindo gerenciamento de identidades, controles de detecção, proteção de infraestrutura, proteção de dados e resposta a incidentes."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué pilar del AWS Well-Architected Framework se centra en la gestión estructurada de identidades, la aplicación del principio de privilegio mínimo, la habilitación de la trazabilidad mediante registros de auditoría y la aplicación de controles de seguridad en todas las capas?",
            "options": [
                {
                    "id": "A",
                    "text": "Optimización de Costos (Cost Optimization)",
                    "explanation": "Incorrecto: La Optimización de Costos se centra en reducir los gastos y maximizar el retorno de la inversión (ROI)."
                },
                {
                    "id": "B",
                    "text": "Excelencia Operacional (Operational Excellence)",
                    "explanation": "Incorrecto: La Excelencia Operacional se centra en automatizar los procedimientos operativos y aprender de los fallos."
                },
                {
                    "id": "C",
                    "text": "Seguridad (Security)",
                    "explanation": "Correcto: El pilar de Seguridad se centra en proteger datos, sistemas y activos, aplicar el privilegio mínimo e implementar una trazabilidad integral."
                },
                {
                    "id": "D",
                    "text": "Confiabilidad (Reliability)",
                    "explanation": "Incorrecto: La Confiabilidad se centra en recuperarse de interrupciones de infraestructura y probar la recuperación ante desastres."
                }
            ],
            "generalExplanation": "El pilar de Seguridad abarca las bases de la seguridad, incluida la gestión de identidades, controles de detección, protección de infraestructura, protección de datos y respuesta ante incidentes."
        }
    },
    "clf-q014": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual princípio de design arquitetural recomenda desacoplar aplicações monolíticas em componentes independentes que se comunicam de forma assíncrona por meio de filas ou barramentos de eventos para evitar falhas em cascata?",
            "options": [
                {
                    "id": "A",
                    "text": "Acoplamento fraco (Loose coupling)",
                    "explanation": "Correto: O acoplamento fraco garante que os componentes de uma aplicação sejam independentes; se um componente for alterado ou falhar, os outros componentes continuarão funcionando."
                },
                {
                    "id": "B",
                    "text": "Acoplamento forte (Tight coupling)",
                    "explanation": "Incorreto: O acoplamento forte cria fortes interdependências em que a falha de um componente derruba todo o sistema."
                },
                {
                    "id": "C",
                    "text": "Escalabilidade vertical (Vertical scaling)",
                    "explanation": "Incorreto: A escalabilidade vertical significa adicionar CPU/RAM a uma única máquina."
                },
                {
                    "id": "D",
                    "text": "Criação de ponto único de falha",
                    "explanation": "Incorreto: Os princípios de arquitetura buscam eliminar pontos únicos de falha, não criá-los."
                }
            ],
            "generalExplanation": "O acoplamento fraco reduz as interdependências entre os componentes do sistema, tornando-os mais resilientes, escaláveis e fáceis de manter."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué principio de diseño arquitectónico recomienda desacoplar aplicaciones monolíticas en componentes independientes que se comunican de forma asíncrona mediante colas o buses de eventos para evitar fallas en cascada?",
            "options": [
                {
                    "id": "A",
                    "text": "Acoplamiento débil (Loose coupling)",
                    "explanation": "Correcto: El acoplamiento débil garantiza que los componentes de una aplicación sean independientes; si un componente cambia o falla, los demás componentes continúan ejecutándose."
                },
                {
                    "id": "B",
                    "text": "Acoplamiento fuerte (Tight coupling)",
                    "explanation": "Incorrecto: El acoplamiento fuerte crea fuertes interdependencias donde la falla de un componente hace caer todo el sistema."
                },
                {
                    "id": "C",
                    "text": "Escalabilidad vertical (Vertical scaling)",
                    "explanation": "Incorrecto: La escalabilidad vertical significa agregar CPU/RAM a una sola máquina."
                },
                {
                    "id": "D",
                    "text": "Creación de punto único de falla",
                    "explanation": "Incorrecto: Los principios de arquitectura buscan eliminar puntos únicos de falla, no crearlos."
                }
            ],
            "generalExplanation": "El acoplamiento débil reduce las interdependencias entre los componentes del sistema, haciéndolos más resilientes, escalables y mantenibles."
        }
    },
    "clf-q015": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "De acordo com o AWS Cloud Adoption Framework (AWS CAF), quais das opções a seguir são categorizadas como perspectivas de Negócios? (Escolha duas.)",
            "options": [
                {
                    "id": "A",
                    "text": "Plataforma (Platform)",
                    "explanation": "Incorreto: Plataforma é uma das perspectivas Técnicas."
                },
                {
                    "id": "B",
                    "text": "Governança (Governance)",
                    "explanation": "Correto: A perspectiva de Governança concentra-se na orquestração de iniciativas em nuvem, no gerenciamento de portfólio e no gerenciamento de riscos de negócios."
                },
                {
                    "id": "C",
                    "text": "Segurança (Security)",
                    "explanation": "Incorreto: Segurança é uma das perspectivas Técnicas."
                },
                {
                    "id": "D",
                    "text": "Operações (Operations)",
                    "explanation": "Incorreto: Operações é uma das perspectivas Técnicas."
                },
                {
                    "id": "E",
                    "text": "Pessoas (People)",
                    "explanation": "Correto: A perspectiva de Pessoas conecta os stakeholders de negócios e tecnologia para desenvolver competências organizacionais, cultura e prontidão."
                }
            ],
            "generalExplanation": "As três perspectivas de Negócios do AWS CAF são Negócios, Pessoas e Governança. As três perspectivas Técnicas são Plataforma, Segurança e Operações."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "Según el AWS Cloud Adoption Framework (AWS CAF), ¿cuáles de las siguientes se clasifican como perspectivas de Negocios? (Elija dos.)",
            "options": [
                {
                    "id": "A",
                    "text": "Plataforma (Platform)",
                    "explanation": "Incorrecto: Plataforma es una de las perspectivas Técnicas."
                },
                {
                    "id": "B",
                    "text": "Gobernanza (Governance)",
                    "explanation": "Correcto: La perspectiva de Gobernanza se centra en orquestar iniciativas en la nube, la gestión de carteras y la gestión de riesgos empresariales."
                },
                {
                    "id": "C",
                    "text": "Seguridad (Security)",
                    "explanation": "Incorrecto: Seguridad es una de las perspectivas Técnicas."
                },
                {
                    "id": "D",
                    "text": "Operaciones (Operations)",
                    "explanation": "Incorrecto: Operaciones es una de las perspectivas Técnicas."
                },
                {
                    "id": "E",
                    "text": "Personas (People)",
                    "explanation": "Correcto: La perspectiva de Personas une a las partes interesadas del negocio y la tecnología para desarrollar habilidades organizacionales, cultura y preparación."
                }
            ],
            "generalExplanation": "Las tres perspectivas de Negocios del AWS CAF son Negocios, Personas y Gobernanza. Las tres perspectivas Técnicas son Plataforma, Seguridad y Operaciones."
        }
    },
    "clf-q016": {
        "pt": {
            "domainName": "Domínio 1: Conceitos de Nuvem",
            "statement": "Qual benefício fundamental da computação em nuvem elimina a necessidade de as organizações preverem os requisitos de capacidade de pico com anos de antecedência, evitando o provisionamento excessivo dispendioso ou o subprovisionamento severo?",
            "options": [
                {
                    "id": "A",
                    "text": "Contratos fixos de licenciamento de longo prazo",
                    "explanation": "Incorreto: A nuvem elimina o licenciamento fixo e rígido em favor de preços sob demanda baseados no consumo."
                },
                {
                    "id": "B",
                    "text": "Infraestrutura dedicada de locatário único",
                    "explanation": "Incorreto: A elasticidade na nuvem é habilitada principalmente por meio de pools compartilhados de infraestrutura multilocatária (multi-tenant)."
                },
                {
                    "id": "C",
                    "text": "Parar de adivinhar a capacidade (Stop guessing capacity)",
                    "explanation": "Correto: 'Parar de adivinhar a capacidade' permite que os sistemas dimensionem recursos dinamicamente para mais ou para menos conforme a demanda exigir, em vez de investir excessivamente em hardware estático."
                },
                {
                    "id": "D",
                    "text": "Substituição anual obrigatória de hardware",
                    "explanation": "Incorreto: A manutenção do hardware é gerenciada integralmente pela AWS sem envolvimento do cliente."
                }
            ],
            "generalExplanation": "'Parar de adivinhar a capacidade' significa que as organizações não precisam mais adquirir hardware caro com base na demanda futura estimada; a capacidade é dimensionada de forma elástica."
        },
        "es": {
            "domainName": "Dominio 1: Conceptos de la Nube",
            "statement": "¿Qué beneficio fundamental de la computación en la nube elimina la necesidad de que las organizaciones predigan los requisitos de capacidad máxima con años de anticipación, evitando un costoso sobreaprovisionamiento o un grave subaprovisionamiento?",
            "options": [
                {
                    "id": "A",
                    "text": "Contratos de licenciamiento fijos a largo plazo",
                    "explanation": "Incorrecto: La nube elimina las licencias fijas y rígidas a favor de precios bajo demanda basados en el consumo."
                },
                {
                    "id": "B",
                    "text": "Infraestructura dedicada de inquilino único",
                    "explanation": "Incorrecto: La elasticidad de la nube se habilita principalmente a través de grupos compartidos de infraestructura multi-inquilino (multi-tenant)."
                },
                {
                    "id": "C",
                    "text": "Dejar de adivinar la capacidad (Stop guessing capacity)",
                    "explanation": "Correcto: 'Dejar de adivinar la capacidad' permite que los sistemas escalen recursos dinámicamente hacia arriba o hacia abajo según lo requiera la demanda, en lugar de invertir en exceso en hardware estático."
                },
                {
                    "id": "D",
                    "text": "Reemplazo anual obligatorio de hardware",
                    "explanation": "Incorrecto: El mantenimiento del hardware lo gestiona en su totalidad AWS sin intervención del cliente."
                }
            ],
            "generalExplanation": "'Dejar de adivinar la capacidad' significa que las organizaciones ya no tienen que comprar hardware costoso en función de la demanda futura estimada; la capacidad escala de manera elástica."
        }
    },
    "clf-q017": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes opções é uma responsabilidade direta do cliente ao executar cargas de trabalho em instâncias do Amazon EC2?",
            "options": [
                {
                    "id": "A",
                    "text": "Descomissionamento e destruição física de discos rígidos com falha",
                    "explanation": "Incorreto: A destruição física do hardware é responsabilidade da AWS."
                },
                {
                    "id": "B",
                    "text": "Manutenção e aplicação de patches no software hipervisor de virtualização",
                    "explanation": "Incorreto: A aplicação de patches no hipervisor é gerenciada inteiramente pela AWS."
                },
                {
                    "id": "C",
                    "text": "Instalação de patches de segurança do sistema operacional e configuração das regras de firewall do SO convidado",
                    "explanation": "Correto: Em serviços IaaS como o Amazon EC2, o cliente é totalmente responsável pelo gerenciamento do sistema operacional convidado, pela instalação de patches do SO e pela configuração de regras de grupos de segurança e firewall (Segurança NA Nuvem)."
                },
                {
                    "id": "D",
                    "text": "Segurança física das instalações do data center que abrigam os servidores",
                    "explanation": "Incorreto: A segurança física dos data centers é estritamente de responsabilidade da AWS (Segurança DA Nuvem)."
                }
            ],
            "generalExplanation": "Sob o Modelo de Responsabilidade Compartilhada da AWS para o Amazon EC2 (IaaS), os clientes são responsáveis pelo gerenciamento dos sistemas operacionais convidados, patches de software, configuração de aplicações e regras de firewall."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "Según el Modelo de Responsabilidad Compartida de AWS, ¿cuál de las siguientes es una responsabilidad directa del cliente al ejecutar cargas de trabajo en instancias de Amazon EC2?",
            "options": [
                {
                    "id": "A",
                    "text": "Desmantelamiento y destrucción física de discos duros dañados",
                    "explanation": "Incorrecto: La destrucción física del hardware es responsabilidad de AWS."
                },
                {
                    "id": "B",
                    "text": "Mantenimiento y aplicación de parches en el software del hipervisor de virtualización",
                    "explanation": "Incorrecto: La aplicación de parches en el hipervisor es administrada en su totalidad por AWS."
                },
                {
                    "id": "C",
                    "text": "Instalación de parches de seguridad del sistema operativo y configuración del firewall del SO invitado",
                    "explanation": "Correcto: En servicios IaaS como Amazon EC2, el cliente es totalmente responsable de administrar el sistema operativo invitado, instalar parches del SO y configurar las reglas de grupos de seguridad y firewall (Seguridad EN la Nube)."
                },
                {
                    "id": "D",
                    "text": "Seguridad física de las instalaciones de los centros de datos que albergan los servidores",
                    "explanation": "Incorrecto: La seguridad física de los centros de datos es estrictamente responsabilidad de AWS (Seguridad DE la Nube)."
                }
            ],
            "generalExplanation": "Bajo el Modelo de Responsabilidad Compartida de AWS para Amazon EC2 (IaaS), los clientes son responsables de administrar los sistemas operativos invitados, los parches de software, la configuración de aplicaciones y las reglas de firewall."
        }
    },
    "clf-q018": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual tarefa de segurança é responsabilidade da AWS quando os clientes armazenam dados no Amazon S3?",
            "options": [
                {
                    "id": "A",
                    "text": "Classificação dos arquivos enviados como públicos, confidenciais ou restritos",
                    "explanation": "Incorreto: A classificação e categorização dos dados é responsabilidade do cliente."
                },
                {
                    "id": "B",
                    "text": "Gerenciamento de senhas de usuários do IAM e autenticação multifator (MFA)",
                    "explanation": "Incorreto: O gerenciamento de credenciais de usuários do IAM é responsabilidade do cliente."
                },
                {
                    "id": "C",
                    "text": "Configuração de políticas de bucket do S3 e gerenciamento das configurações de bloqueio de acesso público",
                    "explanation": "Incorreto: As permissões e controles de acesso aos buckets do S3 são responsabilidades do cliente."
                },
                {
                    "id": "D",
                    "text": "Manutenção do hardware de armazenamento físico subjacente, discos e instalações do data center",
                    "explanation": "Correto: A AWS é responsável pela infraestrutura física, hardware de servidor, rede e descarte de discos que sustentam o Amazon S3."
                }
            ],
            "generalExplanation": "A AWS é responsável pela 'Segurança DA Nuvem'—incluindo data centers físicos, rede, manutenção de discos e infraestrutura de virtualização."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "Según el Modelo de Responsabilidad Compartida de AWS, ¿qué tarea de seguridad es responsabilidad de AWS cuando los clientes almacenan datos en Amazon S3?",
            "options": [
                {
                    "id": "A",
                    "text": "Clasificación de los archivos subidos como públicos, confidenciales o restringidos",
                    "explanation": "Incorrecto: La clasificación y categorización de los datos es responsabilidad del cliente."
                },
                {
                    "id": "B",
                    "text": "Gestión de contraseñas de usuarios de IAM y autenticación multifactor (MFA)",
                    "explanation": "Incorrecto: La administración de credenciales de usuarios de IAM es responsabilidad del cliente."
                },
                {
                    "id": "C",
                    "text": "Configuración de políticas de bucket de S3 y administración de la configuración de bloqueo de acceso público",
                    "explanation": "Incorrecto: Los permisos y controles de acceso de los buckets de S3 son responsabilidad del cliente."
                },
                {
                    "id": "D",
                    "text": "Mantenimiento del hardware de almacenamiento físico subyacente, discos e instalaciones de centros de datos",
                    "explanation": "Correcto: AWS es responsable de la infraestructura física, el hardware del servidor, las redes y la eliminación de discos que dan soporte a Amazon S3."
                }
            ],
            "generalExplanation": "AWS es responsable de la 'Seguridad DE la Nube'—incluyendo centros de datos físicos, redes, mantenimiento de discos e infraestructura de virtualización."
        }
    },
    "clf-q019": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual prática recomendada de segurança dita que os usuários e roles do AWS IAM devem receber apenas as permissões mínimas necessárias para desempenhar suas funções atribuídas?",
            "options": [
                {
                    "id": "A",
                    "text": "Delegação total de acesso administrativo",
                    "explanation": "Incorreto: Conceder acesso administrativo total viola as melhores práticas de segurança."
                },
                {
                    "id": "B",
                    "text": "Credenciais compartilhadas da conta root",
                    "explanation": "Incorreto: O compartilhamento de credenciais root é uma grave vulnerabilidade de segurança."
                },
                {
                    "id": "C",
                    "text": "Grupos de segurança stateless",
                    "explanation": "Incorreto: Security groups são firewalls de rede stateful, não princípios de acesso do IAM."
                },
                {
                    "id": "D",
                    "text": "Princípio do menor privilégio",
                    "explanation": "Correto: O princípio do menor privilégio estabelece que os usuários devem receber apenas as permissões específicas necessárias para realizar suas tarefas, e nada mais."
                }
            ],
            "generalExplanation": "Conceder o menor privilégio é uma prática recomendada fundamental de segurança na AWS: conceda aos usuários apenas as permissões necessárias para desempenhar suas tarefas obrigatórias."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué práctica recomendada de seguridad establece que a los usuarios y roles de AWS IAM solo se les deben otorgar los permisos mínimos necesarios para realizar las funciones laborales asignadas?",
            "options": [
                {
                    "id": "A",
                    "text": "Delegación total de acceso administrativo",
                    "explanation": "Incorrecto: Otorgar acceso administrativo total infringe las prácticas recomendadas de seguridad."
                },
                {
                    "id": "B",
                    "text": "Credenciales compartidas de la cuenta root",
                    "explanation": "Incorrecto: Compartir las credenciales de la cuenta root es una vulnerabilidad de seguridad grave."
                },
                {
                    "id": "C",
                    "text": "Grupos de seguridad sin estado (stateless)",
                    "explanation": "Incorrecto: Los grupos de seguridad son firewalls de red con estado (stateful), no principios de acceso de IAM."
                },
                {
                    "id": "D",
                    "text": "Principio de privilegio mínimo",
                    "explanation": "Correcto: El principio de privilegio mínimo establece que a los usuarios solo se les deben otorgar los permisos específicos requeridos para realizar sus tareas, y nada más."
                }
            ],
            "generalExplanation": "Otorgar el privilegio mínimo es una práctica recomendada de seguridad fundamental en AWS: asigne a los usuarios solo los permisos necesarios para realizar sus tareas requeridas."
        }
    },
    "clf-q020": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual das seguintes opções é uma prática recomendada para proteger o usuário root da conta da AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Gerar uma chave de acesso e uma chave de acesso secreta para o usuário root e compartilhá-las com a equipe de desenvolvimento.",
                    "explanation": "Incorreto: Chaves de acesso nunca devem ser geradas para o usuário root."
                },
                {
                    "id": "B",
                    "text": "Habilitar a Autenticação Multifator (MFA) no usuário root e evitar o uso do usuário root para tarefas administrativas diárias.",
                    "explanation": "Correto: Proteger o usuário root requer habilitar um dispositivo MFA robusto e usar usuários/roles de administrador do IAM dedicados para as tarefas diárias."
                },
                {
                    "id": "C",
                    "text": "Desabilitar requisitos de complexidade de senha na conta root para facilitar o acesso.",
                    "explanation": "Incorreto: Senhas fracas comprometem a segurança da conta."
                },
                {
                    "id": "D",
                    "text": "Anexar uma política em linha de administrador à conta root.",
                    "explanation": "Incorreto: A conta root possui intrinsecamente acesso irrestrito a todos os recursos e não utiliza políticas do IAM."
                }
            ],
            "generalExplanation": "A AWS recomenda fortemente restringir o usuário root habilitando o MFA, excluindo chaves de acesso root e criando usuários do IAM dedicados para tarefas administrativas do dia a dia."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Cuál de las siguientes es una práctica recomendada para proteger al usuario root de la cuenta de AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "Generar una clave de acceso y una clave de acceso secreta para el usuario root y compartirlas con el equipo de desarrollo.",
                    "explanation": "Incorrecto: Nunca se deben generar claves de acceso para el usuario root."
                },
                {
                    "id": "B",
                    "text": "Habilitar la autenticación multifactor (MFA) en el usuario root y evitar usar el usuario root para las tareas administrativas diarias.",
                    "explanation": "Correcto: Proteger al usuario root requiere habilitar un dispositivo MFA seguro y usar usuarios/roles de administración de IAM dedicados para las tareas cotidianas."
                },
                {
                    "id": "C",
                    "text": "Deshabilitar los requisitos de complejidad de contraseñas en la cuenta root para facilitar el acceso.",
                    "explanation": "Incorrecto: Las contraseñas débiles comprometen la seguridad de la cuenta."
                },
                {
                    "id": "D",
                    "text": "Adjuntar una política en línea de administrador a la cuenta root.",
                    "explanation": "Incorrecto: La cuenta root posee intrínsecamente acceso sin restricciones a todos los recursos y no utiliza políticas de IAM."
                }
            ],
            "generalExplanation": "AWS recomienda encarecidamente proteger al usuario root habilitando MFA, eliminando las claves de acceso root y creando usuarios de IAM dedicados para las tareas administrativas del día a día."
        }
    },
    "clf-q021": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Uma equipe de auditoria empresarial necessita de acesso sob demanda à documentação de segurança e conformidade da AWS, incluindo relatórios SOC, relatórios PCI-DSS e certificações ISO, para verificar a conformidade. Qual serviço da AWS fornece acesso em autoatendimento a esses relatórios?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Shield Advanced",
                    "explanation": "Incorreto: O AWS Shield é um serviço de mitigação de DDoS."
                },
                {
                    "id": "B",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorreto: O CloudTrail registra atividades de API da conta, não certificações formais de auditoria de conformidade de terceiros."
                },
                {
                    "id": "C",
                    "text": "AWS Artifact",
                    "explanation": "Correto: O AWS Artifact é o portal central de autoatendimento para acesso sob demanda aos relatórios e acordos de conformidade da AWS."
                },
                {
                    "id": "D",
                    "text": "AWS Trusted Advisor",
                    "explanation": "Incorreto: O Trusted Advisor fornece recomendações de otimização para contas da AWS, não relatórios de conformidade de terceiros."
                }
            ],
            "generalExplanation": "O AWS Artifact é o seu recurso central para informações relacionadas à conformidade, fornecendo acesso sob demanda aos relatórios de segurança e conformidade da AWS (SOC, PCI, ISO) e aos acordos."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "El equipo de auditoría de una empresa requiere acceso bajo demanda a la documentación de seguridad y cumplimiento de AWS, incluidos informes SOC, informes PCI-DSS y certificaciones ISO, para verificar el cumplimiento. ¿Qué servicio de AWS proporciona acceso de autoservicio a estos informes?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Shield Advanced",
                    "explanation": "Incorrecto: AWS Shield es un servicio de mitigación de ataques DDoS."
                },
                {
                    "id": "B",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorrecto: CloudTrail registra la actividad de las API de la cuenta, no las certificaciones formales de auditoría de cumplimiento de terceros."
                },
                {
                    "id": "C",
                    "text": "AWS Artifact",
                    "explanation": "Correcto: AWS Artifact es el portal central de autoservicio para el acceso bajo demanda a los informes y acuerdos de cumplimiento de AWS."
                },
                {
                    "id": "D",
                    "text": "AWS Trusted Advisor",
                    "explanation": "Incorrecto: Trusted Advisor proporciona recomendaciones de optimización para cuentas de AWS, no informes de cumplimiento de terceros."
                }
            ],
            "generalExplanation": "AWS Artifact es el recurso central de referencia para obtener información sobre cumplimiento, ya que proporciona acceso bajo demanda a los informes de seguridad y cumplimiento de AWS (SOC, PCI, ISO) y a los acuerdos."
        }
    },
    "clf-q022": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço da AWS oferece proteção automática e integrada contra ataques comuns de negação de serviço distribuída (DDoS) nas camadas 3 e 4 (como ataques SYN flood e de reflexão UDP) sem custo adicional para todos os clientes da AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Key Management Service (KMS)",
                    "explanation": "Incorreto: O KMS gerencia chaves de criptografia."
                },
                {
                    "id": "B",
                    "text": "AWS Shield Advanced",
                    "explanation": "Incorreto: O Shield Advanced é um serviço por assinatura pago que oferece suporte 24/7 da equipe de resposta a DDoS (DRT) e proteção financeira contra picos de cobrança."
                },
                {
                    "id": "C",
                    "text": "Amazon GuardDuty",
                    "explanation": "Incorreto: O GuardDuty é um serviço de detecção inteligente de ameaças, não um mecanismo ativo em linha de mitigação de DDoS."
                },
                {
                    "id": "D",
                    "text": "AWS Shield Standard",
                    "explanation": "Correto: O AWS Shield Standard oferece proteção automática contra ataques comuns de DDoS na camada de rede e transporte sem custo adicional para todos os clientes da AWS."
                }
            ],
            "generalExplanation": "O AWS Shield Standard defende todos os clientes da AWS contra ataques comuns de DDoS na infraestrutura automaticamente e sem custo adicional."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de AWS proporciona protección automática e integrada contra ataques comunes de denegación de servicio distribuido (DDoS) en las Capas 3 y 4 (como inundaciones SYN y ataques de reflexión UDP) sin cargo adicional para todos los clientes de AWS?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Key Management Service (KMS)",
                    "explanation": "Incorrecto: KMS administra claves de cifrado."
                },
                {
                    "id": "B",
                    "text": "AWS Shield Advanced",
                    "explanation": "Incorrecto: Shield Advanced es un servicio de suscripción de pago que ofrece soporte 24/7 del equipo de respuesta a DDoS (DRT) y protección contra picos de costos."
                },
                {
                    "id": "C",
                    "text": "Amazon GuardDuty",
                    "explanation": "Incorrecto: GuardDuty es un servicio inteligente de detección de amenazas, no un motor activo de mitigación de DDoS en línea."
                },
                {
                    "id": "D",
                    "text": "AWS Shield Standard",
                    "explanation": "Correcto: AWS Shield Standard ofrece protección automática contra ataques DDoS comunes en las capas de red y transporte sin costo adicional para todos los clientes de AWS."
                }
            ],
            "generalExplanation": "AWS Shield Standard defiende a todos los clientes de AWS contra ataques DDoS comunes a la infraestructura automáticamente y sin costo adicional."
        }
    },
    "clf-q023": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço da AWS opera na camada de aplicação (Camada 7) para inspecionar o tráfego web de entrada e bloquear explorações web comuns, como injeção de SQL (SQLi) e Cross-Site Scripting (XSS)?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorreto: O Direct Connect é uma conexão de rede física dedicada entre o ambiente on-premises e a AWS."
                },
                {
                    "id": "B",
                    "text": "AWS Systems Manager",
                    "explanation": "Incorreto: O Systems Manager é uma ferramenta de gerenciamento operacional para instâncias de computação."
                },
                {
                    "id": "C",
                    "text": "AWS Web Application Firewall (AWS WAF)",
                    "explanation": "Correto: O AWS WAF monitora solicitações HTTP e HTTPS encaminhadas para o Amazon CloudFront, ALB ou API Gateway e filtra ameaças web de Camada 7, como injeção de SQL e XSS."
                },
                {
                    "id": "D",
                    "text": "Listas de Controle de Acesso à Rede (NACLs)",
                    "explanation": "Incorreto: As NACLs operam na Camada 4 (IP/porta) e não podem analisar payloads HTTP em busca de injeção de SQL."
                }
            ],
            "generalExplanation": "O AWS WAF é um firewall de aplicações web que oferece controle sobre como o tráfego chega às suas aplicações criando regras de segurança que bloqueiam padrões comuns de exploração."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de AWS opera en la capa de aplicación (Capa 7) para inspeccionar el tráfico web entrante y bloquear vulnerabilidades web comunes como la inyección SQL (SQLi) y Cross-Site Scripting (XSS)?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Direct Connect",
                    "explanation": "Incorrecto: Direct Connect es una conexión de red física dedicada entre las instalaciones locales y AWS."
                },
                {
                    "id": "B",
                    "text": "AWS Systems Manager",
                    "explanation": "Incorrecto: Systems Manager es una herramienta de gestión operativa para instancias de cómputo."
                },
                {
                    "id": "C",
                    "text": "AWS Web Application Firewall (AWS WAF)",
                    "explanation": "Correcto: AWS WAF monitorea las solicitudes HTTP y HTTPS reenviadas a Amazon CloudFront, ALB o API Gateway y filtra las amenazas web de Capa 7 como la inyección SQL y XSS."
                },
                {
                    "id": "D",
                    "text": "Listas de control de acceso a la red (NACLs)",
                    "explanation": "Incorrecto: Las NACL operan en la Capa 4 (IP/puerto) y no pueden analizar cargas útiles HTTP en busca de inyección SQL."
                }
            ],
            "generalExplanation": "AWS WAF es un firewall de aplicaciones web que le permite controlar cómo llega el tráfico a sus aplicaciones mediante la creación de reglas de seguridad que bloquean patrones de explotación comunes."
        }
    },
    "clf-q024": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Uma empresa precisa de um serviço gerenciado para criar, controlar e rotacionar com segurança chaves de criptografia usadas para criptografar dados em repouso em serviços da AWS, como Amazon S3, Amazon EBS e Amazon RDS. Qual serviço deve ser usado?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Secrets Manager",
                    "explanation": "Incorreto: O Secrets Manager gerencia credenciais e senhas de API, utilizando o KMS para a criptografia subjacente das chaves."
                },
                {
                    "id": "B",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorreto: O CloudTrail registra chamadas de API para auditoria."
                },
                {
                    "id": "C",
                    "text": "AWS Certificate Manager (ACM)",
                    "explanation": "Incorreto: O ACM gerencia certificados SSL/TLS para criptografia em trânsito (HTTPS), não chaves simétricas de criptografia de dados."
                },
                {
                    "id": "D",
                    "text": "AWS Key Management Service (AWS KMS)",
                    "explanation": "Correto: O AWS KMS é um serviço totalmente gerenciado que facilita a criação e o gerenciamento de chaves criptográficas e o controle de seu uso em uma ampla gama de serviços da AWS."
                }
            ],
            "generalExplanation": "O AWS KMS facilita a criação e o gerenciamento de chaves criptográficas para criptografar dados em repouso em serviços e aplicações da AWS."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "Una empresa necesita un servicio administrado para crear, controlar y rotar de forma segura claves de cifrado utilizadas para cifrar datos en reposo en servicios de AWS como Amazon S3, Amazon EBS y Amazon RDS. ¿Qué servicio se debe utilizar?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Secrets Manager",
                    "explanation": "Incorrecto: Secrets Manager administra credenciales y contraseñas de API, utilizando KMS para el cifrado de claves subyacente."
                },
                {
                    "id": "B",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorrecto: CloudTrail registra llamadas a la API con fines de auditoría."
                },
                {
                    "id": "C",
                    "text": "AWS Certificate Manager (ACM)",
                    "explanation": "Incorrecto: ACM gestiona certificados SSL/TLS para cifrado en tránsito (HTTPS), no claves de cifrado de datos simétricas."
                },
                {
                    "id": "D",
                    "text": "AWS Key Management Service (AWS KMS)",
                    "explanation": "Correcto: AWS KMS es un servicio totalmente administrado que facilita la creación y administración de claves criptográficas y el control de su uso en una amplia gama de servicios de AWS."
                }
            ],
            "generalExplanation": "AWS KMS facilita la creación y administración de claves criptográficas para cifrar datos en reposo en servicios y aplicaciones de AWS."
        }
    },
    "clf-q025": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço de segurança da AWS usa machine learning e detecção de anomalias para monitorar continuamente contas da AWS contra comportamentos não autorizados, como credenciais comprometidas ou mineração de criptomoedas em instâncias EC2?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon GuardDuty",
                    "explanation": "Correto: O Amazon GuardDuty é um serviço de detecção inteligente de ameaças que monitora continuamente atividades maliciosas e comportamentos não autorizados."
                },
                {
                    "id": "B",
                    "text": "AWS Config",
                    "explanation": "Incorreto: O AWS Config registra o histórico de configurações e avalia a conformidade dos recursos em relação às regras desejadas."
                },
                {
                    "id": "C",
                    "text": "AWS IAM Identity Center",
                    "explanation": "Incorreto: O IAM Identity Center gerencia o logon único (single sign-on) para a força de trabalho."
                },
                {
                    "id": "D",
                    "text": "Amazon Inspector",
                    "explanation": "Incorreto: O Amazon Inspector verifica vulnerabilidades de software (CVEs) no EC2, ECR e Lambda, não inteligência de ameaças em tempo real."
                }
            ],
            "generalExplanation": "O Amazon GuardDuty é um serviço inteligente de detecção de ameaças que analisa fontes de dados fundamentais (CloudTrail, VPC Flow Logs, logs de DNS) para identificar recursos comprometidos."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de seguridad de AWS utiliza machine learning y detección de anomalías para monitorear continuamente las cuentas de AWS en busca de comportamientos no autorizados, como credenciales comprometidas o minería de criptomonedas en instancias EC2?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon GuardDuty",
                    "explanation": "Correcto: Amazon GuardDuty es un servicio inteligente de detección de amenazas que monitorea continuamente la actividad maliciosa y el comportamiento no autorizado."
                },
                {
                    "id": "B",
                    "text": "AWS Config",
                    "explanation": "Incorrecto: AWS Config registra el historial de configuraciones y evalúa el cumplimiento de los recursos con respecto a las reglas deseadas."
                },
                {
                    "id": "C",
                    "text": "AWS IAM Identity Center",
                    "explanation": "Incorrecto: IAM Identity Center administra el inicio de sesión único (single sign-on) para la fuerza laboral."
                },
                {
                    "id": "D",
                    "text": "Amazon Inspector",
                    "explanation": "Incorrecto: Amazon Inspector analiza vulnerabilidades de software (CVEs) en EC2, ECR y Lambda, no inteligencia de amenazas en tiempo real."
                }
            ],
            "generalExplanation": "Amazon GuardDuty es un servicio inteligente de detección de amenazas que analiza fuentes de datos fundamentales (CloudTrail, VPC Flow Logs, registros DNS) para identificar recursos comprometidos."
        }
    },
    "clf-q026": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço da AWS verifica automaticamente instâncias do Amazon EC2, imagens de contêiner no Amazon ECR e funções do AWS Lambda em busca de vulnerabilidades de software e exposição não intencional de rede?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Trusted Advisor",
                    "explanation": "Incorreto: O Trusted Advisor fornece recomendações de práticas recomendadas em alto nível, não verificação profunda de vulnerabilidades de pacotes CVE."
                },
                {
                    "id": "B",
                    "text": "Amazon Macie",
                    "explanation": "Incorreto: O Amazon Macie verifica buckets do S3 em busca de dados confidenciais (PII)."
                },
                {
                    "id": "C",
                    "text": "AWS Shield Standard",
                    "explanation": "Incorreto: O Shield Standard é um serviço de mitigação de DDoS."
                },
                {
                    "id": "D",
                    "text": "Amazon Inspector",
                    "explanation": "Correto: O Amazon Inspector é um serviço automatizado de gerenciamento de vulnerabilidades que verifica continuamente cargas de trabalho em busca de vulnerabilidades de software conhecidas (CVEs) e exposição de rede."
                }
            ],
            "generalExplanation": "O Amazon Inspector descobre cargas de trabalho automaticamente e analisa instâncias EC2, imagens de contêiner e funções Lambda em busca de vulnerabilidades de software e exposição."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de AWS analiza automáticamente instancias de Amazon EC2, imágenes de contenedores en Amazon ECR y funciones de AWS Lambda en busca de vulnerabilidades de software y exposición de red no intencionada?",
            "options": [
                {
                    "id": "A",
                    "text": "AWS Trusted Advisor",
                    "explanation": "Incorrecto: Trusted Advisor ofrece recomendaciones de alto nivel sobre prácticas recomendadas, no análisis profundo de vulnerabilidades de paquetes CVE."
                },
                {
                    "id": "B",
                    "text": "Amazon Macie",
                    "explanation": "Incorrecto: Amazon Macie analiza buckets de S3 en busca de datos confidenciales (PII)."
                },
                {
                    "id": "C",
                    "text": "AWS Shield Standard",
                    "explanation": "Incorrecto: Shield Standard es un servicio de mitigación de ataques DDoS."
                },
                {
                    "id": "D",
                    "text": "Amazon Inspector",
                    "explanation": "Correcto: Amazon Inspector es un servicio automatizado de gestión de vulnerabilidades que analiza continuamente las cargas de trabajo en busca de vulnerabilidades de software conocidas (CVE) y exposición de red."
                }
            ],
            "generalExplanation": "Amazon Inspector descubre automáticamente cargas de trabajo y analiza instancias EC2, imágenes de contenedores y funciones Lambda en busca de vulnerabilidades de software y exposición."
        }
    },
    "clf-q027": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Uma empresa financeira precisa descobrir e proteger dados confidenciais de clientes, como números de cartão de crédito e informações de passaporte (Informações de Identificação Pessoal - PII), armazenados em buckets do Amazon S3. Qual serviço da AWS é projetado para essa finalidade?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Macie",
                    "explanation": "Correto: O Amazon Macie usa machine learning e correspondência de padrões para descobrir, classificar e proteger dados confidenciais (PII) armazenados no Amazon S3."
                },
                {
                    "id": "B",
                    "text": "Amazon GuardDuty",
                    "explanation": "Incorreto: O GuardDuty detecta anomalias de conta, não o conteúdo de PII em documentos no S3."
                },
                {
                    "id": "C",
                    "text": "AWS Artifact",
                    "explanation": "Incorreto: O AWS Artifact fornece relatórios de conformidade para a infraestrutura da AWS."
                },
                {
                    "id": "D",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorreto: O CloudTrail registra chamadas de API, não o conteúdo de dados de arquivos."
                }
            ],
            "generalExplanation": "O Amazon Macie é um serviço de privacidade e segurança de dados totalmente gerenciado que usa machine learning e correspondência de padrões para descobrir e proteger dados confidenciais no S3."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "Una empresa financiera necesita descubrir y proteger datos confidenciales de clientes, como números de tarjetas de crédito e información de pasaportes (Información de Identificación Personal - PII), almacenados en buckets de Amazon S3. ¿Qué servicio de AWS está diseñado para este propósito?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon Macie",
                    "explanation": "Correcto: Amazon Macie utiliza machine learning y coincidencia de patrones para descubrir, clasificar y proteger datos confidenciales (PII) almacenados en Amazon S3."
                },
                {
                    "id": "B",
                    "text": "Amazon GuardDuty",
                    "explanation": "Incorrecto: GuardDuty detecta anomalías en la cuenta, no contenido de PII en documentos dentro de S3."
                },
                {
                    "id": "C",
                    "text": "AWS Artifact",
                    "explanation": "Incorrecto: AWS Artifact proporciona informes de cumplimiento para la infraestructura de AWS."
                },
                {
                    "id": "D",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorrecto: CloudTrail registra llamadas a la API, no el contenido de los archivos de datos."
                }
            ],
            "generalExplanation": "Amazon Macie es un servicio de seguridad y privacidad de datos totalmente administrado que utiliza machine learning y coincidencia de patrones para descubrir y proteger datos confidenciales en S3."
        }
    },
    "clf-q028": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual serviço da AWS fornece uma visão abrangente e centralizada de alertas de segurança de alta prioridade e status de conformidade ao agregar descobertas de múltiplos serviços da AWS (como GuardDuty, Inspector e Macie)?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon CloudWatch",
                    "explanation": "Incorreto: O CloudWatch monitora métricas de desempenho e logs de aplicações."
                },
                {
                    "id": "B",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorreto: O CloudTrail registra logs de auditoria de API."
                },
                {
                    "id": "C",
                    "text": "AWS Security Hub",
                    "explanation": "Correto: O AWS Security Hub oferece um serviço unificado de gerenciamento de postura de segurança que agrega, organiza e prioriza descobertas de segurança de múltiplos serviços da AWS."
                },
                {
                    "id": "D",
                    "text": "AWS Systems Manager",
                    "explanation": "Incorreto: O Systems Manager gerencia configurações de nós e patches."
                }
            ],
            "generalExplanation": "O AWS Security Hub oferece uma visão abrangente dos seus alertas de segurança e da sua postura de segurança em todas as suas contas da AWS, agregando descobertas de múltiplas ferramentas de segurança."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué servicio de AWS proporciona una vista integral y centralizada de las alertas de seguridad de alta prioridad y el estado de cumplimiento al agregar hallazgos de múltiples servicios de AWS (como GuardDuty, Inspector y Macie)?",
            "options": [
                {
                    "id": "A",
                    "text": "Amazon CloudWatch",
                    "explanation": "Incorrecto: CloudWatch monitorea métricas de rendimiento y registros de aplicaciones."
                },
                {
                    "id": "B",
                    "text": "AWS CloudTrail",
                    "explanation": "Incorrecto: CloudTrail registra registros de auditoría de llamadas a la API."
                },
                {
                    "id": "C",
                    "text": "AWS Security Hub",
                    "explanation": "Correcto: AWS Security Hub proporciona un servicio unificado de gestión de la postura de seguridad que agrega, organiza y prioriza los hallazgos de seguridad de múltiples servicios de AWS."
                },
                {
                    "id": "D",
                    "text": "AWS Systems Manager",
                    "explanation": "Incorrecto: Systems Manager administra configuraciones de nodos y parches."
                }
            ],
            "generalExplanation": "AWS Security Hub le brinda una vista completa de sus alertas de seguridad y de su postura de seguridad en todas sus cuentas de AWS al agregar hallazgos de múltiples herramientas de seguridad."
        }
    },
    "clf-q029": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual recurso do AWS Organizations permite que um administrador aplique proteções (guardrails) preventivas centrais e restrinja as permissões máximas disponíveis para contas-membro em toda a organização?",
            "options": [
                {
                    "id": "A",
                    "text": "Senhas de Usuário do IAM",
                    "explanation": "Incorreto: As senhas do IAM gerenciam a autenticação de usuários individuais."
                },
                {
                    "id": "B",
                    "text": "Grupos de Segurança (Security Groups)",
                    "explanation": "Incorreto: Security groups são firewalls virtuais para instâncias de computação."
                },
                {
                    "id": "C",
                    "text": "Políticas de Controle de Serviços (Service Control Policies - SCPs)",
                    "explanation": "Correto: As Service Control Policies (SCPs) são políticas preventivas usadas no AWS Organizations para gerenciar permissões e aplicar proteções (guardrails) nas contas-membro."
                },
                {
                    "id": "D",
                    "text": "Tabelas de Rotas da VPC",
                    "explanation": "Incorreto: As tabelas de rotas controlam o encaminhamento de pacotes de rede em uma VPC."
                }
            ],
            "generalExplanation": "As Políticas de Controle de Serviços (SCPs) oferecem controle central sobre as permissões máximas disponíveis para todas as contas de uma organização."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué característica de AWS Organizations permite a un administrador aplicar barreras de protección preventivas centrales y restringir los permisos máximos disponibles para las cuentas miembro en toda la organización?",
            "options": [
                {
                    "id": "A",
                    "text": "Contraseñas de usuario de IAM",
                    "explanation": "Incorrecto: Las contraseñas de IAM administran la autenticación de usuarios individuales."
                },
                {
                    "id": "B",
                    "text": "Grupos de seguridad (Security Groups)",
                    "explanation": "Incorrecto: Los grupos de seguridad son firewalls virtuales para instancias de cómputo."
                },
                {
                    "id": "C",
                    "text": "Políticas de Control de Servicios (Service Control Policies - SCPs)",
                    "explanation": "Correcto: Las Service Control Policies (SCPs) son políticas preventivas utilizadas en AWS Organizations para administrar permisos y aplicar barreras de protección en las cuentas miembro."
                },
                {
                    "id": "D",
                    "text": "Tablas de ruteo de la VPC",
                    "explanation": "Incorrecto: Las tablas de ruteo controlan el reenvío de paquetes de red en una VPC."
                }
            ],
            "generalExplanation": "Las Service Control Policies (SCPs) ofrecen control central sobre los permisos máximos disponibles para todas las cuentas de una organización."
        }
    },
    "clf-q030": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Uma aplicação executada em uma instância do Amazon EC2 precisa acessar com segurança objetos em um bucket do Amazon S3. Qual mecanismo deve ser usado para fornecer credenciais à aplicação sem armazenar chaves de acesso estáticas da AWS na instância?",
            "options": [
                {
                    "id": "A",
                    "text": "Atribuir uma IAM Role à instância EC2 por meio de um perfil de instância (instance profile).",
                    "explanation": "Correto: As IAM Roles permitem que aplicações executadas em instâncias EC2 obtenham credenciais de segurança temporárias e rotacionadas automaticamente, sem embutir chaves estáticas no código."
                },
                {
                    "id": "B",
                    "text": "Inserir as credenciais root da conta da AWS diretamente no código-fonte da aplicação.",
                    "explanation": "Incorreto: Inserir credenciais root no código é uma vulnerabilidade de segurança gravíssima."
                },
                {
                    "id": "C",
                    "text": "Tornar o bucket do S3 publicamente legível e gravável para qualquer pessoa na internet.",
                    "explanation": "Incorreto: Tornar os dados públicos gera uma grave exposição de segurança."
                },
                {
                    "id": "D",
                    "text": "Criar um usuário do IAM e salvar a chave de acesso em um arquivo de texto na área de trabalho do EC2.",
                    "explanation": "Incorreto: Armazenar credenciais estáticas em texto sem formatação no disco viola as melhores práticas de segurança."
                }
            ],
            "generalExplanation": "As IAM Roles para o Amazon EC2 permitem que as aplicações nas instâncias obtenham com segurança credenciais temporárias da AWS por meio do Serviço de Metadados de Instância (IMDS)."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "Una aplicación que se ejecuta en una instancia de Amazon EC2 necesita acceder de forma segura a objetos en un bucket de Amazon S3. ¿Qué mecanismo se debe utilizar para proporcionar credenciales a la aplicación sin almacenar claves de acceso estáticas de AWS en la instancia?",
            "options": [
                {
                    "id": "A",
                    "text": "Asignar un rol de IAM a la instancia EC2 mediante un perfil de instancia (instance profile).",
                    "explanation": "Correcto: Los roles de IAM permiten que las aplicaciones que se ejecutan en instancias EC2 obtengan credenciales de seguridad temporales rotadas automáticamente sin codificar claves estáticas."
                },
                {
                    "id": "B",
                    "text": "Incorporar las credenciales root de la cuenta de AWS en el código fuente de la aplicación.",
                    "explanation": "Incorrecto: Incrustar credenciales root en el código fuente es una vulnerabilidad de seguridad gravísima."
                },
                {
                    "id": "C",
                    "text": "Hacer que el bucket de S3 sea legible y modificable públicamente para cualquier persona en Internet.",
                    "explanation": "Incorrecto: Hacer públicos los datos genera una grave exposición de seguridad."
                },
                {
                    "id": "D",
                    "text": "Crear un usuario de IAM y guardar la clave de acceso en un archivo de texto en el escritorio de EC2.",
                    "explanation": "Incorrecto: Almacenar credenciales estáticas en texto plano en el disco viola las prácticas recomendadas de seguridad."
                }
            ],
            "generalExplanation": "Los roles de IAM para Amazon EC2 permiten que las aplicaciones en las instancias recuperen de forma segura credenciales temporales de AWS mediante el Servicio de Metadatos de Instancia (IMDS)."
        }
    },
    "clf-q031": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual mecanismo de autenticação adiciona uma camada extra de segurança além do nome de usuário e senha tradicionais, exigindo uma chave de segurança física ou um código temporário de uso único (TOTP) de um aplicativo autenticador?",
            "options": [
                {
                    "id": "A",
                    "text": "Autenticação Multifator (MFA)",
                    "explanation": "Correto: A Autenticação Multifator (MFA) exige que os usuários forneçam dois ou mais fatores de autenticação (senha + token/chave temporária) antes de obter acesso."
                },
                {
                    "id": "B",
                    "text": "Tempo limite de federação de logon único (SSO)",
                    "explanation": "Incorreto: O tempo limite controla a duração da sessão, não a autenticação de dois fatores."
                },
                {
                    "id": "C",
                    "text": "Marcação de recursos (Resource tagging)",
                    "explanation": "Incorreto: A marcação de recursos é usada para organização de metadados e rastreamento de custos."
                },
                {
                    "id": "D",
                    "text": "Validação de modelos do AWS CloudFormation",
                    "explanation": "Incorreto: A validação de modelos do CloudFormation verifica a sintaxe de infraestrutura como código."
                }
            ],
            "generalExplanation": "A Autenticação Multifator (MFA) é uma prática recomendada simples que adiciona uma camada extra de proteção sobre o seu nome de usuário e senha."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué mecanismo de autenticación agrega una capa adicional de seguridad más allá del nombre de usuario y la contraseña tradicionales al requerir una clave de seguridad física o un código de un solo uso basado en el tiempo (TOTP) desde una aplicación autenticadora?",
            "options": [
                {
                    "id": "A",
                    "text": "Autenticación multifactor (MFA)",
                    "explanation": "Correcto: La autenticación multifactor (MFA) requiere que los usuarios proporcionen dos o más factores de autenticación (contraseña + token/clave temporal) antes de obtener acceso."
                },
                {
                    "id": "B",
                    "text": "Tiempo de espera de federación de inicio de sesión único (SSO)",
                    "explanation": "Incorrecto: El tiempo de espera controla la duración de la sesión, no la autenticación de dos factores."
                },
                {
                    "id": "C",
                    "text": "Etiquetado de recursos (Resource tagging)",
                    "explanation": "Incorrecto: El etiquetado de recursos se utiliza para la organización de metadatos y el seguimiento de costos."
                },
                {
                    "id": "D",
                    "text": "Validación de plantillas de AWS CloudFormation",
                    "explanation": "Incorrecto: La validación de plantillas de CloudFormation verifica la sintaxis de la infraestructura como código."
                }
            ],
            "generalExplanation": "La autenticación multifactor (MFA) es una práctica recomendada sencilla que agrega una capa adicional de protección a su nombre de usuario y contraseña."
        }
    },
    "clf-q032": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Sob o Modelo de Responsabilidade Compartilhada da AWS, quais das seguintes opções são exemplos de 'Segurança DA Nuvem' gerenciada pela AWS? (Escolha duas.)",
            "options": [
                {
                    "id": "A",
                    "text": "Gerenciamento de usuários do IAM do cliente e associações a grupos",
                    "explanation": "Incorreto: O cliente é responsável por gerenciar usuários e políticas do IAM."
                },
                {
                    "id": "B",
                    "text": "Configuração de contas de usuários de banco de dados e permissões SQL",
                    "explanation": "Incorreto: O cliente gerencia usuários de banco de dados e permissões de tabelas."
                },
                {
                    "id": "C",
                    "text": "Manutenção e substituição de hardware físico defeituoso de servidores de computação",
                    "explanation": "Correto: A AWS gerencia e mantém todo o hardware do host físico, racks e cabos de rede."
                },
                {
                    "id": "D",
                    "text": "Segurança física de data centers e instalações de servidores",
                    "explanation": "Correto: A AWS é a única responsável pela segurança do perímetro físico do data center, entrada biométrica e vigilância."
                },
                {
                    "id": "E",
                    "text": "Criptografia de arquivos confidenciais do cliente antes do upload para o Amazon S3",
                    "explanation": "Incorreto: A criptografia do lado do cliente e a classificação dos dados são de responsabilidade do cliente."
                }
            ],
            "generalExplanation": "A AWS é responsável pela 'Segurança DA Nuvem'—a infraestrutura física, instalações, hardware e camada de virtualização fundamental."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "Bajo el Modelo de Responsabilidad Compartida de AWS, ¿cuáles de los siguientes son ejemplos de 'Seguridad DE la Nube' administrada por AWS? (Elija dos.)",
            "options": [
                {
                    "id": "A",
                    "text": "Gestión de usuarios de IAM del cliente y membresías de grupos",
                    "explanation": "Incorrecto: El cliente es responsable de administrar los usuarios y las políticas de IAM."
                },
                {
                    "id": "B",
                    "text": "Configuración de cuentas de usuario de bases de datos y permisos SQL",
                    "explanation": "Incorrecto: El cliente administra los usuarios de la base de datos y los permisos de las tablas."
                },
                {
                    "id": "C",
                    "text": "Mantenimiento y reemplazo de hardware físico defectuoso de servidores de cómputo",
                    "explanation": "Correcto: AWS administra y mantiene todo el hardware físico del host, racks y cables de red."
                },
                {
                    "id": "D",
                    "text": "Seguridad física de centros de datos e instalaciones de servidores",
                    "explanation": "Correcto: AWS es el único responsable de la seguridad perimetral física de los centros de datos, acceso biométrico y videovigilancia."
                },
                {
                    "id": "E",
                    "text": "Cifrado de archivos confidenciales del cliente antes de subirlos a Amazon S3",
                    "explanation": "Incorrecto: El cifrado del lado del cliente y la clasificación de datos son responsabilidad del cliente."
                }
            ],
            "generalExplanation": "AWS es responsable de la 'Seguridad DE la Nube'—la infraestructura física, las instalaciones, el hardware y la capa de virtualización fundamental."
        }
    },
    "clf-q033": {
        "pt": {
            "domainName": "Domínio 2: Segurança e Conformidade",
            "statement": "Qual firewall virtual em uma Amazon VPC opera no nível da interface de rede da instância e é stateful (ou seja, o tráfego de retorno é permitido automaticamente, independentemente das regras de saída)?",
            "options": [
                {
                    "id": "A",
                    "text": "Grupo de Segurança (Security Group)",
                    "explanation": "Correto: Os Security Groups operam no nível da instância/ENI e são stateful (com estado)—o tráfego de entrada permitido por uma regra autoriza o tráfego de resposta automaticamente."
                },
                {
                    "id": "B",
                    "text": "Lista de Controle de Acesso à Rede (NACL)",
                    "explanation": "Incorreto: As Network ACLs operam no nível da sub-rede e são stateless (sem estado, exigindo regras explícitas de entrada e de saída)."
                },
                {
                    "id": "C",
                    "text": "Internet Gateway",
                    "explanation": "Incorreto: Um Internet Gateway fornece roteamento entre a VPC e a internet, não filtragem com estado de firewall na instância."
                },
                {
                    "id": "D",
                    "text": "Tabela de Rotas (Route Table)",
                    "explanation": "Incorreto: As tabelas de rotas determinam para onde o tráfego de rede é direcionado."
                }
            ],
            "generalExplanation": "Os grupos de segurança atuam como um firewall virtual para suas instâncias EC2 para controlar o tráfego de entrada e saída no nível da instância com filtragem com estado (stateful)."
        },
        "es": {
            "domainName": "Dominio 2: Seguridad y Cumplimiento",
            "statement": "¿Qué firewall virtual en una Amazon VPC opera a nivel de interfaz de red de la instancia y tiene estado (stateful, lo que significa que el tráfico de retorno se permite automáticamente independientemente de las reglas de salida)?",
            "options": [
                {
                    "id": "A",
                    "text": "Grupo de Seguridad (Security Group)",
                    "explanation": "Correcto: Los Security Groups operan a nivel de instancia/ENI y son stateful (con estado): el tráfico de entrada permitido por una regla autoriza automáticamente el tráfico de respuesta."
                },
                {
                    "id": "B",
                    "text": "Lista de Control de Acceso a la Red (NACL)",
                    "explanation": "Incorrecto: Las Network ACL operan a nivel de subred y son stateless (sin estado, requiriendo reglas explícitas de entrada y salida)."
                },
                {
                    "id": "C",
                    "text": "Internet Gateway",
                    "explanation": "Incorrecto: Un Internet Gateway proporciona enrutamiento entre la VPC e Internet, no filtrado con estado de firewall en la instancia."
                },
                {
                    "id": "D",
                    "text": "Tabla de Ruteo (Route Table)",
                    "explanation": "Incorrecto: Las tablas de ruteo determinan hacia dónde se dirige el tráfico de red."
                }
            ],
            "generalExplanation": "Los grupos de seguridad actúan como un firewall virtual para sus instancias EC2 para controlar el tráfico entrante y saliente a nivel de instancia con filtrado con estado (stateful)."
        }
    }
}
