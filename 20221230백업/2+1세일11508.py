import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap =[]
for i in range(n):
    heapq.heappush(heap, -int(input()))
ans = 0
cnt =1
for i in range(n):
    if cnt % 3 == 0: 
        heapq.heappop(heap)
        cnt +=1
        continue
    ans -=  heap[0]
    heapq.heappop(heap)
    cnt+=1
print(ans)