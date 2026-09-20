const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));

const rawQ = data.questions[12];
const lang = 'pt';

const t = rawQ.translations[lang];
const q = {
  ...rawQ,
  domainName: t.domainName || rawQ.domainName,
  statement: t.statement || rawQ.statement,
  options: (rawQ.options || []).map((opt) => {
    const transOpt = t.options?.find((o) => o.id === opt.id);
    return {
      id: opt.id,
      text: transOpt?.text || opt.text,
      explanation: transOpt?.explanation || opt.explanation,
    };
  }),
  generalExplanation: t.generalExplanation || rawQ.generalExplanation,
};

console.log('q.correctAnswers:', q.correctAnswers);
console.log('q.options[0].id:', q.options[0].id);
console.log('isThisCorrect:', (q.correctAnswers || []).includes(q.options[0].id));
