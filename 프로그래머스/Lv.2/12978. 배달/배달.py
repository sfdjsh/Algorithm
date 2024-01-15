def solution(N, road, K):
    
    dis = [[float('inf')] * (N + 1) for _ in range(N + 1)]    
    
    for r1, r2, d in road:
        dis[r1][r2] = min(dis[r1][r2], d)
        dis[r2][r1] = min(dis[r2][r1], d)
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    
    answer = 0
    dis[1][1] = 0
    for n1 in dis[1]:
        if n1 <= K:
            answer += 1
    
    return answer