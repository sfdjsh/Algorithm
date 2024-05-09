
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        answer += 1
        sco1 = heapq.heappop(scoville)
        sco2 = heapq.heappop(scoville)
        shake_sco = sco1 + (sco2 * 2)
        heapq.heappush(scoville, shake_sco)
    
    return answer