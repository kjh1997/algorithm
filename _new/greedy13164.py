n,k = map(int,input().split())

arr = list(map(int,input().split()))
dist = []
for i in range(1,len(arr)):
    dist.append(arr[i]-arr[i-1])
dist.sort()
re=0
for i in range(n-k):
    re+=dist[i]
print(re)

