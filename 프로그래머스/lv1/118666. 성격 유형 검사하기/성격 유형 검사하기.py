def solution(survey, choices):
    answer = ''
    
    per = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']  # 성격 유형
    per_cnt = [0, 0, 0, 0, 0, 0, 0, 0]              # 성격 점수 
    
    ag_dag = [0, 3, 2, 1, 0, 1, 2, 3]               # 동의 비동의
    for sur, cho in zip(survey, choices):
        per1, per2 = sur[0], sur[1]                 # 성격 유형 자르기
        if cho < 4:                                 # 질문에서 비동의를 체크했을 때
            idx = per.index(per1)                   
            per_cnt[idx] += ag_dag[cho]
        else:                                       # 질문에서 동의를 체크했을 때
            idx = per.index(per2)
            per_cnt[idx] += ag_dag[cho]
    
    for i in range(0, len(per_cnt), 2):
        if per_cnt[i] == per_cnt[i + 1]:            # 점수가 같으면 사전순 앞에 유형
            answer += per[i]
        elif per_cnt[i] < per_cnt[i + 1]:           # 점수가 높은 성격 찾기
            answer += per[i + 1]
        else:
            answer += per[i]

    return answer