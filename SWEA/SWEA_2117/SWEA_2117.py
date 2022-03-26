import sys
sys.stdin = open('input.txt')

di, dj = ((1, -1, 0, 0), (0, 0, 1, -1))     # 상하좌우


def bfs(si, sj):
    old = cnt = sol = 0     # old는 운영 영역의 크기, cnt = 집의 갯수, sol = 결과값
    visited = [[0]*N for _ in range(N)]     # 방문 기록 체크
    q = []
    q.append((si, sj))

    visited[si][sj] = 1                     # 시작점 방문 체크
    if arr[si][sj]:
        cnt += 1

    while q:
        ci, cj = q.pop(0)

        # K가 n일때마다 운영비용과 집 * 지불비용을 비교해 집의 최댓값을 구함.
        if old != visited[ci][cj]:
           old = visited[ci][cj]
           if cost[visited[ci][cj]] <= cnt * M and sol < cnt:
                sol = cnt

        # 상하좌우 순회하면서 범위 내에 방문하지 않았으면 q에 추가하고, 그 안에 집이 있으면 더해준다.
        for i in range(4):
            ni,nj = ci+di[i], cj+dj[i]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj))
                if arr[ni][nj] == 1:
                    cnt += 1
    return sol


cost = [0] + [k*k+(k-1)*(k-1) for k in range(1, 40)]    # N이 최대 20까지이므로, 모든 행렬을 다 돌기 위해서는 N*2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N이 행렬, M이 한 집당 지불할 수 있는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 행렬의 모든 지점을 돌면서 집의 갯수에 대한 최댓값 갱신
    for si in range(N):
        for sj in range(N):
            if ans <= bfs(si,sj):
                ans = bfs(si,sj)
    print(f'#{tc} {ans}')


