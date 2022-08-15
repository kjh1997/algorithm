n, k = map(int, input().split())
data = list()
for _ in range(n):
    data.append(tuple(map(int, input().split())))
dp = [0] * (k+1)
for i in range(n):
    for j in range(k, data[i][0]-1, -1):
        dp[j] = max(dp[j], dp[j-data[i][0]] + data[i][1])
print(dp[k])