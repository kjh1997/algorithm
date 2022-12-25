from collections import deque
dest =int(input())
n = int(input())
cost = {}
visit=[]
graph = {}
for i in range(1,dest+1): graph[i] =[]
for i in range(n):
    a,b,c= map(int,input().split())
    graph[a].append(b)
    if str(a)+"to"+str(b) not in cost :
        cost[str(a)+"to"+str(b)]=c
    else:
        cost[str(a)+"to"+str(b)]=min(c,cost[str(a)+"to"+str(b)])
q = deque()
s,e = map(int,input().split())
q.append((s,0))
print(cost)
re = []
while q:
    cur, c = q.pop()
    if cur==e:
        re.append(c)
    for i in graph[cur]:
        if str(cur)+"to"+str(i) not in cost: 
            continue
        q.append((i, cost[str(cur)+"to"+str(i)]+c))
print(min(re))



# import sys
# from heapq import heappush, heappop

# input = sys.stdin.readline
# INF = 1e9

# N = int(input())
# M = int(input())
# graph = [[] for _ in range(N)]
# dp = [INF]*N
# heap = []

# for _ in range(M):
#     u, v, w = map(int, input().split())
#     graph[u-1].append([v-1, w])

# start, end = map(int, input().split())


# def dijkstra(K):
#     dp[K-1] = 0
#     heappush(heap, [0, K-1])
#     while heap:
#         cost, pos = heappop(heap)
#         if dp[pos] < cost:
#             continue
#         for p, c in graph[pos]:
#             c += cost
#             if c < dp[p]:
#                 dp[p] = c
#                 heappush(heap, [c, p])


# dijkstra(start)

# print(dp[end-1])