def solution(n, m, section):
    answer = 1
    
    tmp = section[0]
    for i in range(1, len(section)):
        if section[i] - tmp >= m:
            answer += 1
            tmp = section[i]
    
    return answer