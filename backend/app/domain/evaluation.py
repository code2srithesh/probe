def evaluate_attempt(answer: str, required_keywords: list[str]) -> bool:
    for word in required_keywords:
        if word not in answer.lower():
            return False
    return True