import heapq
n = int(input())
data = []
for i in range(n):
    num ,start, end = map(int, input().split())
    data.append([start, end])
data.sort()
heap = []
heapq.heappush(heap, data[0][1])
for i in range(1, n):
    if data[i][0] < heap[0]: 
        heapq.heappush(heap, data[i][1]) 
    else: 
        heapq.heappop(heap)
        heapq.heappush(heap, data[i][1])
print(len(heap))