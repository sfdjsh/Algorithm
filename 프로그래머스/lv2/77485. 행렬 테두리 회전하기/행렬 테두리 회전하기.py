def solution(rows, columns, queries):
    answer = []
    
    arr = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]    # 2차원 배열 생성
    
    for query in queries:        
        s_x, s_y = query[0] - 1, query[1] - 1
        e_x, e_y = query[2] - 1, query[3] - 1
        
        min_num = arr[s_x][s_y]     # 최소값 구하는 변수
        f_value = min_num           # 초기값
        
        # 아래에서 위
        for i in range(s_x, e_x):
            tmp = arr[i + 1][s_y] 
            arr[i][s_y] = tmp
            min_num = min(min_num, tmp)
        
        # 오른쪽에서 왼쪽
        for i in range(s_y, e_y):
            tmp = arr[e_x][i + 1]
            arr[e_x][i] = tmp
            min_num = min(min_num, tmp)
        
        # 위에서 아래
        for i in range(e_x, s_x, -1):
            tmp = arr[i - 1][e_y]
            arr[i][e_y] = tmp
            min_num = min(min_num, tmp)
        
        # 왼쪽에서 오른쪽
        for i in range(e_y, s_y, -1):
            tmp = arr[s_x][i - 1]
            arr[s_x][i] = tmp
            min_num = min(min_num, tmp)
        
        arr[s_x][s_y + 1] = f_value         # 숫자가 겹치는 현상을 해결하기 위해
        
        answer.append(min_num)
    
    return answer