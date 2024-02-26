def solution(files):
    answer = []
    file_lst = []
    
    for file in files:
        head, number, tail = '', '', ''             # HEAD, NUMBER, TAIL의 변수
        for i in range(len(file)):
            if file[i].isdigit():                   # 파일명에 숫자가 남으면 숫자를 기준으로 구분
                head = file[:i]                     # 숫자가 아닌 문자까지
                number = file[i:]                   # 숫자부터 끝 문자열까지
            
                for j in range(len(number)):
                    if not number[j].isdigit():     # number 숫자 구분
                        tail = number[j:]           # 숫자가 아닌 문자부터 나머지까지
                        number = number[:j]         # 숫자만 담기
                        break
                        
                file_lst.append([head, number, tail])
                break
    file_lst.sort(key = lambda x : (x[0].lower(), int(x[1])))    
    
    for i in file_lst:
        answer.append(''.join(i))
    
    return answer