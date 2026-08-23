#!/usr/bin/env python3
"""
Validador de Questões SAP-C02 para o AWS Exam Simulator.
Verifica integridade de schema, ids únicos, paridade de gabarito, regras de distratores,
distribuição equilibrada/embaralhada de respostas e cotas de tipos de questão.
"""

import sys
import json
import os
from collections import Counter

VALID_DOMAINS = {
    "domain-1-org-complexity": "Domain 1: Design Solutions for Organizational Complexity",
    "domain-2-new-solutions": "Domain 2: Design for New Solutions",
    "domain-3-continuous-improvement": "Domain 3: Continuous Improvement for Existing Solutions",
    "domain-4-migration-modernization": "Domain 4: Accelerate Workload Migration and Modernization"
}

def validate_question(q, index=0, strict=False):
    errors = []
    warnings = []
    prefix = f"Question #{index+1} (ID: {q.get('id', 'MISSING')})"

    # Required fields
    required_fields = ["id", "examId", "domainId", "statement", "type", "requiredChoices", "options", "correctAnswers", "generalExplanation"]
    for f in required_fields:
        if f not in q or q[f] is None:
            errors.append(f"{prefix}: Campo obrigatório ausente '{f}'.")

    if not q.get("examId", "").startswith("SAP-C02"):
        errors.append(f"{prefix}: examId deve começar com 'SAP-C02', encontrado '{q.get('examId')}'.")

    if q.get("domainId") not in VALID_DOMAINS:
        errors.append(f"{prefix}: domainId inválido '{q.get('domainId')}'. Valores permitidos: {list(VALID_DOMAINS.keys())}")

    q_type = q.get("type")
    req_choices = q.get("requiredChoices", 0)
    correct_ans = q.get("correctAnswers", [])
    options = q.get("options", [])

    if q_type not in ["single", "multiple"]:
        errors.append(f"{prefix}: 'type' deve ser 'single' ou 'multiple'.")

    if q_type == "single" and req_choices != 1:
        errors.append(f"{prefix}: Questões do tipo 'single' devem ter requiredChoices = 1.")
        
    if q_type == "single" and len(options) != 4:
        errors.append(f"{prefix}: Questões do tipo 'single' devem ter exatamente 4 opções de resposta.")

    if q_type == "multiple":
        if req_choices < 2:
            errors.append(f"{prefix}: Questões do tipo 'multiple' devem ter requiredChoices >= 2.")
        
        # Enforce options count for multiple choice
        if req_choices == 2 and len(options) != 5:
            errors.append(f"{prefix}: Questões do tipo 'multiple' com 2 respostas devem ter exatamente 5 opções (A-E).")
        if req_choices == 3 and len(options) != 6:
            errors.append(f"{prefix}: Questões do tipo 'multiple' com 3 respostas devem ter exatamente 6 opções (A-F).")

    if len(correct_ans) != req_choices:
        errors.append(f"{prefix}: Quantidade de correctAnswers ({len(correct_ans)}) diferente de requiredChoices ({req_choices}).")

    if not isinstance(options, list) or len(options) < 4:
        errors.append(f"{prefix}: Deve ter no mínimo 4 opções de resposta.")
    else:
        option_ids = set()
        option_lengths = []
        for idx, opt in enumerate(options):
            opt_id = opt.get("id")
            if not opt_id:
                errors.append(f"{prefix} Opção #{idx+1}: ID da opção ausente.")
            elif opt_id in option_ids:
                errors.append(f"{prefix} Opção '{opt_id}': ID duplicado.")
            option_ids.add(opt_id)

            text = opt.get("text", "").strip()
            if not text:
                errors.append(f"{prefix} Opção '{opt_id}': Texto da opção vazio.")
            else:
                option_lengths.append(len(text))
                words_count = len(text.split())
                if words_count < 20:
                    msg = f"{prefix} Opção '{opt_id}': Texto muito curto ({words_count} palavras). Distratores SAP-C02 devem ter ao menos 20 a 25 palavras."
                    if strict:
                        errors.append(msg)
                    else:
                        warnings.append(msg)

            explanation = opt.get("explanation", "").strip()
            if not explanation:
                errors.append(f"{prefix} Opção '{opt_id}': Explicação da opção vazia.")
            elif len(explanation.split()) < 10:
                msg = f"{prefix} Opção '{opt_id}': Explicação muito rasa ({len(explanation.split())} palavras). Deve justificar tecnicamente o acerto ou erro."
                if strict:
                    errors.append(msg)
                else:
                    warnings.append(msg)

        # Checagem de assimetria de distratores (evita alternativa correta gigante e erradas minúsculas)
        if option_lengths:
            min_len = min(option_lengths)
            max_len = max(option_lengths)
            if max_len > 0 and (min_len / max_len) < 0.25:
                msg = f"{prefix}: Grande assimetria entre alternativas (menor: {min_len} chars, maior: {max_len} chars). Mantenha simetria estrutural para evitar distratores óbvios."
                if strict:
                    errors.append(msg)
                else:
                    warnings.append(msg)

        for ans in correct_ans:
            if ans not in option_ids:
                errors.append(f"{prefix}: Gabarito '{ans}' não existe entre as opções disponíveis ({sorted(list(option_ids))}).")

    if not q.get("generalExplanation", "").strip():
        errors.append(f"{prefix}: 'generalExplanation' não pode ser vazio.")

    return errors, warnings

