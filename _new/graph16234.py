dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,l,r = map(int,input().split())

data  = [list(map(int,input().split())) for _ in range(n)]
from collections import deque

re = 0
def bfs(x,y):
    visit = []
    visit.append((w,h))
    q = deque()
    q.append((w,h))
    result = 0
    sum_board=0
    sum_board += data[h][w]
    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx < n and 0<= ny < n and (nx,ny) not in visit:
                if  l <= abs(data[ny][nx]-data[cy][cx]) <= r :
                    visit.append((nx,ny))
                    q.append((nx,ny))
                    sum_board += data[ny][nx]
                    result += 1
    sum_board = sum_board//len(visit)
    for nx,ny in visit:
        data[ny][nx]=sum_board
    if result != 0: return 1
    else: return 0
for w in range(n):
    for h in range(n):
        if 0 != bfs(w,h): re+=1
        print(data)
            
print(re)

