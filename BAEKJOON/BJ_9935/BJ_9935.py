c_str = list(input())                   # 문자열
boom = list(input())                    # 폭발하는 문자열

stack = []                              # 결과
for i in c_str:                         # 문자열 순회하여 stack에 추가
    stack.append(i)
    if len(stack) >= len(boom):         # 문자열이 폭발하는 경우는 폭발의 길이보다 크거나 같음.
        if stack[-len(boom):] == boom:  # 폭발의 길이에서 stack의 마지막에 들어온 것이 폭발하는 문자열이 같으면
            for j in range(len(boom)):  # boom의 길이만큼 제거
                stack.pop()

if len(stack) == 0:                     # stack이 비어 있는 것과 결과 값 출력
    print('FRULA')
else:
    print(''.join(stack))