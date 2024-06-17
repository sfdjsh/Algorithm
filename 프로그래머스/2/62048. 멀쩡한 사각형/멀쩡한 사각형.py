def solution(w,h):
    answer = 1
    
    gcd = 1
    for n in range(min(w, h), 1, -1):
        if w % n == 0 and h % n == 0:
            gcd = n
            break
    
    return w * h - (w + h - gcd)