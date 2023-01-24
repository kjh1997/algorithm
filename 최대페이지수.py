# import sys
# input = sys.stdin.readline
# n,m=map(int,input().split())
# data = []
# weight={}
# for i in range(m):
#     a,b = map(int,input().split())
#     data.append([[a,b],b/a])
# data.sort(key=lambda x:(x[1], x[0][1]), reverse=True)
# ans = 0
# print(data)
# for i in range(m):
#     tmp = 0
#     for j in range(i,m):
#         if n - data[j][0][0] >=0: 
#             n -= data[j][0][0]
#             tmp += data[j][0][1] 
    
#     ans = max(tmp,ans)
# print(ans)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    d, p = map(int,input().split())

    for j in range(1, n + 1):
        if j - d >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - d] + p)

        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])