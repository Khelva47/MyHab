from typing import Optional
from datetime import datetime, date


class StepCount:
    def __init__(
        self,
        id: str,
        user_id: str,
        date: date,
        steps: int = 0,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.steps = steps
        self.created_at = created_at
        self.updated_at = updated_at
