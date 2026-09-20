const fs = require('fs');
const path = require('path');

const sims = ['sap-c02-sim-1.json', 'sap-c02-sim-2.json', 'sap-c02-sim-3.json', 'sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json'];

for (const sim of sims) {
  const filePath = path.join(__dirname, '../src/data/exams', sim);
  if (!fs.existsSync(filePath)) continue;
  
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  let modified = false;

  for (const q of (data.questions || [])) {
    // 0.2 Fix options that are arrays of strings!
    if (Array.isArray(q.options)) {
      q.options = q.options.map((opt, idx) => {
        if (typeof opt === 'string') {
          modified = true;
          return {
            id: String.fromCharCode(97 + idx), // a, b, c, d
            text: opt
          };
        }
        return opt;
      });
    }

    if (q.translations) {
      for (const lang of Object.keys(q.translations)) {
        if (Array.isArray(q.translations[lang].options)) {
          q.translations[lang].options = q.translations[lang].options.map((opt, idx) => {
            if (typeof opt === 'string') {
              modified = true;
              return {
                id: String.fromCharCode(97 + idx), // a, b, c, d
                text: opt
              };
            }
            return opt;
          });
        }
      }
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log(`Deep normalized 3 ${sim}`);
  }
}
