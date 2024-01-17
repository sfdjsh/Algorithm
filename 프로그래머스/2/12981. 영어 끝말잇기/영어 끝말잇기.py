def solution(n, words):
    answer = [0, 0]
    
    lst = [words[i:i + n] for i in range(0, len(words), n)]
    
    end_str = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] in end_str:
                return [j + 1, i + 1]
            
            if end_str and end_str[-1][-1] != lst[i][j][0]:
                return [j + 1, i + 1]
            
            else:
                end_str.append(lst[i][j])
    
    return answer