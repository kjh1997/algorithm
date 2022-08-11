from collections import deque
n = int(input())
r1,c1,r2,c2=map(int,input().split())
board = [[0]*n for i in range(n)]
move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
q = deque()
q.append((r1,c1,0))
visit=[]
while q:
    r,c,cnt = q.popleft()
    if r==r2 and c==c2: 
        print(cnt);exit()
    for dx,dy in move:
        if 0 > r+dx or r+dx > n-1 or  0 > c+dy or c+dy > n-1 or (r+dx,c+dy) in visit:
            continue
        q.append((r+dx,c+dy,cnt+1))
        visit.append((r+dx,c+dy))
print(-1)