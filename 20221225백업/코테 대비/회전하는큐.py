from collections import deque
import sys
input = sys.stdin.readline
N,M= map(int,input().split())
arr = list(map(int,input().split()))
d = deque([i for i in range(1, N + 1)])
c = 0
for i in arr:
    while True:
        if d[0] == i:
            d.popleft()
            break
        else:
            if d.index(i) < len(d)/2:
                while d[0] != i:
                    d.append(d.popleft())
                    c+=1
            else:
                while d[0] != i:
                    d.appendleft(d.pop())
                    c+=1
print(c)