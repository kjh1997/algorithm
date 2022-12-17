import sys
n,k = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
cur = sum(data[:k])
result= cur
for i in range(k,len(data)):
    cur = cur - data[i-k] + data[i]
    result = max(result,cur)

print(result)