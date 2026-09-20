const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));

let issues = 0;
data.questions.forEach((q, i) => {
  if (!Array.isArray(q.options)) {
    console.log(`Q${i} options is not an array:`, q.options);
    issues++;
  }
});
console.log("SIM 5 options array issues:", issues);
