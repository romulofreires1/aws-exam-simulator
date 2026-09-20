const fs = require('fs');

const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));
let issues = 0;
data.questions.forEach((q, i) => {
  if (!q.correctAnswers) { console.log(`Question ${i} missing correctAnswers`); issues++; }
  if (!q.domainId) { console.log(`Question ${i} missing domainId`); issues++; }
  if (!q.options) { console.log(`Question ${i} missing options`); issues++; }
  if (q.options && q.options.length < 4) { console.log(`Question ${i} options length < 4`); issues++; }
});
console.log("Total issues:", issues);
