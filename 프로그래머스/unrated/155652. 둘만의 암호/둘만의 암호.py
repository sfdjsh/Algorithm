def solution(s, skip, index):
    answer = ''
    
    for a in s:
        cnt = 0
        tmp = ord(a)
        while cnt < index:
            tmp += 1
            if tmp > 122:
                tmp = 97
            
            if chr(tmp) not in skip:
                cnt += 1

        answer += chr(tmp)
        
    return answer