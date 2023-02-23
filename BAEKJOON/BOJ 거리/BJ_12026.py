N = int(input())
boj = list(input())

dp = [float('INF')] * N
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if boj[j] == 'B' and boj[i] == 'O':
            dp[i] = min(dp[i], dp[j] + ((i - j) ** 2))
        elif boj[j] == 'O' and boj[i] == 'J':
            dp[i] = min(dp[i], dp[j] + ((i - j) ** 2))
        elif boj[j] == 'J' and boj[i] == 'B':
            dp[i] = min(dp[i], dp[j] + ((i - j) ** 2))

if dp[N-1] != float('INF'):
    print(dp[N-1])
else:
    print(-1)