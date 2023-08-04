from itertools import combinations

def solution(relation):
    column = len(relation[0])       # 열의 갯수
    row = len(relation)             # 행의 갯수
        
    # coulmn에 대한 인덱스 조합 구하기
    idx_lst = []
    for i in range(1, column + 1):
        idx_lst.extend(combinations(range(column), i))
    
    # 유일성 체크
    unique = []
    for comb in idx_lst:
        tmp = set(tuple(item[i] for i in comb) for item in relation)
        if len(tmp) == row:
            unique.append(comb)
    
    # 최소성 체크
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    
    return len(answer)