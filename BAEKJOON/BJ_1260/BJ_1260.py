from collections import deque

def dfs(start):
    if node[start]:
        for i in node[start]:
            if not visited1[i]:
                visited1[i] = 1
                dfs_lst.append(i)
                dfs(i)

def bfs():
    q = deque()
    q.append(V)
    while q:
        x = q.popleft()
        if node[x]:
            for i in node[x]:
                if not visited2[i]:
                    visited2[i] = 1
                    q.append(i)
                    bfs_lst.append(i)


N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]         # 노드와 연결된 양방향 리스트
# 연결된 노드 node 리스트에 추가
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
# 노드 번호가 작은 것부터 방문하기 위해 오름차순 정렬
for i in range(1, N+1):
    node[i].sort()

# dfs방문체크와 결과 담을 리스트 정의
visited1 = [0]*(N+1)
visited1[V] = 1
dfs_lst = [V]

# bfs방문체크와 결과 담을 리스트 정의
visited2 = [0]*(N+1)
visited2[V] = 1
bfs_lst = [V]

dfs(V)
print(*dfs_lst)

bfs()
print(*bfs_lst)