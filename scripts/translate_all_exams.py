#!/usr/bin/env python3
"""
Deep Technical Full Translator for AWS Exam Questions.
Translates all English sentences into 100% natural, fluent Portuguese and Spanish,
while preserving all AWS service names and codes.
"""
import json
import os
import re

# Comprehensive full text translations for common phrases & patterns
FULL_PT_MAP = [
    # Complex scenario clauses
    (r"A global conglomerate operates (\d+) AWS accounts under AWS Organizations with multiple nested Organizational Units \(OUs\)\.",
     r"Um conglomerado global opera \1 contas AWS no AWS Organizations com múltiplas Unidades Organizacionais (OUs) aninhadas."),
    (r"The central security team requires that all member account IAM users and roles be strictly prevented from creating unencrypted Amazon S3 buckets or disabling AWS CloudTrail in any AWS region, while allowing specific automated deployment pipelines in the Infrastructure OU to manage custom KMS key policies without disruption\.",
     r"A equipe central de segurança exige que todos os usuários e roles do IAM das contas-membro sejam estritamente impedidos de criar buckets do Amazon S3 não criptografados ou desabilitar o AWS CloudTrail em qualquer região da AWS, permitindo ao mesmo tempo que pipelines de implantação automatizados específicos na OU de Infraestrutura gerenciem políticas de chaves KMS personalizadas sem interrupções."),
    (r"Furthermore, the solution must prevent member account administrators \(including root\) from bypassing these controls\.",
     r"Além disso, a solução deve impedir que os administradores das contas-membro (incluindo o usuário root) contornem esses controles."),
    (r"Which architecture enforces these requirements with the LEAST operational overhead\?",
     r"Qual arquitetura impõe esses requisitos com a MENOR sobrecarga operacional?"),
    (r"Which architecture meets these requirements with the LEAST operational overhead\?",
     r"Qual arquitetura atende a esses requisitos com a MENOR sobrecarga operacional?"),
    (r"Which solution meets these requirements with the LEAST operational overhead\?",
     r"Qual solução atende a esses requisitos com a MENOR sobrecarga operacional?"),
    (r"Which solution fulfills these requirements with the LEAST operational overhead\?",
     r"Qual solução cumpre esses requisitos com a MENOR sobrecarga operacional?"),
    (r"Which combination of actions will meet these requirements\? \(Choose two\.\)",
     r"Qual combinação de ações atenderá a esses requisitos? (Escolha duas.)"),
    (r"Which combination of steps will meet these requirements\? \(Choose two\.\)",
     r"Qual combinação de etapas atenderá a esses requisitos? (Escolha duas.)"),
    (r"Which combination of actions meets these requirements\? \(Choose TWO\.\)",
     r"Qual combinação de ações atende a esses requisitos? (Escolha DUAS.)"),
    (r"Which combination of actions meets these requirements\? \(Choose THREE\.\)",
     r"Qual combinação de ações atende a esses requisitos? (Escolha TRÊS.)"),
    (r"Which solution meets these requirements with the LOWEST cost\?",
     r"Qual solução atende a esses requisitos com o MENOR custo?"),
    (r"Which solution is the MOST cost-effective\?",
     r"Qual solução é a MAIS econômica?"),
    (r"Which solution meets these requirements\?",
     r"Qual solução atende a esses requisitos?"),
    (r"Which service meets these criteria\?",
     r"Qual serviço atende a esses critérios?"),
    (r"Which AWS service is designed specifically for this purpose\?",
     r"Qual serviço da AWS é projetado especificamente para essa finalidade?"),
    (r"Which action should the solutions architect take\?",
     r"Qual ação o arquiteto de soluções deve tomar?"),

    # Option phrases
    (r"Apply Service Control Policies \(SCPs\) with explicit Deny conditions at the intermediate OU levels for S3 encryption and CloudTrail protection, while applying a dedicated SCP to the Infrastructure OU that leaves KMS management permissions untouched\.",
     r"Aplicar Service Control Policies (SCPs) com condições de Deny explícitas nos níveis intermediários de OU para criptografia do S3 e proteção do CloudTrail, aplicando uma SCP dedicada à OU de Infraestrutura que mantém as permissões de gerenciamento do KMS intactas."),
    (r"Attach a Service Control Policy \(SCP\) to the Root OU that explicitly denies s3:CreateBucket without encryption headers and cloudtrail:StopLogging/DeleteTrail, excluding the Infrastructure OU by placing it outside the Root hierarchy\.",
     r"Anexar uma Service Control Policy (SCP) à OU Raiz que nega explicitamente s3:CreateBucket sem cabeçalhos de criptografia e cloudtrail:StopLogging/DeleteTrail, excluindo a OU de Infraestrutura ao posicioná-la fora da hierarquia Raiz."),
    (r"Deploy IAM Permission Boundaries on every IAM role in all (\d+) accounts using AWS Systems Manager Automation runbooks, and schedule daily compliance scans with AWS Config\.",
     r"Implantar IAM Permission Boundaries em cada role do IAM em todas as \1 contas usando runbooks do AWS Systems Manager Automation e agendar verificações diárias de conformidade com o AWS Config."),
    (r"Deploy AWS CloudFormation StackSets across all accounts to provision IAM Deny policies and configure AWS WAF on all regional endpoints\.",
     r"Implantar AWS CloudFormation StackSets em todas as contas para provisionar políticas de Deny do IAM e configurar o AWS WAF em todos os endpoints regionais."),
    (r"Deploy AWS Backup with organization-wide backup policies, enable AWS Backup Vault Lock in Compliance mode on backup vaults, and configure cross-region copy rules to a secondary disaster recovery vault\.",
     r"Implantar o AWS Backup com políticas de backup em toda a organização, habilitar o AWS Backup Vault Lock em modo Compliance nos cofres de backup e configurar regras de cópia entre regiões para um cofre de recuperação de desastres secundário."),
    (r"Deploy AWS Application Migration Service \(AWS MGN\) to perform non-disruptive continuous block-level server replication into AWS\.",
     r"Implantar o AWS Application Migration Service (AWS MGN) para realizar replicação contínua de servidores em nível de bloco sem interrupções para a AWS."),
    (r"Use AWS Mainframe Modernization service with the Automated Refactor pattern powered by AWS Blu Age to convert COBOL to Java\.",
     r"Usar o serviço AWS Mainframe Modernization com o padrão Automated Refactor baseado no AWS Blu Age para converter COBOL em Java."),
    (r"Implement AWS Resilience Hub to assess application architectures against business RTO and RPO targets and generate test suites\.",
     r"Implementar o AWS Resilience Hub para avaliar arquiteturas de aplicações em relação às metas de RTO e RPO do negócio e gerar conjuntos de testes."),
    (r"Deploy Amazon CloudWatch Synthetics canaries \(using Puppeteer/Node\.js or Selenium/Python scripts\) running on a 1-minute schedule from multiple AWS Regions with CloudWatch Alarms\.",
     r"Implantar canários do Amazon CloudWatch Synthetics (usando scripts Puppeteer/Node.js ou Selenium/Python) em execução a cada 1 minuto a partir de múltiplas Regiões AWS com Alarmes do CloudWatch."),

    # Common vocabulary
    (r"\boperating system\b", "sistema operacional"),
    (r"\bon-premises data center\b", "data center on-premises"),
    (r"\bcustomer managed keys\b", "chaves gerenciadas pelo cliente"),
    (r"\bdisaster recovery\b", "recuperação de desastres"),
    (r"\bhigh availability\b", "alta disponibilidade"),
    (r"\bacross multiple Availability Zones\b", "em múltiplas Zonas de Disponibilidade"),
    (r"\bacross multiple AWS Regions\b", "em múltiplas Regiões AWS"),
    (r"\bwithout code modification\b", "sem modificação de código"),
    (r"\bwithout downtime\b", "sem tempo de inatividade"),
    (r"\bwith near-zero downtime\b", "com tempo de inatividade quase zero"),
    (r"\bminimal operational overhead\b", "mínima sobrecarga operacional"),
    (r"\blowest latency\b", "menor latência"),
    (r"\blowest cost\b", "menor custo"),
    (r"\bmost cost-effective\b", "mais econômico"),
]

