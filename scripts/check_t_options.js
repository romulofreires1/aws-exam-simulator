const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));

let issues = 0;
data.questions.forEach((q, i) => {
  if (q.translations) {
    for (const lang of Object.keys(q.translations)) {
      const t = q.translations[lang];
      if (t.options && !Array.isArray(t.options)) {
        console.log(`Q${i} [${lang}] options is not an array:`, typeof t.options);
        issues++;
      }
    }
  }
});
console.log("SIM 5 translations options array issues:", issues);
