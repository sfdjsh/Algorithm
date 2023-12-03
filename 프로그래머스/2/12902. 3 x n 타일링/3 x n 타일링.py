def solution(n):
    answer = 0
    
    dp = [0] * (n + 1)
    dp[2], dp[4] = 3, 11
    
    if n % 2 != 0:
        return 0
    if n < 6:
        return dp[n]
    
    for i in range(6, n + 1, 2):
        dp[i] = (dp[i - 2] * 3 + sum(dp[2:i-2:2]) * 2 + 2) % 1000000007
    
    return dp[n]