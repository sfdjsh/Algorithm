def solution(today, terms, privacies):
    answer = []
    
    term = {}                       # 약관 종류, 유효기간 담을 딕셔너리
    for t in terms:
        tp, time = t.split(' ')     # 약관 종류, 유효기간
        term[tp] = int(time)
    
    today = today.split('.')        # 오늘 날짜 = 년, 월, 일로 쪼개기
    today = list(map(int, today))
    
    for i in range(len(privacies)):
        date, tp = privacies[i].split(' ')  # 날짜, 약관 종류
        
        date = date.split('.')              # 날짜 = 년, 월, 일로 쪼개기
        date = list(map(int, date))
        
        if tp in term:
            date[1] = date[1] + term[tp]    # 날짜의 월에 유효기간 더하기
        
        if date[1] > 12:                    # 12월달 넘어갔을 때, 년과 월 갱신
            date[0] += 1
            date[1] -= 12
        
        date[2] -= 1                        # 일이 0이 됐을때, 월과 일 갱신
        if date[2] == 0:
            date[1] -= 1
            date[2] = 28
        
        today_tmp = today[0] * 360 + today[1] * 30 + today[2]
        date_tmp = date[0] * 360 + date[1] * 30 + date[2]
        
        if date_tmp < today_tmp:
            answer.append(i + 1)
            
    return answer