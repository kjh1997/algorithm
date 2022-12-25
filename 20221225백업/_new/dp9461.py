n=int(input())

dp = [0 for i in range(101)]
dp[1],dp[2],dp[3],dp[4],dp[5],dp[6],dp[7],dp[8],dp[9]=\
    1,1,1,2,2,3,4,5,7
for i in range(10,101):
    dp[i]=dp[i-1]+dp[i-5]
for i in range(n):
    print(dp[int(input())])


