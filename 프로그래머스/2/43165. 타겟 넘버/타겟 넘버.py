def solution(numbers, target):
    answer = 0   
    
    def dfs(idx, cnt):
        nonlocal answer
        
        if idx == len(numbers):
            if cnt == target:
                answer += 1
            return
        
        dfs(idx + 1, cnt + numbers[idx])
        dfs(idx + 1, cnt - numbers[idx])
        
    dfs(0, 0)

    return answer