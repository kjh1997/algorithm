import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = defaultdict(list)
visit=[False]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = {}
tmp = 0
def bfs(start):
    global tmp
    visit[start] = True
    q = deque()
    q.append((start,0))
    while q:
        cur,cnt = q.popleft()
        for i in graph[cur]:
            if visit[i]==False:
                visit[i] = True
                q.append((i,cnt+1))
                if cnt+1 not in ans:
                    ans[cnt+1] = [i]
                    tmp = cnt+1
                else: 
                    ans[cnt+1].append(i)
bfs(1)
print(min(ans[tmp]), tmp, len(ans[tmp]))