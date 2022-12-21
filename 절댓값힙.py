import sys
import heapq
# re = []
# N = int(sys.stdin.readline())
# hash = {}
# for i in range(N):
#     d = int(sys.stdin.readline())
#     if d ==0:
#         if len(hash) == 0: re.append(0); continue
#         for i in sorted(hash.items):
#             hash[i].sort()
#             re.append(hash[i][0])
#             hash[i].pop(0)
#             if len(hash[i]) ==0 : del hash[i]
#             break
#     else:
#         e = abs(d)
#         if e in hash: hash[e].append(d)
#         else: hash[e] = [d]
# for i in re:
#     print(i)

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, (abs(n),n))
        print(heap)
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)


