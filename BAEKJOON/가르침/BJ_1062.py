def DFS(idx, cnt):
    global result

    if cnt == K - 5:
        pass_check = 0
        for words in english:
            check = True
            for w in words:
                if not alpha[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                pass_check += 1
        result = max(result, pass_check)
        return

    for w in range(idx, len(alpha)):
        if not alpha[w]:
            alpha[w] = 1
            DFS(w, cnt + 1)
            alpha[w] = 0

N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()

english = [set(input()) for _ in range(N)]
result = 0
alpha = [0] * 26

ess_alpha = ['a', 'c', 'n', 'i', 't']
for a in ess_alpha:
    alpha[ord(a) - ord('a')] = 1

DFS(0, 0)
print(result)



