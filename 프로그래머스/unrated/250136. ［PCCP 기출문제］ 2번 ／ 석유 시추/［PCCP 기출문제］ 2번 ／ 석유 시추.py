from collections import deque
import copy

def solution(land):
    
    def bfs(sx, sy):    
        lst = []                # 석유 위치 담을 리스트       
        
        q = deque()
        q.append((sx, sy))
        cnt = 1         
        land[sx][sy] = 0
        lst.append(sy)
        
        # bfs 시작
        while q:
            x, y = q.popleft()
            for i in range(4):
                dx, dy = x + di[i], y + dj[i]
                if 0 <= dx < x_len and 0 <= dy < y_len and land[dx][dy]:
                    land[dx][dy] = 0
                    q.append((dx, dy))
                    cnt += 1
                    if dy not in lst:
                        lst.append(dy)
                
        # 같은 열에 있는 석유 덩어리는 land_lst의 행에 중복 허용하지 않음            
        for j in lst:
            land_lst[j] += cnt

    answer = 0
    
    di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))     # 상, 하, 좌, 우
    
    x_len = len(land)
    y_len = len(land[0])
    
    land_lst = [0] * y_len          # 행 기준 석유의 갯수 담을 리스트
    
    for i in range(x_len):
        for j in range(y_len):
            if land[i][j] == 1:
                bfs(i, j)           # bfs 실행
    
    return max(land_lst)            # 제일 많은 석유 갯수 구하기