from typing import Optional
from datetime import datetime

class Habit:
    def __init__(
        self,
        id: str,
        user_id: str,
        name: str,
        description: Optional[str] = "",
        goal: int = 1,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.goal = goal
        self.created_at = created_at
        self.updated_at = updated_at