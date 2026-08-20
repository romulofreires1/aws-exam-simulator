# 🛡️ AWS Exam Simulator

> **A modern, offline-ready, 100% client-side AWS Certification Exam Simulator designed with high fidelity to the official testing interface (Pearson VUE).**

---

## ✨ Key Features

- ⏱️ **Real Exam Mode**: Official AWS countdown timer (with visual warning banners at 15m and 5m remaining), free navigation, pre-submission review screen, and scaled scoring on the official AWS scale (100 to 1000 points).
- 💡 **Practice Mode (Study)**: Untimed mode with on-demand answer checking, detailed option-by-option architectural rationales, and official AWS documentation links.
- 🚫 **Option Strikethrough**: Eliminate incorrect options using a dedicated button or right-clicking.
- ✨ **Text Highlighting**: Select any text in the question statement to highlight in yellow with cross-question persistence.
- 🚩 **Flag & Scratchpad**: Flag questions to review later and take dedicated scratchpad notes for each question.
- 📊 **Domain Performance Breakdown**: Comprehensive score breakdown by domain competency according to the official AWS exam guide.
- 💾 **100% Client-Side Local Storage**: Continuous automatic saving in `localStorage`. Refresh or close the browser tab without losing active session progress or attempt history.
- ⌨️ **Keyboard Shortcuts**: Keys <kbd>A</kbd>–<kbd>E</kbd> to select options, <kbd>F</kbd> to flag/unflag, <kbd>→</kbd> / <kbd>Enter</kbd> for next question, and <kbd>←</kbd> for previous.
- 🌗 **Layout Switching**: Toggle in real time between the **Modern Dark AWS Console** theme and the classic **Pearson VUE** testing layout.

---

## 📚 Included Certification Exams

| Code | Certification | Level | Official Time | Passing Score |
| :--- | :--- | :--- | :--- | :--- |
| **SAP-C02** | AWS Certified Solutions Architect - Professional | Professional | 180 min | 750 / 1000 |
| **SAA-C03** | AWS Certified Solutions Architect - Associate | Associate | 130 min | 720 / 1000 |
| **CLF-C02** | AWS Certified Cloud Practitioner | Foundational | 90 min | 700 / 1000 |

---

## 💻 Local Development and Execution

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Development Server (Hot-Reload)
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### 3. Production Build and Static Export
```bash
npm run build
npm run start
```

---

## 🤖 Adding New Exams with AI

The project includes a standardized template and automated validation script for easily adding new exams:

1. Open [`.agent/AI_PROMPT_TEMPLATE.md`](.agent/AI_PROMPT_TEMPLATE.md) and copy the prompt to your favorite AI assistant (ChatGPT, Claude, Gemini).
2. Save the generated JSON file to `src/data/exams/[exam-code].json`.
3. Register the exam in the `AVAILABLE_EXAMS` array in `src/data/exams/index.ts`.
4. Validate the JSON integrity by running:
   ```bash
   npm run validate:exams
   ```
5. Commit and push:
   ```bash
   git add src/data/exams/
   git commit -m "feat: add DVA-C02 exam"
   git push origin main
   ```

---

## 🚀 Deployment and AWS Infrastructure

This project is configured for automated CI/CD deployment via GitHub Actions:

- **Infrastructure**: Amazon S3 (static website hosting), Amazon CloudFront (global CDN with ACM SSL), and Amazon Route 53 (DNS).
- **CI/CD**: Upon `git push origin main`, GitHub Actions validates exams, generates the static export (`out/`), synchronizes files to Amazon S3, and invalidates the CloudFront cache.

---

## 🛠️ Technologies

- **Framework**: Next.js 15 (App Router, Static HTML Export)
- **UI & Styling**: React 19, Tailwind CSS, Lucide React, Canvas Confetti
- **Language**: TypeScript
- **Validation & Scripts**: TSX, Node.js
