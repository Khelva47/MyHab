from datetime import datetime, date, timedelta
from typing import List


def get_today() -> str:
    return date.today().isoformat()


def get_date_range(days: int) -> List[str]:
    today = date.today()
    return [(today - timedelta(days=i)).isoformat() for i in range(days)]


def calculate_streak(completion_dates: List[str]) -> int:
    if not completion_dates:
        return 0

    sorted_dates = sorted([datetime.fromisoformat(d).date() for d in completion_dates], reverse=True)
    today = date.today()

    streak = 0
    expected_date = today

    for completion_date in sorted_dates:
        if completion_date == expected_date:
            streak += 1
            expected_date -= timedelta(days=1)
        elif completion_date < expected_date:
            break

    return streak


def get_week_start() -> str:
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    return week_start.isoformat()
