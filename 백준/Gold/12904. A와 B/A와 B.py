S = list(input())
T = list(input())

answer = 0
while T:
    if S == T:
        answer = 1
        break

    elif T[-1] == 'A':
        T.pop(-1)

    elif T[-1] == 'B':
        T.pop(-1)
        T.reverse()

print(answer)