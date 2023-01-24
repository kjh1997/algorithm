import sys
from collections import defaultdict,deque
input = sys.stdin.readline
a,b,c= map(int,input().split())
data = defaultdict(set)
for i in range(b):
    x,y = map(int,input().split())
    data[x].add(y)
    data[y].add(x)
q = deque()
q.append(1)
visit = [False] * (a+1)
while q:
    cur = q.pop()
    if visit[cur] ==True: continue
    else:
        print(cur)
        visit[cur]= True
        
    next =sorted(data[cur])

    q.extend(next)
print(0)  