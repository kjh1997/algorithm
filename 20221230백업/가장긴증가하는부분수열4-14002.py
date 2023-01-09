import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
d = list(map(int,input().split()))
r = []
r.append(d[0])
t= [(0,d[0])]
for n in d[1:]:
    if n > r[-1]:
        r.append(n)
        t.append((len(r)-1,n))
    else:
        i =  bisect_left(r,n)
        t.append((i,n))
        r[i]=n
ans = []
last = len(r)-1
for i in range(N-1,-1,-1):
    if t[i][0] == last:
        ans.append(t[i][1])
        last-=1
print(*ans[::-1])