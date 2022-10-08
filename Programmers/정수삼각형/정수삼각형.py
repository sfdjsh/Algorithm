def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            # 왼쪽 대각선일 때
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            # 오른쪽 대각선일 때
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            # 그 외 (왼쪽 한 칸, 오른쪽 한 칸 중 제일 큰 값)
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    answer = max(triangle[-1])  # 마지막 줄에서 최댓값 리턴
    return answer