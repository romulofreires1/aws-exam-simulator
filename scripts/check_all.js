const fs = require('fs');

const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));

let issues = 0;
data.questions.forEach((q, i) => {
  if (!q.correctAnswers) { console.log(`Q${i} missing correctAnswers`); issues++; }
  if (!q.statement) { console.log(`Q${i} missing statement`); issues++; }
  if (!q.options || q.options.length === 0) { console.log(`Q${i} missing options`); issues++; }
  if (q.options && q.options.length > 0 && !q.options[0].id) { console.log(`Q${i} options missing id`); issues++; }
});
console.log("SIM 5 Issues:", issues);

const data6 = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-6.json', 'utf8'));
issues = 0;
data6.questions.forEach((q, i) => {
  if (!q.correctAnswers) { console.log(`Q${i} missing correctAnswers`); issues++; }
  if (!q.statement) { console.log(`Q${i} missing statement`); issues++; }
});
console.log("SIM 6 Issues:", issues);
