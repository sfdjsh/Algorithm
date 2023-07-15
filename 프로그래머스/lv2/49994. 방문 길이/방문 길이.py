def solution(dirs):
    answer = 0
    
    lst = set()
    s_x, s_y = 5, 5
    for array in dirs:
        if array == 'U':
            n_x, n_y = s_x - 1, s_y
        elif array == 'D':
            n_x, n_y = s_x + 1, s_y
        elif array == 'R':
            n_x, n_y = s_x, s_y + 1
        elif array == 'L':
            n_x, n_y = s_x, s_y - 1
        
        if 0 <= n_x < 11 and 0 <= n_y < 11: 
            lst.add(((s_x, s_y), (n_x, n_y)))
            lst.add(((n_x, n_y), (s_x, s_y)))
            s_x, s_y = n_x, n_y
        
    return len(lst) // 2