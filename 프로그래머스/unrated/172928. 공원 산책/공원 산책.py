def solution(park, routes):
    
    dx, dy = ((-1, 1, 0, 0), (0, 0, -1, 1)) # 상 하 좌 우
    
    answer = []
    
    x, y = 0, 0     # 현재 위치
    
    # 시작점 찾기
    n, m = len(park), len(park[0])      
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    for i in range(len(routes)):
        arrow, cnt = routes[i].split(' ')   # 방향, 이동 수
        
        tmp_x, tmp_y = x, y    
        
        # 북쪽으로 이동
        if arrow == 'N':
            for i in range(int(cnt)):
                x, y = x + dx[0], y + dy[0]
                # 범위를 벗어나거나, 장애물을 만났을 때
                if x < 0 or x >= n or y < 0 or y >= m or park[x][y] == 'X': 
                    x, y = tmp_x, tmp_y     # x, y 초기화
                    break
        
        # 남쪽으로 이동
        if arrow == 'S':
            for i in range(int(cnt)):
                x, y = x + dx[1], y + dy[1]
                if x < 0 or x >= n or y < 0 or y >= m or park[x][y] == 'X':
                    x, y = tmp_x, tmp_y
                    break
        
        # 서쪽으로 이동
        if arrow == 'W':
            for i in range(int(cnt)):
                x, y = x + dx[2], y + dy[2]
                if x < 0 or x >= n or y < 0 or y >= m or park[x][y] == 'X':
                    x, y = tmp_x, tmp_y
                    break
        
        # 동쪽으로 이동
        if arrow == 'E':
            for i in range(int(cnt)):
                x, y = x + dx[3], y + dy[3]
                if x < 0 or x >= n or y < 0 or y >= m or park[x][y] == 'X':
                    x, y = tmp_x, tmp_y
                    break  
                    
    answer = [x, y]
    
    return answer