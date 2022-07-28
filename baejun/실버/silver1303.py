import sys
from collections import deque
a,b = map(int, sys.stdin.readline().split())
d = []
for i in range(b):
    d.append(list(sys.stdin.readline().strip()))
W, B=0,0
dx = [0,0,1,-1]
dy = [-1,1,0,0]
def cal(x,y,color):
    d[x][y] = "_"
    global W,B
    q = deque()
    q.append((y,x))
    if color != "W" and color !="B": return 0
    cnt = 1
    while q:
        x,y=q.pop()
        for i in range(4):
            cur_x = x+dx[i]; cur_y = y+dy[i]
            if (cur_x <0) or (cur_y) <0 or (cur_x >=a) or (cur_y)>=b: continue
            if d[cur_y][cur_x] == color:
                q.append((cur_x, cur_y))
                d[cur_y][cur_x] = "_"
                cnt +=1
    if color=="W": 
        W= W+cnt**2
    elif color=="B": 
        B= B+cnt**2
    


for i in range(b):
    for j in range(a):
        cal(i,j,d[i][j])
print(W,B)


