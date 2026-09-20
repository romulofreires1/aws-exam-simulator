const fs = require('fs');

const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));
data.questions.forEach((q, i) => {
  if (q.services && !Array.isArray(q.services)) {
    console.log(`Q${i} services is not an array:`, q.services);
  }
});
console.log("Done checking services.");
