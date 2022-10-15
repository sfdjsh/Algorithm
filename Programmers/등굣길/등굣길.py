def solution(m, n, puddles):
    path = [[0] * (m + 1) for _ in range(n + 1)]  # 길 리스트 만들기
    path[1][1] = 1  # 시작점

    # 물 웅덩이 체크
    for i, j in puddles:
        path[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 물 웅덩이가 있는 곳은 갈 수 없으므로 0으로 초기화
            if path[i][j] == -1:
                path[i][j] = 0
            else:
                path[i][j] += path[i - 1][j] + path[i][j - 1]

    return path[n][m] % 1000000007