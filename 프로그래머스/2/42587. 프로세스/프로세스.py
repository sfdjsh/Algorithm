from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while True:
        max_pri = max(item[0] for item in q)
        pri, inx = q.popleft()
        if pri < max_pri:
            q.append((pri, inx))
        else:
            answer += 1
            if inx == location:
                break
        
    return answer