def solution(s):
    answer = len(s)
    
    for n in range(1, len(s) // 2 + 1):     # 압축할 수 있는 최대 길이 = length / 2
        tmp = ''                            # 문자열 변수
        idx = 0                             
        
        while idx < len(s):
            cnt = 1                         # 압축된 변수의 갯수
            char = s[idx : idx + n]         # n 범위까지의 문자
            
            while True:
                if char == s[idx + cnt * n : idx + (cnt + 1) * n]: # n 범위만큼 char과 같은 지 판별하여 압축할 수 있는지 없는지 판단
                    cnt += 1        # 압축 가능하면 cnt + 1
                else:               # 압축 할 수 없으면 반복문 종료
                    break
            
            if cnt > 1:                 # 압축할 수 있는 경우
                tmp += str(cnt) + char  # tmp 변수에 카운트 갯수와 문자 넣기
                idx += cnt * n          # idx 갱신    
            else:                       # 압축할 수 없는 경우
                tmp += char             # tmp 변수에 문자 넣기
                idx += n                # idx 갱신
        
        answer = min(answer, len(tmp))  # 최소값 구하기
                    
    return answer