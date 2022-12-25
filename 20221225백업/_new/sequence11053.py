N = int(input())
dp = [0] * (N+1)

data = list(map(int, input().split()))
data.insert(0,0)
for i in range(1, N+1):
    for j in range(i):
        if data [i] > data [j]:
            dp[i] = max(dp[j]+1, dp[i])
            print(dp)

            
print(max(dp))
