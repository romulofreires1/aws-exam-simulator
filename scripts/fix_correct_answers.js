const fs = require('fs');

const sims = ['sap-c02-sim-1.json', 'sap-c02-sim-2.json', 'sap-c02-sim-3.json', 'sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json'];

for (const sim of sims) {
  const path = `./src/data/exams/${sim}`;
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));
  let modified = false;

  for (const q of data.questions) {
    if (!q.correctAnswers && q.correctOptions) {
      q.correctAnswers = q.correctOptions;
      delete q.correctOptions;
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
    console.log(`Fixed correctAnswers in ${sim}`);
  }
}
