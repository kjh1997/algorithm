import sys
import heapq
input = sys.stdin.readline

n = int(input())
data= [n+2] + list(map(int,input().split()))+[n+2]
ans =0
while n >= 2:
    idx = data.index(n)
    ans += min(abs(data[idx] - data[idx-1]), abs(data[idx]- data[idx+1]))
    data.pop(idx)
    n -=1
print(ans)
