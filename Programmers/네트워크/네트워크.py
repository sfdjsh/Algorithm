def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]  # 컴퓨터 체크 리스트

    # 컴퓨터를 방문하지 않았을 때 DFS 함수 실행
    for c in range(n):
        if not visited[c]:
            DFS(n, computers, visited, c)
            answer += 1

    return answer


def DFS(n, computers, visited, c):
    visited[c] = 1  # 컴퓨터 체크
    for i in range(n):
        if not visited[i] and computers[c][i] == 1:  # 각각의 컴퓨터와 연결되어 있는지 판단
            DFS(n, computers, visited, i)