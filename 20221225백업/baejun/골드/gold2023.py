import math
from collections import deque
n = int(input())
head = ["2","3","5","7"]
tail = ["1","3","7","9"]
def prime_cal(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False
    return True    
def pass_def(a):
    return a
def bfs():
    q = deque()
    for h in head:
        q.append((h,1))
        while q:
            d,cnt = map(pass_def,q.popleft())
            for i in tail:
                if prime_cal(int(d+i)):
                    if cnt==n-1: print(d+i)
                    elif cnt < n: q.append((d+i,cnt+1))
if n !=1 :bfs()
else : 
    for i in head:    print(i)