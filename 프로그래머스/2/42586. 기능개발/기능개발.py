def solution(progresses, speeds):
    answer = []
    
    publish = []
    for p, s in zip(progresses, speeds):
        leave_percent = 100 - p
        work_period = leave_percent // s
        if leave_percent % s:
            work_period += 1 
        publish.append(work_period)
    
    while publish:
        period = publish.pop(0)
        cnt = 1
        while publish and publish[0] <= period:
            publish.pop(0)
            cnt += 1
        
        answer.append(cnt)
        
    return answer