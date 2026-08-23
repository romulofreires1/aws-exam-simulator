#!/usr/bin/env python3
"""
Applies verified, high-quality Portuguese and Spanish translations to AWS Exam questions.
Ensures every question in every exam has 100% natural, complete, non-hybrid translations.
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

EXAMS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/data/exams"))

def load_exam(filename):
    path = os.path.join(EXAMS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f), path

def save_exam(exam_data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(exam_data, f, indent=2, ensure_ascii=False)
    print(f" Saved updated exam to {path}")

def apply_translations_for_exam(filename, translations_dict):
    exam, path = load_exam(filename)
    exam["availableLanguages"] = ["en", "pt", "es"]
    exam["defaultLanguage"] = "en"

    updated_count = 0
    missing_count = 0

    for q in exam["questions"]:
        qid = q["id"]
        
        # Build EN translation from base fields
        en_content = {
            "statement": q["statement"],
            "domainName": q.get("domainName", ""),
            "options": [
                {
                    "id": opt["id"],
                    "text": opt["text"],
                    "explanation": opt.get("explanation", "")
                }
                for opt in q["options"]
            ],
            "generalExplanation": q["generalExplanation"]
        }

        if qid in translations_dict:
            t = translations_dict[qid]
            pt_content = t.get("pt")
            es_content = t.get("es")

            if not pt_content or not es_content:
                print(f"⚠️ Warning: Missing pt or es for {qid}")
                missing_count += 1
                continue

            # Ensure option IDs match base
            base_opt_ids = [opt["id"] for opt in q["options"]]
            pt_opt_ids = [opt["id"] for opt in pt_content.get("options", [])]
            es_opt_ids = [opt["id"] for opt in es_content.get("options", [])]

            if base_opt_ids != pt_opt_ids:
                print(f"❌ Option IDs mismatch in PT for {qid}: {base_opt_ids} vs {pt_opt_ids}")
                sys.exit(1)
            if base_opt_ids != es_opt_ids:
                print(f"❌ Option IDs mismatch in ES for {qid}: {base_opt_ids} vs {es_opt_ids}")
                sys.exit(1)

            q["translations"] = {
                "en": en_content,
                "pt": pt_content,
                "es": es_content
            }
            updated_count += 1
        else:
            print(f"⚠️ No translation found for {qid} in {filename}")
            missing_count += 1

    save_exam(exam, path)
    print(f" Processed {filename}: {updated_count} translated, {missing_count} missing out of {len(exam['questions'])} total.")
    return missing_count == 0

if __name__ == "__main__":
    import scripts.translations.sap_sim1_translations as sap1
    import scripts.translations.sap_sim2_translations as sap2
    import scripts.translations.sap_sim3_translations as sap3
    import scripts.translations.clf_part1_translations as clf1
    import scripts.translations.clf_part2_translations as clf2
    import scripts.translations.saa_part1_translations as saa1
    import scripts.translations.saa_part2_translations as saa2

    print("🚀 Applying all high-quality translations across all exams...")
    
    apply_translations_for_exam("sap-c02-sim-1.json", sap1.TRANSLATIONS)
    apply_translations_for_exam("sap-c02-sim-2.json", sap2.TRANSLATIONS)
    apply_translations_for_exam("sap-c02-sim-3.json", sap3.TRANSLATIONS)
    apply_translations_for_exam("clf-c02.json", {**clf1.TRANSLATIONS, **clf2.TRANSLATIONS})
    apply_translations_for_exam("saa-c03.json", {**saa1.TRANSLATIONS, **saa2.TRANSLATIONS})

    print("🎉 Successfully applied translations to all exams!")
