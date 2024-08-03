from datetime import datetime

from pydantic import BaseModel


class CalendarSchema(BaseModel):
    pk: int
    assigned_from: int
    assigned_from: int
    title: str
    task: str
    priority: int
    start_date: datetime
    due_date: datetime


class AddCalendarSchema(BaseModel):
    who_assigned: str
    for_who_assigned: str
    title: str
    task: str
    priority: str
    start_date: datetime
    due_date: datetime


class CalendarAccessSchema(BaseModel):
    user_id: int
    accessible_user_id: int


