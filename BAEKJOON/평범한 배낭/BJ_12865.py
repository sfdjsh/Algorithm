N, K = map(int, input().split())

thing = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    thing.append([W, V])

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[N][K])

