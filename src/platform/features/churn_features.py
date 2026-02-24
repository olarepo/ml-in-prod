from typing import Dict
from src.platform.common.churn_schema import ChurnRecord


def build_churn_features(record: ChurnRecord) -> Dict[str, float]:
    """
    Deterministic feature engineering for churn.
    """

    return {
        "tenure_months": float(record.tenure_months),
        "monthly_spend": float(record.monthly_spend),
        "support_tickets_last_3m": float(record.support_tickets_last_3m),
        "low_tenure": 1.0 if record.tenure_months < 6 else 0.0,
        "high_support_load": 1.0 if record.support_tickets_last_3m > 5 else 0.0,
        "inactive_user": 0.0 if record.is_active_user else 1.0,
    }