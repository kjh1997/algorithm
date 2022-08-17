dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,l,r = map(int,input().split())

data  = [list(map(int,input().split())) for _ in range(n)]
from collections import deque
visit = []
re = 0
def bfs(x,y):
    q = deque()
    q.append((w,h))
    result = 0
    
    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx < n and 0<= ny < n and (nx,ny) not in visit:
                if  l <= abs(data[ny][nx]-data[cy][cx]) <= r :
                    visit.append((nx,ny))
                    q.append((nx,ny))
                    result += 1
    if result != 0: return 1
    else: return 0
for w in range(n):
    for h in range(n):
        if (w,h) not in visit:
            visit.append((w,h))
            if 0 != bfs(w,h): re+=1
            print(visit)
print(re)

