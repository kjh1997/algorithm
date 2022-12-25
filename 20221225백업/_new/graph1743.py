from collections import deque
h,w, k = map(int,input().split())
board = [[0]*(w+1) for i in range(h+1)]
for i in range(k):
    y,x = map(int,input().split())
    board[y][x]=1
re =0
visit=[]
move = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(x,y):
    q = deque()
    board[y][x]=0
    q.append((x,y))
    re =1
    while q:
        x,y = q.popleft()
        for dx,dy in move:
            mx,my = x+dx,y+dy 
            if  (0< mx < w+1) and (0<my<h+1) and ((mx,my) not in visit) and board[my][mx]==1:
                q.append((mx,my))
                visit.append((mx,my))
                board[my][mx]=0
                re+=1
    return re
tmp =0
for dx in range(1,w+1):
    for dy in range(1,h+1):
        if board[dy][dx] ==1:
            tmp = max(tmp,bfs(dx,dy))

print(tmp)


