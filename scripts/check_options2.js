const fs = require('fs');
const sims = ['sap-c02-sim-4.json', 'sap-c02-sim-6.json', 'sap-c02-sim-7-gaps.json'];
for (const sim of sims) {
  const data = JSON.parse(fs.readFileSync('./src/data/exams/' + sim, 'utf8'));
  for (const q of (data.questions || [])) {
    if (q.options && !Array.isArray(q.options)) {
      console.log(`${sim} - Question ${q.id} options is not array. Type: ${typeof q.options}`);
    }
  }
}
