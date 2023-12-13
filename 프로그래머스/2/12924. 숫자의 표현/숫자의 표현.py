def solution(n):
    answer = 0
    
    s_num = 1
    while s_num <= n:
        cnt = 0
        for i in range(s_num, n + 1):
            cnt += i
            if cnt == n:
                answer += 1
                break
            
            if cnt > n:
                break
            
        s_num += 1
    
    return answer