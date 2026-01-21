# Coding Standards for Production ML

## General Principles

- Code is read more than it is written  
- Explicit is better than implicit  
- Production code over clever code  

---

## Naming Conventions

Item | Convention  
-----|-----------  
Modules | snake_case.py  
Functions | snake_case  
Classes | PascalCase  
Constants | UPPER_CASE  

---

## Function Design

- Functions should do one thing  
- Prefer pure functions  
- No hidden state  
- Type hints everywhere  

Example:

    def validate_schema(df: pd.DataFrame, schema: Dict[str, str]) -> None:
        ...

---

## Error Handling

- Fail fast on invalid data  
- Raise explicit exceptions  
- Never silently ignore errors  

---

## Logging

- Log at boundaries (ingress, egress, failures)  
- Never log raw sensitive data  
- Always log config and model version  

---

## Testing Rules

- Every public function has a unit test  
- Business logic and platform logic tested separately  
- No tests depend on cloud resources  

---

## Code Review Checklist

- Is this in the right layer?  
- Is behavior controlled by config?  
- Is this reproducible?  
- Is this testable?  
- Does this leak business logic into platform code?  
