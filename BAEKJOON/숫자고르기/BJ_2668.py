def dfs(n, i):
    v[n] = 1    # 방문 체크

    # 현재 번호와 연결된 다음 번호로 이동
    for k in num[n]:    
        if not v[k]:
            dfs(k, i)
        
        # 번호를 방문했고 간선이 같은 번호로 돌아왔으면 리스트에 추가
        elif v[k] and k == i:
            result.append(k)

N = int(input())

# 노드와 간선 설정
num = [[] for _ in range(N+1)]
for i in range(1, N+1):
    num[i].append(int(input()))

result = []
for i in range(1, N+1):
    v = [0] * (N+1)
    dfs(i, i)

print(len(result))
for i in result:
    print(i)

