def solution(s):
    answer = [0, 0]
    
    while len(s) > 1:
        answer[1] += s.count('0')
        remove_zero = s.replace('0', '')
        
        s = bin(len(remove_zero))[2:]
        answer[0] += 1

    return answer