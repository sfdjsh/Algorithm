N, S = map(int, input().split())
num_lst = list(map(int, input().split()))

i, j = 0, 0
sum_num = 0
result = 100001

while True:
    if sum_num >= S:
        result = min(result, j - i)
        sum_num -= num_lst[i]
        i += 1
    elif j == N:
        break

    else:
        sum_num += num_lst[j]
        j += 1

if result == 100001:
    print(0)
else:
    print(result)