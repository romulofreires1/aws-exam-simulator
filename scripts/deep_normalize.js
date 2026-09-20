const fs = require('fs');
const path = require('path');

const sims = ['sap-c02-sim-1.json', 'sap-c02-sim-2.json', 'sap-c02-sim-3.json', 'sap-c02-sim-4.json', 'sap-c02-sim-5.json', 'sap-c02-sim-6.json'];

let totalFixed = 0;

for (const sim of sims) {
  const filePath = path.join(__dirname, '../src/data/exams', sim);
  if (!fs.existsSync(filePath)) continue;
  
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  let modified = false;

  for (const q of (data.questions || [])) {
    // 1. Fix correctAnswers from options array (isCorrect: true)
    if (!q.correctAnswers) {
      // Find options that have isCorrect: true
      const correctIds = (q.options || [])
        .filter(opt => opt.isCorrect === true || opt.isCorrect === "true")
        .map(opt => opt.id);
        
      if (correctIds.length > 0) {
        q.correctAnswers = correctIds;
        modified = true;
      }
    }

    // 2. Fix correctAnswers from fallback keys
    if (!q.correctAnswers) {
      let correct = null;
      if (q.correctOptions) correct = q.correctOptions;
      else if (q.correctOptionId) correct = Array.isArray(q.correctOptionId) ? q.correctOptionId : [q.correctOptionId];
      else if (q.correctAnswer) correct = Array.isArray(q.correctAnswer) ? q.correctAnswer : [q.correctAnswer];
      else if (q.correctOptionIds) correct = q.correctOptionIds;
      
      if (correct) {
        q.correctAnswers = correct;
        modified = true;
      }
    }

    // Cleanup bad keys
    delete q.correctOptions;
    delete q.correctOptionId;
    delete q.correctAnswer;
    delete q.correctOptionIds;
    delete q.isMultipleChoice;

    // Remove isCorrect from root options
    if (q.options) {
      q.options.forEach(opt => {
        if ('isCorrect' in opt) {
          delete opt.isCorrect;
          modified = true;
        }
      });
    }

    // 3. Fix missing statement or generalExplanation by pulling from translations
    if (!q.statement && q.translations && q.translations['en'] && q.translations['en'].statement) {
      q.statement = q.translations['en'].statement;
      modified = true;
    } else if (!q.statement && q.translations && q.translations['en'] && q.translations['en'].text) {
      q.statement = q.translations['en'].text;
      q.translations['en'].statement = q.translations['en'].text;
      delete q.translations['en'].text;
      modified = true;
    }

    if (!q.generalExplanation && q.translations && q.translations['en'] && q.translations['en'].generalExplanation) {
      q.generalExplanation = q.translations['en'].generalExplanation;
      modified = true;
    }

    // Fix translation texts instead of statement
    if (q.translations) {
      for (const lang of Object.keys(q.translations)) {
        if (q.translations[lang].text && !q.translations[lang].statement) {
          q.translations[lang].statement = q.translations[lang].text;
          delete q.translations[lang].text;
          modified = true;
        }
        if (q.translations[lang].options) {
          q.translations[lang].options.forEach(opt => {
            if ('isCorrect' in opt) {
              delete opt.isCorrect;
              modified = true;
            }
          });
        }
      }
    }

    // 4. Fallback domainId and domainName
    if (!q.domainId) {
      q.domainId = "domain-3-continuous-improvement"; // Fallback
      modified = true;
    }
    if (!q.domainName) {
      q.domainName = "Domain 3: Continuous Improvement for Existing Solutions";
      modified = true;
    }

    if (modified) totalFixed++;
  }

  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log(`Deep normalized ${sim}`);
  }
}

console.log(`Total questions fixed: ${totalFixed}`);
