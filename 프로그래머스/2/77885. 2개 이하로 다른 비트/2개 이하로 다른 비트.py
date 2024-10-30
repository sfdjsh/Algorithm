def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            bin_n = '0' + bin(n)[2:]
            idx = bin_n.rfind('0')
            bin_n = list(bin_n)
            bin_n[idx] = '1'
            bin_n[idx + 1] = '0'
            answer.append(int(''.join(bin_n), 2))
    
    return answer