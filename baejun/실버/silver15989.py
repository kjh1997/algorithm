n = int(input())
dp = [1 for i in range(10001)]
for i in range(2,10001):
    dp[i] = dp[i-2]+dp[i]
for i in range(3,10001):
    dp[i] = dp[i-3] + dp[i]
for i in range(n):
    num = int(input())
    print(dp[num])




