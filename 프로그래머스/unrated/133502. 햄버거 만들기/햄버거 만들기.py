def solution(ingredient):
    answer = 0
    
    buger = [1, 2, 3, 1]
    idx = 0
    
    while idx <= len(ingredient) - 4:
        if ingredient[idx] != 1:
            idx += 1 
        else:
            tmp = ingredient[idx : idx + 4]
            if tmp == buger:
                answer += 1
                del ingredient[idx : idx + 4]
                if idx < 4:
                    idx = 0
                else:
                    idx -= 4
                    
            else:
                idx += 1
        
    return answer