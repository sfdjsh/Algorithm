N, K = map(int, input().split())

result = 0
cnt = 0
for i in range(1, N+1):
    # 나머지가 0이면 result와 cnt 추가
    if N % i == 0:
        result = i
        cnt += 1

    # 약수의 K번째가 되면 result 출력
    if cnt == K:
        print(result)
        break

# 약수의 개수가 K개보다 적다면 0 출력
if cnt < K:
    print(0)
