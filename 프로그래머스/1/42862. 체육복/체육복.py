def solution(n, lost, reserve):
    answer = 0
    
    lst = lost.copy()
    lost.sort()
    reserve.sort()
    
    for c in lost:
        if c in reserve:            # 도난과 빌려줄 수 있는 학생이 같을 때
            lst.remove(c)
            reserve.remove(c)       
        elif c - 1 in reserve and c - 1 not in lost:      # 앞 번호 학생에게 빌릴 수 있을 때
            lst.remove(c)
            reserve.remove(c - 1)
        elif c + 1 in reserve and c + 1 not in lost:      # 뒷 번호 학생에게 빌릴 수 있을 때
            lst.remove(c)
            reserve.remove(c + 1)
    
    return n - len(lst)