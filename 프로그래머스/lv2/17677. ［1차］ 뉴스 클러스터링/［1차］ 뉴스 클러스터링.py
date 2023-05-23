import math

def solution(str1, str2):

    str1, str2 = str1.lower(), str2.lower() # 대소문자 구분 x

    set_str1, set_str2 = [], []             # 문자열 집합 담을 리스트
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha(): # str1의 두 글자가 영어일 때 
            set_str1.append(str1[i] + str1[i + 1])      

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha(): # str2의 두 글자가 영어일 때
            set_str2.append(str2[i] + str2[i + 1])

    inter_str = []                  # 교집합 담을 리스트
    idx = 0
    while idx < len(set_str1):
        tmp = set_str1[idx]         
        if tmp in set_str2:         # 교집합일 때
            inter_str.append(tmp)   # inter_str에 추가
            set_str1.remove(tmp)    # 교집합 문자 제거
            set_str2.remove(tmp)    # 교집합 문자 제거
        else:
            idx += 1

    intersection = len(inter_str)   # 교집합 갯수
    union = intersection + len(set_str1) + len(set_str2)    # 합집합 갯수

    if union == 0:      # 제로디비젼에러 방지
        answer = 65536
    else:
        answer = math.floor((intersection / union) * 65536) # 자카드 * 65536 후 버림

    return answer