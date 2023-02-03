bracket = list(input())
stack = []

result = 0
tmp = 1
for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == '[':
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if bracket[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()

    elif bracket[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if bracket[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
