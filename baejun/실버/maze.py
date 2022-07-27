from collections import deque
n,m=map(int,input().split())
board=[ list(input().rstrip()) for i in range(n)]
visited=[ [0]*m for _ in range(n)]
visited[0][0]=1
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(start):
    q=deque()
    q.append(start)
    while q:
        x,y = q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<=nx <n and 0<= ny <m:
                if visited[nx][ny] ==0 and board[nx][ny] =='1':
                    visited[nx][ny]= visited[x][y]+1
                    q.append((nx,ny))
print(bfs((0,0)))
