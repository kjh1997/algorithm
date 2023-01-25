# import sys
# input = sys.stdin.readline

# n,m  = map(int,input().split())
# data = list(map(int,input().split()))
# arr = [0]*(n+1)
# for i in range(m):
#     a,b,c = map(int,input().split())
#     for i in range(a-1,b):
#         data[i]+=c
# print(*data)
    
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))
tmp = [0] * (N+1)
for _ in range(M):
    a, b, k = map(int, input().split())
    tmp[a-1] += k
    tmp[b] -= k

dp = [0] * (N+1)
dp[0] = tmp[0]
for i in range(1,N+1):
    dp[i] = dp[i-1] + tmp[i]
for i in range(N):
    print(H[i] + dp[i], end=' ')




