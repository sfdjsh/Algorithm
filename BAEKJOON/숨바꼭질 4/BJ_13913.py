from collections import deque

def check_path(n):
    lst = []
    tmp = n
    for _ in range(visited[n] + 1):
        lst.append(tmp)
        tmp = check[tmp]
    print(*lst[::-1])


def BFS():
    q = deque()
    q.append(N)

    while q:
        num = q.popleft()
        if num == K:
            print(visited[num])
            check_path(num)
            return

        if 0 <= num + 1 <= 100000 and not visited[num + 1]:
            visited[num + 1] = visited[num] + 1
            check[num + 1] = num
            q.append(num + 1)

        if 0 <= num - 1 <= 100000 and not visited[num - 1]:
            visited[num - 1] = visited[num] + 1
            check[num - 1] = num
            q.append(num - 1)

        if 0 <= num * 2 <= 100000 and not visited[num * 2]:
            visited[num * 2] = visited[num] + 1
            check[num * 2] = num
            q.append(num * 2)

N, K = map(int, input().split())

visited = [0] * 100001
check = [0] * 100001
BFS()

