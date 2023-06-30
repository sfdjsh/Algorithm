from itertools import permutations


def solution(expression):
    
    # +, -, * 연산 함수
    def operation(num1, num2, op):
        if op == '*':
            return str(int(num1) * int(num2))
        if op == '-':
            return str(int(num1) - int(num2))
        if op == '+':
            return str(int(num1) + int(num2))

    def func_cal(cal):
        cal_lst = []
        tmp = ''
        for c in expression:        # 숫자와 연산 분해과정
            if c.isdigit():
                tmp += c
            else:
                cal_lst.append(tmp)
                cal_lst.append(c)
                tmp = ''

        cal_lst.append(tmp)


        for c in cal:
            stack = []
            while cal_lst:
                tmp = cal_lst.pop(0)
                if tmp == c:
                    stack.append(operation(stack.pop(), cal_lst.pop(0), tmp))   # 연산 순위에 따른 계산
                else:
                    stack.append(tmp)
            cal_lst = stack
        
        return abs(int(*cal_lst))   # 절대값 계산

    answer = 0

    cals = list(permutations(['*', '-', '+'], 3))   # 연산 순열 리스트       

    for cal in cals:
        answer = max(answer, func_cal(cal))     # 각 연산 규칙을 통해 최대값 구하기

    return answer