import math

def solution(str1, str2):
    answer = 0
    two_str1, two_str2 = [], []
    for i in range(len(str1) - 1):
        tmp = str1[i] + str1[i + 1]
        if tmp.isalpha():
            two_str1.append(tmp.lower())
    
    for i in range(len(str2) - 1):
        tmp = str2[i] + str2[i + 1]
        if tmp.isalpha():
            two_str2.append(tmp.lower())
    
    inter = 0
    for t in two_str1:
        if t in two_str2:
            inter += 1
            two_str2.remove(t)
    union = len(two_str1) + len(two_str2)
    
    if not union:
        return 65536
    else:
        return math.trunc(((inter / union) * 65536))
    
