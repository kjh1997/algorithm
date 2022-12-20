import sys

n,m = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = data[i-1][j-1] + dp[i][j-1] - dp[i-1][j-1] + dp[i-1][j]




for i in range(int(sys.stdin.readline())):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] )

