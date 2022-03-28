T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # N은 행렬 크기, M은 돌을 놓는 횟수
    arr = [[0]*(N+1) for _ in range(N+1)]
    # 흑돌 초기 값 행렬에 넣기
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2][N//2+1] = arr[N//2+1][N//2] = 1

    # M만큼 반복
    for _ in range(M):
        si, sj, c = map(int, input().split())   # x좌표, y좌표, 바둑돌 색깔
        arr[si][sj] = c
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):   # 상하좌우 대각선 순회
            lst = []
            for k in range(1, N+1): # 행렬 탐색
                ni,nj = si+di*k, sj+dj*k    # 다음 좌표 값
                if 0 < ni <= N and 0 < nj <= N:     # 다음 좌표가 범위 내에 있을 때
                    if arr[ni][nj] == 0:            # 바둑돌이 없으면 다음 방향으로
                        break
                    elif arr[ni][nj] == c:          # 같은 색의 돌이 나오면 그 사이에 모든 바둑돌 같은 색으로 바꾸기
                        for ci,cj in lst:
                            arr[ci][cj] = c
                        break
                    else:                           # 다른 색의 돌이 나오면 lst에 추가
                        lst.append((ni,nj))
                else:                               # 범위 밖이면 다음 방향으로
                    break

    b_cnt = w_cnt = 0
    for i in arr:
        b_cnt += i.count(1)         # 흑돌 개수
        w_cnt += i.count(2)         # 흰돌 개수
    print(f'#{tc} {b_cnt} {w_cnt}')
