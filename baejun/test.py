# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# answer = 0

# dp = [[0] * n for _ in range(n)] 
# dp[0][0] = 1

# for i in range(n):
#     for j in range(n):
#         if i == n - 1 and j == n - 1:
#             print(dp[i][j])
#             break
#         cur = board[i][j]
#         if j + cur < n:
#             dp[i][j + cur] += dp[i][j]
#         if i + cur < n:
#             dp[i + cur][j] += dp[i][j]
a = [[0]*4 for i in range(4)]
print(a)
a[0][0]=1
print(a)
