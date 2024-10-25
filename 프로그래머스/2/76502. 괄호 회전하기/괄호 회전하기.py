def solution(s):
    
    def check_bracket(bracket):
        stack = []
        flag = True
        
        for b in bracket:
            if b in ['(', '[', '{']:
                stack.append(b)
            
            if stack and flag:
                if b == ')' and stack.pop(-1) != '(':
                    flag = False
                if b == ']' and stack.pop(-1) != '[':
                    flag = False
                if b == '}' and stack.pop(-1) != '{':
                    flag = False
            else:
                flag = False
        
        if stack:
            flag = False
        
        return flag
                    
    answer = 0
    s = list(s)
    for i in range(len(s)):
        first_str = s.pop(0)
        s.append(first_str)
        
        if check_bracket(s):
            answer += 1
    
    return answer