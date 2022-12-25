from collections import deque
def graphSearch(start):
    q = deque()
    q.append([start])
    while q:
        arr = q.popleft()
        for i in arr:
            if i in graph:
                q.append(graph[i])
                del graph[i]

n, m= map(int,input().split())
graph = {}
for i in range(1,n+1):
    graph[i]=[]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt = 0
for i in range(1,n+1):
    if i in graph:
        cnt +=1
        graphSearch(i)
print(cnt)