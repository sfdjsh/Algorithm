def solution(s):
    
    stack = []
    
    for i in range(len(s)):
        if not stack:               # 스택이 비어있으면 문자열 넣기
            stack.append(s[i])
        
        elif s[i] == stack[-1]:     # 짝지어진 같은 문자면 스택의 맨 마지막 요소 제거
            stack.pop(-1)
        
        else:                       # 둘 다 아니면 스택에 추가
            stack.append(s[i])   
    
    if stack:       # 스택에 문자가 있으면 0 리턴
        return 0
    else:           # 스택에 문자가 비어있으면 1 리턴
        return 1
    
    
