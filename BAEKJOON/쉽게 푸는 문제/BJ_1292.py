A, B = map(int, input().split())
result = 0

num = 1
cnt = 0
for n in range(1, B+1):
    cnt += 1
    if A <= n <= B:
        result += num

    if num == cnt:
        num += 1
        cnt = 0

print(result)