from collections import deque

di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))

# bfs 함수
def bfs(sx, sy, color):
    tmp = 0
    
    lst = []
    lst.append([sx, sy])
    
    visited = [[0] * 6 for _ in range(12)]
    visited[sx][sy] = 1

    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            if 0 <= dx < 12 and 0 <= dy < 6 and not visited[dx][dy] and puyo[dx][dy] == color:
                visited[dx][dy] = 1
                q.append((dx, dy))
                lst.append([dx, dy])

    if len(lst) >= 4:           # 같은 뿌요가 4개 이상일 때
        tmp = 1
        for i, j in lst:
            puyo[i][j] = '.'    # 뿌요 터트리기
        return tmp

# 터진 뿌요 자리에, 위에서 아래로 떨어뜨리기
def down():
    for k in range(6):
        for i in range(11, -1, -1):
            for j in range(i - 1, -1, -1):
                if puyo[i][k] == '.' and puyo[j][k] != '.':
                    puyo[i][k] = puyo[j][k]
                    puyo[j][k] = '.'
                    break

answer = 0

puyo = []
for _ in range(12):
    arr = list(input())
    puyo.append(arr)

while True:
    flag = False    # 연쇄 판별 변수
    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] != '.':
                if bfs(i, j, puyo[i][j]) == 1:  # 색깔 뿌요 bfs 실행
                    flag = True

    if flag:            # 터진 뿌요가 있을 때
        answer += 1
        down()          # 뿌요 내리기
    else:               # 터진 뿌요가 없으면 while문 종료
        break

print(answer)