import sys
input = sys.stdin.readline

n,m= map(int,input().split())

arr = [ list(map(int,input().split())) for _ in range(n)]
dx,dy = [0,1,1],[1,0,1]
tmp = 0
def cal(x,y,cur):
    global tmp
    if x == n-1 and y == m-1: 
        tmp = max(cur, tmp)
        return
    for i in range(3):
        cx = x + dx[i]
        cy = y + dy[i]
        if cx < n and cy < m:
            cal(cx,cy,cur+arr[cx][cy])
    
cal(0,0,arr[0][0])

print(tmp)


import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for i in range(n)]
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+arr[i][j]
print(dp[n][m])