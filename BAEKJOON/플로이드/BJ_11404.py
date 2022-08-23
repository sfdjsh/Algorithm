n = int(input())
m = int(input())
inf = 100000000
cities = [[inf] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    cities[a-1][b-1] = min(cities[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                cities[i][j] = 0
            else:
                cities[i][j] = min(cities[i][j], cities[i][k] + cities[k][j])

for i in cities:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
