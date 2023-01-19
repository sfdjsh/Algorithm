def calculate(idx, result):
    global max_num, min_num, plus, minus, multi, div

    if idx == N:
        max_num = max(max_num, result)
        min_num = min(min_num, result)

    else:
        if plus > 0:
            plus -= 1
            calculate(idx + 1, result + num[idx])
            plus += 1
        if minus > 0:
            minus -= 1
            calculate(idx + 1, result - num[idx])
            minus += 1
        if multi > 0:
            multi -= 1
            calculate(idx + 1, result * num[idx])
            multi += 1
        if div > 0:
            div -= 1
            calculate(idx + 1, int(result / num[idx]))
            div += 1

N = int(input())
num = list(map(int, input().split()))
plus, minus, multi, div = list(map(int, input().split()))

max_num = -100000000
min_num = 100000000
calculate(1, num[0])

print(max_num)
print(min_num)
