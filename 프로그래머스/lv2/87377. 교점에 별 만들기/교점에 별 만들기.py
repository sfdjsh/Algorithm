def solution(line):
    
    star_x = []
    star_y = []
    for i in range(len(line) - 1):
        for j in range(i, len(line)):
            A, B, C, D, E, F = line[i][0], line[i][1], line[j][0], line[j][1], line[i][2], line[j][2]
            if ((A * D) - (B * C)) != 0:    # 두 직선 AD-BC 가 0이 아닐때 
                x = (((B * F) - (E * D)) / ((A * D) - (B * C))) # x = (BF - ED) / (AD - BC)
                y = (((E * C) - (A * F)) / ((A * D) - (B * C))) # y = (EC - AF) / (AD - BC)
                
                if x == int(x) and y == int(y):     # x점과 y점의 정수 교점 찾기
                    star_x.append(int(x))
                    star_y.append(int(y))
    
    min_x, max_x = min(star_x), max(star_x)         # x 교점 최소값, 최대값
    min_y, max_y = min(star_y), max(star_y)         # y 교점 최소값, 최대값
    
    answer = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]  # 격자판 생성
    
    for x, y in zip(star_x, star_y):
        answer[y - min_y][x - min_x] = '*'  # 교점 지점 *로 변경
    
    answer.reverse()    # 격자판 뒤집기
    
    return [''.join(s) for s in answer]