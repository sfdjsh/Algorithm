def solution(s):
    answer = 0
    s = list(s)
    
    def check(s):
        stack = []          # 열린 괄호 넣는 공간
        
        for bracket in s: 
            # 열린 괄호 나왔을 때
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            
            # 닫힌 괄호 나왔을 때
            if bracket == ')':  
                if not stack or stack.pop() != '(':
                    return False
                
            if bracket == ']':
                if not stack or stack.pop() != '[':
                    return False
                
            if bracket == '}':
                if not stack or stack.pop() != '{':
                    return False
        
        if not stack:
            return True
            
    
    for _ in range(len(s)):
        if check(s):
            answer += 1
            
        s.append(s.pop(0))      # 괄호 회전
    
    return answer