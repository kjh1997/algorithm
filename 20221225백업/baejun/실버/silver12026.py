import math
n = int(input())
boj = input()
dp =[math.inf for i in range(n)]
dp[0]=0
for j in range(n-1):
    for i in range(j+1, n):
        if boj[j] =="B" and boj[i]=="O":
            dp[i] = min(dp[i],dp[j]+ (i-j)**2)
        if boj[j] =="O" and boj[i]=="J":
            dp[i] = min(dp[i],dp[j]+ (i-j)**2)
        if boj[j] =="J" and boj[i]=="B":
            dp[i] = min(dp[i],dp[j]+ (i-j)**2)

if dp[n-1] == math.inf : print(-1)
else: print(dp[n-1])
    
