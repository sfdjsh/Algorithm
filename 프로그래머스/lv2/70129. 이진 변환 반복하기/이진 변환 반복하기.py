def solution(s):
    
    answer = [0, 0]
    
    while True:
        if s == '1':                        # s가 1일 때 종료
            break
            
        answer[0] += 1
        
        start_len = len(s)                  # 처음 문자열 길이
        s = s.replace('0', '')              # 0 제거
        end_len = len(s)                    # 0 제거 후 문자열 길이
        
        answer[1] += start_len - end_len    # 0 개수 더하기
        
        s = bin(int(end_len))[2:]           # 이진수 변환
            
    return answer