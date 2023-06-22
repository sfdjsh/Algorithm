def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def comp(x, y, l):
        tmp = arr[x][y]
        
        for i in range(x, x + l):
            for j in range(y, y + l):
                if tmp != arr[i][j]:
                    l = l // 2
                    comp(x, y, l)
                    comp(x + l, y, l)
                    comp(x, y + l, l)
                    comp(x + l, y + l, l)
                    return
        
        answer[tmp] += 1
    
    
    comp(0, 0, length)
    

    return answer