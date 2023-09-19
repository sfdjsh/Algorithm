def solution(number, limit, power):
    answer = 0
    
    # 약수 개수 구하는 함수
    def prime(n):
        cnt = 0                 # 약수의 개수
        if n == 1:              # 숫자가 1이면 1리턴
            return 1
        if n == 2 or n == 3:    # 숫자가 2나 3이면 2 리턴
            return 2
        
        for i in range(1, int(n**(1/2)) + 1):   # 숫자 3부터 약수의 개수 구하기
            if n % i == 0:      # 약수 판별
                if i * i == n:  # 약수가 하나일 때, ex) 25 = 5 * 5
                    cnt += 1
                else:           # 약수가 짝지어져있을때, ex) 30 = 5 * 6
                    cnt += 2
            
            if cnt > limit:     # 약수의 개수가 제한수치보다 크면 공격력(power) 리턴
                return power
        
        return cnt              # 아니면 약수의 개수 리턴
            
    for n in range(1, number + 1):
        answer += prime(n)
    
    return answer