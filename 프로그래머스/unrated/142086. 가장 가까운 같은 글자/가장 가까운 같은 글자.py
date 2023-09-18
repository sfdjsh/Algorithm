def solution(s):
    answer = []
    
    dict = {}
    
    for idx, alpha in enumerate(s):
        if alpha not in dict:
            answer.append(-1)
            dict[alpha] = idx
        else:
            answer.append(idx - dict[alpha])
            dict[alpha] = idx
    
    return answer