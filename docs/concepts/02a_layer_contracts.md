# Layer Contracts

This document defines what each layer is allowed to know and do.

## Data Layer

Inputs:
- Raw files
- Database tables
- External feeds

Outputs:
- Clean feature tables
- Validated schemas

Must NOT:
- Train models
- Call APIs
- Contain business rules

---

## Platform Layer

Inputs:
- Feature tables
- Use case configuration

Outputs:
- Trained models
- Prediction services
- Monitoring metrics

Must NOT:
- Hard-code business logic
- Depend on UI frameworks
- Contain cloud-specific code

---

## Use Case Layer

Inputs:
- Domain data
- Business definitions

Outputs:
- Feature definitions
- Target definitions
- Thresholds & metrics

Must NOT:
- Implement pipelines
- Know deployment details
- Call Azure directly

---

## UI Layer

Inputs:
- API responses

Outputs:
- Visualizations
- User interactions

Must NOT:
- Load models
- Run training
- Access raw data