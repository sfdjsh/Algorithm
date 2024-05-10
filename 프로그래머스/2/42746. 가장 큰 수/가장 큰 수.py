def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    numbers.sort(key = lambda x:x*3, reverse = True)
    
    return str(int(''.join(numbers)))