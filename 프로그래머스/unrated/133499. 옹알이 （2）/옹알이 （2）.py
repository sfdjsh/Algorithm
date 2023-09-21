from itertools import permutations

def solution(babbling):
    answer = 0
    
    for baby in babbling:
        stack = ['aya', 'ye', 'woo', 'ma']
        speak, tmp = '', ''                 # 발음하고 있는 단어, 발음했던 단어
        for b in baby:
            speak += b
            
            if len(speak) >= 4:             # 발음할 수 있는 최대 길이가 3이기 때문에, 4 이상이 되면 break
                break
            
            if speak in stack:              # 발음할 수 있는 단어일 때
                if not tmp:                 
                    tmp = speak             # tmp에 발음할 수 있는 단어 넣기
                    stack.remove(speak)     # stack에서 발음한 단어 제거
                    speak = ''              # 발음 초기화
                    
                else:                       # 새로운 발음을 할 수 있는 단어가 나왔을 때
                    stack.append(tmp)       # 전에 했던 발음 stack에 추가   
                    stack.remove(speak)     # 지금 발음한 단어 stack에서 제거
                    tmp = speak             # tmp에 발음할 수 있는 단어 넣기
                    speak = ''              # 발음 초기화
                    
        if not speak:   
            answer += 1
            
    return answer