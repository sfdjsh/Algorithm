def solution(numbers, hand):
    
    # 키패드 숫자의 인덱스
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}   
                
    answer = ''
    keypad = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*', '0', '#']]     # 키패드 패턴의 2차원 배열 생성
    
    left, right = dic['*'], dic['#']    # 왼손, 오른손의 시작점
    
    for n in numbers:
        now = dic[n]            # 눌러야할 번호의 인덱스
        
        if n in [1, 4, 7]:      # 1,4,7을 입력할 때는 왼손 
            answer += 'L'
            left = now          # 왼손 위치 저장
        
        elif n in [3, 6, 9]:    # 3,6,9를 입력할 때는 오른손
            answer += 'R'
            right = now         # 오른손 위치 저장
        
        else:   # 가운데 열 키패드를 누를 때 
            left_cnt = abs(left[0] - now[0]) + abs(left[1] - now[1])        # 왼손에서 눌러야 할 키패드까지의 거리 계산
            right_cnt = abs(right[0] - now[0]) + abs(right[1] - now[1])     # 오른손에서 눌러야 할 키패드까지의 거리 계산
            
            if left_cnt == right_cnt:   # 거리가 같으면 오른손잡이, 왼손잡이에 따라 처리
                if hand == 'right':
                    answer += 'R'
                    right = now
                if hand == 'left':  
                    answer += 'L'
                    left = now
                    
            if left_cnt < right_cnt:    # 왼손에서 누르는 것이 더 가까울 때
                answer += 'L'
                left = now
                
            if right_cnt < left_cnt:    # 오른손에서 누르는 것이 더 가까울 때
                answer += 'R'
                right = now
    
    return answer