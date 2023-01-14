from collections import deque

di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))

def BFS(x, y, color):
    q = deque()
    q.append((x, y))

    cnt = 1             # count 초기값
    visited[x][y] = 1   # 최초 방문 체크

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            # 다음 위치가 행렬 범위 안에 있고, 방문하지 않았고, 색이 같다면
            if 0 <= dx < M and 0 <= dy < N and not visited[dx][dy] and arr[dx][dy] == color:
                visited[dx][dy] = 1     # 방문 체크
                cnt += 1                # count 증가
                q.append((dx, dy))

    return cnt

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]

w_result = 0    # 우리의 병사 위력
b_result = 0    # 적군의 병사 위력

visited = [[0] * N for _ in range(M)]
color = 'W'     # 병사 색깔

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:      # 반복문을 돌면서 방문 안한 인덱스 체크
            if arr[i][j] == 'W':    # 색이 W인 병사, BFS
                color = 'W'
                w_result += BFS(i, j, color)**2     # N명이 뭉쳐있을 때는 N^2 의 위력
            else:                   # 색이 B인 병사, BFS
                color = 'B'
                b_result += BFS(i, j, color)**2     # N명이 뭉쳐있을 때는 N^2 의 위력

print(w_result, b_result)