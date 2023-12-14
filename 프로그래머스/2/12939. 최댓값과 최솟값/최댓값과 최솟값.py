def solution(s):
    answer = ''
    
    s = s.split()
    s = list(map(int, s))
    max_num, min_num = max(s), min(s)
    
    return str(min_num) + ' ' + str(max_num)