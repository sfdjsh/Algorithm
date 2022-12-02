tc = int(input())

for _ in range(tc):
    N = bin(int(input()))[2:]
    for idx, val in enumerate(N[::-1]):
        if val == '1':
            print(idx, end=' ')