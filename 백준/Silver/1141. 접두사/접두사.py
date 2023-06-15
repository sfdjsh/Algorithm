N = int(input())
answer = N

prefix = list(input() for _ in range(N))
prefix.sort(key = lambda x : len(x))        # 문자열 길이로 정렬

for i in range(N):
    flag = True

    for j in range(i + 1, N):
        if prefix[i] == prefix[j][:len(prefix[i])]:     # 문자열 길이 단위로 접두사 판별
            flag = False
            break

    if not flag:
        answer -= 1

print(answer)
