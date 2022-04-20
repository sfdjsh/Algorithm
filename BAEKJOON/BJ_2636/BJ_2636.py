from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))

def bfs():
    q = deque()
    q.append((0,0))
    v[0][0] = 1
    cheese = 0

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0<= ni < N and 0<= nj < M and not v[ni][nj]:
                if arr[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))
                elif arr[ni][nj] == 1:
                    v[ni][nj] = 1
                    arr[ni][nj] = 0
                    cheese += 1
    return cheese

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = []
time = 0
while True:
    time += 1
    v = [[0] * M for _ in range(N)]
    cnt = bfs()
    result.append(cnt)
    if cnt == 0:
        break

print(time-1)
print(result[-2])