N = int(input())
lst = list(map(int, input().split()))

result = 0
for num in lst:
    if num == 1:                    # 1일 때는 pass
        continue
    else:
        cnt = 0
        for i in range(1, num + 1):     # 1부터 해당 자연수까지 반복문
            # 나누어떨어지는 수가 있으면 cnt + 1
            if num % i == 0:
                cnt += 1
            if cnt == 3:                # cnt = 3이면 약수가 아니므로 종료
                break
        else:               # 약수이면 result + 1
            result += 1

print(result)