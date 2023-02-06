# 각 층의 처음위치부터 끝위치까지 빗물이 고인 갯수를 구하는 함수
def rain(x, s_y, e_y):
    cnt = 0
    for y in range(s_y, e_y):
        if arr[x][y] == 0:
           cnt += 1

    return cnt

H, W = map(int, input().split())            # 세로 가로
arr = [[0] * (W + 1) for _ in range(H + 1)]
lst = list(map(int, input().split()))
result = 0

# arr 행렬에 블록 쌓기
y = 1
while y <= len(lst):
    for i in range(1, lst[y-1] + 1):
        arr[i][y] = 1
    y += 1

for i in range(1, H + 1):
    x, s_y, e_y = 0, 0, 0               # 층, 층의 처음 블록 위치, 층의 끝 블록 위치
    x = i
    for j in range(1, W + 1):
        if arr[i][j] == 1:
            if s_y == 0:
                s_y = j
            else:
                e_y = j

    # 층에서 처음 블록 위치와 끝 블록 위치가 있으면 빗물이 고일 수 있으므로 함수 실행
    if s_y != 0 and e_y != 0:
        result += rain(x, s_y, e_y)

print(result)