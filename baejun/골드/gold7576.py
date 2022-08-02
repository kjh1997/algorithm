# from collections import deque
# move = [(-1,0),(0,1),(1,0),(0,-1)]
# cnt=0
# def bfs(x,y):
#     global cnt
#     print(visit, x, y)
#     q=deque()
#     q.append((x,y))
    
#     while q:
#         cnt+=1
#         print(farm)
#         nx,ny = q.pop()
#         for dx,dy in move:
#             mx=dx+nx; my=dy+ny
#             if nx+dx <0 or nx+dx >w-1 or ny+dy <0 or ny+dy >h-1:continue
#             if farm[my][mx] !=-1 and not visit[my][mx]: 
#                 q.append((mx,my))
#                 farm[my][mx]=1
#                 visit[my][mx]=True

# w,h = map(int,input().split())
# farm=[]
# visit =[[False]*w for i in range(h)]

# for i in range(h):
#     farm.append(list(map(int,input().split())))

# for mh in range(h):
#     for mw in range(w):
#         if farm[mh][mw] ==1 and not visit[mh][mw] :
#             bfs(mw,mh)
# print(farm, cnt)

# ==================================================
# from collections import deque
# def dfs(x,y,cnt):
#     print(farm, x, y)
#     nx,ny = x,y
#     for dx,dy in move:
#         mx=dx+nx; my=dy+ny
#         if nx+dx <0 or nx+dx >w-1 or ny+dy <0 or ny+dy >h-1:continue
#         if farm[my][mx] ==0 and not visit[my][mx]: 
            
#             farm[my][mx]=1+farm[ny][nx]
#             visit[my][mx]=True
#             dfs(mx,my,cnt+1)
#     return cnt

# move = [(-1,0),(0,1),(1,0),(0,-1)]
# cnt=0
# w,h = map(int,input().split())
# farm=[]
# visit =[[False]*w for i in range(h)]

# for i in range(h):
#     farm.append(list(map(int,input().split())))

# for mh in range(h):
#     for mw in range(w):
#         if farm[mh][mw] ==0 and not visit[mh][mw] :
#             cnt+= dfs(mw,mh,0)

# print(cnt)


from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)