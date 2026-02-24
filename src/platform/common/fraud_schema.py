from pydantic import BaseModel
from typing import Optional


class InvoiceFraudRecord(BaseModel):
    """
    Schema for invoice fraud detection.
    """

    invoice_id: str
    vendor_id: str
    invoice_amount: float
    invoice_age_days: int
    country: str
    is_new_vendor: bool
    label: Optional[int] = None