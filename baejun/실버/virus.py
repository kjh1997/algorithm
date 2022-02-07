from collections import deque
def dfs(start):
    stack = deque()
    stack.append([start])

    while stack:
        data = stack.pop() 
        for i in data:
            if i in d: 
                stack.append(list(set(d[i])))
                del d[i]
            else: continue
d={}
input()
for i in range(int(input())):
    a,b=input().split()   
    if a not in d:  d[a] = [b]
    if b not in d:  d[b] = [a]
    d[a].append(b); d[b].append(a)
a=len(d)
dfs('1')
print(a-1-len(d))