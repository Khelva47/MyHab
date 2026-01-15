from typing import Optional
from datetime import datetime, date

class Completion:
    def __init__(
      self,
      id: str,
      habit_id: str,
      date: date,
      completed_steps: int = 0,
      notes: Optional[str] = "",
      created_at: Optional[datetime] = None
    ):
        self.id = id
        self.habit_id = habit_id
        self.completed_steps = completed_steps
        self.notes = notes
        self.date = date
        self.created_at = created_at