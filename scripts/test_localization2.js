const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-5.json', 'utf8'));
const rawQ = data.questions[12]; // Question 13
const t = rawQ.translations['pt'];

const q = {
  ...rawQ,
  options: (rawQ.options || []).map((opt) => {
    const transOpt = t.options?.find((o) => o.id === opt.id);
    return {
      id: opt.id,
      text: transOpt?.text || opt.text,
      explanation: transOpt?.explanation || opt.explanation,
    };
  }),
};

console.log(JSON.stringify(q, null, 2));
