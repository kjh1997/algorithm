import sys

input = sys.stdin.readline
n,k= map(int,input().split())
coin = [ int(input().strip()) for _ in range(n) ]
dp=[0 for i in range(k+1)]
dp[0]=1
for i in coin:
    for j in range(k+1):
        if j-i >= 0:
            dp[j]+= dp[j-i]

print(dp[k])
