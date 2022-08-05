n = int(input())
graph = {}
for i in range(1,n+1):
    graph[i]=[]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
from collections import deque
q = deque()
q.append([1])
re = [0 for i in range(n+1)]
while q:
    arr = q.popleft()
    
    for i in arr:
        if i in graph:
            a = graph[i]
            for j in a:
                if re[j] != 0: continue
                re[j]=i
            q.append(graph[i])
            del graph[i]
del re[:2]
for i in re: print(i)