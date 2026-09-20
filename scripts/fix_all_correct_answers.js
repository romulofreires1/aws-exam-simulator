const fs = require('fs');

const sims = ['sap-c02-sim-1.json', 'sap-c02-sim-2.json', 'sap-c02-sim-3.json', 'sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json'];

let totalFixed = 0;
for (const sim of sims) {
  const path = `./src/data/exams/${sim}`;
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));
  let modified = false;

  for (const q of (data.questions || [])) {
    let correct = q.correctAnswers;
    if (!correct) {
      if (q.correctOptions) correct = q.correctOptions;
      else if (q.correctOptionId) correct = Array.isArray(q.correctOptionId) ? q.correctOptionId : [q.correctOptionId];
      else if (q.correctAnswer) correct = Array.isArray(q.correctAnswer) ? q.correctAnswer : [q.correctAnswer];
      else if (q.correctOptionIds) correct = q.correctOptionIds;
      else {
        console.log(`Could not find correct answers for question ${q.id} in ${sim}`);
        continue;
      }
      
      q.correctAnswers = correct;
      delete q.correctOptions;
      delete q.correctOptionId;
      delete q.correctAnswer;
      delete q.correctOptionIds;
      modified = true;
      totalFixed++;
    }
  }

  if (modified) {
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
    console.log(`Fixed correct answers in ${sim}`);
  }
}
console.log(`Total questions fixed: ${totalFixed}`);
