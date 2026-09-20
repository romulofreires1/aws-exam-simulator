const fs = require('fs');

const sims = ['sap-c02-sim-1.json', 'sap-c02-sim-2.json', 'sap-c02-sim-3.json', 'sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json'];

for (const sim of sims) {
  const path = `./src/data/exams/${sim}`;
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));
  let modified = false;

  for (let i = 0; i < data.questions.length; i++) {
    const q = data.questions[i];
    if (q.question && !q.statement) {
      modified = true;
      
      // Determine base language, prefer 'pt'
      const baseLang = 'pt';
      
      // 1. Translations
      q.translations = {};
      const langs = Object.keys(q.question || {});
      for (const lang of langs) {
        q.translations[lang] = {
          domainName: q.domain || "",
          statement: q.question[lang] || "",
          generalExplanation: (q.explanation && q.explanation[lang]) ? q.explanation[lang] : "",
          options: []
        };
      }
      
      // Options
      const baseOptions = [];
      for (const opt of q.options) {
        // Base option
        baseOptions.push({
          id: opt.id,
          text: opt.text[baseLang] || opt.text['en'] || "",
          explanation: opt.explanation ? (opt.explanation[baseLang] || opt.explanation['en']) : undefined
        });
        
        // Translation options
        for (const lang of langs) {
          q.translations[lang].options.push({
            id: opt.id,
            text: opt.text[lang] || "",
            explanation: opt.explanation ? opt.explanation[lang] : undefined
          });
        }
      }
      
      // Base fields
      q.statement = q.question[baseLang] || q.question['en'] || "";
      q.generalExplanation = (q.explanation && (q.explanation[baseLang] || q.explanation['en'])) || "";
      q.domainName = q.domain || "Domain 2: Design for New Solutions";
      q.domainId = q.domainId || "domain-2-new-solutions";
      q.examId = q.examId || "SAP-C02";
      q.services = q.tags || [];
      q.requiredChoices = q.type === 'multiple' ? (q.correctAnswers ? q.correctAnswers.length : 2) : 1;
      q.options = baseOptions;
      
      // Clean up old fields
      delete q.question;
      delete q.domain;
      delete q.tags;
      delete q.explanation;
    }
  }

  if (modified) {
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
    console.log(`Normalized ${sim}`);
  }
}
console.log("Done.");
