from collections import deque
h,w,k=map(int,input().split())
board = [[0]*w for i in range(h)]
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for dw in range(x1,x2):
        for dh in range(y1,y2):
            board[dh][dw] = 1
re = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    board[y][x]=1
    q = deque()
    q.append((x,y))
    cnt = 1
    while q:
        nx,ny = q.popleft()
        for i in range(4):
            mx=nx+dx[i]
            my=ny+dy[i]
            if mx<0 or mx>w-1 or my < 0 or my > h-1:
                continue
            if board[my][mx] != 1:
                cnt+=1
                q.append((mx,my))
                board[my][mx]=1
    return cnt 

for y in range(h):
    for x in range(w):
        if board[y][x]==0:
            re.append(bfs(x,y))
re.sort()
print(len(re))
for i in re: print(i,end=" ")