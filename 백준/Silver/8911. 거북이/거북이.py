N = int(input())

di, dj = ((1, 0, -1, 0), (0, 1, 0, -1))     # 상 우 하 좌

for _ in range(N):
    square = [[0, 0]]

    turtle = list(input())
    arror = 0                   # 현재 방향
    now_x, now_y = 0, 0         # 현재 위치

    for t in turtle:
        if t == 'F':    # 앞으로 갈 때
            dx, dy = now_x + di[arror], now_y + dj[arror]
            if [dx, dy] not in square:      # square 리스트에서 이동한 위치가 없을 때
                square.append([dx, dy])
            now_x, now_y = dx, dy           # 현재 위치 갱신

        elif t == 'B':  # 뒤로 갈 때
            dx, dy = now_x - di[arror], now_y - dj[arror]
            if [dx, dy] not in square:      # square 리스트에서 이동한 위치가 없을 때
                square.append([dx, dy])
            now_x, now_y = dx, dy           # 현재 위치 갱신

        elif t == 'R':      # 오른쪽으로 방향 전환
            if arror == 3:
                arror = 0
            else:
                arror += 1

        elif t == 'L':      # 왼쪽으로 방향 전환
            if arror == 0:
                arror = 3
            else:
                arror -= 1

    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    for i, j in square:
        min_x, max_x = min(min_x, i), max(max_x, i)
        min_y, max_y = min(min_y, j), max(max_y, j)

    print(abs(max_x - min_x) * abs(max_y - min_y))      # 사각형 넓이 구하기
