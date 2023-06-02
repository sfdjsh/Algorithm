def solution(places):
    answer = []
    
    # 응시자 간의 거리두기를 지키는지 여부를 체크하는 함수
    def check_place(p, x, y):
        if 0 <= x + 1 < 5 and 0 <= y < 5 and p[x + 1][y] == 'P':
            return 0
        
        if 0 <= x < 5 and 0 <= y + 1 < 5 and p[x][y + 1] == 'P':
            return 0
        
        if 0 <= x < 5 and 0 <= y + 2 < 5 and p[x][y + 2] == 'P':
            if p[x][y + 1] != 'X':
                return 0
        
        if 0 <= x < 5 and 0 <= y - 1 < 5 and p[x][y - 1] == 'P':
            return 0
        
        if 0 <= x < 5 and 0 <= y - 2 < 5 and p[x][y - 2] == 'P':
            if p[x][y - 1] != 'X':
                return 0        
        
        if 0 <= x + 1 < 5 and 0 <= y + 1 < 5 and p[x + 1][y + 1] == 'P':
            if p[x + 1][y] != 'X' or p[x][y + 1] != 'X':
                return 0
            
        if 0 <= x + 1 < 5 and 0 <= y - 1 < 5 and p[x + 1][y - 1] == 'P':
            if p[x + 1][y] != 'X' or p[x][y - 1] != 'X':
                return 0
        
        if 0 <= x + 2 < 5 and 0 <= y < 5 and p[x + 2][y] == 'P':
            if p[x + 1][y] != 'X':
                return 0    
        
        return 1    
    
    def place(p):
        result = 1
        for i in range(5):
            for j in range(5):
                # 각 대기실 별 응시자 위치로 check_place 함수 실행
                if p[i][j] == 'P':
                    if not check_place(p, i, j):
                        return 0    # 거리두기를 지키고 있지 않으면 0 리턴
                    
        return 1    # 거리두기를 지키고 있다면 1 리턴
    
    for p in places:
        answer.append(place(p))
        
    return answer