from collections import deque

di, dj = ((1, -1, 0, 0), (0, 0, 1, -1)) # 상하좌우

def solution(maps):
    n = len(maps)                       # 행의 길이
    m = len(maps[0])                    # 열의 길이
    v = [[0] * m for _ in range(n)]     # 방문 체크 리스트

    q = deque()
    q.append([0, 0, 1])     # x, y, count
    while q:
        x, y, cnt = q.popleft()
        # 마지막 지점에 도착하면 count 리턴
        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < n and 0 <= dy < m:             # 다음 위치가 범위 내에 있을 때
                if not v[dx][dy] and maps[dx][dy] != 0: # 다음 위치가 방문하지 않았고, 갈 수 있는 길일 때
                    v[dx][dy] = 1                       # 방문 체크
                    q.append([dx, dy, cnt + 1])         # 다음위치, count+1

    return -1   # 도착 못할 경우 -1 리턴