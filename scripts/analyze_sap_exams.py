import json
import glob
import os

files = glob.glob('src/data/exams/sap-c02*.json')
files.sort()

for fpath in files:
    with open(fpath, 'r') as f:
        data = json.load(f)
    
    questions = data.get('questions', [])
    num_q = len(questions)
    
    # Calculate proportional time based on 75 questions = 210 mins
    # time = (num_q / 75) * 210
    target_time = round((num_q / 75) * 210)
    
    # Analyze text length
    statement_words = []
    option_words = []
    for q in questions:
        statement_words.append(len(q.get('statement', '').split()))
        for opt in q.get('options', []):
            option_words.append(len(opt.get('text', '').split()))
            
    avg_stmt = sum(statement_words) / len(statement_words) if statement_words else 0
    avg_opt = sum(option_words) / len(option_words) if option_words else 0
    
    short_options = sum(1 for w in option_words if w < 10)
    
    print(f"--- {os.path.basename(fpath)} ---")
    print(f"Questions: {num_q}")
    print(f"Current Time: {data.get('timeLimitMinutes')} mins | Target Time (210m/75q): {target_time} mins")
    print(f"Avg Statement Words: {avg_stmt:.1f} (SAP target: >50)")
    print(f"Avg Option Words: {avg_opt:.1f} (SAP target: >20)")
    print(f"Short Options (<10 words): {short_options}")
    
    # Auto-adjust time
    if data.get('timeLimitMinutes') != target_time:
        data['timeLimitMinutes'] = target_time
        with open(fpath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("-> [FIXED] Updated timeLimitMinutes")
    print()

