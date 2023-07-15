def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        flag = True
        stack = list(skill)             # 스킬 순서 스택에 넣기
        for s in skill_tree:            
            if s in list(skill):        # 스킬 트리가 선행 스킬 순서에 있을 때
                if s != stack.pop(0):   # 첫번째 스킬트리와 선행 스킬 순서가 같은지 비교
                    flag = False
        if flag:
            answer += 1
                    
    return answer