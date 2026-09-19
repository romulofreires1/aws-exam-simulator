import os
import json
import argparse
import asyncio
try:
    import openai
except ImportError:
    print("Please install openai: pip install openai")
    exit(1)

from pydantic import BaseModel, Field
from typing import List, Literal, Optional

# --- Define the JSON Schema for the output using Pydantic ---
class Option(BaseModel):
    id: str
    text: str = Field(description="Must be detailed, at least 15-25 words. Describe a complete architectural solution step.")
    explanation: str = Field(description="Must be a deep technical explanation (30+ words). Explain why it succeeds or fails based on AWS limitations.")

class QuestionDraft(BaseModel):
    id: str
    type: Literal["single", "multiple"]
    requiredChoices: int
    statement: str = Field(description="Complex enterprise scenario (2-4 paragraphs) with conflicting constraints.")
    options: List[Option]
    correctAnswers: List[str]
    generalExplanation: str = Field(description="Synthesize the recommended architecture.")
    referenceUrl: str = Field(description="A valid AWS documentation URL.")
    services: List[str] = Field(description="List of AWS services involved.")
    difficulty: Literal["medium", "hard"]

# Prompt templates
SYSTEM_PROMPT = """You are an Expert AWS Certified Solutions Architect - Professional (SAP-C02) exam creator.
Your goal is to write highly complex, realistic, and completely accurate exam questions.
1. The scenario must be 2-4 paragraphs long, detailing enterprise constraints (cost, migration, RTO/RPO, legacy systems).
2. Options must be LONG and DETAILED (20+ words each). No short answers like 'Use Amazon S3'.
3. Explanations must be highly technical, explaining exactly why an option fails or succeeds based on AWS service quotas, limits, or specific architectural trade-offs.
4. Correct answers must NOT always be A or B. Randomize the correct answer logically.
"""

REFINER_PROMPT = """You are an AWS Exam Quality Auditor. Review the generated question draft.
1. Ensure the scenario is Professional level (SAP-C02), not Associate level.
2. Ensure options are mutually exclusive and highly detailed.
3. Fix any hallucinated AWS services (e.g., 'AWS DataSync Gateway' does not exist).
4. Verify the referenceUrl is a plausible official AWS documentation link.
5. If the question type is 'multiple', ensure 'requiredChoices' matches the number of 'correctAnswers', and that the combinations make architectural sense.
Output the FINAL, refined JSON structure perfectly.
"""

async def generate_question(domain_name: str, q_type: str, api_key: str):
    client = openai.AsyncOpenAI(api_key=api_key)
    
    print(f"🔄 [Step 1] Generating draft for {domain_name} ({q_type} choice)...")
    draft_completion = await client.beta.chat.completions.parse(
        model="gpt-4o", # Can be overridden by user
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Create a new {q_type} choice question for {domain_name}."}
        ],
        response_format=QuestionDraft,
    )
    draft = draft_completion.choices[0].message.parsed
    
    print(f"🔍 [Step 2] Refining and auditing the question...")
    refiner_completion = await client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": REFINER_PROMPT},
            {"role": "user", "content": f"Refine this draft to SAP-C02 perfection:\n\n{draft.model_dump_json(indent=2)}"}
        ],
        response_format=QuestionDraft,
    )
    final_question = refiner_completion.choices[0].message.parsed
    return final_question

def main():
    parser = argparse.ArgumentParser(description="Automated LLM Generator for AWS SAP-C02")
    parser.add_argument("--domain", type=str, default="Domain 1: Design Solutions for Organizational Complexity", help="Target domain")
    parser.add_argument("--type", choices=["single", "multiple"], default="single", help="Question type")
    parser.add_argument("--count", type=int, default=1, help="Number of questions to generate")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable is missing.")
        print("Please run: export OPENAI_API_KEY='your-key'")
        exit(1)

    async def run_batch():
        questions = []
        for i in range(args.count):
            print(f"\n--- Generating Question {i+1}/{args.count} ---")
            q = await generate_question(args.domain, args.type, api_key)
            questions.append(q.model_dump())
        
        output_file = "generated_questions.json"
        with open(output_file, "w") as f:
            json.dump(questions, f, indent=2)
        print(f"\n✅ Successfully saved {args.count} questions to {output_file}")

    asyncio.run(run_batch())

if __name__ == "__main__":
    main()
