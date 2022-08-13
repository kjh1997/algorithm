from collections import deque
h,w = map(int,input())
board = [ list(map(int,input())) for i in range(h)]
move = [(0,1),(-1,0),(1,0),(0,-1)]

q= deque()
q.append((0,0,False,1))
while q:
    x,y,bre,num = q.popleft()
    
    for dx,dy in move:
        mx = x+dx
        my = y+dy
        if 0<= mx <h and 0<=  my < h:


