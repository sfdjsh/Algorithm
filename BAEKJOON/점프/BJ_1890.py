N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break

        right = j + arr[i][j]
        under = i + arr[i][j]

        if right < N:
            dp[i][right] += dp[i][j]
        if under < N:
            dp[under][j] += dp[i][j]

print(dp[N-1][N-1])
