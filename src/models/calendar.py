from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime

from database.database import metadata

tasks_calendar = Table(
    "tasks_calendar",
    metadata,
    Column("pk", Integer, primary_key=True, autoincrement=True),
    Column("assigned_from", Integer, ForeignKey('user.id'), nullable=False),
    Column("assigned_to", Integer, ForeignKey('user.id'), nullable=False),
    Column("title", String(40), nullable=True),
    Column("task", String(128), nullable=False),
    Column("priority", Integer, nullable=False, default=3),
    Column("start_date", DateTime, nullable=False),
    Column("due_date", DateTime, nullable=False)
)

