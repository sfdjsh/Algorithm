def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        num1 = i // n + 1
        num2 = i % n + 1
        num = max(num1, num2)
        answer.append(num)
    
    return answer