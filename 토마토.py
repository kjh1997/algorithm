import sys
from collections import deque


input = sys.stdin.readline
m,n,h = map(int,input().split())

data  = [ [ list(map(int,input().split())) for i in range(n) ] for j in range(h)  ]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                q.append((i,j,k))
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
if len(q) == 0: print(-1); exit()
cur = len(q)
tmp = len(q)
while q:
    z,x,y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if -1<nx<n and -1<ny<m and -1<nz<h:
            if data[nz][nx][ny] == 0:
                data[nz][nx][ny] = data[z][x][y]+1
                q.append((nz,nx,ny))
  
flag = 0
result = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                flag = 1
            result = max(result,data[i][j][k])
if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
