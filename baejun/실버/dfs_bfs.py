from collections import deque
import sys
N,M,V = map(int, sys.stdin.readline().split())
data = {}
for i in range(M):
    a,  b = input().split()
    if a not in data:  data[a] = [b]
    if b not in data:  data[b] = [a]
    data[a].append(b); data[b].append(a)
for i in data:
    data[i] = sorted(list(set(data[i])))


def dfs(graph, start):
    visit = []
    stack = deque()
    stack.append(start)
    while stack:
       # print(stack)
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            stack.extend(graph[n][::-1])
    return visit
result = ""
a = dfs(data, str(V))
for i in a:
    if i == a[len(a)-1]:result += i
    else:result += i + " "
print(result)
def bfs(graph, start):
    visit = []
    queue = deque()
    queue.append(start)
    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            queue.extend(graph[n])
    return visit

result = ""
a = bfs(data, str(V))
for i in a:
    if i == a[len(a)-1]:result += i
    else:result += i + " "
print(result)