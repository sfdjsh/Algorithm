N = int(input())

T, P = [], []
dp = [0] * (N + 1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

tmp = 0
for i in range(N):
    tmp = max(tmp, dp[i])
    if i + T[i] <= N:
        dp[i + T[i]] = max(tmp + P[i], dp[i + T[i]])

print(max(dp))