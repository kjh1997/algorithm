import sys
from collections import deque
input()
input = sys.stdin.readline
n = input()
graph={}
for i in range(int(n)):
    a,b = input().split()
    if a not in graph: graph[a]=[]
    if b not in graph: graph[b]=[]   
    graph[a].append(b)
    graph[b].append(a)
def dfs(start):
    q = deque()
    q.append([start])
    while q:
        data = q.popleft()

        for i in data:
            if i in graph:
                q.append(graph[i])
                del graph[i]
            else: continue
l = len(graph)
dfs('1')
print(l-1-len(graph))

