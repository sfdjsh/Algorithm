def solution(operations):
    answer = []

    for s in operations:
        if s[0] == "I":
            answer.append(int(s[2:]))
        elif answer:
            if s == "D -1":
                answer.remove(min(answer))
            if s == "D 1":
                answer.remove(max(answer))

    if answer:
        return max(answer), min(answer)
    else:
        return [0, 0]