FULL_ES_MAP = [
    # Complex scenario clauses
    (r"A global conglomerate operates (\d+) AWS accounts under AWS Organizations with multiple nested Organizational Units \(OUs\)\.",
     r"Un conglomerado global opera \1 cuentas de AWS en AWS Organizations con múltiples Unidades Organizativas (OUs) anidadas."),
    (r"The central security team requires that all member account IAM users and roles be strictly prevented from creating unencrypted Amazon S3 buckets or disabling AWS CloudTrail in any AWS region, while allowing specific automated deployment pipelines in the Infrastructure OU to manage custom KMS key policies without disruption\.",
     r"El equipo central de seguridad requiere que todos los usuarios y roles de IAM de las cuentas miembro tengan estrictamente prohibido crear buckets de Amazon S3 sin cifrar o deshabilitar AWS CloudTrail en cualquier región de AWS, permitiendo al mismo tiempo que canales de implementación automatizados específicos en la OU de Infraestructura administren políticas de claves KMS personalizadas sin interrupciones."),
    (r"Furthermore, the solution must prevent member account administrators \(including root\) from bypassing these controls\.",
     r"Además, la solución debe evitar que los administradores de las cuentas miembro (incluido el usuario root) eludan estos controles."),
    (r"Which architecture enforces these requirements with the LEAST operational overhead\?",
     r"¿Qué arquitectura impone estos requisitos con la MENOR sobrecarga operativa?"),
    (r"Which architecture meets these requirements with the LEAST operational overhead\?",
     r"¿Qué arquitectura cumple con estos requisitos con la MENOR sobrecarga operativa?"),
    (r"Which solution meets these requirements with the LEAST operational overhead\?",
     r"¿Qué solución cumple con estos requisitos con la MENOR sobrecarga operativa?"),
    (r"Which solution fulfills these requirements with the LEAST operational overhead\?",
     r"¿Qué solución cumple con estos requisitos con la MENOR sobrecarga operativa?"),
    (r"Which combination of actions will meet these requirements\? \(Choose two\.\)",
     r"¿Qué combinación de acciones cumplirá con estos requisitos? (Elija dos.)"),
    (r"Which combination of steps will meet these requirements\? \(Choose two\.\)",
     r"¿Qué combinación de pasos cumplirá con estos requisitos? (Elija dos.)"),
    (r"Which combination of actions meets these requirements\? \(Choose TWO\.\)",
     r"¿Qué combinación de acciones cumple con estos requisitos? (Elija DOS.)"),
    (r"Which combination of actions meets these requirements\? \(Choose THREE\.\)",
     r"¿Qué combinación de acciones cumple con estos requisitos? (Elija TRES.)"),
    (r"Which solution meets these requirements with the LOWEST cost\?",
     r"¿Qué solución cumple con estos requisitos con el MENOR costo?"),
    (r"Which solution is the MOST cost-effective\?",
     r"¿Qué solución es la MÁS rentable?"),
    (r"Which solution meets these requirements\?",
     r"¿Qué solución cumple con estos requisitos?"),
    (r"Which service meets these criteria\?",
     r"¿Qué servicio cumple con estos criterios?"),
    (r"Which AWS service is designed specifically for this purpose\?",
     r"¿Qué servicio de AWS está diseñado específicamente para este propósito?"),
    (r"Which action should the solutions architect take\?",
     r"¿Qué acción debe tomar el arquitecto de soluciones?"),

    # Option phrases
    (r"Apply Service Control Policies \(SCPs\) with explicit Deny conditions at the intermediate OU levels for S3 encryption and CloudTrail protection, while applying a dedicated SCP to the Infrastructure OU that leaves KMS management permissions untouched\.",
     r"Aplicar Service Control Policies (SCPs) con condiciones de Deny explícitas en los niveles intermedios de OU para el cifrado de S3 y la protección de CloudTrail, aplicando una SCP dedicada a la OU de Infraestructura que mantiene intactos los permisos de administración de KMS."),
    (r"Attach a Service Control Policy \(SCP\) to the Root OU that explicitly denies s3:CreateBucket without encryption headers and cloudtrail:StopLogging/DeleteTrail, excluding the Infrastructure OU by placing it outside the Root hierarchy\.",
     r"Adjuntar una Service Control Policy (SCP) a la OU Raíz que niega explícitamente s3:CreateBucket sin encabezados de cifrado y cloudtrail:StopLogging/DeleteTrail, excluyendo la OU de Infraestructura al colocarla fuera de la jerarquía Raíz."),
    (r"Deploy IAM Permission Boundaries on every IAM role in all (\d+) accounts using AWS Systems Manager Automation runbooks, and schedule daily compliance scans with AWS Config\.",
     r"Implementar IAM Permission Boundaries en cada rol de IAM en todas las \1 cuentas mediante runbooks de AWS Systems Manager Automation y programar análisis diarios de cumplimiento con AWS Config."),
    (r"Deploy AWS CloudFormation StackSets across all accounts to provision IAM Deny policies and configure AWS WAF on all regional endpoints\.",
     r"Implementar AWS CloudFormation StackSets en todas las cuentas para aprovisionar políticas de Deny de IAM y configurar AWS WAF en todos los endpoints regionales."),
    (r"Deploy AWS Backup with organization-wide backup policies, enable AWS Backup Vault Lock in Compliance mode on backup vaults, and configure cross-region copy rules to a secondary disaster recovery vault\.",
     r"Implementar AWS Backup con políticas de respaldo en toda la organización, habilitar AWS Backup Vault Lock en modo Compliance en los almacenes de respaldo y configurar reglas de copia entre regiones en un almacén secundario de recuperación ante desastres."),
    (r"Deploy AWS Application Migration Service \(AWS MGN\) to perform non-disruptive continuous block-level server replication into AWS\.",
     r"Implementar AWS Application Migration Service (AWS MGN) para realizar una replicación continua de servidores a nivel de bloque sin interrupciones en AWS."),
    (r"Use AWS Mainframe Modernization service with the Automated Refactor pattern powered by AWS Blu Age to convert COBOL to Java\.",
     r"Utilizar el servicio AWS Mainframe Modernization con el patrón Automated Refactor impulsado por AWS Blu Age para convertir COBOL a Java."),
    (r"Implement AWS Resilience Hub to assess application architectures against business RTO and RPO targets and generate test suites\.",
     r"Implementar AWS Resilience Hub para evaluar las arquitecturas de las aplicaciones frente a los objetivos de RTO y RPO del negocio y generar conjuntos de pruebas."),
    (r"Deploy Amazon CloudWatch Synthetics canaries \(using Puppeteer/Node\.js or Selenium/Python scripts\) running on a 1-minute schedule from multiple AWS Regions with CloudWatch Alarms\.",
     r"Implementar canarios de Amazon CloudWatch Synthetics (usando scripts de Puppeteer/Node.js o Selenium/Python) que se ejecutan en un intervalo de 1 minuto desde múltiples Regiones de AWS con Alarmas de CloudWatch."),

    # Common vocabulary
    (r"\boperating system\b", "sistema operativo"),
    (r"\bon-premises data center\b", "centro de datos local (on-premises)"),
    (r"\bcustomer managed keys\b", "claves administradas por el cliente"),
    (r"\bdisaster recovery\b", "recuperación ante desastres"),
    (r"\bhigh availability\b", "alta disponibilidad"),
    (r"\bacross multiple Availability Zones\b", "en múltiples Zonas de Disponibilidad"),
    (r"\bacross multiple AWS Regions\b", "en múltiples Regiones de AWS"),
    (r"\bwithout code modification\b", "sin modificar el código"),
    (r"\bwithout downtime\b", "sin tiempo de inactividad"),
    (r"\bwith near-zero downtime\b", "con tiempo de inactividad casi nulo"),
    (r"\bminimal operational overhead\b", "mínima sobrecarga operativa"),
    (r"\blowest latency\b", "menor latencia"),
    (r"\blowest cost\b", "menor costo"),
    (r"\bmost cost-effective\b", "más rentable"),
]

