def solution(s):
    answer = []
    
    s = s.replace('{', '')
    s = list(s)
    
    tuple_lst = []
    
    # s의 각각의 원소를 리스트로 바꾸는 과정 
    lst, tmp = [], ''
    for i in range(len(s) - 1):
        if s[i].isdigit():
            if s[i + 1].isdigit():
                tmp += s[i]
            else:
                lst.append(int(tmp + s[i]))
                tmp = ''
        
        if s[i] == '}':             # 닫힌 괄호가 나오면 튜플 리스트에 원소들 넣기
            tuple_lst.append(lst)
            lst = []
    
    tuple_lst.sort(key = lambda x : len(x))     # 집합의 길이로 오름차순 정렬
    
    for i in tuple_lst:
        for j in i:
            if j not in answer:
                answer.append(j)
                
    return answer