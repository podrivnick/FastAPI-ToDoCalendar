from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class TaskCalendar(Base):
    __tablename__ = 'tasks_calendar'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    assigned_from: Mapped[str] = mapped_column(String, ForeignKey('user.username'), nullable=False)
    assigned_to: Mapped[str] = mapped_column(String, ForeignKey('user.username'), nullable=False)
    title: Mapped[str] = mapped_column(String(40), nullable=False)
    task: Mapped[str] = mapped_column(String(128), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    def read_model(self):
        return {
            "id": self.id,
            "assigned_from": self.assigned_from,
            "assigned_to": self.assigned_to,
            "title": self.title,
            "task": self.task,
            "priority": self.priority,
            "start_date": str(self.start_date),
            "due_date": str(self.due_date),
        }

