import sys
input = sys.stdin.readline
N = int(input())
arr = []
arr = list(map(int, input().split()))
dp = [ [0]*(N+2) for _ in range(2) ]
dp[0][0] = arr[0]      
dp[1][0] = 0          
answer = arr[0]
for i in range(1, N):
    dp[0][i] = max(dp[0][i-1]+arr[i], arr[i])          
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+arr[i])     
    answer = max({dp[0][i],dp[1][i],answer})
print(answer)


# n = int(input())
# arr = list(map(int,input().split()))

# if max(arr) <=0: print(max(arr))
# else:
#     min = min(arr)
#     if min <= 0: 
#         arr.pop(arr.index(min))
#         temp = sum(arr)
#         for i in range(n-1):
#             temp = max(temp, sum(arr[:i]),sum(arr[i:]))
#     else:
#         temp = sum(arr)
#         for i in range(n-1):
#             temp = max(temp, sum(arr[:i]),sum(arr[i:]))  
#     print(temp)
