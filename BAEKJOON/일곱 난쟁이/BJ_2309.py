lst = list(int(input()) for _ in range(9))
lst.sort()

sum_height = sum(lst)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if sum_height - lst[i] - lst[j] == 100:
            for k in range(len(lst)):
                if k == i or k == j:
                    pass
                else:
                    print(lst[k])
            exit()
