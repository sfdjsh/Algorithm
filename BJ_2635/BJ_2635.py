# BJ_2635 (수 이어가기)

# 문제
# 첫 번째 줄에는 입력된 첫 번째 수로 시작하여 위의 규칙에 따라 만들 수 있는 수들의 최대 개수를 출력한다.
# 둘째 줄에 그 최대 개수의 수들을 차례대로 출력한다. 이들 수 사이에는 빈칸을 하나씩 둔다.

first_num = int(input())                            # 첫번째 수
num_len = 0                                         # 수의 길이 초기값
result = []                                         # 수의 결과를 담을 리스트

for i in range(first_num+1):                        # input의 정수만큼 반복 순회
    gap_lst = [first_num, i]                        # input 정수값과 비교할 첫번째 수
    j = 0
    while True:                                     # 두 수의 차이가 음수가 나올 때까지 반복
        num_gap = gap_lst[j] - gap_lst[j+1]
        j += 1
        if num_gap < 0:
            break
        gap_lst.append(num_gap)                     # 두 수의 차이에 대한 결과를 리스트에 추가

        if num_len < len(gap_lst):                  # 최대 길이를 찾기 위한 조건문
            num_len = len(gap_lst)
            result = gap_lst

print(num_len)
print(*result)