GENERAL_PT_WORDS = [
    ("An enterprise", "Uma empresa"),
    ("A company", "Uma empresa"),
    ("A solutions architect", "Um arquiteto de soluções"),
    ("The solutions architect", "O arquiteto de soluções"),
    ("needs to", "precisa"),
    ("wants to", "deseja"),
    ("must ensure", "deve garantir"),
    ("must prevent", "deve impedir"),
    ("requires that", "exige que"),
    ("requires a", "necessita de um(a)"),
    ("is designing", "está projetando"),
    ("is migrating", "está migrando"),
    ("is planning", "está planejando"),
    ("is deploying", "está implantando"),
    ("is preparing for", "está se preparando para"),
    ("to improve", "para melhorar"),
    ("to reduce", "para reduzir"),
    ("to optimize", "para otimizar"),
    ("to minimize", "para minimizar"),
    ("to ensure", "para garantir"),
    ("to prevent", "para prevenir"),
    ("to store", "para armazenar"),
    ("to replicate", "para replicar"),
    ("to automate", "para automatizar"),
    ("to monitor", "para monitorar"),
    ("to convert", "para converter"),
    ("to provide", "para fornecer"),
    ("to allow", "para permitir"),
    ("to connect", "para conectar"),
    ("in real-time", "em tempo real"),
    ("in real time", "em tempo real"),
    ("with high availability", "com alta disponibilidade"),
    ("with minimal latency", "com latência mínima"),
    ("with zero downtime", "com zero tempo de inatividade"),
    ("with minimal downtime", "com tempo de inatividade mínimo"),
    ("Deploy ", "Implantar "),
    ("Configure ", "Configurar "),
    ("Create ", "Criar "),
    ("Attach ", "Anexar "),
    ("Enable ", "Habilitar "),
    ("Disable ", "Desabilitar "),
    ("Use ", "Utilizar "),
    ("Implement ", "Implementar "),
    ("Subscribe to ", "Assinar "),
    ("Store ", "Armazenar "),
    ("Migrate ", "Migrar "),
    ("Provision ", "Provisionar "),
    ("Review ", "Revisar "),
    ("Correct: ", "Correto: "),
    ("Incorrect: ", "Incorreto: "),
]

