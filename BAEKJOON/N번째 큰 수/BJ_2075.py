# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# last_num = arr[-1]
#
# result = 0
#
# cnt = 1
# while cnt <= N:
#     max_num = max(last_num)
#     print(arr.index(max_num, 0, 53))
#
#     # for i in range(len(arr)):
#     #     for j in range(len(arr)):
#     #         if arr[i][j] == max_num:
#     #             last_num[j] = arr[i-1][j]
#     #             break
#
#     result = max_num
#     cnt += 1
#
# print(result)

import heapq

N = int(input())
heap = []

for _ in range(N):
    lst = list(map(int, input().split()))
    for n in lst:
        if len(heap) < N:
            heapq.heappush(heap, n)
        else:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
print(heap[0])


