from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))   # 상하좌우

def bfs(si, sj):
    global result   # 최단 거리 값
    v = [[0]*M for _ in range(N)]
    v[si][sj] = 1
    q = deque()
    q.append((si,sj))
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0<= ni < N and 0<= nj < M and arr[ni][nj] == 'L':    # 범위 내에 있고 다음위치가 육지일 때
                if v[ni][nj] == 0:  # 방문하지 않았을 때
                    v[ni][nj] = v[ci][cj] + 1   # 다음 위치 = 처음 위치 + 1
                    result = max(result, v[ni][nj])     # 가장 먼 거리 값 리셋
                    q.append((ni,nj))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

result = 0
# 두 곳의 육지의 가장 먼 최단거리를 찾아야하기 때문에 육지인 모든 위치를 bfs 탐색
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i,j)

print(result-1)
