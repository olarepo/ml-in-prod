# Deterministic Feature Engineering

## What Problem Are We Solving?

Models require numeric input, not raw business data.

Feature engineering converts validated records into:
- Numeric representations
- Derived indicators
- Model-ready vectors

## Where This Exists in Code

- src/platform/features/late_payment_features.py

## Core Design Principle

Features must be:

- Deterministic
- Pure functions
- Free of side effects
- Identical in training and serving

## Why Determinism Matters

Non-deterministic feature logic causes:
- Reproducibility failures
- Inconsistent predictions
- Debugging nightmares

Training and serving must share the same transformation logic.