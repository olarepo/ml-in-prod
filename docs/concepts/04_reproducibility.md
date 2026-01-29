# Reproducibility in Production ML

## Why Reproducibility Matters

If you cannot reproduce a model:
- You cannot debug it
- You cannot trust it
- You cannot improve it
- You cannot explain it

Reproducibility is not optional in production systems.

---

## Sources of Non-Reproducibility

1. Random initialization  
2. Data drift  
3. Dependency version changes  
4. Configuration changes  
5. Undocumented preprocessing  

---

## How This Repo Enforces Reproducibility

1. Pinned dependencies  
2. Config-driven behavior  
3. Logged random seeds  
4. Versioned models  
5. Immutable training artifacts  

---

## Environments

We support two environments:

- dev → local development  
- prod → production deployment  

Each environment has:
- Its own config
- Its own secrets
- Its own logging level

---

## Reproducible Training Flow

1. Load config  
2. Set random seed  
3. Load and validate data  
4. Train model  
5. Save model with metadata  
6. Log config + metrics  
7. Register model version  

If any step changes, the model version must change.

---