import fs from 'fs';
import path from 'path';

// Define a list of known valid AWS service prefixes to catch obvious hallucinations
const VALID_SERVICE_PREFIXES = ['AWS ', 'Amazon '];

async function validateUrl(url: string): Promise<boolean> {
  if (!url || !url.startsWith('http')) return false;
  try {
    // We do a HEAD request to be fast, fallback to GET if HEAD fails
    let res = await fetch(url, { method: 'HEAD' });
    if (!res.ok && res.status === 404) {
      // Sometimes AWS docs don't like HEAD, try GET
      res = await fetch(url, { method: 'GET' });
    }
    return res.ok;
  } catch (error) {
    return false;
  }
}

async function validateExamContent(filePath: string) {
  console.log(`\n🔍 Validating content for: ${path.basename(filePath)}`);
  
  let data;
  try {
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    data = JSON.parse(fileContent);
  } catch (err) {
    console.error(`❌ Failed to read or parse JSON: ${(err as Error).message}`);
    return;
  }

  const questions = data.questions || [];
  let brokenUrls = 0;
  let suspiciousServices = 0;

  for (const q of questions) {
    // 1. Check URL
    const url = q.referenceUrl;
    if (url) {
      const isValid = await validateUrl(url);
      if (!isValid) {
        console.warn(`⚠️  [${q.id}] Broken or unreachable URL: ${url}`);
        brokenUrls++;
      }
    } else {
      console.warn(`⚠️  [${q.id}] Missing referenceUrl`);
      brokenUrls++;
    }

    // 2. Check Services
    const services = q.services || [];
    for (const service of services) {
      const isKnown = VALID_SERVICE_PREFIXES.some(prefix => service.startsWith(prefix)) || service === 'DynamoDB' || service === 'EC2'; // allow some common ones without prefix
      if (!isKnown) {
        console.warn(`⚠️  [${q.id}] Suspicious service name (might be hallucinated): "${service}"`);
        suspiciousServices++;
      }
    }
  }

  console.log(`\n📊 Validation Report for ${path.basename(filePath)}:`);
  console.log(`- Questions checked: ${questions.length}`);
  console.log(`- Broken URLs: ${brokenUrls}`);
  console.log(`- Suspicious Services: ${suspiciousServices}`);
  
  if (brokenUrls === 0 && suspiciousServices === 0) {
    console.log(`✅ Passed all content checks!`);
  } else {
    console.log(`❌ Found potential hallucinations.`);
  }
}

async function main() {
  const args = process.argv.slice(2);
  const targetFile = args[0];
  
  if (targetFile) {
    await validateExamContent(targetFile);
  } else {
    // Scan all exams if no file provided
    const examsDir = path.join(__dirname, '../src/data/exams');
    const files = fs.readdirSync(examsDir).filter(f => f.endsWith('.json'));
    for (const file of files) {
      await validateExamContent(path.join(examsDir, file));
    }
  }
}

main();
