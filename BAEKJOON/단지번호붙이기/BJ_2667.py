from collections import deque
di, dj = ((-1,1,0,0), (0,0,-1,1))

def BFS(i, j):
    q = deque()
    q.append([i, j])
    cnt = 1
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
                if arr[dx][dy]:
                    cnt += 1
                    visited[dx][dy] = 1
                    q.append([dx, dy])

    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited= [[0] * N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
           result.append(BFS(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
