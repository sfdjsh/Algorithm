from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))

def bfs():
    q = deque()
    q.append((s,e))
    v[s][e] = 1
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                if arr[ni][nj]:
                    v[ni][nj] = 1
                    arr[ni][nj] = arr[ci][cj] + 1
                    q.append((ni,nj))

    for i in range(N):
        for j in range(M):
            if arr[i][j] and not v[i][j]:
                arr[i][j] = -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

s = e = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            arr[i][j] = 0
            s,e = i,j
            break
bfs()

for i in arr:
    print(*i)