# import sys

# v,e = map(int,sys.stdin.readline().split())

# arr = [ [1e9] *( v+1) for _ in range( v+1)]
# for i in range(e):
#     x,y,c = map(int,sys.stdin.readline().split())
#     arr[x][y]=c

# for k in range(1,v+1):
#     for i in range(1,v+1):
#         for j in range(1,v+1):
#             if arr[i][k] + arr[k][j] < arr[i][j]:
#                 arr[i][j] = arr[i][k] + arr[k][j]

# ans = 1e9
# for i in range(1,v+1):
#     ans = min(ans,arr[i][i])

# if ans == 1e9: print(-1)
# else: print(ans)



import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra():
    while heap:
        d, start, end = heapq.heappop(heap)
        if start == end:
            print(d)
            break

        if dist[start][end] < d: continue

        for n_dist, n_node in graph[end]:
            if dist[start][n_node] > d + n_dist:
                dist[start][n_node] = d + n_dist
                heapq.heappush(heap, [dist[start][n_node], start, n_node])

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
dist = [[INF] * (v + 1) for _ in range(v + 1)]
heap = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    
    heapq.heappush(heap, [c, a, b]) 

dijkstra()