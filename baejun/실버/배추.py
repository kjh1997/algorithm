from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(start):
    stack = deque()
    stack.append(start)
    while stack:
        a = stack.pop()
        for i,j in zip(dx,dy):
            nx=a[0]+i; ny= a[1]+j
            if nx>=0 and nx <m and ny >=0 and ny < n and board[ny][nx] == 1:
                stack.append((nx,ny)); board[ny][nx]=0

for i in range(int(input())):
    m,n,k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    cnt =0
    for _ in range(k): 
        x,y=map(int,input().split()); 
        board[y][x]=1
    for i in range(m):
        for j in range(n):
            if board[j][i]==1:
                board[j][i]=0; cnt +=1
                bfs((i,j))
    print(cnt)