def solution(N, stages):
    answer = []
    
    stage_lst = []
    
    total = len(stages)
    for i in range(1, N + 1):
        if total == 0:
            stage_lst.append([0, i])
        else:
            cnt = stages.count(i)
            fail = cnt / total
            stage_lst.append([fail, i])
            total -= cnt
    
    stage_lst.sort(key = lambda x : x[0] , reverse = True)
    for s in stage_lst:
        answer.append(s[1])
    
    return answer