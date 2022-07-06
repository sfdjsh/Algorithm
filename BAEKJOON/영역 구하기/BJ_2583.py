from collections import deque

dx, dy = ((-1,1,0,0), (0,0,-1,1))

def bfs(i, j):
    q = deque()
    q.append((i, j))
    quad[i][j] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and not quad[nx][ny]:
                q.append((nx, ny))
                quad[nx][ny] = 1    # 방문한 면적 체크하기
                cnt += 1    # 면적 더하기
    result.append(cnt)  # 총 면적 넣기

M, N, K = map(int, input().split())     # 행, 열, 사각형 수
quad = [[0]*N for _ in range(M)]    # 모눈종이

for _ in range(K):
    # 직사각형의 좌표를 모눈종이에 적용하기
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            quad[i][j] = 1

result = []
# 분리되어 나누어지는 영역을 출력하기 위해 bfs 탐색
for i in range(M):
    for j in range(N):
        if not quad[i][j]:
            bfs(i, j)

result.sort()   # 오름차순 정렬

print(len(result))
print(*result)
