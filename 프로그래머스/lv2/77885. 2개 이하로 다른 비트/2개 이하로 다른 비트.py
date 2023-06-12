def solution(numbers):
    answer = []
                 
    # 규칙 1. number가 짝수일 때, 그 다음 숫자 answer 리스트에 추가
    # 규칙 2. number가 홀수일 때, 뒤에서 0인 문자 1로 바꾸고, 그 뒤에 문자 0으로 바꾸기
    for n in numbers:
        if n % 2 == 0:                   
            answer.append(n + 1)
        else:
            bin_n = bin(n)[2:]
            if '0' not in bin_n:
                bin_n = '0' + bin_n
                
            zero_index = bin_n.rfind('0')
            bin_n = list(bin_n)   
            if zero_index == len(bin_n) - 1:    # 인덱스 에러 방지
                bin_n[zero_index] = '1'
            else:                           
                bin_n[zero_index] = '1'
                bin_n[zero_index + 1] = '0'
            
            
            answer.append(int(''.join(bin_n), 2))
    
    return answer