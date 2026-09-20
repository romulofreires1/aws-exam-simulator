const fs = require('fs');

const indexData = fs.readFileSync('./src/data/exams/index.ts', 'utf8');
console.log(indexData.substring(0, 500));

