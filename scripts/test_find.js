const fs = require('fs');

const exam4 = JSON.parse(fs.readFileSync('./src/data/exams/sap-c02-sim-4.json', 'utf8'));

console.log(exam4.id); // Should be SAP-C02-SIM-4
console.log(exam4.code); // Should be SAP-C02

const AVAILABLE_EXAMS = [exam4];
const normalizedId = "SAP-C02-SIM-4".toUpperCase();

const found = AVAILABLE_EXAMS.find(
  (exam) => exam.id.toUpperCase() === normalizedId || exam.code.toUpperCase() === normalizedId
);

console.log(found ? found.id : "NOT FOUND");

