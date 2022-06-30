from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))

def bfs(S, X, Y):
    time = 0            # 시간 초기값
    q = deque(virus)
    while q:
        if time == S:   # 시간이 다되면 break
            break
        # q의 길이만큼 for문
        for _ in range(len(q)):
            result, x, y = q.popleft()  # 바이러스 번호, x좌표, y좌표
            for i in range(4):
                ni, nj = x + di[i], y+dj[i]
                if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                    arr[ni][nj] = result
                    q.append((result, ni, nj))
        time += 1
    return arr[X-1][Y-1]    # 결과 도출

N, K = map(int, input().split())        # NxN , 최대 바이러스 번호
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())     # 시간 제한, 찾아야 할 : x좌표, y좌표

# 바이러스 번호가 있는 것을 리스트에 담기
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            virus.append((arr[i][j], i, j)) # 바이러스 번호, x좌표, y좌표
virus.sort()    # 바이러스 번호 오름차순 정렬

print(bfs(S, X, Y))
