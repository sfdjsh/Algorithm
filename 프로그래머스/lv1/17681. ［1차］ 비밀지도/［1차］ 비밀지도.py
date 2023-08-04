def solution(n, arr1, arr2):
    answer = [['#'] * n for _ in range(n)]
    
    idx = 0
    for a, b in zip(arr1, arr2): 
        line = bin(a | b)[2:].zfill(n)      # 2진수 변환 후, OR 연산자, n만큼 0채우기
        for i in range(len(line)):
            if line[i] == '0':              # 0일 때는 공백
                answer[idx][i] = ' '
        idx += 1
    
    
    return [''.join(a) for a in answer]