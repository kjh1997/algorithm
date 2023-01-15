import sys
from collections import deque
input = sys.stdin.readline

n,m= map(int,input().split())
graph = {}
for i in range(n+1): graph[i]=[]
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

ans = []
tmp = 0
for i in range(1,n+1):
    q = deque([i])
    visit = [False] * (n+1)
    cnt = 0
    visit[i]=False
    while q:
        cur = q.popleft()
       
        for j in graph[cur]:
            if visit[j] == False and j in graph:
                q.append(j)
                visit[j]=True
                cnt +=1
    if tmp <= cnt:
        ans.append(i)
        tmp = cnt

print(*ans,end="")