N = int(input())

dp = [float('inf')] * N
dp[0] = 0
jump = []

for i in range(N - 1):
    j_1, j_2 = map(int, input().split())
    jump.append([j_1, j_2])

    if i + 1 < N:
        dp[i + 1] = min(dp[i + 1], dp[i] + j_1)
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + j_2)

K = int(input())
dp_min = dp[-1]
for i in range(3, N):
    e, dp1, dp2 = dp[i-3] + K, 1e9, 1e9
    for j in range(i, N - 1):
        if i + 1 < N:
            dp1 = min(dp1, e+jump[j][0])
        if i + 2 < N:
            dp2 = min(dp2, e+jump[j][1])

        e, dp1, dp2 = dp1, dp2, 1e9

    dp_min = min(dp_min, e)

print(dp_min)
