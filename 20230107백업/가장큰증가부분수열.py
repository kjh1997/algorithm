n = int(input())
arr = [int(x) for x in input().split()]
dp = arr.copy()
answer = dp[0]
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
    if answer < dp[i]:
        answer = dp[i]

print(answer)