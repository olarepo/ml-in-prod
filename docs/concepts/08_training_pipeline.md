# Training Pipeline Architecture

## What Problem Are We Solving?

Training is not just "fit a model".

A production training pipeline must:

1. Validate input
2. Build deterministic features
3. Split data reproducibly
4. Train a model
5. Evaluate performance
6. Persist artifacts

## Where This Exists in Code

- src/platform/training/late_payment_training.py

## Determinism Controls

- RANDOM_STATE fixed
- Stratified splitting
- Explicit feature construction

## Why Persistence Matters

Model artifacts must be:
- Loadable later
- Versionable
- Deployable

Training without persistence is not production-ready.