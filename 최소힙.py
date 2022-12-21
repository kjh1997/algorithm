import sys, heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
