n = int(input())
arr = []
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort()
dp=[1]*n
for i in range(n):
    cnt=1
    for j in range(i):
        if arr[j][1] <arr[i][1] and dp[i] < dp[j] +1:
            dp[i]= dp[j]+1
print(n-max(dp))

# N = int(input())

# lineList = []

# for _ in range(N):
#     lineList.append(list(map(int, input().split())))

# lineList.sort()

# dp = [1]*N
# for i in range(N):
#     for j in range(i):
#         if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
#             dp[i] = dp[j] + 1

# print(N-max(dp))
