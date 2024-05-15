from itertools import permutations

def find_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
        
    return True
        
def solution(numbers):
    answer = 0
    comb = []
    for i in range(1, len(numbers) + 1):
        comb += list(permutations(numbers, i))
    
    num_lst = set()
    for c in comb:
        c = int(''.join(c))
        num_lst.add(c)
    
    for n in num_lst:
        if (find_prime(n)):
            answer += 1
    
    return answer