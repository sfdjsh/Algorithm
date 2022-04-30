from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for i in range(1, N+1):
    for j in combinations(lst, i):
        if sum(j) == S:
            result += 1

print(result)



