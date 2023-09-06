def solution(name, yearning, photo):
    answer = []
    
    dict = {}
    for n, y in zip(name, yearning):
        dict[n] = y
     
    for tc in photo:
        cnt = 0
        for p in tc:
            if p in name:
                cnt += dict[p]
        answer.append(cnt)
    
    return answer