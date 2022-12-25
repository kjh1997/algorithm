# n=int(input())
# dp=[0 for i in range(46)]
# dp[0]=0
# dp[1]=1
# dp[2]=1
# dp[3]=2
# def dpAction(n):
#     if dp[n]==0: 
#         dp[n]=dpAction(n-2) + dpAction(n-1)
#         return dp[n]
#     else:
#         return dp[n]
# print(dpAction(n))

dp = [0,1,1,2]
a = int(input())
for i in range(4,a):
    dp.append(dp[i-1]+dp[i-2])
print(dp)

