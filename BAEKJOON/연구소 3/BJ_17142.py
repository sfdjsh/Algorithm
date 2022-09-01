from itertools import combinations
from collections import deque

dx, dy = ((-1,1,0,0), (0,0,-1,1))

def bfs(b):
    q = deque(b)
    cnt = 0     # 거리 변수 설정

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 비활성 바이러스이고 방문 하지 않았을 때
                if arr[nx][ny] == 2 and v[nx][ny] == -1:
                    q.append([nx, ny])
                    v[nx][ny] = v[x][y] + 1     # 결과에는 반영 안되지만 거리는 갱신해줘야함. ex) 예제 입력 7

                # 활성 바이러스이고 방문 하지 않았을 때
                elif arr[nx][ny] == 0 and v[nx][ny] == -1:
                    q.append([nx, ny])
                    v[nx][ny] = v[x][y] + 1
                    cnt = max(cnt, v[nx][ny])   # 거리 변수 갱신

    wall_check = 0      # v의 벽(-1) 체크
    for i in range(N):
        for j in range(N):
            if v[i][j] == -1:
                wall_check += 1

    if wall_check == wall:  # 벽의 갯수가 같으면 벽을 제외한 모든 바이러스는 다 전염됌
        return cnt
    else:
        return 3000


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []  # 바이러스 위치 담을 리스트
wall = 0    # 벽의 갯수
for i in range(N):
    for j in range(N):
     if arr[i][j] == 2:
         virus.append([i, j])
     elif arr[i][j] == 1:
        wall += 1

result = 3000
for b in list(combinations(virus, M)):
    v = [[-1] * N for _ in range(N)]    # BFS를 돌리면서 v의 -1 갯수와 wall 갯수가 같으면 모든 구역 바이러스 
    for x,y in b:
        v[x][y] = 0     # 처음 위치는 결과값에 반영이 되지 않으므로 0으로 설정
    result = min(result, bfs(b))

if result == 3000:  # bfs를 돌고 값이 바뀌지 않았으면 모든 빈 칸을 바이러스로 퍼뜨릴 수 없음
    print(-1)
else:
    print(result)