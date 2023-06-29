def solution(n):
    di, dj = ((1, 0, -1), (0, 1, -1))
    
    answer = [[0] * i for i in range(1, n + 1)]
    answer[0][0] = 1
    
    max_num = 0
    for i in range(1, n + 1):
        max_num += i
    
    num, idx = 2, 0
    sx, sy = 0, 0
    while num <= max_num:
        dx, dy = sx + di[idx], sy + dj[idx]
        
        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            idx = (idx + 1) % 3
        
        elif 0 <= dx < n and 0 <= dy < n:
            if answer[dx][dy] != 0:
                idx = (idx + 1) % 3
                
            else:
                answer[dx][dy] = num
                num += 1
                sx, sy = dx, dy
    
    result = []
    for i in answer:
        for j in i:
            result.append(j)
    
    return result