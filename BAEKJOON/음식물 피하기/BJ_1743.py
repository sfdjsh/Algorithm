from collections import deque

di, dj = ((-1,1,0,0) , (0,0,-1,1))

def BFS(i, j):
    q = deque()
    q.append([i, j])
    arr[i][j] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < N and 0 <= dy < M and arr[dx][dy] == -1:
                cnt += 1
                q.append([dx, dy])
                arr[dx][dy] = 0

    return cnt

N, M, K = map(int, input().split())

arr = [[0] * M for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())
    arr[N - x][y - 1] = -1

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            trash = BFS(i, j)
            if result < trash:
                result = trash
print(result)
