import sys
sys.stdin = open('input.txt')

dx, dy = ((0, -1, 1, 0, 0), (0, 0, 0, -1, 1))   # 상:1, 하:2, 좌:3, 우:4
opp = [0, 2, 1, 4, 3]   # (상:1, 하:2, 좌:3, 우:4) 의 반대방향
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N은 행렬크기, M은 격리시간, K는 미생물 군집의 개수
    arr = [list(map(int, input().split())) for _ in range(K)]   # arr[0]=x, arr[1]=y, arr[2]=미생물 수, arr[3]=이동방향

    for _ in range(M):  # 격리시간만큼 반복
        # 좌표 이동
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + dx[arr[i][3]]
            arr[i][1] = arr[i][1] + dy[arr[i][3]]
            # 미생물이 끝점에 가면 미생물의 개수를 반으로 나누고 방향을 반대로
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] = arr[i][2] // 2
                arr[i][3] = opp[arr[i][3]]
     
        arr.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)   # 좌표와 미생물의 개수가 큰 것부터 정렬

        i = 1
        while i < len(arr):
            # 같은 좌표일 때 작은 미생물의 개수를 큰 미생물에 더하고 지우기
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            # 없으면 다음 좌표에서 비교
            else:
                i += 1
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][2]    # 각 좌표에 있는 미생물의 개수 다 더하기

    print(f'#{tc} {ans}')



