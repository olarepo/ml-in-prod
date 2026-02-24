# Data Contracts & Schema Validation

## What Problem Are We Solving?

Most ML failures originate from bad data, not bad models.

Schemas define:
- Required fields
- Data types
- Optional vs mandatory fields

## Where This Exists in Code

- src/platform/common/schema.py
- src/platform/common/validation.py

## Core Design

Raw dict → Pydantic schema → Validated object

This ensures:
- Type safety
- Early failure
- Self-documenting data structures

## Why This Matters

Without validation:
- Training-serving skew occurs
- Silent type coercion happens
- Bugs surface late in production

Schema validation is a production guardrail.