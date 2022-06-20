di, dj = ((0, 1, 1), (1, 1, 0)) # 파이프 방향

def dfs(x, y, arrow):
    global result
    # arrow = 0일 때 가로방향, arrow = 1일 때 대각선 방향, arrow = 2일때 세로방향

    # 도착 지점에 도달했을 때
    if x == N-1 and y == N-1:
        result += 1
        return

    # 가로 방향으로 갈 수 있을 때
    if arrow == 0 or arrow == 1:
        if y + 1 < N and arr[x][y+1] == 0:
            dfs(x, y+1, 0)

    # 세로 방향으로 갈 수 있을 때
    if arrow == 1 or arrow == 2:
        if x + 1 < N and arr[x+1][y] == 0:
            dfs(x+1, y, 2)

    # 대각선 방향으로 갈 수 있을 때
    if x + 1 < N and y + 1 < N:
        if arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0:
            dfs(x+1, y+1, 1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0      # 최종 결과 값
dfs(0, 1, 0)    # 처음 위치와 방향
print(result)

