from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))

# 매 분마다 불이 번지는 것을 체크
def fire():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < N and 0 <= dy < M and not f_lst[dx][dy] and miro[dx][dy] != '#':
                f_lst[dx][dy] = f_lst[x][y] + 1
                f_queue.append((dx, dy))

def bfs():
    while j_queue:
        x, y = j_queue.popleft()

        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < N and 0 <= dy < M:
                if not j_lst[dx][dy] and miro[dx][dy] != '#':
                    if j_lst[x][y] + 1 < f_lst[dx][dy] or not f_lst[dx][dy]:    # 다음 위치가 불이 번지는 속도보다 낮거나, 불이 번지지 않았을 때
                        j_lst[dx][dy] = j_lst[x][y] + 1
                        j_queue.append((dx, dy))
            else:   # 가장 자리에서 벗어났을 때
                return j_lst[x][y]

    return 'IMPOSSIBLE'         # 탈출이 불가능할 때


N, M = map(int, input().split())

miro = [list(input()) for _ in range(N)]

f_queue, j_queue = deque(), deque()
f_lst = [[0] * M for _ in range(N)]         # 불이 퍼지는 리스트
j_lst = [[0] * M for _ in range(N)]         # 갈 수 있는 리스트

for i in range(N):
    for j in range(M):
        if miro[i][j] == 'F':
            f_queue.append((i, j))
            f_lst[i][j] = 1

        if miro[i][j] == 'J':
            j_queue.append((i, j))
            j_lst[i][j] = 1

fire()
result = bfs()
print(result)