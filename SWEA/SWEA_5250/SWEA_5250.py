di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))     # 상하좌우
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[100000]*N for _ in range(N)]   # 최대값 행렬
    dist[0][0] = 0  # 시작 위치

    q = []
    q.append((0,0))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            ni, nj = x+di[i], y+dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                temp = 1    # 이동 값
                # 높이 차 구현
                if arr[ni][nj] > arr[x][y]:
                    temp += arr[ni][nj] - arr[x][y]
                # 거리 갱신
                if dist[ni][nj] > dist[x][y] + temp:
                    dist[ni][nj] = dist[x][y] + temp
                    q.append((ni,nj))

    print(f'#{tc} {dist[N-1][N-1]}')