# + 방향 분사하는 것 더하기
def plus(lst):
    p_total = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            total1 = lst[i][j]
            for k in range(1, M):
                for l in range(4):
                    ni = i + (di[l] * k)
                    nj = j + (dj[l] * k)
                    if 0 <= ni < N and 0 <= nj < N:
                        total1 += lst[ni][nj]
            if p_total < total1:    # 각 위치의 + 분사에 대한 최대값 구하기
                p_total = total1
    return p_total

# x 방향 분사하는 것 더하기
def x(lst):
    x_total = 0
    di = [-1, 1, 1, -1]
    dj = [1, 1, -1, -1]
    for i in range(N):
        for j in range(N):
            total2 = lst[i][j]
            for k in range(1, M):
                for l in range(4):
                    ni = i + (di[l] * k)
                    nj = j + (dj[l] * k)
                    if 0 <= ni < N and 0 <= nj < N:
                        total2 += lst[ni][nj]
            if x_total < total2:    # 각 위치의 x 분사에 대한 최대값 구하기
                x_total = total2
    return x_total


T = int(input())                                                # 테스트 케이스
for tc in range(1, T+1):
    N, M = map(int, input().split())                            # N은 NxN행렬, M은 분사크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2차원 행렬 생성

    print(f'#{tc} {max(plus(arr), x(arr))}')                    # +와 x방향의 최대값 출력