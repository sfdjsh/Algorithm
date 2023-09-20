def solution(food):
    answer = ''
    
    first = []
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            first.append(str(i))
            
    end = sorted(first, reverse = True)
    
    answer += ''.join(first) + '0' + ''.join(end)
    
    return answer