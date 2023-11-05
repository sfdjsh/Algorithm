def solution(answers):
    answer = []
    
    soopo1 = [1, 2, 3, 4, 5]
    soopo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    soopo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer1 = [answers[i:i+len(soopo1)] for i in range(0, len(answers), len(soopo1))]
    cnt1 = 0
    for ans in answer1:
        for i in range(len(ans)):
            if ans[i] == soopo1[i]:
                cnt1 += 1
    answer.append(cnt1)
    
    answer2 = [answers[i:i+len(soopo2)] for i in range(0, len(answers), len(soopo2))]
    cnt2 = 0
    for ans in answer2:
        for i in range(len(ans)):
            if ans[i] == soopo2[i]:
                cnt2 += 1
    answer.append(cnt2)
    
    answer3 = [answers[i:i+len(soopo3)]for i in range(0, len(answers), len(soopo3))]
    cnt3 = 0
    for ans in answer3:
        for i in range(len(ans)):
            if ans[i] == soopo3[i]:
                cnt3 += 1
    answer.append(cnt3)
    
    result = []
    tmp = max(answer)
    for i in range(len(answer)):
        if answer[i] == tmp:
            result.append(i + 1)
    
    result.sort()
    
    return result