from collections import deque
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현
def bfs():
    while queue:    # queue가 비어 있지 않을 때까지 반복
        x, y = queue.popleft()
        # 상하좌우 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 행렬을 벗어나지 않으면서 행렬의 인덱스값이 0이면
            if 0 <= nx < N and 0 <= ny < M:
                if not arr[nx][ny]:
                    queue.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1 # 상하좌우 1씩 더하기

# 결과값 출력
def result():
    answer = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:  # 사과가 익지 않은 게 있으므로 -1 출력
                print(-1)
                return
            else:
                if answer < arr[i][j]:  # 행렬의 최대값 구하기
    print(answer-1)

M, N = map(int, input().split())    # N은 행, M은 열
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
# 사과 위치를 찾고 큐 리스트에 추가
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))

bfs()
result()




