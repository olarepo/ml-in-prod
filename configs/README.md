# Configuration Strategy

## Why Config Matters

Hard-coded values are the enemy of reproducibility.

All environment-specific and use-case-specific behavior must be controlled via config.

---

## What Goes in Config

- Data paths  
- Feature lists  
- Model hyperparameters  
- Training settings  
- Thresholds  
- Azure resource names  

---

## Structure

```text
configs/
├── base.yaml  
├── late_payment.yaml  
├── invoice_fraud.yaml  
├── churn_risk.yaml  
├── dev.yaml  
└── prod.yaml  
```

---

## Config Precedence

Configs are merged in this order:

1. base.yaml  
2. use case config  
3. environment config  

Later configs override earlier ones.

---

## Example

model:  
  type: xgboost  
  max_depth: 6  
  learning_rate: 0.1  

training:  
  random_seed: 42  
  n_folds: 5  

---

## Design Rules

1. No magic numbers in code  
2. All tunable values in config  
3. Configs are versioned  
4. Configs are logged with every run  

