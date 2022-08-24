from collections import deque

def bfs(x):
    visited = [0] * (n+1)
    visited[x] = 1          # 자기 자신 방문 체크

    q = deque()
    for i in relation[x]:
        q.append([i, 0])    # 친구와 점수 q에 append

    while q:
        a, score = q.popleft()

        # 방문을 안했으면 방문리스트에 점수를 추가해주고 a의 친구 관계와 점수를 q에 append
        if not visited[a]:
            visited[a] = score+1
            for friend in relation[a]:
                q.append([friend, score+1])

    return max(visited)

n = int(input())
relation = [[] for _ in range(n+1)]

check = True
while check:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        check = False
    else:
        relation[a].append(b)
        relation[b].append(a)

result = [0] * (n+1)
for i in range(1, n+1):
    result[i] = bfs(i)  # 방문 횟수 최대값을 result에 할당

min_num = min(result[1:])   # 최소값 구하기
boss = []
# 최소값과 같은 회원(인덱스)을 boss에 append
for i in range(1, len(result)):
    if result[i] == min_num:
        boss.append(i)

print(min_num, len(boss))
boss.sort()
print(*boss)