def DFS(num, cnt):
    global result

    if num == B:
        if result > cnt:
            result = cnt
        return

    if num > B:
        return

    for i in range(2):
        if i == 0:
            DFS(num * 2, cnt + 1)
        else:
            num = str(num) + '1'
            num = int(num)
            DFS(num, cnt + 1)



A, B = map(int, input().split())
result = float('inf')

DFS(A, 1)

if result != float('inf'):
    print(result)
else:
    print(-1)