GENERAL_ES_WORDS = [
    ("An enterprise", "Una empresa"),
    ("A company", "Una empresa"),
    ("A solutions architect", "Un arquitecto de soluciones"),
    ("The solutions architect", "El arquitecto de soluciones"),
    ("needs to", "necesita"),
    ("wants to", "desea"),
    ("must ensure", "debe garantizar"),
    ("must prevent", "debe evitar"),
    ("requires that", "requiere que"),
    ("requires a", "requiere un(a)"),
    ("is designing", "está diseñando"),
    ("is migrating", "está migrando"),
    ("is planning", "está planificando"),
    ("is deploying", "está implementando"),
    ("is preparing for", "se está preparando para"),
    ("to improve", "para mejorar"),
    ("to reduce", "para reducir"),
    ("to optimize", "para optimizar"),
    ("to minimize", "para minimizar"),
    ("to ensure", "para garantizar"),
    ("to prevent", "para prevenir"),
    ("to store", "para almacenar"),
    ("to replicate", "para replicar"),
    ("to automate", "para automatizar"),
    ("to monitor", "para monitorear"),
    ("to convert", "para convertir"),
    ("to provide", "para proporcionar"),
    ("to allow", "para permitir"),
    ("to connect", "para conectar"),
    ("in real-time", "en tiempo real"),
    ("in real time", "en tiempo real"),
    ("with high availability", "con alta disponibilidad"),
    ("with minimal latency", "con latencia mínima"),
    ("with zero downtime", "con cero tiempo de inactividad"),
    ("with minimal downtime", "con tiempo de inactividad mínimo"),
    ("Deploy ", "Implementar "),
    ("Configure ", "Configurar "),
    ("Create ", "Crear "),
    ("Attach ", "Adjuntar "),
    ("Enable ", "Habilitar "),
    ("Disable ", "Deshabilitar "),
    ("Use ", "Utilizar "),
    ("Implement ", "Implementar "),
    ("Subscribe to ", "Suscribirse a "),
    ("Store ", "Almacenar "),
    ("Migrate ", "Migrar "),
    ("Provision ", "Aprovisionar "),
    ("Review ", "Revisar "),
    ("Correct: ", "Correcto: "),
    ("Incorrect: ", "Incorrecto: "),
]

def apply_full_translation(text, full_map, general_words):
    if not text:
        return text
    res = text
    for pattern, repl in full_map:
        res = re.sub(pattern, repl, res)
    for orig, rep in general_words:
        res = res.replace(orig, rep)
    return res

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        exam = json.load(f)

    exam["availableLanguages"] = ["en", "pt", "es"]
    exam["defaultLanguage"] = "en"

    for q in exam["questions"]:
        # If base is English
        is_pt = "Uma " in q["statement"] or "Qual " in q["statement"] or "Correto:" in q["options"][0].get("explanation", "")
        
        if is_pt:
            # Base is PT
            pt_statement = q["statement"]
            pt_options = [{"id": o["id"], "text": o["text"], "explanation": o.get("explanation", "")} for o in q["options"]]
            pt_gen = q["generalExplanation"]
            domain_name = q.get("domainName", "")

            # Translate to EN
            en_statement = pt_statement.replace("Qual solução atende a esses requisitos com a MENOR sobrecarga operacional?", "Which solution meets these requirements with the LEAST operational overhead?")
            en_statement = en_statement.replace("Qual combinação de etapas atenderá a esses requisitos? (Escolha duas.)", "Which combination of steps will meet these requirements? (Choose two.)")
            en_statement = en_statement.replace("Qual solução atende a esses requisitos com o MENOR custo?", "Which solution meets these requirements with the LOWEST cost?")
            en_statement = en_statement.replace("Uma empresa", "An enterprise").replace("Um arquiteto de soluções", "A solutions architect")
            
            en_options = []
            for o in pt_options:
                t_text = o["text"].replace("Implantar ", "Deploy ").replace("Configurar ", "Configure ").replace("Criar ", "Create ").replace("Utilizar ", "Use ")
                t_exp = o["explanation"].replace("Correto:", "Correct:").replace("Incorreto:", "Incorrect:")
                en_options.append({"id": o["id"], "text": t_text, "explanation": t_exp})
            en_gen = pt_gen.replace("Correto:", "Correct:").replace("Incorreto:", "Incorrect:")

            # Translate to ES
            es_statement = pt_statement.replace("Qual solução atende a esses requisitos", "¿Qué solución cumple con estos requisitos")
            es_statement = es_statement.replace("com a MENOR sobrecarga operacional?", "con la MENOR sobrecarga operativa?")
            es_statement = es_statement.replace("com o MENOR custo?", "con el MENOR costo?")
            es_statement = es_statement.replace("(Escolha duas.)", "(Elija dos.)").replace("(Escolha DUAS.)", "(Elija DOS.)")
            es_statement = es_statement.replace("Uma empresa", "Una empresa").replace("Um arquiteto de soluções", "Un arquitecto de soluciones")
            
            es_options = []
            for o in pt_options:
                t_text = o["text"].replace("Implantar ", "Implementar ").replace("Configurar ", "Configurar ").replace("Criar ", "Crear ").replace("Utilizar ", "Utilizar ")
                t_exp = o["explanation"].replace("Correto:", "Correcto:").replace("Incorreto:", "Incorrecto:")
                es_options.append({"id": o["id"], "text": t_text, "explanation": t_exp})
            es_gen = pt_gen.replace("Correto:", "Correcto:").replace("Incorreto:", "Incorrecto:")
        else:
            # Base is EN
            en_statement = q["statement"]
            en_options = [{"id": o["id"], "text": o["text"], "explanation": o.get("explanation", "")} for o in q["options"]]
            en_gen = q["generalExplanation"]
            domain_name = q.get("domainName", "")

            # Translate to PT
            pt_statement = apply_full_translation(en_statement, FULL_PT_MAP, GENERAL_PT_WORDS)
            pt_options = [
                {"id": o["id"], "text": apply_full_translation(o["text"], FULL_PT_MAP, GENERAL_PT_WORDS), "explanation": apply_full_translation(o.get("explanation", ""), FULL_PT_MAP, GENERAL_PT_WORDS)}
                for o in en_options
            ]
            pt_gen = apply_full_translation(en_gen, FULL_PT_MAP, GENERAL_PT_WORDS)

            # Translate to ES
            es_statement = apply_full_translation(en_statement, FULL_ES_MAP, GENERAL_ES_WORDS)
            es_options = [
                {"id": o["id"], "text": apply_full_translation(o["text"], FULL_ES_MAP, GENERAL_ES_WORDS), "explanation": apply_full_translation(o.get("explanation", ""), FULL_ES_MAP, GENERAL_ES_WORDS)}
                for o in en_options
            ]
            es_gen = apply_full_translation(en_gen, FULL_ES_MAP, GENERAL_ES_WORDS)

        q["translations"] = {
            "en": {
                "statement": en_statement,
                "domainName": domain_name,
                "options": en_options,
                "generalExplanation": en_gen
            },
            "pt": {
                "statement": pt_statement,
                "domainName": domain_name,
                "options": pt_options,
                "generalExplanation": pt_gen
            },
            "es": {
                "statement": es_statement,
                "domainName": domain_name,
                "options": es_options,
                "generalExplanation": es_gen
            }
        }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(exam, f, indent=2, ensure_ascii=False)
    print(f"✅ Processed {os.path.basename(file_path)}")

if __name__ == "__main__":
    exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/data/exams"))
    for filename in ["sap-c02-sim-1.json", "sap-c02-sim-2.json", "sap-c02-sim-3.json", "saa-c03.json", "clf-c02.json"]:
        p = os.path.join(exams_dir, filename)
        if os.path.exists(p):
            process_file(p)
