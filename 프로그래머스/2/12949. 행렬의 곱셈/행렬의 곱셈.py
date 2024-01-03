import numpy as np

def solution(arr1, arr2):
    answer = []
    
    arr1_x = len(arr1)
    arr2_x = len(arr2)
    arr2_y = len(arr2[0])
    idx = 0
    
    while idx < arr1_x:
        lst = []
        for j in range(arr2_y):
            tmp = 0
            for i in range(arr2_x):
                tmp += arr1[idx][i] * arr2[i][j]
            
            lst.append(tmp)
        
        answer.append(lst)
        idx += 1
        
    
    return answer