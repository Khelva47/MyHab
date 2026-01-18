def is_valid_habit_name(name: str) -> bool:
    if not name or len(name.strip()) < 2:
        return False
    if len(name) > 100:
        return False
    return True


def is_valid_goal(goal: int) -> bool:
    return 0 < goal <= 100
