def solution(dirs):
    answer = []
        
    arr = [[0] * 11 for _ in range(11)]
    sx, sy = 5, 5
    for dir in dirs:
        dx, dy = sx, sy
        if dir == "U":
            dx, dy = dx - 1, dy
        elif dir == "L":
            dx, dy = dx, dy - 1
        elif dir == "R":
            dx, dy = dx, dy + 1
        elif dir == "D":
            dx, dy = dx + 1, dy
        
        if 0 <= dx <= 10 and 0 <= dy <= 10:
            answer.append([sx, sy, dx, dy])
            answer.append([dx, dy, sx, sy])
            sx, sy = dx, dy
            
    answer = list(set(map(tuple, answer)))
    
    return len(answer) // 2