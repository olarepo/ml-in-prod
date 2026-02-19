from pydantic import BaseModel
from typing import Optional


class LatePaymentRecord(BaseModel):
    """
    Schema for a single late payment training or inference record.
    """

    customer_id: str
    invoice_amount: float
    days_late: int
    country: str
    is_repeat_customer: bool
    label: Optional[int] = None
