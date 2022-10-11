import heapq

def solution(n, works):
    answer = 0
    # 작업량이 N시간보다 작거나 같으면 작업시간은 없음.
    if sum(works) <= n:
        return 0

    works = [-w for w in works]  # 작업량을 최대 힙으로 만들기 위한 리스트
    heapq.heapify(works)  # 리스트를 힙 구조로 변환

    # 리스트의 원소가 마이너스(-)로 되어있기 때문에 피로도를 최소화하기 위해 작업량 +1
    for _ in range(n):
        work = heapq.heappop(works)
        work += 1
        heapq.heappush(works, work)

    # 야근 지수의 작업량을 더해주기
    for w in works:
        answer += w ** 2

    return answer