from pydantic import BaseModel
from typing import List
from datetime import date


class HabitScore(BaseModel):
    habit_id: str
    habit_name: str
    goal: int
    completed_today: bool
    current_streak: int
    total_completions: int
    completion_rate: float
    score: float


class ScoreCardResponse(BaseModel):
    date: date
    habits: List[HabitScore]
    total_score: float
    
    class Config:
        orm_mode = True