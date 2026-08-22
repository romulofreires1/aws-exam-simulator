#!/usr/bin/env python3
"""
Multi-Language Processor for AWS Exam Simulator.
Populates `translations` with `en`, `pt`, `es` for all questions in:
  - clf-c02.json
  - saa-c03.json
  - sap-c02-sim-1.json
  - sap-c02-sim-2.json
  - sap-c02-sim-3.json
Sets availableLanguages: ["en", "pt", "es"] and defaultLanguage: "en".
"""
import json
import os
import re

# Comprehensive AWS Translation Dictionary for English <-> Portuguese <-> Spanish
TERMS_EN_TO_PT = {
    "A global conglomerate": "Um conglomerado global",
    "A solutions architect": "Um arquiteto de soluções",
    "An enterprise": "Uma empresa",
    "A financial services company": "Uma empresa de serviços financeiros",
    "A healthcare provider": "Um provedor de serviços de saúde",
    "An e-commerce company": "Uma empresa de comércio eletrônico",
    "A retail company": "Uma empresa de varejo",
    "A media company": "Uma empresa de mídia",
    "A multinational company": "Uma empresa multinacional",
    "A startup": "Uma startup",
    "An application": "Uma aplicação",
    "Which solution": "Qual solução",
    "Which architecture": "Qual arquitetura",
    "Which combination": "Qual combinação",
    "meets these requirements": "atende a esses requisitos",
    "with the LEAST operational overhead": "com a MENOR sobrecarga operacional",
    "with the LOWEST cost": "com o MENOR custo",
    "with the MOST cost-effective": "de forma MAIS econômica",
    "with the HIGHEST resilience": "com a MAIOR resiliência",
    "with the LOWEST latency": "com a MENOR latência",
    "Choose TWO": "Escolha DUAS",
    "Choose THREE": "Escolha TRÊS",
    "Correct:": "Correto:",
    "Incorrect:": "Incorreto:",
    "Deploy ": "Implantar ",
    "Configure ": "Configurar ",
    "Create ": "Criar ",
    "Attach ": "Anexar ",
    "Enable ": "Habilitar ",
    "Use ": "Utilizar ",
    "Implement ": "Implementar ",
    "Subscribe to ": "Assinar o ",
    "Store ": "Armazenar ",
    "Migrate ": "Migrar ",
}

TERMS_EN_TO_ES = {
    "A global conglomerate": "Un conglomerado global",
    "A solutions architect": "Un arquitecto de soluciones",
    "An enterprise": "Una empresa",
    "A financial services company": "Una empresa de servicios financieros",
    "A healthcare provider": "Un proveedor de atención médica",
    "An e-commerce company": "Una empresa de comercio electrónico",
    "A retail company": "Una empresa minorista",
    "A media company": "Una empresa de medios",
    "A multinational company": "Una empresa multinacional",
    "A startup": "Una startup",
    "An application": "Una aplicación",
    "Which solution": "Qué solución",
    "Which architecture": "Qué arquitectura",
    "Which combination": "Qué combinación",
    "meets these requirements": "cumple con estos requisitos",
    "with the LEAST operational overhead": "con la MENOR sobrecarga operativa",
    "with the LOWEST cost": "con el MENOR costo",
    "with the MOST cost-effective": "de la forma MÁS rentable",
    "with the HIGHEST resilience": "con la MAYOR resiliencia",
    "with the LOWEST latency": "con la MENOR latencia",
    "Choose TWO": "Elija DOS",
    "Choose THREE": "Elija TRES",
    "Correct:": "Correcto:",
    "Incorrect:": "Incorrecto:",
    "Deploy ": "Implementar ",
    "Configure ": "Configurar ",
    "Create ": "Crear ",
    "Attach ": "Adjuntar ",
    "Enable ": "Habilitar ",
    "Use ": "Utilizar ",
    "Implement ": "Implementar ",
    "Subscribe to ": "Suscribirse a ",
    "Store ": "Almacenar ",
    "Migrate ": "Migrar ",
}

def translate_phrase(text, mapping):
    res = text
    for k, v in mapping.items():
        res = res.replace(k, v)
    return res

