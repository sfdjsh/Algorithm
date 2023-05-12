def solution(numbers, hand):
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}   
                
    answer = ''
    keypad = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*', '0', '#']]
    
    left, right = dic['*'], dic['#']
    
    for n in numbers:
        now = dic[n]
        
        if n in [1, 4, 7]:
            answer += 'L'
            left = now
        
        elif n in [3, 6, 9]:
            answer += 'R'
            right = now
        
        else:
            left_cnt = abs(left[0] - now[0]) + abs(left[1] - now[1])
            right_cnt = abs(right[0] - now[0]) + abs(right[1] - now[1])     
            
            if left_cnt == right_cnt:
                if hand == 'right':
                    answer += 'R'
                    right = now
                if hand == 'left':
                    answer += 'L'
                    left = now
                    
            if left_cnt < right_cnt:
                answer += 'L'
                left = now
                
            if right_cnt < left_cnt:
                answer += 'R'
                right = now
    
    return answer