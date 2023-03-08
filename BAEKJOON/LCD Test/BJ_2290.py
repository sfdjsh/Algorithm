s, n = map(int, input().split())
row, col = '-', '|'


def sketch(s):
    num = [[' '] * (s + 2) for _ in range(2 * s + 3)]
    return num

def top():
    for i in range(1, s + 1):
        num[0][i] = row

def left_top():
    for i in range(1, s + 1):
        num[i][0] = col

def right_top():
    for i in range(1, s + 1):
        num[i][-1] = col

def middle():
    for i in range(1, s + 1):
        num[s + 1][i] = row

def left_under():
    for i in range(s + 2, 2 * s + 2):
        num[i][0] = col

def right_under():
    for i in range(s + 2, 2 * s + 2):
        num[i][-1] = col

def under():
    for i in range(1, s + 1):
        num[2 * s + 2][i] = '-'

def draw(n):
    if n in [2, 3, 5, 6, 7, 8, 9, 0]:
        top()
    if n in [4, 5, 6, 8, 9, 0]:
        left_top()
    if n in [1, 2, 3, 4, 7, 8, 9, 0]:
        right_top()
    if n in [2, 3, 4, 5, 6, 8, 9]:
        middle()
    if n in [2, 6, 8, 0]:
        left_under()
    if n in [1, 3, 4, 5, 6, 7, 8, 9, 0]:
        right_under()
    if n in [2, 3, 5, 6, 8, 9, 0]:
        under()

n = str(n)
arr = []

for i in n:
    num = sketch(s)
    draw(int(i))
    arr.append(num)

ans = [[] for _ in range(2 * s + 3)]

for i in range(0, 2 * s + 3):
    for idx in range(len(arr)):
        ans[i] += arr[idx][i]
        ans[i].append(' ')

for r in ans:
    print(''.join(r))



