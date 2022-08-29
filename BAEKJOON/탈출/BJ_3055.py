from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))
q = deque()

def bfs():
    while q:

        # 비버의 굴에 도착했으면 결과값 리턴
        if forest[Dx][Dy] == 'S':
            return visited[Dx][Dy]

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+di[i], y+dj[i]
            if 0 <= nx < R and 0 <= ny < C:
                # 물이 차있는 좌표의 다음 좌표도 물 채우고 q리스트에 추가
                if (forest[nx][ny] == '.' or forest[nx][ny] == 'S') and forest[x][y] == '*':
                    forest[nx][ny] = '*'
                    q.append([nx, ny])
                # 고슴도치의 이동 경로 만들어주기 (비버의 굴이 S가 되면 고슴도치가 갈 수 있다고 판단)
                elif (forest[nx][ny] == '.' or forest[nx][ny] == 'D') and forest[x][y] == 'S':
                    forest[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1     # 이동 거리 추가
                    q.append([nx, ny])

    return 'KAKTUS'     # 갈 수 없을 때

R, C = map(int, input().split())            # R은 행, C는 열
visited = [[0] * C for _ in range(R)]       # 거리 체크 리스트
forest = [list(input()) for _ in range(R)]
Dx, Dy = 0, 0

for i in range(R):
    for j in range(C):
        # 고슴도치 시작 좌표 q 리스트에 추가
        if forest[i][j] == 'S':
            q.append([i, j])

        # 비버의 굴 좌표 Dx, Dy에 할당
        if forest[i][j] == 'D':
            Dx, Dy = i, j

# 물이 차있는 지역 q 리스트에 추가
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            q.append([i, j])

print(bfs())