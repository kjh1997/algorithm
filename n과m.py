import sys,re
from itertools import permutations
n,m = map(int,sys.stdin.readline().split())

if m == 1: 
    for i in range(1,n+1): print(i)
else:
    d = [i for i in range(1,n+1)]
    result = permutations(d,m)
    for i in result: 
        print(*i)

