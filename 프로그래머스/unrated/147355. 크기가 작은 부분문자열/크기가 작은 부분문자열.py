def solution(t, p):
    answer = 0
    
    t_len = len(t)
    p_len = len(p)
    
    idx = 0
    while idx <= t_len - p_len:
        tmp = t[idx : idx + p_len]
        if int(tmp) <= int(p):
            answer += 1
        
        idx += 1
    
    return answer