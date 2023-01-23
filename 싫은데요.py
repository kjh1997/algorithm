import sys

input = sys.stdin.readline
n,m= map(int,input().split())
data = list(map(int,input().split()))
arr = [data[0]]+[0]*m
for i in range(1,n):
    arr[i]= arr[i-1]+data[i]
s=0
e=1
ans =0
arr = [0]+arr
data = [0]+data
while True:
    if e > n: break
    if data[e] >m:
        e = e+1; s = e
    ans = max(ans, arr[e]-arr[s-1] )
    if e-s <=n:
        e+=1
    else:
        s+=1
        e+=1
print(ans)





