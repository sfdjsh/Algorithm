from itertools import permutations
    
def solution(expression):    
    
    def func_oper(num1, num2, op):
        if op == '*':
            return num1 * num2
        elif op == '-':
            return num1 - num2
        elif op == '+':
            return num1 + num2
        
    def func_max(op):
        expre_split = []
        num = ''
        for c in expression:
            if c.isdigit():
                num += c
            else:
                expre_split.append(int(num))
                expre_split.append(c)
                num = ''
        if num:
            expre_split.append(int(num))
        
        for o in op:
            stack = []
            while expre_split:
                tmp = expre_split.pop(0)
                if tmp == o:
                    stack.append(func_oper(stack.pop(-1), expre_split.pop(0), o))
                else:
                    stack.append(tmp)
            expre_split = stack
        
        return abs(expre_split[0])
    
    answer = 0
    operation = list(permutations(['-', '+', '*'], 3))
    for op in operation:
        answer = max(answer, func_max(op))
                
    return answer