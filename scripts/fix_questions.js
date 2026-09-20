const fs = require('fs');

const sims = [
  'sap-c02-sim-4.json',
  'sap-c02-sim-5.json',
  'sap-c02-sim-6.json',
  'sap-c02-sim-7-gaps.json'
];

for (const sim of sims) {
  const path = `./src/data/exams/${sim}`;
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));

  let modified = false;
  for (const q of data.questions) {
    if (!q.statement || !q.options || !q.generalExplanation) {
      // Use Portuguese by default since it's the primary language for these
      const t = q.translations && (q.translations.pt || q.translations.en || Object.values(q.translations)[0]);
      if (t) {
        q.statement = q.statement || t.statement;
        q.options = q.options || t.options;
        q.generalExplanation = q.generalExplanation || t.generalExplanation;
        q.domainName = q.domainName || t.domainName;
        modified = true;
      }
    }
  }

  if (modified) {
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
    console.log(`Fixed ${sim}`);
  }
}
console.log("Done.");
