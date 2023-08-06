def solution(dartResult):
    answer = 0
    
    stack = []
    num = ''
    for d in dartResult:
        # 다트의 숫자 판별
        if d.isdigit():
            num += d
        elif num:
            stack.append(int(num))
            num = ''
        
        # 더블일 때
        if d == 'D':
            double = stack.pop(-1)
            stack.append(double ** 2)

        # 트리플일 때
        if d == 'T':
            triple = stack.pop(-1)
            stack.append(triple ** 3)

        # 스타상일 때
        if d == '*':
            if len(stack) >= 2:     # 스타상의 숫자가 2개일 때
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b * 2)
                stack.append(a * 2)
            else:                   # 스타상의 숫자가 1개일 때
                a = stack.pop(-1)
                stack.append(a * 2)

        # 아차상일 때
        if d == '#':
            a = stack.pop(-1)
            stack.append(a * -1)
    
    answer = sum(stack)
    
    
    return answer