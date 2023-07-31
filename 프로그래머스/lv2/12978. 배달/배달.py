import heapq

def solution(N, road, K):
    answer = 0

    distance = [float('inf')] * (N + 1)     # 노드 1번부터 각 노드의 최소거리
    distance[1] = 0                         # 노드 1번 초기화

    adj = [[] for _ in range(N + 1)]        # 연결된 노드와 거리를 담을 리스트
    for s, e, c in road:
        # 양방향 연결
        adj[s].append([e, c])               
        adj[e].append([s, c])

    heap = []
    heapq.heappush(heap, (1, 0))           

    while heap:
        node, cost = heapq.heappop(heap)        # 현재 노드, 거리
        for next_n, c in adj[node]:
            total_cost = cost + c               # 다음 노드까지의 최소 거리
            if total_cost < distance[next_n]:   # 최소 거리 갱신
                distance[next_n] = cost + c
                heapq.heappush(heap, (next_n, total_cost))

    for i in range(1, N + 1):
        if distance[i] <= K:    # 음식 배달이 가능한 노드 찾기
            answer += 1

    return answer