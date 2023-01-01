import sys
import heapq
input = sys.stdin.readline

tc = int(input())
for t in range(tc):
    K = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)

    total_cost = 0
    while len(heap) > 1:
        b = heap[0]; heapq.heappop(heap)
        a = heap[0]; heapq.heappop(heap)
        cost = a + b
        heapq.heappush(heap, cost)
        total_cost += cost

    print(total_cost) 
