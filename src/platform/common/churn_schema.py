from pydantic import BaseModel
from typing import Optional


class ChurnRecord(BaseModel):
    """
    Schema for churn risk prediction.
    """

    customer_id: str
    tenure_months: int
    monthly_spend: float
    support_tickets_last_3m: int
    is_active_user: bool
    label: Optional[int] = None