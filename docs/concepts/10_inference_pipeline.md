# Inference Pipeline Architecture

## What Problem Are We Solving?

A trained model is useless without a safe serving pipeline.

Inference must:

1. Validate incoming data
2. Rebuild features identically to training
3. Load persisted model
4. Produce structured outputs

## Where This Exists in Code

- src/platform/serving/late_payment_serving.py

## Training-Serving Parity

The transformation path must match:

Training:
validate → features → model

Serving:
validate → features → model

If these diverge, predictions become unreliable.

## Structured Outputs

Predictions return:

{
  "customer_id": ...,
  "risk_probability": ...,
  "predicted_label": ...
}

This enables:
- APIs
- Monitoring
- Business traceability