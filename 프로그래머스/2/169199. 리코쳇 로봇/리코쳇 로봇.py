from collections import deque

def solution(board):
    
    di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))
     
    board_x = len(board)
    board_y = len(board[0])
    visited = [[0] * board_y for _ in range(board_x)]
    
    sx, sy = 0, 0
    for i in range(len(board)):
        if 'R' in board[i]:
            sx, sy = i, board[i].index('R')
    
    q = deque()
    q.append([sx, sy, 0])
    visited[sx][sy] = 1
    while q:
        x, y, cnt = q.popleft()
        if board[x][y] == 'G':
            return cnt

        for i in range(4):
            dx, dy = x + di[i], y + dj[i]
            while True:
                if 0 <= dx < board_x and 0 <= dy < board_y and board[dx][dy] == 'D':
                    dx -= di[i]
                    dy -= dj[i]
                    break

                if dx < 0 or dx >= board_x or dy < 0 or dy >= board_y:
                    dx -= di[i]
                    dy -= dj[i]
                    break

                else:
                    dx += di[i]
                    dy += dj[i]

            if not visited[dx][dy]:
                q.append([dx, dy, cnt + 1])
                visited[dx][dy] = 1
                        
    return -1