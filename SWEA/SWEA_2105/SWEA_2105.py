import sys
sys.stdin = open('input.txt')

# 마름모 방향 순회
di, dj = (1,1,-1,-1), (-1,1,1,-1)


def dfs(d, ci, cj, v, cnt):
    global si, sj, ans
    # 마름모 방향 형성되면 종료
    if d > 3:
        return
    
    # 마름모 방향이 되었을 때 현재위치와 시작위치가 같으면, 디저트의 최대 갯수 갱신
    if d == 3 and ci == si and cj == sj and ans < cnt:
        ans = cnt
        return
    
    # 가는 방향을 그대로 유지할껀지, 꺽을껀지 결정
    for i in range(d, d+2):
        ni, nj = ci+di[d], cj+dj[d]
        # 행렬 범위 안에 있고 같은 디저트 카페에 들리지 않았다면 재귀 반복
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            dfs(i, ni, nj, v+[arr[ni][nj]], cnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1    # 디저트 초기값
    # 모든 행렬 순회
    for si in range(N):
        for sj in range(N):
            dfs(0, si, sj, [], 0)

    print(f'#{tc} {ans}')
