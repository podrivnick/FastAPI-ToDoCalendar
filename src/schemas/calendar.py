from datetime import datetime

from pydantic import BaseModel


class CalendarSchema(BaseModel):
    pk: int
    assigned_from: int
    assigned_from: int
    task: str
    priority: int
    start_date: datetime
    due_date: datetime



