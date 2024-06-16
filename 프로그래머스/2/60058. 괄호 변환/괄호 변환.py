def blance_bket(p):
    open_cnt = 0
    close_cnt = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            open_cnt += 1
        else:
            close_cnt += 1
        if open_cnt == close_cnt:
            return p[:i + 1],  p[i + 1:]
    
def check_bket(u):
    stack = []
    for c in u:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    
    return True
            
def solution(p):
    if not p:
        return ""
    
    u, v = blance_bket(p)
    if check_bket(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        u = u[1: len(u) - 1]
        for c in u:
            if c == "(":
                answer += ")"
            else:
                answer += "("
                        
    return answer