# Model Evaluation Principles

## What Problem Are We Solving?

Accuracy alone is insufficient for risk models.

We introduced:

- Accuracy
- Precision
- Recall

## Where This Exists in Code

- src/platform/training/late_payment_training.py

## Why These Metrics?

For risk systems:

Precision → Avoid false accusations  
Recall → Avoid missing risky cases  

Different use cases prioritize different tradeoffs.

## Deterministic Evaluation

We use:
- Fixed random seed
- Explicit test split
- Returned metrics dictionary

Evaluation must be reproducible to be meaningful.