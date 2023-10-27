def solution(n):
    answer = 0
    
    thr_num = []
    
    while n >= 1:
        thr_num.append(n % 3)
        n = n // 3
    
    tmp = 1
    for i in range(len(thr_num) - 1, -1, -1):
        if thr_num[i]:
            answer += thr_num[i] * tmp
        tmp *= 3
    
    return answer