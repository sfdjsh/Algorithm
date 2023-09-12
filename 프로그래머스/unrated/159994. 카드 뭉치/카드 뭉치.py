def solution(cards1, cards2, goal):
    answer = ''
    
    flag = True
    for g in goal:
        if cards1:
            card1 = cards1[0]
        if cards2:
            card2 = cards2[0]        
        
        
        if g == card1:
            cards1.pop(0)
        elif g == card2:
            cards2.pop(0)
        else:
            flag = False
            break
    
    if flag:
        answer = 'Yes'
    else:
        answer = 'No'
    
    return answer