from pydantic import BaseModel
from typing import Dict, List
from datetime import date


class DailyStats(BaseModel):
    date: date
    completed_habits: int
    total_habits: int
    steps: int


class WeeklySummary(BaseModel):
    week_start: date
    week_end: date
    daily_stats: List[DailyStats]
    total_completions: int
    average_completion_rate: float
    total_steps: int
    best_streak_habit: str
    best_streak_days: int


class HabitAnalytics(BaseModel):
    habit_id: str
    habit_name: str
    total_completions: int
    current_streak: int
    longest_streak: int
    completion_rate: float
    completions_by_day: Dict[str, int]