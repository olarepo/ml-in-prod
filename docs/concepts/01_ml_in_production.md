# ML in Production — Core Concepts

## What Is Machine Learning in Production?

Machine Learning in production is about running models **reliably, repeatedly, and safely**
inside real systems — not just training them in notebooks.

A production ML system must:
- Ingest real data
- Make predictions automatically
- Handle failures gracefully
- Be monitored and improved over time

A model that cannot be monitored, reproduced, or updated is **not production-ready**.

---

## How Production ML Differs from Notebooks

| Notebook ML | Production ML |
|------------|---------------|
| One-off experiments | Automated pipelines |
| Manual data loading | Validated data ingestion |
| Ad-hoc training | Reproducible training runs |
| Offline evaluation | Live monitoring |
| Single model | Versioned models |
| No users | Real users & systems |

---

## What Usually Goes Wrong in Production

Common failure modes:
- Data schema changes silently
- Model performance degrades over time
- Training cannot be reproduced
- Predictions cannot be explained
- No clear ownership or lifecycle

This repository is structured to **prevent these failures by design**.

---

## Core Principles of Production ML

### 1. Separation of Concerns
Different parts of the system have different responsibilities:
- Platform code: reusable ML infrastructure
- Use cases: business-specific logic
- UI: consumer of predictions

### 2. Reproducibility
The same code + data + config should always produce the same model.

### 3. Observability
You must be able to answer:
- Is the model being used?
- Is it still performing well?
- Has the data changed?

### 4. Automation
Manual steps do not scale.
Training, deployment, and monitoring should be automated.

### 5. Lifecycle Thinking
Models are not static.
They are trained, deployed, monitored, retrained, and retired.

---

## How These Principles Appear in This Repo

| Principle | Where You’ll See It |
|---------|--------------------|
| Separation of concerns | `src/platform/`, `src/use_cases/`, `ui/` |
| Reproducibility | Config files, versioned models |
| Observability | Monitoring pipelines + UI |
| Automation | CI/CD + Azure Functions |
| Lifecycle | Retraining pipelines |

---

## Risk Engineering Context

This repo demonstrates production ML using **risk use cases**:
- Late payment risk
- Invoice fraud detection
- Customer churn risk

These are ideal examples because:
- They are high-impact
- They degrade over time
- They require monitoring and explainability