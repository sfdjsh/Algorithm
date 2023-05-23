from collections import deque

def solution(m, n, board):
    board = [list(i) for i in board]
    
    answer = 0
    
    # 2 * 2 블록이 있는지 확인하는 함수
    def check_block():
        check_board = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '0':
                    if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                        check_board.update({(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)})
        return check_board
    
    # 지워진 블록 후 위에 있는 블록을 아래로 떨어뜨리는 함수
    def re_board():
        for i_1 in range(m - 1, 0, -1):
            for j in range(n):
                if board[i_1][j] == '0':                    # 지워진 블록을 발견했을 때
                    for i_2 in range(i_1 - 1, -1, -1):
                        if board[i_2][j] != '0':            # 지워진 블록 위에 있는 블록과 바꾸기    
                            board[i_1][j] = board[i_2][j]
                            board[i_2][j] = '0'
                            break
    
    answer = 0
    
    while check_block():            # 지워지는 블록이 있을때까지 반복
        for x, y in check_block():
            board[x][y] = '0'       # 블록 지우기
            answer += 1             
        re_board()                  # 지워진 블록 채우기
    
    return answer
