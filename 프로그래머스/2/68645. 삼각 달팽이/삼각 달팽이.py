def solution(n):
    arrow = ((1, 0), (0, 1), (-1, -1))

    lst = [[0] * c for c in range(1, n + 1)]
    lst[0][0] = 1

    x, y = 0, 0
    dist = 0
    cnt, max_cnt = 2, 0
    for i in range(1, n + 1):
        max_cnt += i

    while cnt <= max_cnt:
        dx, dy = x + arrow[dist][0], y + arrow[dist][1]
        if dx >= len(lst) or dy >= len(lst[x]):
            dist = (dist + 1) % 3
            continue

        if lst[dx][dy]:
            dist = (dist + 1) % 3
            continue

        if not lst[dx][dy]:
            lst[dx][dy] = cnt
            x, y = dx, dy
            cnt += 1

    answer = sum(lst, [])
    return answer