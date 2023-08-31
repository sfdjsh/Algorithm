def solution(plans):
    answer = []
    
    plan = []    
    for i in range(len(plans)):
        time = list(map(int, plans[i][1].split(':')))
        sum_time = time[0] * 60 + time[1]
        plan.append([sum_time, int(plans[i][2]), plans[i][0]])  # 시작 시간, 걸리는 시간, 과제 이름
    plan.sort(key = lambda x : x[0])    # 시작 시간을 기준으로 정렬
    
    stack = []    
    for i in range(len(plan)):
        if i == len(plan) - 1:          # 마지막 인덱스 스택에 추가
            stack.append(plan[i])
            break
            
        st, tt, sub = plan[i]           # 시작 과제 (시작 시간, 걸리는 시간, 과제 이름) 
        nst, ntt, nsub = plan[i + 1]    # 다음 과제 (시작 시간, 걸리는 시간, 과제 이름)
        if st + tt <= nst:              # 시작 시간 + 걸리는 시간이 다음 과제보다 빨리 끝났을 때
            answer.append(sub)
            tmp = nst - (st + tt)       # 여유 시간 계산 
            
            while tmp > 0 and stack:        # 여유 시간으로 잠시 멈춘 과제 계산
                t, tt, sub = stack.pop()
                if tt <= tmp:               # 잠시 멈춘 과제 계산의 걸리는 시간이 여유 시간보다 작을 때
                    answer.append(sub)
                    tmp -= tt               # 여유 시간 갱신
                else:                       
                    stack.append([t, tt - tmp, sub])
                    tmp -= tt
            
        else:
            plan[i][1] = tt - (nst - st)    # 시작 과제의 걸리는 시간 갱신
            stack.append(plan[i])
    
    while stack:
        t, tt, sub = stack.pop()
        answer.append(sub)
    
    return answer