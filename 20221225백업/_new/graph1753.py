n,m = map(int,input().split())
start = int(input())
graph = {}
wight = {}
for i in range(1,n+1): graph[n]=[]
for _ in range(m):
    x,y,w = map(int,input().split())
    graph[x]=y
    wight[str(x)+"to"+str(y)] = w
from collections import deque
for _ in range(1,n+1):
    visit = [0 for i in range(n+1)]

    for j in range(1,n+1):
        if start==j: print(0)
        q = deque()
        q.append((start, 0))

        while q:
            cur,cost = q.popleft()
            if cur == j: 
            for i in graph[i]:
                if visit[i] == 1: continue
                visit[i] = 1
                q.append((i, cost+wight[str(cur) + 'to' + str(i)]))





