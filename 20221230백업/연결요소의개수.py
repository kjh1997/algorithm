import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

v = [False for i in range(n+1)]
graph = {}
for i in range(1,n+1):
    graph[i]=[]
for i in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def search(a):
    q = deque(graph[a])
    while q:
        cur = q.popleft()
        if v[cur] ==False:
            q.extend(graph[cur])
            v[cur]=True
ans = 0
for i in range(1,n+1):
    if v[i] == False:
        v[i]=True
        ans +=1
        search(i) 
    
print(ans)