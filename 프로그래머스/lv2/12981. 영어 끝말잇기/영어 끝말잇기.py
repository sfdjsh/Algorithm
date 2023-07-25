def solution(n, words):
    answer = [0, 0]
    
    lst = [words[0]]
    
    for i in range(1, len(words)):
        # 다음 사람이 끝말을 이었고, 같은 단어가 안나왔을 경우
        if words[i][0] == words[i - 1][-1] and words[i] not in lst:     
            lst.append(words[i])        # 리스트에 나왔던 단어 추가
            
        else:                           # 끝말의 규칙을 어겼을 경우
            answer[0] = (i % n) + 1     # 몇 번째 사람인지 구하기
            answer[1] = (i // n) + 1    # 그 사람이 몇 번째 말한 단어인지 구하기
            break
                
    return answer