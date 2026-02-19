from typing import List, Type
from pydantic import BaseModel, ValidationError


def validate_records(
    records: List[dict],
    schema: Type[BaseModel],
) -> List[BaseModel]:
    """
    Validate a list of records against a Pydantic schema.

    Returns validated model instances or raises ValidationError.
    """
    validated = []

    for record in records:
        validated.append(schema(**record))

    return validated
