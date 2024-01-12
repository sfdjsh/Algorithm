def solution(s):
    
    stack = []
    
    for alpha in s:
        if len(stack) > 0 and stack[-1] == alpha:
            stack.pop(-1)
        else:
            stack.append(alpha)
    
    if stack:
        return 0
    else:
        return 1
    
    
