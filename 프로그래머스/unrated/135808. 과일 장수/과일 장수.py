def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    idx = m - 1
    for _ in range(len(score) // m):  
        answer += score[idx] * m
        idx += m
    
    return answer