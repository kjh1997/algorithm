import sys
sys.setrecursionlimit(10**7)
r = int(input())
board=[]
for i in range(r):
    board.append(list(map(int, input().split())))
dp = [[0]*r for i in range(r)]
def dp_action(x,y,n):
    if x+n ==r-1 and y+n == r-1: return
    if x+n <r:
        dp[x+n][y] = dp[x+n][y] + 1
        dp_action(x+n,y,board[x+n][y])
    if y+n < r:
        dp[x][y+n] = dp[x][y+n] + 1
        dp_action(x,y+n,board[x][y+n])
dp_action(0,0,board[0][0])
print(dp[r-1][r-1])


