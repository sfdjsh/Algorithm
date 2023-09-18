def solution(s):    
    answer = 0
    
    tmp1, tmp2 = 0, 0
    x = ''
    for i in range(len(s)):
        if i == len(s) - 1:
            answer += 1
            break
        
        if not x:
            tmp1 += 1
            x = s[i]                
        else:
            if s[i] == x:
                tmp1 += 1
            else:
                tmp2 += 1
        
        if tmp1 == tmp2:
            answer += 1
            tmp1, tmp2 = 0, 0
            x = ''
   
    return answer