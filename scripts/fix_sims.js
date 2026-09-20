const fs = require('fs');

const domains = [
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
      "id": "domain-4-cost-control",
      "name": "Domain 4: Accelerate Workload Migration and Modernization",
      "weightPercentage": 20
    }
];

const files = [
  'sap-c02-sim-4.json',
  'sap-c02-sim-5.json',
  'sap-c02-sim-6.json',
  'sap-c02-sim-7-gaps.json'
];

for (let i = 0; i < files.length; i++) {
  const file = files[i];
  const numMatch = file.match(/sim-(\d+)/);
  const num = numMatch ? numMatch[1] : 'Unknown';
  const path = `/home/romulofreires/projects/aws-exam-simulator/src/data/exams/${file}`;
  let data = JSON.parse(fs.readFileSync(path, 'utf8'));
  
  data.id = `SAP-C02-SIM-${num}${file.includes('gaps') ? '-GAPS' : ''}`;
  data.title = `AWS Certified Solutions Architect - Professional - Mock Exam ${num}${file.includes('gaps') ? ' (Gap Analysis)' : ''}`;
  data.code = "SAP-C02";
  data.category = "Professional";
  
  if (file.includes('gaps')) {
    data.description = "Comprehensive enterprise-level mock exam for AWS SAP-C02 focused on gap analysis: Governance, Cost Optimization, Advanced Analytics, Security and Advanced Hybrid Networking.";
  } else {
    data.description = `Comprehensive enterprise-level mock exam for AWS SAP-C02 featuring complex multi-account, hybrid networking, disaster recovery, and modernization scenarios.`;
  }
  
  data.totalQuestions = data.questions.length;
  data.passingScore = 750;
  data.timeLimitMinutes = 180;
  data.icon = "shield-check";
  data.domains = domains;
  
  delete data.name;

  const { id, title, code, category, description, totalQuestions, timeLimitMinutes, passingScore, icon, domains: doms, questions, ...rest } = data;
  const newData = { id, title, code, category, description, totalQuestions, timeLimitMinutes, passingScore, icon, domains: doms, ...rest, questions };
  
  fs.writeFileSync(path, JSON.stringify(newData, null, 2));
}

console.log("Updated files successfully.");
