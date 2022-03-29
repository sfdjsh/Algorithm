N = int(input())
lst = list(map(int, input().split()))
a = len(lst)

result = set()              # 시간초과로 인해 리스트를 셋으로 수정
for i in range(1<<a):       # 모든 집합 순회
    total = 0
    for j in range(a):
        # 부분집합의 합 result에 담기
        if i & (1<<j):
            total += lst[j]
    result.add(total)

answer = 0
for i in range(1, 2000000):
    if i not in result:     # 만약에 i가 result 안에 없으면 연속된 숫자가 없음.
        answer = i
        break
print(answer)