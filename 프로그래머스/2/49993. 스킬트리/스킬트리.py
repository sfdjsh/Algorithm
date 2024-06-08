def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        stack = list(skill)
        flag = True
        for s in skill_tree:
            if s in stack and s != stack.pop(0):
                flag = False
                break
        
        if flag:
            answer += 1
    
    return answer