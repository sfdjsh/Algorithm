def solution(keymap, targets):
    answer = []
    
    for target in targets:
        result = 0
        flag = True
        for alpha in target:
            cnt = 100
            for key in keymap:
                if alpha in key:
                    tmp = key.index(alpha) + 1
                    cnt = min(tmp, cnt)
            if cnt == 100:
                answer.append(-1)
                flag = False
                break
            else:
                result += cnt
                
        if flag and result != 0:
            answer.append(result)
    
    return answer