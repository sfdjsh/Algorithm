# 마지막 N비트까지 모두 1인지 판별하는 함수
def result(n):
    # 1을 한칸씩 옮기면서 M의 2진수 표현이 1이 아니면 'OFF', 마지막까지 if문을 안 타면 'ON' 출력
    for i in range(N):
        if not n & (1<<i):
            return 'OFF'
    return 'ON'

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N:마지막 N비트, M: 정수
    print(f'#{tc} {result(M)}')