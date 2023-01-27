from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))

def check():
    row_cnt, col_cnt = 1, 1
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if row_cnt < cnt:
                row_cnt = cnt

    for j in range(N):
        cnt = 1
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j]:
                cnt += 1
            else:
                cnt = 1
            if col_cnt < cnt:
                col_cnt = cnt

    return max(row_cnt, col_cnt)

N = int(input())
arr = [list(input()) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        for k in range(4):
            dx, dy = i + di[k], j + dj[k]
            if 0 <= dx < N and 0 <= dy < N and arr[i][j] != arr[dx][dy]:
                arr[i][j], arr[dx][dy] = arr[dx][dy], arr[i][j]
                cnt = check()
                if result < cnt:
                    result = cnt
                arr[i][j], arr[dx][dy] = arr[dx][dy], arr[i][j]

print(result)
