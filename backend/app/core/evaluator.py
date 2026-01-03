def evaluate_answer(answer: str, depth: int) -> bool:
    answer = answer.lower()

    if depth == 1:
        keywords = ["list", "python"]
    elif depth == 2:
        keywords = ["mutable", "index", "dynamic"]
    elif depth == 3:
        keywords = ["array", "memory", "resize"]
    else:
        return False

    score = 0
    for word in keywords:
        if word in answer:
            score += 1

    return score >= len(keywords) // 2 + 1