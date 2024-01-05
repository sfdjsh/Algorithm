def solution(s):
    
    s = list(s.split(' '))
    
    for i in range(len(s)):
        if len(s[i]):
            s[i] = s[i][0].upper() + s[i][1:].lower()
                    
    return ' '.join(s)


# "a b " => "A B " 출력
# s[i] = s[i][0].upper() + s[i][1:].lower() 하면 공백에서 오류가 남.
# 공백이 아닌 문자의 길이가 있어야 런타임 에러를 방지할 수 있음. 