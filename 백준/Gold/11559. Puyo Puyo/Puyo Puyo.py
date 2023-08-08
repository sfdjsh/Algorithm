from collections import deque

di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))

def bfs(sx, sy, color):

    tmp = 0
    lst = []
    visited = [[0] * 6 for _ in range(12)]
    visited[sx][sy] = 1

    q = deque()
    q.append((sx, sy))
    lst.append([sx, sy])

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < 12 and 0 <= dy < 6 and not visited[dx][dy] and puyo[dx][dy] == color:
                visited[dx][dy] = 1
                q.append((dx, dy))
                lst.append([dx, dy])


    if len(lst) >= 4:
        tmp = 1
        for i, j in lst:
            puyo[i][j] = '.'
        return tmp

def delete():
    for k in range(6):
        for i in range(11, -1, -1):
            for j in range(i - 1, -1, -1):
                if puyo[i][k] == '.' and puyo[j][k] != '.':
                    puyo[i][k] = puyo[j][k]
                    puyo[j][k] = '.'
                    break

answer = 0
puyo = []
for _ in range(12):
    arr = list(input())
    puyo.append(arr)

while True:
    flag = False

    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] != '.':
                if bfs(i, j, puyo[i][j]) == 1:
                    flag = True


    if flag:
        answer += 1
        delete()
    else:
        break

print(answer)
