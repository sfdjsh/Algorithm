def solution(k, score):
    answer = []
    
    lst = []
    for s in score:
        if len(lst) < k:
            lst.append(s)
        else:
            if s > min(lst):
                lst.remove(min(lst))
                lst.append(s)
                
        answer.append(min(lst))
    
    return answer