const fs = require('fs');
const sims = ['sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json', 'sap-c02-sim-7-gaps.json'];

for (const sim of sims) {
  const data = JSON.parse(fs.readFileSync('./src/data/exams/' + sim, 'utf8'));
  for (let i = 0; i < data.questions.length; i++) {
    const q = data.questions[i];
    if (q.question && !q.statement) {
      console.log(`${sim} - Question ${i} has bad schema: ${q.id}`);
    }
  }
}
