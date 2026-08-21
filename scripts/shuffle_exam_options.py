#!/usr/bin/env python3
"""
Script para embaralhar as opções de resposta em todos os bancos de questões JSON.
Garante distribuição uniforme dos gabaritos entre A, B, C, D (e E, F).
"""

import json
import glob
import random
import os

LETTERS = ["A", "B", "C", "D", "E", "F"]

def shuffle_question_options(q, rng):
    old_correct = set(q.get("correctAnswers", []))
    old_options = q.get("options", [])
    if not old_options:
        return q

    # Marca quais opções eram corretas
    marked_options = []
    for opt in old_options:
        was_correct = opt["id"] in old_correct
        marked_options.append({
            "text": opt["text"],
            "explanation": opt.get("explanation", ""),
            "was_correct": was_correct
        })

    # Embaralha as opções
    rng.shuffle(marked_options)

    # Reatribui letras e descobre os novos gabaritos
    new_options = []
    new_correct = []

    for idx, opt_data in enumerate(marked_options):
        new_id = LETTERS[idx]
        new_options.append({
            "id": new_id,
            "text": opt_data["text"],
            "explanation": opt_data["explanation"]
        })
        if opt_data["was_correct"]:
            new_correct.append(new_id)

    q["options"] = new_options
    q["correctAnswers"] = sorted(new_correct)
    return q

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "questions" not in data or not isinstance(data["questions"], list):
        print(f"Pugando {file_path} (sem lista de questions)")
        return

    # Usamos uma seed fixa por arquivo para garantir reprodutibilidade
    seed = sum(ord(c) for c in os.path.basename(file_path)) + 42
    rng = random.Random(seed)

    questions = data["questions"]
    for q in questions:
        shuffle_question_options(q, rng)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Estatísticas de distribuição
    single_counts = {}
    multi_counts = {}
    for q in questions:
        if q.get("type") == "single":
            ans = q["correctAnswers"][0]
            single_counts[ans] = single_counts.get(ans, 0) + 1
        else:
            ans = tuple(q["correctAnswers"])
            multi_counts[ans] = multi_counts.get(ans, 0) + 1

    print(f"✅ {file_path}: {len(questions)} questões")
    print(f"   Single choice distribution: {single_counts}")
    if multi_counts:
        print(f"   Multiple choice distribution: {multi_counts}")

def main():
    target_files = sorted(glob.glob("src/data/exams/*.json"))
    for f in target_files:
        if "_template" in f:
            continue
        process_file(f)

if __name__ == "__main__":
    main()
