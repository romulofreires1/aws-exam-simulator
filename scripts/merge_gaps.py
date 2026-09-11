import json
import os
import glob

TEMP_DIR = "src/data/exams/temp"
EXAMS_DIR = "src/data/exams"

filepath = os.path.join(EXAMS_DIR, "sap-c02-sim-7-gaps.json")

# Initialize the file if it doesn't exist
if not os.path.exists(filepath):
    data = {
        "id": "sap-c02-sim-7-gaps",
        "name": "AWS Certified Solutions Architect - Professional (Mock 7 - Gap Analysis)",
        "description": "Simulado focado nos gaps identificados: Governança, Cost Optimization, Advanced Analytics, Security e Advanced Hybrid Networking.",
        "passingScore": 75,
        "timeLimitMinutes": 180,
        "questions": []
    }
else:
    with open(filepath, "r") as f:
        data = json.load(f)
        
# Find all batch files for sim 7
batch_files = glob.glob(os.path.join(TEMP_DIR, "sim7_gap_batch*.json"))

for batch_file in batch_files:
    try:
        with open(batch_file, "r") as f:
            batch_data = json.load(f)
            if isinstance(batch_data, list):
                data["questions"].extend(batch_data)
                print(f"Merged {len(batch_data)} questions from {batch_file}")
            # Remove the batch file after successful merge
        os.remove(batch_file)
    except Exception as e:
        print(f"Failed to merge {batch_file}: {e}")
        
# Save the updated main file
with open(filepath, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Simulado 7 (Gaps) now has {len(data['questions'])} questions.")
