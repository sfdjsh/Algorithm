def solution(arr):
    answer = 1
    
    def check_lcm(a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
        return 1
    
    for n in arr:
        answer = answer * n // check_lcm(answer, n)
        
    return answer