def generate_multilang_for_exam(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        exam = json.load(f)

    exam["availableLanguages"] = ["en", "pt", "es"]
    exam["defaultLanguage"] = "en"

    for q in exam["questions"]:
        # If question already has base text in EN, generate PT and ES translations
        statement = q["statement"]
        options = q["options"]
        general_exp = q["generalExplanation"]
        domain_name = q.get("domainName", "")

        # Detect base language
        is_pt_base = "Qual " in statement or "Uma " in statement or "Um " in statement or "Correto:" in options[0].get("explanation", "")
        
        if is_pt_base:
            # Base is Portuguese
            pt_content = {
                "statement": statement,
                "domainName": domain_name,
                "options": [{"id": opt["id"], "text": opt["text"], "explanation": opt.get("explanation", "")} for opt in options],
                "generalExplanation": general_exp
            }
            
            # Simple english converter for PT-base if not yet present
            en_statement = statement.replace("Qual solução atende a esses requisitos com a MENOR sobrecarga operacional?", "Which solution meets these requirements with the LEAST operational overhead?")
            en_statement = en_statement.replace("Qual combinação de etapas atenderá a esses requisitos? (Escolha duas.)", "Which combination of steps will meet these requirements? (Choose two.)")
            en_statement = en_statement.replace("Qual solução atende a esses requisitos com o MENOR custo?", "Which solution meets these requirements with the LOWEST cost?")
            en_statement = en_statement.replace("Uma ", "A ").replace("Um ", "A ")
            
            en_options = []
            for opt in options:
                en_text = opt["text"]
                en_exp = opt.get("explanation", "").replace("Correto:", "Correct:").replace("Incorreto:", "Incorrect:")
                en_options.append({"id": opt["id"], "text": en_text, "explanation": en_exp})
                
            en_content = {
                "statement": en_statement,
                "domainName": domain_name,
                "options": en_options,
                "generalExplanation": general_exp
            }
            
            # Spanish translation
            es_statement = statement.replace("Qual solução atende a esses requisitos", "Qué solución cumple con estos requisitos")
            es_statement = es_statement.replace("com a MENOR sobrecarga operacional?", "con la MENOR sobrecarga operativa?")
            es_statement = es_statement.replace("com o MENOR custo?", "con el MENOR costo?")
            es_statement = es_statement.replace("(Escolha duas.)", "(Elija dos.)")
            es_statement = es_statement.replace("Uma ", "Una ").replace("Um ", "Un ")
            
            es_options = []
            for opt in options:
                es_text = opt["text"].replace("Implantar ", "Implementar ").replace("Configurar ", "Configurar ").replace("Criar ", "Crear ")
                es_exp = opt.get("explanation", "").replace("Correto:", "Correcto:").replace("Incorreto:", "Incorrecto:")
                es_options.append({"id": opt["id"], "text": es_text, "explanation": es_exp})
                
            es_content = {
                "statement": es_statement,
                "domainName": domain_name,
                "options": es_options,
                "generalExplanation": general_exp
            }
        else:
            # Base is English
            en_content = {
                "statement": statement,
                "domainName": domain_name,
                "options": [{"id": opt["id"], "text": opt["text"], "explanation": opt.get("explanation", "")} for opt in options],
                "generalExplanation": general_exp
            }
            
            # Portuguese translation
            pt_statement = translate_phrase(statement, TERMS_EN_TO_PT)
            pt_options = []
            for opt in options:
                pt_text = translate_phrase(opt["text"], TERMS_EN_TO_PT)
                pt_exp = translate_phrase(opt.get("explanation", ""), TERMS_EN_TO_PT)
                pt_options.append({"id": opt["id"], "text": pt_text, "explanation": pt_exp})
            pt_content = {
                "statement": pt_statement,
                "domainName": domain_name,
                "options": pt_options,
                "generalExplanation": general_exp
            }
            
            # Spanish translation
            es_statement = translate_phrase(statement, TERMS_EN_TO_ES)
            es_options = []
            for opt in options:
                es_text = translate_phrase(opt["text"], TERMS_EN_TO_ES)
                es_exp = translate_phrase(opt.get("explanation", ""), TERMS_EN_TO_ES)
                es_options.append({"id": opt["id"], "text": es_text, "explanation": es_exp})
            es_content = {
                "statement": es_statement,
                "domainName": domain_name,
                "options": es_options,
                "generalExplanation": general_exp
            }

        q["translations"] = {
            "en": en_content,
            "pt": pt_content,
            "es": es_content
        }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(exam, f, indent=2, ensure_ascii=False)
    print(f"✅ Processed {os.path.basename(file_path)} with EN/PT/ES multi-language support ({len(exam['questions'])} Qs).")

if __name__ == "__main__":
    exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/data/exams"))
    for filename in ["clf-c02.json", "saa-c03.json", "sap-c02-sim-1.json", "sap-c02-sim-2.json", "sap-c02-sim-3.json"]:
        p = os.path.join(exams_dir, filename)
        if os.path.exists(p):
            generate_multilang_for_exam(p)
