from itertools import combinations
cnt = 0
n, objective = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(1,n+1):
    data = list(combinations(arr,i))
    for d in data:
        if sum(d) == objective: cnt+=1
print(cnt)

