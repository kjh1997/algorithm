import sys

n,m = map(int,sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.extend(list(map(int,sys.stdin.readline().split())))
dp = [0 for i in range(len(arr)+1)]
dp[0]=arr[0]

for i in range(1,len(arr)):
    dp[i]= arr[i]+ dp[i-1]
# print(dp)
for i in range(m):

    x1,y1, x2,y2 = map(int,sys.stdin.readline().split())
    s = (x1-1)*n +y1
    e = (x2-1)*n +y2
    if s==e : print(arr[s-1]); continue
    if s==1: print(dp[e-1]); continue
    print(dp[e-1]-dp[s-1])



