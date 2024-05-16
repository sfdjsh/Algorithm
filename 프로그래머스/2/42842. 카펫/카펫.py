def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            width = [i, yellow // i]
            width.sort(reverse = True)
            if (width[0] + 2) * 2 + (width[1] * 2) == brown:
                answer = [width[0] + 2, width[1] + 2]
    
    return answer