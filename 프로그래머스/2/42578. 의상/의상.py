from itertools import combinations

def solution(clothes):
    answer = 1
    
    cloth_type = {}
    
    for cloth in clothes:
        if cloth[1] not in cloth_type:
            cloth_type[cloth[1]] = [cloth[0]]
        else:
            cloth_type[cloth[1]] += [cloth[0]]
    
    for key in cloth_type:
        answer *= len(cloth_type[key]) + 1

    return answer - 1