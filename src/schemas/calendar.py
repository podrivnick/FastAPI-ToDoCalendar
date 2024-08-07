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
    assigned_from: str
    assigned_to: str
    title: str
    task: str
    priority: int
    start_date: datetime
    due_date: datetime


class DeleteCalendarSchema(BaseModel):
    assigned_from: str
    assigned_to: str
    start_date: datetime
    due_date: datetime


class CalendarAccessSchema(BaseModel):
    user_id: int
    accessible_user_id: int


class CalendarAssignedForSchema(BaseModel):
    assigned_to: str

