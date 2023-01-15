import sys
from collections import deque
input = sys.stdin.readline

dx,dy = [0,0,-1,1],[-1,1,0,0]



def cal(x,y):
    q = deque()
    data[x][y] = "."
    q.append((x,y))
    while q:
        ddx,ddy=q.popleft()
        for i in range(4):
            cx,cy = dx[i]+ddx,dy[i] +ddy
            if 0<=cx<h and 0<=cy<w and data[cx][cy] =="#":
                data[cx][cy] = "."
                q.append((cx,cy))
                

for i in range(int(input())):
    h,w = map(int,input().split())
    data = [ list(input().strip()) for i in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] == "#": 
                cnt +=1; cal(i,j)
    print(cnt)