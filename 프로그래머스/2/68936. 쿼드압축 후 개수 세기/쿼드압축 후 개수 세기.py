def solution(arr):
    answer = [0, 0]
    
    def qdtree_compress(x, y, l):
        num = arr[x][y]
        
        for i in range(x, x + l):
            for j in range(y, y + l):
                if arr[i][j] != num:
                    l = l // 2
                    qdtree_compress(x, y, l)
                    qdtree_compress(x + l, y, l)
                    qdtree_compress(x, y + l, l)
                    qdtree_compress(x + l, y + l, l)
                    return
        
        answer[num] += 1
        
    qdtree_compress(0, 0, len(arr))
    
    return answer