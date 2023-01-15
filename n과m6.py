import sys
input = sys.stdin.readline
n,m=map(int,input().split())
data= list(map(int,input().split()))
data.sort()
def cal(arr, idx):
    if len(arr) == m: print(*arr); return
    for i in range(idx+1,n):
        cal(arr+[data[i]],i)
for i in range(len(data)-m+1):
    cal([data[i]], i)