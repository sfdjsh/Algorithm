from collections import deque

N, M = map(int, input().split())

def bfs(a, b):
    visited = [0] * (N + 1)     # 방문 체크
    q = deque()
    q.append((a, 0))

    while q:
        n, cnt = q.popleft()

        if n == b:              # 지정한 사람과의 관계를 찾았을 때 cnt 리턴
            return cnt

        for i in kebin[n]:
            if not visited[i]:
                visited[n] = 1
                q.append((i, cnt + 1))


kebin = [[] for _ in range(N + 1)]      # 각 사람의 연결관계 담을 리스트

for _ in range(M):
    a, b = map(int, input().split())
    kebin[a].append(b)
    kebin[b].append(a)

answer = []

# 한 명의 사람과 그 외의 모든 사람들의 관계를 정의
for i in range(1, N + 1):
    result = 0
    for j in range(1, N + 1):
        if j == i:
            continue
        else:
            result += bfs(i, j)
    answer.append(result)

min_num = min(answer)               # 리스트의 최소값
for i in range(len(answer)):        # 여러 명일 경우 번호가 가장 작은 사람 출력
    if answer[i] == min_num:
        print(i + 1)
        break