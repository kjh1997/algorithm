import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    a,b=map(int,input().split())
    visit = [False] * 200
    q = deque()
    q.append((a,b,0))
    while q:
        a,b,c = q.popleft()
        if a == b: print(c);break
        
        if a <= b and visit[a] == False:
            q.append((a*2,b+3,c+1))
            q.append((a+1,b,c+1))