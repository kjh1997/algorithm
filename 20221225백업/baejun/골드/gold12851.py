from collections import deque
import sys
input = sys.stdin.readline
a,b= map(int,input().split())
v=[False for _ in range(100001)]
CNT =int(1e7)
def bfs(start):
    r,cnt = 0,CNT
    q = deque()
    q.append((start,0))
    while q:
        c,cn = q.popleft()
        v[c]=True
        if c==b: 
            if cn < cnt: r=1;cnt = cn
            elif cn ==cnt:  r+=1
        if cn > cnt: 
            print(cnt)
            print(r)
            exit()
        if 0 <=c*2<=100000:
            if not v[c*2]: q.append((c*2,cn+1))

        if 0 <=c-1<=100000 :
            if not v[c-1]: q.append((c-1,cn+1))

        if 0 <=c+1<=100000:
            if not v[c+1]: q.append((c+1,cn+1))
    return cnt, r


a,b= bfs(a)
print(a)
print(b)