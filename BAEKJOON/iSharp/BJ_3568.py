variable = list(input().replace(',', '').replace(';', '').split())

for i in range(1, len(variable)):
    variable[i] = variable[i].replace('[]', '][')

for i in range(1, len(variable)):
    print(variable[0], end='')

    for t in variable[i][::-1]:
        if not t.isalpha():
            print(t, end='')

    print('', end=' ')

    for a in variable[i]:
        if a.isalpha():
            print(a, end='')

    print(';', sep='\n')