def check_answer_distribution(questions):
    """
    Verifica se as respostas não estão viciadas em A ou A, B.
    Em um simulado com >= 10 questões, nenhuma opção individual deve concentrar mais de 45% dos gabaritos.
    """
    warnings = []
    errors = []
    
    if len(questions) == 0:
        return errors, warnings

    single_answers = []
    multiple_answer_sets = []

    for q in questions:
        if q.get("type") == "single" and q.get("correctAnswers"):
            single_answers.append(q["correctAnswers"][0])
        elif q.get("type") == "multiple" and q.get("correctAnswers"):
            multiple_answer_sets.append(tuple(sorted(q["correctAnswers"])))

    total_qs = len(questions)
    mult_count = len(multiple_answer_sets)
    mult_pct = (mult_count / total_qs) * 100
    
    if total_qs >= 10 and mult_pct < 15:
         errors.append(f"Cota de Múltipla Escolha violada: O arquivo tem {mult_pct:.1f}% de questões multiple. Exigido: pelo menos 20%.")

    if single_answers and len(questions) >= 10:
        counts = Counter(single_answers)
        total = len(single_answers)
        for opt, cnt in counts.items():
            pct = (cnt / total) * 100
            if pct > 45.0:
                warnings.append(
                    f"⚠️ Vício de gabarito detectado: Opção '{opt}' concentra {pct:.1f}% ({cnt}/{total}) das questões single choice! As alternativas devem ser embaralhadas uniformemente."
                )

    if multiple_answer_sets:
        all_ab = all(s == ("A", "B") for s in multiple_answer_sets)
        if len(multiple_answer_sets) >= 3 and all_ab:
            warnings.append(
                "⚠️ Vício de gabarito múltiplo: 100% das questões de múltipla escolha têm gabarito ['A', 'B']. Embaralhe as posições das alternativas corretas."
            )

    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 validate_questions.py <caminho_para_arquivo.json> [--strict]")
        sys.exit(1)

    strict_mode = "--strict" in sys.argv
    file_path = [arg for arg in sys.argv[1:] if not arg.startswith("--")][0]

    if not os.path.exists(file_path):
        print(f"❌ Arquivo não encontrado: {file_path}")
        sys.exit(1)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        sys.exit(1)

    questions_to_validate = []
    if isinstance(data, dict):
        if "questions" in data and isinstance(data["questions"], list):
            questions_to_validate = data["questions"]
        else:
            # Single question or map of examples
            for k, v in data.items():
                if isinstance(v, dict) and "statement" in v:
                    questions_to_validate.append(v)
                elif isinstance(v, list):
                    questions_to_validate.extend(v)
    elif isinstance(data, list):
        questions_to_validate = data

    print(f"🔍 Validando {len(questions_to_validate)} questão(ões) em {file_path} (Modo estrito: {strict_mode})...")

    all_errors = []
    all_warnings = []
    seen_ids = set()

    for idx, q in enumerate(questions_to_validate):
        q_id = q.get("id")
        if q_id:
            if q_id in seen_ids:
                all_errors.append(f"ID duplicado detectado no arquivo: '{q_id}'")
            seen_ids.add(q_id)
        errs, warns = validate_question(q, idx, strict=strict_mode)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    # Check distribution
    dist_errors, dist_warnings = check_answer_distribution(questions_to_validate)
    all_errors.extend(dist_errors)
    all_warnings.extend(dist_warnings)

    if all_errors:
        print(f"❌ Foram encontrados {len(all_errors)} erro(s):")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        if all_warnings:
            print(f"⚠️ {len(all_warnings)} aviso(s) de qualidade de distratores detectado(s):")
            for w in all_warnings[:10]:
                print(f"  - {w}")
            if len(all_warnings) > 10:
                print(f"  ... e mais {len(all_warnings) - 10} avisos.")
        print("🎉 Todas as questões foram validadas com sucesso e atendem ao padrão SAP-C02!")

if __name__ == "__main__":
    main()
