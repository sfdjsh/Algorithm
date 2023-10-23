def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        tmp = 0
        for i in range(1, int(num**(1/2)) + 1):
            if num % i == 0:
                if i * i == num:
                    tmp += 1
                else:
                    tmp += 2
        
        if tmp % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer