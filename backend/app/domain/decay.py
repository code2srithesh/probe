from datetime import datetime, timedelta

DECAY_RULES = {
    1: timedelta(days=120),
    2: timedelta(days=90),
    3: timedelta(days=60),
    4: timedelta(days=30),
}

def is_skill_stale(depth: int, last_verified: datetime) -> bool:
    max_age = DECAY_RULES.get(depth, timedelta(days=60))
    return datetime.utcnow() - last_verified > max_age