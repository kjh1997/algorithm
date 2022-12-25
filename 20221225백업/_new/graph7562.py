from collections import deque
xx = [-1, -2, -2, -1, 1, 2, 2, 1]
yy = [2, 1, -1, -2, -2, -1, 1, 2]
tc = int(input())
for i in range(tc):
    n = int(input())
    board = [[0]*(n+1) for _ in range(n+1)]
    x,y = map(int,input().split())
    dx,dy = map(int,input().split())
    q = deque()
    q.append((x,y))
    board[x][y]=1
    while q:
        nx,ny = q.popleft()
        if nx == dx and ny== dy:
            print(board[nx][ny]-1)
            break
        for i in range(8):
            tx = nx + xx[i]
            ty = ny + yy[i]
            if 0 <= tx < n and 0 <= ty < n:
                if board[tx][ty]==0: 
                    board[tx][ty]= board[nx][ny]+1
                    q.append([tx,ty])
