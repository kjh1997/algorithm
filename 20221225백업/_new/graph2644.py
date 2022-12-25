from collections import deque
graph ={}
for i in range(1, int(input())+1):
    graph[i]=[]
x, y = map(int, input().split())
for i in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(start, end):
    q = deque()
    q.append(([start],0))
    while q:
        x,cnt  = q.popleft()
        for i in x:
            if i == end: return cnt
            else:
                if i in graph:
                    q.append((graph[i],cnt+1))
                    del graph[i]
    return -1
print(bfs(x,y))