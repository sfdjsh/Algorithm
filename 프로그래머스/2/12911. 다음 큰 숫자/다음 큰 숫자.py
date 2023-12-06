def solution(n):
    answer = 0
    
    one_cnt = bin(n).count('1')
    
    while True:
        n += 1
        tmp_cnt = bin(n).count('1')
        if one_cnt == tmp_cnt:
            answer = n
            break
    
    return answer