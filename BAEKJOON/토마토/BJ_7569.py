from collections import deque

dx, dy, dz = ((-1,1,0,0,0,0), (0,0,-1,1,0,0), (0,0,0,0,-1,1))   # 상,하,좌,우,위,아래

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]   # 3차원 배열 생성

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 익은 토마토 q에 추가
            if arr[i][j][k] == 1:
                q.append((i,j,k))

# bfs 구현
while q:
    z, x, y = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and not arr[nz][nx][ny]:
            q.append((nz, nx, ny))
            arr[nz][nx][ny] = arr[z][x][y] + 1  # 익은 토마토 체크 and 날짜 체크

result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 익지 않은 토마토가 있다면 -1 출력하고 바로 종료
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, arr[i][j][k])  # 토마토가 익는 날짜 갱신

print(result - 1)   # 처음 arr값이 1이였기 때문에 -1 해서 결과 출력