const fs = require('fs');
const sims = ['sap-c02-sim-1.json', 'sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json', 'sap-c02-sim-7-gaps.json'];

for (const sim of sims) {
  const data = JSON.parse(fs.readFileSync('./src/data/exams/' + sim, 'utf8'));
  const numQuestions = data.questions ? data.questions.length : 0;
  // 180 minutes for 75 questions -> 2.4 min per question
  const expectedTime = Math.round(numQuestions * 2.4);
  console.log(`${sim}: ${numQuestions} questions -> ${expectedTime} minutes (currently ${data.timeLimitMinutes})`);
}
