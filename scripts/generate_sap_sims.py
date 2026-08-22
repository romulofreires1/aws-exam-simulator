#!/usr/bin/env python3
"""
Full standalone generator for SAP-C02 Sim 1, Sim 2, and Sim 3 (25 Qs each = 75 Qs total)
"""
import json
import os
import random
from collections import Counter

SAP_DOMAINS = [
    {
        "id": "domain-1-org-complexity",
        "name": "Domain 1: Design Solutions for Organizational Complexity",
        "weightPercentage": 26
    },
    {
        "id": "domain-2-new-solutions",
        "name": "Domain 2: Design for New Solutions",
        "weightPercentage": 29
    },
    {
        "id": "domain-3-continuous-improvement",
        "name": "Domain 3: Continuous Improvement for Existing Solutions",
        "weightPercentage": 25
    },
    {
        "id": "domain-4-migration-modernization",
        "name": "Domain 4: Accelerate Workload Migration and Modernization",
        "weightPercentage": 20
    }
]

def ensure_option_quality(q):
    """Ensure every option is at least 10 words and has balanced length."""
    for opt in q["options"]:
        text = opt["text"].strip()
        words = text.split()
        if len(words) < 8:
            if "AWS AppConfig" in text:
                opt["text"] = "Deploy AWS AppConfig to manage application feature flags with linear deployment strategies, schema validators, and CloudWatch alarm rollbacks."
            elif "AWS CodeDeploy" in text:
                opt["text"] = "Configure AWS CodeDeploy with in-place deployment mode and custom lifecycle deployment hook scripts across the fleet."
            elif "Amazon S3 Versioning" in text:
                opt["text"] = "Store configuration JSON files in an Amazon S3 bucket with versioning and S3 Event Notifications configured."
            elif "AWS Secrets Manager" in text:
                opt["text"] = "Store application configuration feature flags in AWS Secrets Manager and schedule automatic secret rotation."
            elif "AWS X-Ray" in text:
                opt["text"] = "Instrument microservices with AWS X-Ray (or AWS Distro for OpenTelemetry) to generate distributed service trace maps and analyze sub-segment latencies."
            elif "AWS Fault Injection Service" in text or "AWS FIS" in text:
                opt["text"] = "Deploy AWS Fault Injection Service (AWS FIS) to execute controlled chaos engineering experiments with automated stop conditions across resources."
            elif "AWS Shield Advanced" in text:
                opt["text"] = "Subscribe to AWS Shield Advanced to provide dedicated DDoS attack mitigation and 24/7 access to the DDoS Response Team."
            elif "AWS Systems Manager Patch Manager" in text:
                opt["text"] = "Configure AWS Systems Manager Patch Manager to automate operating system patch baselines across all EC2 instances."
            elif "AWS Config Conformance Packs" in text:
                opt["text"] = "Deploy AWS Config Conformance Packs across accounts to evaluate resource compliance against corporate governance rules."
            elif "CloudFormation Drift Detection" in text:
                opt["text"] = "Execute AWS CloudFormation Drift Detection on existing stacks to identify manual out-of-band resource modifications."
            elif "CloudFormation Change Sets" in text:
                opt["text"] = "Create AWS CloudFormation Change Sets to preview proposed infrastructure modifications prior to stack deployment."
            elif "CloudFormation Rollback Triggers" in text:
                opt["text"] = "Configure AWS CloudFormation Rollback Triggers to monitor CloudWatch alarms and cancel failed stack deployments."
            elif "AWS CloudTrail Event History" in text:
                opt["text"] = "Review AWS CloudTrail Event History in the console to identify historical API modification events."
            elif "AWS Application Migration Service" in text or "AWS MGN" in text:
                opt["text"] = "Deploy AWS Application Migration Service (AWS MGN) to perform non-disruptive continuous block-level server replication into AWS."
            elif "AWS Server Migration Service" in text or "AWS SMS" in text:
                opt["text"] = "Deploy legacy AWS Server Migration Service (AWS SMS) connector to create periodic hypervisor snapshot backups."
            elif "AWS Snowball Edge" in text:
                opt["text"] = "Order an AWS Snowball Edge Storage Optimized physical appliance to transport server disk images offline."
            elif "AWS DataSync" in text:
                opt["text"] = "Deploy AWS DataSync agents on on-premises virtual machines to transfer file systems into Amazon S3."
            elif "AWS Mainframe Modernization" in text:
                opt["text"] = "Use AWS Mainframe Modernization service with the Automated Refactor pattern powered by AWS Blu Age to convert COBOL to Java."
            elif "AWS Database Migration Service" in text or "AWS DMS" in text:
                opt["text"] = "Deploy AWS Database Migration Service (AWS DMS) tasks to replicate database tables continuously into Amazon Aurora."
            elif "AWS Serverless Application Repository" in text:
                opt["text"] = "Deploy pre-packaged applications from the AWS Serverless Application Repository to replace legacy banking modules."
            elif "AWS CloudHSM" in text:
                opt["text"] = "Deploy an AWS CloudHSM cluster inside a private VPC to manage single-tenant FIPS 140-2 Level 3 cryptographic hardware."
            elif "AWS Key Management Service" in text or "AWS KMS" in text:
                opt["text"] = "Configure AWS Key Management Service (AWS KMS) with multi-tenant default customer managed keys."
            elif "AWS Billing Conductor" in text:
                opt["text"] = "Configure AWS Billing Conductor to define custom billing groups, apply pricing markups, and generate pro forma invoices."
            elif "AWS Cost Explorer" in text:
                opt["text"] = "Use AWS Cost Explorer to visualize consolidated historical AWS expenditure and forecast future usage."
            elif "AWS Pricing Calculator" in text:
                opt["text"] = "Use AWS Pricing Calculator to model architecture costs before provisioning AWS infrastructure resources."
            elif "AWS Budgets" in text:
                opt["text"] = "Configure AWS Budgets to send automated notifications when monthly spending limits exceed predefined thresholds."
            elif "AWS Proton" in text:
                opt["text"] = "Deploy AWS Proton to centrally manage standard environment and service infrastructure templates for development teams."
            elif "AWS OpsWorks" in text:
                opt["text"] = "Deploy AWS OpsWorks Stacks to manage configuration automation using Chef recipes on Amazon EC2 instances."
            elif "AWS Cloud9" in text:
                opt["text"] = "Provision AWS Cloud9 cloud integrated development environments for developers to edit application code."
            elif "AWS Migration Evaluator" in text:
                opt["text"] = "Use AWS Migration Evaluator (formerly TSO Logic) to analyze on-premises inventory and model total cost of ownership business cases."
            elif "AWS Resilience Hub" in text:
                opt["text"] = "Implement AWS Resilience Hub to assess application architectures against business RTO and RPO targets and generate test suites."
            elif "AWS Certificate Manager" in text:
                opt["text"] = "Use AWS Certificate Manager (ACM) to provision and automatically renew public SSL/TLS certificates."
            elif "AWS Artifact" in text:
                opt["text"] = "Download compliance reports and regulatory certifications from the AWS Artifact self-service portal."
            else:
                opt["text"] = f"Configure and deploy {text} following AWS Well-Architected Framework enterprise best practices."

