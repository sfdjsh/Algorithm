N, S, M = map(int, input().split())
volume = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(N):
    for j in range(M + 1):
        if dp[i][j] == 1:
            if j + volume[i] <= M:
                dp[i + 1][j + volume[i]] = 1
            if j - volume[i] >= 0:
                dp[i + 1][j - volume[i]] = 1

print(dp)
result = -1
for j in range(M, -1, -1):
    if dp[N][j] == 1:
        result = j
        break

print(result)