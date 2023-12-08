def solution(s):  
    stack = []
    for oc in s:
        if oc == '(':
            stack.append(oc)
        else:
            if not stack:
                return False
            
            stack.pop(-1)
    
    if stack:
        return False
    else:
        return True
