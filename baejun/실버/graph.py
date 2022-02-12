from collections import deque
n,m = map(int,input().split())
data = [[] for i in range(n+1)]
visited=[0]*n
print(data)
for i in range(m):
    x,y=map(int,input().split())
    data[x].append(y); data[y].append(x)
    print(data)

def bfs(start):
    stack = deque()
    stack.append(start)
    while stack:
        idx=stack.pop()
        stack.extend(data[idx])
        data.pop(idx)
cnt = 0

    
    bfs(x)