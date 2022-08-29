from collections import deque
n = int(input())
dx,dy = [0,0,-1,1],[1,-1,0,0]
arr = [list(map(int,input().split())) for i in range(n)]

maxNum = 0
for i in range(n):
    if maxNum < max(arr[i]):
        maxNum = max(arr[i])
def bfs(x,y,r):
    q = deque()
    q.append((x,y))
    visit[y][x] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<=ny <n and visit[ny][nx] != True:
                 
                if arr[ny][nx] > r:
                    q.append((nx,ny))
                visit[ny][nx]= True   

re = []
for r in range(maxNum+1):
    cnt = 0
    visit = [[0]*n for i in range(n)]
    for w in range(n):
        for h in range(n):
            if arr[h][w] > r and visit[h][w] != True:
                visit
                bfs(w,h,r); cnt +=1

    re.append(cnt)

print(max(re))