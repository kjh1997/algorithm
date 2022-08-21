from collections import deque

h,w = map(int,input().split())

arr = [list(map(str,input())) for _ in range(h)]
dx, dy = [0,0,-1,1],[1,-1,0,0]
visit = [ [False]*w for i in range(h)]
def bfs(x,y):
    global ve,s
    q= deque()
    q.append((x,y))
    wolf = 0
    sheep = 0
    if arr[y][x] == 'v': wolf +=1
    elif arr[y][x] == 'o': sheep+=1
    arr[y][x] = "#"
    
    visit[y][x] = True
    while q:

        cx,cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<= nx < w and 0<= ny <h:
                if visit[ny][nx] ==False and arr[ny][nx] != '#':
                    q.append((nx,ny))
                    visit[ny][nx] = True

                    if arr[ny][nx] == 'o': 
                        sheep += 1
                    if arr[ny][nx] == 'v': 
                        wolf += 1
                    arr[ny][nx] ="#"

    if sheep > wolf:
        s += sheep
    else: 
        ve += wolf

ve = 0
s = 0

for wide in range(w):
    for height in range(h):
        if arr[height][wide] != "#":
            
            bfs(wide,height)
print(s,ve)