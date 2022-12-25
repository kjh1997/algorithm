import sys
read=sys.stdin.readline

n=int(read())
if n ==1:
    print(2)
    sys.exit()
elif n == 2:
    print(7)
    sys.exit()

dp = list(0 for _ in range(n+1))
dp[0]=1
dp[1]=2
dp[2]=7

for i in range(3,n+1):
    dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3])%1000000007
print(dp[n])

leng = int(input())

memo = [0]*(leng+1)
memo[0:3] = [1, 2, 7]

summemo = 0
for i in range(3, leng+1):
    summemo += memo[i-3]
    memo[i] = (2*memo[i-1] + 3*memo[i-2] + 2*summemo)%1000000007

print(memo[leng]) 
#동적프로그래밍 메모이제이션