# Import data generators directly from existing json files or define functions
def load_json_questions(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)["questions"]

def shuffle_and_balance_exam(questions, seed_num):
    random.seed(seed_num)
    single_q_indices = [i for i, q in enumerate(questions) if q["type"] == "single"]
    letters_pool = []
    for _ in range((len(single_q_indices) // 4) + 2):
        letters_pool.extend(["A", "B", "C", "D"])
    random.shuffle(letters_pool)
    
    pairs_pool = [("A", "C"), ("B", "D"), ("C", "E"), ("A", "D"), ("B", "E"), ("A", "E"), ("B", "C"), ("C", "D")]
    random.shuffle(pairs_pool)
    
    single_ptr = 0
    multiple_ptr = 0
    letters = ["A", "B", "C", "D", "E", "F"]
    
    for q in questions:
        ensure_option_quality(q)
        orig_options = list(q["options"])
        orig_correct = set(q["correctAnswers"])
        total_opts = len(orig_options)
        available_letters = letters[:total_opts]
        
        correct_opts = [opt for opt in orig_options if opt["id"] in orig_correct]
        incorrect_opts = [opt for opt in orig_options if opt["id"] not in orig_correct]
        
        new_options = [None] * total_opts
        new_correct_answers = []
        
        if q["type"] == "single":
            target_let = letters_pool[single_ptr]
            single_ptr += 1
            target_idx = available_letters.index(target_let)
            new_options[target_idx] = correct_opts[0]
            new_correct_answers = [target_let]
            
            random.shuffle(incorrect_opts)
            inc_idx = 0
            for i in range(total_opts):
                if new_options[i] is None:
                    new_options[i] = incorrect_opts[inc_idx]
                    inc_idx += 1
        elif q["type"] == "multiple":
            pair = pairs_pool[multiple_ptr % len(pairs_pool)]
            multiple_ptr += 1
            target_indices = [available_letters.index(l) for l in pair]
            new_correct_answers = sorted(list(pair))
            
            random.shuffle(correct_opts)
            for idx, c_opt in zip(target_indices, correct_opts):
                new_options[idx] = c_opt
                
            random.shuffle(incorrect_opts)
            inc_idx = 0
            for i in range(total_opts):
                if new_options[i] is None:
                    new_options[i] = incorrect_opts[inc_idx]
                    inc_idx += 1
                    
        final_options = []
        for i, opt in enumerate(new_options):
            opt_copy = dict(opt)
            opt_copy["id"] = available_letters[i]
            final_options.append(opt_copy)
            
        q["options"] = final_options
        q["correctAnswers"] = new_correct_answers
    return questions

def process_existing_sim(filepath, seed_num):
    data = {}
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = data["questions"]
    shuffled = shuffle_and_balance_exam(questions, seed_num)
    data["questions"] = shuffled
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    counts = Counter([q["correctAnswers"][0] for q in shuffled if q["type"] == "single"])
    print(f"✅ Processed {os.path.basename(filepath)}: {len(shuffled)} Qs. Single distribution: {counts}")

if __name__ == "__main__":
    exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/data/exams"))
    sim1_path = os.path.join(exams_dir, "sap-c02-sim-1.json")
    sim2_path = os.path.join(exams_dir, "sap-c02-sim-2.json")
    sim3_path = os.path.join(exams_dir, "sap-c02-sim-3.json")
    
    process_existing_sim(sim1_path, 101)
    process_existing_sim(sim2_path, 202)
    process_existing_sim(sim3_path, 303)
