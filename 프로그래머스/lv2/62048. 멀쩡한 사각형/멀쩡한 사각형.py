def solution(w,h):
    max_g = 0              
    # 대각선 방향으로 잘랐을 때 정사각형을 사용 할 수 없는 갯수는
    # 가로 길이 + 세로 길이 - 가로,세로 길이의 최대 공약수
    for i in range(min(w, h), 0, -1):    
        if w % i == 0 and h % i == 0:
            max_g = i
            break
    
    return (w * h) - (w + h - max_g)