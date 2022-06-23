from collections import deque

def bfs():
    q = deque()
    q.append(1) # 시작 위치
    v[1] = 1    # 방문 체크

    while q:
        ci = q.popleft()
        # 100칸에 도달하면 리턴
        if ci == 100:
            return v[100] - 1

        # 주사위 굴리기
        for i in range(1,7):
            di = ci + i
            if di <= 100:
                dice = game[di]
                if not v[dice]:
                    q.append(dice)
                    v[dice] = v[ci] + 1

game = [i for i in range(101)]
v = [0] * 101

N, M = map(int, input().split())
# 뱀과 사다리를 통해 갈 수 있는 위치 game 리스트에서 체인지
for _ in range(N+M):
    a, b = map(int, input().split())
    game[a] = b

print(bfs())