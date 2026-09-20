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
    // 0. Fix options object to array
    if (q.options && !Array.isArray(q.options)) {
      const newOptions = [];
      for (const [key, text] of Object.entries(q.options)) {
        newOptions.push({
          id: key.toLowerCase(),
          text: typeof text === 'string' ? text : (text.pt || text.en || 'Missing option text')
        });
      }
      q.options = newOptions;
      modified = true;
    }

    // 0.1 Fix options with text object instead of string
    if (Array.isArray(q.options)) {
      q.options.forEach(opt => {
        if (typeof opt.text === 'object') {
          opt.text = opt.text.pt || opt.text.en || 'Missing';
          modified = true;
        }
      });
    }

    // 1. Fix correctAnswers from options array (isCorrect: true)
    if (!q.correctAnswers) {
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
        // Ensure lowercase
        q.correctAnswers = correct.map(c => c.toLowerCase());
        modified = true;
      }
    } else {
      q.correctAnswers = q.correctAnswers.map(c => c.toLowerCase());
      modified = true; // just to be safe
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
    if (!q.statement && q.translations && q.translations['pt'] && q.translations['pt'].statement) {
      q.statement = q.translations['pt'].statement;
      modified = true;
    } else if (!q.statement && q.translations && q.translations['pt'] && q.translations['pt'].text) {
      q.statement = q.translations['pt'].text;
      q.translations['pt'].statement = q.translations['pt'].text;
      delete q.translations['pt'].text;
      modified = true;
    } else if (!q.statement && q.translations && q.translations['en'] && q.translations['en'].text) {
      q.statement = q.translations['en'].text;
      q.translations['en'].statement = q.translations['en'].text;
      delete q.translations['en'].text;
      modified = true;
    }

    if (!q.generalExplanation && q.translations && q.translations['pt'] && q.translations['pt'].generalExplanation) {
      q.generalExplanation = q.translations['pt'].generalExplanation;
      modified = true;
    } else if (!q.generalExplanation) {
      q.generalExplanation = "No explanation provided.";
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
        
        if (q.translations[lang].options && !Array.isArray(q.translations[lang].options)) {
          const newOptions = [];
          for (const [key, text] of Object.entries(q.translations[lang].options)) {
            newOptions.push({
              id: key.toLowerCase(),
              text: typeof text === 'string' ? text : 'Missing option text'
            });
          }
          q.translations[lang].options = newOptions;
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
    if (!q.services) q.services = [];

    if (modified) totalFixed++;
  }

  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log(`Deep normalized ${sim}`);
  }
}

console.log(`Total questions fixed: ${totalFixed}`);
