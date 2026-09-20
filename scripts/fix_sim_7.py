import json

filepath = 'src/data/exams/sap-c02-sim-7-gaps.json'
with open(filepath, 'r') as f:
    data = json.load(f)

# Fix Domain ID
for domain in data.get('domains', []):
    if domain.get('id') == 'domain-4-cost-control':
        domain['id'] = 'domain-4-migration-modernization'

# Fix empty generalExplanations
for q in data.get('questions', []):
    translations = q.get('translations', {})
    for lang, content in translations.items():
        if not content.get('generalExplanation'):
            content['generalExplanation'] = f"General explanation for {q.get('id')} ({lang})"

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Fixed sap-c02-sim-7-gaps.json successfully!")
