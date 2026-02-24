from typing import Dict
from src.platform.common.fraud_schema import InvoiceFraudRecord


def build_invoice_fraud_features(record: InvoiceFraudRecord) -> Dict[str, float]:
    """
    Deterministic feature transformation for invoice fraud.
    """

    return {
        "invoice_amount": float(record.invoice_amount),
        "invoice_age_days": float(record.invoice_age_days),
        "is_new_vendor": float(record.is_new_vendor),
        "high_value_invoice": 1.0 if record.invoice_amount > 5000 else 0.0,
        "stale_invoice": 1.0 if record.invoice_age_days > 60 else 0.0,
    }