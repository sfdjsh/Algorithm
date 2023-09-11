def solution(keymap, targets):
    answer = []
    
    alpha = {}
    
    for key in keymap:
        for i, a in enumerate(key):
            if a in alpha:
                alpha[a] = min(alpha[a], i + 1)
            else:
                alpha[a] = i + 1
    
    for target in targets:
        cnt = 0
        for t in target:
            if t in alpha:
                cnt += alpha[t]
            else:
                cnt = -1
                break
        
        if cnt < 0:
            answer.append(-1)
        else:
            answer.append(cnt)
    
    return answer