from itertools import combinations

def func(n):
    global result

    if n == 15:
        result = 1
        for s in graph:
            if s.count(0) != 3:
                result = 0
                break
        return

    g1, g2 = game[n]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if graph[g1][x] > 0 and graph[g2][y] > 0:
            graph[g1][x] -= 1
            graph[g2][y] -= 1
            func(n + 1)
            graph[g1][x] += 1
            graph[g2][y] += 1

game = list(combinations(range(6), 2))
answer = []

for _ in range(4):
    w_d_l = list(map(int, input().split()))
    graph = [w_d_l[i * 3:i * 3 + 3] for i in range(6)]
    result = 0
    func(0)
    answer.append(result)

print(*answer)
