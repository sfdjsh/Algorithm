from collections import deque

# bfs 함수 구현
def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        n = queue.popleft()     # queue에 제일 첫번째 인자 뽑기
        if n == K:              # 동생을 찾으면 종료
            print(visited[n])
            break

        for i in [n-1, n+1, n*2]:   # 문제에서 주어진 X-1, X+1, X*2 를 순회
            # if not visited[i] and 0 <= i <= max_num:
            if 0 <= i <= max_num and not visited[i]:    # 점 범위안에 있고 방문기록이 없을 때
                visited[i] = visited[n] + 1             # 방문기록 체크함과 동시에 횟수
                queue.append(i)                         # 큐 리스트에 추가

N, K = map(int, input().split())    # input 값
max_num = 100000                    # 최대값 설정
visited = [0] * 100001              # 방문기록 설정
bfs()