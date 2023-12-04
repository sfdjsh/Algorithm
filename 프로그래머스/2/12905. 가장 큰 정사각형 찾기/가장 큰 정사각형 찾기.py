def solution(board): 
    
    x = len(board)
    y = len(board[0])
    
    dp = [[0] * y for _ in range(x)]
    dp[0] = board[0]
    for i in range(x):
        dp[i][0] = board[i][0]
    
    for i in range(1, x):
        for j in range(1, y):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    
    return max(map(max, dp)) ** 2