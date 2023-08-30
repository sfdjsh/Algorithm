def solution(sequence, k):
    answer = []
    
    si = 0
    ni = -1
    sum = 0
    
    while True:
        if sum == k:
            answer.append([si, ni])
        
        if sum < k:
            ni += 1
            if ni >= len(sequence):
                break
            sum += sequence[ni]
        
        else:
            sum -= sequence[si]
            if si >= len(sequence):
                break
            si += 1
            
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))    
    return answer[0]