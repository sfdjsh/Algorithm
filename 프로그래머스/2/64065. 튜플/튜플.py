def solution(s):
    answer = []
    
    s = s[:len(s) - 1].replace('{', '')
    total_lst = []
    
    lst = []
    num = ''
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num:
                lst.append(int(num))
                num = ''
            if c == '}' and lst:
                total_lst.append(lst)
                lst = []
                
    total_lst.sort(key = lambda x : len(x))
    for lst in total_lst:
        for n in lst:
            if n not in answer:
                answer.append(n)
    
    return answer