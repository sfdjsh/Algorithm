def hanoi(n, s, e):
    if n == 0:
        return

    hanoi(n-1, s, 6 - s - e)
    print(s, e)
    hanoi(n-1, 6 - s - e, e)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)