import sys
n,m=map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
data.insert(0,0)
dp = [0]*(len(data)+1)
dp[1] = data[0]

for i in range(1,len(data)):
    dp[i] = dp[i-1] + data[i]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(dp[b]-dp[a-1])