import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
d = list(map(int,input().split()))
r = []
r.append(d[0])
for n in d[1:]:
    if n > r[-1]:
        r.append(n)
    else:
        i =  bisect_left(r,n)
        r[i]=n
print(len(r))