result = 0
people = 0

for i in range(10):
    out, get = map(int, input().split())
    people = people - out
    people = people + get

    if result < people:
        result = people

print(result)



