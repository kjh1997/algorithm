from collections import deque
n = int(input())
arr=[]
visit = [[0]*n for i in range(n)]
for i in range(n):
    arr.append(list(map(str, input())))
nx = [-1,1,0,0]
ny = [0,0,1,-1]
re =[]
def maze(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    visit[x][y]=-1
    while q:
        x2,y2 = q.popleft()
        for i in range(4):
            x3 = x2+nx[i]
            y3 = y2+ny[i]
            if x3 < 0 or x3 > n-1 or y3 < 0 or y3 > n-1:
                continue
            if arr[x3][y3]=='1' and visit[x3][y3] != -1:
                visit[x3][y3]=-1
                q.append((x3,y3))
                cnt+=1
    re.append(cnt)
for i in range(n):
    for j in range(n):
        if arr[i][j] != '0' and visit[i][j] != -1:
            maze(i,j)

re.sort()
print(len(re))
for i in re: print(i)





