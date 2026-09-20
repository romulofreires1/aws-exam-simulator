const fs = require('fs');
const sims = ['sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json', 'sap-c02-sim-7-gaps.json'];

for (const sim of sims) {
  const path = `./src/data/exams/${sim}`;
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));
  
  if (data.timeLimitMinutes === 180 && data.questions.length === 25) {
    data.timeLimitMinutes = 73;
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
    console.log(`Updated ${sim} to 73 minutes.`);
  }
}
