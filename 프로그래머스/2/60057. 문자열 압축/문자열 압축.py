def solution(s):
    answer = 1000
    
    if len(s) == 1:
        return 1
    
    for unit in range(1, len(s) // 2 + 1):
        spt_str = list(s[i : i + unit] for i in range(0, len(s), unit))
        
        press_str = ""  
        cnt = 1
        for i in range(len(spt_str) - 1):
            if spt_str[i] == spt_str[i + 1]:
                cnt += 1
            else:
                if cnt > 1:
                    press_str += str(cnt) + spt_str[i]
                else:
                    press_str += spt_str[i]
                cnt = 1
        
        if cnt > 1:
            press_str += str(cnt) + spt_str[-1]
        else:
            press_str += spt_str[-1]
        
        answer = min(answer, len(press_str))
    
    return answer