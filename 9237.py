import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data.sort(reverse=True)
result = []
for i in range(0,n):
    result.append(data[i] + 2 + i)

print(max(result))




