M = int(input())
N = int(input())

min_result = 0
max_result = 0
for n in range(M, N+1):
    if n == 1:
        continue
    number = n
    for i in range(2, n):
        if n % i == 0:
            number = 0
            break
    if number != 0:
        if min_result == 0:
            min_result = n
        max_result += n

if min_result != 0:
    print(max_result)
    print(min_result)
else:
    print(-1)
