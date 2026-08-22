# 🛡️ AWS Exam Simulator

> **A modern, offline-ready, 100% client-side AWS Certification Exam Simulator designed with high fidelity to the official testing interface (Pearson VUE).**

---

## ✨ Key Features

- ⏱️ **Real Exam Mode**: Official AWS countdown timer (with visual warning banners at 15m and 5m remaining), free navigation, pre-submission review screen, and scaled scoring on the official AWS scale (100 to 1000 points).
- 💡 **Practice Mode (Study)**: Untimed mode with on-demand answer checking, detailed option-by-option architectural rationales, and official AWS documentation links.
- ⏸️ **In-Exam Pause & Resume**: Pause the exam at any time directly from the interface. The timer freezes, remaining time is saved to `localStorage`, and question content is masked with a dedicated resume overlay.
- 🚪 **Abandon Exam Modal**: Safe exit flow with confirmation dialog to abandon or return to the dashboard without losing past attempt history.
- 🌐 **Multi-Language Support (i18n)**: Live in-exam language switcher supporting **English (🇺🇸 EN)**, **Portuguese (🇧🇷 PT)**, and **Spanish (🇪🇸 ES)** with automatic fallback and disabled badges when translations are unavailable.
- 🔍 **Interactive Catalog & Filters**: Real-time search by keyword (code, title, description, category), category filter pills with dynamic count badges (*All, Foundational, Associate, Professional, Specialty*), and clean pagination (6 items per page).
- 🚫 **Option Strikethrough**: Eliminate incorrect options using a dedicated button or right-clicking.
- ✨ **Text Highlighting**: Select any text in the question statement to highlight in yellow with cross-question session persistence.
- 🚩 **Flag & Scratchpad**: Flag questions to review later and take dedicated scratchpad notes for each question.
- 📊 **Domain Performance Breakdown**: Comprehensive score breakdown by domain competency according to the official AWS exam guide with percentage progress bars and pass/fail thresholds.
- 💾 **100% Client-Side Local Storage**: Continuous automatic saving in `localStorage`. Refresh or close the browser tab without losing active session progress or attempt history.
- ⌨️ **Keyboard Shortcuts**: Keys <kbd>A</kbd>–<kbd>E</kbd> to select options, <kbd>F</kbd> to flag/unflag, <kbd>→</kbd> / <kbd>Enter</kbd> for next question, and <kbd>←</kbd> for previous.
- 🌗 **Layout Switching**: Toggle in real time between the **Modern Dark AWS Console** theme and the classic **Pearson VUE** testing layout.
- 🤖 **AI Question Generator Skills**: 3 specialized agent skills with 2x2 decision matrix engineering, strict distractor guidelines, anti-bias shuffle rules, and automated schema validators.

---

## 📚 Included Certification Exams (205 Total Realistic Questions)

| Code | Certification / Exam | Level | Questions | Official Time | Passing Score |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **SAP-C02-SIM-1** | AWS Certified Solutions Architect - Professional *(Mock 1)* | Professional | 25 | 70 min | 750 / 1000 |
| **SAP-C02-SIM-2** | AWS Certified Solutions Architect - Professional *(Mock 2)* | Professional | 25 | 70 min | 750 / 1000 |
| **SAP-C02-SIM-3** | AWS Certified Solutions Architect - Professional *(Mock 3)* | Professional | 25 | 70 min | 750 / 1000 |
| **SAA-C03** | AWS Certified Solutions Architect - Associate | Associate | 65 | 130 min | 720 / 1000 |
| **CLF-C02** | AWS Certified Cloud Practitioner | Foundational | 65 | 90 min | 700 / 1000 |

> All mock exams feature **balanced answer distributions** (randomized across options A, B, C, D, E) and **realistic enterprise scenarios** without obvious or naive distractors.

---

## 🤖 AI Question Generator Skills (`.agents/skills/`)

The repository includes ready-to-use Agent Skills designed for generating exam-grade questions with strict fidelity rules:

| Skill Name | Certification | Path |
| :--- | :--- | :--- |
| `clf-c02-question-generator` | AWS Certified Cloud Practitioner (CLF-C02) | [`.agents/skills/clf-c02-question-generator/`](.agents/skills/clf-c02-question-generator/) |
| `saa-c03-question-generator` | AWS Certified Solutions Architect - Associate (SAA-C03) | [`.agents/skills/saa-c03-question-generator/`](.agents/skills/saa-c03-question-generator/) |
| `sap-c02-question-generator` | AWS Certified Solutions Architect - Professional (SAP-C02) | [`.agents/skills/sap-c02-question-generator/`](.agents/skills/sap-c02-question-generator/) |

### Core Question Engineering Standards:
- **2x2 Decision Matrix**: Options are structured in conceptual pairs to test nuanced trade-offs (e.g., cost vs. operational overhead, managed AWS services vs. custom scripts).
- **Strict Distractor Plausibility**: All alternatives represent technically valid, modern AWS services; distractors fail only on subtle scenario constraints.
- **Answer Shuffling**: Gabaritos are uniformly distributed across letters A through E.
- **Dual Export Formats**: Exports directly to **JSON** (for simulator) or **Markdown** (for Obsidian study vaults).

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

### 4. Validate Exam Integrity
```bash
npm run validate:exams
```

---

## ➕ Adding New Exams

The project supports adding new exams via AI agents or manually:

1. Use one of the dedicated Agent Skills in [`.agents/skills/`](.agents/skills/) or copy [`.agents/AI_PROMPT_TEMPLATE.md`](.agents/AI_PROMPT_TEMPLATE.md).
2. Save the generated JSON file to `src/data/exams/[exam-code].json`.
3. Register the exam in `src/data/exams/index.ts`.
4. Validate the JSON integrity:
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
- **Static Export**: Configured with `output: 'export'` and `trailingSlash: true` in `next.config.ts` for clean static routing.
- **CI/CD**: Upon `git push origin main`, GitHub Actions validates exams, generates the static export (`out/`), synchronizes files to Amazon S3, and invalidates the CloudFront cache.

---

## 🛠️ Technologies

- **Framework**: Next.js 15 (App Router, Static HTML Export)
- **UI & Styling**: React 19, Tailwind CSS, Lucide React, Canvas Confetti
- **Language**: TypeScript
- **Internationalization**: Custom lightweight SSR-safe client i18n engine (`localization.ts`)
- **Validation & Tooling**: TSX, Python 3, Node.js

