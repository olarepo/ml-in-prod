# Use Case Layer

## Purpose

The use case layer contains business-specific ML logic.

This is where late payment, fraud, and churn differ.

This code:
- Defines features
- Defines targets
- Defines metrics and thresholds
- Contains domain assumptions

It must NOT:
- Implement pipelines
- Handle deployment
- Know about Azure or UI

---

## Structure

```text
src/use_cases/
├── late_payment/
│   ├── README.md  
│   ├── features.py  
│   ├── target.py  
│   └── metrics.py  
├── invoice_fraud/
│   └── ...  
└── churn_risk/
    └── ...  
```

---

## Responsibilities

Each use case defines:

- Feature definitions  
- Target construction  
- Evaluation metrics  
- Business thresholds  

The platform decides:

- How to train  
- How to serve  
- How to monitor  

---

## Example Contract

Each use case must expose:

    def build_features(raw_data) -> FeatureTable:
        ...

    def build_target(raw_data) -> TargetVector:
        ...

    def evaluation_metrics() -> Dict[str, Callable]:
        ...

---

## Design Rules

1. No pipeline orchestration here  
2. No cloud code here  
3. No UI code here  
4. Only domain logic  

This keeps business logic isolated and testable.


