from collections import deque
h,w = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
map2 = [list(map(int,input().split())) for i in range(h)]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    re = 1
    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < w and 0<= ny < h:
                if map2[ny][nx] == 1:
                    map2[ny][nx] =0
                    q.append((nx,ny))
                    re+=1
    return re
tmp=0
d=0
for i in range(w):
    for j in range(h):
        if map2[j][i] == 1:
            tmp = max(bfs(i,j),tmp)
            d +=1
print(d)
if tmp == 0: print(0)
else:
    print(tmp if tmp == 1 else tmp-1)

