answer = 0

# dfs 함수
def dfs(k, visited, cnt, dungeons):
    global answer

    if cnt > answer:    # 최대값 갱신
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = 1
            dfs(k - dungeons[i][1], visited, cnt + 1, dungeons)
            visited[i] = 0


def solution(k, dungeons):
    global answer

    visited = [0] * len(dungeons)
    dfs(k, visited, 0, dungeons)

    return answer
