N, M = map(int, input().split())

great_divisor = 1               # 최대공약수 초기 값
least_multi = 1                 # 최소공배수 초기 값

while True:
    for n in range(2, 10000):
        if N % n == 0 and M % n == 0:           # 자연수 2개의 약수를 구한다면
            great_divisor = great_divisor * n   # 최대공약수 * 구한 약수
            least_multi = least_multi * n       # 최소공배수 * 구한 약수
            N = N // n                          # N 나누기 약수
            M = M // n                          # M 나누기 약수
            break                               # for문 종료
    # 구해진 약수가 없으면 최소공배수 * N * M 후, while문 종료
    else:
        least_multi = least_multi * N * M
        break

print(great_divisor)
print(least_multi)


