from collections import deque

N, K = map(int, input().split())

result = abs(K - N) + 1
case = 0

q = deque()
q.append((N, 0))
visited = [0] * 100001

while q:
    num, cnt = q.popleft()
    visited[num] = 1

    if cnt <= result:
        if num == K:
            if result > cnt:
                result = cnt
                case = 0
            case += 1

        for dn in (num + 1, num - 1, num * 2):
            if 0 <= dn < 100001 and not visited[dn]:
                q.append((dn, cnt + 1))

print(result)
print(case)