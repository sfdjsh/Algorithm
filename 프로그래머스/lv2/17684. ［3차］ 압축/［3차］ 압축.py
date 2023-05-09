def solution(msg):
    answer = []
    
    dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
           'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 
           'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
       
    tmp = ''
    idx = 0
    max_num = 27
    while idx < len(msg):
        
        tmp += msg[idx]
        
        if tmp in dic.keys():               # 딕셔너리 키에 해당 문자가 있으면, 다음 문자열 진행
            idx += 1
        else:
            answer.append(dic[tmp[:-1]])    # 마지막 문자를 제외한 문자열 키값의 value값 넣기
            dic[tmp] = max_num              # 딕셔너리에 새로운 문자 : value값의 최대값 + 1으로 넣기
            max_num += 1
            tmp = ''
    
    answer.append(dic[tmp])
    
    return answer