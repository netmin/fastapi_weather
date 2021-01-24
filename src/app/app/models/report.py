from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..models.location import Location


class ReportSubmittal(BaseModel):
    description: str
    location: Location

    class Config:
        arbitrary_types_allowed = True


class Report(ReportSubmittal):
    id: str
    created_date: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
