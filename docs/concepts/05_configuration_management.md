# Configuration Management

## What Problem Are We Solving?

Hardcoded values make ML systems fragile.

We externalize configuration so that:
- Behavior can change without code changes
- Environments (local, staging, prod) differ safely
- Parameters are version-controlled

## Where This Exists in Code

- src/platform/common/config.py
- configs/base.yaml

## Design Principles

1. Single source of truth
2. YAML-based configuration
3. Fail fast on missing config
4. Code reads config — never defines it

## Why This Matters

Without config discipline:
- Thresholds get duplicated
- Training and serving diverge
- Debugging becomes guesswork

Configuration is the foundation for:
- Cloud deployment
- Experiment tracking
- Model versioning