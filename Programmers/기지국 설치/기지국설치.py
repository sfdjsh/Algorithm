from math import ceil

def solution(n, stations, w):
    answer = 0          # 결과값

    spread = w * 2 + 1  # 전파 크기
    start = 1
    for s in stations:
        '''
        1. stations에서 전파되지 않은 왼쪽 구역 ceil함수를 이용하여, 전파 크기로 나누고 반올림한 값을 answer에 더하기
        2. 기지국이 설치된 아파트에서 전파 거리를 더하여 시작 지점 재갱신
        '''
        answer += ceil((s - w - start) / spread)
        start = (s + w + 1)

    # stations에서 전파되지 않은 오른쪽 구역 처리
    if n >= start:
        answer += ceil((n - start + 1) / spread)

    return answer