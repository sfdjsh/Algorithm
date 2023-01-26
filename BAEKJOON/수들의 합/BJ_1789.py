S = int(input())

result = 1
N = 0
while N <= S:
    if N + result <= S:
        N += result
        result += 1
    else:
        break

print(result - 1)