# System Architecture for ML in Production

## Why Architecture Matters

Most ML failures in production are not caused by bad models.
They are caused by **bad system design**.

Without clear architecture:
- Models are tightly coupled to data
- UI talks directly to training code
- Changes in one place break everything else
- Scaling becomes impossible

Good architecture makes ML systems:
- Testable
- Maintainable
- Scalable
- Replaceable

---

## High-Level Components

This repository uses **four major layers**:

1. **Data Layer**
   - Raw data sources
   - Feature pipelines
   - Data validation

2. **ML Platform Layer**
   - Training pipelines  
   - Model versioning  
   - Serving pipelines  
   - Monitoring & retraining  

3. **Use Case Layer**
   - Late payment logic  
   - Invoice fraud logic  
   - Churn risk logic  

4. **Application Layer**
   - APIs (Azure Functions)
   - UI dashboards
   - Batch interfaces

Each layer has a **single responsibility**.

---

## Core Design Principle: Separation of Concerns

| Layer | Responsibility | What It Must NOT Do |
|------|---------------|--------------------|
| Data | Ingest & validate data | Know about UI or business logic |
| Platform | Generic ML pipelines | Know business rules |
| Use Cases | Business-specific logic | Know infrastructure details |
| UI | Consume APIs | Know anything about models |

This separation:
- Prevents tight coupling
- Allows reuse across use cases
- Enables independent testing and scaling

---

## End-to-End Flow (Conceptual)

1. Raw data arrives
2. Data pipeline validates & transforms it
3. Training pipeline trains a model
4. Model is versioned and stored
5. Serving pipeline exposes API endpoint
6. UI calls API to get predictions
7. Monitoring tracks performance and drift
8. Retraining updates the model when needed

This is a **closed loop system**, not a one-time process.

---

## Multi–Use Case Architecture

A key design goal is:

> **One platform, many use cases**

This means:
- One data pipeline framework
- One training pipeline framework
- One serving framework
- Three different business configurations

Late payment, fraud, and churn differ only in:
- Feature definitions
- Target variable
- Evaluation metrics
- Thresholds

The infrastructure remains the same.

---

## Cloud Boundary (Azure)

In this project:

- APIs run on **Azure Functions**
- Models are stored in **Blob Storage**
- UI runs as a **Static Web App**
- Monitoring uses **Application Insights**

Cloud concerns are isolated in:
- `deployment/`
- `configs/`

ML code never directly depends on Azure SDKs.

---
