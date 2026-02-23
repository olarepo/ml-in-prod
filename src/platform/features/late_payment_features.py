from typing import Dict

from src.platform.common.schema import LatePaymentRecord


def build_late_payment_features(record: LatePaymentRecord) -> Dict[str, float]:
    """
    Convert a validated LatePaymentRecord into numeric model features.

    This function must be:
    - Deterministic
    - Pure (no side effects)
    - Stable across training and serving
    """

    return {
        "invoice_amount": float(record.invoice_amount),
        "days_late": float(record.days_late),
        "is_repeat_customer": float(record.is_repeat_customer),
        "high_value_invoice": 1.0 if record.invoice_amount > 1000 else 0.0,
        "severely_late": 1.0 if record.days_late > 30 else 0.0,
    }