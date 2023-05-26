from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = len(queue1) * 3
    
    q1, q2 = deque(queue1), deque(queue2)
    
    max_sum = sum(queue1) + sum(queue2)
    mid_sum = max_sum / 2 
    
    if max_sum % 2 != 0:
        return -1
    
    sum_q1, sum_q2 = sum(q1), sum(q2)
    
    while True:
        if answer >= limit:
            answer = -1
            break
        
        if sum_q1 == sum_q2:
            break
        
        if sum_q1 > mid_sum:
            num1 = q1.popleft()
            q2.append(num1)
            sum_q1 -= num1
            sum_q2 += num1
            answer += 1
        
        elif sum_q2 > mid_sum:
            num2 = q2.popleft()
            q1.append(num2)
            sum_q1 += num2
            sum_q2 -= num2
            answer += 1
            
    return answer