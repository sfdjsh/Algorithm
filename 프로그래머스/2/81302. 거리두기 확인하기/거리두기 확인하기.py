from collections import deque

def solution(places):
    answer = []
    di, dj = ((1, -1, 0, 0), (0, 0, -1, 1))
    
    def check_keep_dis(x, y):
        
        visited = [[0] * 5 for _ in range(5)]
        
        q = deque()
        q.append([x, y, 0])
        while q:
            x, y, cnt = q.popleft()
            if cnt >= 2:
                continue
            
            visited[x][y] = 1
            for i in range(4):
                dx, dy = x + di[i], y + dj[i]
                if 0 <= dx < 5 and 0 <= dy < 5 and not visited[dx][dy]:
                    if place[dx][dy] == 'P' and cnt < 2:
                        return 0
                    
                    if place[dx][dy] == 'O':
                        q.append([dx, dy, cnt + 1])
        
        return 1
    
    answer = []
    
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])
        
        if not people:
            answer.append(1)
            continue
        
        flag = 1
        for x, y in people:
            if not check_keep_dis(x, y):
                flag = 0
                break
        
        answer.append(flag)
    
    return answer