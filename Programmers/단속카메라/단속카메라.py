def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # 도착지점을 기준으로 오름차순 정렬
    camera = min(map(min, routes)) - 1  # 출발 지점 = routes의 최소값 - 1

    # camera 가 차량의 진입 지점보다 작다면 카메라 설치하고,
    # camera 위치를 차량의 진입 지점으로 갱신하고, answer += 1
    for r in routes:
        if camera < r[0]:
            answer += 1
            camera = r[1]
    return answer