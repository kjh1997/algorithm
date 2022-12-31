import sys
input = sys.stdin.readline
N = int(input())
data = [int(input()) for i in range(N)]
ans = 0
for i in range(len(data)-1,0,-1):
    if data[i]<= data[i-1]:
        cur = data[i-1]-data[i] +1
        ans +=  cur
        data[i-1] -= cur
print(ans)