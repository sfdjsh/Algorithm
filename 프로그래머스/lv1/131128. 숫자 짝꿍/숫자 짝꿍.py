def solution(X, Y):
  
    lst = ''
    for k in range(9, -1, -1):
        x_cnt, y_cnt = X.count(str(k)), Y.count(str(k))
        tmp = min(x_cnt, y_cnt)
        if tmp > 0:
            lst += str(k) * tmp
    
    lst = list(lst)
    answer = ''.join(lst)
    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'
    else:
        # return int(answer)
        return str(answer)