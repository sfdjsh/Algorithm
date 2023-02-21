N = int(input())

dp = [i for i in range(101)]
for i in range(7, 101):
    dp[i] = max(dp[i-3] * 2, dp[i-4] * 3, dp[i-5] * 4)

print(dp[N])
